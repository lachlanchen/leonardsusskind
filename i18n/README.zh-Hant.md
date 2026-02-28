[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# Leonard Susskind 講義資料庫

![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg)
![Content Type](https://img.shields.io/badge/content-Lecture%20Notes%20%26%20LaTeX-informational)
![Status](https://img.shields.io/badge/status-Active%20Archive-success)
![LaTeX](https://img.shields.io/badge/tooling-LaTeX-008080)
![Core Tracks](https://img.shields.io/badge/core_tracks-6-1f6feb)
![Supplemental Tracks](https://img.shields.io/badge/supplemental_tracks-9-9a6700)
![i18n](https://img.shields.io/badge/i18n-10%20translations%20%2B%20English-orange)

## 概覽
本倉庫是以內容為先的檔案庫，彙整 Leonard Susskind 教授課程的講義筆記教材。

> 這是 Leonard Susskind 教授的課程講義。若有任何版權問題，請聯絡我以刪除此倉庫。Susskind 教授不為筆記中的錯誤或錯誤資訊負責，我亦不負責。

### 主要目標
- 將課程筆記與進度集中保留於同一處。
- 在核心與補充軌道中保留草稿／筆記進度的可見性。
- 提供持續編寫所需的原始素材（PDF、TeX、BibTeX、範本）。

## 功能
- 核心課程追蹤與參考資料。
- 補充課程進度追蹤。
- 多個核心軌道已有既有課堂 PDF。
- 指定軌道提供 LaTeX 原始素材。
- 可重複使用的 LaTeX 範本位於 `template/tuftle` 與 `template/kaobook`。
- 儲存庫視覺素材位於 `figs/`。
- 多語言 README 於 `i18n/`。

## 快速總覽
| 區域 | 可用內容 |
|---|---|
| 📝 筆記 | 多組課程筆記，並含進度追蹤 |
| 🧾 來源 | 選定子專案中提供 TeX/BibTeX 原始碼 |
| 🧱 範本 | `template/tuftle` 與 `template/kaobook` |
| 🎨 品牌素材 | `figs/banner.*`、`figs/logo.*`、`figs/logo-w-text.*` |
| 🌍 國際化 | `i18n/README.*.md` 語言變體 |

## 目錄
- [概覽](#概覽)
- [功能](#功能)
- [快速總覽](#快速總覽)
- [專案結構](#專案結構)
- [先決條件](#先決條件)
- [安裝](#安裝)
- [使用方式](#使用方式)
- [設定](#設定)
- [範例](#範例)
- [開發備註](#開發備註)
- [課程進度（保留並重整）](#課程進度（保留並重整）)
- [疑難排解](#疑難排解)
- [路線圖](#路線圖)
- [貢獻](#貢獻)
- [❤️ Support](#-support)
- [致謝](#致謝)
- [授權](#授權)

## 專案結構
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

## 先決條件
只需閱讀時：
- 一個 PDF 閱讀器。

編輯／編譯 TeX 資料時：
- LaTeX 發行版（TeX Live / MiKTeX）。
- `pdflatex`。
- 依子專案使用 `bibtex` 或 `biber`。
- 使用索引功能的範本需要 `makeindex`。

備註：
- 本倉庫沒有單一根目錄建置系統（`Makefile`、`package.json`、`pyproject.toml`）。

## 安裝
```bash
git clone https://github.com/<your-user>/leonardsusskind.git
cd leonardsusskind
```

若此倉庫是 fork 或鏡像，請將 `<your-user>` 替換為正確帳號。

基本閱讀用途不需要安裝套件。

## 使用方式
### 1) 閱讀既有筆記
開啟對應資料夾中的 PDF，例如：
- `core_general_relativity/lesson_1.pdf`
- `core_cosmology/lesson_1.pdf`
- `core_statistical_mechanics/lesson_1.pdf`
- `supplemental_particle_physics_2/NumberTheory.pdf`

### 2) 編寫 LaTeX 材料
- 在目標課程／範本資料夾中編輯 `.tex` 與 `.bib` 檔案。
- 依該資料夾預期的工具鏈執行編譯。
- 優先在本機專案目錄內執行建置命令，以確保相對路徑正確解析。

### 3) 依軌道 README 導覽
每個主要軌道都有自己的 `README.md`，用於該領域的筆記與進度脈絡。

## 設定
本倉庫沒有全域設定檔。

設定是各 TeX 專案各自維護（文件類別、參考文獻後端、樣式檔、圖片路徑），例如：
- `template/kaobook/main.tex`
- `template/tuftle/main.tex`
- `core_cosmology/cosmology_ch10/cosmology_ch10.tex`
- `supplemental_particle_physics_1/ch1/main.tex`
- `supplemental_advanced_quantum/ch1/main.tex`

## 範例
### 範例 A：建置 `template/kaobook`
`template/kaobook/main.tex` 說明了此編譯流程：

```bash
cd template/kaobook
pdflatex main
makeindex main.idx -s StyleInd.ist
biber main
pdflatex main
pdflatex main
```

### 範例 B：建置 `core_cosmology/cosmology_ch10`
`cosmology_ch10.tex` 採用 `\bibliography{ref}`（BibTeX 風格流程）：

```bash
cd core_cosmology/cosmology_ch10
pdflatex cosmology_ch10.tex
bibtex cosmology_ch10
pdflatex cosmology_ch10.tex
pdflatex cosmology_ch10.tex
```

### 範例 C：建置 `supplemental_particle_physics_1/ch1` 的 Tufte 章節
```bash
cd supplemental_particle_physics_1/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### 範例 D：建置 `supplemental_advanced_quantum/ch1` 的 Tufte 章節
```bash
cd supplemental_advanced_quantum/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### 範例 E：開啟產生的章節 PDF
```bash
xdg-open supplemental_particle_physics_1/ch1/main.pdf
```

## 開發備註
- 這主要是文件與筆記倉庫，而非應用程式程式碼庫。
- 部分資料夾包含已生成且提交於倉庫內的 TeX 產物（如 `.aux`、`.log`、`.toc`、`.bbl`）。
- 建置指令會因子目錄不同而異；請依當地 `.tex` 規範執行。
- 各軌道的 `README.md` 均存在於核心／補充目錄，需與根目錄進度說明保持一致。
- `i18n/` 已存在，供多語 README 版本使用。
- 根 README 視為正本；多語版本在更新時應與其對齊。

## 課程進度（保留並重整）

### 核心課程

#### 古典力學
本課程書籍 [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681) 已出版。你可在 Amazon 購買 [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681)。

#### 量子力學
本課程書籍 [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903) 已出版。你可在 Amazon 購買 [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903)。

#### 狹義相對論與電動力學
本課程書籍 [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065) 已出版。你可在 Amazon 購買 [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065)。

#### 核心進度表
| 課程 | 草稿進度 | 筆記進度 | 筆記／參考 |
|---|---:|---:|---|
| General Relativity | 10/10 | 10/10 | 本課程講義已由 https://www.lapasserelle.com/general_relativity/ 取錄。 |
| Cosmology | 10/10 | 9/10 | 講義自第 1 章到第 9 章已由 https://www.lapasserelle.com/cosmology/ 取錄。第 10 章仍在進行中。 |
| Statistical Mechanics | 11/11 | 10/10 | 本課程講義已由 https://www.lapasserelle.com/statistical_mechanics/ 取錄。 |

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

### 進度一致性說明
- 上方進度表格的內容沿用自英文主 README 的原始文本。
- 倉庫包含成熟與占位兩類軌道；若表格條目與實際資料夾狀態不一致，請以表格為既定紀錄，並在後續修訂中一併更新兩者。

## 疑難排解
| 問題 | 解法 |
|---|---|
| `pdflatex: command not found` | 安裝 LaTeX 發行版，並確認可執行檔在 `PATH` 中。 |
| 參考文獻或索引未出現 | 先執行所需後端（`bibtex` 或 `biber`）與 `makeindex`（若使用），再重跑 `pdflatex`。 |
| 缺少樣式／類別檔錯誤 | 從正確的專案目錄執行建置，以正確解析本地資源的相對路徑。 |
| 不同環境的建置結果不同 | 本倉庫含有不同環境下產生的材料；盡量統一套件版本。 |
| 多語連結過時或語言 README 缺失 | 確保頂部語言選單與 `i18n/` 內所有 README 一致。
| GitHub markdown 連結與資料夾更名後不一致 | 一次性重新檢查 root 語言連結與所有 `i18n/README.*.md` 的參照 |

## 路線圖
- 持續補充補充軌道的實際章節內容與原始檔。
- 改善各課程 README 的一致性。
- 擴充並維護 `i18n/` 下的多語 README，並保持語言切換同步。
- 為含有 TeX 原始檔的子專案新增倉庫級建置指引。
- 在本地工具鏈差異明顯的軌道補上每軌道編譯指令片段。
- 加入 README/i18n 連結完整性的最小自動化檢查。

## 貢獻
你可透過 fork 此專案並提交 pull request 來參與。

建議貢獻範圍：
- 新增或改進章節筆記與參考資料。
- 改善 TeX 原始檔品質並補上可重現建置說明。
- 維持根目錄與各軌道 README 的進度陳述同步。
- 在 `i18n/` 下維持多語 README 的同步。

建議 PR 流程：
- 註明變更了哪些軌道資料夾。
- 如有修改原始檔，請列出實際使用的 TeX 編譯命令。
- 當章節狀態有變更時，更新對應進度表。
- 英文主 README 有變更時，同步更新 `i18n/` README。

## ❤️ Support

| Donate | PayPal | Stripe |
|---|---|---|
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=ko-fi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 致謝
- 感謝 Leonard Susskind 教授提供原始課程內容。
- 參考筆記來源：
  - https://www.lapasserelle.com/general_relativity/
  - https://www.lapasserelle.com/cosmology/
  - https://www.lapasserelle.com/statistical_mechanics/

## 授權
本倉庫依 GNU General Public License v3.0 授權。詳見 [LICENSE](LICENSE)。
