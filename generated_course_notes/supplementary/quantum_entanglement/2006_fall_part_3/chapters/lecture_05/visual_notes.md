# Visual Evidence
## Frame Inventory
- `lecture_05_figure_03.png`: Whiteboard frame showing a column-vector equation on the left and an explicit \(3\times 3\) rotation matrix \(M\) on the right; the screenshot should remain in the final notes as primary evidence for the matrix notation and board layout.
- `lecture_05_figure_04.png`: Split board frame with a large curved trajectory at left and four-velocity / chain-rule equations at right; the screenshot should remain in the final notes as the primary visual anchor for the tangent-vector interpretation.
- `lecture_05_figure_05.png`: Tight crop of the same curved trajectory, with the upper-end mark more visible but no readable equations; the screenshot should remain only as secondary visual evidence near the proper-acceleration discussion.

## Equation Extraction
- `lecture_05_figure_03.png`: \(\begin{pmatrix}x'\\ y'\\ z'\end{pmatrix} = M \begin{pmatrix}x\\ y\\ z\end{pmatrix}\) [visible]
- `lecture_05_figure_03.png`: \(M = \begin{pmatrix}\cos\theta & \sin\theta & 0 \\ -\sin\theta & \cos\theta & 0 \\ 0 & 0 & 1\end{pmatrix}\) [visible]
- `lecture_05_figure_03.png`: \(x'^i = M^i{}_j x^j\) [partially visible]
- `lecture_05_figure_04.png`: \(\dfrac{dX^\mu}{d\tau} = u^\mu\) [visible]
- `lecture_05_figure_04.png`: \(\dfrac{dx}{d\tau} = \dfrac{dx}{dt}\dfrac{dt}{d\tau}\) [visible]
- `lecture_05_figure_04.png`: a lower line involving \(\dfrac{dt}{d\tau}\) is present but not fully legible [partially visible]
- `lecture_05_figure_04.png`: \(u^0 = \dfrac{dt}{d\tau}\) [standard completion]
- `lecture_05_figure_05.png`: no legible equation content [visible]

## Diagram Extraction
- `lecture_05_figure_03.png` is not mainly a geometric sketch; its value is the left-right board structure that moves from vector notation to explicit matrix entries. It should be preserved as a screenshot, and any redraw should be optional rather than required.
- `lecture_05_figure_04.png` contains a qualitative curve with no axes, labels, or coordinates, paired with the defining equation for four-velocity. This should be shown both ways: keep the screenshot, and redraw a minimal TikZ curve with a tangent vector to clarify the geometric point.
- `lecture_05_figure_05.png` is a cleaner visual crop of the same curve and should support the same TikZ redraw if the notes want a second, cleaner geometric cue. It should not be treated as evidence for any force arrow, coordinate system, or explicit acceleration formula.
- Taken together, `lecture_05_figure_04.png` and `lecture_05_figure_05.png` support a curve-with-tangent diagram, not a fully specified spacetime plot. The redraw should therefore remain schematic.

## Reconstruction Guidance
- Turn `lecture_05_figure_03.png` into one clean displayed rotation equation and one clean displayed matrix, with the indexed form typeset separately as a cautious normalization of the partially blocked chalk line. Keep the screenshot beside these equations, because the image itself shows how Susskind organized the board.
- Use `lecture_05_figure_04.png` to anchor the statement that four-velocity is the tangent vector to the worldline. The clean note-quality equations should come from the visible top line and the visible chain-rule line, while the rest of the component formulas should be completed from the transcript rather than guessed from blurred chalk.
- Redraw the curve from `lecture_05_figure_04.png` and `lecture_05_figure_05.png` as a smooth unlabeled path with a tangent mark or tangent arrow. Keep the redraw simple, because the screenshot supports the idea of tangency but not a heavy set of labels.
- If the notes discuss proper acceleration immediately after the tangent-vector section, use `lecture_05_figure_05.png` only as supporting geometry and place the real mathematics in typeset equations reconstructed from the transcript. The frame alone does not justify a full dynamical diagram.
- When the chalk is visually incomplete, prefer standardizing notation rather than imitating board messiness. The goal is to preserve the lecture’s content and layout cues, not its accidental chalk ambiguities.

## Uncertainties
- In `lecture_05_figure_03.png`, the lower indexed formula is partly occluded by Susskind’s arm and hand, so the exact prime and index placement is not directly recoverable from the frame alone.
- In `lecture_05_figure_03.png`, the matrix entries are readable, but the chalk is soft enough that the final notes should typeset the trigonometric matrix cleanly rather than copying its handwritten spacing.
- In `lecture_05_figure_04.png`, the coordinate symbol looks like \(X^\mu\) rather than \(x^\mu\), but the case is not fully secure from the frame alone.
- In `lecture_05_figure_04.png`, the right-hand symbol looks like \(u^\mu\), but the exact shape is soft enough that the transcript should confirm the final notation.
- In `lecture_05_figure_04.png`, the lowest displayed line with \(\dfrac{dt}{d\tau}\) is too cropped and faint to transcribe reliably.
- In `lecture_05_figure_05.png`, the small mark near the upper end of the curve may be a tangent cue, an arrow-like mark, or just chalk emphasis; it should not be overinterpreted.
- `lecture_05_figure_05.png` does not visually support the subtitle’s nearby \(f=ma\) discussion by itself, so any acceleration formulas must come from transcript-backed reconstruction rather than from the frame.