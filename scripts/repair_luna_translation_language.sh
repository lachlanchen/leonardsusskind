#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
language="${1:?Language code is required}"
round="${2:?Repair round is required}"
python="${TRANSLATION_PYTHON:-python}"
provider="${TRANSLATION_PROVIDER:-codex}"
model="${TRANSLATION_MODEL:-gpt-6-luna}"
cd "$root"
case "$language" in fr|es|de|zh-Hant|ko|vi|ru|ar) ;; *) exit 2 ;; esac
[[ "$round" =~ ^[1-3]$ ]] || exit 2
[[ ! -e .translation-work/STOP ]] || exit 1

# The normal worker has exited. Retry cached content under the same queue lock
# before spending a model call; recovered passages still go to semantic review.
recheck="$("$python" scripts/polished_translation.py recheck --language "$language" --apply-queued-repairs)"
printf '%s\n' "$recheck"
if printf '%s\n' "$recheck" | tail -n 1 | jq -e '.applied_packets > 0 or .recovered > 0 or (.layout_rebuilds|length) > 0' >/dev/null; then
  printf 'Local repairs made progress; retrying normal validation before invoking a repair agent.\n'
  exit 0
fi

if [[ "$provider" == codex ]]; then
  model=gpt-6-luna
  export TRANSLATION_QUOTA_HELPER="${TRANSLATION_QUOTA_HELPER:-$root/scripts/translation_quota.py}"
  PYTHONPATH="$root/scripts${PYTHONPATH:+:$PYTHONPATH}" "$python" - <<'PY'
import polished_translation as p
p.check_codex_quota()
PY
elif [[ "$provider" != aginti-openai || ! "$model" =~ ^[a-zA-Z0-9._-]+$ ]]; then
  exit 2
fi

umask 077
directory="$root/.translation-work/language-repairs/$language"
mkdir -p "$directory"
packet="$directory/round-$round.md"
cat >"$packet" <<EOF
Repair the blocked $language editions in this repository and complete this one
repair sweep. The owner has authorized completion of all languages, sequentially,
using $provider with $model. You own this bounded repair step while the generation queue is
stopped; do not start another translation queue or background agent.

You ARE the repair worker launched by repair_luna_translation_language.sh.
Its wrapper PID is $$, and its agent child with this exact prompt is YOU, not
a competing repair agent. Your result file is empty until you finish. Never
wait for your own wrapper, agent process, log, or result file to complete.
Do not monitor yourself or defer work because this same repair invocation is
visible in ps. Diagnose and repair files directly now, then exit this sweep.
If no safe repair is possible, report the blocker and exit instead of polling.

For page overflow, correlate the log's open chapter and printed page number
with the PDF footer. A physical PDF page index is offset by the front matter;
using it as a printed page number can select the wrong chapter. Inspect the
actual failing page, locate its text in that chapter, and use a unique source
anchor there. A small measured page enlargement is allowed when margins remain
sound, but never hide warnings or move an anchor in an unrelated chapter.

Read AGENTS.md, references/POLISHED_TRANSLATIONS.md, and the publisher-voice skill.
Inspect .translation-work/status.json, book-state/, build logs, source-bound
translation caches, reviews, git status, and scripts/polished_translation.py.
All existing untracked translations/$language outputs from the queue are in scope
only under translations/<book-id>/$language/. Unrelated changes are not yours.

Repair structural parsing, missing font/hyphenation support, real semantic defects,
or individual layout failures from evidence. Reuse accepted caches, touch only
failed paragraphs where necessary, and preserve all equations, references, figures,
qualifications and disclosures. For Traditional Chinese use the validated Simplified
Chinese conversion as the draft, never independently regenerate from English.
Do not modify English, Japanese, or Simplified Chinese sources or editions.
Do not weaken, suppress, bypass or fabricate quality gates, alter request budgets,
invent adjudications, delete failed material, or label an unvalidated PDF available.
Do not print credentials, inspect private sessions, change other repositories,
force-push, or rewrite existing commits. Do not change the model or reasoning.
Do not create a new worktree or copy of this repository. If $provider is
aginti-openai, do not invoke Codex, inspect its quota, or change billing settings.

The local recheck has already applied queued source-bound corrections and
reconsidered saved drafts without inference. Recovered and corrected passages
are in review_ids and must pass normal semantic review.
For remaining numerical errors, compare the English and the saved draft in
context, including sign, negation, magnitude, and limiting language. Do not
spell out an unsupported quantity merely to get it through the digit check.

Only one build at a time. Stop on auth/payment/quota failure; do not retry those.
The shared workstation resource policy applies. Do not launch GUI desktops.

For each repaired book run the normal compile command with --provider $provider
--model $model --review-model $model --reasoning high --language $language
and --book ID. Run relevant tests and inspect representative PDF pages.
Run mocked translation tests with TRANSLATION_QUOTA_HELPER unset so that their
mock subprocesses do not accidentally intercept a real quota probe. The real
translation and compile commands must retain their normal quota checks.
Refresh README with the script. Commit only tested pipeline repairs and validated
$language outputs plus owned README availability changes. Push and verify both
configured remotes with push_publication_remotes(). No private work/cache files
belong in Git. Never commit blocked or building quality records.

Finish this sweep, summarize exact repairs/tests/remaining blockers, then exit.
The parent wrapper will rerun the normal language queue to verify completeness
and continue. If a defect cannot be safely repaired, retain the evidence and
report it rather than claiming completion. This is bounded sweep $round of 3.
EOF

if [[ "$provider" == aginti-openai ]]; then
  AGINTI_EXECUTION_TIER=focused timeout --kill-after=15s 45m "${TRANSLATION_AGINTI_BIN:-aginti}" run --stdin --json \
    --cwd "$root" --provider openai --model "$model" --main-reasoning high \
    --routing manual --task-profile coding -s normal --sandbox-mode host \
    --package-install-policy block --max-steps 60 --no-scs --allow-shell --allow-file-tools \
    --no-web-search --no-mcp --no-wrappers --no-auxiliary-tools --no-parallel-scouts --no-auto-update \
    <"$packet" >"$directory/round-$round-aginti.json" 2>"$directory/round-$round-aginti.log"
  jq -e --arg model "$model" '.ok and (.failed|not) and (.stopped|not) and .provider=="openai" and .model==$model' \
    "$directory/round-$round-aginti.json" >/dev/null
  jq -r .result "$directory/round-$round-aginti.json" >"$directory/round-$round-result.md"
else
  "${TRANSLATION_CODEX_BIN:-codex}" exec --ephemeral --ignore-user-config --skip-git-repo-check \
  -C "$root" --sandbox danger-full-access -m gpt-6-luna \
  -c 'model_reasoning_effort="high"' \
  -o "$directory/round-$round-result.md" "$(cat "$packet")" \
  >"$directory/round-$round.log" 2>&1
fi
