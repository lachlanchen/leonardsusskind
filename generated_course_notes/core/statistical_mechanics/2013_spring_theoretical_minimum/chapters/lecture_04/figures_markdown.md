# Figure Notes
## Image Inventory
- `lecture_04_figure_02.png`: Blackboard frame from the Boltzmann-distribution derivation. The lecturer stands in front of the board, but the main right-hand derivation is still readable: a stationarity equation at top, a logarithmic rearrangement in the middle, and a boxed final probability formula below.
- `lecture_04_figure_03.png`: Blackboard frame centered on the thermodynamic definition of temperature. The right lower panel contains a vertical sequence of three equations relating \(E\), \(S\), and \(T\). A cropped boxed formula from the preceding entropy discussion remains visible above.
- `lecture_04_figure_04.png`: Blackboard frame from the ideal-gas example. The board shows a beta-derivative formula for the energy at upper right, a lower line giving the \(\log z\) dependence on \(\log \beta\), and leftover ideal-gas partition-function factors on the left, including \(\left(2m\pi/\beta\right)^{3N/2}\).

## Blackboard Equations
- `lecture_04_figure_02.png`: [visible] \(\dfrac{\partial F'}{\partial P_i}=\log P_i+1+\alpha+\beta E_i=0\)
- `lecture_04_figure_02.png`: [visible] \(\log P_i=-(1+\alpha)-\beta E_i\)
- `lecture_04_figure_02.png`: [visible] \(P_i=\dfrac{1}{Z}e^{-\beta E_i}\)
- `lecture_04_figure_03.png`: [visible] \(dE=T\,dS\)
- `lecture_04_figure_03.png`: [visible] \(\dfrac{dE}{dS}=T\)
- `lecture_04_figure_03.png`: [visible] \(\dfrac{1}{T}=\dfrac{dS}{dE}\)
- `lecture_04_figure_03.png`: [partially visible] \(S=\beta E+\log z(\beta)\)
- `lecture_04_figure_04.png`: [visible] \(-\dfrac{\partial \log z}{\partial \beta}=+\dfrac{3N}{2}T\)
- `lecture_04_figure_04.png`: [partially visible] \(\left(\dfrac{2m\pi}{\beta}\right)^{3N/2}\)
- `lecture_04_figure_04.png`: [partially visible] \(\log z=-\dfrac{3N}{2}\log\beta+\mathrm{const}\)
- `lecture_04_figure_04.png`: [standard reconstruction] \(E=-\dfrac{d\log z}{d\beta}\)

## Diagram And Layout Reading
- `lecture_04_figure_02.png`: The board is organized as a short top-to-bottom derivation. The visual emphasis is the boxed final line, so the screenshot works as documentary evidence for the moment when the Lagrange-multiplier calculation turns into the exponential probability law.
- `lecture_04_figure_02.png`: There is no actual diagram here, but the layout matters: top line is the extremization condition, middle line solves for \(\log P_i\), bottom line rewrites the answer in normalized exponential form.
- `lecture_04_figure_03.png`: The right-hand board is reserved for the thermodynamic identities. The three equations are stacked vertically and read naturally downward as a derivation from \(dE=T\,dS\) to the inverse-temperature relation.
- `lecture_04_figure_03.png`: The cropped boxed expression above the stack visually ties this temperature step back to the earlier entropy formula, even though that upper formula is not fully visible in the frame.
- `lecture_04_figure_04.png`: The board is visually split. The right-hand side isolates the energy formula, while the left-hand side preserves the ideal-gas \(\beta\)-dependence from the partition-function calculation. The frame therefore shows both the result and the source of the result at once.
- `lecture_04_figure_04.png`: There is no plotted graph or axis here; the important “layout reading” is that the right upper formula is a summary statement, while the lower and left fragments record the logarithmic and partition-function ingredients used to get it.

## TeX Reconstruction Plan
- `lecture_04_figure_02.png` should remain visible in the notes. Pair it with a clean displayed derivation of the canonical distribution:
  \[
  \frac{\partial F'}{\partial P_i}=0
  \quad\Rightarrow\quad
  \log P_i=-(1+\alpha)-\beta E_i
  \quad\Rightarrow\quad
  P_i=\frac{1}{Z}e^{-\beta E_i}.
  \]
- `lecture_04_figure_02.png` does not need a TikZ redraw. Its value is equation evidence and board sequencing.
- `lecture_04_figure_03.png` should remain visible in the notes. Pair it with a clean displayed chain
  \[
  dE=T\,dS,\qquad \frac{dE}{dS}=T,\qquad \frac{1}{T}=\frac{dS}{dE},
  \]
  and, if useful in the surrounding prose, also reproduce the earlier entropy relation \(S=\beta E+\log z\) nearby as a transcript-backed completion of the cropped box.
- `lecture_04_figure_03.png` does not need a TikZ redraw. The frame is purely equation-documentary.
- `lecture_04_figure_04.png` should remain visible in the notes. Pair it with clean displayed equations for
  \[
  E=-\frac{d\log z}{d\beta},
  \qquad
  \log z=-\frac{3N}{2}\log\beta+\mathrm{const},
  \qquad
  E=\frac{3N}{2}T.
  \]
- `lecture_04_figure_04.png` also does not need TikZ. What matters is the documentary relation between the \(\beta\)-dependence of the ideal-gas partition function and the resulting energy formula.

## Caption Drafts
- `lecture_04_figure_02.png`: Lagrange-multiplier derivation of the Boltzmann distribution
- `lecture_04_figure_03.png`: Temperature from the entropy-energy derivative
- `lecture_04_figure_04.png`: Ideal-gas energy from the \(\beta\)-dependence of \(\log z\)

## Uncertainties
- `lecture_04_figure_02.png`: The function name in the top derivative appears to be \(F'\), but the lecturer partly blocks the left side of the line; the intended expression is nevertheless clear from the visible symbols and the surrounding algebra.
- `lecture_04_figure_02.png`: The normalization symbol in the final boxed line looks like an uppercase \(Z\), whereas the lecture transcript often speaks of \(z\). The notes should standardize deliberately and note only if the distinction matters locally.
- `lecture_04_figure_03.png`: The boxed formula above the temperature relations is cropped; only the right portion is visible. The completion \(S=\beta E+\log z(\beta)\) is supported by the transcript but is not fully documented by the screenshot alone.
- `lecture_04_figure_04.png`: The upper-right equation uses a partial-derivative symbol on the board, but in the ideal-gas context the dependence is effectively only on \(\beta\), so the notes may reasonably standardize to an ordinary derivative in the cleaned derivation.
- `lecture_04_figure_04.png`: The left side of the lower \(\log z\) equation is partly obscured by the lecturer, so the full expression \(\log z=-\frac{3N}{2}\log\beta+\mathrm{const}\) is a cautious completion of a partially visible line rather than a fully literal transcription.
- `lecture_04_figure_04.png`: The board handwriting for \(\log\) is somewhat abbreviated, closer to “lg” in places; the notes should normalize this to \(\log\).