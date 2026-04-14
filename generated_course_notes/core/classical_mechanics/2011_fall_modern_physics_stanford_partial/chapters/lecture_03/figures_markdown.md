# Figure Notes
## Image Inventory
- `lecture_03_figure_02.png`: Mid-board view from the Euler-Lagrange discussion. On the left board there is a large displayed term consisting of a total time derivative acting on a partial derivative of the Lagrangian with respect to a dotted coordinate. On the right board there is a partially visible trajectory sketch with a slanted segment and a curved path.
- `lecture_03_figure_03.png`: Close board view during the introduction of canonical momentum. The main visible content is a definition of a \(\pi\)-like quantity with subscript \(i\) equal to a partial derivative of the Lagrangian with respect to \(\dot q_i\). Susskind points near the left side of the formula.
- `lecture_03_figure_04.png`: Wide board view in the two-dimensional near-Earth example. The top line contains the kinetic-energy terms in \(\dot x\) and \(\dot y\). At the left there is a simple setup sketch with a horizontal baseline and a vertical coordinate line. On the far right Susskind is still writing a new term, so that part is incomplete.

## Blackboard Equations
- `lecture_03_figure_02.png`: \(\displaystyle \frac{d}{dt}\left(\frac{\partial \mathcal{L}}{\partial \dot q_i}\right)\) [visible]
- `lecture_03_figure_02.png`: \(\displaystyle \frac{\partial \mathcal{L}}{\partial q_i}\) [standard reconstruction]
  The transcript makes clear that the displayed left-hand term is being compared with the derivative of the Lagrangian with respect to the corresponding coordinate, even though that matching right-hand term is not fully shown in this frame.
- `lecture_03_figure_03.png`: \(\displaystyle \Pi_i=\frac{\partial \mathcal{L}}{\partial \dot q_i}\) [visible]
- `lecture_03_figure_03.png`: \(\displaystyle \pi_i=\frac{\partial \mathcal{L}}{\partial \dot q_i}\) [standard reconstruction]
  The transcript supports the usual lowercase \(\pi_i\), though the board symbol can be read as a capital \(\Pi_i\).
- `lecture_03_figure_04.png`: \(\displaystyle \frac12 m\dot x^{\,2}+\frac12 m\dot y^{\,2}\) [partially visible]
- `lecture_03_figure_04.png`: \(\displaystyle T=\frac12 m\dot x^{\,2}+\frac12 m\dot y^{\,2}\) [standard reconstruction]
  The transcript identifies this line as the kinetic energy for motion in two dimensions, but the leading symbol or equality on the board is not fully secure from the image alone.

## Diagram And Layout Reading
- `lecture_03_figure_02.png` is laid out as algebra on the left, geometry on the right. The left equation is large and isolated, as if Susskind is rewriting the Euler-Lagrange equation term by term. The right-hand sketch looks like a qualitative path or trajectory picture, not a precise geometric construction.
- In `lecture_03_figure_02.png`, the right board shows a slanted line segment below and a curved path above, with a few small marks near the path. This reads as supporting intuition for motion or variation along a trajectory rather than as a separate formal derivation.
- `lecture_03_figure_03.png` is a clean definition board. The equation is centered and pedagogically self-contained: first the symbol \(\pi_i\), then the equals sign, then the derivative of the Lagrangian with respect to the corresponding velocity component.
- `lecture_03_figure_04.png` combines a setup sketch and a kinetic-energy expression. The left sketch appears to show a horizontal surface with a vertical direction marked upward from it and a point representing the particle. The top formula then translates that setup into the two-coordinate kinetic term.
- In `lecture_03_figure_04.png`, the rightmost writing is still in progress and should be treated as process rather than as a stable transcription source. The frame is more valuable for the established top equation and the coordinate layout than for the fresh marks being added on the right.

## TeX Reconstruction Plan
- `lecture_03_figure_02.png` should remain visible in the notes. Nearby, typeset the clean Euler-Lagrange term
  \[
  \frac{d}{dt}\left(\frac{\partial \mathcal{L}}{\partial \dot q_i}\right)
  \]
  and, if the chapter uses the right-hand sketch, add a modest TikZ redraw of a qualitative trajectory or local path segment. The screenshot should remain the primary evidence for the board layout.
- `lecture_03_figure_03.png` should remain visible in the notes. Nearby, typeset the canonical-momentum definition cleanly as
  \[
  \pi_i=\frac{\partial \mathcal{L}}{\partial \dot q_i}.
  \]
  No TikZ is needed here; the main value of the screenshot is the board witness for the notation and the moment of definition.
- `lecture_03_figure_04.png` should remain visible in the notes. Nearby, reconstruct the kinetic-energy formula as a displayed equation,
  \[
  T=\frac12 m\dot x^{\,2}+\frac12 m\dot y^{\,2},
  \]
  and add a simple TikZ redraw of the two-dimensional near-Earth setup with horizontal \(x\), vertical \(y\), and a particle above the surface. Do not reconstruct the unfinished right-hand writing from the image alone.

## Caption Drafts
- `lecture_03_figure_02.png`: Euler-Lagrange time-derivative term with trajectory sketch
- `lecture_03_figure_03.png`: Canonical momentum from the Lagrangian
- `lecture_03_figure_04.png`: Two-dimensional kinetic term and near-Earth setup

## Uncertainties
- In `lecture_03_figure_02.png`, the exact subscript structure in the denominator is not perfectly crisp; the transcript strongly supports reading the denominator as \(\dot q_i\).
- In `lecture_03_figure_02.png`, the right-hand sketch is partly cropped and low-detail. It should be treated as a qualitative motion or variation picture, not as a metrically exact diagram.
- In `lecture_03_figure_03.png`, the momentum symbol looks like an uppercase \(\Pi_i\) on the board, while the transcript and standard notation suggest lowercase \(\pi_i\).
- In `lecture_03_figure_04.png`, the top kinetic-energy line is incomplete at its left and right edges; the image alone does not securely show whether a leading \(T=\) is written.
- In `lecture_03_figure_04.png`, the coordinate labels in the left sketch are faint. The transcript is needed to regularize the intended interpretation as horizontal \(x\) and vertical \(y\).
- In `lecture_03_figure_04.png`, the far-right writing is visibly in progress and should not be used as a stable source for the potential-energy formula.