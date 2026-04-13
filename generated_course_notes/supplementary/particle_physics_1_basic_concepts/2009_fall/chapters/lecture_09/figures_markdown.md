# Figure Notes
## Image Inventory

- `lecture_09_figure_03.png`: A clean whiteboard shot showing the general functional form of the Lagrangian. The equation stretches across the top of the board and reads as a transition from explicit dependence on the field and its time/space derivatives to the compact relativistic notation with \(\partial_\mu \phi\). Susskind appears only at the lower-left edge and does not materially block the formula.
- `lecture_09_figure_04.png`: A tighter crop of the right half of the board during the scalar-field example. The top line shows the Euler-Lagrange field-equation structure, the middle line shows the scalar-field Lagrangian terms with the potential \(-V(\phi)\) clearly visible on the right, and the lower line begins the resulting field equation with second-derivative terms.
- `lecture_09_figure_05.png`: A board-only close-up with two lines of Dirac-field mathematics. The top line is the Dirac equation in one spatial dimension, written with \(\alpha\) and \(\beta\), and the lower line is a parenthesized Lagrangian expression built from \(\Psi^\dagger\), time and space derivative terms, and the mass term.
- `lecture_09_figure_06.png`: A medium shot of Susskind in front of the board during the QED interaction discussion. Behind him one can still see lines beginning with \(\Psi=\) and \(\Psi^\dagger=\), energy annotations for electron/positron operator pieces, a partially obscured interaction term beginning with \(e\), and a wavy-line sketch on the right that reads as a photon-emission or absorption diagram.

## Blackboard Equations

- `lecture_09_figure_03.png`: \(\mathcal{L}=\mathcal{L}\!\left(\phi,\partial_t\phi,\partial_x\phi,\ldots\right)=\mathcal{L}\!\left(\phi,\partial_\mu\phi\right)\) [visible]

- `lecture_09_figure_04.png`: \(\frac{\partial}{\partial x}\frac{\partial \mathcal{L}}{\partial \phi_x}+\cdots=\frac{\partial \mathcal{L}}{\partial \phi}\) [visible]
- `lecture_09_figure_04.png`: \(-\frac{1}{2}\left(\frac{\partial \phi}{\partial x}\right)^2-\cdots -V(\phi)\) [visible]
- `lecture_09_figure_04.png`: \(\phï-\frac{\partial^2\phi}{\partial x^2}-\cdots=\) [partially visible]
- `lecture_09_figure_04.png`: \(\frac{\partial}{\partial t}\frac{\partial \mathcal{L}}{\partial \dot{\phi}}+\frac{\partial}{\partial x}\frac{\partial \mathcal{L}}{\partial \phi_x}+\cdots=\frac{\partial \mathcal{L}}{\partial \phi}\) [standard reconstruction]
- `lecture_09_figure_04.png`: \(\mathcal{L}=\frac12\dot{\phi}^{\,2}-\frac12\left(\frac{\partial \phi}{\partial x}\right)^2-\cdots -V(\phi)\) [standard reconstruction]
- `lecture_09_figure_04.png`: \ddot{\phi}-\frac{\partial^2\phi}{\partial x^2}-\cdots=-\frac{\partial V}{\partial \phi}\) [standard reconstruction]

- `lecture_09_figure_05.png`: \(i\dot{\Psi}= i\alpha \frac{\partial \Psi}{\partial x}+m\beta\Psi\) [visible]
- `lecture_09_figure_05.png`: \(i\left(\Psi^\dagger\frac{\partial\Psi}{\partial t}+\Psi^\dagger\alpha\frac{\partial\Psi}{\partial x}+\Psi^\dagger\beta\Psi\,m\right)\) [visible]
- `lecture_09_figure_05.png`: \(\mathcal{L}=i\left(\Psi^\dagger\frac{\partial\Psi}{\partial t}+\Psi^\dagger\alpha\frac{\partial\Psi}{\partial x}+m\Psi^\dagger\beta\Psi\right)\) [standard reconstruction]

- `lecture_09_figure_06.png`: \(\Psi=\cdots\) [partially visible]
- `lecture_09_figure_06.png`: \(\Psi^\dagger=\cdots\) [partially visible]
- `lecture_09_figure_06.png`: \(\Psi=C^-_{\text{electron}}(+\text{energy})+C^+_{\text{positron}}(+\text{energy})\) [standard reconstruction]
- `lecture_09_figure_06.png`: \(\Psi^\dagger=C^+_{\text{electron}}(+\text{energy})+C^-_{\text{positron}}(+\text{energy})\) [standard reconstruction]
- `lecture_09_figure_06.png`: \(e\,(\text{interaction term involving }\Psi,\Psi^\dagger,\text{ and the photon field})\) [standard reconstruction]

