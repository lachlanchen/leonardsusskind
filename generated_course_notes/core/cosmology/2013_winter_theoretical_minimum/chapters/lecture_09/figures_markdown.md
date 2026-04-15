# Figure Notes
## Image Inventory
- `lecture_09_figure_02.png`: A sparse blackboard fragment showing the opening of the Euler-Lagrange operator. The board visibly contains `d/dt` and the beginning of a partial-derivative expression involving a script `L`. No denominator is present in the frame, and the rest of the board is blank.
- `lecture_09_figure_03.png`: A two-board view. On the left board, `V(\phi)` is still visible from the earlier potential discussion. On the right board, the Euler-Lagrange equation is written above, and below it the scalar-field equation has been simplified to a Newton-like form with `\ddot{\phi}` and a derivative of `V`.
- `lecture_09_figure_04.png`: A mixed diagram-and-equation frame. The left board shows a hand-drawn potential curve against axes, with the horizontal axis marked `\phi`. On the right, only partial algebra is visible, including the beginning of a Lagrangian line and fragments of nearby terms; the lecturer is gesturing directly at this area.
- `lecture_09_figure_05.png`: A dense comparison board. The left side retains the flat-space Euler-Lagrange and force-from-potential form; the right side shows the expanding-universe scalar-field equation first in `a^3(t)\dot\phi` form and then in the `3\dot a/a` and `3H` rewrite.
- `lecture_09_figure_06.png`: A Friedmann-equation board. The top line gives `H^2` in terms of `(\dot a/a)^2` and energy density; the middle line substitutes the scalar-field energy density `\dot\phi^2/2 + V(\phi)`; the lower part boxes a square-root expression involving `V(\phi)`, which the lecturer is pointing at.

## Blackboard Equations
- `lecture_09_figure_02.png`
  - `\frac{d}{dt}` [visible]
  - `\partial \mathcal{L}` [visible]
  - `\frac{d}{dt}\!\left(\frac{\partial \mathcal{L}}{\partial \dot{\phi}}\right)=\frac{\partial \mathcal{L}}{\partial \phi}` [standard reconstruction]

- `lecture_09_figure_03.png`
  - `V(\phi)` [visible]
  - `\frac{d}{dt}\!\left(\frac{\partial \mathcal{L}}{\partial \dot{\phi}}\right)=\frac{\partial \mathcal{L}}{\partial \phi}` [partially visible]
  - `\ddot{\phi}=-\frac{\partial V}{\partial \phi}` [visible]

- `lecture_09_figure_04.png`
  - `\phi` [visible]
  - `\mathcal{L}=` [partially visible]
  - `\frac{\dot{\phi}^{2}}{2}` [partially visible]
  - `\rho=\frac{\dot{\phi}^{2}}{2}+V(\phi)` [standard reconstruction]
  - `\mathcal{L}=a^{3}(t)\left(\frac{\dot{\phi}^{2}}{2}-V(\phi)\right)` [standard reconstruction]

- `lecture_09_figure_05.png`
  - `\frac{d}{dt}\!\left(\frac{\partial \mathcal{L}}{\partial \dot{\phi}}\right)=\frac{\partial \mathcal{L}}{\partial \phi}` [partially visible]
  - `\ddot{\phi}=-\frac{\partial V}{\partial \phi}` [visible]
  - `\frac{d}{dt}\!\left(a^{3}(t)\dot{\phi}\right)=-a^{3}\frac{\partial V}{\partial \phi}` [partially visible]
  - `\ddot{\phi}+3\dot{\phi}\frac{\dot a}{a}=-\frac{\partial V}{\partial \phi}` [partially visible]
  - `\ddot{\phi}+3H\dot{\phi}=-\frac{\partial V}{\partial \phi}` [standard reconstruction]

- `lecture_09_figure_06.png`
  - `H^{2}=\left(\frac{\dot a}{a}\right)^{2}=\frac{8\pi G}{3}\rho` [partially visible]
  - `H^{2}=\left(\frac{\dot a}{a}\right)^{2}=\frac{8\pi G}{3}\left[\frac{\dot{\phi}^{2}}{2}+V(\phi)\right]` [partially visible]
  - `\sqrt{\frac{8\pi G}{3}V(\phi)}` [visible]
  - `H\approx \sqrt{\frac{8\pi G}{3}V(\phi)}` [standard reconstruction]

