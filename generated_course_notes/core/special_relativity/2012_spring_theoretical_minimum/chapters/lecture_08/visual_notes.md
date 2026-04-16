# Visual Evidence
## Frame Inventory
- `lecture_08_figure_02.png`: tight board crop with the field-tensor definition and a second line identifying a mixed component with the electric field; this screenshot should remain in the final notes because it is the clearest direct evidence for the tensor definition.
- `lecture_08_figure_03.png`: Susskind writes the electric-field line beneath an already completed magnetic-field formula; this screenshot should remain because it captures the board transition from `\vec B` to `\vec E`, even though the lower line is unfinished.
- `lecture_08_figure_04.png`: clean grouped view of the two homogeneous Maxwell equations with minimal occlusion; this screenshot should remain because it is the best visual evidence for that paired board layout.
- `lecture_08_figure_05.png`: rhetorical overview frame with Susskind in front of two grouped Maxwell-equation blocks, source-free on the left and sourced on the right; this screenshot may remain if the notes want the lecture’s staging, but it should not be treated as a primary transcription source.
- `lecture_08_figure_06.png`: similar grouped-Maxwell frame during the move to tensor language, with slightly more board exposed than in figure 05; this screenshot is optional support and may remain if the chapter wants a second overview frame, though its mathematical content overlaps heavily with figure 05.

## Equation Extraction
- `lecture_08_figure_02.png`: `F_{\mu\nu}=\partial_{\mu}A_{\nu}-\partial_{\nu}A_{\mu}` [visible]
- `lecture_08_figure_02.png`: `F_{0n}=E_m` or `F_{0n}=E_n` [partially visible]
- `lecture_08_figure_02.png`: `F_{0n}=E_n` [standard completion]
- `lecture_08_figure_03.png`: `\vec B=\nabla\times\vec A` [visible]
- `lecture_08_figure_03.png`: `\vec E=` [partially visible]
- `lecture_08_figure_03.png`: `-E_x,\,-E_y,\,-E_z` as entries in a cropped field-tensor matrix fragment at the lower edge [partially visible]
- `lecture_08_figure_03.png`: `\vec E=\partial_t\vec A-\nabla A_0` [standard completion]
- `lecture_08_figure_04.png`: `\nabla\cdot\vec B=0` [visible]
- `lecture_08_figure_04.png`: `\nabla\times\vec E-\frac{\partial\vec B}{\partial t}=0` [visible]
- `lecture_08_figure_05.png`: `\nabla\cdot\vec B=0` [partially visible]
- `lecture_08_figure_05.png`: `\nabla\times\vec E-\frac{\partial\vec B}{\partial t}=0` [partially visible]
- `lecture_08_figure_05.png`: `\nabla\cdot\vec E=\rho` [partially visible]
- `lecture_08_figure_05.png`: `\nabla\times\vec B+\frac{\partial\vec E}{\partial t}=\vec J` [standard completion]
- `lecture_08_figure_06.png`: `\nabla\cdot\vec B=0` [partially visible]
- `lecture_08_figure_06.png`: `\nabla\times\vec E-\frac{\partial\vec B}{\partial t}=0` [partially visible]
- `lecture_08_figure_06.png`: `\nabla\cdot\vec E=\rho` [partially visible]
- `lecture_08_figure_06.png`: `\nabla\times\vec B+\frac{\partial\vec E}{\partial t}=\vec J` [standard completion]

## Diagram Extraction
- `lecture_08_figure_02.png` is not really a diagram; it should be preserved as a screenshot and paired with clean displayed equations, not redrawn in TikZ.
- `lecture_08_figure_03.png` is a transition frame rather than a finished figure; it should be preserved as a screenshot, and the mathematics should be typeset cleanly nearby rather than redrawn.
- `lecture_08_figure_04.png` shows a meaningful board grouping: one scalar equation above one vector equation, enclosed by a left grouping stroke; preserve the screenshot, but represent the mathematics in the notes as clean displayed equations instead of TikZ.
- `lecture_08_figure_05.png` and `lecture_08_figure_06.png` show the board split into two pedagogical blocks, homogeneous on the left and sourced on the right; preserve at least one screenshot if the chapter wants this board architecture, but do not redraw the hand-drawn boxes literally in TikZ.
- From this frame set alone, there is no clean geometric sketch that needs TikZ; the value here is equation state and board organization, not a polished diagram.

## Reconstruction Guidance
- Use `lecture_08_figure_02.png` as direct evidence for the displayed definition `F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu`, but reconstruct the lower component line cautiously from the transcript rather than copying the handwriting literally.
- Use `lecture_08_figure_03.png` to preserve the lecture rhythm: `\vec B=\nabla\times\vec A` is already on the board, and the electric-field formula is being unfolded underneath it. In the notes, typeset both formulas cleanly and normalize all hand-drawn vector arrows into standard notation.
- Use `lecture_08_figure_04.png` as the main screenshot for the homogeneous Maxwell pair, and reproduce the pair as clean displayed equations immediately nearby so the notes do not depend on handwriting legibility.
- Use `lecture_08_figure_05.png` and `lecture_08_figure_06.png` primarily as layout evidence for the full Maxwell system before tensor reformulation. The final notes should typeset all four equations cleanly; the screenshots are there to preserve the lecture’s board grouping and rhetorical transition.
- If figure count must be reduced, keep `lecture_08_figure_05.png` as the main overview frame and treat `lecture_08_figure_06.png` as optional support.
- Do not imitate the board calligraphy for arrows, `\nabla`, or grouping lines. Clean LaTeX should carry the mathematics; the screenshots should document the lecture moment.
- Prefer cautious standard completion only when the frame is clearly pointing to a standard formula already supported by the transcript, especially for the electric-field formula and the sourced Maxwell equation.

## Uncertainties
- In `lecture_08_figure_02.png`, the lower line is not fully reliable as written: the subscripts on both `F` and `E` are ambiguous, and the transcript shows Susskind verbally correcting indices around this moment.
- In `lecture_08_figure_02.png`, the exact sign convention linking `F_{0n}` to `E_n` should be checked against the lecture’s surrounding conventions rather than inferred from the handwriting alone.
- In `lecture_08_figure_03.png`, the lower electric-field line is incomplete in-frame, so the finished formula must come from the transcript, not from the screenshot alone.
- In `lecture_08_figure_03.png`, the cropped field-tensor matrix fragment is too partial to justify reconstructing the full matrix from this frame by itself.
- In `lecture_08_figure_05.png` and `lecture_08_figure_06.png`, the lower right sourced equation is not fully legible, especially the final `=\vec J`, and should be completed from the transcript.
- In `lecture_08_figure_05.png` and `lecture_08_figure_06.png`, parts of the left-hand lower homogeneous equation are blocked by Susskind, so these frames are better treated as layout evidence than as precise transcription sources.
- The hand-drawn board groupings in figures 04 through 06 indicate teaching structure, not formal mathematical bracketing, and should be preserved as exposition rather than copied literally.