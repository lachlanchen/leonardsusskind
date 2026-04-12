# Figure Notes
## Image Inventory
- `lecture_06_figure_03.png`: Leonard Susskind is drawing on the right half of the board. Two tall nearly vertical lines are visible, with a single wavy line connecting them across the middle. Above them sits an older irregular closed outline with a small detached loop near its upper right; this appears to be leftover board content from the earlier string-splitting discussion rather than part of the new exchange diagram.
- `lecture_06_figure_04.png`: Susskind stands to the left of a simple schematic on the right side of the board. A circular region with cross-hatched interior is drawn on the far right. A long horizontal line with arrowheads is drawn toward that circular region. On the far left, older wavy tangle-like strokes remain faintly visible as board residue.
- `lecture_06_figure_05.png`: The board shows a compact block of equations comparing black-hole entropy and string entropy. The top line begins with \(S_{BH}\), the second with \(S_{ST}\), and a lower line begins with \(R_s=\) as Susskind writes. On the far left a boxed or bracketed earlier relation involving \(\ell_p^2\) is only partially in frame.

## Blackboard Equations
- `lecture_06_figure_03.png`
  - No explicit equation labels are legible on the main exchange sketch. [visible]
  - A photon propagator is strongly implied by the wavy connector between the two vertical lines. [standard reconstruction]
  - \(\gamma\) as a label for the exchanged wavy line is standard but not written on the board in this frame. [standard reconstruction]

- `lecture_06_figure_04.png`
  - No legible equation text is visible. [visible]
  - A black-hole or horizon region is represented schematically by the hatched circle. [standard reconstruction]

- `lecture_06_figure_05.png`
  - \(S_{BH}=\dfrac{A}{\ell_p^2}=M^2G\) [visible]
  - \(S_{ST}=\dfrac{L}{\ell_s}=M\ell_s\) [visible]
  - \(R_s=\) [visible]
  - \(\ell_p^2=\cdots\) at the far left margin, from an earlier boxed relation, is only partly in frame. [partially visible]
  - \(R_s\approx \ell_s\) as the transition condition is not yet fully written in this frame but is the intended relation in the surrounding lecture moment. [standard reconstruction]

## Diagram And Layout Reading
- `lecture_06_figure_03.png` is a board sketch of a Feynman-style exchange diagram. The two nearly vertical strokes act as the external worldlines or source lines, and the wavy transverse connector is the exchanged photon. The older blob-and-loop above should not be over-read into the same diagram; visually it belongs to the previous string-coupling explanation.
- `lecture_06_figure_04.png` is a qualitative near-horizon board schematic rather than a coordinate diagram. The right-hand circle reads naturally as the black hole, while the long horizontal arrowed line is used to point toward or indicate the location “on the horizon, or near the horizon.” The left-side wavy tangle is not the main content of this frame and should be treated as residual board context.
- `lecture_06_figure_05.png` is an equation board, organized as a comparison table. The top line gives black-hole entropy in area and mass form; the next line gives string entropy in length and mass form; the lower line starts a new relation for the Schwarzschild radius. The layout itself is useful because it shows Susskind juxtaposing the two entropy formulas before moving to the transition condition.

## TeX Reconstruction Plan
- `lecture_06_figure_03.png` should remain visible in the notes. Nearby, add a clean TikZ redraw of the exchange diagram: two external lines with one wavy photon propagator between them. Keep the redraw minimal and avoid adding labels not needed by the surrounding prose. The screenshot serves as evidence for Susskind’s board sequencing and hand-drawn geometry.
- `lecture_06_figure_04.png` should remain visible in the notes. Pair it with a small TikZ schematic rather than a formal Penrose or spacetime diagram. The redraw should show a black-hole boundary on the right and a simple directional or proximity indicator from the exterior toward the horizon. Do not over-interpret the arrow as a precise coordinate axis unless a later frame supports that.
- `lecture_06_figure_05.png` should remain visible in the notes. Pair it with cleaned displayed equations, not TikZ as the primary reconstruction. The cleaned LaTeX nearby should present the entropy comparison and then, in the prose or in a short displayed equation, the transition condition \(R_s\sim \ell_s\). This screenshot is strongest as documentary evidence for the equation block and for the lecture’s comparison-driven board layout.

## Caption Drafts
- `lecture_06_figure_03.png`: Photon-exchange Feynman sketch on the board
- `lecture_06_figure_04.png`: Near-horizon schematic for stringy degrees of freedom
- `lecture_06_figure_05.png`: Blackboard comparison of black-hole and string entropy formulas

## Uncertainties
- In `lecture_06_figure_03.png`, the irregular closed shape and small detached loop above the exchange diagram are visible but not clearly tied to the exchange sketch itself. They should be treated as leftover context unless another nearby frame proves otherwise.
- In `lecture_06_figure_03.png`, no coupling labels such as electric charge or \(g\) are legible in the frame, even though the transcript discusses them.
- In `lecture_06_figure_04.png`, the exact meaning of the horizontal arrow is not explicitly labeled. The notes should reconstruct it only as a qualitative indicator of location relative to the black-hole boundary.
- In `lecture_06_figure_04.png`, the hatched circle is clear, but whether the hatching is meant to represent the whole black hole, its interior, or a fuzzy horizon atmosphere is not explicit from the frame alone.
- In `lecture_06_figure_05.png`, the far-left boxed relation is cropped; only part of the \(\ell_p^2\) expression is visible.
- In `lecture_06_figure_05.png`, the lower \(R_s=\) line is only beginning to be written at this instant, so the transition equation should be completed cautiously from the surrounding lecture rather than claimed as fully visible here.