# Figure Notes
## Image Inventory
- `lecture_07_figure_02.png`: Medium board view with Susskind at the left, pointing at a fraction on the board. The central visible expression is the one-dimensional free-particle Lagrangian written as a dotted \(x\) squared over \(2\), and the right side begins a canonical-momentum line with `\(P_x=\)`.
- `lecture_07_figure_03.png`: Tight crop of a nearly blank board containing an action-like expression. The visible line shows an integral with the kinetic term \(mv^2/2\), followed by `\(dt\)`, and then the beginning of a vector-potential term written as `\(+ q A_i\)`.
- `lecture_07_figure_04.png`: Tight board crop from the magnetic-field derivation. The clearest visible content is an equality whose right-hand side is a velocity times a derivative of the vector potential, readable as the \(x\)-component contribution \(q\dot x\,\partial A_x/\partial z\). Cropped earlier terms remain visible at the left edge.

## Blackboard Equations
- `lecture_07_figure_02.png`: \(L=\frac{\dot x^2}{2}\) [visible]
- `lecture_07_figure_02.png`: \(P_x=\) [visible]
- `lecture_07_figure_02.png`: \(P_x=\frac{\partial L}{\partial \dot x}=\dot x\) [standard reconstruction]

- `lecture_07_figure_03.png`: \(\int \frac{mv^2}{2}\,dt + qA_i\) [partially visible]
- `lecture_07_figure_03.png`: \(q\int A_i\,dx_i\) [standard reconstruction]
- `lecture_07_figure_03.png`: \(q\int \mathbf{A}\cdot d\mathbf{x}\) [standard reconstruction]
- `lecture_07_figure_03.png`: \(S=\int \frac12 mv^2\,dt + q\int A_i\,dx_i\) [standard reconstruction]

- `lecture_07_figure_04.png`: \(= q\dot x\,\frac{\partial A_x}{\partial z}\) [visible]
- `lecture_07_figure_04.png`: \(\frac{\partial L}{\partial z}=q\dot x\,\frac{\partial A_x}{\partial z}+q\dot y\,\frac{\partial A_y}{\partial z}+q\dot z\,\frac{\partial A_z}{\partial z}\) [standard reconstruction]

## Diagram And Layout Reading
- None of the selected images is a geometric diagram in the usual sense; all three are equation-board moments.
- `lecture_07_figure_02.png` is organized horizontally: the Lagrangian sits to the left, the fraction \(\dot x^2/2\) is centered, and the canonical-momentum statement begins on the right. The lecturer’s hand points at the denominator, which helps confirm that the board is reading the free-particle Lagrangian term-by-term.
- `lecture_07_figure_03.png` is a single-line formula on an otherwise empty board. Its value is not layout complexity but documentary timing: it catches the transition from the usual kinetic action term to the extra magnetic coupling term.
- `lecture_07_figure_04.png` centers an equals sign and a right-hand derivative term. The cropped left edge shows that this belongs to a longer multi-term line, but the frame’s real value is to certify the first explicit contribution \(q\dot x\,\partial A_x/\partial z\) in the \(z\)-derivative of the Lagrangian.
- No axes, arrows, or standalone sketches are visible in these crops, so there is no need for board-faithful TikZ diagram reconstruction.

## TeX Reconstruction Plan
- `lecture_07_figure_02.png` should remain visible in the notes. Nearby, the notes should typeset the cleaned equations
  \[
  L=\frac{\dot x^2}{2},
  \qquad
  P_x=\frac{\partial L}{\partial \dot x}=\dot x.
  \]
  The screenshot is useful as evidence for the board moment when the canonical momentum is introduced from the derivative with respect to \(\dot x\).

- `lecture_07_figure_03.png` should remain visible in the notes. It should be paired with a cleaned displayed reconstruction of the action term, for example
  \[
  S=\int \frac12 mv^2\,dt + q\int A_i\,dx_i
  \]
  or equivalently
  \[
  S=\int \left(\frac12 mv^2 + qA_i\dot x_i\right)\,dt.
  \]
  The screenshot itself only certifies the kinetic term and the start of the \(qA_i\) coupling, so the full line-integral structure should be typeset from cautious transcript-backed reconstruction rather than claimed as fully visible.

- `lecture_07_figure_04.png` should remain visible in the notes. It should be paired with a cleaned displayed equation for the full derivative line, such as
  \[
  \frac{\partial L}{\partial z}
  =
  q\dot x\,\frac{\partial A_x}{\partial z}
  +
  q\dot y\,\frac{\partial A_y}{\partial z}
  +
  q\dot z\,\frac{\partial A_z}{\partial z}.
  \]
  The screenshot most strongly backs the first right-hand term and the board’s equality structure; the remaining terms should be reconstructed from the transcript and surrounding derivation.
- No TikZ redraw is needed for any of these three assets. All three should be treated as `screenshot_plus_equation`, not as diagram figures.

## Caption Drafts
- `lecture_07_figure_02.png`: Free-particle Lagrangian and the definition of \(P_x\)
- `lecture_07_figure_03.png`: Action guess with kinetic term and vector-potential coupling
- `lecture_07_figure_04.png`: First term in \(\partial L/\partial z\) from the vector potential

## Uncertainties
- In `lecture_07_figure_02.png`, the leftmost symbol is a cursive \(L\)-like mark and could be written either as \(L\) or \(\mathcal{L}\) in clean typesetting. The completed derivative equation to the right is not fully visible in the frame and needs transcript-backed completion.
- In `lecture_07_figure_03.png`, the integral sign is cropped at the far left, and the visible `\(+qA_i\)` does not by itself certify the following differential. The full line-integral form \(A_i\,dx_i\) or \(\mathbf A\cdot d\mathbf x\) should therefore be treated as a standard reconstruction rather than a direct transcription from the image alone.
- In `lecture_07_figure_04.png`, the right-hand factor is best read as \(q\dot x\,\partial A_x/\partial z\), but the handwritten dot and \(x\) are close enough that the reading depends partly on the transcript. The left-side earlier terms are too cropped to transcribe confidently from the image by itself.