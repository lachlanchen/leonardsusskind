# Figure Notes
## Image Inventory
- `lecture_06_figure_02.png`: A medium board shot from the early space-time recap. The upper line gives the proper-time interval in metric form, the middle of the board shows the Minkowski metric as a \(4\times4\) diagonal matrix, and the lower line rewrites the interval in components. A short slanted line at upper right is labeled \(dx^\mu\). Susskind stands at the right edge but does not block the central matrix.
- `lecture_06_figure_04.png`: A board shot from the coordinate-freedom counting argument. At upper right is the quadratic coordinate transformation \(y^m = x^m + c^m{}_{rs}x^r x^s\), beneath it a count written as \(D(D+1)/2\), and below-left the condition that the first derivatives of the metric in the new coordinates vanish. A curved pointer line from the left and Susskind’s hand emphasize the derivative condition.
- `lecture_06_figure_05.png`: A tighter board shot from the next step of the same argument. At upper left the board states that the first derivatives of the metric vanish in the chosen \(x\)-coordinates, and below it appears the Christoffel-symbol formula in terms of derivatives of \(g\). On the right edge, the earlier coordinate transformation and the \(D(D+1)/2\) count remain partially visible as contextual carryover.

## Blackboard Equations
- `lecture_06_figure_02.png`: \(d\tau^2 = g_{\mu\nu}\,dx^\mu dx^\nu\) [visible]
- `lecture_06_figure_02.png`: \(\eta_{\mu\nu}=\begin{pmatrix}1&0&0&0\\0&-1&0&0\\0&0&-1&0\\0&0&0&-1\end{pmatrix}\) [visible]
- `lecture_06_figure_02.png`: \(d\tau^2 = dt^2 - \dfrac{dx^2+dy^2+dz^2}{c^2}\) [standard reconstruction]
- `lecture_06_figure_02.png`: \(dx^\mu\) [visible]

- `lecture_06_figure_04.png`: \(y^m = x^m + c^m{}_{rs}\,x^r x^s\) [visible]
- `lecture_06_figure_04.png`: \(\dfrac{D(D+1)}{2}\) [visible]
- `lecture_06_figure_04.png`: \(\dfrac{\partial g_{mn}(y)}{\partial y^s}=0\) [visible]
- `lecture_06_figure_04.png`: \(\neq 0\) at the far left margin [partially visible]

- `lecture_06_figure_05.png`: \(\dfrac{\partial g_{mn}(x)}{\partial x^r}=0\) [visible]
- `lecture_06_figure_05.png`: \(\Gamma^r{}_{mn}=\dfrac12\,g^{rs}\!\left(\dfrac{\partial g_{sm}}{\partial x^n}+\dfrac{\partial g_{sn}}{\partial x^m}-\dfrac{\partial g_{mn}}{\partial x^s}\right)\) [visible]
- `lecture_06_figure_05.png`: \(y^m = x^m + \cdots\) [partially visible]
- `lecture_06_figure_05.png`: \(\dfrac{D(D+1)}{2}\) [partially visible]

## Diagram And Layout Reading
- `lecture_06_figure_02.png` has no geometric sketch, but the board layout is important. Susskind organizes the argument vertically: general metric contraction on top, explicit Minkowski metric in the middle, and the component interval below. The slanted segment labeled \(dx^\mu\) visually marks the infinitesimal space-time displacement.
- `lecture_06_figure_04.png` also has no true diagram; its value is argumentative layout. The quadratic coordinate transformation and the coefficient count sit at the upper right, while the target condition \(\partial g/\partial y = 0\) is written large below and physically pointed to. This makes the unknowns-versus-equations logic visually explicit.
- `lecture_06_figure_05.png` continues that same board organization. The vanishing derivative condition sits above, the Christoffel formula below, and remnants of the previous coordinate-transformation setup remain at the right. This is useful documentary evidence that Susskind is now turning the counting argument into the statement that the Christoffel symbols vanish when the first metric derivatives vanish.
- Across all three images, the visual value is equation placement and lecture flow rather than a redrawable sketch. None of these frames calls for TikZ as a replacement for the screenshot itself.

## TeX Reconstruction Plan
- `lecture_06_figure_02.png` should remain visible in the notes. It is the best documentary frame for the lecture’s shift from ordinary spatial metric notation to the space-time metric \(\eta_{\mu\nu}\). Pair it with a clean displayed equation block giving \(d\tau^2=g_{\mu\nu}dx^\mu dx^\nu\), the explicit Minkowski matrix, and the cleaned interval formula with \(c^2\) in the denominator. No TikZ redraw is needed.
- `lecture_06_figure_04.png` should remain visible near the discussion of coordinate freedom at a point. Pair it with typeset versions of the quadratic coordinate transformation, the count \(D(D+1)/2\), and the imposed condition \(\partial_s g_{mn}(y)=0\). The screenshot is valuable because it shows the board logic of “available coefficients above, target condition below.”
- `lecture_06_figure_05.png` should remain visible immediately after or alongside the passage where Susskind explains that vanishing first derivatives of the metric imply vanishing Christoffel symbols at the point. Pair it with a cleaned display of \(\partial_r g_{mn}(x)=0\) and the Christoffel formula. Again, no TikZ redraw is needed; the board equation itself is the evidence.
- The three screenshots work best as documentary anchors beside normalized LaTeX equations. They should not be replaced by redrawn boards, because what matters here is the lecture’s sequencing and board organization.

## Caption Drafts
- `lecture_06_figure_02.png`: Minkowski metric and proper-time interval
- `lecture_06_figure_04.png`: Coordinate freedom and vanishing metric derivative
- `lecture_06_figure_05.png`: Vanishing first derivatives and Christoffel symbols

## Uncertainties
- In `lecture_06_figure_02.png`, the lower interval formula is partly cramped and slightly occluded at the right; the cleaned form \(d\tau^2 = dt^2 - (dx^2+dy^2+dz^2)/c^2\) is the safe reconstruction from the visible board plus the transcript.
- In `lecture_06_figure_02.png`, the precise spacing and punctuation around the \(dx^\mu\) sketch are not important, but the label is clearly intended as the infinitesimal displacement.
- In `lecture_06_figure_04.png`, the leading linear term looks like \(x^m\), though the handwriting can momentarily resemble an uppercase \(X\). The transcript strongly supports the lowercase reading.
- In `lecture_06_figure_04.png`, Susskind’s finger partially crowds the numerator \(g_{mn}(y)\), but the full condition \(\partial g_{mn}(y)/\partial y^s=0\) is still recoverable directly from the frame.
- In `lecture_06_figure_04.png`, the cropped \(\neq 0\) at the far left is residue from earlier board work and should not be treated as part of the main displayed condition.
- In `lecture_06_figure_05.png`, the Christoffel formula is highly legible, but the exact handwritten index shapes are still worth normalizing to the standard clean form when typeset.
- In `lecture_06_figure_05.png`, the right-hand remnants of the earlier transformation and the \(D(D+1)/2\) count are cropped and should be treated as contextual carryover, not as the main content of the figure.
- The lecture and board alternate between lowercase \(d\) and uppercase \(D\) for dimension counting in nearby discussion; the visible count in these frames is uppercase \(D\), so the notes should preserve that locally unless the surrounding chapter intentionally normalizes notation.