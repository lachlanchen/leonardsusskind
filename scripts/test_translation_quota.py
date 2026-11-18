import io
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import time
from types import SimpleNamespace
import unittest
from unittest.mock import patch

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

    def test_explicit_server_failure_is_transport_not_quota(self):
        self.assertTrue(q.quota_error('quota endpoint returned HTTP 502').startswith('APIConnectionError:'))

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


if __name__ == '__main__':
    unittest.main()
