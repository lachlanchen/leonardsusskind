# Figure Notes
## Image Inventory
- `lecture_03_figure_01.png`: Introductory Stanford title overlay on a campus/courtyard shot. No blackboard, lecturer boardwork, or mathematical content is visible.
- `lecture_03_figure_02.png`: Leonard Susskind stands at the board and begins writing a second line under a clearly legible top reference equation. The visible board content is sparse but mathematically relevant: a flat-space line element in the new \(ds^2\) sign convention and the start of a new metric line below it.
- `lecture_03_figure_03.png`: Side view of Susskind against an essentially blank board or wall segment. No useful equation block, diagram, or board layout is visible.
- `lecture_03_figure_04.png`: Susskind stands near a lower-board equation fragment. The most legible mathematical content is a fraction with numerator \(\rho^2\) and denominator involving \(16M^2G^2\). The frame is usable only as partial evidence for the near-horizon algebra.
- `lecture_03_figure_05.png`: Susskind writes on a board already containing a left-hand equation block and a central-right spacetime sketch. The diagram shows two crossing diagonal lines, a marked central point, a newly drawn right-hand curve or boundary, and hatched shading above/right. Partial algebra involving \(\omega\) and \(dt^2/(16M^2G^2)\) is visible on the left.

## Blackboard Equations
- `lecture_03_figure_02.png` [visible]:
  \[
  ds^2 = dt^2 - dx^2
  \]
- `lecture_03_figure_02.png` [partially visible]:
  \[
  ds^2 =
  \]
  The lower line has only just begun.
- `lecture_03_figure_02.png` [standard reconstruction]:
  \[
  ds^2 = -\left(1-\frac{2MG}{r}\right)dt^2 + \frac{dr^2}{1-\frac{2MG}{r}} + \cdots
  \]
  This matches the transcript’s sign-flipped Schwarzschild metric in the \(ds^2\) convention, with the angular term suppressed in the spoken discussion.
- `lecture_03_figure_03.png` [visible]: no usable blackboard equation is visible.
- `lecture_03_figure_04.png` [partially visible]:
  \[
  \frac{\rho^2}{16M^2G^2}
  \]
  The surrounding sign, adjacent \(dt^2\), and the rest of the line are not fully visible.
- `lecture_03_figure_04.png` [standard reconstruction]:
  \[
  ds^2 = -\frac{\rho^2\,dt^2}{16M^2G^2} + d\rho^2
  \]
  This is the near-horizon intermediate form described in the transcript immediately before the \(t \mapsto \omega\) rescaling.
- `lecture_03_figure_05.png` [partially visible]:
  \[
  \frac{t}{4MG} = \omega
  \]
- `lecture_03_figure_05.png` [partially visible]:
  \[
  \frac{dt^2}{16M^2G^2} = d\omega^2
  \]
- `lecture_03_figure_05.png` [partially visible]:
  \[
  r-2MG
  \]
  only as a cropped label fragment near the lower right.
- `lecture_03_figure_05.png` [standard reconstruction]:
  \[
  ds^2 = -\rho^2\,d\omega^2 + d\rho^2
  \]
  This is the clean flat-space hyperbolic-polar metric that the lecture uses to interpret the near-horizon region.

## Diagram And Layout Reading
- `lecture_03_figure_01.png` has no note-writing value beyond showing the Stanford intro card; it should not inform the mathematical chapter.
- `lecture_03_figure_02.png` shows a simple two-line board layout: a reference flat-space line element on top and a new line beginning below it. For note writing, the important point is the visual transition from the old convention to the rewritten Schwarzschild metric, not the incomplete lower line itself.
- `lecture_03_figure_03.png` does not preserve any meaningful board organization. It is essentially a talking-head frame.
- `lecture_03_figure_04.png` appears to capture a lower portion of the near-horizon derivation after the \(\rho\) substitution. The image does not preserve enough of the whole board to function as layout evidence, but it does show that the \(\rho^2/(16M^2G^2)\) factor was written explicitly on the board.
- `lecture_03_figure_05.png` is the strongest diagram frame. The board contains:
  - a left equation block with the \(t \to \omega\) rescaling;
  - a central X-shaped crossing of diagonal lines, visually reading like null lines or light-cone boundaries;
  - a marked point near the crossing;
  - a right-hand curve or nearly vertical line being added at the moment of capture;
  - hatched shading in the upper-right region;
  - a lower-right cropped radial label fragment.
  This is clearly not just an equation board; it is a board-layout-plus-diagram moment and should be treated that way in the notes.

