# Visual Evidence
## Frame Inventory
- `lecture_06_figure_02.png`: Right-board double-pendulum work with a top `T-V` line and a lower momentum-form Euler-Lagrange equation for `\theta`; this screenshot should remain in the final notes.
- `lecture_06_figure_03.png`: Hamiltonian derivation board with the definition of `H` above and a boxed pair of Hamilton equations below; this screenshot should remain in the final notes.
- `lecture_06_figure_04.png`: Left-board phase-space sketch with nested closed curves, dotted sample points, and a heavier overdrawn trajectory, plus only cropped formula fragments at the edges; this screenshot should remain in the final notes.
- `lecture_06_figure_05.png`: Combined board state showing the phase-space picture on the left and the oscillator Lagrangian and Euler-Lagrange line on the right; this screenshot should remain in the final notes.

## Equation Extraction
- `lecture_06_figure_02.png`: `T - V = \dot{\theta}^{\,2} + \frac{(\dot{\theta}-\dot{\alpha})^{2}}{2} + \dot{\theta}(\dot{\theta}-\dot{\alpha})\cos\alpha` [partially visible]
- `lecture_06_figure_02.png`: `\dot{P}_{\theta} = \frac{\partial L}{\partial \theta}` [visible]
- `lecture_06_figure_03.png`: `H = \sum_i \dot q_i p_i - L` [partially visible]
- `lecture_06_figure_03.png`: `\delta H = \sum_i \dot q_i\,\delta p_i - \dot p_i\,\delta q_i` [standard completion]
- `lecture_06_figure_03.png`: `\frac{\partial H}{\partial p_i} = \dot q_i` [visible]
- `lecture_06_figure_03.png`: `\frac{\partial H}{\partial q_i} = -\dot p_i` [visible]
- `lecture_06_figure_05.png`: `\dot q = \omega p` [partially visible]
- `lecture_06_figure_05.png`: `\dot p = -\omega q` [standard completion]
- `lecture_06_figure_05.png`: `L = \frac{1}{2\omega}\dot q^{\,2} - \frac{\omega}{2}q^{2}` [partially visible]
- `lecture_06_figure_05.png`: `\frac{d}{dt}\!\left(\frac{\dot q}{\omega}\right) = -\omega q` [partially visible]
- `lecture_06_figure_05.png`: `\frac{\ddot q}{\omega} = -\omega q` [visible]
- `lecture_06_figure_05.png`: `\ddot q = -\omega^{2}q` [standard completion]

## Diagram Extraction
- `lecture_06_figure_02.png`: No standalone diagram, but the board structure matters: an expanded `T-V` line above and the `\dot p_\theta` equation below. Preserve the screenshot rather than redrawing the layout.
- `lecture_06_figure_03.png`: No geometric diagram, but the box around Hamilton’s equations is visually important. Preserve the screenshot and typeset the boxed equations cleanly nearby.
- `lecture_06_figure_04.png`: Redraw this as TikZ and also keep the screenshot. The figure is a phase-space portrait with horizontal and vertical axes crossing at a central point, several nested closed curves, many dotted points filling part of the annular region, one dark marked point on an outer curve, and one heavier trajectory drawn across the family of orbits.
- `lecture_06_figure_05.png`: Show both the screenshot and a TikZ redraw. The left side repeats the phase-space portrait idea, while the right side visually pairs first-order Hamiltonian motion with the second-order oscillator equation.

## Reconstruction Guidance
- For `lecture_06_figure_02.png`, keep the screenshot and typeset the lower equation `\dot p_\theta=\partial L/\partial\theta` as the clean note version. The upper `T-V` line can be reproduced only with a caution that its sign convention is lecture-local and partly contested in the transcript.
- For `lecture_06_figure_03.png`, use the screenshot as evidence for the derivation-to-summary transition, then typeset `H=\sum_i \dot q_i p_i-L` and the boxed Hamilton equations in clean display form. The screenshot is useful because the box and Susskind’s gesture reinforce that this is the final canonical form.
- For `lecture_06_figure_04.png`, do not try to extract edge equations from the crop. Use the screenshot as visual evidence, and redraw only the phase-space geometry: axes, nested closed trajectories, scattered points, and one emphasized path.
- For `lecture_06_figure_05.png`, keep the screenshot because the side-by-side board arrangement is itself part of the lecture’s argument. Reconstruct nearby the oscillator Lagrangian, the Hamilton equations, and the resulting second-order equation, and pair them with a clean TikZ phase portrait.
- In prose and typeset equations, it is reasonable to normalize notation to lowercase canonical momentum `p`, but the screenshot evidence should still note that the board in `lecture_06_figure_02.png` writes uppercase `P_\theta`.
- Prefer transcript-backed standard completion only where the image clearly points to a familiar formula but the crop or obstruction prevents full legibility.

## Uncertainties
- `lecture_06_figure_02.png`: The last factor on the top line is cropped; it reads like a cosine term, most likely `\cos\alpha`, but the exact completion should be treated cautiously. The `\dot\theta \pm \dot\alpha` convention is explicitly unstable in the lecture discussion.
- `lecture_06_figure_03.png`: The top Hamiltonian definition is not fully unobstructed at the far right, and the intermediate `\delta H` line is only partly legible. The boxed equations are the secure visual content.
- `lecture_06_figure_04.png`: The marginal formula fragments are too cropped to trust. The closed curves are hand-drawn and not perfectly circular, so a redraw should capture the phase-space idea rather than literal board wobble.
- `lecture_06_figure_05.png`: The left-board second Hamilton equation is partly blocked by Susskind’s body. On the right board, the Lagrangian and `d/dt` line are readable in structure but not sharp enough to rely on for every symbol without transcript support.
- Across these frames, the geometry is more reliable than the cropped peripheral algebra. The safest reconstructions are the boxed Hamilton equations, `\dot p_\theta=\partial L/\partial\theta`, and the oscillator equation `\ddot q=-\omega^2 q`.