import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
from unittest.mock import patch
import polished_translation as p


class TranslationTests(unittest.TestCase):
    def setUp(self):
        p.PROVIDER_STOP.clear()

    def tearDown(self):
        p.PROVIDER_STOP.clear()

    def test_lossless_math_and_paths(self):
        source = r'\section{Motion} A field $x^2$ has 2 states.\begin{equation}E=mc^2\end{equation}\includegraphics[width=.8\textwidth]{board_1.png}'
        text, frozen = p.protect(source)
        self.assertEqual(p.restore(text, frozen), source)
        self.assertNotIn('E=mc', text)
        self.assertNotIn('board_1', text)
        self.assertIn('Motion', text)

    def test_prose_line_endings_do_not_change_frozen_equations(self):
        source = 'A field. \n' + r'\begin{equation}x=1  ' + '\n' + r'\end{equation}'
        masked, frozen = p.protect(source)
        result = p.restore(p.clean_prose_line_endings(masked), frozen)
        self.assertEqual(result, source.replace('field. \n', 'field.\n'))

    def test_heading_intro_and_caption_are_translatable(self):
        text, frozen = p.protect(r'\section{Heading}' + '\n\nIntroduction.\n\n' + r'\begin{figure}[tbp]\includegraphics{x.png}\caption{A board}\lectureframe{00:12:34}\end{figure}')
        for word in ['Heading', 'Introduction', 'A board']:
            self.assertIn(word, text)
        self.assertNotIn('00:12:34', text)
        self.assertNotIn('tbp', text)

    def test_heading_prose_cannot_escape_closing_braces(self):
        source, frozen = p.protect(r'\section{The Common Value of \texorpdfstring{\(L^2\)}{L squared}}')
        a, b, c, d = p.TOKEN.findall(source)
        self.assertIsNone(p.validate(source, a + b + 'Lの二乗' + c + 'の共通値' + d, 'ja', frozen))
        self.assertEqual(p.validate(source, a + b + 'Lの二乗' + c + d + 'の共通値', 'ja', frozen),
                         'heading text escaped its title argument')
        self.assertEqual(p.validate(source, a + '@' + b + 'Lの二乗' + c + d, 'ja', frozen),
                         'stray placeholder character')

    def test_closing_token_migration_preserves_existing_tex_and_ids(self):
        old = [r'\section{', r'\texorpdfstring{\(L^2\)}{', '}}']
        masked = '@@T000000@@Value @@T000001@@L squared@@T000002@@'
        updated, frozen, expansion = p.split_closing_tokens(masked, old)
        self.assertEqual(p.restore(masked, old), p.restore(updated, frozen))
        self.assertEqual(frozen[:2], old[:2])
        self.assertEqual(expansion, {'@@T000002@@': '@@T000002@@@@T000003@@'})
        self.assertEqual(p.split_closing_tokens(updated, frozen), (updated, frozen, {}))

    def test_malformed_json_is_archived_and_retried_once(self):
        with TemporaryDirectory() as tmp:
            dest = Path(tmp) / 'reply.json'
            calls = []

            def completion(prompt, path, log, **kwargs):
                calls.append(prompt)
                path.write_text('{broken' if len(calls) == 1 else '{"translations": {"0": "text"}}')

            with patch.dict(p.sys.modules, {'llm_chat_backend': SimpleNamespace(run_chat_completion=completion)}):
                result = p.chat('Translate', dest, SimpleNamespace(toolkit_root=Path(tmp), model='fixture'))
            self.assertEqual(len(calls), 2)
            self.assertEqual(result, {'translations': {'0': 'text'}})
            self.assertEqual(len(list(Path(tmp).glob('*.invalid-json'))), 1)

    def test_codex_transport_creates_private_destination_directory(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp) / 'work'):
            dest = Path(tmp) / 'nested' / 'reply.json'

            def completed(command, **kwargs):
                message = Path(command[command.index('-o') + 1])
                message.write_text('{"translations":{"0":"texte"}}', encoding='utf-8')
                return SimpleNamespace(returncode=0, stdout=b'completed')

            args = SimpleNamespace(reasoning='high', codex_timeout=60)
            with patch.object(p.subprocess, 'run', side_effect=completed):
                self.assertEqual(p.codex_chat('prompt', dest, args, 'gpt-6-luna'),
                                 {'translations': {'0': 'texte'}})
            self.assertTrue(dest.is_file())

    def test_json_parser_accepts_only_surplus_closing_braces(self):
        expected = {'translations': {'0': 'texte'}}
        self.assertEqual(p._parse_json_message('{"translations":{"0":"texte"}}}'), expected)
        with self.assertRaises(ValueError):
            p._parse_json_message('{"translations":{"0":"texte"}} commentary')

    def test_no_unsafe_model_syntax(self):
        self.assertIsNotNone(p.validate('Hello', r'\input{secret}', 'ja'))
        self.assertIsNotNone(p.validate('@@T000000@@ Hello', 'こんにちは', 'ja'))
        self.assertIsNotNone(p.validate('Hello', 'こんにちは 3', 'ja'))
        self.assertEqual(p.validate('position', '位�置', 'zh'), 'corrupt Unicode/control character')

    def test_each_new_language_rejects_untranslated_long_prose(self):
        source = ('The physical state evolves continuously while the measured observable '
                  'retains the same expectation value throughout the experiment.')
        translations = {
            'fr': 'L’état physique évolue continûment tandis que l’observable mesurée conserve la même valeur moyenne pendant toute l’expérience.',
            'es': 'El estado físico evoluciona continuamente mientras el observable medido conserva el mismo valor esperado durante el experimento.',
            'de': 'Der physikalische Zustand entwickelt sich stetig, während die gemessene Observable während des Experiments denselben Erwartungswert behält.',
            'zh-Hant': '物理狀態連續演化，而測得的可觀測量在整個實驗中保持相同的期望值。',
            'ko': '물리적 상태는 연속적으로 변하지만 측정된 관측량은 실험 내내 같은 기댓값을 유지한다.',
            'vi': 'Trạng thái vật lý biến đổi liên tục, trong khi đại lượng quan sát được vẫn giữ nguyên giá trị kỳ vọng trong suốt thí nghiệm.',
            'ru': 'Физическое состояние непрерывно эволюционирует, а измеряемая наблюдаемая сохраняет одно и то же среднее значение на протяжении эксперимента.',
            'ar': 'تتطور الحالة الفيزيائية بصورة متصلة، بينما تحتفظ الكمية المرصودة المقاسة بالقيمة المتوقعة نفسها طوال التجربة.',
        }
        for lang, translated in translations.items():
            with self.subTest(language=lang):
                self.assertIsNone(p.validate(source, translated, lang))
                self.assertEqual(p.validate(source, source, lang), 'untranslated prose')

    def test_traditional_chinese_uses_direct_conversion_before_polish(self):
        self.assertEqual(p.OPENCC_S2T.convert('量子纠缠与信息'), '量子糾纏與資訊')
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp)):
            book = {'id': 'fixture', 'titles': {'en': 'Physics', 'zh-Hant': '物理學'}}
            rel = 'chapter.tex'
            prepared = {'source_sha256': 'test', 'parts': ['Quantum entanglement and information.'], 'protected': []}
            p.write(p.WORK / 'prepared/fixture' / (rel + '.json'), prepared)
            p.write(p.result_path(book, 'zh', rel), {
                'source_sha256': 'test', 'accepted': {'0': '量子纠缠与信息。'}})
            prompts = []

            def reply(prompt, *args, **kwargs):
                prompts.append(prompt)
                return {'translations': {'0': '量子糾纏與資訊。'}}

            with patch.object(p, 'chat', side_effect=reply):
                p.translate_file(book, 'zh-Hant', rel, SimpleNamespace(batch_chars=80000))
            self.assertIn('"simplified_chinese_drafts": {"0": "量子糾纏與資訊。"}', prompts[0])
            self.assertIn('Do not retranslate from scratch', prompts[0])

    def test_published_cache_evidence_prevents_destructive_migration(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp) / 'work'), \
             patch.object(p, 'OUT', Path(tmp) / 'out'):
            slug, lang, rel = 'fixture', 'zh', 'chapter.tex'
            payload = {'source_sha256': 'source-hash'}
            accepted = {'0': '已验证的译文。'}
            translated = '已验证的完整 TeX。'
            p.write(p.WORK / 'results' / slug / lang / (rel + '.json'), {
                'source_sha256': 'source-hash', 'accepted': accepted})
            p.textwrite(p.OUT / slug / lang / rel, translated)
            p.write(p.OUT / slug / lang / 'quality.json', {
                'status': 'validated',
                'source_files': {rel: 'source-hash'},
                'translation_results': {rel: p.digest(p.json.dumps(
                    accepted, ensure_ascii=False, sort_keys=True))},
                'translated_tex': {rel: p.digest(translated)},
            })
            self.assertTrue(p.published_cache_proven(slug, rel, payload))
            p.textwrite(p.OUT / slug / lang / rel, translated + 'changed')
            self.assertFalse(p.published_cache_proven(slug, rel, payload))

    def test_math_at_end_of_heading_has_separate_closing_brace(self):
        source = r'\chapter{The meaning of \(k\)}'
        masked, protected = p.protect(source)
        a, math, b = p.TOKEN.findall(masked)
        self.assertEqual(p.restore(masked, protected), source)
        self.assertIsNone(p.validate(masked, a + math + 'の意味' + b, 'ja', protected))

    def test_layout_arguments_are_not_prose(self):
        source = r'\begin{adjustbox}{max width=\linewidth}Hello\end{adjustbox}'
        masked, frozen = p.protect(source)
        self.assertNotIn('max width', masked)
        self.assertEqual(p.restore(masked, frozen), source)
        bad = source.replace('max width', '最大宽度').replace('Hello', '你好')
        self.assertEqual(p.restore_layout_arguments(source, bad), source.replace('Hello', '你好'))

    def test_layout_restores_omitted_and_misplaced_optional_arguments(self):
        source = r'\begin{minipage}[t]{0.48\textwidth}Hello\end{minipage}'
        for header in (r'{0.48\textwidth}', r'{[t]0.48\textwidth}'):
            translated = r'\begin{minipage}' + header + r'Bonjour\end{minipage}'
            self.assertEqual(p.restore_layout_arguments(source, translated), source.replace('Hello', 'Bonjour'))

    def test_layout_restores_all_minipage_options_and_nested_headers(self):
        source = (r'\begin{minipage}[t][3cm][c]{0.5\textwidth}'
                  r'\begin{adjustbox}{max width=\linewidth}Hello\end{adjustbox}\end{minipage}')
        translated = (r'\begin{minipage}{0.5\textwidth}'
                      r'\begin{adjustbox}{\linewidth}Bonjour\end{adjustbox}\end{minipage}')
        self.assertEqual(p.restore_layout_arguments(source, translated), source.replace('Hello', 'Bonjour'))

    def test_layout_still_rejects_removed_environments(self):
        source = r'\begin{minipage}[c]{0.5\textwidth}Hello\end{minipage}'
        with self.assertRaisesRegex(ValueError, 'Layout environment structure changed'):
            p.restore_layout_arguments(source, 'Bonjour')

    def test_empty_content_does_not_stop_other_chapters(self):
        def completion(*args, **kwargs):
            try:
                raise RuntimeError('chat backend returned an empty message')
            except RuntimeError as exc:
                raise RuntimeError('deepseek completion failed after 3 attempt(s): RuntimeError') from exc
        with patch.dict(p.sys.modules, {'llm_chat_backend': SimpleNamespace(run_chat_completion=completion)}):
            with self.assertRaises(p.InvalidReply):
                p.chat('Translate', Path('/unused'), SimpleNamespace(toolkit_root=Path('/unused'), model='fixture'))
        self.assertFalse(p.PROVIDER_STOP.is_set())

    def test_layout_dimensions_are_explicit(self):
        self.assertIn('paperwidth=177.6mm,paperheight=252mm', p.page_layout())
        self.assertIn(r'\fancyfoot[C]', p.page_layout())
        self.assertIn(r'\setlength{\headwidth}{\textwidth}', p.page_layout())

    def test_spanish_page_layout_repairs_are_source_anchored(self):
        statistical = next(b for b in p.read(p.MANIFEST)['books']
                           if b['id'] == 'core--statistical_mechanics--2013_spring_theoretical_minimum')
        figure = ('\\begin{figure}[H]\n\\centering\n'
                  '\\includegraphics[width=0.90\\textwidth]{lecture_06_figure_16.png}')
        repaired = p.layout_repairs(statistical, 'es', 'chapters/lecture_06/content.tex', figure)
        self.assertEqual(repaired, '\\clearpage\n' + figure)
        with self.assertRaisesRegex(ValueError, 'layout anchor changed'):
            p.layout_repairs(statistical, 'es', 'chapters/lecture_06/content.tex', 'no figure here')
        cosmology = next(b for b in p.read(p.MANIFEST)['books']
                        if b['id'] == 'core--cosmology--2009_winter_legacy_cosmology')
        heading = r'\section{De la planitud a la estructura}'
        self.assertEqual(p.layout_repairs(cosmology, 'es', 'chapters/lecture_08/content.tex', heading),
                         '\\enlargethispage{1pt}\n' + heading)

    def test_german_layout_repairs_preserve_prose_and_column_widths(self):
        books = {book['id']: book for book in p.read(p.MANIFEST)['books']}
        heading = r'\section{Moden, Orthogonalität und Vollständigkeit}'
        advanced = books['supplementary--advanced_quantum_mechanics--2013_fall']
        self.assertEqual(p.layout_repairs(advanced, 'de', 'chapters/lecture_07/content.tex', heading),
                         '\\enlargethispage{1pt}\n' + heading)
        row = 'Gesamtenergie & Räumliche Krümmung & Entwicklung'
        entanglement = books['supplementary--quantum_entanglement--2006_fall_part_3']
        self.assertEqual(p.layout_repairs(entanglement, 'de', 'chapters/lecture_09/content.tex', row),
                         'Gesamt\\-energie & Räumliche Krümmung & Entwicklung')

    def test_traditional_chinese_overflow_break_is_bound_to_failing_references(self):
        cosmology = next(b for b in p.read(p.MANIFEST)['books']
                         if b['id'] == 'core--cosmology--2013_winter_theoretical_minimum')
        anchor = (r'方程式~\eqref{eq:c03-hyperboloid}與~'
                  r'\eqref{eq:c03-ambient-minkowski}')
        self.assertEqual(
            p.layout_repairs(cosmology, 'zh-Hant', 'chapters/lecture_03/content.tex', anchor),
            anchor + r'\allowbreak')
        with self.assertRaisesRegex(ValueError, 'layout anchor changed'):
            p.layout_repairs(cosmology, 'zh-Hant', 'chapters/lecture_03/content.tex',
                             'unrelated paragraph')

    def test_translation_tex_format_is_isolated(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp)):
            baseline = p.translation_tex_environment()
            fmt = p.WORK / 'texmf-var/web2c/xetex/xelatex.fmt'
            fmt.parent.mkdir(parents=True)
            fmt.touch()
            isolated = p.translation_tex_environment()
            self.assertEqual(isolated['TEXMFHOME'], str(p.WORK / 'texmf'))
            self.assertEqual(isolated['TEXMFVAR'], str(p.WORK / 'texmf-var'))
            self.assertEqual(isolated['TEXMFCONFIG'], str(p.WORK / 'texmf-config'))
            self.assertEqual(baseline.get('TEXMFVAR'), p.os.environ.get('TEXMFVAR'))

    def test_codex_quota_gate_caches_probe_and_blocks_low_quota(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp)), \
             patch.dict(p.os.environ, {'TRANSLATION_QUOTA_HELPER': '/quota-helper'}):
            completed = SimpleNamespace(stdout='{"ok":true,"remaining_percent":49}', returncode=0)
            with patch.object(p.subprocess, 'run', return_value=completed) as run:
                p.check_codex_quota()
                p.check_codex_quota()
                self.assertEqual(run.call_count, 1)
                self.assertEqual(run.call_args.args[0], [p.sys.executable, '/quota-helper', 'quota'])
            p.write(p.WORK / 'quota-check.json', {
                'ok': True, 'remaining_percent': 4, 'checked_at': p.time.time()})
            with patch.object(p.subprocess, 'run') as run, self.assertRaises(p.ProviderUnavailable):
                p.check_codex_quota()
            run.assert_not_called()

    def test_quota_probe_failure_is_not_reported_as_exhaustion(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp)), \
             patch.dict(p.os.environ, {'TRANSLATION_QUOTA_HELPER': '/quota-helper'}):
            p.write(p.WORK / 'quota-check.json', {
                'ok': False, 'error': 'RPC rejected', 'checked_at': p.time.time()})
            with self.assertRaisesRegex(p.ProviderUnavailable, 'telemetry unavailable.*RPC rejected'):
                p.check_codex_quota()

    def test_existing_credits_require_project_local_consent_and_positive_balance(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp)):
            data = {'credits': {'has_credits': True, 'balance': '12.5'}}
            self.assertFalse(p.existing_translation_credits_allowed(data))
            p.write(p.WORK / 'spending-policy.json', {'allow_existing_paid_credits': True})
            self.assertTrue(p.existing_translation_credits_allowed(data))
            for balance in ('0', '-1', 'NaN', 'Infinity', 'unknown'):
                self.assertFalse(p.existing_translation_credits_allowed({
                    'credits': {'has_credits': True, 'balance': balance}}))
            self.assertFalse(p.existing_translation_credits_allowed({}))

    def test_authorized_existing_credits_can_continue_below_quota_floor(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp)), \
             patch.dict(p.os.environ, {'TRANSLATION_QUOTA_HELPER': '/quota-helper'}):
            p.write(p.WORK / 'spending-policy.json', {'allow_existing_paid_credits': True})
            p.write(p.WORK / 'quota-check.json', {
                'ok': True, 'remaining_percent': 0, 'checked_at': p.time.time(),
                'credits': {'has_credits': True, 'balance': '12.5'}})
            with patch.object(p.subprocess, 'run') as probe:
                p.check_codex_quota()
            probe.assert_not_called()

    def test_temporary_codex_installation_gap_uses_bounded_transport_recovery(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp)), \
             patch.object(p, 'check_codex_quota'), \
             patch.object(p.subprocess, 'run', return_value=SimpleNamespace(
                 returncode=127, stdout=b'codex wrapper error: real Codex binary not found')):
            with self.assertRaisesRegex(p.ProviderUnavailable, 'APIConnectionError: Codex installation'):
                p.codex_chat('prompt', Path(tmp) / 'response.json',
                             SimpleNamespace(reasoning='high', codex_timeout=60), 'gpt-6-luna')

    def test_publication_refuses_an_unvalidated_edition(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'ROOT', Path(tmp)), \
             patch.object(p, 'validated_output', return_value=False), \
             patch.object(p.subprocess, 'check_output', return_value='') as git:
            (p.ROOT / 'README.md').touch()
            with self.assertRaisesRegex(RuntimeError, 'Refusing to publish an unvalidated'):
                p.publish_book({'id': 'book'}, ['es'])
            self.assertFalse(any(call.args[0][1] == 'add' for call in git.call_args_list))

    def test_cover_track_metadata_is_localized(self):
        self.assertEqual(p.localized_track('path/2013_fall', 'fr'), 'automne 2013')
        self.assertEqual(p.localized_track('path/2006_fall_part_1', 'fr'), 'automne 2006, première partie')
        self.assertEqual(p.localized_track('path/2011_winter_topics_in_string_theory', 'zh-Hant'),
                         '2011年冬季・弦理論專題')
        for lang in p.LANGS:
            label = p.localized_track('path/2012_spring_theoretical_minimum', lang)
            self.assertNotRegex(label, r'\b(?:spring|theoretical_minimum)\b')

    def test_cover_does_not_hyphenate_titles(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'ROOT', Path(tmp)):
            source = p.ROOT / 'generated_course_notes/course/2013_fall/course.tex'
            source.parent.mkdir(parents=True)
            source.write_text(r'\begin{titlepage}\color{black!80} Old title}\end{titlepage}')
            result = p.cover({'course': 'course/2013_fall', 'titles': {'fr': 'Théorie des cordes'}}, 'fr')
            self.assertIn(r'\hyphenpenalty=10000\exhyphenpenalty=10000', result)

    def test_caption_boundary_escape_is_rejected(self):
        source, protected = p.protect(r'\begin{figure}\caption{A particle diagram.}\label{fig:one}\end{figure}')
        tokens = p.TOKEN.findall(source)
        caption_start = next(t for t in tokens if p.restore(t, protected).endswith(r'\caption{'))
        closing = next(t for t in tokens if p.restore(t, protected).startswith('}'))
        target = source.replace('A particle diagram.', '粒子の').replace(closing, closing + '図。', 1)
        self.assertEqual(p.validate(source, target, 'ja', protected), 'caption text escaped its argument')
        self.assertTrue(caption_start)

    def test_url_protected_link_title_translated(self):
        text, _ = p.protect(r'\href{https://example.com}{Readable title}')
        self.assertNotIn('example.com', text)
        self.assertIn('Readable title', text)

    def test_math_table_and_question(self):
        source = r'\begin{classroomqa}\audiencequestion{Why $x$?}\lecturerresponse{Because $y$.}\end{classroomqa}'
        masked, tokens = p.protect(source)
        self.assertIn('Why', masked)
        self.assertIn('Because', masked)
        self.assertEqual(p.restore(masked, tokens), source)

    def test_only_words_trigger_translation(self):
        self.assertFalse(p.needs_translation('@@T000001@@\n\n'))
        self.assertTrue(p.needs_translation('@@T000001@@Introduction'))

    def test_valid_number_word_translation(self):
        self.assertIsNone(p.validate('the six quark flavors', '6種類のクォークフレーバー', 'ja'))
        self.assertIsNotNone(p.validate('the six quark flavors', '7種類のクォークフレーバー', 'ja'))
        self.assertIsNone(p.validate('one and a half times, at two standard deviations', '1.5倍で2標準偏差', 'ja'))
        self.assertIsNone(p.validate('Spin-One-Half', 'スピン1/2', 'ja'))

    def test_teen_compound_and_unity_are_not_invented_numbers(self):
        self.assertIsNone(p.validate('eight and eighteen elements', '8個と18個の元素', 'ja'))
        self.assertIsNone(p.validate('exactly thirty-seven particles', 'ちょうど37個の粒子', 'ja'))
        self.assertIsNotNone(p.validate('exactly thirty-seven particles', 'ちょうど38個の粒子', 'ja'))
        self.assertIsNotNone(p.validate('exactly thirty-seven particles', '30個と7個の粒子', 'ja'))
        self.assertIsNone(p.validate('eigenvalues of unit magnitude', '固有値の絶対値は1', 'ja'))
        self.assertIsNone(p.validate('their commutator is unity', '它们的对易子为1', 'zh'))
        self.assertIsNotNone(p.validate('a unit of energy', '能量为1', 'zh'))
        self.assertIsNone(p.validate('the first row and the second column', '第1行と第2列', 'ja'))
        self.assertIsNone(p.validate('a single trial and a quarter turn', '1回の試行と4分の1回転', 'ja'))
        self.assertIsNotNone(p.validate('a quarter turn', '3分の1回転', 'ja'))
        self.assertIsNone(p.validate('a penny and a dime', '1セント硬貨と10セント硬貨', 'ja'))
        self.assertIsNotNone(p.validate('a penny and a dime', '5セント硬貨と10セント硬貨', 'ja'))
        self.assertIsNone(p.validate('differentiate once', '1回微分する', 'ja'))
        self.assertIsNone(p.validate('Nineteenth-century physics', '19世紀の物理学', 'ja'))
        self.assertIsNone(p.validate('the two-thirds law', '3分の2の法則', 'ja'))
        self.assertIsNotNone(p.validate('the two-thirds law', '3分の1の法則', 'ja'))
        self.assertIsNotNone(p.validate('a year of time', '時間の2年', 'ja'))

    def test_reference_glue_and_accented_names_can_move_with_prose(self):
        source, frozen = p.protect(r'Now set \(y=x\) in Eq.~\eqref{test}.')
        tokens = p.TOKEN.findall(source)
        self.assertIsNone(p.validate(source, '式' + tokens[1] + 'において' + tokens[0] + 'と置く。', 'ja', frozen))
        self.assertTrue(p.movable_token(r'Schr\"odinger'))

    def test_large_number_units_preserve_values_not_writing_system(self):
        self.assertIsNone(p.validate('ten to twelve billion years; the size doubles', '100億年から120億年で2倍', 'ja'))
        self.assertIsNone(p.validate('a thousand times longer', '1000倍長い', 'ja'))
        self.assertIsNone(p.validate('a million years', '100万年', 'ja'))
        self.assertIsNone(p.validate('two billion years', '20亿年', 'zh'))
        self.assertIsNotNone(p.validate('ten to twelve billion years', '10億年から12億年', 'ja'))
        self.assertIsNotNone(p.validate('a thousand times longer', '100倍長い', 'ja'))
        self.assertIsNone(p.validate('doubles in size, acquiring a doubled wavelength', '大きさが2倍、波長も2倍', 'ja'))
        self.assertIsNone(p.validate('a one-kilogram object', '一个1千克的物体', 'zh'))
        self.assertIsNone(p.validate('two kilowatts', '2千瓦', 'zh'))
        self.assertIsNone(p.validate('three thousand years', '3千年', 'zh'))

    def test_inline_math_can_pass_around_but_not_enter_emphasis(self):
        source, frozen = p.protect(r'The integer \(n_i\) is the \emph{occupation number} of oscillator \(i\).')
        a, opening, closing, b = p.TOKEN.findall(source)
        valid = '整数' + a + '是第' + b + '个振子的' + opening + '占据数' + closing + '。'
        invalid = '整数' + a + '是' + opening + '第' + b + '个占据数' + closing + '。'
        self.assertIsNone(p.validate(source, valid, 'zh', frozen))
        self.assertIsNotNone(p.validate(source, invalid, 'zh', frozen))

    def test_repeated_equation_token_is_still_rejected(self):
        source, frozen = p.protect(r'Both \(x\) and \(y\) commute with \(H\).')
        a, b, h = p.TOKEN.findall(source)
        self.assertIsNotNone(p.validate(source, a + '与' + h + '对易，' + b + '也与' + h + '对易。', 'zh', frozen))

    def test_unknown_nested_structure_does_not_open_a_math_escape(self):
        frozen = [r'\emph{', r'\footnote{', '$x$', '}', '}']
        source = '@@T000000@@A@@T000001@@B@@T000002@@@@T000003@@@@T000004@@'
        escaped = '@@T000000@@A@@T000001@@B@@T000003@@@@T000004@@@@T000002@@'
        self.assertFalse(p.token_integrity(source, escaped, frozen))

    def test_source_bound_repair_validates_whole_packet_before_writing(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp) / 'work'), patch.object(p, 'MANIFEST', Path(tmp) / 'manifest.json'):
            book = {'id': 'fixture', 'source_files': {'chapter.tex': 'sha'}}
            p.write(p.MANIFEST, {'books': [book]})
            p.write(p.WORK / 'prepared/fixture/chapter.tex.json', {
                'source_sha256': 'sha', 'parts': ['eighteen states'], 'protected': []})
            packet = Path(tmp) / 'repairs.json'
            row = {'lang': 'ja', 'file': 'chapter.tex', 'segment_id': '0', 'source_sha256': 'sha',
                   'source': 'eighteen states', 'translation': '18個の状態', 'reason': 'Number-word check'}
            p.write(packet, {'book': 'fixture', 'repairs': [row, {**row, 'source': 'stale'}]})
            with patch.object(p, 'verify_sources'):
                with self.assertRaisesRegex(ValueError, 'Stale repair source'):
                    p.apply_reviewed_repairs(packet)
                self.assertFalse(p.result_path(book, 'ja', 'chapter.tex').exists())
                p.write(packet, {'book': 'fixture', 'repairs': [row]})
                p.apply_reviewed_repairs(packet)
                result = p.read(p.result_path(book, 'ja', 'chapter.tex'))
                self.assertEqual(result['accepted'], {'0': '18個の状態'})
                self.assertEqual(result['review_ids'], ['0'])
                p.write(packet, {'book': 'fixture', 'repairs': [{**row, 'translation': '18の状態'}]})
                with self.assertRaisesRegex(ValueError, 'Existing translation changed'):
                    p.apply_reviewed_repairs(packet)
                result['accepted']['0'] = '18個の状�態'
                p.write(p.result_path(book, 'ja', 'chapter.tex'), result)
                p.write(packet, {'book': 'fixture', 'repairs': [{
                    **row, 'previous_sha256': p.digest(result['accepted']['0'])}]})
                p.apply_reviewed_repairs(packet)

    def test_review_adjudication_is_bound_to_exact_sample_and_issue(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp)):
            book = {'id': 'fixture'}
            issue = {'source_quote': 'roughly one percent', 'translation_quote': 'およそ1パーセント',
                     'correction': '0.7パーセント'}
            report = {'pass': False, 'issues': [issue], 'sample_sha256': 'current'}
            path = p.WORK / 'review-decisions/fixture/ja.current.json'
            p.write(path, {'sample_sha256': 'current', 'decisions': [{
                'issue_sha256': p.digest(p.json.dumps(issue, ensure_ascii=False, sort_keys=True)),
                'decision': 'dismiss', 'reason': 'The translation preserves the source approximation.'}]})
            effective = p.adjudicated_review(book, 'ja', report)
            self.assertTrue(effective['pass'])
            self.assertEqual(effective['raw_issues'], [issue])
            self.assertFalse(p.adjudicated_review(book, 'ja', {**report, 'sample_sha256': 'changed'})['pass'])
            with self.assertRaisesRegex(ValueError, 'stale review decision'):
                p.adjudicated_review(book, 'ja', {**report, 'issues': [{'other': 'issue'}]})

    def test_inline_math_can_move_but_not_across_structural_boundaries(self):
        source = '@@T000000@@One @@T000001@@ two @@T000002@@@@T000003@@'
        protected = [r'\section{', '$x$', '$y$', '}']
        good = '@@T000000@@日本語@@T000002@@、@@T000001@@@@T000003@@'
        bad = '@@T000000@@日本語@@T000002@@@@T000003@@@@T000001@@'
        self.assertIsNone(p.validate(source, good, 'ja', protected))
        self.assertIsNotNone(p.validate(source, bad, 'ja', protected))

    def test_display_math_must_not_move(self):
        source = '@@T000000@@A@@T000001@@'
        self.assertFalse(p.token_integrity(source, '@@T000001@@A@@T000000@@',
                                          [r'\begin{equation}x\end{equation}', r'\begin{equation}y\end{equation}']))
        self.assertTrue(p.token_integrity(source, '@@T000001@@A@@T000000@@',
                                         [r'\begin{equation}x\end{equation}', '$y$']))

    def test_accented_name_is_atomic(self):
        source = r'Fran\c{c}ois Englert found it.'
        masked, frozen = p.protect(source)
        self.assertNotIn('Fran', masked)
        self.assertEqual(frozen[0], r'Fran\c{c}ois')
        self.assertEqual(p.restore(masked, frozen), source)
        masked, frozen = p.protect(r'Schr\"odinger equation')
        self.assertNotIn('Schr', masked)
        self.assertEqual(frozen[0], r'Schr\"odinger')

    def test_retry_only_failed_segment_then_resume_without_calls(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp)):
            book = {'id': 'fixture', 'titles': {'en': 'Physics', 'ja': '物理'}}
            rel = 'chapters/lecture_01/content.tex'
            prepared = {'source_sha256': 'test', 'parts': ['First paragraph.', '\n\n', 'Second paragraph.'], 'protected': []}
            p.write(p.WORK / 'prepared/fixture' / (rel + '.json'), prepared)
            prompts = []

            def fake_chat(prompt, dest, args):
                prompts.append(prompt)
                if len(prompts) == 1:
                    return {'translations': {'0': '第一の段落。', '2': ''}}
                self.assertNotIn('First paragraph.', prompt)
                return {'translations': {'2': '第二の段落。'}}

            with patch.object(p, 'chat', side_effect=fake_chat):
                p.translate_file(book, 'ja', rel, SimpleNamespace())
                p.translate_file(book, 'ja', rel, SimpleNamespace())
            self.assertEqual(len(prompts), 2)
            result = p.read(p.result_path(book, 'ja', rel))
            self.assertEqual(set(result['accepted']), {'0', '2'})

    def test_source_mutation_blocks_queue(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'ROOT', Path(tmp)):
            source = Path(tmp) / 'generated_course_notes/demo/content.tex'
            source.parent.mkdir(parents=True)
            source.write_text('changed')
            with self.assertRaisesRegex(RuntimeError, 'source changed'):
                p.verify_sources({'course': 'demo', 'source_files': {'content.tex': p.digest('original')}})

    def test_failed_segments_use_bounded_reasoning_repair_and_preserve_success(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp)):
            book = {'id': 'fixture', 'titles': {'en': 'Physics', 'ja': '物理'}}
            rel = 'chapter.tex'
            prepared = {'source_sha256': 'test', 'parts': ['A year of time.', '\n\n', 'A simple statement.'], 'protected': []}
            p.write(p.WORK / 'prepared/fixture' / (rel + '.json'), prepared)
            calls = []

            def reply(prompt, dest, args, **kwargs):
                calls.append(kwargs.get('model', 'writer'))
                if len(calls) == 1:
                    return {'translations': {'0': '時間の2年。', '2': '単純な文。'}}
                self.assertNotIn('A simple statement.', prompt)
                return {'translations': {'0': '時間の2年。' if len(calls) == 2 else '年という時間。'}}

            with patch.object(p, 'chat', side_effect=reply):
                p.translate_file(book, 'ja', rel, SimpleNamespace())
                p.translate_file(book, 'ja', rel, SimpleNamespace())
            self.assertEqual(calls, ['writer', 'writer', 'deepseek-reasoner'])
            result = p.read(p.result_path(book, 'ja', rel))
            self.assertEqual(result['accepted'], {'0': '年という時間。', '2': '単純な文。'})
            self.assertIn('0', result['review_ids'])

    def test_korean_zero_predicates_are_local_counted_and_polarity_sensitive(self):
        for source, candidate in [
                ('The field vanishes.', '장이 0이 된다.'),
                ('There is a nonzero field.', '0이 아닌 장이 있다.')]:
            evidence = []
            self.assertIsNone(p.validate(source, candidate, 'ko', [], number_evidence=evidence))
            self.assertTrue(evidence)
        for source, candidate in [
                ('The field vanishes.', '장이 0이 아니다.'),
                ('The field never vanishes.', '장이 0이 된다.'),
                ('The field nearly vanishes.', '장이 0이 된다.'),
                ('The field vanishes.', '장이 0이고 힘도 0이다.'),
                ('The field is nonzero.', '장이 0이다.'),
                ('It is nonzero.', '값이 0이 아닌 것은 아니다.'),
                ('The field vanishes.', '장이 0.1이 된다.'),
                ('The field vanishes.', '장이 -0이 된다.'),
                ('The field vanishes.', '장이 0이 되고 힘은 7이다.'),
                ('It vanishes. Another observation.', '장이 사라진다. 힘은 0이다.'),
                ('It is nonzero@@T000000@@here.', '여기에@@T000000@@0이 아닌 값이 있다.'),
                ('It is so.', '장이 0이다.')]:
            with self.subTest(candidate=candidate, source=source):
                self.assertEqual(p.validate(source, candidate, 'ko', ['$x$']), 'introduced unprotected number')
        self.assertIsNotNone(p.validate('The field vanishes.', '장이 0이 된다.', 'ja'))

    def test_korean_zero_predicate_survives_movable_inline_math(self):
        source, protected = p.protect(r'A nonzero value $x$ is allowed.')
        token = p.TOKEN.findall(source)[0]
        translated = token + '0이 아닌 값은 허용된다.'
        self.assertIsNone(p.validate(source, translated, 'ko', protected))
        self.assertEqual(p.validate(source, translated + ' 0이 아닌 다른 값도 있다.', 'ko', protected),
                         'introduced unprotected number')
        self.assertIsNone(p.validate('the two-thirds law', '3분의 2 법칙', 'ko'))
        self.assertIsNotNone(p.validate('the two-thirds law', '3분의 1 법칙', 'ko'))
        self.assertIsNone(p.validate('one sixth of a period', '주기의 6분의 1', 'ko'))
        self.assertIsNone(p.validate('one third of the acceleration', '가속도의 3분의 1', 'ko'))
        self.assertIsNone(p.validate('The separation is nonzero, but the set is not finite.',
                                     '간격은 0이 아니지만 집합은 유한하지 않다.', 'ko'))
        self.assertIsNone(p.validate('The matrix has a vanishing row.', '행렬에는 0인 행이 있다.', 'ko'))
        self.assertIsNone(p.validate('The component vanishes although the vector is nonzero.',
                                     '성분은 0이지만 벡터는 0이 아니다.', 'ko'))
        self.assertIsNone(p.validate('zeros everywhere else', '나머지 모든 성분은 0이다.', 'ko'))
        self.assertIsNone(p.validate('zero momentum and nonzero angular momentum',
                                     '운동량은 0이고 각운동량은 0이 아니다.', 'ko'))
        self.assertEqual(p.validate('zero momentum and nonzero angular momentum',
                                     '운동량은 0이고 각운동량은 0이 아니며 에너지도 0이다.', 'ko'),
                         'introduced unprotected number')
        self.assertIsNone(p.validate('the following decade', '그 뒤 10년', 'ko'))
        self.assertIsNone(p.validate('the entropy vanishes even though it is small.',
                                     '엔트로피가 작아도 0이어도 된다.', 'ko'))
        source, protected = p.protect('The expectation value vanishes along every axis:\n$x=0$')
        token = p.TOKEN.findall(source)[0]
        self.assertIsNone(p.validate(source, '모든 축에서 기댓값은 0이다.\n' + token,
                                     'ko', protected))

    def test_korean_numeric_recovery_never_spends_or_replaces_accepted_text(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp)):
            book = {'id': 'fixture', 'titles': {'en': 'Physics'}}
            rel = 'chapter.tex'
            prepared = {'source_sha256': 'test', 'parts': ['First passage.', 'A nonzero factor.'], 'protected': []}
            p.write(p.WORK / 'prepared/fixture' / (rel + '.json'), prepared)
            attempts = {'1': {'writer': 2, 'repair': 2}}
            dest = p.result_path(book, 'ko', rel)
            p.write(dest, {'source_sha256': 'test', 'accepted': {'0': '첫 문단.'}, 'attempts': attempts,
                           'candidates': {'0': '교체하지 말 것.', '1': '0이 아닌 인자.'}})
            with patch.object(p, 'chat') as chat:
                for _ in range(2):
                    p.translate_file(book, 'ko', rel, SimpleNamespace())
                chat.assert_not_called()
            r = p.read(dest)
            self.assertEqual(r['attempts'], attempts)
            self.assertEqual(r['review_ids'], ['1'])
            self.assertEqual(r['accepted'], {'0': '첫 문단.', '1': '0이 아닌 인자.'})
            self.assertEqual(r['cache_rechecks'], {'1': p.digest(r['accepted']['1'])})
            fresh = {'accepted': {}}
            p.accept_candidates(prepared, fresh, {'1': prepared['parts'][1]}, {'1': r['accepted']['1']}, 'ko', 'writer')
            self.assertEqual(fresh['review_ids'], ['1'])

    def test_language_recheck_refuses_stale_source_and_dry_run_never_writes(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            with patch.object(p, 'WORK', root), patch.object(p, 'OUT', root/'out'), \
                    patch.object(p, 'MANIFEST', root/'manifest'), patch.object(p, 'verify_sources') as verify:
                book = {'id': 'demo', 'source_files': {'file.tex': 'hash'}}
                p.write(p.MANIFEST, {'books': [book]})
                src = root/'prepared/demo/file.tex.json'
                p.write(src, {'source_sha256': 'hash', 'parts': ['A nonzero factor.'], 'protected': []})
                dest = p.result_path(book, 'ko', 'file.tex')
                original = {'source_sha256': 'hash', 'accepted': {}, 'candidates': {'0': '0이 아닌 인자.'}}
                p.write(dest, original)
                self.assertEqual(p.recheck_language('ko', True), 1)
                self.assertEqual(p.read(dest), original)
                verify.assert_called_once_with(book)
                p.write(dest, {**original, 'source_sha256': 'other'})
                with self.assertRaisesRegex(ValueError, 'Stale repair source'):
                    p.recheck_language('ko', False)
                p.write(dest, original)
                self.assertEqual(p.recheck_language('ko', False), 1)
                self.assertEqual(p.recheck_language('ko', False), 0)

    def test_persistent_budget_prevents_resume_retry_amplification(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp)):
            book = {'id': 'fixture', 'titles': {'en': 'Physics', 'ja': '物理'}}
            rel = 'chapter.tex'
            p.write(p.WORK / 'prepared/fixture' / (rel + '.json'), {
                'source_sha256': 'test', 'parts': ['A field.'], 'protected': []})
            with patch.object(p, 'chat', return_value={'translations': {'0': '場999'}}) as chat:
                for _ in range(3):
                    with self.assertRaisesRegex(RuntimeError, 'Needs segment repair'):
                        p.translate_file(book, 'ja', rel, SimpleNamespace())
                self.assertEqual(chat.call_count, 4)

    def test_interrupted_completed_response_is_recovered_without_new_call(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp)):
            book = {'id': 'fixture', 'titles': {'en': 'Physics', 'ja': '物理'}}
            rel = 'chapter.tex'
            p.write(p.WORK / 'prepared/fixture' / (rel + '.json'), {
                'source_sha256': 'test', 'parts': ['A field.'], 'protected': []})
            response = Path(tmp) / 'response.json'
            p.write(response, {'translations': {'0': 'ある場。'}})
            p.write(p.result_path(book, 'ja', rel), {'source_sha256': 'test', 'accepted': {},
                'inflight': {'path': str(response), 'ids': ['0'], 'stage': 'writer', 'source_sha256': 'test'}})
            with patch.object(p, 'chat') as chat:
                p.translate_file(book, 'ja', rel, SimpleNamespace())
                chat.assert_not_called()
            self.assertEqual(p.read(p.result_path(book, 'ja', rel))['accepted'], {'0': 'ある場。'})

    def test_provider_failure_stops_calls_and_refunds_content_attempt(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp)):
            book = {'id': 'fixture', 'titles': {'en': 'Physics', 'ja': '物理'}}
            prepared = {'source_sha256': 'test', 'parts': ['A field.'], 'protected': []}
            result = {'source_sha256': 'test', 'accepted': {}}
            with patch.object(p, 'chat', side_effect=p.ProviderUnavailable('balance')):
                with self.assertRaises(p.ProviderUnavailable):
                    p.request_segments(book, 'ja', 'chapter.tex', prepared, result,
                                       {'0': 'A field.'}, SimpleNamespace(), 'writer', {}, 'prompt')
            self.assertEqual(result['attempts']['0']['writer'], 0)
            self.assertNotIn('inflight', result)
            args = SimpleNamespace(toolkit_root=Path(tmp), model='fixture')
            with patch.dict(p.sys.modules, {'llm_chat_backend': SimpleNamespace(
                    run_chat_completion=lambda *a, **k: (_ for _ in ()).throw(RuntimeError('402')))}):
                with self.assertRaises(p.ProviderUnavailable):
                    p.chat('prompt', Path(tmp) / 'reply.json', args)
                self.assertTrue(p.PROVIDER_STOP.is_set())

    def test_one_blocked_language_does_not_prevent_other_finalization(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp)):
            book = {'id': 'fixture', 'source_files': {'chapter.tex': 'sha'}}
            args = SimpleNamespace(workers=1, ramp_seconds=0)
            with patch.object(p, 'translate_file', side_effect=[RuntimeError('bad ja'), None]), \
                 patch.object(p, 'update_readmes'), patch.object(p, 'validated_output', return_value=False), \
                 patch.object(p, 'language_complete', side_effect=[False, True]), \
                 patch.object(p, 'compile_book') as compile_book:
                errors = p.run_book(book, args)
            self.assertEqual(len(errors), 1)
            compile_book.assert_called_once_with(book, 'zh', args)

    def test_semantic_repair_retains_original_until_candidate_validates(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp) / 'work'), \
             patch.object(p, 'OUT', Path(tmp) / 'out'):
            book = {'id': 'fixture', 'titles': {'en': 'Physics'}, 'source_files': {'chapter.tex': 'sha'}}
            source, frozen = p.protect(r'The charge is \(q\).')
            token = p.TOKEN.findall(source)[0]
            old = '電荷は' + token + '。'
            p.write(p.WORK / 'prepared/fixture/chapter.tex.json', {
                'source_sha256': 'sha', 'parts': [source], 'protected': frozen})
            p.write(p.result_path(book, 'ja', 'chapter.tex'), {'source_sha256': 'sha', 'accepted': {'0': old}})
            report = {'issues': [{'chapter': 'chapter.tex', 'segment_id': '0', 'reason': 'Fixture only'}]}
            with patch.object(p, 'chat', return_value={'translations': {'0': '電荷の説明。'}}):
                self.assertTrue(p.repair_review(book, 'ja', report, SimpleNamespace()))
            self.assertEqual(p.read(p.result_path(book, 'ja', 'chapter.tex'))['accepted']['0'], old)
            with patch.object(p, 'chat', return_value={'translations': {'0': '電荷は' + token + 'である。'}}):
                self.assertTrue(p.repair_review(book, 'ja', report, SimpleNamespace()))
            result = p.read(p.result_path(book, 'ja', 'chapter.tex'))
            self.assertEqual(result['superseded']['0'], [old])
            self.assertEqual(result['review_ids'], ['0'])
            self.assertEqual(p.read(p.OUT / 'fixture/ja/quality.json')['status'], 'needs_rebuild')
            with patch.object(p, 'chat') as chat:
                self.assertFalse(p.repair_review(book, 'ja', report, SimpleNamespace()))
                chat.assert_not_called()

    def test_failed_batch_does_not_abandon_remaining_chapter(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp)):
            book = {'id': 'fixture', 'titles': {'en': 'Physics', 'ja': '物理'}}
            p.write(p.WORK / 'prepared/fixture/chapter.tex.json', {
                'source_sha256': 'sha', 'parts': ['First paragraph. ' * 300, '\n\n', 'Second paragraph.'], 'protected': []})

            def reply(prompt, *args, **kwargs):
                return {'translations': {'2': '第二の段落。'}} if 'Second paragraph.' in prompt else {'translations': {}}

            with patch.object(p, 'chat', side_effect=reply):
                with self.assertRaisesRegex(RuntimeError, 'Needs segment repair'):
                    p.translate_file(book, 'ja', 'chapter.tex', SimpleNamespace())
            self.assertEqual(p.read(p.result_path(book, 'ja', 'chapter.tex'))['accepted'], {'2': '第二の段落。'})

    def test_blocked_book_does_not_stop_later_books(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp)), \
             patch.object(p, 'MANIFEST', Path(tmp) / 'manifest.json'):
            books = [{'id': 'first'}, {'id': 'second'}]
            p.write(p.MANIFEST, {'books': books})
            p.write(p.WORK / 'pilot-approved.json', {})
            args = SimpleNamespace(pilot_only=False, workers=5, publish=False)
            complete = set()

            def process(book, args, languages):
                if book['id'] == 'second':
                    complete.add('second')
                    return []
                return [{'stage': 'translation', 'error': 'bad paragraph'}]

            with patch.object(p, 'verify_sources'), patch.object(p, 'update_readmes'), \
                 patch.object(p, 'language_complete', return_value=True), \
                 patch.object(p, 'validated_output', side_effect=lambda b, l: b['id'] in complete), \
                 patch.object(p, 'run_book', side_effect=process) as runner:
                p.run(args)
            self.assertEqual(runner.call_count, 2)
            self.assertEqual(p.read(p.WORK / 'status.json')['blocked_books'], ['first'])
            self.assertEqual(p.read(p.WORK / 'book-state/second.json')['state'], 'complete')

    def test_transport_recovery_waits_only_for_transient_failures(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp)):
            p.write(p.WORK / 'status.json', {'state': 'provider_blocked'})
            args = SimpleNamespace(transport_resumes=2, transport_retry_seconds=0)
            with patch.object(p, 'run', side_effect=[p.ProviderUnavailable('status=429'), None]) as run:
                p.run_with_transport_recovery(args)
                self.assertEqual(run.call_count, 2)
            with patch.object(p, 'run', side_effect=p.ProviderUnavailable('status=402')) as run:
                with self.assertRaises(p.ProviderUnavailable):
                    p.run_with_transport_recovery(args)
                self.assertEqual(run.call_count, 1)
            with patch.object(p, 'run', side_effect=p.ProviderUnavailable('APIConnectionError')) as run:
                with self.assertRaises(p.ProviderUnavailable):
                    p.run_with_transport_recovery(args)
                self.assertEqual(run.call_count, 3)

    def test_transport_wait_honors_stop_marker(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp)):
            p.write(p.WORK / 'status.json', {'state': 'provider_blocked'})
            (p.WORK / 'STOP').touch()
            with patch.object(p, 'run', side_effect=p.ProviderUnavailable('status=503')), patch.object(p.time, 'sleep') as sleep:
                p.run_with_transport_recovery(SimpleNamespace(transport_resumes=2, transport_retry_seconds=300))
                sleep.assert_not_called()
            self.assertEqual(p.read(p.WORK / 'status.json')['state'], 'paused')

    def test_transport_budget_resets_only_after_measurable_progress(self):
        with TemporaryDirectory() as tmp, patch.object(p, 'WORK', Path(tmp)), \
             patch.object(p, 'transport_progress', side_effect=[(0, 0), (1, 0), (2, 0), (2, 0), (2, 0)]), \
             patch.object(p, 'run', side_effect=p.ProviderUnavailable('APIConnectionError')) as run:
            with self.assertRaises(p.ProviderUnavailable):
                p.run_with_transport_recovery(SimpleNamespace(transport_resumes=2, transport_retry_seconds=0))
            self.assertEqual(run.call_count, 4)

    def test_publication_pushes_and_verifies_each_remote_with_retry(self):
        attempts = {}

        def git(*args):
            if args == ('rev-parse', 'HEAD'):
                return 'abc123\n'
            if args == ('remote', 'get-url', '--push', '--all', 'origin'):
                return 'canonical\nmirror\n'
            if args[0] == 'push':
                attempts[args[1]] = attempts.get(args[1], 0) + 1
                if args[1] == 'canonical' and attempts[args[1]] == 1:
                    raise RuntimeError('transient transport failure')
                return ''
            if args[0] == 'ls-remote':
                return 'abc123\trefs/heads/main\n'
            self.fail(f'Unexpected git call: {args}')

        with patch.object(p.time, 'sleep') as sleep:
            p.push_publication_remotes(git)
        self.assertEqual(attempts, {'canonical': 2, 'mirror': 1})
        sleep.assert_called_once_with(1)

    def test_publication_rejects_unverified_remote_sha(self):
        def git(*args):
            if args == ('rev-parse', 'HEAD'):
                return 'local\n'
            if args == ('remote', 'get-url', '--push', '--all', 'origin'):
                return 'canonical\n'
            if args[0] == 'push':
                return ''
            if args[0] == 'ls-remote':
                return 'stale\trefs/heads/main\n'
            self.fail(f'Unexpected git call: {args}')

        with patch.object(p.time, 'sleep'), self.assertRaisesRegex(RuntimeError, 'after 3 attempts'):
            p.push_publication_remotes(git)

    def test_preamble_retains_custom_macros_and_localizes_labels(self):
        source = r'\usepackage[utf8]{inputenc}' + '\n' + r'\newcommand{\custom}[1]{#1}\newcommand{\lectureoverview}[1]{\paragraph{Overview.} #1}'
        result = p.translated_preamble(source, 'ja')
        self.assertNotIn('inputenc', result)
        self.assertIn(r'\newcommand{\custom}', result)
        self.assertIn('Noto Serif CJK JP', result)
        self.assertIn('概観。', result)
        self.assertIn(r'\emergencystretch=2em', result)
        korean = p.translated_preamble(source, 'ko')
        self.assertIn(r'\usepackage[CJKspace]{xeCJK}', korean)
        self.assertIn('Noto Serif CJK KR', korean)
        self.assertNotIn('[CJKspace]', p.translated_preamble(source, 'zh'))
        french = p.translated_preamble(source, 'fr')
        self.assertIn(r'\emergencystretch=6em', french)
        self.assertIn(r'\sectionfont{\raggedright}', french)
        self.assertIn(r'\subsectionfont{\raggedright}', french)
        self.assertIn(r'\usepackage{tocloft}', french)
        self.assertIn(r'\renewcommand{\@pnumwidth}{2.2em}', french)
        self.assertIn(r'\setlength{\cftsecnumwidth}{3em}', french)
        self.assertIn(r'\setlength{\cftsubsecnumwidth}{4em}', french)
        arabic = p.translated_preamble(source, 'ar')
        self.assertIn(r'\sectionfont{\raggedleft}', arabic)
        self.assertIn(r'\subsectionfont{\raggedleft}', arabic)


if __name__ == '__main__':
    unittest.main()
