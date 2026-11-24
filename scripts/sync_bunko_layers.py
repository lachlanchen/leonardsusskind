#!/usr/bin/env python3
"""Add published Susskind translations to existing Bunko content bundles."""
import argparse
from collections import defaultdict
from copy import deepcopy
from datetime import date
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from tempfile import TemporaryDirectory
import unicodedata

from pylatexenc.latex2text import LatexNodes2Text

import polished_translation as p

BUNKO = p.ROOT.parent / 'Bunko'
DEFAULT_BOOKS = p.ROOT.parent / 'bunko-books'
BASE = ('en', 'ja', 'zh')
LABELS = ('Overview', 'Question from the audience', 'Response', 'Question for the class',
          'Lecture timestamp', 'Lecture frame', 'Editorial clarification')


def require(ok, reason):
    if not ok:
        raise ValueError(reason)


def encode(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':')).encode()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def git(root, *args):
    return subprocess.check_output(['git', '-C', str(root), *args], text=True)


def groups(blocks):
    grouped = defaultdict(list)
    for block in blocks:
        grouped[block.get('_sourceSegment')].append(block)
    return grouped


def topology(block, math_inventory):
    return block['kind'], math_inventory(block), block.get('figure', {}).get('path'), len(block['u'])


def join_prose(blocks):
    require(all(b['kind'] in {'text', 'equation'} and len(b['u']) == 1 for b in blocks),
            'Cannot coalesce structural blocks')
    a = deepcopy(blocks[0])
    for b in blocks[1:]:
        unit, other = a['u'][0], b['u'][0]
        rich = unit.get('rich', {}).get('en', [{'text': unit['src']}])
        tail = other.get('rich', {}).get('en', [{'text': other['src']}])
        a['src'] += ' ' + b['src']
        a['kind'] = 'text'
        unit.update(src=a['src'], en=[a['src']], rich={'en': rich + [{'text': ' '}] + tail})
    return a


def baseline_groups(raw, legacy):
    aligned = deepcopy(raw)
    entries = [groups(aligned[lang]) for lang in BASE]
    require(all(list(layer) == list(entries[0]) for layer in entries), 'Base source segment mismatch')
    return {key: legacy.reconcile_source_groups({lang: entries[n][key] for n, lang in enumerate(BASE)})['en']
            for key in entries[0]}


def fit_layer(aligned, blocks, math_inventory):
    candidate = groups(blocks)
    require(list(candidate) == list(aligned), 'Source segment coverage changed')
    flat = []
    for key, source in aligned.items():
        target = list(candidate[key])
        expected = [topology(x, math_inventory) for x in source]
        if len(target) == len(source) + 1:
            for index, original in enumerate(source):
                figure, caption = target[index:index+2]
                if (original['kind'] == figure['kind'] == 'figure' and figure['src'] == 'Figure'
                        and figure['u'][0]['en'] == [''] and caption['kind'] == 'text'):
                    # This is a split caption, not a change to the source's
                    # frame timestamp or any separate paragraph.
                    merged = {**figure, 'src': caption['src'], 'u': caption['u']}
                    proposal = target[:index] + [merged] + target[index+2:]
                    if [topology(x, math_inventory) for x in proposal] == expected:
                        target = proposal
                        break
        if [topology(x, math_inventory) for x in target] != expected and len(source) == 1 and len(target) > 1:
            target = [join_prose(target)]
        # Pandoc may split adjacent inline prose after translated punctuation.
        require([topology(x, math_inventory) for x in target] == expected, f'{key}: block/figure/math mismatch')
        flat.extend(target)
    return flat


def labels_for(lang):
    sample = '\n'.join(f'@@BUNKOLABEL{i}@@{label}' + ('.' if i < 4 else ':')
                       for i, label in enumerate(LABELS))
    localized = p.translated_preamble(sample, lang)
    return {label + ':': re.search(f'@@BUNKOLABEL{i}@@([^\n]+)', localized)[1]
            for i, label in enumerate(LABELS)}


def localize_labels(blocks, lang):
    labels = labels_for(lang)
    def translate(text):
        return re.sub('|'.join(map(re.escape, labels)), lambda m: labels[m[0]], text)
    for block in blocks:
        block['src'] = translate(block['src'])
        for unit in block['u']:
            unit['src'] = translate(unit['src'])
            unit['en'] = [translate(token) for token in unit['en']]
            for span in unit.get('rich', {}).get('en', []):
                if 'text' in span:
                    span['text'] = translate(span['text'])


