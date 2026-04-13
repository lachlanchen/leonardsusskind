# Figure Notes
## Image Inventory
- `lecture_08_figure_01.png`: Opening Stanford title card over a campus walkway and buildings. No lecture-room board, equations, or diagram content is present.
- `lecture_08_figure_02.png`: Close board crop showing the complex-field plane with horizontal and vertical axes, a first-quadrant radial vector, and the angle label. Cropped equations at left show part of the conjugate/polar decomposition, while a lower-left fragment hints at the angular kinetic term. Susskind stands at the right edge without blocking the diagram.
- `lecture_08_figure_03.png`: Wider classroom board view with a large partial sombrero-like sketch at far left, a second smaller bowl-like sketch near the top center, and the green label \(V(\phi)\). There are also faint lower-left axis marks and some unrelated-looking numerical complex-number examples on the right. The lecturer is centered in front of the board.
- `lecture_08_figure_04.png`: Board showing a local phase transformation for \(\phi(x)\), a second line comparing derivative terms before and after priming, and the handwritten verdict “not sym” at right. The lecturer is at the left margin, leaving the algebra mostly unobstructed.
- `lecture_08_figure_05.png`: Lower board with a cleaned gauge-theory Lagrangian line containing a covariant scalar term, a potential term, and a final \(+F^2\) contribution. Above it, on the upper board, \(\rho=f+H\) remains visible. Below the equation is a small symmetry-breaking potential sketch; on the right is faint field-strength transformation work.
- `lecture_08_figure_06.png`: Tight crop of an in-progress substitution line beginning with \(D\phi\), followed by an arrow and a partially written right-hand side of the form \(f\,\partial\alpha+\cdots\). The equation is cut off at the right edge, and the lecturer’s hand/marker enters from the side.

## Blackboard Equations
- `lecture_08_figure_02.png`: \(\phi_I\) [visible]
- `lecture_08_figure_02.png`: \(\phi_R\) [visible]
- `lecture_08_figure_02.png`: \(\rho\) [visible]
- `lecture_08_figure_02.png`: \(\alpha\) [visible]
- `lecture_08_figure_02.png`: \(\phi^*=\phi_R-i\phi_I\) [partially visible]
- `lecture_08_figure_02.png`: \(\phi^*=\rho e^{-i\alpha}\) [partially visible]
- `lecture_08_figure_02.png`: \((\partial\alpha)^2\) [partially visible]

- `lecture_08_figure_03.png`: \(V(\phi)\) [visible]
- `lecture_08_figure_03.png`: \(\phi_R\) [partially visible]

