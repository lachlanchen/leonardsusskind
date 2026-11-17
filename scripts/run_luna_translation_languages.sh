#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python="${TRANSLATION_PYTHON:-python}"
languages=(fr es de zh-Hant ko vi ru ar)

cd "$root"
mkdir -p .translation-work
rm -f .translation-work/STOP

for language in "${languages[@]}"; do
  printf '[%s] Starting %s\n' "$(date -Is)" "$language" | tee -a .translation-work/luna-queue.log
  "$python" scripts/polished_translation.py run \
    --provider codex \
    --model gpt-6-luna \
    --review-model gpt-6-luna \
    --reasoning high \
    --codex-timeout 1800 \
    --batch-chars 24000 \
    --workers 5 \
    --language "$language" \
    --publish 2>&1 | tee -a .translation-work/luna-queue.log

  "$python" - "$language" <<'PY'
import json
from pathlib import Path
import sys

status = json.loads(Path('.translation-work/status.json').read_text())
if status.get('state') != 'complete' or status.get('blocked_books'):
    raise SystemExit(f'{sys.argv[1]} did not complete cleanly: {status}')
PY
  if [[ -n "$(git status --porcelain)" ]]; then
    printf 'Translation publication left a dirty worktree after %s.\n' "$language" >&2
    git status --short >&2
    exit 1
  fi
  if [[ "$(git rev-list --count '@{upstream}..HEAD')" != 0 ]]; then
    printf 'Local commits remain unpushed after %s.\n' "$language" >&2
    exit 1
  fi
  printf '[%s] Completed and published %s\n' "$(date -Is)" "$language" | tee -a .translation-work/luna-queue.log
done
