# Figure Notes
## Image Inventory
- `lecture_08_figure_02.png` shows the right half of the classical-mechanics board: several curved arrowed flow lines on the left side of the frame, a short horizontal axis labeled `x` below, and on the right the Hamiltonian written as a function of `x` and `p` together with the explicit example `p^2/2m + U(x)`. Susskind’s arm and finger point toward the kinetic term.
- `lecture_08_figure_03.png` shows a wider board state from the polarization example: on the left are ket labels paired with energies, on the right are two Hamiltonian eigenvalue equations for `|x\rangle` and `|y\rangle`, and below is a partially obscured expression for `|\psi(t)\rangle` as a two-component state with entries involving `\alpha(t)` and `\beta(t)`.
- `lecture_08_figure_04.png` shows a clean, isolated equation on an otherwise blank board: the ket time-evolution equation with a dotted `\psi` on the left and `-iH|\psi\rangle` on the right.
- `lecture_08_figure_05.png` shows Susskind in front of a board carrying an intermediate bra-ket manipulation: the left part of a matrix-element expression `\langle\psi|\hat K|\dot\psi\rangle` is visible across the top, a vertical `d/dt` appears on the left, and the right-hand side is partly blocked by Susskind’s body and arm.

## Blackboard Equations
- `lecture_08_figure_02.png`: `\frac{p^2}{2m}+U(x)` [visible]
- `lecture_08_figure_02.png`: `H(x\,p)` or `H(x,p)` [partially visible]
- `lecture_08_figure_02.png`: `x` [visible]
- `lecture_08_figure_02.png`: `H(x,p)=\frac{p^2}{2m}+U(x)` [standard reconstruction]

- `lecture_08_figure_03.png`: `|y\rangle` [visible]
- `lecture_08_figure_03.png`: `E_2` [visible]
- `lecture_08_figure_03.png`: `|x\rangle` [visible]
- `lecture_08_figure_03.png`: `E_1` [visible]
- `lecture_08_figure_03.png`: `H|x\rangle = E_1|x\rangle` [partially visible]
- `lecture_08_figure_03.png`: `H|y\rangle = E_2|y\rangle` [partially visible]
- `lecture_08_figure_03.png`: `|\psi(t)\rangle =` [partially visible]
- `lecture_08_figure_03.png`: `\alpha(t)` [partially visible]
- `lecture_08_figure_03.png`: `\beta(t)` [partially visible]
- `lecture_08_figure_03.png`: `|\psi(t)\rangle=\begin{pmatrix}\alpha(t)\\ \beta(t)\end{pmatrix}` [standard reconstruction]

- `lecture_08_figure_04.png`: `|\dot{\psi}\rangle=-iH|\psi\rangle` [visible]

- `lecture_08_figure_05.png`: `\langle\psi|\hat K|\dot{\psi}\rangle` [visible]
- `lecture_08_figure_05.png`: `\frac{d}{dt}` [visible]
- `lecture_08_figure_05.png`: a continuation to the right of the equals sign, consistent with a second bra-ket term in the product rule [partially visible]
- `lecture_08_figure_05.png`: `\frac{d}{dt}\langle\psi|\hat K|\psi\rangle=\langle\psi|\hat K|\dot{\psi}\rangle+\langle\dot{\psi}|\hat K|\psi\rangle` [standard reconstruction]

## Diagram And Layout Reading
- `lecture_08_figure_02.png` is not just an equation crop. The left side contains a small flow-line sketch with several curved arrows, evidently part of the phase-space discussion, while the right side gives the concrete Hamiltonian example. The layout matters: sketch on the left, formula on the right, and the pointing hand tying the derivative-with-respect-to-momentum discussion to the kinetic term.
- In `lecture_08_figure_02.png`, only the `x` label is plainly visible; the complementary axis label is not visible in the crop. Any redraw should therefore remain schematic rather than pretending to recover a full axis system from the image alone.
- `lecture_08_figure_03.png` preserves a multi-part board organization. The left board lists the polarization basis states and their energies; the right board writes the Hamiltonian acting on those basis states; the lower region transitions to the explicit time-dependent state vector. That arrangement is useful evidence for the lecture’s movement from eigenstates to the Schrödinger evolution of a general polarization state.
- In `lecture_08_figure_03.png`, Susskind’s paper blocks part of the lower expression. The image is still valuable because it documents how the board joins the eigenvalue equations to the `\psi(t)` column-vector representation.
- `lecture_08_figure_04.png` is visually simple and centered. It is best read as a clean board snapshot of the ket Schrödinger equation after setting `\hbar=1`, just before he introduces the corresponding bra equation.
- `lecture_08_figure_05.png` is mainly useful as layout evidence for the intermediate algebra. The visible top line shows one of the two product-rule terms, while the vertical `d/dt` on the left indicates that the larger expression concerns the time derivative of an expectation value. The board is not fully legible, but it clearly belongs to the derivation that leads to the commutator formula.

