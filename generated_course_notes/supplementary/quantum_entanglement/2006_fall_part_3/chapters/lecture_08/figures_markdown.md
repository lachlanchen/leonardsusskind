# Figure Notes
## Image Inventory
- `lecture_08_figure_02.png`: Leonard Susskind stands between two boards. On the left board there are two hand-drawn waveforms, one smoother and one more jagged or higher-frequency, stacked one above the other. On the right board there is a vertical cluster of equations built from repeated `m` factors and second-derivative fractions, corresponding to the linear-oscillator discussion.
- `lecture_08_figure_03.png`: A clean close-up of a whiteboard with a quadratic-form expression across the top and a \(2\times2\) matrix written below it. No lecturer is in the frame. This is the clearest board-only evidence for the coefficient matrix being interpreted as the metric.
- `lecture_08_figure_04.png`: Susskind is seen from behind at the board. On the left there is a circular or spherical sketch with a marked point and a small differential triangle-like construction. Across the top is a line-element formula beginning with \(ds^2\), including a \(d\theta^2\) term and a \(\sin^2\theta\) factor. A sliver of the earlier metric-matrix board remains visible at the right edge.
- `lecture_08_figure_05.png`: Susskind stands in front of a board that now mixes earlier and later notation. On the left are tensor-style interval expressions with repeated indices and differential factors; below is a faint parenthesized coefficient display. On the right, part of the earlier quadratic-form expression and its \(2\times2\) matrix are still visible. The frame is useful mainly as evidence for the transition from concrete coefficient matrices to \(g_{\mu\nu}\)-style notation.

## Blackboard Equations
- `lecture_08_figure_02.png`: \(m\frac{d^2 x}{dt^2}\) [partially visible]
- `lecture_08_figure_02.png`: several harmonic-oscillator-style terms of the form \(m\frac{d^2(\cdots)}{dt^2}\) [visible]
- `lecture_08_figure_02.png`: \(m\frac{d^2 x_1}{dt^2}=-k x_1,\qquad m\frac{d^2 x_2}{dt^2}=-k x_2\) [standard reconstruction]
- `lecture_08_figure_02.png`: \(m\frac{d^2(x_1+x_2)}{dt^2}=-k(x_1+x_2)\) [standard reconstruction]

- `lecture_08_figure_03.png`: \(a_{11}\,dx^2 + a_{22}\,dy^2 + a_{12}\,dx\,dy\) [visible]
- `lecture_08_figure_03.png`: \(\begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}\) [visible]
- `lecture_08_figure_03.png`: \(a_{21}\,dy\,dx\) [standard reconstruction]

- `lecture_08_figure_04.png`: \(ds^2\) [visible]
- `lecture_08_figure_04.png`: \(d\theta^2\) [visible]
- `lecture_08_figure_04.png`: \(+\sin^2\theta\,(d\phi)^2\) [partially visible]
- `lecture_08_figure_04.png`: \(ds^2=d\theta^2+\sin^2\theta\,d\phi^2\) [standard reconstruction]

- `lecture_08_figure_05.png`: \(dx^\mu dx_\mu\) [partially visible]
- `lecture_08_figure_05.png`: \(g_{\mu\nu}\,dx^\mu dx^\nu\) [partially visible]
- `lecture_08_figure_05.png`: \(\begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}\) [partially visible]
- `lecture_08_figure_05.png`: \(ds^2=g_{\mu\nu}(x)\,dx^\mu dx^\nu\) [standard reconstruction]

