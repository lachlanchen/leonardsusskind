# Visual Evidence
## Frame Inventory
- `lecture_07_figure_02.png`: Shows the complex \(\phi\)-plane with axes labeled by real and imaginary components, a rotated-vector sketch, and the component formulas for \(\phi\) and \(\phi^*\); this screenshot should remain in the final notes.
- `lecture_07_figure_03.png`: Shows the quartic symmetry-breaking potential, the \(\rho,\alpha\) form of the Lagrangian, a boxed low-energy angular term, and a Mexican-hat-style sketch; this screenshot should remain in the final notes.
- `lecture_07_figure_04.png`: Shows a red long-wavelength wave profile used in the Goldstone/spin-wave analogy, partly obscured by the lecturer; this screenshot should remain only if that analogy is kept, and it should not stand alone without a redraw.
- `lecture_07_figure_05.png`: Shows the cleaned covariant-derivative equations and assembled gauge-invariant Lagrangian terms on the right board, with partial transformation work on the left; this screenshot should remain in the final notes.

## Equation Extraction
- `lecture_07_figure_02.png`: \(\phi_R\) [visible]
- `lecture_07_figure_02.png`: \(\phi_I\) [visible]
- `lecture_07_figure_02.png`: \(\phi=\phi_R+i\phi_I\) [visible]
- `lecture_07_figure_02.png`: \(\phi^*=\phi_R-i\phi_I\) [visible]
- `lecture_07_figure_02.png`: \(\phi^*\phi\) [visible]
- `lecture_07_figure_02.png`: \(\phi^*\phi=\phi_R^2+\phi_I^2\) [standard completion]

- `lecture_07_figure_03.png`: \(-a\,\phi^*\phi+b(\phi^*\phi)^2\) [visible]
- `lecture_07_figure_03.png`: \((\partial\rho)^2+\rho^2(\partial\alpha)^2-V(\rho)\) [standard completion]
- `lecture_07_figure_03.png`: \(f^2(\partial\alpha)^2\) [partially visible]
- `lecture_07_figure_03.png`: \(\phi=\rho e^{i\alpha}\) [standard completion]

- `lecture_07_figure_04.png`: \(\phi^*\phi\) [partially visible]
- `lecture_07_figure_04.png`: \(e^{i\alpha}\) [partially visible]
- `lecture_07_figure_04.png`: \(-a\,\phi^*\phi\) [partially visible]

- `lecture_07_figure_05.png`: \(D_\mu\phi=\partial_\mu\phi+iA_\mu\phi\) [standard completion]
- `lecture_07_figure_05.png`: \(D_\mu\phi^*=\partial_\mu\phi^*-iA_\mu\phi^*\) [standard completion]
- `lecture_07_figure_05.png`: \(D_\mu\phi\,D_\mu\phi^*-V(\phi^*\phi)\) [standard completion]
- `lecture_07_figure_05.png`: \(+\,F^2\) [visible]
- `lecture_07_figure_05.png`: \(\phi e^{i\theta}\) [partially visible]
- `lecture_07_figure_05.png`: \(A-\partial\theta\) [partially visible]
- `lecture_07_figure_05.png`: \(F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu\) [standard completion]

## Diagram Extraction
- `lecture_07_figure_02.png`: The main diagram is the \((\phi_R,\phi_I)\) plane with a vector from the origin and a nearby rotated vector or arc. This should be shown both ways: keep the screenshot and redraw it in TikZ as a clean internal-space rotation diagram.
- `lecture_07_figure_03.png`: The right-hand sketch is a Mexican-hat-style potential shown both as a surface-of-revolution and as a lower cross-section through a chosen minimum. This should also be shown both ways: keep the screenshot and redraw the potential cleanly in TikZ.
- `lecture_07_figure_03.png`: The boxed \(f^2(\partial\alpha)^2\) is not a diagram but a layout cue showing the low-energy reduction separated from the full \(\rho,\alpha\) Lagrangian. That board structure should be preserved in typeset layout even if not literally boxed in the final notes.
- `lecture_07_figure_04.png`: The red sketch is a long-wavelength profile with a left vertical marker, a small open circle, and a slowly varying line extending rightward. It should be preserved as a screenshot only if the Goldstone-wave analogy is retained, and it should definitely be redrawn in TikZ because the geometry is partly blocked.
- `lecture_07_figure_05.png`: The important visual content is the two-board layout, with unfinished transformation algebra on the left and the cleaned final covariant-derivative formulas on the right. This should be preserved as a screenshot, while the final equations themselves should be typeset rather than redrawn as a figure.

