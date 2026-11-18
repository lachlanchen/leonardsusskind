#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
session="susskind-luna-translations"

if tmux has-session -t "$session" 2>/dev/null; then
  printf 'Existing session: %s\n' "$session"
  exit 0
fi
if [[ -n "$(git -C "$root" status --porcelain)" ]]; then
  printf 'Refusing to start from a dirty worktree.\n' >&2
  git -C "$root" status --short >&2
  exit 1
fi
codex_bin="${TRANSLATION_CODEX_BIN:-$(command -v codex)}"
"$codex_bin" --version >/dev/null
mkdir -p "$root/.translation-work"
bash "$root/scripts/setup_translation_tex.sh"
tmux new-session -d -s "$session" -c "$root" \
  -e "PATH=$PATH" -e "TRANSLATION_CODEX_BIN=$codex_bin" \
  'bash scripts/run_luna_translation_languages.sh >>.translation-work/luna-tmux.log 2>&1'
printf 'Started %s; log: %s/.translation-work/luna-queue.log\n' "$session" "$root"
