# Final Polished Multilingual Editions

This queue translates the **accepted editorial TeX**, never `draft.tex`, OCR,
legacy unpolished PDFs, or the earlier duplicate lecture runs. It includes the
15-course editorial queue and its completed eight-chapter Cosmology pilot: 16
books and 145 chapters. Japanese and Simplified Chinese are complete. The next
sequence adds French, Spanish, German, Traditional Chinese, Korean, Vietnamese,
Russian and Arabic, one complete language at a time.

Each language is an **independent, normally readable book**, not an interlinear
export. The original English edition remains unchanged. Bunko also uses aligned
English/Japanese/Chinese paragraph layers; LazyLearn links to every validated
standalone PDF. These reader exports do not replace the standalone translations.

The short Higgs book was the first Japanese/Chinese pilot. Each added language
must pass the same structural, semantic and PDF gates before publication. These are
AI-assisted companion translations, not Susskind manuscripts or endorsed
translations. Automatic checks and sampled semantic review do not establish
error-free translation throughout a book.

## Pipeline

1. Verify chapter counts and passing `editorial_fidelity.json` records.
2. Hash-lock the final TeX and prepare losslessly masked paragraph segments.
3. Use pylatexenc's structured parser to preserve all syntax, equations,
   numeric values, references, asset paths and environments. Translate prose,
   titles, introductions, captions, questions and responses with `gpt-6-luna`
   through the authenticated Codex CLI. Traditional Chinese is the exception:
   OpenCC converts each validated Simplified Chinese segment with the `s2twp`
   profile, then Luna polishes that conversion against the English source. It is
   not independently regenerated from English.
   Inline math/reference tokens can reorder within the same structural block
   for natural target-language syntax; display equations, braces and environments
   cannot move. Reordered and retried rows receive additional semantic review.
4. Cache valid segments and retry only invalid segments once. Up to two targeted
   reasoning-model repairs may then address the failed segments. Attempts are
   persisted before requests, so restarting cannot silently reset the budget.
   API transport errors have three bounded attempts; exhaustion stops new calls
   across all workers. There is no perpetual quota retry loop.
5. Reassemble real TeX, retaining source figure assets and the accepted layout.
   Use XeLaTeX with Noto CJK, Noto Serif/Sans or Amiri as appropriate.
   Original blackboard writing and English labels
   inside frozen mathematical displays are intentionally retained, not redrawn.
6. Build three passes; require a nonempty PDF and outline, target-language text, no missing
   glyphs, unresolved references or overfull boxes. Run a sampled semantic audit
   covering opening and technical paragraphs from each chapter plus repaired or
   reordered rows, in bounded ten-pair review batches. Unresolved issues
   receive up to two source-bound, paragraph-only semantic repairs followed by
   a fresh review. Unresolved issues block that language's publication, not the
   remaining chapters or later books, and never create an available download.
7. Update the README availability table, with PDF links only for validated output.

No source English file is overwritten. Per-language output is under
`translations/<course-id>/<language>/`; intermediate requests, caches, usage logs,
build artifacts and queue state are under ignored `.translation-work/`.
Original figure directories are referenced by relative TeX paths, not duplicated.
Availability is bound to the PDF and translated-TeX hashes. Preparation and manual
compilation share the queue lock and cannot race a live worker run.

## Commands

Dependencies: Python with `pylatexenc==2.10`, `PyMuPDF` and `opencc`; XeLaTeX,
Noto Serif/Sans, Noto CJK, Amiri and DejaVu Sans Mono; tmux and
the CLI for the selected translation provider. Reuse the
shared Python environment. Codex account authentication is reused by the CLI;
no credential, cookie or session file is copied into the repository.
`scripts/setup_translation_tex.sh` prepares an isolated XeLaTeX format under
`.translation-work/` with hash-verified French, Spanish, German and Russian
hyphenation patterns pinned to an upstream revision. No system TeX configuration
or other project's format is changed. The tmux launcher runs this setup once;
later compilations reuse it. Missing hyphenation patterns fail the PDF gate.

