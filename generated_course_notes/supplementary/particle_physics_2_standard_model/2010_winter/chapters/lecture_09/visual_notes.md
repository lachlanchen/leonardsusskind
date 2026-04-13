# Visual Evidence
## Frame Inventory
- `lecture_09_figure_02.png`: Shows the board-level reminder \(F_{\mu\nu}\) together with a separate `\(F^2\)` shorthand for the gauge-field term, and it should remain in the final notes as a screenshot.
- `lecture_09_figure_03.png`: Shows the frozen Higgs-field substitution, the covariant-derivative step, and a faint broken-potential sketch, and it should remain in the final notes as a screenshot.
- `lecture_09_figure_04.png`: Shows the continuation of the broken-phase derivation down to the isolated `\(f^2A^2\)` term with Susskind’s finger marking the target term, and it should remain in the final notes as a screenshot.
- `lecture_09_figure_05.png`: Shows the stacked Dirac and left-right coupled fermion equations, and it should remain in the final notes as a screenshot.

## Equation Extraction
- `lecture_09_figure_02.png`: \(F_{\mu\nu}=\dfrac{\partial A_\mu}{\partial x^\nu}-\dfrac{\partial A_\nu}{\partial x^\mu}\) [visible]
- `lecture_09_figure_02.png`: \(F^2\) [visible]

- `lecture_09_figure_03.png`: \(\phi = f e^{i\alpha}\) [visible]
- `lecture_09_figure_03.png`: \(D\phi = \partial\phi + iA\phi\) [visible]
- `lecture_09_figure_03.png`: \(D\phi = i(\partial\alpha + A)\, f e^{i\alpha}\) [visible]

- `lecture_09_figure_04.png`: \(D\phi = \partial\phi + iA\phi\) [partially visible]
- `lecture_09_figure_04.png`: \(D\phi = i(\partial\alpha + A)\, f e^{i\alpha}\) [partially visible]
- `lecture_09_figure_04.png`: \(f^2(\partial\alpha + A)^2\) [visible]
- `lecture_09_figure_04.png`: \(f^2A^2\) [visible]
- `lecture_09_figure_04.png`: \(|D_\mu\phi|^2 \approx f^2(\partial_\mu\alpha + A_\mu)(\partial^\mu\alpha + A^\mu)\) [standard completion]
- `lecture_09_figure_04.png`: \(f^2A_\mu A^\mu\) [standard completion]

- `lecture_09_figure_05.png`: \(i\left(\dfrac{\partial\Psi}{\partial t}+\alpha_i\dfrac{\partial\Psi}{\partial x_i}\right)=m\beta\Psi\) [visible]
- `lecture_09_figure_05.png`: \(i\left(\dfrac{\partial\Psi_R}{\partial t}+i\,\alpha_i\dfrac{\partial\Psi_R}{\partial x_i}\right)=m\Psi_L\) [standard completion]
- `lecture_09_figure_05.png`: \(i\left(\dfrac{\partial\Psi_L}{\partial t}-i\,\alpha_i\dfrac{\partial\Psi_L}{\partial x_i}\right)=m\Psi_R\) [standard completion]
- `lecture_09_figure_05.png`: \(m\Psi_L,\; m\Psi_R\) [visible]

## Diagram Extraction
- `lecture_09_figure_02.png` does not contain a diagram, but the board layout matters: the field-strength definition at upper left and the separate `\(F^2\)` lower left visually encode the move from tensor to Lagrangian shorthand, so this should be preserved as a screenshot only.
- `lecture_09_figure_03.png` contains the only genuine sketch: a faint radial slice of the broken Higgs potential with a minimum marked near \(f\). This should be shown both ways: keep the screenshot as evidence, and redraw a clean TikZ version nearby for legibility.
- `lecture_09_figure_04.png` is not a diagram in the usual sense, but it does have meaningful visual emphasis: the lower line isolates `\(A^2\)` and the pointing gesture identifies the mass-generating term. This should be preserved as a screenshot only.
- `lecture_09_figure_05.png` is an equation stack rather than a diagram. It should be preserved as a screenshot, with no TikZ redraw of the board itself; if the chapter later wants a tiny chiral-mixing schematic, that should be an added explanatory aid rather than a replacement.

## Reconstruction Guidance
- Use `lecture_09_figure_02.png` to anchor the opening gauge-field recap, but typeset the field-strength definition in standard index notation \(F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu\). Treat the board’s `\(F^2\)` as lecture shorthand for the gauge-field kinetic term rather than as a full equation.
- Use `lecture_09_figure_03.png` and `lecture_09_figure_04.png` together as one derivational block: first the frozen-radius substitution \(\phi \approx f e^{i\alpha}\), then the covariant derivative, then the squared combination \(f^2(\partial\alpha + A)^2\), and finally the effective \(A^2\) mass term after the gauge redefinition. The notes should restore Lorentz indices and the modulus square cleanly even though the board suppresses them.
- Keep the original screenshots beside the cleaned equations whenever the board organization carries interpretive weight. In practice that especially matters for `lecture_09_figure_03.png`, where the derivation sits directly above the potential sketch, and for `lecture_09_figure_04.png`, where the pointing gesture singles out the term being interpreted physically.
- Redraw the faint sketch from `lecture_09_figure_03.png` in TikZ as a simple radial cross-section of the broken potential, not as an overly elaborate full Mexican-hat surface. The screenshot should still remain nearby because it shows the lecture’s actual board flow.
- Use `lecture_09_figure_05.png` as evidence for the existence and layout of the coupled left-right equations, but retypeset them from a cautious transcript-guided reconstruction rather than copying the board line for line. The final notes should standardize the notation for \(\alpha_i\), \(\beta\), \(\Psi_L\), and \(\Psi_R\), and make the coupling between left and right explicit.
- Standardize the vacuum-value symbol once in the written notes. The frames visibly use lower-case \(f\), while the transcript often speaks of upper-case \(F\); the chapter should pick one convention and note the lecture-level variation only if it helps avoid confusion.

## Uncertainties
- In `lecture_09_figure_02.png`, the equation is legible in intent but written in a nonstandard fraction form, and the superscript/subscript placement on the coordinate labels is not fully trustworthy as a final typeset model.
- In `lecture_09_figure_03.png`, the derivative in \((\partial\alpha + A)\) is schematic and index-free, and the sign convention for the covariant derivative is not fully secure from the frame alone.
- The small potential sketch in `lecture_09_figure_03.png` is faint and minimal. It reliably indicates a broken minimum at nonzero \(f\), but it does not justify a highly specific reconstruction of the full potential shape.
- In `lecture_09_figure_04.png`, the visible `\(A^2\)` is clear, but the intended relativistic expression has to be completed cautiously as \(A_\mu A^\mu\); the indices are not written on the board.
- In `lecture_09_figure_05.png`, the exact placement of the \(i\) factors and the precise form of the spatial-derivative terms are not fully legible. The transcript itself later admits inconsistency in how the \(i\) was handled on the board, so the split equations should be treated as cautious standard completions.
- Also in `lecture_09_figure_05.png`, the matrix multiplying the spatial derivative is almost certainly \(\alpha_i\), but the visual evidence alone is weaker than the transcript-backed reading.
- Across the Higgs-mechanism frames, the gauge coupling constant is suppressed entirely. Any fully indexed or normalized formula in the final notes is therefore a reconstruction, not a verbatim board transcription.