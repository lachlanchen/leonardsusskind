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
  --model <name>            codex model (default: NOTE_MODEL or gpt-5.3-codex-spark)
  --reasoning <level>       low|medium|high|xhigh (default: NOTE_REASONING or high)
  --max-lectures <n>        stop after n generated lectures
  --allow-partial-course    allow a specific course even if transcripts are incomplete
  -h, --help                show help
USAGE
}

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_root="/home/lachlan/ProjectsLFS/YoutubeDownloader/downloads/PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG"
model="${NOTE_MODEL:-gpt-5.3-codex-spark}"
reasoning="${NOTE_REASONING:-xhigh}"
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

cd "$repo_root"

processed=0
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

  rel_no_ext="${next_rel%.md}"
  bash ./scripts/codex_commit_push.sh \
    "$repo_root" \
    "Add generated notes for ${rel_no_ext}" \
    generated_course_notes

  processed=$((processed + 1))
  if [[ "$max_lectures" -gt 0 && "$processed" -ge "$max_lectures" ]]; then
    echo "Reached max lecture limit: $max_lectures"
    exit 0
  fi
done
