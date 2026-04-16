# Figure Notes
## Image Inventory
- `lecture_07_figure_02.png`: Susskind stands at the left of a whiteboard section showing a basis-expansion formula for a state vector. The left side of the equation is partly blocked by his body, but the top line clearly has a summation, bras/kets, and a final ket factor. On the right, a lower label of the form `\Psi(a,b,c,\ldots)` is visible.
- `lecture_07_figure_03.png`: A clean vertical list of ket notation appears on an otherwise open whiteboard. The visible progression runs from single-subsystem kets to a composite ket `|a,b\rangle`, ending with a large general state ket `|\Psi\rangle`.
- `lecture_07_figure_04.png`: The right side of the board contains reduced-density-matrix algebra. A top line shows a sum over `b` built from starred and unstarred `\Psi` components. Below it is a summed matrix action on a component indexed by `a'`, with `\rho` carrying two indices. Some rightmost symbols are cut off or soft.
- `lecture_07_figure_06.png`: A multi-row horizontal sketch shows numbered trials or pairs, with circles labeled `1` and `2` at left and corresponding numbered circles at right. A central source marker `E` appears on the top row. Two right-side outcome labels are fully readable: `\sigma_z=+1` and `\sigma_x=-1`. A lower right-side outcome is being written but is blocked by Susskind.

## Blackboard Equations
- `lecture_07_figure_02.png`: $|\Psi\rangle = \sum_{a,b,\ldots}\langle a,b,\ldots|\Psi\rangle\,|a,b,\ldots\rangle$ [partially visible]
- `lecture_07_figure_02.png`: $\Psi(a,b,c,\ldots)$ [visible]
- `lecture_07_figure_02.png`: $\Psi(a,b,c,\ldots)=\langle a,b,c,\ldots|\Psi\rangle$ [standard reconstruction]
- `lecture_07_figure_02.png`: $|\Psi\rangle=\sum_{a,b,c,\ldots}\Psi(a,b,c,\ldots)\,|a,b,c,\ldots\rangle$ [standard reconstruction]

- `lecture_07_figure_03.png`: $|a\rangle$ [visible]
- `lecture_07_figure_03.png`: $|b\rangle$ [partially visible]
- `lecture_07_figure_03.png`: $|a,b\rangle$ [visible]
- `lecture_07_figure_03.png`: $|\Psi\rangle$ [visible]

- `lecture_07_figure_04.png`: $\rho_{a'a}=\sum_b \Psi_{a'b}^*\,\Psi_{ab}$ [partially visible]
- `lecture_07_figure_04.png`: $\sum_{a'} \rho_{aa'}\,\psi_{a'}$ [partially visible]
- `lecture_07_figure_04.png`: $\sum_{a'} \rho_{aa'}\,\psi_{a'}=\psi_a$ [standard reconstruction]

- `lecture_07_figure_06.png`: $\sigma_z=+1$ [visible]
- `lecture_07_figure_06.png`: $\sigma_x=-1$ [visible]
- `lecture_07_figure_06.png`: $\sigma_y=+1$ [standard reconstruction]

## Diagram And Layout Reading
- `lecture_07_figure_02.png`: The board is organized as a two-step definition. The upper line is the abstract basis expansion of the state vector; the lower right isolates the wavefunction as a function of basis labels. The image helps show that Susskind is moving from ket notation to coefficient notation, not yet doing a long derivation.
- `lecture_07_figure_03.png`: The layout is pedagogical rather than algebraic. The items are stacked vertically to show a progression from a subsystem ket to another subsystem ket, then to the tensor-product-style composite ket, and finally to the generic full state.
- `lecture_07_figure_04.png`: The visible board area is a compact algebra block on the right board. The top line defines reduced-density-matrix components by summing over Bob’s index; the next line turns that matrix into an operator acting on Alice’s column vector components. The left edge shows unrelated remnants from earlier board work and should not drive reconstruction.
- `lecture_07_figure_06.png`: The sketch is a row-by-row record of different measurement settings and outcomes across repeated entangled-pair trials. The circles label runs or particles, the horizontal lines track each run, and the central `E` marks the emission/source setup. The right margin is where measurement choices and results are being written.

## TeX Reconstruction Plan
- `lecture_07_figure_02.png` should remain visible. The screenshot captures the board rhythm of “state vector first, wavefunction second,” but the full formula should be typeset cleanly nearby as displayed equations for the basis expansion and the definition of $\Psi(a,b,c,\ldots)$.
- `lecture_07_figure_03.png` should remain visible. The point of this frame is the visual ladder of notation, so keep the screenshot and also reproduce the short ket list in typeset form nearby rather than replacing it with prose alone.
- `lecture_07_figure_04.png` should remain visible, but the mathematics should be reconstructed in clean display math next to it. The board evidence is useful for order and emphasis, while the indices and right-hand side are too soft to rely on without a careful typeset reconstruction.
- `lecture_07_figure_06.png` must remain visible and should be paired with a small TikZ redraw. The screenshot preserves the authentic board layout and the fact that the third label is being written in real time; the TikZ should only clarify the repeated-pair layout and complete the transcript-supported lower label $\sigma_y=+1$.

## Caption Drafts
- `lecture_07_figure_02.png`: State vector expanded in a labeled basis
- `lecture_07_figure_03.png`: From subsystem kets to the composite state ket
- `lecture_07_figure_04.png`: Reduced density matrix acting on Alice components
- `lecture_07_figure_06.png`: Example Bell-pair measurement outcomes across runs

## Uncertainties
- `lecture_07_figure_02.png`: The exact bra label string inside the summand is blurry, and the left side of the top equation is partially blocked by Susskind. The coefficient interpretation is clear, but the full formula should be treated as a cautious standard completion.
- `lecture_07_figure_03.png`: The second single-subsystem ket is soft enough that only its role is certain, not every character. `|a,b\rangle` and `|\Psi\rangle` are the safest readable anchors.
- `lecture_07_figure_04.png`: The order of indices on $\rho$ and the fully visible right-hand side of the matrix-action equation are not perfectly legible in the frame. The transcript strongly supports the standard pure-state reconstruction $\sum_{a'}\rho_{aa'}\psi_{a'}=\psi_a$.
- `lecture_07_figure_06.png`: The lower outcome being written is not readable from the image itself. Using $\sigma_y=+1$ is justified by the aligned subtitle window, but no further unseen labels or geometry should be invented.