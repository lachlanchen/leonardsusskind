# Visual Evidence
## Frame Inventory
- `lecture_08_figure_03.png`: A clean board moment showing the conservative-force relation \(F=-\nabla U\) with little other writing; keep this screenshot in the final notes as documentary evidence for the transition from ordinary conservative forces to the electromagnetic case.
- `lecture_08_figure_04.png`: A three-line board summary showing the magnetic field from a vector potential, the electric field from a scalar potential, and the relation \(U=qV\); keep this screenshot because the ordering of the three lines matters for the lecture’s logic.
- `lecture_08_figure_05.png`: A wider board view with the Lorentz-force law at the top and an action-like integral expression below, including a brace that visually groups the terms; keep this screenshot because it preserves the lecture’s board layout at the point where the action is made to look like a Lagrangian integral.
- `lecture_08_figure_06.png`: A local derivation shot in which Susskind points to the kinetic term while discussing differentiation with respect to \(\dot x\); keep this screenshot if the canonical-momentum derivation is retained in full, because the finger placement is the main visual evidence here.

## Equation Extraction
- `lecture_08_figure_03.png`: \(\mathbf{F}=-\nabla U\) [visible]

- `lecture_08_figure_04.png`: \(\mathbf{B}=\nabla\times\mathbf{A}\) [visible]
- `lecture_08_figure_04.png`: \(\mathbf{E}=-\nabla V\) [partially visible]
- `lecture_08_figure_04.png`: \(U=qV\) [visible]

- `lecture_08_figure_05.png`: \(m\ddot{\mathbf{x}}=q\mathbf{E}+q\,\dot{\mathbf{x}}\times\mathbf{B}\) [partially visible]
- `lecture_08_figure_05.png`: \(\int \frac{1}{2}m(\dot{x}^{2}+\dot{y}^{2})\) [visible]
- `lecture_08_figure_05.png`: \(q\int A_i\,dx_i\) [visible]
- `lecture_08_figure_05.png`: \(-V\,dt\) [visible]
- `lecture_08_figure_05.png`: \(S=\int \frac{1}{2}m(\dot{x}^{2}+\dot{y}^{2})\,dt+q\int A_i\,dx_i-q\int V\,dt\) [standard completion]
- `lecture_08_figure_05.png`: \(S=\int\left[\frac{1}{2}m(\dot{x}^{2}+\dot{y}^{2})+qA_i\dot{x}_i-qV\right]dt\) [standard completion]

- `lecture_08_figure_06.png`: \(m\ddot{\mathbf{x}}=q\mathbf{E}+q\,\dot{\mathbf{x}}\times\mathbf{B}\) [partially visible]
- `lecture_08_figure_06.png`: \(\frac{1}{2}m(\dot{x}^{2}+\dot{y}^{2})\) [visible]
- `lecture_08_figure_06.png`: \(q\,\mathbf{A}\cdot\mathbf{v}-V(x)\) [partially visible]
- `lecture_08_figure_06.png`: \(L=\frac{1}{2}m(\dot{x}^{2}+\dot{y}^{2})+q\,\mathbf{A}\cdot\mathbf{v}-qV\) [standard completion]
- `lecture_08_figure_06.png`: \(p_x=\frac{\partial L}{\partial \dot{x}}\) [standard completion]
- `lecture_08_figure_06.png`: \(p_x=m\dot{x}+qA_x\) [standard completion]

## Diagram Extraction
- `lecture_08_figure_03.png` is not a geometric diagram; it is best preserved as a screenshot plus a nearby clean displayed equation.
- `lecture_08_figure_04.png` is not a TikZ figure either; its value is the three-line board structure, so it should remain as a screenshot and be paired with a clean three-relation display in the notes.
- `lecture_08_figure_05.png` contains a meaningful board layout rather than a standalone diagram: top equation, lower action terms, and a right-hand brace showing regrouping. This should be preserved as a screenshot; the mathematics should be typeset cleanly, but no TikZ redraw is necessary.
- `lecture_08_figure_06.png` is a derivation-layout shot, not a figure for TikZ. The important visual fact is the lecturer’s finger marking the \(\dot x\)-dependent term, so this should remain as a screenshot if used at all.
- No independent sketch in these four frames needs to be redrawn in TikZ. They are equation-board moments, not board-drawn geometry.

## Reconstruction Guidance
- Use `lecture_08_figure_03.png` to anchor the prose move from ordinary conservative mechanics into electromagnetism. The note-quality equation should be typeset simply as \(\mathbf{F}=-\nabla U\), while the screenshot remains as evidence for the board moment.
- Use `lecture_08_figure_04.png` as evidence for the lecture’s summary ordering: first \(\mathbf{B}=\nabla\times\mathbf{A}\), then \(\mathbf{E}=-\nabla V\), then \(U=qV\). In the notes, these should appear as a clean aligned display rather than as a photographic transcription.
- Use `lecture_08_figure_05.png` to reconstruct the electromagnetic action in a clean form. The screenshot should stay nearby because the board brace and split-integral layout show the lecture’s “make it look like a Lagrangian” maneuver, but the printed notes should normalize the formula into either the split-integral form or the single-integral Lagrangian form.
- When reconstructing from `lecture_08_figure_05.png` and `lecture_08_figure_06.png`, restore the charge factor on the scalar-potential term. The frames alone are abbreviated, but the lecture logic goes through \(U=qV\), so the clean note-quality formulas should carry \(-qV\), not just \(-V\).
- Use `lecture_08_figure_06.png` as local visual evidence for which term is being differentiated, not as evidence that the full canonical-momentum equation is legible on the board. In the final notes, typeset the cleaned statements
  \[
  L=\frac{1}{2}m(\dot{x}^{2}+\dot{y}^{2})+q\,\mathbf{A}\cdot\mathbf{v}-qV,
  \qquad
  p_x=\frac{\partial L}{\partial \dot{x}}=m\dot{x}+qA_x,
  \]
  and let the screenshot support the derivational rhythm rather than the full algebra.
- Normalize notation across the notes: use bold vectors for \(\mathbf{E}\), \(\mathbf{B}\), \(\mathbf{A}\), and \(\mathbf{v}\), and reserve scalar \(V\) for electric potential so the printed notes do not inherit the board’s velocity/potential ambiguity.

## Uncertainties
- In `lecture_08_figure_04.png`, the middle line is best read as \(\mathbf{E}=-\nabla V\), but the initial symbol is less crisp than the top and bottom lines.
- In `lecture_08_figure_05.png`, the lower expression is visibly split across lines, and the exact placement of the \(dt\) is not fully clear from the frame alone.
- In `lecture_08_figure_05.png`, the top Lorentz-force equation is cropped at the left edge, so the full vector notation must be normalized rather than copied literally from the image.
- In `lecture_08_figure_06.png`, the lower interaction term is only partially legible; the clean forms \(qA_i\dot{x}_i\) and \(q\,\mathbf{A}\cdot\mathbf{v}\) are cautious completions rather than direct full-frame readings.
- In `lecture_08_figure_06.png`, the screenshot does not itself show the completed equation \(p_x=m\dot{x}+qA_x\); that equality should be treated as a standard completion supported by the transcript, not as fully visible board text.