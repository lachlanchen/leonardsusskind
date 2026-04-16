# Visual Evidence
## Frame Inventory
- `lecture_07_figure_02.png`: Shows Susskind partly blocking a basis-expansion formula for a state vector, with a separate wavefunction-style label on the right; this screenshot should remain in the final notes.
- `lecture_07_figure_03.png`: Shows a vertical progression of ket notation from single-subsystem states to the composite ket `|a,b\rangle` and a generic state `|\Psi\rangle`; this screenshot should remain in the final notes.
- `lecture_07_figure_04.png`: Shows reduced-density-matrix algebra on the right board, including a summed definition and a matrix-on-column-vector step; this screenshot should remain in the final notes.
- `lecture_07_figure_06.png`: Shows a repeated-trial Bell-style board sketch with numbered rows, a central source `E`, and right-side measurement outcomes; this screenshot should remain in the final notes and be paired with a redraw.

## Equation Extraction
- `lecture_07_figure_02.png`: $|\Psi\rangle = \sum_{a,b,\ldots}\langle a,b,\ldots|\Psi\rangle\,|a,b,\ldots\rangle$ [partially visible]
- `lecture_07_figure_02.png`: $\Psi(a,b,c,\ldots)$ [visible]
- `lecture_07_figure_02.png`: $\Psi(a,b,c,\ldots)=\langle a,b,c,\ldots|\Psi\rangle$ [standard completion]
- `lecture_07_figure_02.png`: $|\Psi\rangle=\sum_{a,b,c,\ldots}\Psi(a,b,c,\ldots)\,|a,b,c,\ldots\rangle$ [standard completion]

- `lecture_07_figure_03.png`: $|a\rangle$ [visible]
- `lecture_07_figure_03.png`: $|b\rangle$ [partially visible]
- `lecture_07_figure_03.png`: $|a,b\rangle$ [visible]
- `lecture_07_figure_03.png`: $|\Psi\rangle$ [visible]

- `lecture_07_figure_04.png`: $\rho_{a'a}=\sum_b \Psi_{a'b}^*\,\Psi_{ab}$ [partially visible]
- `lecture_07_figure_04.png`: $\Psi_{a'}^*$ [visible]
- `lecture_07_figure_04.png`: $\sum_{a'} \rho_{aa'}\,\psi_{a'}$ [partially visible]
- `lecture_07_figure_04.png`: $\sum_{a'} \rho_{aa'}\,\psi_{a'}=\psi_a$ [standard completion]

- `lecture_07_figure_06.png`: $\sigma_z=+1$ [visible]
- `lecture_07_figure_06.png`: $\sigma_x=-1$ [visible]
- `lecture_07_figure_06.png`: $\sigma_y=+1$ [standard completion]

## Diagram Extraction
- `lecture_07_figure_02.png`: This is not really a diagram; preserve it as a screenshot and typeset the reconstructed equations nearby rather than redrawing it in TikZ.
- `lecture_07_figure_03.png`: This is a notation ladder rather than a geometric figure; preserve it as a screenshot and also reproduce the short ket list as clean display notation.
- `lecture_07_figure_04.png`: This is algebraic board layout, not a TikZ figure; preserve it as a screenshot and reconstruct the density-matrix steps in clean displayed equations.
- `lecture_07_figure_06.png`: This should be shown both ways. Preserve the screenshot for board evidence, and redraw a small TikZ version showing the numbered rows, the source `E`, and the right-side outcome labels.

## Reconstruction Guidance
- Use `lecture_07_figure_02.png` to support the narrative move from abstract ket expansion to wavefunction coefficients, but let the final equations be clean transcript-guided typesetting rather than a literal board transcription.
- Use `lecture_07_figure_03.png` as visual evidence for how Susskind introduces composite-state notation; the notes should reproduce the same vertical progression so the reader sees the tensor-product labeling unfold.
- Use `lecture_07_figure_04.png` to anchor the reduced-density-matrix discussion, but normalize the notation once in the chapter and write the algebra in a consistent index order even if the board order is soft.
- Use `lecture_07_figure_06.png` as documentary evidence of the repeated-trial Bell setup, then redraw only the stable structural elements in TikZ. The redraw should clarify the layout, not invent extra rows, arrows, or outcomes beyond what the frame and transcript support.
- Where the board is blurred, prefer the transcript’s mathematical intent and standard quantum-mechanics notation over aggressive visual guesswork.

## Uncertainties
- In `lecture_07_figure_02.png`, the summand labels inside the bra and ket are not fully legible, and the left side is partly blocked by Susskind’s body.
- In `lecture_07_figure_02.png`, the visible wavefunction label looks like `\Psi(a,b,c,\ldots)`, but the lecture verbally uses little `\psi`; the case should be normalized cautiously in the notes.
- In `lecture_07_figure_03.png`, the second single-subsystem ket is too soft to trust character-by-character; only its role in the vertical list is clear.
- In `lecture_07_figure_04.png`, the order of indices on $\rho$ and the exact right-hand side of the matrix-action line are not fully readable from the frame alone.
- In `lecture_07_figure_06.png`, the lower outcome label is occluded while being written; `\sigma_y=+1` is transcript-supported but not directly legible in the image.
- The transcript is notably garbled around the transition into the density-matrix section, so any completion beyond the visible board lines should be taken from the clearer surrounding statements, not from that noisy patch alone.