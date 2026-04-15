#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

exec python3 "$repo_root/scripts/sync_lazyingart_books.py" --repo-root "$repo_root" "$@"
