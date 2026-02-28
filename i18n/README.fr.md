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

> 🎓 Une archive multilingue de supports de cours de Leonard Susskind, préservant à la fois des PDF finalisés et les sources LaTeX éditables pour l’étude, la réutilisation et la référence.

## Présentation
Ce dépôt est une archive centrée sur le contenu regroupant les matériaux de notes de cours issus de l’écosystème d’enseignement du professeur Leonard Susskind.

> Les notes de cours du professeur Leonard Susskind. Si cela enfreint des droits d’auteur, veuillez me contacter pour supprimer ce dépôt. Le professeur Susskind n’est pas responsable des erreurs ou de la désinformation présentes dans les notes, ni moi non plus.

Il combine trois niveaux en un seul endroit :

- Suivi des notes de cours par parcours et progression par matière.
- Documents publiés (`.pdf`) prêts à la lecture et au partage.
- Fichiers sources (`.tex`, `.bib`, modèles) pour les personnes qui maintiennent ou enrichissent l’archive.

### Objectifs principaux
- Regrouper les notes de cours et l’état d’avancement au même endroit.
- Préserver la visibilité de l’avancement des brouillons/notes sur les parcours principaux et complémentaires.
- Fournir des sources (PDF, TeX, BibTeX, modèles) pour poursuivre la rédaction.

## Fonctionnalités
- Suivi et références des cours principaux.
- Suivi de progression des cours complémentaires.
- PDFs de leçons existants pour plusieurs parcours principaux.
- Sources LaTeX dans certains parcours sélectionnés.
- Modèles LaTeX réutilisables dans `template/tuftle` et `template/kaobook`.
- Contenus visuels du dépôt dans `figs/`.
- Ensemble de README multilingues dans `i18n/`.

## Aperçu rapide
| Domaine | Contenu disponible |
|---|---|
| 📝 Notes | Plusieurs jeux de notes de cours avec suivi de progression |
| 🧾 Source | Sources TeX/BibTeX dans des sous-projets sélectionnés |
| 🧱 Templates | `template/tuftle` et `template/kaobook` |
| 🎨 Identité visuelle | `figs/banner.*`, `figs/logo.*`, `figs/logo-w-text.*` |
| 🌍 i18n | `i18n/README.*.md` variantes linguistiques |

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

## Prérequis
Pour la lecture :
- Un lecteur PDF (système ou application).

Pour l’édition et la compilation de contenus TeX :
- Une distribution LaTeX (`TeX Live` / `MiKTeX`).
- `pdflatex`.
- `bibtex` ou `biber` selon le sous-projet.
- `makeindex` pour les projets qui utilisent des entrées indexées.

Hypothèses :
- Il n’existe pas de système de build unique à la racine (`Makefile`, `package.json`, `pyproject.toml`) visible dans ce dépôt.
- Les workflows de build doivent être lancés depuis chaque répertoire de sous-projet.

## Installation
```bash
# Clone the repository
git clone https://github.com/lachlanchen/leonardsusskind.git
cd leonardsusskind
```

Ce dépôt est conçu comme « content-first ». S’il est cloné en miroir ou forké, remplacez l’URL distante par celle de votre copie.

Aucune installation globale de package n’est nécessaire pour lire les notes existantes.

## Utilisation
### 1) Lire les notes existantes
Ouvrez les PDF dans les dossiers concernés, par exemple :
- `core_general_relativity/lesson_1.pdf`
- `core_cosmology/lesson_1.pdf`
- `core_statistical_mechanics/lesson_1.pdf`
- `supplemental_particle_physics_2/NumberTheory.pdf`

### 2) Rédiger ou étendre les matériaux LaTeX
- Modifiez les fichiers `.tex` et `.bib` dans le dossier du cours/modèle ciblé.
- Compilez avec la chaîne d’outils spécifiée par ce dossier.
- Compilez depuis le répertoire local afin que les chemins relatifs vers les assets et styles soient correctement résolus.

