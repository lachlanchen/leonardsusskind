# Figure Notes
## Image Inventory
- `lecture_03_figure_01.png`: black Stanford University title card with centered white serif text and a thin horizontal line below; no classroom, board, equations, or diagrammatic content.
- `lecture_03_figure_02.png`: Susskind is writing on a mostly clean whiteboard; the left side clearly shows `P_x =`, and on the right he is writing the beginning of a derivative/fraction expression while partially blocking it.
- `lecture_03_figure_03.png`: left board shows a vector momentum-balance equation ending in `= 0`; Susskind gestures toward it. The right board still contains an earlier low-velocity expansion with relativistic square-root terms and a visible `-m + mv^2/2` style endpoint.
- `lecture_03_figure_04.png`: nearly blank whiteboard with only `H =` written near the upper center; no completed Hamiltonian formula is present.
- `lecture_03_figure_05.png`: multi-board view. On the left is the nonrelativistic reminder `E = \frac12 mv^2 = \frac{p^2}{2m}`. On the right, higher on the board, there is a component relation involving \(m^2 u_0^2\) and spatial \(u_i^2\) terms, and centrally there is a clear invariant relation `E^2 - P^2 = m^2`.
- `lecture_03_figure_06.png`: Susskind stands in front of a board showing the earlier interval formula `\Delta \tau^2 = \Delta t^2 - \Delta x^2`; this is more of a talking-head plus carryover-board shot than a clean energy derivation frame.

## Blackboard Equations
- `lecture_03_figure_02.png`: \(P_x =\) [visible]
- `lecture_03_figure_02.png`: \(P_x = \frac{\partial L}{\partial \dot{x}}\) [standard reconstruction]
- `lecture_03_figure_03.png`: \(\vec{P}_{\mathrm{initial}} - \vec{P}_{\mathrm{final}} = 0\) [partially visible]
- `lecture_03_figure_03.png`: \(-m\sqrt{1-v^2}\) [partially visible]
- `lecture_03_figure_03.png`: \(-m\left(1-\frac{v^2}{2}\right)\) [partially visible]
- `lecture_03_figure_03.png`: \(-m + \frac{mv^2}{2}\) [partially visible]
- `lecture_03_figure_04.png`: \(H=\) [visible]
- `lecture_03_figure_04.png`: \(H=\sum_i \dot{x}_i\,p_i - L\) [standard reconstruction]
- `lecture_03_figure_05.png`: \(E=\frac12 mv^2\) [visible]
- `lecture_03_figure_05.png`: \(E=\frac{p^2}{2m}\) [visible]
- `lecture_03_figure_05.png`: \(m^2u_0^2 - m^2u_x^2 - m^2u_y^2 - m^2u_z^2 = m^2\) [partially visible]
- `lecture_03_figure_05.png`: \(u_0^2-\vec{u}^{\,2}=1\) [standard reconstruction]
- `lecture_03_figure_05.png`: \(E^2-P^2=m^2\) [visible]
- `lecture_03_figure_06.png`: \(\Delta \tau^2 = \Delta t^2 - \Delta x^2\) [visible]
- `lecture_03_figure_06.png`: \(E = m + \frac{mv^2}{2}\) [standard reconstruction]
- `lecture_03_figure_06.png`: \(E = \frac{m}{\sqrt{1-v^2}}\) [standard reconstruction]

