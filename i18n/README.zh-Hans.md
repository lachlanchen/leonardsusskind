[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


<p align="center">
  <img src="https://raw.githubusercontent.com/lachlanchen/lachlanchen/main/logos/banner.png" alt="LazyingArt banner" />
</p>

# Leonard Susskind 讲义笔记仓库

![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg)
![Content Type](https://img.shields.io/badge/content-Lecture%20Notes%20%26%20LaTeX-informational)
![Status](https://img.shields.io/badge/status-Active%20Archive-success)
![LaTeX](https://img.shields.io/badge/tooling-LaTeX-008080)
![i18n](https://img.shields.io/badge/i18n-directory%20ready-orange)

## 📖 概览
本仓库是一个以内容为核心的归档项目，收录了与 Leonard Susskind 教授课程相关的讲义笔记资料。

这里是 Leonard Susskind 教授课程讲义的笔记整理。如果这侵犯了任何版权，请联系我删除本仓库。对于笔记中的错误或不实信息，Susskind 教授不承担责任，我也不承担责任。

### 主要目标
- 将课程笔记与进度统一维护在同一仓库中。
- 保留核心课程与补充课程的草稿/笔记进度可见性。
- 提供可持续编写所需的源材料（PDF、TeX、BibTeX、模板）。

## ✨ 特性
- 核心课程的进度追踪与参考资料。
- 补充课程的进度追踪。
- 多个核心课程方向已包含现成 PDF 讲义。
- 部分课程方向提供 LaTeX 源文件。
- 在 `template/tuftle` 和 `template/kaobook` 中提供可复用 LaTeX 模板。
- 仓库视觉资源位于 `figs/`。

## 📌 快速概览
| 区域 | 已提供内容 |
|---|---|
| 📚 笔记 | 多套课程笔记及进度追踪 |
| 🧪 源文件 | 部分子项目包含 TeX/BibTeX 源文件 |
| 🧰 模板 | `template/tuftle` 和 `template/kaobook` |
| 🌐 i18n | `i18n/` 目录已存在（目前为空） |

## 🗂️ 项目结构
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

## 🧩 先决条件
仅阅读内容时：
- 一个 PDF 阅读器。

编辑/构建 TeX 材料时：
- LaTeX 发行版（TeX Live / MiKTeX）。
- `pdflatex`。
- 根据子项目需求使用 `bibtex` 或 `biber`。
- 对使用索引的模板，需安装 `makeindex`。

假设说明：
- 本仓库根目录没有统一的构建系统（`Makefile`、`package.json`、`pyproject.toml`）。

## 🚀 安装
```bash
git clone https://github.com/<your-user>/leonardsusskind.git
cd leonardsusskind
```

基础使用（阅读现有笔记）不需要额外安装包。

## 🛠️ 使用方式
### 1) 阅读现有笔记
- 打开相应目录中的 PDF，例如：
  - `core_general_relativity/lesson_1.pdf`
  - `core_cosmology/lesson_1.pdf`
  - `core_statistical_mechanics/lesson_1.pdf`

### 2) 编辑 LaTeX 材料
- 在目标课程/模板目录中编辑 `.tex` 和 `.bib` 文件。
- 使用该目录预期的工具链进行编译。

## ⚙️ 配置
本仓库没有全局配置文件。

配置按各个 TeX 项目本地维护（文档类、参考文献后端、样式文件、图形路径），例如：
- `template/kaobook/main.tex`
- `template/tuftle/main.tex`
- `core_cosmology/cosmology_ch10/cosmology_ch10.tex`

## 🧪 示例
### 示例 A：构建 `template/kaobook`
`template/kaobook/main.tex` 记录了如下编译链：

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

### 示例 C：查看已生成章节 PDF
```bash
xdg-open supplemental_particle_physics_1/ch1/main.pdf
```

## 📝 开发说明
- 这里主要是文档/笔记仓库，而不是应用程序代码库。
- 部分目录提交了 TeX 生成产物（`.aux`、`.log`、`.toc`、`.bbl` 等）。
- 构建命令会随子目录而变化，请遵循本地 `.tex` 约定。
- `i18n/` 已存在，并预留用于多语言 README 变体。

## 📚 规范化课程进度（已保留并重组）

### 核心课程

#### Classical Mechanics
本课程教材 [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681) 已出版。你可以在 Amazon 购买 [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681)。

#### Quantum Mechanics
本课程教材 [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903) 已出版。你可以在 Amazon 购买 [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903)。

#### Special Relativity and Electrodynamics
本课程教材 [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065) 已出版。你可以在 Amazon 购买 [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065)。

#### 核心进度表
| 课程 | 草稿进度 | 笔记进度 | 笔记/参考 |
|---|---:|---:|---|
| General Relativity | 10/10 | 10/10 | The lecture notes had been taken by https://www.lapasserelle.com/general_relativity/ . |
| Cosmology | 10/10 | 9/10 | The lecture notes, from chapter 1 to 9, had been taken by https://www.lapasserelle.com/cosmology/ . The chapter 10 is in the process. |
| Statistical Mechanics | 11/11 | 10/10 | The lecture notes had been taken by https://www.lapasserelle.com/statistical_mechanics/. |

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

## 🧯 故障排查
- `pdflatex: command not found`
  - 安装 LaTeX 发行版，并确保其二进制文件在 `PATH` 中。
- 参考文献/索引未显示
  - 运行所需后端（`bibtex` 或 `biber`）和 `makeindex`（如有使用），然后重新运行 `pdflatex`。
- 缺少样式/类文件错误
  - 请在目标项目目录下构建，确保本地资源的相对路径能够正确解析。
- 不同环境下构建结果不一致
  - 本仓库材料来自不同环境，尽可能对齐相关包版本。

## 🗺️ 路线图
- 持续补充补充课程的实际章节内容与源文件。
- 提升各课程 README 的一致性。
- 在 `i18n/` 下添加多语言 README，并保持语言选择器同步。
- 为包含 TeX 源文件的子项目补充仓库级构建指引。

## ❤️ 贡献或捐助
你可以通过 fork 本项目并提交 pull request 来参与贡献。如果这个项目帮你节省了开发时间，也欢迎请我喝杯咖啡 :)

## 🙏 致谢
- 感谢 Leonard Susskind 教授提供原始课程内容。
- 已引用的现有笔记来源：
  - https://www.lapasserelle.com/general_relativity/
  - https://www.lapasserelle.com/cosmology/
  - https://www.lapasserelle.com/statistical_mechanics/

## 📄 许可证
本仓库采用 GNU General Public License v3.0 许可。详见 [LICENSE](LICENSE)。
