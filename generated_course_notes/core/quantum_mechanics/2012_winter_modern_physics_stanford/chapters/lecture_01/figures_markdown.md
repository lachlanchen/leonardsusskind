# Figure Notes
## Image Inventory
- `lecture_01_figure_02.png` shows a whiteboard layout centered on a broad single-peaked curve drawn across the lower middle of the board. At left there is a large faint oval enclosing a smaller cluster of concentric loops or rings near its center, plus a short isolated arc near the upper left edge. At upper right there is a small triangle-like sketch with three marked points joined by directed segments. Leonard Susskind stands at the far right edge, leaving the drawings largely unobstructed.
- `lecture_01_figure_04.png` shows the equation cluster from the photon-to-de Broglie derivation. At upper left the photon-energy relation is written; at upper middle/right the angular-frequency relation appears; at right center there is a time-or-period relation and a standalone wavelength symbol; at center-right a boxed relation connects \(c\), \(\lambda\), and \(f\). Lower left and lower middle contain partially blocked momentum formulas. The lecturer stands in front of the lower-left part of the derivation.
- `lecture_01_figure_05.png` is a tighter crop of the same board region, now focused on the lecturer actively rewriting an erased equation at center-right. The top-left photon-energy relation remains visible, the \(\omega=2\pi f\) line is partly visible at upper right, and the boxed \(c/\lambda\)-to-\(f\) relation is partly visible at lower right. The exact equation being rewritten is hidden by the lecturer’s hand and body.

## Blackboard Equations
- `lecture_01_figure_02.png`: no stable equation is legible; the frame is primarily diagrammatic. Any point labels in the upper-right triangle are too unclear to transcribe safely.
- `lecture_01_figure_04.png`: \(E = h f = \hbar \omega\) [partially visible]
- `lecture_01_figure_04.png`: \(\omega = 2\pi f\) [visible]
- `lecture_01_figure_04.png`: \(t = \frac{1}{f}\) [visible]
- `lecture_01_figure_04.png`: \(\lambda\) [visible]
- `lecture_01_figure_04.png`: \(\frac{c}{\lambda} = f\) [partially visible]
- `lecture_01_figure_04.png`: \(\frac{E}{c} = p\) [partially visible]
- `lecture_01_figure_04.png`: \(p = \frac{h f}{c}\) [partially visible]
- `lecture_01_figure_04.png`: \(p = \frac{h}{\lambda}\) [standard reconstruction]
- `lecture_01_figure_05.png`: \(E = h f = \hbar \omega\) [partially visible]
- `lecture_01_figure_05.png`: \(\omega = 2\pi f\) [partially visible]
- `lecture_01_figure_05.png`: \(\frac{c}{\lambda} = f\) [partially visible]
- `lecture_01_figure_05.png`: \(\lambda\) [visible]
- `lecture_01_figure_05.png`: \(p = \frac{h}{\lambda}\) [standard reconstruction]

## Diagram And Layout Reading
- In `lecture_01_figure_02.png`, the board is organized around a central probability-profile sketch. The broad hump has no explicit axes, but its role as a probability distribution is supported by the transcript and by the way it is isolated at center stage. The left-hand oval-with-inner-rings sketch looks like a retained detector or aperture drawing from the immediately preceding discussion rather than a second probability plot. The upper-right triangle-like figure is an auxiliary sketch with arrows between three points; it is visually distinct from the main curve and should not be overread as part of the probability distribution itself.
- The most important visual fact of `lecture_01_figure_02.png` is therefore layout: Susskind has left an earlier detector sketch on the left, introduced the new broad distribution in the middle, and kept a small auxiliary directional diagram at upper right. That arrangement helps preserve the lecture’s flow from detector geometry to momentum-distribution reasoning.
- In `lecture_01_figure_04.png`, the board is arranged as a derivation cluster rather than as a single display equation. The top line gives photon energy and angular frequency, the right side gives the period/wavelength facts, and the boxed relation at center-right functions as the bridge from wave kinematics to the elimination of frequency. The lower-left region, partly covered by the lecturer, is where the momentum relation is being assembled.
- In `lecture_01_figure_05.png`, the emphasis is no longer the finished cluster but the act of restoration: the lecturer is rewriting an erased step at the place where the momentum-wavelength relation belongs. The screenshot is valuable because it documents that the relation was explicitly reintroduced, even though the chalk itself is occluded.

## TeX Reconstruction Plan
- `lecture_01_figure_02.png` should remain visible. It should be paired with a clean TikZ redraw of the broad one-dimensional probability distribution nearby. The screenshot should carry the original board layout, while the TikZ figure should carry the legibility burden for the probability-profile shape. The left oval sketch and the upper-right triangle should be mentioned in the prose as auxiliary board remnants unless the chapter later needs them enough to justify separate redraws.
- `lecture_01_figure_04.png` should remain visible. Nearby, the notes should typeset the cleaned derivation as displayed equations, not rely on the board for full legibility. The likely equation block is:
  \(E = h f = \hbar \omega\),
  \(\omega = 2\pi f\),
  \(T = 1/f\) or, if preserving the board more literally, \(t = 1/f\),
  \(c = \lambda f\) equivalently \(f = c/\lambda\),
  \(p = E/c\),
  and then \(p = h/\lambda\).
  The screenshot is especially useful as documentary evidence for how Susskind grouped these relations on the board.
- `lecture_01_figure_05.png` should also remain visible, but as a supporting screenshot-plus-equation figure rather than as the primary source for the equation itself. It should be placed near the point in the notes where the lecturer says that the erased equation was the momentum relation. The nearby typeset equation should explicitly restore \(p = h/\lambda\), with a brief note that the screenshot documents the reprise even though the exact chalk line is blocked by the lecturer’s hand.

## Caption Drafts
- `lecture_01_figure_02.png`: Probability-distribution sketch for the detector momentum
- `lecture_01_figure_04.png`: Photon relations leading to the de Broglie formula
- `lecture_01_figure_05.png`: Rewriting the erased momentum-wavelength relation

## Uncertainties
- In `lecture_01_figure_02.png`, the left oval-and-rings sketch is clear as a drawing but unclear in exact interpretation from the image alone; it likely belongs to the preceding detector discussion. The upper-right triangle-like diagram also contains labels that are too faint to transcribe confidently.
- The central hump in `lecture_01_figure_02.png` has no drawn axes or symbolic labels in the frame itself. Its reading as a probability distribution comes from the subtitle and surrounding lecture context rather than from board labels.
- In `lecture_01_figure_04.png`, the lower-left momentum chain is partly hidden by the lecturer, so the exact chalk sequence from \(p=E/c\) to \(p=h/\lambda\) is not fully recoverable character by character from the image alone.
- The boxed wave relation in `lecture_01_figure_04.png` looks like \(\frac{c}{\lambda}=f\), but a normalized typeset form \(c=\lambda f\) may read better in the notes. The frame supports the equivalence, not necessarily the preferred final formatting.
- The relation written as \(t=\frac{1}{f}\) on the board may be intended as the period of one cycle; in polished notes it may be worth normalizing this to \(T=\frac{1}{f}\), while noting that the board itself appears to use lowercase \(t\).
- In `lecture_01_figure_05.png`, the exact erased equation being rewritten is not readable because the lecturer’s hand and body block it. The transcript strongly supports reconstructing it as \(p=\frac{h}{\lambda}\), but that reconstruction should be presented as transcript-guided rather than as a direct character-by-character board transcription.