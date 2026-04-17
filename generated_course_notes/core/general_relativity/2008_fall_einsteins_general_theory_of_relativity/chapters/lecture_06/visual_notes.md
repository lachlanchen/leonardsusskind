# Visual Evidence
## Frame Inventory
- `lecture_06_figure_02.png`: Shows the proper-time interval in metric form, the explicit Minkowski metric matrix, and a component rewrite of the interval; this screenshot should remain in the final notes as documentary evidence for the sign convention and board sequencing.
- `lecture_06_figure_04.png`: Shows the quadratic coordinate transformation, the combinatorial count \(D(D+1)/2\), and the condition that first derivatives of the metric vanish in the new coordinates; this screenshot should remain in the final notes because the board layout is part of the argument.
- `lecture_06_figure_05.png`: Shows the vanishing first-derivative condition together with the Christoffel-symbol formula, while remnants of the previous counting argument remain at right; this screenshot should remain in the final notes because it captures the transition from local coordinate choice to \(\Gamma=0\) at a point.

## Equation Extraction
- `lecture_06_figure_02.png`: \(d\tau^2 = g_{\mu\nu}\,dx^\mu dx^\nu\) [visible]
- `lecture_06_figure_02.png`: \(\eta_{\mu\nu}=\begin{pmatrix}1&0&0&0\\0&-1&0&0\\0&0&-1&0\\0&0&0&-1\end{pmatrix}\) [visible]
- `lecture_06_figure_02.png`: \(d\tau^2 = dt^2 - \dfrac{dx^2+dy^2+dz^2}{c^2}\) [standard completion]
- `lecture_06_figure_02.png`: \(dx^\mu\) [visible]

- `lecture_06_figure_04.png`: \(y^m = x^m + c^m{}_{rs}\,x^r x^s\) [visible]
- `lecture_06_figure_04.png`: \(\dfrac{D(D+1)}{2}\) [visible]
- `lecture_06_figure_04.png`: \(\dfrac{\partial g_{mn}(y)}{\partial y^s}=0\) [visible]
- `lecture_06_figure_04.png`: \(\neq 0\) at the far left edge of the board [partially visible]

- `lecture_06_figure_05.png`: \(\dfrac{\partial g_{mn}(x)}{\partial x^r}=0\) [visible]
- `lecture_06_figure_05.png`: \(\Gamma^r{}_{mn}=\dfrac12\,g^{rs}\!\left(\dfrac{\partial g_{sm}}{\partial x^n}+\dfrac{\partial g_{sn}}{\partial x^m}-\dfrac{\partial g_{mn}}{\partial x^s}\right)\) [visible]
- `lecture_06_figure_05.png`: \(y^m = x^m + \cdots\) [partially visible]
- `lecture_06_figure_05.png`: \(\dfrac{D(D+1)}{2}\) [partially visible]

## Diagram Extraction
- `lecture_06_figure_02.png` does not contain a geometric diagram, but the vertical board structure is important: general metric contraction at the top, explicit Minkowski matrix in the middle, and the component interval below. This should be preserved as a screenshot, not redrawn in TikZ.
- `lecture_06_figure_02.png` also includes a short slanted mark labeled \(dx^\mu\), which functions as a tiny board cue for the infinitesimal displacement rather than a standalone figure. It does not require TikZ.
- `lecture_06_figure_04.png` has no true sketch, but it does have a diagram-like argumentative layout: the transformation and coefficient count sit above, while the target condition \(\partial g/\partial y=0\) sits below and is physically indicated by Susskind’s hand and a curved pointer line. This should be preserved as a screenshot, not replaced by TikZ.
- `lecture_06_figure_05.png` likewise contains no geometric sketch; the important visual content is the placement of the vanishing-derivative condition above the Christoffel formula, with partial carryover from the previous board work at right. This should be preserved as a screenshot, not redrawn.
- Across these three frames, there is no board figure that needs a TikZ redraw. The useful “diagram” content is really board organization and equation adjacency.

## Reconstruction Guidance
- Use `lecture_06_figure_02.png` beside a clean typeset display of the proper-time interval and the Minkowski metric. The lower component formula should be normalized in standard notation, but the screenshot should stay visible because it documents Susskind’s ordering and sign choice.
- Use `lecture_06_figure_04.png` beside a normalized display of the quadratic coordinate transformation and the condition \(\partial_s g_{mn}(y)=0\). The screenshot matters because it shows that this was presented as a freedom-counting argument on the board, not merely as an abstract theorem.
- Use `lecture_06_figure_05.png` beside a clean Christoffel-symbol formula and the local condition \(\partial_r g_{mn}(x)=0\). Keep the screenshot visible because it is the visual evidence for the lecture’s transition from vanishing first derivatives to vanishing Christoffel symbols at a point.
- Do not imitate these frames with faux-blackboard TikZ. For these assets, the correct note-writing move is screenshot plus clean LaTeX reconstruction, with the reconstruction kept close to what is actually visible.
- When a formula is only partly cramped or partly cropped, prefer a cautious standard completion rather than trying to preserve every handwritten imperfection. The notes should read cleanly, but the screenshot should remain nearby wherever the lecture’s board rhythm matters.

## Uncertainties
- In `lecture_06_figure_02.png`, the lower interval formula is not fully crisp, especially toward the right; the standard completion with \(c^2\) in the denominator is safe, but the exact handwritten spacing is not reliable.
- In `lecture_06_figure_02.png`, the slanted \(dx^\mu\) mark is clear as a label but not part of a fully developed sketch.
- In `lecture_06_figure_04.png`, the leading linear term is best read as \(x^m\), though the handwriting could momentarily be mistaken for an uppercase \(X\).
- In `lecture_06_figure_04.png`, Susskind’s finger slightly crowds the numerator \(g_{mn}(y)\), so the derivative condition is legible but not perfectly clean.
- In `lecture_06_figure_04.png`, the isolated \(\neq 0\) at the far left appears to be residual board content from an earlier step and should not be elevated into a main displayed equation.
- In `lecture_06_figure_05.png`, the Christoffel-symbol formula is highly legible, but index placement should still be normalized in standard typeset form.
- In `lecture_06_figure_05.png`, the right-edge remnants of \(y^m=x^m+\cdots\) and \(D(D+1)/2\) are contextual carryover, not the primary equation of the frame.
- The board shifts between lowercase \(d\) and uppercase \(D\) for dimension counting in nearby discussion; these frames visibly show uppercase \(D\), so any normalization should be deliberate rather than accidental.