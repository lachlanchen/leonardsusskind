# Visual Evidence
## Frame Inventory

- `lecture_06_figure_02.png` shows a tiny horizontal bidirectional polarization mark near the upper left of an otherwise blank board; this screenshot should remain in the final notes because it preserves Susskind’s notation choice that the polarization axis has no preferred left-right direction.
- `lecture_06_figure_03.png` shows the orthogonality statement \(\langle x|y\rangle=0\) and a diagonal \(2\times 2\) matrix acting on \(\begin{pmatrix}1\\0\end{pmatrix}\); this screenshot should remain in the final notes because it captures both the equations and the board layout of the operator check.
- `lecture_06_figure_04.png` shows a long horizontal baseline with two separated smooth peaks above it; this screenshot should remain in the final notes because it is the visual evidence for the symmetric two-lump wavefunction example in the expectation-value discussion.

## Equation Extraction

- `lecture_06_figure_02.png`: \(\leftrightarrow\) [visible]
- `lecture_06_figure_02.png`: horizontal bidirectional polarization-axis mark, used as notation rather than a signed vector arrow [standard completion]

- `lecture_06_figure_03.png`: \(\langle x|y\rangle = 0\) [visible]
- `lecture_06_figure_03.png`: \(\begin{pmatrix}1 & 0\\ 0 & -1\end{pmatrix}\begin{pmatrix}1\\0\end{pmatrix}\) [visible]
- `lecture_06_figure_03.png`: \(\begin{pmatrix}1 & 0\\ 0 & -1\end{pmatrix}\begin{pmatrix}1\\0\end{pmatrix}=\begin{pmatrix}1\\0\end{pmatrix}\) [standard completion]
- `lecture_06_figure_03.png`: \(P_{xy}=\begin{pmatrix}1 & 0\\ 0 & -1\end{pmatrix}\) if the nearby prose explicitly identifies the observable [standard completion]

- `lecture_06_figure_04.png`: no symbolic equation is visible in the frame; the content is purely schematic [visible]
- `lecture_06_figure_04.png`: symmetric two-lump wavefunction profile over a horizontal baseline [standard completion]

## Diagram Extraction

- `lecture_06_figure_02.png` should be shown both ways: keep the screenshot and also redraw the mark in TikZ as a very small horizontal bidirectional axis symbol. The point of the figure is not a full diagram but a convention about how polarization is marked on the page.
- `lecture_06_figure_03.png` is not really a diagram to redraw in TikZ; it should be preserved as a screenshot and accompanied by clean typeset equations. What matters visually is the board structure: orthogonality is written off to the upper left, while the matrix-vector action occupies the central field.
- `lecture_06_figure_04.png` should be shown both ways: keep the screenshot and also redraw it in TikZ as a schematic two-peaked wavefunction on a horizontal baseline. The redraw should preserve the broad geometry of the two separated lobes and the low central region, without inventing labels absent from the frame.

## Reconstruction Guidance

- For `lecture_06_figure_02.png`, keep the screenshot near the sentence explaining that horizontal polarization is not “to the right” versus “to the left.” The TikZ redraw should stay minimal and notation-focused, since the frame is evidentiary rather than mathematically rich.
- For `lecture_06_figure_03.png`, typeset the visible \(\langle x|y\rangle=0\) exactly as written and place the cleaned matrix action nearby as a displayed equation. It is reasonable to complete the multiplication by writing the output vector, but only if the surrounding prose makes clear that this is the standard continuation of the visible step rather than a direct transcription of the frame.
- For `lecture_06_figure_03.png`, preserve the screenshot even if the equations are typeset cleanly, because the image documents how Susskind separated the orthogonality remark from the operator calculation on the board.
- For `lecture_06_figure_04.png`, do not extract algebra from the bitmap itself. Use the screenshot and TikZ redraw only to preserve the shape of the example; any statements about symmetry, \(\langle x\rangle=0\), or labels such as \(x=0\) or \(\pm x_0\) should come from the transcript, not from the image.
- For all three frames, use the transcript only to disambiguate meaning or complete an immediately adjacent standard step. Do not backfill extra textbook detail into the figures beyond what the lecture is actually motivating.

## Uncertainties

- In `lecture_06_figure_02.png`, the chalk mark is very small, so the arrowheads are visible but not perfectly crisp. The fact that it is bidirectional is secure; tiny endpoint details are not.
- In `lecture_06_figure_02.png`, there is no written label attached to the symbol, so its interpretation as polarization notation depends on the nearby lecture context.
- In `lecture_06_figure_03.png`, the equality to the resulting column vector is not written in the visible frame. That final step is a safe mathematical completion, but it is not directly visible.
- In `lecture_06_figure_03.png`, faint erased marks remain on the board behind the active writing. They do not appear to belong to the current derivation and should not be reconstructed.
- In `lecture_06_figure_04.png`, no axis labels, coordinate marks, or symbols are visible. Any later labeling must be introduced from the transcript or omitted.
- In `lecture_06_figure_04.png`, a few stray chalk marks lower on the board appear unrelated to the main wavefunction sketch and should be ignored.