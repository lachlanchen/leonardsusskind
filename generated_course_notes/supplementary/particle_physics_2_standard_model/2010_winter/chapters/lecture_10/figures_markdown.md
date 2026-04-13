# Figure Notes
## Image Inventory
- `lecture_10_figure_02.png`: Susskind stands at the left side of the board while a long top-line expression in the older \(\alpha,\beta\) Dirac notation runs across the chalkboard and ends with an equality to the Lagrangian symbol. A small forked chalk mark sits below the line.
- `lecture_10_figure_03.png`: A clean board-only frame showing the same Dirac-Lagrangian discussion after it has been rewritten into a more compact barred-spinor, gamma-matrix form. Older \(\alpha,\beta\) notation remains faintly visible above.
- `lecture_10_figure_04.png`: Susskind stands at the left edge while the board now focuses on the mass term split into left- and right-handed pieces. The top line is the key content; beneath it is a simple branching chalk doodle, with older faint writing lower down.
- `lecture_10_figure_05.png`: The board combines three elements at once: a top-line chiral/Higgs coupling expression, a small central branching sketch labeled by left/right and \(\phi\), and a large double-well potential sketch on the right that serves as the visual cue for the Mexican-hat discussion.

## Blackboard Equations
- `lecture_10_figure_02.png`: \(\psi^\dagger(\cdots + \alpha_i \partial_i \psi - \beta m \psi)=\mathcal{L}\) [partially visible]
- `lecture_10_figure_02.png`: \(\beta m\psi\) [visible]
- `lecture_10_figure_02.png`: \(\mathcal{L}\) [visible]

- `lecture_10_figure_03.png`: \(\bar{\psi}(\gamma^\mu \partial_\mu + m)\psi\) [visible]
- `lecture_10_figure_03.png`: \(m\bar{\psi}\psi\) [visible]
- `lecture_10_figure_03.png`: \(\bar{\psi}\gamma_i\partial_i\psi\) [partially visible]
- `lecture_10_figure_03.png`: \(\bar{\psi}(i\gamma^\mu\partial_\mu - m)\psi\) [standard reconstruction]

- `lecture_10_figure_04.png`: \(\bar{\psi}\psi=\psi_L^\dagger\psi_R+\psi_R^\dagger\psi_L\) [partially visible]
- `lecture_10_figure_04.png`: \(\psi_L,\ \psi_R\) [visible]

- `lecture_10_figure_05.png`: \(\bar{\psi}\psi=\psi_L^\dagger\phi\,\psi_R+\psi_R^\dagger\phi^\dagger\psi_L\) [partially visible]
- `lecture_10_figure_05.png`: \(\phi\) [visible]
- `lecture_10_figure_05.png`: \(L,\ R\) [visible]

## Diagram And Layout Reading
- `lecture_10_figure_02.png` is organized as a single long board line. The important layout feature is that the lecture is still in the older Dirac \(\alpha,\beta\) notation, before the covariant \(\gamma^\mu\) rewrite has been cleaned up. The small forked chalk mark under the equation looks like a mnemonic pointer rather than a formal diagram.
- `lecture_10_figure_03.png` is a conversion board. The upper remnants preserve the older \(\beta m\psi\) presentation, while the lower line compresses the result into a barred-spinor form. The spatial organization itself helps the notes: the lecture is visibly moving from the older notation to the more elegant covariant one.
- `lecture_10_figure_04.png` is a focused board for the chirality point. The top line is the content that matters: the scalar bilinear is being decomposed into left-right mixing pieces. The branching doodle below is not a proper Feynman diagram; it functions more like a quick visual reminder that the term connects two distinct chiral sectors.
- `lecture_10_figure_05.png` is the richest visual record. The top equation extends the left-right mixing story by inserting the Higgs field \(\phi\). The central little sketch, labeled \(L\), \(R\), and \(\phi\), is again a mnemonic Yukawa-style coupling picture rather than a precise diagram. On the right, the large curve is a one-dimensional cross-section through the symmetry-breaking potential: two minima separated by a central hump, with no axes or labels written. It is better read as a radial slice of the Mexican hat than as a full two-dimensional surface.

## TeX Reconstruction Plan
- `lecture_10_figure_02.png` must remain visible. It should be paired with a cleaned displayed equation in the older notation, reconstructed from the transcript rather than the board alone, e.g. the Dirac equation multiplied by \(\psi^\dagger\) to form the Lagrangian. The screenshot is evidence of the board layout; the equation nearby should do the mathematical heavy lifting.
- `lecture_10_figure_03.png` must remain visible. It should sit next to a clean typeset covariant form of the Dirac Lagrangian, with the notes explicitly standardizing the sign and \(i\)-factor conventions from the transcript. The screenshot shows the transition in notation; the typeset equation should state the final cleaned form.
- `lecture_10_figure_04.png` must remain visible. The notes should reconstruct the chiral mass decomposition as a displayed equation nearby. No TikZ redraw is necessary unless the chapter later wants a tiny schematic for left-right mixing; the screenshot already preserves the board emphasis.
- `lecture_10_figure_05.png` must remain visible. It should be paired with two reconstructed elements nearby: a clean displayed Yukawa-style left-right coupling involving \(\phi\), and a TikZ redraw of the right-hand double-well potential as a clear one-dimensional symmetry-breaking cross-section. If the small \(L/R/\phi\) chalk doodle is used pedagogically, it may also be redrawn as a minimal schematic, but the main redraw priority is the potential curve.
- Across all four figures, the screenshots should be treated as visual evidence of lecture flow and board organization, while the final displayed equations in the notes should be transcript-controlled and notation-stabilized.

## Caption Drafts
- `lecture_10_figure_02.png`: Dirac Lagrangian in \(\alpha,\beta\) notation.
- `lecture_10_figure_03.png`: Covariant gamma-matrix form of the Dirac Lagrangian.
- `lecture_10_figure_04.png`: Left-right decomposition of the Dirac mass term.
- `lecture_10_figure_05.png`: Higgs-inserted chiral coupling and double-well potential.

## Uncertainties
- In `lecture_10_figure_02.png`, the beginning of the long line is partly cropped and the exact placement of the time-derivative term is not securely legible from the frame alone. The overall \(i\)-factor convention should be taken from the transcript, not the chalk.
- In `lecture_10_figure_03.png`, the compact form on the right is structurally clear, but the board does not reliably settle the standard sign choice or the explicit \(i\) in front of \(\gamma^\mu\partial_\mu\). This is a classic place where transcript-guided standard reconstruction is needed.
- In `lecture_10_figure_04.png`, the first left-right term is clearer than the second; the second summand is faint and partly off toward the right, so the full symmetric decomposition should be reconstructed cautiously from the transcript.
- In `lecture_10_figure_05.png`, the top-line Higgs insertion is only partially legible, especially on the far right. The image strongly supports the presence of \(\phi\) mediating between \(L\) and \(R\), but the exact dagger/star notation on the second term should be transcript-controlled.
- Also in `lecture_10_figure_05.png`, the potential sketch has no axes, labels, or algebra attached to it. It is reliable as a qualitative shape only: two minima and a central barrier. Any labeled TikZ redraw should therefore stay minimal and avoid overcommitting beyond what the screenshot actually shows.
- The forked or branching chalk marks in `lecture_10_figure_02.png`, `lecture_10_figure_04.png`, and `lecture_10_figure_05.png` appear to be quick explanatory doodles rather than fully specified mathematical diagrams. They should not be overinterpreted.