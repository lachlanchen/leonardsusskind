# Figure Notes
## Image Inventory
- `lecture_02_figure_02.png` shows Leonard Susskind standing at the left side of the board beside a linear-combination expression. To the right, two arrows emerge from a common origin: one points upward-right and is labeled near its tip, and one points roughly horizontally to the right and is also labeled. The figure is a clean board state for the discussion of spanning a two-dimensional plane with two vectors.
- `lecture_02_figure_03.png` shows a completed top-line mapping from function notation to Dirac ket notation. At upper left is `\psi(x)`, followed by a long rightward implication arrow, and at upper right a ket labeled with `\psi`. Below it, Susskind is beginning a second analogous line starting with another function, apparently `\phi(x)`, followed by a partially drawn rightward arrow.
- `lecture_02_figure_06.png` shows Susskind gesturing beside a simple geometric sketch of ordinary blackboard vectors. A vertical reference line is drawn, and from a common point on that line two rightward rays extend, one steeper and one flatter. There are no visible labels; the value of the image is diagrammatic and spatial rather than symbolic.

## Blackboard Equations
- `lecture_02_figure_02.png`: `r_1 V_1 + r_2 V_2` `[partially visible]`
- `lecture_02_figure_02.png`: `V_1` `[visible]`
- `lecture_02_figure_02.png`: `V_2` `[visible]`
- `lecture_02_figure_03.png`: `\psi(x) \Rightarrow |\psi\rangle` `[visible]`
- `lecture_02_figure_03.png`: `\phi(x)` `[visible]`
- `lecture_02_figure_03.png`: `\phi(x) \Rightarrow` `[partially visible]`
- `lecture_02_figure_03.png`: `\phi(x) \Rightarrow |\phi\rangle` `[standard reconstruction]`
- `lecture_02_figure_06.png`: no stable symbolic notation is legible; the figure is diagrammatic rather than algebraic.

## Diagram And Layout Reading
- In `lecture_02_figure_02.png`, the board is split into two functional regions: algebra on the left and geometry on the right. The right-hand sketch consists of two non-collinear vectors from a common origin, forming an open wedge in which a third vector could be inserted. This spatial arrangement supports the spoken point that two non-collinear vectors span the plane and that an additional vector in between is redundant.
- In `lecture_02_figure_03.png`, the board is organized as a notation translation. The completed top line turns a complex function of a real variable into an abstract ket vector. The lower line is being built as a parallel example, so the board layout itself conveys that different functions correspond to different vectors in the same vector space.
- In `lecture_02_figure_06.png`, the sketch is intentionally elementary: it looks like the kind of ordinary geometric vector drawing one makes on a blackboard before talking about operations such as rotation or reflection. The vertical stroke functions as a reference axis or guide, and the two rightward rays illustrate ordinary spatial vectors rather than bras, kets, or component columns.

## TeX Reconstruction Plan
- `lecture_02_figure_02.png` must remain visible. Nearby, the notes should typeset the clean linear-combination expression and include a TikZ redraw of the two spanning vectors. If the prose follows the transcript closely, the redraw may also include a third vector inside the wedge as a transcript-guided construction, but that third vector should be clearly treated as a reconstruction rather than as something already visible in the screenshot.
- `lecture_02_figure_03.png` must remain visible. The top-line mapping should be re-expressed as a clean displayed equation in LaTeX, since it is fully legible and conceptually important. The lower line should be completed in the notes only with a brief acknowledgment that the screenshot shows an in-progress second example and that the full `\phi(x) \Rightarrow |\phi\rangle` line is a cautious transcript-guided completion.
- `lecture_02_figure_06.png` must remain visible. A clean TikZ redraw should sit nearby, because the screenshot preserves the lecture’s board layout and gestural context while the diagram itself is simple enough to redraw more legibly. The redraw should stay unlabeled unless nearby transcript material warrants labels.

## Caption Drafts
- `lecture_02_figure_02.png`: Linear combination from two spanning vectors
- `lecture_02_figure_03.png`: Mapping `\psi(x)` to ket notation
- `lecture_02_figure_06.png`: Ordinary vectors drawn on the blackboard

## Uncertainties
- In `lecture_02_figure_02.png`, the first coefficient in the linear-combination expression is slightly compromised by Susskind’s position. The board lettering looks like uppercase `V`, while the transcript speaks of `v_1`, `v_2`, and `v_3`; the notes should normalize this consistently but acknowledge that the chalk glyph is visually closer to `V`.
- In `lecture_02_figure_02.png`, no third vector is actually drawn inside the wedge in the selected frame. The subtitle line about drawing another vector refers to the spoken possibility, not to a completed visible chalk sketch.
- In `lecture_02_figure_03.png`, the exact arrow style is graphical rather than formally symbolic; it reads as an implication or identification arrow, not as a strict equality sign. The lower line is incomplete in the image, so any full ket on that second line requires cautious reconstruction.
- In `lecture_02_figure_06.png`, the diagram has no labels and no legible symbolic annotations. The vertical line may be an axis, a guide line, or simply part of a quick sketch for ordinary vectors; the notes should avoid overinterpreting it.
- In `lecture_02_figure_06.png`, the two rightward rays are clear enough as ordinary vectors, but the precise intended operation on them belongs to surrounding lecture context rather than to the image alone.