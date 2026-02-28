[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


<p align="center">
  <img src="https://raw.githubusercontent.com/lachlanchen/lachlanchen/main/logos/banner.png" alt="Bannière LazyingArt" />
</p>

# Dépôt de notes de cours de Leonard Susskind


![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg)
![Content Type](https://img.shields.io/badge/content-Lecture%20Notes%20%26%20LaTeX-informational)
![Status](https://img.shields.io/badge/status-Active%20Archive-success)
![LaTeX](https://img.shields.io/badge/tooling-LaTeX-008080)
![i18n](https://img.shields.io/badge/i18n-directory%20ready-orange)

## 📖 Vue d'ensemble
Ce dépôt est une archive orientée contenu de notes de cours liées aux cours du professeur Leonard Susskind.

Les notes de cours du professeur Leonard Susskind. Si cela enfreint des droits d’auteur, merci de me contacter pour supprimer ce dépôt. Le professeur Susskind n’assume aucune responsabilité concernant les erreurs ou informations inexactes de ces notes, moi non plus.

### Objectifs principaux
- Regrouper les notes de cours et l’avancement au même endroit.
- Préserver la visibilité de l’avancement des brouillons/notes sur les parcours principaux et complémentaires.
- Fournir les sources (PDF, TeX, BibTeX, modèles) pour poursuivre la rédaction.

## ✨ Fonctionnalités
- Suivi des cours principaux et références.
- Suivi de l’avancement des cours complémentaires.
- PDF de leçons déjà présents pour plusieurs parcours principaux.
- Sources LaTeX dans certains parcours.
- Modèles LaTeX réutilisables dans `template/tuftle` et `template/kaobook`.
- Visuels du dépôt dans `figs/`.

## 📌 Aperçu rapide
| Zone | Contenu disponible |
|---|---|
| 📚 Notes | Plusieurs ensembles de notes de cours, avec suivi de progression |
| 🧪 Sources | Sources TeX/BibTeX dans certains sous-projets |
| 🧰 Modèles | `template/tuftle` et `template/kaobook` |
| 🌐 i18n | Le dossier `i18n/` existe |

## 🗂️ Structure du projet
```text
leonardsusskind/
├── README.md
├── LICENSE
├── tuftle_book_guide.pdf
├── figs/
│   ├── banner.(png|svg)
│   ├── logo.(png|svg)
│   └── logo-w-text.(png|svg)
├── i18n/                      # variantes README multilingues
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

## 🧩 Prérequis
Pour la lecture uniquement :
- Un lecteur PDF.

Pour éditer/compiler les contenus TeX :
- Une distribution LaTeX (TeX Live / MiKTeX).
- `pdflatex`.
- `bibtex` ou `biber` selon le sous-projet.
- `makeindex` pour les modèles qui utilisent un index.

Note d’hypothèse :
- Il n’existe pas de système de build unique à la racine (`Makefile`, `package.json`, `pyproject.toml`) dans ce dépôt.

## 🚀 Installation
```bash
git clone https://github.com/<your-user>/leonardsusskind.git
cd leonardsusskind
```

Aucune étape d’installation de package n’est nécessaire pour l’usage de base (lecture des notes existantes).

## 🛠️ Utilisation
### 1) Lire les notes existantes
- Ouvrez les PDF dans les dossiers concernés, par exemple :
  - `core_general_relativity/lesson_1.pdf`
  - `core_cosmology/lesson_1.pdf`
  - `core_statistical_mechanics/lesson_1.pdf`

### 2) Travailler sur les contenus LaTeX
- Modifiez les fichiers `.tex` et `.bib` dans le dossier cours/modèle ciblé.
- Compilez avec la chaîne d’outils attendue dans ce dossier.

## ⚙️ Configuration
Il n’existe pas de fichier de configuration global.

La configuration est locale à chaque projet TeX (classe de document, moteur bibliographique, fichiers de style, chemins des images), par exemple :
- `template/kaobook/main.tex`
- `template/tuftle/main.tex`
- `core_cosmology/cosmology_ch10/cosmology_ch10.tex`

## 🧪 Exemples
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

### Exemple C : Afficher un PDF de chapitre généré
```bash
xdg-open supplemental_particle_physics_1/ch1/main.pdf
```

## 📝 Notes de développement
- Il s’agit principalement d’un dépôt de documentation/notes, pas d’une base de code applicative.
- Certains dossiers incluent des artefacts TeX générés (`.aux`, `.log`, `.toc`, `.bbl`, etc.) versionnés dans le dépôt.
- Les commandes de build peuvent varier selon le sous-répertoire ; suivez les conventions `.tex` locales.
- `i18n/` existe et est réservé aux variantes multilingues du README.

## 📚 Progression canonique des cours (préservée et réorganisée)

### Cours principaux

#### Mécanique classique
Le manuel de ce cours [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681) a été publié. Vous pouvez l’acheter sur Amazon [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681).

#### Mécanique quantique
Le manuel de ce cours [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903) a été publié. Vous pouvez l’acheter sur Amazon [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903).

#### Relativité restreinte et électrodynamique
Le manuel de ce cours [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065) a été publié. Vous pouvez l’acheter sur Amazon [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065).

#### Tableau d’avancement des cours principaux
| Cours | Avancement brouillon | Avancement notes | Notes/Référence |
|---|---:|---:|---|
| Relativité générale | 10/10 | 10/10 | Les notes de cours ont été prises par https://www.lapasserelle.com/general_relativity/ . |
| Cosmologie | 10/10 | 9/10 | Les notes de cours, du chapitre 1 au 9, ont été prises par https://www.lapasserelle.com/cosmology/ . Le chapitre 10 est en cours. |
| Mécanique statistique | 11/11 | 10/10 | Les notes de cours ont été prises par https://www.lapasserelle.com/statistical_mechanics/. |

### Cours complémentaires
| Cours | Avancement brouillon | Avancement notes |
|---|---:|---:|
| Mécanique quantique avancée | 0/10 | 0/10 |
| Boson de Higgs | 0/1 | 0/1 |
| Intrication quantique | 0/9 | 0/9 |
| Relativité | 0/9 | 0/9 |
| Physique des particules 1 : concepts de base | 6/10 | 0/10 |
| Physique des particules 2 : modèle standard | 0/10 | 0/10 |
| Physique des particules 3 : supersymétrie et grande unification | 0/10 | 0/10 |
| Théorie des cordes | 0/11 | 10/10 |
| Cosmologie et trous noirs | 0/8 | 0/10 |

## 🧯 Dépannage
- `pdflatex: command not found`
  - Installez une distribution LaTeX et assurez-vous que les binaires sont dans `PATH`.
- Bibliographie/index absent
  - Exécutez le backend requis (`bibtex` ou `biber`) et `makeindex` si nécessaire, puis relancez `pdflatex`.
- Erreurs de fichier style/classe manquant
  - Compilez depuis le répertoire projet prévu afin que les chemins relatifs vers les ressources locales se résolvent correctement.
- Le rendu diffère selon les environnements
  - Ce dépôt contient des éléments produits dans différents environnements ; alignez les versions de packages lorsque c’est possible.

## 🗺️ Feuille de route
- Continuer les parcours complémentaires avec du contenu réel de chapitres et des fichiers source.
- Améliorer la cohérence des README par cours.
- Ajouter des README multilingues sous `i18n/` et garder le sélecteur de langues synchronisé.
- Ajouter une section de guide de build au niveau dépôt pour chaque sous-projet qui contient des sources TeX.

## ❤️ Contribution ou don
Vous pouvez contribuer à ce projet en le forkant puis en envoyant une pull request. Si ce projet vous aide à réduire votre temps de développement, vous pouvez m’offrir un café :)

## 🙏 Remerciements
- Professeur Leonard Susskind pour le contenu original des cours.
- Sources de notes référencées existantes :
  - https://www.lapasserelle.com/general_relativity/
  - https://www.lapasserelle.com/cosmology/
  - https://www.lapasserelle.com/statistical_mechanics/

## 📄 Licence
Ce dépôt est distribué sous licence GNU General Public License v3.0. Voir [LICENSE](../LICENSE).
