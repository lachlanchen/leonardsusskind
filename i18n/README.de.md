[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


<p align="center">
  <img src="https://raw.githubusercontent.com/lachlanchen/lachlanchen/main/logos/banner.png" alt="LazyingArt banner" />
</p>

# Leonard-Susskind-Vorlesungsnotizen-Repository


![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg)
![Content Type](https://img.shields.io/badge/content-Lecture%20Notes%20%26%20LaTeX-informational)
![Status](https://img.shields.io/badge/status-Active%20Archive-success)
![LaTeX](https://img.shields.io/badge/tooling-LaTeX-008080)
![i18n](https://img.shields.io/badge/i18n-directory%20ready-orange)

## 📖 Überblick
Dieses Repository ist ein inhaltsorientiertes Archiv von Vorlesungsnotizen zu Kursen von Professor Leonard Susskind.

Die Vorlesungsnotizen von Professor Leonard Susskind. Falls dies gegen Urheberrechte verstößt, kontaktieren Sie mich bitte, damit ich dieses Repository lösche. Professor Susskind übernimmt keine Verantwortung für Fehler oder Fehlinformationen in den Notizen, ebenso wenig wie ich.

### Primäre Ziele
- Kursnotizen und Fortschritt an einem Ort bündeln.
- Sichtbarkeit des Entwurfs-/Notizenfortschritts über Kern- und Ergänzungskurse hinweg erhalten.
- Quellmaterialien (PDF, TeX, BibTeX, Templates) für die weitere Ausarbeitung bereitstellen.

## ✨ Funktionen
- Nachverfolgung und Referenzen für Kernkurse.
- Fortschrittsverfolgung für ergänzende Kurse.
- Vorhandene Lektions-PDFs für mehrere Kernbereiche.
- LaTeX-Quellmaterial in ausgewählten Bereichen.
- Wiederverwendbare LaTeX-Templates in `template/tuftle` und `template/kaobook`.
- Repository-Grafiken in `figs/`.

## 📌 Schnellübersicht
| Bereich | Verfügbar |
|---|---|
| 📚 Notizen | Mehrere Kurs-Notizensammlungen mit Fortschrittsverfolgung |
| 🧪 Quellen | TeX/BibTeX-Quellen in ausgewählten Unterprojekten |
| 🧰 Templates | `template/tuftle` und `template/kaobook` |
| 🌐 i18n | `i18n/`-Verzeichnis vorhanden (ursprünglich als leer markiert; inzwischen mit Sprachdateien befüllt) |

## 🗂️ Projektstruktur
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

## 🧩 Voraussetzungen
Nur zum Lesen:
- Ein PDF-Reader.

Zum Bearbeiten/Bauen von TeX-Materialien:
- Eine LaTeX-Distribution (TeX Live / MiKTeX).
- `pdflatex`.
- `bibtex` oder `biber` je nach Unterprojekt.
- `makeindex` für Templates, die einen Index verwenden.

Annahmehinweis:
- In diesem Repository gibt es kein einheitliches Build-System auf Root-Ebene (`Makefile`, `package.json`, `pyproject.toml`).

## 🚀 Installation
```bash
git clone https://github.com/<your-user>/leonardsusskind.git
cd leonardsusskind
```

Für die grundlegende Nutzung (Lesen bestehender Notizen) ist kein Paket-Installationsschritt erforderlich.

## 🛠️ Nutzung
### 1) Bestehende Notizen lesen
- Öffnen Sie PDFs in den entsprechenden Ordnern, zum Beispiel:
  - `core_general_relativity/lesson_1.pdf`
  - `core_cosmology/lesson_1.pdf`
  - `core_statistical_mechanics/lesson_1.pdf`

### 2) An LaTeX-Materialien arbeiten
- Bearbeiten Sie `.tex`- und `.bib`-Dateien im Zielkurs-/Template-Ordner.
- Kompilieren Sie mit der für diesen Ordner erwarteten Toolchain.

## ⚙️ Konfiguration
Es gibt keine globale Konfigurationsdatei.

Die Konfiguration ist lokal für jedes TeX-Projekt (Dokumentklasse, Bibliografie-Backend, Style-Dateien, Grafikpfade), zum Beispiel:
- `template/kaobook/main.tex`
- `template/tuftle/main.tex`
- `core_cosmology/cosmology_ch10/cosmology_ch10.tex`

## 🧪 Beispiele
### Beispiel A: `template/kaobook` bauen
`template/kaobook/main.tex` dokumentiert diese Kompilierkette:

```bash
cd template/kaobook
pdflatex main
makeindex main.idx -s StyleInd.ist
biber main
pdflatex main
pdflatex main
```

### Beispiel B: `core_cosmology/cosmology_ch10` bauen
`cosmology_ch10.tex` verwendet `\bibliography{ref}` (BibTeX-Workflow):

```bash
cd core_cosmology/cosmology_ch10
pdflatex cosmology_ch10.tex
bibtex cosmology_ch10
pdflatex cosmology_ch10.tex
pdflatex cosmology_ch10.tex
```

### Beispiel C: Ein erzeugtes Kapitel-PDF anzeigen
```bash
xdg-open supplemental_particle_physics_1/ch1/main.pdf
```

## 📝 Entwicklungshinweise
- Dies ist primär ein Dokumentations-/Notizen-Repository, keine Anwendungs-Codebasis.
- Manche Ordner enthalten erzeugte TeX-Artefakte (`.aux`, `.log`, `.toc`, `.bbl` usw.), die im Repository versioniert sind.
- Build-Befehle können je Unterverzeichnis variieren; befolgen Sie die lokalen `.tex`-Konventionen.
- `i18n/` existiert und ist für mehrsprachige README-Varianten vorgesehen.

## 📚 Kanonischer Kursfortschritt (Erhalten und neu strukturiert)

### Kernkurse

#### Klassische Mechanik
Das Lehrbuch dieses Kurses [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681) wurde veröffentlicht. Sie können es bei Amazon kaufen: [Classical Mechanics](https://www.amazon.com/gp/product/0465075681?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465075681).

#### Quantenmechanik
Das Lehrbuch dieses Kurses [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903) wurde veröffentlicht. Sie können es bei Amazon kaufen: [Quantum Mechanics](https://www.amazon.com/gp/product/0465062903?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=0465062903).

#### Spezielle Relativitätstheorie und Elektrodynamik
Das Lehrbuch dieses Kurses [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065) wurde veröffentlicht. Sie können es bei Amazon kaufen: [Special Relativity and Electrodynamics](https://www.amazon.com/gp/product/1541674065?ie=UTF8&tag=lachlanchen-20&camp=1789&linkCode=xm2&creativeASIN=1541674065).

#### Kernfortschrittstabelle
| Kurs | Entwurfsfortschritt | Notizenfortschritt | Notizen/Referenz |
|---|---:|---:|---|
| General Relativity | 10/10 | 10/10 | Die Vorlesungsnotizen wurden von https://www.lapasserelle.com/general_relativity/ erstellt. |
| Cosmology | 10/10 | 9/10 | Die Vorlesungsnotizen von Kapitel 1 bis 9 wurden von https://www.lapasserelle.com/cosmology/ erstellt. Kapitel 10 ist in Bearbeitung. |
| Statistical Mechanics | 11/11 | 10/10 | Die Vorlesungsnotizen wurden von https://www.lapasserelle.com/statistical_mechanics/ erstellt. |

### Ergänzende Kurse
| Kurs | Entwurfsfortschritt | Notizenfortschritt |
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

## 🧯 Fehlerbehebung
- `pdflatex: command not found`
  - Installieren Sie eine LaTeX-Distribution und stellen Sie sicher, dass die Binärdateien im `PATH` liegen.
- Literaturverzeichnis/Index erscheint nicht
  - Führen Sie das benötigte Backend (`bibtex` oder `biber`) sowie ggf. `makeindex` aus und führen Sie dann `pdflatex` erneut aus.
- Fehlende Style-/Class-Dateien
  - Bauen Sie aus dem vorgesehenen Projektverzeichnis, damit relative Pfade zu lokalen Assets korrekt aufgelöst werden.
- Build-Ausgabe unterscheidet sich zwischen Umgebungen
  - Dieses Repository enthält Materialien aus unterschiedlichen Umgebungen; gleichen Sie Paketversionen nach Möglichkeit an.

## 🗺️ Roadmap
- Ergänzende Kurse mit echten Kapitelinhalten und Quelldateien fortsetzen.
- Konsistenz der kursspezifischen README-Dateien verbessern.
- Mehrsprachige README-Dateien unter `i18n/` ergänzen und die Sprachauswahl synchron halten.
- Einen repositoryweiten Build-Leitfaden für jedes Unterprojekt mit TeX-Quellen ergänzen.

## ❤️ Beitrag oder Spende
Man kann zu diesem Projekt beitragen, indem man dieses Projekt forkt und einen Pull Request sendet. Wenn dieses Projekt Ihnen hilft, Entwicklungszeit zu sparen, können Sie mir einen Kaffee spendieren :)

## 🙏 Danksagung
- Professor Leonard Susskind für die ursprünglichen Vorlesungsinhalte.
- Vorhandene referenzierte Notizquellen:
  - https://www.lapasserelle.com/general_relativity/
  - https://www.lapasserelle.com/cosmology/
  - https://www.lapasserelle.com/statistical_mechanics/

## 📄 Lizenz
Dieses Repository ist unter der GNU General Public License v3.0 lizenziert. Siehe [LICENSE](LICENSE).
