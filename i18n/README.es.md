[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# Repositorio de apuntes de clases de Leonard Susskind

![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg)
![Content Type](https://img.shields.io/badge/content-Lecture%20Notes%20%26%20LaTeX-informational)
![Status](https://img.shields.io/badge/status-Active%20Archive-success)
![LaTeX](https://img.shields.io/badge/tooling-LaTeX-008080)
![Core Tracks](https://img.shields.io/badge/core_tracks-6-1f6feb)
![Supplemental Tracks](https://img.shields.io/badge/supplemental_tracks-9-9a6700)
![i18n](https://img.shields.io/badge/i18n-10%20translations%20%2B%20English-orange)

## Resumen
Este repositorio es un archivo centrado en contenido con materiales de apuntes de clase relacionados con los cursos del profesor Leonard Susskind.

> Apuntes de clase del profesor Leonard Susskind. Si esto infringe algún derecho de autor, por favor contácteme para eliminar este repositorio. El profesor Susskind no se hace responsable de errores o información incorrecta en los apuntes, ni yo tampoco.

### Objetivos principales
- Mantener en un solo lugar los apuntes de los cursos y su progreso.
- Preservar la visibilidad del avance de borradores/apuntes en rutas principales y complementarias.
- Proporcionar materiales fuente (PDF, TeX, BibTeX, plantillas) para continuar la autoría.

## Características
- Seguimiento y referencias de cursos principales.
- Seguimiento del progreso de cursos complementarios.
- PDFs de lecciones existentes para varias rutas principales.
- Material fuente en LaTeX en rutas seleccionadas.
- Plantillas LaTeX reutilizables en `template/tuftle` y `template/kaobook`.
- Recursos visuales del repositorio en `figs/`.
- Conjunto README multilingüe en `i18n/`.

## Vista rápida
| Área | Qué está disponible |
|---|---|
| 📝 Apuntes | Varios conjuntos de apuntes de cursos con seguimiento de progreso |
| 🧾 Fuentes | Fuentes TeX/BibTeX en subproyectos seleccionados |
| 🧱 Plantillas | `template/tuftle` y `template/kaobook` |
| 🎨 Marca | `figs/banner.*`, `figs/logo.*`, `figs/logo-w-text.*` |
| 🌍 i18n | Variantes de idioma `i18n/README.*.md` |

## Tabla de contenido
- [Resumen](#resumen)
- [Características](#características)
- [Vista rápida](#vista-rápida)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Requisitos previos](#requisitos-previos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Configuración](#configuración)
- [Ejemplos](#ejemplos)
- [Notas de desarrollo](#notas-de-desarrollo)
- [Progreso canónico de cursos (preservado y reorganizado)](#progreso-canónico-de-cursos-preservado-y-reorganizado)
- [Resolución de problemas](#resolución-de-problemas)
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
Solo para lectura:
- Un lector de PDF.

Para editar/compilar materiales TeX:
- Una distribución LaTeX (TeX Live / MiKTeX).
- `pdflatex`.
- `bibtex` o `biber` según el subproyecto.
- `makeindex` para plantillas que usan índices.

Nota de supuesto:
- En este repositorio no hay un sistema de compilación único en la raíz (`Makefile`, `package.json`, `pyproject.toml`).

## Instalación
```bash
git clone https://github.com/<your-user>/leonardsusskind.git
cd leonardsusskind
```

Si este repositorio está bifurcado o espejado, reemplaza `<your-user>` por la cuenta correcta.

No se requiere ningún paso de instalación de paquetes para uso básico (leer apuntes existentes).

## Uso
### 1) Leer apuntes existentes
Abre los PDF en las carpetas relevantes, por ejemplo:
- `core_general_relativity/lesson_1.pdf`
- `core_cosmology/lesson_1.pdf`
- `core_statistical_mechanics/lesson_1.pdf`
- `supplemental_particle_physics_2/NumberTheory.pdf`

### 2) Trabajar en materiales LaTeX
- Edita los archivos `.tex` y `.bib` en la carpeta de curso/plantilla de destino.
- Compila con la cadena de herramientas esperada por esa carpeta.
- Se recomienda ejecutar los comandos de compilación desde el directorio local del proyecto para que las rutas relativas se resuelvan correctamente.

### 3) Navegar por los archivos README de cada ruta
Cada ruta principal tiene su propio `README.md` local para apuntes acotados y contexto de progreso.

## Configuración
No hay un archivo de configuración global.

La configuración es local para cada proyecto TeX (clase de documento, backend bibliográfico, archivos de estilo, rutas de gráficos), por ejemplo:
- `template/kaobook/main.tex`
- `template/tuftle/main.tex`
- `core_cosmology/cosmology_ch10/cosmology_ch10.tex`
- `supplemental_particle_physics_1/ch1/main.tex`
- `supplemental_advanced_quantum/ch1/main.tex`

## Ejemplos
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

### Ejemplo C: Compilar un capítulo basado en Tufte (`supplemental_particle_physics_1/ch1`)
```bash
cd supplemental_particle_physics_1/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### Ejemplo D: Compilar un capítulo basado en Tufte (`supplemental_advanced_quantum/ch1`)
```bash
cd supplemental_advanced_quantum/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### Ejemplo E: Ver un PDF de capítulo generado
```bash
xdg-open supplemental_particle_physics_1/ch1/main.pdf
```

## Notas de desarrollo
- Este repositorio es principalmente de documentación/apuntes, no una base de código de aplicación.
- Algunas carpetas incluyen artefactos TeX generados (`.aux`, `.log`, `.toc`, `.bbl`, etc.) versionados dentro del repositorio.
- Los comandos de compilación pueden variar por subdirectorio; sigue las convenciones locales de cada `.tex`.
- Existen archivos `README.md` por ruta en los directorios core/supplemental y deben mantenerse alineados con las afirmaciones de progreso del README raíz.
- `i18n/` existe y se usa para variantes multilingües del README.
- El README de la raíz se considera canónico; los archivos multilingües deben seguirlo cuando se actualice.

## Progreso canónico de cursos (preservado y reorganizado)

### Cursos principales

#### Mecánica clásica
El libro de texto de este curso [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681) ya fue publicado. Puedes comprarlo en Amazon [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681).

#### Mecánica cuántica
El libro de texto de este curso [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903) ya fue publicado. Puedes comprarlo en Amazon [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903).

#### Relatividad especial y electrodinámica
El libro de texto de este curso [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065) ya fue publicado. Puedes comprarlo en Amazon [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065).

#### Tabla de progreso de cursos principales
| Course | Draft Progress | Notes Progress | Notes/Reference |
|---|---:|---:|---|
| General Relativity | 10/10 | 10/10 | The lecture notes had been taken by https://www.lapasserelle.com/general_relativity/ . |
| Cosmology | 10/10 | 9/10 | The lecture notes, from chapter 1 to 9, had been taken by https://www.lapasserelle.com/cosmology/ . The chapter 10 is in the process. |
| Statistical Mechanics | 11/11 | 10/10 | The lecture notes had been taken by https://www.lapasserelle.com/statistical_mechanics/. |

### Cursos complementarios
| Course | Draft Progress | Notes Progress |
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

### Nota sobre integridad del progreso
- Las tablas de progreso anteriores se conservan desde el texto canónico del README.
- Los archivos del repositorio incluyen tanto rutas maduras como rutas de marcador de posición; si una entrada de tabla y el estado de una carpeta parecen inconsistentes, trata la tabla como la intención documentada y actualiza ambos en conjunto en futuras revisiones.

## Resolución de problemas
| Problema | Resolución |
|---|---|
| `pdflatex: command not found` | Instala una distribución LaTeX y asegúrate de que los binarios estén en `PATH`. |
| La bibliografía/índice no aparece | Ejecuta el backend requerido (`bibtex` o `biber`) y `makeindex` si se usa, luego vuelve a ejecutar `pdflatex`. |
| Errores de archivo de estilo/clase faltante | Compila desde el directorio de proyecto previsto para que las rutas relativas a recursos locales se resuelvan correctamente. |
| La salida de compilación difiere entre entornos | Este repositorio contiene materiales producidos en entornos distintos; alinea versiones de paquetes cuando sea posible. |
| Enlaces multilingües desactualizados o README de idioma faltante | Asegúrate de que la línea superior de opciones de idioma y los archivos bajo `i18n/` se mantengan sincronizados. |
| Incompatibilidad de enlaces markdown en GitHub tras renombrar carpetas | Vuelve a validar de una pasada los enlaces de idioma en raíz y todas las referencias `i18n/README.*.md`. |

## Hoja de ruta
- Continuar las rutas complementarias con contenido real de capítulos y archivos fuente.
- Mejorar la consistencia de los archivos README por curso.
- Ampliar y mantener los README multilingües en `i18n/` y mantener sincronizado el selector de idioma.
- Añadir una sección de guía de compilación a nivel de repositorio para cada subproyecto que tenga fuentes TeX.
- Añadir fragmentos de compilación por ruta donde existan diferencias de toolchain local.
- Añadir automatización mínima para validar la integridad de enlaces README/i18n.

## Contribución
Puedes contribuir a este proyecto bifurcándolo y enviando un pull request.

Alcance sugerido para contribuciones:
- Añadir o mejorar apuntes de capítulos y referencias.
- Mejorar la calidad de fuentes TeX e instrucciones de compilación reproducibles.
- Mantener sincronizadas las afirmaciones de progreso del README raíz y los README por ruta.
- Mantener la paridad multilingüe de README en `i18n/`.

Higiene recomendada para pull requests:
- Menciona la(s) carpeta(s) de ruta exacta(s) modificada(s).
- Incluye los comandos de compilación TeX usados (si se editaron archivos fuente).
- Actualiza las tablas de progreso relevantes cuando cambie el estado de capítulos.
- Actualiza los readmes de `i18n/` tras cambios en el README canónico en inglés.

## ❤️ Support

| Donate | PayPal | Stripe |
|---|---|---|
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=ko-fi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## Agradecimientos
- Profesor Leonard Susskind por el contenido original de las clases.
- Fuente de apuntes de referencia existente: https://www.lapasserelle.com/general_relativity/
- Fuente de apuntes de referencia existente: https://www.lapasserelle.com/cosmology/
- Fuente de apuntes de referencia existente: https://www.lapasserelle.com/statistical_mechanics/

## Licencia
Este repositorio está licenciado bajo GNU General Public License v3.0. Consulta [LICENSE](LICENSE).
