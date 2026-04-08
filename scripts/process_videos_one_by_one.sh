#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_root="/home/lachlan/ProjectsLFS/YoutubeDownloader/downloads/PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG"
min_free_gpu_mib="${MIN_FREE_GPU_MIB:-20000}"

cd "$repo_root"

wait_for_gpu_memory() {
  while true; do
    free_mib="$(nvidia-smi --query-gpu=memory.free --format=csv,noheader,nounits | head -n 1 | tr -d ' ')"
    if [[ -n "$free_mib" ]] && (( free_mib >= min_free_gpu_mib )); then
      return
    fi
    echo "Waiting for GPU memory: ${free_mib:-unknown} MiB free, need ${min_free_gpu_mib} MiB"
    sleep 60
  done
}

while true; do
  next_video="$(python3 scripts/transcribe_video.py --repo-root "$repo_root" --source-root "$source_root" --print-next)"
  if [[ -z "$next_video" ]]; then
    echo "No pending videos remain."
    exit 0
  fi

  wait_for_gpu_memory
  echo "Processing $next_video"
  PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True python3 scripts/transcribe_video.py \
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
