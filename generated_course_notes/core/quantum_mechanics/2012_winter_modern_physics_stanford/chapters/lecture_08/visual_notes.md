# Visual Evidence
## Frame Inventory
- `lecture_08_figure_02.png` shows the classical Hamiltonian example beside a small phase-space flow sketch with curved arrows and an `x` label; it should remain in the final notes as both equation evidence and board-layout evidence.
- `lecture_08_figure_03.png` shows the polarization Hamiltonian eigenvalue equations, left-side state/energy labels, and a partially blocked `|\psi(t)\rangle` column-vector expression; it should remain in the final notes because the layout helps document the transition from eigenstates to time evolution.
- `lecture_08_figure_04.png` shows a clean isolated ket time-evolution equation on an otherwise blank board; it should remain in the final notes as a direct visual witness of the board-level Schrödinger equation.
- `lecture_08_figure_05.png` shows an intermediate bra-ket derivation with a visible time derivative marker and one visible product-rule term; it should remain in the final notes as supporting evidence for the derivation, even though the full equation is not fully readable.

## Equation Extraction
- `lecture_08_figure_02.png`: `\frac{p^2}{2m}+U(x)` [visible]
- `lecture_08_figure_02.png`: `H(x,p)` or `H(x\,p)` [partially visible]
- `lecture_08_figure_02.png`: `x` [visible]
- `lecture_08_figure_02.png`: `H(x,p)=\frac{p^2}{2m}+U(x)` [standard completion]

- `lecture_08_figure_03.png`: `|y\rangle` [visible]
- `lecture_08_figure_03.png`: `E_2` [visible]
- `lecture_08_figure_03.png`: `|x\rangle` [visible]
- `lecture_08_figure_03.png`: `E_1` [visible]
- `lecture_08_figure_03.png`: `H|x\rangle = E_1|x\rangle` [partially visible]
- `lecture_08_figure_03.png`: `H|y\rangle = E_2|y\rangle` [partially visible]
- `lecture_08_figure_03.png`: `|\psi(t)\rangle =` [partially visible]
- `lecture_08_figure_03.png`: `\alpha(t)` [partially visible]
- `lecture_08_figure_03.png`: `\beta(t)` [partially visible]
- `lecture_08_figure_03.png`: `|\psi(t)\rangle=\begin{pmatrix}\alpha(t)\\ \beta(t)\end{pmatrix}` [standard completion]

- `lecture_08_figure_04.png`: `|\dot{\psi}\rangle=-iH|\psi\rangle` [visible]

- `lecture_08_figure_05.png`: `\langle\psi|K|\dot{\psi}\rangle` [visible]
- `lecture_08_figure_05.png`: `\frac{d}{dt}` [visible]
- `lecture_08_figure_05.png`: continuation to the right of the equals sign, consistent with a second term from differentiating the bra [partially visible]
- `lecture_08_figure_05.png`: `\frac{d}{dt}\langle\psi|K|\psi\rangle=\langle\psi|K|\dot{\psi}\rangle+\langle\dot{\psi}|K|\psi\rangle` [standard completion]

## Diagram Extraction
- `lecture_08_figure_02.png` contains the only real sketch among the four frames: several curved flow lines with arrowheads, apparently part of a phase-space picture, plus a short horizontal axis labeled `x`. This should be shown both ways: keep the screenshot and add a conservative TikZ redraw nearby.
- `lecture_08_figure_03.png` is mainly a board-organization figure rather than a standalone diagram. Keep it as a screenshot, but do not redraw the board layout in TikZ; clean equations beside it are enough.
- `lecture_08_figure_04.png` is not a diagram and needs no TikZ. Keep it purely as a screenshot-plus-equation pairing.
- `lecture_08_figure_05.png` is also not a redraw candidate. Its value is the visible structure of the derivation, so keep the screenshot and reconstruct the algebra in typeset equations rather than as a TikZ figure.

## Reconstruction Guidance
- For `lecture_08_figure_02.png`, print the cleaned Hamiltonian `H(x,p)=\frac{p^2}{2m}+U(x)` as a displayed equation and place the screenshot next to a schematic TikZ flow sketch. The redraw should stay minimal: curved arrows, one visible `x` axis, and no invented second axis label.
- For `lecture_08_figure_03.png`, typeset the two eigenvalue equations and the two-component state vector separately in clean LaTeX. Keep the screenshot close by, because the board arrangement itself shows how Susskind moved from basis eigenstates to the explicit time-dependent polarization state.
- For `lecture_08_figure_04.png`, use the screenshot as direct evidence for the board form `|\dot{\psi}\rangle=-iH|\psi\rangle`. If the final notes restore `\hbar`, that restored version should be presented as a cleaned note-level form, not as a literal transcription of what is written in the frame.
- For `lecture_08_figure_05.png`, do not try to recover the full derivation from the image alone. Use the transcript to typeset the product-rule step and the later commutator statement, while keeping the screenshot nearby as evidence that this was indeed the intermediate board stage.
- Across all four figures, prefer “screenshot plus cleaned equation” over replacing the screenshot entirely. These frames are valuable not only for formulas but for the lecturer’s board rhythm and placement.

## Uncertainties
- In `lecture_08_figure_02.png`, the exact punctuation in `H(x,p)` is not fully secure, and an equality sign to the explicit formula is not visible in the crop.
- In `lecture_08_figure_02.png`, the sketch strongly suggests phase-space flow lines, but only the `x` label is clearly legible; any missing axis or label should not be invented.
- In `lecture_08_figure_03.png`, the lower `|\psi(t)\rangle` expression is partly covered by Susskind’s paper, so the full column-vector form should be treated as a cautious completion rather than a pure transcription.
- In `lecture_08_figure_03.png`, the left-side state/energy pairing is visually cramped; the transcript is needed to confirm that `|x\rangle` pairs with `E_1` and `|y\rangle` with `E_2`.
- In `lecture_08_figure_04.png`, the Hamiltonian is clearly written as `H`, but any hat notation is not visible.
- In `lecture_08_figure_05.png`, the symbol on the operator `K` may or may not carry a hat in the handwriting; the right-hand side of the line is also substantially blocked by Susskind’s body.
- In `lecture_08_figure_05.png`, the visible `\frac{d}{dt}` likely belongs to a larger cropped expression, so the full product-rule equation should come from transcript-backed reconstruction, not from the frame alone.