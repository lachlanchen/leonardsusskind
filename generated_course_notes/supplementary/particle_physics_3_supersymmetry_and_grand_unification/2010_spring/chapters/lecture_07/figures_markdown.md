# Figure Notes
## Image Inventory
- `lecture_07_figure_02.png`: A tight whiteboard crop showing, on the upper line, a mass times number-operator expression involving bosonic and fermionic creation/annihilation operators. Below it is a large displayed Lagrangian in terms of a single bosonic mode \(\phi\), written with a kinetic term \(\dot\phi^2/2\) and a mass term \(m^2\phi^2/2\).
- `lecture_07_figure_03.png`: A clean whiteboard crop with a single operator identity written large across the board: \(H = i\,\partial/\partial t\). There is a short stray vertical chalk mark at lower left, but no further mathematics is developed in the frame.
- `lecture_07_figure_05.png`: A wide board shot showing three stacked lines of superspace/component algebra. The first two lines are superfield component expansions in \(\theta\) and \(\bar\theta\), with component fields \(\phi,\psi,\bar\psi,D\). The third line forms a product of superfields and expands its \(\bar\theta\theta\) component terms. The left edge includes only a small bit of lecturer/shadow and does not materially block the equations.

## Blackboard Equations
- `lecture_07_figure_02.png`: \(m\!\left(a^{+}a^{-}+c^{+}c^{-}\right)\) [partially visible]
- `lecture_07_figure_02.png`: \(L=\dfrac{\dot{\phi}^{2}}{2}+\dfrac{m^{2}\phi^{2}}{2}\) [visible]
- `lecture_07_figure_03.png`: \(H=i\,\dfrac{\partial}{\partial t}\) [visible]
- `lecture_07_figure_05.png`: \(\Phi=\phi+\bar{\theta}\psi+\bar{\psi}\theta+D\,\bar{\theta}\theta\) [partially visible]
- `lecture_07_figure_05.png`: \(\bar{\Phi}=\phi+\bar{\theta}\psi+\bar{\psi}\theta+D\,\bar{\theta}\theta\) [partially visible]
- `lecture_07_figure_05.png`: \(\bar{\Phi}\Phi=\phi^{2}+\cdots+2\phi D\,\bar{\theta}\theta-2\bar{\psi}\psi\,\bar{\theta}\theta\) [partially visible]
- `lecture_07_figure_05.png`: \(\bar{\Phi}\Phi=\phi^{2}+2\phi\,\bar{\theta}\psi+2\phi\,\bar{\psi}\theta+\left(2\phi D-2\bar{\psi}\psi\right)\bar{\theta}\theta\) [standard reconstruction]

## Diagram And Layout Reading
- `lecture_07_figure_02.png` is not a diagram but a board-layout milestone: the operator-language Hamiltonian is left above, while the field-language Lagrangian sits below as the main displayed equation. This makes the transition from creation/annihilation operators to the one-dimensional harmonic-oscillator Lagrangian visually explicit.
- `lecture_07_figure_03.png` is purely a slogan-like operator identity. Its value is documentary and conceptual rather than diagrammatic: the Hamiltonian is being reinterpreted as the generator of time translations.
- `lecture_07_figure_05.png` has a useful three-line organization. The top two lines define the component expansions; the third line performs the multiplication and visibly gathers the \(\bar\theta\theta\) terms on the right, which is exactly the part that matters for Berezin integration and for constructing an ordinary Lagrangian from a superfield expression.
- None of these images contains axes, geometric sketches, or state diagrams. Their importance is algebraic layout and sequencing on the board.

## TeX Reconstruction Plan
- `lecture_07_figure_02.png` should remain visible. Place it next to a clean displayed equation for the bosonic-mode Lagrangian. The upper operator line may be typeset nearby as supporting context, but the main note-writing payoff is the displayed \(L(\phi,\dot\phi)\).
- `lecture_07_figure_03.png` should remain visible. Pair it with a clean displayed operator identity \(H=i\,\partial/\partial t\) and a brief line in the notes explaining that this is the one-dimensional quantum-mechanical representation of the Hamiltonian as time translation.
- `lecture_07_figure_05.png` should remain visible. Nearby, reconstruct the superspace algebra in a clean aligned display: first the superfield expansion, then the product, then the \(\bar\theta\theta\) coefficient that survives Grassmann integration. No TikZ redraw is needed; ordinary displayed equations are the right reconstruction tool here.
- For `lecture_07_figure_05.png`, the notes should use the transcript to stabilize the algebra when the board is not perfectly crisp, especially for the combined \(\bar\theta\theta\) coefficient and the ordering/signs of barred versus unbarred fermions.
- None of these figures requires a separate TikZ schematic. Their purpose is to preserve blackboard evidence while the mathematics is cleaned up in standard LaTeX nearby.

## Caption Drafts
- `lecture_07_figure_02.png`: Bosonic oscillator Lagrangian from the one-mode field setup
- `lecture_07_figure_03.png`: Hamiltonian as the generator of time translations
- `lecture_07_figure_05.png`: Product of superfields expanded in components

## Uncertainties
- In `lecture_07_figure_02.png`, the plus sign in the displayed mass term is clearly visible on the board, but the transcript shortly afterward records Susskind correcting the bosonic Lagrangian from \(T+V\) to \(T-V\). The notes should therefore preserve the screenshot as evidence of the live board state while using the transcript to correct the final mathematics.
- In `lecture_07_figure_02.png`, the operator notation in the upper line is legible only at the level of a mass times bosonic and fermionic number operators; whether the superscripts should be read as \(+\)/\(-\) or dagger/minus notation should not be overclaimed from the image alone.
- In `lecture_07_figure_03.png`, only the operator identity itself is visible. The wavefunction that \(H\) acts on is not written in the frame and should not be added as if it were board-backed.
- In `lecture_07_figure_05.png`, the exact barred/unbarred labels on the first two lines are not fully crisp from the image alone. The broad structure is secure, but the detailed component notation should be stabilized by the transcript before final typesetting.
- In `lecture_07_figure_05.png`, the third-line expansion is only partly sharp. The existence of a \(\bar\theta\theta\) coefficient and the appearance of terms proportional to \(\phi D\) and \(\bar\psi\psi\) are well supported, but the exact coefficients and signs should be treated as a cautious standard reconstruction rather than a purely image-derived transcription.