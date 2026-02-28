[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# レナード・サスキンド講義ノートリポジトリ

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

> 🎓 レオナルド・サスキンドの講義ノート資料を多言語でまとめたアーカイブ。学習・再利用・参照のために、完成版 PDF と編集可能な LaTeX ソースを併せて保管しています。

---

## Overview
このリポジトリは、レオナルド・サスキンド教授の教育資源を集約した、講義ノート中心のアーカイブです。

> レオナルド・サスキンド教授の講義ノートです。著作権に抵触する場合は削除依頼をお願いします。サスキンド教授はノートの誤りや誤情報について責任を負いません。私も同様です。

ここでは、三つの層を一箇所にまとめています。

- 厳選されたノートトラックとコース進行状況の管理。
- 読了・共有用の公開成果物（`.pdf`）。
- アーカイブの保守・拡張向けに `.tex`、`.bib`、テンプレートといったソースを提供。

### Primary Goals
- コースノートと進行管理を一元化する。
- コア・補助トラック双方でドラフトとノート進行の可視性を維持する。
- 継続的な執筆向けに教材ソース（PDF、TeX、BibTeX、テンプレート）を提供する。

## Features
- 📚 コア科目の追跡と参照情報。
- 📌 補助科目の進行トラッキング。
- 📄 いくつかのコアトラック向けに既存のレッスン PDF を掲載。
- 🧪 一部トラックで LaTeX ソースを公開。
- 🧷 `template/tuftle` と `template/kaobook` の再利用可能テンプレート。
- 🎨 ビジュアル素材は `figs/` に保存。
- 🌐 多言語版 README は `i18n/` で管理。

## Quick Snapshot
| 領域 | 利用可能内容 |
|---|---|
| 📝 ノート | 進行管理付きの複数のコースノートセット |
| 🧾 ソース | 選定サブプロジェクトでの TeX/BibTeX ソース |
| 🧱 テンプレート | `template/tuftle` および `template/kaobook` |
| 🎨 ブランディング | `figs/banner.*`、`figs/logo.*`、`figs/logo-w-text.*` |
| 🌍 i18n | `i18n/README.*.md` 言語版 |

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
閲覧時:
- 📖 PDF リーダー（OS標準またはアプリ）。

TeX 材料の編集・ビルド時:
- 📦 LaTeX ディストリビューション（TeX Live / MiKTeX）。
- ⚙️ `pdflatex`。
- 🗂️ サブプロジェクトに応じた `bibtex` または `biber`。
- 🔎 インデックスを使うプロジェクトでは `makeindex`。

---

Assumption notes:
- このリポジトリのルートには、単一のビルドシステム (`Makefile`、`package.json`、`pyproject.toml`) がありません。
- 各サブプロジェクトのディレクトリ内でビルドを実行する前提です。

## Installation
```bash
# Clone the repository
git clone https://github.com/lachlanchen/leonardsusskind.git
cd leonardsusskind
```

このリポジトリはコンテンツ重視です。ミラーやフォークを作成する場合は、用途に合わせてリモート URL をあなた自身のコピーへ置き換えてください。

既存ノートを読むだけなら、追加のグローバルパッケージは不要です。

## Usage
### 1) Read existing notes
対応フォルダ内の PDF を開いてください。例:
- `core_general_relativity/lesson_1.pdf`
- `core_cosmology/lesson_1.pdf`
- `core_statistical_mechanics/lesson_1.pdf`
- `supplemental_particle_physics_2/NumberTheory.pdf`

### 2) Author or extend LaTeX materials
- 対象のコース／テンプレートフォルダ内の `.tex` と `.bib` を編集。
- そのフォルダで定義されているワークフローに従ってコンパイル。
- 相対パスが正しく解決されるよう、対象ディレクトリ内でビルドする。

### 3) Navigate by track-level entry points
主要トラックごとに `README.md` があり、参照先・進行状況・ノート範囲を定義しています。

## Configuration
グローバル設定ファイルはありません。

設定は各 TeX プロジェクト単位で管理されます。典型的な設定箇所は以下です。
- 文書クラスとパッケージ設定：`template/kaobook/main.tex`
- 再利用可能なスタイル／構成：`template/kaobook/`
- 文献管理と引用スタイル：ローカルの `main.tex` / `ref.bib` ペア
- 画像や章別アセットの参照パス：各プロジェクト内

代表的なローカル設定ファイル:
- `template/kaobook/main.tex`
- `template/tuftle/main.tex`
- `core_cosmology/cosmology_ch10/cosmology_ch10.tex`
- `supplemental_particle_physics_1/ch1/main.tex`
- `supplemental_advanced_quantum/ch1/main.tex`

## Examples
### Example A: Build `template/kaobook`
`template/kaobook/main.tex` の手順は以下です。

```bash
cd template/kaobook
pdflatex main
makeindex main.idx -s StyleInd.ist
biber main
pdflatex main
pdflatex main
```

### Example B: Build `core_cosmology/cosmology_ch10`
`cosmology_ch10.tex` は BibTeX 系のワークフローを使います。

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
- 本リポジトリは主に文書・ノート中心であり、アプリケーションコードのコードベースではありません。
- 一部のフォルダには、生成物としての TeX アーティファクト（`.aux`、`.log`、`.toc`、`.bbl` など）がコミットされています。
- フォルダごとにビルドコマンドが異なる場合があるため、ローカルの `.tex` 規約に従ってください。
- コア・補助各ディレクトリにはトラック別 `README.md` があり、ルートの進行ステータスと整合させる必要があります。
- 多言語化は `i18n/` で管理されています。
- ルート README を正規情報源とし、更新時には各言語版も追従します。

## Canonical Course Progress (Preserved and Reorganized)

### Core Courses

#### Classical Mechanics
この講義の教科書は [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681) として刊行されています。Amazon から購入できます: [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681)。

#### Quantum Mechanics
この講義の教科書は [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903) として刊行されています。Amazon から購入できます: [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903)。

#### Special Relativity and Electrodynamics
この講義の教科書は [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065) として刊行されています。Amazon から購入できます: [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065)。

#### Core Progress Table
| Course | Draft Progress | Notes Progress | Notes/Reference |
|---|---:|---:|---|
| General Relativity | 10/10 | 10/10 | 講義ノートは https://www.lapasserelle.com/general_relativity/ から取得されています。 |
| Cosmology | 10/10 | 9/10 | 講義ノート（第1〜9章）は https://www.lapasserelle.com/cosmology/ から取得されています。第10章は作成中です。 |
| Statistical Mechanics | 11/11 | 10/10 | 講義ノートは https://www.lapasserelle.com/statistical_mechanics/ から取得されています。 |

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
- 上記の進行表はルートの正規 README から継承しています。
- このリポジトリには完成済みトラックとプレースホルダートラックが混在しています。表の値と実フォルダの状態に差異がある場合は、表を基準（将来改訂時に両者を同時更新）として扱ってください。

## Troubleshooting
| Issue | Resolution |
|---|---|
| `pdflatex: command not found` | LaTeX ディストリビューションをインストールし、バイナリが `PATH` に含まれていることを確認してください。 |
| 参考文献/インデックスが表示されない | 必要なバックエンド（`bibtex` または `biber`）と `makeindex` を実行してから `pdflatex` を再実行します。 |
| スタイル／クラスファイルエラー | プロジェクト用のディレクトリからビルドし、ローカルアセットへの相対パスが解決されるようにします。 |
| 環境間でビルド結果が異なる | 本リポジトリには異なる環境由来の資料が混在しています。可能な範囲でパッケージバージョンを揃えてください。 |
| 多言語リンクの崩れ、または言語 README の欠落 | 先頭の言語リンク行と `i18n/` 配下の README を同期させます。 |
| GitHub Markdown のリンク不整合（フォルダ名変更後） | ルートの言語リンクと全 `i18n/README.*.md` のリンクを一括で再検証してください。 |

## Roadmap
- 補助トラックの実際の章コンテンツとソースを継続追加。
- トラック別 README の整合性を改善。
- `i18n/` の多言語 README を拡充・維持し、言語セレクタの同期を確保。
- TeX ソースを持つサブプロジェクトごとに、リポジトリレベルのビルドガイダンスを追加。
- ローカルツールチェーン差分のあるトラックごとのコンパイル例を追加。
- README / i18n リンク整合を検証する最小限の自動化を追加。

## Contribution
このプロジェクトには、フォークしてプルリクエストを送ることで参加できます。

推奨される貢献範囲:
- 章ノートや参考資料の追加・改善。
- TeX ソース品質向上と再現可能なビルド手順の整備。
- ルートと各トラック README の進行状況表を同期。
- `i18n/` のREADMEを `README.md` 更新時に対応する言語版へ反映。

プルリクエストの運用推奨:
- 変更したトラックフォルダを明記する。
- ソース編集を伴う場合は使用した TeX コンパイルコマンドを添える。
- 章の状態が変わったときは関連する進行表を更新する。
- 英語版 README 変更後は `i18n/` の README を更新する。

## Acknowledgements
- 元講義コンテンツの提供者であるレオナルド・サスキンド教授に感謝します。
- 参照元ノート: https://www.lapasserelle.com/general_relativity/
- 参照元ノート: https://www.lapasserelle.com/cosmology/
- 参照元ノート: https://www.lapasserelle.com/statistical_mechanics/

## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## License
このリポジトリは GNU General Public License v3.0 の下で公開されています。詳細は [LICENSE](LICENSE)。
