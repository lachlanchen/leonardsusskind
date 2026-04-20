#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
session="${README_I18N_TMUX_SESSION:-readme-i18n-sync}"
attach=0
replace=0
langs=()

usage() {
  cat <<'EOF'
Usage: scripts/start_readme_translation_tmux.sh [options]

Starts a tmux session that syncs i18n README translations from the root README.

Options:
  --session <name>   tmux session name (default: readme-i18n-sync)
  --lang <code>      limit run to one language; repeatable
  --attach           attach after launch
  --replace          kill an existing session with the same name first
  -h, --help         show this help
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --session)
      session="$2"
      shift 2
      ;;
    --lang)
      langs+=("$2")
      shift 2
      ;;
    --attach)
      attach=1
      shift
      ;;
    --replace)
      replace=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 1
      ;;
  esac
done

if ! command -v tmux >/dev/null 2>&1; then
  echo "tmux not found." >&2
  exit 1
fi

work_root="${README_I18N_WORK_ROOT:-$repo_root/.auto-readme-work/readme-i18n}"
mkdir -p "$work_root/logs"
log_path="$work_root/logs/${session}_$(date +%Y%m%d_%H%M%S).log"

if tmux has-session -t "$session" 2>/dev/null; then
  if [[ "$replace" == "1" ]]; then
    tmux kill-session -t "$session"
  else
    echo "tmux session already running: $session"
    echo "attach: tmux attach -t $session"
    exit 0
  fi
fi

lang_args=""
for lang in "${langs[@]}"; do
  lang_args+=" --lang $(printf '%q' "$lang")"
done

tmux_cmd="cd $(printf '%q' "$repo_root") && export NOTE_TMUX_SESSION_NAME=$(printf '%q' "$session") && bash $(printf '%q' "$repo_root/scripts/sync_readme_translations.sh")${lang_args} 2>&1 | tee $(printf '%q' "$log_path")"

tmux new-session -d -s "$session" -c "$repo_root" "bash -lc $(
  printf '%q' "$tmux_cmd"
)"
tmux rename-window -t "$session:0" "readme-i18n"
tmux set-option -t "$session" -g mouse on

echo "tmux session: $session"
echo "log: $log_path"
echo "attach: tmux attach -t $session"

if [[ "$attach" == "1" ]]; then
  exec tmux attach -t "$session"
fi