## Diagram And Layout Reading

- `lecture_09_figure_03.png` is primarily a board-layout witness. The important visual fact is that the lecture first writes the Lagrangian in explicit component language and then compresses it into relativistic notation on the same line. The board is nearly empty otherwise, so the equation itself is the whole point.
- `lecture_09_figure_04.png` has a vertical logical structure. The top row gives the general Euler-Lagrange rule, the middle row plugs in the scalar-field Lagrangian, and the lower row begins the resulting field equation. The far-right \(-V(\phi)\) anchors the lecturer’s point that the undifferentiated field enters only through the potential.
- `lecture_09_figure_05.png` is not a geometric diagram, but the two-line organization matters. The top line is the equation of motion; the lower parenthesized line is presented as the Lagrangian that generates it. Because there is no lecturer in frame, the board state is unusually stable and documentary.
- `lecture_09_figure_06.png` is split conceptually rather than symmetrically. On the left are operator decompositions for \(\Psi\) and \(\Psi^\dagger\) with energy annotations; toward the lower middle is a partially hidden interaction expression; on the right is a simple wavy-line sketch suggestive of photon emission or absorption. The lecturer’s gesture points into the interaction/diagram region, so the screenshot is useful mainly for board layout and diagrammatic staging rather than for exact symbol-by-symbol transcription.

## TeX Reconstruction Plan

- `lecture_09_figure_03.png` should remain visible. Its equation is fully legible and is best paired with a clean displayed equation reproducing \(\mathcal{L}(\phi,\partial_t\phi,\partial_x\phi,\ldots)=\mathcal{L}(\phi,\partial_\mu\phi)\).
- `lecture_09_figure_04.png` should remain visible. Nearby, the notes should typeset the full Euler-Lagrange field equation, the scalar-field Lagrangian, and the resulting wave equation with \(-\partial V/\partial\phi\). The screenshot is useful because it shows how the lecturer stacked these three levels of the argument on the board.
- `lecture_09_figure_05.png` should remain visible. It should be paired with a cleaned LaTeX version of the Dirac equation and the corresponding Lagrangian. Because the lecture itself wavers on signs, parentheses, and the placement of the overall \(i\), the typeset equation should be presented cautiously and follow the transcript-stabilized form rather than the chalk literally where they conflict.
- `lecture_09_figure_06.png` should remain visible. The screenshot should not be relied on for an exact operator formula, but it is valuable documentary evidence for the board organization of the QED discussion. A small TikZ redraw of the wavy photon line and a simple electron-photon interaction vertex can sit nearby, while any operator decomposition for \(\Psi\) and \(\Psi^\dagger\) should be typeset only as a cautious reconstruction in the prose or as a short displayed schematic.

## Caption Drafts

- `lecture_09_figure_03.png`: Lagrangian as a function of fields and derivatives
- `lecture_09_figure_04.png`: Potential term in the scalar-field Lagrangian
- `lecture_09_figure_05.png`: Dirac equation and its Lagrangian
- `lecture_09_figure_06.png`: Field-operator decomposition and photon-emission sketch

## Uncertainties

- In `lecture_09_figure_03.png`, there is very little uncertainty. The only caution is that the ellipsis in the explicit derivative list stands for the omitted \(y\)- and \(z\)-derivative terms before the compact \(\partial_\mu\phi\) notation is introduced.
- In `lecture_09_figure_04.png`, the left edge of the board is cropped. The time-derivative term in the Euler-Lagrange equation and the left half of the scalar-field Lagrangian are not fully visible, and the lower field equation begins off-frame. Those pieces should therefore be completed from the transcript and standard scalar-field notation rather than copied literally from the crop.
- In `lecture_09_figure_05.png`, the lecture itself acknowledges uncertainty about where the \(i\)’s and parentheses go. The board is valuable evidence that a Dirac-equation Lagrangian is being written, but the final notes should not canonize every chalk sign placement without transcript-based stabilization.
- In `lecture_09_figure_06.png`, the lecturer blocks part of the board. The subscripts, plus/minus signs, and some words in the \(\Psi\) and \(\Psi^\dagger\) decompositions are only partly legible, and the lower interaction term is too obscured for exact transcription. The wavy-line sketch is clear in purpose, but the exact surrounding formula should be treated as a cautious reconstruction rather than a definitive board reading.