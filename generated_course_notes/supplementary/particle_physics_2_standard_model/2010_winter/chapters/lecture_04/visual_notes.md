# Visual Evidence

## Frame Inventory

- `lecture_04_figure_01.png`: Opening Stanford title/campus frame with no board mathematics; it should not remain in the final notes.
- `lecture_04_figure_02.png`: Tight close-up of Susskind writing a determinant-near-identity line on the board; keep it only if the nearby notes include the infinitesimal determinant argument.
- `lecture_04_figure_03.png`: Three-line board derivation showing the infinitesimal unitarity condition and the conclusion that the generator is Hermitian; this should remain in the final notes.
- `lecture_04_figure_04.png`: Single-line SU(3) representation-product statement for two quarks, `3\otimes 3`; this should remain in the final notes.
- `lecture_04_figure_05.png`: Isolated board checkpoint `8\times 8 = 1 + 63`, clearly a state-counting line for two gluons; this should remain in the final notes.

## Equation Extraction

- `lecture_04_figure_02.png`: `\lvert M\rvert = 1 + \epsilon m` [partially visible]
- `lecture_04_figure_02.png`: `\det(1+\epsilon m)=1+\epsilon\,\operatorname{tr}m+O(\epsilon^2)` [standard completion]
- `lecture_04_figure_03.png`: `(1+i\epsilon T)(1-i\epsilon T^\dagger)=1` [partially visible]
- `lecture_04_figure_03.png`: `i\epsilon\,(T-T^\dagger)=0` [visible]
- `lecture_04_figure_03.png`: `T=T^\dagger` [visible]
- `lecture_04_figure_03.png`: `U=1+i\epsilon T` [standard completion]
- `lecture_04_figure_04.png`: `3\otimes 3=\bar 3+6` [visible]
- `lecture_04_figure_04.png`: `3\otimes 3=\bar 3\oplus 6` [standard completion]
- `lecture_04_figure_05.png`: `8\times 8=1+63` [visible]
- `lecture_04_figure_05.png`: `8\otimes 8=1\oplus 8\oplus 8\oplus 10\oplus \overline{10}\oplus 27` [standard completion]

## Diagram Extraction

- `lecture_04_figure_01.png` contains no usable mathematical diagram.
- `lecture_04_figure_02.png` is not a diagram but a documentary board close-up; preserve as a screenshot if the determinant expansion is discussed, and do not redraw it in TikZ.
- `lecture_04_figure_03.png` preserves a useful board layout: top line for unitarity, middle line for first-order expansion, bottom line for the Hermiticity conclusion; keep the screenshot and typeset the cleaned derivation beside it.
- `lecture_04_figure_04.png` is a single algebraic checkpoint, not a drawable sketch; keep as a screenshot and pair with a clean displayed equation.
- `lecture_04_figure_05.png` is also a board checkpoint rather than a sketch; keep as a screenshot and pair with cleaned state-counting prose or equations.
- None of these frames requires a TikZ redraw; the visual evidence here is algebraic, not geometric.

## Reconstruction Guidance

- Treat `lecture_04_figure_02.png` as evidence for the lecture’s move to a matrix close to the identity, but typeset the actual note-quality statement as the standard first-order determinant expansion. Keep the screenshot nearby only as documentary support.
- For `lecture_04_figure_03.png`, reconstruct the board as a short displayed chain: start from infinitesimal unitarity, drop \(O(\epsilon^2)\), and conclude \(T=T^\dagger\). Use standard notation `\dagger` even if the board mark looks more like a superscript plus.
- For `lecture_04_figure_04.png`, typeset the clean decomposition with `\oplus`, then explain in prose that the antisymmetric two-quark piece gives the \(\bar 3\) and the symmetric piece gives the \(6\). Keep the screenshot as the literal board evidence.
- For `lecture_04_figure_05.png`, keep the literal board statement \(8\times 8=1+63\) as a counting remark. If the notes also include the full irreducible decomposition of \(8\otimes 8\), present it explicitly as a cleaned completion from lecture context, not as a direct transcription of the screenshot.
- Do not manufacture flux-tube or confinement drawings from this image set. Those later physical pictures belong to the transcript, not to the present frames.

## Uncertainties

- In `lecture_04_figure_02.png`, the right-hand side is unfinished on screen; the trace term is not literally visible even though the transcript strongly supports it.
- In `lecture_04_figure_03.png`, the top line is partly blocked and cropped, so the adjoint on the second factor is inferred from context and the lower lines.
- In `lecture_04_figure_03.png`, the board notation for the adjoint may be a superscript `+` rather than a clearly written dagger.
- In `lecture_04_figure_04.png`, the board shows a plain `+`, not an explicit direct-sum symbol.
- In `lecture_04_figure_05.png`, `1+63` is a state count, not the full SU(3) irrep decomposition; the full `8\otimes 8` split is not visible in the frame.
- `lecture_04_figure_01.png` is visually real but mathematically irrelevant and should be excluded rather than preserved.