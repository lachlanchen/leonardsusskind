#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: scripts/monitor_course_notes.sh [options]

Periodically monitors the course-note tmux worker, asks Codex for a status/action
decision, and restarts the worker when it has exited or stalled.

Defaults:
- target notes session: susskind-notes
- interval: 1800 seconds
- monitor model: gpt-5.4-mini
- monitor reasoning: low

Options:
  --session <name>              target notes tmux session (default: susskind-notes)
  --interval <seconds>          monitor interval (default: 1800)
  --model <name>                Codex model for monitor checks
  --reasoning <level>           low|medium|high|xhigh
  --course <rel>                optional course restriction when restarting notes
  --notes-session-scope <scope> global|course|lecture (default: global)
  --allow-partial-course        pass through on restart
  -h, --help                    show help
USAGE
}

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
session="susskind-notes"
interval="${NOTE_MONITOR_INTERVAL:-1800}"
model="${NOTE_MONITOR_MODEL:-gpt-5.4-mini}"
reasoning="${NOTE_MONITOR_REASONING:-low}"
course=""
notes_session_scope="${NOTE_CODEX_SESSION_SCOPE:-global}"
allow_partial_course=0
monitor_tmux_name="${NOTE_MONITOR_TMUX_NAME:-susskind-notes-monitor}"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --session)
      session="${2:-}"
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

case "$reasoning" in
  low|medium|high|xhigh) ;;
  *)
    echo "Invalid reasoning level: $reasoning" >&2
    exit 1
    ;;
esac

case "$notes_session_scope" in
  global|course|lecture) ;;
  *)
    echo "Invalid notes session scope: $notes_session_scope" >&2
    exit 1
    ;;
esac

if ! [[ "$interval" =~ ^[0-9]+$ ]] || [[ "$interval" -lt 10 ]]; then
  echo "Interval must be an integer >= 10 seconds." >&2
  exit 1
fi

cd "$repo_root"

monitor_root="$repo_root/.lecture-notes-work/monitor/$session"
mkdir -p "$monitor_root"
prompt_file="$monitor_root/monitor.prompt.txt"
decision_file="$monitor_root/monitor.decision.json"
history_log="$monitor_root/monitor.history.log"
monitor_session_file="$monitor_root/monitor.session_id"
monitor_session_doc="$monitor_root/monitor.session.md"
source_root="/home/lachlan/ProjectsLFS/YoutubeDownloader/downloads/PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG"

print_header() {
  printf '[%s] %s\n' "$(date --iso-8601=seconds)" "$1" | tee -a "$history_log"
}

latest_log_path() {
  ls -1t "$repo_root/.lecture-notes-work/logs/${session}"_*.log 2>/dev/null | head -n1 || true
}

session_exists() {
  tmux has-session -t "$session" 2>/dev/null
}

session_process_tree() {
  local pane_pid sid
  pane_pid="$(tmux list-panes -t "$session" -F '#{pane_pid}' 2>/dev/null | head -n1 || true)"
  [[ -n "$pane_pid" ]] || return 0
  sid="$(ps -o sid= -p "$pane_pid" 2>/dev/null | tr -d ' ' || true)"
  [[ -n "$sid" ]] || return 0
  ps -o pid,ppid,stat,etime,cmd --forest -g "$sid" 2>/dev/null || true
}

notes_active() {
  local tree
  tree="$(session_process_tree)"
  grep -E -q 'generate_course_notes\.py|codex exec|pdflatex|ffmpeg .*frame_probe|pdfunite' <<<"$tree"
}

next_pending() {
  local cmd
  cmd=(python3 scripts/generate_course_notes.py --repo-root "$repo_root" --source-root "$source_root" --print-next)
  if [[ -n "$course" ]]; then
    cmd+=(--course "$course")
  fi
  if [[ "$allow_partial_course" -eq 1 ]]; then
    cmd+=(--allow-partial-course)
  fi
  "${cmd[@]}" 2>/dev/null || true
}

build_fallback_decision() {
  local session_present="$1"
  local active="$2"
  local next_rel="$3"
  local latest_log="$4"
  local log_tail="$5"

  if [[ -z "$next_rel" ]] && grep -q "No eligible pending lectures remain." <<<"$log_tail"; then
    cat <<'EOF'
{"status":"finished","action":"done","reason":"No eligible pending lectures remain.","summary":"The note queue is complete."}
EOF
    return
  fi

  if [[ "$session_present" == "1" && "$active" == "1" ]]; then
    cat <<'EOF'
{"status":"healthy","action":"none","reason":"The tmux session exists and active note-generation subprocesses are running.","summary":"The worker is healthy."}
EOF
    return
  fi

  if [[ "$session_present" == "1" && "$active" == "0" && -n "$next_rel" ]]; then
    cat <<EOF
{"status":"stalled","action":"restart_kill","reason":"The tmux session exists but no active note-generation subprocesses were found.","summary":"Restart the note worker on the next pending lecture: $next_rel."}
EOF
    return
  fi

  if [[ "$session_present" == "0" && -n "$next_rel" ]]; then
    cat <<EOF
{"status":"crashed","action":"restart","reason":"The tmux session is missing while pending lectures remain.","summary":"Restart the note worker on the next pending lecture: $next_rel."}
EOF
    return
  fi

  cat <<'EOF'
{"status":"unknown","action":"none","reason":"State is inconclusive.","summary":"No automatic action taken."}
EOF
}

