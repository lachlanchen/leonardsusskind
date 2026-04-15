# Figure Notes
## Image Inventory
- `lecture_09_figure_02.png`: Susskind stands at the far left edge of the frame while the board is mostly unobstructed. At upper left the board shows the \(x\)-component notation for a cross product, and at upper right it shows the corresponding component formula. To the right-middle there is a hand-drawn \(3\times 3\) array-like sketch with zeros on the diagonal and matched off-diagonal entries, used to visualize antisymmetry and the count of independent components.
- `lecture_09_figure_03.png`: Susskind stands to the right of a mostly clean board. At upper left is the vector-potential definition of the magnetic field, and below it is a gauge-shift equation for the vector potential. The board is sparse, and the main value of the frame is the paired layout of those two equations.
- `lecture_09_figure_05.png`: Susskind is writing on the board. The left side shows the action written as a symbol \(A\) followed by an equals-or-colon mark and an integral sign; the far right shows \(dt\). The middle integrand is only partly formed, so the frame captures the live construction of the action formula rather than a fully finished equation.

## Blackboard Equations
- `lecture_09_figure_02.png`: \((\mathbf V \times \mathbf A)_x\) [visible]
- `lecture_09_figure_02.png`: \(V_y A_z - V_z A_y\) [visible]
- `lecture_09_figure_02.png`: a \(3\times 3\) antisymmetric matrix pattern with diagonal zeros and opposite off-diagonal entries [standard reconstruction]
- `lecture_09_figure_02.png`: \(M_{ij}=-M_{ji}\) [standard reconstruction]

- `lecture_09_figure_03.png`: \(\vec B=\nabla\times\vec A\) [visible]
- `lecture_09_figure_03.png`: \(\vec A+\nabla s=\vec A'\) [visible]

- `lecture_09_figure_05.png`: \(A=\int \cdots\,dt\) [partially visible]
- `lecture_09_figure_05.png`: \(A=\int L\,dt\) [standard reconstruction]

## Diagram And Layout Reading
- `lecture_09_figure_02.png` is valuable less as a polished equation frame than as a board-layout frame. The left and right top lines isolate one explicit component of the cross product, while the right-middle sketch turns the cross product into an antisymmetric \(3\times 3\) object. The diagonal entries are marked as zero; the lower-half entries are visually indicated as sign-opposites of the upper-half entries. The doodled circles in some cells appear to be mnemonic marks rather than mathematical symbols and should not be transcribed literally.
- `lecture_09_figure_03.png` has a very clean two-line organization. The upper line states that the magnetic field is the curl of the vector potential; the lower line states the gauge transformation. This sparse arrangement is itself useful evidence because the lecture is emphasizing the ambiguity of \(A\) before moving into Lagrangians and Hamiltonians.
- `lecture_09_figure_05.png` shows the action formula being staged across the width of the board: action symbol at left, integral sign in the center, time differential at far right. That spacing matters because it shows Susskind building the formula in time, not merely presenting a finished textbook statement. There is no useful geometric diagram here, but the board layout supports the narrative moment where the action is introduced.

## TeX Reconstruction Plan
- `lecture_09_figure_02.png` should remain visible. Nearby, the notes should typeset
  \[
  (\mathbf V\times \mathbf A)_x=V_yA_z-V_zA_y,
  \]
  and also reconstruct the antisymmetric-matrix idea cleanly, for example with a displayed matrix or compact statement \(M_{ij}=-M_{ji}\). The screenshot preserves the lecturer’s schematic way of counting components; the typeset math should provide the clean version.
- `lecture_09_figure_03.png` should remain visible. Nearby, the notes should typeset
  \[
  \vec B=\nabla\times \vec A,
  \qquad
  \vec A'=\vec A+\nabla s.
  \]
  No TikZ redraw is needed; the main value is the board’s sparse paired layout.
- `lecture_09_figure_05.png` should remain visible, but it should be paired with a clean displayed reconstruction of the action formula,
  \[
  A=\int L\,dt,
  \]
  or, if the chapter standardizes notation later, a brief note can explain that Susskind is using \(A\) for the action at this moment even though \(A\) also denotes the vector potential elsewhere. The screenshot is evidence of the live introduction; the typeset equation should carry the mathematical burden.

## Caption Drafts
- `lecture_09_figure_02.png`: Cross-product component and antisymmetric matrix sketch
- `lecture_09_figure_03.png`: Magnetic field as curl and gauge shift of the vector potential
- `lecture_09_figure_05.png`: Action written as an integral of the Lagrangian

## Uncertainties
- In `lecture_09_figure_02.png`, the entries inside the antisymmetric-matrix sketch are not literal algebraic symbols in every cell; some appear to be mnemonic doodles or quick sign markers. The mathematical content is the zero diagonal and the sign-opposed off-diagonal pairing, not the exact doodled marks.
- In `lecture_09_figure_02.png`, the left-hand notation is clearly the \(x\)-component of a cross product, but the vector letters are handwritten quickly and should be regularized in the notes as \(\mathbf V\) and \(\mathbf A\).
- In `lecture_09_figure_03.png`, the equation is fully legible, but the prime on \(\vec A'\) is written by hand and could be typeset either as \(\vec A'\) or by rearranging the equation to \(\vec A'=\vec A+\nabla s\) for clarity.
- In `lecture_09_figure_05.png`, the integrand is not yet legible from the image alone; only the action symbol, integral sign, and \(dt\) are visually secure. The completion to \(A=\int L\,dt\) relies on the nearby lecture narration.
- In `lecture_09_figure_05.png`, the symbol before the integral looks like \(A\) followed by a colon or hastily written equality sign. The notes should normalize this to a standard equality sign.