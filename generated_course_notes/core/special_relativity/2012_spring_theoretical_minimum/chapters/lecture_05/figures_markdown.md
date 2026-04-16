# Figure Notes
## Image Inventory
- `lecture_05_figure_02.png`: mid-board view from the particle-coupling discussion. At upper left the field label `\phi(xt)` or `\phi(x,t)` is visible. Near the center the board shows the relativistic particle Lagrangian in square-root form, with the left-hand `\mathcal L` and its subscript partly blocked by Susskind. On the far right there is a separate slanted tick-mark sketch, preserved only as board context.
- `lecture_05_figure_03.png`: board view from the Euler–Lagrange calculation for the coupled field. The dominant visible content is a stacked combination of second derivatives, beginning with an equals sign and then the time derivative term minus the three spatial second derivatives. On the left Susskind is just beginning to write a new partial-derivative symbol.
- `lecture_05_figure_04.png`: board view from the relativity-notation section. On the left appears a scalar contraction of a four-vector together with a boxed metric-based expression. On the right, a large expression shows the differential of a scalar field written as its derivative with respect to \(x^\mu\) times \(dx^\mu\), and below it the derivative components are expanded in coordinates.
- `lecture_05_figure_05.png`: board view from the Klein–Gordon setup. Across the top is a field-theory Lagrangian with the usual \(1/2\) factor, a time-derivative square, a minus spatial-derivative square, ellipsis for the remaining spatial directions, and a mass term proportional to \(\phi^2\). Below it sits a lower comparison line for the ordinary harmonic-oscillator form.

## Blackboard Equations
- `lecture_05_figure_02.png`: \(\phi(x,t)\) [visible]
- `lecture_05_figure_02.png`: \(\mathcal L_{\text{particle}}\) [partially visible]
- `lecture_05_figure_02.png`: \(= -m\sqrt{1-\dot x^{\,2}}\) [visible]
- `lecture_05_figure_02.png`: \(\mathcal L_{\text{particle}}=-m\sqrt{1-\dot x^{\,2}}\) [standard reconstruction]

- `lecture_05_figure_03.png`: \(=\frac{\partial^2\phi}{\partial t^2}-\frac{\partial^2\phi}{\partial x^2}-\frac{\partial^2\phi}{\partial y^2}-\frac{\partial^2\phi}{\partial z^2}\) [visible]
- `lecture_05_figure_03.png`: a newly started partial-derivative symbol on the left [partially visible]

- `lecture_05_figure_04.png`: \(A^\mu A_\mu=\mathrm{Sca}\ldots\) [partially visible]
- `lecture_05_figure_04.png`: \(A^\mu \eta_{\mu\nu}A^\nu\) [partially visible]
- `lecture_05_figure_04.png`: \(\frac{\partial\phi(x)}{\partial x^\mu}\,dx^\mu\) [visible]
- `lecture_05_figure_04.png`: \(\frac{\partial\phi}{\partial x^\mu}=\left(\frac{\partial\phi}{\partial t},\frac{\partial\phi}{\partial x},\ldots\right)\) [partially visible]
- `lecture_05_figure_04.png`: \(A^\mu A_\mu=A^\mu\eta_{\mu\nu}A^\nu\) [standard reconstruction]

- `lecture_05_figure_05.png`: \(\frac12\left[\left(\frac{\partial\phi}{\partial t}\right)^2-\left(\frac{\partial\phi}{\partial x}\right)^2+\cdots-M^2\phi^2\right]\) [partially visible]
- `lecture_05_figure_05.png`: \(\frac{\dot\phi^2}{2}-\frac{\mu^2\phi^2}{2}\) [partially visible]
- `lecture_05_figure_05.png`: \(\frac12\left[\left(\frac{\partial\phi}{\partial t}\right)^2-\left(\frac{\partial\phi}{\partial x}\right)^2-\left(\frac{\partial\phi}{\partial y}\right)^2-\left(\frac{\partial\phi}{\partial z}\right)^2-\mu^2\phi^2\right]\) [standard reconstruction]

