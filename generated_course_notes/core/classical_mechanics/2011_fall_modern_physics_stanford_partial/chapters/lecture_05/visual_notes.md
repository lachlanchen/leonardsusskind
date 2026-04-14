# Visual Evidence
## Frame Inventory

- `lecture_05_figure_02.png`: Close simple-pendulum board view showing the \(T\), \(U\), and \(\mathcal L\) lines together, with Susskind pointing at the \(+mgr\cos\theta\) term; this screenshot should remain in the final notes.
- `lecture_05_figure_03.png`: Wider simple-pendulum board view preserving the small pendulum sketch, the Lagrangian line, and the beginning of the canonical-momentum step on the lower board; this screenshot should remain in the final notes.
- `lecture_05_figure_04.png`: Double-pendulum equation board showing \(T\), \(U\), the coupled Lagrangian, and the symmetry shifts \(\theta\to\theta+\epsilon\), \(\phi\to\phi+\epsilon\); this screenshot should remain in the final notes.
- `lecture_05_figure_05.png`: Harmonic-oscillator Hamiltonian board showing canonical momentum, the \(H=P\dot x-\mathcal L\) substitution step, and a boxed simplified energy expression; this screenshot should remain in the final notes.

## Equation Extraction

- `lecture_05_figure_02.png`: \(T=\frac{m}{2}r^2\dot{\theta}^{\,2}\) [visible]
- `lecture_05_figure_02.png`: \(U=-mgr\cos\theta\) [visible]
- `lecture_05_figure_02.png`: \(\mathcal{L}=\frac{mr^2}{2}\dot{\theta}^{\,2}+mgr\cos\theta\) [visible]

- `lecture_05_figure_03.png`: \(U=-mgr\cos\theta\) [visible]
- `lecture_05_figure_03.png`: \(\mathcal{L}=\frac{mr^2}{2}\dot{\theta}^{\,2}+mgr\cos\theta\) [visible]
- `lecture_05_figure_03.png`: \(\pi_\theta=mr^2\dot{\theta}\) [partially visible]
- `lecture_05_figure_03.png`: \(\frac{d}{dt}\left(mr^2\dot{\theta}\right)=\frac{\partial\mathcal L}{\partial\theta}\) [standard completion]

- `lecture_05_figure_04.png`: \(T=mr^2\dot{\theta}^{\,2}+\frac{1}{2}mr^2\dot{\phi}^{\,2}+mr^2\dot{\theta}\dot{\phi}\cos(\theta-\phi)\) [visible]
- `lecture_05_figure_04.png`: \(U=-2mgr\cos\theta-mgr\cos\phi\) [visible]
- `lecture_05_figure_04.png`: \(\mathcal{L}=mr^2\dot{\theta}^{\,2}+\frac{1}{2}mr^2\dot{\phi}^{\,2}+mr^2\dot{\theta}\dot{\phi}\cos(\theta-\phi)+mgr(2\cos\theta+\cos\phi)\) [partially visible]
- `lecture_05_figure_04.png`: \(\theta\to\theta+\epsilon\) [visible]
- `lecture_05_figure_04.png`: \(\phi\to\phi+\epsilon\) [visible]
- `lecture_05_figure_04.png`: \(\frac{\partial\mathcal L}{\partial\theta}\) [standard completion]

- `lecture_05_figure_05.png`: \(P=\Pi_x=\frac{\partial\mathcal L}{\partial\dot x}=m\dot x\) [visible]
- `lecture_05_figure_05.png`: \(H=P\dot x-\frac{m}{2}\dot x^{\,2}+\frac{k}{2}x^2\) [partially visible]
- `lecture_05_figure_05.png`: \(H=\frac{m}{2}\dot x^{\,2}+\frac{k}{2}x^2\) [visible]
- `lecture_05_figure_05.png`: \(H=\frac{p^2}{2m}+\frac{k}{2}x^2\) [standard completion]

## Diagram Extraction

