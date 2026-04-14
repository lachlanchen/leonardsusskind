# Visual Evidence
## Frame Inventory
- `lecture_08_figure_02.png`: Susskind stands between two boards, with two stacked wave sketches on the left and a vertical cluster of second-derivative equations on the right; the screenshot should remain in the final notes.
- `lecture_08_figure_03.png`: A clean board-only close-up shows a quadratic differential form above a \(2\times2\) coefficient matrix; the screenshot should remain in the final notes.
- `lecture_08_figure_04.png`: Susskind partly blocks a board containing a spherical or circular local sketch and a line element with \(d\theta^2\) and a \(\sin^2\theta\) factor; the screenshot should remain in the final notes.
- `lecture_08_figure_05.png`: A transition frame shows tensor-style interval notation on the left and part of the earlier quadratic-form matrix example on the right; the screenshot should remain in the final notes.

## Equation Extraction
- `lecture_08_figure_02.png`: \(m\frac{d^2 x}{dt^2}\) [partially visible]
- `lecture_08_figure_02.png`: several terms of the form \(m\frac{d^2(\cdots)}{dt^2}\) arranged vertically [visible]
- `lecture_08_figure_02.png`: \(m\frac{d^2 x_1}{dt^2}=-k x_1,\qquad m\frac{d^2 x_2}{dt^2}=-k x_2\) [standard completion]
- `lecture_08_figure_02.png`: \(m\frac{d^2(x_1+x_2)}{dt^2}=-k(x_1+x_2)\) [standard completion]

- `lecture_08_figure_03.png`: \(a_{11}\,dx^2 + a_{22}\,dy^2 + a_{12}\,dx\,dy\) [visible]
- `lecture_08_figure_03.png`: \(\begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}\) [visible]
- `lecture_08_figure_03.png`: \(a_{21}\,dy\,dx\) [standard completion]

- `lecture_08_figure_04.png`: \(ds^2\) [visible]
- `lecture_08_figure_04.png`: \(d\theta^2\) [visible]
- `lecture_08_figure_04.png`: \(+\sin^2\theta\,(d\phi)^2\) [partially visible]
- `lecture_08_figure_04.png`: \(ds^2=d\theta^2+\sin^2\theta\,d\phi^2\) [standard completion]

- `lecture_08_figure_05.png`: repeated-index differential products on the left board, plausibly of the form \(dx^\mu dx_\mu\) [partially visible]
- `lecture_08_figure_05.png`: tensor-style line-element notation of the form \(g_{\mu\nu}\,dx^\mu dx^\nu\) [partially visible]
- `lecture_08_figure_05.png`: \(\begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}\) at the right edge [partially visible]
- `lecture_08_figure_05.png`: \(ds^2=g_{\mu\nu}(x)\,dx^\mu dx^\nu\) [standard completion]

## Diagram Extraction
- `lecture_08_figure_02.png`: The two left-board waveforms should be shown both ways: keep the screenshot as evidence and redraw the waves in TikZ if the notes want a cleaner superposition illustration.
- `lecture_08_figure_02.png`: The right-board equation stack does not need TikZ, only clean typeset equations placed near the screenshot.
- `lecture_08_figure_03.png`: The board layout itself matters more than a geometric sketch, so keep the screenshot and typeset the quadratic form and matrix cleanly; no TikZ is needed.
- `lecture_08_figure_04.png`: The spherical local sketch should be shown both ways: keep the screenshot and redraw the local patch, point, and differential triangle in TikZ.
- `lecture_08_figure_04.png`: The line element should be typeset cleanly next to the screenshot rather than relied on in handwritten form.
- `lecture_08_figure_05.png`: Keep the screenshot as evidence for the transition from concrete matrix notation to \(g_{\mu\nu}\)-notation; no dedicated TikZ is necessary unless the chapter wants a schematic bridge figure.

## Reconstruction Guidance
- Use `lecture_08_figure_02.png` to preserve the board rhythm of “wave pictures on the left, linear equations on the right,” but normalize the actual oscillator equations from the transcript because the detailed right-hand sides are not fully readable.
- Use `lecture_08_figure_03.png` as the anchor image for the moment where the coefficient matrix becomes the metric; nearby, typeset the full symmetrized quadratic form and the \(2\times2\) matrix in polished LaTeX.
- Use `lecture_08_figure_04.png` as evidence that Susskind is pairing a local geometric construction on the sphere with the angular line element; redraw the geometry in TikZ and typeset the spherical metric in standard clean form.
- Use `lecture_08_figure_05.png` to preserve the pedagogical transition from the earlier two-coordinate example to general spacetime tensor notation; the final notes should present the clean line element in standard \(g_{\mu\nu}(x)\) notation while keeping the screenshot nearby.
- When a frame is partly blocked or cropped, prefer a cautious standard completion already motivated by the lecture rather than trying to over-read the handwriting.
- Preserve screenshots where board layout carries explanatory weight, especially in figures `02`, `03`, `04`, and `05`; use LaTeX and TikZ to supply legibility, not to replace the evidence.

## Uncertainties
- In `lecture_08_figure_02.png`, the second-derivative structure is clear, but the exact numerators, subscripts, and right-hand sides are not fully legible.
- In `lecture_08_figure_03.png`, the top expression is cropped before the full symmetrized mixed term is visible, so \(a_{21}\,dy\,dx\) should be treated as a completion rather than a directly read term.
- In `lecture_08_figure_04.png`, Susskind blocks part of the central formula, so the full \(ds^2=d\theta^2+\sin^2\theta\,d\phi^2\) expression is not wholly image-secure even though its main pieces are.
- In `lecture_08_figure_04.png`, the local labels on the spherical sketch are too unclear to transcribe exactly.
- In `lecture_08_figure_05.png`, the top-left repeated-index notation is not fully reliable symbol by symbol; the frame supports the general move to tensor notation more strongly than any single exact left-board formula.
- In `lecture_08_figure_05.png`, the dependence on position in \(g_{\mu\nu}(x)\) is transcript-supported and only weakly image-supported.