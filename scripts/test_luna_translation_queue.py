import os
from pathlib import Path
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest


class LunaQueueTests(unittest.TestCase):
    def setUp(self):
        self.temp = TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'scripts').mkdir()
        (self.root / '.translation-work').mkdir()
        shutil.copy2(Path(__file__).with_name('run_luna_translation_languages.sh'), self.root / 'scripts')
        (self.root / 'scripts/repair_luna_translation_language.sh').write_text(
            'printf "%s %s\\n" "$1" "$2" >>.translation-work/repairs.log\n'
            'touch ".translation-work/repaired-$1"\n')
        self.bin = self.root / 'bin'
        self.bin.mkdir()
        self.executable('python', '''
import json, os
from pathlib import Path
import sys
if sys.argv[1:3] != ['scripts/polished_translation.py', 'run']:
    os.execv(sys.executable, [sys.executable, *sys.argv[1:]])
lang = sys.argv[sys.argv.index('--language') + 1]
work = Path('.translation-work')
with (work / 'runs.log').open('a') as stream:
    stream.write(lang + '\\n')
scenario = os.environ.get('SCENARIO', 'complete')
state = 'complete'
if scenario == 'provider':
    state = 'provider_blocked'
elif scenario == 'always' or scenario == 'once' and not (work / ('repaired-' + lang)).exists():
    state = 'finished_with_blockers'
(work / 'status.json').write_text(json.dumps({'state': state, 'blocked_books': [] if state == 'complete' else ['book']}))
''')
        self.executable('git', '''
import os, sys
args = sys.argv[1:]
if args[:2] == ['remote', 'get-url']:
    print('canonical\\nmirror')
elif args[0] == 'ls-remote':
    print(('stale' if os.environ.get('MISMATCH') else 'abc123') + '\\trefs/heads/main')
elif args[0] == 'rev-parse':
    print('abc123')
elif args[0] != 'status':
    raise SystemExit('Unexpected git call: ' + str(args))
''')

    def executable(self, name, code):
        path = self.bin / name
        path.write_text('#!' + sys.executable + '\n' + code)
        path.chmod(0o700)

    def run_queue(self, **overrides):
        env = {**os.environ, 'PATH': str(self.bin) + os.pathsep + os.environ['PATH'],
               'TRANSLATION_PYTHON': str(self.bin / 'python'), **overrides}
        return subprocess.run(['bash', 'scripts/run_luna_translation_languages.sh'],
                              cwd=self.root, env=env, capture_output=True, text=True, timeout=30)

    def test_all_languages_finish_in_order(self):
        result = self.run_queue()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((self.root / '.translation-work/runs.log').read_text().splitlines(),
                         ['fr', 'es', 'de', 'zh-Hant', 'ko', 'vi', 'ru', 'ar'])

    def test_blocked_language_gets_repaired_before_the_next_language(self):
        result = self.run_queue(SCENARIO='once')
        self.assertEqual(result.returncode, 0, result.stderr)
        runs = (self.root / '.translation-work/runs.log').read_text().splitlines()
        self.assertEqual(runs[:4], ['fr', 'fr', 'es', 'es'])
        self.assertEqual(len((self.root / '.translation-work/repairs.log').read_text().splitlines()), 8)

    def test_repairs_stop_after_three_sweeps(self):
        result = self.run_queue(SCENARIO='always')
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual((self.root / '.translation-work/runs.log').read_text().splitlines(), ['fr'] * 4)
        self.assertEqual((self.root / '.translation-work/repairs.log').read_text().splitlines(),
                         ['fr 1', 'fr 2', 'fr 3'])

    def test_provider_failure_does_not_launch_a_repair(self):
        result = self.run_queue(SCENARIO='provider')
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((self.root / '.translation-work/repairs.log').exists())

    def test_stop_marker_is_not_removed(self):
        stop = self.root / '.translation-work/STOP'
        stop.touch()
        result = self.run_queue()
        self.assertNotEqual(result.returncode, 0)
        self.assertTrue(stop.exists())
        self.assertFalse((self.root / '.translation-work/runs.log').exists())

    def test_remote_mismatch_prevents_advancing(self):
        result = self.run_queue(MISMATCH='1')
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual((self.root / '.translation-work/runs.log').read_text().splitlines(), ['fr'])


if __name__ == '__main__':
    unittest.main()