## TeX Reconstruction Plan
- `lecture_03_figure_01.png` should not remain visible in the chapter. It is an intro/title visual with no mathematical or diagrammatic value.
- `lecture_03_figure_02.png` can remain visible as secondary screenshot evidence for the sign-convention switch and the start of the Schwarzschild rewrite. It should be paired with clean displayed equations nearby:
  \[
  ds^2 = dt^2 - dx^2
  \]
  as the flat reference line, followed by the transcript-backed Schwarzschild metric in the new \(ds^2\) convention.
- `lecture_03_figure_03.png` should not remain visible. It adds no useful equation content, diagram content, or board layout evidence.
- `lecture_03_figure_04.png` is weak as a full screenshot but still useful as equation evidence. If retained, it should appear only near the near-horizon algebra and be paired with a clean displayed reconstruction of
  \[
  ds^2 = -\frac{\rho^2\,dt^2}{16M^2G^2} + d\rho^2
  \]
  before the rescaling to \(\omega\). If the layout becomes crowded, the typeset equation should take priority over the screenshot.
- `lecture_03_figure_05.png` must remain visible. It is the strongest direct evidence for the spacetime sketch used later to discuss horizons, constant-\(r\) curves, and the outside/inside distinction.
- Near `lecture_03_figure_05.png`, the notes should reconstruct in TikZ:
  - the crossed null lines;
  - the marked central point corresponding to \(\rho=0\) and hence \(r=2MG\);
  - the added right-hand constant-\(r\) line or curve;
  - the hatched/shaded region only in a restrained schematic way.
- Near `lecture_03_figure_05.png`, the notes should also typeset the nearby coordinate equations:
  \[
  \omega = \frac{t}{4MG},
  \qquad
  d\omega^2 = \frac{dt^2}{16M^2G^2},
  \qquad
  ds^2 = -\rho^2\,d\omega^2 + d\rho^2.
  \]
- The near-horizon \(\rho\)-substitution itself should be typeset cleanly from the transcript rather than forced entirely out of the images:
  \[
  \rho = \sqrt{8MG}\,\sqrt{r-2MG},
  \qquad
  \rho^2 = 8MG(r-2MG).
  \]

## Caption Drafts
- `lecture_03_figure_01.png`: Stanford University title card.
- `lecture_03_figure_02.png`: Flat-space line element and start of Schwarzschild rewrite.
- `lecture_03_figure_03.png`: Lecturer beside blank board segment.
- `lecture_03_figure_04.png`: Near-horizon \(\rho^2/(16M^2G^2)\) term on the board.
- `lecture_03_figure_05.png`: Horizon sketch with \(\omega\) rescaling and constant-\(r\) construction.

## Uncertainties
- `lecture_03_figure_02.png`: the lower line is too incomplete to read directly as the Schwarzschild metric; the full expression must come from the transcript.
- `lecture_03_figure_04.png`: the denominator appears to be \(16M^2G^2\), but the full surrounding term is cropped; the sign and adjacent \(dt^2\) are not directly secure from the frame alone.
- `lecture_03_figure_05.png`: the left equation block is partly cropped, so the exact order of the equality in \(\omega = t/(4MG)\) versus \(t/(4MG)=\omega\) is visually unimportant but not perfectly fixed.
- `lecture_03_figure_05.png`: the newly drawn right-hand feature is clearly a significant curve or boundary in the spacetime sketch, but its exact label is not legible in the image alone.
- `lecture_03_figure_05.png`: the lower-right label fragment containing \(r-2MG\) is incomplete and should not be overinterpreted without the transcript.
- `lecture_03_figure_01.png` and `lecture_03_figure_03.png` are visually weak for note purposes and should not drive any reconstruction decisions.