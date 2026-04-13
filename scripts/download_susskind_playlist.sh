#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

exec "$repo_root/Video2Book/scripts/download_susskind_playlist.sh" "$@"
