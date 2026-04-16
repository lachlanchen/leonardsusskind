# Figure Notes
## Image Inventory
- `lecture_08_figure_02.png`: tight whiteboard crop showing the definition of the electromagnetic field tensor in terms of the vector potential. A second line below tries to identify a mixed time-space component with an electric-field component. Only a sliver of the lecturer is visible at the lower left.
- `lecture_08_figure_03.png`: Susskind is writing on the board. The upper line clearly gives the magnetic field as the curl of the vector potential. A lower line begins an electric-field formula after `\vec E =`, but the expression is still in progress. The bottom edge of the frame also catches part of an earlier field-tensor matrix.
- `lecture_08_figure_04.png`: the board displays the two source-free Maxwell equations as a grouped set. The equations are legible, and the hand-drawn grouping line at the left is visible. Susskind stands to the side and does not block the mathematics.
- `lecture_08_figure_05.png`: frontal shot of Susskind speaking with two grouped blocks of Maxwell equations behind him. The left block is the source-free pair; the right block is the sourced pair. The frame is more rhetorical than cleanly mathematical, but the board organization is still visible.
- `lecture_08_figure_06.png`: another frontal shot, with Susskind leaning forward so a bit more of the grouped Maxwell-equation layout is exposed. The right-hand sourced block is more readable than in the previous image, though the lecturer still obscures parts of the left block.

## Blackboard Equations
- `lecture_08_figure_02.png`: `F_{\mu\nu}=\partial_{\mu}A_{\nu}-\partial_{\nu}A_{\mu}` [visible]
- `lecture_08_figure_02.png`: `F_{0n}=E_{m}` or `F_{0n}=E_{n}` [partially visible]
- `lecture_08_figure_02.png`: `F_{0n}=E_n` [standard reconstruction]
- `lecture_08_figure_03.png`: `\vec B=\nabla\times\vec A` [visible]
- `lecture_08_figure_03.png`: `\vec E =` [partially visible]
- `lecture_08_figure_03.png`: `\vec E=\partial_t \vec A-\nabla A_0` [standard reconstruction]
- `lecture_08_figure_04.png`: `\nabla\cdot\vec B=0` [visible]
- `lecture_08_figure_04.png`: `\nabla\times\vec E-\frac{\partial \vec B}{\partial t}=0` [visible]
- `lecture_08_figure_05.png`: `\nabla\cdot\vec B=0` [partially visible]
- `lecture_08_figure_05.png`: `\nabla\times\vec E-\frac{\partial \vec B}{\partial t}=0` [partially visible]
- `lecture_08_figure_05.png`: `\nabla\cdot\vec E=\rho` [partially visible]
- `lecture_08_figure_05.png`: `\nabla\times\vec B+\frac{\partial \vec E}{\partial t}=\vec J` [standard reconstruction]
- `lecture_08_figure_06.png`: `\nabla\cdot\vec B=0` [partially visible]
- `lecture_08_figure_06.png`: `\nabla\times\vec E-\frac{\partial \vec B}{\partial t}=0` [partially visible]
- `lecture_08_figure_06.png`: `\nabla\cdot\vec E=\rho` [partially visible]
- `lecture_08_figure_06.png`: `\nabla\times\vec B+\frac{\partial \vec E}{\partial t}=\vec J` [standard reconstruction]

