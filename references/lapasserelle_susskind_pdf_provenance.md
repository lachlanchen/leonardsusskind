# La Passerelle Provenance Notes

This note documents the strongest public provenance signals for the older PDF note sets preserved in this repository under:

- `core_cosmology/`
- `core_general_relativity/`
- `core_statistical_mechanics/`

It distinguishes between two different roles:

- original note source or notetaker attribution
- repository curation and publication into this Git archive

## Summary

| Course folder | Public source page | Public attribution signal | Confidence |
| --- | --- | --- | --- |
| `core_cosmology/` | <https://www.lapasserelle.com/cosmology/> | The page labels `Notetaker` and links that label to <https://www.lapasserelle.com/webmaster.html>, whose page title is `André Cabannes webmaster`. | Strong |
| `core_statistical_mechanics/` | <https://www.lapasserelle.com/statistical_mechanics/> | The page labels `Notetaker` and links that label to <https://www.lapasserelle.com/webmaster.html>, whose page title is `André Cabannes webmaster`. | Strong |
| `core_general_relativity/` | <https://www.lapasserelle.com/general_relativity/> | The page links `Coauthor` to <https://www.lapasserelle.com/webmaster.html>, again pointing to `André Cabannes webmaster`. The current page emphasizes the later book edition more than the old downloadable lesson PDFs. | Moderate |

## What The Local PDFs Say

The older lesson PDFs do not name a notetaker in their embedded metadata or on the first page.

What they do say on page one:

- `core_cosmology/lesson_1.pdf`: notes from Prof. Susskind video lectures publicly available on YouTube
- `core_general_relativity/lesson_1.pdf`: notes from Prof. Susskind video lectures publicly available on YouTube
- `core_statistical_mechanics/lesson_1.pdf`: the same statement, plus a note that pages 7 to 20 on elementary probability theory were developed by the notetaker from the original lecture

That statistical mechanics remark confirms editorial intervention by a notetaker, but it still does not name that person inside the PDF.

## What The La Passerelle Pages Add

The La Passerelle course pages provide the clearest public attribution signal currently visible:

- the cosmology page links `Notetaker` to `webmaster.html`
- the statistical mechanics page links `Notetaker` to `webmaster.html`
- the webmaster page is titled `André Cabannes webmaster`
- the general relativity page links `Coauthor` to the same webmaster page

Taken together, that strongly suggests André Cabannes was involved in preparing or curating the La Passerelle note sets, especially for cosmology and statistical mechanics. For general relativity, the signal is still meaningful, but the current public page is less explicit about the older lesson PDF series.

## What This Repository Adds

These files were brought into this Git archive by Lachlan Chen, but that does not by itself establish original authorship of the notes.

Relevant repository history:

- commit `2d20335` added the `general_relativity/lesson_*.pdf` set
- commit `98bb288` added the `cosmology/lesson_*.pdf` and `statistical_mechanics/lesson_*.pdf` sets
- commit `7c0e824` later renamed the old folder layout into the current `core_*` structure

So the careful reading is:

- likely original public note source: La Passerelle
- strongest named public attribution signal: André Cabannes
- repository curator who archived these copies here: Lachlan Chen

## Caution

This is provenance documentation, not a claim of exclusive authorship.

The evidence supports a practical statement such as:

> The older cosmology, general relativity, and statistical mechanics PDFs preserved in this repository appear to derive from La Passerelle note sets associated with André Cabannes, while the Git repository copies themselves were later archived here by Lachlan Chen.

That is a defensible summary of the available evidence without overstating it.