def format_only(row):
    return (row['kind'] == 'text' and not row.get('figure')
            and all(c.isspace() or unicodedata.category(c) == 'Cf' for c in row['src']))


def extract(book, rel, lang, legacy):
    original = p.ROOT / 'generated_course_notes' / book['course']
    source = (original / rel).read_text()
    prepared = p.read(p.WORK / 'prepared' / book['id'] / (rel + '.json'))
    require(prepared['source_sha256'] == p.digest(source), 'Stale prepared source')
    if lang == 'en':
        accepted = {}
    elif lang in BASE:
        # Existing layers are immutable alignment evidence. Their original
        # accepted caches were checked against the published quality record.
        cached = p.read(p.result_path(book, lang, rel))
        require(cached['source_sha256'] == prepared['source_sha256'], 'Stale base reader cache')
        accepted = cached['accepted']
    else:
        accepted = p.load_results(book, lang, rel, prepared)['accepted']
    front = rel == 'course.tex'
    parts = []
    for i, part in enumerate(prepared['parts']):
        if p.needs_translation(part):
            parts.extend((f'BUNKOUNIT{i:06d}TOKEN\n',
                          part if lang == 'en' else (accepted[str(i)] if front else re.sub(r'\n\s*\n', '\n', accepted[str(i)]))))
        elif not front:
            parts.append(part)
    text = p.restore(('\n\n' if front else '').join(parts), prepared['protected'])
    if front:
        nodes, _, _ = p.lw.LatexWalker(text).get_latex_nodes()
        end = next((n.pos for n in nodes if isinstance(n, p.lw.LatexMacroNode)
                    and n.macroname in {'tableofcontents', 'mainmatter'}), len(text))
        text = text[:end]
    else:
        text = p.restore_layout_arguments(source, text)
    with TemporaryDirectory(prefix='bunko-layer-') as tmp:
        path = Path(tmp)/'edition.tex'
        path.write_text(text)
        blocks, _ = legacy.owner.tex_blocks(path, None if front else original/'figures', origin=original/rel,
                                           strict=True, language=lang if lang in BASE else 'en')
    if lang not in BASE:
        blocks = [row for row in blocks if not format_only(row)]
        localize_labels(blocks, lang)
    want = {f'BUNKOUNIT{i:06d}TOKEN' for i, part in enumerate(prepared['parts']) if p.needs_translation(part)}
    require(want == set(groups(blocks)) - {None}, f'{rel}/{lang}: source segment coverage mismatch')
    return blocks


def add_layers(previous, baseline, additions, math_inventory):
    require(len(previous) == len(baseline), 'Published block count differs from source')
    for old, expected in zip(previous, baseline):
        require(old['src'] == expected['src'] and topology(old, math_inventory) == topology(expected, math_inventory),
                f'Published passage differs from source: {old["id"]}')
    merged = deepcopy(previous)
    for lang, blocks in additions.items():
        require(len(blocks) == len(merged), f'{lang}: wrong layer length')
        for block, target in zip(merged, blocks):
            for unit, new in zip(block['u'], target['u']):
                unit[lang] = new['en']
                if new.get('rich'):
                    unit.setdefault('rich', {})[lang] = new['rich']['en']
            if 'figure' in block:
                block['figure']['caption'][lang] = target['figure']['caption']['en']
    return merged


def published_pdf(book, lang, published, object_format):
    rel = f'translations/{book["id"]}/{lang}'
    quality = p.ROOT / rel / 'quality.json'
    if f'{rel}/book.pdf' not in published or not quality.is_file():
        return False
    data = quality.read_bytes()
    oid = hashlib.new(object_format, f'blob {len(data)}\0'.encode() + data).hexdigest()
    return oid == published.get(f'{rel}/quality.json') and p.validated_output(book, lang)


