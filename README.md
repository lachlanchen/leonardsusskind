[English](README.md) · [العربية](i18n/README.ar.md) · [Español](i18n/README.es.md) · [Français](i18n/README.fr.md) · [日本語](i18n/README.ja.md) · [한국어](i18n/README.ko.md) · [Tiếng Việt](i18n/README.vi.md) · [中文 (简体)](i18n/README.zh-Hans.md) · [中文（繁體）](i18n/README.zh-Hant.md) · [Deutsch](i18n/README.de.md) · [Русский](i18n/README.ru.md)

[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://lazying.art)

# Leonard Susskind Lecture Notes Repository

[![Archive](https://img.shields.io/badge/archive-active-16a34a?style=flat-square)](#)
[![Subtitles](https://img.shields.io/badge/subtitles-.srt-2563eb?style=flat-square)](#-canonical-paths)
[![Transcripts](https://img.shields.io/badge/transcripts-markdown-0f766e?style=flat-square)](#-canonical-paths)
[![Generated Notes](https://img.shields.io/badge/generated_notes-LaTeX-f97316?style=flat-square)](#-canonical-paths)
[![PDF Outputs](https://img.shields.io/badge/outputs-PDF-a855f7?style=flat-square)](#-canonical-paths)
[![Theoretical Minimum](https://img.shields.io/badge/focus-Theoretical%20Minimum-f59e0b?style=flat-square)](#)

This repository is a physics-study archive centered on Leonard Susskind lectures, the broader *Theoretical Minimum* ecosystem, and transcript-derived companion notes.

It is not only a PDF dump. The repository is organized so that lecture videos, subtitles, Markdown transcripts, generated TeX notes, compiled PDFs, and hand-maintained course folders all live in one place with stable paths.

If any material should not be mirrored here, open an issue or contact the maintainer and it can be reviewed or removed.

> 📘 This repo provides full lecture transcriptions, subtitle files, generated TeX note workflows, and published course PDFs in one organized archive.

## ✨ What This Repo Provides

- Existing hand-maintained course PDFs and LaTeX material in `core_*` and `supplemental_*` folders.
- A paired transcription layer for the lecture archive:
  - `subtitles/` for `.srt`
  - `markdown/` for timestamped Markdown transcripts
- A transcript-to-TeX pipeline in `generated_course_notes/`.
- Imported companion material in `theoretical_minimum_companion_notes/`.
- Reusable LaTeX templates in `template/kaobook` and `template/tuftle`.

English is the canonical README. Translations live in `i18n/` and may lag behind the English file.

## 🎬 Source Playlist

The main transcript and subtitle archive in this repository is derived from this YouTube playlist:

- <https://www.youtube.com/playlist?list=PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG>

## 🗂️ Canonical Paths

| 📚 Layer | 📍 Canonical path | 🧾 What it contains |
|---|---|---|
| Hand-maintained course folders | `core_*`, `supplemental_*` | Existing PDFs, READMEs, and selected LaTeX sources |
| Subtitles | `subtitles/<track>/<subject>/<run>/` | Lecture `.srt` files |
| Markdown transcripts | `markdown/<track>/<subject>/<run>/` | Timestamped lecture transcripts |
| Generated lecture note sources | `generated_course_notes/<track>/<subject>/<run>/chapters/lecture_XX/` | `content.tex`, `lecture.tex`, analysis files, figure notes, and chapter build inputs |
| Generated lecture PDFs | `generated_course_notes/<track>/<subject>/<run>/chapters/lecture_XX/lecture.pdf` | One compiled PDF per lecture |
| Generated merged course PDFs | `generated_course_notes/<track>/<subject>/<run>/course.pdf` | One compiled PDF for the full course run |
| Canonical published Advanced Quantum PDFs | `supplemental_advanced_quantum/course.pdf` and `supplemental_advanced_quantum/lecture_*.pdf` | Reader-facing published artifacts for that track |
| Legacy chapter-10 cosmology build artifacts | `core_cosmology/cosmology_ch10/artifacts/` | PDF and LaTeX build outputs for the older chapter-10 subproject |
| Companion note import | `theoretical_minimum_companion_notes/` | Imported TeX companion notes derived from `weka511/tm` |
| Theoretical Minimum submodule | `the_theoretical_minimum/` | Separate submodule checkout for related material |
| Templates | `template/kaobook/`, `template/tuftle/` | Reusable LaTeX scaffolding |

## 🧭 Root Course Folders

| 🏷️ Group | 📂 Folders |
|---|---|
| Core | `core_classical`, `core_quantum`, `core_special_relativity`, `core_general_relativity`, `core_cosmology`, `core_statistical_mechanics` |
| Supplemental | `supplemental_advanced_quantum`, `supplemental_cosmology_and_black_holes`, `supplemental_higgs_boson`, `supplemental_particle_physics_1`, `supplemental_particle_physics_2`, `supplemental_particle_physics_3`, `supplemental_quantum_entanglement`, `supplemental_relativity`, `supplemental_string_theory` |

## 🚀 How To Use The Repo

### 📖 Read published notes

Open the PDFs in the relevant course folder, for example:

- `core_general_relativity/lesson_1.pdf`
- `core_cosmology/lesson_1.pdf`
- `core_statistical_mechanics/lesson_1.pdf`
- `supplemental_advanced_quantum/course.pdf`

### 📝 Read transcripts directly

For the same lecture archive, use:

- `subtitles/.../*.srt` for subtitle-style reading and timestamp fidelity
- `markdown/.../*.md` for text review, searching, and note generation

### 🧪 Work on transcript-derived notes

The generated-note tree lives under:

- `generated_course_notes/<track>/<subject>/<run>/`

Typical generated outputs include:

- chapter TeX in `chapters/lecture_XX/content.tex`
- lecture PDF in `chapters/lecture_XX/lecture.pdf`
- merged course PDF in `course.pdf`

### 📚 Work on imported companion notes

```bash
./theoretical_minimum_companion_notes/build_all.sh
```

## 🤝 Collaboration

Collaborations are welcome, especially if you want to improve the mathematical quality and reach of Leonard Susskind-related study material.

High-value contribution areas:

- transcript cleanup
  - fix speaker attribution
  - repair timestamps
  - correct physics terms, names, and notation
- TeX improvement
  - turn transcripts into cleaner mathematical exposition
  - improve structure, typography, and cross-references
  - refine generated chapters into durable course notes
- figure and equation work
  - verify extracted lecture frames
  - redraw diagrams in TikZ
  - convert blackboard equations into reliable LaTeX
- broader physics archival work
  - improve *Theoretical Minimum* companion material
  - connect related Susskind lectures, books, and note sets
  - help spread and preserve this body of physics teaching responsibly

If you contribute, prefer focused commits and mention the exact folders, transcripts, or course runs you changed.

> 🛠️ If you care about physics communication, TeX quality, transcript correctness, or preserving Susskind-related teaching material, this repository is meant to be collaboratively improved.

## 🙏 Acknowledgements

- Leonard Susskind for the original lecture content.
- Repository curation and publication tooling: [LazyingArt LLC](https://lazying.art)
- Simon Crase for the companion-note repository imported into `theoretical_minimum_companion_notes/`.
- Companion note source repository: <https://github.com/weka511/tm>
- Existing referenced note sources:
  - <https://www.lapasserelle.com/general_relativity/>
  - <https://www.lapasserelle.com/cosmology/>
  - <https://www.lapasserelle.com/statistical_mechanics/>

## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## License

This repository is licensed under the GNU General Public License v3.0. See [LICENSE](LICENSE).