## Diagram And Layout Reading
- `lecture_08_figure_02.png` is organized as a comparison between visual waveforms on the left and equation structure on the right. The left board suggests the superposition discussion: two distinct wave shapes are shown separately. The right board appears to collect the linear differential-equation forms used to argue that sums of solutions remain solutions.
- `lecture_08_figure_03.png` has a very deliberate pedagogical layout. The top line gives the distance or interval as a quadratic expression in differentials, while the matrix beneath packages the coefficients into a single object. The board moment visually enacts the sentence “the matrix is called a metric.”
- `lecture_08_figure_04.png` combines a geometric sketch with a line element. The left diagram is a sphere or circular cross-section with a point on the surface and a small local triangle indicating the two differential directions. The top formula gives the corresponding metric in angular coordinates. The board is partially blocked by the lecturer, so the screenshot is strongest as evidence for the coexistence of the sketch and the formula, not for every symbol.
- `lecture_08_figure_05.png` is a transition frame. The right board still preserves the earlier concrete \(2\times2\) metric-matrix example, while the left board has moved to relativistic tensor notation. That juxtaposition is useful for note writing because it shows the lecture broadening from a two-coordinate coefficient matrix to the general \(g_{\mu\nu}\) line element.

## TeX Reconstruction Plan
- `lecture_08_figure_02.png` should remain visible in the notes. Nearby, the notes should typeset the harmonic-oscillator equations and the summed linear equation cleanly. If the chapter emphasizes the superposition argument, the two wave sketches can be redrawn in TikZ beside the screenshot rather than relying only on the hand-drawn board shapes.
- `lecture_08_figure_03.png` should remain visible and should be paired with a clean displayed quadratic form and a typeset \(2\times2\) matrix. The screenshot is valuable because it preserves the board layout of “quadratic expression above, matrix below.”
- `lecture_08_figure_04.png` should remain visible and should be paired with both a clean displayed line element and a TikZ redraw of the local spherical-coordinate sketch. The diagram is pedagogically important, but the formula in the screenshot is partly blocked, so the typeset equation should be normalized from the transcript.
- `lecture_08_figure_05.png` should remain visible as evidence for the transition to tensor notation. Nearby, the notes should typeset the general line element \(ds^2=g_{\mu\nu}(x)\,dx^\mu dx^\nu\), and if helpful, briefly show its relation to the earlier finite-dimensional coefficient matrix. No separate TikZ is necessary unless the chapter wants a schematic “concrete matrix to tensor notation” bridge.

## Caption Drafts
- `lecture_08_figure_02.png`: Wave superposition sketches and linear second-derivative equations
- `lecture_08_figure_03.png`: Quadratic form and metric matrix
- `lecture_08_figure_04.png`: Sphere sketch and angular line element
- `lecture_08_figure_05.png`: Metric tensor notation in the line element

## Uncertainties
- In `lecture_08_figure_02.png`, the exact numerators and right-hand sides of the differential equations are not fully legible. The second-derivative structure is clear, but the precise \(x_1\), \(x_2\), and \(-k x_i\) terms should be normalized from the transcript rather than claimed as fully image-derived.
- In `lecture_08_figure_03.png`, the right edge of the top expression is cropped. The visible part securely shows \(a_{11}dx^2 + a_{22}dy^2 + a_{12}dx\,dy\), but the symmetrized \(a_{21}dy\,dx\) completion comes from the surrounding lecture logic rather than the crop alone.
- In `lecture_08_figure_04.png`, the lecturer blocks part of the central top formula. The presence of \(ds^2\), \(d\theta^2\), and a \(\sin^2\theta\) factor is clear, but the clean full formula should be treated as a cautious standard reconstruction.
- In `lecture_08_figure_04.png`, the geometric sketch is suggestive rather than fully precise. It clearly represents a local construction on a sphere, but the exact placement of the differential labels is not completely readable from the frame.
- In `lecture_08_figure_05.png`, the top-left line is not fully secure symbol by symbol. It appears to include an interval expression with repeated indices, but whether the visible line is exactly \(dx^\mu dx_\mu\) or part of a larger equality should be normalized from transcript context.
- In `lecture_08_figure_05.png`, the general dependence \(g_{\mu\nu}(x)\) is transcript-backed rather than fully readable in the screenshot. The image mainly confirms the move to \(g_{\mu\nu}\)-notation and the continued presence of the earlier matrix example.