## Diagram And Layout Reading
- `lecture_05_figure_02.png` preserves a board layout rather than a polished diagram. The left side still carries the field label, the center carries the relativistic particle Lagrangian, and the right side contains a separate slanted tick-mark sketch. The sketch is too stripped down to identify confidently as a worldline or wavefront construction from the image alone, but it is useful as contextual evidence that Susskind was juxtaposing the formula with a small geometric doodle.
- `lecture_05_figure_03.png` is laid out as an in-progress derivation. The right half already contains the completed second-derivative combination, while the left half shows him starting the next symbol. For note writing, the value of the frame is precisely this incomplete-but-live board rhythm.
- `lecture_05_figure_04.png` has a strong two-column logic. On the left is the reminder that contracting upper and lower indices makes a scalar. On the right is the key infinitesimal relation \(d\phi=(\partial\phi/\partial x^\mu)dx^\mu\), with the pointing hand emphasizing the \(dx^\mu\) factor. The lower-right line then expands the covariant derivative components.
- `lecture_05_figure_05.png` is organized pedagogically: the upper line is the field-theory Lagrangian, while the lower line is the ordinary oscillator comparison. This layered layout matters because the lecture is explicitly saying that the field theory is the oscillator with added space derivatives.

## TeX Reconstruction Plan
- `lecture_05_figure_02.png` should remain visible. Nearby the notes should typeset the cleaned equation
  \[
  \mathcal L_{\mathrm{particle}}=-m\sqrt{1-\dot x^{\,2}}.
  \]
  The right-hand sketch should be left in the screenshot rather than redrawn unless later frames clarify its meaning enough to justify a separate TikZ diagram.
- `lecture_05_figure_03.png` should remain visible. The notes should typeset the derivative stack cleanly as
  \[
  \frac{\partial^2\phi}{\partial t^2}
  -\frac{\partial^2\phi}{\partial x^2}
  -\frac{\partial^2\phi}{\partial y^2}
  -\frac{\partial^2\phi}{\partial z^2},
  \]
  and, if needed, reconstruct the fuller Euler–Lagrange step from the transcript rather than from the hidden left side of the screenshot.
- `lecture_05_figure_04.png` should remain visible. The notes should typeset, near the screenshot,
  \[
  A^\mu A_\mu=A^\mu\eta_{\mu\nu}A^\nu,
  \qquad
  d\phi=\frac{\partial\phi(x)}{\partial x^\mu}\,dx^\mu,
  \qquad
  \frac{\partial\phi}{\partial x^\mu}
  =\left(\frac{\partial\phi}{\partial t},\frac{\partial\phi}{\partial x},\frac{\partial\phi}{\partial y},\frac{\partial\phi}{\partial z}\right),
  \]
  with prose explaining that these are the covariant components. No TikZ redraw is needed.
- `lecture_05_figure_05.png` should remain visible. The notes should reconstruct the upper field Lagrangian in a cleaned displayed form and also preserve the lower oscillator analogy:
  \[
  \mathcal L
  =\frac12\left[
  \left(\frac{\partial\phi}{\partial t}\right)^2
  -\left(\frac{\partial\phi}{\partial x}\right)^2
  -\left(\frac{\partial\phi}{\partial y}\right)^2
  -\left(\frac{\partial\phi}{\partial z}\right)^2
  -\mu^2\phi^2
  \right],
  \qquad
  L_{\text{osc}}=\frac{\dot\phi^2}{2}-\frac{\mu^2\phi^2}{2}.
  \]
  The transcript should be used to standardize the omitted \(y\) and \(z\) terms and the mass parameter notation.

## Caption Drafts
- `lecture_05_figure_02.png`: Relativistic particle Lagrangian on the board
- `lecture_05_figure_03.png`: Second-derivative terms in the field equation
- `lecture_05_figure_04.png`: Derivative of a scalar field paired with \(dx^\mu\)
- `lecture_05_figure_05.png`: Field Lagrangian with spatial-gradient terms

## Uncertainties
- `lecture_05_figure_02.png`: the left-hand \(\mathcal L\) label and its subscript are partly blocked by Susskind’s body, so the full \(\mathcal L_{\text{particle}}\) label is a cautious completion rather than a direct transcription. The small right-hand sketch is visually preserved but not interpretable with confidence from this frame alone.
- `lecture_05_figure_03.png`: the visible derivative stack is clear, but the new symbol being started on the left is incomplete. One should not infer too much from that left fragment beyond the fact that another partial-derivative term was being written.
- `lecture_05_figure_04.png`: the word “scalar” is truncated, and the boxed contraction on the left is partly obscured, so \(A^\mu\eta_{\mu\nu}A^\nu\) should be treated as a cautious standard completion rather than a full verbatim blackboard transcription. The lower-right component list is cut off after the first entries.
- `lecture_05_figure_05.png`: the mass parameter on the top line may visually resemble a capital \(M\), while the lecture transcript strongly suggests \(\mu\). The far-right bracket and the full set of spatial derivative terms are not all explicit in the frame, so the full four-dimensional expression requires cautious standard completion. The lower line is shorthand and partly stylized, so it should be regularized in LaTeX using the transcript-backed harmonic-oscillator comparison.