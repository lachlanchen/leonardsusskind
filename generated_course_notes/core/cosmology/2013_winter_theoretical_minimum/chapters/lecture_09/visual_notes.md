# Visual Evidence
## Frame Inventory
- `lecture_09_figure_02.png`: A sparse opening blackboard fragment showing the start of the Euler-Lagrange operator, with `d/dt` and the beginning of a script-`L` partial-derivative term; this should remain in the final notes as a small supporting screenshot, not as a standalone mathematical record.
- `lecture_09_figure_03.png`: A two-board view with leftover `V(\phi)` on the left and, on the right, the variational equation above the simplified field equation below; this should remain in the final notes because it preserves the move from formal mechanics to force-from-potential form.
- `lecture_09_figure_04.png`: A hybrid frame combining a potential sketch on the left with partial Lagrangian algebra on the right; this should remain in the final notes because the graph-plus-algebra juxtaposition is part of the lecture’s logic.
- `lecture_09_figure_05.png`: A comparison board showing the flat-space field equation on the left and the expanding-universe correction on the right, including the `3\dot a/a` and `3H` forms; this should remain in the final notes because the board layout itself explains the staged derivation.
- `lecture_09_figure_06.png`: A vertically organized Friedmann board with the general equation at top, scalar-field substitution in the middle, and a boxed potential-dominated expression at bottom; this should remain in the final notes because the box and pointing gesture mark the term Susskind wants emphasized.

## Equation Extraction
- `lecture_09_figure_02.png`
  - `[visible]` `\frac{d}{dt}`
  - `[visible]` `\partial \mathcal{L}`
  - `[standard completion]` `\frac{d}{dt}\!\left(\frac{\partial \mathcal{L}}{\partial \dot{\phi}}\right)=\frac{\partial \mathcal{L}}{\partial \phi}`

- `lecture_09_figure_03.png`
  - `[visible]` `V(\phi)`
  - `[partially visible]` `\frac{d}{dt}\!\left(\frac{\partial \mathcal{L}}{\partial \dot{\phi}}\right)=\frac{\partial \mathcal{L}}{\partial \phi}`
  - `[visible]` `\ddot{\phi}=-\frac{\partial V}{\partial \phi}`

- `lecture_09_figure_04.png`
  - `[visible]` `\phi`
  - `[partially visible]` `\mathcal{L}=`
  - `[partially visible]` `\frac{\dot{\phi}^{2}}{2}`
  - `[standard completion]` `\rho=\frac{\dot{\phi}^{2}}{2}+V(\phi)`
  - `[standard completion]` `\mathcal{L}=a^{3}(t)\left(\frac{\dot{\phi}^{2}}{2}-V(\phi)\right)`

- `lecture_09_figure_05.png`
  - `[partially visible]` `\frac{d}{dt}\!\left(\frac{\partial \mathcal{L}}{\partial \dot{\phi}}\right)=\frac{\partial \mathcal{L}}{\partial \phi}`
  - `[visible]` `\ddot{\phi}=-\frac{\partial V}{\partial \phi}`
  - `[partially visible]` `\frac{d}{dt}\!\left(a^{3}(t)\dot{\phi}\right)=-a^{3}\frac{\partial V}{\partial \phi}`
  - `[partially visible]` `\ddot{\phi}+3\dot{\phi}\frac{\dot a}{a}=-\frac{\partial V}{\partial \phi}`
  - `[standard completion]` `\ddot{\phi}+3H\dot{\phi}=-\frac{\partial V}{\partial \phi}`

- `lecture_09_figure_06.png`
  - `[partially visible]` `H^{2}=\left(\frac{\dot a}{a}\right)^{2}=\frac{8\pi G}{3}\rho`
  - `[partially visible]` `H^{2}=\left(\frac{\dot a}{a}\right)^{2}=\frac{8\pi G}{3}\left[\frac{\dot{\phi}^{2}}{2}+V(\phi)\right]`
  - `[visible]` `\sqrt{\frac{8\pi G}{3}V(\phi)}`
  - `[standard completion]` `H\approx\sqrt{\frac{8\pi G}{3}V(\phi)}`

