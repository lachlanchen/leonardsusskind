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

## 개요
이 저장소는 Leonard Susskind 교수의 강의와 관련된 강의 노트 자료를 콘텐츠 중심으로 아카이브한 공간입니다.

> Leonard Susskind 교수님의 강의 노트입니다. 저작권을 침해한다면 이 저장소를 삭제할 수 있도록 연락해 주세요. 노트의 오류나 잘못된 정보에 대해 Susskind 교수님도, 저도 책임지지 않습니다.

### 주요 목표
- 강의 노트와 진행 상황을 한곳에서 관리합니다.
- 핵심 트랙과 보조 트랙 전반에서 초안/노트 진행 상황의 가시성을 유지합니다.
- 작성 작업을 이어갈 수 있도록 원본 자료(PDF, TeX, BibTeX, 템플릿)를 제공합니다.

## 기능
- 핵심 강의 트랙 진행 상황 추적 및 참고 정보 제공.
- 보조 강의 트랙 진행 상황 추적.
- 여러 핵심 트랙의 기존 레슨 PDF 제공.
- 일부 트랙의 LaTeX 원본 자료 제공.
- `template/tuftle` 및 `template/kaobook`의 재사용 가능한 LaTeX 템플릿.
- `figs/`의 저장소 시각 자료.
- `i18n/`의 다국어 README 세트.

## 빠른 현황
| 영역 | 제공 내용 |
|---|---|
| 📝 노트 | 진행 상황 추적이 포함된 여러 강의 노트 세트 |
| 🧾 소스 | 일부 하위 프로젝트의 TeX/BibTeX 소스 |
| 🧱 템플릿 | `template/tuftle` 및 `template/kaobook` |
| 🎨 브랜딩 | `figs/banner.*`, `figs/logo.*`, `figs/logo-w-text.*` |
| 🌍 i18n | `i18n/README.*.md` 언어별 버전 |

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
읽기 전용 사용 시:
- PDF 리더.

TeX 자료를 편집/빌드할 때:
- LaTeX 배포판(TeX Live / MiKTeX).
- `pdflatex`.
- 하위 프로젝트에 따라 `bibtex` 또는 `biber`.
- 색인을 사용하는 템플릿의 경우 `makeindex`.

가정 참고:
- 이 저장소에는 루트 레벨의 단일 빌드 시스템(`Makefile`, `package.json`, `pyproject.toml`)이 없습니다.

## 설치
```bash
git clone https://github.com/<your-user>/leonardsusskind.git
cd leonardsusskind
```

이 저장소가 포크 또는 미러된 경우 `<your-user>`를 올바른 계정으로 바꿔 주세요.

기본 사용(기존 노트 열람)에는 별도의 패키지 설치가 필요하지 않습니다.

## 사용법
### 1) 기존 노트 읽기
예를 들어 관련 폴더의 PDF를 엽니다:
- `core_general_relativity/lesson_1.pdf`
- `core_cosmology/lesson_1.pdf`
- `core_statistical_mechanics/lesson_1.pdf`
- `supplemental_particle_physics_2/NumberTheory.pdf`

### 2) LaTeX 자료 작업
- 대상 강의/템플릿 폴더에서 `.tex` 및 `.bib` 파일을 편집합니다.
- 해당 폴더에서 기대하는 도구 체인으로 컴파일합니다.
- 상대 경로가 올바르게 해석되도록 로컬 프로젝트 디렉터리 안에서 빌드 명령을 실행하는 것을 권장합니다.

### 3) 트랙 README로 탐색
각 주요 트랙에는 범위가 분리된 노트와 진행 상황 문맥을 위한 로컬 `README.md`가 있습니다.

## 구성
전역 구성 파일은 없습니다.

구성은 각 TeX 프로젝트별로 로컬에서 관리됩니다(문서 클래스, 참고문헌 백엔드, 스타일 파일, 그래픽 경로). 예:
- `template/kaobook/main.tex`
- `template/tuftle/main.tex`
- `core_cosmology/cosmology_ch10/cosmology_ch10.tex`
- `supplemental_particle_physics_1/ch1/main.tex`
- `supplemental_advanced_quantum/ch1/main.tex`

## 예시
### 예시 A: `template/kaobook` 빌드
`template/kaobook/main.tex`에는 다음 컴파일 체인이 문서화되어 있습니다:

```bash
cd template/kaobook
pdflatex main
makeindex main.idx -s StyleInd.ist
biber main
pdflatex main
pdflatex main
```

### 예시 B: `core_cosmology/cosmology_ch10` 빌드
`cosmology_ch10.tex`는 `\bibliography{ref}`를 사용합니다(BibTeX 스타일 워크플로):

```bash
cd core_cosmology/cosmology_ch10
pdflatex cosmology_ch10.tex
bibtex cosmology_ch10
pdflatex cosmology_ch10.tex
pdflatex cosmology_ch10.tex
```

### 예시 C: Tufte 기반 챕터 빌드 (`supplemental_particle_physics_1/ch1`)
```bash
cd supplemental_particle_physics_1/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### 예시 D: Tufte 기반 챕터 빌드 (`supplemental_advanced_quantum/ch1`)
```bash
cd supplemental_advanced_quantum/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### 예시 E: 생성된 챕터 PDF 보기
```bash
xdg-open supplemental_particle_physics_1/ch1/main.pdf
```

