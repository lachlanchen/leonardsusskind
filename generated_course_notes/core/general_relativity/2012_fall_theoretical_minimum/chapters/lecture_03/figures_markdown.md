# Figure Notes
## Image Inventory
- `lecture_03_figure_02.png`: A three-part board state. On the left board there is a coordinate-expansion formula under a large `y` label, reading like an expansion of `x^m` in powers of `y`. In the middle there is a small geometric sketch: a curved green coordinate line passing through two nearby points, with local black axes/tangent markers and several green rays near the upper point. On the right there is a large boxed equation stating that a coordinate derivative of a vector component is zero. Susskind is walking leftward and partly overlaps the middle sketch, but the boxed equation is unobstructed.
- `lecture_03_figure_03.png`: A theorem-style board layout headed `Gaussian normal`. The center of the board lists three metric conditions: the metric equals a Kronecker delta at a point, the first derivative vanishes there, and a second derivative is nonzero in general. On the right is a partially visible coordinate-expansion formula in `y` variables and the chalk label `Cristoffel`. A small cross-like mark sits at the left side of the board. Susskind stands at the far left and does not block the main equations.

## Blackboard Equations
- `lecture_03_figure_02.png`: [visible] \(x^m = y^m + C^m{}_{nr}\, y^n y^r\)
- `lecture_03_figure_02.png`: [visible] \(\dfrac{\partial V_m}{\partial x^r} = 0\)
- `lecture_03_figure_03.png`: [visible] \(\text{Gaussian normal}\)
- `lecture_03_figure_03.png`: [visible] \(g_{mn} = \delta_{mn} \quad \text{at } x=0\)
- `lecture_03_figure_03.png`: [visible] \(\dfrac{\partial g_{mn}}{\partial x^r} = 0 \quad \text{at } x=0\)
- `lecture_03_figure_03.png`: [visible] \(\dfrac{\partial^2 g_{mn}}{\partial x^r \partial x^s} \neq 0\)
- `lecture_03_figure_03.png`: [partially visible] \(x^m = y^m + C^m{}_{nr}\, y^n y^r\)
- `lecture_03_figure_03.png`: [visible] \(\text{Cristoffel}\)

## Diagram And Layout Reading
- `lecture_03_figure_02.png` is organized deliberately from left to right: coordinate transformation on the left, geometric intuition in the middle, and the boxed algebraic condition on the right. That board layout matters because it visually links curving coordinates to the failure of the naive condition \(\partial V_m/\partial x^r=0\) to be tensorial.
- In the middle sketch of `lecture_03_figure_02.png`, the black axes through the lower point look like the locally straight or Gaussian-normal frame, while the green curve and green rays suggest a superposed curvilinear coordinate system. The upper point appears to show a nearby tangent frame or local basis orientation. The sketch is not a finished diagram in itself, but it clearly supports the lecture’s point about coordinates changing from point to point.
- `lecture_03_figure_03.png` is laid out like a small theorem. The center stack carries the real mathematical payload: Gaussian normal coordinates make the metric locally flat-looking up to first order, but not generically to second order. The right side keeps the earlier coordinate-expansion machinery visible, along with the Christoffel label, so the board still shows where these conditions are heading.
- The small cross-like chalk mark on the left of `lecture_03_figure_03.png` does not appear to carry much mathematical content by itself; it is more a leftover board mark than a stand-alone figure element.

## TeX Reconstruction Plan
- `lecture_03_figure_02.png` should remain visible. It is useful not just for the boxed equation but for the three-zone board layout joining coordinate expansion, local geometric sketch, and boxed zero-derivative condition.
- Near `lecture_03_figure_02.png`, typeset the boxed condition cleanly as a displayed equation. A nearby TikZ redraw should simplify the middle sketch into a clean schematic: one locally straight frame, one curving coordinate line, and a nearby point with shifted local directions. The TikZ should clarify the geometry, but the screenshot should stay as documentary evidence of how Susskind organized the argument on the board.
- `lecture_03_figure_03.png` should also remain visible. Its main value is the stacked Gaussian-normal conditions as actually written on the board.
- Near `lecture_03_figure_03.png`, reconstruct the three central conditions as clean displayed equations in standard LaTeX. The right-hand coordinate-expansion formula can be typeset nearby if the chapter needs it, but it should be treated as supporting context rather than the main equation of the figure.
- No TikZ redraw is necessary for `lecture_03_figure_03.png`; the mathematical content is better handled by clean displayed equations and brief explanatory prose.

## Caption Drafts
- `lecture_03_figure_02.png`: Curved coordinates and a boxed zero-derivative condition
- `lecture_03_figure_03.png`: Gaussian normal coordinate conditions for the metric

## Uncertainties
- In `lecture_03_figure_02.png`, the index on \(V\) in the boxed equation looks like a lower index, but the transcript nearby discusses both covariant and contravariant components. The safest transcription from the image is \(\partial V_m/\partial x^r = 0\).
- In `lecture_03_figure_02.png`, the geometric sketch is clear as a local-coordinate comparison, but not every line has an unambiguous standalone meaning. It should be redrawn schematically rather than copied literally.
- In `lecture_03_figure_03.png`, the right-hand coordinate-expansion formula is cropped at the frame edge. The standard completion \(x^m = y^m + C^m{}_{nr} y^n y^r\) is well motivated by the visible portion and the surrounding lecture, but the full chalk expression is not completely shown.
- In `lecture_03_figure_03.png`, the chalk label is written as `Cristoffel`, not the normalized `Christoffel`. The notes should normalize the spelling silently.
- In `lecture_03_figure_03.png`, the first two lines explicitly say `at x=0`; the third line does not visibly repeat that phrase, even though the lecture context suggests the same local point is intended.