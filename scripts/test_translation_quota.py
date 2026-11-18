import io
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import time
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

import translation_quota as q


class TranslationQuotaTests(unittest.TestCase):
    def test_uses_most_depleted_codex_window(self):
        result = q.normalize({'rateLimitsByLimitId': {
            'codex': {'primary': {'usedPercent': 52}, 'secondary': {'usedPercent': 80}},
            'other': {'primary': {'usedPercent': 99}},
        }})
        self.assertTrue(result['ok'])
        self.assertEqual(result['remaining_percent'], 20)

    def test_invalid_or_missing_windows_fail_closed(self):
        for value in (None, True, float('nan')):
            with self.assertRaises(ValueError):
                q.normalize({'rateLimits': {'primary': {'usedPercent': value}}})

    def test_existing_credit_evidence_is_preserved_without_spending(self):
        result = q.normalize({'rateLimits': {
            'primary': {'usedPercent': 100},
            'credits': {'hasCredits': True, 'unlimited': False, 'balance': '12.5'}}})
        self.assertEqual(result['credits'], {'has_credits': True, 'unlimited': False, 'balance': '12.5'})
        self.assertEqual(result['remaining_percent'], 0)

    def test_explicit_server_failure_is_transport_not_quota(self):
        self.assertTrue(q.quota_error('quota endpoint returned HTTP 502').startswith('APIConnectionError:'))
        self.assertTrue(q.quota_error('failed to fetch codex rate limits: error sending request for url').startswith('APIConnectionError:'))

    def test_missing_launcher_is_a_transport_failure(self):
        with patch.object(q.subprocess, 'Popen', side_effect=FileNotFoundError):
            with self.assertRaisesRegex(RuntimeError, 'APIConnectionError: quota app-server launcher'):
                q.read_limits()

    def test_auth_and_exhaustion_cannot_enter_transport_retries(self):
        for message in ('HTTP 403 connection refused', 'quota exhausted HTTP 429', 'authentication failed'):
            self.assertFalse(q.quota_error(message).startswith('APIConnectionError:'))

    def test_recent_success_uses_cache_without_an_rpc(self):
        with TemporaryDirectory() as tmp, patch.object(q, 'WORK', Path(tmp)):
            payload = {'ok': True, 'remaining_percent': 48, 'observed_at_epoch': time.time()}
            (q.WORK / 'quota-upstream.json').write_text(json.dumps(payload))
            with patch.object(q, 'read_limits') as rpc:
                self.assertEqual(q.status(), payload)
            rpc.assert_not_called()

    def test_failed_probe_does_not_return_or_overwrite_stale_success(self):
        with TemporaryDirectory() as tmp, patch.object(q, 'WORK', Path(tmp)):
            payload = {'ok': True, 'remaining_percent': 48, 'observed_at_epoch': time.time() - 181}
            cache = q.WORK / 'quota-upstream.json'
            cache.write_text(json.dumps(payload))
            with patch.object(q, 'read_limits', side_effect=RuntimeError('APIConnectionError: timed out')) as rpc:
                self.assertFalse(q.status()['ok'])
            self.assertEqual(json.loads(cache.read_text()), payload)
            rpc.assert_called_once()

    def test_account_initialization_precedes_rate_limit_read(self):
        class Recorder(io.StringIO):
            def close(self):
                pass

        stream = Recorder()
        replies = [{'id': 1, 'result': {}}, {'id': 2, 'result': {'account': {'type': 'chatgpt'}}},
                   {'id': 3, 'result': {'rateLimits': {'primary': {'usedPercent': 52}}}}]
        process = SimpleNamespace(stdin=stream, stdout=io.StringIO('\n'.join(json.dumps(r) for r in replies)),
                                  wait=lambda timeout: 0)
        with patch.object(q.subprocess, 'Popen', return_value=process):
            self.assertIn('rateLimits', q.read_limits())
        requests = [json.loads(line) for line in stream.getvalue().splitlines()]
        self.assertEqual([r['method'] for r in requests],
                         ['initialize', 'initialized', 'account/read', 'account/rateLimits/read'])
        self.assertFalse(requests[2]['params']['refreshToken'])

    def test_successful_quota_survives_slow_probe_shutdown(self):
        replies = [{'id': 1, 'result': {}}, {'id': 2, 'result': {}},
                   {'id': 3, 'result': {'rateLimits': {'primary': {'usedPercent': 52}}}}]
        process = SimpleNamespace(pid=12345, stdin=io.StringIO(),
                                  stdout=io.StringIO('\n'.join(json.dumps(r) for r in replies)),
                                  wait=Mock(side_effect=[q.subprocess.TimeoutExpired('codex', 5),
                                                         q.subprocess.TimeoutExpired('codex', 5), 0]))
        with patch.object(q.subprocess, 'Popen', return_value=process) as launch, \
             patch.object(q.os, 'killpg') as kill:
            self.assertIn('rateLimits', q.read_limits())
        self.assertTrue(launch.call_args.kwargs['start_new_session'])
        self.assertEqual([call.args for call in kill.call_args_list],
                         [(12345, q.signal.SIGTERM), (12345, q.signal.SIGKILL)])

    def test_probe_cleanup_does_not_mask_an_auth_failure(self):
        replies = [{'id': 1, 'result': {}}, {'id': 2, 'result': {}},
                   {'id': 3, 'error': {'message': 'HTTP 403 authentication failed'}}]
        process = SimpleNamespace(pid=12345, stdin=io.StringIO(),
                                  stdout=io.StringIO('\n'.join(json.dumps(r) for r in replies)),
                                  wait=Mock(side_effect=[q.subprocess.TimeoutExpired('codex', 5),
                                                         q.subprocess.TimeoutExpired('codex', 5), 0]))
        with patch.object(q.subprocess, 'Popen', return_value=process), patch.object(q.os, 'killpg'):
            with self.assertRaisesRegex(RuntimeError, 'Quota telemetry rejected: HTTP 403'):
                q.read_limits()


if __name__ == '__main__':
    unittest.main()
