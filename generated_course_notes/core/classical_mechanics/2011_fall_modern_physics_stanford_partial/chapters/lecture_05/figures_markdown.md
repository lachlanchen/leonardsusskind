# Figure Notes
## Image Inventory

- `lecture_05_figure_02.png`: Close board view from the simple-pendulum discussion. The upper-left corner contains part of the pendulum sketch with a point mass at the end of a rod of length \(r\). At the upper right one sees the kinetic term \(T\), below it the potential-energy line \(U\), and across the middle the Lagrangian \(\mathcal{L}\). Susskind’s hand points directly at the \(+mgr\cos\theta\) term.
- `lecture_05_figure_03.png`: Wider board view of the same simple-pendulum setup. The pendulum sketch remains visible at the upper left, the \(U=-mgr\cos\theta\) line and the Lagrangian are still readable on the upper board, and the lower board begins the canonical-momentum and equation-of-motion step.
- `lecture_05_figure_04.png`: Equation-dominant board view from the double-pendulum discussion. The board shows a top line for \(T\), a second line for \(U\), a long Lagrangian line with the mixed \(\dot\theta\dot\phi\cos(\theta-\phi)\) term, a boxed term at the right, and below that the symmetry shifts \(\theta\to\theta+\epsilon\), \(\phi\to\phi+\epsilon\). Susskind points near the \(\cos(\theta-\phi)\) factor.
- `lecture_05_figure_05.png`: Harmonic-oscillator board view during the transition from Lagrangian to Hamiltonian form. The top line identifies the canonical momentum \(P=\Pi_x\), the middle line writes the Hamiltonian in terms of \(P\dot x\) and the Lagrangian pieces, and the lower line boxes the simplified final energy expression.

## Blackboard Equations

- `lecture_05_figure_02.png`: \(T=\frac{m}{2}r^2\dot{\theta}^{\,2}\) [visible]
- `lecture_05_figure_02.png`: \(U=-mgr\cos\theta\) [visible]
- `lecture_05_figure_02.png`: \(\mathcal{L}=\frac{mr^2}{2}\dot{\theta}^{\,2}+mgr\cos\theta\) [visible]

- `lecture_05_figure_03.png`: \(U=-mgr\cos\theta\) [visible]
- `lecture_05_figure_03.png`: \(\mathcal{L}=\frac{mr^2}{2}\dot{\theta}^{\,2}+mgr\cos\theta\) [visible]
- `lecture_05_figure_03.png`: \(\pi_\theta=mr^2\dot{\theta}\) [partially visible]
- `lecture_05_figure_03.png`: \(\frac{d}{dt}\left(mr^2\dot{\theta}\right)=\frac{\partial \mathcal{L}}{\partial \theta}\) [standard reconstruction]

- `lecture_05_figure_04.png`: \(T=mr^2\dot{\theta}^{\,2}+\frac{1}{2}mr^2\dot{\phi}^{\,2}+mr^2\dot{\theta}\dot{\phi}\cos(\theta-\phi)\) [visible]
- `lecture_05_figure_04.png`: \(U=-2mgr\cos\theta-mgr\cos\phi\) [visible]
- `lecture_05_figure_04.png`: \(\mathcal{L}=mr^2\dot{\theta}^{\,2}+\frac{1}{2}mr^2\dot{\phi}^{\,2}+mr^2\dot{\theta}\dot{\phi}\cos(\theta-\phi)+mgr(2\cos\theta+\cos\phi)\) [partially visible]
- `lecture_05_figure_04.png`: \(\theta\to\theta+\epsilon\) [visible]
- `lecture_05_figure_04.png`: \(\phi\to\phi+\epsilon\) [visible]
- `lecture_05_figure_04.png`: \(\frac{\partial \mathcal{L}}{\partial \theta}\) [standard reconstruction]

- `lecture_05_figure_05.png`: \(P=\Pi_x=\frac{\partial \mathcal{L}}{\partial \dot{x}}=m\dot{x}\) [visible]
- `lecture_05_figure_05.png`: \(H=P\dot{x}-\frac{m}{2}\dot{x}^{\,2}+\frac{k}{2}x^2\) [partially visible]
- `lecture_05_figure_05.png`: \(H=\frac{m}{2}\dot{x}^{\,2}+\frac{k}{2}x^2\) [visible]
- `lecture_05_figure_05.png`: \(H=\frac{p^2}{2m}+\frac{k}{2}x^2\) [standard reconstruction]

## Diagram And Layout Reading

