# Figure Notes
## Image Inventory
- `lecture_07_figure_02.png`: Two-board classroom frame with Leonard Susskind standing between the boards. On the right board the notation `H.D =` appears above the clearly written relation `D = c/H`. On the left board there is a cropped remnant of an earlier formula involving a fraction, a visible `\rho_0`, and an equality ending in `H`, but most of that expression is off-frame or obscured.
- `lecture_07_figure_03.png`: Blackboard frame during the scalar-field discussion. On the left side of the board one sees `\phi` and the label `V(\phi)`. To the right is a hand-drawn graph with axes and a qualitatively varying potential curve: a dip, then a rise to a hump, and then a descent. The lecturer’s hand points at the descending right-hand side of the curve.
- `lecture_07_figure_04.png`: Blackboard frame showing a more developed inflationary potential sketch. The graph has a high left plateau with a slight slope, a sharp drop or “cliff,” and then a minimum with a rising branch to the right. A horizontal-axis label `\phi` is visible near the right-hand side. The lecturer has stepped away enough that the overall shape is readable.

## Blackboard Equations
- `D = \dfrac{c}{H}` [visible] in `lecture_07_figure_02.png`
- `H D =` [visible] in `lecture_07_figure_02.png`
- `H D = c` [standard reconstruction] for the partially written top line in `lecture_07_figure_02.png`
- `\rho_0` [partially visible] in `lecture_07_figure_02.png`
- `\sqrt{\dfrac{8\pi G}{3}\rho_0}=H` [standard reconstruction] as the likely left-board relation only partially preserved in `lecture_07_figure_02.png`
- `\phi` [visible] in `lecture_07_figure_03.png`
- `V(\phi)` [visible] in `lecture_07_figure_03.png`
- `V` [partially visible] as the vertical-axis label in `lecture_07_figure_03.png`
- `\phi` [visible] as the horizontal-axis label in `lecture_07_figure_04.png`
- `V(\phi)` [standard reconstruction] for the potential being plotted in `lecture_07_figure_04.png`
- `V` [partially visible] as the vertical-axis label in `lecture_07_figure_04.png`

## Diagram And Layout Reading
- In `lecture_07_figure_02.png`, the main visual fact is board organization: the right board isolates the horizon-distance relation, while the left board preserves a cropped remnant of the vacuum-energy/Hubble-rate derivation. This is documentary evidence for how the lecture moves from the Friedmann-style relation to the horizon formula.
- `lecture_07_figure_03.png` shows a standard potential-versus-field sketch rather than an algebraic derivation. The horizontal axis is the field value `\phi`, and the vertical direction represents the potential `V`. The curve is not monotone: it dips, rises, and then falls again. This matters because the lecture is emphasizing that different values of the field correspond to different potential energies.
- `lecture_07_figure_04.png` is a clearer large-scale inflationary-potential sketch. The curve begins high on the left, stays almost flat for a long interval, then drops steeply near the right, reaches a minimum, and rises again. The plateau/cliff/minimum organization is the main thing to preserve; it visually supports the slow-roll-plus-drop narrative of the lecture.
- The line in `lecture_07_figure_04.png` is heavily overtraced on the plateau, so the exact local micro-shape is not authoritative. What is authoritative is the qualitative structure: broad flat region, sharp descent, nonzero minimum, then rising branch.

## TeX Reconstruction Plan
- `lecture_07_figure_02.png` should remain visible in the notes as documentary board evidence for the horizon-distance relation. Nearby, the notes should typeset the clean equation
  \[
  D=\frac{c}{H},
  \]
  and, if useful for exposition, also the equivalent form \(H D=c\). The left-board material should not be transcribed as a firm equation unless the transcript requires it; at most it should be treated as contextual residue from the preceding derivation.
- `lecture_07_figure_03.png` must remain visible, because it preserves both the notation `V(\phi)` and the qualitative potential curve. Next to it, the notes should include a clean TikZ redraw of a generic potential \(V(\phi)\) with the same qualitative shape and a short display or inline reminder that different values of \(\phi\) correspond to different potential energies.
- `lecture_07_figure_04.png` must also remain visible. It is the clearest documentary image for the “high plateau / cliff / minimum” potential used in the inflation discussion. A clean TikZ redraw should sit nearby, emphasizing the long shallow plateau, the steep drop, and the right-hand minimum. The redraw should be qualitative only; do not overfit the exact hand-drawn line.
- For `lecture_07_figure_03.png` and `lecture_07_figure_04.png`, it is better to keep the screenshots and redraw the curves cleanly than to rely on the screenshots alone. The screenshots carry the lecture’s board texture; the TikZ versions should carry the mathematical readability.
- The notes should not replace these screenshots entirely with interpreted graphics. Each selected screenshot is useful evidence for board layout or the intended potential shape and should remain visible in the final chapter.

## Caption Drafts
- `lecture_07_figure_02.png`: Hubble distance relation on the board
- `lecture_07_figure_03.png`: Scalar potential \(V(\phi)\) sketch
- `lecture_07_figure_04.png`: Plateau and cliff in the inflationary potential

## Uncertainties
- In `lecture_07_figure_02.png`, the upper line `H.D =` is incomplete in the frame; `H D = c` is the natural completion, but the `c` is not cleanly visible.
- In `lecture_07_figure_02.png`, the left-board formula is too cropped and occluded to trust as a direct transcription. The visible `\rho_0` and trailing `= H` strongly suggest the square-root Friedmann/vacuum-energy relation, but that should be treated as a cautious reconstruction rather than a direct reading of the pixels.
- In `lecture_07_figure_03.png`, the axis labels are not equally sharp. `V(\phi)` and `\phi` on the left are clear, but the graph’s own axis labels are less secure.
- In `lecture_07_figure_03.png`, the lecturer’s hand partially covers the descending part of the curve, so the exact right-hand shape should not be reconstructed too literally.
- In `lecture_07_figure_04.png`, the vertical-axis label is not fully legible, though the graph is clearly a potential plotted against `\phi`.
- In `lecture_07_figure_04.png`, the right-hand branch after the minimum is partly cropped by the frame edge, so only its upward trend should be retained in redraws, not an exact endpoint or exact slope.