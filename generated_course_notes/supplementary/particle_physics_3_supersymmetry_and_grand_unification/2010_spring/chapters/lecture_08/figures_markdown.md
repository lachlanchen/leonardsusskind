# Figure Notes
## Image Inventory
- `lecture_08_figure_02.png`: Tight whiteboard crop from the early Dirac-helicity discussion. On the right Susskind is writing the Hamiltonian as \(H=\sigma\cdot p\). On the left the board still retains the local setup for a chiral two-component spinor, including the label “Chiral” and a partially visible \(\psi\)-spinor notation.
- `lecture_08_figure_03.png`: Wide board shot from the supersymmetric Lagrangian construction. The board contains several stacked lines of component algebra with brackets, derivatives, \(\phi,\psi,F\)-type fields, and a lower line ending in the identification of the ordinary Lagrangian on the far right.
- `lecture_08_figure_04.png`: Close crop of the right-hand end of the same component-Lagrangian discussion. The visible line includes a fermionic derivative term, an auxiliary-field product \(F^\ast(x)F(x)\), and a final equality into the Lagrangian notation. At lower left there is also a small dashed chalk sketch consistent with the nearby discussion of the trivial \(F\)-propagator/contact behavior.

## Blackboard Equations
- `lecture_08_figure_02.png`: \(\text{Chiral}\) [visible]
- `lecture_08_figure_02.png`: \(\psi=\begin{pmatrix}\psi_1\\ \psi_2\end{pmatrix}\) [partially visible]
- `lecture_08_figure_02.png`: \(\psi_\alpha\) [partially visible]
- `lecture_08_figure_02.png`: \(H=\sigma\cdot\) [visible]
- `lecture_08_figure_02.png`: \(H=\boldsymbol{\sigma}\cdot\mathbf{p}\) [standard reconstruction]

- `lecture_08_figure_03.png`: \(\phi(x)\), \(\psi(x)\), \(F(x)\) [visible]
- `lecture_08_figure_03.png`: \(\dfrac{\partial^2}{\partial x^2}\phi\) [partially visible]
- `lecture_08_figure_03.png`: \(\dfrac{\partial \bar\psi}{\partial x}\,\sigma^\mu_{\alpha\beta}\psi_\beta\) [partially visible]
- `lecture_08_figure_03.png`: \(F^\ast(x)F(x)\) [visible]
- `lecture_08_figure_03.png`: \(F^\ast(x)F(x)=\mathcal{L}\) [partially visible]
- `lecture_08_figure_03.png`: \(\mathcal{L}\sim \phi^\ast \Box \phi+\bar\psi\,\sigma^\mu\partial_\mu\psi+F^\ast F\) [standard reconstruction]

- `lecture_08_figure_04.png`: \(\dfrac{\partial \bar\psi}{\partial x}\,\sigma^\mu_{\alpha\beta}\psi_\beta + F^\ast(x)F(x)\) [partially visible]
- `lecture_08_figure_04.png`: \(F^\ast(x)F(x)\) [visible]
- `lecture_08_figure_04.png`: \(=\mathcal{L}\) [partially visible]
- `lecture_08_figure_04.png`: \(F^\ast=0,\qquad F=0\) [standard reconstruction]
- `lecture_08_figure_04.png`: \(\mathcal{L}\supset F^\ast F\) [standard reconstruction]

## Diagram And Layout Reading
- `lecture_08_figure_02.png` is primarily board-layout evidence rather than a finished equation plate. Its value is that it preserves the local transition from the chiral two-component spinor setup on the left to the new Hamiltonian statement on the right. This is exactly the moment when Susskind turns from chirality/helicity language to \(H=\sigma\cdot p\).
- `lecture_08_figure_03.png` has a useful three-zone organization. The upper region holds the superfield-product/setup line, the middle region works through bracketed component expressions, and the lower region gathers the ordinary component terms that will become the Lagrangian. That board organization is useful evidence for how the lecture unfolds the superspace calculation into familiar component physics.
- `lecture_08_figure_04.png` is not just a tighter duplicate of the previous frame. It isolates the right-hand end of the lower line, where the auxiliary-field term \(F^\ast F\) sits next to the Lagrangian identification. That makes it the best documentary close-up for the later point that this term has no derivatives and therefore no ordinary propagating degree of freedom.
- `lecture_08_figure_04.png` also includes a small dashed chalk sketch at lower left. It is not a full diagram with axes, but it looks like a local propagator/contact doodle tied to the discussion of the trivial \(F\)-field propagator. This is secondary to the equation, but it is worth noting if the notes later mention the delta-function/contact character of the auxiliary field.

