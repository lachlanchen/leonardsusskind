#!/usr/bin/env python3
"""Derive multilingual reading links from verified outputs, never planned editions."""
import argparse
import html
import json
from pathlib import Path
import re
from urllib.parse import urlencode

import polished_translation as pipeline
from publish_generated_course_pdf import CANONICAL_FILENAMES

ROOT = Path(__file__).resolve().parents[1]
READER = pipeline.PDF_READER

CITATION_LABELS = {
    'en': ('Citation and Support', 'Cite these independent companion notes, not the original lectures:'),
    'ja': ('引用と支援', '以下は独立した補助講義ノートの引用情報です。元の講義は別途引用してください。'),
    'zh-Hans': ('引用与支持', '以下引用信息适用于独立编写的配套讲义，原始讲座请另行引用。'),
    'zh-Hant': ('引用與支持', '以下引用資訊適用於獨立編寫的配套講義，原始講座請另行引用。'),
    'ar': ('الاستشهاد والدعم', 'هذه بيانات الاستشهاد بالملاحظات المستقلة؛ يُرجى الاستشهاد بالمحاضرات الأصلية بصورة منفصلة.'),
    'de': ('Zitation und Unterstützung', 'Diese Angabe zitiert die unabhängigen Begleitnotizen; die Originalvorlesungen bitte gesondert zitieren.'),
    'es': ('Cita y apoyo', 'Esta referencia corresponde a los apuntes independientes; cita las conferencias originales por separado.'),
    'fr': ('Citation et soutien', 'Cette référence concerne les notes indépendantes ; citez les conférences originales séparément.'),
    'ko': ('인용 및 후원', '독립적으로 편집한 보조 강의 노트의 인용 정보입니다. 원래 강의는 별도로 인용해 주세요.'),
    'ru': ('Цитирование и поддержка', 'Эта ссылка относится к независимым сопроводительным заметкам; исходные лекции цитируйте отдельно.'),
    'vi': ('Trích dẫn và hỗ trợ', 'Thông tin này dành cho ghi chú đồng hành độc lập; vui lòng trích dẫn riêng các bài giảng gốc.'),
}


def citation_block(locale):
    heading, explanation = CITATION_LABELS[locale]
    prefix = '' if locale == 'en' else '../'
    return ('<!-- reading-citation:start -->\n## ' + heading + '\n\n' + explanation
            + '\n\n[CITATION.cff](' + prefix + 'CITATION.cff) · '
            '[GitHub Sponsors](https://github.com/sponsors/lachlanchen)\n\n'
            '```bibtex\n@software{lazyingart_susskind_companion_notes,\n'
            '  author = {{LazyingArt contributors}},\n'
            '  title = {Leonard Susskind Lecture Notes: Independent Multilingual Companion Editions},\n'
            '  url = {https://github.com/lachlanchen/leonardsusskind}\n}\n```\n'
            '<!-- reading-citation:end -->\n')

