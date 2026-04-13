# Figure Notes
## Image Inventory
- `lecture_05_figure_03.png`: A whiteboard shot centered on the matrix form of a spatial rotation. On the left is a column-vector relation with primed coordinates \((x',y',z')\) related to unprimed coordinates \((x,y,z)\), with Susskind pointing at an indexed version below. On the right is a large explicit \(3\times 3\) matrix labeled \(M\), with trigonometric entries and a third row that leaves the last coordinate unchanged.
- `lecture_05_figure_04.png`: A split board view combining geometry and notation. At the left is a large smooth curved line, visually serving as a trajectory or worldline sketch. At the right are stacked equations defining the relativistic velocity as a derivative with respect to proper time, together with a chain-rule relation for one component.
- `lecture_05_figure_05.png`: A tighter crop of the curved-trajectory sketch alone. The main visible content is a long upward-curving line with a small mark near its upper end that suggests a tangent or directional indicator. No readable equations remain in this crop.

## Blackboard Equations
- `lecture_05_figure_03.png`: \(\begin{pmatrix}x'\\ y'\\ z'\end{pmatrix} = M \begin{pmatrix}x\\ y\\ z\end{pmatrix}\) [visible]
- `lecture_05_figure_03.png`: \(M = \begin{pmatrix}\cos\theta & \sin\theta & 0 \\ -\sin\theta & \cos\theta & 0 \\ 0 & 0 & 1\end{pmatrix}\) [visible]
- `lecture_05_figure_03.png`: \(x'^i = M^i{}_{j} x^j\) [partially visible]
- `lecture_05_figure_04.png`: \(\dfrac{dX^\mu}{d\tau} = u^\mu\) [visible]
- `lecture_05_figure_04.png`: \(\dfrac{dx}{d\tau} = \dfrac{dx}{dt}\dfrac{dt}{d\tau}\) [visible]
- `lecture_05_figure_04.png`: an additional line involving \(\dfrac{dt}{d\tau}\) appears below, but the full right-hand side is unclear [partially visible]
- `lecture_05_figure_05.png`: no legible equation content [visible]

## Diagram And Layout Reading
- `lecture_05_figure_03.png` has a clear left-right pedagogical structure: abstract vector notation and indexed notation on the left, explicit matrix realization on the right. This is useful because it shows the lecture moving between geometric linear-algebra language and concrete component formulas.
- In `lecture_05_figure_03.png`, the matrix is visually large and self-contained, while the indexed expression below the left column vectors is partly occluded by Susskind’s arm and hand. The image therefore supports both a clean displayed matrix equation and a more cautious transcript-guided reconstruction of the index notation.
- `lecture_05_figure_04.png` visually links a curved path on the left to derivative notation on the right. That board layout matters: Susskind is not only defining \(u^\mu\) algebraically, but placing it next to a curve whose tangent the quantity is meant to represent.
- The curve in `lecture_05_figure_04.png` has no visible axes or labels. Its importance is qualitative rather than coordinate-specific: it is a trajectory sketch used to motivate the tangent-vector interpretation.
- `lecture_05_figure_05.png` isolates that curved-line sketch more cleanly than `lecture_05_figure_04.png` does. The upper-end mark is the main extra visual clue in this crop, but it is not fully legible as a formal arrow or label.
- Taken together, `lecture_05_figure_04.png` and `lecture_05_figure_05.png` show that the lecture is using the same board drawing both as a curve in ordinary geometry and as an analogy for the relativistic worldline/tangent-vector discussion.

## TeX Reconstruction Plan
- `lecture_05_figure_03.png` should remain visible in the notes. It should be paired with a clean displayed equation for the column-vector transformation and a separately typeset indexed form nearby. The screenshot is the evidence for the board layout and for the explicit matrix entries; the LaTeX should standardize the notation cleanly.
- For `lecture_05_figure_03.png`, no TikZ redraw is necessary unless the chapter wants a fully polished rotation diagram elsewhere. The main value here is equation evidence, not a geometric sketch.
- `lecture_05_figure_04.png` should remain visible and should be paired with both displayed equations and a small TikZ redraw. The equations to reconstruct nearby are the defining relation \(u^\mu = dX^\mu/d\tau\) and the clear chain-rule component formula. The TikZ redraw should show a smooth curve with a tangent vector, since the screenshot itself supports that conceptual pairing.
- `lecture_05_figure_05.png` should remain visible only as secondary diagram evidence for the later proper-acceleration discussion. It should sit near a clean TikZ redraw of a curved trajectory, but the mathematical formulas themselves should come from the transcript and from `lecture_05_figure_04.png`, not from this screenshot.
- For `lecture_05_figure_05.png`, the redraw should stay qualitative: a smooth curve with a tangent indication is enough. One should not infer additional labels, axes, or force arrows from the crop alone.
- If space is tight, `lecture_05_figure_04.png` is the primary image for the tangent-vector discussion, while `lecture_05_figure_05.png` functions as supporting evidence for the curve’s shape rather than as a standalone mathematical figure.

## Caption Drafts
- `lecture_05_figure_03.png`: Rotation matrix acting on spatial coordinates
- `lecture_05_figure_04.png`: Four-velocity and the tangent-vector construction
- `lecture_05_figure_05.png`: Curved trajectory for the proper-acceleration discussion

## Uncertainties
- In `lecture_05_figure_03.png`, the lower indexed formula is partly blocked by Susskind’s arm and hand. The intended structure is clear, but the exact placement of primes and indices on \(M\) and \(x\) should be normalized from the transcript rather than copied verbatim from the frame.
- In `lecture_05_figure_03.png`, the trigonometric entries are legible, but the chalk is soft enough that one should still standardize the matrix carefully in LaTeX.
- In `lecture_05_figure_04.png`, the symbol on the right-hand side of \(\dfrac{dX^\mu}{d\tau}=\cdots\) looks like \(u^\mu\), but the case of the letter is not completely secure from the image alone.
- In `lecture_05_figure_04.png`, the lowest displayed line involving \(\dfrac{dt}{d\tau}\) is too soft and cropped to transcribe safely in full.
- In `lecture_05_figure_04.png` and `lecture_05_figure_05.png`, the curve has no explicit axes or labels. Its meaning as a trajectory/worldline comes from the nearby lecture context, not from self-contained board annotation.
- In `lecture_05_figure_05.png`, the small mark near the top of the curve may be a tangent indicator, an arrow-like direction mark, or just a local chalk emphasis. Any TikZ completion should keep that feature modest and noncommittal.