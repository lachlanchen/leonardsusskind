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
   Use XeLaTeX with Noto CJK, Noto Serif/Sans or Noto Arabic fonts as appropriate.
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
Noto Serif/Sans, Noto CJK and Noto Arabic fonts; Codex CLI and tmux. Reuse the
shared Python environment. Codex account authentication is reused by the CLI;
no credential, cookie or session file is copied into the repository.

```bash
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
Per-book failures and publication state are retained under
`.translation-work/book-state/`. Final queue state distinguishes `complete`,
`finished_with_blockers`, `provider_blocked`, and user-requested `paused`.
An interrupted request with a saved valid response is recovered without a new
API call. Malformed or missing responses still consume the finite content
attempt budget; transport failures refund it because they produced no content.
Transient connection, timeout, rate-limit or server failures may resume the
queue twice after five- and ten-minute cooldowns. No calls run during the wait;
STOP is checked every five seconds. Authentication/payment failures stop for
owner attention, never automatic charging or endless credit checks. Override
with `--transport-resumes` and `--transport-retry-seconds`.

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

Use `repair --repairs PATH.json` for reviewed corrections. The packet records
the book ID and per-row language, source file, segment ID, source hash, complete
restored source, masked translation, and review reason. The tool validates the
entire packet first, backs up changed caches, and schedules every repair for
additional semantic review. Replacing already accepted text also requires its
`previous_sha256`. No full-chapter regeneration is required.

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

The Bunko importer lives in `../Bunko/tools/import_polished_physics.py`; the
published content lives in `../bunko-books`, not in the app repository. It
retains schema 1 and existing book identities and adds aligned `en`, `ja`, `zh`
layers. Coverage checks include front matter, overviews, classroom Q&A,
footnotes, captions and tables. Equations are protected before Pandoc parsing
and every rich expression must render with the app's KaTeX configuration.
Matched passage IDs and old content-addressed files remain valid for readers.
No new translation calls are made by the reader importer.

Release commands after the queue has exited:

```bash
python scripts/audit_reading_editions.py
python ../Bunko/tools/import_polished_physics.py
python ../bunko-books/tools/catalogue.py --write
python scripts/polished_translation.py readme
python scripts/translation_catalog.py --reader ../LazyLearn/docs/leonardsusskind-reader.html
python ../Bunko/tools/check_polished_reader.py
python ../LazyLearn/tests/check_susskind_reader.py
```

The generated catalogue exposes only currently validated translations. It
drives the language links under README covers, all eleven localized availability
notices, and LazyLearn's PDF language selector. Existing English links remain
available. Publish the book PDFs and Bunko catalogue before the website changes;
then run `../LazyLearn/tests/check_susskind_reader.py --live` to verify the actual
published PDFs on desktop and mobile. The reader starts at page width with its
outline closed so a phone's reading area is not covered by the sidebar.

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
