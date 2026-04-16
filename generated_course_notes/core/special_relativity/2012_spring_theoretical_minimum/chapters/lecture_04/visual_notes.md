# Visual Evidence
## Frame Inventory
- `lecture_04_figure_02.png`: Close crop of the nonrelativistic-particle recap showing the central Lagrangian \(L=\frac{m}{2}\dot\phi^2-V(\phi)\), the beginning of the Euler–Lagrange operator, and a cropped fragment of the earlier time-axis sketch; this should remain in the final notes as a primary screenshot.
- `lecture_04_figure_03.png`: Transitional board frame with Susskind writing, showing the field-theory action at the top, the ordinary Euler–Lagrange equation in the middle, and the start of the field-theory generalization below; this should remain in the final notes as a primary screenshot.
- `lecture_04_figure_04.png`: Talking-head frame that still preserves the particle-style action, the nonrelativistic \(L=T-V\) line, and cropped continuation of spatial-derivative terms at the far left; this may remain in the final notes as secondary contextual screenshot evidence.
- `lecture_04_figure_05.png`: The clearest board snapshot of the completed field-theory Euler–Lagrange layout, with the action on top, the ordinary equation in the middle, and the spacetime form below; this should remain in the final notes as a primary screenshot.
- `lecture_04_figure_06.png`: Late-board frame showing the interval relation derived from the metric on the upper board and a four-vector example \(A^\mu(x,t)\) with its Lorentzian norm on the lower board; this should remain in the final notes as a primary screenshot.

## Equation Extraction
- `lecture_04_figure_02.png`: \(L=\frac{m}{2}\dot\phi^2-V(\phi)\) [visible]
- `lecture_04_figure_02.png`: \(\frac{d}{dt}\frac{\partial L}{\partial\dot\phi}\) [visible]
- `lecture_04_figure_02.png`: \(A=\int_a^b\left[\frac12\left(\frac{d\phi}{dt}\right)^2-V(\phi)\right]dt\) [partially visible]
- `lecture_04_figure_02.png`: \(A=\int_a^b\left[\frac{m}{2}\left(\frac{d\phi}{dt}\right)^2-V(\phi)\right]dt\) [standard completion]

- `lecture_04_figure_03.png`: \(A=\int d^4x\,\mathcal L\!\left(\phi,\frac{\partial\phi}{\partial x^\mu}\right)\) [partially visible]
- `lecture_04_figure_03.png`: \(\frac{d}{dt}\frac{\partial\mathcal L}{\partial\!\left(\frac{\partial\phi}{\partial t}\right)}-\frac{\partial\mathcal L}{\partial\phi}=0\) [visible]
- `lecture_04_figure_03.png`: \(\frac{\partial}{\partial x^\mu}\frac{\partial\mathcal L}{\partial\!\left(\frac{\partial\phi}{\partial x^\mu}\right)}-\cdots\) [partially visible]
- `lecture_04_figure_03.png`: \(\frac{\partial}{\partial x^\mu}\left(\frac{\partial\mathcal L}{\partial\!\left(\frac{\partial\phi}{\partial x^\mu}\right)}\right)-\frac{\partial\mathcal L}{\partial\phi}=0\) [standard completion]

- `lecture_04_figure_04.png`: \(L=\frac{m}{2}\dot\phi^2-V(\phi)\) [visible]
- `lecture_04_figure_04.png`: \(A=\int_a^b\left[\frac12\left(\frac{d\phi}{dt}\right)^2-V(\phi)\right]dt\) [partially visible]
- `lecture_04_figure_04.png`: \(-\frac{\partial\mathcal L}{\partial\phi}=0\) [partially visible]
- `lecture_04_figure_04.png`: \(-\left(\frac{\partial\phi}{\partial y}\right)^2-\left(\frac{\partial\phi}{\partial z}\right)^2\) [partially visible]

- `lecture_04_figure_05.png`: \(A=\int d^4x\,\mathcal L\!\left(\phi,\frac{\partial\phi}{\partial x^\mu}\right)\) [partially visible]
- `lecture_04_figure_05.png`: \(\frac{d}{dt}\frac{\partial\mathcal L}{\partial\!\left(\frac{\partial\phi}{\partial t}\right)}-\frac{\partial\mathcal L}{\partial\phi}=0\) [visible]
- `lecture_04_figure_05.png`: \(\sum_\mu \frac{\partial}{\partial x^\mu}\frac{\partial\mathcal L}{\partial\!\left(\frac{\partial\phi}{\partial x^\mu}\right)}-\frac{\partial\mathcal L}{\partial\phi}=0\) [partially visible]
- `lecture_04_figure_05.png`: \(\frac{\partial}{\partial x^\mu}\left(\frac{\partial\mathcal L}{\partial\!\left(\frac{\partial\phi}{\partial x^\mu}\right)}\right)-\frac{\partial\mathcal L}{\partial\phi}=0\) [standard completion]

