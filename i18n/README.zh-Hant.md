[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# Leonard Susskind 講義筆記儲存庫

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

> 🎓 一個多語系封存的 Leonard Susskind 講義資料庫，保留可閱讀的精美 PDF 與可編輯的 LaTeX 原始檔，方便學習、重複使用與查閱。

## 概覽
本儲存庫是個以內容為先的講義資料彙整庫，集中整理自 Leonard Susskind 教授的教學體系。

> 這是 Leonard Susskind 教授的課堂講義。若有任何版權疑慮，請聯絡我刪除此儲存庫。Susskind 教授不對筆記中的錯誤或誤導性資訊負責，我也同樣不負責。

### 主要目標
- 將課程筆記與進度集中管理於一處。
- 在核心軌道與補充軌道中保留草稿與筆記進度的可見性。
- 提供源資料（PDF、TeX、BibTeX、範本），讓後續編寫與延展更順暢。

## 特性
- 核心課程追蹤與參考資料。
- 補充課程進度追蹤。
- 若干核心軌道已有課程 PDF。
- 選定軌道具備 LaTeX 原始檔。
- 可重複使用的 LaTeX 範本位於 `template/tuftle` 與 `template/kaobook`。
- 倉庫視覺素材位於 `figs/`。
- 多語系 README 存放於 `i18n/`。

## 快速快照
| 區域 | 可用內容 |
|---|---|
| 📝 筆記 | 多套課程筆記並含進度追蹤 |
| 🧾 原始碼 | 選定子專案提供 TeX/BibTeX 原始檔 |
| 🧱 範本 | `template/tuftle` 與 `template/kaobook` |
| 🎨 品牌素材 | `figs/banner.*`、`figs/logo.*`、`figs/logo-w-text.*` |
| 🌍 國際化 | `i18n/README.*.md` 多語系版本 |

## 目錄
- [概覽](#概覽)
- [特性](#特性)
- [快速快照](#快速快照)
- [專案結構](#專案結構)
- [先決條件](#先決條件)
- [安裝](#安裝)
- [使用方式](#使用方式)
- [設定](#設定)
- [範例](#範例)
- [開發說明](#開發說明)
- [標準化課程進度（已保留並重組）](#標準化課程進度已保留並重組)
- [問題排解](#問題排解)
- [路線圖](#路線圖)
- [貢獻](#貢獻)
- [❤️ Support](#-support)
- [致謝](#致謝)
- [授權條款](#授權條款)

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
閱讀時：
- 一個 PDF 閱讀器（系統內建或應用程式皆可）。

編輯／建立 TeX 材料時：
- 一套 LaTeX 環境（TeX Live / MiKTeX）。
- `pdflatex`。
- 依子專案需求，使用 `bibtex` 或 `biber`。
- 使用索引功能的專案需額外安裝 `makeindex`。

前提說明：
- 倉庫根目錄未提供單一建置系統（例如 `Makefile`、`package.json`、`pyproject.toml`）。
- 各子專案應於各自目錄內執行建置流程。

## 安裝
```bash
# Clone the repository
git clone https://github.com/lachlanchen/leonardsusskind.git
cd leonardsusskind
```

本儲存庫以內容為核心。如欲鏡像或 fork，請依你的版本替換 remote URL。

僅閱讀現有筆記不需要安裝任何全域套件。

## 使用方式
### 1) 閱讀現有筆記
在對應資料夾開啟 PDF，例如：
- `core_general_relativity/lesson_1.pdf`
- `core_cosmology/lesson_1.pdf`
- `core_statistical_mechanics/lesson_1.pdf`
- `supplemental_particle_physics_2/NumberTheory.pdf`

### 2) 編寫或擴充 LaTeX 材料
- 在目標課程／範本目錄中編輯 `.tex` 與 `.bib`。
- 依該目錄指定流程進行編譯。
- 在原地建置，確保相對路徑與樣式檔正確解析。

### 3) 依軌道入口檔案導航
每個主要軌道都有自己的 `README.md`，內含該軌道的進度與範圍說明。

## 設定
本倉庫沒有全域設定檔。

設定為每個 TeX 專案本地維護，常見設定點如下：
- `template/kaobook/main.tex` 中的文件類型與套件設定。
- `template/kaobook/` 中可重複使用的樣式／結構。
- 本地 `main.tex` / `ref.bib` 配對中的參考文獻後端與引用樣式。
- 各專案中各章節資源與圖片的 include 路徑。

代表性設定入口：
- `template/kaobook/main.tex`
- `template/tuftle/main.tex`
- `core_cosmology/cosmology_ch10/cosmology_ch10.tex`
- `supplemental_particle_physics_1/ch1/main.tex`
- `supplemental_advanced_quantum/ch1/main.tex`

## 範例
### 範例 A：建置 `template/kaobook`
`template/kaobook/main.tex` 示範了以下編譯流程：

```bash
cd template/kaobook
pdflatex main
makeindex main.idx -s StyleInd.ist
biber main
pdflatex main
pdflatex main
```

### 範例 B：建置 `core_cosmology/cosmology_ch10`
`cosmology_ch10.tex` 使用類似 BibTeX 的流程：

```bash
cd core_cosmology/cosmology_ch10
pdflatex cosmology_ch10.tex
bibtex cosmology_ch10
pdflatex cosmology_ch10.tex
pdflatex cosmology_ch10.tex
```

### 範例 C：建置 `supplemental_particle_physics_1/ch1`
```bash
cd supplemental_particle_physics_1/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### 範例 D：建置 `supplemental_advanced_quantum/ch1`
```bash
cd supplemental_advanced_quantum/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### 範例 E：本機查看輸出
```bash
xdg-open supplemental_particle_physics_1/ch1/main.pdf
```

## 開發說明
- 本儲存庫主要是文件／筆記庫，而非應用程式原始碼。
- 部分目錄已提交已生成的 TeX 產物（如 `.aux`、`.log`、`.toc`、`.bbl` 等）。
- 建置指令可能因子目錄不同而異；請依各 `.tex` 內部規定。
- 每個核心與補充課程下都有 `README.md`，應與根目錄進度描述一致。
- `i18n/` 用於管理多語系 README。
- 根目錄 README 視為規範版本，本地化更新時請與之對齊。

## 標準化課程進度（已保留並重組）

### 核心課程

#### 古典力學
本課程教材 [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681) 已出版。可於 Amazon 購買 [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681)。

#### 量子力學
本課程教材 [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903) 已出版。可於 Amazon 購買 [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903)。

#### 特殊相對論與電動力學
本課程教材 [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065) 已出版。可於 Amazon 購買 [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065)。

#### 核心課程進度表
| 課程 | 草稿進度 | 筆記進度 | 筆記/參考來源 |
|---|---:|---:|---|
| 一般相對論 | 10/10 | 10/10 | 講義由 https://www.lapasserelle.com/general_relativity/ 記錄。 |
| 宇宙學 | 10/10 | 9/10 | 講義已由 https://www.lapasserelle.com/cosmology/ 記錄第 1 到 9 章，第 10 章仍在進行中。 |
| 統計力學 | 11/11 | 10/10 | 講義由 https://www.lapasserelle.com/statistical_mechanics/ 記錄。 |

### 補充課程
| 課程 | 草稿進度 | 筆記進度 |
|---|---:|---:|
| 進階量子力學 | 0/10 | 0/10 |
| 希格斯玻色子 | 0/1 | 0/1 |
| 量子糾纏 | 0/9 | 0/9 |
| 相對論 | 0/9 | 0/9 |
| 粒子物理學 1：基本概念 | 6/10 | 0/10 |
| 粒子物理學 2：標準模型 | 0/10 | 0/10 |
| 粒子物理學 3：超對稱與大統一 | 0/10 | 0/10 |
| 弦論 | 0/11 | 10/10 |
| 宇宙學與黑洞 | 0/8 | 0/10 |

### 進度完整性說明
- 上述進度表沿用自標準化英文 README 文字。
- 倉庫同時包含成熟內容與占位內容；若某項目錄與表格條目看似不一致，請以表格為文件化目標，並在後續版本中同步更新。

## 問題排解
| 問題 | 解法 |
|---|---|
| `pdflatex: command not found` | 安裝 LaTeX 發行版，並確認可執行檔已加入 `PATH`。 |
| 參考文獻或索引未顯示 | 執行必要後端（`bibtex` 或 `biber`）並如有需要加上 `makeindex`，再重跑 `pdflatex`。 |
| 缺少樣式／類別檔 | 請在預期的專案目錄中建置，確保本機相對資源路徑正確。 |
| 不同環境建置結果不同 | 倉庫中的素材來自不同環境；可盡量對齊套件版本。 |
| 語系連結過時或缺少語系 README | 維持頂部語言選項列與 `i18n/` 內的文件同步。 |
| GitHub markdown 連結在資料夾改名後失效 | 請整體重新驗證根 README 與所有 `i18n/README.*.md` 的語系連結。 |

## 路線圖
- 繼續補齊補充軌道的實際章節內容與源檔。
- 提升各課程 README 的一致性。
- 擴充並維護 `i18n/` 下的多語 README，並同步語言選擇器。
- 為每個含 TeX 原始檔的子專案新增倉庫層級建置指引。
- 在各軌道補齊本地工具鏈差異的編譯範例。
- 新增最小化自動化流程以驗證 README 與多語連結完整性。

## 貢獻
你可透過 fork 並提交 pull request 來為專案做出貢獻。

建議的貢獻範圍：
- 新增或改善章節筆記與參考資料。
- 改善 TeX 原始檔品質與可重現建置指引。
- 維持根 README 與各課程 README 的進度陳述同步。
- 在英文 README 變更後，更新 `i18n/` 的多語 README。

建議的 PR 操作方式：
- 明確說明變更的軌道資料夾。
- 若有編輯源檔，請附上實際使用的 TeX 編譯指令。
- 當章節狀態變更時，更新相關進度表。
- 更新 `i18n/` 內 README，以回應英文 README 的變更。

## 致謝
- Leonard Susskind 教授，原始講義內容的授權與啟發來源。
- 現有筆記參考來源： https://www.lapasserelle.com/general_relativity/
- 現有筆記參考來源： https://www.lapasserelle.com/cosmology/
- 現有筆記參考來源： https://www.lapasserelle.com/statistical_mechanics/

## 授權條款
本儲存庫採用 GNU General Public License v3.0 授權。請參閱 [LICENSE](LICENSE)。


## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |
