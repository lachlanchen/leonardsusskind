# Visual Evidence
## Frame Inventory
- `lecture_05_figure_02.png`: A transitional review frame showing Susskind beside the previously written scale-factor laws and a newly introduced \(\rho\)-symbol; it should remain only if the final notes want a brief visual marker for the pivot from \(a(t)\) to energy density.
- `lecture_05_figure_03.png`: A strong split-board frame showing reviewed cosmological scalings on the left and the equation-of-state plus thermodynamic box sketch on the right; it should remain in the final notes.
- `lecture_05_figure_04.png`: A close board frame centered on the separated differential relation and the start of the logarithmic integration step; it should remain in the final notes.

## Equation Extraction
- `lecture_05_figure_02.png`: \(a(t)\sim t^{2/3}\) [partially visible]
- `lecture_05_figure_02.png`: \(a(t)\sim t^{1/2}\) [visible]
- `lecture_05_figure_02.png`: \(\rho\) [visible]
- `lecture_05_figure_03.png`: \(a(t)\sim t^{2/3}\) [visible]
- `lecture_05_figure_03.png`: \(a(t)\sim t^{1/2}\) [partially visible]
- `lecture_05_figure_03.png`: \(\rho=\dfrac{\rho_0}{a^3}\) [partially visible]
- `lecture_05_figure_03.png`: \(\rho=\dfrac{\rho_0}{a^4}\) [partially visible]
- `lecture_05_figure_03.png`: \(P=W\rho\) [visible]
- `lecture_05_figure_03.png`: \(dE=-P\,dV\) [standard completion]
- `lecture_05_figure_04.png`: \(\dfrac{d\rho}{\rho}=-(1+w)\dfrac{dV}{V}\) [visible]
- `lecture_05_figure_04.png`: \(\log\rho=\) [visible]
- `lecture_05_figure_04.png`: \(d(\log\rho)=-(1+w)\,d(\log V)\) [standard completion]
- `lecture_05_figure_04.png`: \(\log\rho=-(1+w)\log V+\text{const.}\) [standard completion]

## Diagram Extraction
- `lecture_05_figure_02.png`: This is not a finished diagram; its value is the board staging, with the old scale-factor review above and the new \(\rho\) notation below, so it is useful only as a screenshot and does not need a TikZ redraw.
- `lecture_05_figure_03.png`: The right side contains a rectangular prism sketch with one face labeled \(A\) and a displacement marked \(dx\); this should be shown both ways, with the original screenshot preserved and a clean TikZ redraw nearby.
- `lecture_05_figure_03.png`: The board is divided into a left review column and a right derivation column by a vertical separator; that overall layout is worth preserving in the screenshot but does not itself need a separate redraw.
- `lecture_05_figure_04.png`: This is not a geometric figure but a derivation board state; it should be preserved as a screenshot and accompanied by clean displayed equations rather than redrawn as TikZ.

## Reconstruction Guidance
- Use `lecture_05_figure_03.png` as the main visual anchor for the section that moves from reviewed cosmological scalings to the thermodynamic derivation. Nearby, typeset a cleaned block such as \(\rho_{\text{matter}}=\rho_0/a^3\), \(\rho_{\text{rad}}=\rho_0/a^4\), and \(P=w\rho\), with the handwritten board \(W\) normalized to \(w\).
- Redraw the box in `lecture_05_figure_03.png` in TikZ as a simple prism with face area \(A\) and displacement \(dx\), so that \(dV=A\,dx\) and then \(dE=-P\,dV\) can be presented cleanly; keep the screenshot adjacent because the lecture’s visual logic depends on the board sketch.
- Use `lecture_05_figure_04.png` to justify the separation-of-variables step. The screenshot should sit next to the cleaned derivation \(\frac{d\rho}{\rho}=-(1+w)\frac{dV}{V}\), then the logarithmic step, then the integrated form.
- Treat `lecture_05_figure_02.png` as optional supporting evidence only. If it is kept, pair it with brief prose that says the lecture is pivoting from the known scale-factor laws to the energy-density variable \(\rho\), rather than asking it to carry a full equation.
- Keep the visible board evidence and the cleaned equations close together in the final notes. These frames are most useful when the reader can immediately compare the handwritten board state with the reconstructed mathematics.
- Prefer modest standard completions over ambitious restoration. The frames justify the structure of the derivation very well, but not every final symbol on the board is fully legible.

## Uncertainties
- In `lecture_05_figure_02.png`, the upper \(a(t)\sim t^{2/3}\) line is cropped and the new lower mark is only a \(\rho\)-like symbol, not a full displayed formula.
- In `lecture_05_figure_03.png`, the lower-left radiation-density formula is partly obscured, so \(\rho=\rho_0/a^4\) is best treated as a cautious reading rather than a perfectly clear transcription.
- In `lecture_05_figure_03.png`, the lower-right formula is cropped after \(dE=-P\cdots\), so the completion to \(dE=-P\,dV\) should be marked as standard completion rather than fully visible board text.
- In `lecture_05_figure_03.png`, the board uses uppercase \(W\), but the lecture and the cleaned notes should use lowercase \(w\).
- In `lecture_05_figure_04.png`, the full right-hand side of the logarithmic equation is not written out on the visible board, so \(\log\rho=-(1+w)\log V+\text{const.}\) is a reconstruction, not a literal full-board transcription.
- In `lecture_05_figure_04.png`, the board writes `log` by hand; whether the final notes keep \(\log\) or standardize to \(\ln\) should be an editorial choice, not a claim about what is explicitly visible.