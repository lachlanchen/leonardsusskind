# Figure Notes
## Image Inventory
- `lecture_10_figure_01.png` shows the black Stanford University title card with centered white serif lettering and a thin horizontal rule; there is no lecturer, no board, and no mathematical content.
- `lecture_10_figure_02.png` shows a mostly blank blue board with a single equation written at the upper left, relating the electric field to the time derivative of the vector potential; Susskind stands at the left edge holding notes.
- `lecture_10_figure_03.png` shows a comparison board for different notions of momentum: a top mechanical-momentum relation, a partially written canonical-momentum relation in the middle, and `L(q_i,\dot q_i)` on the right; the lecturer is writing in the center.
- `lecture_10_figure_04.png` shows the single-particle Lagrangian `\frac12 m\dot x^2 - V(x)` written large across the top of the board; the rest of the board is mostly empty, with only faint cropped remnants at the far right.
- `lecture_10_figure_05.png` shows the same particle-mechanics board at a later moment: the top Lagrangian is still present, `P=m\dot x` appears in the middle, and a lower positive-energy expression is visible at lower right; the lecturer’s paper partly occludes the upper formula.
- `lecture_10_figure_06.png` shows a fuller field-theory board: a scalar-field Lagrangian at the top, a conjugate-momentum relation at left-middle, and a Hamiltonian integral across the lower half with a positive potential term; some older formulas remain cropped at the far right.

## Blackboard Equations
- `lecture_10_figure_02.png`: [visible] `\vec E_M=-\frac{\partial \vec A}{\partial t}`
- `lecture_10_figure_02.png`: [standard reconstruction] `(\vec E_M)_i=-\frac{\partial A_i}{\partial t}+\partial_i A_0`
- `lecture_10_figure_03.png`: [visible] `P_m=m\dot X_m`
- `lecture_10_figure_03.png`: [visible] `L(q_i,\dot q_i)`
- `lecture_10_figure_03.png`: [partially visible] `P_c=\partial \cdots`
- `lecture_10_figure_03.png`: [standard reconstruction] `p_i=\frac{\partial L}{\partial \dot q_i}`
- `lecture_10_figure_04.png`: [visible] `L=\frac12 m\dot x^2-V(x)`
- `lecture_10_figure_05.png`: [partially visible] `L=\frac12 m\dot x^2-V(x)`
- `lecture_10_figure_05.png`: [visible] `P=m\dot x`
- `lecture_10_figure_05.png`: [partially visible] `\frac12 m\dot x^2+V`
- `lecture_10_figure_05.png`: [standard reconstruction] `H=p\dot x-L=\frac12 m\dot x^2+V(x)`
- `lecture_10_figure_06.png`: [visible] `\mathcal L=\frac12 \dot\phi^2-\frac12\left(\frac{\partial \phi}{\partial x}\right)^2-V(\phi)`
- `lecture_10_figure_06.png`: [visible] `\Pi_\phi=\dot\phi`
- `lecture_10_figure_06.png`: [partially visible] `H=\int dx\left[\frac12 \dot\phi^2+\frac12\left(\frac{\partial \phi}{\partial x}\right)^2+V(\cdot)\right]`
- `lecture_10_figure_06.png`: [standard reconstruction] `H=\int dx\left[\frac12 \dot\phi^2+\frac12\left(\frac{\partial \phi}{\partial x}\right)^2+V(\phi)\right]`

## Diagram And Layout Reading
- `lecture_10_figure_01.png` has no board layout value for the chapter; it is pure title-card material.
- `lecture_10_figure_02.png` records the start of a new board panel: one compact equation is placed at the extreme upper left, leaving the rest of the board blank. That emptiness matters, because the lecture is isolating one term in the electric-field definition before rebuilding the full expression verbally.
- `lecture_10_figure_03.png` has a useful comparison layout. The board is organized horizontally: mechanical momentum above and slightly left, canonical momentum being developed in the center, and the generic Lagrangian dependence written separately on the right. This spatial separation helps the notes preserve the “different notions of momentum” rhythm.
- `lecture_10_figure_04.png` is not a diagram but an isolated top-strip formula. Its value is mainly documentary: the lecture has reset to the simplest particle Lagrangian before deriving canonical momentum and Hamiltonian.
- `lecture_10_figure_05.png` has a vertical progression rather than a diagram. The top line is the Lagrangian, the middle line gives the momentum, and the lower-right line shows the positive-energy combination. This is useful as a board-layout cue for the sign flip from Lagrangian to Hamiltonian.
- `lecture_10_figure_06.png` has the strongest field-theory layout. The top line gives the scalar-field Lagrangian density, the left-middle gives the conjugate momentum, and the lower line gives the Hamiltonian as a space integral. This stacked layout is valuable for note writing because it shows the mechanics-to-field-theory analogy on a single board.

