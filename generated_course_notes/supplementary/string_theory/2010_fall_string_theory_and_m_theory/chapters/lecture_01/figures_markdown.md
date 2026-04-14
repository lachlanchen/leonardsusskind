# Figure Notes
## Image Inventory
- `lecture_01_figure_02.png`: Wide board shot with three linked visual elements. At left is a simple plot with a vertical axis, a horizontal axis labeled `m^2`, and a short rising sequence of points; above the middle is the handwritten word `Regge`. At center is a dashed-line interaction sketch with a vertical wavy internal segment. At right is a second dashed-line interaction sketch with a horizontal wavy segment and a large dashed arc.
- `lecture_01_figure_04.png`: Blackboard close-up from the light-cone/infinite-momentum discussion. The upper line shows a partially visible square-root expansion involving a large longitudinal momentum \(P_3\). The main line below begins with `E =` and a large \(\sum P_3\) term, followed by summed correction terms of the form transverse momentum squared and mass squared over longitudinal momentum.
- `lecture_01_figure_05.png`: Later board state from the same derivation. The left side now visibly identifies the energy expression with the Hamiltonian, with a partially cropped `i\,\partial/\partial t = H =` structure leading into the same summed light-cone energy formula. The upper square-root expansion remains faintly visible above.
- `lecture_01_figure_06.png`: Board shot from the open-string continuum-limit discussion. The upper half still contains remnants of the earlier Hamiltonian derivation, but the main new content is a discrete spring-chain energy formula, a term \(\frac{k}{2}(X_i-X_{i+1})^2\), an arrow to a continuum derivative term \(\left(\frac{\partial X}{\partial \sigma}\right)^2\), and a lower integral from \(0\) to \(\pi\) over \(\sigma\) with a kinetic term involving \(\dot X^2(\sigma)\).

## Blackboard Equations
- `lecture_01_figure_02.png`: \(m^2\) [visible]
- `lecture_01_figure_02.png`: \(\text{Regge}\) [visible]
- `lecture_01_figure_02.png`: angular momentum or spin on the vertical axis [standard reconstruction]
- `lecture_01_figure_02.png`: \(\pi\)- and \(\rho\)-type labels on the interaction sketches [partially visible]

- `lecture_01_figure_04.png`: \(P_3\sqrt{1+\dfrac{p_x^2+p_y^2+m^2}{P_3^2}}\) [partially visible]
- `lecture_01_figure_04.png`: \(E=\sum P_3+\sum \dfrac{p_\perp^2}{2P_z}+\sum \dfrac{m^2}{2P_z}\) [standard reconstruction]
- `lecture_01_figure_04.png`: \(\sum P_3\) [visible]
- `lecture_01_figure_04.png`: \(\dfrac{p_\perp^2}{2P_z}\) [partially visible]
- `lecture_01_figure_04.png`: \(\dfrac{m^2}{2P_z}\) [partially visible]

- `lecture_01_figure_05.png`: \(i\frac{\partial}{\partial t}=H\) [partially visible]
- `lecture_01_figure_05.png`: \(H=\sum_i\left(\dfrac{p_{\perp i}^2}{2P_{zi}}+\dfrac{m_i^2}{2P_{zi}}\right)\) [standard reconstruction]
- `lecture_01_figure_05.png`: \(H=\) [visible]
- `lecture_01_figure_05.png`: \(P_3\sqrt{1+\dfrac{p_x^2+p_y^2+m^2}{P_3^2}}\) [partially visible]

- `lecture_01_figure_06.png`: \(E=m\sum_i \dfrac{\dot X_i^2}{2}+\dfrac{k}{2}(X_i-X_{i+1})^2\) [partially visible]
- `lecture_01_figure_06.png`: \((X_i-X_{i+1})^2 \rightarrow \left(\dfrac{\partial X}{\partial \sigma}\right)^2\) [partially visible]
- `lecture_01_figure_06.png`: \(\int_0^\pi d\sigma\) [visible]
- `lecture_01_figure_06.png`: \(\dfrac{\dot X^2(\sigma)}{2}\) [partially visible]
- `lecture_01_figure_06.png`: \(\left(\dfrac{\partial X}{\partial \sigma}\right)^2\) [visible at upper right, standard completion in the lower integral]