- `lecture_05_figure_02.png` contains only a cropped mnemonic pendulum sketch; it is worth preserving as a screenshot, but not sufficient by itself as the clean figure for the chapter.
- `lecture_05_figure_03.png` preserves the most useful visible pendulum geometry: pivot, rod, bob, length \(r\), and the board context around the Lagrangian; this should be shown both as the original screenshot and as a nearby clean TikZ redraw of the simple pendulum.
- `lecture_05_figure_04.png` is not a geometry figure so much as a board-layout figure: \(T\) on top, \(U\) below, \(\mathcal L\) across the middle, symmetry shifts at lower left, and a boxed expression at right; it should remain as a screenshot, while any planar double-pendulum geometry used in the notes should be redrawn separately in TikZ.
- `lecture_05_figure_05.png` is a sequencing figure rather than a diagram: the important visual fact is the order canonical momentum \(\to\) Hamiltonian substitution \(\to\) boxed simplified energy; it should remain as a screenshot, and the algebra should be re-typeset cleanly rather than redrawn as TikZ.

## Reconstruction Guidance

- Use `lecture_05_figure_02.png` as evidence for the sign structure of the simple-pendulum Lagrangian. The notes should typeset the cleaned displayed equations for \(T\), \(U\), and \(\mathcal L\), while keeping the screenshot nearby because the lecturer’s pointing gesture materially emphasizes why the final term is positive.
- Use `lecture_05_figure_03.png` as the main visual witness for the simple-pendulum board. Redraw the pendulum in TikZ with the lecture’s notation, then typeset the Lagrangian and the canonical momentum cleanly; keep the screenshot nearby so the reader can see the original board transition from setup to dynamics.
- Use `lecture_05_figure_04.png` to anchor the exact board composition of the double-pendulum section. The notes should typeset a cleaned Lagrangian and symmetry transformation lines from the visible board content, but any fully expanded Euler–Lagrange step should be reconstructed cautiously from the lecture logic rather than claimed as directly legible from the frame.
- Use `lecture_05_figure_04.png` as equation evidence, not geometry evidence. If the chapter includes a double-pendulum drawing, it should be a fresh TikZ redraw with both angles measured from the vertical, while the screenshot remains as documentary support for the coupled \(\dot\theta\dot\phi\cos(\theta-\phi)\) structure.
- Use `lecture_05_figure_05.png` to preserve the shift into Hamiltonian language. The notes should re-typeset \(P=\partial\mathcal L/\partial\dot x\), then \(H=P\dot x-\mathcal L\), and finally the simplified oscillator Hamiltonian, while retaining the screenshot because it records the board’s algebraic progression and boxed endpoint.
- In all four cases, the screenshot should not be the only presentation of the mathematics. The final notes should pair each retained frame with a clean displayed equation block or a TikZ redraw wherever the board is cropped, partially occluded, or visually noisy.

## Uncertainties

- In `lecture_05_figure_02.png`, the pendulum sketch is cropped, so the angle marker and full geometry are not reliably readable from the frame alone.
- In `lecture_05_figure_03.png`, the lower-board canonical-momentum and Euler–Lagrange lines are only partially visible, so the derivative step should be treated as a cautious standard completion.
- In `lecture_05_figure_04.png`, the coefficients in the \(U\) line are readable, but the boxed expression at the right is not reliably legible enough to transcribe with confidence.
- In `lecture_05_figure_04.png`, the frame supports the presence of the \(\cos(\theta-\phi)\) coupling and the symmetry shifts very well, but not a fully trustworthy symbol-by-symbol transcription of the later derivative step.
- In `lecture_05_figure_05.png`, the middle substitution line is partly obscured by the lecturer’s body and hand, so the clean Hamiltonian derivation should be presented as a note-quality reconstruction anchored by the clearly visible top and bottom lines.
- The transcript is useful for confirming what the board is trying to do, but the notes should avoid claiming direct visual legibility for any symbol or step that is only weakly visible in the extracted frames.