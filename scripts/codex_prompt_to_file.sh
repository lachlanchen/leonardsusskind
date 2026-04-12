#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 5 ]]; then
  echo "Usage: $0 <repo_path> <prompt_file> <output_file> <model> <reasoning> [<image> ...]" >&2
  exit 1
fi

repo_path="$1"
prompt_file="$2"
output_file="$3"
model="$4"
reasoning="$5"
shift 5
session_file="${CODEX_SHARED_SESSION_FILE:-}"
session_doc_file="${CODEX_SHARED_SESSION_DOC_FILE:-}"
tmux_session_name="${NOTE_TMUX_SESSION_NAME:-susskind-notes}"
session_scope="${NOTE_CODEX_SESSION_SCOPE:-global}"

extract_session_id() {
  python3 - "$1" <<'PY'
import json
import sys

path = sys.argv[1]
with open(path, encoding="utf-8", errors="replace") as handle:
    for line in handle:
        line = line.strip()
        if not line:
            continue
        try:
            data = json.loads(line)
        except json.JSONDecodeError:
            continue
        if data.get("type") == "session_meta":
            payload = data.get("payload", {})
            session_id = payload.get("id")
            if session_id:
                print(session_id)
                break
        if data.get("type") == "thread.started":
            thread_id = data.get("thread_id")
            if thread_id:
                print(thread_id)
                break
PY
}

write_session_doc() {
  local session_id="$1"
  local target="$2"
  [[ -n "$target" ]] || return 0
  mkdir -p "$(dirname "$target")"
  cat > "$target" <<EOF
# Shared Codex Session

- tmux session: $tmux_session_name
- codex session id: $session_id
- codex session file: $session_file
- codex session scope: $session_scope
- repo root: $repo_path
- model: $model
- updated at: $(date --iso-8601=seconds)
EOF
}

if [[ -n "$session_file" ]]; then
  mkdir -p "$(dirname "$session_file")"
  if [[ -z "$session_doc_file" ]]; then
    session_doc_file="${session_file%.session_id}.session.md"
  fi
fi

jsonl_file="$(mktemp)"
trap 'rm -f "$jsonl_file"' EXIT

if [[ -n "$session_file" && -s "$session_file" ]]; then
  session_id="$(tr -d '[:space:]' < "$session_file")"
  cmd=(
    codex
    exec
    resume
    --json
    -m "$model"
    -c "model_reasoning_effort=\"$reasoning\""
    -o "$output_file"
  )
else
  cmd=(
    codex
    exec
    --json
    -m "$model"
    -c "model_reasoning_effort=\"$reasoning\""
    -s read-only
    -C "$repo_path"
    -o "$output_file"
  )
fi

for image in "$@"; do
  cmd+=(--image "$image")
done

if [[ -n "${session_id:-}" ]]; then
  cmd+=("$session_id" -)
else
  cmd+=(-)
fi

set +e
"${cmd[@]}" < "$prompt_file" > "$jsonl_file"
status=$?
set -e

if [[ -n "$session_file" && ! -s "$session_file" ]]; then
  new_session_id="$(extract_session_id "$jsonl_file")"
  if [[ -n "$new_session_id" ]]; then
    printf '%s\n' "$new_session_id" > "$session_file"
    write_session_doc "$new_session_id" "$session_doc_file"
  fi
elif [[ -n "${session_id:-}" ]]; then
  write_session_doc "$session_id" "$session_doc_file"
fi

cat "$jsonl_file"
exit "$status"
