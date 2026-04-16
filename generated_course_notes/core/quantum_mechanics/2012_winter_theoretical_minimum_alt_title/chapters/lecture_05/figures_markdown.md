# Figure Notes
## Image Inventory
- `lecture_05_figure_01.png`: Opening title-transition image over a Stanford courtyard. Large superimposed title letters dominate the frame; no lecturer, blackboard, or mathematical content is visible.
- `lecture_05_figure_02.png`: Medium shot of Susskind at the board during the simultaneous-measurability argument. The board shows the action of \(ML\) on \(|i\rangle\), intermediate scalar-pulling steps, and a lower concluding line that says \(LM|i\rangle\) gives the “same thing.”
- `lecture_05_figure_03.png`: Tight blackboard close-up of the difference-quotient step in the infinitesimal-time derivation. Only the equation is visible; no lecturer occlusion.
- `lecture_05_figure_04.png`: Tight blackboard close-up of the expectation-value evolution equation. The left-hand derivative, \(\langle L\rangle\), the factor \(-i\), and the commutator inside brackets are all visible.
- `lecture_05_figure_05.png`: Medium shot of Susskind in front of the board while returning to the energy-eigenvector expansion of the state. The top line identifies \(|i\rangle\) with \(|E_i\rangle\), and a lower line writes the state as a sum over basis vectors with time-dependent coefficients.
- `lecture_05_figure_06.png`: Wide blackboard shot for the spin-in-a-magnetic-field example. It shows an upward arrow labeled \(B_z\), a second slanted arrow, the Hamiltonian \(H=\omega\sigma_z/2\), and a vertical list \(\sigma_x,\sigma_y,\sigma_z\).

## Blackboard Equations
- `lecture_05_figure_02.png`: \(ML|i\rangle = M\,l_i|i\rangle\) [visible]
- `lecture_05_figure_02.png`: \(= l_i\,M|i\rangle\) [partially visible]
- `lecture_05_figure_02.png`: \(= l_i m_i |i\rangle\) [partially visible]
- `lecture_05_figure_02.png`: \(LM|i\rangle = \text{same thing}\) [partially visible]
- `lecture_05_figure_03.png`: \(\dfrac{|\psi(\epsilon)\rangle-|\psi(0)\rangle}{\epsilon}=-\,i\,H|\psi(0)\rangle\) [visible]
- `lecture_05_figure_04.png`: \(\dfrac{d}{dt}\langle L\rangle=-\,i\,\langle [L,H]\rangle\) [visible]
- `lecture_05_figure_05.png`: \(|i\rangle = |E_i\rangle\) [partially visible]
- `lecture_05_figure_05.png`: \(|\psi(t)\rangle = \sum_j \alpha_j(t)\,|j\rangle\) [partially visible]
- `lecture_05_figure_06.png`: \(H=\dfrac{\omega}{2}\sigma_z\) [visible]
- `lecture_05_figure_06.png`: \(\sigma_x\) [visible]
- `lecture_05_figure_06.png`: \(\sigma_y\) [visible]
- `lecture_05_figure_06.png`: \(\sigma_z\) [visible]

## Diagram And Layout Reading
- `lecture_05_figure_01.png` is not a lecture-board image at all; it is an opening visual transition and contributes no board layout evidence.
- `lecture_05_figure_02.png` preserves the proof-like layout of the commuting-operator argument: a top line applying \(ML\) to a common eigenvector, two scalar-reordering steps beneath it, and a lower line asserting that \(LM|i\rangle\) gives the same result. The important visual feature is not elegance but the staged blackboard logic.
- `lecture_05_figure_03.png` is purely algebraic. The horizontal fraction bar and isolated \(\epsilon\) underneath it visually emphasize the passage from finite difference to derivative.
- `lecture_05_figure_04.png` is also purely algebraic, but the layout is cleaner and more symmetrical: derivative on the left, expectation value in the middle, and the commutator expectation value on the right.
- `lecture_05_figure_05.png` shows a board organized around basis expansion. The top identification \(|i\rangle=|E_i\rangle\) sits above the lower expansion of the state. The rightmost \(|j\rangle\) is especially clear, while the lecturer obscures part of the summation.
- `lecture_05_figure_06.png` combines equation and sketch. The upward arrow labeled \(B_z\) marks the magnetic-field direction; the second slanted arrow is a suggestive classical-looking spin-direction sketch. The left column listing \(\sigma_x,\sigma_y,\sigma_z\) sets up the later time-evolution discussion of all three components.

