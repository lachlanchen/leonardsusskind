# Visual Evidence
## Frame Inventory
- `lecture_10_figure_01.png` shows the Stanford University title card with no blackboard content; it should not remain in the final notes.
- `lecture_10_figure_02.png` shows a mostly blank board with a single electric-field relation at the upper left; it should remain if the convention discussion is illustrated visually.
- `lecture_10_figure_03.png` shows a comparison board separating mechanical momentum, canonical momentum, and generic Lagrangian notation; it should remain.
- `lecture_10_figure_04.png` shows the simple particle Lagrangian written across the top of the board; it is optional and can be kept small or omitted.
- `lecture_10_figure_05.png` shows the same particle example at a later stage with the Hamiltonian sign flip developing, but the lecturer’s paper blocks part of the board; it usually should not remain unless continuity matters.
- `lecture_10_figure_06.png` shows the scalar-field Lagrangian, conjugate momentum, and Hamiltonian stacked on one board; it should remain.

## Equation Extraction
- `lecture_10_figure_02.png`: [visible] `\vec E_M=-\frac{\partial \vec A}{\partial t}`
- `lecture_10_figure_02.png`: [standard completion] `(\vec E_M)_i=-\frac{\partial A_i}{\partial t}+\partial_i A_0`

- `lecture_10_figure_03.png`: [visible] `P_m=m\dot X_m`
- `lecture_10_figure_03.png`: [visible] `L(q_i,\dot q_i)`
- `lecture_10_figure_03.png`: [partially visible] `P_c=\partial \cdots`
- `lecture_10_figure_03.png`: [standard completion] `p_i=\frac{\partial L}{\partial \dot q_i}`

- `lecture_10_figure_04.png`: [visible] `\frac12 m\dot x^2-V(x)`
- `lecture_10_figure_04.png`: [standard completion] `L=\frac12 m\dot x^2-V(x)`

- `lecture_10_figure_05.png`: [partially visible] `P=m\dot x`
- `lecture_10_figure_05.png`: [partially visible] `\frac12 m\dot x^2+V`
- `lecture_10_figure_05.png`: [standard completion] `H=p\dot x-L=\frac12 m\dot x^2+V(x)`

- `lecture_10_figure_06.png`: [visible] `\mathcal L=\frac12\dot\phi^2-\frac12\left(\frac{\partial\phi}{\partial x}\right)^2-V(\phi)`
- `lecture_10_figure_06.png`: [partially visible] `\Pi_\phi=\dot\phi`
- `lecture_10_figure_06.png`: [partially visible] `H=\int dx\left[\frac12\dot\phi^2+\frac12\left(\frac{\partial\phi}{\partial x}\right)^2+V(\cdot)\right]`
- `lecture_10_figure_06.png`: [standard completion] `H=\int dx\left[\frac12\dot\phi^2+\frac12\left(\frac{\partial\phi}{\partial x}\right)^2+V(\phi)\right]`

## Diagram Extraction
- No frame contains a true geometric diagram, axis sketch, or spacetime figure that needs mandatory TikZ redrawing.
- `lecture_10_figure_02.png` is worth preserving as a screenshot because the board is intentionally empty except for one term, which reflects the lecture’s step-by-step isolation of the electric-field definition.
- `lecture_10_figure_03.png` is worth preserving as a screenshot because its horizontal layout carries meaning: mechanical momentum appears first, canonical momentum is being introduced in the center, and `L(q_i,\dot q_i)` is set off to the right.
- `lecture_10_figure_05.png` does not justify TikZ and is visually weaker than typeset reconstruction; if used at all, it should be a small continuity screenshot rather than a primary figure.
- `lecture_10_figure_06.png` is worth preserving as a screenshot because the stacked board layout shows the lecture’s mechanics-to-field-theory progression: Lagrangian density at the top, conjugate momentum at left, Hamiltonian below.
- If a later chapter editor wants a cleaner pedagogical figure, it should be a supplementary schematic rather than a replacement for the screenshots; none of the attached frames requires a TikZ redraw at this stage.

## Reconstruction Guidance
- Use `lecture_10_figure_02.png` as evidence for the sign convention discussion, but typeset the full Maxwell-side definition next to it. The board only gives the time-derivative piece clearly; the gradient term should be supplied from the transcript, not claimed as visible chalk.
- Use `lecture_10_figure_03.png` to preserve the rhetorical contrast between kinds of momentum. The clean note version should typeset `p_i=\partial L/\partial \dot q_i`, while the screenshot shows that the lecturer introduced it as a comparison, not as an isolated final formula.
- For the particle example, let typeset equations do most of the work. `lecture_10_figure_04.png` can support the reset to `L=\frac12 m\dot x^2-V(x)`, but the canonical-momentum and Hamiltonian derivations should be reconstructed cleanly in prose and display math.
- Treat `lecture_10_figure_05.png` cautiously. It is better as corroboration of the sign flip from Lagrangian to Hamiltonian than as a source for exact transcription.
- Use `lecture_10_figure_06.png` as the main visual evidence for the scalar-field Hamiltonian discussion. The notes should typeset the Lagrangian density, the conjugate momentum, and the Hamiltonian in polished form, while the screenshot preserves the one-board analogy between particle mechanics and field theory.
- Preserve screenshot evidence where board layout matters most: `lecture_10_figure_02.png`, `lecture_10_figure_03.png`, and `lecture_10_figure_06.png`. For the rest, prefer clean TeX reconstruction over visual duplication.

## Uncertainties
- In `lecture_10_figure_02.png`, only the `-\partial_t\vec A` term is directly visible; the `+\nabla A_0` term is a cautious completion.
- In `lecture_10_figure_03.png`, the left-hand labels and the full canonical formula are partly blocked by the lecturer, so only the comparison structure is fully secure.
- In `lecture_10_figure_04.png`, the leading `L=` is not as secure visually as the main expression `\frac12 m\dot x^2-V(x)`.
- In `lecture_10_figure_05.png`, the lecturer’s paper obscures both the upper formula and part of the middle line, so exact chalk transcription is unreliable.
- In `lecture_10_figure_06.png`, the lower potential term is blurry enough that the still can suggest either `V(\phi)` or `V(x)`; the lecture context strongly supports `V(\phi)`.
- In `lecture_10_figure_06.png`, the left-middle conjugate-momentum line is partly hidden by the lecturer, so `\Pi_\phi=\dot\phi` is safer as a reconstruction than as a fully visible board transcription.