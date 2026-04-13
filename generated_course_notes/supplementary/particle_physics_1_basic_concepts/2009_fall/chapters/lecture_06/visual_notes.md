# Visual Evidence
## Frame Inventory
- `lecture_06_figure_02.png`: Shows the transition to two-component matrix notation, with a column spinor at left, the symbol `\Psi` in the middle, the matrix `\alpha` at upper right, and the compact wave equation below; this screenshot should remain in the final notes.
- `lecture_06_figure_03.png`: Shows the decoupled rest-frame equations for `\psi_+` and `\psi_-` together with `\omega=\pm m`; this screenshot should remain in the final notes.
- `lecture_06_figure_04.png`: Shows Susskind pointing at a wider board where the earlier matrix equation sits at left and a more spread-out matrix layout occupies the center and right; this screenshot should remain in the final notes as documentary board-layout evidence.
- `lecture_06_figure_05.png`: Shows the label `V(\phi)` and two side-by-side potential sketches, one centered and one with a displaced minimum; this screenshot should remain in the final notes and be paired with a redraw.

## Equation Extraction
- `lecture_06_figure_02.png`: `\Psi=\begin{pmatrix}\psi_R\\ \psi_L\end{pmatrix}` [partially visible]
- `lecture_06_figure_02.png`: `\alpha=\begin{pmatrix}1&0\\0&-1\end{pmatrix}` [visible]
- `lecture_06_figure_02.png`: `\frac{\partial \Psi}{\partial t}=-\alpha\,\frac{\partial \Psi}{\partial x}` [visible]

- `lecture_06_figure_03.png`: `i\,\dot{\psi}_{+}=m\psi_{+}` [visible]
- `lecture_06_figure_03.png`: `i\,\dot{\psi}_{-}=-m\psi_{-}` [visible]
- `lecture_06_figure_03.png`: `\omega=m` [visible]
- `lecture_06_figure_03.png`: `\omega=-m` [visible]
- `lecture_06_figure_03.png`: `\psi_L,\ \psi_R` in a boxed side reminder at the far left [partially visible]
- `lecture_06_figure_03.png`: `\psi_\pm=\psi_R\pm\psi_L` [standard completion]

- `lecture_06_figure_04.png`: `\frac{\partial \Psi}{\partial t}=-\alpha\,\frac{\partial \Psi}{\partial x}` [partially visible]
- `lecture_06_figure_04.png`: a chain of `2\times2` matrices with entries `0`, `1`, and `-1` is present, but not legible enough for exact entry-by-entry transcription [partially visible]
- `lecture_06_figure_04.png`: matrix decomposition of the two-component equation into left- and right-moving pieces [standard completion]

- `lecture_06_figure_05.png`: `V(\phi)` [visible]
- `lecture_06_figure_05.png`: `0` or `\phi=0` marked near the horizontal axis beneath the centered well [partially visible]

## Diagram Extraction
- `lecture_06_figure_02.png` is not a diagram in the TikZ sense; its value is the board layout of the notation change. Keep it as a screenshot and pair it with clean typeset equations rather than redrawing the board.
- `lecture_06_figure_03.png` is also not a diagram but a finished equation board. Keep it as a screenshot because the stacked layout of the two equations and the two frequencies is part of the visual logic of the lecture.
- `lecture_06_figure_04.png` should be preserved as a screenshot only. It records how Susskind spatially organized the decomposition and pointed back to the original equation, but it is too occluded to justify an exact visual redraw.
- `lecture_06_figure_05.png` is the one frame that should be shown both ways. Keep the screenshot and also redraw the potential sketches in TikZ as a clean comparison between a centered minimum and a displaced minimum.

## Reconstruction Guidance
- For `lecture_06_figure_02.png`, use the screenshot as evidence for the notational pivot, then typeset the spinor definition, the diagonal `\alpha` matrix, and the compact matrix equation cleanly in display math. The screenshot matters because it shows the board organization of that shift from two equations to one column-vector equation.
- For `lecture_06_figure_03.png`, keep the screenshot nearby, but do not make the reader rely on chalk legibility. Typeset the two decoupled equations and the frequency statements cleanly, and use the transcript to justify the standard completion `\psi_\pm=\psi_R\pm\psi_L`.
- For `lecture_06_figure_04.png`, use the image only to support board structure and interpretive placement. Reconstruct the actual mathematics from the transcript and neighboring clearer frames, not from the obstructed matrix chain itself.
- For `lecture_06_figure_05.png`, redraw the visible comparison in TikZ with smooth clean curves and explicit axis labels, but keep the screenshot adjacent because it is the direct evidence for the lecturer’s board sketch and the label `V(\phi)`. The redraw should stay modest and faithful to the frame rather than expanding into a more elaborate textbook potential than the image supports.
- When a formula is only partly readable, prefer a cautious standard completion that is already demanded by the surrounding visible material and transcript, rather than inventing extra intermediate steps.

## Uncertainties
- In `lecture_06_figure_02.png`, the left entries of the column vector are partly cropped and shadowed; `\psi_R` and `\psi_L` are the best reading, but the chalk is not perfectly sharp.
- In `lecture_06_figure_03.png`, the boxed side note at the far left is incomplete and should not control the final notation. The reliable content is the pair of `\psi_\pm` equations and the two frequency lines.
- In `lecture_06_figure_04.png`, the exact center-right matrix entries are not reliably readable because Susskind blocks part of the board. This frame should not be used for exact symbol-by-symbol transcription.
- In `lecture_06_figure_05.png`, the left sketch is cut off enough that one should not claim more than a displaced minimum from the pixels alone. If the final notes discuss symmetry-breaking minima more fully, that extra structure should come from the transcript, not from over-reading the frame.
- Also in `lecture_06_figure_05.png`, the small axis mark near the centered well is faint. Any explicit `\phi=0` labeling in the final notes should be treated as cautious clarification rather than hard pixel certainty.