```bash
bash scripts/setup_translation_tex.sh
python scripts/polished_translation.py prepare
python -m unittest discover -s scripts -p 'test_*translation*.py'
python scripts/polished_translation.py run --provider codex --model gpt-6-luna \
  --review-model gpt-6-luna --reasoning high --batch-chars 24000 \
  --workers 2 --language fr --book supplementary--higgs_boson--2012_summer
python scripts/polished_translation.py status
bash scripts/start_luna_translation_tmux.sh
```

One tmux session: `susskind-luna-translations`. The fixed order is `fr`, `es`,
`de`, `zh-Hant`, `ko`, `vi`, `ru`, `ar`. A language completes and publishes
before the next starts. At most five isolated Codex calls run simultaneously;
books and compile jobs remain sequential. `touch .translation-work/STOP` stops
at the next book boundary. Remove that marker to resume. Accepted caches survive
interruptions. Check `.translation-work/status.json` and `luna-queue.log` before restarting.
The launcher passes its verified Codex executable and PATH into the project
session explicitly, rather than inheriting an older shared tmux server PATH.
A brief missing-executable window during a shared CLI update uses the same
bounded transport cooldowns; the queue never reinstalls or copies the shared CLI.
Per-book failures and publication state are retained under
`.translation-work/book-state/`. Final queue state distinguishes `complete`,
`finished_with_blockers`, `provider_blocked`, and user-requested `paused`.
An interrupted request with a saved valid response is recovered without a new
API call. Malformed or missing responses still consume the finite content
attempt budget; transport failures refund it because they produced no content.
For new language queues, a failed language may receive up to three bounded Luna
repair sweeps before the wrapper stops. Each sweep runs only after the normal
queue has exited, reuses accepted caches, and must retain the same source,
semantic and PDF gates. It cannot silently skip a language, publish blocked
outputs, increase request budgets, or modify the accepted English, Japanese or
Simplified Chinese editions. Private prompts and results remain under
`.translation-work/language-repairs/`.

### Run Without Codex

To resume on AgInTi's direct OpenAI API provider, first confirm
`aginti keys status` reports that OpenAI is available, then run:

```bash
TRANSLATION_PROVIDER=aginti-openai bash scripts/start_luna_translation_tmux.sh --resume-from vi
```

Replace `vi` with the first unfinished language. This mode uses the existing
AgInTi OpenAI API configuration and defaults to `gpt-5.4` with high reasoning.
It does not use ChatGPT/Codex quota or Codex wrappers, including during repair.
Translation and review call AgInTi's provider client directly, without an agent
planner or tools. Repair sweeps use the AgInTi CLI with focused execution.
API calls are billed to the OpenAI API account configured in AgInTi; the
queue never buys credits or changes billing settings. It stops on API
authentication or billing failure and bounds retries for transient failures.
The accepted caches and existing book titles carry over, but new PDFs still
require source checks, semantic review, and a clean build. Run only one
language driver at a time.

### Codex Quota

