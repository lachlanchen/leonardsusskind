# Visual Evidence
## Frame Inventory
- `lecture_04_figure_02.png`: Shows a closed-loop string sketch in the \(xy\)-plane with one marked point labeled \(\sigma=0\) and a nearby \(x\)-\(y\) axis cross; the screenshot should remain in the final notes.
- `lecture_04_figure_03.png`: Shows the later board state with a partially cropped discretized closed loop, the labels \(X(\sigma)\), \(X_i\), \(Y_i\), \(i=1\ldots N\), and a partly obscured wavefunction block on the right; the screenshot should remain in the final notes.
- `lecture_04_figure_04.png`: Shows the key local equation for the infinitesimal sigma shift, with \(0=\Psi(X(\sigma+\epsilon))-\cdots\) above and a derivative product below; the screenshot should remain in the final notes.
- `lecture_04_figure_05.png`: Shows the transition from the discrete relabeling \(X_i\to X_{i+1}\) to the beginning of the continuous integral constraint while Susskind is erasing; the screenshot should remain in the final notes.

## Equation Extraction
- `lecture_04_figure_02.png`: \(\sigma=0\) [visible]
- `lecture_04_figure_02.png`: \(x\) [visible]
- `lecture_04_figure_02.png`: \(y\) [visible]

- `lecture_04_figure_03.png`: \(X(\sigma)\) [visible]
- `lecture_04_figure_03.png`: \(X_i\) [visible]
- `lecture_04_figure_03.png`: \(Y_i\) [visible]
- `lecture_04_figure_03.png`: \(i=1\ldots N\) [visible]
- `lecture_04_figure_03.png`: \(\Psi(\cdots)\) [partially visible]
- `lecture_04_figure_03.png`: \(\Psi(x_1,x_2,x_3,\ldots,x_N)\) [standard completion]
- `lecture_04_figure_03.png`: \(\Psi(x_2,\ldots,x_N,x_1)\) [standard completion]

- `lecture_04_figure_04.png`: \(0=\Psi\bigl(X(\sigma+\epsilon)\bigr)-\cdots\) [partially visible]
- `lecture_04_figure_04.png`: \(\dfrac{\partial\Psi}{\partial X(\sigma)}\,\dfrac{\partial X}{\partial\sigma}\,\epsilon\) [visible]
- `lecture_04_figure_04.png`: \(\Psi\bigl(X(\sigma+\epsilon)\bigr)-\Psi\bigl(X(\sigma)\bigr)\) [standard completion]

- `lecture_04_figure_05.png`: \(X_i\to X_{i+1}\) [visible]
- `lecture_04_figure_05.png`: \(\phi\) [partially visible]
- `lecture_04_figure_05.png`: \(\phi=\int P(\sigma)\cdots\) [partially visible]
- `lecture_04_figure_05.png`: \(\int d\sigma\,P(\sigma)\,\partial_\sigma X(\sigma)=0\) [standard completion]
- `lecture_04_figure_05.png`: \(\int d\sigma\,\partial_\tau X\,\partial_\sigma X=0\) [standard completion]

## Diagram Extraction
- `lecture_04_figure_02.png`: The closed string with one distinguished point should be shown both ways: preserve the screenshot as blackboard evidence and redraw it in TikZ as a clean loop in the \(xy\)-plane with a marked \(\sigma=0\) point.
- `lecture_04_figure_03.png`: The discretized closed loop and the board layout linking \(X(\sigma)\), \(X_i\), \(Y_i\), and the cyclic wavefunction should also be shown both ways: keep the screenshot and add a compact TikZ redraw of a discretized loop plus a clean typeset wavefunction relation.
- `lecture_04_figure_04.png`: This is not really a diagram frame; it is equation evidence. Keep the screenshot, but do not redraw it in TikZ. Instead, place a cleaned displayed equation nearby.
- `lecture_04_figure_05.png`: This is mainly a board-transition frame rather than a clean standalone equation. Keep the screenshot as evidence of the shift from \(X_i\to X_{i+1}\) to the integral constraint, then typeset the clean equations rather than trying to redraw the board state.

## Reconstruction Guidance
- Use `lecture_04_figure_02.png` to anchor the opening closed-string geometry. The notes should reproduce the idea cleanly as a TikZ loop with one marked point, but the screenshot should stay nearby because it captures the blackboard fact that the chosen \(\sigma=0\) point is arbitrary rather than geometrically distinguished.
- Use `lecture_04_figure_03.png` to support the later shift-invariance discussion. The clean note version should separate the content into two pieces: a short displayed block for \(X(\sigma)\), \(X_i\), \(Y_i\), \(i=1,\ldots,N\), and a separate displayed cyclic relation such as \(\Psi(x_1,\ldots,x_N)=\Psi(x_2,\ldots,x_N,x_1)\).
- Use `lecture_04_figure_04.png` as evidence for the local small-\(\epsilon\) expansion, but not as the sole source of the final notation. The finished notes should typeset a cleaned first-order expansion of the shifted wavefunctional, and the derivative should be upgraded cautiously to functional notation only if the surrounding exposition makes that step explicit.
- Use `lecture_04_figure_05.png` to preserve the conceptual bridge, not to transcribe every symbol literally. The clean notes should state the continuous constraint in full,
  \(\int d\sigma\,P(\sigma)\,\partial_\sigma X(\sigma)=0\),
  then substitute \(P(\sigma)=\partial_\tau X\) in the lecture’s model to obtain
  \(\int d\sigma\,\partial_\tau X\,\partial_\sigma X=0\).
- Where a screenshot is incomplete, prefer a clean displayed equation backed by transcript context rather than an over-literal but broken transcription. The screenshots matter most as visual proof of board order, emphasis, and the presence of key terms.

## Uncertainties
- In `lecture_04_figure_03.png`, the right-hand wavefunction block is partly obscured by Susskind, so the exact cyclic argument order is not fully image-secured and should be stabilized from the transcript.
- In `lecture_04_figure_03.png`, the notation \(i=1\ldots N\) is readable in substance, but the exact punctuation or separator on the board is faint.
- In `lecture_04_figure_04.png`, the top line is cropped on the right, so the subtraction term after \(\Psi(X(\sigma+\epsilon))\) is not fully visible.
- In `lecture_04_figure_04.png`, the board uses ordinary derivative-looking notation, but the mathematical object is a wavefunctional; the final notes should handle that upgrade carefully rather than pretending the board itself was fully explicit.
- In `lecture_04_figure_05.png`, the leading lower symbol may be \(\phi\) or another placeholder, but it is partly erased and should not be treated as reliable notation.
- In `lecture_04_figure_05.png`, only the beginning of the integral is visible, so the completed constraint must come from cautious reconstruction rather than direct transcription from the image alone.