## 개발 노트
- 이 저장소는 애플리케이션 코드베이스가 아니라 문서/노트 저장소가 중심입니다.
- 일부 폴더에는 생성된 TeX 산출물(`.aux`, `.log`, `.toc`, `.bbl` 등)이 저장소에 커밋되어 있습니다.
- 빌드 명령은 하위 디렉터리마다 다를 수 있으므로 로컬 `.tex` 관례를 따르세요.
- 핵심/보조 디렉터리 전반에 트랙별 `README.md`가 있으며, 루트 README의 진행 상태 문구와 일치하도록 유지해야 합니다.
- `i18n/`은 다국어 README 변형에 사용됩니다.
- 루트 README는 기준 문서로 취급되며, 다국어 파일은 업데이트 시 이를 따라야 합니다.

## 표준 강의 진행 상황(보존 및 재구성)

### 핵심 강의

#### 고전역학
이 강의의 교재 [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681)는 출판되었습니다. Amazon에서 [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681)를 구매할 수 있습니다.

#### 양자역학
이 강의의 교재 [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903)는 출판되었습니다. Amazon에서 [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903)를 구매할 수 있습니다.

#### 특수상대성이론과 전자기학
이 강의의 교재 [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065)는 출판되었습니다. Amazon에서 [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065)를 구매할 수 있습니다.

#### 핵심 진행 표
| 강의 | 초안 진행도 | 노트 진행도 | 노트/참고 |
|---|---:|---:|---|
| General Relativity | 10/10 | 10/10 | 강의 노트는 https://www.lapasserelle.com/general_relativity/ 의 자료를 참고해 작성되었습니다. |
| Cosmology | 10/10 | 9/10 | 1장부터 9장까지의 강의 노트는 https://www.lapasserelle.com/cosmology/ 의 자료를 참고해 작성되었으며, 10장은 진행 중입니다. |
| Statistical Mechanics | 11/11 | 10/10 | 강의 노트는 https://www.lapasserelle.com/statistical_mechanics/ 의 자료를 참고해 작성되었습니다. |

### 보조 강의
| 강의 | 초안 진행도 | 노트 진행도 |
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
- 위 진행 표는 기준 README 텍스트에서 보존한 내용입니다.
- 저장소 파일에는 성숙한 트랙과 자리표시자 트랙이 함께 포함되어 있습니다. 표 항목과 폴더 상태가 불일치해 보이면, 표를 문서화된 의도로 간주하고 이후 수정 시 둘 다 함께 업데이트하세요.

## 문제 해결
| 문제 | 해결 방법 |
|---|---|
| `pdflatex: command not found` | LaTeX 배포판을 설치하고 바이너리가 `PATH`에 포함되어 있는지 확인하세요. |
| 참고문헌/색인이 표시되지 않음 | 필요한 백엔드(`bibtex` 또는 `biber`)와 `makeindex`(사용 시)를 실행한 뒤 `pdflatex`를 다시 실행하세요. |
| 스타일/클래스 파일 누락 오류 | 로컬 자산에 대한 상대 경로가 올바르게 해석되도록 의도된 프로젝트 디렉터리에서 빌드하세요. |
| 환경에 따라 빌드 출력이 다름 | 이 저장소에는 서로 다른 환경에서 생성된 자료가 포함되어 있으므로 가능하면 패키지 버전을 맞추세요. |
| 다국어 링크가 오래되었거나 언어 README가 누락됨 | 상단 언어 선택 줄과 `i18n/` 하위 파일이 서로 동기화되어 있는지 확인하세요. |
| 폴더 이름 변경 후 GitHub 마크다운 링크 불일치 | 루트 언어 링크와 `i18n/README.*.md` 참조를 한 번에 다시 점검하세요. |

## 로드맵
- 실제 챕터 콘텐츠와 소스 파일로 보조 트랙을 계속 확장.
- 강의별 README 파일의 일관성 개선.
- `i18n/`의 다국어 README를 확장/유지하고 언어 선택기를 동기화.
- TeX 소스가 있는 각 하위 프로젝트를 위한 저장소 수준 빌드 가이드 섹션 추가.
- 로컬 도구 체인 차이가 있는 트랙에 트랙별 컴파일 스니펫 추가.
- README/i18n 링크 무결성을 검증하는 최소 자동화 추가.

## 기여
이 프로젝트는 포크한 뒤 pull request를 보내는 방식으로 기여할 수 있습니다.

권장 기여 범위:
- 챕터 노트와 참고자료 추가 또는 개선.
- TeX 소스 품질과 재현 가능한 빌드 지침 개선.
- 루트 및 트랙별 README의 진행 상태 문구를 동기화.
- `i18n/` 아래 다국어 README 간 동등성 유지.

권장 pull request 위생:
- 변경한 트랙 폴더를 정확히 명시.
- 소스 파일을 수정했다면 사용한 TeX 컴파일 명령을 포함.
- 챕터 상태가 바뀌면 관련 진행 표를 업데이트.
- 기준 영어 README 변경 후 `i18n/` README도 업데이트.

## ❤️ Support

| Donate | PayPal | Stripe |
|---|---|---|
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=ko-fi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 감사의 말
- 원본 강의 콘텐츠를 제공해 주신 Leonard Susskind 교수님.
- 기존 참고 노트 출처: https://www.lapasserelle.com/general_relativity/
- 기존 참고 노트 출처: https://www.lapasserelle.com/cosmology/
- 기존 참고 노트 출처: https://www.lapasserelle.com/statistical_mechanics/

## 라이선스
이 저장소는 GNU General Public License v3.0에 따라 라이선스가 부여됩니다. [LICENSE](../LICENSE)를 참조하세요.
