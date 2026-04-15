# Figure Notes
## Image Inventory
- `lecture_08_figure_01.png`: Stanford title card with the red block `S`, green tree emblem, the words “STANFORD UNIVERSITY,” and the URL `www.stanford.edu`. No classroom, blackboard, or mathematical content is visible.
- `lecture_08_figure_02.png`: Classroom frame with Leonard Susskind standing in front of a blue board. On the left are residual cosmology formulas including a clearly visible `M/a^3`, a visible `k/a^2`, and a boxed expression containing `H^2`. On the right are two simple horizontal chalk traces, one slightly wavy and one nearly straight.
- `lecture_08_figure_03.png`: Blackboard sketch of a qualitative potential-energy profile. The curve begins high on the left, slopes gently, drops steeply to a low point near the middle-right, and then rises again on the far right. A long horizontal reference line is drawn beneath the upper plateau. Susskind’s hand points below the main curve rather than covering the turning points.
- `lecture_08_figure_04.png`: Classroom frame with the left edge of the potential sketch still visible and, on the right, the exponential factor `e^{Ht}` clearly written. Above it there is a partial relation beginning with `H` and appearing to connect `H` to `V(\phi)` through a square root, but the formula is incomplete. Susskind stands in front of part of the board.
- `lecture_08_figure_05.png`: Tight board shot of the scalar-field equation-of-motion derivation. The middle line shows a total time derivative involving \(a(t)^3\dot\phi\), and the bottom line rewrites it as a damped equation with a `3H\dot\phi` term and a derivative of the potential on the right. The top line is a partial Lagrangian or Lagrangian-density expression.

## Blackboard Equations
- `lecture_08_figure_01.png`: No blackboard equations or lecture notation are present.

- `lecture_08_figure_02.png`:
  - \( \dfrac{M}{a^3} \) [visible]
  - \( \dfrac{k}{a^2} \) [visible]
  - \( H^2 \) [visible]
  - A boxed ratio or combination involving \(H^2\) and a curvature term, plausibly of the form \( -\dfrac{k/a^2}{H^2} \) or related normalized-curvature notation [partially visible]

- `lecture_08_figure_03.png`:
  - No secure equation text is legible.
  - The sketch is a qualitative potential profile, standardly read as \(V(\phi)\) [standard reconstruction]

- `lecture_08_figure_04.png`:
  - \( e^{Ht} \) [visible]
  - A partial relation beginning with \(H\) and appearing to involve a square root of the potential, plausibly \(H \propto \sqrt{V(\phi)}\) [partially visible]
  - The left-side curve is a residual piece of the potential sketch, standardly interpreted as part of \(V(\phi)\) [standard reconstruction]

- `lecture_08_figure_05.png`:
  - \( \dfrac{d}{dt}\bigl(a(t)^3\dot{\phi}\bigr) = -a^3 \dfrac{\partial V}{\partial \phi} \) [visible]
  - \( \ddot{\phi} + 3H\dot{\phi} = - \dfrac{\partial V}{\partial \phi} \) [visible]
  - A top partial Lagrangian-density line with an \(a^3\) factor and a \(\dot{\phi}^2/2\) term, plausibly \(L = a^3\!\left[\dfrac{\dot{\phi}^2}{2} - V(\phi)\right]\) [partially visible]
  - The top line may more properly be a Lagrangian density \(\mathcal{L}\) before multiplying by volume [standard reconstruction]

## Diagram And Layout Reading
- `lecture_08_figure_01.png` is purely an intro card and carries no lecture-board information.

- `lecture_08_figure_02.png` preserves board layout from the early \(\Omega\)-discussion. The left side contains dilution terms and a boxed normalized quantity, while the right side shows a small comparison sketch made of two horizontal traces. The image is useful mainly as documentary residue of the FRW/\(\Omega\) board, not as a self-sufficient figure for the dark-matter-dissipation passage.

- `lecture_08_figure_03.png` is the key diagrammatic figure. The important visual structure is:
  - a high left plateau with a gentle downward slope,
  - a cliff-like descent,
  - a low minimum near the center-right,
  - a rising right-hand branch,
  - and a long horizontal reference line under the upper part of the curve.
  No axis labels are securely visible, but the transcript makes clear that this is a potential-energy graph, with field value on the horizontal axis and potential energy vertically.

- `lecture_08_figure_04.png` is a mixed board-layout frame. It combines:
  - the left-hand remnant of the potential sketch,
  - a right-hand exponential growth formula \(e^{Ht}\),
  - and a partial top relation connecting \(H\) to the potential.
  It documents the lecture’s move from the potential picture to exponential expansion, but it is not as clean or self-contained as either the pure potential sketch or the later equation board.

