# Editorial Revision Status

The generated PDFs are independently edited companion notes reconstructed from machine transcripts, subtitles, selected blackboard frames, and identified references. They are not exact transcripts, Leonard Susskind's original manuscripts, or lecturer-endorsed editions.

## Corpus Baseline

The July 2026 audit covers 19 generated books and 175 chapters. It found systematic prompt-shaped prose, repetitive lecture choreography, forced Q&A and summaries, missing provenance, weak figure metadata, duplicate title pages, and ambiguous authorship declarations. The detailed reproducible audit is maintained in [`Video2Book/references/susskind-corpus-audit-2026-07.md`](../Video2Book/references/susskind-corpus-audit-2026-07.md).

## Revision Order

The approved production queue now covers 15 books and 137 chapters. It revises all nine supplementary courses first, followed by the latest complete Classical Mechanics, Quantum Mechanics, Special Relativity, General Relativity, Statistical Mechanics, and Cosmology runs. The completed Cosmology pilot and three older or partial duplicate runs are excluded from this pass.

The tracked queue is `references/editorial_revision_queue.json`. It uses one persistent full-access `gpt-5.6-sol` writer session at `ultra` reasoning with approvals disabled. Codex saves candidates under `.editorial-revision-work/`; the driver promotes them after validation, commits and pushes each accepted chapter, and resumes from atomic queue state. Each accepted chapter receives an editorial audit, fidelity report, and machine-readable source map. Normal and pocket PDFs are republished only after source, style, figure, and LaTeX gates pass.

## Pilot Result

The Cosmology pilot completed on July 16, 2026. All eight chapters pass the source-fidelity critic and deterministic prose scan, covering 92 verified classroom exchanges, 27 figure decisions, and 222 timestamped source-map entries. The merged 83-page edition compiles without final-pass errors, undefined references, or overfull boxes.

Local 6-by-9-inch review editions were also built at normal and 1.2-times font size. They contain 122 and 152 pages respectively, and both report zero actionable overfulls, page-builder overflows, underfull paragraphs, or leaked TeX sizing tokens. The normal, pocket, and 1.2-times pocket artifacts were visually checked at the cover, front matter, chapter openings, wrapped running heads, equations, Q&A blocks, and retained blackboard figures.

The pilot standard is now approved for the remaining latest-edition queue. Older duplicate editions remain available but will not be revised until the canonical supplementary and core sequence is complete.
