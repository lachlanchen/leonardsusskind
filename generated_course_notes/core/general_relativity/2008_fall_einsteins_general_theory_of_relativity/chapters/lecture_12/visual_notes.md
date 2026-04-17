# Visual Evidence
## Frame Inventory
- `lecture_12_figure_02.png`: A clear right-Rindler-wedge board drawing with constant-\(r\) hyperbolae, constant-\(\omega\) rays, and the start of the \((r,\omega)\mapsto(x,t)\) coordinate map; the screenshot should remain in the final notes.
- `lecture_12_figure_03.png`: The clearest surviving board view of the Schwarzschild line element written as a single display; the screenshot should remain.
- `lecture_12_figure_04.png`: A wider causal redraw showing \(\omega=0\), a family of constant-\(\omega\) rays, and repeated \(x^2-t^2=\cdots\) relations at the moment Susskind emphasizes that the horizon is reached only at \(\omega=\infty\); the screenshot should remain.
- `lecture_12_figure_05.png`: A right-side crop dominated by the near-horizon Rindler-form metric and the time rescaling \(\omega=t/(4MG)\), with only the edge of the new redraw visible; the screenshot should remain.
- `lecture_12_figure_06.png`: A comparative board panel with a leftover invariant relation, the vacuum Einstein equation, and a schematic Poisson analogy; the screenshot should remain.

## Equation Extraction
- `lecture_12_figure_02.png`: \(x=t\) [visible]
- `lecture_12_figure_02.png`: \(r,\ \omega\) [visible]
- `lecture_12_figure_02.png`: \(x=r\cosh\omega\) [partially visible]
- `lecture_12_figure_02.png`: \(t=r\sinh\omega\) [standard completion]
- `lecture_12_figure_02.png`: \(\omega=1,\omega=2,\omega=3,\omega=4\) on successive rays [partially visible]
- `lecture_12_figure_03.png`: \(\left(1-\frac{2MG}{r}\right)dt^2-\frac{dr^2}{1-\frac{2MG}{r}}-r^2d\Omega^2\) [partially visible]
- `lecture_12_figure_03.png`: \(d\tau^2=\left(1-\frac{2MG}{r}\right)dt^2-\frac{dr^2}{1-\frac{2MG}{r}}-r^2d\Omega^2\) [standard completion]
- `lecture_12_figure_04.png`: \(\omega=0\) [visible]
- `lecture_12_figure_04.png`: \(x^2-t^2=\cdots\) [visible]
- `lecture_12_figure_04.png`: \(x^2-t^2=\text{const}\) [standard completion]
- `lecture_12_figure_04.png`: \(\rho^2d\omega^2-d\rho^2\) or part of that metric block [partially visible]
- `lecture_12_figure_05.png`: \(d\tau^2=\rho^2d\omega^2-d\rho^2-dz^2-dy^2\) [standard completion]
- `lecture_12_figure_05.png`: \(\omega=\frac{t}{4MG}\) [visible]
- `lecture_12_figure_05.png`: \(d\omega=\frac{dt}{4MG}\) [partially visible]
- `lecture_12_figure_06.png`: \(X^2-t^2=R\) [partially visible]
- `lecture_12_figure_06.png`: \(R_{\mu\nu}-\frac12 g_{\mu\nu}R=0\) [visible]
- `lecture_12_figure_06.png`: \(\nabla^2\phi=\rho\) [partially visible]
- `lecture_12_figure_06.png`: \(\nabla^2\phi=\text{source}\) [standard completion]

## Diagram Extraction
- `lecture_12_figure_02.png` should be shown both ways: keep the screenshot and redraw it in TikZ as the right Rindler wedge with the light cone, constant-\(r\) hyperbolae, constant-\(\omega\) rays, and labels \(x\), \(t\), and \(x=t\).
- `lecture_12_figure_03.png` should be preserved as a screenshot but not redrawn as a diagram; the mathematics belongs in a clean displayed equation.
- `lecture_12_figure_04.png` should be shown both ways: keep the screenshot and redraw a second TikZ version focused on constant-\(\omega\) slices piling up against the horizon as \(\omega\to\infty\).
- `lecture_12_figure_05.png` should remain a screenshot-plus-equation figure; it is useful as board-layout evidence but not reliable enough to serve as the primary source for the redraw being started there.
- `lecture_12_figure_06.png` should remain a screenshot paired with typeset equations; the key point is the visual juxtaposition of Einstein and Newton, not a geometric sketch.
- The later inside-the-horizon/singularity picture should be redrawn in TikZ from the transcript logic and surrounding frames, with `lecture_12_figure_05.png` kept nearby only as supporting board evidence.

## Reconstruction Guidance
- Use the transcript to fix order, narrative emphasis, and completed formulas; use the frames to preserve what was actually on the board together and how Susskind organized the board.
- Typeset the coordinate map beside `lecture_12_figure_02.png` as \(x=r\cosh\omega,\ t=r\sinh\omega\), but keep the screenshot because it carries the actual ray labels and wedge geometry.
- Normalize `lecture_12_figure_03.png` into a clean Schwarzschild line element with \(d\tau^2\) and \(d\Omega^2\); the screenshot is documentary support, not the sole legibility source.
- Treat the repeated \(x^2-t^2=\cdots\) in `lecture_12_figure_04.png` as evidence for the invariant relation, but do not preserve unreadable right-hand constants one by one; \(x^2-t^2=\text{const}\) is the cautious reconstruction.
- Reconstruct `lecture_12_figure_05.png` as a clean near-horizon metric block together with \(\omega=t/(4MG)\) and \(d\omega=dt/(4MG)\), while keeping the screenshot because it shows that the metric and the redraw setup coexisted on the board at that moment.
- Typeset `lecture_12_figure_06.png` as the vacuum Einstein equation above a normalized Poisson analogy, but preserve the screenshot because the pedagogical force lies in the comparison panel as drawn.

## Uncertainties
- In `lecture_12_figure_02.png`, the lecturer blocks the right edge of the coordinate map, so \(t=r\sinh\omega\) is better taken from the transcript than from the image alone.
- The individual \(\omega\)-labels in `lecture_12_figure_02.png` are not all fully legible.
- The left side of the Schwarzschild display in `lecture_12_figure_03.png` is cropped, so \(d\tau^2=\) is a completion rather than a literal full-board transcription.
- The constants on the right-hand sides of the repeated \(x^2-t^2=\cdots\) relations in `lecture_12_figure_04.png` are not reliably readable.
- The top metric line in `lecture_12_figure_05.png` is blurred and partly cut, so the full Rindler-form metric should be treated as transcript-supported reconstruction.
- In `lecture_12_figure_06.png`, the lower source term is schematic and may not literally be a clean \(\rho\); it is safer to read it as a Poisson-style source term.
- The top relation in `lecture_12_figure_06.png` may use uppercase \(X\) rather than lowercase \(x\), and the underlined \(R\) looks like leftover board notation rather than a central formula.
- The rough circular mark in `lecture_12_figure_06.png` should not be overread as part of the mathematical argument.