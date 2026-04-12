#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 3 ]]; then
  echo "Usage: $0 <repo_path> <commit_message> <pathspec> [<pathspec> ...]" >&2
  exit 1
fi

repo_path="$1"
commit_message="$2"
shift 2
pathspecs=("$@")

model="${CODEX_COMMIT_MODEL:-gpt-5.3-codex-spark}"
reasoning_effort="${CODEX_COMMIT_REASONING:-low}"
session_file="${CODEX_COMMIT_SESSION_FILE:-}"
session_doc_file="${CODEX_COMMIT_SESSION_DOC_FILE:-}"
tmux_session_name="${NOTE_TMUX_SESSION_NAME:-susskind-notes}"

prompt_file="$(mktemp)"
jsonl_file="$(mktemp)"
trap 'rm -f "$prompt_file" "$jsonl_file"' EXIT

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

{
  echo "You are handling a focused commit and push step."
  echo
  echo "Inputs:"
  echo "- Repo path: $repo_path"
  echo "- Commit message: $commit_message"
  echo "- Stage only these pathspecs:"
  for item in "${pathspecs[@]}"; do
    echo "  - $item"
  done
  echo
  echo "Required actions:"
  echo "1. Stage only the listed pathspecs."
  echo "2. If staging is empty, print: No changes to commit for step: $commit_message"
  echo "3. Otherwise run:"
  echo "   - git commit -m \"$commit_message\""
  echo "   - git push origin main"
  echo
  echo "Important constraints:"
  echo "- Do not modify files."
  echo "- Do not amend previous commits."
  echo "- Do not use force push."
  echo "- Do not stage files outside the provided pathspec list."
} > "$prompt_file"

if [[ -n "$session_file" && -s "$session_file" ]]; then
  session_id="$(tr -d '[:space:]' < "$session_file")"
  cat "$prompt_file" | codex exec resume \
    --json \
    --model "$model" \
    -c "model_reasoning_effort=\"$reasoning_effort\"" \
    --dangerously-bypass-approvals-and-sandbox \
    --skip-git-repo-check \
    "$session_id" \
    - > "$jsonl_file"
else
  cat "$prompt_file" | codex exec \
    --json \
    --model "$model" \
    -c "model_reasoning_effort=\"$reasoning_effort\"" \
    --dangerously-bypass-approvals-and-sandbox \
    -C "$repo_path" \
    --skip-git-repo-check \
    - > "$jsonl_file"

  if [[ -n "$session_file" && ! -s "$session_file" ]]; then
    new_session_id="$(extract_session_id "$jsonl_file")"
    if [[ -n "$new_session_id" ]]; then
      printf '%s\n' "$new_session_id" > "$session_file"
      write_session_doc "$new_session_id" "$session_doc_file"
    fi
  fi
fi

if [[ -n "${session_id:-}" ]]; then
  write_session_doc "$session_id" "$session_doc_file"
fi

cat "$jsonl_file"
