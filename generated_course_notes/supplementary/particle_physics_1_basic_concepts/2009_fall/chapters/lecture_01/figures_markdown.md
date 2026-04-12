# Figure Notes
## Image Inventory
- `lecture_01_figure_02.png`: Susskind stands at a mostly blank board and writes at the upper left. The visible notation is the Greek letter lambda followed by an equals sign and the beginning of a word. The image is useful mainly as documentary evidence for the introduction of the wavelength symbol.
- `lecture_01_figure_03.png`: A tight crop of the right-hand board region. The upper relation `f = 1/T` is clearly visible, and below it the equation `\lambda f = c` is written large and centered. At the far left edge there are cropped remnants of earlier writing, including part of the word “period” and part of an earlier boxed relation.
- `lecture_01_figure_04.png`: A later board state showing a more developed cluster of wave formulas. At upper right appears the frequency conversion relation in terms of omega and \(2\pi\); below it is `f = c/\lambda`; and at lower right a boxed final equation gives the wave-motion relation in terms of \(\omega\), \(c\), and \(\lambda\). A partial earlier box remains at the left edge.
- `lecture_01_figure_05.png`: Susskind points at a cleanly written `E = m` on the right side of the board. Beneath it is a second, less legible dimensional-looking relation involving \(m\), a squared length-like quantity over \(t^2\), and \(E\). At the far right edge there is a cropped sketch from the earlier rest-energy discussion.

## Blackboard Equations
- `lecture_01_figure_02.png`: `\lambda =` [visible]
- `lecture_01_figure_02.png`: `\lambda = \text{w...}` [partially visible]
- `lecture_01_figure_02.png`: `\lambda = \text{wavelength}` [standard reconstruction]

- `lecture_01_figure_03.png`: `f = \frac{1}{T}` [visible]
- `lecture_01_figure_03.png`: `\lambda f = c` [visible]
- `lecture_01_figure_03.png`: `\text{period}` [partially visible]

- `lecture_01_figure_04.png`: `\frac{\omega}{2\pi} = f` [partially visible]
- `lecture_01_figure_04.png`: `f = \frac{c}{\lambda}` [visible]
- `lecture_01_figure_04.png`: `\omega = \frac{2\pi c}{\lambda}` [visible]
- `lecture_01_figure_04.png`: `\lambda f = c` [partially visible]

- `lecture_01_figure_05.png`: `E = m` [visible]
- `lecture_01_figure_05.png`: `E = mc^{2} \to E = m` [standard reconstruction]
- `lecture_01_figure_05.png`: `m\,\ell^{2}/t^{2} = E` [partially visible]

## Diagram And Layout Reading
- `lecture_01_figure_02.png` is not a diagrammatic figure in the usual sense; its value is the board position and lecture moment. The notation is introduced at the upper left of an otherwise empty board, so the screenshot records the start of a new mini-derivation.
- `lecture_01_figure_03.png` shows a compact right-side board layout: the more basic relation `f = 1/T` sits above, and the more directly useful wave-speed relation `\lambda f = c` is placed below in larger writing. The left edge preserves enough of the earlier board to show that this is continuing a sequence rather than an isolated formula.
- `lecture_01_figure_04.png` preserves the derivational organization of the board. The older relation remains boxed at left, the intermediate conversion formulas are stacked above and center-right, and the final result `\omega = 2\pi c/\lambda` is boxed below. That boxed lower-right placement matters for note writing because it shows which equation Susskind is treating as the takeaway.
- `lecture_01_figure_05.png` is organized around the natural-units simplification on the right side of the board. Susskind’s pointing gesture makes `E = m` the focal statement. The lower dimensional relation and the cropped sketch at right indicate this comes out of a larger discussion of energy, units, and rest-energy examples rather than standing alone.

## TeX Reconstruction Plan
- `lecture_01_figure_02.png` should remain visible. It is the documentary evidence for the moment when Susskind introduces \(\lambda\) as the symbol for wavelength. Pair it with a clean displayed or inline reconstruction `\lambda = \text{wavelength}` nearby.
- `lecture_01_figure_03.png` should remain visible. Reconstruct the two equations as clean display math:
  \[
  f=\frac{1}{T}, \qquad \lambda f = c.
  \]
  No TikZ redraw is needed; the screenshot already functions mainly as board evidence.
- `lecture_01_figure_04.png` should remain visible. It is best treated as the culmination of the wave-relation sequence, and it should be paired with a clean reconstruction of
  \[
  \frac{\omega}{2\pi}=f,\qquad f=\frac{c}{\lambda},\qquad \omega=\frac{2\pi c}{\lambda}.
  \]
  The notes benefit from preserving the screenshot and then typesetting the final boxed equation cleanly.
- `lecture_01_figure_05.png` should remain visible. Pair it with a careful typeset explanation that in natural units \(c=1\), so the rest-energy relation is written as
  \[
  E = m.
  \]
  The screenshot should not be used to support any stronger claim about the lower relation unless the transcript also carries that step clearly.
- Across the chapter, `lecture_01_figure_03.png` and `lecture_01_figure_04.png` should appear as a short visual sequence: first the basic wavelength-frequency relation, then the omega-based reformulation.

## Caption Drafts
- `lecture_01_figure_02.png`: Introducing \(\lambda\) as wavelength
- `lecture_01_figure_03.png`: Frequency and wavelength relations on the board
- `lecture_01_figure_04.png`: Boxed wave-motion relation in terms of \(\omega\)
- `lecture_01_figure_05.png`: Rest-energy relation in natural units

## Uncertainties
- In `lecture_01_figure_02.png`, only the beginning of the word after the equals sign is visible. The full reading “wavelength” is supported by the subtitle and transcript, not by the screenshot alone.
- In `lecture_01_figure_03.png`, the denominator in `f = 1/T` is best read as \(T\), but the handwritten form is slightly stylized. The nearby cropped word “period” supports that interpretation.
- In `lecture_01_figure_04.png`, the top relation `\omega/(2\pi)=f` is not as crisp as the lower equations; the boxed final equation is the most secure element of the frame.
- In `lecture_01_figure_05.png`, the lower relation beneath `E = m` is not fully legible. It appears to be a dimensional mnemonic of the form \(m\,\ell^{2}/t^{2}=E\), but that should be treated cautiously unless confirmed elsewhere in the transcript or surrounding frames.
- `lecture_01_figure_05.png` shows the natural-units simplification `E = m`, not the full textbook form `E = mc^{2}`. The distinction matters because the lecture is explicitly discussing the convention \(c=1\).