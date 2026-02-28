[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)



[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# Repository der Leonard-Susskind-Vorlesungsnotizen

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

> 🎓 Ein mehrsprachiges Archiv von Leonard Susskind-Vorlesungsunterlagen, das sowohl aufbereitete PDFs als auch editierbare LaTeX-Quellen für Studium, Wiederverwendung und Referenz bewahrt.

## Überblick
Dieses Repository ist ein inhaltlich ausgerichtetes Archiv von Vorlesungsunterlagen aus dem Lehrumfeld von Professor Leonard Susskind.

> Die Vorlesungsnotizen von Professor Leonard Susskind. Wenn dies gegen Urheberrechte verstößt, kontaktieren Sie mich bitte, um dieses Repository zu entfernen. Professor Susskind übernimmt weder Verantwortung für Fehler noch Fehlinformationen in den Notizen – das gilt ebenfalls für mich.

Es vereint drei Ebenen an einem Ort:

- Kuratierte Notizspuren und kursbezogenen Fortschritt.
- Verfügbare Artefakte (`.pdf`) zum Lesen und Teilen.
- Quelldateien (`.tex`, `.bib`, Templates) für Personen, die das Archiv pflegen oder erweitern.

### Hauptziele
- Kursnotizen und Fortschritt an einer Stelle zusammenführen.
- Entwurfs- und Notizfortschritt für Kern- und Ergänzungskurse sichtbar halten.
- Quellmaterialien (PDF, TeX, BibTeX, Templates) für fortgesetztes Erstellen bereitstellen.

## Funktionen
- Nachverfolgung und Referenzen für Kernkurse.
- Fortschrittsnachverfolgung für Ergänzungskurse.
- Vorliegende Vorlesungs-PDFs für mehrere Kernkurse.
- LaTeX-Quellmaterial in ausgewählten Pfaden.
- Wiederverwendbare LaTeX-Templates in `template/tuftle` und `template/kaobook`.
- Repository-Assets in `figs/`.
- Mehrsprachige README-Varianten in `i18n/`.

## Schnellübersicht
| Bereich | Verfügbarkeit |
|---|---|
| 📝 Notizen | Mehrere Kursnotiz-Sammlungen mit Fortschrittsnachverfolgung |
| 🧾 Quelle | TeX/BibTeX-Quellen in ausgewählten Teilprojekten |
| 🧱 Templates | `template/tuftle` und `template/kaobook` |
| 🎨 Branding | `figs/banner.*`, `figs/logo.*`, `figs/logo-w-text.*` |
| 🌍 Mehrsprachigkeit | Sprachvarianten `i18n/README.*.md` |

## Inhaltsverzeichnis
- [Überblick](#überblick)
- [Funktionen](#funktionen)
- [Schnellübersicht](#schnellübersicht)
- [Projektstruktur](#projektstruktur)
- [Voraussetzungen](#voraussetzungen)
- [Installation](#installation)
- [Nutzung](#nutzung)
- [Konfiguration](#konfiguration)
- [Beispiele](#beispiele)
- [Entwicklungsnotizen](#entwicklungsnotizen)
- [Kanonischer Kursfortschritt (Erhalten und reorganisiert)](#kanonischer-kursfortschritt-erhalten-und-reorganisiert)
- [Fehlerbehebung](#fehlerbehebung)
- [Roadmap](#roadmap)
- [Beitrag](#beitrag)
- [❤️ Support](#-support)
- [Danksagung](#danksagung)
- [Lizenz](#lizenz)

## Projektstruktur
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

## Voraussetzungen
Zum Lesen:
- Ein PDF-Reader (systemseitig oder als App).

Zum Bearbeiten/Erstellen von TeX-Materialien:
- Eine LaTeX-Distribution (TeX Live / MiKTeX).
- `pdflatex`.
- `bibtex` oder `biber`, je nach Unterprojekt.
- `makeindex` für Projekte, die Indizes verwenden.

Hinweis zu Annahmen:
- Es gibt kein einheitliches Root-Buildsystem (`Makefile`, `package.json`, `pyproject.toml`) in diesem Repository.
- Build-Workflows werden voraussichtlich aus jedem Unterverzeichnis ausgeführt.

## Installation
```bash
git clone https://github.com/lachlanchen/leonardsusskind.git
cd leonardsusskind
```

Dieses Repository ist inhaltlich priorisiert. Wenn es gespiegelt oder geforkt wird, ersetzen Sie die Remote-URL entsprechend durch Ihre eigene Kopie.

Für das reine Lesen bestehender Notizen ist keine globale Paketinstallation erforderlich.

## Nutzung
### 1) Bestehende Notizen lesen
Öffnen Sie die PDFs in den passenden Ordnern, zum Beispiel:
- `core_general_relativity/lesson_1.pdf`
- `core_cosmology/lesson_1.pdf`
- `core_statistical_mechanics/lesson_1.pdf`
- `supplemental_particle_physics_2/NumberTheory.pdf`

### 2) LaTeX-Materialien erstellen oder erweitern
- Bearbeiten Sie `.tex`- und `.bib`-Dateien im Zielkurs-/Template-Ordner.
- Kompilieren Sie mit dem in diesem Ordner vorgesehenen Workflow.
- Arbeiten Sie lokal im jeweiligen Projektverzeichnis, damit relative Pfade zu Assets und Stil-Dateien korrekt aufgelöst werden.

### 3) Per Track-Einstieg navigieren
Jede große Spur (`track`) hat ihr eigenes `README.md` mit lokalem Kontext, Referenzen und Fortschrittsstatus.

## Konfiguration
Es gibt keine globale Konfigurationsdatei.

Die Konfiguration ist lokal für jedes TeX-Projekt definiert. Typische Einstellpunkte sind in den Quelldateien eingebettet, darunter:
- Dokumentenklasse und Paketkonfiguration in `template/kaobook/main.tex`
- Wiederverwendbarer Stil/Struktur in `template/kaobook/`
- Bibliografie-Backend und Zitierstil in lokalen `main.tex`/`ref.bib`-Paaren
- Einbindepfade für Bilder und kapitelspezifische Assets in jedem Projekt

Typische lokale Konfigurationspunkte:
- `template/kaobook/main.tex`
- `template/tuftle/main.tex`
- `core_cosmology/cosmology_ch10/cosmology_ch10.tex`
- `supplemental_particle_physics_1/ch1/main.tex`
- `supplemental_advanced_quantum/ch1/main.tex`

## Beispiele
### Beispiel A: Build von `template/kaobook`
`template/kaobook/main.tex` dokumentiert diese Kompilierkette:

```bash
cd template/kaobook
pdflatex main
makeindex main.idx -s StyleInd.ist
biber main
pdflatex main
pdflatex main
```

### Beispiel B: Build von `core_cosmology/cosmology_ch10`
`cosmology_ch10.tex` verwendet einen BibTeX-artigen Workflow:

```bash
cd core_cosmology/cosmology_ch10
pdflatex cosmology_ch10.tex
bibtex cosmology_ch10
pdflatex cosmology_ch10.tex
pdflatex cosmology_ch10.tex
```

### Beispiel C: Build von `supplemental_particle_physics_1/ch1`
```bash
cd supplemental_particle_physics_1/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### Beispiel D: Build von `supplemental_advanced_quantum/ch1`
```bash
cd supplemental_advanced_quantum/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### Beispiel E: Ausgabe lokal anzeigen
```bash
xdg-open supplemental_particle_physics_1/ch1/main.pdf
```

## Entwicklungsnotizen
- Dieses Repository ist primär ein Dokumentations- und Notiz-Repository, kein Anwendungs-Codebestand.
- Einige Ordner enthalten generierte TeX-Artefakte (`.aux`, `.log`, `.toc`, `.bbl` usw.), die im Repository versioniert sind.
- Build-Befehle können je nach Unterverzeichnis variieren; folgen Sie den lokalen `.tex`-Konventionen.
- Pro-Track-`README.md`-Dateien existieren in den Kern- und Ergänzungsverzeichnissen und sollten mit den Fortschrittsangaben der Wurzel synchron bleiben.
- `i18n/` ist vorhanden und dient den mehrsprachigen README-Varianten.
- Die Root-README ist kanonisch; lokalisierte Dateien sollten ihr bei Aktualisierungen folgen.

## Kanonischer Kursfortschritt (Erhalten und reorganisiert)

### Kernkurse

#### Klassische Mechanik
Das Lehrbuch zu diesem Kurs [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681) wurde veröffentlicht. Sie können es bei Amazon unter [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681) kaufen.

#### Quantenmechanik
Das Lehrbuch zu diesem Kurs [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903) wurde veröffentlicht. Sie können es bei Amazon unter [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903) kaufen.

#### Spezielle Relativitätstheorie und Elektrodynamik
Das Lehrbuch zu diesem Kurs [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065) wurde veröffentlicht. Sie können es bei Amazon unter [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065) kaufen.

#### Kernfortschrittstabelle
| Kurs | Entwurfsfortschritt | Notizfortschritt | Notizen/Referenzen |
|---|---:|---:|---|
| General Relativity | 10/10 | 10/10 | Die Vorlesungsnotizen wurden von https://www.lapasserelle.com/general_relativity/ erstellt. |
| Cosmology | 10/10 | 9/10 | Die Vorlesungsnotizen von Kapitel 1 bis 9 wurden von https://www.lapasserelle.com/cosmology/ erstellt. Kapitel 10 befindet sich in Bearbeitung. |
| Statistical Mechanics | 11/11 | 10/10 | Die Vorlesungsnotizen wurden von https://www.lapasserelle.com/statistical_mechanics/ erstellt. |

### Ergänzende Kurse
| Kurs | Entwurfsfortschritt | Notizfortschritt |
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

### Fortschrittsintegrität
- Die obigen Fortschrittstabellen wurden aus dem kanonischen README-Text übernommen.
- Das Repository enthält sowohl ausgearbeitete als auch Platzhalter-Tracks; stimmen ein Tabellenwert und der aktuelle Ordnerzustand nicht überein, ist die Tabelle als dokumentierte Intention zu behandeln und beide sollten in zukünftigen Überarbeitungen gemeinsam aktualisiert werden.

## Fehlerbehebung
| Problem | Lösung |
|---|---|
| `pdflatex: command not found` | Installieren Sie eine LaTeX-Distribution und stellen Sie sicher, dass die Binaries im `PATH` verfügbar sind. |
| Literaturverzeichnis/Index erscheint nicht | Führen Sie das erforderliche Backend (`bibtex` oder `biber`) und `makeindex` falls nötig aus und starten Sie `pdflatex` anschließend erneut. |
| Fehler durch fehlende Style-/Klassen-Dateien | Bauen Sie im vorgesehenen Projektverzeichnis, damit relative Pfade zu lokalen Assets korrekt aufgelöst werden. |
| Build-Ausgabe unterscheidet sich zwischen Umgebungen | Dieses Repository enthält Materialien aus unterschiedlichen Umgebungen; versuchen Sie, Paketversionen wo möglich zu synchronisieren. |
| Veraltete Mehrsprachigkeitslinks oder fehlende Sprach-README | Halten Sie die Sprachauswahllinie oben und die Dateien unter `i18n/` synchron. |
| GitHub-Markdown-Linkfehler nach Ordnerumbenennung | Validieren Sie die Root-Sprachlinks und sämtliche Verweise auf `i18n/README.*.md` in einem Durchlauf. |

## Roadmap
- Fortführung ergänzender Kurse mit echtem Kapitelinhalt und Quelldateien.
- Konsistenz der pro-Kurs-README-Dateien verbessern.
- Erweiterung und Pflege der mehrsprachigen README-Dateien unter `i18n/` und Synchronisierung des Sprachselectors.
- Ergänzen eines repositoryweiten Build-Leitfadens pro Unterprojekt mit TeX-Quellen.
- Ergänzen von pro-Track-Kompilierungsschnipseln dort, wo lokale Toolchains differieren.
- Einführung minimaler Automatisierung zur Validierung von README-/i18n-Link-Konsistenz.

## Beitrag
Sie können zu diesem Projekt beitragen, indem Sie es forken und einen Pull Request einreichen.

Empfohlener Beitrag:
- Ergänzen oder verbessern Sie Kapitelnotizen und Referenzen.
- Verbessern Sie die Qualität der TeX-Quellen und anwendbare Build-Anleitungen.
- Halten Sie Fortschrittsangaben von Root- und Track-README synchron.
- Sorgen Sie für mehrsprachige README-Konsistenz unter `i18n/`.

Empfohlene Pull-Request-Hygiene:
- Nennen Sie die genauen geänderten Track-Ordner.
- Fügen Sie die verwendeten TeX-Kompilierungsbefehle bei (falls Quelldateien bearbeitet wurden).
- Aktualisieren Sie relevante Fortschrittstabellen, wenn sich Kapitelzustände ändern.
- Aktualisieren Sie `i18n/`-README-Dateien nach Änderungen an der kanonischen englischen README.

## Danksagung
- Professor Leonard Susskind für die ursprünglichen Vorlesungsinhalte.
- Referenzierte Notizquelle: https://www.lapasserelle.com/general_relativity/
- Referenzierte Notizquelle: https://www.lapasserelle.com/cosmology/
- Referenzierte Notizquelle: https://www.lapasserelle.com/statistical_mechanics/

## Lizenz
Dieses Repository ist unter der GNU General Public License v3.0 lizenziert. Siehe [LICENSE](LICENSE).


## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |
