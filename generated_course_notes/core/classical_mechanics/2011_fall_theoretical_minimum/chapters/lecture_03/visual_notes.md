# Visual Evidence
## Frame Inventory
- `lecture_03_figure_02.png`: Shows Susskind beside a clean one-dimensional equilibrium condition, \(\frac{dV(x)}{dx}=0\), with open board space below for the imminent graph; this screenshot should remain in the final notes.
- `lecture_03_figure_03.png`: Shows a fixed-endpoint U-shaped curve with endpoint dots and a long shallow line beneath it, read most plausibly as the hanging-chain or stationary-curve example; this screenshot should remain in the final notes.
- `lecture_03_figure_04.png`: Shows the Euler-Lagrange derivation board with an upper derivative term in \(x_i\) and a lower velocity-derivative line, but only partially and somewhat cropped; this screenshot should remain in the final notes as documentary derivation evidence.
- `lecture_03_figure_05.png`: Shows the clearest summary board linking potential energy, kinetic energy, the Lagrangian \(L=T-V\), and the force-law form of Newton’s equation; this screenshot should remain in the final notes.

## Equation Extraction
- `lecture_03_figure_02.png`: \(\frac{dV(x)}{dx}=0\) [visible]

- `lecture_03_figure_04.png`: \(\frac{\partial L}{\partial x_i}\) [visible]
- `lecture_03_figure_04.png`: \(\frac{1}{\epsilon}\frac{\partial L}{\partial v_i}\) [partially visible]
- `lecture_03_figure_04.png`: \(-\frac{d}{dt}\!\left(\frac{\partial L}{\partial \dot x}\right)+\frac{\partial L}{\partial x}\) [standard completion]
- `lecture_03_figure_04.png`: \(\frac{d}{dt}\!\left(\frac{\partial L}{\partial \dot x}\right)=\frac{\partial L}{\partial x}\) [standard completion]

- `lecture_03_figure_05.png`: \(V(x_i)\) [visible]
- `lecture_03_figure_05.png`: \(\sum_i \frac{m}{2}\dot x_i^2\) [partially visible]
- `lecture_03_figure_05.png`: \(L=\frac{m\dot x^2}{2}-V(x)\) [visible]
- `lecture_03_figure_05.png`: \(m\ddot x_i=-\frac{\partial V}{\partial x_i}=F_i(x)\) [partially visible]
- `lecture_03_figure_05.png`: \(L=T-V\) [standard completion]

- `lecture_03_figure_03.png`: no symbolic equation is legible in the frame itself [visible]
- `lecture_03_figure_03.png`: a fixed-endpoint stationary curve minimizing or stationarizing an integral quantity [standard completion]

## Diagram Extraction
- `lecture_03_figure_02.png`: No full diagram is yet drawn, but the board layout matters. The large equation high on the board with blank space below should be preserved via the screenshot because it visually records the lecture’s transition from algebraic condition to graphical interpretation.
- `lecture_03_figure_03.png`: The main diagram is a smooth U-shaped curve suspended between two marked endpoints. This should be shown both ways: preserved as the screenshot for authentic board evidence, and redrawn in TikZ as a clean schematic with two endpoint markers and a smooth sagging curve.
- `lecture_03_figure_03.png`: The lower long line beneath the U-shaped curve is visually present but unlabeled. If redrawn at all, it should be rendered only as a faint baseline or omitted unless later context confirms its meaning.
- `lecture_03_figure_04.png`: This is not really a stand-alone diagram, but it does preserve the vertical board organization of the derivation: upper position-derivative term, lower velocity-derivative line. The screenshot is useful as layout evidence, while the mathematics itself should be re-typeset cleanly.
- `lecture_03_figure_05.png`: This frame preserves a summary-board structure rather than a geometric figure. The final notes should keep the screenshot and also re-typeset the equations nearby to clarify the relationship between \(V\), \(T\), \(L\), and \(F_i\).

## Reconstruction Guidance
- Use `lecture_03_figure_02.png` as the visual anchor for the equilibrium discussion, but typeset the equation cleanly as \(\frac{dV(x)}{dx}=0\). Do not invent a graph from this frame alone; if the notes later show a potential graph, it should be presented as transcript-backed reconstruction rather than claimed as visible here.
- Use `lecture_03_figure_03.png` as evidence that Susskind actually drew a fixed-endpoint stationary curve on the board. Pair it with a restrained TikZ redraw: two endpoint dots, one smooth sagging curve, no extra labels unless the transcript requires them.
- Use `lecture_03_figure_04.png` to justify the presence and order of the Euler-Lagrange ingredients, but do not transcribe every intermediate symbol literally. The clean note version should present the finished Euler-Lagrange equation and, if needed, one compact finite-difference precursor derived from standard cautious completion.
- Use `lecture_03_figure_05.png` to preserve the lecture’s summary layout while normalizing the notation in the notes. The board visibly mixes single-coordinate and indexed notation, so the note version should choose one consistent register at a time and explain the transition explicitly.
- For `lecture_03_figure_05.png`, the most reliable note-quality presentation is to typeset
  \(T=\sum_i \frac{m_i}{2}\dot x_i^2\) or the single-particle version \(T=\frac{m\dot x^2}{2}\),
  \(L=T-V\),
  and
  \(m\ddot x_i=-\frac{\partial V}{\partial x_i}=F_i\),
  while keeping the screenshot nearby to show that this summary really appeared on the board.
- Across all four frames, let the transcript govern the mathematical sequence and motivation. The frames should confirm notation, sketches, and board emphasis, not replace missing derivational detail with aggressive guesswork.

## Uncertainties
- In `lecture_03_figure_03.png`, the long shallow lower line is not securely identifiable from the image alone. It may be a baseline, a guide line, or residual board geometry.
- In `lecture_03_figure_03.png`, the curve is clearly fixed-endpoint and U-shaped, but the frame alone does not prove whether it is meant as a literal hanging chain, a potential sketch, or a generic stationary configuration; the transcript is needed for that interpretation.
- In `lecture_03_figure_04.png`, the upper \(\partial L/\partial x_i\) is readable, but neighboring coefficients, indices, and the full lower expression are not reliably legible.
- In `lecture_03_figure_04.png`, the appearance of \(v_i\) versus \(\dot x_i\) is not clean enough to treat the frame as exact notation evidence; the note version should use the standard form consistent with the transcript’s finite-difference discussion.
- In `lecture_03_figure_05.png`, the left-side kinetic-energy expression is only partly visible, so the summation structure should be restored cautiously rather than claimed as fully legible.
- In `lecture_03_figure_05.png`, the board mixes \(V(x_i)\), \(L=\frac{m\dot x^2}{2}-V(x)\), and \(m\ddot x_i=-\partial V/\partial x_i\). That mixture is visually real, but the final notes should regularize the notation rather than reproduce the inconsistency.
- `lecture_03_figure_02.png` captures the setup before the graph is drawn, so it supports the stationary-point condition strongly but only supports the forthcoming graphical interpretation indirectly.