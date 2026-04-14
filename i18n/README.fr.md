[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)



[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# Dépôt des notes de cours de Leonard Susskind

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

> 🎓 Une archive multilingue des notes de cours de Leonard Susskind, conservant à la fois les PDF finalisés et les sources LaTeX modifiables pour l’étude, la réutilisation et la référence.

---

## Présentation
Ce dépôt est une archive centrée sur le contenu des notes de cours du professeur Leonard Susskind.

> Les notes de cours du professeur Leonard Susskind. Si cela enfreint des droits d’auteur, veuillez me contacter pour supprimer ce dépôt. Le professeur Susskind n’est pas responsable des erreurs ou de la désinformation contenues dans les notes, pas plus que moi.

Il regroupe trois niveaux en un seul endroit :

- Sélection de parcours de notes et suivi de progression au niveau des cours.
- Ressources publiées (`.pdf`) pour la lecture et le partage.
- Fichiers source (`.tex`, `.bib`, modèles) pour les personnes qui maintiennent ou étendent l’archive.

### Objectifs principaux
- Centraliser les notes de cours et l’état d’avancement.
- Conserver la visibilité de la progression (brouillons/notes) pour les parcours principaux et complémentaires.
- Fournir des matériaux sources (PDF, TeX, BibTeX, modèles) pour la production continue.

## Fonctionnalités
- 📚 Suivi de cours principaux et références associées.
- 📌 Suivi de progression des cours complémentaires.
- 📄 PDF de leçons existants pour plusieurs parcours principaux.
- 🧪 Sources LaTeX disponibles dans des parcours sélectionnés.
- 🧷 Modèles LaTeX réutilisables dans `template/tuftle` et `template/kaobook`.
- 🎨 Visuels du dépôt dans `figs/`.
- 🌐 README multilingue dans `i18n/`.

## Aperçu rapide
| Domaine | Ce qui est disponible |
|---|---|
| 📝 Notes | Plusieurs ensembles de notes de cours avec suivi de progression |
| 🧾 Sources | Fichiers TeX/BibTeX dans des sous-projets sélectionnés |
| 🧱 Modèles | `template/tuftle` et `template/kaobook` |
| 🎨 Identité visuelle | `figs/banner.*`, `figs/logo.*`, `figs/logo-w-text.*` |
| 🌍 i18n | `i18n/README.*.md` dans plusieurs langues |

## Table des matières
- [Présentation](#présentation)
- [Fonctionnalités](#fonctionnalités)
- [Aperçu rapide](#aperçu-rapide)
- [Structure du projet](#structure-du-projet)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Configuration](#configuration)
- [Exemples](#exemples)
- [Notes de développement](#notes-de-développement)
- [Progression canonique des cours (préservée et réorganisée)](#progression-canonique-des-cours-préservée-et-réorganisée)
- [Dépannage](#dépannage)
- [Feuille de route](#feuille-de-route)
- [Contribution](#contribution)
- [❤️ Support](#-support)
- [Remerciements](#remerciements)
- [Licence](#licence)

## Structure du projet
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
├── core_classical_mechanics/
│   └── README.md
├── core_quantum_mechanics/
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

## Prérequis
Pour la lecture :
- 📖 Un lecteur PDF (système ou application).

Pour l’édition/compilation de ressources TeX :
- 📦 Une distribution LaTeX (`TeX Live` / `MiKTeX`).
- ⚙️ `pdflatex`.
- 🗂️ `bibtex` ou `biber` selon le sous-projet.
- 🔎 `makeindex` pour les projets qui utilisent des index.

---

Hypothèses :
- Aucun système de build global à la racine (`Makefile`, `package.json`, `pyproject.toml`) n’est visible dans ce dépôt.
- Les workflows de build sont attendus depuis chaque répertoire de sous-projet.

## Installation
```bash
# Clone the repository
git clone https://github.com/lachlanchen/leonardsusskind.git
cd leonardsusskind
```

Ce dépôt adopte une approche centrée sur le contenu. S’il est cloné en miroir ou forké, remplacez l’URL distante par celle de votre propre copie.

Aucune installation de paquet globale n’est requise pour lire les notes existantes.

## Utilisation
### 1) Lire les notes existantes
Ouvrez les PDF dans les dossiers concernés, par exemple :
- `core_general_relativity/lesson_1.pdf`
- `core_cosmology/lesson_1.pdf`
- `core_statistical_mechanics/lesson_1.pdf`
- `supplemental_particle_physics_2/NumberTheory.pdf`

### 2) Rédiger ou étendre des sources LaTeX
- Modifiez les fichiers `.tex` et `.bib` dans le dossier du cours/le modèle visé.
- Compilez selon le flux de travail indiqué par ce dossier.
- Compilez localement afin que les chemins relatifs vers les ressources et styles soient correctement résolus.

### 3) Naviguer par points d’entrée de chaque parcours
Chaque parcours principal dispose de son propre `README.md` avec des notes ciblées, des références et la progression.

## Configuration
Il n’existe pas de fichier de configuration global.

La configuration est propre à chaque projet TeX. Les réglages habituels sont intégrés dans les sources de documents, notamment :
- La classe de document et la configuration des paquets dans `template/kaobook/main.tex`
- Style/structure réutilisable dans `template/kaobook/`
- Moteur de bibliographie et style de citation dans les paires locales `main.tex`/`ref.bib`
- Chemins d’inclusion pour images et ressources spécifiques aux chapitres dans chaque projet

Points de configuration locaux courants :
- `template/kaobook/main.tex`
- `template/tuftle/main.tex`
- `core_cosmology/cosmology_ch10/cosmology_ch10.tex`
- `supplemental_particle_physics_1/ch1/main.tex`
- `supplemental_advanced_quantum/ch1/main.tex`

## Exemples
### Exemple A : Build `template/kaobook`
`template/kaobook/main.tex` présente cette chaîne de compilation :

```bash
cd template/kaobook
pdflatex main
makeindex main.idx -s StyleInd.ist
biber main
pdflatex main
pdflatex main
```

### Exemple B : Build `core_cosmology/cosmology_ch10`
`cosmology_ch10.tex` utilise un flux de travail de type BibTeX :

```bash
cd core_cosmology/cosmology_ch10
pdflatex cosmology_ch10.tex
bibtex cosmology_ch10
pdflatex cosmology_ch10.tex
pdflatex cosmology_ch10.tex
```

### Exemple C : Build `supplemental_particle_physics_1/ch1`
```bash
cd supplemental_particle_physics_1/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### Exemple D : Build `supplemental_advanced_quantum/ch1`
```bash
cd supplemental_advanced_quantum/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### Exemple E : Visualiser le rendu localement
```bash
xdg-open supplemental_particle_physics_1/ch1/main.pdf
```

## Notes de développement
- Il s’agit principalement d’un dépôt de documentation/notes, et non d’une base applicative.
- Certains dossiers incluent des artefacts TeX générés (`.aux`, `.log`, `.toc`, `.bbl`, etc.) versionnés dans le dépôt.
- Les commandes de build peuvent varier selon le sous-répertoire ; suivez les conventions locales `.tex`.
- Des fichiers `README.md` existent par parcours dans les répertoires principaux et complémentaires et doivent rester alignés avec les états de progression annoncés dans le README racine.
- `i18n/` existe et sert aux variantes multilingues du README.
- Le README racine est considéré comme canonical; les versions localisées doivent s’appuyer dessus lors des mises à jour.

## Progression canonique des cours (préservée et réorganisée)

### Cours principaux

#### Mécanique classique
Le manuel de ce cours [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681) a été publié. Vous pouvez l’acheter sur Amazon [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681).

#### Mécanique quantique
Le manuel de ce cours [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903) a été publié. Vous pouvez l’acheter sur Amazon [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903).

#### Relativité restreinte et électrodynamique
Le manuel de ce cours [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065) a été publié. Vous pouvez l’acheter sur Amazon [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065).

#### Tableau de progression principale
| Cours | Avancement brouillon | Avancement des notes | Notes/Référence |
|---|---:|---:|---|
| Relativité générale | 10/10 | 10/10 | Les notes de cours ont été prises sur https://www.lapasserelle.com/general_relativity/ . |
| Cosmologie | 10/10 | 9/10 | Les notes de cours, du chapitre 1 au chapitre 9, ont été prises sur https://www.lapasserelle.com/cosmology/ . Le chapitre 10 est en cours. |
| Mécanique statistique | 11/11 | 10/10 | Les notes de cours ont été prises sur https://www.lapasserelle.com/statistical_mechanics/. |

### Cours complémentaires
| Cours | Avancement brouillon | Avancement des notes |
|---|---:|---:|
| Mécanique quantique avancée | 0/10 | 0/10 |
| Boson de Higgs | 0/1 | 0/1 |
| Intrication quantique | 0/9 | 0/9 |
| Relativité | 0/9 | 0/9 |
| Physique des particules 1 : concepts de base | 6/10 | 0/10 |
| Physique des particules 2 : Modèle standard | 0/10 | 0/10 |
| Physique des particules 3 : supersymétrie et grande unification | 0/10 | 0/10 |
| Théorie des cordes | 0/11 | 10/10 |
| Cosmologie et trous noirs | 0/8 | 0/10 |

### Note sur la fiabilité de progression
- Les tableaux de progression ci-dessus sont conservés tels qu’ils apparaissent dans le README canonique.
- Les fichiers du dépôt contiennent des parcours aboutis et des placeholders ; si une entrée du tableau ne correspond pas au contenu réel d’un dossier, prenez ce tableau comme intention documentée et mettez à jour les deux ensemble lors des prochaines révisions.

## Dépannage
| Problème | Résolution |
|---|---|
| `pdflatex: command not found` | Installez une distribution LaTeX et vérifiez que les exécutables sont dans le `PATH`. |
| Bibliographie/index non visibles | Exécutez le backend requis (`bibtex` ou `biber`) et `makeindex` si nécessaire, puis relancez `pdflatex`. |
| Erreurs de style/classe manquants | Lancez la compilation depuis le répertoire du projet prévu pour que les chemins relatifs des ressources locales se résolvent correctement. |
| Résultats de compilation différents selon l’environnement | Ce dépôt contient des contenus produits dans des environnements variés ; alignez les versions des paquets autant que possible. |
| Liens multilingues obsolètes ou README de langue manquant | Assurez la cohérence de la ligne de langues en tête et des fichiers sous `i18n/`. |
| Discordance de liens markdown GitHub après renommage de dossier | Revalidez en une seule passe les liens de langue racine et toutes les références `i18n/README.*.md`. |

## Feuille de route
- Poursuivre les parcours complémentaires avec du contenu de chapitre réel et des sources.
- Améliorer la cohérence des README par parcours.
- Développer et maintenir les README multilingues sous `i18n/` et garder le sélecteur de langue synchronisé.
- Ajouter une section de guidance de build au niveau du dépôt pour chaque sous-projet possédant des sources TeX.
- Ajouter des extraits de compilation par parcours quand les chaînes d’outils locales diffèrent.
- Ajouter une automatisation légère de validation de l’intégrité des liens entre README et i18n.

## Contribution
Vous pouvez contribuer à ce projet en le forquant puis en soumettant une pull request.

Périmètre de contribution recommandé :
- Ajouter ou améliorer les notes de chapitre et les références.
- Améliorer la qualité des sources LaTeX et les instructions de compilation reproductibles.
- Garder synchronisés les états de progression du README racine et des README par parcours.
- Maintenir la parité des README multilingues sous `i18n/`.

Bonnes pratiques de pull request recommandées :
- Mentionner précisément les dossiers de parcours modifiés.
- Inclure les commandes de compilation LaTeX utilisées (si des fichiers source ont été modifiés).
- Mettre à jour les tableaux de progression pertinents lorsque l’état d’un chapitre change.
- Mettre à jour les readmes dans `i18n/` après modification du README canonique anglais.

## Remerciements
- Professeur Leonard Susskind pour le contenu original des cours.
- Source de notes de référence existante : https://www.lapasserelle.com/general_relativity/
- Source de notes de référence existante : https://www.lapasserelle.com/cosmology/
- Source de notes de référence existante : https://www.lapasserelle.com/statistical_mechanics/

## Licence
Ce dépôt est sous licence GNU General Public License v3.0. Voir [LICENSE](LICENSE).


## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |
