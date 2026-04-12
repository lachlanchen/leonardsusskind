#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: scripts/start_course_notes_monitor_tmux.sh [options]

Starts a tmux session that periodically checks the notes worker and restarts it
when needed.

Defaults:
- monitor session: susskind-notes-monitor
- target notes session: susskind-notes
- interval: 1800 seconds
- model: gpt-5.4-mini
- reasoning: low

Options:
  --session <name>              monitor tmux session name (default: susskind-notes-monitor)
  --target-session <name>       target notes tmux session (default: susskind-notes)
  --interval <seconds>          monitor interval (default: 1800)
  --model <name>                Codex model for monitor checks
  --reasoning <level>           low|medium|high|xhigh
  --course <rel>                optional course restriction when restarting notes
  --notes-session-scope <scope> global|course|lecture
  --allow-partial-course        pass through on restart
  --kill                        kill existing monitor session and recreate
  --no-attach                   do not attach after startup
  -h, --help                    show help
USAGE
}

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
session="susskind-notes-monitor"
target_session="susskind-notes"
interval="${NOTE_MONITOR_INTERVAL:-1800}"
model="${NOTE_MONITOR_MODEL:-gpt-5.4-mini}"
reasoning="${NOTE_MONITOR_REASONING:-low}"
course=""
notes_session_scope="${NOTE_CODEX_SESSION_SCOPE:-global}"
allow_partial_course=0
kill_existing=0
attach=1

while [[ $# -gt 0 ]]; do
  case "$1" in
    --session)
      session="${2:-}"
      shift 2
      ;;
    --target-session)
      target_session="${2:-}"
      shift 2
      ;;
    --interval)
      interval="${2:-1800}"
      shift 2
      ;;
    --model)
      model="${2:-}"
      shift 2
      ;;
    --reasoning)
      reasoning="${2:-}"
      shift 2
      ;;
    --course)
      course="${2:-}"
      shift 2
      ;;
    --notes-session-scope)
      notes_session_scope="${2:-global}"
      shift 2
      ;;
    --allow-partial-course)
      allow_partial_course=1
      shift
      ;;
    --kill)
      kill_existing=1
      shift
      ;;
    --no-attach)
      attach=0
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 1
      ;;
  esac
done

log_dir="$repo_root/.lecture-notes-work/logs"
mkdir -p "$log_dir"
timestamp="$(date +%Y%m%d_%H%M%S)"
log_path="$log_dir/${session}_${timestamp}.log"

if tmux has-session -t "$session" 2>/dev/null; then
  if [[ "$kill_existing" -eq 1 ]]; then
    tmux kill-session -t "$session"
  else
    if [[ "$attach" -eq 1 ]]; then
      exec tmux attach -t "$session"
    fi
    echo "tmux session already running: $session"
    exit 0
  fi
fi

cmd=(bash ./scripts/monitor_course_notes.sh --session "$target_session" --interval "$interval" --model "$model" --reasoning "$reasoning" --notes-session-scope "$notes_session_scope")
if [[ -n "$course" ]]; then
  cmd+=(--course "$course")
fi
if [[ "$allow_partial_course" -eq 1 ]]; then
  cmd+=(--allow-partial-course)
fi

tmux new-session -d -s "$session" -c "$repo_root" "bash -lc 'cd \"$repo_root\" && NOTE_MONITOR_TMUX_NAME=\"$session\" ${cmd[*]} 2>&1 | tee \"$log_path\"'"
tmux rename-window -t "$session:0" "monitor"
tmux set-option -t "$session" -g mouse on

echo "tmux session: $session"
echo "log: $log_path"
echo "attach: tmux attach -t $session"

if [[ "$attach" -eq 1 ]]; then
  exec tmux attach -t "$session"
fi
