# Figure Notes

## Image Inventory

- `lecture_09_figure_02.png`: Medium close-up of the whiteboard during the supersymmetry recap. The top line shows the shifted chiral coordinate, the middle line shows the chiral superfield expansion, and the lower line collects component terms, including the fermion kinetic term that the subtitle names.
- `lecture_09_figure_03.png`: Wider board shot from the discussion of \(\Phi^n\) in the chiral \(d^2\theta\) integral. On the left is the superspace expression, in the middle are repeated component factors built from \(\phi+\psi\theta+F\theta\theta\), and below is an implication arrow leading to the extracted two-\(\theta\) terms.
- `lecture_09_figure_04.png`: Tight crop of the lower board during the auxiliary-field discussion. The main visible line isolates the \(F\)-dependent part of the Lagrangian, written in terms of derivatives of the superpotential and the algebraic \(F^\ast F\) term.
- `lecture_09_figure_05.png`: Wider two-board view late in the supersymmetry-breaking discussion. The left board contains a boxed condition involving \(\partial V/\partial\phi\) and \(F\), while the right board summarizes the positive potential and related derivative conditions. The split layout itself is useful evidence for how Susskind organizes the argument.

## Blackboard Equations

- `lecture_09_figure_02.png`: \(y=x+i\bar{\theta}\sigma\theta\) [visible]
- `lecture_09_figure_02.png`: \(\Phi=\phi+\psi\theta+F\theta\theta\) [visible]
- `lecture_09_figure_02.png`: \(\bar{\psi}\,\sigma^\mu \partial_\mu \psi\) [standard reconstruction]
- `lecture_09_figure_02.png`: \(\phi^\ast \Box \phi+\bar{\psi}\,\sigma^\mu \partial_\mu \psi+F^\ast F\) [standard reconstruction]

- `lecture_09_figure_03.png`: \(\int \Phi^n\, d^2\theta+\mathrm{cc}\) [partially visible]
- `lecture_09_figure_03.png`: \(\phi+\psi\theta+F\theta\theta\) [visible]
- `lecture_09_figure_03.png`: \(\rightarrow\) [visible]
- `lecture_09_figure_03.png`: \(n\,F\,\phi^{\,n-1}+\frac{n(n-1)}{2}\phi^{\,n-2}\psi\psi+\mathrm{cc}\) [standard reconstruction]

- `lecture_09_figure_04.png`: \(F\,\dfrac{\partial V}{\partial \phi}+F^\ast\dfrac{\partial V}{\partial \phi^\ast}+F^\ast F\) [visible]
- `lecture_09_figure_04.png`: \(V(\phi)=\phi^n\ldots\) [partially visible]

- `lecture_09_figure_05.png`: \(\dfrac{\partial V}{\partial \phi}+F=0\) [partially visible]
- `lecture_09_figure_05.png`: \(V(\phi)=\left|\dfrac{\partial V}{\partial \phi}\right|^2\) [partially visible]
- `lecture_09_figure_05.png`: \(\dfrac{\partial V}{\partial \phi^\ast}+F^\ast=0\) [standard reconstruction]

## Diagram And Layout Reading

- `lecture_09_figure_02.png` has a clear three-level board structure: the shifted coordinate \(y\) at the top, the chiral superfield expansion beneath it, and the resulting component Lagrangian on the lower line. That layered layout is useful for notes because it shows Susskind moving from superspace data to ordinary component physics in one visual block.
- `lecture_09_figure_03.png` is valuable less for any one perfectly legible symbol than for the board logic. The left side gives the source expression in superspace, the middle shows the repeated factors of the component expansion, and the lower arrow indicates extraction of the two-\(\theta\) contribution. The subtitle explicitly warns that the arrow is not an equality sign, so the board’s arrow semantics matter.
- `lecture_09_figure_04.png` is not a diagram but an isolated equation plate. Its main value is that it cleanly groups all of the \(F\)-dependent terms together on one line, exactly at the point where Susskind is about to vary with respect to \(F\) and eliminate the auxiliary field.
- `lecture_09_figure_05.png` uses the two sliding boards as a before-and-after layout. The boxed equation on the left functions like a local condition or checkpoint, while the right board collects the broader consequences: the positive potential and the equations that characterize the vacuum. That spatial separation is useful to preserve in the notes.
- None of these four figures requires a standalone TikZ diagram. The only genuinely diagram-like feature is the implication arrow in `lecture_09_figure_03.png`, and that is better preserved by keeping the screenshot visible and using a nearby cleaned display with the same arrow notation.

## TeX Reconstruction Plan

