# Figure Notes
## Image Inventory
- `lecture_06_figure_02.png`: A clean board view showing a two-component column vector at left, identified with `\Psi` in the middle, an `\alpha` matrix at upper right, and the matrix-form first-order wave equation across the lower half. A small portion of Susskind and his shadow appear at lower left, but the mathematics is mostly unobstructed.
- `lecture_06_figure_03.png`: A tighter board crop showing two decoupled first-order equations for `\psi_+` and `\psi_-`, with the corresponding frequency statements `\omega=m` and `\omega=-m` written underneath. A cropped boxed reminder of earlier `\psi_L` and `\psi_R` notation remains at the far left edge.
- `lecture_06_figure_04.png`: A wider, more documentary frame with Susskind pointing at the board. The left side still shows the earlier matrix-form equation, while the middle and right preserve a chain of `2\times 2` matrices with entries `0`, `1`, and `-1`. The lecturer partly blocks the center, but the overall board organization is visible.
- `lecture_06_figure_05.png`: A board labeled `V(\phi)` with two potential sketches. At center-right there is a symmetric upward-opening well centered on a vertical axis. At left there is another upward-opening well whose minimum is displaced along the horizontal axis. The lecturer is mostly out of frame, so the diagrams are clear.

## Blackboard Equations
- `lecture_06_figure_02.png`: `\Psi=\begin{pmatrix}\psi_R\\ \psi_L\end{pmatrix}` [partially visible]
- `lecture_06_figure_02.png`: `\alpha=\begin{pmatrix}1&0\\0&-1\end{pmatrix}` [visible]
- `lecture_06_figure_02.png`: `\frac{\partial \Psi}{\partial t}=-\alpha\,\frac{\partial \Psi}{\partial x}` [visible]

- `lecture_06_figure_03.png`: `i\,\dot{\psi}_{+}=m\psi_{+}` [visible]
- `lecture_06_figure_03.png`: `i\,\dot{\psi}_{-}=-m\psi_{-}` [visible]
- `lecture_06_figure_03.png`: `\omega=m` [visible]
- `lecture_06_figure_03.png`: `\omega=-m` [visible]
- `lecture_06_figure_03.png`: `\psi_L,\ \psi_R` inside a boxed side note at the far left [partially visible]

- `lecture_06_figure_04.png`: `\frac{\partial \Psi}{\partial t}=-\alpha\,\frac{\partial \Psi}{\partial x}` [partially visible]
- `lecture_06_figure_04.png`: a horizontal chain of `2\times 2` matrices with entries `0`, `1`, and `-1` [partially visible]
- `lecture_06_figure_04.png`: matrix decomposition of the original two-component equation into left- and right-moving pieces [standard reconstruction]

- `lecture_06_figure_05.png`: `V(\phi)` [visible]
- `lecture_06_figure_05.png`: `\phi=0` or a `0` marking near the horizontal axis under the centered well [partially visible]

## Diagram And Layout Reading
- `lecture_06_figure_02.png` is a notation board. The layout matters: the spinor definition is on the left, the symbol `\Psi` is isolated in the middle, the matrix `\alpha` is written separately at upper right, and the compact matrix equation sits below. It reads as a transition from two separate equations to one column-vector equation.
- `lecture_06_figure_03.png` is a finished equation board rather than a diagram. The two equations are stacked, and the derived frequencies are written directly below them, so the board visually emphasizes the passage from differential equations to the two allowed frequency values.
- `lecture_06_figure_04.png` is mainly useful for board organization. The left side retains the original matrix equation, while the middle and right show matrix products or matrix comparisons spread across the board. Susskind is pointing into the left portion, so the frame records how he is reading the components back into physical left- and right-moving content.
- `lecture_06_figure_05.png` is the one genuinely diagrammatic figure in this set. The label `V(\phi)` sits above two side-by-side potential sketches. The centered well at right has its minimum on the vertical axis; the left sketch places the minimum away from the apparent origin on the horizontal axis. The comparison is clearly about where the minimum of the potential sits.

## TeX Reconstruction Plan
- `lecture_06_figure_02.png` should remain visible in the notes. Pair it with clean displayed equations for the spinor definition, the diagonal `\alpha` matrix, and the compact matrix equation.
- `lecture_06_figure_03.png` should remain visible. Typeset the two decoupled equations and the two frequency statements cleanly nearby rather than asking the reader to read them from the chalk alone.
- `lecture_06_figure_04.png` should remain visible as documentary board-layout evidence, but the matrix algebra should be reconstructed in clean LaTeX from the transcript and neighboring clearer boards. The screenshot is valuable for showing how the board was spatially organized during the conceptual explanation, not for exact symbol-by-symbol transcription.
- `lecture_06_figure_05.png` must remain visible and should be paired with a TikZ redraw. The redraw should preserve the comparison of candidate minima: one well centered at the origin and one with a displaced minimum. The screenshot should stay nearby because it records the actual board moment and the side-by-side comparison under the `V(\phi)` label.

## Caption Drafts
- `lecture_06_figure_02.png`: Spinor column vector and alpha matrix
- `lecture_06_figure_03.png`: Decoupled `\psi_\pm` equations and `\omega=\pm m`
- `lecture_06_figure_04.png`: Matrix layout for left- and right-moving components
- `lecture_06_figure_05.png`: Potential `V(\phi)` and candidate minima

## Uncertainties
- In `lecture_06_figure_02.png`, the left column-vector entries are slightly shadowed and cropped at the extreme left; they are best read as `\psi_R` and `\psi_L`, but the exact chalk shape is not perfectly crisp.
- In `lecture_06_figure_03.png`, the boxed notation at the far left edge is cropped and should not control the final notation; the main equations and `\omega=\pm m` are the reliable content.
- In `lecture_06_figure_04.png`, the exact entries of the matrices across the center and right are not fully trustworthy from the pixels alone because Susskind partly blocks them. This frame should therefore support layout and intent, not exact transcription.
- In `lecture_06_figure_05.png`, the left potential sketch is partially cut off at the far left, so one should not over-interpret it as a fully visible double-well from the image alone. What is directly visible is a comparison between a centered minimum and a displaced minimum.
- Also in `lecture_06_figure_05.png`, the small axis markings near the minima are faint; any explicit `\phi=0` labeling in the final notes should be treated as transcript-supported clarification rather than purely pixel-legible chalk.