#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
session="susskind-luna-translations"

if tmux has-session -t "=$session" 2>/dev/null; then
  printf 'Existing session: %s\n' "$session"
  exit 0
fi
cd "$root"
if [[ $# != 0 ]]; then
  [[ $# == 2 && $1 == --resume-from ]] || exit 2
  case "$2" in fr|es|de|zh-Hant|ko|vi|ru|ar) ;; *) exit 2 ;; esac
fi
status="$(git status --porcelain)"
if [[ $# == 2 && "$status" == ' M README.md' ]]; then
  # The queue may have written progress counters after its last publication.
  python - <<'PY'
import re
import subprocess
from pathlib import Path

marker = r'<!-- polished-translations:start -->.*?<!-- polished-translations:end -->'
before = subprocess.check_output(['git', 'show', 'HEAD:README.md'], text=True)
after = Path('README.md').read_text()
if re.sub(marker, '', before, flags=re.S) != re.sub(marker, '', after, flags=re.S):
    raise SystemExit('Refusing to resume over unrelated README changes')
PY
elif [[ -n "$status" ]]; then
  printf 'Refusing to start from a dirty worktree.\n' >&2
  git -C "$root" status --short >&2
  exit 1
fi
provider="${TRANSLATION_PROVIDER:-codex}"
case "$provider" in
  codex)
    bin="${TRANSLATION_CODEX_BIN:-$(command -v codex)}"
    bin_env="TRANSLATION_CODEX_BIN=$bin"
    ;;
  aginti-openai)
    bin="${TRANSLATION_AGINTI_BIN:-$(command -v aginti)}"
    bin_env="TRANSLATION_AGINTI_BIN=$bin"
    ;;
  *) exit 2 ;;
esac
"$bin" --version >/dev/null
mkdir -p "$root/.translation-work"
bash "$root/scripts/setup_translation_tex.sh"
tmux new-session -d -s "$session" -c "$root" \
  -e "PATH=$PATH" -e "$bin_env" -e "TRANSLATION_PROVIDER=$provider" \
  -e "TRANSLATION_MODEL=${TRANSLATION_MODEL:-}" \
  bash -c 'exec bash scripts/run_luna_translation_languages.sh "$@" >>.translation-work/luna-tmux.log 2>&1' _ "$@"
printf 'Started %s; log: %s/.translation-work/luna-queue.log\n' "$session" "$root"
