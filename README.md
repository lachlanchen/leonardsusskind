[English](README.md) · [العربية](i18n/README.ar.md) · [Español](i18n/README.es.md) · [Français](i18n/README.fr.md) · [日本語](i18n/README.ja.md) · [한국어](i18n/README.ko.md) · [Tiếng Việt](i18n/README.vi.md) · [中文 (简体)](i18n/README.zh-Hans.md) · [中文（繁體）](i18n/README.zh-Hant.md) · [Deutsch](i18n/README.de.md) · [Русский](i18n/README.ru.md)



[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# Leonard Susskind Lecture Notes Repository

![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg)
![Content Type](https://img.shields.io/badge/content-Lecture%20Notes%20%26%20LaTeX-informational)
![Status](https://img.shields.io/badge/status-Active%20Archive-success)
![LaTeX](https://img.shields.io/badge/tooling-LaTeX-008080)
![Core Tracks](https://img.shields.io/badge/core_tracks-6-1f6feb)
![Supplemental Tracks](https://img.shields.io/badge/supplemental_tracks-9-9a6700)
![i18n](https://img.shields.io/badge/i18n-10%20translations%20%2B%20English-orange)
![Stars](https://img.shields.io/github/stars/lachlanchen/leonardsusskind?style=flat-square&logo=github&label=stars&color=22c55e)
![Forks](https://img.shields.io/github/forks/lachlanchen/leonardsusskind?style=flat-square&logo=github&label=forks&color=3b82f6)
![Last Commit](https://img.shields.io/github/last-commit/lachlanchen/leonardsusskind?style=flat-square&color=8b5cf6)

> 🎓 A multilingual archive of Leonard Susskind lecture-note materials, preserving both polished PDFs and editable LaTeX sources for study, reuse, and reference.

---

## Overview
This repository is a content-first archive of lecture-note materials from Professor Leonard Susskind's teaching ecosystem.

> The lecture notes of Professor Leonard Susskind. If this violates any copyrights, please contact me to delete this repository. Professor Susskind takes no responsibility for the error or misinformation in the notes, neither do I.

It combines three layers in one place:

- Curated note tracks and course-level progress.
- Published artifacts (`.pdf`) for reading and sharing.
- Source files (`.tex`, `.bib`, templates) for people who maintain or extend the archive.

### Primary Goals
- Keep course notes and progress in one place.
- Preserve draft/notes progress visibility across core and supplementary tracks.
- Provide source materials (PDF, TeX, BibTeX, templates) for continued authoring.

## Features
- 📚 Core course tracking and references.
- 📌 Supplementary course progress tracking.
- 📄 Existing lesson PDFs for several core tracks.
- 🧪 LaTeX source material in selected tracks.
- 🧷 Reusable LaTeX templates in `template/tuftle` and `template/kaobook`.
- 🎨 Repository visuals in `figs/`.
- 🌐 Multilingual README set in `i18n/`.

## Quick Snapshot
| Area | What is available |
|---|---|
| 📝 Notes | Multiple course note sets with progress tracking |
| 🧾 Source | TeX/BibTeX sources in selected subprojects |
| 🧱 Templates | `template/tuftle` and `template/kaobook` |
| 🎨 Branding | `figs/banner.*`, `figs/logo.*`, `figs/logo-w-text.*` |
| 🌍 i18n | `i18n/README.*.md` language variants |

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Quick Snapshot](#quick-snapshot)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Examples](#examples)
- [Development Notes](#development-notes)
- [Canonical Course Progress (Preserved and Reorganized)](#canonical-course-progress-preserved-and-reorganized)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)
- [Contribution](#contribution)
- [❤️ Support](#-support)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## Project Structure
```text
leonardsusskind/
├── README.md
├── LICENSE
├── tuftle_book_guide.pdf
├── figs/
│   ├── banner.(png|svg)
│   ├── logo.(png|svg)
│   └── logo-w-text.(png|svg)
├── i18n/
│   ├── README.ar.md
│   ├── README.de.md
│   ├── README.es.md
│   ├── README.fr.md
│   ├── README.ja.md
│   ├── README.ko.md
│   ├── README.ru.md
│   ├── README.vi.md
│   ├── README.zh-Hans.md
│   └── README.zh-Hant.md
├── core_classical/
│   └── README.md
├── core_quantum/
│   └── README.md
├── core_special_relativity/
│   └── README.md
├── core_general_relativity/
│   ├── README.md
│   └── lesson_1.pdf ... lesson_10.pdf
├── core_cosmology/
│   ├── README.md
│   ├── lesson_1.pdf ... lesson_9.pdf
│   └── cosmology_ch10/
│       ├── cosmology_ch10.tex
│       └── ref.bib
├── core_statistical_mechanics/
│   ├── README.md
│   └── lesson_1.pdf ... lesson_11.pdf
├── supplemental_advanced_quantum/
│   ├── README.md
│   └── ch1/
│       ├── main.tex
│       ├── book_1_template.tex
│       └── bibliography.bib
├── supplemental_cosmology_and_black_holes/
│   └── README.md
├── supplemental_higgs_boson/
│   └── README.md
├── supplemental_particle_physics_1/
│   ├── README.md
│   ├── ch1/
│   │   ├── main.tex
│   │   ├── book_1_template.tex
│   │   └── bibliography.bib
│   └── lecture transcript .txt files
├── supplemental_particle_physics_2/
│   ├── README.md
│   ├── NumberTheory.pdf
│   └── lecture transcript .txt files
├── supplemental_particle_physics_3/
│   └── README.md
├── supplemental_quantum_entanglement/
│   └── README.md
├── supplemental_relativity/
│   └── README.md
├── supplemental_string_theory/
│   └── README.md
└── template/
    ├── kaobook/
    │   ├── main.tex
    │   ├── structure.tex
    │   └── bibliography.bib
    └── tuftle/
        ├── main.tex
        ├── book_1_template.tex
        └── bibliography.bib
```

## Prerequisites
For reading:
- 📖 A PDF reader (system or app-based).

For editing/building TeX materials:
- 📦 A LaTeX distribution (TeX Live / MiKTeX).
- ⚙️ `pdflatex`.
- 🗂️ `bibtex` or `biber` depending on subproject.
- 🔎 `makeindex` for projects that use indexed entries.

---

Assumption notes:
- There is no single root-level build system (`Makefile`, `package.json`, `pyproject.toml`) visible in this repository.
- Build workflows are expected to be run from each subproject directory.

## Installation
```bash
# Clone the repository
git clone https://github.com/lachlanchen/leonardsusskind.git
cd leonardsusskind
```

This repository is content-first. If it is mirrored or forked, replace the remote URL with your own copy accordingly.

No global package install is required to read existing notes.

## Usage
### 1) Read existing notes
Open PDFs in relevant folders, for example:
- `core_general_relativity/lesson_1.pdf`
- `core_cosmology/lesson_1.pdf`
- `core_statistical_mechanics/lesson_1.pdf`
- `supplemental_particle_physics_2/NumberTheory.pdf`

### 2) Author or extend LaTeX materials
- Edit `.tex` and `.bib` files in the target course/template folder.
- Compile with the workflow specified by that folder.
- Build in-place so local relative assets and style files resolve correctly.

### 3) Navigate by track-level entry points
Each major track has its own `README.md` with scoped scope notes, references, and progress.

## Configuration
There is no global configuration file.

Configuration is local to each TeX project. Typical knobs are embedded in document sources, including:
- Document class and package setup in `template/kaobook/main.tex`
- Reusable style/structure in `template/kaobook/`
- Bibliography backend and cite style in local `main.tex`/`ref.bib` pairs
- Include paths for images and chapter-specific assets in each project

Representative local configuration points:
- `template/kaobook/main.tex`
- `template/tuftle/main.tex`
- `core_cosmology/cosmology_ch10/cosmology_ch10.tex`
- `supplemental_particle_physics_1/ch1/main.tex`
- `supplemental_advanced_quantum/ch1/main.tex`

## Examples
### Example A: Build `template/kaobook`
`template/kaobook/main.tex` documents this compile chain:

```bash
cd template/kaobook
pdflatex main
makeindex main.idx -s StyleInd.ist
biber main
pdflatex main
pdflatex main
```

### Example B: Build `core_cosmology/cosmology_ch10`
`cosmology_ch10.tex` uses a BibTeX-style workflow:

```bash
cd core_cosmology/cosmology_ch10
pdflatex cosmology_ch10.tex
bibtex cosmology_ch10
pdflatex cosmology_ch10.tex
pdflatex cosmology_ch10.tex
```

### Example C: Build `supplemental_particle_physics_1/ch1`
```bash
cd supplemental_particle_physics_1/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### Example D: Build `supplemental_advanced_quantum/ch1`
```bash
cd supplemental_advanced_quantum/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### Example E: View output locally
```bash
xdg-open supplemental_particle_physics_1/ch1/main.pdf
```

## Development Notes
- This is primarily a documentation/notes repository, not an application codebase.
- Some folders include generated TeX artifacts (`.aux`, `.log`, `.toc`, `.bbl`, etc.) committed in-repo.
- Build commands can vary by subdirectory; follow the local `.tex` conventions.
- Per-track `README.md` files exist across core and supplemental directories and should be kept aligned with root-level progress claims.
- `i18n/` exists and is used for multilingual README variants.
- The root README is treated as canonical; localized files should follow it when updated.

## Canonical Course Progress (Preserved and Reorganized)

### Core Courses

#### Classical Mechanics
The textbook of this courses [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681) had been published. You can buy it from Amazon [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681).

#### Quantum Mechanics
The textbook of this courses [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903) had been published. You can buy it from Amazon [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903).

#### Special Relativity and Electrodynamics
The textbook of this courses [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065) had been published. You can buy it from Amazon [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065).

#### Core Progress Table
| Course | Draft Progress | Notes Progress | Notes/Reference |
|---|---:|---:|---|
| General Relativity | 10/10 | 10/10 | The lecture notes had been taken by https://www.lapasserelle.com/general_relativity/ . |
| Cosmology | 10/10 | 9/10 | The lecture notes, from chapter 1 to 9, had been taken by https://www.lapasserelle.com/cosmology/ . The chapter 10 is in the process. |
| Statistical Mechanics | 11/11 | 10/10 | The lecture notes had been taken by https://www.lapasserelle.com/statistical_mechanics/. |

### Supplementary Courses
| Course | Draft Progress | Notes Progress |
|---|---:|---:|
| Advanced Quantum Mechanics | 0/10 | 0/10 |
| Higgs Boson | 0/1 | 0/1 |
| Quantum Entanglement | 0/9 | 0/9 |
| Relativity | 0/9 | 0/9 |
| Particle Physics 1: Basic Concepts | 6/10 | 0/10 |
| Particle Physics 2: Standard Model | 0/10 | 0/10 |
| Particle Physics 3: Supersymmetry and Grand Unification | 0/10 | 0/10 |
| String Theory | 0/11 | 10/10 |
| Cosmology and Black Holes | 0/8 | 0/10 |

### Progress Integrity Note
- The progress tables above are preserved from the canonical README text.
- Repository files include both mature and placeholder tracks; if a table entry and folder state appear inconsistent, treat the table as the documented intent and update both together in future revisions.

## Troubleshooting
| Issue | Resolution |
|---|---|
| `pdflatex: command not found` | Install a LaTeX distribution and ensure binaries are in `PATH`. |
| Bibliography/index not appearing | Run the required backend (`bibtex` or `biber`) and `makeindex` if used, then rerun `pdflatex`. |
| Missing style/class file errors | Build from the intended project directory so relative paths to local assets resolve correctly. |
| Build output differs across environments | This repository contains materials produced in different environments; align package versions where possible. |
| Stale multilingual links or missing language README | Ensure the top language options line and files under `i18n/` stay synchronized. |
| GitHub markdown link mismatch after folder rename | Revalidate root-language links and all `i18n/README.*.md` references in one pass. |

## Roadmap
- Continue supplementary tracks with real chapter content and source files.
- Improve consistency of per-course README files.
- Expand and maintain multilingual README files under `i18n/` and keep the language selector synchronized.
- Add a repository-level build guidance section for each subproject that has TeX sources.
- Add per-track compile snippets where local toolchain differences exist.
- Add minimal automation to validate README/i18n link integrity.

## Contribution
You can contribute to this project by forking it and sending a pull request.

Suggested contribution scope:
- Add or improve chapter notes and references.
- Improve TeX source quality and reproducible build instructions.
- Keep root and per-track README progress statements synchronized.
- Maintain multilingual README parity under `i18n/`.

Recommended pull request hygiene:
- Mention the exact track folder(s) changed.
- Include the TeX compile commands used (if source files were edited).
- Update relevant progress tables when chapter state changes.
- Update `i18n/` readmes after canonical English README changes.

## Acknowledgements
- Professor Leonard Susskind for the original lecture content.
- Existing referenced note source: https://www.lapasserelle.com/general_relativity/
- Existing referenced note source: https://www.lapasserelle.com/cosmology/
- Existing referenced note source: https://www.lapasserelle.com/statistical_mechanics/

## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## License
This repository is licensed under the GNU General Public License v3.0. See [LICENSE](LICENSE).
