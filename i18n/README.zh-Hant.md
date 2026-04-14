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

> 🎓 一個多語言講義檔案庫，保留了 Leonard Susskind 的講義 PDF 與可編輯 LaTeX 原始檔，供學習、重用與參考。

---

## 概覽
本儲存庫是以內容為核心的 Leonard Susskind 教授教學體系講義資料檔案庫。

> 這是 Leonard Susskind 教授的課堂筆記。若涉及版權問題，請聯繫我以刪除此儲存庫。Susskind 教授不對筆記中的錯誤或誤導性資訊負責，我也一樣不負責。

它在同一處彙整了三層內容：

- 精選課程軌道與課程進度。
- 已發布成果（`.pdf`）以供閱讀與分享。
- 原始檔（`.tex`、`.bib`、範本）供維護與延伸本檔案庫。

### 主要目標
- 將課程筆記與進度集中在同一位置。
- 在核心與補充軌道中保留草稿與筆記進度的可見性。
- 提供原始資料（PDF、TeX、BibTeX、範本）以支援後續撰寫。

## 特性
- 📚 核心課程追蹤與參考資源。
- 📌 補充課程進度追蹤。
- 📄 若干核心軌道已提供現有課程 PDF。
- 🧪 選定軌道包含 LaTeX 原始素材。
- 🧷 可重複使用的 LaTeX 範本位於 `template/tuftle` 與 `template/kaobook`。
- 🎨 儲存庫視覺素材位於 `figs/`。
- 🌐 多語言 README 組合位於 `i18n/`。

## 快速快照
| 區域 | 可用內容 |
|---|---|
| 📝 筆記 | 多套課程筆記並含進度追蹤 |
| 🧾 原始檔 | 指定子專案提供 TeX/BibTeX 檔案 |
| 🧱 範本 | `template/tuftle` 與 `template/kaobook` |
| 🎨 品牌素材 | `figs/banner.*`、`figs/logo.*`、`figs/logo-w-text.*` |
| 🌍 國際化 | `i18n/README.*.md` 多語言版本 |

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
├── core_classical_mechanics/
│   └── README.md
├── core_quantum_mechanics/
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
- 📖 PDF 閱讀器（系統內建或應用程式皆可）。

編修／建置 TeX 素材時：
- 📦 LaTeX 發行套件（TeX Live / MiKTeX）。
- ⚙️ `pdflatex`。
- 🗂️ 視子專案而定，使用 `bibtex` 或 `biber`。
- 🔎 使用索引的專案需有 `makeindex`。

---

備註：
- 根目錄沒有單一全域建置系統（例如 `Makefile`、`package.json`、`pyproject.toml`）。
- 建置流程預期在每個子專案目錄中個別執行。

## 安裝
```bash
# Clone the repository
git clone https://github.com/lachlanchen/leonardsusskind.git
cd leonardsusskind
```

本儲存庫以內容為先。若要鏡像或 Fork，請改為使用你自己的遠端網址。

閱讀現有筆記不需安裝任何全域套件。

## 使用方式
### 1) 閱讀現有筆記
開啟對應資料夾中的 PDF，例如：
- `core_general_relativity/lesson_1.pdf`
- `core_cosmology/lesson_1.pdf`
- `core_statistical_mechanics/lesson_1.pdf`
- `supplemental_particle_physics_2/NumberTheory.pdf`

### 2) 編寫或延伸 LaTeX 素材
- 在目標課程／範本資料夾編修 `.tex` 與 `.bib`。
- 依該資料夾指定流程進行編譯。
- 在當地目錄內建置，以確保本機相對路徑與樣式檔可正確解析。

### 3) 依軌道入口檔導覽
每個主要軌道都有自己的 `README.md`，提供該軌道的範圍說明、參考資料與進度。

## 設定
沒有全域設定檔。

設定位於各 LaTeX 專案內部，本地維護，常見位置如下：
- `template/kaobook/main.tex` 中的文件類別與套件設定。
- `template/kaobook/` 的可重複使用樣式與架構。
- 本地 `main.tex`／`ref.bib` 組合中的參考文獻後端與引用樣式。
- 各專案中的圖片與章節資源 include 路徑。

代表性本地設定點：
- `template/kaobook/main.tex`
- `template/tuftle/main.tex`
- `core_cosmology/cosmology_ch10/cosmology_ch10.tex`
- `supplemental_particle_physics_1/ch1/main.tex`
- `supplemental_advanced_quantum/ch1/main.tex`

## 範例
### 範例 A：建置 `template/kaobook`
`template/kaobook/main.tex` 說明了以下編譯流程：

```bash
cd template/kaobook
pdflatex main
makeindex main.idx -s StyleInd.ist
biber main
pdflatex main
pdflatex main
```

### 範例 B：建置 `core_cosmology/cosmology_ch10`
`cosmology_ch10.tex` 採用類似 BibTeX 的流程：

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

