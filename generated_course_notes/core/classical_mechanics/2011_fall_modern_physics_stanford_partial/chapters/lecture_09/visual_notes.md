# Visual Evidence
## Frame Inventory
- `lecture_09_figure_02.png`: Tight board crop showing a cropped product-rule line above and the clearly written special case \(\{P,P\}=0\) below, with Susskind pointing at it; this screenshot should remain in the final notes.
- `lecture_09_figure_03.png`: Local board shot showing the start of the claim \(\{F(q),P\}=\cdots\) as Susskind begins writing the right-hand side; this screenshot should remain in the final notes.

## Equation Extraction
- `lecture_09_figure_02.png`: \(\{P,P\}=0\) [visible]
- `lecture_09_figure_02.png`: \(\{AB,C\}=A\{B,C\}\) [partially visible]
- `lecture_09_figure_02.png`: \(\{AB,C\}=A\{B,C\}+B\{A,C\}\) [standard completion]

- `lecture_09_figure_03.png`: \(\{F(q),P\}=\) [partially visible]
- `lecture_09_figure_03.png`: \(\{F(q),P\}=\dfrac{dF}{dq}\) [standard completion]
- `lecture_09_figure_03.png`: \(\{F(q),P\}=\dfrac{\partial F}{\partial q}\) [standard completion]

## Diagram Extraction
- `lecture_09_figure_02.png` is not a geometric diagram; it is a board-layout moment in which the upper cropped line preserves the surrounding abstract algebra and the lower line isolates the concrete consequence \(\{P,P\}=0\). It should be preserved as a screenshot, not redrawn as TikZ.
- `lecture_09_figure_03.png` is also not a geometric figure; it is a derivation-in-progress board state showing the transition from bracket notation to differentiation language. It should be preserved as a screenshot, not redrawn as TikZ.
- No axes, arrows, state diagrams, or sketches are visible in these two frames, so there is no independent TikZ obligation here.

## Reconstruction Guidance
- Keep `lecture_09_figure_02.png` beside a clean displayed equation \(\{P,P\}=0\), since the frame is strong visual evidence for the lecture’s use of antisymmetry to force self-brackets to vanish.
- If the surrounding notes mention the product rule at that point, typeset the full rule cleanly as \(\{AB,C\}=A\{B,C\}+B\{A,C\}\), but make clear that only the first part is directly visible in the frame.
- Keep `lecture_09_figure_03.png` beside a cleaned statement of the result that bracketing a function of \(q\) with \(P\) differentiates it with respect to \(q\). The transcript supports this completion even though the right-hand side is not yet legible in the frame.
- Prefer using the screenshot as documentary evidence of lecture rhythm and board emphasis, while using typeset equations for the mathematically complete statement. These are screenshot-plus-equation figures, not screenshot-only figures.
- Do not invent extra intermediate board steps not visible in the frames. If a derivation is needed in the notes, reconstruct it from the transcript’s later verbal proof rather than from these images alone.

## Uncertainties
- In `lecture_09_figure_02.png`, the upper formula is cropped before the second term is visible, so the full product rule is reconstruction, not direct reading.
- In `lecture_09_figure_03.png`, the right-hand side has not yet been written clearly enough to read from the image alone.
- The variable in `lecture_09_figure_03.png` looks most like \(q\), but final letter case should follow the chapter’s normalized notation.
- The derivative notation in `lecture_09_figure_03.png` could be rendered as either \(dF/dq\) or \(\partial F/\partial q\); the frame itself does not settle that choice.
- Neither frame shows indices, so nothing about the indexed relation \(\{Q_i,P_j\}=\delta_{ij}\) should be inferred from the images themselves.