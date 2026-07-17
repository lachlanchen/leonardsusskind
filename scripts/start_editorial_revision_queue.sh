#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

exec "$repo_root/Video2Book/scripts/start_editorial_revision_queue_tmux.sh" \
  --repo-root "$repo_root" \
  --manifest references/editorial_revision_queue.json \
  --session susskind-editorial \
  --watchdog-session susskind-editorial-watchdog \
  --interval 1800 \
  --model gpt-5.6-sol \
  --reasoning ultra \
  "$@"
