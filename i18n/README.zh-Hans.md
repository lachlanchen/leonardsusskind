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

## 概览
本仓库是一个以内容为核心的讲义资料档案，收录了与 Leonard Susskind 教授课程相关的材料。

> 这是 Leonard Susskind 教授的课程讲义笔记。若此举涉及任何版权问题，请联系我以删除本仓库。Susskind 教授对笔记中的错误或误导性信息不承担责任，我也不承担责任。

### 主要目标
- 将课程笔记与进度集中管理在一个地方。
- 在核心与补充课程中保留草稿和笔记进度的可见性。
- 提供可持续创作所需的源材料（PDF、TeX、BibTeX、模板）。

## 特性
- 核心课程进度跟踪与参考资料。
- 补充课程进度跟踪。
- 多个核心课程已提供现成的课程 PDF。
- 部分课程方向提供 LaTeX 源文件。
- 在 `template/tuftle` 和 `template/kaobook` 中可复用的 LaTeX 模板。
- 仓库视觉资源位于 `figs/`。
- 多语言 README 位于 `i18n/`。

## 快速快照
| 区域 | 可用内容 |
|---|---|
| 📝 笔记 | 多套课程笔记及其进度跟踪 |
| 🧾 源文件 | 部分子项目包含 TeX/BibTeX 源 |
| 🧱 模板 | `template/tuftle` 与 `template/kaobook` |
| 🎨 品牌素材 | `figs/banner.*`、`figs/logo.*`、`figs/logo-w-text.*` |
| 🌍 i18n | `i18n/README.*.md` 多语言版本 |

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
仅阅读时：
- 一个 PDF 阅读器。

编辑/构建 TeX 材料时：
- LaTeX 发行版（TeX Live / MiKTeX）。
- `pdflatex`。
- 根据子项目不同，使用 `bibtex` 或 `biber`。
- 若模板使用索引功能，需要 `makeindex`。

注意：
- 仓库根目录没有单一的构建系统（`Makefile`、`package.json`、`pyproject.toml`）。

## 安装
```bash
git clone https://github.com/<your-user>/leonardsusskind.git
cd leonardsusskind
```

如果此仓库被 fork 或镜像，请把 `<your-user>` 替换为正确账户。

基础阅读现有笔记不需要额外安装软件包。

## 使用说明
### 1) 阅读现有笔记
打开相关目录中的 PDF，例如：
- `core_general_relativity/lesson_1.pdf`
- `core_cosmology/lesson_1.pdf`
- `core_statistical_mechanics/lesson_1.pdf`
- `supplemental_particle_physics_2/NumberTheory.pdf`

### 2) 编辑 LaTeX 材料
- 在目标课程/模板目录中编辑 `.tex` 和 `.bib` 文件。
- 使用该目录预期的工具链执行编译。
- 建议在本地项目目录内运行构建命令，以确保相对路径正确解析。

### 3) 按课程 README 导航
每个主要课程都有自己的 `README.md`，提供对应范围的笔记与进度上下文。

## 配置
不存在全局配置文件。

配置在各个 TeX 项目本地管理（文档类、参考文献后端、样式文件、图片路径等），例如：
- `template/kaobook/main.tex`
- `template/tuftle/main.tex`
- `core_cosmology/cosmology_ch10/cosmology_ch10.tex`
- `supplemental_particle_physics_1/ch1/main.tex`
- `supplemental_advanced_quantum/ch1/main.tex`

## 示例
### 示例 A：构建 `template/kaobook`
`template/kaobook/main.tex` 记录了如下编译流程：

```bash
cd template/kaobook
pdflatex main
makeindex main.idx -s StyleInd.ist
biber main
pdflatex main
pdflatex main
```

### 示例 B：构建 `core_cosmology/cosmology_ch10`
`cosmology_ch10.tex` 使用 `\bibliography{ref}`（BibTeX 风格流程）：

```bash
cd core_cosmology/cosmology_ch10
pdflatex cosmology_ch10.tex
bibtex cosmology_ch10
pdflatex cosmology_ch10.tex
pdflatex cosmology_ch10.tex
```

### 示例 C：构建基于 Tufte 的章节（`supplemental_particle_physics_1/ch1`）
```bash
cd supplemental_particle_physics_1/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### 示例 D：构建基于 Tufte 的章节（`supplemental_advanced_quantum/ch1`）
```bash
cd supplemental_advanced_quantum/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### 示例 E：查看生成的章节 PDF
```bash
xdg-open supplemental_particle_physics_1/ch1/main.pdf
```