## TeX Reconstruction Plan
- `lecture_10_figure_01.png` should not remain as a body figure in the chapter. It can be omitted entirely from the notes, or at most treated as front-matter video metadata outside the mathematical narrative.
- `lecture_10_figure_02.png` should remain visible if the chapter keeps a brief visual record of the convention discussion. The nearby TeX should reconstruct the full Maxwell-side electric-field definition as a displayed equation, not just the isolated `-\partial_t\vec A` term visible on the board.
- `lecture_10_figure_03.png` should remain visible. Its board layout helps communicate that mechanical momentum, canonical momentum, and Lagrangian dependence are being distinguished before the formal definition is completed. The displayed equation nearby should be the clean typeset formula `p_i=\partial L/\partial \dot q_i`.
- `lecture_10_figure_04.png` does not need to carry much visual weight by itself. The main work should be done by a clean displayed equation for `L=\frac12 m\dot x^2-V(x)` and then the canonical-momentum relation. The screenshot can be kept small or dropped if the chapter needs to reduce visual redundancy.
- `lecture_10_figure_05.png` is the weakest of the mathematics screenshots because the paper partly blocks the board and it overlaps strongly with `lecture_10_figure_04.png`. The notes should primarily reconstruct the Hamiltonian sign flip in TeX. Keep the screenshot only if board continuity is desired; otherwise it can be replaced by typeset equations.
- `lecture_10_figure_06.png` should remain visible. It is the clearest board witness for the scalar-field Hamiltonian with a positive potential term. The nearby TeX should typeset both the Lagrangian density and the Hamiltonian integral cleanly.
- No attached image requires TikZ reconstruction. All useful content here is equation-based and should be reconstructed as displayed mathematics rather than redrawn diagrams.

## Caption Drafts
- `lecture_10_figure_01.png`: Stanford University title card
- `lecture_10_figure_02.png`: Electric field from the time derivative of the vector potential
- `lecture_10_figure_03.png`: Canonical momentum as a derivative of the Lagrangian
- `lecture_10_figure_04.png`: Particle Lagrangian for the one-coordinate example
- `lecture_10_figure_05.png`: From particle Lagrangian to positive-energy Hamiltonian
- `lecture_10_figure_06.png`: Scalar-field Hamiltonian with positive potential term

## Uncertainties
- In `lecture_10_figure_02.png`, the board itself only shows the time-derivative term. The full `+\nabla A_0` piece is not visible in the frame and should be treated as transcript-supported completion, not direct board transcription.
- In `lecture_10_figure_03.png`, the left-side labels are partly blocked by the lecturer, and the canonical formula is only being started in the frame. The full derivative formula is a standard completion from the lecture context rather than a fully visible board line.
- In `lecture_10_figure_04.png`, faint cropped writing at the far right is not reliable enough to use.
- In `lecture_10_figure_05.png`, the lecturer’s paper obscures part of the top formula, and the lower positive-energy expression is incomplete on the board. It clearly points toward the Hamiltonian sign flip, but the exact full line should be reconstructed cautiously.
- In `lecture_10_figure_06.png`, the last argument of the potential term is not perfectly crisp in the lower Hamiltonian line. The lecture context strongly suggests `V(\phi)`, but the chalk can momentarily look like `V(x)` in the still frame.
- In `lecture_10_figure_06.png`, the far-right remnants such as `A=\int dt\cdots` and `\Pi(x)=\cdots` are cropped and should not be used as primary evidence.