def build_book(book, directory, published, object_format, source_commit, legacy):
    meta = p.read(directory/'meta.json')
    rights = p.read(directory/'rights.json')
    require(rights['status'] == 'ship' and rights.get('license') == 'GPL-3.0-only'
            and meta['langs'] == rights['langs'], 'No matching published rights record')
    languages = [lang for lang in p.LANGS if lang not in meta['langs']
                 and published_pdf(book, lang, published, object_format)]
    if not languages:
        return {}, {'book': directory.name, 'added': [], 'skipped': {}}
    require(all(published_pdf(book, lang, published, object_format) for lang in ('ja', 'zh')),
            'Existing translation bases no longer match their published quality records')
    p.verify_sources(book)
    skipped, chapters, math_rows = {}, [], []
    intro = baseline_groups({lang: extract(book, 'course.tex', lang, legacy) for lang in BASE}, legacy)
    extra_intro = {}
    for lang in languages:
        try:
            extra_intro[lang] = fit_layer(intro, extract(book, 'course.tex', lang, legacy), legacy.math_inventory)
        except (OSError, ValueError, KeyError, RuntimeError, subprocess.SubprocessError) as exc:
            skipped[lang] = str(exc)
    rels = [rel for rel in book['source_files'] if rel.endswith('content.tex')]
    require(len(rels) == len(meta['chapters']), 'Published chapter count differs from source')
    for number, (rel, row) in enumerate(zip(rels, meta['chapters']), 1):
        require(row['n'] == number, 'Published chapter numbering differs')
        raw = {lang: extract(book, rel, lang, legacy) for lang in BASE}
        baseline = baseline_groups(raw, legacy)
        old = p.read(directory/row['file'])
        flat = [b for group in baseline.values() for b in group]
        if number == 1:
            flat = [b for group in intro.values() for b in group] + flat
        target, titles = {}, {}
        for lang in (l for l in languages if l not in skipped):
            try:
                layer = fit_layer(baseline, extract(book, rel, lang, legacy), legacy.math_inventory)
                titles[lang] = LatexNodes2Text().latex_to_text(next(b['src'] for b in layer if b['kind']=='heading'))
                target[lang] = (extra_intro[lang] if number == 1 else []) + layer
            except (OSError, ValueError, KeyError, RuntimeError, StopIteration, subprocess.SubprocessError) as exc:
                skipped[lang] = f'{rel}: {exc}'
        chapters.append((row, old, flat, target, titles))
    added = [lang for lang in languages if lang not in skipped]
    if not added:
        return {}, {'book': directory.name, 'added': [], 'skipped': skipped}
    outputs = {}
    sentence_path = directory/'sentences-v1.json'
    sentence_map = p.read(sentence_path) if sentence_path.is_file() else None
    for row, chapter, flat, target, titles in chapters:
        chapter['p'] = add_layers(chapter['p'], flat, {lang: target[lang] for lang in added}, legacy.math_inventory)
        for lang in added:
            chapter['title'][lang] = [titles[lang]]
            row['title'][lang] = titles[lang]
        for block in chapter['p']:
            for unit in block['u']:
                for lang in added:
                    for part in unit.get('rich', {}).get(lang, []):
                        if 'math' in part:
                            math_rows.append({**part, 'location': f'{row["n"]}/{block["id"]}/{lang}'})
        data = encode(chapter)
        hash_value = sha(data)
        name = f'c{row["n"]:04d}-{hash_value[:12]}.json'
        outputs[name] = data
        if sentence_map and row['file'] in sentence_map['chapters']:
            coordinates = sentence_map['chapters'].pop(row['file'])
            require(coordinates['chapterHash'] == row['sha256'], 'Stale original sentence-map chapter')
            sentence_map['chapters'][name] = {**coordinates, 'chapterHash': hash_value}
        row.update(file=name, sha256=hash_value, bytes=len(data))
    check = subprocess.run(['node', str(BUNKO/'tools/check_polished_math.mjs')], input=encode(math_rows),
                           capture_output=True, timeout=120)
    require(not check.returncode, 'KaTeX rejected a new layer: ' + check.stdout.decode()[:1000])
    meta['langs'].extend(added)
    rights['langs'] = meta['langs'][:]
    for lang in added:
        title = p.book_title(book, lang)
        meta['title'][lang] = [title]
        meta['titleText'][lang] = title
    meta['bytes'] = sum(row['bytes'] for row in meta['chapters'])
    rights['basis'] = rights['basis'].split(' Japanese and Simplified Chinese are complete')[0].split(' Additional aligned layers')[0]
    rights['basis'] += ' Additional aligned layers use published, AI-assisted translations of the same source. Equations and original figures are retained.'
    rights['checked'] = date.today().isoformat()
    outputs['meta.json'] = encode(meta)
    outputs['rights.json'] = json.dumps(rights, ensure_ascii=False, indent=2).encode() + b'\n'
    if sentence_map:
        outputs[sentence_path.name] = encode(sentence_map)
    report = {'book': directory.name, 'added': added, 'skipped': skipped, 'chapters': len(chapters),
              'retained_passages': meta['paras'], 'math_checked': len(math_rows)}
    audit_path = directory/'translation-audit.json'
    audit = p.read(audit_path) if audit_path.is_file() else {}
    audit['languages'] = meta['langs']
    audit['additionalLayers'] = {**audit.get('additionalLayers', {}),
        **{lang: sha((p.OUT/book['id']/lang/'quality.json').read_bytes()) for lang in added}}
    audit['layerSourceCommits'] = {**audit.get('layerSourceCommits', {}), **dict.fromkeys(added, source_commit)}
    outputs[audit_path.name] = json.dumps(audit, ensure_ascii=False, indent=2).encode() + b'\n'
    return outputs, report


