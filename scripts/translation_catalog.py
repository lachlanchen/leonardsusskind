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
READER = 'https://learn.lazying.art/leonardsusskind-reader.html'
RAW = 'https://raw.githubusercontent.com/lachlanchen/leonardsusskind/main/'

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
 'en': ('Choose a book language',
        'All 16 books are available in English, Japanese, Simplified Chinese, French, Spanish and German. The [PDF table by book and language]({table}) also tracks Traditional Chinese, Korean, Vietnamese, Russian and Arabic. Choose **Available PDF** to read a published edition; **In preparation** means there is no download yet.',
        'New translated PDFs use 1.2 × A5 paper (177.6 × 252 mm), with 12 pt text, clear spacing, equations and original figures. The older “pocket 1.2x” files refer to enlarged type, not this paper size.',
        'Help with scientific proofreading, accessibility or layout by opening an issue or contributing a source-backed correction.'),
 'ja': ('多言語版を読む',
        '全16冊を英語、日本語、中国語（簡体字）、フランス語、スペイン語、ドイツ語で読めます。[書名・言語別のPDF一覧]({table})には、中国語（繁体字）、韓国語、ベトナム語、ロシア語、アラビア語の公開状況も掲載しています。**Available PDF** は公開済み、**In preparation** は準備中です。',
        '新しい翻訳PDFはA5の縦横を1.2倍にした177.6 × 252 mm、本文12 ptです。数式・原図を保持しています。従来の「pocket 1.2x」は文字の拡大率であり、この用紙寸法とは異なります。',
        '物理内容、アクセシビリティ、組版について、根拠のある修正をIssueでお寄せください。'),
 'zh-Hans': ('阅读多语言版本',
        '全套 16 册均有英语、日语、简体中文、法语、西班牙语和德语版。[各册 PDF 语言对照表]({table})也列出了繁体中文、韩语、越南语、俄语和阿拉伯语版的出版进度。点击 **Available PDF** 即可阅读；**In preparation** 表示尚未开放下载。',
        '新译本默认使用A5长宽各放大1.2倍的纸张（177.6 × 252 mm）、12 pt正文和舒适行距，保留公式与原图。旧版“pocket 1.2x”指字号放大，并非此纸张尺寸。',
        '欢迎通过 Issue 提交有依据的科学内容校订、无障碍改进或排版修正。'),
 'zh-Hant': ('閱讀多語言版本',
        '全套 16 冊均有英語、日語、簡體中文、法語、西班牙語和德語版。[各冊 PDF 語言對照表]({table})也列出繁體中文、韓語、越南語、俄語和阿拉伯語版的出版進度。點選 **Available PDF** 即可閱讀；**In preparation** 表示尚未開放下載。',
        '新譯本預設使用A5長寬各放大1.2倍的紙張（177.6 × 252 mm）、12 pt正文和舒適行距，保留公式與原圖。舊版「pocket 1.2x」指字號放大，並非此紙張尺寸。',
        '歡迎透過 Issue 提交有依據的科學內容校訂、無障礙改進或排版修正。'),
 'de': ('Mehrsprachige Ausgaben lesen',
        'Alle 16 Bände sind auf Englisch, Japanisch, Chinesisch (Kurzzeichen), Französisch, Spanisch und Deutsch erschienen. Die [PDF-Übersicht nach Band und Sprache]({table}) zeigt auch den Stand für Chinesisch (Langzeichen), Koreanisch, Vietnamesisch, Russisch und Arabisch. **Available PDF** öffnet die veröffentlichte Ausgabe; **In preparation** bedeutet, dass noch kein Download verfügbar ist.',
        'Neue übersetzte PDFs verwenden 177.6 × 252 mm (beide A5-Seiten × 1.2), 12 pt Schrift und erhalten Formeln und Abbildungen. Das ältere „pocket 1.2x“ bezeichnet größere Schrift, nicht dieses Papierformat.',
        'Belegte Korrekturen zu Physik, Barrierefreiheit oder Satz sind als Issue willkommen.'),
 'es': ('Leer las ediciones multilingües',
        'Los 16 libros están disponibles en inglés, japonés, chino simplificado, francés, español y alemán. En la [tabla de PDF por libro e idioma]({table}) también puedes consultar las ediciones en chino tradicional, coreano, vietnamita, ruso y árabe. **Available PDF** abre una edición publicada; **In preparation** indica que aún no se puede descargar.',
        'Los nuevos PDF traducidos usan papel de 177.6 × 252 mm (ambas dimensiones de A5 × 1.2), texto de 12 pt y conservan ecuaciones e ilustraciones. El antiguo «pocket 1.2x» amplía la tipografía, no indica este tamaño de papel.',
        'Se agradecen correcciones documentadas de física, accesibilidad o maquetación mediante una incidencia.'),
 'fr': ('Lire les éditions multilingues',
        'Les 16 livres sont disponibles en anglais, japonais, chinois simplifié, français, espagnol et allemand. Le [tableau des PDF par livre et par langue]({table}) indique aussi où en sont les éditions en chinois traditionnel, coréen, vietnamien, russe et arabe. **Available PDF** ouvre une édition publiée ; **In preparation** signifie que le PDF n’est pas encore disponible.',
        'Les nouveaux PDF traduits utilisent du papier de 177.6 × 252 mm (chaque dimension A5 × 1.2), un corps de 12 pt et conservent équations et figures. L’ancien « pocket 1.2x » désigne des caractères agrandis, pas ce format de papier.',
        'Les corrections documentées concernant la physique, l’accessibilité ou la mise en page sont les bienvenues via une issue.'),
 'ko': ('다국어판 읽기',
        '총 16권 모두 영어, 일본어, 중국어 간체, 프랑스어, 스페인어, 독일어로 읽을 수 있습니다. [책과 언어별 PDF 목록]({table})에서 중국어 번체, 한국어, 베트남어, 러시아어, 아랍어판의 출간 여부도 확인할 수 있습니다. **Available PDF**를 누르면 출간된 책이 열립니다. **In preparation**은 아직 내려받을 수 없다는 뜻입니다.',
        '새 번역 PDF는 A5의 가로·세로를 각각 1.2배 한 177.6 × 252 mm 용지와 12 pt 본문을 사용하며 수식과 원본 그림을 유지합니다. 기존 “pocket 1.2x”는 글자 확대율로, 이 용지 크기와 다릅니다.',
        '물리 내용, 접근성, 조판에 관한 근거 있는 수정은 Issue로 보내 주세요.'),
 'ru': ('Читайте многоязычные издания',
        'Все 16 книг доступны на английском, японском, упрощённом китайском, французском, испанском и немецком. В [таблице PDF по книгам и языкам]({table}) также можно проверить, вышла ли нужная книга на традиционном китайском, корейском, вьетнамском, русском или арабском. Ссылка **Available PDF** открывает издание; пометка **In preparation** означает, что скачать его пока нельзя.',
        'Новые переводные PDF используют бумагу 177.6 × 252 мм (обе стороны A5 × 1.2), шрифт 12 pt и сохраняют формулы и рисунки. Старое обозначение «pocket 1.2x» означает увеличение шрифта, а не этот формат бумаги.',
        'Присылайте через issue обоснованные исправления по физике, доступности или вёрстке.'),
 'vi': ('Đọc các ấn bản đa ngôn ngữ',
        'Cả 16 cuốn đều có bản tiếng Anh, Nhật, Trung giản thể, Pháp, Tây Ban Nha và Đức. [Bảng PDF theo sách và ngôn ngữ]({table}) cũng cho biết cuốn nào đã có bản tiếng Trung phồn thể, Hàn, Việt, Nga hoặc Ả Rập. Chọn **Available PDF** để mở bản đã xuất bản; **In preparation** nghĩa là chưa có bản tải xuống.',
        'PDF dịch mới dùng giấy 177.6 × 252 mm (mỗi chiều A5 × 1.2), chữ 12 pt, giữ nguyên công thức và hình. “pocket 1.2x” cũ chỉ cỡ chữ phóng lớn, không phải khổ giấy này.',
        'Vui lòng gửi qua issue các bản sửa có căn cứ về vật lý, khả năng tiếp cận hoặc dàn trang.'),
 'ar': ('اقرأ الطبعات متعددة اللغات',
        'تتوفر الكتب الستة عشر كلها بالإنجليزية واليابانية والصينية المبسطة والفرنسية والإسبانية والألمانية. ويبيّن [جدول ملفات PDF بحسب الكتاب واللغة]({table}) أيضاً ما صدر بالصينية التقليدية والكورية والفيتنامية والروسية والعربية. يفتح رابط **Available PDF** النسخة المنشورة، أما **In preparation** فتعني أنها غير متاحة للتنزيل بعد.',
        'تستخدم ملفات PDF المترجمة الجديدة ورقاً بقياس 177.6 × 252 مم (كل بُعد من A5 مضروب في 1.2)، وخطاً بحجم 12 نقطة، مع حفظ المعادلات والرسوم. يشير «pocket 1.2x» القديم إلى تكبير الخط لا إلى حجم الورق هذا.',
        'نرحب عبر issue بالتصحيحات الموثقة في الفيزياء أو الإتاحة أو التنسيق.'),
}