## Diagram And Layout Reading
- `lecture_01_figure_02.png` is organized as a left-to-right conceptual board. The left panel is a Regge-style plot: a nearly vertical axis, a shallow horizontal axis labeled \(m^2\), and a short ascending sequence of points. The middle and right panels are two channel pictures for meson scattering. The middle sketch reads like an annihilation/recreation diagram with dashed external legs and a vertical wavy exchanged state; the right sketch reads like the crossed-channel version with a horizontal wavy exchange and a large dashed arc. The board layout itself matters because the lecture is moving from Regge trajectories to dual channel pictures.
- `lecture_01_figure_04.png` is not a geometric diagram but a two-level algebra board. The upper line is the single-particle square-root expression expanded for large \(P_3\); the lower, larger line is the many-particle energy decomposition into a huge conserved \(\sum P_3\) term plus small transverse and mass corrections. The visual hierarchy is pedagogically important: top line for the expansion trick, main line for the Hamiltonian-like result.
- `lecture_01_figure_05.png` preserves the next pedagogical step in the same derivation. What matters visually is that the energy formula has now been re-read as the Hamiltonian and tied to time evolution through the partially visible \(i\,\partial/\partial t = H\) structure. This is less about new algebra than about reinterpretation.
- `lecture_01_figure_06.png` is vertically staged. The upper new line gives the discrete chain energy with kinetic and spring terms; the arrow at the right converts the nearest-neighbor difference into a \(\sigma\)-derivative; the lower line converts the sum into \(\int_0^\pi d\sigma\) and begins the continuum Hamiltonian. The layout mirrors the lecture’s logic: discrete masses and springs first, then continuum limit, then derivative language.

## TeX Reconstruction Plan
- `lecture_01_figure_02.png` must remain visible. Its value is not only the individual symbols but the board-wide juxtaposition of the Regge plot and the two channel sketches. Nearby, the notes should include a clean TikZ reconstruction of:
  - a simple Regge-trajectory plot with angular momentum versus \(m^2\),
  - the two scattering-channel/topology sketches with dashed external legs and wavy exchanged states.
  The screenshot should remain as evidence for the original board layout and hand-drawn topology.
- `lecture_01_figure_04.png` must remain visible. Nearby, the notes should typeset the cleaned large-\(P_z\) expansion and the many-particle energy decomposition in displayed math. No TikZ is needed.
- `lecture_01_figure_05.png` must remain visible. It should be paired with a clean displayed equation making explicit the Hamiltonian/time-evolution identification,
  \[
  i\frac{\partial}{\partial t}=H,
  \qquad
  H=\sum_i\left(\frac{p_{\perp i}^2}{2P_{zi}}+\frac{m_i^2}{2P_{zi}}\right),
  \]
  while noting in prose that the large \(\sum_i P_{zi}\) term can be dropped as a conserved additive constant.
- `lecture_01_figure_06.png` must remain visible. Nearby, the notes should reconstruct the discrete-to-continuum passage in displayed mathematics:
  \[
  E \sim \sum_i \left(\frac{m}{2}\dot X_i^2+\frac{k}{2}(X_i-X_{i+1})^2\right)
  \]
  and
  \[
  E \sim \int_0^\pi d\sigma\left(\frac{\dot X^2(\sigma)}{2}+\left(\frac{\partial X}{\partial \sigma}\right)^2\right),
  \]
  with coefficients normalized cautiously to the transcript. No TikZ is needed; the key visual evidence is algebraic board flow rather than geometry.

## Caption Drafts
- `lecture_01_figure_02.png`: Regge trajectory and dual scattering sketches
- `lecture_01_figure_04.png`: Large-\(P_z\) expansion of the relativistic energy
- `lecture_01_figure_05.png`: Hamiltonian form of the light-cone energy
- `lecture_01_figure_06.png`: Discrete string energy and continuum \(\sigma\)-derivative limit

## Uncertainties
- In `lecture_01_figure_02.png`, the vertical-axis label on the Regge plot is not legible in the frame; the transcript indicates angular momentum or spin, but the board itself does not secure the exact handwritten symbol.
- In `lecture_01_figure_02.png`, the external-leg labels on the interaction sketches are faint, and the rightmost sketch is partially cropped at the frame edge. The topology is reliable; the exact particle labels should be normalized from the transcript.
- In `lecture_01_figure_04.png`, the upper square-root line is truncated on the right, and the board notation alternates between \(P_3\) and what may be read as \(P_z\). The cleaned notation should be standardized in the notes.
- In `lecture_01_figure_04.png` and `lecture_01_figure_05.png`, the exact placement of the summation sign relative to the transverse and mass terms is not completely secure from the board alone; the transcript supports the intended summed many-particle expression.
- In `lecture_01_figure_05.png`, the leftmost `i\,\partial/\partial t` is partially cropped and faint. The Hamiltonian identification is clear, but the full operator equation should be reconstructed cautiously.
- In `lecture_01_figure_06.png`, the lower continuum integral is still in-progress handwriting. The potential term in the lower line does not fully display the square in a stable way, even though the top-right replacement and the spoken lecture make \(\left(\partial X/\partial \sigma\right)^2\) the intended result.
- In `lecture_01_figure_06.png`, the coefficient normalization in going from the discrete chain to the continuum expression is not fully recoverable from the board alone; the lecture explicitly says he has absorbed constants, so the final notes should preserve the structural form rather than pretend the coefficients are all visually fixed.