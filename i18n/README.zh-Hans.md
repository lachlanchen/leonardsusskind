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

> 🎓 一个多语种归档库，整理了 Leonard Susskind 的讲义资料，保留可阅读的精美 PDF 与可编辑的 LaTeX 源文件，便于学习、复用与引用。

## 概览
本仓库是一个以内容为先的讲义资料归档库，整理了 Leonard Susskind 教授课程体系中的课程材料。

> 这是 Leonard Susskind 教授的课程讲义。若有版权问题，请联系我删除该仓库。Susskind 教授不对讲义中的错误或错误信息负责，我亦不承担责任。

### 主要目标
- 在一个地方集中管理课程笔记与进度。
- 在核心轨道与补充轨道中保留草稿/笔记进度的可见性。
- 提供源材料（PDF、TeX、BibTeX、模板），便于持续编写与维护。

## 特性
- 核心课程跟踪与参考资料。
- 补充课程进度跟踪。
- 已提供若干核心轨道的课程 PDF。
- 已提供部分轨道的 LaTeX 源材料。
- 可复用的 LaTeX 模板位于 `template/tuftle` 与 `template/kaobook`。
- 仓库视觉素材位于 `figs/`。
- 多语 README 存放在 `i18n/`。

## 快速快照
| 区域 | 可用内容 |
|---|---|
| 📝 笔记 | 多套课程笔记并含进度追踪 |
| 🧾 源码 | 部分子项目提供 TeX/BibTeX 源文件 |
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
- [使用说明](#使用说明)
- [配置](#配置)
- [示例](#示例)
- [开发说明](#开发说明)
- [标准化课程进度（已保留并重组）](#标准化课程进度已保留并重组)
- [故障排查](#故障排查)
- [路线图](#路线图)
- [贡献](#贡献)
- [❤️ Support](#-support)
- [致谢](#致谢)
- [许可证](#许可证)

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

## 先决条件
阅读场景：
- 一个 PDF 阅读器（系统应用或命令行可读程序）。

编辑／构建 TeX 材料时：
- LaTeX 发行版（TeX Live / MiKTeX）。
- `pdflatex`。
- 按子项目不同，使用 `bibtex` 或 `biber`。
- 使用索引的项目还需要 `makeindex`。

说明：
- 仓库根目录不存在统一的构建入口（如 `Makefile`、`package.json`、`pyproject.toml`）。
- 各子项目的构建流程应在对应目录内执行。

## 安装
```bash
git clone https://github.com/lachlanchen/leonardsusskind.git
cd leonardsusskind
```

本仓库以内容为核心。若进行镜像或 fork，请按需将远程 URL 替换为你的仓库地址。

仅用于阅读现有笔记时无需安装全局依赖。

## 使用说明
### 1) 阅读现有笔记
打开对应文件夹中的 PDF，例如：
- `core_general_relativity/lesson_1.pdf`
- `core_cosmology/lesson_1.pdf`
- `core_statistical_mechanics/lesson_1.pdf`
- `supplemental_particle_physics_2/NumberTheory.pdf`

### 2) 编写或扩展 LaTeX 材料
- 在目标课程或模板目录编辑 `.tex` 与 `.bib` 文件。
- 按该目录规定的工作流编译。
- 在本地原路径下构建，以确保相对资源路径与样式文件被正确解析。

### 3) 按轨道入口文件导航
每个主轨道都有自己的 `README.md`，记录了范围化笔记与进度。

## 配置
仓库中不存在统一的配置文件。

配置在每个 TeX 项目内部本地维护，常见设置包括：
- `template/kaobook/main.tex` 中的文档类与宏包。
- `template/kaobook/` 中可复用的样式/结构。
- `template/tuftle/main.tex` 与对应 `ref.bib` 中的参考文献后端与引用样式。
- 每个项目中的图片与章节资源 include 路径。

典型配置入口：
- `template/kaobook/main.tex`
- `template/tuftle/main.tex`
- `core_cosmology/cosmology_ch10/cosmology_ch10.tex`
- `supplemental_particle_physics_1/ch1/main.tex`
- `supplemental_advanced_quantum/ch1/main.tex`

## 示例
### 示例 A：构建 `template/kaobook`
`template/kaobook/main.tex` 展示了如下编译链：

```bash
cd template/kaobook
pdflatex main
makeindex main.idx -s StyleInd.ist
biber main
pdflatex main
pdflatex main
```

### 示例 B：构建 `core_cosmology/cosmology_ch10`
`cosmology_ch10.tex` 使用 BibTeX 风格流程：

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

### 示例 E：本地查看输出
```bash
xdg-open supplemental_particle_physics_1/ch1/main.pdf
```

## 开发说明
- 这是一个文档/笔记仓库，而非应用程序代码库。
- 某些文件夹提交了生成后的 TeX 产物（如 `.aux`、`.log`、`.toc`、`.bbl` 等）。
- 构建命令可能因子目录不同而变化；请遵循本地 `.tex` 约定。
- 各主课程与补充课程下都有 `README.md`，应与根目录进度声明保持一致。
- `i18n/` 用于托管多语言 README。
- 根 README 被视为规范版本，本地化文件更新时应与之对齐。

## 标准化课程进度（已保留并重组）

### 核心课程

#### 古典力学
本课程教材 [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681) 已出版，你可以从 Amazon 购买 [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681)。

#### 量子力学
本课程教材 [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903) 已出版，你可以从 Amazon 购买 [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903)。

#### 狭义相对论与电动力学
本课程教材 [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065) 已出版，你可以从 Amazon 购买 [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065)。

#### 核心进度表
| 课程 | 草稿进度 | 笔记进度 | 笔记/参考 |
|---|---:|---:|---|
| General Relativity | 10/10 | 10/10 | 讲义内容由 https://www.lapasserelle.com/general_relativity/ 采集。 |
| Cosmology | 10/10 | 9/10 | 第1章至第9章讲义已采集自 https://www.lapasserelle.com/cosmology/，第10章仍在进行中。 |
| Statistical Mechanics | 11/11 | 10/10 | 讲义内容由 https://www.lapasserelle.com/statistical_mechanics/ 采集。 |

### 补充课程
| 课程 | 草稿进度 | 笔记进度 |
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

### 进度完整性说明
- 上方进度表内容沿用英文主 README 的原文。
- 仓库包含已完成与占位的轨道；若表格条目与目录实际状态存在不一致，请以表格为项目内定义并在后续更新中同步两者。

## 故障排查
| 问题 | 解决方案 |
|---|---|
| `pdflatex: command not found` | 安装 LaTeX 发行版并确保二进制已加入 `PATH`。 |
| 参考文献或索引未显示 | 按项目要求执行后端（`bibtex` 或 `biber`）并在使用时运行 `makeindex`，然后重跑 `pdflatex`。 |
| 缺少样式/类文件 | 请在目标项目目录内构建，使本地资源和样式文件的相对路径正确解析。 |
| 不同环境导致构建结果不一致 | 仓库中的材料来自不同环境；尽量对齐使用的依赖版本。 |
| 多语链接陈旧或缺失语言 README | 确保语言导航与 `i18n/` 中所有文件持续同步。 |
| 文件夹重命名后 GitHub 链接失配 | 一次性校验根 README 的语言链接及所有 `i18n/README.*.md` 引用。 |

## 路线图
- 继续完善补充课程的真实章节内容和源文件。
- 提升每个课程 README 的一致性。
- 扩展并维护 `i18n/` 下多语 README，保持语言选择同步。
- 为每个含 TeX 源的子项目补充仓库级别构建指引。
- 在不同工具链差异明显的课程中补充单轨编译片段。
- 增加最小化自动化检查，验证 README/i18n 链接完整性。

## 贡献
你可以通过 fork 项目并提交 pull request 进行贡献。

建议贡献范围：
- 新增或改进章节笔记与参考文献。
- 改善 TeX 源质量并补充可复现构建说明。
- 保持根目录与课程 README 的进度声明同步。
- 维护 `i18n/` 中多语 README 的一致性。

建议的 PR 规范：
- 明确说明改动涉及的课程目录。
- 如果修改了源文件，请附上实际使用的 TeX 编译命令。
- 课程章节状态变化时更新对应进度表。
- 英文主 README 更新后同步更新 `i18n/` README。

## 致谢
- 感谢 Leonard Susskind 教授提供原始课程内容。
- 已引用的笔记来源：
  - https://www.lapasserelle.com/general_relativity/
  - https://www.lapasserelle.com/cosmology/
  - https://www.lapasserelle.com/statistical_mechanics/

## 许可证
本仓库采用 GNU 通用公共许可证 v3.0 授权。详见 [LICENSE](../LICENSE)。


## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |
