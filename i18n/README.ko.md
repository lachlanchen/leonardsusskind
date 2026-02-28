[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


<p align="center">
  <img src="https://raw.githubusercontent.com/lachlanchen/lachlanchen/main/logos/banner.png" alt="LazyingArt banner" />
</p>

# Leonard Susskind 강의 노트 저장소


![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg)
![Content Type](https://img.shields.io/badge/content-Lecture%20Notes%20%26%20LaTeX-informational)
![Status](https://img.shields.io/badge/status-Active%20Archive-success)
![LaTeX](https://img.shields.io/badge/tooling-LaTeX-008080)
![i18n](https://img.shields.io/badge/i18n-directory%20ready-orange)

## 📖 개요
이 저장소는 Leonard Susskind 교수의 강의와 관련된 강의 노트 자료를 콘텐츠 중심으로 아카이브한 공간입니다.

Susskind 교수의 강의 노트를 정리한 저장소입니다. 저작권을 침해하는 내용이 있다면 저장소 삭제를 위해 연락해 주세요. 노트의 오류나 잘못된 정보에 대해 Susskind 교수는 책임지지 않으며, 저 또한 책임지지 않습니다.

### 주요 목표
- 강의 노트와 진행 상황을 한곳에서 관리합니다.
- 핵심/보충 트랙 전반에서 초안 및 노트 진행 상황의 가시성을 유지합니다.
- 지속적인 작성 작업을 위해 소스 자료(PDF, TeX, BibTeX, 템플릿)를 제공합니다.

## ✨ 특징
- 핵심 강의 트래킹 및 참고자료 정리.
- 보충 강의 진행 상황 트래킹.
- 여러 핵심 트랙의 기존 강의 PDF 제공.
- 일부 트랙의 LaTeX 소스 자료 제공.
- `template/tuftle`, `template/kaobook`의 재사용 가능한 LaTeX 템플릿.
- `figs/`의 저장소 비주얼 자료.

## 📌 빠른 요약
| 영역 | 제공 내용 |
|---|---|
| 📚 노트 | 진행 상황 추적이 포함된 여러 강의 노트 세트 |
| 🧪 소스 | 일부 하위 프로젝트의 TeX/BibTeX 소스 |
| 🧰 템플릿 | `template/tuftle` 및 `template/kaobook` |
| 🌐 i18n | `i18n/` 디렉터리 존재 (현재 비어 있음) |

## 🗂️ 프로젝트 구조
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

## 🧩 사전 요구사항
읽기 전용 사용 시:
- PDF 리더.

TeX 자료 편집/빌드 시:
- LaTeX 배포판(TeX Live / MiKTeX).
- `pdflatex`.
- 하위 프로젝트에 따라 `bibtex` 또는 `biber`.
- 인덱스를 사용하는 템플릿용 `makeindex`.

가정 참고:
- 이 저장소에는 루트 레벨 단일 빌드 시스템(`Makefile`, `package.json`, `pyproject.toml`)이 없습니다.

## 🚀 설치
```bash
git clone https://github.com/<your-user>/leonardsusskind.git
cd leonardsusskind
```

기본 사용(기존 노트 열람)에는 별도의 패키지 설치가 필요하지 않습니다.

## 🛠️ 사용법
### 1) 기존 노트 읽기
- 관련 폴더의 PDF를 엽니다. 예:
  - `core_general_relativity/lesson_1.pdf`
  - `core_cosmology/lesson_1.pdf`
  - `core_statistical_mechanics/lesson_1.pdf`

### 2) LaTeX 자료 작업
- 대상 강의/템플릿 폴더에서 `.tex`, `.bib` 파일을 편집합니다.
- 해당 폴더에서 요구하는 툴체인으로 컴파일합니다.

## ⚙️ 설정
전역 설정 파일은 없습니다.

설정은 각 TeX 프로젝트 내부(문서 클래스, 참고문헌 백엔드, 스타일 파일, 그래픽 경로)에서 관리됩니다. 예:
- `template/kaobook/main.tex`
- `template/tuftle/main.tex`
- `core_cosmology/cosmology_ch10/cosmology_ch10.tex`

## 🧪 예시
### 예시 A: `template/kaobook` 빌드
`template/kaobook/main.tex`에는 다음 컴파일 체인이 안내되어 있습니다:

```bash
cd template/kaobook
pdflatex main
makeindex main.idx -s StyleInd.ist
biber main
pdflatex main
pdflatex main
```

### 예시 B: `core_cosmology/cosmology_ch10` 빌드
`cosmology_ch10.tex`는 `\bibliography{ref}`를 사용합니다(BibTeX 스타일 워크플로우):

```bash
cd core_cosmology/cosmology_ch10
pdflatex cosmology_ch10.tex
bibtex cosmology_ch10
pdflatex cosmology_ch10.tex
pdflatex cosmology_ch10.tex
```

### 예시 C: 생성된 챕터 PDF 보기
```bash
xdg-open supplemental_particle_physics_1/ch1/main.pdf
```

## 📝 개발 노트
- 이 저장소는 애플리케이션 코드베이스가 아니라 문서/노트 중심 저장소입니다.
- 일부 폴더에는 생성된 TeX 산출물(`.aux`, `.log`, `.toc`, `.bbl` 등)이 저장소에 커밋되어 있습니다.
- 빌드 명령은 하위 디렉터리별로 다를 수 있으므로, 각 위치의 `.tex` 관례를 따르세요.
- `i18n/`은 다국어 README 변형을 위해 예약되어 있습니다.

## 📚 정식 강의 진행 현황 (보존 및 재구성)

### 핵심 강의

#### 고전역학
이 강의의 교재 [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681)는 이미 출판되었습니다. Amazon에서 [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681)를 구매할 수 있습니다.

#### 양자역학
이 강의의 교재 [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903)는 이미 출판되었습니다. Amazon에서 [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903)를 구매할 수 있습니다.

#### 특수상대론과 전자기학
이 강의의 교재 [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065)는 이미 출판되었습니다. Amazon에서 [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065)를 구매할 수 있습니다.

#### 핵심 진행 표
| 강의 | 초안 진행률 | 노트 진행률 | 노트/참고 |
|---|---:|---:|---|
| General Relativity | 10/10 | 10/10 | 강의 노트는 https://www.lapasserelle.com/general_relativity/ 에서 정리되었습니다. |
| Cosmology | 10/10 | 9/10 | 1장부터 9장까지의 강의 노트는 https://www.lapasserelle.com/cosmology/ 에서 정리되었습니다. 10장은 진행 중입니다. |
| Statistical Mechanics | 11/11 | 10/10 | 강의 노트는 https://www.lapasserelle.com/statistical_mechanics/. 에서 정리되었습니다. |

### 보충 강의
| 강의 | 초안 진행률 | 노트 진행률 |
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

## 🧯 문제 해결
- `pdflatex: command not found`
  - LaTeX 배포판을 설치하고 바이너리가 `PATH`에 포함되어 있는지 확인하세요.
- 참고문헌/인덱스가 나타나지 않음
  - 필요한 백엔드(`bibtex` 또는 `biber`)와 `makeindex`(사용 시)를 실행한 뒤 `pdflatex`를 다시 실행하세요.
- 스타일/클래스 파일 누락 오류
  - 로컬 에셋에 대한 상대 경로가 올바르게 해석되도록 의도된 프로젝트 디렉터리에서 빌드하세요.
- 환경마다 빌드 결과가 다름
  - 이 저장소의 자료는 서로 다른 환경에서 생성되었으므로, 가능한 범위에서 패키지 버전을 맞추세요.

## 🗺️ 로드맵
- 보충 트랙에 실제 챕터 콘텐츠와 소스 파일을 계속 추가.
- 강의별 README의 일관성 개선.
- `i18n/` 아래 다국어 README를 추가하고 언어 선택 줄을 동기화 유지.
- TeX 소스가 있는 하위 프로젝트별 저장소 수준 빌드 가이드 섹션 추가.

## ❤️ 기여 또는 후원
이 프로젝트는 포크 후 Pull Request를 보내 기여할 수 있습니다. 이 프로젝트가 개발 시간을 줄이는 데 도움이 되었다면 커피 한 잔 후원도 환영합니다 :)

## 🙏 감사의 말
- 원 강의 콘텐츠를 제공한 Leonard Susskind 교수님.
- 기존 참고 노트 출처:
  - https://www.lapasserelle.com/general_relativity/
  - https://www.lapasserelle.com/cosmology/
  - https://www.lapasserelle.com/statistical_mechanics/

## 📄 라이선스
이 저장소는 GNU General Public License v3.0으로 배포됩니다. [LICENSE](../LICENSE)를 참고하세요.
