# Visual Evidence
## Frame Inventory
- `lecture_01_figure_02.png`: Wide blackboard shot showing a left-hand Regge plot and two meson-scattering channel sketches; the screenshot should remain in the final notes because the board-wide layout and hand-drawn topology are useful evidence and should also be paired with a clean TikZ redraw.
- `lecture_01_figure_04.png`: Blackboard close-up of the large-\(P_z\) energy expansion with an upper square-root formula and a lower many-particle decomposition beginning with \(E=\sum P_3+\cdots\); the screenshot should remain because it directly evidences the lecture’s algebraic hierarchy.
- `lecture_01_figure_05.png`: Later state of the same board where the light-cone energy is explicitly identified with the Hamiltonian through a partially cropped \(i\,\partial/\partial t = H =\) line; the screenshot should remain because it captures the interpretive step from energy formula to Hamiltonian.
- `lecture_01_figure_06.png`: Blackboard shot of the discrete masses-and-springs string energy, its nearest-neighbor term, the arrow to a \(\sigma\)-derivative, and the lower continuum integral; the screenshot should remain because it preserves the actual discrete-to-continuum board flow.

## Equation Extraction
- `lecture_01_figure_02.png`: \(m^2\) [visible]
- `lecture_01_figure_02.png`: \(\text{Regge}\) [visible]
- `lecture_01_figure_02.png`: vertical-axis quantity interpreted as angular momentum or spin [standard completion]

- `lecture_01_figure_04.png`: \(P_3\sqrt{1+\dfrac{p_x^2+p_y^2+m^2}{P_3^2}}\) [partially visible]
- `lecture_01_figure_04.png`: \(E=\sum P_3+\sum \dfrac{p_\perp^2}{2P_z}+\sum \dfrac{m^2}{2P_z}\) [standard completion]
- `lecture_01_figure_04.png`: \(\sum P_3\) [visible]
- `lecture_01_figure_04.png`: \(\dfrac{p_\perp^2}{2P_z}\) [partially visible]
- `lecture_01_figure_04.png`: \(\dfrac{m^2}{2P_z}\) [partially visible]

- `lecture_01_figure_05.png`: \(i\frac{\partial}{\partial t}=H\) [partially visible]
- `lecture_01_figure_05.png`: \(H=\sum_i\left(\dfrac{p_{\perp i}^2}{2P_{zi}}+\dfrac{m_i^2}{2P_{zi}}\right)\) [standard completion]
- `lecture_01_figure_05.png`: \(H=\) [visible]
- `lecture_01_figure_05.png`: \(P_3\sqrt{1+\dfrac{p_x^2+p_y^2+m^2}{P_3^2}}\) [partially visible]

- `lecture_01_figure_06.png`: \(E=m\sum_i \dfrac{\dot X_i^2}{2}+\dfrac{k}{2}(X_i-X_{i+1})^2\) [partially visible]
- `lecture_01_figure_06.png`: \((X_i-X_{i+1})^2 \rightarrow \left(\dfrac{\partial X}{\partial \sigma}\right)^2\) [partially visible]
- `lecture_01_figure_06.png`: \(\int_0^\pi d\sigma\) [visible]
- `lecture_01_figure_06.png`: \(\dfrac{\dot X^2(\sigma)}{2}\) [partially visible]
- `lecture_01_figure_06.png`: \(E\sim \int_0^\pi d\sigma\left(\dfrac{\dot X^2(\sigma)}{2}+\left(\dfrac{\partial X}{\partial \sigma}\right)^2\right)\) [standard completion]

## Diagram Extraction
- `lecture_01_figure_02.png`: The left part is a Regge-style plot with a shallow horizontal axis labeled \(m^2\) and an ascending family of points; this should be shown both as the original screenshot and as a clean TikZ redraw.
- `lecture_01_figure_02.png`: The center and right parts are two related meson-scattering channel sketches, one with a vertical wavy internal segment and one with a horizontal wavy exchange; these should also be shown both ways, since the screenshot records the original board juxtaposition while TikZ can make the topology clean.
- `lecture_01_figure_04.png`: This is not a diagram to redraw in TikZ; it should be preserved as a screenshot and accompanied by clean displayed equations.
- `lecture_01_figure_05.png`: This is likewise algebraic board evidence rather than a geometric figure; preserve as screenshot and typeset the cleaned Hamiltonian identification nearby.
- `lecture_01_figure_06.png`: The board is organized as a derivation rather than a geometric figure, with discrete expression on top, derivative replacement at right, and continuum integral below; preserve as screenshot and typeset the cleaned discrete and continuum formulas rather than forcing a TikZ redraw.

## Reconstruction Guidance
- Use `lecture_01_figure_02.png` as visual evidence for the lecture’s historical pivot from Regge trajectories to dual channel scattering pictures, but redraw the plot and both channel sketches in TikZ so the notes can present them clearly and consistently.
- Keep the screenshot next to the TikZ redraw for `lecture_01_figure_02.png`, because what matters is not only the objects themselves but also the fact that Susskind placed the Regge plot and the two channels on the same board as one conceptual cluster.
- For `lecture_01_figure_04.png`, normalize the notation to one convention, preferably \(P_z\) and \(p_\perp^2=p_x^2+p_y^2\), then typeset the cleaned large-\(P_z\) expansion and the many-particle energy formula as displayed math.
- For `lecture_01_figure_05.png`, make the interpretive step explicit in print: the conserved \(\sum_i P_{zi}\) term may be dropped as an additive constant, leaving the transverse Hamiltonian \(H\); keep the screenshot nearby because it shows this step happening on the board rather than being imposed later.
- For `lecture_01_figure_06.png`, present the derivation in two stages: first the discrete chain with kinetic and Hooke-law terms, then the continuum replacement \(\sum_i\to\int d\sigma\) and \(X_i-X_{i+1}\to \partial_\sigma X\); the screenshot should stay because the visible arrow and vertical staging carry the derivational logic.
- In all algebra-heavy cases, prefer a cautious cleaned reconstruction over literal board typography: preserve structure and meaning, but do not copy uncertain coefficients or index choices unless they are actually legible or transcript-supported.

## Uncertainties
- In `lecture_01_figure_02.png`, the vertical-axis label is not legible enough to fix the exact symbol from the image alone, though the lecture context strongly suggests angular momentum or spin.
- In `lecture_01_figure_02.png`, the particle labels on the channel sketches are faint, and the rightmost sketch is cropped at the edge, so only the topology is visually secure.
- In `lecture_01_figure_04.png`, the upper square-root expression is truncated on the right, and the board alternates between something that looks like \(P_3\) and something that looks like \(P_z\).
- In `lecture_01_figure_04.png` and `lecture_01_figure_05.png`, the exact scope of the summation signs relative to the transverse and mass terms is not fully legible from the image alone.
- In `lecture_01_figure_05.png`, the left part of \(i\,\partial/\partial t = H\) is partially cropped, so the full operator identity should be treated as cautious reconstruction rather than fully visible board text.
- In `lecture_01_figure_06.png`, the lower continuum integrand is still being written and does not stably display every exponent or coefficient; the derivative-squared structure is supported, but the fully normalized continuum formula is not purely image-legible.
- In `lecture_01_figure_06.png`, the coefficient choices appear to have been absorbed by convention during the lecture, so the notes should preserve the form of the derivation without overclaiming exact board-normalized prefactors.