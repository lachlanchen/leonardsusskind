# Visual Evidence
## Frame Inventory
- `lecture_07_figure_02.png`: A close crop of Susskind standing side-on in front of the upper-right board, with a partially occluded two-line classical-oscillator derivation ending in \(1/\beta\) and \(T\); this screenshot should remain in the final notes as secondary visual evidence.
- `lecture_07_figure_03.png`: A near-duplicate later frame with the lecturer shifted enough that the left-hand \(E\) is a little clearer while the same two-line derivation remains visible; this screenshot should remain in the final notes as the primary visual evidence.

## Equation Extraction
- `lecture_07_figure_02.png`, `lecture_07_figure_03.png` [partially visible]: \(\log Z = c\ldots\)
- `lecture_07_figure_02.png`, `lecture_07_figure_03.png` [partially visible]: \(E = -\frac{\partial \log Z}{\partial \beta} = \frac{1}{\beta} = T\)
- `lecture_07_figure_02.png`, `lecture_07_figure_03.png` [standard completion]: \(\log Z = \text{const} - \log \beta\)
- `lecture_07_figure_02.png`, `lecture_07_figure_03.png` [standard completion]: \(E = -\partial_\beta \log Z\)
- `lecture_07_figure_02.png`, `lecture_07_figure_03.png` [standard completion]: \(\frac{1}{\beta} = T\)

## Diagram Extraction
- No geometric diagram, axes, arrows, or sketch is actually visible in either frame.
- The board layout itself is useful and should be preserved: a short upper reminder line about \(\log Z\), with the main energy formula written directly beneath it on the same upper-right panel.
- These are best treated as screenshot-plus-equation figures, not as diagram figures.
- No TikZ redraw is needed for anything directly visible in the images.
- If the chapter later redraws phase-space blobs or coarse-graining in TikZ, that redraw comes from the transcript, not from these frames.

## Reconstruction Guidance
- Use `lecture_07_figure_03.png` as the main screenshot beside a clean displayed equation \(E=-\frac{\partial \log Z}{\partial \beta}=\frac{1}{\beta}=T\).
- Keep `lecture_07_figure_02.png` nearby only as corroborating board evidence; it should not be treated as a separate mathematical step.
- The upper board line should be reconstructed cautiously as \(\log Z=\text{const}-\log\beta\), because the visible initial `c` and the lower derivative line support that standard completion, but the full text is not legible.
- Do not infer from the frames alone the separate equipartition statement \(\langle K\rangle=\langle U\rangle=T/2\); that belongs in the notes only because the transcript explicitly states it.
- Preserve the screenshot when presenting the cleaned equation, because the lecturer blocks the middle of the board and the note-quality formula is partly a cautious reconstruction rather than a full literal transcription.

## Uncertainties
- The upper line is cropped and only the beginning of `\(\log Z = c\ldots\)` is visible, so the constant term is strongly suggested but not fully readable.
- The middle of the lower line, especially the `\(\log Z\)` inside the derivative, is partially hidden by the lecturer in both frames.
- The rightmost \(T\) is only partly visible in the crop, though the continuation from \(1/\beta\) is clear enough to justify the standard completion.
- `lecture_07_figure_02.png` aligns with the spoken line about average kinetic and potential energy, but the board content still shows the earlier total-energy formula rather than an explicit written \(\langle K\rangle=\langle U\rangle=T/2\).
- Because the two frames are visually very close, they should not be used to suggest two distinct derivations or two different board states.