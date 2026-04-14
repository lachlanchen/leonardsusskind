[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)



[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# Leonard Susskind 讲义笔记仓库

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

> 🎓 一个多语种归档项目，保留 Leonard Susskind 的课程讲义 PDF 与可编辑 LaTeX 源文件，便于学习、复用和查阅。

---

## 概览
本仓库是以内容为核心的讲义资料归档库，集中汇总了 Leonard Susskind 教授教学体系中的课程材料。

> 这是 Leonard Susskind 教授的课程讲义。若有版权问题，请联系我以删除该仓库。Susskind 教授不对讲义中的错误或误导性信息负责，我也不负责。

### 主要目标
- 把课程笔记与进度集中管理在一个位置。
- 在核心轨道与补充轨道中保留草稿和笔记进度的可见性。
- 提供源材料（PDF、TeX、BibTeX、模板），便于继续编辑和扩展。

## 特性
- 📚 核心课程跟踪和参考资料。
- 📌 补充课程进度跟踪。
- 📄 若干核心轨道已提供课程 PDF。
- 🧪 部分轨道提供 LaTeX 源文件。
- 🧷 可复用 LaTeX 模板位于 `template/tuftle` 与 `template/kaobook`。
- 🎨 仓库视觉资源位于 `figs/`。
- 🌐 多语言 README 集合位于 `i18n/`。

## 快速快照
| 区域 | 可用内容 |
|---|---|
| 📝 笔记 | 多套课程笔记并带有进度追踪 |
| 🧾 源码 | 选定子项目提供 TeX/BibTeX 源文件 |
| 🧱 模板 | `template/tuftle` 与 `template/kaobook` |
| 🎨 品牌素材 | `figs/banner.*`、`figs/logo.*`、`figs/logo-w-text.*` |
| 🌍 国际化 | `i18n/README.*.md` 多语言版本 |

## 目录
- [概览](#概览)
- [特性](#特性)
- [快速快照](#快速快照)
- [项目结构](#项目结构)
- [先决条件](#先决条件)
- [安装](#安装)
- [用法](#用法)
- [配置](#配置)
- [示例](#示例)
- [开发说明](#开发说明)
- [标准化课程进度（已保留并重组）](#标准化课程进度已保留并重组)
- [故障排除](#故障排除)
- [路线图](#路线图)
- [贡献](#贡献)
- [❤️ Support](#-support)
- [致谢](#致谢)
- [许可](#许可)

## 项目结构
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

## 先决条件
用于阅读：
- 📖 PDF 阅读器（系统自带或 App 都可以）。

用于编辑/构建 TeX 材料：
- 📦 LaTeX 发行版（TeX Live / MiKTeX）。
- ⚙️ `pdflatex`。
- 🗂️ 根据子项目使用 `bibtex` 或 `biber`。
- 🔎 对使用索引的项目，需要 `makeindex`。

---

说明：
- 根目录不存在统一的构建系统（如 `Makefile`、`package.json`、`pyproject.toml`）。
- 构建流程应在各子项目目录中分别执行。

## 安装
```bash
# Clone the repository
git clone https://github.com/lachlanchen/leonardsusskind.git
cd leonardsusskind
```

本仓库以内容为中心。如果你要镜像或 fork，请将远程地址替换为你的仓库地址。

仅阅读现有笔记不需要安装任何全局依赖。

## 用法
### 1) 阅读现有笔记
打开对应目录下的 PDF，例如：
- `core_general_relativity/lesson_1.pdf`
- `core_cosmology/lesson_1.pdf`
- `core_statistical_mechanics/lesson_1.pdf`
- `supplemental_particle_physics_2/NumberTheory.pdf`

### 2) 编写或扩展 LaTeX 材料
- 在目标课程/模板目录编辑 `.tex` 和 `.bib` 文件。
- 按该目录指定的流程编译。
- 在本地目录内构建以确保相对路径和样式文件解析正确。

### 3) 按轨道入口文件导航
每个主要轨道都有自己的 `README.md`，包含该轨道的范围说明、参考资料和进度。

## 配置
根目录不存在全局配置文件。

配置在每个 TeX 项目内本地维护，常见位置包括：
- `template/kaobook/main.tex` 中的文档类与宏包设置。
- `template/kaobook/` 中可复用的样式和结构。
- 本地 `main.tex`/`ref.bib` 对中的文献后端与引用样式。
- 各项目中的图片与章节资源 include 路径。

典型配置入口：
- `template/kaobook/main.tex`
- `template/tuftle/main.tex`
- `core_cosmology/cosmology_ch10/cosmology_ch10.tex`
- `supplemental_particle_physics_1/ch1/main.tex`
- `supplemental_advanced_quantum/ch1/main.tex`

## 示例
### 示例 A：构建 `template/kaobook`
`template/kaobook/main.tex` 展示了以下编译链：

```bash
cd template/kaobook
pdflatex main
makeindex main.idx -s StyleInd.ist
biber main
pdflatex main
pdflatex main
```

### 示例 B：构建 `core_cosmology/cosmology_ch10`
`cosmology_ch10.tex` 使用类似 BibTeX 的流程：

```bash
cd core_cosmology/cosmology_ch10
pdflatex cosmology_ch10.tex
bibtex cosmology_ch10
pdflatex cosmology_ch10.tex
pdflatex cosmology_ch10.tex
```

### 示例 C：构建 `supplemental_particle_physics_1/ch1`
```bash
cd supplemental_particle_physics_1/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### 示例 D：构建 `supplemental_advanced_quantum/ch1`
```bash
cd supplemental_advanced_quantum/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### 示例 E：在本地查看输出
```bash
xdg-open supplemental_particle_physics_1/ch1/main.pdf
```

## 开发说明
- 这是一个以文档/笔记为主的仓库，而非应用程序代码库。
- 某些文件夹会提交生成的 TeX 构建产物（如 `.aux`、`.log`、`.toc`、`.bbl` 等）。
- 构建命令会因子目录而异，请遵循各目录内的 `.tex` 约定。
- 核心与补充课程下都存在 `README.md`，应与根 README 的进度说明保持一致。
- `i18n/` 用于托管多语言 README。
- 根 README 被视为权威版本，本地化文件应与其保持同步。

## 标准化课程进度（已保留并重组）

### 核心课程

#### 古典力学
本课程教材 [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681) 已出版，可在 Amazon 购买 [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681)。

#### 量子力学
本课程教材 [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903) 已出版，可在 Amazon 购买 [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903)。

#### 狭义相对论与电动力学
本课程教材 [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065) 已出版，可在 Amazon 购买 [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065)。

#### 核心进度表
| 课程 | 草稿进度 | 笔记进度 | 笔记/参考 |
|---|---:|---:|---|
| 一般相对论 | 10/10 | 10/10 | 讲义由 https://www.lapasserelle.com/general_relativity/ 采集。 |
| 宇宙学 | 10/10 | 9/10 | 讲义在第 1 章到第 9 章由 https://www.lapasserelle.com/cosmology/ 采集，当前第 10 章仍在进行中。 |
| 统计力学 | 11/11 | 10/10 | 讲义由 https://www.lapasserelle.com/statistical_mechanics/ 采集。 |

### 补充课程
| 课程 | 草稿进度 | 笔记进度 |
|---|---:|---:|
| 进阶量子力学 | 0/10 | 0/10 |
| 希格斯玻色子 | 0/1 | 0/1 |
| 量子纠缠 | 0/9 | 0/9 |
| 相对论 | 0/9 | 0/9 |
| 粒子物理学 1：基础概念 | 6/10 | 0/10 |
| 粒子物理学 2：标准模型 | 0/10 | 0/10 |
| 粒子物理学 3：超对称与大统一理论 | 0/10 | 0/10 |
| 弦理论 | 0/11 | 10/10 |
| 宇宙学与黑洞 | 0/8 | 0/10 |

### 进度完整性说明
- 上述进度表内容沿用了英文主 README 中的原始表述。
- 仓库同时包含成熟内容与占位内容；若表格条目与实际目录状态出现不一致，请以该表为文档化目标，并在后续版本中同步更新。

## 故障排除
| 问题 | 解决方案 |
|---|---|
| `pdflatex: command not found` | 安装 LaTeX 发行版并确保可执行文件在 `PATH` 中。 |
| 参考文献/索引未显示 | 运行项目所需后端（`bibtex` 或 `biber`），如有索引再运行 `makeindex`，然后重跑 `pdflatex`。 |
| 缺少样式或类文件错误 | 在对应项目目录中进行构建，确保本地资源和样式文件的相对路径被正确解析。 |
| 不同环境下构建结果不同 | 本仓库的材料来自不同环境，尽量统一版本依赖。 |
| 语言链接过期或缺少语言 README | 确保顶部语言选项行与 `i18n/` 下的文件持续保持同步。 |
| 文件夹改名后 GitHub 链接不匹配 | 统一重检根 README 与所有 `i18n/README.*.md` 的链接。 |

## 路线图
- 继续补齐补充轨道的真实章节内容与源文件。
- 提升各课程 README 的一致性。
- 扩展并维护 `i18n/` 下的多语言 README，并保持语言选择器同步。
- 为每个含 TeX 源的子项目补充仓库层级的构建说明。
- 在本地工具链差异明显的课程中补充单轨编译示例。
- 加入轻量化自动化检查，验证 README 与 i18n 链接完整性。

## 贡献
你可以通过 fork 并提交 pull request 来参与项目。

建议的贡献范围：
- 增加或改进章节笔记与参考资料。
- 提升 TeX 源质量并补充可复现的构建说明。
- 保持根 README 与各课程 README 的进度声明一致。
- 更新英文本 README 后，同步更新 `i18n/` 的语言版本。

建议的 PR 规范：
- 明确说明修改了哪些课程目录。
- 如果编辑过源文件，请附上实际执行的 TeX 编译命令。
- 章节状态变化时更新相关进度表。
- 英文 README 更新后同步更新 `i18n/` 下的 README。

## 致谢
- Leonard Susskind 教授提供原始讲义内容。
- 已引用的讲义来源：
  - https://www.lapasserelle.com/general_relativity/
  - https://www.lapasserelle.com/cosmology/
  - https://www.lapasserelle.com/statistical_mechanics/

## 许可
本仓库采用 GNU General Public License v3.0 授权。详情见 [LICENSE](LICENSE).


## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |
