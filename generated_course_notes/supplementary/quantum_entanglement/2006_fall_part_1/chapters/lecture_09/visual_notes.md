# Visual Evidence
## Frame Inventory
- `lecture_09_figure_03.png`: A clean crop of an otherwise blank board showing the difference-quotient definition of the time derivative of the state vector; this screenshot should remain in the final notes as direct evidence for the transition from infinitesimal evolution to the Schrödinger equation.
- `lecture_09_figure_04.png`: Susskind stands beneath a clearly legible board equation \(H|\psi\rangle = E|\psi\rangle\); this screenshot should remain in the final notes as evidence for the stationary-state premise.
- `lecture_09_figure_05.png`: A wider classroom frame shows a split-board layout with the energy-frequency relation on the left and remnants of the scalar phase-evolution derivation on the right; this screenshot should remain in the final notes because it captures the lecture’s visual linkage between \(E=\hbar\omega\) and the exponential time factor.
- `lecture_09_figure_06.png`: Susskind stands aside from a nearly blank board carrying a single expansion in Hamiltonian eigenvectors near the top; this screenshot should remain in the final notes as evidence for the move to general superpositions.

## Equation Extraction
- `lecture_09_figure_03.png`: \(\dfrac{d}{dt}|\psi\rangle = \dfrac{|\psi(\epsilon)\rangle - |\psi(0)\rangle}{\epsilon}\) [visible]
- `lecture_09_figure_03.png`: \(\dfrac{d}{dt}|\psi(t)\rangle = \dfrac{|\psi(t+\epsilon)\rangle - |\psi(t)\rangle}{\epsilon}\) [standard completion]

- `lecture_09_figure_04.png`: \(H|\psi\rangle = E|\psi\rangle\) [visible]

- `lecture_09_figure_05.png`: \(E=\hbar\omega\) [partially visible]
- `lecture_09_figure_05.png`: \(\dfrac{E}{\hbar}=\omega\) [partially visible]
- `lecture_09_figure_05.png`: \(\dot f = -\dfrac{iE}{\hbar}f(t)\) [partially visible]
- `lecture_09_figure_05.png`: \(e^{-iEt/\hbar}\) [partially visible]
- `lecture_09_figure_05.png`: \(|\psi_E(t)\rangle = e^{-iEt/\hbar}|\psi_E(0)\rangle\) [standard completion]

- `lecture_09_figure_06.png`: \(\sum_n \alpha_n |\psi_n\rangle\) [visible]
- `lecture_09_figure_06.png`: \(|\psi\rangle = \sum_n \alpha_n |\psi_n\rangle\) [standard completion]

## Diagram Extraction
- `lecture_09_figure_03.png` does not contain a geometric diagram; its value is the board structure itself, namely one isolated equation on a blank field. Preserve it as a screenshot, not as TikZ.
- `lecture_09_figure_04.png` is likewise not a geometric sketch; the important visual fact is that the eigenvalue equation is written as a single standalone line above the lecturer. Preserve it as a screenshot, not as TikZ.
- `lecture_09_figure_05.png` contains no redraw-worthy diagram, but it does preserve a meaningful split-board layout: the left board states the energy-frequency relation while the right board still carries the preceding derivation. Preserve it as a screenshot; do not redraw this board state in TikZ.
- `lecture_09_figure_06.png` again has no geometric figure, but it shows a sparse board reset with one top-line expansion. Preserve it as a screenshot, not as TikZ.
- From the current frame set, no figure should be shown both as screenshot and TikZ, because none of the retained frames contains a genuine board sketch or axis diagram; they are equation witnesses rather than diagram witnesses.

## Reconstruction Guidance
- For `lecture_09_figure_03.png`, keep the screenshot beside a clean typeset equation for the derivative step, but regularize the notation in the text or display so that the time labels are consistent with the surrounding derivation.
- For `lecture_09_figure_04.png`, use the screenshot to anchor the section on energy eigenvectors, then typeset \(H|\psi\rangle=E|\psi\rangle\) cleanly and continue with the scalar-factor ansatz in LaTeX rather than trying to infer later steps from the frame alone.
- For `lecture_09_figure_05.png`, treat the screenshot as evidence of the lecture’s board choreography rather than as a complete literal source. The final notes should typeset the cleaned chain \(\dot f = -(iE/\hbar)f\), \(f(t)=e^{-iEt/\hbar}\), and \(E=\hbar\omega\), while keeping the screenshot nearby to show that the lecture itself visually tied those facts together.
- For `lecture_09_figure_06.png`, keep the screenshot near the abstract discussion of general states in the Hamiltonian eigenbasis, but typeset the expansion with an explicit left-hand side and then follow it with the time-evolved sum in clean notation.
- Across all four frames, use the images to preserve sequencing, board emphasis, and notation style, while letting the transcript control the final mathematical wording and the completed equations.
- Avoid inventing intermediate lines that are not visible and not securely supported by the transcript; when a step is only partially visible, jump directly to the standard clean form that the lecture is clearly aiming at.

## Uncertainties
- `lecture_09_figure_03.png`: The visible left-hand side appears as \(\frac{d}{dt}|\psi\rangle\) without an explicit time argument, so any conversion to \(|\psi(t)\rangle\) is a regularization rather than a literal transcription.
- `lecture_09_figure_03.png`: The numerator uses \(|\psi(\epsilon)\rangle\) and \(|\psi(0)\rangle\) visibly, but the more standard \(|\psi(t+\epsilon)\rangle-|\psi(t)\rangle\) form is not in the frame and should only appear as a cautious completion.
- `lecture_09_figure_05.png`: The left-board formulas are small and slightly soft, so \(\hbar\), \(\omega\), and the lower rearranged line should be treated as partly visible and transcript-confirmed rather than frame-certain.
- `lecture_09_figure_05.png`: The right-board derivation is partly blocked by Susskind and partly cropped, so the exact placement of \(f(t)\), dots, and phase factors is not fully recoverable from the image alone.
- `lecture_09_figure_06.png`: The coefficient is best read as \(\alpha_n\), but the handwriting is small enough that the index and coefficient family should be treated with modest caution.
- None of these four frames supports a literal full-board reconstruction of the entire derivation; they support specific local equations and board emphases, and the rest should be completed only where the transcript makes the intended mathematics unambiguous.