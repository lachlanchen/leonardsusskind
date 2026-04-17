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

validate_pocket_pdf_text() {
  local pdf_path="$1"
  python3 - "$pdf_path" <<'PY'
from pathlib import Path
import re
import subprocess
import sys

pdf_path = Path(sys.argv[1])
text = subprocess.run(
    ["pdftotext", "-layout", str(pdf_path), "-"],
    check=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
).stdout

bad_pattern = re.compile(r"(?:footnotesize|scriptsize|normalsize|ootnotesize|ormalsize|criptsize)")
match = bad_pattern.search(text)
if match:
    line = text[max(0, match.start() - 120): match.start() + 120].splitlines()
    excerpt = "\n".join(line[:6])
    raise SystemExit(f"pocket PDF leaked TeX size token in {pdf_path}:\n{excerpt}")
PY
}

bash "$repo_root/scripts/publish_generated_course_pdf.sh" --repo-root "$repo_root" --course "$course"

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
root_pdf="$repo_root/$root_track_dir/$run_name/$filename"
course_pdf="generated_course_notes/$course/course.pdf"
pocket_1x_name="${filename%.pdf}_pocket.pdf"
pocket_1_2x_name="${filename%.pdf}_pocket_1_2x.pdf"

publish_pocket_variant() {
  local font_mode="$1"
  local output_dir="$2"
  local suffix="$3"
  local nutstore_dir="$4"
  local pocket_name="${filename%.pdf}_${suffix}.pdf"
  local pocket_src="$output_dir/$pocket_name"
  local pocket_dst="$repo_root/$root_track_dir/$run_name/$pocket_name"

  bash "$video2book_root/scripts/export_course_pocket_pdfs.sh" \
    --host-root "$repo_root" \
    --course "$course" \
    --font-mode "$font_mode" \
    --output-dir "$output_dir" \
    --suffix "$suffix" \
    --nutstore-dir "$nutstore_dir"

  validate_pocket_pdf_text "$pocket_src"
  hardlink_or_copy "$pocket_src" "$pocket_dst"
  printf 'published %s pocket -> %s\n' "$suffix" "$pocket_dst"
}

publish_pocket_variant \
  normal \
  "$repo_root/all_notes/pocket_books" \
  pocket \
  "$nutstore_root/pocket_books"

publish_pocket_variant \
  onepointtwo \
  "$repo_root/all_notes/pocket_books_1_2x" \
  pocket_1_2x \
  "$nutstore_root/pocket_books_1_2x"

bash "$video2book_root/scripts/codex_commit_push.sh" \
  "$repo_root" \
  "Publish pocket overflow outputs for $course" \
  "$course_pdf" \
  "${root_track_dir}/${run_name}/${filename}" \
  "${root_track_dir}/${run_name}/${pocket_1x_name}" \
  "${root_track_dir}/${run_name}/${pocket_1_2x_name}" \
  "all_notes/${filename}" \
  "all_notes/pocket_books/${pocket_1x_name}" \
  "all_notes/pocket_books_1_2x/${pocket_1_2x_name}"
