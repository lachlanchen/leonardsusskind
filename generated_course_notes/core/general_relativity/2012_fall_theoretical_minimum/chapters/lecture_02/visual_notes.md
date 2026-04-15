# Visual Evidence
## Frame Inventory
- `lecture_02_figure_02.png`: A sparse board showing the componentwise subtraction of two like-indexed tensors and the resulting \((T-S)\) object; this screenshot should remain in the final notes as documentary evidence for the tensor-equation discussion.
- `lecture_02_figure_03.png`: A metric-transformation board with the line element, partial substitutions for \(dx^m,dx^n\), a small box around the primed metric term, and a larger box around the Jacobian-transformed expression; this screenshot should remain because the boxed board layout is part of the argument.
- `lecture_02_figure_06.png`: A later board state combining the top-line metric transformation, the inverse-metric identity at left, and a \(2\times2\) matrix example below; this screenshot should remain because it captures how Susskind ties symmetry, inverse matrix, and metric notation together.

## Equation Extraction
- `lecture_02_figure_02.png` [visible] \(T^{m\cdots}{}_{\cdots p} - S^{m\cdots}{}_{\cdots p} = (T-S)^{m\cdots}{}_{\cdots p}\)
- `lecture_02_figure_03.png` [visible] \(g_{mn}(x)\,dx^m dx^n = g'_{pq}(y)\,dy^p dy^q\)
- `lecture_02_figure_03.png` [visible] \(g'_{pq}(y)\,dy^p dy^q = \left[g_{mn}(x)\,\frac{\partial x^m}{\partial y^p}\,\frac{\partial x^n}{\partial y^q}\right]dy^p dy^q\)
- `lecture_02_figure_03.png` [partially visible] \(dx^m = \frac{\partial x^m}{\partial y^p}\,dy^p\)
- `lecture_02_figure_03.png` [partially visible] \(dx^n = \frac{\partial x^n}{\partial y^q}\,dy^q\)
- `lecture_02_figure_06.png` [partially visible] \(g_{mn}(x)\,dx^m dx^n = g'_{pq}(y)\,dy^p dy^q = \left[g_{mn}(x)\,\frac{\partial x^m}{\partial y^p}\,\frac{\partial x^n}{\partial y^q}\right]dy^p dy^q\)
- `lecture_02_figure_06.png` [partially visible] \(g_{mn}\,g^{np} = \delta_m{}^{p}\)
- `lecture_02_figure_06.png` [visible] \(\begin{pmatrix} g_{11} & g_{12} \\ g_{21} & g_{22} \end{pmatrix}\begin{pmatrix} g^{11} & g^{12} \\ g^{21} & g^{22} \end{pmatrix} = \)
- `lecture_02_figure_06.png` [standard completion] \(g'_{pq}(y)=g_{mn}(x)\,\frac{\partial x^m}{\partial y^p}\,\frac{\partial x^n}{\partial y^q}\)
- `lecture_02_figure_06.png` [standard completion] \(g_{mn}=g_{nm}\)

## Diagram Extraction
- `lecture_02_figure_02.png`: This is not a true diagram frame; preserve it as a screenshot only, because its value is the board’s reduction of tensor equality to the zero-tensor statement \(T-S=0\).
- `lecture_02_figure_03.png`: The important “diagram” is really board organization, with a small box around \(g'_{pq}(y)\) and a larger box around the transformed coefficient; this should be shown both ways, with the screenshot preserved and the mathematics typeset cleanly nearby, but no TikZ redraw is necessary.
- `lecture_02_figure_03.png`: Susskind’s pointing gesture toward \(g_{mn}(x)\) inside the large box is visually meaningful and is best preserved by keeping the screenshot rather than replacing it with a pure typeset equation.
- `lecture_02_figure_06.png`: The useful visual structure is the three-part board layout: top transformation law, left inverse identity, lower matrix product; this should also be shown both ways, with the screenshot kept and the matrix relation typeset cleanly nearby.
- Across all three frames, there are no axes, geometric sketches, or freehand figures that need TikZ reconstruction; the surviving evidence is equation layout, boxing, and matrix arrangement.

## Reconstruction Guidance
- Use `lecture_02_figure_02.png` as evidence for the claim that subtraction of like-indexed tensors produces another tensor of the same type. In the notes, typeset the equation cleanly and keep the screenshot adjacent, but preserve the generic ellipsis structure rather than inventing missing indices.
- For `lecture_02_figure_03.png`, reconstruct the metric-transformation step in clean LaTeX as a displayed equation, using the screenshot to justify the boxed identification of the transformed coefficient with the primed metric tensor.
- Treat the left-side substitution lines in `lecture_02_figure_03.png` as partial evidence only. Their clean note version should be supplied in canonical form, but the prose should make clear that the frame mainly supports the structure of the transformation, not every chalk mark.
- For `lecture_02_figure_06.png`, do not try to mimic the chalkboard literally. Typeset the inverse-metric identity \(g_{mn}g^{np}=\delta_m{}^{p}\) and the \(2\times2\) matrix example in standard LaTeX, while keeping the screenshot nearby to preserve the board’s sequencing and emphasis.
- Use the screenshots as evidence of what Susskind chose to isolate and emphasize, especially the boxed terms and the matrix layout. Use clean LaTeX for the final equations; do not let chalk spacing or occluded symbols dictate the final notation.
- Avoid over-reconstructing derivational steps that the frames do not fully show. The transcript can support cautious completion, but the notes should distinguish between board-visible content and canonically completed notation.

## Uncertainties
- In `lecture_02_figure_02.png`, the omitted index pattern is only indicated by ellipses. The rank and exact placement of all suppressed indices are not recoverable from the frame alone.
- In `lecture_02_figure_03.png`, the auxiliary formulas for \(dx^m\) and \(dx^n\) are only partially visible; the trailing \(dy^p\) and \(dy^q\) factors are a cautious standard completion rather than fully legible chalk.
- In `lecture_02_figure_03.png` and `lecture_02_figure_06.png`, the board boxes mark conceptual grouping, but their exact geometry should not be treated as notation.
- In `lecture_02_figure_06.png`, the left inverse-metric identity is partly cramped and visually weighted toward the boxed \(g^{np}\); the safest clean reconstruction is \(g_{mn}g^{np}=\delta_m{}^{p}\).
- In `lecture_02_figure_06.png`, the lower matrix product is unfinished on the board. The two matrices are clear, but the resulting matrix or component equations are not fully written out in the frame.
- The frame subtitle “And that’s why the matrix is going to be symmetric” should not be taken as a complete proof from the image alone; the symmetry statement belongs to the broader lecture argument, not to a fully legible standalone derivation in the frame.
- Small faint marks elsewhere on the board do not look mathematically reliable and should be ignored.