# Visual Evidence
## Frame Inventory
- `lecture_01_figure_02.png`: A Hamiltonian-like board expression for two nuclei plus electrons is visible, with the electron sector visually grouped off to the right; this screenshot should remain in the final notes.
- `lecture_01_figure_03.png`: A clean two-line scalar-field setup shows the Lagrangian density above and the action written as its spacetime integral below; this screenshot should remain in the final notes.
- `lecture_01_figure_04.png`: The left side shows the fermion mass term `m\bar\psi\psi`, while the right side contains quick chirality or interaction mnemonics; this screenshot should remain in the final notes.

## Equation Extraction
- `lecture_01_figure_02.png`: `\frac{e^2}{R_{12}}` [visible]
- `lecture_01_figure_02.png`: `\sum_i \frac{q_i^2}{2m}` [partially visible]
- `lecture_01_figure_02.png`: `\frac{e^2}{r_{ij}}` [visible]
- `lecture_01_figure_02.png`: `\frac{e^2}{R_{12}}+\left[\sum_i \frac{q_i^2}{2m}+\sum_{i<j}\frac{e^2}{r_{ij}}-\sum_i\left(\frac{e^2}{R_{1i}}+\frac{e^2}{R_{2i}}\right)\right]` [standard completion]

- `lecture_01_figure_03.png`: `\mathcal{L}=(\partial_\mu\phi)^2 - V(\phi)` [visible]
- `lecture_01_figure_03.png`: `S=\int d^4x\,\mathcal{L}` [visible]

- `lecture_01_figure_04.png`: `m\bar{\psi}\psi` [visible]
- `lecture_01_figure_04.png`: `R` [visible]
- `lecture_01_figure_04.png`: `L` [partially visible]

## Diagram Extraction
- `lecture_01_figure_02.png`: There is no standalone figure in the usual sense, but the board layout itself functions like a structural diagram: a nucleus-nucleus term on the left and a grouped electron sub-Hamiltonian on the right. Preserve it as a screenshot rather than redrawing the board layout in TikZ.
- `lecture_01_figure_03.png`: No diagram is present; the value of the frame is the two-step equation layout from local Lagrangian density to action. Preserve it as a screenshot only.
- `lecture_01_figure_04.png`: The right-hand chalk sketches are conceptual fermion-line mnemonics and are the only material here that should also be redrawn in TikZ. Show this frame both ways: keep the screenshot as evidence and add a small, schematic TikZ redraw nearby.

## Reconstruction Guidance
- For `lecture_01_figure_02.png`, keep the screenshot visible and place a clean displayed Hamiltonian beside it. The screenshot should preserve the grouping logic and blackboard structure, while the typed equation should restore the hidden electron-nucleus attraction terms from the transcript.
- For `lecture_01_figure_03.png`, typeset the two equations essentially as written on the board and keep the screenshot adjacent. This is a case where the original board order matters as much as the formulas themselves.
- For `lecture_01_figure_04.png`, typeset `m\bar{\psi}\psi` cleanly and redraw only the qualitative chirality-flow idea on the right. The TikZ should stay minimal, because the chalk marks are explanatory mnemonics rather than a fully specified Feynman-diagram calculation.
- When a term is only partly legible, prefer a cautious standard completion anchored by the transcript, not an aggressive image-only guess. The final notes should make clear what is reconstructed for clarity and what is directly visible on the board.

## Uncertainties
- In `lecture_01_figure_02.png`, the electron momentum symbol is not fully secure from the frame alone; it looks like `q_i`, but the transcript is more reliable for the exact notation.
- In `lecture_01_figure_02.png`, the electron-nucleus attraction terms are largely blocked by Susskind, so the full Hamiltonian cannot be recovered from the image alone.
- In `lecture_01_figure_02.png`, the lower grouping mark reads as a visual brace or bracket, but its exact chalk notation is not important enough to reproduce literally.
- In `lecture_01_figure_03.png`, the scalar Lagrangian is written schematically, without textbook normalization factors; those should not be inserted silently unless the notes explicitly shift to a conventional normalization.
- In `lecture_01_figure_04.png`, the small handwritten annotation near the middle sketch is not legible enough to transcribe confidently.
- In `lecture_01_figure_04.png`, the right-hand sketches do not fix a precise Feynman topology on their own; the transcript is needed to interpret them as chirality-preserving versus chirality-flipping processes.