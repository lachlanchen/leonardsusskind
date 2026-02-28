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

## Überblick
Dieses Repository ist ein inhaltlich zentriertes Archiv von Unterlagen zu Vorlesungen von Professor Leonard Susskind.

> Die Vorlesungsnotizen von Professor Leonard Susskind. Falls dies gegen Urheberrechte verstößt, kontaktieren Sie mich bitte, damit ich das Repository lösche. Professor Susskind übernimmt weder für Fehler noch für Fehlinformationen in den Notizen Verantwortung – das gilt ebenso für mich.

### Primäre Ziele
- Kursnotizen und Fortschritt an einem Ort bündeln.
- Sichtbarkeit des Entwurfs- und Notizfortschritts für Kern- und Ergänzungskurse erhalten.
- Quelldateien (PDF, TeX, BibTeX, Templates) für die weitere Bearbeitung bereitstellen.

## Funktionen
- Verfolgung und Referenzen für Kernkurse.
- Fortschrittsverfolgung für ergänzende Kurse.
- Vorhandene Vorlesungspdfs für mehrere Kernkurse.
- LaTeX-Quellmaterial in ausgewählten Teilprojekten.
- Wiederverwendbare LaTeX-Templates in `template/tuftle` und `template/kaobook`.
- Repository-Assets in `figs/`.
- Multilinguale README-Varianten in `i18n/`.

## Schnellübersicht
| Bereich | Verfügbar |
|---|---|
| 📝 Notizen | Mehrere Notizsammlungen mit Fortschrittsnachverfolgung |
| 🧾 Quelle | TeX/BibTeX-Quellen in ausgewählten Unterprojekten |
| 🧱 Templates | `template/tuftle` und `template/kaobook` |
| 🎨 Branding | `figs/banner.*`, `figs/logo.*`, `figs/logo-w-text.*` |
| 🌍 Mehrsprachigkeit | `i18n/README.*.md`-Sprachvarianten |

