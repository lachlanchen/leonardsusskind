# Figure Notes

## Image Inventory

- `lecture_04_figure_01.png`: opening title-sequence frame with a Stanford courtyard and oversized overlaid title letters; no blackboard, no lecturer mathematics, no usable lecture-room layout for notes.
- `lecture_04_figure_02.png`: close crop of Susskind writing on the board from behind; the visible line is a determinant-style expression beginning with vertical bars around a capital \(M\), followed by an equals sign and a near-identity form \(1+\epsilon(\cdots)\).
- `lecture_04_figure_03.png`: whiteboard derivation in three stacked lines, with Susskind pointing at the first factor of the top line; the board shows the near-identity unitary product and the Hermiticity condition for the generator \(T\).
- `lecture_04_figure_04.png`: single-line representation-theory equation high on the board behind the lecturer: the tensor product of two triplets decomposes into an anti-triplet and a sextet.
- `lecture_04_figure_05.png`: isolated board equation on an otherwise blank whiteboard: \(8\times 8=1+63\); this is clearly a state-counting line rather than the full irreducible decomposition.

## Blackboard Equations

- `lecture_04_figure_02.png`: \(\lvert M\rvert = 1 + \epsilon m\) [partially visible]
- `lecture_04_figure_02.png`: \(\det(1+\epsilon m)=1+\epsilon\,\operatorname{tr}m+O(\epsilon^2)\) [standard reconstruction]
- `lecture_04_figure_03.png`: \((1+i\epsilon T)(1-i\epsilon T^\dagger)=1\) [partially visible]
- `lecture_04_figure_03.png`: \(i\epsilon\,(T-T^\dagger)=0\) [visible]
- `lecture_04_figure_03.png`: \(T=T^\dagger\) [visible]
- `lecture_04_figure_03.png`: \(U=1+i\epsilon T\) [standard reconstruction]
- `lecture_04_figure_04.png`: \(3\otimes 3=\bar 3+6\) [visible]
- `lecture_04_figure_04.png`: \(3\otimes 3=\bar 3\oplus 6\) [standard reconstruction]
- `lecture_04_figure_05.png`: \(8\times 8=1+63\) [visible]
- `lecture_04_figure_05.png`: \(8\otimes 8=1\oplus 8\oplus 8\oplus 10\oplus \overline{10}\oplus 27\) [standard reconstruction]

## Diagram And Layout Reading

- `lecture_04_figure_01.png` contains no mathematical diagram at all; it is purely an opening visual.
- `lecture_04_figure_02.png` is a documentary close-up of the board at the moment the determinant expansion is being introduced. The framing is tight, and the lecturer’s body blocks the lower board, so this image preserves the immediate board gesture rather than a full derivation.
- `lecture_04_figure_03.png` has the clearest mathematical layout of the set: a top product line, a middle first-order condition, and a bottom simplified conclusion. The lecture’s logic is visibly vertical: start from unitarity, expand to first order, conclude Hermiticity.
- `lecture_04_figure_04.png` shows a single decomposition line with a large amount of empty whiteboard around it. There is no auxiliary sketch; the value of the frame is the isolated representation-theory statement itself.
- `lecture_04_figure_05.png` is similarly sparse: one centered counting equation with faint remnants of earlier writing at the top edge. It reads as a board checkpoint, not as a completed derivation.
- Across these selected images there are no axes, arrows, tensor diagrams, or geometric sketches; the visual content is entirely algebraic board writing.

## TeX Reconstruction Plan

- `lecture_04_figure_01.png` should not remain in the chapter. It is an intro/title image and adds nothing to the mathematical notes.
- `lecture_04_figure_02.png` should remain visible only if the chapter includes the near-identity determinant discussion. Pair it with a cleaned displayed equation for the first-order determinant expansion, and state briefly that the screenshot captures the board before the trace statement is fully completed.
- `lecture_04_figure_03.png` should remain visible. Reconstruct the mathematics nearby as a short displayed chain:
  \((1+i\epsilon T)(1-i\epsilon T^\dagger)=1\),
  \(i\epsilon(T-T^\dagger)=0\),
  \(T=T^\dagger\).
  No TikZ is needed.
- `lecture_04_figure_04.png` should remain visible. Pair it with a clean displayed decomposition \(3\otimes 3=\bar 3\oplus 6\), and explain in nearby prose that the antisymmetric part gives the \(\bar 3\) while the symmetric part gives the \(6\).
- `lecture_04_figure_05.png` should remain visible. Pair it first with the literal board counting equation \(8\otimes 8=1+63\). If the chapter also presents the later full decomposition, typeset that separately and make clear that it is a lecture completion beyond what this frame itself shows.
- All retained screenshots should be centered and used as documentary evidence beside cleaned equations, not as substitutes for the typeset mathematics.

## Caption Drafts

- `lecture_04_figure_01.png`: Opening Stanford title sequence.
- `lecture_04_figure_02.png`: Near-identity determinant expansion on the board.
- `lecture_04_figure_03.png`: First-order unitarity implies a Hermitian generator.
- `lecture_04_figure_04.png`: Two-quark triplet product decomposed into \(\bar 3\) and \(6\).
- `lecture_04_figure_05.png`: Two-gluon state count written as \(8\times 8=1+63\).

## Uncertainties

- In `lecture_04_figure_02.png`, the determinant notation is clear, but the final right-hand symbol is unfinished and does not visibly show the trace. The transcript strongly supports completing this as a first-order trace formula, but that completion is not literally present in the image.
- In `lecture_04_figure_03.png`, the top line is partly occluded and cropped at the right, so the dagger on the second factor is inferred from the lower lines and the lecture context rather than fully cleanly visible.
- In `lecture_04_figure_04.png`, the board uses a plain plus sign rather than an explicit direct-sum symbol; the notes may safely typeset \(\oplus\), but the screenshot itself shows \(+\).
- In `lecture_04_figure_05.png`, the board does not show the full irreducible decomposition of \(8\otimes 8\); it shows only the counting statement \(1+63\). The later decomposition should therefore be presented as a transcript-backed completion, not as a direct transcription of the screenshot.
- `lecture_04_figure_01.png` is visually real but mathematically irrelevant; it should be treated as excluded evidence rather than as a figure to preserve.