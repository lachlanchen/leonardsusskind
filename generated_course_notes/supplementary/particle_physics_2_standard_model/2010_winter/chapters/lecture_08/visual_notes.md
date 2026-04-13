# Visual Evidence
## Frame Inventory
- `lecture_08_figure_01.png`: Stanford title card over campus footage with no blackboard mathematics or lecture-room layout; it should not remain in the final notes.
- `lecture_08_figure_02.png`: Close crop of the complex-field plane with \(\phi_R,\phi_I,\rho,\alpha\) and partial polar-form equations at left; it should remain in the final notes.
- `lecture_08_figure_03.png`: Wider board view with two potential-energy sketches and the green label \(V(\phi)\), used to emphasize radial symmetry of the potential rather than of the field value; it should remain in the final notes.
- `lecture_08_figure_04.png`: Board derivation showing the local phase transformation and the conclusion that the ordinary derivative term is “not sym”; it should remain in the final notes.
- `lecture_08_figure_05.png`: Summary board containing \(\rho=f+H\), a schematic gauge-invariant Lagrangian, and faint field-strength invariance scratchwork; it should remain only if used as a secondary screenshot.
- `lecture_08_figure_06.png`: Tight crop of an unfinished substitution \(D\phi \to f\,\partial\alpha+\cdots\); it should not be a primary final screenshot and should be kept only as fallback evidence if no fuller neighboring frame exists.

## Equation Extraction
- `lecture_08_figure_02.png`: \(\phi_I\) [visible]
- `lecture_08_figure_02.png`: \(\phi_R\) [visible]
- `lecture_08_figure_02.png`: \(\rho\) [visible]
- `lecture_08_figure_02.png`: \(\alpha\) [visible]
- `lecture_08_figure_02.png`: \(\phi^*=\phi_R-i\phi_I\) [partially visible]
- `lecture_08_figure_02.png`: \(\phi^*=\rho e^{-i\alpha}\) [partially visible]
- `lecture_08_figure_02.png`: \((\partial\alpha)^2\) [partially visible]

- `lecture_08_figure_03.png`: \(V(\phi)\) [visible]
- `lecture_08_figure_03.png`: \(\phi_R\) [partially visible]

- `lecture_08_figure_04.png`: \(\phi'(x)=e^{i\theta(x)}\phi(x)\) [visible]
- `lecture_08_figure_04.png`: \(\partial\phi^*\,\partial\phi \neq \partial\phi^{*\prime}\,\partial\phi'\) [standard completion]
- `lecture_08_figure_04.png`: \(\text{not sym}\) [visible]

- `lecture_08_figure_05.png`: \(\rho=f+H\) [visible]
- `lecture_08_figure_05.png`: \(D\phi^*\,D\phi - V(\phi^*\phi) + F^2\) [visible]
- `lecture_08_figure_05.png`: \(F'=F\) [partially visible]
- `lecture_08_figure_05.png`: \(-\partial_\nu\partial_\mu\theta\) [partially visible]

- `lecture_08_figure_06.png`: \(D\phi \to f\,\partial\alpha+\cdots\) [partially visible]
- `lecture_08_figure_06.png`: \(D_\mu\phi \sim f(\partial_\mu\alpha \pm A_\mu)\times(\text{phase factor})\) [standard completion]

## Diagram Extraction
- `lecture_08_figure_02.png`: The internal field-space plane should be shown both ways: keep the screenshot as visual evidence and redraw it in TikZ with horizontal \(\phi_R\), vertical \(\phi_I\), a radial line labeled \(\rho\), and the angular wedge labeled \(\alpha\).
- `lecture_08_figure_03.png`: The potential-energy sketches should also be shown both ways: keep the screenshot and redraw a clean Mexican-hat or radial-slice version in TikZ, because the board layout is useful evidence but the hand-drawn curves are not precise enough to carry the final exposition alone.
- `lecture_08_figure_04.png`: This is not a geometry figure but a derivational board state; preserve it as a screenshot, and do not redraw it in TikZ.
- `lecture_08_figure_05.png`: The small symmetry-breaking potential doodle beneath the Lagrangian can be redrawn if desired, but the main value of the frame is as a board-summary screenshot rather than as a stand-alone diagram.
- `lecture_08_figure_06.png`: This crop is not strong enough to justify a redrawn figure by itself; its content should survive as a typeset equation, not as a TikZ diagram.
- `lecture_08_figure_01.png`: No diagram content should be preserved from this frame.

## Reconstruction Guidance
- Use `lecture_08_figure_02.png` to anchor a clean note-quality presentation of the complex scalar field in Cartesian and polar form. The final notes should typeset the full equations cleanly and place the screenshot beside a TikZ redraw of the field-space plane, since the frame clearly shows the board geometry but only partial equations.
- Use `lecture_08_figure_03.png` to support the passage explaining that radial symmetry belongs to the potential energy, not to the field value at a point. The final notes should redraw the potential cleanly in TikZ and keep the screenshot nearby as evidence of how Susskind organized the board and labeled \(V(\phi)\).
- Use `lecture_08_figure_04.png` to preserve the pedagogical beat “try local phase rotation, then see why it fails.” The notes should standardize the displayed equations with proper indices and priming, but the screenshot should remain because the board rhythm and the handwritten “not sym” are part of the lecture’s logic.
- Use `lecture_08_figure_05.png` only to support the cleaned schematic gauge-theory Lagrangian and the remembered expansion \(\rho=f+H\). Do not present it as evidence for the forbidden explicit photon mass term \(A_\mu A^\mu\), because that term is not actually visible in the frame.
- Use `lecture_08_figure_06.png` only as weak corroboration that Susskind is substituting the frozen-\(\rho\) form of the field into the covariant derivative. The finished equation in the notes should be reconstructed cautiously from standard gauge-theory algebra and checked against the transcript, because the visible line is incomplete and the board convention for signs is unstable.
- Ignore the unrelated right-side numerical examples in `lecture_08_figure_03.png`; they should not be promoted into the chapter.
- Keep screenshots near the corresponding clean equations or redrawn diagrams whenever the screenshot adds evidentiary value about notation, board placement, or lecture pacing.

## Uncertainties
- In `lecture_08_figure_02.png`, the left-hand equations are cropped, so the visible conjugate and polar expressions are only partial and should not be over-read.
- In `lecture_08_figure_03.png`, the far-left sketch is cropped, and the lower-left axis sketch is too faint to quote confidently.
- In `lecture_08_figure_04.png`, the derivative notation is schematic and omits explicit Lorentz indices, so the final notes must choose a consistent index convention.
- In `lecture_08_figure_05.png`, the right-hand scratchwork beyond \(F'=F\) is too faint to reconstruct reliably from the image alone.
- In `lecture_08_figure_05.png`, the subtitle timing sits in the discussion of the forbidden vector-potential-squared term, but that explicit term is not visible on the board in this frame.
- In `lecture_08_figure_06.png`, the right-hand side is cut off before the crucial gauge-field term is finished, so the presence of \(A\) or \(A_\mu\), any sign, any factor of \(i\), and any overall phase factor must be treated as cautious standard completion rather than literal transcription.
- Across the gauge-theory portion of the lecture, sign conventions for \(D_\mu\) and the gauge transformation of \(A_\mu\) are not stable on the board, so the final notes should enforce one internally consistent convention rather than mimic every board fluctuation.