- `lecture_05_figure_02.png` includes a compact pendulum sketch rather than a fully geometric diagram. Its function is mnemonic: pivot above, rod length \(r\), bob at the end, angle \(\theta\) measured from the vertical. The real value of the frame is the simultaneous visibility of \(T\), \(U\), and the finished Lagrangian line.
- In `lecture_05_figure_02.png`, the lecturer’s gesture matters: the hand is placed at the \(+mgr\cos\theta\) term, so the board emphasis is on the sign change produced by subtracting a negative potential energy.
- `lecture_05_figure_03.png` preserves a two-tier board layout. The upper board still carries the pendulum setup and Lagrangian; the lower board has already moved on to \(\pi_\theta\) and the time-derivative step. This makes it useful as evidence for the lecture’s transition from writing down \(\mathcal{L}\) to deriving the equation of motion.
- `lecture_05_figure_04.png` is organized horizontally by conceptual layer: \(T\) on top, \(U\) below it, the full \(\mathcal{L}\) across the middle, the common rotation shifts on the lower left, and a boxed term on the right. The lecturer points at the \(\cos(\theta-\phi)\) factor, so the board is emphasizing that only angle differences appear in the coupling.
- `lecture_05_figure_04.png` does not preserve a clean geometric drawing of the double pendulum itself; it is primarily a formula witness. If the notes need a double-pendulum diagram, it should be supplied elsewhere from a cleaner source or redrawn separately.
- `lecture_05_figure_05.png` is a pure algebra board. The composition is sequential: top line defines canonical momentum, middle line substitutes into \(H=P\dot{x}-\mathcal{L}\), and the lower line boxes the simplified energy. There is no independent diagram here; the value is the board sequence.

## TeX Reconstruction Plan

- `lecture_05_figure_02.png` should remain visible. Nearby, typeset the simple-pendulum formulas
  \[
  T=\frac{m}{2}r^2\dot{\theta}^{\,2},\qquad
  U=-mgr\cos\theta,\qquad
  \mathcal{L}=\frac{mr^2}{2}\dot{\theta}^{\,2}+mgr\cos\theta.
  \]
  No TikZ is required if `lecture_05_figure_03.png` already carries the pendulum sketch more usefully.
- `lecture_05_figure_03.png` should remain visible. It should be paired with the same clean displayed Lagrangian and, because this frame still preserves the pendulum geometry, a small TikZ redraw of the simple pendulum is appropriate nearby. If the notes also want the next step, add a cautious displayed line for
  \[
  \pi_\theta=\frac{\partial\mathcal{L}}{\partial\dot{\theta}}=mr^2\dot{\theta}.
  \]
- `lecture_05_figure_04.png` should remain visible. Nearby, typeset the cleaned double-pendulum Lagrangian and the symmetry shift lines,
  \[
  \mathcal{L}=mr^2\dot{\theta}^{\,2}+\frac{1}{2}mr^2\dot{\phi}^{\,2}
  +mr^2\dot{\theta}\dot{\phi}\cos(\theta-\phi)
  +mgr(2\cos\theta+\cos\phi),
  \]
  \[
  \theta\to\theta+\epsilon,\qquad \phi\to\phi+\epsilon.
  \]
  This figure is equation-heavy, so a TikZ redraw is not necessary here unless the chapter separately needs a clean double-pendulum geometry.
- `lecture_05_figure_05.png` should remain visible. Nearby, typeset the harmonic-oscillator Hamiltonian derivation cleanly:
  \[
  P=\Pi_x=\frac{\partial\mathcal{L}}{\partial\dot{x}}=m\dot{x},
  \qquad
  H=P\dot{x}-\mathcal{L}
  =\frac{m}{2}\dot{x}^{\,2}+\frac{k}{2}x^2.
  \]
  If the chapter is already transitioning into Hamiltonian variables, also add the converted form
  \[
  H=\frac{p^2}{2m}+\frac{k}{2}x^2.
  \]

## Caption Drafts

- `lecture_05_figure_02.png`: Potential-energy sign inside the pendulum Lagrangian
- `lecture_05_figure_03.png`: Pendulum Lagrangian and the first momentum step
- `lecture_05_figure_04.png`: Two-angle Lagrangian with the \(\cos(\theta-\phi)\) coupling
- `lecture_05_figure_05.png`: Hamiltonian for the harmonic oscillator

## Uncertainties

- In `lecture_05_figure_02.png`, the pendulum sketch is cropped, so the exact angle marker is not fully preserved in the frame even though the geometry is clearly the simple pendulum.
- In `lecture_05_figure_03.png`, the lower-board canonical-momentum and Euler–Lagrange lines are incomplete in the crop. They support the transition to the equation of motion, but not a fully trustworthy symbol-by-symbol transcription.
- In `lecture_05_figure_04.png`, the exact coefficients in the potential-energy line and in the boxed term at the right are not perfectly sharp. The transcript strongly supports
  \[
  U=-2mgr\cos\theta-mgr\cos\phi,
  \qquad
  \mathcal{L}\supset +mgr(2\cos\theta+\cos\phi),
  \]
  but those should be treated as cautious completions rather than purely direct chalk transcription.
- In `lecture_05_figure_04.png`, the frame does not itself clearly show the explicit written derivative \(\partial\mathcal{L}/\partial\theta\); the subtitle and gesture identify the lecture moment, but the visible board is mainly the Lagrangian and symmetry setup.
- In `lecture_05_figure_05.png`, the middle Hamiltonian-substitution line is partly obscured by the lecturer’s body and gesture, so the clean displayed equation should be presented as a standard reconstruction anchored by the more legible top canonical-momentum line and boxed final result.
- Across these figures, the transcript is needed to disambiguate the intended algebraic step, but the notes should not claim more blackboard legibility than the frames actually support.