## Diagram And Layout Reading
- `lecture_08_figure_02.png` is not a diagram but a clean board-definition frame: one main defining equation, then a secondary component-identification line beneath it. It works as evidence for the lecture’s move from abstract tensor notation back to electric-field components.
- `lecture_08_figure_03.png` records a transition rather than a finished derivation. The layout matters: the already-finished magnetic relation sits above, and the electric-field relation is being introduced directly below it, with Susskind writing the first symbol after the equals sign.
- `lecture_08_figure_04.png` uses a left-side grouping stroke to present the source-free Maxwell pair as one block. This is useful for preserving the lecture rhythm: one scalar equation on top, one vector equation underneath.
- `lecture_08_figure_05.png` and `lecture_08_figure_06.png` both show the board split into two large grouped regions. The left region holds the “free” or identity-based equations, and the right region holds the sourced or dynamical equations. The exact box outlines are hand-drawn and informal, but the two-block organization is pedagogically important.
- In figures 03 through 06, the board uses hand-drawn arrows over `E`, `B`, and sometimes over `\nabla`. In the notes these should be normalized into standard vector notation rather than copied literally as board-calligraphy.
- The lower edge of `lecture_08_figure_03.png` preserves a fragment of the previously drawn field-tensor matrix, which helps signal that the Maxwell-equation discussion is still anchored to the tensor formalism already on the board.

## TeX Reconstruction Plan
- `lecture_08_figure_02.png` must remain visible. It is the cleanest direct board evidence for the defining relation `F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu`. The main equation should be reconstructed as a displayed equation immediately nearby. The lower component-identification line should be typeset separately in a cleaned standard form rather than trusted exactly as handwritten.
- `lecture_08_figure_03.png` should remain visible because it captures the lecture’s pivot from the magnetic relation to the electric-field relation. The screenshot should be paired with displayed equations for `\vec B=\nabla\times\vec A` and the completed electric-field formula from the transcript. No TikZ is needed.
- `lecture_08_figure_04.png` must remain visible. It is the clearest frame for the grouped homogeneous Maxwell equations. Both equations should also be reconstructed as displayed equations next to or below the screenshot so the notes do not depend on the handwriting.
- `lecture_08_figure_05.png` can remain visible as a rhetorical overview frame showing the full Maxwell system before tensor reformulation. The mathematics should not rely on the screenshot alone; all four equations should be typeset cleanly in LaTeX nearby.
- `lecture_08_figure_06.png` can remain visible as a second overview frame if the chapter wants to preserve Susskind’s staging of the two equation blocks while he says that `E` and `B` form an antisymmetric rank-two tensor and `J,\rho` form a four-vector. If figure count must be kept tight, this is the easiest frame to downweight, since its mathematical content overlaps heavily with figure 05.
- None of these images require TikZ reconstruction. What matters is equation cleanup and, for figures 04 through 06, preserving the two-block board organization in prose or layout rather than redrawing boxes.

## Caption Drafts
- `lecture_08_figure_02.png`: Definition of the electromagnetic field tensor on the board
- `lecture_08_figure_03.png`: From `\vec B=\nabla\times\vec A` to the electric-field formula
- `lecture_08_figure_04.png`: The source-free Maxwell equations as a grouped pair
- `lecture_08_figure_05.png`: Maxwell’s equations arranged in two board blocks before tensor reformulation
- `lecture_08_figure_06.png`: Grouped Maxwell equations during the move to tensor language

## Uncertainties
- In `lecture_08_figure_02.png`, the lower line is not fully trustworthy as written in the frame. The subscripts on both `F` and `E` are ambiguous, and the transcript suggests Susskind was verbally correcting indices around this moment.
- In `lecture_08_figure_03.png`, the electric-field expression is incomplete in the screenshot. The image supports the transition, but not a literal full transcription of the lower equation.
- In `lecture_08_figure_03.png`, the sign convention in the completed electric-field formula should be taken from the lecture transcript and surrounding conventions, not from the partially written board symbol alone.
- In `lecture_08_figure_05.png` and `lecture_08_figure_06.png`, the right-hand lower sourced equation is cropped or obscured enough that the final `=\vec J` is not cleanly readable in-frame and should be reconstructed from the transcript.
- In `lecture_08_figure_05.png` and `lecture_08_figure_06.png`, parts of the left-hand lower homogeneous equation are blocked by the lecturer, so these images are best read as layout evidence rather than as standalone transcription sources.
- The hand-drawn board groupings in figures 04 through 06 indicate pedagogical clustering, not exact mathematical bracketing; they should be preserved in exposition, not interpreted too literally as formal notation.