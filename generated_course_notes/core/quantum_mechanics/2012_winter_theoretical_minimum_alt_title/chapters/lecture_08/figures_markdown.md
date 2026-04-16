# Figure Notes
## Image Inventory
- `lecture_08_figure_02.png`: close board crop from the unitary-evolution proof. The upper line shows a manipulated composite wavefunction `\Psi(ab)` or `\Psi_M(ab)` set equal to a sum over `b'`, with a matrix element `U_{bb'}` multiplying `\Psi(a b')`. The lower line shows the bra-side relation with `\Psi^*(a' b'')` and a daggered matrix element on the right. Susskind stands at the left edge and partly blocks the lower-left start of the second line.
- `lecture_08_figure_03.png`: a later frame of the same board region. The upper left now more clearly shows `\Psi_M(ab)`, and the same two transformation lines remain visible. Susskind is centered low in the frame, so the lower-left side is still obscured, but the right half of both equations is readable.
- `lecture_08_figure_05.png`: centered abstract inner product `\langle\psi|\phi\rangle` written above an expanded double-sum expression. The lower line visibly contains `\sum_{q',q}\psi^*(q')`, then a bra basis factor `\langle q'|`, then a ket-side factor involving `\phi(q)|q\rangle`. Susskind is pointing toward the lower line. A cropped normalization integral from the previous board survives along the top edge.

## Blackboard Equations
- `lecture_08_figure_02.png` and `lecture_08_figure_03.png`: [partially visible] `\Psi_M(ab)=\sum_{b'} U_{bb'}\,\Psi(ab')`
- `lecture_08_figure_02.png` and `lecture_08_figure_03.png`: [partially visible] `\Psi_M^*(a'b)=\sum_{b''}\Psi^*(a'b'')\,U^\dagger_{b''b}`
- `lecture_08_figure_02.png` and `lecture_08_figure_03.png`: [standard reconstruction] `\Psi_M(a,b)=\sum_{b'} U_{bb'}\,\Psi(a,b')`
- `lecture_08_figure_05.png`: [visible] `\langle \psi|\phi\rangle`
- `lecture_08_figure_05.png`: [partially visible] `\langle \psi|\phi\rangle=\sum_{q',q}\psi^*(q')\,\langle q'|\,\phi(q)\,|q\rangle`
- `lecture_08_figure_05.png`: [partially visible] `\int \phi^*(x)\phi(x)\,dx=1`
- `lecture_08_figure_05.png`: [standard reconstruction] after inserting the basis inner product, the board is heading toward the usual reduced form `\langle\psi|\phi\rangle=\sum_q \psi^*(q)\phi(q)`

## Diagram And Layout Reading
- There are no true diagrams, axes, or sketches in these three figures. Their value is the blackboard layout.
- Figures 02 and 03 are organized as a stacked pair: ket-side unitary action on top, bra-side Hermitian-conjugate action below. That vertical arrangement should be preserved in the notes because it matches the spoken point that bras transform with the daggered operator.
- In figures 02 and 03, the upper line is the cleaner documentary line, while the lower line is more important conceptually because the dagger sits prominently at the far right. The screenshots are therefore useful both as board evidence and as a record of how Susskind visually paired the two statements.
- Figure 05 uses a header-and-expansion layout. The abstract inner product sits centered at the top, and the lower line unpacks it into coefficients and basis bras/kets. This is exactly the visual form needed for the sentence that `\psi^*` supplies the coefficients of the bra vector.
- The cropped top strip of figure 05 matters only as context: it shows that the board is carrying over from the continuous-basis discussion, but it is not the main figure content.

## TeX Reconstruction Plan
- `lecture_08_figure_02.png` should remain visible as the primary screenshot for the composite-system unitary-action argument. Place a cleaned two-line displayed equation beside or just after it.
- `lecture_08_figure_03.png` is mathematically near-duplicate, but it is still useful if the chapter preserves the nearby Question & Answer rhythm around the student’s confusion about evolution and unitarity. If space is tight, keep it smaller and reuse the same displayed equations rather than typesetting the pair twice.
- `lecture_08_figure_05.png` should remain visible because the board arrangement itself helps explain the bra-coefficient point. Pair it with a cleaned displayed version of the inner-product expansion.
- No TikZ reconstruction is needed for any of these three figures.
- In the typeset equations, it is reasonable to standardize the board’s compressed argument style `\Psi(ab)` to `\Psi(a,b)` for readability, while keeping the screenshot itself unchanged.
- In figure 05, restore any missing Dirac bar and standard spacing in the typeset reconstruction; do not reproduce the board omission literally.

## Caption Drafts
- `lecture_08_figure_02.png`: Unitary action on the composite ket and the corresponding bra transformation
- `lecture_08_figure_03.png`: The same ket-bra transformation formulas during the locality discussion
- `lecture_08_figure_05.png`: Inner-product expansion with `\psi^*` as the coefficients of the bra vector

## Uncertainties
- In figures 02 and 03, the matrix letter can look like `L` in the screenshot, but the transcript and context strongly indicate the intended symbol is the unitary matrix `U`.
- In figure 02, the subscript `M` on the upper `\Psi` is weak or partly obscured; figure 03 makes the manipulated-state notation clearer.
- In figures 02 and 03, the lecturer blocks part of the lower-left expression, so the exact left-hand notation of the bra-side equation should be typeset cautiously rather than overclaimed from the screenshot alone.
- In figure 05, the visible indices look like `q,q'`, while the surrounding lecture often uses generic indices such as `a,a'`. For the figure brief, `q,q'` is the faithful reading of the board.
- In figure 05, one Dirac vertical bar appears faint or missing in the lower expansion line. The notes should restore the standard bra-ket syntax in LaTeX.
- The cropped top formula in figure 05 looks like a normalization condition from the previous continuous-variable discussion, but it is incomplete and should not be treated as a principal transcribed equation.