- `lecture_04_figure_06.png`: \(d\tau^2=dt^2-dx^2-\cdots\) [visible]
- `lecture_04_figure_06.png`: \(\tau^2=t^2-x^2-y^2-z^2\) [visible]
- `lecture_04_figure_06.png`: \(A^\mu(x,t)\) [visible]
- `lecture_04_figure_06.png`: \((A^0)^2-(A^x)^2-(A^y)^2-(A^z)^2\) [partially visible]
- `lecture_04_figure_06.png`: \(A_0^2-\vec A^{\,2}\) or equivalently \((A^0)^2-\vec A^{\,2}\) [standard completion]

## Diagram Extraction
- `lecture_04_figure_02.png` preserves only a fragment of the earlier particle-history sketch: a horizontal axis labeled \(t\) and a lower label \(b\). This fragment should be kept as screenshot evidence, but it is not complete enough to serve as a standalone diagram transcription.
- `lecture_04_figure_03.png` and `lecture_04_figure_05.png` preserve an important board layout rather than a geometric sketch: top line action, middle line ordinary Euler–Lagrange equation, bottom line field-theory generalization. These should be preserved as screenshots, not redrawn as faux blackboard art.
- `lecture_04_figure_04.png` does not add a distinct diagram, but it does show the board layering: the old particle formula remains visible while the lecture is verbally reinterpreting spatial-gradient terms as potential-like structure. This is screenshot-only contextual evidence.
- `lecture_04_figure_06.png` preserves a two-level board structure that matters: interval relation above, generic four-vector norm below. This should be preserved as a screenshot and paired with clean typeset equations nearby.
- No TikZ redraw is required for the five extracted frames themselves. If the final chapter adds a separate clean schematic of the particle trajectory \(\phi(t)\), it should be presented as a companion illustration, not as a claim that the extracted frame fully captured the original board sketch.

## Reconstruction Guidance
- Use `lecture_04_figure_02.png` to anchor the nonrelativistic prototype. In the notes, typeset the action, \(L=\frac{m}{2}\dot\phi^2-V(\phi)\), and the full ordinary Euler–Lagrange equation cleanly beside the screenshot; do not rely on the cropped action line alone for the coefficient of \(m\).
- Use `lecture_04_figure_03.png` and `lecture_04_figure_05.png` together to preserve the lecture’s board logic. The notes should first show the ordinary Euler–Lagrange form and then the field-theory version in explicit \(\partial/\partial x^\mu\) notation before optionally compressing to \(\partial_\mu\).
- Treat `lecture_04_figure_04.png` as corroborating context, not as the decisive source for exact field-theory notation. It is useful for narrative placement of the “kinetic minus potential” discussion, but the cleaned equations should be reconstructed from transcript-backed physics rather than from this partly occluded frame.
- Use `lecture_04_figure_06.png` as evidence for the bridge from metric to invariant quadratic forms. The notes should typeset the fully expanded interval \(d\tau^2=dt^2-dx^2-dy^2-dz^2\) and the corresponding four-vector norm in standard form beside the screenshot.
- Standardize notation where the board is inconsistent or cropped. In particular, use \(L\) for the particle Lagrangian, \(\mathcal L\) for the field-theory Lagrangian density, and keep the action symbol \(A\) when mirroring the board unless the chapter has a strong pre-existing convention.
- Prefer faithful completion over aggressive cleanup. Where the board only shows the beginning of a formula, complete it only to the extent that the transcript and standard classical field theory make the missing continuation unambiguous.

## Uncertainties
- `lecture_04_figure_02.png`: the top action integral is cropped and faint, so the coefficient of the kinetic term is less secure there than in the clearly visible central \(L=\frac{m}{2}\dot\phi^2-V(\phi)\).
- `lecture_04_figure_02.png`: the left-edge axis fragment is too incomplete to reconstruct the full particle-history sketch from the image alone.
- `lecture_04_figure_03.png`: the lower field-theory Euler–Lagrange line is only partially written and partly occluded by Susskind’s body and hand.
- `lecture_04_figure_03.png`: the argument list of \(\mathcal L\) at the top is cropped on the right, so the exact punctuation and enclosure marks should be standardized rather than copied literally.
- `lecture_04_figure_04.png`: the far-left cropped bracketed terms suggest continued squared spatial derivatives, but the exact preceding symbols are not reliably legible.
- `lecture_04_figure_04.png`: the visible \(-\partial\mathcal L/\partial\phi\) fragment is incomplete enough that it should not be treated as primary equation evidence.
- `lecture_04_figure_05.png`: the presence or absence of an explicit \(\sum_\mu\) is not fully settled by the frame because the far-left edge is cropped; the final notes should choose one convention and state it cleanly.
- `lecture_04_figure_06.png`: the upper line shows the interval pattern clearly, but not every spatial term is equally visible in that first line; the full \(dt^2-dx^2-dy^2-dz^2\) expansion is a cautious completion.
- `lecture_04_figure_06.png`: the lower quadratic form is partly occluded and cropped, so the exact superscript style on the spatial components should be standardized rather than claimed directly from the frame.
- The later transcript discussion of Lorentz transformation formulas for generic four-vectors is much less securely backed by these frames than the metric and norm relations are; those formulas should be reconstructed from the transcript only if the chapter genuinely needs them.