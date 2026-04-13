# Visual Evidence
## Frame Inventory
- `lecture_04_figure_02.png`: Partial early board showing an operator acting on a ket with visible `\psi` and a second line suggestive of the unitarity condition; the screenshot should remain in the final notes as evidential context because the board is partly occluded.
- `lecture_04_figure_03.png`: Sparse board with a short operator-on-ket expression, most naturally read as a symmetry operator acting on an energy eigenstate; the screenshot should remain because it fixes the local notation and lecture pacing.
- `lecture_04_figure_04.png`: Clean centered shot of the Hamiltonian eigenvalue equation \(H|E\rangle=E|E\rangle\); the screenshot should remain because it is legible and mathematically central.
- `lecture_04_figure_05.png`: Three-line derivation from the energy eigenvalue equation to a commutator acting on \(|E\rangle\), with curved guide marks connecting the steps; the screenshot must remain because both the equations and the board layout matter.
- `lecture_04_figure_06.png`: Final stacked commutator statements showing that symmetry operators and generators commute with the Hamiltonian; the screenshot should remain because it records the lecture’s condensed conclusion.

## Equation Extraction
- `lecture_04_figure_02.png`: \(U|\psi\rangle\) [partially visible]
- `lecture_04_figure_02.png`: \(U^\dagger U = 1\) [standard completion]
- `lecture_04_figure_03.png`: \(U|E\rangle\) [visible]
- `lecture_04_figure_04.png`: \(H|E\rangle = E|E\rangle\) [visible]
- `lecture_04_figure_05.png`: \(H|E\rangle = E|E\rangle\) [visible]
- `lecture_04_figure_05.png`: \(H\,U|E\rangle = U\,E|E\rangle\) [visible]
- `lecture_04_figure_05.png`: \(U\,H|E\rangle\) [visible]
- `lecture_04_figure_05.png`: \((HU-UH)|E\rangle = 0\) [visible]
- `lecture_04_figure_06.png`: \([U,H]=0\) [visible]
- `lecture_04_figure_06.png`: \([L,H]=0\) [partially visible]
- `lecture_04_figure_06.png`: \([L_i,H]=0\) [standard completion]

## Diagram Extraction
- `lecture_04_figure_02.png`: This is not really a standalone diagram; it should be preserved as a screenshot rather than redrawn, since its value is the lecture-board transition from transformed state notation to unitarity.
- `lecture_04_figure_03.png`: No diagram is present; preserve as screenshot and pair with a clean displayed equation only.
- `lecture_04_figure_04.png`: No diagram is present; preserve as screenshot and pair with a clean displayed equation only.
- `lecture_04_figure_05.png`: This should be shown both ways: keep the screenshot and also redraw the three-line derivation in clean aligned LaTeX, with a very light TikZ companion or overlay reproducing the two curved guide marks above the middle step.
- `lecture_04_figure_06.png`: No geometric diagram is present; preserve as screenshot and place clean commutator equations nearby rather than making a separate TikZ figure.

## Reconstruction Guidance
- Use the frames to anchor notation and board sequencing, but let the transcript determine the logical order and the intended mathematical statement.
- For `lecture_04_figure_02.png`, reconstruct only the secure point that symmetry acts on a ket and that unitarity is being imposed; do not try to recover more from the obscured lower line than \(U^\dagger U=1\).
- For `lecture_04_figure_03.png` and `lecture_04_figure_04.png`, the cleanest note-quality treatment is screenshot plus nearby displayed equation, since the board content is short and stable.
- For `lecture_04_figure_05.png`, typeset the derivation as aligned equations, but keep the screenshot immediately adjacent because the board’s staged layout and the curved guide marks are part of the pedagogical evidence.
- For `lecture_04_figure_06.png`, standardize the conclusion as \([U,H]=0\) and then cautiously pass to \([L_i,H]=0\), while noting in prose that the lower generator label is visually less secure than the upper line.
- When a visible expression is mathematically obvious but incomplete, prefer a cautious standard completion over a speculative transcription; the notes should read cleanly, but the screenshot should remain nearby whenever the completion goes beyond what is fully legible.

## Uncertainties
- `lecture_04_figure_02.png`: The full upper-line ket is not entirely visible, even though `\psi` is clear.
- `lecture_04_figure_02.png`: The lower line strongly suggests \(U^\dagger U=1\), but the final symbol could visually be read as `1` or `I`.
- `lecture_04_figure_03.png`: The visible expression is very likely \(U|E\rangle\), but the crop is tight enough that it may once have been part of a longer nearby statement.
- `lecture_04_figure_05.png`: The middle line is legible as \(H\,U|E\rangle = U\,E|E\rangle\), but the separate right-hand \(U\,H|E\rangle\) should not be silently erased when rewriting the derivation.
- `lecture_04_figure_05.png`: The curved guide marks are explanatory arcs, not precise arrowed maps; any TikZ version should stay schematic.
- `lecture_04_figure_06.png`: The lower generator is not fully sharp and may be \(L\), \(L_i\), or a nearby variant of the same notation.
- Across the eigenstate sequence, the lecture uses \(E\) both as the scalar energy and as the ket label inside \(|E\rangle\); the notes should preserve the lecture’s notation locally but clarify the distinction in prose.