### 3) Naviguer via les points d’entrée de chaque parcours
Chaque parcours majeur possède son propre `README.md` avec des notes de portée, des références et l’état de progression.

## Configuration
Il n’existe pas de fichier de configuration global.

La configuration est locale à chaque projet TeX. Les paramètres habituels sont intégrés dans les sources de document, notamment :
- Classe de document et configuration des paquets dans `template/kaobook/main.tex`
- Style/structure réutilisables dans `template/kaobook/`
- Backend bibliographique et style de citation dans les paires locales `main.tex`/`ref.bib`
- Chemins d’inclusion pour les images et les assets spécifiques aux chapitres dans chaque projet

Points de configuration locaux typiques :
- `template/kaobook/main.tex`
- `template/tuftle/main.tex`
- `core_cosmology/cosmology_ch10/cosmology_ch10.tex`
- `supplemental_particle_physics_1/ch1/main.tex`
- `supplemental_advanced_quantum/ch1/main.tex`

## Exemples
### Exemple A : Générer `template/kaobook`
`template/kaobook/main.tex` décrit cette chaîne de compilation :

```bash
cd template/kaobook
pdflatex main
makeindex main.idx -s StyleInd.ist
biber main
pdflatex main
pdflatex main
```

### Exemple B : Générer `core_cosmology/cosmology_ch10`
`cosmology_ch10.tex` utilise un flux de travail de type BibTeX :

```bash
cd core_cosmology/cosmology_ch10
pdflatex cosmology_ch10.tex
bibtex cosmology_ch10
pdflatex cosmology_ch10.tex
pdflatex cosmology_ch10.tex
```

### Exemple C : Générer `supplemental_particle_physics_1/ch1`
```bash
cd supplemental_particle_physics_1/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### Exemple D : Générer `supplemental_advanced_quantum/ch1`
```bash
cd supplemental_advanced_quantum/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### Exemple E : Visualiser la sortie localement
```bash
xdg-open supplemental_particle_physics_1/ch1/main.pdf
```

## Notes de développement
- Il s’agit principalement d’un dépôt de documentation/notes, et non d’une base applicative.
- Certains dossiers contiennent des artefacts TeX générés (`.aux`, `.log`, `.toc`, `.bbl`, etc.) versionnés dans le dépôt.
- Les commandes de build peuvent varier selon le sous-répertoire ; suivez les conventions locales `.tex`.
- Des fichiers `README.md` par parcours existent dans les répertoires principal et complémentaires et doivent rester alignés avec les déclarations de progression du README racine.
- `i18n/` existe et sert aux variantes multilingues du README.
- Le README racine est traité comme canonique ; les fichiers localisés doivent s’y conformer lors des mises à jour.

## Progression canonique des cours (préservée et réorganisée)

### Cours principaux

#### Mécanique classique
Le manuel de ce cours, [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681), a été publié. Vous pouvez l’acheter sur Amazon : [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681).

#### Mécanique quantique
Le manuel de ce cours, [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903), a été publié. Vous pouvez l’acheter sur Amazon : [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903).

#### Relativité restreinte et électrodynamique
Le manuel de ce cours, [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065), a été publié. Vous pouvez l’acheter sur Amazon : [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065).

#### Tableau de progression principal
| Cours | Avancement du brouillon | Avancement des notes | Notes/Référence |
|---|---:|---:|---|
| Relativité générale | 10/10 | 10/10 | Les notes de cours ont été prises sur https://www.lapasserelle.com/general_relativity/ . |
| Cosmologie | 10/10 | 9/10 | Les notes de cours, du chapitre 1 au 9, ont été prises sur https://www.lapasserelle.com/cosmology/ . Le chapitre 10 est en cours. |
| Mécanique statistique | 11/11 | 10/10 | Les notes de cours ont été prises sur https://www.lapasserelle.com/statistical_mechanics/ . |

