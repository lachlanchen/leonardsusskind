#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
video2book_root="${VIDEO2BOOK_ROOT:-/home/lachlan/ProjectsLFS/Video2Book}"
nutstore_root="${NUTSTORE_ROOT:-/home/lachlan/Nutstore Files/Projects/LazyingArtBooks}"

course=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --repo-root)
      repo_root="${2:-}"
      shift 2
      ;;
    --course)
      course="${2:-}"
      shift 2
      ;;
    *)
      echo "Unknown option: $1" >&2
      exit 1
      ;;
  esac
done

if [[ -z "$course" ]]; then
  echo "Missing --course" >&2
  exit 1
fi

hardlink_or_copy() {
  local src="$1"
  local dst="$2"
  mkdir -p "$(dirname "$dst")"
  rm -f "$dst"
  if ! ln "$src" "$dst" 2>/dev/null; then
    cp -f "$src" "$dst"
  fi
}

bash "$repo_root/scripts/publish_generated_course_pdf.sh" --repo-root "$repo_root" --course "$course"

bash "$video2book_root/scripts/export_course_pocket_pdfs.sh" \
  --host-root "$repo_root" \
  --course "$course" \
  --font-mode onepointtwo \
  --output-dir "$repo_root/all_notes/pocket_books_1_2x" \
  --suffix pocket_1_2x \
  --nutstore-dir "$nutstore_root/pocket_books_1_2x"

mapfile -t meta < <(python3 - "$repo_root" "$course" <<'PY'
from pathlib import Path
import importlib.util
import sys

repo_root = Path(sys.argv[1])
course_rel = sys.argv[2]
module_path = repo_root / "scripts" / "publish_generated_course_pdf.py"
spec = importlib.util.spec_from_file_location("publish_generated_course_pdf", module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
print(module.course_filename(course_rel))
print(module.root_track_dir(course_rel))
print(Path(course_rel).parts[-1])
PY
)

filename="${meta[0]}"
root_track_dir="${meta[1]}"
run_name="${meta[2]}"
pocket_name="${filename%.pdf}_pocket_1_2x.pdf"
pocket_src="$repo_root/all_notes/pocket_books_1_2x/$pocket_name"
pocket_dst="$repo_root/$root_track_dir/$run_name/$pocket_name"
root_pdf="$repo_root/$root_track_dir/$run_name/$filename"
course_pdf="generated_course_notes/$course/course.pdf"

hardlink_or_copy "$pocket_src" "$pocket_dst"

printf 'published onepointtwo pocket -> %s\n' "$pocket_dst"

bash "$video2book_root/scripts/codex_commit_push.sh" \
  "$repo_root" \
  "Publish pocket overflow outputs for $course" \
  "$course_pdf" \
  "${root_track_dir}/${run_name}/${filename}" \
  "${root_track_dir}/${run_name}/${pocket_name}" \
  "all_notes/${filename}" \
  "all_notes/pocket_books_1_2x/${pocket_name}"
