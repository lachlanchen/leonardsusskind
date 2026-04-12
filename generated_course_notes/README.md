# Generated Course Notes

This tree holds transcript-derived lecture notes generated from the repository’s `markdown/` transcripts and sampled video frames.

Design goals:

- keep generated material separate from the hand-maintained `core_*` and `supplemental_*` note trees
- preserve the original course hierarchy under `generated_course_notes/`
- compile each lecture as its own PDF, then rebuild a full course PDF at the course root
- advance strictly course by course, with `supplementary/*` processed before `core/*`
- only start a course when both `markdown/` and `subtitles/` fully cover that course’s source videos

Structure:

```text
generated_course_notes/
  core|supplementary/<subject>/<run>/
    common_preamble.tex
    course.tex
    course.pdf
    assets/
    chapters/
      lecture_01/
        analysis.md
        visual_notes.md
        narrative_map.md
        math_bank.md
        draft.tex
        content.tex
        lecture.tex
        lecture.pdf
        metadata.json
```

Main commands:

```bash
python3 scripts/generate_course_notes.py --print-next
python3 scripts/generate_course_notes.py --lecture "supplementary/advanced_quantum_mechanics/2013_fall/185 - Advanced Quantum Mechanics Lecture 1 [8mi0PoPvLvs].md"
bash scripts/process_course_notes_one_by_one.sh
bash scripts/start_course_notes_tmux.sh --no-attach
```

Defaults:

- note-writing model: `gpt-5.3-codex-spark`
- reasoning: `xhigh`
- generation order: fully transcribed supplementary courses first, then core courses
- when available, prompts also use local Susskind-authored PDFs from `susskind-books-and-lecture-notes/` as a style and notation reference
- each lecture now runs through explicit stages: frame review, plan, visual equation/diagram extraction, narrative map, math bank, LaTeX draft, refinement, compile, and course-book rebuild
- after each material edit stage, the loop triggers a codex-driven commit/push step so progress is preserved incrementally
- every prompt stage receives the corresponding lecture transcript path and the full transcript text for that lecture
- the writer loop reuses one shared non-interactive Codex session id from `.lecture-notes-work/codex_sessions/susskind-notes.session_id` so prompt stages accumulate local task context across steps and lectures
- the current shared session is documented at `.lecture-notes-work/codex_sessions/susskind-notes.session.md`, including the tmux session name and the live Codex session id

Runtime prompts, logs, and temporary compile artifacts live under `.lecture-notes-work/` and are intentionally not tracked.
