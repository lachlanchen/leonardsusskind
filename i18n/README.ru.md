[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)



[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# Репозиторий конспектов лекций Леонарда Сасскинда

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

> 🎓 Многоязычный архив материалов лекций Леонарда Сасскинда с отредактированными PDF и исходниками LaTeX для изучения, доработки и справок.

---

## Обзор
Этот репозиторий — архив материалов лекций профессора Леонарда Сасскинда с фокусом на содержимое.

> Конспекты лекций профессора Леонарда Сасскинда. Если это нарушает чьи-либо авторские права, пожалуйста, свяжитесь со мной для удаления репозитория. Ни профессор Сасскинд, ни я не несем ответственности за ошибки и возможные неточности в заметках.

В одном месте собраны три уровня материалов:

- Отобранные учебные треки и прогресс по курсам.
- Готовые артефакты (`.pdf`) для чтения и обмена.
- Исходные файлы (`.tex`, `.bib`, шаблоны) для поддержки и расширения архива.

### Основные цели
- Хранить материалы по курсам и прогресс в одном месте.
- Поддерживать видимость статуса черновиков и заметок для базовых и вспомогательных треков.
- Предоставлять исходные материалы (PDF, TeX, BibTeX, шаблоны) для дальнейшей работы с ними.

## Особенности
- 📚 Отслеживание курсов и справочных материалов базового трека.
- 📌 Отслеживание прогресса по дополнительным трекам.
- 📄 Готовые PDF-версии для нескольких базовых треков.
- 🧪 Исходники LaTeX в выбранных треках.
- 🧷 Повторно используемые шаблоны LaTeX в `template/tuftle` и `template/kaobook`.
- 🎨 Визуальные материалы репозитория в `figs/`.
- 🌐 Многоязычный набор README в `i18n/`.

## Краткий обзор
| Область | Что доступно |
|---|---|
| 📝 Конспекты | Несколько наборов учебных материалов с отслеживанием прогресса |
| 🧾 Исходники | Исходники TeX/BibTeX в выбранных подпроектах |
| 🧱 Шаблоны | `template/tuftle` и `template/kaobook` |
| 🎨 Брендинг | `figs/banner.*`, `figs/logo.*`, `figs/logo-w-text.*` |
| 🌍 i18n | Языковые варианты `i18n/README.*.md` |

## Содержание
- [Обзор](#обзор)
- [Особенности](#особенности)
- [Краткий обзор](#краткий-обзор)
- [Структура проекта](#структура-проекта)
- [Требования](#требования)
- [Установка](#установка)
- [Использование](#использование)
- [Конфигурация](#конфигурация)
- [Примеры](#примеры)
- [Заметки по разработке](#заметки-по-разработке)
- [Канонический прогресс курсов (сохранён и реорганизован)](#канонический-прогресс-курсов-сохранён-и-реорганизован)
- [Устранение неполадок](#устранение-неполадок)
- [Дорожная карта](#дорожная-карта)
- [Вклад](#вклад)
- [❤️ Support](#-support)
- [Благодарности](#благодарности)
- [Лицензия](#лицензия)

## Структура проекта
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

## Требования
Для чтения:
- 📖 PDF-читалка (системная или в приложении).

Для редактирования/сборки материалов LaTeX:
- 📦 Дистрибутив LaTeX (TeX Live / MiKTeX).
- ⚙️ `pdflatex`.
- 🗂️ `bibtex` или `biber` в зависимости от подпроекта.
- 🔎 `makeindex` для проектов с индексом.

---

Примечания по предположениям:
- На уровне корня нет единой системы сборки (`Makefile`, `package.json`, `pyproject.toml`).
- Ожидается запускать процесс сборки из каталога каждого подпроекта.

## Установка
```bash
# Clone the repository
git clone https://github.com/lachlanchen/leonardsusskind.git
cd leonardsusskind
```

Этот репозиторий ориентирован на содержимое. Если он является зеркальной копией или форком, замените удалённый URL на адрес вашей версии.

Для чтения существующих конспектов установка глобальных пакетов не требуется.

## Использование
### 1) Чтение существующих конспектов
Откройте PDF-файлы в нужных папках, например:
- `core_general_relativity/lesson_1.pdf`
- `core_cosmology/lesson_1.pdf`
- `core_statistical_mechanics/lesson_1.pdf`
- `supplemental_particle_physics_2/NumberTheory.pdf`

### 2) Написание и расширение материалов LaTeX
- Редактируйте `.tex` и `.bib` файлы в целевой папке курса/шаблона.
- Собирайте документ по рабочему процессу, описанному в этой папке.
- Запускайте сборку в месте нахождения проекта, чтобы локальные относительные зависимости разрешались корректно.

### 3) Навигация по трекам
У каждого большого трека есть свой `README.md` с локальными заметками, ссылками и прогрессом.

## Конфигурация
Глобального файла конфигурации нет.

Настройка хранится локально в каждом TeX-проекте. Типичные параметры обычно находятся в исходниках, включая:
- Класс документа и подключение пакетов в `template/kaobook/main.tex`
- Повторно используемую структуру и стили в `template/kaobook/`
- Backend библиографии и стиль ссылок в локальных парах `main.tex`/`ref.bib`
- Пути для включения изображений и материалов главы в каждом проекте

Типичные локальные точки настройки:
- `template/kaobook/main.tex`
- `template/tuftle/main.tex`
- `core_cosmology/cosmology_ch10/cosmology_ch10.tex`
- `supplemental_particle_physics_1/ch1/main.tex`
- `supplemental_advanced_quantum/ch1/main.tex`

## Примеры
### Пример A: Сборка `template/kaobook`
`template/kaobook/main.tex` описывает такой конвейер сборки:

```bash
cd template/kaobook
pdflatex main
makeindex main.idx -s StyleInd.ist
biber main
pdflatex main
pdflatex main
```

### Пример B: Сборка `core_cosmology/cosmology_ch10`
`cosmology_ch10.tex` использует рабочий процесс в стиле BibTeX:

```bash
cd core_cosmology/cosmology_ch10
pdflatex cosmology_ch10.tex
bibtex cosmology_ch10
pdflatex cosmology_ch10.tex
pdflatex cosmology_ch10.tex
```

### Пример C: Сборка `supplemental_particle_physics_1/ch1`
```bash
cd supplemental_particle_physics_1/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### Пример D: Сборка `supplemental_advanced_quantum/ch1`
```bash
cd supplemental_advanced_quantum/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### Пример E: Просмотр результата локально
```bash
xdg-open supplemental_particle_physics_1/ch1/main.pdf
```

## Заметки по разработке
- Это, прежде всего, репозиторий с документацией и заметками, а не прикладным кодом.
- Некоторые папки содержат сгенерированные артефакты TeX (`.aux`, `.log`, `.toc`, `.bbl` и т. д.), сохранённые в репозитории.
- Команды сборки могут отличаться по подпапкам; ориентируйтесь на локальные соглашения `.tex`.
- В корневом и дополнительных `README.md` по трекам есть сведения, которые нужно синхронизировать с утверждённым прогрессом на уровне репозитория.
- Папка `i18n/` используется для многоязычных вариантов README.
- Корневой README считается каноническим; локализованные версии должны соответствовать ему при обновлениях.

## Канонический прогресс курсов (сохранён и реорганизован)

### Базовые курсы

#### Классическая механика
Учебник курса [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681) уже издан. Купить его можно на Amazon: [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681).

#### Квантовая механика
Учебник курса [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903) уже издан. Купить его можно на Amazon: [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903).

#### Специальная теория относительности и электродинамика
Учебник курса [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065) уже издан. Купить его можно на Amazon: [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065).

#### Таблица прогресса базовых курсов
| Курс | Прогресс черновика | Прогресс заметок | Замечания |
|---|---:|---:|---|
| Общая теория относительности | 10/10 | 10/10 | Конспекты этого курса взяты с https://www.lapasserelle.com/general_relativity/. |
| Космология | 10/10 | 9/10 | Конспекты этого курса с 1 по 9 глав взяты с https://www.lapasserelle.com/cosmology/. Глава 10 находится в процессе доработки. |
| Статистическая механика | 11/11 | 10/10 | Конспекты взяты с https://www.lapasserelle.com/statistical_mechanics/. |

### Дополнительные курсы
| Курс | Прогресс черновика | Прогресс заметок |
|---|---:|---:|
| Продвинутая квантовая механика | 0/10 | 0/10 |
| Бозон Хиггса | 0/1 | 0/1 |
| Квантовая запутанность | 0/9 | 0/9 |
| Относительность | 0/9 | 0/9 |
| Физика элементарных частиц 1: Основные понятия | 6/10 | 0/10 |
| Физика элементарных частиц 2: Стандартная модель | 0/10 | 0/10 |
| Физика элементарных частиц 3: Суперсимметрия и великое объединение | 0/10 | 0/10 |
| Струнная теория | 0/11 | 10/10 |
| Космология и чёрные дыры | 0/8 | 0/10 |

### Примечание к целостности прогресса
- Таблицы прогресса выше сохранены из каноничного английского README.
- В репозитории есть как завершённые, так и шаблонные треки; если запись в таблице и состояние папок расходятся, используйте таблицу как документированную правду и обновляйте обе части вместе в следующих ревизиях.

## Устранение неполадок
| Проблема | Решение |
|---|---|
| `pdflatex: command not found` | Установите дистрибутив LaTeX и убедитесь, что исполняемые файлы доступны в `PATH`. |
| Не отображается библиография/индекс | Запустите нужный backend (`bibtex` или `biber`) и `makeindex`, если он используется, затем повторите запуск `pdflatex`. |
| Ошибка отсутствующих файлов стилей/класса | Собирайте проект из его целевой папки, чтобы относительные пути к локальным файлам разрешались корректно. |
| Сборка отличается в разных окружениях | Репозиторий содержит материалы, созданные в разных окружениях; где возможно, выравнивайте версии пакетов. |
| Устаревшие ссылки на языки или отсутствуют README | Проверьте синхронность строки выбора языков вверху и файлов в `i18n/`. |
| Несоответствие markdown-ссылок после переименования папки | Перепроверьте в одном проходе ссылки корневого README и всех `i18n/README.*.md`. |

## Дорожная карта
- Продолжить работу над дополнительными треками с полноценно заполненными главами и исходниками.
- Повысить согласованность README по каждому треку.
- Расширять и поддерживать многоязычные версии README в `i18n/` и синхронизировать языковой выбор.
- Добавить на уровне репозитория раздел с рекомендациями по сборке для каждого подпроекта с исходниками LaTeX.
- Добавить примеры сборки для треков, где есть расхождения в локальных toolchain.
- Добавить минимальную автоматизацию проверки целостности ссылок README/i18n.

## Вклад
Вы можете внести вклад в проект, сделав fork и отправив pull request.

Рекомендуемые направления:
- Добавление или улучшение глав и ссылок в конспектах.
- Улучшение качества TeX-исходников и воспроизводимых инструкций по сборке.
- Синхронизация заявлений о прогрессе между корневым README и README треков.
- Поддержание единообразия многоязычных README в `i18n/`.

Рекомендуемая практика pull request:
- Указывайте точные папки треков, которые вы изменили.
- Приводите команды сборки LaTeX, если правили исходные файлы.
- Обновляйте соответствующие таблицы прогресса при изменении статуса глав.
- Обновляйте `i18n/` после изменений в каноническом английском README.

## Благодарности
- Профессору Леонарду Сасскинду за исходные лекционные материалы.
- Ссылка на исходный материал заметок: https://www.lapasserelle.com/general_relativity/
- Ссылка на исходный материал заметок: https://www.lapasserelle.com/cosmology/
- Ссылка на исходный материал заметок: https://www.lapasserelle.com/statistical_mechanics/

## Лицензия
Этот репозиторий распространяется по лицензии GNU General Public License v3.0. См. файл [LICENSE](LICENSE).


## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |
