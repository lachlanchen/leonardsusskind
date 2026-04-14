# Figure Notes
## Image Inventory
- `lecture_07_figure_02.png`: A whiteboard frame centered on a large parenthesized matrix-style layout for an antisymmetric \(3\times 3\) object. The diagonal zeros are visible, the upper-triangular entries are labeled by \(C_3\), \(C_2\), and \(C_1\), and the component formulas are written next to them. Susskind is only at the far left edge, so the board organization is mostly unobstructed.
- `lecture_07_figure_03.png`: A whiteboard frame showing a clean vertical list of the three cross-product component identities, with Susskind leaning below the writing. This is a correction-and-summary style board moment rather than a matrix layout.
- `lecture_07_figure_05.png`: A whiteboard frame from the later relativistic-force discussion. The board is split into a left-hand force ansatz fragment and right-hand contracted equations, with Susskind turned away from the board. The key visible content is the antisymmetric-tensor force term and the zero-contraction argument.

## Blackboard Equations
- `lecture_07_figure_02.png`: \(C_3\) [visible]
- `lecture_07_figure_02.png`: \(A_1B_2-A_2B_1\) [visible]
- `lecture_07_figure_02.png`: \(C_2\) [visible]
- `lecture_07_figure_02.png`: \(A_1B_3-A_3B_1\) [visible]
- `lecture_07_figure_02.png`: \(C_1\) [visible]
- `lecture_07_figure_02.png`: \(A_2B_3-A_3B_2\) [visible]
- `lecture_07_figure_02.png`: several diagonal \(0\) entries in the matrix display [visible]
- `lecture_07_figure_02.png`: \(\mu=(0,\dots,3)\), \(m=(1,2,3)\) or equivalent index-range notes at the upper right [partially visible]

- `lecture_07_figure_03.png`: \(C_3=A_1B_2-A_2B_1\) [visible]
- `lecture_07_figure_03.png`: \(C_1=A_2B_3-A_3B_2\) [visible]
- `lecture_07_figure_03.png`: \(C_2=A_3B_1-A_1B_3\) [visible]

- `lecture_07_figure_05.png`: \(=q\,F^{\mu\nu}u_\nu\) [partially visible]
- `lecture_07_figure_05.png`: \(2\,\dfrac{du^\mu}{d\tau}u_\mu=0\) [standard reconstruction]
- `lecture_07_figure_05.png`: \(F^{\mu\nu}u_\nu u_\mu=0\) [visible]

## Diagram And Layout Reading
- `lecture_07_figure_02.png` is organized as a board-level translation between a vector cross product and an antisymmetric tensor. The matrix is not fully populated cell-by-cell; instead, the diagonal zeros and the upper-triangular symbolic entries are emphasized, with component formulas written beside the labels. This makes the pedagogical point visually: the cross product is being re-read as an antisymmetric tensor in three dimensions.
- In `lecture_07_figure_02.png`, the upper-right entry is labeled \(C_2\) at this stage, which reflects the temporary board identification that the lecture then corrects a few moments later. That temporal board logic matters and should not be flattened away.
- `lecture_07_figure_03.png` abandons the matrix view and turns to a clean three-line list. The layout is that of a correction or consolidation: each component \(C_3\), \(C_1\), \(C_2\) is written explicitly as a cyclic difference of products. This is the best readable board evidence for the corrected sign pattern.
- `lecture_07_figure_05.png` is arranged as a force-law argument split across the board. The left side carries the force ansatz built from \(F^{\mu\nu}\) and \(u_\nu\); the right side carries the orthogonality calculation showing that contraction with \(u_\mu\) vanishes. There are no diagrams, only board structure: ansatz on the left, consistency condition on the right.

## TeX Reconstruction Plan
- `lecture_07_figure_02.png` must remain visible in the notes. Its value is the original board layout: the large parenthesized antisymmetric matrix with the \(C_i\) labels placed into tensor slots. Nearby, the notes should reconstruct a clean antisymmetric \(3\times 3\) matrix in LaTeX or TikZ and explain that in three dimensions the cross product may be represented by such a tensor. Because the visible \(C_2\) placement is part of a temporary board step, the clean reconstruction should be normalized using the later correction rather than copied blindly.
- `lecture_07_figure_03.png` must also remain visible. It is the strongest board evidence for the corrected component identities, and nearby the notes should typeset the three displayed equations for \(C_3\), \(C_1\), and \(C_2\) exactly as the board presents them in cleaned LaTeX.
- `lecture_07_figure_05.png` should remain visible as evidence for the transition from the force ansatz to the orthogonality argument. Nearby, the notes should typeset the clean relativistic force ansatz and the contraction equations as displayed mathematics. This figure does not need TikZ; what matters is the equation flow from \(F^{\mu\nu}u_\nu\) to the vanishing contraction.
- For `lecture_07_figure_05.png`, the notes should silently normalize the index placement where needed, because the board is partially cropped and the transcript makes the intended contraction structure clearer than the image alone.

## Caption Drafts
- `lecture_07_figure_02.png`: Cross product written in antisymmetric-tensor form
- `lecture_07_figure_03.png`: Corrected component formulas for the cross product
- `lecture_07_figure_05.png`: Antisymmetric-tensor force ansatz and vanishing contraction

## Uncertainties
- In `lecture_07_figure_02.png`, the lower-left and lower-middle matrix entries are not fully secure from the image alone. The matrix is being used schematically, and not every slot is written with equal clarity.
- In `lecture_07_figure_02.png`, the upper-right slot is visibly labeled \(C_2\), but the transcript shows that this is a temporary identification that is corrected moments later to a minus sign. The clean notes should preserve the lecture rhythm while not freezing the temporary mistake as final mathematics.
- In `lecture_07_figure_02.png`, the small index-range note at the upper right is present but not fully crisp; it appears to distinguish Greek spacetime indices from Latin spatial indices.
- In `lecture_07_figure_03.png`, the top line is slightly cropped at the top edge, though the formula is still readable as \(C_3=A_1B_2-A_2B_1\).
- In `lecture_07_figure_05.png`, the left-hand equation is cropped on its left side; only the right-hand portion \(=q\,F^{\mu\nu}u_\nu\) is visibly secure from the frame.
- In `lecture_07_figure_05.png`, the upper contracted derivative line is not fully legible in its index placement. The transcript supports a normalized reconstruction of the zero-contraction relation, but the exact upstairs/downstairs placement should not be attributed solely to the image.
- In `lecture_07_figure_05.png`, the lower line \(F^{\mu\nu}u_\nu u_\mu=0\) is much more secure than the upper line and should carry the main mathematical weight if only one board equation from the image is emphasized.