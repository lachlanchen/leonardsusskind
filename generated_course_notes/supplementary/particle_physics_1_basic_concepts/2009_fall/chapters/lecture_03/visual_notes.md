# Visual Evidence
## Frame Inventory
- `lecture_03_figure_01.png`: Stanford University title card over a campus courtyard; it should not remain in the final notes.
- `lecture_03_figure_02.png`: Susskind writes occupation-number notation, with a boxed `n(k)` on the left and a later indexed entry on the right; it may remain as a documentary screenshot for the occupation-number section.
- `lecture_03_figure_03.png`: Tight board crop showing the paired mode operators `a^{+}(k)` and `a^{-}(k)`, with the lower line partly blocked by hand and eraser; it may remain as notation evidence.
- `lecture_03_figure_04.png`: Talking-head shot with only residual board fragments behind Susskind; it should not remain in the final notes.
- `lecture_03_figure_05.png`: Strong derivation frame showing `\Psi^\dagger(x)|0\rangle` and its rewrite as a momentum-state superposition; it should remain in the final notes.
- `lecture_03_figure_06.png`: Two-board frame showing field expansions on the left and the later \(\ell,m\) probability discussion on the right; it should remain in the final notes.

## Equation Extraction
- `lecture_03_figure_02.png`: `n(k)` `[visible]`
- `lecture_03_figure_02.png`: `n(2)` `[visible]`
- `lecture_03_figure_02.png`: `n(1),\,n(2),\,n(3),\,\dots` `[standard completion]`
- `lecture_03_figure_03.png`: `a^{+}(k)` `[visible]`
- `lecture_03_figure_03.png`: `a^{-}(k)` `[partially visible]`
- `lecture_03_figure_04.png`: `e^{ikx}` or `e^{-ikx}` fragments `[partially visible]`
- `lecture_03_figure_04.png`: `\dfrac{2\pi}{\lambda}` `[visible]`
- `lecture_03_figure_04.png`: `k=\dfrac{2\pi}{\lambda}` `[standard completion]`
- `lecture_03_figure_05.png`: `\Psi^{\dagger}(x)\,|0\rangle` `[visible]`
- `lecture_03_figure_05.png`: `\sum e^{-ikx} a^{\dagger}(k)\,|0\rangle` `[partially visible]`
- `lecture_03_figure_05.png`: `\sum_k e^{-ikx} a^{\dagger}(k)\,|0\rangle` `[standard completion]`
- `lecture_03_figure_05.png`: `\sum_k e^{-ikx}\,|k\rangle` `[partially visible]`
- `lecture_03_figure_05.png`: `a^{\dagger}(k)\,|0\rangle = |k\rangle` `[standard completion]`
- `lecture_03_figure_06.png`: `\Psi(x)=\sum_k a(k)e^{ikx}` `[partially visible]`
- `lecture_03_figure_06.png`: `\Psi^{\dagger}(x)=\sum_{\ell} a^{\dagger}(\ell)e^{-i\ell x}` `[standard completion]`
- `lecture_03_figure_06.png`: `\sum_{\ell m}` `[visible]`
- `lecture_03_figure_06.png`: `e^{ikx}` `[visible]`
- `lecture_03_figure_06.png`: `e^{-i\ell x}` `[partially visible]`
- `lecture_03_figure_06.png`: `e^{-imx}` `[partially visible]`
- `lecture_03_figure_06.png`: `\sum_{\ell m} e^{i(k_{\mathrm{initial}}-\ell-m)x}\,|\ell,m\rangle` `[standard completion]`
- `lecture_03_figure_06.png`: `\sqrt{2}` `[partially visible]`

