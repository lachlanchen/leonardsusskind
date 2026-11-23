import re
import unittest
from html.parser import HTMLParser
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

import translation_catalog as catalog

try:
    from markdown_it import MarkdownIt
except ImportError:
    MarkdownIt = None


class CoverImages(HTMLParser):
    def __init__(self):
        super().__init__()
        self.sources = []

    def handle_starttag(self, tag, attrs):
        source = dict(attrs).get('src', '')
        if tag == 'img' and 'readme-covers/' in source:
            self.sources.append(source)


class CoverTableTests(unittest.TestCase):
    def setUp(self):
        self.temp = TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.readme = self.root / 'README.md'
        self.data = {'books': {'sample': {'editions': {'en': {}, 'ja': {}, 'zh': {}}}}}
        self.original = (
            '# Sample\n\nOpening paragraph.\n\n<table>\n  <tr>\n'
            '    <td align="center">\n'
            '      <a href="' + catalog.READER + '?book=sample">'
            '<img src="figs/readme-covers/sample.png" alt="Sample"></a><br>\n'
            '      <sub>Course</sub>\n    </td>\n  </tr>\n</table>\n\n'
            'Closing paragraph.\n\nAnother paragraph.\n'
        )
        self.readme.write_text(self.original, encoding='utf-8')

    def decorate(self):
        with patch.object(catalog, 'ROOT', self.root), patch.object(catalog, 'catalog', return_value=self.data):
            catalog.decorate_readmes()
        return self.readme.read_text(encoding='utf-8')

    def assert_valid_cover_table(self, text):
        table = re.search(r'<table>.*?</table>', text, flags=re.S)[0]
        self.assertNotRegex(table, r'\n[ \t]*\n')
        self.assertEqual(table.count('<!-- edition-links -->'), 1)
        self.assertIn('src="figs/readme-covers/sample.png"', table)
        return table

    def test_new_links_do_not_interrupt_html_block(self):
        text = self.decorate()
        table = self.assert_valid_cover_table(text)
        for lang in ('en', 'ja', 'zh'):
            self.assertIn('?book=sample&amp;lang=' + lang, table)
        self.assertIn('Closing paragraph.\n\nAnother paragraph.', text)

    def test_published_readmes_point_to_the_same_pdf_table(self):
        root = catalog.ROOT / 'README.md'
        self.assertIn('\n## PDF Editions\n', root.read_text())
        self.assertEqual(len(catalog.NOTICES), 11)
        for locale in catalog.NOTICES:
            with self.subTest(locale=locale):
                path = root if locale == 'en' else root.parent / 'i18n' / f'README.{locale}.md'
                notice = catalog.language_notice(locale)
                self.assertIn(notice, path.read_text())
                table_path = '' if locale == 'en' else '../README.md'
                self.assertIn(f']({table_path}#final-polished-translations)', notice)
                self.assertIn(catalog.APP_STORE, notice)
                self.assertIn(catalog.PLAY_STORE, notice)
                for asset in ('icon.png', 'library-ios.png', 'reader-android.png'):
                    self.assertIn(f'src="{table_path and "../"}figs/bunko/{asset}"', notice)
                    self.assertTrue((root.parent / 'figs/bunko' / asset).is_file())

    def test_pdf_table_shows_only_verified_downloads_and_can_mark_completion(self):
        book = {'id': 'sample', 'course': 'supplementary/higgs_boson/2012_summer',
                'titles': {'en': 'Higgs Boson'}}
        row = {lang + '_pdf': 'validated' for lang in catalog.pipeline.LANGS}
        self.assertIn('All 1 books are available', catalog.pipeline.pdf_editions_block([book], [row]))
        row['ar_pdf'] = 'blocked'
        table = catalog.pipeline.pdf_editions_block([book], [row])
        self.assertIn('**9/10 translated PDFs published.**', table)
        self.assertIn('In preparation', table)
        self.assertNotIn('translations/sample/ar/book.pdf', table)

    def test_every_validated_language_is_linked(self):
        self.data['books']['sample']['editions'].update({'fr': {}, 'zh-Hant': {}, 'ar': {}})
        table = self.assert_valid_cover_table(self.decorate())
        for lang in ('fr', 'zh-Hant', 'ar'):
            self.assertIn('?book=sample&amp;lang=' + lang, table)

    def test_existing_broken_annotation_is_repaired_idempotently(self):
        broken = self.original.replace(
            '    </td>', '\n      <!-- edition-links --><br><sub>old links</sub>'
            '<!-- /edition-links -->\n    </td>')
        self.readme.write_text(broken, encoding='utf-8')
        repaired = self.decorate()
        self.assert_valid_cover_table(repaired)
        self.assertNotIn('old links', repaired)
        self.assertEqual(self.decorate(), repaired)

    def test_only_available_languages_are_linked(self):
        self.data['books']['sample']['editions'] = {'en': {}}
        table = self.assert_valid_cover_table(self.decorate())
        self.assertIn('&amp;lang=en', table)
        self.assertNotIn('&amp;lang=ja', table)
        self.assertNotIn('&amp;lang=zh', table)

    def test_legacy_cover_cells_remain_unchanged(self):
        self.data['books'] = {}
        text = self.decorate()
        original_table = re.search(r'<table>.*?</table>', self.original, flags=re.S)[0]
        self.assertIn(original_table, text)
        self.assertNotIn('<!-- edition-links -->', text)

    @unittest.skipUnless(MarkdownIt, 'markdown-it-py required for CommonMark rendering check')
    def test_rendered_tables_preserve_every_cover_in_all_readmes(self):
        parser = MarkdownIt('commonmark')
        paths = [catalog.ROOT / 'README.md', *sorted((catalog.ROOT / 'i18n').glob('README.*.md'))]
        self.assertEqual(len(paths), 11)
        for path in paths:
            with self.subTest(readme=path.name):
                source = path.read_text(encoding='utf-8')
                raw, rendered = CoverImages(), CoverImages()
                raw.feed(source)
                rendered.feed(parser.render(source))
                self.assertGreaterEqual(len(raw.sources), 16)
                self.assertEqual(rendered.sources, raw.sources)
                for image in raw.sources:
                    self.assertTrue((path.parent / image).is_file(), image)


if __name__ == '__main__':
    unittest.main()
