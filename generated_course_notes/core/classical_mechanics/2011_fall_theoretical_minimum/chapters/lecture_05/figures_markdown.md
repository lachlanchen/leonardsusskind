# Figure Notes
## Image Inventory
- `lecture_05_figure_02.png`: A clean board close-up showing the start of the calculation of the time derivative of the Lagrangian. The visible content is essentially `d/dt` applied to `L` with generalized-coordinate arguments in parentheses. No lecturer is blocking the board.
- `lecture_05_figure_03.png`: A summary board state with three stacked items: the general Lagrangian `L(q,\dot q,t)` at the top, the canonical momentum definition in the middle, and the start of a lower line beginning with `\dot P`. Susskind is at the left edge, writing the bottom line.
- `lecture_05_figure_04.png`: A single, legible equation on a mostly blank board: the time derivative of the Hamiltonian equals minus the explicit time derivative of the Lagrangian. Susskind stands to the right without obscuring the equation.
- `lecture_05_figure_05.png`: A wider two-board view. On the right board the equation `dH/dt = -\partial \mathcal{L}/\partial t` remains visible above a double-pendulum-style sketch with two rods and angle labels. On the left board there are cropped remnants of earlier summary formulas involving a conserved quantity `Q` and the Hamiltonian definition.
- `lecture_05_figure_06.png`: A close-up of the nonstandard-Lagrangian example. The left side still shows the potential term `-q^2/2`, while the right side shows the differentiated left-hand side `q^2\ddot q + 2q\dot q^2 =`. Only Susskind’s hand appears at the far right edge.

## Blackboard Equations
- `lecture_05_figure_02.png`: [visible] `\frac{d}{dt}L(q_i,\dot q_i)`
- `lecture_05_figure_02.png`: [standard reconstruction] `\frac{dL}{dt}=\sum_i \frac{\partial L}{\partial q_i}\dot q_i+\sum_i \frac{\partial L}{\partial \dot q_i}\ddot q_i`
- `lecture_05_figure_03.png`: [visible] `L(q,\dot q,t)`
- `lecture_05_figure_03.png`: [visible] `P=\frac{\partial L}{\partial \dot q}`
- `lecture_05_figure_03.png`: [visible] `\dot P`
- `lecture_05_figure_03.png`: [standard reconstruction] `\dot p_i=\frac{\partial L}{\partial q_i}`
- `lecture_05_figure_04.png`: [visible] `\frac{dH}{dt}=-\frac{\partial \mathcal{L}}{\partial t}`
- `lecture_05_figure_05.png`: [visible] `\frac{dH}{dt}=-\frac{\partial \mathcal{L}}{\partial t}`
- `lecture_05_figure_05.png`: [partially visible] `Q=\sum_i p_i f_i(q),\qquad \dot Q=0`
- `lecture_05_figure_05.png`: [partially visible] `H=\sum_i p_i \dot q_i-L`
- `lecture_05_figure_06.png`: [visible] `-\frac{q^2}{2}`
- `lecture_05_figure_06.png`: [visible] `q^2\ddot q+2q\dot q^2=`
- `lecture_05_figure_06.png`: [standard reconstruction] `\frac{\partial L}{\partial q}=q\dot q^2-q`
- `lecture_05_figure_06.png`: [standard reconstruction] `q^2\ddot q+2q\dot q^2=q\dot q^2-q`
- `lecture_05_figure_06.png`: [standard reconstruction] `q^2\ddot q+q\dot q^2=-q`

