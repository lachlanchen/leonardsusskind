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

## Vue d'ensemble
Ce dépôt est une archive orientée contenu de supports de notes de cours liés aux cours du professeur Leonard Susskind.

> Les notes de cours du professeur Leonard Susskind. Si cela enfreint des droits d'auteur, veuillez me contacter pour que je supprime ce dépôt. Le professeur Susskind n'assume aucune responsabilité concernant les erreurs ou informations inexactes contenues dans ces notes, moi non plus.

### Objectifs principaux
- Regrouper les notes de cours et leur avancement au même endroit.
- Préserver la visibilité de la progression des brouillons/notes sur les parcours principaux et complémentaires.
- Fournir les sources (PDF, TeX, BibTeX, modèles) pour poursuivre la rédaction.

## Fonctionnalités
- Suivi et références des cours principaux.
- Suivi de progression des cours complémentaires.
- PDF de leçons existants pour plusieurs parcours principaux.
- Sources LaTeX dans certains parcours.
- Modèles LaTeX réutilisables dans `template/tuftle` et `template/kaobook`.
- Ressources visuelles du dépôt dans `figs/`.
- Ensemble de README multilingues dans `i18n/`.

## Aperçu rapide
| Domaine | Contenu disponible |
|---|---|
| 📝 Notes | Plusieurs ensembles de notes de cours avec suivi de progression |
| 🧾 Source | Sources TeX/BibTeX dans certains sous-projets |
| 🧱 Modèles | `template/tuftle` et `template/kaobook` |
| 🎨 Identité visuelle | `figs/banner.*`, `figs/logo.*`, `figs/logo-w-text.*` |
| 🌍 i18n | Variantes de langue `i18n/README.*.md` |

