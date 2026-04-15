# Figure Notes
## Image Inventory
- `lecture_02_figure_02.png`: A clean top-board equation frame. The board shows a tensor subtraction written componentwise, with Susskind already moved to the right so the whole equation is visible. There are no supporting diagrams; the rest of the board is nearly blank.
- `lecture_02_figure_03.png`: A metric-transformation frame. The top line shows the invariant interval in unprimed and primed coordinates, with a small box around the primed metric term and a larger box around the transformed expression built from the unprimed metric and Jacobians. On the left side, auxiliary substitutions for \(dx^m\) and \(dx^n\) in terms of \(dy\)-coordinates are partially visible. Susskind points directly at the \(g_{mn}(x)\) factor in the large box.
- `lecture_02_figure_06.png`: A fuller board-state frame later in the lecture. The top line still shows the metric transformation formula. Below it, at left, the inverse-metric identity with a boxed \(g^{np}\) term is visible. In the lower center, a \(2\times 2\) lower-index metric matrix is multiplied by a \(2\times 2\) upper-index inverse-metric matrix, illustrating the matrix viewpoint and the symmetry discussion.

## Blackboard Equations
- `lecture_02_figure_02.png`: [visible] \(T^{m\cdots}{}_{\cdots p} - S^{m\cdots}{}_{\cdots p} = (T-S)^{m\cdots}{}_{\cdots p}\)
- `lecture_02_figure_03.png`: [visible] \(g_{mn}(x)\,dx^m dx^n = g'_{pq}(y)\,dy^p dy^q\)
- `lecture_02_figure_03.png`: [visible] \(g'_{pq}(y)\,dy^p dy^q = \left[g_{mn}(x)\,\frac{\partial x^m}{\partial y^p}\,\frac{\partial x^n}{\partial y^q}\right]dy^p dy^q\)
- `lecture_02_figure_03.png`: [partially visible] \(dx^m = \frac{\partial x^m}{\partial y^p}\,dy^p\)
- `lecture_02_figure_03.png`: [partially visible] \(dx^n = \frac{\partial x^n}{\partial y^q}\,dy^q\)
- `lecture_02_figure_06.png`: [partially visible] \(g_{mn}(x)\,dx^m dx^n = g'_{pq}(y)\,dy^p dy^q = \left[g_{mn}(x)\,\frac{\partial x^m}{\partial y^p}\,\frac{\partial x^n}{\partial y^q}\right]dy^p dy^q\)
- `lecture_02_figure_06.png`: [partially visible] \(g_{mn}\,g^{np} = \delta_m{}^{p}\)
- `lecture_02_figure_06.png`: [visible] \(\begin{pmatrix} g_{11} & g_{12} \\ g_{21} & g_{22} \end{pmatrix}\begin{pmatrix} g^{11} & g^{12} \\ g^{21} & g^{22} \end{pmatrix} = \)
- `lecture_02_figure_06.png`: [standard reconstruction] \(g_{mn}=g_{nm}\)

## Diagram And Layout Reading
- `lecture_02_figure_02.png` is not a diagram frame. Its value is that it shows the board reduced to one conceptual statement: the difference of two tensors of the same type is again a tensor of that same type.
- `lecture_02_figure_03.png` is organized as a chain of equalities across the top of the board. The small box isolates the primed metric \(g'_{pq}(y)\), while the large box isolates the transformed expression built from \(g_{mn}(x)\) and two Jacobian factors. This boxed layout matters because it visually identifies the object that must be interpreted as the new metric tensor in the primed coordinates.
- In `lecture_02_figure_03.png`, Susskind’s pointing gesture is semantically important: he points to the unprimed-frame factor \(g_{mn}(x)\) inside the large box, matching the spoken emphasis that the primed metric is “given by the metric tensor in the unprimed frame” together with the coordinate derivatives.
- `lecture_02_figure_06.png` has a three-part board structure that is useful for note writing: the transformation law across the top, the inverse-metric identity at left, and the small matrix example below. The frame is valuable not because of one single equation alone, but because it documents how Susskind is tying together transformation law, inverse matrix, and symmetry.
- There are no axes or geometric sketches in these selected frames that need formal diagram recovery. The only visually structured material beyond equations is the use of boxes and the matrix layout.

## TeX Reconstruction Plan
- `lecture_02_figure_02.png` should remain visible as a documentary screenshot. Pair it with a clean displayed equation for the tensor subtraction rule. No TikZ redraw is needed.
- `lecture_02_figure_03.png` should remain visible. Reconstruct the full displayed metric-transformation formula cleanly in LaTeX nearby, preserving the lecture’s logic that the boxed transformed coefficient is the primed metric tensor. If helpful, preserve the two-box emphasis typographically, for example by discussing the small boxed \(g'_{pq}(y)\) and the larger boxed expression in the prose.
- `lecture_02_figure_03.png` does not need TikZ. The board is already functioning as an equation-layout figure, not a geometric drawing.
- `lecture_02_figure_06.png` should remain visible because the board layout itself matters. Near it, typeset the inverse-metric identity \(g_{mn}g^{np}=\delta_m{}^{p}\) and a clean \(2\times2\) matrix example to illustrate the symmetric matrix discussion.
- For `lecture_02_figure_06.png`, a small LaTeX matrix reconstruction is preferable to trying to reproduce the chalk layout literally. No TikZ is necessary; standard matrix notation is enough.
- The notes should not rely on these frames to establish the whole derivation of the inverse metric or the full symmetry argument. They are best used as supporting evidence for board layout and for the named equations.

## Caption Drafts
- `lecture_02_figure_02.png`: Tensor subtraction as a tensor equation
- `lecture_02_figure_03.png`: Metric tensor in primed and unprimed coordinates
- `lecture_02_figure_06.png`: Inverse metric identity and symmetric matrix example

## Uncertainties
- In `lecture_02_figure_02.png`, the exact number and placement of the omitted indices are represented only by ellipses on the board. The notes should preserve the generic tensor-index pattern without pretending the omitted slots are fully specified.
- In `lecture_02_figure_03.png`, the auxiliary substitution lines for \(dx^m\) and \(dx^n\) are only partially visible. The transcript strongly supports the standard completion with trailing factors \(dy^p\) and \(dy^q\), but the screenshot alone does not show every symbol cleanly.
- In `lecture_02_figure_03.png` and `lecture_02_figure_06.png`, the boxed top-line transformation formula is legible in structure, but the exact spacing and box boundaries are chalkboard layout rather than notation that should be copied literally. A clean typeset reconstruction is preferable.
- In `lecture_02_figure_06.png`, the left-hand inverse-metric identity is not perfectly isolated: part of the left factor is close to the frame edge and the boxed \(g^{np}\) is visually emphasized more strongly than the whole product. The safe clean reconstruction is \(g_{mn}g^{np}=\delta_m{}^{p}\).
- In `lecture_02_figure_06.png`, the lower matrix example is unfinished as written on the board. The two matrices are visible, but the product/result on the right is not fully developed. The notes should reconstruct only the visible matrices and state the intended matrix viewpoint in prose.
- The small faint marks elsewhere on the boards in `lecture_02_figure_02.png` and `lecture_02_figure_06.png` do not look mathematically reliable and should be ignored.