## Diagram Extraction
- `lecture_03_figure_01.png` contains no mathematical diagram and should not be used.
- `lecture_03_figure_02.png` is not really a diagram, but it does preserve the left-right board layout of the occupation-number notation; keep it as a screenshot rather than redrawing it.
- `lecture_03_figure_03.png` is also notation rather than a diagram; keep it as a screenshot if the notes want visual evidence for the operator labels, but do not redraw it in TikZ.
- `lecture_03_figure_04.png` does not preserve a usable diagram or finished equation; omit it.
- `lecture_03_figure_05.png` preserves an important three-line derivational layout, including the brace that translates operator language into state-vector language; keep it as a screenshot and typeset the cleaned derivation beside it rather than redrawing the board structure.
- `lecture_03_figure_06.png` preserves the most useful board architecture of the later discussion: definitions on the left board and the \(\ell,m\) amplitude/probability algebra on the right; keep it as a screenshot and, if a local interaction picture is desired, add only a small TikZ reaction cartoon nearby rather than a full board redraw.

## Reconstruction Guidance
- Use `lecture_03_figure_02.png` to justify introducing the state by occupation numbers, but write the final notation cleanly in LaTeX as a mode-indexed occupation-number list rather than trying to preserve the exact board handwriting.
- Use `lecture_03_figure_03.png` only as a witness for the labels \(a^{+}(k)\) and \(a^{-}(k)\). The actual operator action, including the square-root factors, should be reconstructed from the transcript and written as clean displayed equations.
- Ignore `lecture_03_figure_04.png` when reconstructing the mathematics. Its visible symbols are leftovers, not reliable evidence for the nearby subtitle moment.
- For `lecture_03_figure_05.png`, keep the screenshot and typeset the cleaned chain
  \[
  \Psi^{\dagger}(x)|0\rangle
  = \sum_k e^{-ikx} a^{\dagger}(k)|0\rangle
  = \sum_k e^{-ikx}|k\rangle,
  \]
  because that is exactly the conceptual step the board is documenting.
- For `lecture_03_figure_06.png`, keep the screenshot and reconstruct two separate displayed pieces nearby: first the field expansions \(\Psi(x)\) and \(\Psi^\dagger(x)\), then the local-reaction sum with distinct dummy indices \(\ell\) and \(m\). The screenshot matters here mainly for board layout and for showing that the probability discussion is the continuation of the field-expansion discussion.
- If the final chapter includes a TikZ figure, it should be a minimal schematic of a local process at a point \(x\): one incoming particle absorbed and two emitted from the same point. That schematic should appear next to `lecture_03_figure_06.png`, not as a substitute for it.
- Prefer standard completion only where the board is clearly pointing to a familiar formula already stabilized by the transcript. Do not promote weakly legible chalk marks into precise new formulas unless the transcript fixes them.

## Uncertainties
- In `lecture_03_figure_02.png`, only `n(k)` and one later indexed term such as `n(2)` are clearly readable; the fuller sequence is a cautious completion, not direct transcription.
- In `lecture_03_figure_02.png`, the large joke text at the top of the board is unrelated to the mathematics and should be ignored.
- In `lecture_03_figure_03.png`, the lower `a^{-}(k)` is partly hidden, so the sign and full letter shape are not as secure as the upper `a^{+}(k)`.
- In `lecture_03_figure_04.png`, the visible `2\pi/\lambda` relation may be readable, but it is not reliable evidence for the subtitle-linked argument about state vectors.
- In `lecture_03_figure_05.png`, the summation index is not equally clear in every place. The cleaned \(\sum_k\) form is transcript-supported rather than purely frame-derived.
- In `lecture_03_figure_05.png`, the brace strongly suggests the identification \(a^{\dagger}(k)|0\rangle = |k\rangle\), but that equality is not separately written as a complete standalone board equation.
- In `lecture_03_figure_06.png`, the signs of the exponential factors are not fully secure from the pixels alone; the transcript is needed to settle the final sign convention.
- In `lecture_03_figure_06.png`, the lower left-board \(\Psi^\dagger\) line is partly cropped or blocked, so its full expansion is a cautious reconstruction.
- In the late \(\ell=m\) discussion, the visible `\sqrt{2}` supports Bose enhancement, but the full combinatoric comparison between equal- and different-momentum channels is not legible from the frame and must be taken from the transcript with care.