- `lecture_08_figure_05.png` is a mathematical derivation board. The layout is sequential:
  - top: the Lagrangian/Lagrangian-density setup,
  - middle: Euler–Lagrange equation in total-derivative form,
  - bottom: simplified equation showing the \(3H\dot\phi\) “Hubble friction” term.
  This is strong equation evidence and does not need a diagram redraw.

## TeX Reconstruction Plan
- `lecture_08_figure_01.png` should not remain visible in the final notes. It is an intro card, not lecture evidence.

- `lecture_08_figure_02.png` is weak as a final-note figure. The board content is real, but it belongs to an earlier \(\Omega\)/curvature discussion and does not materially support the subtitle moment attached to it. The notes should prefer transcript-backed equations for the \(\Omega\)-section rather than keep this screenshot.

- `lecture_08_figure_03.png` must remain visible. It is the strongest screenshot evidence for the inflationary potential shape. It should be paired with a clean TikZ redraw nearby that shows:
  - a broad shallow plateau,
  - a steep drop,
  - a low minimum,
  - and a rising right branch.
  The redraw should be qualitative only, not an overfit of the chalk trace.

- `lecture_08_figure_04.png` is not strong enough to keep as a standalone final figure if the chapter is being curated tightly. Its useful content should instead be reconstructed directly in LaTeX:
  - a displayed relation of the form \(H \propto \sqrt{V(\phi)}\) or, with transcript-backed normalization, \(H=\sqrt{8\pi G V(\phi)/3}\),
  - and the exponential law \(a(t)\propto e^{Ht}\).
  If one wants extra documentary texture, it could appear as a secondary supporting screenshot, but it is not necessary once the equations are typeset cleanly.

- `lecture_08_figure_05.png` must remain visible. It should be paired with clean displayed equations nearby:
  - \(\dfrac{d}{dt}\bigl(a^3\dot\phi\bigr)=-a^3\dfrac{\partial V}{\partial\phi}\),
  - \(\ddot\phi+3H\dot\phi=-\dfrac{\partial V}{\partial\phi}\).
  If the chapter also introduces the Lagrangian explicitly, the top partial board line may be standardized cautiously as
  \(\mathcal{L}=a^3\left[\dfrac{1}{2}\dot\phi^2 - V(\phi)\right]\),
  but this should be presented as a cleaned reconstruction rather than a literal transcription of the cropped chalk.

## Caption Drafts
- `lecture_08_figure_01.png`: Stanford title card
- `lecture_08_figure_02.png`: Residual \(\Omega\)-board terms and \(H^2\)
- `lecture_08_figure_03.png`: Inflationary potential with plateau and minimum
- `lecture_08_figure_04.png`: Exponential growth beside the potential sketch
- `lecture_08_figure_05.png`: Scalar-field equation with Hubble friction

## Uncertainties
- `lecture_08_figure_01.png`: No mathematical uncertainty; the uncertainty is purely curatorial, namely that it should not be used at all in the notes.

- `lecture_08_figure_02.png`:
  - The boxed left-board expression is not fully legible.
  - The right-side horizontal traces are unlabeled and weakly diagnostic.
  - The frame appears to preserve earlier board residue rather than a clean visual match to the subtitle moment “But its potential energy can’t go anywhere.”

- `lecture_08_figure_03.png`:
  - Axis labels are not visibly secure.
  - The horizontal reference line may be part of the lecturer’s explanatory layout rather than an axis.
  - The exact local shape near the minimum should not be overinterpreted; only the plateau–cliff–minimum organization is robust.

- `lecture_08_figure_04.png`:
  - The top relation involving \(H\) and \(V(\phi)\) is incomplete and partly obscured.
  - The visible `123`-like chalk in the middle is not interpretable as secure mathematical notation.
  - This frame is best treated as documentary support for the transition from \(V(\phi)\) to exponential growth, not as a source for a literal equation transcription.

- `lecture_08_figure_05.png`:
  - The top Lagrangian/Lagrangian-density line is cropped and only partially legible.
  - The sign structure is legible in the lower equation, but the lecturer’s own spoken correction in the transcript shows that one should standardize the final sign only after checking the transcript.
  - The board writes ordinary \(L\) in places where the lecture discussion distinguishes energy density, Lagrangian density, and full Lagrangian; the final notes should regularize that carefully.