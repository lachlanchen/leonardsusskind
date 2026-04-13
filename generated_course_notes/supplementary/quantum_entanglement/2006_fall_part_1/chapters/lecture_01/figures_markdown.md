# Figure Notes
## Image Inventory
- `lecture_01_figure_01.png`: Stanford University title card with the red block `S`, tree emblem, and the text `STANFORD UNIVERSITY` plus `www.stanford.edu`. No lecture board, mathematics, or diagram content is present.
- `lecture_01_figure_02.png`: Blackboard shot from the reversibility discussion. At upper left there is a closed loop-like directed state diagram. At upper right there is a four-state polygonal/diamond-like sketch with arrows and the handwritten label `UNITARITY`. Beneath it is a smaller square-like directed diagram. At lower left there is another small square-like sketch, partly occluded by Susskind.
- `lecture_01_figure_03.png`: Sparse board shot dominated by a tall parenthesized column with four visible entries arranged vertically. Susskind has stepped aside enough that the column-vector sketch is clear, but most earlier left-hand writing is gone.
- `lecture_01_figure_04.png`: Wider board shot from the matrix-algebra section. A central matrix-like grid of small entries is visible, with a secondary vertical array to its right and a parenthesized column vector farther right. Earlier writing and a large curved bracket remain faintly visible on the left board.
- `lecture_01_figure_05.png`: Close-up board shot showing a left-hand \(2\times 2\) matrix labeled with \(m\)-type entries, next to a second object drawn column-by-column with \(n\)-type entries, followed by an equals sign and a right-hand result matrix area. This is the clearest worked board layout for the matrix-by-matrix discussion.

## Blackboard Equations
- `lecture_01_figure_01.png`: no blackboard equations; only the title-card text `\text{Stanford University}` and `\texttt{www.stanford.edu}` are visible. [visible]
- `lecture_01_figure_02.png`: `\text{unitarity}` written beside the upper-right diagram. [visible]
- `lecture_01_figure_02.png`: directed update diagrams for a few four-state systems; these are diagrammatic rather than algebraic, but they correspond to reversible versus non-reversible update rules. [standard reconstruction]
- `lecture_01_figure_03.png`: a parenthesized four-entry column vector,
  \[
  \begin{pmatrix}
  \cdot\\
  \cdot\\
  \cdot\\
  \cdot
  \end{pmatrix}
  \]
  with the individual entries too small to transcribe confidently. [visible]
- `lecture_01_figure_03.png`: a clean companion reconstruction should use the lecture’s generic vector notation
  \[
  \begin{pmatrix}
  A_1\\
  A_2\\
  A_3\\
  A_4
  \end{pmatrix}.
  \]
  [standard reconstruction]
- `lecture_01_figure_04.png`: a central square array of entries, schematically
  \[
  \begin{pmatrix}
  \cdot & \cdot & \cdot & \cdot\\
  \cdot & \cdot & \cdot & \cdot\\
  \cdot & \cdot & \cdot & \cdot\\
  \cdot & \cdot & \cdot & \cdot
  \end{pmatrix},
  \]
  though the individual symbols are not legible enough for literal transcription. [visible]
- `lecture_01_figure_04.png`: a parenthesized column vector at the far right, again with entries too small to read securely. [partially visible]
- `lecture_01_figure_04.png`: the nearby mathematics is the generic action of a matrix on a vector,
  \[
  M\mathbf{v},
  \qquad
  M\begin{pmatrix}
  A_1\\
  A_2\\
  A_3\\
  A_4
  \end{pmatrix}.
  \]
  [standard reconstruction]
- `lecture_01_figure_05.png`: a left \(2\times 2\) matrix
  \[
  \begin{pmatrix}
  m_{11} & m_{12}\\
  m_{21} & m_{22}
  \end{pmatrix}
  \]
  is clearly visible. [visible]
- `lecture_01_figure_05.png`: the next object is drawn as two adjacent columns with \(n\)-type entries, corresponding to
  \[
  \begin{pmatrix}
  n_{11} & n_{12}\\
  n_{21} & n_{22}
  \end{pmatrix},
  \]
  though some subscripts are only partly legible. [partially visible]
- `lecture_01_figure_05.png`: the right-hand side is a result matrix sketched as an output location rather than a fully written formula. [visible]
- `lecture_01_figure_05.png`: the clean mathematical reconstruction should be
  \[
  \begin{pmatrix}
  m_{11} & m_{12}\\
  m_{21} & m_{22}
  \end{pmatrix}
  \begin{pmatrix}
  n_{11} & n_{12}\\
  n_{21} & n_{22}
  \end{pmatrix},
  \]
  with the first product entry given by
  \[
  m_{11}n_{11}+m_{12}n_{21}.
  \]
  [standard reconstruction]

