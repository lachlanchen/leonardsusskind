# Visual Evidence
## Frame Inventory
- `lecture_06_figure_03.png`: Whiteboard frame showing the indexed Lorentz-transformation law at the top and the beginning of a column-vector rewriting below; this screenshot should remain in the final notes because it preserves the board transition from index notation to matrix form.
- `lecture_06_figure_05.png`: Whiteboard frame showing rank-two and rank-three tensor notation on the left and a schematic parenthesized \(4\times4\) component grid on the right; this screenshot should remain in the final notes because it captures both the notation and the layout used for component counting.

## Equation Extraction
- `lecture_06_figure_03.png`: \(X'^{\mu} = L^{\mu}{}_{\nu} X^{\nu}\) [partially visible]
- `lecture_06_figure_03.png`: a vertical four-entry component list at the right margin, plausibly \(x,y,z,t\) or \(x^1,x^2,x^3,x^0\) [partially visible]
- `lecture_06_figure_03.png`: \(\begin{pmatrix}x'\\ y'\\ z'\\ t'\end{pmatrix} = L \begin{pmatrix}x\\ y\\ z\\ t\end{pmatrix}\) [standard completion]
- `lecture_06_figure_05.png`: \(A^{\mu}B^{\nu} = \text{2nd rank tensor}\) [visible]
- `lecture_06_figure_05.png`: \(A^{\mu}B^{\nu}C^{\sigma}\) [partially visible]
- `lecture_06_figure_05.png`: a parenthesized \(4\times4\) matrix-style display for tensor components [visible]
- `lecture_06_figure_05.png`: \(T^{\mu\nu}=T^{\nu\mu}\) [standard completion]
- `lecture_06_figure_05.png`: \(\#\{\text{independent components of a symmetric rank-two tensor in four dimensions}\}=10\) [standard completion]

## Diagram Extraction
- `lecture_06_figure_03.png` is not really a diagram frame; its value is the board structure. Preserve it as a screenshot, but do not redraw it in TikZ.
- In `lecture_06_figure_03.png`, the large parenthesis being written below the indexed equation is useful evidence that the lower expression is meant as a column vector. That structural cue should be preserved by keeping the screenshot next to the clean typeset equations.
- `lecture_06_figure_05.png` contains a schematic \(4\times4\) component grid that should be shown both ways: keep the screenshot as evidence, and redraw a clean schematic matrix or TikZ grid for readability.
- The grid in `lecture_06_figure_05.png` is only partially marked, so the redraw should remain schematic. It should emphasize the diagonal and one half of the matrix rather than inventing detailed entries that are not legible in the frame.
- No axes, arrows, or geometric motion sketches are reliably visible in these frames, so the visual evidence here is mainly organizational rather than pictorial.

## Reconstruction Guidance
- For `lecture_06_figure_03.png`, typeset the indexed equation \(X'^{\mu}=L^{\mu}{}_{\nu}X^{\nu}\) cleanly, then typeset the corresponding column-vector form on the next line or in a nearby display. Keep the screenshot adjacent because the image shows the lecture’s actual progression from one notation to the other.
- For `lecture_06_figure_03.png`, treat the lower column-vector equality as a cautious standard completion rather than a direct transcription. The frame supports the direction of the rewrite, but not every symbol is fully visible.
- For `lecture_06_figure_05.png`, typeset the visible tensor-rank examples \(A^{\mu}B^{\nu}\) and \(A^{\mu}B^{\nu}C^{\sigma}\) as clean equations. Use the transcript to supply the symmetric condition and the statement about \(10\) independent components.
- For `lecture_06_figure_05.png`, redraw the \(4\times4\) component layout as a clean schematic matrix or TikZ figure, but keep the screenshot beside it. The redraw is for legibility; the screenshot is the evidence for the original board arrangement.
- For both frames, prefer note-quality typeset equations over trying to reproduce every imperfection of the chalkboard. The screenshot should document lecture rhythm and layout, while the LaTeX should carry the mathematically clean statement.

## Uncertainties
- In `lecture_06_figure_03.png`, the precise placement of indices on \(L\) is partly obscured by Susskind’s body, so \(L^{\mu}{}_{\nu}\) is a cleaned reconstruction rather than a fully visible transcription.
- In `lecture_06_figure_03.png`, the lower column-vector expression is only beginning to be written, not fully shown.
- In `lecture_06_figure_03.png`, the right-edge component labels are cropped and cannot be read with complete confidence.
- In `lecture_06_figure_05.png`, the final letters of “2nd rank tensor” are somewhat soft.
- In `lecture_06_figure_05.png`, the third superscript in the lower product is not perfectly crisp; \(\sigma\) is the most plausible cautious reconstruction.
- In `lecture_06_figure_05.png`, the marked cells inside the grid are too schematic to identify as definite component labels.
- The “10 independent components” statement is not visibly written in the frame and should therefore be treated as transcript-backed standard completion, not image-only evidence.