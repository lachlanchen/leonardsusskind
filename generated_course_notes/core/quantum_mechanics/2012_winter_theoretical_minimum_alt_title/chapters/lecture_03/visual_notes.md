# Visual Evidence
## Frame Inventory
- `lecture_03_figure_02.png`: A clean board-only frame showing the operator equation, its projection onto \(\langle i|\), and the component rewrite ending in \(\sum_j m_{ij}\alpha_j=\beta_i\); this screenshot should remain in the final notes.
- `lecture_03_figure_03.png`: A wider board state showing the same operator action rewritten as an explicit matrix multiplying an \(\alpha\)-column to produce a \(\beta\)-column, with the lecturer partly in frame but not blocking the main structure; this screenshot should remain in the final notes.

## Equation Extraction
- `lecture_03_figure_02.png`: \(M|A\rangle = |B\rangle\) `[visible]`
- `lecture_03_figure_02.png`: \(\langle i|M|A\rangle = \langle i|B\rangle = \beta_i\) `[visible]`
- `lecture_03_figure_02.png`: \(\sum_j \langle i|M|j\rangle \langle j|A\rangle = \langle i|M|j\rangle\,\alpha_j = \beta_i\) `[partially visible]`
- `lecture_03_figure_02.png`: \(\sum_j m_{ij}\alpha_j=\beta_i\) `[visible]`
- `lecture_03_figure_02.png`: \(m_{ij}=\langle i|M|j\rangle\) `[standard completion]`
- `lecture_03_figure_03.png`: \(\begin{pmatrix} M_{11} & M_{12} & M_{13} & \cdots \\ M_{21} & M_{22} & \cdots & \cdots \\ \vdots & & & \\ \cdots & & & \end{pmatrix}\begin{pmatrix} \alpha_1 \\ \alpha_2 \\ \vdots \\ \alpha_N \end{pmatrix}=\begin{pmatrix} \beta_1 \\ \beta_2 \\ \vdots \\ \beta_N \end{pmatrix}\) `[partially visible]`
- `lecture_03_figure_03.png`: The lower-left cropped remnant appears to continue the component equation, likely ending with \(\alpha_j=\beta_i\) or \(\sum_j m_{ij}\alpha_j=\beta_i\), but it is not fully readable and should not be treated as a fresh primary equation `[partially visible]`

## Diagram Extraction
- `lecture_03_figure_02.png` contains no geometric diagram, but it does preserve a meaningful board layout: top line abstract operator equation, second line projected equation, third line inserted-basis step, bottom line indexed component formula. This should be preserved as a screenshot and also re-typeset as clean displayed equations.
- `lecture_03_figure_03.png` likewise contains no geometric sketch, but it preserves a strong computational layout: square matrix on the left, input coefficient column in the middle, equality sign, output coefficient column on the right. This should be preserved as a screenshot and also re-typeset as a clean matrix equation.
- No TikZ redraw is required for either accepted frame. The visual evidence here is board sequencing and notation layout, not a figure that benefits from vector redrawing.

## Reconstruction Guidance
- Use `lecture_03_figure_02.png` as visual evidence for the transition from the abstract operator statement \(M|A\rangle=|B\rangle\) to the component equation \(\sum_j m_{ij}\alpha_j=\beta_i\). In the notes, re-typeset this as a short aligned derivation, but keep the screenshot nearby because it documents the lecture’s actual blackboard progression.
- Use `lecture_03_figure_03.png` as visual evidence for the final packaging of the same relation as matrix multiplication. In the notes, re-typeset the matrix equation with a standard matrix environment rather than trying to imitate the handwriting exactly.
- Treat \(m_{ij}=\langle i|M|j\rangle\) as a cautious standard completion rather than as a fully legible board transcription. It is justified by the visible equations and the transcript, but it should not be presented as though the entire definition is perfectly readable in the frame itself.
- Preserve the board order in prose: abstract operator action, projection onto a basis vector, insertion of a complete set, definition of matrix elements, indexed component equation, then matrix-times-column-vector form.
- Do not promote the cropped lower-left writing in `lecture_03_figure_03.png` into an independent equation block. It is only a leftover fragment from the earlier derivation.
- Neither frame needs a separate diagram environment. Standard displayed equations plus the original screenshots are the right note-writing treatment.

## Uncertainties
- In `lecture_03_figure_02.png`, the long middle line is not perfectly crisp after the first equality; the intended structure is clear, but the exact placement of the summation and the factor \(\langle j|A\rangle\) is not fully sharp.
- In `lecture_03_figure_02.png`, the handwritten symbol that looks like \(m_{ij}\) could visually blur with \(M_{ij}\). The lecture context strongly indicates matrix elements, but the handwriting does not enforce a strict typographic distinction.
- In `lecture_03_figure_03.png`, several lower-row matrix entries are blocked by the lecturer or left as dots, so only the general matrix pattern is secure, not every individual entry.
- In `lecture_03_figure_03.png`, the final index on the columns appears as \(N\) rather than \(n\), but this is just the visible handwriting convention in the frame; the notes should follow the lecture’s surrounding notation consistently.
- The lower-left cropped text in `lecture_03_figure_03.png` is too incomplete to quote reliably.
- The frames support the operator-to-matrix passage very well, but they do not independently certify any later Hermitian-conjugation or eigenvalue material; those later steps should come from the transcript, not be inferred from these images.