## Diagram And Layout Reading
- `lecture_01_figure_01.png` is not part of the mathematical lecture staging. It is purely a provenance/title frame and should not guide note layout.
- `lecture_01_figure_02.png` is important because it preserves the board as a cluster of logical state-transition diagrams, not spatial pictures. The upper-left closed loop suggests a reversible cyclic update rule. The upper-right sketch, placed next to `unitarity`, is the most visually emphasized object and should be read as the lecturer’s attempt to classify which update patterns are acceptable. The lower sketches look like smaller variants used for comparison.
- `lecture_01_figure_03.png` isolates the column-vector notation after the more discursive board work has been erased. Its value is less in the literal entries than in the board rhythm: the lecture has moved from state diagrams into linear-algebra notation.
- `lecture_01_figure_04.png` preserves the wider board organization of the matrix-algebra segment. The center of gravity is a matrix-like array in the middle, then a vector-like object to the right. This is useful evidence for the lecture’s shift from diagrams of state evolution to linear operations that update vectors.
- `lecture_01_figure_05.png` is the clearest pedagogical layout of the matrix-by-matrix rule. The left matrix is the fixed operator, the middle object is effectively the second matrix read column-by-column, and the right side is the destination where the resulting columns are placed. This board layout matters because Susskind is explicitly explaining matrix multiplication as repeated matrix-times-vector multiplication.

## TeX Reconstruction Plan
- `lecture_01_figure_01.png` should not remain visible in the mathematical notes. If it is preserved anywhere, it belongs only to video provenance or front-matter context, not to the lecture chapter itself.
- `lecture_01_figure_02.png` should remain visible if the chapter includes the discussion of reversible update rules and the classical precursor to unitarity. It should be paired with a small TikZ redraw of the state-transition sketches nearby. The redraw should preserve the board logic rather than the hand-drawn irregularity: a loop, a reversible four-state pattern, and a contrasting nontrivial four-state update sketch.
- `lecture_01_figure_03.png` may remain visible as transitional evidence for the introduction of column-vector notation, but it needs a clean displayed vector next to it. The mathematical content should be reconstructed as a generic four-component column vector, not by over-reading the tiny board entries.
- `lecture_01_figure_04.png` should remain visible if the chapter wants the wider board context for matrix algebra. Nearby, reconstruct a clean displayed matrix acting on a vector, with the matrix and vector typeset legibly. The screenshot supplies layout and staging; the equation should supply the readable mathematics.
- `lecture_01_figure_05.png` should definitely remain visible. It is the strongest screenshot for the matrix-by-matrix rule explained column-by-column. Pair it with a clean \(2\times 2\) matrix product in LaTeX and, if useful, a short displayed line showing that the first output column is obtained by multiplying the left matrix by the first column of the right matrix.
- If space is limited, `lecture_01_figure_05.png` is the better close-up for the matrix-multiplication subsection, while `lecture_01_figure_04.png` is the better wide-context companion.

## Caption Drafts
- `lecture_01_figure_01.png`: Stanford title card
- `lecture_01_figure_02.png`: State-update sketches and unitarity
- `lecture_01_figure_03.png`: Column-vector notation on the board
- `lecture_01_figure_04.png`: Matrix algebra with a column vector
- `lecture_01_figure_05.png`: Multiplying a \(2\times 2\) matrix by matrix columns

## Uncertainties
- `lecture_01_figure_01.png` is visually clear but mathematically irrelevant; it should not be mistaken for usable lecture evidence.
- In `lecture_01_figure_02.png`, the exact arrow directions in the lower two small diagrams are not perfectly crisp, and the handwritten `unitarity` label is legible but rough.
- In `lecture_01_figure_02.png`, the diagrams are clearly about update rules and reversibility, but they are not accompanied by symbolic labels for the states, so any redrawn TikZ should stay schematic unless the transcript later pins down a specific mapping.
- In `lecture_01_figure_03.png`, the actual four entries in the column are too small to read reliably. The image supports “column vector” far better than it supports any exact components.
- In `lecture_01_figure_04.png`, the central matrix-like entries and the far-right vector entries are too small to transcribe literally. The screenshot should be used for board organization, not for exact symbol recovery.
- In `lecture_01_figure_05.png`, the second matrix is drawn in a way that visually emphasizes its columns; this is compatible with the transcript, but the exact subscripts on the \(n\)-entries are not equally sharp in every slot.
- In `lecture_01_figure_05.png`, the right-hand output matrix is only a placeholder sketch in the frame, not a fully written formula, so the notes should reconstruct the actual matrix product cleanly in LaTeX rather than pretending the product entries are visible on the board.