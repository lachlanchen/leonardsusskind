import unittest
from collections import Counter
from copy import deepcopy
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

import sync_bunko_layers as s


def block(text, kind='text', math=None):
    unit = {'src': text, 'en': [text]}
    if math:
        unit['rich'] = {'en': [{'math': math}]}
    return {'id': 'stable-key', '_sourceSegment': 'source-key', 'kind': kind, 'src': text, 'u': [unit]}


def math_inventory(row):
    return Counter(piece['math'] for unit in row['u'] for piece in unit.get('rich', {}).get('en', [])
                   if 'math' in piece)


class BunkoLayerTests(unittest.TestCase):
    def test_alignment_checks_math_and_source_identity(self):
        source = block('A field.', math='F')
        target = block('Un campo.', math='F')
        base = s.groups([source])
        self.assertEqual(s.fit_layer(base, [target], math_inventory), [target])
        target['u'][0]['rich']['en'][0]['math'] = 'G'
        with self.assertRaisesRegex(ValueError, 'block/figure/math mismatch'):
            s.fit_layer(base, [target], math_inventory)
        target['_sourceSegment'] = 'new-key'
        with self.assertRaisesRegex(ValueError, 'Source segment coverage'):
            s.fit_layer(base, [target], math_inventory)

    def test_only_formatting_only_text_can_be_filtered(self):
        self.assertTrue(s.format_only(block('\u200c \u200b')))
        self.assertFalse(s.format_only(block('\u200c hello')))
        self.assertFalse(s.format_only(block('\u200c', 'heading')))

    def test_existing_layers_assets_and_passage_id_are_not_replaced(self):
        source = block('Figure.', kind='figure')
        source['figure'] = {'path': 'assets/board.webp', 'caption': {'en': ''}}
        old = deepcopy(source)
        old['id'] = 'stable-existing-reader-anchor'
        old['u'][0]['zh'] = ['图']
        old['u'][0]['ja'] = ['図']
        target = block('Figure française.', kind='figure')
        target['figure'] = {'path': 'assets/board.webp', 'caption': {'en': ''}}
        merged, = s.add_layers([old], [source], {'fr': [target]}, math_inventory)
        self.assertEqual(merged['id'], old['id'])
        self.assertEqual(merged['figure']['path'], old['figure']['path'])
        self.assertEqual(merged['u'][0].pop('fr'), ['Figure française.'])
        self.assertEqual(merged['figure']['caption'].pop('fr'), '')
        self.assertEqual(merged, old)

    def test_detached_caption_is_recovered_only_within_the_figure_segment(self):
        source = block('Figure caption.', kind='figure')
        source['figure'] = {'path': 'assets/board.webp', 'caption': {'en': ''}}
        placeholder = deepcopy(source)
        placeholder['src'] = 'Figure'
        placeholder['u'][0]['en'] = ['']
        caption = block('Légende.')
        fitted, = s.fit_layer(s.groups([source]), [placeholder, caption], math_inventory)
        self.assertEqual(fitted['figure'], source['figure'])
        self.assertEqual(fitted['u'][0]['en'], ['Légende.'])
        caption['_sourceSegment'] = 'another-segment'
        with self.assertRaisesRegex(ValueError, 'Source segment coverage'):
            s.fit_layer(s.groups([source]), [placeholder, caption], math_inventory)

    def test_quality_hash_must_match_the_published_git_snapshot(self):
        book = {'id': 'sample'}
        rel = 'translations/sample/fr'
        with TemporaryDirectory() as tmp, patch.object(s.p, 'ROOT', Path(tmp)):
            path = s.p.ROOT / rel / 'quality.json'
            s.p.textwrite(path, 'verified quality')
            data = path.read_bytes()
            snapshot = {rel + '/book.pdf': 'present',
                        rel + '/quality.json': s.sha(f'blob {len(data)}\0'.encode() + data)}
            with patch.object(s.p, 'validated_output', return_value=True) as verified:
                self.assertTrue(s.published_pdf(book, 'fr', snapshot, 'sha256'))
                path.write_text('new uncommitted quality')
                self.assertFalse(s.published_pdf(book, 'fr', snapshot, 'sha256'))
                verified.assert_called_once_with(book, 'fr')


if __name__ == '__main__':
    unittest.main()