## Diagram And Layout Reading
- `lecture_09_figure_02.png` matters mainly as board rhythm: Susskind is starting from the operator itself, not yet from a finished equation. The blank surrounding space reinforces that this is the first stroke of the Euler-Lagrange reminder.
- `lecture_09_figure_03.png` has a clear left-right board logic: the leftover `V(\phi)` notation sits on one board while the right board carries the formal derivation and the simplified equation of motion. This helps the notes preserve the move from abstract variational form to force-from-potential form.
- `lecture_09_figure_04.png` is the one image in this set where the board is genuinely hybrid. The left board contains a potential sketch with a vertical axis and a horizontal axis labeled `\phi`; the curve undulates, with at least one visible dip and rise. The right side is algebraic, but only in fragments. The important visual fact is the juxtaposition of graph and sign-change discussion.
- `lecture_09_figure_05.png` is organized as a comparison board. Left: the non-expanding scalar-field equation. Right: the expanding-universe correction, first in derivative form and then rewritten to expose the Hubble-friction term. The board layout itself is useful evidence for presenting the derivation in stages.
- `lecture_09_figure_06.png` is vertically structured rather than diagrammatic: general Friedmann equation at top, scalar-field substitution in the middle, boxed potential-dominated approximation at bottom. The box is important; it visually marks the approximation Susskind wants emphasized.

## TeX Reconstruction Plan
- `lecture_09_figure_02.png` should remain visible, but only as a small supporting screenshot. The notes should typeset the full Euler-Lagrange equation beside it, because the frame itself is too incomplete to stand alone mathematically.
- `lecture_09_figure_03.png` should remain visible. Reconstruct the cleaned pair of displayed equations nearby: the Euler-Lagrange equation and the resulting `\ddot{\phi}=-\partial V/\partial\phi`. The screenshot carries the board continuity; the TeX should carry the legibility.
- `lecture_09_figure_04.png` should remain visible. Reconstruct the energy-density and Lagrangian formulas explicitly in displayed math, since the right-hand algebra is too partial in the image. A small TikZ redraw of the potential curve is justified if the chapter wants a clean schematic of the rolling field; otherwise the screenshot alone is enough for the visual.
- `lecture_09_figure_05.png` should remain visible. Reconstruct the expanding-universe scalar-field equation as a short displayed sequence:
  `\frac{d}{dt}(a^{3}\dot\phi)=-a^{3}\partial V/\partial\phi`,
  then
  `\ddot\phi+3(\dot a/a)\dot\phi=-\partial V/\partial\phi`,
  then
  `\ddot\phi+3H\dot\phi=-\partial V/\partial\phi`.
  The screenshot is useful because it shows these forms coexisting on the board.
- `lecture_09_figure_06.png` should remain visible. Reconstruct the Friedmann equation and the potential-dominated approximation in clean display math. Keep the screenshot because the boxed lower term and the pointing gesture help explain that the potential energy, not the potential derivative, is what drives the expansion.

## Caption Drafts
- `lecture_09_figure_02.png`: Opening Euler-Lagrange operator on the board
- `lecture_09_figure_03.png`: Field equation from the derivative of the potential
- `lecture_09_figure_04.png`: Potential sketch beside the energy-to-Lagrangian transition
- `lecture_09_figure_05.png`: Scalar-field equation with Hubble friction
- `lecture_09_figure_06.png`: Friedmann equation in the potential-dominated limit

## Uncertainties
- In `lecture_09_figure_02.png`, the denominator under the partial derivative is not visible at all; only the start of the operator is secure.
- In `lecture_09_figure_03.png`, the top Euler-Lagrange line is partly cropped and partly blocked by the lecturer, though the intended equation is clear.
- In `lecture_09_figure_04.png`, the right-hand algebra is the weakest in the set. The presence of `\mathcal L =` is plausible from the image, but most of the actual formula must be supplied from standard reconstruction supported by the transcript.
- In `lecture_09_figure_04.png`, the potential curve is only partially captured; the full shape beyond the frame should not be overinterpreted.
- In `lecture_09_figure_05.png`, the right-hand equations are cut off after the equals sign in places, so the full right-hand side should be supplied in typeset form, not claimed as fully legible from the screenshot.
- In `lecture_09_figure_06.png`, the leading symbol before the boxed square-root term is off-frame or obscured; the image securely supports the square-root expression in `V(\phi)`, but not the exact preceding equality or approximation sign.
- In `lecture_09_figure_06.png`, the subtitle line mentions the derivative of the potential, but this frame visually supports the contrasting statement about the potential energy itself entering the Friedmann equation more strongly than the derivative statement.