### Cours complémentaires
| Cours | Avancement du brouillon | Avancement des notes |
|---|---:|---:|
| Mécanique quantique avancée | 0/10 | 0/10 |
| Boson de Higgs | 0/1 | 0/1 |
| Intrication quantique | 0/9 | 0/9 |
| Relativité | 0/9 | 0/9 |
| Physique des particules 1 : notions de base | 6/10 | 0/10 |
| Physique des particules 2 : Modèle standard | 0/10 | 0/10 |
| Physique des particules 3 : supersymétrie et grande unification | 0/10 | 0/10 |
| Théorie des cordes | 0/11 | 10/10 |
| Cosmologie et trous noirs | 0/8 | 0/10 |

### Note d’intégrité de la progression
- Les tableaux de progression ci-dessus sont conservés depuis le texte canonical du README.
- Les fichiers du dépôt comprennent des parcours matures et des placeholders ; si une entrée du tableau semble incohérente avec l’état réel d’un dossier, considérez le tableau comme intention documentée et mettez à jour les deux de manière conjointe lors des révisions futures.

## Dépannage
| Problème | Résolution |
|---|---|
| `pdflatex: command not found` | Installez une distribution LaTeX et assurez-vous que les exécutables sont dans le `PATH`. |
| Bibliographie/index non affichés | Exécutez le backend requis (`bibtex` ou `biber`) et `makeindex` si nécessaire, puis relancez `pdflatex`. |
| Erreurs de style/classe manquantes | Compilez dans le répertoire prévu du projet pour que les chemins relatifs vers les assets locaux soient correctement résolus. |
| Résultats de build différents selon l’environnement | Ce dépôt contient des matériels produits dans différents environnements ; alignez les versions de paquets lorsque possible. |
| Liens multilingues périmés ou README de langue manquant | Veillez à ce que la ligne de langue en tête et les fichiers sous `i18n/` restent synchronisés. |
| Incohérence de liens Markdown GitHub après renommage de dossier | Revalidez les liens de langue racine et toutes les références `i18n/README.*.md` en une seule passe. |

## Feuille de route
- Poursuivre les parcours complémentaires avec de vrais contenus de chapitres et de sources.
- Améliorer la cohérence des README par cours.
- Étendre et maintenir les README multilingues dans `i18n/` et garder le sélecteur de langue synchronisé.
- Ajouter une section d’aide au build au niveau du dépôt pour chaque sous-projet possédant des sources LaTeX.
- Ajouter des extraits de compilation par parcours quand les chaînes d’outils locales diffèrent.
- Ajouter une automatisation légère pour valider l’intégrité des liens entre README et i18n.

## Contribution
Vous pouvez contribuer à ce projet en créant un fork puis en envoyant une pull request.

Périmètre de contribution recommandé :
- Ajouter ou améliorer les notes de chapitre et les références.
- Améliorer la qualité des sources LaTeX et les instructions de compilation reproductibles.
- Maintenir la cohérence des déclarations de progression entre le README racine et les README par parcours.
- Assurer la parité des README multilingues sous `i18n/`.

Bonnes pratiques de pull request recommandées :
- Mentionner précisément les dossiers de parcours modifiés.
- Inclure les commandes de compilation TeX utilisées (si des fichiers sources ont été modifiés).
- Mettre à jour les tableaux de progression pertinents quand l’état d’un chapitre change.
- Mettre à jour les readmes sous `i18n/` après une modification du README canonique anglais.

## Remerciements
- Professeur Leonard Susskind pour le contenu original des cours.
- Source des notes de référence existante : https://www.lapasserelle.com/general_relativity/
- Source des notes de référence existante : https://www.lapasserelle.com/cosmology/
- Source des notes de référence existante : https://www.lapasserelle.com/statistical_mechanics/

## Licence
Ce dépôt est sous licence GNU General Public License v3.0. Voir [LICENSE](LICENSE).


## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |
