# Visual Evidence
## Frame Inventory
- `lecture_10_figure_02.png`: Sparse introductory board with component notation for the magnetic field, \(\nabla\!\cdot\!\mathbf B=0\), and \(\mathbf B=\nabla\times\mathbf A\); this screenshot should remain in the final notes because it cleanly captures the lecture’s pivot to the vector potential.
- `lecture_10_figure_03.png`: Top-of-board one-line magnetic Lagrangian with the kinetic term and the explicit component form of \(\mathbf A\cdot\dot{\mathbf x}\), plus an irrelevant stray chalk stroke below; this screenshot should remain because it preserves the board layout of the interaction term.
- `lecture_10_figure_04.png`: Mid-derivation board showing the Euler–Lagrange relation, the canonical momentum definition, and the expanded time derivative of \(A_x(\mathbf x)\) along the trajectory; this screenshot should remain because it anchors the transition from Lagrangian formalism to canonical momentum.
- `lecture_10_figure_05.png`: More finished \(x\)-component force-law derivation, with bracketed derivative combinations of the vector potential and the simplified magnetic-field form; this screenshot should remain because it is the clearest visual evidence for the emergence of the Lorentz-force combination.
- `lecture_10_figure_06.png`: Left-side list of the three canonical momentum components and a newly started Hamiltonian line \(H=\sum_i p_i\) on an otherwise blank board; this screenshot should remain because it records the live transition into the Hamiltonian construction.

## Equation Extraction
- `lecture_10_figure_02.png`: `\(B_i(x)\)` together with the visible component labels `\(B_x\)`, `\(B_y\)`, `\(B_z\)` [visible]
- `lecture_10_figure_02.png`: `\(\nabla\cdot \mathbf B = 0\)` [visible]
- `lecture_10_figure_02.png`: `\(\mathbf B=\nabla\times\mathbf A\)` [visible]

- `lecture_10_figure_03.png`: `\(L=\frac{1}{2}m\left(\dot x^2+\dot y^2+\dot z^2\right)+\frac{e}{c}\left(A_x\dot x+A_y\dot y+A_z\dot z\right)\)` [partially visible]
- `lecture_10_figure_03.png`: the left curved chalk stroke below the main equation appears non-mathematical and should not be transcribed as a formula [visible]

- `lecture_10_figure_04.png`: `\(\dot p_x=\frac{\partial L}{\partial x}\)` [partially visible]
- `lecture_10_figure_04.png`: `\(p_x=\frac{\partial L}{\partial \dot x}=m\dot x+\frac{e}{c}A_x(x)\)` [partially visible]
- `lecture_10_figure_04.png`: `\(m\ddot x+\frac{e}{c}\left(\frac{\partial A_x}{\partial x}\dot x+\frac{\partial A_x}{\partial y}\dot y+\frac{\partial A_x}{\partial z}\dot z\right)\)` [partially visible]

- `lecture_10_figure_05.png`: `\(m a_x=\frac{e}{c}\left[\left(-\frac{\partial A_x}{\partial y}+\frac{\partial A_y}{\partial x}\right)\dot y+\left(\frac{\partial A_z}{\partial x}-\frac{\partial A_x}{\partial z}\right)\dot z\right]\)` [standard completion]
- `lecture_10_figure_05.png`: `\(m a_x=\frac{e}{c}\left(B_z\dot y-B_y\dot z\right)\)` [visible]
- `lecture_10_figure_05.png`: `\(\frac{e}{c}(\mathbf v\times\mathbf B)_x\)` [visible]

- `lecture_10_figure_06.png`: `\(p_x=m\dot x+\frac{e}{c}A_x\)` [visible]
- `lecture_10_figure_06.png`: `\(p_y=m\dot y+\frac{e}{c}A_y\)` [visible]
- `lecture_10_figure_06.png`: `\(p_z=m\dot z+\frac{e}{c}A_z\)` [visible]
- `lecture_10_figure_06.png`: `\(H=\sum_i p_i\)` [partially visible]
- `lecture_10_figure_06.png`: `\(H=\sum_i p_i\dot x^i-L\)` [standard completion]

## Diagram Extraction
- `lecture_10_figure_02.png` is not a geometric diagram, but its three-line board structure should be preserved as a screenshot because the vertical layout matters: magnetic-field notation at top, the constraint in the middle, and the vector-potential cure below.
- `lecture_10_figure_03.png` is likewise not a diagram; its value lies in the long one-line display of the magnetic Lagrangian, so it should be preserved as a screenshot rather than redrawn.
- `lecture_10_figure_04.png` is a derivation-layout image, not a figure. It should be preserved as a screenshot because the vertical progression from \(\dot p_x=\partial L/\partial x\) to the expanded canonical-momentum formula is part of the lecture’s unfolding logic.
- `lecture_10_figure_05.png` should be preserved as a screenshot because the upper bracketed grouping and the lower magnetic-field recognition line form a meaningful algebraic layout that is better evidenced by the original board than by a stylized redraw.
- `lecture_10_figure_06.png` should be preserved as a screenshot because the mostly empty board is itself evidential: it shows that Susskind is only beginning the Hamiltonian construction.
- None of the extracted frames contains a true blackboard sketch that must be redrawn in TikZ.
- If the final chapter later adds a clean editorial TikZ schematic of uniform circular motion in a magnetic field, that would be a transcript-driven explanatory addition rather than a redraw of any visible frame in this set.

## Reconstruction Guidance
- Keep all five screenshots in the chapter near the relevant derivation steps; these are not decorative frames but evidence for board order and emphasis.
- For `lecture_10_figure_02.png`, typeset the clean equations \(\nabla\!\cdot\!\mathbf B=0\) and \(\mathbf B=\nabla\times\mathbf A\) beside the screenshot, while regularizing the top line only cautiously as component notation \(B_i(x)\), not as a more polished equation than the pixels justify.
- For `lecture_10_figure_03.png`, use the screenshot as evidence that Susskind writes the interaction explicitly in components, then typeset the note-quality version
  \[
  L=\frac{1}{2}m(\dot x^2+\dot y^2+\dot z^2)+\frac{e}{c}(A_x\dot x+A_y\dot y+A_z\dot z),
  \]
  or equivalently \(\frac{e}{c}\mathbf A\cdot\dot{\mathbf x}\).
- For `lecture_10_figure_04.png`, preserve the screenshot and pair it with a cleaned derivation block showing the canonical momentum and the \(x\)-component Euler–Lagrange setup. The screenshot matters because it records the lecture’s board progression, but the typeset equations should remove cropped clutter.
- For `lecture_10_figure_05.png`, preserve the screenshot and present a cleaned aligned derivation beside it, since the board evidence is strongest for the lower line and the bracketed grouping but weaker at the left edge of the upper line. This is a case where the screenshot and the cleaned equation should be shown together.
- For `lecture_10_figure_06.png`, treat the screenshot as staging evidence and reconstruct the full Hamiltonian definition from the transcript rather than from direct legibility. The visible board only securely supports the momentum list and the opening \(H=\sum_i p_i\).
- Do not infer extra steps from the screenshots alone. Where a line is only half visible, use the transcript and standard mechanics notation to complete it conservatively, and mark that completion as a reconstruction rather than a direct reading.

## Uncertainties
- In `lecture_10_figure_02.png`, the top line is not fully secure as an equation; the notation \(B_i(x)\) and the component labels are clear, but the exact punctuation or equality relation among them is not.
- In `lecture_10_figure_03.png`, the far-right end of the coupling term is near the image boundary, so the completion to \(A_z\dot z\) is strongly plausible but not equally sharp at the pixel level.
- In `lecture_10_figure_04.png`, the top relation is cramped enough that the precise subscript and derivative variable should be checked against the transcript before typesetting.
- In `lecture_10_figure_04.png`, the visible \(A_x(x)\) notation may just be shorthand for \(A_x(\mathbf x)\); the frame alone does not settle whether the argument is scalar \(x\) or full position \(\mathbf x\).
- In `lecture_10_figure_05.png`, the left side of the upper bracketed formula is partly cropped, so the full derivative combination must be regularized from the transcript and standard curl identities.
- In `lecture_10_figure_05.png`, Susskind’s own sign-checking in the transcript warns that the final vector-identification step should be normalized carefully to the convention \((\mathbf v\times\mathbf B)_x=v_yB_z-v_zB_y\).
- In `lecture_10_figure_06.png`, the visible Hamiltonian line stops too early to support the full formula directly; only the beginning \(H=\sum_i p_i\) is truly image-backed.
- The transcript near the Hamiltonian transition briefly mislabels the canonical-momentum list as “the Hamiltonian,” so the final note-quality reconstruction must silently correct that mismatch.