## TeX Reconstruction Plan
- `lecture_08_figure_02.png` should remain visible in the section where the lecture introduces the massless chiral Hamiltonian. Pair it with a clean displayed equation
  \[
  H=\boldsymbol{\sigma}\cdot\mathbf{p},
  \]
  and a short sentence explaining that this is the helicity Hamiltonian for the two-component chiral field. The screenshot should be kept because it preserves the chiral-spinor context on the same board.
- `lecture_08_figure_03.png` should remain visible in the section where the superfield product is converted into the ordinary component Lagrangian. Nearby, reconstruct the mathematics as a cleaned aligned display rather than as a literal character-by-character transcription, because the board is dense and partly obstructed. The safest nearby typeset form is a transcript-stabilized component Lagrangian schematic, for example the scalar term, the fermionic kinetic term, and the auxiliary-field term collected into one displayed line.
- `lecture_08_figure_04.png` should remain visible near the paragraph where Susskind emphasizes that the \(F\)-term is “extremely trivial” because it has no derivatives. Pair it with a short displayed equation isolating
  \[
  \mathcal{L}\supset F^\ast F
  \]
  and then, if the notes discuss the Euler–Lagrange consequence explicitly, with the algebraic equation of motion \(F=0\) in the free case. This screenshot works best as a close-up supporting figure rather than as a replacement for the wider board shot.
- No mandatory TikZ redraw is needed for `lecture_08_figure_02.png` or `lecture_08_figure_03.png`.
- For `lecture_08_figure_04.png`, a small optional TikZ redraw could be added only if the final chapter explicitly discusses the auxiliary-field propagator as a contact or delta-function object. If added, it should be clearly marked as a pedagogical redraw, not as a transcription of a precise board diagram.

## Caption Drafts
- `lecture_08_figure_02.png`: Chiral-spinor setup and the Hamiltonian \(H=\sigma\cdot p\)
- `lecture_08_figure_03.png`: Component expansion leading to the ordinary Lagrangian
- `lecture_08_figure_04.png`: Auxiliary-field term in the simple supersymmetric Lagrangian

## Uncertainties
- In `lecture_08_figure_02.png`, the final momentum symbol is partly covered by Susskind’s hand. The transcript securely resolves the intended statement as “Hamiltonian is Sigma dot P,” so the cleaned nearby equation should use \(H=\boldsymbol{\sigma}\cdot\mathbf{p}\), while the image itself should be treated as partial board evidence.
- In `lecture_08_figure_02.png`, the left-side spinor notation is only partly visible. The presence of a chiral two-component \(\psi\) is clear, but the exact arrangement of \(\psi_1,\psi_2\) and \(\psi_\alpha\) should not be overclaimed from the frame alone.
- In `lecture_08_figure_03.png`, the upper and middle lines are dense and partly blocked by the lecturer. The broad structure of the calculation is secure, but the exact placements of stars, indices, and derivatives on every term are not fully recoverable from the image alone.
- In `lecture_08_figure_03.png`, the rightmost symbol is best read as the ordinary Lagrangian notation, but whether the board is marking \(\mathcal{L}\) itself or speaking loosely of the integrated ordinary Lagrangian should be stabilized by the surrounding transcript.
- In `lecture_08_figure_04.png`, the auxiliary-field product \(F^\ast(x)F(x)\) is clear, but the full left-hand kinetic terms are cropped and should be reconstructed nearby from transcript context rather than claimed as fully image-derived.
- In `lecture_08_figure_04.png`, the small dashed sketch at lower left is incomplete. It likely supports the later propagator/contact discussion, but the frame alone does not fully settle whether it should be read as a propagator, a local contact symbol, or simply a partial chalk doodle from the ongoing explanation.