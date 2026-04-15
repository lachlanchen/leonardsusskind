# Visual Evidence
## Frame Inventory
- `lecture_09_figure_02.png`: Shows the \(x\)-component of a cross product together with a hand-drawn \(3\times 3\) antisymmetric-matrix sketch; this screenshot should remain in the final notes.
- `lecture_09_figure_03.png`: Shows the defining curl relation for the magnetic field and a gauge-shift equation for the vector potential on a sparse board; this screenshot should remain in the final notes.
- `lecture_09_figure_05.png`: Shows Susskind writing the action as an integral, with the action symbol at left, the integral sign in the middle, and \(dt\) at the far right; this screenshot should remain in the final notes.

## Equation Extraction
- `lecture_09_figure_02.png`: \((\mathbf V \times \mathbf A)_x\) [visible]
- `lecture_09_figure_02.png`: \(V_yA_z - V_zA_y\) [visible]
- `lecture_09_figure_02.png`: \(M_{ij}=-M_{ji}\) [standard completion]
- `lecture_09_figure_02.png`: \(M \sim \begin{pmatrix}0 & * & *\\ -* & 0 & *\\ -* & -* & 0\end{pmatrix}\) [standard completion]

- `lecture_09_figure_03.png`: \(\vec B=\nabla\times\vec A\) [visible]
- `lecture_09_figure_03.png`: \(\vec A+\nabla s=\vec A'\) [visible]

- `lecture_09_figure_05.png`: \(A=\int \cdots\,dt\) [partially visible]
- `lecture_09_figure_05.png`: \(A=\int L\,dt\) [standard completion]

## Diagram Extraction
- `lecture_09_figure_02.png`: The important visual object is the hand-drawn antisymmetric \(3\times 3\) array with zeros on the diagonal and opposite off-diagonal entries. It should be preserved as a screenshot and also rendered cleanly in note-quality mathematics, but not as a literal TikZ copy of the doodled cells.
- `lecture_09_figure_03.png`: There is no real diagram here; the value is the two-line board structure pairing \(\vec B=\nabla\times\vec A\) with the gauge transformation. Keep the screenshot; no TikZ redraw is needed.
- `lecture_09_figure_05.png`: There is no geometric figure, only the staged layout of the action formula across the board. Keep the screenshot and pair it with a clean displayed equation; no TikZ redraw is needed.

## Reconstruction Guidance
- For `lecture_09_figure_02.png`, regularize the handwriting into clean vector notation and typeset
  \[
  (\mathbf V\times\mathbf A)_x = V_yA_z - V_zA_y.
  \]
  Then express the matrix idea formally as an antisymmetric tensor or matrix with zero diagonal. Keep the screenshot nearby because it records Susskind’s board-level way of counting independent components.
- For `lecture_09_figure_03.png`, typeset the two equations exactly as the conceptual pair they are:
  \[
  \vec B=\nabla\times\vec A,
  \qquad
  \vec A'=\vec A+\nabla s.
  \]
  The screenshot should stay visible because the sparse board layout itself helps convey that the lecture is pausing to isolate the ambiguity of \(\vec A\).
- For `lecture_09_figure_05.png`, do not infer the integrand from the pixels alone. Use the transcript-backed completion \(A=\int L\,dt\), or normalize later to \(S=\int L\,dt\) in the finished notes while briefly noting that the board at this moment uses \(A\) for the action. Keep the screenshot because it captures the live construction of the formula, not just its final cleaned form.
- None of these frames require an aggressive visual reconstruction. The right workflow is screenshot plus clean typeset equation, not screenshot replacement.

## Uncertainties
- In `lecture_09_figure_02.png`, the off-diagonal matrix entries are not fully literal algebraic symbols; some cells contain quick mnemonic marks or doodles rather than reliably readable formulas.
- In `lecture_09_figure_02.png`, the handwritten vector letters are most plausibly \(V\) and \(A\), but the exact pen strokes are rough enough that they should be regularized in typesetting.
- In `lecture_09_figure_03.png`, the prime on \(\vec A'\) is handwritten and slightly cramped; the mathematically clean form can be written either as \(\vec A+\nabla s=\vec A'\) or \(\vec A'=\vec A+\nabla s\).
- In `lecture_09_figure_05.png`, the symbol between the action letter and the integral looks like a hurried equals sign or colon, and the integrand itself is not legible from the frame.
- In `lecture_09_figure_05.png`, only the left action symbol, the integral sign, and the \(dt\) are visually secure; the completion to \(A=\int L\,dt\) comes from cautious reconstruction, not direct legibility.