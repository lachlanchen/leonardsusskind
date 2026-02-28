[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


<p align="center">
  <img src="https://raw.githubusercontent.com/lachlanchen/lachlanchen/main/logos/banner.png" alt="LazyingArt banner" />
</p>

# Repositorio de apuntes de clases de Leonard Susskind


![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg)
![Content Type](https://img.shields.io/badge/content-Lecture%20Notes%20%26%20LaTeX-informational)
![Status](https://img.shields.io/badge/status-Active%20Archive-success)
![LaTeX](https://img.shields.io/badge/tooling-LaTeX-008080)
![i18n](https://img.shields.io/badge/i18n-directory%20ready-orange)

## 📖 Resumen
Este repositorio es un archivo centrado en contenido con materiales de apuntes de clases relacionados con cursos del profesor Leonard Susskind.

Los apuntes de clases del profesor Leonard Susskind. Si esto viola algún copyright, por favor contáctame para eliminar este repositorio. El profesor Susskind no asume responsabilidad por errores o información incorrecta en los apuntes, y yo tampoco.

### Objetivos principales
- Mantener en un solo lugar los apuntes de cursos y el progreso.
- Preservar la visibilidad del progreso de borradores/apuntes en las rutas principales y suplementarias.
- Proporcionar materiales fuente (PDF, TeX, BibTeX, plantillas) para continuar la redacción.

## ✨ Características
- Seguimiento y referencias de cursos principales.
- Seguimiento del progreso de cursos suplementarios.
- PDFs de lecciones existentes en varias rutas principales.
- Material fuente en LaTeX en rutas seleccionadas.
- Plantillas LaTeX reutilizables en `template/tuftle` y `template/kaobook`.
- Recursos visuales del repositorio en `figs/`.

## 📌 Vista rápida
| Área | Qué está disponible |
|---|---|
| 📚 Apuntes | Múltiples conjuntos de apuntes de cursos, con seguimiento de progreso |
| 🧪 Fuentes | Fuentes TeX/BibTeX en subproyectos seleccionados |
| 🧰 Plantillas | `template/tuftle` y `template/kaobook` |
| 🌐 i18n | El directorio `i18n/` existe (actualmente vacío) |

## 🗂️ Estructura del proyecto
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

## 🧩 Requisitos previos
Para solo lectura:
- Un lector de PDF.

Para editar/compilar materiales TeX:
- Una distribución de LaTeX (TeX Live / MiKTeX).
- `pdflatex`.
- `bibtex` o `biber` según el subproyecto.
- `makeindex` para plantillas que usan índices.

Nota de supuesto:
- No hay un único sistema de compilación a nivel raíz (`Makefile`, `package.json`, `pyproject.toml`) en este repositorio.

## 🚀 Instalación
```bash
git clone https://github.com/<your-user>/leonardsusskind.git
cd leonardsusskind
```

No se requiere un paso de instalación de paquetes para el uso básico (leer los apuntes existentes).

## 🛠️ Uso
### 1) Leer apuntes existentes
- Abre PDFs en las carpetas relevantes, por ejemplo:
  - `core_general_relativity/lesson_1.pdf`
  - `core_cosmology/lesson_1.pdf`
  - `core_statistical_mechanics/lesson_1.pdf`

### 2) Trabajar en materiales LaTeX
- Edita archivos `.tex` y `.bib` en la carpeta de curso/plantilla objetivo.
- Compila con la cadena de herramientas esperada por esa carpeta.

## ⚙️ Configuración
No hay un archivo de configuración global.

La configuración es local a cada proyecto TeX (clase de documento, backend de bibliografía, archivos de estilo, rutas de gráficos), por ejemplo:
- `template/kaobook/main.tex`
- `template/tuftle/main.tex`
- `core_cosmology/cosmology_ch10/cosmology_ch10.tex`

## 🧪 Ejemplos
### Ejemplo A: Compilar `template/kaobook`
`template/kaobook/main.tex` documenta esta cadena de compilación:

```bash
cd template/kaobook
pdflatex main
makeindex main.idx -s StyleInd.ist
biber main
pdflatex main
pdflatex main
```

### Ejemplo B: Compilar `core_cosmology/cosmology_ch10`
`cosmology_ch10.tex` usa `\bibliography{ref}` (flujo de trabajo estilo BibTeX):

```bash
cd core_cosmology/cosmology_ch10
pdflatex cosmology_ch10.tex
bibtex cosmology_ch10
pdflatex cosmology_ch10.tex
pdflatex cosmology_ch10.tex
```

### Ejemplo C: Ver un PDF de capítulo generado
```bash
xdg-open supplemental_particle_physics_1/ch1/main.pdf
```

## 📝 Notas de desarrollo
- Este es principalmente un repositorio de documentación/apuntes, no una base de código de aplicación.
- Algunas carpetas incluyen artefactos TeX generados (`.aux`, `.log`, `.toc`, `.bbl`, etc.) versionados en el repositorio.
- Los comandos de compilación pueden variar por subdirectorio; sigue las convenciones locales de cada `.tex`.
- `i18n/` existe y está reservado para variantes multilingües del README.

## 📚 Progreso canónico de cursos (preservado y reorganizado)

### Cursos principales

#### Mecánica clásica
El libro de texto de este curso [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681) ya fue publicado. Puedes comprarlo en Amazon [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681).

#### Mecánica cuántica
El libro de texto de este curso [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903) ya fue publicado. Puedes comprarlo en Amazon [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903).

#### Relatividad especial y electrodinámica
El libro de texto de este curso [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065) ya fue publicado. Puedes comprarlo en Amazon [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065).

#### Tabla de progreso de cursos principales
| Curso | Progreso de borrador | Progreso de apuntes | Apuntes/Referencia |
|---|---:|---:|---|
| General Relativity | 10/10 | 10/10 | The lecture notes had been taken by https://www.lapasserelle.com/general_relativity/ . |
| Cosmology | 10/10 | 9/10 | The lecture notes, from chapter 1 to 9, had been taken by https://www.lapasserelle.com/cosmology/ . The chapter 10 is in the process. |
| Statistical Mechanics | 11/11 | 10/10 | The lecture notes had been taken by https://www.lapasserelle.com/statistical_mechanics/. |

### Cursos suplementarios
| Curso | Progreso de borrador | Progreso de apuntes |
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

## 🧯 Solución de problemas
- `pdflatex: command not found`
  - Instala una distribución de LaTeX y asegúrate de que los binarios estén en `PATH`.
- La bibliografía/índice no aparece
  - Ejecuta el backend requerido (`bibtex` o `biber`) y `makeindex` si aplica, luego vuelve a ejecutar `pdflatex`.
- Errores por archivos de estilo/clase faltantes
  - Compila desde el directorio de proyecto previsto para que las rutas relativas a recursos locales se resuelvan correctamente.
- La salida de compilación difiere entre entornos
  - Este repositorio contiene materiales producidos en diferentes entornos; alinea versiones de paquetes cuando sea posible.

## 🗺️ Hoja de ruta
- Continuar las rutas suplementarias con contenido real de capítulos y archivos fuente.
- Mejorar la consistencia de los archivos README por curso.
- Añadir archivos README multilingües en `i18n/` y mantener sincronizado el selector de idioma.
- Añadir una sección de guía de compilación a nivel repositorio para cada subproyecto que tenga fuentes TeX.

## ❤️ Contribución o donación
Puedes contribuir a este proyecto bifurcándolo y enviando un pull request. Si este proyecto te ayuda a reducir tiempo de desarrollo, puedes invitarme un café :)

## 🙏 Agradecimientos
- Profesor Leonard Susskind por el contenido original de las clases.
- Fuentes de apuntes referenciadas existentes:
  - https://www.lapasserelle.com/general_relativity/
  - https://www.lapasserelle.com/cosmology/
  - https://www.lapasserelle.com/statistical_mechanics/

## 📄 Licencia
Este repositorio está licenciado bajo GNU General Public License v3.0. Consulta [LICENSE](../LICENSE).