EDITION_LABELS = {'en': 'English', **{
    lang: spec['label'] for lang, spec in pipeline.LANGUAGE_SPECS.items()}}


def catalog():
    result = {'schema': 1, 'translatedPdfLayout': pipeline.LAYOUT, 'paperMm': [177.6, 252], 'books': {}}
    for book in pipeline.read(pipeline.MANIFEST)['books']:
        filename = CANONICAL_FILENAMES[book['course']]
        slug = filename[:-4].replace('_', '-')
        bunko = next((p.parent.name for p in (ROOT.parent / 'bunko-books/books').glob('physics-*/rights.json')
                      if any(r.endswith('/generated_course_notes/' + book['course']) for r in pipeline.read(p)['references'])), None)
        row = {'id': book['id'], 'titles': dict(book['titles']), 'bunkoId': bunko, 'editions': {
            'en': {'pdf': RAW + 'all_notes/pocket_books_1_2x/' + filename[:-4] + '_pocket_1_2x.pdf',
                   'layout': 'legacy-pocket-1.2x-type'}}}
        for lang in pipeline.LANGS:
            if pipeline.validated_output(book, lang):
                row['editions'][lang] = {'pdf': RAW + f'translations/{book["id"]}/{lang}/book.pdf',
                                         'layout': pipeline.LAYOUT}
                title = pipeline.read(pipeline.OUT / book['id'] / lang / 'quality.json').get('title')
                if title:
                    row['titles'][lang] = title
        result['books'][slug] = row
    return result


def language_notice(locale):
    heading, available, layout, invitation = NOTICES[locale]
    table = ('' if locale == 'en' else '../README.md') + '#final-polished-translations'
    return ('<!-- reading-languages:start -->\n## ' + heading + '\n\n'
            + available.format(table=table) + '\n\n' + layout + '\n\n' + invitation + '\n\n'
            '[Bunko](https://lachlan.lazying.art/Bunko/) · [LazyLearn](' + READER + ') · '
            '[GitHub Issues](https://github.com/lachlanchen/leonardsusskind/issues)\n'
            '<!-- reading-languages:end -->')


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
