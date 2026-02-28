[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# Leonard Susskind 강의 노트 저장소

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

> 🎓 Leonard Susskind 강의 노트 자료의 다국어 아카이브입니다. 정리된 PDF와 편집 가능한 LaTeX 소스를 모두 보존해 학습, 재사용, 참조에 활용할 수 있습니다.

## 개요
이 저장소는 Leonard Susskind 교수의 교육 생태계에서 제공된 강의 노트 자료를 콘텐츠 우선 방식으로 아카이브한 저장소입니다.

> Leonard Susskind 교수의 강의 노트입니다. 이 자료가 저작권을 침해한다고 판단되면 삭제를 위해 연락해 주세요. 강의 노트의 오류나 오정보에 대해서는 Susskind 교수님도, 저도 책임지지 않습니다.

한 곳에서 세 가지 층위를 결합합니다.

- 정돈된 강의 트랙과 과정별 진행 상황
- 읽기/공유를 위한 공개 산출물 (`.pdf`)
- 아카이브를 유지·확장할 수 있도록 원본 파일 (`.tex`, `.bib`, 템플릿)

### 주요 목표
- 강의 노트와 진행 상황을 한 곳에서 통합해 관리합니다.
- 핵심 트랙과 보조 트랙 전반의 초안/노트 진행 가시성을 유지합니다.
- 계속 작성할 수 있도록 원본 자료(PDF, TeX, BibTeX, 템플릿)를 제공합니다.

## 기능
- 핵심 과목 진행 추적과 참조 정리.
- 보조 과목 진행 추적.
- 여러 핵심 트랙의 기존 레슨 PDF 보유.
- 선택된 트랙의 LaTeX 원문 자료.
- `template/tuftle`와 `template/kaobook`의 재사용 가능한 LaTeX 템플릿.
- `figs/`의 저장소 시각 자료.
- `i18n/`의 다국어 README 구성.

## 빠른 현황
| 영역 | 사용 가능 항목 |
|---|---|
| 📝 노트 | 진행 상황 추적이 포함된 여러 강의 노트 집합 |
| 🧾 소스 | 선택된 하위 프로젝트의 TeX/BibTeX 원본 |
| 🧱 템플릿 | `template/tuftle` 및 `template/kaobook` |
| 🎨 브랜드 요소 | `figs/banner.*`, `figs/logo.*`, `figs/logo-w-text.*` |
| 🌍 i18n | `i18n/README.*.md` 언어 버전 |

## 목차
- [개요](#개요)
- [기능](#기능)
- [빠른 현황](#빠른-현황)
- [프로젝트 구조](#프로젝트-구조)
- [사전 요구사항](#사전-요구사항)
- [설치](#설치)
- [사용법](#사용법)
- [구성](#구성)
- [예시](#예시)
- [개발 노트](#개발-노트)
- [표준 강의 진행 상황(보존 및 재구성)](#표준-강의-진행-상황보존-및-재구성)
- [문제 해결](#문제-해결)
- [로드맵](#로드맵)
- [기여](#기여)
- [❤️ Support](#-support)
- [감사의 말](#감사의-말)
- [라이선스](#라이선스)

## 프로젝트 구조
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

## 사전 요구사항
읽기 전용 사용:
- PDF 리더(시스템 또는 앱 기반).

TeX 자료 편집/빌드 시:
- LaTeX 배포판(TeX Live / MiKTeX).
- `pdflatex`.
- 하위 프로젝트에 따라 `bibtex` 또는 `biber`.
- 색인 항목을 사용하는 프로젝트는 `makeindex`.

참고:
- 이 저장소에는 루트 수준의 단일 빌드 시스템(`Makefile`, `package.json`, `pyproject.toml`)이 보이지 않습니다.
- 빌드 워크플로는 각 하위 프로젝트 디렉터리에서 실행되는 것으로 가정합니다.

## 설치
```bash
git clone https://github.com/lachlanchen/leonardsusskind.git
cd leonardsusskind
```

이 저장소는 콘텐츠 우선 구조입니다. 포크 또는 미러된 경우, 원격 URL을 본인 저장소 주소로 바꿔 사용하세요.

기존 노트 열람에는 별도의 패키지 설치가 필요하지 않습니다.

## 사용법
### 1) 기존 노트 읽기
관련 폴더에서 PDF를 열어 보세요. 예:
- `core_general_relativity/lesson_1.pdf`
- `core_cosmology/lesson_1.pdf`
- `core_statistical_mechanics/lesson_1.pdf`
- `supplemental_particle_physics_2/NumberTheory.pdf`

### 2) LaTeX 자료 작성 또는 확장하기
- 대상 과목/템플릿 폴더에서 `.tex` 및 `.bib` 파일을 편집합니다.
- 해당 폴더의 워크플로우에 맞게 컴파일합니다.
- 지역 상대 경로와 스타일 파일이 올바르게 해석되도록 프로젝트 폴더 내부에서 빌드합니다.

### 3) 트랙 단위 진입점으로 탐색하기
각 주요 트랙에는 범위가 분리된 노트와 참조, 진행 상황이 들어 있는 `README.md`가 있습니다.

## 구성
전역 구성 파일은 없습니다.

구성은 각 TeX 프로젝트에서 로컬로 관리됩니다. 보통 문서 소스에 설정값이 내장되어 있습니다.
- 문서 클래스 및 패키지 설정: `template/kaobook/main.tex`
- `template/kaobook/`의 재사용 가능한 스타일/구조
- 로컬 `main.tex`/`ref.bib` 쌍의 참고문헌 백엔드 및 인용 스타일
- 각 프로젝트의 이미지/챕터 자산 경로 설정

주요 로컬 구성 지점:
- `template/kaobook/main.tex`
- `template/tuftle/main.tex`
- `core_cosmology/cosmology_ch10/cosmology_ch10.tex`
- `supplemental_particle_physics_1/ch1/main.tex`
- `supplemental_advanced_quantum/ch1/main.tex`

## 예시
### 예시 A: `template/kaobook` 빌드
`template/kaobook/main.tex`는 다음 컴파일 흐름을 보여줍니다.

```bash
cd template/kaobook
pdflatex main
makeindex main.idx -s StyleInd.ist
biber main
pdflatex main
pdflatex main
```

### 예시 B: `core_cosmology/cosmology_ch10` 빌드
`cosmology_ch10.tex`는 BibTeX 스타일 워크플로우를 사용합니다.

```bash
cd core_cosmology/cosmology_ch10
pdflatex cosmology_ch10.tex
bibtex cosmology_ch10
pdflatex cosmology_ch10.tex
pdflatex cosmology_ch10.tex
```

### 예시 C: `supplemental_particle_physics_1/ch1` 빌드
```bash
cd supplemental_particle_physics_1/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### 예시 D: `supplemental_advanced_quantum/ch1` 빌드
```bash
cd supplemental_advanced_quantum/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### 예시 E: 출력물을 로컬에서 보기
```bash
xdg-open supplemental_particle_physics_1/ch1/main.pdf
```

## 개발 노트
- 이 저장소는 애플리케이션 코드베이스가 아니라 문서/노트 저장소 중심의 저장소입니다.
- 일부 폴더에는 생성된 TeX 산출물(`.aux`, `.log`, `.toc`, `.bbl` 등)이 저장소에 커밋되어 있습니다.
- 빌드 명령은 하위 디렉터리마다 다를 수 있으므로 로컬 `.tex` 규칙을 따라야 합니다.
- 핵심 및 보조 디렉터리 전반에 트랙별 `README.md` 파일이 있으며 루트 진행 상황과 정렬되어야 합니다.
- `i18n/`가 다국어 README 변형에 사용됩니다.
- 루트 README는 기준으로 간주되며, 로컬 파일은 업데이트 시 이를 따라야 합니다.

## 표준 강의 진행 상황(보존 및 재구성)

### 핵심 강의

#### 고전 역학
이 강의의 교재 [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681)는 출판이 완료되었습니다. Amazon에서 [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681)를 구매할 수 있습니다.

#### 양자 역학
이 강의의 교재 [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903)는 출판이 완료되었습니다. Amazon에서 [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903)를 구매할 수 있습니다.

#### 특수상대성이론과 전자기학
이 강의의 교재 [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065)는 출판이 완료되었습니다. Amazon에서 [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065)를 구매할 수 있습니다.

#### 핵심 진행표
| 과목 | 초안 진행도 | 노트 진행도 | 노트/참고 |
|---|---:|---:|---|
| General Relativity | 10/10 | 10/10 | 강의 노트는 https://www.lapasserelle.com/general_relativity/ 에서 정리되었습니다. |
| Cosmology | 10/10 | 9/10 | 1장부터 9장까지의 강의 노트는 https://www.lapasserelle.com/cosmology/ 에서 정리되었으며, 10장은 진행 중입니다. |
| Statistical Mechanics | 11/11 | 10/10 | 강의 노트는 https://www.lapasserelle.com/statistical_mechanics/ 에서 정리되었습니다. |

### 보조 강의
| 과목 | 초안 진행도 | 노트 진행도 |
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

### 진행 무결성 참고
- 위 진행표는 기준 README 텍스트에서 보존된 값입니다.
- 저장소에는 완성된 트랙과 플레이스홀더 트랙이 모두 포함됩니다. 표 항목과 폴더 상태가 맞지 않으면 문서화된 의도로 표를 우선하고 추후 함께 업데이트하세요.

## 문제 해결
| 문제 | 해결 방법 |
|---|---|
| `pdflatex: command not found` | LaTeX 배포판을 설치하고 바이너리가 `PATH`에 있는지 확인합니다. |
| 참고문헌/색인이 보이지 않음 | 필요한 백엔드(`bibtex` 또는 `biber`)와 사용 시 `makeindex`를 실행한 뒤 `pdflatex`를 다시 실행합니다. |
| 스타일/클래스 파일 오류 | 의도한 프로젝트 디렉터리에서 빌드해 지역 자산의 상대 경로가 올바르게 해석되도록 합니다. |
| 환경에 따라 빌드 결과가 달라짐 | 저장소에 다양한 환경에서 생성된 자료가 섞여 있으므로 가능하면 패키지 버전을 맞춰 정렬합니다. |
| 다국어 링크가 오래되었거나 언어별 README 누락 | 상단 언어 선택 줄과 `i18n/` 하위 파일을 동기화 상태로 유지하세요. |
| GitHub 마크다운 링크 불일치(폴더명 변경 후) | 루트 언어 링크와 모든 `i18n/README.*.md` 참조를 한 번에 재검증하세요. |

## 로드맵
- 보조 트랙을 실제 챕터 내용과 소스 파일로 계속 확장.
- 과목별 README 일관성 개선.
- `i18n/`에서 다국어 README 파일을 확장하고 언어 선택기를 동기화.
- TeX 소스가 있는 각 하위 프로젝트에 저장소 수준 빌드 가이드를 추가.
- 로컬 도구 체인 차이가 있는 트랙별 컴파일 스니펫 추가.
- README/i18n 링크 무결성 확인 자동화 최소화.

## 기여
이 프로젝트는 포크 후 풀 리퀘스트로 기여할 수 있습니다.

권장 기여 범위:
- 챕터 노트와 참조 추가/개선.
- TeX 소스 품질 및 재현 가능한 빌드 지침 개선.
- 루트와 과목별 README의 진행 상태 문구 동기화.
- `i18n/`에서 README 다국어 패리티 유지.

권장 PR 운영:
- 변경한 트랙 폴더를 정확히 명시.
- 소스 파일을 수정한 경우 사용한 TeX 컴파일 명령을 기재.
- 챕터 상태가 바뀌면 관련 진행표를 업데이트.
- 기준 영어 README 변경 후 `i18n/` README를 갱신.

## 감사의 말
- 원래 강의 콘텐츠를 제공한 Leonard Susskind 교수님께 감사드립니다.
- 기존 노트 참고 출처: https://www.lapasserelle.com/general_relativity/
- 기존 노트 참고 출처: https://www.lapasserelle.com/cosmology/
- 기존 노트 참고 출처: https://www.lapasserelle.com/statistical_mechanics/

## 라이선스
이 저장소는 GNU General Public License v3.0에 따라 라이선스됩니다. [LICENSE](../LICENSE)를 확인하세요.


## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |
