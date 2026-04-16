# Figure Notes
## Image Inventory
- `lecture_01_figure_01.png`: a black title card with large white serif text reading “STANFORD UNIVERSITY” and a thin horizontal white line below; no lecture board, equations, or diagrams are present.
- `lecture_01_figure_02.png`: a mostly blank whiteboard with a vertical time axis labeled `t` and a horizontal space axis labeled `x`; Susskind is writing an equation on the right, and only the beginning `x =` is visible.
- `lecture_01_figure_03.png`: a spacetime diagram on the board with axes labeled `t` and `x`; a steep blue line from the origin is labeled `x=vt`, and a shallower green line also runs from the origin; Susskind is gesturing toward the blue worldline.
- `lecture_01_figure_04.png`: a cropped view of a more crowded board; the upper line includes light-ray equations, and below are Galilean-style transformation formulas; the left side is cut off and some terms are obscured by Susskind’s body and the crop.
- `lecture_01_figure_05.png`: a strong spacetime diagram with a marked origin, vertical `t` axis, horizontal `X` axis, two green 45-degree light rays, and several blue parallel worldlines; the first blue line is labeled `x=vt` and `x'=0`, and a neighboring one is labeled `x=vt+1`.
- `lecture_01_figure_06.png`: a two-board view; the left board contains older algebra with fractions and a circled result, while the right board presents the general transformation ansatz for `x'` and `t'`; the lower right equation is partly crossed by Susskind’s moving hand.

## Blackboard Equations
- `lecture_01_figure_01.png`: no blackboard equations or notation.
- `lecture_01_figure_02.png`: `$t$` [visible], `$x$` [visible], `$x = \cdots$` [partially visible], `$x = ct$` [standard reconstruction].
- `lecture_01_figure_03.png`: `$x = vt$` [visible], `$x = ct$` [standard reconstruction].
- `lecture_01_figure_04.png`: `$x = -ct$` [visible], `$x = ct$` [partially visible], `$x' = x - vt$` [partially visible], `$t' = t$` [partially visible].
- `lecture_01_figure_05.png`: `$t$` [visible], `$X$` [visible], `$x = vt$` [visible], `$x' = 0$` [visible], `$x = vt + 1$` [visible], `$x = vt + 2$` [standard reconstruction], `$x = t$` [standard reconstruction], `$x = -t$` [standard reconstruction].
- `lecture_01_figure_06.png`: `$x' = (x-vt)\,f(v)$` [visible], `$t' = (t-vx)\,g(v)$` [partially visible], `$x-vt = 2$` [visible], `$\frac{2v}{1-v^2}$` [partially visible], `$\frac{2}{1-v^2}$` [partially visible].

## Diagram And Layout Reading
- `lecture_01_figure_02.png` shows the initial board layout for the whole spacetime discussion: the axes are separated from the equation, with the diagram on the left and the analytic statement being written on the right.
- `lecture_01_figure_03.png` shows the basic comparison Susskind wants the reader to see: a shallower light trajectory and a steeper ordinary worldline on the same `x-t` plane. The board uses color to distinguish them, but the important structural contrast is geometric, not chromatic.
- `lecture_01_figure_04.png` is less a diagram than a transition board. It preserves the coexistence of two right/left-moving light-ray equations with the older Newtonian transformation assumptions beneath them.
- `lecture_01_figure_05.png` is the clearest diagrammatic board in the set. The origin is emphasized, the green rays give the light directions, and the blue parallel lines encode a family of moving observers or fixed-$x'$ trajectories. The labels are arranged above the blue lines rather than directly on the axes.
- `lecture_01_figure_06.png` is organized as “old algebra on the left, new ansatz on the right.” It is useful for showing how Susskind resets the derivation: the right board isolates the general form of the transformation, while the left board records the previous worked example.

## TeX Reconstruction Plan
- Screenshots that should remain visible in the chapter body: `lecture_01_figure_02.png`, `lecture_01_figure_03.png`, `lecture_01_figure_05.png`, and `lecture_01_figure_06.png`.
- `lecture_01_figure_01.png` should not remain as a mathematical figure in the chapter. If it is kept at all, it belongs only in front matter or course-opening material, not in the note body.
- `lecture_01_figure_02.png` should be paired with a clean displayed equation `$x=ct$` and a nearby TikZ spacetime sketch. The screenshot documents the board layout, but the full mathematical content is not yet written visibly enough to stand alone.
- `lecture_01_figure_03.png` should be paired with a clean TikZ redraw of the spacetime axes, the light ray, and the moving trajectory `$x=vt$`. The screenshot is useful as evidence of board geometry and label placement.
- `lecture_01_figure_04.png` should be treated as optional or secondary. If kept, it should be accompanied by reconstructed display math rather than relied on for legibility. If space is tight, omit the screenshot and keep only the reconstructed equations `$x=\pm ct$`, `$x'=x-vt$`, and `$t'=t$`.
- `lecture_01_figure_05.png` should remain visible and should also be redrawn in TikZ. This is the strongest board for the family of parallel worldlines, the light rays, and the identification of `$x'=0$`.
- `lecture_01_figure_06.png` should remain visible as documentary evidence for the general ansatz, but the equations themselves should be typeset cleanly as displayed math. The left-board algebra should not be reconstructed in full unless the surrounding prose explicitly needs that intermediate calculation.

## Caption Drafts
- `lecture_01_figure_01.png`: Stanford opening title card.
- `lecture_01_figure_02.png`: Spacetime axes as the light trajectory is introduced.
- `lecture_01_figure_03.png`: The moving observer’s worldline `$x=vt$`.
- `lecture_01_figure_04.png`: Light-ray equations with the Newtonian transformation law.
- `lecture_01_figure_05.png`: Parallel moving worldlines against the light rays.
- `lecture_01_figure_06.png`: General ansatz for the coordinate transformation.

## Uncertainties
- In `lecture_01_figure_02.png`, only the beginning `$x=$` is actually visible; the completion `$ct$` comes from the nearby lecture context, not from the frame alone.
- In `lecture_01_figure_03.png`, the green line is unlabeled in the image; identifying it as the light trajectory is context-based.
- `lecture_01_figure_04.png` is visually weak and may not match its subtitle window cleanly. The crop hides part of the top equation and makes the lower derived expressions unsafe to transcribe beyond the clearly legible formulas.
- In `lecture_01_figure_05.png`, the third blue worldline is unlabeled in the frame; `$x=vt+2$` is a cautious completion, not a direct reading.
- In `lecture_01_figure_05.png`, whether the green rays are written in the notes as `$x=\pm t$` or `$x=\pm ct$` should follow the local unit convention of the surrounding prose. The frame itself shows geometry, not the formula.
- In `lecture_01_figure_06.png`, the lower `$g(v)$` equation is partly crossed by motion blur from Susskind’s hand, and the left-board fractions are only partly legible.
- Across several frames, the handwritten use of uppercase `X` versus lowercase `x` is inconsistent. The cleaned notes should standardize notation while preserving the mathematical meaning.