def validate_staged_bundle(directory, outputs, book_row):
    with TemporaryDirectory(prefix='bunko-bundle-', dir=p.WORK) as tmp:
        staged = Path(tmp) / directory.name
        staged.mkdir()
        (staged/'assets').symlink_to(directory/'assets', target_is_directory=True)
        for name, data in outputs.items():
            (staged/name).write_bytes(data)
        cover = p.read(staged/'meta.json').get('cover')
        if cover:
            (staged/cover).write_bytes((directory/cover).read_bytes())
        require(book_row(staged) is not None, 'Updated bundle is not shippable')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--books-root', type=Path, default=DEFAULT_BOOKS)
    parser.add_argument('--book', help='Only export the specified Bunko book id')
    parser.add_argument('--source-commit', required=True, help='Verified, published Susskind commit')
    parser.add_argument('--report', type=Path)
    parser.add_argument('--apply', action='store_true', help='Write content bundles, not Git commits')
    args = parser.parse_args()
    root = args.books_root.resolve()
    sys.path.insert(0, str(BUNKO/'tools'))
    import import_polished_physics as legacy
    sys.path.insert(0, str(root/'tools'))
    from catalogue import book_row

    revision = git(p.ROOT, 'rev-parse', '--verify', args.source_commit + '^{commit}').strip()
    object_format = git(p.ROOT, 'rev-parse', '--show-object-format').strip()
    published = {}
    for line in git(p.ROOT, 'ls-tree', '-r', revision, 'translations').splitlines():
        info, path = line.split('\t', 1)
        published[path] = info.split()[-1]
    if args.apply:
        require(not git(root, 'status', '--porcelain'), 'Bunko content checkout must be clean')
        subprocess.run(['git', '-C', str(root), 'merge-base', '--is-ancestor', 'origin/main', 'HEAD'], check=True)
    reports = []
    for book in p.read(p.MANIFEST)['books']:
        suffix = '/generated_course_notes/' + book['course']
        directories = [path.parent for path in (root/'books').glob('physics-*/rights.json')
                       if any(ref.endswith(suffix) for ref in p.read(path)['references'])]
        require(len(directories)==1, f'Missing or ambiguous Bunko identity: {book["id"]}')
        directory = directories[0]
        if args.book and directory.name != args.book:
            continue
        try:
            outputs, report = build_book(book, directory, published, object_format, revision, legacy)
            if outputs:
                validate_staged_bundle(directory, outputs, book_row)
        except (ValueError, RuntimeError, OSError, KeyError, subprocess.SubprocessError) as exc:
            outputs = {}
            report = {'book': directory.name, 'error': str(exc)}
        if outputs and args.apply:
            for name, data in outputs.items():
                tmp = directory/(name + '.sync-tmp')
                tmp.write_bytes(data)
                tmp.replace(directory/name)
            book_row(directory)
        reports.append(report)
        print(json.dumps(report, ensure_ascii=False), flush=True)
    require(bool(reports), 'No matching book')
    if args.report:
        p.write(args.report, {'source_commit': revision, 'books': reports})
    if any('error' in report or report.get('skipped') for report in reports):
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
