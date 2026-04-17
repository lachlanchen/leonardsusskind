# Visual Evidence
## Frame Inventory
- `lecture_08_figure_02.png`: An isolated contraction/index-pattern expression is written on a mostly blank board beside Susskind; this screenshot should remain in the final notes because it documents the Ricci-contraction board layout.
- `lecture_08_figure_03.png`: A Newtonian acceleration relation appears above a boxed metric-potential relation partly hidden by Susskind; this screenshot should remain because the box marks a pedagogical takeaway.
- `lecture_08_figure_04.png`: A compact vertical cluster of Newtonian field equations is visible, moving from acceleration field to divergence law to Poisson equation; this screenshot should remain as evidence of the board sequence.
- `lecture_08_figure_05.png`: The same cluster is extended by the identification with `T^{00}` and a lower line for `g_{00}`; this screenshot should remain because it captures the weak-field bridge to stress-energy.
- `lecture_08_figure_06.png`: A wider board view shows the weak-field equations on the left and the beginning of a coordinate Laplacian expansion plus stress-energy matrix entries on the right; this screenshot should remain because it preserves the split-board transition toward a tensor equation.

## Equation Extraction
- `lecture_08_figure_02.png`: `\delta V^\alpha` [partially visible]
- `lecture_08_figure_02.png`: `g^{\alpha\nu}` [visible]
- `lecture_08_figure_02.png`: `R_{\mu\nu}{}^{\alpha}{}_{\beta}` [partially visible]
- `lecture_08_figure_02.png`: `g^{\alpha\nu} R_{\mu\nu\alpha\beta}` [standard completion]

- `lecture_08_figure_03.png`: `\frac{d^2 x}{dt^2}` [visible]
- `lecture_08_figure_03.png`: `\frac{\partial \phi}{\partial x}` [visible]
- `lecture_08_figure_03.png`: `\frac{d^2 x}{dt^2} = -\frac{\partial \phi}{\partial x}` [standard completion]
- `lecture_08_figure_03.png`: `g_{00} = 2\phi + c` [standard completion]

- `lecture_08_figure_04.png`: `\vec A(x) = \frac{\partial \phi}{\partial x}` [partially visible]
- `lecture_08_figure_04.png`: `\nabla \cdot A = -4\pi \rho G` [visible]
- `lecture_08_figure_04.png`: `\nabla^2 \phi = 4\pi \rho G` [standard completion]

- `lecture_08_figure_05.png`: `\vec A(x) = \frac{\partial \phi}{\partial x}` [partially visible]
- `lecture_08_figure_05.png`: `\nabla \cdot A = -4\pi \rho G` [visible]
- `lecture_08_figure_05.png`: `\nabla^2 \phi = 4\pi \rho G = 4\pi G T^{00}` [visible]
- `lecture_08_figure_05.png`: `\nabla^2 g_{00} = 8\pi G T^{00}` [visible]

- `lecture_08_figure_06.png`: `\vec A(x) = \frac{\partial \phi}{\partial x}` [partially visible]
- `lecture_08_figure_06.png`: `\nabla \cdot A = -4\pi \rho G` [visible]
- `lecture_08_figure_06.png`: `\nabla^2 \phi = 4\pi \rho G = 4\pi G T^{00}` [visible]
- `lecture_08_figure_06.png`: `\nabla^2 g_{00} = 8\pi G T^{00}` [visible]
- `lecture_08_figure_06.png`: `\frac{\partial^2 \phi}{\partial x^2} + \frac{\partial^2 \phi}{\partial y^2} + \frac{\partial^2 \phi}{\partial z^2}` [partially visible]
- `lecture_08_figure_06.png`: `T^{00}` [visible]
- `lecture_08_figure_06.png`: `T^{01}` [visible]
- `lecture_08_figure_06.png`: `T^{10}` [visible]

## Diagram Extraction
- `lecture_08_figure_02.png`: No geometric diagram is present. This should be preserved as a screenshot, not redrawn in TikZ, because its value is the spacing and isolation of the contraction notation on the board.
- `lecture_08_figure_03.png`: No standalone diagram is present, but the two-level layout matters: the upper acceleration law and the lower boxed metric relation. Preserve as a screenshot and also typeset the cleaned equations nearby.
- `lecture_08_figure_04.png`: No TikZ figure is needed. The important “diagram” here is really the vertical board progression from field definition to divergence law to Poisson equation, so the screenshot should be kept.
- `lecture_08_figure_05.png`: Again, not a true diagram; preserve as a screenshot because it visually shows the insertion of `T^{00}` into the left-hand cluster and the separate lower line for `g_{00}`.
- `lecture_08_figure_06.png`: The split-board structure matters more than any individual symbol. Preserve as a screenshot; the stress-energy matrix should be typeset cleanly as a LaTeX array rather than redrawn in TikZ.
- For this particular frame set, no idea requires TikZ. These images are board-layout evidence for equations, not genuine sketches or geometric constructions.

## Reconstruction Guidance
- Use `lecture_08_figure_02.png` to justify a clean Ricci-contraction equation in the notes, but do not force a literal transcription of every index from the screenshot. The screenshot should sit next to the standard cleaned contraction, since the exact index placement is only partly legible.
- Use `lecture_08_figure_03.png` to support two separate displayed equations: the Newtonian acceleration law and the boxed relation between `g_{00}` and `\phi`. The screenshot should remain visible because the box itself is part of the lecture’s emphasis.
- Use `lecture_08_figure_04.png` and `lecture_08_figure_05.png` to reconstruct the Newtonian field sequence as polished displayed equations. Keep both screenshots nearby when the notes move from the acceleration field to Poisson’s equation and then to the `T^{00}` identification.
- Use `lecture_08_figure_06.png` when the notes transition from the weak-field scalar equation to the search for a full tensor equation. Typeset the coordinate Laplacian expansion and the opening entries of `T^{\mu\nu}` cleanly beside the screenshot.
- Where a line is partly hidden or visually weak, prefer transcript-guided standard completion in the typeset notes, but leave the screenshot in place as evidence of board ordering and emphasis.
- Avoid over-interpreting the screenshots as sole authorities on signs. In this lecture the weak-field/Newtonian sign bookkeeping is visibly unstable, so the final equations in the notes should be cleaned cautiously and the prose should acknowledge the sign trouble where relevant.

## Uncertainties
- In `lecture_08_figure_02.png`, the exact placement of the raised and lowered indices on the Riemann tensor is not reliably legible.
- In `lecture_08_figure_03.png`, the left-hand side of the boxed relation is blocked by Susskind, and the sign in the acceleration equation is not visually decisive on its own.
- In `lecture_08_figure_04.png`, the top line involving `A(x)` and `\phi` is only partly legible, including the possible sign and whether the notation is vectorial or one-dimensional shorthand.
- In `lecture_08_figure_04.png` and `lecture_08_figure_05.png`, the sign in the Poisson-style equation should be treated cautiously; the board and the lecture both wobble on sign conventions.
- In `lecture_08_figure_05.png`, the `00` indices on the stress-energy term are clear, but the frame alone does not completely settle raised-versus-lowered placement at every occurrence.
- In `lecture_08_figure_06.png`, the upper-right coordinate expansion is cropped, so the differentiated object and the full sum are not fully secure from the image alone.
- In `lecture_08_figure_06.png`, only the first few stress-energy matrix entries are visible; the full matrix should not be presented as if it were fully shown in the frame.