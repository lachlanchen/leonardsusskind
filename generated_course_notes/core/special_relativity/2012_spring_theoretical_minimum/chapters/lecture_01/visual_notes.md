# Visual Evidence
## Frame Inventory
- `lecture_01_figure_01.png`: a Stanford title card with no board mathematics or diagrams, so it should not remain in the final mathematical notes.
- `lecture_01_figure_02.png`: an initial spacetime board with axes labeled `t` and `x` on the left and the lecturer beginning to write `x =` on the right, and it should remain as visual evidence near the first light-ray discussion.
- `lecture_01_figure_03.png`: a spacetime diagram with a steep blue worldline labeled `x=vt` and a shallower green line from the origin, and it should remain in the final notes alongside a cleaned redraw.
- `lecture_01_figure_04.png`: a cropped transition board showing part of the light-ray equations and the older Galilean transformation formulas, and it should usually not remain except as optional documentary support.
- `lecture_01_figure_05.png`: the clearest spacetime-board frame, with axes, green light rays, and several blue parallel worldlines including labels `x=vt`, `x'=0`, and `x=vt+1`, and it should definitely remain in the final notes.
- `lecture_01_figure_06.png`: a two-board frame with older algebra on the left and the general transformation ansatz on the right, and it should remain as documentary evidence for the Lorentz-derivation setup.

## Equation Extraction
- `\text{Stanford University}` [visible] from `lecture_01_figure_01.png`, but this is title-card text rather than lecture mathematics.
- `t` [visible] from `lecture_01_figure_02.png`.
- `x` [visible] from `lecture_01_figure_02.png`.
- `x = \cdots` [partially visible] from `lecture_01_figure_02.png`.
- `x = ct` [standard completion] for `lecture_01_figure_02.png`, completed from the nearby transcript rather than the frame alone.
- `x = vt` [visible] from `lecture_01_figure_03.png`.
- `x = ct` [standard completion] for the green line in `lecture_01_figure_03.png`.
- `x = -ct` [visible] from `lecture_01_figure_04.png`.
- `x = ct` [partially visible] from `lecture_01_figure_04.png`.
- `x' = x - vt` [partially visible] from `lecture_01_figure_04.png`.
- `t' = t` [partially visible] from `lecture_01_figure_04.png`.
- `t` [visible] from `lecture_01_figure_05.png`.
- `X` [visible] from `lecture_01_figure_05.png`.
- `x = vt` [visible] from `lecture_01_figure_05.png`.
- `x' = 0` [visible] from `lecture_01_figure_05.png`.
- `x = vt + 1` [visible] from `lecture_01_figure_05.png`.
- `x = vt + 2` [standard completion] for the third blue worldline in `lecture_01_figure_05.png`.
- `x = t` [standard completion] for the right-moving light ray in `lecture_01_figure_05.png` if the notes have already switched to units with \(c=1\).
- `x = -t` [standard completion] for the left-moving light ray in `lecture_01_figure_05.png` under the same unit convention.
- `x' = (x-vt)\,f(v)` [visible] from `lecture_01_figure_06.png`.
- `t' = (t-vx)\,g(v)` [partially visible] from `lecture_01_figure_06.png`.
- `x - vt = 2` [visible] from the left board of `lecture_01_figure_06.png`.
- `\frac{2v}{1-v^2}` [partially visible] from the left board of `lecture_01_figure_06.png`.
- `\frac{2}{1-v^2}` [partially visible] from the left board of `lecture_01_figure_06.png`.

## Diagram Extraction
- `lecture_01_figure_02.png` documents the very first board layout: axes on the left, equation on the right. It should be shown both as the original screenshot and as a simple TikZ redraw of the first \(x\)-\(t\) light-ray picture.
- `lecture_01_figure_03.png` captures the contrast between the light trajectory and the moving observer’s worldline. It should be shown both ways: keep the screenshot, and redraw the diagram in TikZ with clear axes and labeled lines.
- `lecture_01_figure_04.png` is mostly useful as evidence that the light-ray equations and Galilean transformation appeared together on the same board. If used at all, preserve it only as a small documentary screenshot; the mathematics itself should be reconstructed from transcript and clean typesetting.
- `lecture_01_figure_05.png` is the strongest board figure for the family of moving worldlines and the light rays. It should be shown both ways, with the screenshot kept nearby and the geometry redrawn cleanly in TikZ.
- `lecture_01_figure_06.png` is not a diagram in the TikZ sense, but it is strong visual evidence for the derivation structure: previous worked algebra on the left, general ansatz on the right. It should remain as a screenshot, while the right-board equations are also typeset cleanly as displayed math.

## Reconstruction Guidance
- Use `lecture_01_figure_02.png` to preserve the lecturer’s board structure, but do not rely on it for the full equation; typeset `x=ct` cleanly from the transcript and place a simple spacetime sketch beside the screenshot.
- Use `lecture_01_figure_03.png` and `lecture_01_figure_05.png` as the main visual witnesses for the spacetime geometry. In the cleaned notes, redraw the axes, light rays, and moving worldlines in TikZ, but keep the screenshots adjacent so the redraw is visibly anchored to the lecture board.
- For `lecture_01_figure_05.png`, the transcript supports a full family of lines \(x=vt\), \(x=vt+1\), \(x=vt+2\); the screenshot only fully labels the first two. The redraw may include the full family, but the prose should signal that only part of the labeling is directly visible on the board.
- `lecture_01_figure_04.png` should not be treated as a transcription source beyond the clearest formulas. If the chapter needs the Newtonian transformation step, write the clean equations from transcript rather than from the cropped frame.
- `lecture_01_figure_06.png` should be used to justify the displayed ansatz
  \(x'=(x-vt)f(v)\), \(t'=(t-vx)g(v)\),
  but the left-board algebra should only be reconstructed if that specific intermediate calculation is used in the prose.
- Standardize notation in the cleaned notes even when the board varies between uppercase `X` and lowercase `x`. The final chapter should keep one consistent notation scheme and mention board inconsistency only if it matters historically or visually.
- When the chapter is already working in relativistic units, redraw light rays as \(x=\pm t\); if the section has not yet switched units, write \(x=\pm ct\). The screenshot itself does not settle that choice, so the surrounding prose must.

## Uncertainties
- In `lecture_01_figure_02.png`, only `x =` is directly visible; the completion to `x=ct` is transcript-based.
- In `lecture_01_figure_03.png`, the green line is unlabeled, so its identification as the light trajectory is a cautious contextual reading.
- `lecture_01_figure_04.png` is heavily cropped and partially blocked by the lecturer, so the top line and lower transformation formulas are not reliably legible in full.
- In `lecture_01_figure_05.png`, the third blue worldline is not labeled in the frame; `x=vt+2` is a standard completion from the lecture logic, not a direct visual transcription.
- In `lecture_01_figure_05.png`, the board uses uppercase `X` on the horizontal axis while nearby equations use lowercase `x`; this should be normalized in the notes.
- In `lecture_01_figure_06.png`, the lower right equation is crossed by motion blur from Susskind’s hand, so the full \(t'\)-equation is only partially visible.
- In `lecture_01_figure_06.png`, the left-board fractions are legible enough to suggest the algebraic pattern, but not enough to justify a line-by-line transcription without transcript support.
- The green-ray formulas in `lecture_01_figure_05.png` are not written on the board, so whether they appear in the notes as \(x=\pm t\) or \(x=\pm ct\) must follow the unit convention of the surrounding derivation.