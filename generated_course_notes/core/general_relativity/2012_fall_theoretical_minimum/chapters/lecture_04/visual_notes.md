# Visual Evidence
## Frame Inventory
- `lecture_04_figure_04.png`: Clean board shot of the Minkowski line element, tensor form, explicit \(4\times 4\) metric matrix, and coordinate-identification list \(X^\mu=(t,x,y,z)\); this screenshot should remain in the final notes.
- `lecture_04_figure_05.png`: Two-board shot showing older boxed geodesic/Christoffel relations on the left and the local accelerated-frame metric expansion on the right, with the boxed first-order approximation as the main payload; this screenshot should remain in the final notes.
- `lecture_04_figure_06.png`: Summary derivation board connecting the geodesic equation, a Christoffel-symbol expression for \(d^2y/d\tau^2\), and a derivative-of-\(g_{tt}\) force law; this screenshot should remain in the final notes.

## Equation Extraction
- `lecture_04_figure_04.png` [visible] \(d\tau^2 = dt^2 - dx^2 - dy^2 - dz^2\)
- `lecture_04_figure_04.png` [visible] \(d\tau^2 = -\,g_{\mu\nu}\,dx^\mu dx^\nu\)
- `lecture_04_figure_04.png` [visible] \(g_{\mu\nu}=\begin{pmatrix}-1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{pmatrix}\)
- `lecture_04_figure_04.png` [visible] \(X^\mu=(t,x,y,z)\)
- `lecture_04_figure_04.png` [visible] \(t=x^0,\quad x=x^1,\quad y=x^2,\quad z=x^3\)

- `lecture_04_figure_05.png` [partially visible] \(d\tau^2=(R^2+2Ry+y^2)\,\cdots\)
- `lecture_04_figure_05.png` [partially visible] \(=\left(1+\frac{2y}{R}+\frac{y^2}{R^2}\right)\,\cdots\)
- `lecture_04_figure_05.png` [partially visible] \(\left(1+2yg\right)dt^2-\cdots\)
- `lecture_04_figure_05.png` [partially visible] \(\cdots+\Gamma^n{}_{mr}\,t^r\,dx^m=0\)
- `lecture_04_figure_05.png` [standard completion] \(d\tau^2=(R^2+2Ry+y^2)\,d\omega^2-dy^2\)
- `lecture_04_figure_05.png` [standard completion] \(d\tau^2=\left(1+\frac{2y}{R}+\frac{y^2}{R^2}\right)R^2\,d\omega^2-dy^2\)
- `lecture_04_figure_05.png` [standard completion] \(d\tau^2\approx (1+2yg)\,dt^2-dy^2,\qquad g=\frac{1}{R}\)

- `lecture_04_figure_06.png` [visible] \(dt^n+\Gamma^n{}_{mr}\,t^r\,dx^m=0\)
- `lecture_04_figure_06.png` [visible] \(\frac{d^2y}{d\tau^2}=-\,\Gamma^{y}{}_{mr}\,\frac{dx^r}{d\tau}\frac{dx^m}{d\tau}\)
- `lecture_04_figure_06.png` [partially visible] \(\frac{dt^n}{dS}=-\,\cdots\)
- `lecture_04_figure_06.png` [partially visible] \(\frac{d^2x^n}{dS^2}=\cdots\)
- `lecture_04_figure_06.png` [visible] \(\frac{d^2y}{d\tau^2}=+\,\frac{\partial g_{tt}}{\partial y}\)
- `lecture_04_figure_06.png` [standard completion] In clean note form, the weak-field slow-motion reduction should be normalized from the transcript and Christoffel formula rather than copied literally from the chalk line.

