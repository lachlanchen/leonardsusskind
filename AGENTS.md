# Repository Guidelines

## Project Structure & Module Organization
This repository is a LaTeX-first archive of Leonard Susskind course notes. Core tracks live in `core_*` directories, supplementary material in `supplemental_*`, shared layouts in `template/kaobook` and `template/tuftle`, images and branding in `figs/`, and translated READMEs in `i18n/`. The [`the_theoretical_minimum`](/home/lachlan/ProjectsLFS/leonardsusskind/the_theoretical_minimum) directory is a Git submodule, so initialize it before editing.

## Build, Test, and Development Commands
There is no root `Makefile` or package manager workflow; build from the specific document directory you touch.

```bash
git submodule update --init --recursive
cd template/kaobook && pdflatex main && makeindex main.idx -s StyleInd.ist && biber main && pdflatex main && pdflatex main
cd core_cosmology/cosmology_ch10 && mkdir -p artifacts && pdflatex -output-directory=artifacts cosmology_ch10.tex && bibtex artifacts/cosmology_ch10 && pdflatex -output-directory=artifacts cosmology_ch10.tex && pdflatex -output-directory=artifacts cosmology_ch10.tex
```

Use `bibtex` or `biber` according to the target document. If a file uses indexes or glossaries, rerun `makeindex` or the relevant glossary step before the final LaTeX passes.

## Coding Style & Naming Conventions
Match the surrounding file style. Most `.tex` sources use minimal indentation, grouped `\usepackage` blocks, and descriptive comments above non-obvious sections. Keep directory names lowercase with underscores, following existing patterns such as `core_general_relativity` and `supplemental_particle_physics_1`. For new docs, prefer clear entry filenames like `main.tex`, `README.md`, or `lesson_10.pdf`.

## Testing Guidelines
There is no automated test suite. Validation is a clean compile of the edited document plus a quick PDF review for broken references, bibliography output, index generation, and missing figures. Do not claim coverage; state exactly which directories you compiled.

## Commit & Pull Request Guidelines
Recent history uses short imperative subjects such as `Add ...` and `Update ...`. Keep commits focused to one track or asset set. PRs should describe the affected directories, note build commands run, and include screenshots when changing README visuals or banner assets. If you update published PDFs, mention whether the underlying `.tex` sources changed too.

## Repository-Specific Notes
The canonical repository is `git@github.com:lachlanchen/leonardsusskind.git`. This checkout is configured to fetch from `lachlanchen` and mirror pushes to both `lachlanchen/leonardsusskind` and `chenmiaomiao/leonardsusskind` via the `github-chenmiaomiao` SSH host alias. Keep English and translated README content aligned when editing contributor-facing docs. Do not commit local-only artifacts such as `.auto-readme-work/` or personal symlinks like `Physics` and `susskind_lecture_videos`.
