# Visual Evidence
## Frame Inventory
- `lecture_06_figure_02.png`: A medium board shot of the tensor-product construction showing the separate state spaces, the combined space, basis-pair labeling, and the beginning of the orthonormality rule; it should remain in the final notes as a screenshot.
- `lecture_06_figure_03.png`: A product-state board shot showing a factorized two-spin state at the top and its expansion into the four composite basis states below; it should remain in the final notes as a screenshot.
- `lecture_06_figure_04.png`: A tight close-up of the spectator-index rule for \(\sigma_x\) acting on composite basis states, with the first line finished and the second still being written; it should remain in the final notes as a screenshot.
- `lecture_06_figure_05.png`: A settled four-line operator table showing action on states \(|a\,u\rangle\) and \(|a\,d\rangle\), with the first index acting as spectator; it should remain in the final notes as a screenshot.
- `lecture_06_figure_06.png`: A board shot during the commutator discussion, with an earlier worked basis-state example on the left and a partly hidden bracketed operator expression on the right; it should remain in the final notes as a screenshot.

## Equation Extraction
- `lecture_06_figure_02.png`: \(S_A,\quad S_I,\quad S_{AI}=S_A\otimes S_I\) [visible]
- `lecture_06_figure_02.png`: \(|a\rangle,\quad |i\rangle \;\mapsto\; |a\,i\rangle\) [partially visible]
- `lecture_06_figure_02.png`: \(\langle b\,j \mid a\,i\rangle=\delta_{ab}\,\delta_{ij}\) [partially visible]

- `lecture_06_figure_03.png`: \(\bigl[\alpha_u|u\rangle+\alpha_d|d\rangle\bigr]\bigl[\beta_u|u\rangle+\beta_d|d\rangle\bigr]\) [partially visible]
- `lecture_06_figure_03.png`: \(\alpha_u\beta_u|uu\rangle+\alpha_u\beta_d|ud\rangle+\alpha_d\beta_u|du\rangle+\alpha_d\beta_d|dd\rangle\) [partially visible]
- `lecture_06_figure_03.png`: \(\bigl(\alpha_u|u\rangle+\alpha_d|d\rangle\bigr)\otimes\bigl(\beta_u|u\rangle+\beta_d|d\rangle\bigr)\) [standard completion]

- `lecture_06_figure_04.png`: \(\sigma_x\,|u\,i\rangle=|d\,i\rangle\) [visible]
- `lecture_06_figure_04.png`: \(\sigma_x\,|d\,i\rangle=|u\,i\rangle\) [partially visible]

- `lecture_06_figure_05.png`: \(\tau_x\,|a\,u\rangle=|a\,d\rangle\) [visible]
- `lecture_06_figure_05.png`: \(\tau_x\,|a\,d\rangle=|a\,u\rangle\) [partially visible]
- `lecture_06_figure_05.png`: \(\tau_z\,|a\,u\rangle=|a\,u\rangle\) [visible]
- `lecture_06_figure_05.png`: \(\tau_z\,|a\,d\rangle=-|a\,d\rangle\) [visible]

- `lecture_06_figure_06.png`: \(\sigma_x\,|u\,d\rangle=|d\,d\rangle\) [partially visible]
- `lecture_06_figure_06.png`: \([\sigma_x,\tau_x]\) [partially visible]
- `lecture_06_figure_06.png`: \([\sigma_x,\tau_x]=0\) [standard completion]

## Diagram Extraction
- `lecture_06_figure_02.png` is not a geometric diagram but a three-tier board layout: top row for \(S_A\), \(S_I\), and \(S_{AI}\); middle row for basis-pair labeling; lower row for orthonormality. It should be preserved as a screenshot, not redrawn as TikZ.
- `lecture_06_figure_03.png` is likewise a layout argument rather than a picture: factorized state above, expanded composite-basis form below. It should be preserved as a screenshot and translated into clean displayed equations, not redrawn in TikZ.
- `lecture_06_figure_04.png` and `lecture_06_figure_05.png` together form a visual operator table for spectator-index action. They should remain as screenshots; the mathematical content should be re-typeset rather than turned into TikZ.
- `lecture_06_figure_06.png` captures a board transition from explicit basis-state action to abstract commutator notation. It should remain as a screenshot; the commutator statement should be typeset nearby rather than redrawn as a diagram.
- For these five frames, no genuine TikZ redraw is required. The useful “redraw” is ordinary note-quality displayed mathematics placed next to the screenshots.

## Reconstruction Guidance
- For `lecture_06_figure_02.png`, keep the screenshot and reconstruct the tensor-product relations as clean display equations: \(S_{AI}=S_A\otimes S_I\), basis pairing \(|a\rangle\otimes|i\rangle\leftrightarrow|a\,i\rangle\), and \(\langle b\,j|a\,i\rangle=\delta_{ab}\delta_{ij}\). The later general-vector formula \(\sum_{a,i}\alpha_{ai}|a\,i\rangle\) belongs in the notes, but it should be treated as transcript-backed continuation, not direct frame transcription.
- For `lecture_06_figure_03.png`, keep the screenshot and typeset both the factored product state and the full four-term expansion. The image is valuable as evidence of board layout and coefficient structure, but the final notes should not depend on the cropped right edge.
- For `lecture_06_figure_04.png`, keep the screenshot and supply the completed second line in typeset form. The visual role of the frame is to show the spectator-index idea unfolding live, while the notes should present the finished two-line rule.
- For `lecture_06_figure_05.png`, keep the screenshot and typeset the full four-line operator table cleanly, with an explicit prose remark that the first index is a spectator. Because the glyphs in the image read as \(\tau\), the notes should follow the image and nearby transcript rather than the subtitle excerpt.
- For `lecture_06_figure_06.png`, keep the screenshot but do not rely on it alone for the finished commutator statement. The final notes should typeset \([\sigma_x,\tau_x]=0\) explicitly and, if useful, add one short worked basis-state example to preserve the board-to-abstraction transition.
- Across all five frames, prefer clean displayed equations over board-faithful typography. The screenshot is the evidence; the typeset math is the authoritative reconstruction.

## Uncertainties
- In `lecture_06_figure_02.png`, the leftmost middle-line ket is blocked by Susskind, and the inner-product line softens toward the right edge. The standard reading is strong, but the frame does not itself show the later general tensor-product vector formula.
- In `lecture_06_figure_03.png`, the right end of the factorized state is cropped, and parts of the expanded coefficients are not equally legible. The full four-term expansion is standard and transcript-supported, but not every symbol is equally secure from the image alone.
- In `lecture_06_figure_04.png`, only the first \(\sigma_x\) rule is fully settled on the board. The second rule is caught mid-writing and should be completed cautiously.
- In `lecture_06_figure_05.png`, the subtitle hint mentions \(\sigma_x\), but the visible operator glyphs appear to be \(\tau_x\) and \(\tau_z\). The frame should therefore be read from the board itself first, with the transcript used only as support.
- In `lecture_06_figure_05.png`, the second-line operator is slightly less crisp than the first, even though the four-line pattern strongly supports the intended reading.
- In `lecture_06_figure_06.png`, the right-hand commutator expression is partly hidden by Susskind’s body and hand. The equality to zero is a cautious standard completion rather than a fully visible inscription.
- In `lecture_06_figure_06.png`, the left-side worked example is cropped at its beginning, so only the tail end of the basis-state calculation is reliably readable from the frame itself.