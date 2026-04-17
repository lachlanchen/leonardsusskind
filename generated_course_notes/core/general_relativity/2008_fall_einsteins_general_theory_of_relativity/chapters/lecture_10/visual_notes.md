# Visual Evidence
## Frame Inventory
- `lecture_10_figure_02.png`: A clean whiteboard frame showing two centered covariant-derivative statements, with only a cropped remnant of an earlier term at the far left; this screenshot should remain in the final notes because it documents the board pairing of Einstein-tensor conservation and metric compatibility.
- `lecture_10_figure_03.png`: A board derivation frame showing the scalar-field stress-energy tensor on the top line and its \(00\)-component expansion below, with Susskind partly occluding the left side; this screenshot should remain in the final notes because it preserves both the compact covariant formula and the board layout of the energy-density unpacking.

## Equation Extraction
- `lecture_10_figure_02.png`: \(\nabla_\mu G^{\mu\nu}=0\) [visible]
- `lecture_10_figure_02.png`: \(\nabla_\mu g^{\mu\nu}=0\) [visible]
- `lecture_10_figure_02.png`: \(\kappa T_{\mu\nu}\) [partially visible]

- `lecture_10_figure_03.png`: \(T_{\mu\nu}=\partial_\mu\phi\,\partial_\nu\phi-\frac12\eta_{\mu\nu}\,\partial_\alpha\phi\,\partial^\alpha\phi\) [visible]
- `lecture_10_figure_03.png`: \(T_{00}=\dot{\phi}^{\,2}-\frac12\left[\dot{\phi}^{\,2}-\left(\frac{\partial\phi}{\partial x}\right)^2-\left(\frac{\partial\phi}{\partial y}\right)^2-\left(\frac{\partial\phi}{\partial z}\right)^2\right]\) [standard completion]
- `lecture_10_figure_03.png`: \(T_{00}=\frac12\left[\dot{\phi}^{\,2}+\left(\frac{\partial\phi}{\partial x}\right)^2+\left(\frac{\partial\phi}{\partial y}\right)^2+\left(\frac{\partial\phi}{\partial z}\right)^2\right]\) [standard completion]
- `lecture_10_figure_03.png`: \(\phi=0\) [partially visible]

## Diagram Extraction
- `lecture_10_figure_02.png` contains no standalone diagram; what matters is the vertical board structure, with \(\nabla_\mu G^{\mu\nu}=0\) written above \(\nabla_\mu g^{\mu\nu}=0\). This should be preserved as a screenshot, not redrawn in TikZ.
- `lecture_10_figure_03.png` is also not a geometric diagram but a blackboard derivation layout: compact tensor formula on top, then the component-level energy-density expansion below. This should be preserved as a screenshot, not redrawn in TikZ.
- No attached frame requires TikZ reconstruction. The two assets are evidence for equation placement and notation, not for a sketch that would benefit from vector redraw.

## Reconstruction Guidance
- Keep `lecture_10_figure_02.png` beside clean displayed LaTeX for the two covariant-derivative statements. The screenshot should function as documentary evidence of how Susskind visually linked the two equations, while the typeset math carries the exact notation in the notes.
- Keep `lecture_10_figure_03.png` beside a clean typeset version of the stress-energy tensor and the \(T_{00}\) expansion. The top equation can be typeset directly from the frame, while the lower lines should be treated as cautious standard completion because the left edge and some punctuation are partially blocked.
- Do not try to recover a full equation from the cropped \(\kappa T_{\mu\nu}\) fragment in `lecture_10_figure_02.png`; it is useful only as context that the board had just been discussing the source term.
- In `lecture_10_figure_03.png`, preserve the lecture’s progression from covariant formula to physical energy density. The final notes should not collapse this into a single isolated formula without showing the intermediate board structure.
- For both frames, prefer screenshot-plus-typeset-equation rather than screenshot replacement. The screenshots matter because the lecture is blackboard-driven and the layout itself carries part of the argument.

## Uncertainties
- In `lecture_10_figure_02.png`, the handwritten covariant-derivative symbol is stylized; \(\nabla\) is the intended reading, but the mark itself is not typographically exact.
- In `lecture_10_figure_02.png`, the cropped left-edge term is incomplete and should not be elevated into a reconstructed full equation.
- In `lecture_10_figure_03.png`, the lower lines are partly obscured by Susskind’s body and hand, so the exact left-hand labels are not fully legible from the image alone.
- In `lecture_10_figure_03.png`, the component expansion is best read as the \(00\)-component from the transcript and standard flat-space scalar-field notation; the frame alone is not sufficient to justify every symbol without cautious completion.
- In `lecture_10_figure_03.png`, the sign pattern and factor of \(\frac12\) are visually consistent with the standard formula, but the notes should rely on the cleaned special-relativistic convention rather than on every handwritten mark being perfectly readable.