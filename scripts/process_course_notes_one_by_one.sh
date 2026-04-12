#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: scripts/process_course_notes_one_by_one.sh [options]

Generates transcript-derived course notes lecture by lecture.

Default behavior:
- only process courses whose markdown and subtitle coverage matches the source videos
- process supplementary courses first, then core courses
- finish one eligible course before moving to the next

Options:
  --course <rel>            restrict to one course rel path
  --source-root <path>      source video root
  --model <name>            codex model (default: NOTE_MODEL or gpt-5.4)
  --reasoning <level>       low|medium|high|xhigh (default: NOTE_REASONING or xhigh)
  --session-scope <scope>   shared Codex session scope: global|course|lecture
  --max-lectures <n>        stop after n generated lectures
  --allow-partial-course    allow a specific course even if transcripts are incomplete
  -h, --help                show help
USAGE
}

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_root="/home/lachlan/ProjectsLFS/YoutubeDownloader/downloads/PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG"
model="${NOTE_MODEL:-gpt-5.4}"
reasoning="${NOTE_REASONING:-xhigh}"
session_scope="${NOTE_CODEX_SESSION_SCOPE:-global}"
shared_session_file="${NOTE_CODEX_SESSION_FILE:-$repo_root/.lecture-notes-work/codex_sessions/susskind-notes.session_id}"
shared_session_doc="${NOTE_CODEX_SESSION_DOC_FILE:-$repo_root/.lecture-notes-work/codex_sessions/susskind-notes.session.md}"
course=""
max_lectures=0
allow_partial_course=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --course)
      course="${2:-}"
      shift 2
      ;;
    --source-root)
      source_root="${2:-}"
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

case "$session_scope" in
  global|course|lecture) ;;
  *)
    echo "Invalid session scope: $session_scope" >&2
    exit 1
    ;;
esac

cd "$repo_root"
mkdir -p "$(dirname "$shared_session_file")"
export CODEX_SHARED_SESSION_FILE="$shared_session_file"
export CODEX_SHARED_SESSION_DOC_FILE="$shared_session_doc"
export CODEX_COMMIT_MODEL="${CODEX_COMMIT_MODEL:-$model}"
export NOTE_TMUX_SESSION_NAME="${NOTE_TMUX_SESSION_NAME:-susskind-notes}"
export NOTE_CODEX_SESSION_SCOPE="$session_scope"

echo "Using shared Codex session file: $CODEX_SHARED_SESSION_FILE"
echo "Documenting shared Codex session at: $CODEX_SHARED_SESSION_DOC_FILE"
echo "Shared Codex session scope: $session_scope"
if [[ -s "$CODEX_SHARED_SESSION_FILE" ]]; then
  echo "Reusing Codex session id: $(tr -d '[:space:]' < "$CODEX_SHARED_SESSION_FILE")"
fi

processed=0
last_session_key=""
while true; do
  next_cmd=(python3 scripts/generate_course_notes.py --repo-root "$repo_root" --source-root "$source_root" --print-next)
  if [[ -n "$course" ]]; then
    next_cmd+=(--course "$course")
  fi
  if [[ "$allow_partial_course" -eq 1 ]]; then
    next_cmd+=(--allow-partial-course)
  fi
  next_rel="$("${next_cmd[@]}")"

  if [[ -z "$next_rel" ]]; then
    echo "No eligible pending lectures remain."
    exit 0
  fi

  echo "Generating notes for $next_rel"
  echo "Using transcript source: markdown/$next_rel"
  lecture_key="${next_rel%.md}"
  case "$session_scope" in
    global)
      session_key="global"
      ;;
    course)
      session_key="$(dirname "$next_rel")"
      ;;
    lecture)
      session_key="$lecture_key"
      ;;
  esac
  if [[ "$session_scope" != "global" && "$session_key" != "$last_session_key" ]]; then
    rm -f "$CODEX_SHARED_SESSION_FILE" "$CODEX_SHARED_SESSION_DOC_FILE"
    echo "Reset shared Codex session for $session_scope: $session_key"
  fi
  last_session_key="$session_key"
  gen_cmd=(
    python3 scripts/generate_course_notes.py
    --repo-root "$repo_root"
    --source-root "$source_root"
    --lecture "$next_rel"
    --model "$model"
    --reasoning "$reasoning"
  )
  if [[ "$allow_partial_course" -eq 1 ]]; then
    gen_cmd+=(--allow-partial-course)
  fi
  "${gen_cmd[@]}"

  processed=$((processed + 1))
  if [[ "$max_lectures" -gt 0 && "$processed" -ge "$max_lectures" ]]; then
    echo "Reached max lecture limit: $max_lectures"
    exit 0
  fi
done
