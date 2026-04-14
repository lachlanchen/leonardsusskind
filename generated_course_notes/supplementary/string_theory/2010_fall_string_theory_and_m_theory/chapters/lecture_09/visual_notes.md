# Visual Evidence
## Frame Inventory
- `lecture_09_figure_02.png`: A large red circular sphere sketch with the label `R` near the upper-left arc and a small marked point near the top; this screenshot should remain in the final notes.
- `lecture_09_figure_03.png`: Susskind stands between two boards, with partial metric notation on the right board and leftover earlier material on the left; this screenshot should remain in the final notes.
- `lecture_09_figure_04.png`: A clean board-only shot of the Einstein-tensor equation ending in the stress tensor; this screenshot should remain in the final notes.
- `lecture_09_figure_05.png`: A live-writing frame showing `E=c|P|` near the top of the board, with the final absolute-value bar being completed; this screenshot should remain in the final notes.

## Equation Extraction
- `lecture_09_figure_02.png`: `R` [visible]
- `lecture_09_figure_03.png`: `g_{\mu\nu}(x)` [visible]
- `lecture_09_figure_03.png`: `\delta g_{\mu\nu}(x)=` [partially visible]
- `lecture_09_figure_03.png`: `\dfrac{L^2}{2I}` [partially visible]
- `lecture_09_figure_04.png`: `G_{\mu\nu}=R_{\mu\nu}-\dfrac{1}{2}g_{\mu\nu}R^{\alpha}{}_{\alpha}=T_{\mu\nu}` [visible]
- `lecture_09_figure_04.png`: `G_{\mu\nu}=R_{\mu\nu}-\dfrac{1}{2}g_{\mu\nu}R=T_{\mu\nu}` [standard completion]
- `lecture_09_figure_05.png`: `E=c|P|` [visible]

## Diagram Extraction
- `lecture_09_figure_02.png` should be shown both ways: keep the screenshot as visual evidence, and redraw the sphere cross-section in TikZ as a simple circle with the label `R` and, if useful, the small marked point near the top.
- `lecture_09_figure_03.png` is mainly board-structure evidence rather than a complete mathematical diagram. Preserve it as a screenshot, but do not attempt a full redraw of the partial equation from pixels alone.
- `lecture_09_figure_04.png` has no diagrammatic content; it should be preserved as a screenshot and paired with a clean typeset displayed equation.
- `lecture_09_figure_05.png` also does not need TikZ; preserve it as a screenshot and pair it with a clean typeset equation.
- No extracted frame here captures the later cylinder, torus, winding, or level-diagram sketches clearly enough to count as image-backed figures; any such diagrams in the notes would be transcript-backed reconstructions, not frame-backed redraws.

## Reconstruction Guidance
- Use `lecture_09_figure_02.png` to anchor the early sphere discussion visually. The TikZ redraw should stay minimal and faithful to the board: a circle, the radius label, and optionally the small top marker, but no invented radial segment or axis unless the transcript explicitly requires it nearby.
- Use `lecture_09_figure_03.png` only to support the appearance of the metric notation and the beginning of a variation/change equation. The clean note-quality formula for the flow of the geometry should come from the transcript and standard notation, not from over-reading the cropped board.
- Convert `lecture_09_figure_04.png` into a canonical displayed equation in the notes, with the screenshot nearby as evidence for board layout and emphasis. It is reasonable to simplify the traced curvature term from \(R^{\alpha}{}_{\alpha}\) to the standard scalar \(R\).
- Convert `lecture_09_figure_05.png` into a clean displayed relation \(E=c|P|\), keeping the screenshot nearby because the lecture is visually stressing the absolute value. If later notes switch to units with \(c=1\), that change should be declared in prose rather than silently imposed here.
- Treat the left-board material in `lecture_09_figure_03.png` as carry-over from the earlier sphere/moment-of-inertia discussion. It should not be merged into the Ricci-flow or metric-tensor argument.

## Uncertainties
- In `lecture_09_figure_02.png`, the label `R` is clear, but there is no drawn radial line, and the small point near the top is unlabeled.
- In `lecture_09_figure_03.png`, the leading symbol before `g_{\mu\nu}(x)` is very likely a change symbol such as `\delta`, but it is not fully reliable from the frame alone.
- In `lecture_09_figure_03.png`, the right-hand side of the partial equation is cut off, so the frame does not by itself justify a full flow equation.
- In `lecture_09_figure_03.png`, the partial `L^2/(2I)` and the wavy sketch on the left board are residual earlier content, not part of the metric discussion.
- In `lecture_09_figure_04.png`, the contraction on the scalar-curvature term is legible but chalk-rough; typesetting it as \(R\) is the safest clean normalization.
- In `lecture_09_figure_05.png`, the final absolute-value bar is being drawn during the frame, so the screenshot is a live-writing witness rather than a perfectly settled final board state.