### 範例 E：在本機查看輸出結果
```bash
xdg-open supplemental_particle_physics_1/ch1/main.pdf
```

## 開發說明
- 這是主要以文件／筆記為主的儲存庫，非應用程式原始碼庫。
- 某些資料夾會提交已產生的 TeX 檔（如 `.aux`、`.log`、`.toc`、`.bbl` 等）。
- 編譯命令會依子目錄不同而有差異；請以各子目錄的 `.tex` 規範為準。
- 核心與補充目錄皆有對應 `README.md`，且應與根目錄進度主張保持一致。
- `i18n/` 用於管理多語言 README。
- 根 README 視為權威版本，本地化檔案應在更新時保持同步。

## 標準化課程進度（已保留並重組）

### 核心課程

#### 古典力學
此課程的教材 [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681) 已出版。你可以在 Amazon 購買 [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681)。

#### 量子力學
此課程的教材 [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903) 已出版。你可以在 Amazon 購買 [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903)。

#### 狹義相對論與電磁學
此課程的教材 [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065) 已出版。你可以在 Amazon 購買 [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065)。

#### 核心進度表
| 課程 | 草稿進度 | 筆記進度 | 筆記/參考 |
|---|---:|---:|---|
| 一般相對論 | 10/10 | 10/10 | 講義由 https://www.lapasserelle.com/general_relativity/ 取材。 |
| 宇宙學 | 10/10 | 9/10 | 第 1 至 9 章的講義由 https://www.lapasserelle.com/cosmology/ 取材，第 10 章尚在進行中。 |
| 統計力學 | 11/11 | 10/10 | 講義由 https://www.lapasserelle.com/statistical_mechanics/ 取材。 |

### 補充課程
| 課程 | 草稿進度 | 筆記進度 |
|---|---:|---:|
| 進階量子力學 | 0/10 | 0/10 |
| 希格斯玻色子 | 0/1 | 0/1 |
| 量子糾纏 | 0/9 | 0/9 |
| 相對論 | 0/9 | 0/9 |
| 粒子物理學 1：基礎觀念 | 6/10 | 0/10 |
| 粒子物理學 2：標準模型 | 0/10 | 0/10 |
| 粒子物理學 3：超對稱與大一統 | 0/10 | 0/10 |
| 弦理論 | 0/11 | 10/10 |
| 宇宙學與黑洞 | 0/8 | 0/10 |

### 進度完整性說明
- 上述進度表沿用英文主 README 的原始文本。
- 倉庫同時包含成熟內容與預留版塊；若表格條目與資料夾實際狀態不一致，請以表格為文件化目標，並於後續修訂同步更新。

## 疑難排解
| 問題 | 解法 |
|---|---|
| `pdflatex: command not found` | 安裝 LaTeX 發行套件，並確認可執行檔已加入 `PATH`。 |
| 書目／索引未顯示 | 先執行所需後端（`bibtex` 或 `biber`），若有索引再執行 `makeindex`，接著重跑 `pdflatex`。 |
| 缺少樣式／類別檔錯誤 | 請在目標專案目錄中建置，確保本機資源與樣式檔相對路徑解析正確。 |
| 不同環境下建置結果不同 | 此儲存庫含多個環境產生的內容；儘量調整套件版本以求一致。 |
| 語言連結過期或缺少語言 README | 請確保頂部語言清單及 `i18n/` 下各檔案保持同步。 |
| GitHub Markdown 連結在資料夾改名後不一致 | 請一次性重新確認根 README 與所有 `i18n/README.*.md` 連結。 |

## 路線圖
- 繼續補上補充軌道中的完整章節內容與原始檔。
- 提升各課程 README 的一致性。
- 擴充並維護 `i18n/` 內的多語言 README，並維持語言切換同步。
- 為每個含 TeX 原始檔的子專案新增專案層級建置指引。
- 在工具鏈差異明顯的軌道中補充每軌編譯範例。
- 導入輕量化流程自動檢查 README 與 i18n 連結完整性。

## 貢獻
你可透過 Fork 並提交 pull request 參與本專案。

建議的貢獻範圍：
- 增加或改進章節筆記與參考資料。
- 改善 TeX 原始檔品質並補上可重現建置指令。
- 保持根 README 與各課程 README 進度敘述同步。
- 每次更新英文 README 後，請同步更新 `i18n/` 的 README。

建議的 PR 規範：
- 明確列出變更的課程資料夾。
- 若有編修原始檔，請附上實際使用的 TeX 編譯命令。
- 章節狀態有變更時，更新對應進度表。
- 根據英文 README 變更，記得更新 `i18n/` 下的 README。

## 致謝
- Leonard Susskind 教授的原始講義內容。
- 已參考的講義來源：
  - https://www.lapasserelle.com/general_relativity/
  - https://www.lapasserelle.com/cosmology/
  - https://www.lapasserelle.com/statistical_mechanics/

## 授權
本儲存庫採用 GNU General Public License v3.0 授權。詳情請見 [LICENSE](LICENSE)。


## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |
