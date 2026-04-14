# Figure Notes
## Image Inventory
- `lecture_04_figure_02.png`: Blackboard sketch of a closed string projected into the \(xy\)-plane. A single point on the loop is marked and labeled \(\sigma=0\). A simple \(x\)-\(y\) axis cross appears at the right. Susskind is visible at the far left but does not block the marked point.
- `lecture_04_figure_03.png`: Blackboard view of the later discrete-string discussion. At the far left there is a partially cropped closed-loop sketch with discrete point marks along part of the contour. In the center are the labels \(X(\sigma)\), \(X_i\), \(Y_i\), and \(i=1\ldots N\). At the right is a partially obscured wavefunction block beginning with \(\Psi(\cdots)\), intended to show cyclic relabeling.
- `lecture_04_figure_04.png`: Close-up of the sigma-shift-invariance equation. The left edge shows a leading \(0\), followed by an equality and a term \(\Psi(X(\sigma+\epsilon))\). Beneath it is a derivative product involving \(\partial\Psi/\partial X(\sigma)\), \(\partial X/\partial\sigma\), and \(\epsilon\). The right side of the upper line is cropped.
- `lecture_04_figure_05.png`: Blackboard snapshot during the level-matching derivation. At the top is the discrete shift \(X_i\to X_{i+1}\). Below it are a small circle mark and a lower line beginning with a symbol that looks like \(\phi\), then an equals sign and the beginning of an integral. Susskind is erasing part of the lower expression. A fragment of an earlier closed-string sketch survives at the far left edge.

## Blackboard Equations
- `lecture_04_figure_02.png`: \(\sigma=0\) [visible]
- `lecture_04_figure_02.png`: \(x\) [visible]
- `lecture_04_figure_02.png`: \(y\) [visible]

- `lecture_04_figure_03.png`: \(X(\sigma)\) [visible]
- `lecture_04_figure_03.png`: \(X_i\) [visible]
- `lecture_04_figure_03.png`: \(Y_i\) [visible]
- `lecture_04_figure_03.png`: \(i=1\ldots N\) [visible]
- `lecture_04_figure_03.png`: \(\Psi(\cdots)\) [partially visible]
- `lecture_04_figure_03.png`: \(\Psi(x_1,x_2,x_3,\ldots,x_N)\) [standard reconstruction]
- `lecture_04_figure_03.png`: \(\Psi(x_2,\ldots,x_N,x_1)\) [standard reconstruction]

- `lecture_04_figure_04.png`: \(0=\Psi(X(\sigma+\epsilon))-\cdots\) [partially visible]
- `lecture_04_figure_04.png`: \(\frac{\partial\Psi}{\partial X(\sigma)}\,\frac{\partial X}{\partial\sigma}\,\epsilon\) [visible]
- `lecture_04_figure_04.png`: \(\Psi(X(\sigma+\epsilon))-\Psi(X(\sigma))\) [standard reconstruction]

- `lecture_04_figure_05.png`: \(X_i\to X_{i+1}\) [visible]
- `lecture_04_figure_05.png`: \(\phi\) [partially visible]
- `lecture_04_figure_05.png`: \(\phi=\int P(\sigma)\cdots\) [partially visible]
- `lecture_04_figure_05.png`: \(\int d\sigma\,P(\sigma)\,\partial_\sigma X(\sigma)=0\) [standard reconstruction]
- `lecture_04_figure_05.png`: \(\int d\sigma\,\partial_\tau X\,\partial_\sigma X=0\) [standard reconstruction]

## Diagram And Layout Reading
- `lecture_04_figure_02.png` is the clean geometric setup for closed strings. The important visual fact is that the choice of \(\sigma=0\) is shown as a marked point on an otherwise featureless loop, with the \(x\)- and \(y\)-axes nearby to stress that the sketch lives in the transverse plane.
- In `lecture_04_figure_02.png`, the loop is not meant to be a mathematically special shape. Its job is to show that one point has been chosen as the origin of the sigma coordinate and that the choice is arbitrary.
- `lecture_04_figure_03.png` has a three-part board organization. Left: a discretized closed-loop picture. Center: the passage from continuous notation \(X(\sigma)\) to discrete labels \(X_i,Y_i\). Right: the wavefunction block, where cyclically shifted argument lists are being compared.
- The left loop in `lecture_04_figure_03.png` is cropped, so the screenshot is useful mainly as evidence for the board layout and the coexistence of the loop picture with the discrete labels and wavefunction, not as a perfect standalone diagram.
- `lecture_04_figure_04.png` is purely equation-focused. The cropped top line shows that the lecture is expanding a shifted wavefunctional argument, while the lower line isolates the derivative structure that comes from a small \(\sigma\to\sigma+\epsilon\) change.
- `lecture_04_figure_05.png` is also a layout frame rather than a clean equation frame. It visibly links the discrete cyclic shift \(X_i\to X_{i+1}\) to the beginning of the continuous integral constraint, which is exactly the conceptual bridge the lecture is making at that moment.
- In `lecture_04_figure_05.png`, Susskind is already erasing part of the lower line. That makes the frame valuable as evidence of the transition and board hierarchy, but not as sufficient evidence for the full formula by itself.

## TeX Reconstruction Plan
- `lecture_04_figure_02.png` should remain visible in the notes. Pair it with a small TikZ redraw of a closed loop in the \(xy\)-plane with one distinguished point marked \(\sigma=0\). The screenshot carries the blackboard feel; the TikZ redraw should carry the clean geometry.
- `lecture_04_figure_03.png` should remain visible in the notes. Nearby, typeset the discrete notation and the cyclic wavefunction condition explicitly:
  \(\Psi(x_1,x_2,\ldots,x_N)=\Psi(x_2,\ldots,x_N,x_1)\),
  with a compact TikZ redraw of a discretized closed loop if a cleaner schematic is needed.
- `lecture_04_figure_04.png` should remain visible in the notes as screenshot evidence for the small-\(\epsilon\) expansion. Pair it with a cleaned displayed equation reconstructed from the lecture:
  \(0=\Psi(X(\sigma+\epsilon))-\Psi(X(\sigma))\),
  followed by the first-order term involving
  \(\frac{\partial\Psi}{\partial X(\sigma)}\frac{\partial X}{\partial\sigma}\epsilon\),
  and then the integrated version over \(\sigma\).
- `lecture_04_figure_05.png` should remain visible in the notes, but it must be supplemented by a cleaned displayed constraint because the image is incomplete:
  \(\int d\sigma\,P(\sigma)\,\partial_\sigma X(\sigma)=0\),
  and then, after using \(P(\sigma)=\partial_\tau X\),
  \(\int d\sigma\,\partial_\tau X\,\partial_\sigma X=0\).
- For `lecture_04_figure_05.png`, the screenshot is best used to preserve the board transition from discrete relabeling \(X_i\to X_{i+1}\) to the continuous reparameterization constraint, rather than as the sole source of the final equation.

## Caption Drafts
- `lecture_04_figure_02.png`: Closed string with a marked \(\sigma=0\) point
- `lecture_04_figure_03.png`: Discrete closed string and cyclic wavefunction labeling
- `lecture_04_figure_04.png`: Small-\(\epsilon\) shift of the wavefunctional argument
- `lecture_04_figure_05.png`: Discrete shift and the emerging reparameterization constraint

## Uncertainties
- In `lecture_04_figure_03.png`, the left loop is cropped at the edge of the frame, and the right wavefunction block is partly obscured by Susskind. The cyclically shifted \(\Psi\)-arguments therefore need transcript-based stabilization.
- In `lecture_04_figure_03.png`, the bottom index range is written faintly; it reads like \(i=1\ldots N\), but the punctuation is not crisp enough to insist on the exact blackboard separator without standard cleanup.
- In `lecture_04_figure_04.png`, the upper line is cut off on the right, so the subtraction term after \(\Psi(X(\sigma+\epsilon))\) is not fully visible. The standard completion \(-\Psi(X(\sigma))\) should be treated as transcript-backed.
- In `lecture_04_figure_04.png`, the lower derivative expression is clear, but the exact status of the derivative as ordinary or functional is part of the lecture’s transition; the final notes should follow the transcript’s logic carefully when upgrading the notation.
- In `lecture_04_figure_05.png`, the lower symbol looks like \(\phi\), but it is partly affected by the erasure. The integral’s right-hand side is cropped, so the full constraint must be reconstructed from the transcript rather than claimed as fully image-secured.
- In `lecture_04_figure_05.png`, the visible integral begins with \(P(\cdots)\), but the exact argument and the rest of the integrand are not fully readable from the image alone.