## TeX Reconstruction Plan
- `lecture_08_figure_02.png` should remain visible in the chapter. Near it, typeset the clean Hamiltonian
  `H(x,p)=\frac{p^2}{2m}+U(x)`
  and include a conservative TikZ redraw of the curved flow-line sketch with an `x` axis. The redraw should stay schematic, since the full axis structure is not visible.
- `lecture_08_figure_03.png` should remain visible. Near it, typeset the clean eigenvalue equations
  `H|x\rangle=E_1|x\rangle`, `H|y\rangle=E_2|y\rangle`
  and the state-vector form
  `|\psi(t)\rangle=\begin{pmatrix}\alpha(t)\\ \beta(t)\end{pmatrix}`.
  No TikZ redraw is needed; the value of the screenshot is the board layout joining these three ingredients.
- `lecture_08_figure_04.png` should remain visible as evidence for the ket time-evolution equation. A nearby displayed equation can reproduce it in the chapter’s house style:
  `|\dot{\psi}\rangle=-iH|\psi\rangle`.
  No redraw is needed.
- `lecture_08_figure_05.png` should remain visible only as supporting evidence for the intermediate product-rule step. The mathematics should be reconstructed nearby as clean LaTeX, not taken from the screenshot alone. The useful companion display is
  `\frac{d}{dt}\langle\psi|\hat K|\psi\rangle=\langle\psi|\hat K|\dot{\psi}\rangle+\langle\dot{\psi}|\hat K|\psi\rangle`,
  followed later by the commutator formula from the transcript.
- For all four figures, keep the screenshot close to the cleaned equation or schematic reconstruction so the reader can see what the board looked like while still reading a legible mathematical version.

## Caption Drafts
- `lecture_08_figure_02.png`: Classical Hamiltonian and flow-line sketch
- `lecture_08_figure_03.png`: Polarization energy eigenstates and time-dependent state
- `lecture_08_figure_04.png`: Ket form of the Schrödinger equation
- `lecture_08_figure_05.png`: Product-rule step toward the commutator formula

## Uncertainties
- In `lecture_08_figure_02.png`, the punctuation inside `H(x,p)` is not fully secure from the image; it looks like `H(x p)` in the handwriting, and the equality sign to the explicit formula is not visible in the crop.
- In `lecture_08_figure_02.png`, the left-hand sketch strongly suggests phase-space flow lines, but only the `x` label is clearly visible. The missing axis label should not be silently invented in a redraw.
- In `lecture_08_figure_03.png`, the lower `|\psi(t)\rangle` expression is partly hidden by Susskind’s paper, so the full column-vector form is best treated as transcript-backed standard reconstruction rather than direct transcription.
- In `lecture_08_figure_03.png`, the left-side ordering of `|x\rangle,|y\rangle` with `E_1,E_2` is visible but slightly cramped. The transcript is needed to confirm the intended pairing.
- In `lecture_08_figure_04.png`, the equation is clear, but whether the Hamiltonian was written with an explicit hat is not visible; the board only clearly shows `H`.
- In `lecture_08_figure_05.png`, the right-hand side of the top equation is significantly obscured, and the screenshot does not by itself yield a secure full transcription of the product-rule line.
- In `lecture_08_figure_05.png`, the visible vertical `d/dt` likely belongs to a larger derivative expression extending outside the crop. The full equation should therefore be reconstructed from the transcript, not from the screenshot alone.