## Diagram Extraction
- `lecture_04_figure_04.png`: There is a small spacetime-orientation sketch at left with \(t\) vertical, \(x\) horizontal, and an upward arrow; preserve the screenshot, and redraw the axes in TikZ only if a tiny orientation figure would help the surrounding prose.
- `lecture_04_figure_04.png`: The more important “diagram” is the board layout itself, moving left-to-right from geometric orientation to line element to metric matrix to coordinate bookkeeping; preserve this as a screenshot rather than trying to redraw the whole board.
- `lecture_04_figure_05.png`: This is not a geometric sketch but a two-zone board composition, with old geodesic machinery on the left and the local accelerated metric on the right; preserve it as a screenshot because the juxtaposition matters for note structure.
- `lecture_04_figure_05.png`: No TikZ redraw is needed for the board layout itself; the right-board content should instead be reconstructed as clean displayed equations.
- `lecture_04_figure_06.png`: This is a derivation map made of boxed equations rather than a literal figure; preserve it as a screenshot because it shows how Susskind staged the reduction from geodesic motion to a force law.
- `lecture_04_figure_06.png`: No TikZ figure is needed here; the mathematical content should be rendered as aligned equations, with the screenshot nearby as evidence for the boxed sequence.

## Reconstruction Guidance
- Use `lecture_04_figure_04.png` to anchor the spacetime pivot. The note-quality reconstruction should typeset the Minkowski line element, the tensor form \(d\tau^2=-g_{\mu\nu}dx^\mu dx^\nu\), the matrix \(\mathrm{diag}(-1,1,1,1)\), and the coordinate identifications exactly in the order the board presents them.
- Keep `lecture_04_figure_04.png` nearby whenever the chapter first fixes signature conventions. The screenshot is valuable not only for the equations but also for documenting that the lecture itself used the explicit minus sign in front of \(g_{\mu\nu}dx^\mu dx^\nu\).
- Use `lecture_04_figure_05.png` to reconstruct the local expansion around \(r=R+y\). The top two lines should be completed cautiously as the standard \(d\omega^2\) expansion, then simplified to the boxed first-order form \(d\tau^2\approx(1+2gy)dt^2-dy^2\).
- Treat the left side of `lecture_04_figure_05.png` as contextual carryover from the earlier geodesic machinery, not as the main new displayed mathematics of that subsection. A brief prose reminder is enough unless the derivation needs a forward reference.
- Use `lecture_04_figure_06.png` to reconstruct the Newtonian-limit derivation in a cleaned sequence: geodesic equation, slow-motion truncation to the \(tt\) term, Christoffel extraction, and final uniform-field result. The board preserves the lecture’s staging, but the final equations in the notes should be normalized with standard index placement and sign bookkeeping.
- Keep `lecture_04_figure_06.png` adjacent to the cleaned derivation because the board visibly compresses several intermediate steps. The screenshot shows the boxed logic, while the typeset equations should supply the legibility and convention control.
- Prefer displayed equations over board-replica graphics for `lecture_04_figure_05.png` and `lecture_04_figure_06.png`. The screenshots already carry the blackboard texture and sequencing; the reconstruction should focus on mathematical clarity.
- Do not invent missing terms beyond cautious standard completion already supported by the transcript and the visible chalk structure. In particular, avoid adding cross terms or extra coordinates that are not visible or motivated in these frames.

## Uncertainties
- In `lecture_04_figure_05.png`, the factors at the ends of the top two right-board lines are cropped, so \(d\omega^2\) and the final \(-dy^2\) are standard completions rather than directly legible chalk.
- In `lecture_04_figure_05.png`, the left-board boxed equations are partly cropped and partly blocked by Susskind, so only their general geodesic/parallel-transport form is secure from the image alone.
- In `lecture_04_figure_05.png`, the boxed lower-right approximation clearly begins \((1+2yg)dt^2-\), but the trailing term is cut off and should be restored cautiously as \(-dy^2\).
- In `lecture_04_figure_06.png`, the lower-left chalk line reads like \(\frac{d^2y}{d\tau^2}=+\frac{\partial g_{tt}}{\partial y}\), but the transcript around this moment contains live sign corrections and a factor-of-\(\tfrac12\) discussion. The final notes should therefore not copy that line verbatim without normalization.
- In `lecture_04_figure_06.png`, the partially hidden middle-right and lower-middle boxes are not legible enough to recover complete equations from the image alone.
- In `lecture_04_figure_04.png`, the matrix and coordinate list are clear, but the lecture’s overall sign convention must still be tracked carefully because the board uses \(d\tau^2=-g_{\mu\nu}dx^\mu dx^\nu\), not a notation-neutral presentation.
- The transcript outside these frames is garbled in several places, especially around the transition into accelerated coordinates and some hyperbolic-function explanations, so any standard completion should be checked against both the visible frame content and the local mathematical argument before being written into the final chapter.