[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# Leonard Susskind 講義ノート・リポジトリ

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

> 🎓 レオナルド・サスキンド（Leonard Susskind）の講義ノート資料を多言語でまとめたアーカイブです。読みやすい PDF と編集可能な LaTeX ソースを、学習・再利用・参照用に保持しています。

## 概要
このリポジトリは、Leonard Susskind 教授の講義活動全体から得られた講義ノート資料を一元化したアーカイブです。

> Leonard Susskind 教授の講義ノートです。著作権上の懸念がある場合は、このリポジトリを削除するため連絡してください。講義ノート内の誤りや誤情報について、Susskind 教授も筆者も責任を負いません。

1 か所で 3 層をまとめています。

- 選定済みのトラックとコース別の進捗。
- 閲覧・共有用の公開成果物（` .pdf`）。
- アーカイブを保守・拡張する方向けのソース (`.tex`, `.bib`, テンプレート)。

### 主な目標
- 各コースのノートと進捗を 1 箇所で管理する。
- コア・補助トラック全体で下書きとノート進捗の可視化を維持する。
- 継続的な執筆のための素材（PDF, TeX, BibTeX, テンプレート）を提供する。

## 特徴
- コアコースの進捗管理と参照情報。
- 補助コースの進捗管理。
- 複数のコアトラックで既存の講義 PDF を保有。
- 一部トラックで TeX ソースを公開。
- 再利用可能な LaTeX テンプレートを `template/tuftle` と `template/kaobook` に収録。
- リポジトリ素材を `figs/` に保管。
- 多言語 README を `i18n/` に配置。

## クイックスナップショット
| 領域 | 利用可能内容 |
|---|---|
| 📝 ノート | 進捗追跡付きの複数コースノート |
| 🧾 ソース | 選定されたサブプロジェクトの TeX/BibTeX ソース |
| 🧱 テンプレート | `template/tuftle` と `template/kaobook` |
| 🎨 ブランディング | `figs/banner.*`, `figs/logo.*`, `figs/logo-w-text.*` |
| 🌍 i18n | `i18n/README.*.md` 各言語版 |

## 目次
- [概要](#概要)
- [特徴](#特徴)
- [クイックスナップショット](#クイックスナップショット)
- [プロジェクト構成](#プロジェクト構成)
- [前提条件](#前提条件)
- [インストール](#インストール)
- [使い方](#使い方)
- [設定](#設定)
- [例](#例)
- [開発ノート](#開発ノート)
- [標準コース進捗（保持・再編成版）](#標準コース進捗保持・再編成版)
- [トラブルシューティング](#トラブルシューティング)
- [ロードマップ](#ロードマップ)
- [コントリビューション](#コントリビューション)
- [❤️ Support](#-support)
- [謝辞](#謝辞)
- [ライセンス](#ライセンス)

## プロジェクト構成
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

## 前提条件
閲覧時:
- PDF リーダー（システム標準またはアプリ）

TeX 資料の編集・ビルド時:
- LaTeX ディストリビューション（TeX Live / MiKTeX）
- `pdflatex`
- サブプロジェクトにより `bibtex` または `biber`
- 索引を使うプロジェクトでは `makeindex`

補足:
- このリポジトリにはルート直下の統一ビルドシステム（`Makefile`, `package.json`, `pyproject.toml`）はありません。
- ビルドは各サブプロジェクトのディレクトリ内で実行する前提です。

## インストール
```bash
# リポジトリをクローン
git clone https://github.com/lachlanchen/leonardsusskind.git
cd leonardsusskind
```

このリポジトリはコンテンツ優先で構成されています。ミラーやフォークを作成する場合は、リモート URL を自分のコピー先に置き換えてください。

既存ノートを読むために必要な全体パッケージのインストールは不要です。

## 使い方
### 1) 既存ノートを読む
対象フォルダ内の PDF を開きます。例:
- `core_general_relativity/lesson_1.pdf`
- `core_cosmology/lesson_1.pdf`
- `core_statistical_mechanics/lesson_1.pdf`
- `supplemental_particle_physics_2/NumberTheory.pdf`

### 2) LaTeX 資料の執筆・拡張
- 対象コース/テンプレートのフォルダ内で `.tex` と `.bib` を編集します。
- そのフォルダで規定されるワークフローでコンパイルします。
- 相対パス参照が正しく解決されるよう、プロジェクト内で直接ビルドします。

### 3) トラック別エントリーポイントを辿る
各主要トラックは独自の `README.md` を持ち、範囲を限定したノート、参考情報、進捗情報が記載されています。

## 設定
グローバル設定ファイルはありません。

設定は各 TeX プロジェクトのローカル内にあります。典型例として、以下が含まれます:
- 書誌設定などを含む文書クラスやパッケージ設定は `template/kaobook/main.tex`
- 再利用可能なスタイル/構造は `template/kaobook/`
- 引用スタイルや参考文献エンジンは `main.tex` と `ref.bib` の対応関係
- 画像パスや章別アセットの include path は各プロジェクト内

代表的なローカル設定ポイント:
- `template/kaobook/main.tex`
- `template/tuftle/main.tex`
- `core_cosmology/cosmology_ch10/cosmology_ch10.tex`
- `supplemental_particle_physics_1/ch1/main.tex`
- `supplemental_advanced_quantum/ch1/main.tex`

## 例
### 例 A: `template/kaobook` をビルド
`template/kaobook/main.tex` はこのコンパイル手順を想定しています:

```bash
cd template/kaobook
pdflatex main
makeindex main.idx -s StyleInd.ist
biber main
pdflatex main
pdflatex main
```

### 例 B: `core_cosmology/cosmology_ch10` をビルド
`cosmology_ch10.tex` は BibTeX ベースのワークフローを使用します:

```bash
cd core_cosmology/cosmology_ch10
pdflatex cosmology_ch10.tex
bibtex cosmology_ch10
pdflatex cosmology_ch10.tex
pdflatex cosmology_ch10.tex
```

### 例 C: `supplemental_particle_physics_1/ch1` をビルド
```bash
cd supplemental_particle_physics_1/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### 例 D: `supplemental_advanced_quantum/ch1` をビルド
```bash
cd supplemental_advanced_quantum/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### 例 E: 出力をローカルで表示
```bash
xdg-open supplemental_particle_physics_1/ch1/main.pdf
```

## 開発ノート
- このリポジトリはアプリケーションコードベースではなく、主にドキュメント/ノートの保存を目的としたものです。
- フォルダによっては生成済み TeX アーティファクト（`.aux`, `.log`, `.toc`, `.bbl` など）がレポジトリにコミットされています。
- ビルドコマンドはサブディレクトリごとに異なる場合があり、各 `.tex` のローカル規約に従ってください。
- コア・補助トラック全体でトラック別の `README.md` が存在し、ルートの進捗説明と整合させる必要があります。
- `i18n/` は多言語 README バリアントを収容するために存在します。
- ルート README が正本として扱われるため、ローカル版は更新時にそれに追従してください。

## 標準コース進捗（保持・再編成版）

### コアコース

#### 古典力学
このコースの教科書 [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681) は出版済みです。Amazon の [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681) から購入できます。

#### 量子力学
このコースの教科書 [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903) は出版済みです。Amazon の [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903) から購入できます。

#### 特殊相対性理論と電磁気学
このコースの教科書 [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065) は出版済みです。Amazon の [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065) から購入できます。

#### コア進捗表
| コース | 下書き進捗 | ノート進捗 | ノート/参照 |
|---|---:|---:|---|
| General Relativity | 10/10 | 10/10 | The lecture notes had been taken by https://www.lapasserelle.com/general_relativity/ . |
| Cosmology | 10/10 | 9/10 | The lecture notes, from chapter 1 to 9, had been taken by https://www.lapasserelle.com/cosmology/ . The chapter 10 is in the process. |
| Statistical Mechanics | 11/11 | 10/10 | The lecture notes had been taken by https://www.lapasserelle.com/statistical_mechanics/. |

### 補助コース
| コース | 下書き進捗 | ノート進捗 |
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

### 進捗整合性ノート
- 上記の進捗表は、ルート README の原文を踏襲して保持しています。
- リポジトリには成熟したトラックとプレースホルダーのトラックが混在します。表の値と実ファイルの状態に不一致がある場合は、表を正式な方針として扱い、将来の更新で双方を同時に整合してください。

## トラブルシューティング
| 問題 | 解決方法 |
|---|---|
| `pdflatex: command not found` | LaTeX ディストリビューションをインストールし、`PATH` にバイナリを含めます。 |
| 参考文献/索引が表示されない | 必要なバックエンド（`bibtex` または `biber`）と `makeindex`（該当時）を実行し、その後 `pdflatex` を再実行します。 |
| style/class ファイルが見つからないエラー | 正しいプロジェクトディレクトリ内でビルドし、ローカル資産の相対パスを正しく解決します。 |
| 環境間で出力が異なる | このリポジトリの素材は生成環境が混在するため、可能なら使用パッケージの版を合わせます。 |
| 多言語リンクが古い／言語 README が不足 | 先頭の言語選択行と `i18n/` 配下のファイルが同期しているか確認します。 |
| GitHub Markdown リンクがフォルダ名変更後にズレる | ルート言語リンクとすべての `i18n/README.*.md` 参照を一括見直します。 |

## ロードマップ
- 補助トラックに実際の章コンテンツとソースファイルを継続的に追加。
- コース別 README の一貫性を改善。
- `i18n/` 下の多言語 README を拡張・維持し、言語選択の同期を保つ。
- TeX ソースを持つ各サブプロジェクトにリポジトリレベルのビルドガイドを追加。
- ローカルのツールチェーン差分がある箇所にトラック別コンパイル例を追加。
- README と i18n リンクの整合性を検証する軽量自動化を追加。

## コントリビューション
このプロジェクトへの貢献は、フォークしてプルリクエストを送ることで可能です。

貢献の推奨範囲:
- 章ノートや参考文献の追加・改善。
- TeX ソース品質と再現可能なビルド手順の改善。
- ルート README とトラック別 README の進捗整合を保つ。
- `i18n/` の多言語 README パリティを維持。

推奨 PR フォーマット:
- 変更したトラックフォルダを明確に記載。
- ソースファイルを編集した場合は、実行した TeX コンパイルコマンドを添付。
- 章状態が変わったら該当進捗表を更新。
- ルート README の更新後、`i18n/` README も更新。

## 謝辞
- 元となる講義コンテンツを提供された Leonard Susskind 教授。
- 参照元ノート（既存）: https://www.lapasserelle.com/general_relativity/
- 参照元ノート（既存）: https://www.lapasserelle.com/cosmology/
- 参照元ノート（既存）: https://www.lapasserelle.com/statistical_mechanics/

## ライセンス
このリポジトリは GNU General Public License v3.0 の下で公開されています。[LICENSE](../LICENSE) を参照してください。


## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |
