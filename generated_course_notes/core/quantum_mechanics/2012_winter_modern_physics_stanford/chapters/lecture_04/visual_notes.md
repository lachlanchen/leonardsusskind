# Visual Evidence
## Frame Inventory
- `lecture_04_figure_02.png` shows the discrete-review board with \(\sum_n P(n)=1\) and \(\langle m|n\rangle=\delta_{nm}\) clearly written while Susskind begins a lower-board sketch, and this screenshot should remain in the final notes.
- `lecture_04_figure_03.png` shows the continuous-density sketch with a bell-shaped curve, an \(x\)-axis, and a marked short interval under the curve, and this screenshot should remain in the final notes.
- `lecture_04_figure_04.png` shows the momentum-operator line and the momentum eigenvalue differential equation for \(\psi(x)\), and this screenshot should remain in the final notes.
- `lecture_04_figure_05.png` shows the normalization integral \(\int \psi^*\psi\,dx\) being written term by term, and this screenshot should remain in the final notes.
- `lecture_04_figure_06.png` shows a split board layout with a partially visible normalized plane wave on the left and a bra-ket expression on the right, and this screenshot should remain in the final notes as layout evidence even though it is the weakest mathematically.

## Equation Extraction
- `lecture_04_figure_02.png`: \(\sum_n P(n)=1\) [visible]
- `lecture_04_figure_02.png`: \(\langle m|n\rangle=\delta_{nm}\) [visible]

- `lecture_04_figure_03.png`: \(P(x)\) or closely related probability-density notation on the vertical axis [partially visible]
- `lecture_04_figure_03.png`: \(x\) [visible]
- `lecture_04_figure_03.png`: \(x+\Delta x\) [partially visible]
- `lecture_04_figure_03.png`: \(\displaystyle \int_x^{x+\Delta x} P(x')\,dx'\) [standard completion]

- `lecture_04_figure_04.png`: \(-i\hbar\,\dfrac{\partial}{\partial x}\) [partially visible]
- `lecture_04_figure_04.png`: \(-i\hbar\,\dfrac{\partial}{\partial x}\,\psi(x)=p\,\psi(x)\) [visible]

- `lecture_04_figure_05.png`: \(\displaystyle \int \psi^*\psi\,dx\) [visible]
- `lecture_04_figure_05.png`: \(\displaystyle \int \psi^*(x)\psi(x)\,dx\) [standard completion]

- `lecture_04_figure_06.png`: \(e^{\frac{i}{\hbar}px}\) [partially visible]
- `lecture_04_figure_06.png`: \(\dfrac{e^{\frac{i}{\hbar}px}}{\sqrt{2\pi R}}\) [partially visible]
- `lecture_04_figure_06.png`: \(\langle q|p\rangle=\) or \(\langle x|p\rangle=\) [partially visible]
- `lecture_04_figure_06.png`: \(\langle x|p\rangle=\dfrac{e^{\frac{i}{\hbar}px}}{\sqrt{2\pi R}}\) [standard completion]

## Diagram Extraction
- `lecture_04_figure_02.png` is mostly equation evidence, but it also preserves the board structure of the discrete review: equations above, probability picture beginning below. Show it both as a screenshot and, if the chapter wants a clean picture, as a nearby TikZ redraw of discrete probability values at integer \(n\).
- `lecture_04_figure_03.png` is strong diagram evidence and should be shown both ways: keep the screenshot and also redraw the curve and highlighted interval in TikZ for a clean note-quality figure.
- `lecture_04_figure_04.png` is not a diagram; preserve it as a screenshot and pair it with a cleaned displayed equation rather than a redraw.
- `lecture_04_figure_05.png` is not a diagram; preserve it as a screenshot and pair it with a cleaned normalization integral.
- `lecture_04_figure_06.png` is best understood as board-layout evidence linking the explicit plane-wave expression to the abstract bra-ket form. Keep the screenshot, but do not attempt a literal graphical redraw; instead place clean equations nearby.

## Reconstruction Guidance
- Use `lecture_04_figure_02.png` to anchor the discrete review visually, but let the typeset equations carry the mathematics. If a discrete-probability sketch is included, redraw it cleanly in TikZ rather than trying to extract the unfinished chalk start from the frame.
- Use `lecture_04_figure_03.png` as the main visual witness for the continuous probability-density picture. The TikZ redraw should make the axis labels and interval \([x,x+\Delta x]\) explicit, while the screenshot remains nearby as the record of Susskind’s board geometry and emphasis.
- Use `lecture_04_figure_04.png` to justify the exact chalk form of the momentum eigenvalue equation. The note version should typeset the equation cleanly and, if needed, restore the operator line above it only to the extent supported by the transcript.
- Use `lecture_04_figure_05.png` as evidence for the structure of the integrand \(\psi^*\psi\) and the differential \(dx\), but not as evidence for any equality sign or final value that is not yet on the board. The note-quality version should restore the \(x\)-dependence and place the completed normalization statement in clean LaTeX.
- Use `lecture_04_figure_06.png` cautiously: it is valuable because it shows both sides of the board at once, but the mathematics should be reconstructed from the transcript and standard circle normalization rather than from the frame alone. The screenshot should sit beside a clean printed formula that makes the relation between the normalized plane wave and the bra-ket notation explicit.
- In all cases, prefer a clean displayed equation or TikZ redraw for readability, while retaining the screenshot when it is the best evidence for notation choice, board sequencing, or lecturer emphasis.

## Uncertainties
- In `lecture_04_figure_02.png`, the lower sketch is only being started, so the frame is much stronger for the two equations than for any actual probability-vs-\(n\) drawing.
- In `lecture_04_figure_03.png`, the vertical-axis label is not fully sharp; it looks like \(P(x)\), but the exact chalk lettering is not perfectly secure.
- In `lecture_04_figure_03.png`, the right-hand endpoint of the marked interval appears to be \(x+\Delta x\), but the \(\Delta\) is not fully crisp.
- In `lecture_04_figure_04.png`, the upper operator line is cropped on the left, so the frame does not by itself certify the full operator identity.
- In `lecture_04_figure_05.png`, the frame shows \(\int \psi^*\psi\,dx\) being written, but not the final equality; any “\(=1\)” must come from the transcript, not from the screenshot.
- In `lecture_04_figure_06.png`, the denominator on the left looks like a square-root normalization, plausibly \(\sqrt{2\pi R}\), but it is not fully legible.
- In `lecture_04_figure_06.png`, the bra-ket on the right could be read as \(\langle q|p\rangle\) or \(\langle x|p\rangle\); the frame alone does not settle the label with certainty.
- `lecture_04_figure_06.png` is partially blocked by Susskind, so it should be treated as supporting layout evidence rather than as a standalone source for exact transcription.
- The frames do not directly show the full interval-probability formula or the fully normalized plane-wave expression in completed chalk form, so those should be reconstructed cautiously from the transcript and standard notation rather than claimed as fully visible board text.