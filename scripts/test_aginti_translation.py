import json
import subprocess
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
from unittest.mock import patch

import polished_translation as p


class AgintiTranslationTests(unittest.TestCase):
    def setUp(self):
        scratch = TemporaryDirectory()
        self.addCleanup(scratch.cleanup)
        self.root = Path(scratch.name)
        self.dest = self.root / 'response.json'
        self.args = SimpleNamespace(provider='aginti-openai', model='gpt-5.4',
                                    reasoning='high', aginti_timeout=60)
        work = patch.object(p, 'WORK', self.root)
        work.start()
        self.addCleanup(work.stop)
        probe = patch.object(p, 'check_codex_quota', side_effect=AssertionError)
        self.probe = probe.start()
        self.addCleanup(probe.stop)
        aginti = patch.object(p.shutil, 'which', return_value='/verified/bin/aginti')
        aginti.start()
        self.addCleanup(aginti.stop)
        self.addCleanup(p.PROVIDER_STOP.clear)
        p.PROVIDER_STOP.clear()

    def run_result(self, reason='', **updates):
        reply = {'ok': not reason, 'failed': bool(reason), 'provider': 'openai',
                 'model': 'gpt-5.4', 'result': '{"translations":{"0":"Năng lượng."}}',
                 'reason': reason, **updates}
        return subprocess.CompletedProcess([], int(bool(reason)), json.dumps(reply), '')

    def test_openai_route_with_tools_disabled_and_no_codex_quota_probe(self):
        with patch.object(p.subprocess, 'run', return_value=self.run_result()) as run:
            self.assertEqual(p.chat('Source text', self.dest, self.args), p.read(self.dest))
        command, = run.call_args.args
        self.assertEqual(command[0], 'node')
        self.assertTrue(command[1].endswith('/aginti_openai_completion.mjs'))
        self.assertEqual(command[2:], ['/verified/bin/aginti', 'gpt-5.4', 'high', '60'])
        self.assertIn('Source text', run.call_args.kwargs['input'])
        self.assertNotIn('Source text', command)
        self.probe.assert_not_called()

    def test_explicit_review_model_is_not_silently_substituted(self):
        with patch.object(p.subprocess, 'run', return_value=self.run_result()) as run:
            with self.assertRaisesRegex(p.ProviderUnavailable, 'requested OpenAI provider and model'):
                p.chat('Review text', self.dest, self.args, model='review-model')
        command, = run.call_args.args
        self.assertEqual(command[3], 'review-model')
        self.assertFalse(self.dest.exists())

    def test_billing_429_stops_but_transient_429_is_retryable(self):
        for reason, message in [('429 insufficient_quota private-detail', '^AgInTi OpenAI API billing'),
                                ('429 rate limit private-detail', '^APIConnectionError:')]:
            p.PROVIDER_STOP.clear()
            with patch.object(p.subprocess, 'run', return_value=self.run_result(reason)):
                with self.assertRaisesRegex(p.ProviderUnavailable, message) as raised:
                    p.chat('Prompt', self.dest, self.args)
            self.assertNotIn('private-detail', str(raised.exception))
            self.assertTrue(p.PROVIDER_STOP.is_set())

    def test_failed_turn_and_invalid_content_are_not_saved_as_a_response(self):
        for updates, error in [({'stopped': True}, p.ProviderUnavailable),
                               ({'result': '[0]'}, p.InvalidReply)]:
            p.PROVIDER_STOP.clear()
            with patch.object(p.subprocess, 'run', return_value=self.run_result(**updates)):
                with self.assertRaises(error):
                    p.chat('Prompt', self.dest, self.args)
            self.assertFalse(self.dest.exists())

    def test_provider_switch_reuses_existing_title_catalogue(self):
        manifest = self.root / 'manifest.json'
        p.write(manifest, {'books': [{'id': 'demo'}]})
        path = self.root / 'titles/vi.json'
        catalog = {'model': 'gpt-6-luna', 'translations': {'demo': 'Cơ học'}}
        p.write(path, catalog)
        with patch.object(p, 'MANIFEST', manifest), patch.object(p, 'chat') as chat:
            p.ensure_language_titles('vi', self.args)
        chat.assert_not_called()
        self.assertEqual(p.read(path), catalog)


if __name__ == '__main__':
    unittest.main()
