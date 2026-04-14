# Visual Evidence
## Frame Inventory
- `lecture_07_figure_02.png`: Susskind stands in front of a partly occluded board; the visible left-hand worldsheet-action term shows a squared \(\tau\)-derivative of \(X^\mu\), a minus sign, and the beginning of the matching \(\sigma\)-derivative term, so the screenshot should remain in the final notes as partial equation evidence.
- `lecture_07_figure_03.png`: An unobstructed board shows a plus-sign second-order PDE at the top and a long subdivided horizontal line below, and this screenshot should remain because it clearly captures both the equation and the first discrete geometric sketch.
- `lecture_07_figure_04.png`: The same board state has been developed into a fuller derivation, with the PDE, a numbered discrete line, a small square lattice, and a finite-difference expression, so this screenshot should remain as one of the strongest pieces of direct mathematical evidence.
- `lecture_07_figure_06.png`: Two vertically stacked interaction-like sketches are visible, one with a short horizontal wavy connector and one with a short vertical wavy connector, and the screenshot should remain because the paired layout itself is the point of the argument.

## Equation Extraction
- `lecture_07_figure_02.png`: \(\left(\frac{\partial X^\mu}{\partial \tau}\right)^2\) [visible]
- `lecture_07_figure_02.png`: \(-\left(\cdots\right)^2\) [partially visible]
- `lecture_07_figure_02.png`: \(\left(\frac{\partial X^\mu}{\partial \tau}\right)^2-\left(\frac{\partial X^\mu}{\partial \sigma}\right)^2\) [standard completion]
- `lecture_07_figure_02.png`: \(\int d\tau\,d\sigma \left[\left(\frac{\partial X^\mu}{\partial \tau}\right)^2-\left(\frac{\partial X^\mu}{\partial \sigma}\right)^2\right]\) [standard completion]

- `lecture_07_figure_03.png`: \(\frac{\partial^2 X}{\partial \tau^2}+\frac{\partial^2 X}{\partial \sigma^2}=0\) [visible]

- `lecture_07_figure_04.png`: \(\frac{\partial^2 X}{\partial \tau^2}+\frac{\partial^2 X}{\partial \sigma^2}=0\) [visible]
- `lecture_07_figure_04.png`: \(\bigl[X(3)-X(2)\bigr]-\bigl[X(2)-X(1)\bigr]\) [partially visible]
- `lecture_07_figure_04.png`: \(X(3)+X(1)-2X(2)\) [visible]
- `lecture_07_figure_04.png`: \(1,\ 2,\ 3\) [visible]

- `lecture_07_figure_06.png`: no legible algebraic notation is visible; the content is diagrammatic.

## Diagram Extraction
- `lecture_07_figure_02.png`: This is not a TikZ-style diagram frame so much as a blocked action-density board state. It should be preserved primarily as a screenshot, with the cleaned mathematics typeset nearby rather than redrawn from the image itself.
- `lecture_07_figure_03.png`: The lower horizontal line with evenly spaced short marks should be redrawn in TikZ as a discretized one-dimensional axis or interval, while the screenshot remains visible as board-layout evidence. The equation above it should be kept both as screenshot evidence and as a clean displayed formula.
- `lecture_07_figure_04.png`: Three visual objects matter here and should be redrawn in TikZ: the numbered subdivided line, the small square lattice patch, and the bracketed finite-difference layout if desired. This frame is strong enough that the screenshot and the redraw should appear together.
- `lecture_07_figure_06.png`: The upper and lower paired sketches should be redrawn in TikZ as a clean comparison figure, but the screenshot should stay nearby because the lecture’s point depends on their stacked board arrangement and relative orientation.
- `lecture_07_figure_06.png`: No labels, arrows, or momenta are visible in the frame, so any redraw should remain geometrically minimal unless labels are introduced later from transcript-backed prose.

## Reconstruction Guidance
- Use `lecture_07_figure_02.png` to support the claim that the worldsheet action density visibly contains a \(\tau\)-derivative term opposed by a \(\sigma\)-derivative term. Do not let the screenshot determine prefactors, measures, or the full extent of the formula; typeset a stabilized action separately.
- Use `lecture_07_figure_03.png` to introduce the Euclideanized equation of motion in the form actually shown on the board, with the visible plus sign. Place a clean displayed equation beside the screenshot and add a simple TikZ discrete line below or beside it so the reader sees the geometric turn that the lecture is making.
- Use `lecture_07_figure_04.png` for the discrete finite-difference explanation. The right-hand board expression should be typeset in cleaned form, and the notes can extend it to the two-dimensional discrete Laplacian relation in prose or display, but only after making clear which part is directly visible and which part is the natural continuation.
- Use `lecture_07_figure_06.png` as visual evidence for the symmetry argument, not for any precise notation. A clean paired TikZ redraw should preserve the upper horizontal wavy bridge and the lower vertical wavy bridge, because the contrast of orientations is the actual content being pointed to.
- Where the frame only partially shows the mathematics, prefer a nearby clean displayed equation rather than forcing the reader to infer too much from the screenshot. Where the frame clearly shows board layout or the sequencing of ideas, keep the screenshot visible even if a redraw is added.

## Uncertainties
- In `lecture_07_figure_02.png`, the far-left measure factor is cropped and the second squared term is mostly hidden by the lecturer, so the full action cannot be read directly from the image.
- In `lecture_07_figure_02.png`, the board may contain more of the action than is visible, but the screenshot does not securely fix the integration limits, overall coefficients, or index contractions.
- In `lecture_07_figure_03.png` and `lecture_07_figure_04.png`, the handwritten field symbol looks like \(X\), but the capitalization is not perfectly stable by eye; the notes should standardize the symbol once the context is explained.
- In `lecture_07_figure_03.png` and `lecture_07_figure_04.png`, the visible PDE uses a plus sign, so any switch to the Lorentzian wave equation with a minus sign must be explicitly motivated as a change of context rather than silently substituted.
- In `lecture_07_figure_04.png`, the rightmost bracket is cut off at the image edge, so the second finite-difference bracket is only partly visible and must be completed cautiously.
- In `lecture_07_figure_04.png`, the small lattice sketch is informal and unlabeled; the interpretation as a discrete \((\tau,\sigma)\)-grid comes from the lecture context rather than from explicit axis labels in the frame.
- In `lecture_07_figure_06.png`, the two sketches have no visible momentum labels or channel labels, so they should not be overinterpreted from the image alone.
- None of these four frames directly show the later disc with four boundary insertion points, so any such figure in the final notes would be a transcript-backed reconstruction, not a frame-backed transcription.