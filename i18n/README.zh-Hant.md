[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


<p align="center">
  <img src="https://raw.githubusercontent.com/lachlanchen/lachlanchen/main/logos/banner.png" alt="LazyingArt banner" />
</p>

# Leonard Susskind Lecture Notes Repository

![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg)
![Content Type](https://img.shields.io/badge/content-Lecture%20Notes%20%26%20LaTeX-informational)
![Status](https://img.shields.io/badge/status-Active%20Archive-success)
![LaTeX](https://img.shields.io/badge/tooling-LaTeX-008080)
![i18n](https://img.shields.io/badge/i18n-directory%20ready-orange)

## 📖 概覽
此儲存庫是一個以內容為核心的檔案庫，收錄與 Leonard Susskind 教授課程相關的講義筆記材料。

這是 Leonard Susskind 教授的課程筆記。若此內容有任何版權疑慮，請聯絡我刪除此儲存庫。Susskind 教授不對筆記中的錯誤或不實資訊負責，我也同樣不承擔責任。

### 主要目標
- 將課程筆記與進度集中管理於同一處。
- 保留核心與補充課程的草稿/筆記進度可見性。
- 提供可持續撰寫的原始材料（PDF、TeX、BibTeX、模板）。

## ✨ 特色
- 核心課程追蹤與參考資料。
- 補充課程進度追蹤。
- 多個核心課程已提供既有講義 PDF。
- 部分課程提供 LaTeX 原始檔。
- 可重複使用的 LaTeX 模板位於 `template/tuftle` 與 `template/kaobook`。
- 儲存庫視覺素材位於 `figs/`。

## 📌 快速摘要
| 區域 | 可用內容 |
|---|---|
| 📚 筆記 | 多組課程筆記，並附進度追蹤 |
| 🧪 原始碼 | 部分子專案提供 TeX/BibTeX 原始檔 |
| 🧰 模板 | `template/tuftle` 與 `template/kaobook` |
| 🌐 i18n | 已有 `i18n/` 目錄（目前為空） |

## 🗂️ 專案結構
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

## 🧩 先備需求
僅閱讀內容：
- 一個 PDF 閱讀器。

編輯/編譯 TeX 材料：
- LaTeX 發行版（TeX Live / MiKTeX）。
- `pdflatex`。
- 視子專案而定的 `bibtex` 或 `biber`。
- 使用索引功能的模板需要 `makeindex`。

假設說明：
- 本儲存庫沒有單一的根目錄建置系統（`Makefile`、`package.json`、`pyproject.toml`）。

## 🚀 安裝
```bash
git clone https://github.com/<your-user>/leonardsusskind.git
cd leonardsusskind
```

基本使用（閱讀既有筆記）不需要安裝其他套件。

## 🛠️ 使用方式
### 1) 閱讀既有筆記
- 開啟相關資料夾中的 PDF，例如：
  - `core_general_relativity/lesson_1.pdf`
  - `core_cosmology/lesson_1.pdf`
  - `core_statistical_mechanics/lesson_1.pdf`

### 2) 編修 LaTeX 材料
- 在目標課程/模板資料夾中編輯 `.tex` 與 `.bib` 檔案。
- 依該資料夾預期的工具鏈進行編譯。

## ⚙️ 設定
本儲存庫沒有全域設定檔。

設定以各 TeX 專案為單位（文件類別、參考文獻後端、樣式檔、圖形路徑），例如：
- `template/kaobook/main.tex`
- `template/tuftle/main.tex`
- `core_cosmology/cosmology_ch10/cosmology_ch10.tex`

## 🧪 範例
### 範例 A：建置 `template/kaobook`
`template/kaobook/main.tex` 文件列出以下編譯流程：

```bash
cd template/kaobook
pdflatex main
makeindex main.idx -s StyleInd.ist
biber main
pdflatex main
pdflatex main
```

### 範例 B：建置 `core_cosmology/cosmology_ch10`
`cosmology_ch10.tex` 使用 `\bibliography{ref}`（BibTeX 風格流程）：

```bash
cd core_cosmology/cosmology_ch10
pdflatex cosmology_ch10.tex
bibtex cosmology_ch10
pdflatex cosmology_ch10.tex
pdflatex cosmology_ch10.tex
```

### 範例 C：查看已產生的章節 PDF
```bash
xdg-open supplemental_particle_physics_1/ch1/main.pdf
```

## 📝 開發說明
- 這主要是文件/筆記儲存庫，而非應用程式程式碼庫。
- 某些資料夾包含已產生並提交到儲存庫的 TeX 產物（`.aux`、`.log`、`.toc`、`.bbl` 等）。
- 建置指令會因子目錄而異；請遵循當地 `.tex` 慣例。
- `i18n/` 已建立，預留給多語 README 版本。

## 📚 課程進度（保留並重整）

### 核心課程

#### 古典力學
本課程教科書 [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681) 已出版。你可以在 Amazon 購買 [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681)。

#### 量子力學
本課程教科書 [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903) 已出版。你可以在 Amazon 購買 [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903)。

#### 狹義相對論與電動力學
本課程教科書 [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065) 已出版。你可以在 Amazon 購買 [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065)。

#### 核心進度表
| 課程 | 草稿進度 | 筆記進度 | 筆記/參考 |
|---|---:|---:|---|
| General Relativity | 10/10 | 10/10 | The lecture notes had been taken by https://www.lapasserelle.com/general_relativity/ . |
| Cosmology | 10/10 | 9/10 | The lecture notes, from chapter 1 to 9, had been taken by https://www.lapasserelle.com/cosmology/ . The chapter 10 is in the process. |
| Statistical Mechanics | 11/11 | 10/10 | The lecture notes had been taken by https://www.lapasserelle.com/statistical_mechanics/. |

### 補充課程
| 課程 | 草稿進度 | 筆記進度 |
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

## 🧯 疑難排解
- `pdflatex: command not found`
  - 安裝 LaTeX 發行版，並確認可執行檔已加入 `PATH`。
- 參考文獻/索引未顯示
  - 執行所需後端（`bibtex` 或 `biber`）與 `makeindex`（若有使用），再重新執行 `pdflatex`。
- 缺少樣式/類別檔錯誤
  - 請從預期的專案目錄建置，以正確解析本地資產的相對路徑。
- 不同環境產生的建置結果不同
  - 本儲存庫包含在不同環境下產生的材料；請盡可能對齊套件版本。

## 🗺️ 路線圖
- 持續補充課程內容，加入實際章節內容與原始檔。
- 改善各課程 README 的一致性。
- 在 `i18n/` 新增多語 README，並保持語言選單同步。
- 為有 TeX 原始碼的子專案新增儲存庫層級建置指引。

## ❤️ 貢獻或贊助
你可以透過 fork 此專案並提交 pull request 來貢獻。若此專案幫你節省了開發時間，也歡迎請我喝杯咖啡 :)

## 🙏 致謝
- Leonard Susskind 教授提供原始課程內容。
- 既有參考筆記來源：
  - https://www.lapasserelle.com/general_relativity/
  - https://www.lapasserelle.com/cosmology/
  - https://www.lapasserelle.com/statistical_mechanics/

## 📄 授權
本儲存庫採用 GNU General Public License v3.0 授權。請參閱 [LICENSE](LICENSE)。
