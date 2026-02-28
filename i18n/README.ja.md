[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# Leonard Susskind 講義ノート リポジトリ

![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg)
![Content Type](https://img.shields.io/badge/content-Lecture%20Notes%20%26%20LaTeX-informational)
![Status](https://img.shields.io/badge/status-Active%20Archive-success)
![LaTeX](https://img.shields.io/badge/tooling-LaTeX-008080)
![Core Tracks](https://img.shields.io/badge/core_tracks-6-1f6feb)
![Supplemental Tracks](https://img.shields.io/badge/supplemental_tracks-9-9a6700)
![i18n](https://img.shields.io/badge/i18n-10%20translations%20%2B%20English-orange)

## 概要
このリポジトリは、Leonard Susskind 教授の講義に関連する講義ノート資料を中心に整理したアーカイブです。

> Leonard Susskind 教授の講義ノートです。著作権上の問題がある場合は、このリポジトリの削除のためご連絡ください。ノート内の誤りや誤情報について、Susskind 教授も私も責任を負いません。

### 主な目的
- 各コースのノートと進捗を一箇所で管理する。
- コアコースと補助コースの下書き/ノート進捗の可視性を維持する。
- 継続的な執筆に使える元資料（PDF、TeX、BibTeX、テンプレート）を提供する。

## 特徴
- コアコースの進捗管理と参照情報。
- 補助コースの進捗管理。
- 複数のコアコースで既存の講義 PDF を収録。
- 一部コースで LaTeX ソースを提供。
- 再利用可能な LaTeX テンプレートを `template/tuftle` と `template/kaobook` に収録。
- リポジトリのビジュアル素材を `figs/` に収録。
- 多言語 README を `i18n/` に収録。

## クイックスナップショット
| 領域 | 利用可能な内容 |
|---|---|
| 📝 ノート | 進捗管理付きの複数コースノート |
| 🧾 ソース | 一部サブプロジェクトに TeX/BibTeX ソース |
| 🧱 テンプレート | `template/tuftle` と `template/kaobook` |
| 🎨 ブランディング | `figs/banner.*`, `figs/logo.*`, `figs/logo-w-text.*` |
| 🌍 i18n | `i18n/README.*.md` 言語別バリアント |

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
- [開発メモ](#開発メモ)
- [標準コース進捗（保持・再編成版）](#標準コース進捗保持再編成版)
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
閲覧のみの場合:
- PDF リーダー。

TeX 資料を編集・ビルドする場合:
- LaTeX ディストリビューション（TeX Live / MiKTeX）。
- `pdflatex`。
- サブプロジェクトに応じて `bibtex` または `biber`。
- 索引を使うテンプレート向けに `makeindex`。

前提メモ:
- このリポジトリには、ルートレベルの統一ビルドシステム（`Makefile`、`package.json`、`pyproject.toml`）はありません。

## インストール
```bash
git clone https://github.com/<your-user>/leonardsusskind.git
cd leonardsusskind
```

このリポジトリがフォークまたはミラーされている場合は、`<your-user>` を正しいアカウントに置き換えてください。

基本的な利用（既存ノートの閲覧）には、パッケージのインストール手順は不要です。

## 使い方
### 1) 既存ノートを読む
たとえば、該当フォルダ内の PDF を開きます:
- `core_general_relativity/lesson_1.pdf`
- `core_cosmology/lesson_1.pdf`
- `core_statistical_mechanics/lesson_1.pdf`
- `supplemental_particle_physics_2/NumberTheory.pdf`

### 2) LaTeX 資料を作業する
- 対象コース/テンプレートフォルダ内の `.tex` と `.bib` を編集します。
- そのフォルダで想定されているツールチェーンでコンパイルします。
- 相対パスを正しく解決するため、ローカルのプロジェクトディレクトリ内でビルドコマンドを実行することを推奨します。

### 3) トラック別 README を参照する
主要トラックごとに、スコープされたノートと進捗情報のためのローカル `README.md` があります。

## 設定
グローバル設定ファイルはありません。

設定は各 TeX プロジェクトにローカルで定義されます（ドキュメントクラス、参考文献バックエンド、スタイルファイル、画像パス）。例:
- `template/kaobook/main.tex`
- `template/tuftle/main.tex`
- `core_cosmology/cosmology_ch10/cosmology_ch10.tex`
- `supplemental_particle_physics_1/ch1/main.tex`
- `supplemental_advanced_quantum/ch1/main.tex`

## 例
### 例 A: `template/kaobook` をビルド
`template/kaobook/main.tex` には次のコンパイル手順が記載されています:

```bash
cd template/kaobook
pdflatex main
makeindex main.idx -s StyleInd.ist
biber main
pdflatex main
pdflatex main
```

### 例 B: `core_cosmology/cosmology_ch10` をビルド
`cosmology_ch10.tex` は `\bibliography{ref}` を使います（BibTeX ワークフロー）:

```bash
cd core_cosmology/cosmology_ch10
pdflatex cosmology_ch10.tex
bibtex cosmology_ch10
pdflatex cosmology_ch10.tex
pdflatex cosmology_ch10.tex
```

### 例 C: Tufte ベースの章をビルド（`supplemental_particle_physics_1/ch1`）
```bash
cd supplemental_particle_physics_1/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### 例 D: Tufte ベースの章をビルド（`supplemental_advanced_quantum/ch1`）
```bash
cd supplemental_advanced_quantum/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### 例 E: 生成された章 PDF を表示
```bash
xdg-open supplemental_particle_physics_1/ch1/main.pdf
```

## 開発メモ
- このリポジトリは主にドキュメント/ノートのリポジトリであり、アプリケーションのコードベースではありません。
- 一部フォルダには、生成済み TeX 生成物（`.aux`、`.log`、`.toc`、`.bbl` など）がコミットされています。
- ビルドコマンドはサブディレクトリごとに異なる場合があります。ローカルの `.tex` 規約に従ってください。
- コア/補助ディレクトリ全体に、トラックごとの `README.md` が存在し、ルート README の進捗記述と整合させる必要があります。
- `i18n/` は多言語 README バリアント用に存在します。
- ルート README は正本として扱われるため、多言語ファイル更新時はそれに追従してください。

## 標準コース進捗（保持・再編成版）

### コアコース

#### 古典力学
このコースの教科書 [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681) はすでに出版されています。Amazon の [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681) から購入できます。

#### 量子力学
このコースの教科書 [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903) はすでに出版されています。Amazon の [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903) から購入できます。

#### 特殊相対論と電磁気学
このコースの教科書 [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065) はすでに出版されています。Amazon の [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065) から購入できます。

#### コア進捗テーブル
| Course | Draft Progress | Notes Progress | Notes/Reference |
|---|---:|---:|---|
| General Relativity | 10/10 | 10/10 | The lecture notes had been taken by https://www.lapasserelle.com/general_relativity/ . |
| Cosmology | 10/10 | 9/10 | The lecture notes, from chapter 1 to 9, had been taken by https://www.lapasserelle.com/cosmology/ . The chapter 10 is in the process. |
| Statistical Mechanics | 11/11 | 10/10 | The lecture notes had been taken by https://www.lapasserelle.com/statistical_mechanics/. |

### 補助コース
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

### 進捗整合性メモ
- 上記の進捗テーブルは、標準 README テキストから保持したものです。
- リポジトリには成熟したトラックとプレースホルダのトラックが混在しています。テーブル記載とフォルダ状態に不整合がある場合は、テーブルを文書化された意図として扱い、今後の改訂で両方を同時に更新してください。

## トラブルシューティング
| 問題 | 解決策 |
|---|---|
| `pdflatex: command not found` | LaTeX ディストリビューションをインストールし、バイナリが `PATH` に含まれていることを確認してください。 |
| 参考文献/索引が表示されない | 必要なバックエンド（`bibtex` または `biber`）と、必要に応じて `makeindex` を実行し、その後に `pdflatex` を再実行してください。 |
| style/class ファイルが見つからないエラー | ローカル資産への相対パスを正しく解決するため、意図したプロジェクトディレクトリからビルドしてください。 |
| 環境ごとにビルド結果が異なる | このリポジトリには異なる環境で作成された資料が含まれます。可能な範囲でパッケージバージョンを揃えてください。 |
| 多言語リンクが古い、または言語 README がない | 先頭の言語選択行と `i18n/` 配下のファイルを同期してください。 |
| フォルダ名変更後に GitHub の Markdown リンクが不一致 | ルートの言語リンクと `i18n/README.*.md` 参照を一括で再確認してください。 |

## ロードマップ
- 補助トラックに実際の章コンテンツとソースファイルを追加していく。
- コース別 README の一貫性を改善する。
- `i18n/` 配下の多言語 README を拡充・維持し、言語セレクタを同期する。
- TeX ソースを持つ各サブプロジェクト向けに、リポジトリレベルのビルドガイダンスを追加する。
- ローカルのツールチェーン差異がある箇所に、トラック別コンパイル例を追加する。
- README/i18n リンク整合性を検証する最小限の自動化を追加する。

## コントリビューション
このプロジェクトには、フォークして pull request を送ることで貢献できます。

推奨される貢献範囲:
- 章ノートと参考資料の追加または改善。
- TeX ソース品質と再現可能なビルド手順の改善。
- ルート README とトラック別 README の進捗記述を同期。
- `i18n/` 配下の多言語 README の同等性を維持。

推奨される pull request の作法:
- 変更したトラックフォルダを正確に明記する。
- （ソースを編集した場合）実行した TeX コンパイルコマンドを含める。
- 章の状態が変わった場合、関連する進捗テーブルを更新する。
- 正本の英語 README 更新後は、`i18n/` README も更新する。

## ❤️ Support

| Donate | PayPal | Stripe |
|---|---|---|
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=ko-fi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 謝辞
- 元の講義コンテンツを提供してくださった Leonard Susskind 教授。
- 既存の参照ノートソース: https://www.lapasserelle.com/general_relativity/
- 既存の参照ノートソース: https://www.lapasserelle.com/cosmology/
- 既存の参照ノートソース: https://www.lapasserelle.com/statistical_mechanics/

## ライセンス
このリポジトリは GNU General Public License v3.0 のもとで公開されています。詳細は [LICENSE](../LICENSE) を参照してください。