## 开发说明
- 这是一个以文档/笔记为主的仓库，而非应用程序代码库。
- 某些文件夹提交了生成的 TeX 文件（`.aux`、`.log`、`.toc`、`.bbl` 等）。
- 构建命令会因子目录而异，请遵循该目录中的 `.tex` 约定。
- 各核心/补充目录均有按课程 `README.md`，应保持与根目录进度说明一致。
- `i18n/` 用于多语言 README 变体。
- 根 README 被视为权威版本，多语言文件更新时应保持同步。

## 标准化课程进度（已保留并重组）

### 核心课程

#### 古典力学
该课程教材 [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681) 已出版。你可以在 Amazon 购买 [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681)。

#### 量子力学
该课程教材 [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903) 已出版。你可以在 Amazon 购买 [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903)。

#### 狭义相对论与电动力学
该课程教材 [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065) 已出版。你可以在 Amazon 购买 [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065)。

#### 核心进度表
| 课程 | 草稿进度 | 笔记进度 | 笔记/参考 |
|---|---:|---:|---|
| General Relativity | 10/10 | 10/10 | 讲稿来自 https://www.lapasserelle.com/general_relativity/ 。 |
| Cosmology | 10/10 | 9/10 | 讲义笔记由 https://www.lapasserelle.com/cosmology/ 提供，第 1 章到第 9 章已录入，10 章正在进行中。 |
| Statistical Mechanics | 11/11 | 10/10 | 讲稿来自 https://www.lapasserelle.com/statistical_mechanics/ 。 |

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
- 上述进度表内容保持与权威 README 原文一致。
- 仓库文件同时包含成熟课程与占位课程；若表项与文件夹状态暂不一致，以表中记录作为文档化意图，并在未来修订时同步更新两者。

## 故障排查
| 问题 | 解决方法 |
|---|---|
| `pdflatex: command not found` | 安装 LaTeX 发行版，并确保二进制文件在 `PATH` 中。 |
| 参考文献/索引未显示 | 按需运行后端（`bibtex` 或 `biber`）和 `makeindex`（如果使用），然后重新运行 `pdflatex`。 |
| 样式/类文件缺失 | 在预期的项目目录内构建，以确保本地资源的相对路径能正确解析。 |
| 不同环境构建结果不一致 | 仓库材料源自不同环境构建，尽量对齐相关依赖版本。 |
| 多语言链接陈旧或缺失语言版 | 请确保顶部语言列表与 `i18n/` 下文件保持同步。 |
| 文件夹重命名后 GitHub 链接不匹配 | 一次性重新校验根语言链接和全部 `i18n/README.*.md` 引用。 |

## 路线图
- 持续补充补充课程的实际章节内容与源文件。
- 提升课程级 README 的一致性。
- 扩展并维护 `i18n/` 下的多语言 README，并保持语言选择器同步。
- 为有 TeX 源的子项目新增仓库级构建说明。
- 在本地工具链差异明显的课程中补充逐课程编译片段。
- 增加最小化自动化检查，验证 README/i18n 链接完整性。

## 贡献
你可以通过 fork 本项目并提交 pull request 参与贡献。

建议的贡献范围：
- 新增或改进章节笔记和参考资料。
- 改进 TeX 源质量并完善可复现构建说明。
- 保持根 README 与各课程 README 的进度表述一致。
- 在 `i18n/` 下维护 README 的多语言一致性。

推荐的 pull request 提交规范：
- 明确说明变更了哪些课程目录。
- 如修改源文件，请附上实际使用的 TeX 编译命令。
- 章节状态变化时更新对应进度表。
- 英文版 README 变更后同步更新 `i18n/` 各语言文件。

## ❤️ Support

| Donate | PayPal | Stripe |
|---|---|---|
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=ko-fi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 致谢
- 感谢 Leonard Susskind 教授提供原始课程内容。
- 已引用的现有笔记来源：
  - https://www.lapasserelle.com/general_relativity/
  - https://www.lapasserelle.com/cosmology/
  - https://www.lapasserelle.com/statistical_mechanics/

## 许可证
本仓库采用 GNU General Public License v3.0 授权。详见 [LICENSE](../LICENSE)。
