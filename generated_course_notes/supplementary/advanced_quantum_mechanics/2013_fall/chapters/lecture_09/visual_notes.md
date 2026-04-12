# Visual Evidence
## Frame Inventory
- `lecture_09_frame_01.png` shows the early nonrelativistic field Hamiltonian board, with the kinetic operator and the added potential-density term visible but the far-left part of the expression cropped off.
- `lecture_09_frame_02.png` shows the short-range electron-proton interaction discussion: a local four-field operator on the left board, a spacetime scattering sketch below it, and older momentum-space formulas still lingering on the right boards.
- `lecture_09_frame_03.png` shows the cleanest one-dimensional Dirac board, with `H=\alpha P` and the two-component massless equation written explicitly in matrix form.
- `lecture_09_frame_04.png` shows the later Dirac algebra board, including `P=E` on the left and, most importantly, the conditions on `\alpha` and `\beta` on the right.

## Equation Extraction
- [partially visible] From `lecture_09_frame_01.png`, the visible part of the integrand is approximately
  $-\dfrac{\nabla^2}{2m}\,\psi(x) + V(x)\psi^\dagger(x)\psi(x)$.
- [standard completion] Using the transcript to restore the cropped left side, the intended full Hamiltonian is
  $H=\int dx\,\psi^\dagger(x)\left(-\dfrac{\nabla^2}{2m}+V(x)\right)\psi(x)$.
- [partially visible] From `lecture_09_frame_02.png`, the left board clearly contains a local four-field product with electron and proton labels, of the form
  $\int dx\,\psi_e^\dagger(x)\psi_p^\dagger(x)\psi_e(x)\psi_p(x)$.
- [standard completion] The transcript supports reading that term as the toy short-range contact interaction
  $H_{\text{int}} \propto \int dx\,\psi_e^\dagger(x)\psi_p^\dagger(x)\psi_e(x)\psi_p(x)$.
- [visible] From `lecture_09_frame_03.png`,
  $H=\alpha P$.
- [visible] From `lecture_09_frame_03.png`,
  $i\,\dfrac{\partial}{\partial t}\begin{pmatrix}\psi_1\\ \psi_2\end{pmatrix}
  =
  -\,i
  \begin{pmatrix}
  1 & 0\\
  0 & -1
  \end{pmatrix}
  \dfrac{\partial}{\partial x}
  \begin{pmatrix}\psi_1\\ \psi_2\end{pmatrix}$.
- [standard completion] The condensed form stated in the transcript is
  $i\,\partial_t\psi=-\,i\,\alpha\,\partial_x\psi$,
  where $\psi$ is the two-component column vector.
- [partially visible] From `lecture_09_frame_04.png`,
  $P=E$.
- [visible] From `lecture_09_frame_04.png`,
  $\alpha^2=1$.
- [visible] From `lecture_09_frame_04.png`,
  $\beta^2=1$.
- [visible] From `lecture_09_frame_04.png`,
  $\alpha\beta+\beta\alpha=0$.
- [standard completion] The transcript later resolves the matrix choice as
  $\beta=\begin{pmatrix}0&1\\1&0\end{pmatrix}$,
  with $\alpha=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$ already visible in frame 3.

## Diagram Extraction
- `lecture_09_frame_01.png`: no standalone figure is worth preserving as a photograph; it is best used as a reference for typesetting the early Hamiltonian with the potential term.
- `lecture_09_frame_02.png`: redraw the spacetime sketch in TikZ. The diagram should have time vertical, space horizontal, one electron line and one proton line meeting at a single point, then emerging again as scattered outgoing lines.
- `lecture_09_frame_02.png`: pair that sketch with the local contact operator, since the lecture explicitly uses the picture to explain why the product of fields represents short-range scattering at the same point.
- `lecture_09_frame_03.png`: this is the only frame that can reasonably be kept as an image figure, because the board is centered and the matrix equation is legible enough to stand on its own.
- `lecture_09_frame_04.png`: redraw the algebra block in clean typeset form rather than keeping the image; the speaker obstructs too much of the board for a polished final figure.

## Reconstruction Guidance
- For the early Hamiltonian, use `lecture_09_frame_01.png` only to preserve board ordering and the visual fact that the potential term is written as $V(x)\psi^\dagger(x)\psi(x)$. Restore the missing outer $\psi^\dagger(x)$ and integral from the transcript, not from guesswork.
- For the contact interaction, trust the transcript for the exact operator order and particle labels, and use `lecture_09_frame_02.png` mainly for the local-vertex picture. The note-quality version should be a clean formula plus a redrawn spacetime sketch.
- Do not try to salvage the extra momentum-space formulas still visible on the right side of `lecture_09_frame_02.png` unless they are independently needed and cross-checked against the transcript; they belong to an earlier board state and are too cropped for safe transcription.
- For the Dirac section, `lecture_09_frame_03.png` is strong enough to anchor both the matrix $\alpha=\mathrm{diag}(1,-1)$ and the explicit two-component equation. The notes can then introduce the condensed form $i\partial_t\psi=-i\alpha\partial_x\psi$.
- For the mass term, use `lecture_09_frame_04.png` to preserve the algebraic logic, not the exact board layout. Present the three conditions $\alpha^2=1$, $\beta^2=1$, and $\alpha\beta+\beta\alpha=0$ first, and only then adopt the transcript-backed choice $\beta=\sigma_1$.
- Keep the notation split clear in the notes: early $\psi(x)$ is a field operator, while later $\psi=\begin{pmatrix}\psi_1\\ \psi_2\end{pmatrix}$ is a two-component wavefunction. The lecture visually reuses the same symbol, but the written notes should distinguish the contexts carefully.

## Uncertainties
- In `lecture_09_frame_01.png`, the full left side of the Hamiltonian is cropped away, so the integral sign and the outer $\psi^\dagger(x)$ are not directly visible in the still.
- In `lecture_09_frame_01.png`, the board glyph looks like a capital-style psi, but the transcript consistently describes the field as $\psi$; the notes should normalize this rather than preserving the handwritten ambiguity.
- In `lecture_09_frame_02.png`, the exact order of the final two fields in the four-field product is not perfectly legible from the image alone, even though the transcript resolves the intended operator sequence.
- In `lecture_09_frame_02.png`, the right-board formulas involving $-\nabla^2\psi^\dagger(x)$ and momentum-space operators are too incomplete to quote safely, especially with coefficients and dummy variables.
- In `lecture_09_frame_03.png`, the far-right repeated column vector after $\partial_x$ is partly cut off, so the transcript should be used to confirm that the derivative acts on the same two-component column.
- In `lecture_09_frame_04.png`, the right-hand side of the anticommutator relation is partly obscured by the lecturer’s arm; the transcript is needed to fix it as zero.
- In `lecture_09_frame_04.png`, the left side contains remnants of earlier equations, but they are not clean enough to support a reliable transcription beyond the visible `P=E`.
- The frames do not visibly show the later choice of $\beta=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, the component massive Dirac equations, or the full one-dimensional Dirac equation with the mass term; those require cautious transcript-backed reconstruction rather than frame-only extraction.