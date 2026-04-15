#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
tmux_name="${LAZYINGART_BOOKS_TMUX_NAME:-susskind-books-sync}"
interval="${LAZYINGART_BOOKS_SYNC_INTERVAL:-1800}"
log_root="$repo_root/.books-sync-work/logs"
mkdir -p "$log_root"
timestamp="$(date +%Y%m%d_%H%M%S)"
log_file="$log_root/${tmux_name}_${timestamp}.log"

kill_session=0
attach=1

while [[ $# -gt 0 ]]; do
  case "$1" in
    --kill)
      kill_session=1
      shift
      ;;
    --no-attach)
      attach=0
      shift
      ;;
    --interval)
      interval="${2:-1800}"
      shift 2
      ;;
    *)
      echo "Unknown option: $1" >&2
      exit 1
      ;;
  esac
done

if [[ "$kill_session" -eq 1 ]] && tmux has-session -t "$tmux_name" 2>/dev/null; then
  tmux kill-session -t "$tmux_name"
fi

if tmux has-session -t "$tmux_name" 2>/dev/null; then
  echo "tmux session already running: $tmux_name"
else
  tmux new-session -d -s "$tmux_name" \
    "cd \"$repo_root\" && bash ./scripts/monitor_lazyingart_books_sync.sh --interval \"$interval\" 2>&1 | tee \"$log_file\""
  echo "tmux session: $tmux_name"
  echo "log: $log_file"
fi

echo "attach: tmux attach -t $tmux_name"
if [[ "$attach" -eq 1 ]]; then
  exec tmux attach -t "$tmux_name"
fi