## Diagram Extraction
- `lecture_09_figure_04.png` contains the one clear hand-drawn potential sketch in this set: vertical axis unlabeled, horizontal axis labeled `\phi`, and an undulating curve with a dip and rise. This is a good candidate to show both ways: preserve the screenshot as evidence, and optionally redraw a simplified TikZ version if the final notes need a clean schematic of the rolling field.
- `lecture_09_figure_05.png` is not a diagram in the usual sense, but its left-right board structure matters. It should be preserved as a screenshot, while the notes recast the same progression as a short sequence of displayed equations.
- `lecture_09_figure_06.png` is also primarily structural rather than pictorial: top general equation, middle substitution, bottom boxed approximation. It should be preserved as a screenshot, and the boxed approximation can be cleanly re-typeset nearby.
- `lecture_09_figure_02.png` and `lecture_09_figure_03.png` do not need TikZ redraws; their value is documentary rather than diagrammatic.
- No frame here supports the later caustics discussion visually, so any caustics figure in the final chapter would need to be a transcript-backed editorial redraw rather than a screenshot-derived reconstruction.

## Reconstruction Guidance
- Use the transcript to supply the full Euler-Lagrange equation wherever the frame only shows its beginning. The screenshot from `lecture_09_figure_02.png` should remain small and contextual, while the equation itself should be typeset cleanly.
- For `lecture_09_figure_03.png`, pair the screenshot with a clean two-line display: first the Euler-Lagrange equation, then `\ddot{\phi}=-\partial V/\partial\phi`. The image preserves the classroom continuity; the TeX carries the mathematical legibility.
- For `lecture_09_figure_04.png`, do not pretend the algebra is fully readable. Reconstruct the energy density and cosmological Lagrangian from the transcript, and treat the screenshot mainly as evidence for the potential sketch and the sign-change discussion.
- For `lecture_09_figure_05.png`, present the expanding-universe field equation in stages: `\frac{d}{dt}(a^{3}\dot\phi)=-a^{3}\partial V/\partial\phi`, then `\ddot\phi+3(\dot a/a)\dot\phi=-\partial V/\partial\phi`, then `\ddot\phi+3H\dot\phi=-\partial V/\partial\phi`. Keep the screenshot nearby because the board visibly compares the non-expanding and expanding cases side by side.
- For `lecture_09_figure_06.png`, typeset the full Friedmann equation, then the scalar-field substitution, then the potential-dominated approximation. Keep the screenshot because the boxed lower term and pointing gesture visually reinforce the lecture’s conceptual distinction: the expansion is driven by `V(\phi)` itself, not by its derivative.
- Normalize notation cautiously when the spoken transcript is sloppy. In particular, use `H=\dot a/a`, `\rho=\dot\phi^{2}/2+V(\phi)`, and the standard Euler-Lagrange denominator `\dot\phi`, but do not add extra formalism not motivated in the lecture.

## Uncertainties
- In `lecture_09_figure_02.png`, the denominator under the partial derivative is not visible at all; only the opening operator is secure.
- In `lecture_09_figure_03.png`, the top Euler-Lagrange line is partly obscured and cropped, so its full form is transcript-backed rather than frame-complete.
- In `lecture_09_figure_04.png`, the right-hand algebra is too partial to quote confidently beyond `\mathcal{L}=` and a visible `\dot\phi^{2}/2` fragment.
- In `lecture_09_figure_04.png`, the potential curve is only partially captured; its detailed shape should not be overinterpreted beyond “rolling down a nontrivial potential.”
- In `lecture_09_figure_05.png`, the right-hand sides of the expanding-universe equations are cut off in places; the fully written right-hand side must be supplied from the transcript and standard completion.
- In `lecture_09_figure_06.png`, the exact symbol before the boxed square-root expression is not securely visible, so `H\approx` should be treated as a cautious completion, not a literal transcription.
- The subtitle excerpt attached to `lecture_09_figure_06.png` mentions the derivative of the potential, but the frame itself more strongly supports the contrasting point that the potential energy enters the Friedmann equation.
- The transcript around 00:09:07–00:09:14 is garbled: it says “derivative of a Lagrangian with respect to the potential,” but the mathematics requires differentiation with respect to `\dot\phi`.
- The transcript around the Friedmann substitution repeats and corrupts lines; the clean scalar-field-energy form should be treated as transcript-guided reconstruction, not as a verbatim board reading.