- `lecture_09_figure_02.png` should remain visible. Nearby, reconstruct the mathematics as cleaned displayed equations:
  \[
  y^\mu=x^\mu+i\bar{\theta}\sigma^\mu\theta,
  \qquad
  \Phi(y,\theta)=\phi(y)+\psi(y)\theta+F(y)\theta^2,
  \]
  followed by a schematic component Lagrangian such as
  \[
  \mathcal L \sim \phi^\ast \Box \phi+\bar{\psi}\,\sigma^\mu\partial_\mu\psi+F^\ast F.
  \]
  The screenshot is best used as board-evidence for the transition from superspace expansion to the fermion kinetic term.

- `lecture_09_figure_03.png` should remain visible. Do not try to redraw the whole board; instead place a cleaned display nearby that preserves the board’s implication structure rather than replacing it with an equals sign, for example
  \[
  \int d^2\theta\,\Phi^n+\mathrm{cc}
  \;\leadsto\;
  nF\phi^{n-1}+\frac{n(n-1)}{2}\phi^{n-2}\psi\psi+\mathrm{cc}.
  \]
  The screenshot is important because it documents the visual logic of “pick out the two-\(\theta\) term.”

- `lecture_09_figure_04.png` should remain visible. Nearby, reconstruct the \(F\)-dependent part of the Lagrangian in a cleaned form. Since the board suppresses some conjugation detail, the safest nearby version is
  \[
  \mathcal L(F)=F\,\frac{\partial V}{\partial\phi}
  +F^\ast\,\frac{\partial V^\ast}{\partial\phi^\ast}
  +F^\ast F,
  \]
  or the corresponding transcript-stabilized schematic equivalent. This screenshot is the documentary anchor for the auxiliary-field elimination step.

- `lecture_09_figure_05.png` should remain visible. Nearby, reconstruct the vacuum-condition and potential formulas as separate displayed equations, for example
  \[
  \frac{\partial V}{\partial\phi}+F^\ast=0,
  \qquad
  \frac{\partial V^\ast}{\partial\phi^\ast}+F=0,
  \]
  together with
  \[
  V_{\text{ordinary}}(\phi)=\left|\frac{\partial V}{\partial\phi}\right|^2.
  \]
  The screenshot is worth keeping because the split-board arrangement itself helps show the move from local algebraic condition to the positivity of the potential and the vacuum discussion.

## Caption Drafts

- `lecture_09_figure_02.png`: Chiral superfield recap and the fermion kinetic term
- `lecture_09_figure_03.png`: Extracting the two-\(\theta\) term from \(\Phi^n\)
- `lecture_09_figure_04.png`: Auxiliary-field terms in the component Lagrangian
- `lecture_09_figure_05.png`: Vacuum condition and the positive supersymmetric potential

## Uncertainties

- In `lecture_09_figure_02.png`, the lower scalar term is partly hidden by Susskind’s body and shadow. The frame strongly supports the fermion kinetic term, but the full scalar kinetic structure is better reconstructed from the surrounding lecture than from the image alone.
- In `lecture_09_figure_02.png`, the exact index placement on the sigma-matrix term is not fully legible, so \(\bar{\psi}\,\sigma^\mu\partial_\mu\psi\) should be treated as a cautious cleaned form rather than a character-by-character board transcription.
- In `lecture_09_figure_03.png`, the right-hand extracted terms are only partly legible. The board definitely shows a component expansion and an implication arrow, but the precise coefficients and every power of \(\phi\) should be stabilized from the transcript, not claimed from the frame alone.
- In `lecture_09_figure_03.png`, the subtitle explicitly warns that the arrow does not mean equality. Any TeX reconstruction should preserve that semantic distinction.
- In `lecture_09_figure_04.png`, the board appears to use \(V(\phi)\) language for the superpotential, but later the lecture also uses \(V\) for the ordinary potential. The notation on the board is therefore locally useful but globally unstable.
- In `lecture_09_figure_04.png`, the second derivative term with respect to \(\phi^\ast\) may have suppressed conjugation on the board. A cleaned nearby formula should note that the lecture is schematic there.
- In `lecture_09_figure_05.png`, the boxed left equation is not crisp enough to settle whether the term added to the derivative is \(F\) or \(F^\ast\). The transcript indicates that Susskind briefly corrects a conjugation issue in this part of the lecture, so the cleaned equation should be treated cautiously.
- In `lecture_09_figure_05.png`, the top-right formula is best read as the ordinary potential written as an absolute-value square of a derivative, but the exact letter choice and conjugation marks are not perfectly stable from the image alone.