NOTICES = {
    'en': ('Books by Language',
         '16 books from the *Theoretical Minimum* and related lectures. [Choose a PDF by book and language]({table}), or [open the online PDF reader]({reader}).',
         'Read in Bunko', 'Read on your phone or tablet. The languages you can select depend on the book.'),
    'ja': ('言語別の書籍',
         '『Theoretical Minimum』と関連講義の全16冊。[書名と言語からPDFを選ぶ]({table})、または[ブラウザーで読む]({reader})。',
         'Bunkoで読む', 'スマートフォンやタブレットで読めます。選べる言語は書籍によって異なります。'),
    'zh-Hans': ('按语言阅读',
         '《Theoretical Minimum》及相关讲座共 16 册。[按书名和语言选择 PDF]({table})，或[在线阅读]({reader})。',
         '在 Bunko 中阅读', '可在手机或平板上阅读。可选语言因书而异。'),
    'zh-Hant': ('依語言閱讀',
         '《Theoretical Minimum》及相關講座共 16 冊。[依書名與語言選擇 PDF]({table})，或[線上閱讀]({reader})。',
         '在 Bunko 閱讀', '可在手機或平板上閱讀。各書提供的語言不同。'),
    'de': ('Bücher nach Sprache',
         '16 Bücher zu *Theoretical Minimum* und verwandten Vorlesungen. [PDF nach Buch und Sprache wählen]({table}) oder [im Browser lesen]({reader}).',
         'In Bunko lesen', 'Auf dem Smartphone oder Tablet lesen. Die Sprachauswahl hängt vom Buch ab.'),
    'es': ('Libros por idioma',
         '16 libros de *Theoretical Minimum* y cursos relacionados. [Elige un PDF por libro e idioma]({table}) o [lee en el navegador]({reader}).',
         'Lee en Bunko', 'Lee en el móvil o la tableta. Los idiomas disponibles dependen de cada libro.'),
    'fr': ('Livres par langue',
         '16 livres issus de *Theoretical Minimum* et de cours connexes. [Choisir un PDF par livre et par langue]({table}) ou [lire dans le navigateur]({reader}).',
         'Lire dans Bunko', 'Lisez sur téléphone ou tablette. Les langues proposées varient selon le livre.'),
    'ko': ('언어별 도서',
         '*Theoretical Minimum*과 관련 강의 16권. [책과 언어별로 PDF 선택]({table}) 또는 [브라우저에서 읽기]({reader}).',
         'Bunko에서 읽기', '휴대전화나 태블릿에서 읽을 수 있습니다. 선택할 수 있는 언어는 책마다 다릅니다.'),
    'ru': ('Книги по языкам',
         '16 книг по курсу *Theoretical Minimum* и смежным лекциям. [Выбрать PDF по книге и языку]({table}) или [открыть в браузере]({reader}).',
         'Читайте в Bunko', 'Читайте на телефоне или планшете. Набор языков зависит от книги.'),
    'vi': ('Sách theo ngôn ngữ',
         '16 cuốn từ *Theoretical Minimum* và các bài giảng liên quan. [Chọn PDF theo sách và ngôn ngữ]({table}) hoặc [đọc trên trình duyệt]({reader}).',
         'Đọc trong Bunko', 'Đọc trên điện thoại hoặc máy tính bảng. Mỗi cuốn hỗ trợ các ngôn ngữ khác nhau.'),
    'ar': ('الكتب حسب اللغة',
         '16 كتاباً من سلسلة *Theoretical Minimum* ومحاضرات ذات صلة. [اختر ملف PDF بحسب الكتاب واللغة]({table}) أو [اقرأ في المتصفح]({reader}).',
         'اقرأ في Bunko', 'اقرأ على الهاتف أو الجهاز اللوحي. تختلف اللغات المتاحة باختلاف الكتاب.'),
}

BUNKO = "https://lachlan.lazying.art/Bunko/"
APP_STORE = "https://apps.apple.com/app/id6815137919"
PLAY_STORE = "https://play.google.com/store/apps/details?id=art.lazying.bunko"


EDITION_LABELS = {'en': 'English', **{
    lang: spec['label'] for lang, spec in pipeline.LANGUAGE_SPECS.items()}}


def catalog():
    return pipeline.reading_catalog(pipeline.read(pipeline.MANIFEST)['books'], pipeline.status())


def language_notice(locale):
    heading, description, app_heading, app_description = NOTICES[locale]
    prefix = '' if locale == 'en' else '../'
    table = ('' if locale == 'en' else '../README.md') + '#final-polished-translations'
    assets = prefix + 'figs/bunko/'
    return (
        f'<!-- reading-languages:start -->\n## {heading}\n\n'
        + description.format(table=table, reader=READER) + '\n\n'
        + ' · '.join(EDITION_LABELS[lang] for lang in ('en', *pipeline.LANGS)) + '\n\n'
        + f'## {app_heading}\n\n'
        + f'<a href="{BUNKO}"><img src="{assets}icon.png" alt="Bunko" width="72"></a>\n\n'
        + app_description + '\n\n'
        + f'**[App Store]({APP_STORE})** · **[Google Play]({PLAY_STORE})** · [Bunko Web]({BUNKO})\n\n'
        + '<p>\n'
        + f'<a href="{APP_STORE}"><img src="{assets}library-ios.png" alt="Bunko library on iPhone" width="180"></a>\n'
        + f'<a href="{PLAY_STORE}"><img src="{assets}reader-android.png" alt="Bunko multilingual reader on Android" width="180"></a>\n'
        + '</p>\n<!-- reading-languages:end -->')


