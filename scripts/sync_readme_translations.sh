#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
work_root="${README_I18N_WORK_ROOT:-$repo_root/.auto-readme-work/readme-i18n}"
mkdir -p "$work_root/logs" "$work_root/prompts" "$work_root/jsonl" "$work_root/codex_sessions"

source_readme="$repo_root/README.md"
model="${README_I18N_MODEL:-gpt-5.4}"
reasoning="${README_I18N_REASONING:-medium}"
session_file="${README_I18N_SESSION_FILE:-$work_root/codex_sessions/readme-i18n.session_id}"
session_doc_file="${README_I18N_SESSION_DOC_FILE:-$work_root/codex_sessions/readme-i18n.session.md}"

langs=()

usage() {
  cat <<'EOF'
Usage: scripts/sync_readme_translations.sh [--lang <code> ...]

Syncs i18n/README.*.md files from the root README.md using codex exec.
Each language is translated, committed, and pushed before the loop advances.

Examples:
  scripts/sync_readme_translations.sh
  scripts/sync_readme_translations.sh --lang zh-Hans --lang ja
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --lang)
      langs+=("$2")
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 1
      ;;
  esac
done

if [[ ${#langs[@]} -eq 0 ]]; then
  while IFS= read -r path; do
    base="$(basename "$path")"
    langs+=("${base#README.}")
    langs[-1]="${langs[-1]%.md}"
  done < <(find "$repo_root/i18n" -maxdepth 1 -type f -name 'README.*.md' | sort)
fi

lang_name() {
  case "$1" in
    ar) echo "Arabic" ;;
    de) echo "German" ;;
    es) echo "Spanish" ;;
    fr) echo "French" ;;
    ja) echo "Japanese" ;;
    ko) echo "Korean" ;;
    ru) echo "Russian" ;;
    vi) echo "Vietnamese" ;;
    zh-Hans) echo "Simplified Chinese" ;;
    zh-Hant) echo "Traditional Chinese" ;;
    *) echo "$1" ;;
  esac
}

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
            if payload.get("id"):
                print(payload["id"])
                break
        if data.get("type") == "thread.started" and data.get("thread_id"):
            print(data["thread_id"])
            break
PY
}

write_session_doc() {
  local session_id="$1"
  mkdir -p "$(dirname "$session_doc_file")"
  cat > "$session_doc_file" <<EOF
# Shared Codex Session

- purpose: README i18n sync
- codex session id: $session_id
- codex session file: $session_file
- repo root: $repo_root
- model: $model
- reasoning: $reasoning
- updated at: $(date --iso-8601=seconds)
EOF
}

run_codex_translation() {
  local prompt_file="$1"
  local jsonl_file="$2"
  local session_id=""
  local -a cmd=()

  if [[ -s "$session_file" ]]; then
    session_id="$(tr -d '[:space:]' < "$session_file")"
    cmd=(
      codex exec resume
      --json
      -m "$model"
      -c "model_reasoning_effort=\"$reasoning\""
      --dangerously-bypass-approvals-and-sandbox
      "$session_id"
      -
    )
  else
    cmd=(
      codex exec
      --json
      -m "$model"
      -c "model_reasoning_effort=\"$reasoning\""
      --dangerously-bypass-approvals-and-sandbox
      -C "$repo_root"
      -
    )
  fi

  set +e
  "${cmd[@]}" < "$prompt_file" > "$jsonl_file"
  local status=$?
  set -e

  if [[ ! -s "$session_file" ]]; then
    local new_session_id
    new_session_id="$(extract_session_id "$jsonl_file")"
    if [[ -n "$new_session_id" ]]; then
      printf '%s\n' "$new_session_id" > "$session_file"
      write_session_doc "$new_session_id"
    fi
  elif [[ -n "$session_id" ]]; then
    write_session_doc "$session_id"
  fi

  return "$status"
}

for lang in "${langs[@]}"; do
  target_rel="i18n/README.${lang}.md"
  target_file="$repo_root/$target_rel"
  language="$(lang_name "$lang")"
  prompt_file="$work_root/prompts/README.${lang}.prompt.txt"
  jsonl_file="$work_root/jsonl/README.${lang}.jsonl"

  if [[ ! -f "$target_file" ]]; then
    echo "Skipping unknown target: $target_rel" >&2
    continue
  fi

  cat > "$prompt_file" <<EOF
You are synchronizing one translated README file for this repository.

Source of truth:
- $source_readme

Target file to rewrite completely:
- $target_file

Task:
- Rewrite the entire target file in $language so it matches the current root README.md.

Requirements:
- Translate natural-language content into $language.
- Preserve the source document's section order, scope, headings, badges, HTML tables, bullets, and emphasis.
- Do not add or remove substantive content relative to the root README.
- Preserve product names and proper nouns such as Leonard Susskind, LazyingArt LLC, Video2Book, and Theoretical Minimum unless a standard localized form is clearly better.
- Keep code blocks, filenames, repo paths, URLs, and PDF names unchanged unless a relative link must change because the target file lives under i18n/.
- Follow the root README's link strategy. If the source uses a public absolute URL, keep that public URL. If the source uses a repo-relative link, rewrite it so it resolves correctly from i18n/. In practice, links that point to root-level repo content should usually gain ../ . External http(s) links must stay unchanged.
- The top language navigation line in the translated file must use ../README.md for English and sibling links like README.es.md for the other translations.
- Do not edit README.md.
- Do not edit any file except $target_file.

After updating $target_file, stop.
EOF

  echo "Syncing $target_rel from README.md -> $language"
  run_codex_translation "$prompt_file" "$jsonl_file"

  if ! git -C "$repo_root" diff --quiet -- README.md; then
    echo "README.md changed unexpectedly during $target_rel sync. Aborting." >&2
    exit 1
  fi

  NOTE_TMUX_SESSION_NAME="${NOTE_TMUX_SESSION_NAME:-readme-i18n-sync}" \
  CODEX_COMMIT_MODEL="$model" \
  CODEX_COMMIT_REASONING="$reasoning" \
  CODEX_COMMIT_SESSION_FILE="$session_file" \
  CODEX_COMMIT_SESSION_DOC_FILE="$session_doc_file" \
    bash "$repo_root/scripts/codex_commit_push.sh" \
      "$repo_root" \
      "Sync ${language} README translation" \
      "$target_rel"
done

echo "README translation sync complete."