## Diagram And Layout Reading
- `lecture_05_figure_02.png`: The board is visually sparse. This functions as a setup frame for a derivation rather than a finished result. The large `d/dt` on the left and the parenthesized argument list on the right make the chain-rule structure visually clear.
- `lecture_05_figure_03.png`: The board is organized top-to-bottom as a recap: first the general form of the Lagrangian, then the definition of canonical momentum, then the motion equation being started underneath. This layout is useful because it shows Susskind compressing the whole formalism into a short summary.
- `lecture_05_figure_04.png`: The layout is a single isolated equation on an otherwise empty board. That isolation matters: it reads as a boxed takeaway even without an actual drawn box.
- `lecture_05_figure_05.png`: The important visual feature is the two-board continuity. The left board preserves earlier summary formulas, while the right board carries both the Hamiltonian time-dependence formula and a mechanical sketch. The lower-right sketch appears to be a double pendulum or linked pendulum: a top pivot, a first rod down to an intermediate mass, then a second rod to a lower mass, with vertical reference lines and angle labels near the rods.
- `lecture_05_figure_06.png`: The equation is spatially split across the board: an earlier potential term remains on the left, while the differentiated kinetic term is written on the right. That separation reflects the Euler-Lagrange comparison of different pieces of the Lagrangian rather than a single compact final equation.

## TeX Reconstruction Plan
- `lecture_05_figure_02.png` should remain visible, but the notes should not rely on the screenshot alone for the mathematics. Keep the screenshot as the visual cue for the start of the calculation and typeset the full chain-rule expansion as a displayed equation nearby.
- `lecture_05_figure_03.png` should remain visible because it captures the summary-board layout. Reconstruct the mathematics in display form as `L(q_i,\dot q_i,t)`, `p_i=\partial L/\partial \dot q_i`, and `\dot p_i=\partial L/\partial q_i`.
- `lecture_05_figure_04.png` should remain visible and the equation should also be typeset as a displayed formula. The screenshot is useful because the board presents the relation as a standalone conclusion.
- `lecture_05_figure_05.png` must remain visible. The right-board equation should be typeset again in display form, and the lower-right pendulum sketch should be redrawn in TikZ as a clean schematic nearby. The cropped left-board formulas should not be used as sole sources; if cited, they should be normalized from transcript-supported reconstruction.
- `lecture_05_figure_06.png` should remain visible because it shows the intermediate algebraic step rather than only the cleaned result. The notes should typeset both the visible intermediate line and the simplified final equation, making clear that the screenshot preserves the working step.

## Caption Drafts
- `lecture_05_figure_02.png`: Beginning the time-derivative calculation for the Lagrangian.
- `lecture_05_figure_03.png`: Lagrangian, canonical momentum, and the start of the Euler-Lagrange equation.
- `lecture_05_figure_04.png`: Hamiltonian change from explicit time dependence of the Lagrangian.
- `lecture_05_figure_05.png`: Hamiltonian time dependence beside a double-pendulum sketch.
- `lecture_05_figure_06.png`: Intermediate Euler-Lagrange algebra for the nonstandard Lagrangian example.

## Uncertainties
- In `lecture_05_figure_02.png`, the parenthesized argument list is clear in intent but not sharp enough to settle every subscript and punctuation mark from the image alone. The full chain-rule formula must come from transcript-supported reconstruction.
- In `lecture_05_figure_03.png`, the bottom line is only the beginning of the equation of motion. The completed form `\dot p_i=\partial L/\partial q_i` is a standard completion supported by the transcript, not fully written in the frame.
- In `lecture_05_figure_04.png` and `lecture_05_figure_05.png`, the letter on the right-hand side looks script-like. It is safest to normalize it to the chapter’s prevailing notation for the Lagrangian, whether `L` or `\mathcal{L}`.
- In `lecture_05_figure_05.png`, the left-board formulas are cropped and faint. They are useful contextual evidence but not reliable enough to serve as definitive standalone transcriptions.
- In `lecture_05_figure_05.png`, the lower angle labels are not perfectly sharp. The upper one is very plausibly `\theta`; the lower one is likely `\phi` or `\varphi`, but the exact handwritten form is not certain from the image alone.
- In `lecture_05_figure_06.png`, the right-hand side after the equals sign is off-frame. The visible board only supports the left-hand side and the existence of a right-hand side; the explicit completion must be taken cautiously from the transcript.
- In `lecture_05_figure_02.png`, the spoken subtitle about the potential and kinetic energy of the Lagrangian is not itself written on the board in this frame; visually the frame is about `dL/dt`, not a displayed `T-V` decomposition.