- `lecture_08_figure_04.png`: \(\phi'(x)=e^{i\theta(x)}\phi(x)\) [visible]
- `lecture_08_figure_04.png`: \(\partial\phi^*\,\partial\phi \neq \partial\phi^{*\prime}\,\partial\phi'\) [standard reconstruction]
- `lecture_08_figure_04.png`: \(\text{not sym}\) [visible]

- `lecture_08_figure_05.png`: \(\rho=f+H\) [visible]
- `lecture_08_figure_05.png`: \(D\phi^*\,D\phi - V(\phi^*\phi) + F^2\) [visible]
- `lecture_08_figure_05.png`: \(F'=F\) [partially visible]
- `lecture_08_figure_05.png`: \(-\partial_\nu\partial_\mu\theta\) [partially visible]

- `lecture_08_figure_06.png`: \(D\phi \to f\,\partial\alpha + \cdots\) [partially visible]
- `lecture_08_figure_06.png`: \(D\phi \to f\,\partial\alpha + A\) [standard reconstruction]

## Diagram And Layout Reading
- `lecture_08_figure_01.png` is not a lecture-board image. It is purely an opening title/exterior shot and contributes nothing to mathematical reconstruction.

- `lecture_08_figure_02.png` is organized around the internal complex-field plane. The horizontal axis is labeled by the real component and the vertical axis by the imaginary component. A radial segment runs into the first quadrant, with \(\rho\) written along the segment and \(\alpha\) written along the wedge from the real axis. The left edge preserves enough of the equations to show that the board is moving between Cartesian and polar forms of the same complex field.

- `lecture_08_figure_03.png` is a layout figure more than a transcription figure. At far left is a larger partially cropped potential sketch, and near the top center is a second, smaller bowl-like sketch. The green \(V(\phi)\) label establishes that these drawings are potential-energy sketches, not field-space points. The lower-left board also contains a separate axis-and-line sketch, while the far-right writing appears to be ad hoc numerical examples rather than the main mathematical spine.

- `lecture_08_figure_04.png` has a clear two-line derivational layout. The top line writes the local phase transformation \(\phi'(x)=e^{i\theta(x)}\phi(x)\). The second line states that the derivative structure is not preserved under priming, and the handwritten note “not sym” gives the pedagogical conclusion. This is exactly the board rhythm of “try the local symmetry, see why it fails.”

- `lecture_08_figure_05.png` uses the board as a summary surface. The left-center equation is the assembled gauge-invariant scalar-plus-gauge Lagrangian in schematic form. Beneath it sits a small symmetry-breaking potential sketch, while the upper board still remembers the Higgs-field expansion \(\rho=f+H\). On the right, faint scratch work appears to concern the invariance of \(F\) under gauge transformation. The visual point is that several threads are present at once: Higgs expansion, final Lagrangian, and field-strength invariance.

- `lecture_08_figure_06.png` is a very tight, in-progress algebra frame. The board shows a substitution of the covariant derivative into a low-energy/frozen-\(\rho\) form, but the right-hand side is cut off before the expression is finished. The left-to-right arrow notation matters, but the frame is incomplete enough that it reads mainly as evidence of board motion rather than as a stand-alone equation figure.

## TeX Reconstruction Plan
- `lecture_08_figure_01.png` should not remain visible in the chapter. It is an opening title card and has no note-writing value.

- `lecture_08_figure_02.png` should remain visible near the passage that reintroduces the complex scalar field and rewrites it in polar coordinates. It should be paired with clean displayed equations for
  \[
  \phi=\phi_R+i\phi_I,\qquad
  \phi^*=\phi_R-i\phi_I,\qquad
  \phi=\rho e^{i\alpha},\qquad
  \phi^*=\rho e^{-i\alpha},
  \]
  and with a TikZ redraw of the \((\phi_R,\phi_I)\)-plane showing the radial vector and the angle \(\alpha\).

- `lecture_08_figure_03.png` should remain visible if the notes keep a visual of the radially symmetric potential discussion. It should be accompanied by a clean TikZ redraw of the potential geometry, ideally a Mexican-hat/surface-of-revolution sketch plus a radial slice. The screenshot should serve as evidence of the board layout and the lecturer’s labeling, while the reconstructed diagram should carry the mathematical burden.

- `lecture_08_figure_04.png` should remain visible in the gauge-invariance review section. It should be paired with a clean displayed equation block for the local phase transformation and the failure of ordinary derivatives, for example the transformed kinetic term or the schematic inequality between primed and unprimed derivative products.

- `lecture_08_figure_05.png` should not be the primary figure for the specific “\(A^2\) mass term” moment, because the screenshot does not actually show the forbidden \(A_\mu A^\mu\) term. If kept at all, it should be kept only as secondary evidence for the cleaned gauge-invariant Lagrangian
  \[
  D\phi^*\,D\phi - V(\phi^*\phi) + F^2,
  \]
  together with the nearby Higgs-expansion note \(\rho=f+H\). A stronger frame should be preferred for the mass-term discussion.

- `lecture_08_figure_06.png` should ideally be replaced by a fuller neighboring frame before final note writing. If no better frame exists, it may remain only as supporting evidence that Susskind is collapsing the covariant derivative into the angular derivative plus the gauge field in the frozen-\(\rho\) approximation. The actual equation should be typeset cleanly nearby rather than read literally from the screenshot.

## Caption Drafts
- `lecture_08_figure_01.png`: Opening Stanford title card.
- `lecture_08_figure_02.png`: Complex field in polar coordinates.
- `lecture_08_figure_03.png`: Radially symmetric potential sketches.
- `lecture_08_figure_04.png`: Local phase transformation is not a symmetry.
- `lecture_08_figure_05.png`: Gauge-invariant Lagrangian and field-strength term.
- `lecture_08_figure_06.png`: In-progress \(D\phi\) substitution in the frozen-\(\rho\) limit.

## Uncertainties
- In `lecture_08_figure_02.png`, the left-edge equations are cropped; the conjugate and polar forms are readable in intent but not in fully intact left-hand notation. The lower-left \((\partial\alpha)^2\) fragment is only partial.

- In `lecture_08_figure_03.png`, the large left-hand potential sketch is cropped, and the lower-left axis sketch is too faint to quote confidently. The numerical examples at right are visible but appear tangential to the main potential-energy discussion.

- In `lecture_08_figure_04.png`, the derivative notation is schematic and omits explicit Lorentz indices. The placement of the prime and star on the right-hand term is hand-drawn loosely, so the notes should standardize this to a consistent relativistic notation.

- In `lecture_08_figure_05.png`, the faint right-hand scratch work beyond \(F'=F\) is hard to read with confidence. The frame does not visibly show the forbidden \(A_\mu A^\mu\) mass term even though the subtitle timestamp is in that part of the lecture.

- In `lecture_08_figure_06.png`, the crucial rightmost term is cut off. The transcript strongly suggests that the intended completion is the vector-potential term \(+A\) or \(+A_\mu\), but the screenshot itself only preserves the plus sign and the start of the next symbol.

- More generally, `lecture_08_figure_05.png` and `lecture_08_figure_06.png` are weaker than `lecture_08_figure_02.png` through `lecture_08_figure_04.png` as final note figures. The first is thematically adjacent but not tightly aligned to its subtitle line, and the second is simply incomplete.