## Inhaltsverzeichnis
- Überblick
- Funktionen
- Schnellübersicht
- Projektstruktur
- Voraussetzungen
- Installation
- Nutzung
- Konfiguration
- Beispiele
- Entwicklungsnotizen
- Kanonischer Kursfortschritt (erhalten und reorganisiert)
- Fehlerbehebung
- Roadmap
- Beitrag
- [❤️ Support](#-support)
- Danksagung
- Lizenz

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
- Ein PDF-Reader.

Zum Bearbeiten/Erstellen von TeX-Materialien:
- Eine LaTeX-Distribution (TeX Live / MiKTeX).
- `pdflatex`.
- `bibtex` oder `biber` je nach Unterprojekt.
- `makeindex` für Templates, die einen Index verwenden.

Anmerkung zur Annahme:
- Es gibt kein einheitliches Build-System auf Root-Ebene (`Makefile`, `package.json`, `pyproject.toml`) in diesem Repository.

## Installation
```bash
git clone https://github.com/<your-user>/leonardsusskind.git
cd leonardsusskind
```

Wenn dieses Repository geforkt oder gespiegelt wurde, ersetzen Sie `<your-user>` durch das richtige Konto.

Für die reine Nutzung (Lesen bestehender Notizen) ist kein Paket-Installationsschritt erforderlich.

## Nutzung
### 1) Bestehende Notizen lesen
Öffnen Sie PDFs in den entsprechenden Ordnern, zum Beispiel:
- `core_general_relativity/lesson_1.pdf`
- `core_cosmology/lesson_1.pdf`
- `core_statistical_mechanics/lesson_1.pdf`
- `supplemental_particle_physics_2/NumberTheory.pdf`

### 2) An LaTeX-Materialien arbeiten
- Editieren Sie `.tex`- und `.bib`-Dateien im Zielkurs-/Template-Ordner.
- Kompilieren Sie mit der für diesen Ordner erwarteten Toolchain.
- Bevorzugen Sie den Ausführungsort im lokalen Projektverzeichnis, damit relative Pfade korrekt aufgelöst werden.

### 3) Nach Track-READMEs navigieren
Jeder große Track hat sein eigenes lokales `README.md` mit kontextbezogenen Notizen und Fortschrittsangaben.

## Konfiguration
Es gibt keine globale Konfigurationsdatei.

Die Konfiguration ist lokal für jedes TeX-Projekt (Dokumentklasse, Bibliografie-Backend, Stildateien, Grafikpfade) festgelegt, zum Beispiel:
- `template/kaobook/main.tex`
- `template/tuftle/main.tex`
- `core_cosmology/cosmology_ch10/cosmology_ch10.tex`
- `supplemental_particle_physics_1/ch1/main.tex`
- `supplemental_advanced_quantum/ch1/main.tex`

## Beispiele
### Beispiel A: Build von `template/kaobook`
`template/kaobook/main.tex` zeigt diese Kompilierkette:

```bash
cd template/kaobook
pdflatex main
makeindex main.idx -s StyleInd.ist
biber main
pdflatex main
pdflatex main
```

### Beispiel B: Build von `core_cosmology/cosmology_ch10`
`cosmology_ch10.tex` verwendet `\bibliography{ref}` (BibTeX-Workflow):

```bash
cd core_cosmology/cosmology_ch10
pdflatex cosmology_ch10.tex
bibtex cosmology_ch10
pdflatex cosmology_ch10.tex
pdflatex cosmology_ch10.tex
```

### Beispiel C: Build eines Tufte-basierten Kapitels (`supplemental_particle_physics_1/ch1`)
```bash
cd supplemental_particle_physics_1/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### Beispiel D: Build eines Tufte-basierten Kapitels (`supplemental_advanced_quantum/ch1`)
```bash
cd supplemental_advanced_quantum/ch1
pdflatex main.tex
bibtex main
makeindex main.idx
pdflatex main.tex
pdflatex main.tex
```

### Beispiel E: Erzeugen und Anzeigen eines Kapitel-PDFs
```bash
xdg-open supplemental_particle_physics_1/ch1/main.pdf
```

## Entwicklungsnotizen
- Dieses Repository ist primär ein Dokumentations- und Notizrepository, kein Anwendungs-Repository.
- Manche Ordner enthalten generierte TeX-Artefakte (`.aux`, `.log`, `.toc`, `.bbl` usw.), die im Repository versioniert sind.
- Build-Befehle können je nach Unterverzeichnis variieren; folgen Sie den lokalen `.tex`-Konventionen.
- Pro-Track-`README.md`-Dateien existieren in den Kern- und Ergänzungspfaden und sollten mit den Fortschrittsangaben der Root-Ebene konsistent gehalten werden.
- `i18n/` ist vorhanden und dient für mehrsprachige README-Varianten.
- Die Root-README gilt als kanonisch; mehrsprachige Dateien sollten bei Aktualisierungen angeglichen werden.

## Kanonischer Kursfortschritt (erhalten und reorganisiert)

### Kernkurse

#### Klassische Mechanik
Das Lehrbuch dieses Kurses [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681) wurde veröffentlicht. Sie können es bei Amazon unter [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681) erwerben.

#### Quantenmechanik
Das Lehrbuch dieses Kurses [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903) wurde veröffentlicht. Sie können es bei Amazon unter [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903) erwerben.

#### Spezielle Relativitätstheorie und Elektrodynamik
Das Lehrbuch dieses Kurses [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065) wurde veröffentlicht. Sie können es bei Amazon unter [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065) erwerben.

#### Kernfortschrittstabelle
| Kurs | Entwurfsfortschritt | Notizfortschritt | Notiz/Referenz |
|---|---:|---:|---|
| General Relativity | 10/10 | 10/10 | Die Vorlesungsnotizen wurden von https://www.lapasserelle.com/general_relativity/ erstellt. |
| Cosmology | 10/10 | 9/10 | Die Vorlesungsnotizen von Kapitel 1 bis 9 wurden von https://www.lapasserelle.com/cosmology/ erstellt. Kapitel 10 ist in Bearbeitung. |
| Statistical Mechanics | 11/11 | 10/10 | Die Vorlesungsnotizen wurden von https://www.lapasserelle.com/statistical_mechanics/ erstellt. |

### Ergänzungskurse
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

### Hinweis zur Fortschrittsintegrität
- Die obigen Fortschrittstabellen wurden aus dem kanonischen README-Text übernommen.
- Das Repository enthält sowohl ausgereifte als auch Platzhalter-Tracks; wenn ein Tabelleneintrag und der aktuelle Ordnerzustand nicht übereinstimmen, gilt die Tabelle als dokumentierte Zielvorgabe und beide sollten in zukünftigen Revisionen gemeinsam aktualisiert werden.

## Fehlerbehebung
| Problem | Lösung |
|---|---|
| `pdflatex: command not found` | Installieren Sie eine LaTeX-Distribution und stellen Sie sicher, dass die Binärdateien im `PATH` enthalten sind. |
| Literaturverzeichnis/Index erscheint nicht | Führen Sie das benötigte Backend (`bibtex` oder `biber`) sowie ggf. `makeindex` aus und starten Sie anschließend `pdflatex` erneut. |
| Fehler wegen fehlender Style-/Klassen-Dateien | Bauen Sie aus dem vorgesehenen Projektverzeichnis, sodass relative Pfade zu lokalen Assets korrekt aufgelöst werden. |
| Build-Ausgabe unterscheidet sich zwischen Umgebungen | Das Repository enthält Materialien aus verschiedenen Umgebungen; stimmen Sie möglichst Paketversionen aufeinander ab. |
| Veraltete Mehrsprachigkeitslinks oder fehlende Sprach-README | Halten Sie die Sprachoptionen-Zeile oben und die Dateien unter `i18n/` synchron. |
| GitHub-Markdown-Linkinkonsistenzen nach Umbenennung | Validieren Sie die Wurzellinks und alle `i18n/README.*.md`-Verweise in einem Durchlauf. |

## Roadmap
- Ergänzungskurse mit echtem Kapitelinhalt und Quelldateien fortführen.
- Konsistenz der pro-Kurs-README-Dateien verbessern.
- Multilinguale README-Dateien unter `i18n/` erweitern und den Sprachselektor synchron halten.
- Einen repositoryweiten Build-Leitfaden pro Unterprojekt mit TeX-Quellen ergänzen.
- Pro-Track-Compile-Snippets ergänzen, wo lokale Toolchains variieren.
- Eine minimale Automatisierung zur Prüfung von README-/i18n-Linkintegrität einführen.

## Beitrag
Sie können zu diesem Projekt beitragen, indem Sie es forken und einen Pull Request einreichen.

Empfohlener Beitragsumfang:
- Ergänzen oder verbessern Sie Kapitelnotizen und Referenzen.
- Verbessern Sie die Qualität der LaTeX-Quellen und reproduzierbare Build-Anweisungen.
- Halten Sie die Fortschrittsangaben von Root- und Kurs-README synchron.
- Pflegen Sie die Sprachparität in `i18n/` bei Änderungen der englischen README.

Empfohlene Pull-Request-Hygiene:
- Benennen Sie die exakt geänderten Track-Ordner.
- Geben Sie die verwendeten TeX-Kompilierungsbefehle an (falls Quelldateien bearbeitet wurden).
- Aktualisieren Sie relevante Fortschrittstabellen, wenn sich der Kapitelstatus ändert.
- Aktualisieren Sie `i18n/`-Readmes nach Änderungen an der kanonischen englischen README.

## ❤️ Support

| Donate | PayPal | Stripe |
|---|---|---|
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=ko-fi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## Danksagung
- Professor Leonard Susskind für die ursprünglichen Vorlesungsinhalte.
- Bereits genannte referenzierte Notizquelle: https://www.lapasserelle.com/general_relativity/
- Bereits genannte referenzierte Notizquelle: https://www.lapasserelle.com/cosmology/
- Bereits genannte referenzierte Notizquelle: https://www.lapasserelle.com/statistical_mechanics/

## Lizenz
Dieses Repository steht unter der GNU General Public License v3.0. Siehe [LICENSE](LICENSE).
