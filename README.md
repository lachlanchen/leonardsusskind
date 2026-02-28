[English](README.md) · [العربية](i18n/README.ar.md) · [Español](i18n/README.es.md) · [Français](i18n/README.fr.md) · [日本語](i18n/README.ja.md) · [한국어](i18n/README.ko.md) · [Tiếng Việt](i18n/README.vi.md) · [中文 (简体)](i18n/README.zh-Hans.md) · [中文（繁體）](i18n/README.zh-Hant.md) · [Deutsch](i18n/README.de.md) · [Русский](i18n/README.ru.md)

<p align="center">
  <img src="https://raw.githubusercontent.com/lachlanchen/lachlanchen/main/logos/banner.png" alt="LazyingArt banner" />
</p>

# Leonard Susskind Lecture Notes Repository


![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg)
![Content Type](https://img.shields.io/badge/content-Lecture%20Notes%20%26%20LaTeX-informational)
![Status](https://img.shields.io/badge/status-Active%20Archive-success)
![LaTeX](https://img.shields.io/badge/tooling-LaTeX-008080)
![i18n](https://img.shields.io/badge/i18n-directory%20ready-orange)

## 📖 Overview
This repository is a content-first archive of lecture-note materials related to Professor Leonard Susskind courses.

The lecture notes of Professor Leonard Susskind. If this violates any copyrights, please contact me to delete this repository. Professor Susskind takes no responsibility for the error or misinformation in the notes, neither do I.

### Primary Goals
- Keep course notes and progress in one place.
- Preserve draft/notes progress visibility across core and supplementary tracks.
- Provide source materials (PDF, TeX, BibTeX, templates) for continued authoring.

## ✨ Features
- Core course tracking and references.
- Supplementary course progress tracking.
- Existing lesson PDFs for several core tracks.
- LaTeX source material in selected tracks.
- Reusable LaTeX templates in `template/tuftle` and `template/kaobook`.
- Repository visuals in `figs/`.

## 📌 Quick Snapshot
| Area | What is available |
|---|---|
| 📚 Notes | Multiple course note sets, with progress tracking |
| 🧪 Source | TeX/BibTeX sources in selected subprojects |
| 🧰 Templates | `template/tuftle` and `template/kaobook` |
| 🌐 i18n | `i18n/` directory exists (currently empty) |

## 🗂️ Project Structure
```text
leonardsusskind/
├── README.md
├── LICENSE
├── tuftle_book_guide.pdf
├── figs/
│   ├── banner.(png|svg)
│   ├── logo.(png|svg)
│   └── logo-w-text.(png|svg)
├── i18n/                      # exists; currently empty
├── core_classical/
├── core_quantum/
├── core_special_relativity/
├── core_general_relativity/   # lesson_1.pdf ... lesson_10.pdf
├── core_cosmology/            # lesson_1.pdf ... lesson_9.pdf + cosmology_ch10/
├── core_statistical_mechanics/# lesson_1.pdf ... lesson_11.pdf
├── supplemental_advanced_quantum/
├── supplemental_cosmology_and_black_holes/
├── supplemental_higgs_boson/
├── supplemental_particle_physics_1/
├── supplemental_particle_physics_2/
├── supplemental_particle_physics_3/
├── supplemental_quantum_entanglement/
├── supplemental_relativity/
├── supplemental_string_theory/
└── template/
   ├── tuftle/
   └── kaobook/
```

## 🧩 Prerequisites
For reading only:
- A PDF reader.

For editing/building TeX materials:
- A LaTeX distribution (TeX Live / MiKTeX).
- `pdflatex`.
- `bibtex` or `biber` depending on subproject.
- `makeindex` for templates that use indexing.

Assumption note:
- There is no single root-level build system (`Makefile`, `package.json`, `pyproject.toml`) in this repository.

## 🚀 Installation
```bash
git clone https://github.com/<your-user>/leonardsusskind.git
cd leonardsusskind
```

No package installation step is required for basic use (reading existing notes).

## 🛠️ Usage
### 1) Read existing notes
- Open PDFs in relevant folders, for example:
  - `core_general_relativity/lesson_1.pdf`
  - `core_cosmology/lesson_1.pdf`
  - `core_statistical_mechanics/lesson_1.pdf`

### 2) Work on LaTeX materials
- Edit `.tex` and `.bib` files in the target course/template folder.
- Compile with the toolchain expected by that folder.

## ⚙️ Configuration
There is no global configuration file.

Configuration is local to each TeX project (document class, bibliography backend, style files, graphics paths), for example:
- `template/kaobook/main.tex`
- `template/tuftle/main.tex`
- `core_cosmology/cosmology_ch10/cosmology_ch10.tex`

## 🧪 Examples
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
`cosmology_ch10.tex` uses `\bibliography{ref}` (BibTeX-style workflow):

```bash
cd core_cosmology/cosmology_ch10
pdflatex cosmology_ch10.tex
bibtex cosmology_ch10
pdflatex cosmology_ch10.tex
pdflatex cosmology_ch10.tex
```

### Example C: View a generated chapter PDF
```bash
xdg-open supplemental_particle_physics_1/ch1/main.pdf
```

## 📝 Development Notes
- This is primarily a documentation/notes repository, not an application codebase.
- Some folders include generated TeX artifacts (`.aux`, `.log`, `.toc`, `.bbl`, etc.) committed in-repo.
- Build commands can vary by subdirectory; follow the local `.tex` conventions.
- `i18n/` exists and is reserved for multilingual README variants.

## 📚 Canonical Course Progress (Preserved and Reorganized)

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

## 🧯 Troubleshooting
- `pdflatex: command not found`
  - Install a LaTeX distribution and ensure binaries are in `PATH`.
- Bibliography/index not appearing
  - Run the required backend (`bibtex` or `biber`) and `makeindex` if used, then rerun `pdflatex`.
- Missing style/class file errors
  - Build from the intended project directory so relative paths to local assets resolve correctly.
- Build output differs across environments
  - This repository contains materials produced in different environments; align package versions where possible.

## 🗺️ Roadmap
- Continue supplementary tracks with real chapter content and source files.
- Improve consistency of per-course README files.
- Add multilingual README files under `i18n/` and keep the language selector synchronized.
- Add a repository-level build guidance section for each subproject that has TeX sources.

## ❤️ Contribution or Donation
One can contribute to this project by forking this project and send a pull request. If this project help you reduce time to develop, you can give me a cup of coffee :)

## 🙏 Acknowledgements
- Professor Leonard Susskind for the original lecture content.
- Existing referenced note sources:
  - https://www.lapasserelle.com/general_relativity/
  - https://www.lapasserelle.com/cosmology/
  - https://www.lapasserelle.com/statistical_mechanics/

## 📄 License
This repository is licensed under the GNU General Public License v3.0. See [LICENSE](LICENSE).