## Diagram And Layout Reading
- `lecture_03_figure_01.png` has no pedagogical board layout; it is pure branding.
- `lecture_03_figure_02.png` is a close single-board writing shot. Its value is not spatial layout but the fact that Susskind is actively introducing canonical momentum from the Lagrangian definition.
- `lecture_03_figure_03.png` uses a two-board layout. The left board carries the new conceptual point, namely momentum conservation written as a vector equation. The right board retains the earlier nonrelativistic expansion, so the frame visually links the conservation-law discussion to the previous Lagrangian/energy approximation work.
- `lecture_03_figure_04.png` shows the start of a new section on a freshly cleared board. The layout signals a transition to the Hamiltonian, but the mathematics is not yet developed enough to be visually informative.
- `lecture_03_figure_05.png` also uses a two-board layout. The left board is a nonrelativistic reminder, while the right board holds the relativistic invariant relation. This side-by-side structure is useful: classical kinetic-energy formula on one side, relativistic mass-shell/four-velocity relation on the other.
- `lecture_03_figure_06.png` is dominated by Susskind’s face and torso; the visible board behind him is an older proper-time formula rather than the energy approximation named in the subtitle. As visual evidence, its layout is weak for the local moment.

## TeX Reconstruction Plan
- `lecture_03_figure_01.png` should not remain visible in the notes. Omit the screenshot entirely unless the project keeps title cards for archival reasons.
- `lecture_03_figure_02.png` may remain visible if the chapter wants one live board-writing frame for the canonical-momentum step, but the actual mathematics should be reconstructed nearby as a clean displayed equation:
  \[
  P_x=\frac{\partial L}{\partial \dot{x}}.
  \]
- `lecture_03_figure_03.png` should remain visible. It captures the board moment where momentum conservation is explicitly reframed as a vector equation. Reconstruct the equation as clean display math next to or below the screenshot, and do not rely on the screenshot for precise typography.
- `lecture_03_figure_04.png` should not remain visible as a figure. It is better treated as a transition point in prose, with the Hamiltonian formula typeset directly:
  \[
  H=\sum_i \dot{x}_i p_i - L.
  \]
- `lecture_03_figure_05.png` should remain visible if the notes want one frame that preserves the board juxtaposition of classical and relativistic formulas. Reconstruct the invariant relations cleanly in display math, especially
  \[
  u_0^2-\vec{u}^{\,2}=1,\qquad E^2-P^2=m^2.
  \]
  The left-board nonrelativistic energy reminder can also be typeset if it is discussed locally.
- `lecture_03_figure_06.png` should probably not remain visible. The nearby mathematics should instead be reconstructed directly in LaTeX as the low-velocity expansion of relativistic energy, using the transcript rather than this weak frame as the main support.
- No TikZ reconstruction is needed from these six images. They are equation-driven board moments rather than geometric diagrams.

## Caption Drafts
- `lecture_03_figure_01.png`: Stanford University title card.
- `lecture_03_figure_02.png`: Canonical momentum defined from the Lagrangian.
- `lecture_03_figure_03.png`: Momentum conservation written as a vector equation.
- `lecture_03_figure_04.png`: Beginning the Hamiltonian definition.
- `lecture_03_figure_05.png`: Four-velocity norm and relativistic energy-momentum invariant.
- `lecture_03_figure_06.png`: Carryover proper-time board near the energy discussion.

## Uncertainties
- `lecture_03_figure_02.png`: the right-hand side is blocked by Susskind’s hand and body; the intended expression is strongly suggested, but the fraction structure itself is only partially visible.
- `lecture_03_figure_03.png`: the vector labels on initial and final momentum are not perfectly crisp, though the overall equation structure is clear.
- `lecture_03_figure_03.png`: the right-board expansion is only partly legible and should not be transcribed beyond the visibly safe pieces unless the transcript is used to standardize it.
- `lecture_03_figure_04.png`: only `H=` is actually present; any fuller Hamiltonian formula is a transcript-backed reconstruction, not image-level evidence.
- `lecture_03_figure_05.png`: the upper-right component equation is partly occluded and faint; the cleanest reliable invariant on the board is \(E^2-P^2=m^2\), while \(u_0^2-\vec{u}^{\,2}=1\) is better treated as cautious standard completion.
- `lecture_03_figure_06.png`: the image does not visibly support the subtitle claim about \(E=m+\frac{mv^2}{2}\); it mainly shows the proper-time formula, so it should not be used as primary evidence for the energy expansion.