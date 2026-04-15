# Visual Evidence
## Frame Inventory
- `lecture_10_figure_01.png` shows the Stanford University title card on a black background and should not remain in the final notes.
- `lecture_10_figure_02.png` shows Susskind beside an almost empty board with the isolated vacuum equation \(R_{\mu\nu}=0\), and it should remain as a screenshot near the opening vacuum discussion.
- `lecture_10_figure_03.png` shows the early weak-field board, with the perturbative metric written on the left and schematic curvature/Christoffel structure on the right, and it should remain as a screenshot.
- `lecture_10_figure_04.png` shows a clearer continuation of the same weak-field board, including the \(\eta+h\) split and the inverse-metric shorthand \(\eta-h\), and it should remain as a screenshot.
- `lecture_10_figure_05.png` shows the coordinate-change example with infinitesimal corrections, transformed differentials, and the induced metric correction, and it should remain as a screenshot.
- `lecture_10_figure_06.png` shows the transverse gravitational-wave board with sinusoidal components, a propagation sketch, and the traceless condition, and it should remain as a screenshot.

## Equation Extraction
- `lecture_10_figure_02.png`: \(R_{\mu\nu}=0\) [visible]

- `lecture_10_figure_03.png`: \(R_{\mu\nu}=0\) [visible]
- `lecture_10_figure_03.png`: \(g_{\mu\nu}=\eta_{\mu\nu}\) [visible]
- `lecture_10_figure_03.png`: \(g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu}(x,t)\) [partially visible]
- `lecture_10_figure_03.png`: \(R=\partial\Gamma+\Gamma\Gamma\) [visible]
- `lecture_10_figure_03.png`: \(\Gamma=\tfrac12\,g^{-1}\partial g\) [visible]

- `lecture_10_figure_04.png`: \(R_{\mu\nu}=0\) [visible]
- `lecture_10_figure_04.png`: \(g_{\mu\nu}=\eta_{\mu\nu}\) [visible]
- `lecture_10_figure_04.png`: \(g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu}(x,t)\) [visible]
- `lecture_10_figure_04.png`: \(\eta-h\) [visible]
- `lecture_10_figure_04.png`: \(R=\partial\Gamma+\Gamma\Gamma\) [visible]
- `lecture_10_figure_04.png`: \(\Gamma=\tfrac12\,g^{-1}\partial g\) [visible]
- `lecture_10_figure_04.png`: \(g^{-1}\sim\eta-h\) [standard completion]

