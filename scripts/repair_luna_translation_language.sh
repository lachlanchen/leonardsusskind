#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
language="${1:?Language code is required}"
round="${2:?Repair round is required}"
python="${TRANSLATION_PYTHON:-python}"
cd "$root"
case "$language" in fr|es|de|zh-Hant|ko|vi|ru|ar) ;; *) exit 2 ;; esac
[[ "$round" =~ ^[1-3]$ ]] || exit 2

export TRANSLATION_QUOTA_HELPER="${TRANSLATION_QUOTA_HELPER:-$HOME/.codex/skills/codex-collaboration/scripts/codex_session.py}"
PYTHONPATH="$root/scripts${PYTHONPATH:+:$PYTHONPATH}" "$python" - <<'PY'
import polished_translation as p
p.check_codex_quota()
PY

directory="$root/.translation-work/language-repairs/$language"
mkdir -p "$directory"
packet="$directory/round-$round.md"
cat >"$packet" <<EOF
Repair the blocked $language editions in this repository and complete this one
repair sweep. The owner has authorized completion of all languages, sequentially,
using gpt-6-luna. You own this bounded repair step while the generation queue is
stopped; do not start another translation queue or background agent.

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

Only one build at a time. Stop on auth/payment/quota failure; do not retry those.
The shared workstation resource policy applies. Do not launch GUI desktops.

For each repaired book run the normal compile command with --provider codex
--model gpt-6-luna --review-model gpt-6-luna --reasoning high --language $language
and --book ID. Run relevant tests and inspect representative PDF pages.
Refresh README with the script. Commit only tested pipeline repairs and validated
$language outputs plus owned README availability changes. Push and verify both
configured remotes with push_publication_remotes(). No private work/cache files
belong in Git. Never commit blocked or building quality records.

Finish this sweep, summarize exact repairs/tests/remaining blockers, then exit.
The parent wrapper will rerun the normal language queue to verify completeness
and continue. If a defect cannot be safely repaired, retain the evidence and
report it rather than claiming completion. This is bounded sweep $round of 3.
EOF

codex exec --ephemeral --ignore-user-config --skip-git-repo-check \
  -C "$root" --sandbox danger-full-access -m gpt-6-luna \
  -c 'model_reasoning_effort="high"' \
  -o "$directory/round-$round-result.md" "$(cat "$packet")" \
  >"$directory/round-$round.log" 2>&1
