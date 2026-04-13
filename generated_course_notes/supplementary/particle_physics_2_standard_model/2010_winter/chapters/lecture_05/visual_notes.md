# Visual Evidence
## Frame Inventory

- `lecture_05_figure_02.png`: close whiteboard view of the Maxwell-theory setup, showing the four-vector potential and a shorter derivative-based line pointing down to `E`; this screenshot should remain in the final notes as visual evidence for notation and board layout.
- `lecture_05_figure_03.png`: sparse whiteboard from the SU(3) discussion, with the ordinary transformation on the top right and the complex-conjugate transformation beneath it, plus an isolated leftover `A_{ij}` on the left; this screenshot should remain in the final notes.
- `lecture_05_figure_04.png`: hand-drawn weak-decay sketch with an incoming `\pi^-`, an intermediate `W^-`, and two outgoing branches labeled by a charged lepton and an antineutrino; this screenshot should remain in the final notes and should also be paired with a clean redraw.

## Equation Extraction

- `lecture_05_figure_02.png`: \(A_\mu = (A_0,\vec A_{1,2,3})\) [visible]
- `lecture_05_figure_02.png`: \(F_x = e\,\nabla A\) [partially visible]
- `lecture_05_figure_02.png`: \(\downarrow\,E\) [visible]
- `lecture_05_figure_02.png`: \(F_x = e\,\partial_x A_0\) [standard completion]

- `lecture_05_figure_03.png`: \(A_{ij}\) [visible]
- `lecture_05_figure_03.png`: \(U_{ij}\,q_j \to q_i'\) [visible]
- `lecture_05_figure_03.png`: \(U_{ij}^{*}\,q_j^{*}\) [visible]
- `lecture_05_figure_03.png`: \(q_i^{\prime *}=U_{ij}^{*}q_j^{*}\) [standard completion]

- `lecture_05_figure_04.png`: \(\pi^-\) [visible]
- `lecture_05_figure_04.png`: \(W^-\) [visible]
- `lecture_05_figure_04.png`: \(\mu^-\) [partially visible]
- `lecture_05_figure_04.png`: \(\bar\nu_\mu\) [visible]
- `lecture_05_figure_04.png`: \(\pi^- \sim d\bar u\) [standard completion]
- `lecture_05_figure_04.png`: \(\pi^- \to W^- \to \mu^-+\bar\nu_\mu\) [standard completion]

## Diagram Extraction

- `lecture_05_figure_02.png`: this is not really a full diagram but a board checkpoint. It should be preserved as a screenshot, not redrawn as TikZ, because its value is documentary: it shows how Susskind introduced the four-potential on the board and visually tied the lower derivative line to the electric field.
- `lecture_05_figure_03.png`: this is an equation-layout figure rather than a geometric diagram. It should be preserved as a screenshot and paired with clean typeset equations, but it does not need a TikZ redraw.
- `lecture_05_figure_04.png`: this is a genuine hand-drawn Feynman-style decay sketch with time running left to right. It should be shown both ways: preserved as a screenshot for board evidence and redrawn in TikZ as a clean decay diagram.
- `lecture_05_figure_04.png`: the incoming pion line appears to carry the quark-content reminder inside the line itself, while the vertex marked `W^-` splits into two outgoing branches. The outgoing labels are uneven in legibility, but the lower branch clearly reads as an antineutrino and the upper branch is consistent with a charged muon.

## Reconstruction Guidance

- For `lecture_05_figure_02.png`, keep the screenshot visible and place a clean displayed equation nearby, preferably \(A_\mu=(A_0,\vec A)\). The lower line should be handled cautiously: use the transcript to explain that Susskind is relating the electric field to derivatives of the scalar potential, rather than claiming that every symbol on the board is perfectly legible.
- For `lecture_05_figure_03.png`, keep the screenshot and typeset the pair of transformations cleanly as \(q_i'=U_{ij}q_j\) and \(q_i^{\prime *}=U_{ij}^*q_j^*\). The screenshot matters because it preserves the vertical two-line board organization: first the original representation, then the conjugate one directly underneath.
- For `lecture_05_figure_04.png`, keep the screenshot and add a clean TikZ redraw of the decay topology. The redraw should make the vertex, outgoing branches, and labels fully legible, while the screenshot remains nearby as evidence for the lecturer’s original board sketch and the specific left-to-right layout.
- In the clean redraw for `lecture_05_figure_04.png`, the pion’s quark content can be added as a small annotation such as \(d\bar u\), but it should stay secondary to the decay topology. The main purpose is to present the process \(\pi^- \to W^- \to \mu^-+\bar\nu_\mu\) clearly.
- More generally, where the board is partial, the notes should prefer cautious normalization of notation over aggressive completion. The transcript should supply the physics; the frames should supply evidence for notation, labels, and layout.

## Uncertainties

- In `lecture_05_figure_02.png`, the lower formula is not reliably legible beyond the broad structure “force equals charge times derivative-like operation on the potential.” The exact derivative symbol and exact argument should not be overclaimed from the frame alone.
- In `lecture_05_figure_02.png`, the spatial part of the four-potential looks like an arrowed \(A\) followed by `1,2,3`; for polished notes this should be normalized to \(\vec A\).
- In `lecture_05_figure_03.png`, the field symbol appears to be \(q\), but the handwriting is loose enough that the transcript should remain the final arbiter.
- In `lecture_05_figure_03.png`, the second line visibly shows the starred matrix and starred field, but the final primed starred output is not written as explicitly as the top line and should be completed only in clean typeset form.
- In `lecture_05_figure_03.png`, the isolated `A_{ij}` on the left should not be mistaken for part of the conjugation derivation; it is residual board content from the adjacent gluon-field discussion.
- In `lecture_05_figure_04.png`, the upper outgoing label is less clear than the lower one. The identification of the top branch as \(\mu^-\) is supported by the surrounding lecture content, not by perfect visual legibility alone.
- In `lecture_05_figure_04.png`, side notes such as `12 minutes`, `1 nsec`, and faint writing around the sketch belong to the surrounding weak-decay discussion and should not be incorporated into the clean decay figure itself.