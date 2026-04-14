# Figure Notes
## Image Inventory
- `lecture_06_figure_02.png`: Susskind stands to the left of a mostly clean right board. The board preserves a top `T-V` line from the double-pendulum calculation, written in angular-velocity notation, and a lower large equation for the `\theta` momentum equation.
- `lecture_06_figure_03.png`: The right board shows the Hamiltonian definition at the top and, below it, a boxed summary of Hamilton’s two first-order equations. Susskind is pointing at the first boxed relation.
- `lecture_06_figure_04.png`: The left board carries a hand-drawn phase-space sketch with crosshair axes, several nested closed curves, many dotted points, and one emphasized winding trajectory. Formula fragments are cropped at both the left and right edges.
- `lecture_06_figure_05.png`: This is the richest composite board state. The left side keeps the phase-space sketch and part of the Hamiltonian-side equations; the right side shows the harmonic-oscillator Lagrangian, an Euler-Lagrange line with `d/dt`, and a boxed second-order oscillator equation.

## Blackboard Equations
- `lecture_06_figure_02.png`: `T - V = \dot{\theta}^{\,2} + \frac{(\dot{\theta}-\dot{\alpha})^{2}}{2} + \dot{\theta}(\dot{\theta}-\dot{\alpha})\cos\alpha` [partially visible]
- `lecture_06_figure_02.png`: `\dot{P}_{\theta} = \frac{\partial L}{\partial \theta}` [visible]
- `lecture_06_figure_03.png`: `H = \sum_i \dot q_i p_i - L` [standard reconstruction]
- `lecture_06_figure_03.png`: `\delta H = \sum_i \dot q_i\,\delta p_i - \dot p_i\,\delta q_i` [standard reconstruction]
- `lecture_06_figure_03.png`: `\frac{\partial H}{\partial p_i} = \dot q_i` [visible]
- `lecture_06_figure_03.png`: `\frac{\partial H}{\partial q_i} = -\dot p_i` [visible]
- `lecture_06_figure_05.png`: `L = \frac{1}{2\omega}\dot q^{\,2} - \frac{\omega}{2}q^{2}` [partially visible]
- `lecture_06_figure_05.png`: `\frac{d}{dt}\!\left(\frac{\dot q}{\omega}\right) = -\omega q` [partially visible]
- `lecture_06_figure_05.png`: `\frac{\ddot q}{\omega} = -\omega q` [visible]
- `lecture_06_figure_05.png`: `\dot q = \omega p` [partially visible]
- `lecture_06_figure_05.png`: `\dot p = -\omega q` [standard reconstruction]
- `lecture_06_figure_05.png`: `\ddot q = -\omega^{2} q` [standard reconstruction]

## Diagram And Layout Reading
- `lecture_06_figure_02.png` is organized as a two-level board: an expanded `T-V` expression above, then the Euler-Lagrange momentum equation below. The empty lower board area helps show that the lecture has paused on a conceptual point about `\dot p`.
- `lecture_06_figure_03.png` is laid out as derivation above and boxed summary below. The box is important: it marks the transition from calculation to the canonical final form of Hamilton’s equations.
- `lecture_06_figure_04.png` is the main diagrammatic evidence. The sketch has horizontal and vertical axes through a central point, several nested closed loops, a marked point on an outer loop, many dotted sample points in the annular region, and a heavier orbit drawn across the family of curves. It reads as a phase-space portrait rather than a mechanical object in ordinary space.
- `lecture_06_figure_05.png` juxtaposes geometry and equations. The left board keeps the phase-space picture and Hamiltonian-side relations; the right board holds the oscillator Lagrangian and the second-order Euler-Lagrange form. The visual point is the equivalence between first-order motion in phase space and the usual second-order oscillator equation.

## TeX Reconstruction Plan
- `lecture_06_figure_02.png` must remain visible. Reconstruct the lower equation `\dot p_\theta = \partial L/\partial \theta` as a clean displayed equation nearby. The top `T-V` line should only be typeset cautiously, since the lecture itself had sign-convention discussion around the angular-velocity terms.
- `lecture_06_figure_03.png` must remain visible. Typeset the Hamiltonian definition and the boxed pair of Hamilton equations nearby as clean displayed mathematics. The screenshot is still worth keeping because it preserves the board hierarchy and Susskind’s emphasis.
- `lecture_06_figure_04.png` must remain visible. Add a nearby TikZ redraw of the phase-space portrait: central axes, nested closed trajectories, one emphasized orbit with direction, and scattered dots indicating a filled set of starting points or a phase-space fluid. The redraw should be cleaner than the board, but not more specific than the image warrants.
- `lecture_06_figure_05.png` must remain visible. Pair it with both displayed equations and a TikZ redraw. The equations should present the oscillator Lagrangian, the first-order Hamilton equations, and the resulting second-order equation. The TikZ should give a clean oscillator phase portrait. Do not let the redraw replace the screenshot, because the side-by-side board layout is part of the lecture’s argument.
- `lecture_06_figure_04.png` and `lecture_06_figure_05.png` should both be kept rather than merged conceptually: the former isolates the hand-drawn phase portrait, while the latter captures the explicit comparison between geometric flow and analytic equations.

## Caption Drafts
- `lecture_06_figure_02.png`: Double-pendulum `T-V` line and the `\dot p_\theta` equation.
- `lecture_06_figure_03.png`: Hamiltonian definition with the boxed Hamilton equations.
- `lecture_06_figure_04.png`: Phase-space sketch with nested closed trajectories.
- `lecture_06_figure_05.png`: Harmonic-oscillator flow beside Hamiltonian and Euler-Lagrange forms.

## Uncertainties
- `lecture_06_figure_02.png`: The final factor on the top line is cropped and only safely reads as a cosine term, most likely `\cos\alpha`. The `\dot\theta \pm \dot\alpha` sign convention was explicitly unstable elsewhere in the lecture, so this line should not be over-normalized from the screenshot alone. The board writes an uppercase `P_\theta`, though the prose notes may prefer lowercase canonical momentum.
- `lecture_06_figure_03.png`: The intermediate `\delta H` line is only partially legible and should be treated as supporting context, not as the primary visual evidence. The boxed equations are the reliable part.
- `lecture_06_figure_04.png`: The edge formulas are too cropped to trust. The important content is the diagram. The hand-drawn loops are irregular even though the lecture later speaks of circular oscillator motion, so the redraw should capture the conceptual phase portrait rather than literal wobble.
- `lecture_06_figure_05.png`: The left-board Hamilton equations are partly hidden by Susskind’s body. The right-board fractions are readable but not perfectly sharp. The step from `\ddot q/\omega = -\omega q` to `\ddot q = -\omega^2 q` is better taken from the transcript-backed standard completion than from the image alone.