## Reconstruction Guidance
- For `lecture_07_figure_02.png`, typeset the clean component identities
  \(\phi=\phi_R+i\phi_I\), \(\phi^*=\phi_R-i\phi_I\), and \(\phi^*\phi=\phi_R^2+\phi_I^2\), and place them beside a TikZ redraw of the complex-field plane. Keep the screenshot nearby because it confirms the geometric reading of phase rotation and the board’s notation.
- For `lecture_07_figure_03.png`, reconstruct the displayed equations in note-quality form as the quartic potential, the \(\rho,\alpha\) Lagrangian, and the low-energy fixed-radius term. Keep the screenshot beside the cleaned equations because it shows that Susskind is presenting algebra and vacuum geometry together, not as separate topics.
- For `lecture_07_figure_03.png`, redraw the Mexican-hat potential rather than trying to quote the faint hand sketch literally. The redraw should prioritize the central maximum, the circular trough of minima, and a radial slice through a chosen vacuum.
- For `lecture_07_figure_04.png`, treat the screenshot as evidence of the lecture-room board sketch, not as a complete mathematical figure. Redraw only the slow wave profile and boundary marker in TikZ, and do not import any precise spin-chain or lattice detail that is not actually visible.
- For `lecture_07_figure_05.png`, typeset a clean aligned block for the covariant derivatives and the gauge-invariant Lagrangian, and use the screenshot to preserve the pedagogical transition from transformation algebra to final result. The left board should inform narrative layout, but not be transcribed as a complete derivation.
- When the board is only partly legible, prefer cautious standard completion that matches the transcripted argument and standard relativistic notation. Do not normalize every coefficient aggressively if the lecture itself treated factors like \(1/2\) or \(1/4\) as conventional.

## Uncertainties
- In `lecture_07_figure_02.png`, the curved arrow and second radial segment clearly indicate a phase rotation, but no explicit angle label is visible.
- In `lecture_07_figure_02.png`, there is cropped leftover writing at the far left edge that should not be transcribed into the notes.
- In `lecture_07_figure_03.png`, the handwritten derivative notation is loose; the clean form \((\partial\rho)^2+\rho^2(\partial\alpha)^2\) is a cautious standard completion rather than a perfectly sharp reading of every symbol.
- In `lecture_07_figure_03.png`, the board writes \(V(\rho)\)-like notation, while the transcripted derivation really points to a potential depending on the radial degree of freedom, often naturally viewed as \(V(\rho^2)\). The final notes should phrase this carefully.
- In `lecture_07_figure_03.png`, the tiny labels near the lower cross-section of the potential are too faint to quote with confidence.
- In `lecture_07_figure_04.png`, the right side of the red profile is obscured by the lecturer, so the full endpoint structure is not reliably visible.
- In `lecture_07_figure_04.png`, the remaining equations at the margins are leftovers from nearby board work and should not be treated as part of the wave sketch.
- In `lecture_07_figure_05.png`, the final displayed equations are readable in structure but not all indices and factors are sharp enough to fix normalization from the image alone.
- In `lecture_07_figure_05.png`, the left-board transformation law is incomplete in frame, and the lecture itself contains sign-checking during this derivation, so the gauge-transformation sign convention should be standardized cautiously in the written notes.