extract_json_field() {
  local file="$1"
  local field="$2"
  python3 - "$file" "$field" <<'PY'
import json
import sys

path, field = sys.argv[1], sys.argv[2]
with open(path, encoding="utf-8", errors="replace") as handle:
    data = json.load(handle)
value = data.get(field, "")
if isinstance(value, str):
    print(value)
PY
}

run_monitor_prompt() {
  local session_present="$1"
  local active="$2"
  local next_rel="$3"
  local latest_log="$4"
  local log_tail="$5"
  local process_tree="$6"
  local git_status="$7"

  cat > "$prompt_file" <<EOF
You are monitoring a tmux-based lecture-note writing daemon for this repository.

Return JSON only with this schema:
{
  "status": "healthy|finished|stalled|crashed|unknown",
  "action": "none|restart|restart_kill|done|needs_human",
  "reason": "short explanation",
  "summary": "short operator-facing summary"
}

Rules:
- If the target tmux session exists and active note-generation subprocesses are present, use \`status="healthy"\` and \`action="none"\`.
- If the latest log shows that no eligible pending lectures remain and the next-pending lecture is empty, use \`status="finished"\` and \`action="done"\`.
- If the tmux session is missing and there is a next pending lecture, prefer \`action="restart"\`.
- If the tmux session exists but no active note-generation subprocesses are present and there is a next pending lecture, prefer \`action="restart_kill"\`.
- Only use \`needs_human\` if the provided state clearly shows an unsafe repository condition that should block auto-resume.
- Ignore untracked partial outputs under \`generated_course_notes/\` when deciding whether restart is safe.
- Prefer resuming progress over conservative inaction when the state is otherwise normal.

Current state:
- target tmux session: $session
- session_exists: $session_present
- active_note_processes: $active
- next_pending_lecture: ${next_rel:-<none>}
- latest_log: ${latest_log:-<none>}

Git status:
$git_status

Process tree:
$process_tree

Latest log tail:
$log_tail
EOF

  if NOTE_TMUX_SESSION_NAME="$monitor_tmux_name" \
     CODEX_SHARED_SESSION_FILE="$monitor_session_file" \
     CODEX_SHARED_SESSION_DOC_FILE="$monitor_session_doc" \
     NOTE_CODEX_SESSION_SCOPE="global" \
     bash "$repo_root/scripts/codex_prompt_to_file.sh" \
       "$repo_root" \
       "$prompt_file" \
       "$decision_file" \
       "$model" \
       "$reasoning" >/dev/null 2>&1; then
    return 0
  fi

  build_fallback_decision "$session_present" "$active" "$next_rel" "$latest_log" "$log_tail" > "$decision_file"
}

restart_notes() {
  local kill_flag="$1"
  local cmd
  cmd=(./scripts/start_course_notes_tmux.sh --session "$session" --session-scope "$notes_session_scope" --no-attach)
  if [[ -n "$course" ]]; then
    cmd+=(--course "$course")
  fi
  if [[ "$allow_partial_course" -eq 1 ]]; then
    cmd+=(--allow-partial-course)
  fi
  if [[ "$kill_flag" == "1" ]]; then
    cmd+=(--kill)
  fi
  "${cmd[@]}"
}

while true; do
  latest_log="$(latest_log_path)"
  log_tail=""
  if [[ -n "$latest_log" && -f "$latest_log" ]]; then
    log_tail="$(tail -n 120 "$latest_log" 2>/dev/null || true)"
  fi

  next_rel="$(next_pending)"
  session_present=0
  active=0
  process_tree=""
  if session_exists; then
    session_present=1
    process_tree="$(session_process_tree)"
    if notes_active; then
      active=1
    fi
  fi

  git_status="$(git status --short 2>/dev/null || true)"
  run_monitor_prompt "$session_present" "$active" "$next_rel" "$latest_log" "$log_tail" "$process_tree" "$git_status"

  action="$(extract_json_field "$decision_file" action 2>/dev/null || true)"
  status="$(extract_json_field "$decision_file" status 2>/dev/null || true)"
  reason="$(extract_json_field "$decision_file" reason 2>/dev/null || true)"
  summary="$(extract_json_field "$decision_file" summary 2>/dev/null || true)"

  if [[ -z "$action" ]]; then
    build_fallback_decision "$session_present" "$active" "$next_rel" "$latest_log" "$log_tail" > "$decision_file"
    action="$(extract_json_field "$decision_file" action 2>/dev/null || true)"
    status="$(extract_json_field "$decision_file" status 2>/dev/null || true)"
    reason="$(extract_json_field "$decision_file" reason 2>/dev/null || true)"
    summary="$(extract_json_field "$decision_file" summary 2>/dev/null || true)"
  fi

  print_header "Monitor decision: status=${status:-unknown} action=${action:-none} reason=${reason:-n/a}"
  if [[ -n "$summary" ]]; then
    print_header "Summary: $summary"
  fi

  case "$action" in
    restart)
      print_header "Restarting notes tmux session without kill."
      restart_notes 0
      ;;
    restart_kill)
      print_header "Restarting notes tmux session with kill."
      restart_notes 1
      ;;
    done)
      print_header "No pending lecture notes remain. Monitor exiting."
      exit 0
      ;;
    needs_human)
      print_header "Monitor requested human attention. No automatic restart."
      ;;
    *)
      print_header "No action taken."
      ;;
  esac

  sleep "$interval"
done
