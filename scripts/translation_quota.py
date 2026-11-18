#!/usr/bin/env python3
"""Read the current Codex account's quota without launching an inference request."""
import argparse
import json
import math
import os
from pathlib import Path
import queue
import re
import signal
import subprocess
import threading
import time


WORK = Path(__file__).resolve().parents[1] / '.translation-work'


def quota_error(message):
    message = str(message)[:1000]
    if not re.search(r'\b(?:401|402|403)\b|unauthor|authenticat|insufficient|quota.*(?:exceed|exhaust|deplet)|usage.limit.*(?:reach|exceed)', message, re.I):
        if re.search(r'\b(?:408|425|429|5\d\d)\b|timed? out|temporar|connect|network|TLS|DNS|unavailable|error sending request', message, re.I):
            return 'APIConnectionError: quota telemetry transport: ' + message
    return 'Quota telemetry rejected: ' + message


def stop_probe(process, reader):
    """Reap only this isolated, read-only probe and its launcher children."""
    def send(sig):
        try:
            if os.name == 'posix':
                os.killpg(process.pid, sig)
            elif sig == signal.SIGTERM:
                process.terminate()
            else:
                process.kill()
        except ProcessLookupError:
            pass

    try:
        process.stdin.close()
    except OSError:
        pass
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        send(signal.SIGTERM)
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            send(signal.SIGKILL)
            process.wait(timeout=5)
    reader.join(timeout=1)
    if reader.is_alive():
        send(signal.SIGKILL)
        reader.join(timeout=2)
    process.stdout.close()


def read_limits(timeout=20):
    try:
        process = subprocess.Popen([os.environ.get('TRANSLATION_CODEX_BIN', 'codex'),
                                    'app-server', '--disable', 'hooks', '--stdio'],
                                   stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=subprocess.DEVNULL, text=True, bufsize=1,
                                   start_new_session=os.name == 'posix')
    except FileNotFoundError as exc:
        raise RuntimeError('APIConnectionError: quota app-server launcher unavailable') from exc
    messages = queue.Queue()

    def receive():
        try:
            for line in process.stdout:
                try:
                    messages.put(json.loads(line))
                except ValueError:
                    continue
        except (OSError, ValueError):
            pass
        finally:
            messages.put(None)

    reader = threading.Thread(target=receive, daemon=True)
    reader.start()

    def request(method, request_id, params):
        process.stdin.write(json.dumps({'id': request_id, 'method': method, 'params': params}) + '\n')
        process.stdin.flush()
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            try:
                response = messages.get(timeout=max(.01, deadline - time.monotonic()))
            except queue.Empty:
                break
            if response is None:
                raise RuntimeError('APIConnectionError: quota app server closed unexpectedly')
            if response.get('id') != request_id:
                continue
            if response.get('error'):
                error = response['error']
                raise RuntimeError(quota_error(error.get('message', error)))
            if not isinstance(response.get('result'), dict):
                raise RuntimeError('Invalid quota RPC payload')
            return response['result']
        raise RuntimeError('APIConnectionError: quota RPC timed out')

    primary_error = None
    try:
        request('initialize', 1, {'clientInfo': {'name': 'translation-quota', 'version': '1.0'},
                                  'capabilities': {'experimentalApi': True}})
        process.stdin.write(json.dumps({'method': 'initialized', 'params': {}}) + '\n')
        process.stdin.flush()
        # Await account initialization before asking for account-scoped limits.
        request('account/read', 2, {'refreshToken': False})
        return request('account/rateLimits/read', 3, {})
    except BaseException as exc:
        primary_error = exc
        raise
    finally:
        try:
            stop_probe(process, reader)
        except (OSError, subprocess.TimeoutExpired) as exc:
            if primary_error is None:
                raise RuntimeError('APIConnectionError: quota probe cleanup timed out') from exc


def normalize(response):
    buckets = response.get('rateLimitsByLimitId') or {}
    snapshot = buckets.get('codex') or response.get('rateLimits') or {}
    windows = [snapshot[name] for name in ('primary', 'secondary')
               if isinstance(snapshot.get(name), dict)
               and type(snapshot[name].get('usedPercent')) in (int, float)
               and math.isfinite(snapshot[name]['usedPercent'])]
    if not windows:
        raise ValueError('Quota response has no metered Codex window')
    observed = time.time()
    credits = snapshot.get('credits') or {}
    return {'ok': True, 'source': 'codex_app_server_account_rate_limits',
            'remaining_percent': min(max(0, min(100, 100 - window['usedPercent'])) for window in windows),
            'observed_at_epoch': observed,
            'credits': {'has_credits': credits.get('hasCredits') is True,
                        'unlimited': credits.get('unlimited') is True,
                        'balance': str(credits.get('balance') or '0')}}


def status(force=False):
    WORK.mkdir(parents=True, exist_ok=True)
    path = WORK / 'quota-upstream.json'
    try:
        cached = json.loads(path.read_text()) if path.exists() else {}
    except ValueError:
        cached = {}
    if not force and cached.get('ok') and 0 <= time.time() - cached.get('observed_at_epoch', 0) < 180:
        return cached
    try:
        data = normalize(read_limits())
    except Exception as exc:
        return {'ok': False, 'error': str(exc), 'observed_at_epoch': time.time()}
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(data) + '\n')
    temporary.replace(path)
    return data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', nargs='?', choices=['quota', 'status', 'probe'], default='status')
    parser.add_argument('--probe', action='store_true')
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()
    data = status(force=args.probe or args.command == 'probe')
    print(json.dumps(data))
    return 0 if data.get('ok') else 1


if __name__ == '__main__':
    raise SystemExit(main())
