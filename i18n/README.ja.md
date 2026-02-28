[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


<p align="center">
  <img src="https://raw.githubusercontent.com/lachlanchen/lachlanchen/main/logos/banner.png" alt="LazyingArt banner" />
</p>

# Leonard Susskind 講義ノート リポジトリ


![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg)
![Content Type](https://img.shields.io/badge/content-Lecture%20Notes%20%26%20LaTeX-informational)
![Status](https://img.shields.io/badge/status-Active%20Archive-success)
![LaTeX](https://img.shields.io/badge/tooling-LaTeX-008080)
![i18n](https://img.shields.io/badge/i18n-directory%20ready-orange)

## 📖 概要
このリポジトリは、Leonard Susskind 教授の講義に関連する講義ノート資料を中心にまとめた、コンテンツ重視のアーカイブです。

本リポジトリには Leonard Susskind 教授の講義ノートが含まれます。著作権上の問題がある場合は、削除のためご連絡ください。ノート内の誤りや不正確な情報については、Susskind 教授も作成者も責任を負いません。

### 主な目的
- 各コースのノートと進捗を一か所で管理する。
- 主要コースと補助コースの下書き/ノート進捗を可視化して保持する。
- 継続的な執筆のためにソース資料（PDF、TeX、BibTeX、テンプレート）を提供する。

## ✨ 特徴
- 主要コースの進捗管理と参照情報。
- 補助コースの進捗管理。
- 主要トラックの一部で既存の講義 PDF を収録。
- 一部トラックで LaTeX ソースを収録。
- `template/tuftle` と `template/kaobook` に再利用可能な LaTeX テンプレート。
- `figs/` にリポジトリ用ビジュアル素材。

## 📌 クイックスナップショット
| Area | What is available |
|---|---|
| 📚 Notes | 複数コースのノートセット（進捗管理付き） |
| 🧪 Source | 一部サブプロジェクトに TeX/BibTeX ソース |
| 🧰 Templates | `template/tuftle` と `template/kaobook` |
| 🌐 i18n | `i18n/` ディレクトリは存在（現在は空） |

## 🗂️ プロジェクト構成
```text
leonardsusskind/
├── README.md
├── LICENSE
├── tuftle_book_guide.pdf
├── figs/
│   ├── banner.(png|svg)
│   ├── logo.(png|svg)
│   └── logo-w-text.(png|svg)
├── i18n/                      # exists; currently empty
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

## 🧩 前提条件
閲覧のみの場合:
- PDF リーダー。

TeX 資料を編集/ビルドする場合:
- LaTeX ディストリビューション（TeX Live / MiKTeX）。
- `pdflatex`。
- サブプロジェクトに応じて `bibtex` または `biber`。
- 索引を使うテンプレート向けに `makeindex`。

前提メモ:
- このリポジトリには、ルートレベルの単一ビルドシステム（`Makefile`、`package.json`、`pyproject.toml`）はありません。

## 🚀 インストール
```bash
git clone https://github.com/<your-user>/leonardsusskind.git
cd leonardsusskind
```

基本的な利用（既存ノートの閲覧）に追加のパッケージインストールは不要です。

## 🛠️ 使い方
### 1) 既存ノートを読む
- 関連フォルダ内の PDF を開きます。例:
  - `core_general_relativity/lesson_1.pdf`
  - `core_cosmology/lesson_1.pdf`
  - `core_statistical_mechanics/lesson_1.pdf`

### 2) LaTeX 資料を作業する
- 対象コース/テンプレートのフォルダで `.tex` と `.bib` を編集します。
- そのフォルダで想定されているツールチェーンでコンパイルします。

## ⚙️ 設定
グローバル設定ファイルはありません。

設定は各 TeX プロジェクトごとにローカル管理です（ドキュメントクラス、文献バックエンド、スタイルファイル、画像パスなど）。例:
- `template/kaobook/main.tex`
- `template/tuftle/main.tex`
- `core_cosmology/cosmology_ch10/cosmology_ch10.tex`

## 🧪 例
### Example A: Build `template/kaobook`
`template/kaobook/main.tex` には次のコンパイル手順が記載されています:

```bash
cd template/kaobook
pdflatex main
makeindex main.idx -s StyleInd.ist
biber main
pdflatex main
pdflatex main
```

### Example B: Build `core_cosmology/cosmology_ch10`
`cosmology_ch10.tex` は `\bibliography{ref}` を使用します（BibTeX 形式のワークフロー）:

```bash
cd core_cosmology/cosmology_ch10
pdflatex cosmology_ch10.tex
bibtex cosmology_ch10
pdflatex cosmology_ch10.tex
pdflatex cosmology_ch10.tex
```

### Example C: View a generated chapter PDF
```bash
xdg-open supplemental_particle_physics_1/ch1/main.pdf
```

## 📝 開発メモ
- このリポジトリは主にドキュメント/講義ノートのためのもので、アプリケーションコードベースではありません。
- 一部フォルダには、生成済み TeX 成果物（`.aux`、`.log`、`.toc`、`.bbl` など）がリポジトリ内に含まれます。
- ビルドコマンドはサブディレクトリごとに異なる場合があります。各 `.tex` のローカル慣習に従ってください。
- `i18n/` は多言語 README バリアント用として確保されています。

## 📚 Canonical Course Progress（保持・再構成済み）

### Core Courses

#### Classical Mechanics
このコースの教科書 [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681) はすでに出版されています。Amazon で購入できます: [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681)。

#### Quantum Mechanics
このコースの教科書 [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903) はすでに出版されています。Amazon で購入できます: [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903)。

#### Special Relativity and Electrodynamics
このコースの教科書 [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065) はすでに出版されています。Amazon で購入できます: [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065)。

#### Core Progress Table
| Course | Draft Progress | Notes Progress | Notes/Reference |
|---|---:|---:|---|
| General Relativity | 10/10 | 10/10 | The lecture notes had been taken by https://www.lapasserelle.com/general_relativity/ . |
| Cosmology | 10/10 | 9/10 | The lecture notes, from chapter 1 to 9, had been taken by https://www.lapasserelle.com/cosmology/ . The chapter 10 is in the process. |
| Statistical Mechanics | 11/11 | 10/10 | The lecture notes had been taken by https://www.lapasserelle.com/statistical_mechanics/. |

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

## 🧯 トラブルシューティング
- `pdflatex: command not found`
  - LaTeX ディストリビューションをインストールし、バイナリが `PATH` に通っていることを確認してください。
- 文献/索引が表示されない
  - 必要なバックエンド（`bibtex` または `biber`）と `makeindex`（使用時）を実行し、その後 `pdflatex` を再実行してください。
- style/class ファイルが見つからないエラー
  - ローカル資産への相対パスが正しく解決されるよう、想定されたプロジェクトディレクトリからビルドしてください。
- 環境によってビルド結果が異なる
  - このリポジトリには異なる環境で生成された資料が含まれるため、可能な範囲でパッケージバージョンを揃えてください。

## 🗺️ ロードマップ
- 補助トラックに実際の章コンテンツとソースファイルを継続追加。
- コースごとの README の一貫性を向上。
- `i18n/` 配下に多言語 README を追加し、言語セレクタを同期維持。
- TeX ソースを持つ各サブプロジェクト向けに、リポジトリレベルのビルドガイドを追加。

## ❤️ Contribution or Donation
このプロジェクトへの貢献は、フォークして Pull Request を送ることで行えます。もしこのプロジェクトが開発時間の短縮に役立った場合は、コーヒーをごちそうしていただけるとうれしいです :)

## 🙏 謝辞
- 元の講義コンテンツを提供された Leonard Susskind 教授。
- 既存の参照ノートソース:
  - https://www.lapasserelle.com/general_relativity/
  - https://www.lapasserelle.com/cosmology/
  - https://www.lapasserelle.com/statistical_mechanics/

## 📄 ライセンス
このリポジトリは GNU General Public License v3.0 の下でライセンスされています。詳細は [LICENSE](LICENSE) を参照してください。
