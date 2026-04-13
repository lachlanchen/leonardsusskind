# Visual Evidence
## Frame Inventory
- `lecture_04_figure_02.png`: Shows the delta-function spike centered at `y=a` on a horizontal `y`-axis, with a large nearby integral sign and `\delta(y-a)`; this screenshot should remain in the final notes because it is the only actual board sketch in the set.
- `lecture_04_figure_03.png`: Shows an almost blank board with `\hbar=1` and the vector relation between momentum and wave vector; this screenshot should remain in the final notes as clean evidence for the unit convention and notation.
- `lecture_04_figure_04.png`: Shows `\hbar=1` at left and the two relations `E=\hbar\omega` and `P=\hbar k` at right; this screenshot should remain in the final notes because the board is unusually clean and legible.
- `lecture_04_figure_05.png`: Shows the start of the time-dependent field expansion `\Psi(x,t)=\sum_k\cdots` on the right board, with older material still faintly visible on the left; this screenshot should remain in the final notes as layout evidence for where the derivation begins.
- `lecture_04_figure_06.png`: Shows the fuller field expansion across the top and lower derivative lines, including the corrected `-i\dot{\Psi}` line during the sign discussion; this screenshot should remain in the final notes because it captures the live structure of the derivation.

## Equation Extraction
- `lecture_04_figure_02.png`: `\delta(y-a)` `[visible]`
- `lecture_04_figure_02.png`: `y=a` `[visible]`
- `lecture_04_figure_02.png`: `\int \delta(y-a)` `[visible]`
- `lecture_04_figure_02.png`: `\int dy\,\delta(y-a)` `[standard completion]`

- `lecture_04_figure_03.png`: `\hbar=1` `[visible]`
- `lecture_04_figure_03.png`: `\vec p=\vec k` `[visible]`

- `lecture_04_figure_04.png`: `\hbar=1` `[visible]`
- `lecture_04_figure_04.png`: `E=\hbar\omega` `[visible]`
- `lecture_04_figure_04.png`: `P=\hbar k` `[visible]`

- `lecture_04_figure_05.png`: `\Psi(x,t)=\sum_k \cdots` `[partially visible]`
- `lecture_04_figure_05.png`: `\Psi(x,t)=\sum_k a^{+}(k)e^{-ikx}e^{i\omega(k)t}` `[standard completion]`

- `lecture_04_figure_06.png`: `\Psi(x,t)=\sum_k a^{+}(k)e^{-ikx}e^{i\omega(k)t}` `[partially visible]`
- `lecture_04_figure_06.png`: `-i\dot{\Psi}` `[partially visible]`
- `lecture_04_figure_06.png`: `\omega(k)` `[partially visible]`
- `lecture_04_figure_06.png`: `\sum_k \omega(k)a^{+}(k)e^{-ikx}e^{i\omega(k)t}` `[standard completion]`
- `lecture_04_figure_06.png`: `-i\dot{\Psi}=\frac{1}{2m}\frac{\partial^2\Psi}{\partial x^2}` `[standard completion]`

## Diagram Extraction
- `lecture_04_figure_02.png` contains the only genuine diagram: a narrow spike on the `y`-axis centered at `y=a`, used to visualize the Dirac delta function. This should be shown both as the original screenshot and as a TikZ redraw, because the sketch is conceptually important and the screenshot preserves the authentic board layout.
- `lecture_04_figure_03.png` is not a diagram in the usual sense, but it is a useful notation board. It should be preserved as a screenshot only, not redrawn.
- `lecture_04_figure_04.png` is likewise a formula board rather than a diagram. It should be preserved as a screenshot only, with the equations typeset cleanly nearby.
- `lecture_04_figure_05.png` is valuable mainly for board organization: it shows the derivation opening on a fresh right board. It should remain as a screenshot, with no TikZ redraw.
- `lecture_04_figure_06.png` is also chiefly board-layout evidence rather than a standalone figure. It should remain as a screenshot, with the derivation reconstructed in clean display math instead of redrawn as a graphic.

## Reconstruction Guidance
- For `lecture_04_figure_02.png`, keep the screenshot visible and place a small TikZ delta-spike diagram beside it, together with a clean displayed statement of the normalization. The TikZ version should clarify the geometry, but the screenshot should remain the authoritative witness for the chalk placement of the spike, the `y=a` mark, and the nearby integral notation.
- For `lecture_04_figure_03.png` and `lecture_04_figure_04.png`, preserve the screenshots and typeset the equations directly beneath or beside them. These frames are already visually simple, so the main editorial task is normalization of notation rather than redrawing.
- For `lecture_04_figure_05.png`, treat the screenshot as documentary evidence that the time-dependent field expansion has just been introduced, not as a complete transcription. The notes should reconstruct the full equation from the transcript and the later board state.
- For `lecture_04_figure_06.png`, keep the screenshot near a clean multi-line derivation of the time derivative and the resulting Schrödinger-type equation. The prose should acknowledge that the sign is being checked live, because that is part of the lecture’s rhythm and not just an accidental board blemish.
- Across the derivation frames, standardize notation once in the notes: if the chapter uses `a^\dagger` instead of board-style `a^{+}`, or `p` instead of a handwritten `P`, make that editorial choice explicit and then remain consistent.

## Uncertainties
- In `lecture_04_figure_02.png`, the integral sign is clear but the measure `dy` is not visibly written, so `\int dy\,\delta(y-a)` should be treated as cautious completion rather than literal chalk transcription.
- In `lecture_04_figure_03.png` and `lecture_04_figure_04.png`, the handwritten momentum letter can be read as either `P` or `p`; editorial normalization is reasonable, but the pixel evidence is not decisive.
- In `lecture_04_figure_05.png`, only the beginning of the field expansion is actually readable. The operator label, the exact summand, and the time-dependent exponential need transcript-backed reconstruction.
- In `lecture_04_figure_06.png`, the top line is readable in outline but not in every character. The lower lines are partly blocked by Susskind, so they should not be presented as exact visual transcription.
- The board appears to use `a^{+}` notation rather than `a^\dagger`. That difference should be treated as a notation issue, not as a mathematical difference.
- The lecture itself wobbles on the sign in the Schrödinger-equation derivation, so the final displayed equation should follow the settled meaning of the transcript while preserving the fact that the sign is checked and corrected on the board.