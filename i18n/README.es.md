[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# Repositorio de notas de clase de Leonard Susskind

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

> 🎓 Un archivo multilingüe de materiales de notas de clase de Leonard Susskind, que conserva tanto PDFs pulidos como fuentes LaTeX editables para estudio, reutilización y consulta.

## Descripción general
Este repositorio es un archivo centrado en contenido de notas de clase del entorno docente del profesor Leonard Susskind.

> Las notas de clase del profesor Leonard Susskind. Si esto viola algún derecho de autor, por favor contáctame para eliminar este repositorio. El profesor Susskind no se hace responsable de errores o desinformación en las notas, y yo tampoco.

Combina tres capas en un solo lugar:

- Pistas de notas y progreso por curso seleccionadas.
- Recursos publicados (`.pdf`) para leer y compartir.
- Archivos fuente (`.tex`, `.bib`, plantillas) para quienes mantengan o amplíen el archivo.

### Objetivos principales
- Mantener las notas de curso y el progreso en un mismo sitio.
- Conservar la visibilidad del avance de borradores/notas entre rutas principales y complementarias.
- Proporcionar materiales fuente (PDF, TeX, BibTeX, plantillas) para la autoría continua.

## Características
- Seguimiento y referencias de cursos principales.
- Seguimiento de progreso de cursos complementarios.
- PDFs de lecciones existentes para varias rutas principales.
- Fuentes de LaTeX en rutas seleccionadas.
- Plantillas reutilizables de LaTeX en `template/tuftle` y `template/kaobook`.
- Recursos visuales del repositorio en `figs/`.
- Conjunto de README multilingües en `i18n/`.

## Resumen rápido
| Área | Qué está disponible |
|---|---|
| 📝 Notas | Múltiples conjuntos de notas de curso con seguimiento de progreso |
| 🧾 Fuente | Fuentes TeX/BibTeX en subproyectos seleccionados |
| 🧱 Plantillas | `template/tuftle` y `template/kaobook` |
| 🎨 Identidad visual | `figs/banner.*`, `figs/logo.*`, `figs/logo-w-text.*` |
| 🌍 i18n | Variantes de idioma `i18n/README.*.md` |

## Índice
- [Descripción general](#descripción-general)
- [Características](#características)
- [Resumen rápido](#resumen-rápido)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Requisitos previos](#requisitos-previos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Configuración](#configuración)
- [Ejemplos](#ejemplos)
- [Notas de desarrollo](#notas-de-desarrollo)
- [Progreso canónico del curso (conservado y reorganizado)](#progreso-canónico-del-curso-conservado-y-reorganizado)
- [Solución de problemas](#solución-de-problemas)
- [Hoja de ruta](#hoja-de-ruta)
- [Contribución](#contribución)
- [❤️ Support](#-support)
- [Agradecimientos](#agradecimientos)
- [Licencia](#licencia)

## Estructura del proyecto
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

## Requisitos previos
Para leer:
- Un lector PDF (del sistema o aplicación).

Para editar/compilar materiales TeX:
- Una distribución LaTeX (TeX Live / MiKTeX).
- `pdflatex`.
- `bibtex` o `biber` según el subproyecto.
- `makeindex` para proyectos que usan entradas indexadas.

Notas de supuesto:
- No hay un sistema de construcción único a nivel raíz (`Makefile`, `package.json`, `pyproject.toml`) visible en este repositorio.
- Los flujos de trabajo se esperan ejecutar desde cada directorio de subproyecto.

## Instalación
```bash
# Clona el repositorio
git clone https://github.com/lachlanchen/leonardsusskind.git
cd leonardsusskind
```

Este repositorio es de contenido primero. Si se clona en espejo o se bifurca, reemplaza la URL remota por tu propia copia según corresponda.

No se requiere instalar paquetes globales para leer las notas existentes.

## Uso
### 1) Leer notas existentes
Abre los PDFs en las carpetas relevantes, por ejemplo:
- `core_general_relativity/lesson_1.pdf`
- `core_cosmology/lesson_1.pdf`
- `core_statistical_mechanics/lesson_1.pdf`
- `supplemental_particle_physics_2/NumberTheory.pdf`

### 2) Crear o ampliar materiales LaTeX
- Edita archivos `.tex` y `.bib` en la carpeta de curso/plantilla objetivo.
- Compila con el flujo de trabajo especificado por esa carpeta.
- Compila en el lugar para que los recursos locales y rutas relativas se resuelvan correctamente.

### 3) Navegar por puntos de entrada por ruta
Cada ruta principal tiene su propio `README.md` con notas de alcance limitado, referencias y progreso.

## Configuración
No existe un archivo de configuración global.

La configuración es local para cada proyecto TeX. Los parámetros típicos se incrustan en fuentes de documentos, incluidos:
- Clase de documento y configuración de paquetes en `template/kaobook/main.tex`
- Estructura/estilo reutilizable en `template/kaobook/`
- Backend de bibliografía y estilo de cita en pares locales `main.tex`/`ref.bib`
- Rutas de inclusión para imágenes y activos de capítulo en cada proyecto

Puntos de configuración locales representativos:
- `template/kaobook/main.tex`
- `template/tuftle/main.tex`
- `core_cosmology/cosmology_ch10/cosmology_ch10.tex`
- `supplemental_particle_physics_1/ch1/main.tex`
- `supplemental_advanced_quantum/ch1/main.tex`

## Ejemplos
### Ejemplo A: Construir `template/kaobook`
`template/kaobook/main.tex` describe esta cadena de compilación:

```bash
cd template/kaobook
pdflatex main
makeindex main.idx -s StyleInd.ist
biber main
pdflatex main
pdflatex main
```

### Ejemplo B: Construir `core_cosmology/cosmology_ch10`
`cosmology_ch10.tex` usa un flujo estilo BibTeX:

```bash
cd core_cosmology/cosmology_ch10
pdflatex cosmology_ch10.tex
bibtex cosmology_ch10
pdflatex cosmology_ch10.tex
pdflatex cosmology_ch10.tex
```

### Ejemplo C: Construir `supplemental_particle_physics_1/ch1`
```bash
cd supplemental_particle_physics_1/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### Ejemplo D: Construir `supplemental_advanced_quantum/ch1`
```bash
cd supplemental_advanced_quantum/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### Ejemplo E: Ver salida localmente
```bash
xdg-open supplemental_particle_physics_1/ch1/main.pdf
```

## Notas de desarrollo
- Este repositorio es principalmente de documentación/notas, no una base de código de aplicación.
- Algunas carpetas incluyen artefactos TeX generados (`.aux`, `.log`, `.toc`, `.bbl`, etc.) versionados en el repositorio.
- Los comandos de compilación pueden variar por subdirectorio; sigue las convenciones locales de `.tex`.
- Existen archivos `README.md` por ruta en directorios principales y complementarios y deben mantenerse alineados con las afirmaciones de progreso de nivel raíz.
- `i18n/` existe y se usa para variantes multilingües del README.
- El README raíz se trata como canónico; los archivos localizados deben seguirlo en actualizaciones.

## Progreso canónico del curso (conservado y reorganizado)

### Cursos principales

#### Mecánica clásica
El libro de texto de este curso [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681) ya fue publicado. Puedes comprarlo en Amazon [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681).

#### Mecánica cuántica
El libro de texto de este curso [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903) ya fue publicado. Puedes comprarlo en Amazon [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903).

#### Relatividad Especial y Electrodinámica
El libro de texto de este curso [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065) ya fue publicado. Puedes comprarlo en Amazon [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065).

#### Tabla de progreso principal
| Curso | Progreso de borradores | Progreso de notas | Notas/Referencia |
|---|---:|---:|---|
| General Relativity | 10/10 | 10/10 | The lecture notes had been taken by https://www.lapasserelle.com/general_relativity/ . |
| Cosmology | 10/10 | 9/10 | The lecture notes, from chapter 1 to 9, had been taken by https://www.lapasserelle.com/cosmology/ . The chapter 10 is in the process. |
| Statistical Mechanics | 11/11 | 10/10 | The lecture notes had been taken by https://www.lapasserelle.com/statistical_mechanics/. |

### Cursos complementarios
| Curso | Progreso de borradores | Progreso de notas |
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

### Nota de integridad del progreso
- Las tablas de progreso anteriores se conservaron del texto canónico del README.
- Los archivos del repositorio incluyen rutas maduras y de marcador; si una entrada de tabla y el estado real de la carpeta parecen inconsistentes, trata la tabla como la intención documentada y actualiza ambos a futuro en una revisión conjunta.

## Solución de problemas
| Problema | Resolución |
|---|---|
| `pdflatex: command not found` | Instala una distribución LaTeX y asegúrate de que los binarios estén en `PATH`. |
| Falta de bibliografía/índice | Ejecuta el backend requerido (`bibtex` o `biber`) y `makeindex` si se usa, luego vuelve a correr `pdflatex`. |
| Errores de archivos de estilo/clase faltantes | Compila desde el directorio del proyecto previsto para que las rutas relativas a recursos locales se resuelvan correctamente. |
| El resultado de compilación difiere entre entornos | Este repositorio contiene materiales generados en entornos distintos; alinea las versiones de paquetes cuando sea posible. |
| Enlaces multilingües obsoletos o README de idioma faltante | Asegura que la línea superior de opciones de idioma y los archivos en `i18n/` permanezcan sincronizados. |
| Desajuste de enlace Markdown de GitHub tras renombrar una carpeta | Vuelve a validar los enlaces de idioma del README raíz y todas las referencias `i18n/README.*.md` en una sola pasada. |

## Hoja de ruta
- Continuar con rutas complementarias con contenido real de capítulos y archivos fuente.
- Mejorar la consistencia de los README por curso.
- Ampliar y mantener README multilingües en `i18n/` y mantener sincronizado el selector de idioma.
- Añadir una sección de guía de compilación a nivel de repositorio para cada subproyecto con fuentes TeX.
- Añadir fragmentos de compilación por ruta cuando existan diferencias locales de cadena de herramientas.
- Añadir automatización mínima para validar la integridad de enlaces README/i18n.

## Contribución
Puedes contribuir a este proyecto biforcándolo y enviando una pull request.

Alcance sugerido de la contribución:
- Añadir o mejorar notas de capítulo y referencias.
- Mejorar la calidad de fuentes TeX e instrucciones reproducibles de compilación.
- Mantener sincronizadas las declaraciones de progreso entre README raíz y README por ruta.
- Mantener la paridad de README multilingües en `i18n/`.

Buenas prácticas recomendadas para pull requests:
- Menciona la(s) carpeta(s) de ruta exacta(s) modificada(s).
- Incluye los comandos de compilación TeX usados (si se editaron archivos fuente).
- Actualiza las tablas de progreso relevantes cuando el estado de capítulos cambie.
- Actualiza los readmes de `i18n/` después de cambios en el README canónico en inglés.

## Agradecimientos
- El profesor Leonard Susskind por el contenido original de las clases.
- Fuente de notas de referencia existente: https://www.lapasserelle.com/general_relativity/
- Fuente de notas de referencia existente: https://www.lapasserelle.com/cosmology/
- Fuente de notas de referencia existente: https://www.lapasserelle.com/statistical_mechanics/

## Licencia
Este repositorio está licenciado bajo la GNU General Public License v3.0. Ver [LICENSE](LICENSE).


## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |
