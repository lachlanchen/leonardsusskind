#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python="${TRANSLATION_PYTHON:-python}"
languages=(fr es de zh-Hant ko vi ru ar)

cd "$root"
mkdir -p .translation-work
if [[ -f .translation-work/STOP ]]; then
  printf 'STOP marker exists; remove it explicitly before resuming.\n' >&2
  exit 1
fi
export TRANSLATION_QUOTA_HELPER="${TRANSLATION_QUOTA_HELPER:-$root/scripts/translation_quota.py}"

if [[ $# != 0 ]]; then
  [[ $# == 2 && $1 == --resume-from ]] || exit 2
  case "$2" in fr|es|de|zh-Hant|ko|vi|ru|ar) ;; *) exit 2 ;; esac
  prior=()
  while [[ ${languages[0]} != "$2" ]]; do
    prior+=("${languages[0]}")
    languages=("${languages[@]:1}")
  done
  # A resume may skip only editions both validated locally and linked by the
  # published commit. Do not mistake a finished private cache for a release.
  remotes="$(git remote get-url --push --all origin)"
  [[ -n "$remotes" ]] || exit 1
  while IFS= read -r remote; do
    [[ "$(git ls-remote "$remote" refs/heads/main | cut -f1)" == "$(git rev-parse HEAD)" ]] || exit 1
  done <<< "$remotes"
  PYTHONPATH="$root/scripts" "$python" - "${prior[@]}" <<'PY'
import subprocess
import sys
import polished_translation as p
readme = subprocess.check_output(['git', 'show', 'HEAD:README.md'], text=True)
for lang in sys.argv[1:]:
    for book in p.read(p.MANIFEST)['books']:
        folder = f'translations/{book["id"]}/{lang}'
        if not p.validated_output(book, lang) or f']({folder}/book.pdf)' not in readme:
            raise SystemExit(f'Cannot skip unpublished edition: {folder}')
        subprocess.run(['git', 'cat-file', '-e', f'HEAD:{folder}/book.pdf'], check=True)
        subprocess.run(['git', 'diff', '--quiet', 'HEAD', '--', folder], check=True)
PY
fi

for language in "${languages[@]}"; do
  printf '[%s] Starting %s\n' "$(date -Is)" "$language" | tee -a .translation-work/luna-queue.log
  for repair_round in 0 1 2 3; do
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

    state="$("$python" -c 'import json; print(json.load(open(".translation-work/status.json"))["state"])')"
    [[ "$state" == complete ]] && break
    if [[ "$state" != finished_with_blockers || "$repair_round" == 3 || -e .translation-work/STOP ]]; then
      printf '%s stopped with state=%s after repair round %s.\n' "$language" "$state" "$repair_round" >&2
      exit 1
    fi
    printf '[%s] Repairing %s: sweep %s\n' "$(date -Is)" "$language" "$((repair_round + 1))" | tee -a .translation-work/luna-queue.log
    bash scripts/repair_luna_translation_language.sh "$language" "$((repair_round + 1))"
  done

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
  while IFS= read -r remote; do
    remote_head="$(git ls-remote "$remote" refs/heads/main | cut -f1)"
    [[ "$remote_head" == "$(git rev-parse HEAD)" ]] || {
      printf 'Remote SHA is not synchronized after %s: %s\n' "$language" "$remote" >&2
      exit 1
    }
  done < <(git remote get-url --push --all origin)
  printf '[%s] Completed and published %s\n' "$(date -Is)" "$language" | tee -a .translation-work/luna-queue.log
done