## TeX Reconstruction Plan
- `lecture_05_figure_01.png` should not remain visible in the final chapter. It is an introductory title-transition image with no mathematical or diagrammatic value for the notes.
- `lecture_05_figure_02.png` should remain visible if the chapter keeps a visual beat for the theorem that simultaneous measurability implies commuting operators. Place a short displayed reconstruction nearby:
  \[
  ML|i\rangle=Ml_i|i\rangle=l_iM|i\rangle=l_im_i|i\rangle,
  \qquad
  LM|i\rangle=l_im_i|i\rangle.
  \]
  Then state the conclusion \(ML=LM\) on the common basis, hence on all vectors.
- `lecture_05_figure_03.png` should remain visible and be paired with the typeset difference quotient. A clean displayed equation should appear nearby, followed immediately by the limiting Schrödinger equation in prose or display.
- `lecture_05_figure_04.png` should remain visible and be paired with the fully typeset commutator equation for expectation values. No redraw is needed; the screenshot serves mainly as blackboard evidence for the sign, ordering, and average-value framing.
- `lecture_05_figure_05.png` should remain visible because it records the moment when the general solution is reassembled from the energy eigenbasis. Typeset the basis-identification line and the state expansion nearby, using the transcript to normalize notation to \(\alpha_j(t)\).
- `lecture_05_figure_06.png` should remain visible and should also be redrawn in a minimal TikZ schematic nearby. The redraw should include an upward axis labeled \(B_z\), a second slanted arrow to echo the board sketch, and the displayed Hamiltonian \(H=\omega\sigma_z/2\). Keep the screenshot as evidence of how Susskind visually organized the setup.

## Caption Drafts
- `lecture_05_figure_01.png`: Stanford University opening transition.
- `lecture_05_figure_02.png`: Common eigenvectors force \(LM\) and \(ML\) to agree.
- `lecture_05_figure_03.png`: Difference quotient on the way to Schrödinger evolution.
- `lecture_05_figure_04.png`: Expectation values evolve by a commutator with \(H\).
- `lecture_05_figure_05.png`: Expanding the state in the energy eigenbasis.
- `lecture_05_figure_06.png`: Magnetic field along \(z\) and the spin-component Hamiltonian.

## Uncertainties
- In `lecture_05_figure_02.png`, the lecturer blocks part of the intermediate steps. The lower line is visibly intended to say that \(LM|i\rangle\) gives the “same thing,” but the exact handwritten characters on the far left are not perfectly clear.
- In `lecture_05_figure_03.png`, the state symbol could be read as \(\Psi\) rather than \(\psi\). The transcript supports ordinary \(\psi\)-notation, but the handwriting itself is somewhat ambiguous.
- In `lecture_05_figure_04.png`, the commutator is written without a clearly visible comma; the image supports \([L,H]\) rather than any alternative, but the punctuation is purely interpretive.
- In `lecture_05_figure_05.png`, the coefficient symbol in the summation looks more like a handwritten \(q_j(t)\) than a clean \(\alpha_j(t)\). The transcript strongly supports \(\alpha_j(t)\), so the typeset notes should normalize to that.
- In `lecture_05_figure_05.png`, the left-hand side of the lower expansion is partly obscured by Susskind, and the full summation sign is not completely unobstructed.
- In `lecture_05_figure_06.png`, the slanted arrow is only a suggestive sketch, not a rigorously labeled vector diagram. It should be treated as atmosphere and layout evidence, not as a precise geometric object.
- In `lecture_05_figure_06.png`, the sign convention in \(H=\omega\sigma_z/2\) is a board-level convention for this lecture; the image alone does not encode the underlying physical sign choices that might arise from magnetic moment conventions.