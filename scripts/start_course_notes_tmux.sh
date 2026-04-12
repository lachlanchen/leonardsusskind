#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: scripts/start_course_notes_tmux.sh [options]

Starts a tmux session for transcript-derived note generation.

Defaults:
- supplementary courses before core courses
- only fully transcribed courses
- model gpt-5.4 with xhigh reasoning
- shared Codex writing session scope defaults to global reuse across lectures

Options:
  --session <name>         tmux session name (default: susskind-notes)
  --course <rel>           restrict to one course rel path
  --model <name>           note-writing model
  --reasoning <level>      low|medium|high|xhigh
  --session-scope <scope>  global|course|lecture
  --max-lectures <n>       stop after n lectures
  --allow-partial-course   allow the selected course even if incomplete
  --kill                   kill existing session and recreate
  --no-attach              do not attach after startup
  -h, --help               show help
USAGE
}

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
session="susskind-notes"
course=""
model="${NOTE_MODEL:-gpt-5.4}"
reasoning="${NOTE_REASONING:-xhigh}"
session_scope="${NOTE_CODEX_SESSION_SCOPE:-global}"
max_lectures=0
allow_partial_course=0
kill_existing=0
attach=1

while [[ $# -gt 0 ]]; do
  case "$1" in
    --session)
      session="${2:-}"
      shift 2
      ;;
    --course)
      course="${2:-}"
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
    --session-scope)
      session_scope="${2:-}"
      shift 2
      ;;
    --max-lectures)
      max_lectures="${2:-0}"
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

if ! command -v tmux >/dev/null 2>&1; then
  echo "tmux not found." >&2
  exit 1
fi

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

cmd=(bash ./scripts/process_course_notes_one_by_one.sh --model "$model" --reasoning "$reasoning")
cmd+=(--session-scope "$session_scope")
if [[ -n "$course" ]]; then
  cmd+=(--course "$course")
fi
if [[ "$max_lectures" -gt 0 ]]; then
  cmd+=(--max-lectures "$max_lectures")
fi
if [[ "$allow_partial_course" -eq 1 ]]; then
  cmd+=(--allow-partial-course)
fi

tmux new-session -d -s "$session" -c "$repo_root" "bash -lc 'cd \"$repo_root\" && ${cmd[*]} 2>&1 | tee \"$log_path\"'"
tmux rename-window -t "$session:0" "notes"
tmux set-option -t "$session" -g mouse on

echo "tmux session: $session"
echo "log: $log_path"
echo "attach: tmux attach -t $session"

if [[ "$attach" -eq 1 ]]; then
  exec tmux attach -t "$session"
fi
