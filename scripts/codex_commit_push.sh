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

prompt_file="$(mktemp)"
trap 'rm -f "$prompt_file"' EXIT

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

cat "$prompt_file" | codex exec \
  --model "$model" \
  -c "model_reasoning_effort=\"$reasoning_effort\"" \
  --dangerously-bypass-approvals-and-sandbox \
  -C "$repo_path" \
  --skip-git-repo-check \
  -
