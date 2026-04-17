#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
session_name="${1:-susskind-pocket-rebuild}"
shift || true

log_dir="$repo_root/.lecture-notes-work/logs"
mkdir -p "$log_dir"
timestamp="$(date +%Y%m%d_%H%M%S)"
log_path="$log_dir/${session_name}_${timestamp}.log"
queue_cmd="cd '$repo_root' && bash scripts/rebuild_all_pocket_books.sh"

if [[ "$#" -gt 0 ]]; then
  for arg in "$@"; do
    queue_cmd+=" $(printf '%q' "$arg")"
  done
fi

queue_cmd+=" 2>&1 | tee '$log_path'"

if tmux has-session -t "$session_name" 2>/dev/null; then
  tmux kill-session -t "$session_name"
fi

tmux new-session -d -s "$session_name" "$queue_cmd"

printf 'session=%s\n' "$session_name"
printf 'log=%s\n' "$log_path"
