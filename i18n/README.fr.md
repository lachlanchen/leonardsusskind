[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://lazying.art)

# Dépôt des notes de cours de Leonard Susskind

> Dirigé par [LazyingArt LLC](https://lazying.art). Sites web : [lazying.art](https://lazying.art) et [learn.lazying.art](https://learn.lazying.art).

[![Archive](https://img.shields.io/badge/archive-active-16a34a?style=flat-square)](#)
[![Subtitles](https://img.shields.io/badge/subtitles-.srt-2563eb?style=flat-square)](#-repo-layout)
[![Transcripts](https://img.shields.io/badge/transcripts-markdown-0f766e?style=flat-square)](#-repo-layout)
[![Generated Notes](https://img.shields.io/badge/generated_notes-LaTeX-f97316?style=flat-square)](#-repo-layout)
[![PDF Outputs](https://img.shields.io/badge/outputs-PDF-a855f7?style=flat-square)](#-repo-layout)
[![Theoretical Minimum](https://img.shields.io/badge/focus-Theoretical%20Minimum-f59e0b?style=flat-square)](#)

Ce dépôt est une archive d’étude de la physique centrée sur les cours de Leonard Susskind, l’écosystème plus large de *Theoretical Minimum* et les notes complémentaires dérivées de transcriptions.

Il combine des transcriptions de cours, des fichiers de sous-titres, des notes TeX générées, des PDF compilés et des dossiers de cours maintenus à la main dans une structure de répertoires stable.

> 📘 Les transcriptions complètes des cours, les fichiers de sous-titres, les workflows de notes TeX générées et les PDF de cours publiés sont conservés ici dans une seule archive.
>
> 🛠️ L’automatisation de téléchargement, de transcription et de conversion des sous-titres en notes utilisée ici est maintenue dans le dépôt d’outils compagnon [Video2Book](https://github.com/lachlanchen/Video2Book), qui est inclus dans ce dépôt comme sous-module `Video2Book/`.

> **Note d’édition :** les transcriptions horodatées sont produites automatiquement et peuvent contenir des erreurs de reconnaissance. Les livres compilés sont des notes d’accompagnement indépendantes, éditées avec l’aide de l’IA et reconstruites à partir des transcriptions et des tableaux ; ce ne sont ni des transcriptions exactes, ni des manuscrits originaux, ni des éditions approuvées par Leonard Susskind. La [révision éditoriale](../references/editorial_revision_status.md) documente les sources et figures chapitre par chapitre.

## 📚 Livres publiés

> 📷 Les couvertures d’aperçu proviennent de la première page du PDF de chaque cours afin que le README racine et les cartes du site web correspondent toujours exactement au texte et à la mise en page réellement publiés.
>
> 📱 Des éditions de poche / éditions penguin sont également publiées pour les livres terminés :
> [Pocket-size 1.0x](../all_notes/pocket_books/) et [Pocket-size 1.2x](../all_notes/pocket_books_1_2x/).
> Ces versions compactes sont réglées pour une lecture confortable sur des appareils e-ink de 10 pouces et des écrans de type iPad.

<table>
  <tr>
    <td colspan="4"><strong>Principal</strong> · Classique → Quantique → Spéciale → Générale → Statistique → Cosmologie</td>
  </tr>
  <tr>
    <td align="center">
      <a href="../core_classical_mechanics/2011_fall_theoretical_minimum/classical_mechanics_theoretical_minimum.pdf"><img src="../figs/readme-covers/classical_mechanics_theoretical_minimum.png" width="170" alt="Classical Mechanics Theoretical Minimum cover"></a><br>
      <strong>Mécanique classique</strong><br>
      <sub>Automne 2011 Theoretical Minimum</sub>
    </td>
    <td align="center">
      <a href="../core_classical_mechanics/2011_fall_modern_physics_stanford_partial/classical_mechanics_stanford_partial.pdf"><img src="../figs/readme-covers/classical_mechanics_stanford_partial.png" width="170" alt="Classical Mechanics Stanford partial cover"></a><br>
      <strong>Mécanique classique</strong><br>
      <sub>Parcours partiel Stanford</sub>
    </td>
    <td align="center">
      <a href="../core_quantum_mechanics/2012_winter_theoretical_minimum/quantum_mechanics_theoretical_minimum.pdf"><img src="../figs/readme-covers/quantum_mechanics_theoretical_minimum.png" width="170" alt="Quantum Mechanics cover"></a><br>
      <strong>Mécanique quantique</strong><br>
      <sub>Hiver 2012 Theoretical Minimum</sub>
    </td>
    <td align="center">
      <a href="../core_quantum_mechanics/2012_winter_modern_physics_stanford/quantum_mechanics_modern_physics_stanford.pdf"><img src="../figs/readme-covers/quantum_mechanics_modern_physics_stanford_first_page.png" width="170" alt="Quantum Mechanics Modern Physics Stanford cover"></a><br>
      <strong>Mécanique quantique</strong><br>
      <sub>Hiver 2012 Modern Physics Stanford</sub>
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="../core_special_relativity/2012_spring_theoretical_minimum/special_relativity_theoretical_minimum.pdf"><img src="../figs/readme-covers/special_relativity_theoretical_minimum.png" width="170" alt="Special Relativity cover"></a><br>
      <strong>Relativité restreinte</strong><br>
      <sub>Printemps 2012 Theoretical Minimum</sub>
    </td>
    <td align="center">
      <a href="../core_general_relativity/2012_fall_theoretical_minimum/general_relativity_theoretical_minimum.pdf"><img src="../figs/readme-covers/general_relativity_theoretical_minimum.png" width="170" alt="General Relativity cover"></a><br>
      <strong>Relativité générale</strong><br>
      <sub>Automne 2012 Theoretical Minimum</sub>
    </td>
    <td align="center">
      <a href="../core_general_relativity/2008_fall_einsteins_general_theory_of_relativity/general_relativity_2008_fall_einsteins_general_theory_of_relativity.pdf"><img src="../figs/readme-covers/general_relativity_2008_fall_einsteins_general_theory_of_relativity_first_page.png" width="170" alt="General Relativity 2008 cover"></a><br>
      <strong>Relativité générale</strong><br>
      <sub>Automne 2008 théorie générale d’Einstein</sub>
    </td>
    <td align="center">
      <a href="../core_statistical_mechanics/2013_spring_theoretical_minimum/statistical_mechanics_theoretical_minimum.pdf"><img src="../figs/readme-covers/statistical_mechanics_theoretical_minimum_first_page.png" width="170" alt="Statistical Mechanics and Thermodynamics cover"></a><br>
      <strong>Mécanique statistique</strong><br>
      <sub>Printemps 2013 Theoretical Minimum</sub>
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="../core_cosmology/2013_winter_theoretical_minimum/cosmology_theoretical_minimum.pdf"><img src="../figs/readme-covers/cosmology_theoretical_minimum_first_page.png" width="170" alt="Cosmology Theoretical Minimum cover"></a><br>
      <strong>Cosmologie</strong><br>
      <sub>Hiver 2013 Theoretical Minimum</sub>
    </td>
    <td align="center">
      <a href="../core_cosmology/2009_winter_legacy_cosmology/cosmology_legacy.pdf"><img src="../figs/readme-covers/cosmology_legacy.png" width="170" alt="Cosmology legacy cover"></a><br>
      <strong>Cosmologie</strong><br>
      <sub>Parcours hérité hiver 2009</sub>
    </td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td colspan="4"><strong>Complémentaire</strong> · Quantique → Spéciale → Générale → Statistique → Cosmologie</td>
  </tr>
  <tr>
    <td align="center">
      <a href="../supplemental_advanced_quantum/advanced_quantum_mechanics.pdf"><img src="../figs/readme-covers/advanced_quantum_mechanics.png" width="170" alt="Advanced Quantum Mechanics cover"></a><br>
      <strong>Mécanique quantique avancée</strong><br>
      <sub>Livre de cours complémentaire</sub>
    </td>
    <td align="center">
      <a href="../supplemental_quantum_entanglement/quantum_entanglement_part_1.pdf"><img src="../figs/readme-covers/quantum_entanglement_part_1.png" width="170" alt="Quantum Entanglement Part 1 cover"></a><br>
      <strong>Intrication quantique</strong><br>
      <sub>Partie 1</sub>
    </td>
    <td align="center">
      <a href="../supplemental_quantum_entanglement/quantum_entanglement_part_3.pdf"><img src="../figs/readme-covers/quantum_entanglement_part_3.png" width="170" alt="Quantum Entanglement Part 3 cover"></a><br>
      <strong>Intrication quantique</strong><br>
      <sub>Partie 3</sub>
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="../supplemental_particle_physics_1/particle_physics_1_basic_concepts.pdf"><img src="../figs/readme-covers/particle_physics_1_basic_concepts.png" width="170" alt="Particle Physics 1 cover"></a><br>
      <strong>Physique des particules 1</strong><br>
      <sub>Concepts de base</sub>
    </td>
    <td align="center">
      <a href="../supplemental_particle_physics_2/particle_physics_2_standard_model.pdf"><img src="../figs/readme-covers/particle_physics_2_standard_model.png" width="170" alt="Particle Physics 2 cover"></a><br>
      <strong>Physique des particules 2</strong><br>
      <sub>Modèle standard</sub>
    </td>
    <td align="center">
      <a href="../supplemental_particle_physics_3/particle_physics_3_supersymmetry_and_grand_unification.pdf"><img src="../figs/readme-covers/particle_physics_3_supersymmetry_and_grand_unification.png" width="170" alt="Particle Physics 3 cover"></a><br>
      <strong>Physique des particules 3</strong><br>
      <sub>Supersymétrie et grande unification</sub>
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="../supplemental_cosmology_and_black_holes/topics_in_string_theory.pdf"><img src="../figs/readme-covers/topics_in_string_theory_first_page.png" width="170" alt="Topics in String Theory cover"></a><br>
      <strong>Sujets de théorie des cordes</strong><br>
      <sub>Ensemble cosmologie et trous noirs</sub>
    </td>
    <td align="center">
      <a href="../supplemental_string_theory/string_theory_and_m_theory.pdf"><img src="../figs/readme-covers/string_theory_and_m_theory.png" width="170" alt="String Theory and M-Theory cover"></a><br>
      <strong>String Theory and M-Theory</strong><br>
      <sub>Livre de cours complémentaire</sub>
    </td>
    <td align="center">
      <a href="../supplemental_higgs_boson/demystifying_the_higgs_boson.pdf"><img src="../figs/readme-covers/demystifying_the_higgs_boson.png" width="170" alt="Demystifying the Higgs Boson cover"></a><br>
      <strong>Démystifier le boson de Higgs</strong><br>
      <sub>Livre d’un seul cours</sub>
    </td>
  </tr>
</table>

## ✨ Ce que fournit ce dépôt

- Les PDF de cours et le matériel LaTeX existants maintenus à la main dans les dossiers `core_*` et `supplemental_*`.
- Une couche de transcription couplée pour l’archive des cours :
  - `subtitles/` pour les fichiers `.srt`
  - `markdown/` pour les transcriptions Markdown horodatées
- Un pipeline de transcription vers TeX dans `generated_course_notes/`.
- Le sous-module `Video2Book/` pour le téléchargement des playlists, la transcription et l’automatisation de conversion des sous-titres en notes.
- Du matériel compagnon importé dans `theoretical_minimum_companion_notes/`.
- Des modèles LaTeX réutilisables dans `template/kaobook` et `template/tuftle`.

L’anglais est le README canonique. Les traductions se trouvent dans `i18n/` et peuvent être en retard par rapport au fichier anglais.

## 🎬 Playlist source

L’archive principale des transcriptions et des sous-titres de ce dépôt est dérivée de cette playlist YouTube :

- <https://www.youtube.com/playlist?list=PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG>

## 🗂️ Organisation du dépôt

<table>
  <colgroup>
    <col style="width: 33%">
    <col style="width: 33%">
    <col style="width: 34%">
  </colgroup>
  <thead>
    <tr>
      <th>📚 Couche</th>
      <th>📍 Chemin principal</th>
      <th>🧾 Contenu</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Dossiers de cours maintenus à la main</td>
      <td><code>core_*</code>, <code>supplemental_*</code></td>
      <td>Dossiers de cours destinés aux lecteurs, PDF publiés, README et sources LaTeX sélectionnées.</td>
    </tr>
    <tr>
      <td>Sous-titres</td>
      <td><code>subtitles/</code></td>
      <td>Fichiers de sous-titres de cours au format <code>.srt</code>.</td>
    </tr>
    <tr>
      <td>Transcriptions Markdown</td>
      <td><code>markdown/</code></td>
      <td>Transcriptions de cours horodatées utilisées pour la lecture, la recherche et la génération de notes.</td>
    </tr>
    <tr>
      <td>Sources des notes générées</td>
      <td><code>generated_course_notes/</code></td>
      <td>Chapitres TeX dérivés de transcriptions, figures, prompts et matériel de build de cours.</td>
    </tr>
    <tr>
      <td>PDF générés publiés</td>
      <td><code>supplemental_*/</code></td>
      <td>Sorties publiées canoniques pour les cours générés terminés, avec un nom de fichier PDF fusionné spécifique à chaque cours ainsi que des fichiers <code>lecture_XX.pdf</code>.</td>
    </tr>
    <tr>
      <td>Artefacts de build hérités</td>
      <td><code>core_cosmology/cosmology_ch10/artifacts/</code></td>
      <td>Sorties de build conservées pour l’ancien sous-projet de cosmologie du chapitre 10.</td>
    </tr>
    <tr>
      <td>Notes compagnons</td>
      <td><code>theoretical_minimum_companion_notes/</code></td>
      <td>Notes TeX compagnons importées et dérivées du projet <code>weka511/tm</code>.</td>
    </tr>
    <tr>
      <td>Modèles et matériel partagé</td>
      <td><code>template/</code>, <code>figs/</code>, <code>the_theoretical_minimum/</code>, <code>Video2Book/</code></td>
      <td>Modèles LaTeX, branding/ressources partagés, checkout du sous-module associé et sous-module d’automatisation du téléchargement/de la transcription.</td>
    </tr>
  </tbody>
</table>

Dans `subtitles/`, `markdown/` et `generated_course_notes/`, le matériel est organisé par parcours (`core/` ou `supplementary`), puis par matière, puis par session de cours.

Pour les notes générées, chaque dossier de cours contient généralement :

- `chapters/` pour le TeX cours par cours et les PDF de chaque cours
- `figures/` pour les captures extraites des cours et les ressources de figures
- `course.tex` et `course.pdf` pour le livre complet fusionné du cours

## 🧭 Dossiers de cours à la racine

| 🏷️ Groupe | 📂 Dossiers |
|---|---|
| Principal | `core_classical_mechanics`, `core_quantum_mechanics`, `core_special_relativity`, `core_general_relativity`, `core_cosmology`, `core_statistical_mechanics` |
| Complémentaire | `supplemental_advanced_quantum`, `supplemental_cosmology_and_black_holes`, `supplemental_higgs_boson`, `supplemental_particle_physics_1`, `supplemental_particle_physics_2`, `supplemental_particle_physics_3`, `supplemental_quantum_entanglement`, `supplemental_relativity`, `supplemental_string_theory` |

## 🚀 Comment utiliser le dépôt

### 📖 Lire les notes publiées

Ouvrez les PDF dans le dossier de cours concerné, par exemple :

- `../core_classical_mechanics/2011_fall_theoretical_minimum/classical_mechanics_theoretical_minimum.pdf`
- `../core_classical_mechanics/2011_fall_modern_physics_stanford_partial/classical_mechanics_stanford_partial.pdf`
- `../core_quantum_mechanics/2012_winter_theoretical_minimum/quantum_mechanics_theoretical_minimum.pdf`
- `../core_quantum_mechanics/2012_winter_modern_physics_stanford/quantum_mechanics_modern_physics_stanford.pdf`
- `../core_special_relativity/2012_spring_theoretical_minimum/special_relativity_theoretical_minimum.pdf`
- `../core_general_relativity/2012_fall_theoretical_minimum/general_relativity_theoretical_minimum.pdf`
- `../core_cosmology/2013_winter_theoretical_minimum/cosmology_theoretical_minimum.pdf`
- `../core_cosmology/2009_winter_legacy_cosmology/cosmology_legacy.pdf`
- `../core_statistical_mechanics/lesson_1.pdf`
- `../supplemental_advanced_quantum/advanced_quantum_mechanics.pdf`
- `../supplemental_cosmology_and_black_holes/topics_in_string_theory.pdf`
- `../supplemental_higgs_boson/demystifying_the_higgs_boson.pdf`
- `../supplemental_particle_physics_1/particle_physics_1_basic_concepts.pdf`
- `../supplemental_particle_physics_2/particle_physics_2_standard_model.pdf`
- `../supplemental_particle_physics_3/particle_physics_3_supersymmetry_and_grand_unification.pdf`
- `../supplemental_quantum_entanglement/quantum_entanglement_part_1.pdf`
- `../supplemental_quantum_entanglement/quantum_entanglement_part_3.pdf`
- `../supplemental_string_theory/string_theory_and_m_theory.pdf`

### 📝 Lire directement les transcriptions

Utilisez :

- `../subtitles/` pour une lecture de type sous-titres et une fidélité aux horodatages
- `../markdown/` pour la relecture de texte, la recherche et la génération de notes

### ⬇️ Actualiser la playlist source

Utilisez le wrapper parent, qui délègue au sous-module `Video2Book` :

```bash
./scripts/download_susskind_playlist.sh
```

### 🎙️ Lancer la file de transcription

Utilisez les wrappers parents, qui délèguent au sous-module `Video2Book` :

```bash
./scripts/start_transcription_tmux.sh
./scripts/start_transcription_monitor_tmux.sh
```

### 🧪 Travailler sur les notes dérivées des transcriptions

L’espace de travail des notes générées se trouve sous :

- `../generated_course_notes/`

Dans chaque session de cours :

- `chapters/` contient un dossier par cours
- chaque dossier de cours contient le chapitre TeX et son PDF compilé
- `course.pdf` est le PDF complet fusionné du cours pour cette session

Exécutez le curateur de notes via les wrappers parents, qui délèguent au sous-module `Video2Book` :

```bash
./scripts/start_course_notes_tmux.sh
./scripts/start_course_notes_monitor_tmux.sh
```

### 📘 Exporter des PDF compacts au format de poche

Générez des variantes portables 6x9 pouces à partir du LaTeX des cours générés terminés :

```bash
./scripts/export_course_pocket_pdfs.sh
./scripts/export_course_pocket_pdfs.sh --size a5 --suffix a5
```

Les sorties sont écrites par défaut dans `../all_notes/pocket_books/<course>_pocket.pdf` (noms de fichiers
canoniques, avec suffixe personnalisé optionnel via `--suffix`).

### 📚 Travailler sur les notes compagnons importées

```bash
./theoretical_minimum_companion_notes/build_all.sh
```

## 🤝 Collaboration

Les contributions qui améliorent la qualité mathématique, la clarté et la préservation du matériel d’étude lié à Leonard Susskind sont bienvenues.

Les domaines prioritaires incluent :

- nettoyage des transcriptions
  - corriger l’attribution des intervenants
  - réparer les horodatages
  - corriger les termes de physique, les noms et la notation
- amélioration de TeX
  - transformer les transcriptions en un exposé mathématique plus propre
  - améliorer la structure, la typographie et les références croisées
  - affiner les chapitres générés pour en faire des notes de cours durables
- travail sur les figures et les équations
  - vérifier les captures extraites des cours
  - redessiner les diagrammes en TikZ
  - convertir les équations au tableau en LaTeX fiable
- travail d’archivage en physique plus large
  - améliorer le matériel compagnon de *Theoretical Minimum*
  - relier les cours, livres et ensembles de notes connexes de Susskind
  - aider à diffuser et préserver de manière responsable cet ensemble d’enseignement de la physique

Les contributions doivent utiliser des commits ciblés et identifier exactement les dossiers, transcriptions ou sessions de cours modifiés.

## 🙏 Remerciements

- Leonard Susskind pour le contenu original des cours.
- Curatelle du dépôt et outillage de publication : [LazyingArt LLC](https://lazying.art)
- Simon Crase pour le dépôt de notes compagnons importé dans `../theoretical_minimum_companion_notes/`.
- Dépôt source des notes compagnons : <https://github.com/weka511/tm>
- Sources de notes référencées existantes :
  - <https://www.lapasserelle.com/general_relativity/>
  - <https://www.lapasserelle.com/cosmology/>
  - <https://www.lapasserelle.com/statistical_mechanics/>
- Note de provenance pour les anciens ensembles PDF dérivés de La Passerelle :
  - [`../references/lapasserelle_susskind_pdf_provenance.md`](../references/lapasserelle_susskind_pdf_provenance.md)

## ❤️ Soutien

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## Licence

Ce dépôt est distribué sous licence GNU General Public License v3.0. Voir [LICENSE](../LICENSE).
