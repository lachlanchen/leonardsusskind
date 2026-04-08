#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
session_name="${1:-susskind-transcribe}"

cd "$repo_root"
mkdir -p transcription_logs

if tmux has-session -t "$session_name" 2>/dev/null; then
  echo "Session already exists: $session_name"
  tmux list-panes -t "$session_name" -F '#S:#I.#P #{pane_current_command}'
  exit 0
fi

log_file="transcription_logs/${session_name}_$(date +%Y%m%d_%H%M%S).log"
tmux new-session -d -s "$session_name" "cd '$repo_root' && bash './scripts/process_videos_one_by_one.sh' 2>&1 | tee '$log_file'"

echo "Started tmux session: $session_name"
echo "Log file: $log_file"
echo "Attach with: tmux attach -t $session_name"
