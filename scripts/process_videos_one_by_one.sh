#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_root="/home/lachlan/ProjectsLFS/YoutubeDownloader/downloads/PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG"

cd "$repo_root"

while true; do
  next_video="$(python3 scripts/transcribe_video.py --repo-root "$repo_root" --source-root "$source_root" --print-next)"
  if [[ -z "$next_video" ]]; then
    echo "No pending videos remain."
    exit 0
  fi

  echo "Processing $next_video"
  python3 scripts/transcribe_video.py \
    --repo-root "$repo_root" \
    --source-root "$source_root" \
    --video "$next_video"

  git add -- subtitles markdown

  if git diff --cached --quiet; then
    echo "No new tracked changes after processing $next_video"
    continue
  fi

  rel_path="${next_video#${source_root}/}"
  rel_path="${rel_path%.*}"
  git commit -m "Add transcript for ${rel_path}"
  git push origin main
done
