# Visual Evidence
## Frame Inventory
- `lecture_03_figure_02.png`: Blackboard frame showing the entropy formula at upper left, a family of schematic probability curves at lower left, and the normalization plus average-energy constraints at upper right; this screenshot should remain in the final notes as documentary evidence.
- `lecture_03_figure_03.png`: Blackboard frame centered on `P(i)=n_i/N`, with a vertical energy-axis sketch and many short level or occupancy marks; this screenshot should remain in the final notes as documentary evidence.

## Equation Extraction
- `lecture_03_figure_02.png`: [visible] \(S=-\sum_i P(i)\log P(i)\)
- `lecture_03_figure_02.png`: [visible] \(\sum_i P(i)=1\)
- `lecture_03_figure_02.png`: [visible] \(\sum_i P(i)E(i)=\langle E\rangle\)
- `lecture_03_figure_02.png`: [partially visible] \(E\) as the horizontal-axis label of the distribution sketch
- `lecture_03_figure_02.png`: [standard completion] In cleaned notes, the visible board notation \(E(i)\) may be standardized to \(E_i\), but only as notation cleanup rather than literal transcription.
- `lecture_03_figure_03.png`: [visible] \(P(i)=\dfrac{n_i}{N}\)
- `lecture_03_figure_03.png`: [partially visible] \(E\) as the label on the vertical axis
- `lecture_03_figure_03.png`: [partially visible] low-lying state labels near the bottom of the axis, plausibly \(i=1\), \(i=2\), \(\dots\)
- `lecture_03_figure_03.png`: [standard completion] When the chapter rewrites the constraints in probability language, it is appropriate to connect this visible equation to \(n_i=NP_i\), \(\sum_i P_i=1\), and \(\sum_i P_iE_i=E\), but those are transcript-backed consequences rather than fully visible board content in this frame.

## Diagram Extraction
- `lecture_03_figure_02.png`: The main diagram is a shared-axis sketch of several distributions, beginning with a very narrow low-energy peak and then several broader, flatter curves extending farther to the right. This should be shown both ways: keep the screenshot and add a simple TikZ redraw.
- `lecture_03_figure_02.png`: The redraw should preserve the qualitative message only: larger average energy corresponds to a distribution that is broader and shifted toward larger \(E\). It should not invent a legible vertical-axis symbol that the frame itself does not show.
- `lecture_03_figure_03.png`: The visible sketch is a vertical energy axis with many short horizontal marks, suggesting discrete energy levels or states, together with nearby dots or strokes indicating occupancy. This can remain primarily as a screenshot; a redraw is optional and should be minimal if used at all.
- `lecture_03_figure_03.png`: If redrawn, the clean version should be a vertical energy-level diagram with a few marked occupied levels, placed near the equation \(P(i)=n_i/N\). It should not attempt to reconstruct the cropped left-hand replica sketch from this frame alone.

## Reconstruction Guidance
- Keep `lecture_03_figure_02.png` visible near the opening recap of entropy and constrained probability distributions. Pair it with clean displayed equations for \(S=-\sum_i P_i\log P_i\), \(\sum_i P_i=1\), and \(\sum_i P_iE_i=\langle E\rangle\).
- Redraw the family of curves from `lecture_03_figure_02.png` in TikZ as an interpretive schematic, not as a forensic copy. The key features to preserve are: one narrow low-energy distribution, several broader ones, a common energy axis, and the monotonic increase of average energy across the family.
- Keep `lecture_03_figure_03.png` visible where the lecture turns from replica counting to probability as fraction. The screenshot matters because it shows the board transition from a state-counting picture to the compact formula \(P(i)=n_i/N\).
- Use `lecture_03_figure_03.png` to motivate the clean note-level relation between occupation numbers and probabilities, then let the transcript carry the algebraic rewriting of the constraints. The frame itself supports the definition, not the full derivation.
- When converting visible board notation into note-quality mathematics, preserve literal transcription where the image is being quoted and use standard notation only in the cleaned derivation. In practice this means keeping \(E(i)\) when describing the board, but using \(E_i\) in the main exposition if the chapter is otherwise consistent.
- Avoid overbuilding the diagrams. The first frame justifies a clean schematic redraw; the second frame justifies a small supporting sketch at most.

## Uncertainties
- In `lecture_03_figure_02.png`, the entropy formula is legible overall, but the handwriting around \(\log P(i)\) is slightly messy.
- In `lecture_03_figure_02.png`, the vertical axis of the curve family is drawn but not clearly labeled.
- In `lecture_03_figure_02.png`, the curves clearly represent a family of probability distributions, but no fully reliable written label for that family is visible.
- In `lecture_03_figure_03.png`, the tiny labels near the bottom of the vertical axis are too blurred to transcribe confidently.
- In `lecture_03_figure_03.png`, the exact meaning of the dots or short marks next to the energy axis is strongly suggestive of occupied states or counted replicas, but the convention is not fully recoverable from this frame alone.
- In `lecture_03_figure_03.png`, the cropped left-hand sketch is incomplete and should not be reconstructed aggressively from image evidence alone.