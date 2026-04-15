#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: scripts/monitor_lazyingart_books_sync.sh [options]

Periodically sync finished full-course PDFs into LazyingArtBooks.

Options:
  --interval <seconds>   sleep interval between sync runs (default: 1800)
  -h, --help             show help
USAGE
}

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
interval=1800

while [[ $# -gt 0 ]]; do
  case "$1" in
    --interval)
      interval="${2:-1800}"
      shift 2
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

cd "$repo_root"
while true; do
  echo "[$(date --iso-8601=seconds)] syncing finished course PDFs"
  bash "$repo_root/scripts/sync_lazyingart_books.sh"
  sleep "$interval"
done