- `lecture_10_figure_05.png`: \(X'=F(x,y)\) [visible]
- `lecture_10_figure_05.png`: \(Y'=G(x,y)\) [visible]
- `lecture_10_figure_05.png`: \(X'=X+f_x(x,y)\) [visible]
- `lecture_10_figure_05.png`: \(Y'=Y+f_y(x,y)\) [visible]
- `lecture_10_figure_05.png`: \(dx'=dx+\dfrac{\partial f_x}{\partial x^m}dx^m\) [visible]
- `lecture_10_figure_05.png`: \(dy'=dy+\dfrac{\partial f_y}{\partial x^m}dx^m\) [visible]
- `lecture_10_figure_05.png`: \(dx'^2+dy'^2=dx^2+dy^2+h_{mn}\,dx^m dx^n\) [visible]

- `lecture_10_figure_06.png`: \(h_{xx}=h_{xx}^{0}\sin k(z-t)\) [partially visible]
- `lecture_10_figure_06.png`: \(h_{yy}=-h_{xx}=h_{yy}^{0}\sin k(z-t)\) [partially visible]
- `lecture_10_figure_06.png`: \(h_{xy}=h_{xy}^{0}\sin k(z-t)\) [partially visible]
- `lecture_10_figure_06.png`: \(h_{ij}^{0}\sin k(z-t)\) [partially visible]
- `lecture_10_figure_06.png`: \(h_{xx}+h_{yy}=0\) [visible]

## Diagram Extraction
- `lecture_10_figure_02.png` should be preserved only as a screenshot; its value is the isolated board layout with the vacuum equation written almost alone.
- `lecture_10_figure_03.png` should be preserved as a screenshot because the two-column board organization matters pedagogically, but it does not need a separate TikZ redraw.
- `lecture_10_figure_04.png` should also be preserved as a screenshot because it captures the same two-column structure more clearly, again without needing a standalone TikZ redraw.
- `lecture_10_figure_05.png` should be shown both ways: keep the screenshot, and redraw in TikZ a flat plane with slightly wiggly coordinate lines or an infinitesimal coordinate deformation, since the partially visible red sketch suggests exactly that explanatory picture.
- `lecture_10_figure_06.png` should be shown both ways: keep the screenshot, and redraw in TikZ the wave propagating along the \(z\)-axis with transverse \(x\)-\(y\) slices, together with a clean plus/cross polarization deformation in the transverse plane.
- In `lecture_10_figure_06.png`, the upper-right sketch visibly labels \(y\) upward, \(z\) to the right, and \(x\) as a slanted transverse axis, with several parallel sheets indicating propagation along \(z\); the lower sketch appears to indicate a rotated transverse orientation and should be treated as supporting evidence for a polarization redraw rather than copied literally.

## Reconstruction Guidance
- Use `lecture_10_figure_02.png` to anchor the opening vacuum equation exactly as written, but typeset it cleanly as \(R_{\mu\nu}=0\) in the notes.
- Use `lecture_10_figure_03.png` and `lecture_10_figure_04.png` as evidence for the schematic first-order argument, not as finished tensor formulas. The clean note version should present \(g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu}\), then cautiously reconstruct \(g^{\mu\nu}\approx\eta^{\mu\nu}-h^{\mu\nu}\), and explain that the board’s \(R=\partial\Gamma+\Gamma\Gamma\) and \(\Gamma\sim\tfrac12 g^{-1}\partial g\) are shorthand for the linearized logic \(\Gamma\sim\partial h\), \(R_{\mu\nu}\sim\partial\partial h\).
- Keep `lecture_10_figure_03.png` and `lecture_10_figure_04.png` nearby when the notes discuss why derivatives of the background metric vanish. That step is visually present on the board and should not be turned into an unsupported full derivation.
- Use `lecture_10_figure_05.png` to reconstruct the infinitesimal coordinate-change example cleanly in LaTeX: first the finite transformation, then the infinitesimal version, then the transformed differentials, then the corrected line element. If the notes need the explicit gauge-form perturbation \(h_{mn}=\partial_n f_m+\partial_m f_n\), present it as a cautious standard completion of the visible board argument rather than as a direct transcription from this frame.
- Use `lecture_10_figure_06.png` to support the transverse-traceless wave discussion, but normalize the notation in print. The notes should present a clean phase convention such as \(\sin k(z-t)\), retain \(h_{xx}+h_{yy}=0\), and translate the board content into the standard transverse-plane polarization description.
- When redrawing `lecture_10_figure_06.png`, prefer a clean physical picture over a literal copy of the chalk sketch: one propagation diagram along \(z\), and one transverse-plane deformation figure for the plus and cross modes. The screenshot should stay nearby as visual evidence that this is how the lecture organized the discussion.
- Omit `lecture_10_figure_01.png` entirely from the mathematical notes.

## Uncertainties
- `lecture_10_figure_01.png` has no mathematical content and should not influence the reconstruction.
- In `lecture_10_figure_03.png` and `lecture_10_figure_04.png`, the argument of \(h_{\mu\nu}\) is not perfectly sharp; \((x,t)\) is the most plausible reading.
- In `lecture_10_figure_03.png` and `lecture_10_figure_04.png`, the right-hand formulas are clearly schematic board shorthand, not full indexed definitions.
- In `lecture_10_figure_04.png`, the \(\eta-h\) note lacks indices and should not be quoted as a complete formula without careful standard completion.
- In `lecture_10_figure_05.png`, the board mixes upper-case and lower-case coordinates, and the top functions \(F,G\) could conceivably be read as lower-case by shape alone.
- In `lecture_10_figure_06.png`, the sinusoidal arguments are partly blurred, so the exact phase convention should be normalized carefully in the notes.
- In `lecture_10_figure_06.png`, the amplitude superscripts look like small zeros or circles and are not completely reliable as literal notation.
- In `lecture_10_figure_06.png`, the lower sketch is suggestive rather than explicit; it supports a rotated polarization interpretation, but it should not be over-read without a cleaner redraw.
- The frames do not reliably determine the full sign convention for \(\eta_{\mu\nu}\); that should be fixed from the broader chapter notation rather than from these images alone.