The launcher configures `TRANSLATION_QUOTA_HELPER` to
`scripts/translation_quota.py`; an alternative helper path can be supplied
through that environment variable. Checks reuse the helper's freshness-checked
snapshot (up to three minutes old) rather than forcing a network request before
each batch; the in-process check is refreshed at least once per minute.
Unavailable quota telemetry or less than five percent remaining stops new requests
and repair sweeps without purchasing credits or repeatedly retrying quota errors.
The default five-percent floor can be crossed only with explicit project-local
consent in the ignored `.translation-work/spending-policy.json`
(`allow_existing_paid_credits: true`) and a fresh positive existing-credit balance.
Missing credit evidence, an empty balance, or unavailable telemetry still stops
requests. This policy never purchases credits, enables account auto-top-up,
changes another project's spending policy, or switches the translation model.
The quota reader initializes the account before requesting limits through the
[official read-only app-server RPC](https://developers.openai.com/codex/app-server/).
It retains RPC errors so an explicit network/server failure can use the existing
bounded transport cooldowns. Authentication, exhausted quota, and unclassified
telemetry failures remain hard stops; no model calls run while transport recovers.
Each read-only quota probe owns an isolated process group. Shutdown escalation
reaps only that probe and its launcher children; slow shutdown cannot masquerade
as exhausted quota or overwrite an authentication error.
Each publication verifies the exact commit SHA on every configured push URL;
one successful mirror push alone does not establish publication completion.
Transient connection, timeout, rate-limit or server failures may resume the
queue twice after five- and ten-minute cooldowns. No calls run during the wait;
STOP is checked every five seconds. Authentication/payment failures stop for
owner attention, never automatic charging or endless credit checks. Override
with `--transport-resumes` and `--transport-retry-seconds`.
Separate transport incidents receive a fresh bounded allowance only after the
queue accepts new segments or validates another PDF. Repeated failures with no
measurable progress still exhaust the allowance and stop. Quota/authentication
failures cannot use this progress-based reset.

## Validation Repairs

Number-word validation recognizes zero through ninety-nine (including compound
forms), first through twelfth, single occurrences, common fractions, and
mathematical unity/unit magnitude. It also recognizes "once", ordinal centuries
through twentieth, and spelled-out fractions such as "two-thirds".
Large spelled-out quantities and shared ranges such as "ten to twelve billion"
are compared to their values in target notation (`100億` to `120億`), not just
the visible digits. Unit names such as `千克` retain their coefficient rather
than being mistaken for a numeric multiplier. Wrong magnitudes still fail.
Japanese denominator-first fractions such as
`4分の1` are compared as rational values; penny/dime denominations are recognized
when those exact source words occur. It still
rejects unsupported new quantities. Immutable accented names and nonbreaking
reference glue may follow natural target-language word order. Math can pass
around a complete emphasis group, but not into or out of its braces. Duplicate
tokens, missing figures, structural movement, and changed equations still fail.

Before requesting a new translation, the queue rechecks saved, unaccepted
drafts against the current validator. For example, Korean `0이 아닌` can
express “nonzero”, and `0이 된다` can express “vanishes”. The check matches
these predicates one for one within corresponding sentences and TeX token
boundaries. It does not treat a mention of zero as permission to introduce
other quantities. Passages accepted on this basis are always included in
semantic review before publication.

Run `python scripts/polished_translation.py recheck --language ko --dry-run`
to count recoverable drafts without making model calls or changing files.
Repair sweeps apply the recheck automatically under the queue lock. It
preserves the original wording and attempt counts. Unresolved drafts still
require a source-backed repair.

After a controlled stop, the queue driver accepts `--resume-from ko` to
resume Korean and continue in the original language order. It first checks
that both remotes match the local commit and that each skipped edition has
a validated PDF, a committed file and a published README link.

Use `repair --repairs PATH.json` for reviewed corrections. The packet records
the book ID and per-row language, source file, segment ID, source hash, complete
restored source, masked translation, and review reason. The tool validates the
entire packet first, backs up changed caches, and schedules every repair for
additional semantic review. Replacing already accepted text also requires its
`previous_sha256`. No full-chapter regeneration is required.

During an active queue, put only trusted, source-checked repair packets in
`.translation-work/pending-reviewed-repairs/<language>/`. The repair sweep
applies them under the queue lock, archives the packets, and gives the normal
pipeline a chance to validate the updated books before asking a repair agent.
Packets for a different language or an already validated edition are rejected.
If a blocked PDF's source-checked TeX has changed since the failed build, the
repair sweep tries the updated render before starting an agent. An unchanged
failed render is not retried on that basis.

On 2026-10-12, ten Advanced Quantum Mechanics segments were checked against the
English source. Most failures were overly restrictive numerical/order checks;
one Chinese paragraph repeated a Hamiltonian token and was rewritten to use it
once. Unsupported numeric paraphrases were corrected without loosening the
global preservation checks. Balance was not the blocker.

The subsequent PDF gate caught two U+FFFD replacement characters in otherwise
intact words. Both were checked against the source and repaired; the segment
validator now rejects corrupt Unicode/control characters before compilation.
Front matter is included in semantic review, and ordinary English wording must
be translated even when nearby proper names remain Latin. These repairs do not
change any frozen equation or original image.

Semantic review now runs before the expensive PDF passes. The `review --book ID
--language ja` command reruns only changed review batches without compiling.
Already validated language editions are skipped when the other language needs
repair. Source-checked false positives can be explicitly adjudicated under
`.translation-work/review-decisions/`: each dismissal is tied to the exact
source/translation sample hash and exact issue hash, with a written reason.
The original report is retained, and the published quality record includes the
decisions. A changed sample or new issue cannot inherit a dismissal. There is
no blanket reviewer bypass or automatic acceptance of model corrections.

Layout restoration matches environment instances rather than counting optional
arguments. Missing minipage alignment options and damaged width keys are restored
from the immutable English headers; translated captions and body text are kept.
Missing, added or reordered layout environments still fail. Contents entries
reserve space for three-level numbering such as `10.10.1`.

## Reading Editions and Release Checks

The default translated PDF profile is `a5-1.2-dimensions-v2`: **177.6 x 252 mm**
(each A5 dimension multiplied by 1.2), 12 pt body text on a 17 pt baseline,
16 mm side margins, and 18 mm top/bottom margins including header and footer.
This is not the old `pocket_1_2x` type-enlargement profile. Existing English
PDFs are unchanged. Running headers wrap within the text width, classroom
questions may break across pages, and page numbers retain a bottom margin.
Source-anchored page adjustments handle three footnote/float cases without
shrinking figures, changing equations, or suppressing overflow diagnostics.

`scripts/audit_reading_editions.py` compares every chapter's mathematical,
diagram and figure-command inventories against the immutable English source,
checks every PDF page's dimensions and text bounds, and records the result in
`references/reading_editions_audit.json`. The per-edition `quality.json` files
also bind the accepted translation, TeX, PDF and layout hashes to passing
compile and sampled semantic checks. These checks are evidence, not a claim
of exhaustive human proofreading or error-free translation.

`scripts/repair_caption_boundaries.py` detects translated caption prose that
escaped its source-defined braces. Its opt-in repair moves existing characters
only, requires the previous translation hash, backs up the cache and schedules
fresh semantic review and compilation. Do not repair a cache while the queue
lock is held. The caption validator prevents recurrence in new output.

The original Bunko importer, `../Bunko/tools/import_polished_physics.py`, created
the aligned `en`, `ja`, `zh` base layers. Do not rerun it in write mode on
published books: it replaces the metadata and drops additional layers.
Published content lives in `../bunko-books`, not in the app repository.
Coverage checks include front matter, overviews, classroom Q&A,
footnotes, captions and tables. Equations are protected before Pandoc parsing
and every rich expression must render with the app's KaTeX configuration.
Matched passage IDs and old content-addressed files remain valid for readers.
No new translation calls are made by the reader importer.

To add further published languages without replacing existing Bunko passages,
use `scripts/sync_bunko_layers.py`. Pass the verified Susskind publication
commit with `--source-commit` and use `--report` to record accepted and held
layers. Add `--apply` only with a clean, up-to-date `bunko-books` checkout.
The exporter checks source segments, equation and figure alignment, KaTeX, and
the Bunko bundle schema, then preserves older chapter files, passage IDs and
sentence maps. Review the report before publishing: an exit status of 1 can
mean some layers were held even though verified layers were written. Rebuild
`reader-index.json` in `bunko-books` before publishing.

Release commands after the queue has exited:

```bash
python scripts/audit_reading_editions.py
python scripts/sync_bunko_layers.py --source-commit "$published_susskind_commit" \
  --apply --report .translation-work/bunko-sync.json
python ../bunko-books/tools/catalogue.py --write
python scripts/polished_translation.py readme
python scripts/translation_catalog.py --reader ../LazyLearn/docs/leonardsusskind-reader.html
python ../Bunko/tools/check_polished_reader.py
python ../LazyLearn/tests/check_susskind_reader.py
```

The publication queue commits the catalogue with the validated PDFs. The
GitHub edition table links directly to the selected book and language in the
web reader, which loads the current catalogue and offers a direct PDF link.
The embedded catalogue is an offline fallback. Refresh it when updating the
reader and verify representative editions on desktop and mobile. The reader
opens at page width with the outline closed.

Use scoped publication commits when neighboring repositories have unrelated
work in progress. Do not deploy an unrelated Bunko app branch: content updates
use the existing reader contract and require only the `bunko-books` release.

Visual TOC inspection also caught translated words placed after a heading's
closing braces. The parser now protects adjacent argument endings separately,
allowing natural Japanese/Chinese suffixes *inside* a title. Existing caches
are migrated without changing their restored TeX or making translation calls;
invalid entries are not silently retained. Whole-heading AST checks reject
text outside its argument, and stray placeholder characters fail validation.
Corrections mark the affected PDF as needing a rebuild. New quality records
also bind availability to accepted-translation hashes, not only PDF/TeX hashes.

Malformed JSON responses are archived and retried once at the transport level;
invalid cached review replies cannot permanently poison a resume. No accepted
translation is discarded by that retry.

### Review Model Qualification

The accepted Japanese and Simplified Chinese editions were translated with
`deepseek-chat` and sampled with the independently tested `deepseek-reasoner`
route. That historical evidence remains bound to those editions.

The eight added languages use the exact `gpt-6-luna` model for both translation
and sampled semantic review, with high reasoning effort. Every request runs in
an ephemeral, read-only Codex working directory; only the controller writes a
validated JSON response into the ignored cache. Model identity is included in
title and review caches, so a model change cannot silently reuse old review
evidence. The model choice follows the official
[GPT-6 Luna documentation](https://developers.openai.com/api/docs/models/gpt-6-luna),
which describes it as a multilingual model for focused, high-volume tasks. This
qualification and sampled review are evidence, not a guarantee of error-free
translation.

## Earlier Verified Checkpoint: 2026-10-12

Advanced Quantum Mechanics is complete in both standalone languages:

| Check | Japanese | Chinese |
| --- | ---: | ---: |
| Accepted segments | 840/840 | 840/840 |
| PDF pages | 142 | 128 |
| Outline entries | 130 | 130 |
| Image placements, including cover | 30 | 30 |
| Displayed equation environments retained | 501 | 501 |
| Inline math fragments retained | 1,147 | 1,147 |
| Chapter figure commands retained | 29 | 29 |
| Reasoning-model semantic sample | 56 pairs | 38 pairs |
| Overflow / missing glyph / out-of-page text | 0 | 0 |

The final reasoning reviews passed with no issues and no manual dismissals.
Cover, contents and figure pages were visually inspected, including the repaired
math-bearing title. The final books were pushed in `50b47822`. All 16 original
English source sets were verified unchanged. This is sampled semantic evidence,
not a claim of exhaustive error-free translation. The next Quantum Entanglement
book resumes from its cached segments; remaining books still require generation
and all finalization gates.

### Part 3 Recovery And Queue Hardening

Eight source-checked passages in Quantum Entanglement Part 3 were recovered on
2026-10-12. Ordinal/fraction representations were validator false positives;
indefinite unit expressions were translated naturally without introducing
digits. One Chinese paragraph duplicated its frozen electric/magnetic-field
tokens: the prose was corrected to keep each expression exactly once. All eight
are included in the next semantic review.

The controller now drains every chapter, records all failures, finalizes each
complete language independently, and advances to later books. It never exports
an incomplete language or labels a skipped book complete. Repairs cannot change
frozen TeX or equations, and prior accepted wording is retained in the local
repair history. Deterministic publication/compile failures remain explicit
blockers; no agent is authorized to weaken checks or rewrite pipeline code.

Part 3 subsequently passed with 642/642 segments in each language. Its separate
Japanese/Chinese PDFs have 144/137 pages, 95 outline entries each, 97 chapter
figures plus the cover, 327 display equations, and 818 inline formulas. Both
math inventories and figure commands match the English source. No overflow,
missing glyphs or out-of-page text was detected; representative TOC, figure,
and equation pages were inspected visually. Reasoning reviews covered 64/42
pairs. The new targeted repair corrected two genuine Chinese distinctions
(velocity vs speed, and lattice vs lattice point), then passed re-review with
no manual dismissals. Publication commit: `d845a58c`.

The recovery/validation regression suite now contains 34 tests, including
restart budgets, response recovery, provider cooldowns, retaining earlier
accepted wording, and continuing after blocked chapters/books.

Readme status is generated deterministically. `--publish` makes a scoped commit
and pushes each validated pair of PDFs. It refuses a pre-existing staged index,
README edits outside the generated block, or files over 95 MiB. A publication
failure is recorded in `.translation-work/publication.json` without discarding
accepted translations or stopping the next book. No inference prompts, keys or
private logs are committed. Without `--publish`, all work remains local.

Parser reference: [pylatexenc LatexWalker](https://pylatexenc.readthedocs.io/en/v2.10/latexwalker/).
