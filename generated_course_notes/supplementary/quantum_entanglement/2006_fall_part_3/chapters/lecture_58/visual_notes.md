# Visual Evidence
## Frame Inventory
- `lecture_58_figure_01.png`: Stanford opening title card with logo and university text; this should not remain in the final notes because it contains no mathematical board content.
- `lecture_58_figure_02.png`: Sparse whiteboard shot of the Lorentz-force formula followed by an incomplete tensor-style rewrite; this should remain in the final notes if the recap-to-covariant pivot is shown.
- `lecture_58_figure_03.png`: Partial anti-symmetric \(F^{\mu\nu}\) matrix with headers \(t,x,y,z\), electric-field entries, and visible zero-diagonal placeholders; this should remain in the final notes.
- `lecture_58_figure_04.png`: Close-up of the one-dimensional wave equation \(\partial_t^2\phi-\partial_z^2\phi=0\) with the lecturer pointing to the spatial term; this should remain in the final notes.
- `lecture_58_figure_05.png`: Blackboard sketch of a sinusoidal transverse wave along a horizontal \(z\)-axis with short oscillation arrows, plus cropped notation above; this should remain only if the final notes use it in the electromagnetic-wave section and explicitly treat it as metadata-misaligned.

## Equation Extraction
- `lecture_58_figure_02.png`: \(F = q(E + V \times B)\) [visible]
- `lecture_58_figure_02.png`: \(= q\,F^{\mu\nu}\) [visible]
- `lecture_58_figure_02.png`: \(f^\mu = q\,F^{\mu}{}_{\nu}u^\nu\) [standard completion]
- `lecture_58_figure_03.png`: \(F^{\mu\nu}\) [visible]
- `lecture_58_figure_03.png`: \(t,\ x,\ y,\ z\) [visible]
- `lecture_58_figure_03.png`: \(0,\ -E_x,\ -E_y,\ -E_z\) across the first row [visible]
- `lecture_58_figure_03.png`: \(+E_x,\ +E_y,\ +E_z\) down the first column below the top entry [visible]
- `lecture_58_figure_03.png`: diagonal zeros of the anti-symmetric matrix [visible]
- `lecture_58_figure_03.png`: \(F^{\mu\nu}=\begin{pmatrix}0&-E_x&-E_y&-E_z\\ E_x&0&-B_z&B_y\\ E_y&B_z&0&-B_x\\ E_z&-B_y&B_x&0\end{pmatrix}\) [standard completion]
- `lecture_58_figure_04.png`: \(\frac{\partial^2 \phi}{\partial t^2}-\frac{\partial^2 \phi}{\partial z^2}=0\) [visible]
- `lecture_58_figure_05.png`: \(z\) [visible]
- `lecture_58_figure_05.png`: an upper cropped expression ending in \(=0\) [partially visible]

## Diagram Extraction
- `lecture_58_figure_02.png` is not really a diagram; it is a board-layout moment where the lecture turns from the three-vector Lorentz force to a covariant tensor formulation. Preserve the screenshot and pair it with a clean displayed equation.
- `lecture_58_figure_03.png` is a matrix-layout figure rather than a geometric sketch. Preserve the screenshot as visual evidence of board organization, then typeset the completed \(4\times4\) tensor cleanly rather than redrawing it in TikZ.
- `lecture_58_figure_04.png` is equation-only content, so it should be preserved as a screenshot and also reproduced as a clean displayed equation nearby.
- `lecture_58_figure_05.png` is the only frame that naturally suggests a TikZ redraw: a transverse sinusoidal wave propagating along \(z\), with oscillation perpendicular to the propagation direction. If used, show both the screenshot and a cleaned-up TikZ version side by side or in close proximity.
- `lecture_58_figure_01.png` contains no usable diagrammatic or mathematical content and should not be used as evidence in the chapter body.

## Reconstruction Guidance
- For `lecture_58_figure_02.png`, keep the screenshot because the emptiness of the board makes the conceptual pivot visually clear. In the notes, do not typeset the second line exactly as written; instead, replace it with a complete covariant force law backed by the transcript.
- For `lecture_58_figure_03.png`, use the screenshot to preserve the matrix headers, sign pattern, and anti-symmetric board logic. Then supply a fully typeset \(F^{\mu\nu}\) matrix in standard notation, completing only the magnetic entries that are securely supported by the transcript.
- For `lecture_58_figure_04.png`, keep the screenshot as evidence for the one-dimensional reduction of the wave equation. Typeset the same equation in normalized notation, and if the surrounding text introduces the full \(3+1\) wave equation, make clear that the full form comes from the transcript rather than from the frame.
- For `lecture_58_figure_05.png`, do not rely on the subtitle metadata. If the final notes place it in the electromagnetic-wave discussion, keep the screenshot as evidence of the lecturer’s board sketch and redraw the wave in TikZ with a labeled \(z\)-axis and clearly transverse oscillation.
- For `lecture_58_figure_05.png`, the cleaned diagram should stay modest: a sinusoidal profile along \(z\), plus arrows or axis labels showing the oscillation direction. The screenshot should remain nearby so the redraw does not drift into generic textbook styling.
- `lecture_58_figure_01.png` should be omitted from the mathematical chapter entirely unless there is a separate archival appendix documenting source-video title cards.

## Uncertainties
- In `lecture_58_figure_02.png`, the lower line \(=q\,F^{\mu\nu}\) is visibly incomplete. The missing index contraction with the four-velocity is not on the board and must be reconstructed cautiously from the transcript.
- In `lecture_58_figure_02.png`, the cross-product variable looks like an uppercase \(V\), but the lecture content suggests ordinary velocity notation. The final notes may normalize this to \(\mathbf v\).
- In `lecture_58_figure_03.png`, the cropped symbols above the matrix belong to neighboring board work and should not be used as evidence for the tensor itself.
- In `lecture_58_figure_03.png`, the magnetic-field entries are not fully visible in the frame. Any completed matrix must therefore be marked as a cautious transcript-backed completion rather than a direct transcription of the image.
- In `lecture_58_figure_04.png`, the lecturer’s hand partly crowds the lower derivative, but the equation is still legible enough for faithful transcription.
- In `lecture_58_figure_05.png`, the upper cropped expression is too incomplete to quote reliably.
- In `lecture_58_figure_05.png`, the sketch clearly shows propagation along \(z\), but it does not by itself prove whether the oscillating quantity is \(E\), \(B\), or a generic field. That identification has to come from the transcript.
- `lecture_58_figure_05.png` is visually useful but timestamp-misaligned with its supplied subtitle metadata, so it should be used only with an explicit editorial caution.