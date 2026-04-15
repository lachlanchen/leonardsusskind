# Visual Evidence
## Frame Inventory
- `lecture_04_figure_01.png`: Stanford opening slate only, with no board content or mathematics; it should not remain in the final chapter body.
- `lecture_04_figure_02.png`: Susskind stands in front of a board listing spatial metric forms under a common `a(t)^2` factor, with visible curvature labels; it should remain only if retimed to the earlier FRW-metric discussion, not at its current timestamp.
- `lecture_04_figure_03.png`: a clear board shot of the Einstein-equation left-hand side together with the prefactor `\frac{8\pi G}{3}`; it should remain in the final notes as the main screenshot for the Einstein-equation section.
- `lecture_04_figure_04.png`: a weaker side-angle frame showing only a fragment of the same Einstein-equation board; it should not remain as a standalone figure.
- `lecture_04_figure_05.png`: a board with a large round closed curve and an irregular peanut-shaped closed curve, apparently illustrating intrinsic versus extrinsic shape; it should remain only if retimed to the earlier geometry discussion, not at its current late timestamp.
- `lecture_04_figure_06.png`: a strong split-board frame showing `P = W\rho` on one side and matter/radiation density scalings on the other; it should remain in the final notes.

## Equation Extraction
- `lecture_04_figure_01.png`: no equations visible.
- `lecture_04_figure_02.png`: `a(t)^2` [visible]
- `lecture_04_figure_02.png`: `dx^2 + dy^2 + dz^2` [visible]
- `lecture_04_figure_02.png`: `dr^2 + r^2 d\Omega_2^2` [partially visible]
- `lecture_04_figure_02.png`: `K = 0` [visible]
- `lecture_04_figure_02.png`: `K = -1` [visible]
- `lecture_04_figure_03.png`: `R^{\mu\nu} - \frac{1}{2} g^{\mu\nu} R = \frac{8\pi G}{3}` [visible]
- `lecture_04_figure_03.png`: `R^{\mu\nu} - \frac{1}{2} g^{\mu\nu} R = \frac{8\pi G}{3}\,T^{\mu\nu}` [standard completion]
- `lecture_04_figure_04.png`: `R^{\mu\nu} - \frac{1}{2} g^{\mu\nu} R` [partially visible]
- `lecture_04_figure_05.png`: no legible equations, only sketches and point/tick marks.
- `lecture_04_figure_06.png`: `P = W\rho` [visible]
- `lecture_04_figure_06.png`: `\frac{\rho_0}{a^3}` [visible]
- `lecture_04_figure_06.png`: `\frac{\rho_0}{a^4}` [visible]
- `lecture_04_figure_06.png`: `\rho_{\text{matter}} = \frac{\rho_0}{a^3}` [standard completion]
- `lecture_04_figure_06.png`: `\rho_{\text{rad}} = \frac{\rho_0}{a^4}` [standard completion]

## Diagram Extraction
- `lecture_04_figure_02.png`: the important visual feature is the board layout, not a single isolated equation: a large brace groups several candidate spatial metrics under one overall scale-factor multiplier. This should be reconstructed as aligned equations in LaTeX, with the screenshot used only as supporting evidence if the figure is moved to the correct earlier section.
- `lecture_04_figure_03.png`: this is best preserved as a screenshot rather than redrawn as a diagram. Its value is as board evidence that Susskind explicitly wrote the Einstein-equation structure before discussing the time-time component.
- `lecture_04_figure_05.png`: the large circular loop and the deformed peanut-shaped loop should be redrawn in TikZ if used, because the mathematical point is the intrinsic equivalence of differently embedded one-dimensional closed spaces. If retimed to the intrinsic-geometry discussion, the screenshot and a clean TikZ redraw should appear together.
- `lecture_04_figure_06.png`: the split-board arrangement should be preserved as a screenshot because it visually stages the lecture’s move from named density scalings to the compact equation of state. The equations themselves should also be retypeset cleanly nearby.

## Reconstruction Guidance
- Use `lecture_04_figure_03.png` as the main visual witness for the Einstein-equation discussion, but typeset the full equation cleanly in the notes. The visible frame supports the left-hand geometric structure and the `\frac{8\pi G}{3}` prefactor; the `T^{\mu\nu}` factor should be supplied from the transcript, not invented from the image.
- Use `lecture_04_figure_06.png` as a retained screenshot and place next to it a clean displayed block with `P = w\rho`, `\rho_{\text{matter}} \propto a^{-3}`, and `\rho_{\text{rad}} \propto a^{-4}`. The board strongly supports this as a meaningful lecture transition.
- Treat `lecture_04_figure_02.png` as stale but still useful visual evidence for the earlier FRW-metric menu. Reconstruct the three spatial metric cases from the transcript in standard aligned form, and use the screenshot only if it can be moved to the right place in the chapter.
- Treat `lecture_04_figure_05.png` the same way: stale at its assigned timestamp, but useful if reassigned to the earlier intrinsic-geometry section. In that section, redraw the round and deformed closed curves in TikZ and keep the screenshot nearby as evidence of the original blackboard presentation.
- Omit `lecture_04_figure_01.png` and `lecture_04_figure_04.png` from the mathematical chapter body. They add no essential note-writing value beyond what other frames already show.
- Normalize notation in the polished notes even when the board is inconsistent: prefer `a(t)`, `w`, `\rho`, and standard tensor typography. The board’s uppercase `W` can be noted implicitly but should not control the final notation.

## Uncertainties
- `lecture_04_figure_02.png` is temporally mismatched with the nearby subtitle about the energy-momentum tensor, so its timestamp should not be trusted for narrative placement.
- `lecture_04_figure_02.png` does not show the full metric stack clearly enough to recover every line from the image alone; the hidden middle entries must come from the transcript.
- `lecture_04_figure_03.png` visibly stops at `\frac{8\pi G}{3}` on the right-hand side. The completion with `T^{\mu\nu}` is justified by the transcript, not by the frame itself.
- `lecture_04_figure_03.png` preserves a lecture-faithful `\frac{8\pi G}{3}` normalization, which is not the standard textbook normalization of the full Einstein equation; the notes should follow the lecture carefully and explain context if needed.
- `lecture_04_figure_04.png` does not visibly support the transcript’s discussion of second-derivative cancellation; it only preserves a leftover equation fragment.
- `lecture_04_figure_05.png` strongly looks like an earlier intrinsic-geometry board, not a late-time `F=ma` discussion frame, so it should not be cited as evidence for the late subtitle window.
- `lecture_04_figure_06.png` shows cropped labels on the left; the interpretations “matter-dominated” and “radiation-dominated” are standard completions supported by the transcript, not fully legible in the frame.
- `lecture_04_figure_06.png` appears to use uppercase `W` on the board. The final notes may reasonably normalize this to lowercase `w`, but that is an editorial choice rather than a purely visual reading.