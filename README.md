[English](README.md) · [العربية](i18n/README.ar.md) · [Español](i18n/README.es.md) · [Français](i18n/README.fr.md) · [日本語](i18n/README.ja.md) · [한국어](i18n/README.ko.md) · [Tiếng Việt](i18n/README.vi.md) · [中文 (简体)](i18n/README.zh-Hans.md) · [中文（繁體）](i18n/README.zh-Hant.md) · [Deutsch](i18n/README.de.md) · [Русский](i18n/README.ru.md)

[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://lazying.art)

# Leonard Susskind Lecture Notes Repository

> Led by [LazyingArt LLC](https://lazying.art). Websites: [lazying.art](https://lazying.art) and [learn.lazying.art](https://learn.lazying.art).

[![Archive](https://img.shields.io/badge/archive-active-16a34a?style=flat-square)](#)
[![Subtitles](https://img.shields.io/badge/subtitles-.srt-2563eb?style=flat-square)](#-repo-layout)
[![Transcripts](https://img.shields.io/badge/transcripts-markdown-0f766e?style=flat-square)](#-repo-layout)
[![Generated Notes](https://img.shields.io/badge/generated_notes-LaTeX-f97316?style=flat-square)](#-repo-layout)
[![PDF Outputs](https://img.shields.io/badge/outputs-PDF-a855f7?style=flat-square)](#-repo-layout)
[![Theoretical Minimum](https://img.shields.io/badge/focus-Theoretical%20Minimum-f59e0b?style=flat-square)](#)

This repository is a physics-study archive centered on Leonard Susskind lectures, the broader *Theoretical Minimum* ecosystem, and transcript-derived companion notes.

It combines lecture transcriptions, subtitle files, generated TeX notes, compiled PDFs, and hand-maintained course folders in a stable directory structure.

> 📘 Full lecture transcriptions, subtitle files, generated TeX note workflows, and published course PDFs are maintained here in one archive.
>
> 🛠️ The download, transcription, and subtitle-to-notes automation used here is maintained in the companion tool repo [Video2Book](https://github.com/lachlanchen/Video2Book), which is included in this repository as the `Video2Book/` submodule.

## 📚 Published Books

<table>
  <tr>
    <td align="center">
      <a href="core_classical_mechanics/2011_fall_theoretical_minimum/classical_mechanics_theoretical_minimum.pdf"><img src="figs/readme-covers/classical_mechanics_theoretical_minimum.png" width="170" alt="Classical Mechanics Theoretical Minimum cover"></a><br>
      <strong>Classical Mechanics</strong><br>
      <sub>2011 Fall Theoretical Minimum</sub>
    </td>
    <td align="center">
      <a href="core_classical_mechanics/2011_fall_modern_physics_stanford_partial/classical_mechanics_stanford_partial.pdf"><img src="figs/readme-covers/classical_mechanics_stanford_partial.png" width="170" alt="Classical Mechanics Stanford partial cover"></a><br>
      <strong>Classical Mechanics</strong><br>
      <sub>Stanford partial run</sub>
    </td>
    <td align="center">
      <a href="supplemental_advanced_quantum/advanced_quantum_mechanics.pdf"><img src="figs/readme-covers/advanced_quantum_mechanics.png" width="170" alt="Advanced Quantum Mechanics cover"></a><br>
      <strong>Advanced Quantum Mechanics</strong><br>
      <sub>Supplementary course book</sub>
    </td>
    <td align="center">
      <a href="supplemental_cosmology_and_black_holes/topics_in_string_theory.pdf"><img src="figs/readme-covers/topics_in_string_theory.png" width="170" alt="Topics in String Theory cover"></a><br>
      <strong>Topics in String Theory</strong><br>
      <sub>Cosmology and Black Holes set</sub>
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="supplemental_higgs_boson/demystifying_the_higgs_boson.pdf"><img src="figs/readme-covers/demystifying_the_higgs_boson.png" width="170" alt="Demystifying the Higgs Boson cover"></a><br>
      <strong>Demystifying the Higgs Boson</strong><br>
      <sub>Single-lecture book</sub>
    </td>
    <td align="center">
      <a href="supplemental_particle_physics_1/particle_physics_1_basic_concepts.pdf"><img src="figs/readme-covers/particle_physics_1_basic_concepts.png" width="170" alt="Particle Physics 1 cover"></a><br>
      <strong>Particle Physics 1</strong><br>
      <sub>Basic Concepts</sub>
    </td>
    <td align="center">
      <a href="supplemental_particle_physics_2/particle_physics_2_standard_model.pdf"><img src="figs/readme-covers/particle_physics_2_standard_model.png" width="170" alt="Particle Physics 2 cover"></a><br>
      <strong>Particle Physics 2</strong><br>
      <sub>Standard Model</sub>
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="supplemental_particle_physics_3/particle_physics_3_supersymmetry_and_grand_unification.pdf"><img src="figs/readme-covers/particle_physics_3_supersymmetry_and_grand_unification.png" width="170" alt="Particle Physics 3 cover"></a><br>
      <strong>Particle Physics 3</strong><br>
      <sub>Supersymmetry and Grand Unification</sub>
    </td>
    <td align="center">
      <a href="supplemental_quantum_entanglement/quantum_entanglement_part_1.pdf"><img src="figs/readme-covers/quantum_entanglement_part_1.png" width="170" alt="Quantum Entanglement Part 1 cover"></a><br>
      <strong>Quantum Entanglement</strong><br>
      <sub>Part 1</sub>
    </td>
    <td align="center">
      <a href="supplemental_quantum_entanglement/quantum_entanglement_part_3.pdf"><img src="figs/readme-covers/quantum_entanglement_part_3.png" width="170" alt="Quantum Entanglement Part 3 cover"></a><br>
      <strong>Quantum Entanglement</strong><br>
      <sub>Part 3</sub>
    </td>
  </tr>
  <tr>
    <td align="center" colspan="3">
      <a href="supplemental_string_theory/string_theory_and_m_theory.pdf"><img src="figs/readme-covers/string_theory_and_m_theory.png" width="170" alt="String Theory and M-Theory cover"></a><br>
      <strong>String Theory and M-Theory</strong><br>
      <sub>Supplementary course book</sub>
    </td>
  </tr>
</table>

## ✨ What This Repo Provides

- Existing hand-maintained course PDFs and LaTeX material in `core_*` and `supplemental_*` folders.
- A paired transcription layer for the lecture archive:
  - `subtitles/` for `.srt`
  - `markdown/` for timestamped Markdown transcripts
- A transcript-to-TeX pipeline in `generated_course_notes/`.
- The `Video2Book/` submodule for playlist download, transcription, and subtitle-to-notes automation.
- Imported companion material in `theoretical_minimum_companion_notes/`.
- Reusable LaTeX templates in `template/kaobook` and `template/tuftle`.

English is the canonical README. Translations live in `i18n/` and may lag behind the English file.

## 🎬 Source Playlist

The main transcript and subtitle archive in this repository is derived from this YouTube playlist:

- <https://www.youtube.com/playlist?list=PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG>

## 🗂️ Repo Layout

<table>
  <colgroup>
    <col style="width: 33%">
    <col style="width: 33%">
    <col style="width: 34%">
  </colgroup>
  <thead>
    <tr>
      <th>📚 Layer</th>
      <th>📍 Main path</th>
      <th>🧾 What it contains</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Hand-maintained course folders</td>
      <td><code>core_*</code>, <code>supplemental_*</code></td>
      <td>Reader-facing course folders, published PDFs, READMEs, and selected LaTeX sources.</td>
    </tr>
    <tr>
      <td>Subtitles</td>
      <td><code>subtitles/</code></td>
      <td>Lecture subtitle files in <code>.srt</code> format.</td>
    </tr>
    <tr>
      <td>Markdown transcripts</td>
      <td><code>markdown/</code></td>
      <td>Timestamped lecture transcripts used for reading, search, and note generation.</td>
    </tr>
    <tr>
      <td>Generated note sources</td>
      <td><code>generated_course_notes/</code></td>
      <td>Transcript-derived TeX chapters, figures, prompts, and course build material.</td>
    </tr>
    <tr>
      <td>Published generated PDFs</td>
      <td><code>supplemental_*/</code></td>
      <td>Canonical published outputs for finished generated courses, using a course-specific merged PDF filename plus <code>lecture_XX.pdf</code> files.</td>
    </tr>
    <tr>
      <td>Legacy build artifacts</td>
      <td><code>core_cosmology/cosmology_ch10/artifacts/</code></td>
      <td>Build outputs kept for the older chapter-10 cosmology subproject.</td>
    </tr>
    <tr>
      <td>Companion notes</td>
      <td><code>theoretical_minimum_companion_notes/</code></td>
      <td>Imported TeX companion notes derived from the <code>weka511/tm</code> project.</td>
    </tr>
    <tr>
      <td>Templates and shared material</td>
      <td><code>template/</code>, <code>figs/</code>, <code>the_theoretical_minimum/</code>, <code>Video2Book/</code></td>
      <td>LaTeX templates, shared branding/assets, the related submodule checkout, and the download/transcription automation submodule.</td>
    </tr>
  </tbody>
</table>

Within `subtitles/`, `markdown/`, and `generated_course_notes/`, material is organized by track (`core/` or `supplementary/`), then subject, then course run.

For generated notes, each course folder usually contains:

- `chapters/` for lecture-by-lecture TeX and per-lecture PDFs
- `figures/` for extracted lecture frames and figure assets
- `course.tex` and `course.pdf` for the merged full-course book

## 🧭 Root Course Folders

| 🏷️ Group | 📂 Folders |
|---|---|
| Core | `core_classical_mechanics`, `core_quantum_mechanics`, `core_special_relativity`, `core_general_relativity`, `core_cosmology`, `core_statistical_mechanics` |
| Supplemental | `supplemental_advanced_quantum`, `supplemental_cosmology_and_black_holes`, `supplemental_higgs_boson`, `supplemental_particle_physics_1`, `supplemental_particle_physics_2`, `supplemental_particle_physics_3`, `supplemental_quantum_entanglement`, `supplemental_relativity`, `supplemental_string_theory` |

## 🚀 How To Use The Repo

### 📖 Read published notes

Open the PDFs in the relevant course folder, for example:

- `core_general_relativity/lesson_1.pdf`
- `core_cosmology/lesson_1.pdf`
- `core_statistical_mechanics/lesson_1.pdf`
- `core_classical_mechanics/2011_fall_theoretical_minimum/classical_mechanics_theoretical_minimum.pdf`
- `core_classical_mechanics/2011_fall_modern_physics_stanford_partial/classical_mechanics_stanford_partial.pdf`
- `supplemental_advanced_quantum/advanced_quantum_mechanics.pdf`
- `supplemental_cosmology_and_black_holes/topics_in_string_theory.pdf`
- `supplemental_higgs_boson/demystifying_the_higgs_boson.pdf`
- `supplemental_particle_physics_1/particle_physics_1_basic_concepts.pdf`
- `supplemental_particle_physics_2/particle_physics_2_standard_model.pdf`
- `supplemental_particle_physics_3/particle_physics_3_supersymmetry_and_grand_unification.pdf`
- `supplemental_quantum_entanglement/quantum_entanglement_part_1.pdf`
- `supplemental_quantum_entanglement/quantum_entanglement_part_3.pdf`
- `supplemental_string_theory/string_theory_and_m_theory.pdf`

### 📝 Read transcripts directly

Use:

- `subtitles/` for subtitle-style reading and timestamp fidelity
- `markdown/` for text review, searching, and note generation

### ⬇️ Refresh the source playlist

Use the parent wrapper, which delegates to the `Video2Book` submodule:

```bash
./scripts/download_susskind_playlist.sh
```

### 🎙️ Run the transcription queue

Use the parent wrappers, which delegate to the `Video2Book` submodule:

```bash
./scripts/start_transcription_tmux.sh
./scripts/start_transcription_monitor_tmux.sh
```

### 🧪 Work on transcript-derived notes

The generated-note workspace lives under:

- `generated_course_notes/`

Within each course run:

- `chapters/` holds one folder per lecture
- each lecture folder contains the chapter TeX and its compiled lecture PDF
- `course.pdf` is the merged full-course PDF for that run

Run the note curator through the parent wrappers, which delegate to the `Video2Book` submodule:

```bash
./scripts/start_course_notes_tmux.sh
./scripts/start_course_notes_monitor_tmux.sh
```

### 📚 Work on imported companion notes

```bash
./theoretical_minimum_companion_notes/build_all.sh
```

## 🤝 Collaboration

Contributions that improve the mathematical quality, clarity, and preservation of Leonard Susskind-related study material are welcome.

Priority areas include:

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

Contributions should use focused commits and identify the exact folders, transcripts, or course runs changed.

## 🙏 Acknowledgements

- Leonard Susskind for the original lecture content.
- Repository curation and publication tooling: [LazyingArt LLC](https://lazying.art)
- Simon Crase for the companion-note repository imported into `theoretical_minimum_companion_notes/`.
- Companion note source repository: <https://github.com/weka511/tm>
- Existing referenced note sources:
  - <https://www.lapasserelle.com/general_relativity/>
  - <https://www.lapasserelle.com/cosmology/>
  - <https://www.lapasserelle.com/statistical_mechanics/>
- Provenance note for the older La Passerelle-derived PDF sets:
  - [`references/lapasserelle_susskind_pdf_provenance.md`](references/lapasserelle_susskind_pdf_provenance.md)

## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## License

This repository is licensed under the GNU General Public License v3.0. See [LICENSE](LICENSE).