def decorate_readmes():
    data = catalog()
    pipeline.write(ROOT / 'references/reading_editions.json', data)
    for path in [ROOT / 'README.md', *sorted((ROOT / 'i18n').glob('README.*.md'))]:
        locale = 'en' if path.parent == ROOT else path.name[7:-3]
        block = language_notice(locale)
        text = path.read_text()
        text = '\n'.join(
            '[Bunko](https://lachlan.lazying.art/Bunko/)'
            if 'https://apps.apple.com/us/app/bunko-classics-with-ruby/' in line
            and 'https://lachlan.lazying.art/Bunko/' in line else line
            for line in text.split('\n'))
        text = re.sub(r'\n*<!-- reading-languages:start -->.*?<!-- reading-languages:end -->\n*', '\n\n', text, flags=re.S)
        text = re.sub(r'(^# [^\n]+\n)', lambda m: m[0] + '\n' + block + '\n', text, count=1, flags=re.M)
        def annotate(match):
            cell = re.sub(r'\s*<!-- edition-links -->.*?<!-- /edition-links -->', '', match[0], flags=re.S)
            link = re.search(r'leonardsusskind-reader\.html\?book=([^"&]+)', cell)
            if not link or link[1] not in data['books']:
                return cell
            row = data['books'][link[1]]
            links = ['<a href="' + READER + '?' + html.escape(urlencode({'book': link[1], 'lang': lang})) + '">' + EDITION_LABELS[lang] + '</a>'
                     for lang in ('en', *pipeline.LANGS) if lang in row['editions']]
            annotation = '\n      <!-- edition-links --><br><sub>' + ' · '.join(links) + '</sub><!-- /edition-links -->\n    '
            # A blank line ends the GFM HTML block; indented rows then become code.
            return re.sub(r'\s*</td>$', lambda _: annotation + '</td>', cell)
        text = re.sub(r'<td align="center">.*?</td>', annotate, text, flags=re.S)
        # Older README translations have no cover catalog. Add one shared, compact
        # catalog rather than leaving their language announcement disconnected.
        text = re.sub(r'\n*<!-- language-covers:start -->.*?<!-- language-covers:end -->\n*', '\n\n', text, flags=re.S)
        if 'readme-covers/' not in text:
            rows = ['<!-- language-covers:start -->', '<table>']
            for slug, row in data['books'].items():
                stem = CANONICAL_FILENAMES[row['id'].replace('--', '/')][:-4]
                images = [ROOT / 'figs/readme-covers' / (stem + suffix + '.png') for suffix in ('', '_first_page')]
                cover = next(p for p in images if p.exists())
                title_locale = 'zh' if locale == 'zh-Hans' else locale
                title = html.escape(row['titles'].get(title_locale, row['titles']['en']))
                links = ['<a href="' + READER + '?' + html.escape(urlencode({'book': slug, 'lang': lang})) + '">' + EDITION_LABELS[lang] + '</a>'
                         for lang in ('en', *pipeline.LANGS) if lang in row['editions']]
                rows.append('<tr><td><img width="85" src="../' + str(cover.relative_to(ROOT)) + '" alt="' + title + '"></td><td><strong>' + title + '</strong><br>' + ' · '.join(links) + '</td></tr>')
            rows += ['</table>', '<!-- language-covers:end -->']
            text = text.replace('<!-- reading-languages:end -->', '<!-- reading-languages:end -->\n\n' + '\n'.join(rows), 1)
        text = re.sub(r'\n*<!-- reading-citation:start -->.*?<!-- reading-citation:end -->\n*', '\n\n', text, flags=re.S)
        text = text.rstrip() + '\n\n' + citation_block(locale)
        pipeline.textwrite(path, re.sub(r'^[ \t]+$', '', text, flags=re.M))
    return data


def sync_reader(data, path):
    text = path.read_text()
    block = '<!-- reading-editions:start -->\n<script id="reading-editions" type="application/json">' + json.dumps(data, ensure_ascii=False).replace('<', '\\u003c') + '</script>\n<!-- reading-editions:end -->'
    if '<!-- reading-editions:start -->' in text:
        text = re.sub(r'<!-- reading-editions:start -->.*?<!-- reading-editions:end -->', lambda m: block, text, flags=re.S)
    else:
        text = text.replace('    <script>\n', block + '\n    <script>\n', 1)
    pipeline.textwrite(path, text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reader', type=Path)
    args = parser.parse_args()
    data = decorate_readmes()
    if args.reader:
        sync_reader(data, args.reader)
