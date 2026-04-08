# Theoretical Minimum Companion Notes

This directory imports the TeX note set from `/home/lachlan/ProjectsLFS/Physics/tm` into a dedicated tree inside this repository without mixing it into the existing `core_*`, `supplemental_*`, or `the_theoretical_minimum/` structures. The original upstream repository is `https://github.com/weka511/tm` by Simon Crase.

Structure:

- `shared/`: common assets copied from `tm`, including `figs/`, `tm.bib`, and `glossary-entries.tex`
- `core/`: imported core-course notes
- `supplementary/`: imported supplementary-course notes
- `extras/`: imported non-course or support TeX notes such as QFT and pytearcat examples

Each leaf directory contains one TeX entry plus symlinks back to the shared assets so it can be compiled in place.

The imported copies include a few minimal compatibility fixes for this environment, including a vendored `shared/tensor.sty` and small TeX corrections needed to get all PDFs building cleanly.

Build everything:

```bash
./theoretical_minimum_companion_notes/build_all.sh
```

Build one note manually:

```bash
cd theoretical_minimum_companion_notes/core/cosmology/cosmology
lualatex cosmology.tex
makeglossaries cosmology
bibtex cosmology
lualatex cosmology.tex
lualatex cosmology.tex
```
