# Visual Evidence
## Frame Inventory
- `lecture_04_figure_02.png`: Shows the lower-board transition from matrix language to index language, with `g^{-1}g=I` above a boxed inverse-metric contraction identity; this screenshot should remain in the final notes.
- `lecture_04_figure_03.png`: Shows the same inverse-metric relation in a cleaner and more finished boxed form, with less occlusion by the lecturer; this screenshot should remain in the final notes.
- `lecture_04_figure_04.png`: Shows the metric tensor explicitly identified with a matrix on the upper board and the contraction `g^{mr}g_{rn}=\delta^m_n` on the lower board; this screenshot should remain in the final notes.
- `lecture_04_figure_05.png`: Shows the lowering-of-an-index step leading to the line element, with the key subexpression circled and `ds^2` at the right; this screenshot should remain in the final notes.
- `lecture_04_figure_06.png`: Shows a flat-space line element on the left and a skew-grid coordinate sketch on the right, making it the main visual evidence for the flat-metric discussion; this screenshot should remain in the final notes.

## Equation Extraction
- `lecture_04_figure_02.png`: \(g^{-1} g = I\) [visible]
- `lecture_04_figure_02.png`: \(g^{mr} g_{rn} = \delta^m_{\ n}\) [visible]
- `lecture_04_figure_03.png`: \(g^{-1} g = I\) [visible]
- `lecture_04_figure_03.png`: \(g^{mr} g_{rn} = \delta^m_{\ n}\) [visible]
- `lecture_04_figure_04.png`: \(g_{mn} \leftrightarrow \begin{pmatrix} g_{11} & g_{12} & g_{13} \\ g_{21} & g_{22} & g_{23} \\ g_{31} & \cdots \end{pmatrix}\) [partially visible]
- `lecture_04_figure_04.png`: \(g^{mr} g_{rn} = \delta^m_{\ n}\) [visible]
- `lecture_04_figure_05.png`: \(dx^m dx_m\) [visible]
- `lecture_04_figure_05.png`: \(dx^n g_{mn}\) [visible]
- `lecture_04_figure_05.png`: \(dx^m\,dx_n = dx^m dx_m\) is suggested by the chalk but should not be treated as a trustworthy literal equality [partially visible]
- `lecture_04_figure_05.png`: \(dx^m (dx^n g_{mn}) = ds^2\) [partially visible]
- `lecture_04_figure_05.png`: \(dx_m = g_{mn}dx^n\) [standard completion]
- `lecture_04_figure_05.png`: \(dx^m dx_m = g_{mn}\,dx^m dx^n = ds^2\) [standard completion]
- `lecture_04_figure_06.png`: \(ds^2 = d{x'}^{\,2} + d{x''}^{\,2}\) or an equivalent primed-coordinate version is what the chalk appears to say [partially visible]
- `lecture_04_figure_06.png`: \(ds^2 = (dx^1)^2 + (dx^2)^2\) [standard completion]
- `lecture_04_figure_06.png`: \(ds^2 = \delta_{mn}\,dx^m dx^n\) [standard completion]

## Diagram Extraction
- `lecture_04_figure_02.png`: This is not a geometric diagram but a pedagogical board layout, with a matrix statement on one line and a boxed indexed statement below; it should be preserved as a screenshot rather than redrawn.
- `lecture_04_figure_03.png`: The boxed inverse-metric relation is the main value here, so it should be preserved as a screenshot and paired with clean typeset equations rather than replaced by a redraw.
- `lecture_04_figure_04.png`: The upper-board matrix layout and lower-board contraction identity form a two-tier argument that is best preserved by keeping the screenshot visible.
- `lecture_04_figure_05.png`: The circled factor on the right is visually important because it marks the lowering step; this should remain as a screenshot, with clean note-quality equations placed nearby.
- `lecture_04_figure_06.png`: The right-hand skew-grid figure should be shown both ways, as the original screenshot and as a schematic TikZ redraw, because the screenshot carries the lecture’s board layout while the redraw can make the coordinate geometry legible.

## Reconstruction Guidance
- Use the frames to justify the specific indexed inverse-metric identity \(g^{mr}g_{rn}=\delta^m_{\ n}\), but typeset it cleanly in normalized notation beside `lecture_04_figure_02.png` and `lecture_04_figure_03.png` rather than reproducing the chalk spacing literally.
- Treat `g^{-1}g=I` as matrix shorthand that should appear in prose or display near the screenshots, with an explicit sentence that the upper-index components \(g^{mn}\) are the components of the inverse matrix.
- From `lecture_04_figure_04.png`, reconstruct the metric-as-matrix idea in a normalized matrix display rather than trying to preserve every partially visible entry exactly; the point of the frame is the matrix viewpoint, not the full finite array.
- From `lecture_04_figure_05.png`, reconstruct the lowering relation as \(dx_m=g_{mn}dx^n\) and then the scalar contraction \(dx^m dx_m = g_{mn}dx^m dx^n = ds^2\), while keeping the screenshot nearby because the circled chalk term is part of the lecture’s logic.
- Do not convert the first chalk line in `lecture_04_figure_05.png` into a literal equation without comment, because the transcript later states that Susskind did not intend that line as an equality but as a contraction step.
- From `lecture_04_figure_06.png`, reconstruct the flat-space interval in clean notation as \(ds^2=(dx^1)^2+(dx^2)^2=\delta_{mn}dx^m dx^n\), and redraw the skew-grid figure schematically in TikZ while keeping the screenshot beside it as evidence of board structure.
- In all five cases, prefer clean mathematical normalization in the notes and let the screenshots serve as documentary support for what was actually written on the board.

## Uncertainties
- In `lecture_04_figure_02.png`, the left factor inside the box is cramped, but the intended reading \(g^{mr}\) is strongly supported by both the visible contraction pattern and the surrounding transcript.
- In `lecture_04_figure_03.png`, the upper identity \(g^{-1}g=I\) is readable, but the cropping means the full upper-board context is incomplete.
- In `lecture_04_figure_04.png`, the matrix of \(g_{mn}\) is only partially visible, so it should be understood as evidence for the matrix viewpoint rather than as a complete literal transcription of the full board.
- In `lecture_04_figure_05.png`, the exact first-line notation is unreliable as written on the board, and the transcript explicitly corrects the impression that Susskind meant a literal equality there.
- In `lecture_04_figure_05.png`, the small \(1/r^2\) at the lower right is almost certainly leftover material from the earlier polar-coordinate inverse example and should not be imported into the lowering-index derivation.
- In `lecture_04_figure_06.png`, the exact prime marks or coordinate labels in the left equation are not fully legible, so the safe reconstruction is the standard flat two-dimensional Cartesian line element rather than a commitment to the exact chalk primes.
- In `lecture_04_figure_06.png`, the right-hand skew-grid sketch has no reliably legible axis labels, so any TikZ redraw should remain schematic unless the chapter text supplies coordinate names from the transcript rather than from the image alone.