## Table des matières
- [Vue d'ensemble](#vue-densemble)
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
Pour la lecture uniquement :
- Un lecteur PDF.

Pour modifier/compiler des contenus TeX :
- Une distribution LaTeX (TeX Live / MiKTeX).
- `pdflatex`.
- `bibtex` ou `biber` selon le sous-projet.
- `makeindex` pour les modèles qui utilisent l'indexation.

Note d'hypothèse :
- Il n'existe pas de système de build unique à la racine (`Makefile`, `package.json`, `pyproject.toml`) dans ce dépôt.

## Installation
```bash
git clone https://github.com/<your-user>/leonardsusskind.git
cd leonardsusskind
```

Si ce dépôt est forké ou mis en miroir, remplacez `<your-user>` par le compte approprié.

Aucune étape d'installation de package n'est requise pour un usage de base (lecture des notes existantes).

## Utilisation
### 1) Lire les notes existantes
Ouvrez les PDF dans les dossiers concernés, par exemple :
- `core_general_relativity/lesson_1.pdf`
- `core_cosmology/lesson_1.pdf`
- `core_statistical_mechanics/lesson_1.pdf`
- `supplemental_particle_physics_2/NumberTheory.pdf`

### 2) Travailler sur les contenus LaTeX
- Modifiez les fichiers `.tex` et `.bib` dans le dossier du cours/modèle ciblé.
- Compilez avec la chaîne d'outils attendue par ce dossier.
- Il est préférable d'exécuter les commandes de build depuis le répertoire du projet local afin que les chemins relatifs soient correctement résolus.

### 3) Naviguer via les fichiers README des parcours
Chaque parcours majeur possède son propre `README.md` local pour des notes ciblées et le contexte de progression.

## Configuration
Il n'existe pas de fichier de configuration global.

La configuration est locale à chaque projet TeX (classe de document, backend bibliographique, fichiers de style, chemins des ressources graphiques), par exemple :
- `template/kaobook/main.tex`
- `template/tuftle/main.tex`
- `core_cosmology/cosmology_ch10/cosmology_ch10.tex`
- `supplemental_particle_physics_1/ch1/main.tex`
- `supplemental_advanced_quantum/ch1/main.tex`

## Exemples
### Exemple A : Compiler `template/kaobook`
`template/kaobook/main.tex` documente cette chaîne de compilation :

```bash
cd template/kaobook
pdflatex main
makeindex main.idx -s StyleInd.ist
biber main
pdflatex main
pdflatex main
```

### Exemple B : Compiler `core_cosmology/cosmology_ch10`
`cosmology_ch10.tex` utilise `\bibliography{ref}` (workflow de type BibTeX) :

```bash
cd core_cosmology/cosmology_ch10
pdflatex cosmology_ch10.tex
bibtex cosmology_ch10
pdflatex cosmology_ch10.tex
pdflatex cosmology_ch10.tex
```

### Exemple C : Compiler un chapitre basé sur Tufte (`supplemental_particle_physics_1/ch1`)
```bash
cd supplemental_particle_physics_1/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### Exemple D : Compiler un chapitre basé sur Tufte (`supplemental_advanced_quantum/ch1`)
```bash
cd supplemental_advanced_quantum/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### Exemple E : Afficher un PDF de chapitre généré
```bash
xdg-open supplemental_particle_physics_1/ch1/main.pdf
```

## Notes de développement
- Il s'agit principalement d'un dépôt de documentation/notes, pas d'une base de code applicative.
- Certains dossiers incluent des artefacts TeX générés (`.aux`, `.log`, `.toc`, `.bbl`, etc.) versionnés dans le dépôt.
- Les commandes de build peuvent varier selon les sous-répertoires ; suivez les conventions `.tex` locales.
- Des fichiers `README.md` par parcours existent dans les répertoires principaux/complémentaires et doivent rester alignés avec les déclarations d'avancement du README racine.
- `i18n/` existe et est utilisé pour les variantes multilingues du README.
- Le README racine est traité comme canonique ; les fichiers multilingues doivent le suivre lors des mises à jour.

## Progression canonique des cours (préservée et réorganisée)

### Cours principaux

#### Mécanique classique
Le manuel de ce cours [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681) a été publié. Vous pouvez l'acheter sur Amazon [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681).

#### Mécanique quantique
Le manuel de ce cours [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903) a été publié. Vous pouvez l'acheter sur Amazon [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903).

#### Relativité restreinte et électrodynamique
Le manuel de ce cours [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065) a été publié. Vous pouvez l'acheter sur Amazon [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065).

#### Tableau de progression principal
| Cours | Progression des brouillons | Progression des notes | Notes/Références |
|---|---:|---:|---|
| General Relativity | 10/10 | 10/10 | The lecture notes had been taken by https://www.lapasserelle.com/general_relativity/ . |
| Cosmology | 10/10 | 9/10 | The lecture notes, from chapter 1 to 9, had been taken by https://www.lapasserelle.com/cosmology/ . The chapter 10 is in the process. |
| Statistical Mechanics | 11/11 | 10/10 | The lecture notes had been taken by https://www.lapasserelle.com/statistical_mechanics/. |

### Cours complémentaires
| Cours | Progression des brouillons | Progression des notes |
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

### Note sur l'intégrité de la progression
- Les tableaux de progression ci-dessus sont conservés à partir du texte canonique du README.
- Les fichiers du dépôt incluent à la fois des parcours avancés et des parcours encore vides ; si une entrée de tableau et l'état du dossier semblent incohérents, considérez le tableau comme l'intention documentée et mettez à jour les deux ensemble lors de révisions futures.

## Dépannage
| Problème | Résolution |
|---|---|
| `pdflatex: command not found` | Installez une distribution LaTeX et assurez-vous que les binaires sont dans `PATH`. |
| Bibliographie/index non affichés | Exécutez le backend requis (`bibtex` ou `biber`) et `makeindex` si utilisé, puis relancez `pdflatex`. |
| Erreurs de fichiers style/class manquants | Compilez depuis le répertoire de projet prévu afin que les chemins relatifs vers les ressources locales soient correctement résolus. |
| Résultat de compilation différent selon les environnements | Ce dépôt contient des contenus produits dans différents environnements ; alignez les versions de packages lorsque c'est possible. |
| Liens multilingues obsolètes ou README de langue manquant | Assurez-vous que la ligne d'options de langue en haut et les fichiers sous `i18n/` restent synchronisés. |
| Incohérence de liens markdown GitHub après renommage de dossier | Revalidez les liens de langue racine et toutes les références `i18n/README.*.md` en une seule passe. |

## Feuille de route
- Continuer les parcours complémentaires avec de vrais contenus de chapitres et des fichiers source.
- Améliorer la cohérence des fichiers README par cours.
- Étendre et maintenir les README multilingues sous `i18n/` et garder le sélecteur de langue synchronisé.
- Ajouter une section de guide de build au niveau du dépôt pour chaque sous-projet ayant des sources TeX.
- Ajouter des extraits de compilation par parcours lorsqu'il existe des différences locales de chaîne d'outils.
- Ajouter une automatisation minimale pour valider l'intégrité des liens README/i18n.

## Contribution
Vous pouvez contribuer à ce projet en le forkant puis en envoyant une pull request.

Périmètre de contribution suggéré :
- Ajouter ou améliorer les notes de chapitre et les références.
- Améliorer la qualité des sources TeX et les instructions de compilation reproductibles.
- Garder synchronisées les déclarations de progression entre le README racine et les README par parcours.
- Maintenir la parité des README multilingues sous `i18n/`.

Bonnes pratiques recommandées pour les pull requests :
- Mentionner le ou les dossier(s) de parcours exact(s) modifié(s).
- Inclure les commandes de compilation TeX utilisées (si des fichiers source ont été modifiés).
- Mettre à jour les tableaux de progression pertinents lorsque l'état des chapitres change.
- Mettre à jour les readmes de `i18n/` après des changements du README canonique en anglais.

## ❤️ Support

| Donate | PayPal | Stripe |
|---|---|---|
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=ko-fi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## Remerciements
- Professeur Leonard Susskind pour le contenu original des cours.
- Source de notes référencée existante : https://www.lapasserelle.com/general_relativity/
- Source de notes référencée existante : https://www.lapasserelle.com/cosmology/
- Source de notes référencée existante : https://www.lapasserelle.com/statistical_mechanics/

## Licence
Ce dépôt est sous licence GNU General Public License v3.0. Voir [LICENSE](LICENSE).
