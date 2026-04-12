# Visual Evidence

## Frame Inventory
- `lecture_07_frame_01.png`: shows the qualitative particle-in-a-box sketch with two visible mode shapes inside the well and the labels `\psi_1(x)`, `\psi_2(x)`, and `\psi_i(x)`, while the left side only preserves cropped remnants of earlier probability-density writing.
- `lecture_07_frame_02.png`: shows the one-particle time-independent Schrödinger equation, the operator identification `P=-i\,\partial/\partial x`, and the lower three-dimensional rewrite with `-\nabla^2/2m`.
- `lecture_07_frame_03.png`: shows a partially cropped and partly obstructed board where the total energy is written as an integral of a local field expression, with a lower line beginning the mode-expansion derivation.

## Equation Extraction
- From `lecture_07_frame_01.png`
  - [visible] `\psi_1(x),\ \psi_2(x),\ \psi_i(x)` appear explicitly as labels beside the sketched eigenfunctions.
  - [partially visible] The left-board fragments appear to contain something like `\psi^*(x)\psi(x)` and the words `\text{Prob dens}`, but they are too cropped to serve as reliable final equations.

- From `lecture_07_frame_02.png`
  - [visible] `\left[\frac{P^2}{2m}+V(x)\right]\psi_i(x)=\omega_i\psi_i(x)`
  - [visible] `P=-i\,\frac{\partial}{\partial x}`
  - [visible] `\left[-\frac{\nabla^2}{2m}+V(x)\right]\psi_i=\omega_i\psi_i`
  - [standard completion] `\left[-\frac{\nabla^2}{2m}+V(x)\right]\psi_i(x)=\omega_i\psi_i(x)` is the clean note version consistent with the transcript’s verbal explanation.

- From `lecture_07_frame_03.png`
  - [partially visible] `E=\int dx\,\Psi^\dagger(x)\left(-\frac{\nabla^2}{2m}+V(x)\right)\cdots`
  - [standard completion] `E=\int dx\,\Psi^\dagger(x)\left(-\frac{\nabla^2}{2m}+V(x)\right)\Psi(x)` is the cautious completion supported jointly by the frame and the transcript.
  - [partially visible] The lower derivation line visibly begins with something of the form `\sum_i a_i^\dagger \psi_i^*(x)` before continuing into the same differential operator and a second factor that is cropped out.

## Diagram Extraction
- `lecture_07_frame_01.png` should be redrawn in TikZ as a clean infinite-well schematic with vertical confining walls, a horizontal reference line, and the first two qualitative eigenfunctions. The important content is node counting and labeling, not the exact hand-drawn amplitudes.
- `lecture_07_frame_02.png` is not a figure to preserve as an image; it is a board-layout reference for a three-line derivation: one-particle eigenvalue equation on top, momentum operator in the middle, and the three-dimensional form below.
- `lecture_07_frame_03.png` should not be preserved as a final image; it is a layout reference for the Hamiltonian/energy-density display. The pedagogically important structure is “integral over space of a local quadratic field expression,” with the upper line giving the final result and the lower line hinting at the mode-expansion proof.
- If a raw lecture still is kept anywhere, `lecture_07_frame_01.png` is the only plausible candidate; the other two are better converted into clean typeset equations.

## Reconstruction Guidance
- Use `lecture_07_frame_01.png` only to preserve the qualitative shape of the well and the ordering of the first two modes. The notes should present a clean schematic and explain that the modes are “basically sines” and are organized by node count, exactly as Susskind says in the transcript.
- Do not promote the cropped left-hand writing in `lecture_07_frame_01.png` into formal equations. For probability density and orthonormality, rely on the transcript rather than the partial board remnants.
- Typeset the equations from `lecture_07_frame_02.png` cleanly and consistently. The board uses uppercase `P`; for polished notes you can keep `P` to match the lecture or switch to `\hat p`/`p`, but the choice should be made once and then kept consistent.
- In the lower equation from `lecture_07_frame_02.png`, restore the omitted function arguments as `\psi_i(x)` using the transcript, not guesswork from the board.
- `lecture_07_frame_03.png` should be used to preserve the form and emphasis of the local Hamiltonian density, not to recover every algebraic detail of the proof. The transcript supplies the missing rightmost factor `\Psi(x)` and the interpretation as both total energy and Hamiltonian.
- For note-quality presentation, it is reasonable to mention that Susskind writes `\int dx` even after promoting the kinetic term to `-\nabla^2/2m`; if the chapter switches to explicit three-dimensional notation such as `\int d^3x`, that should be flagged as a notation cleanup rather than something directly written on the board.
- The lower line in `lecture_07_frame_03.png` should only support a cautious statement that the derivation proceeds by inserting the mode expansions of `\Psi^\dagger(x)` and `\Psi(x)`. The exact index order and intermediate factors should come from the transcript.

## Uncertainties
- The left side of `lecture_07_frame_01.png` is too cropped to trust as a literal transcription; it should not be used to reconstruct the probability-density or normalization formulas.
- In `lecture_07_frame_02.png`, the handwriting makes upper/lowercase psi somewhat ambiguous, but the transcript makes clear that this board is about one-particle wavefunctions `\psi_i(x)`, not field operators `\Psi(x)`.
- In the lower equation of `lecture_07_frame_02.png`, the explicit `(x)` arguments are not cleanly visible on both sides, so they should be restored from the transcript.
- In `lecture_07_frame_03.png`, the far-right factor after `\left(-\nabla^2/2m+V(x)\right)` is off-frame; completing it as `\Psi(x)` is justified by the transcript but not fully visible in the image itself.
- The lower derivation line in `lecture_07_frame_03.png` is both cropped and blocked by Susskind, so the full expanded expression cannot be transcribed reliably from the frame alone.
- The frame shows `E=` on the board, while the transcript verbally shifts between “energy” and “Hamiltonian”; the notes should explain that in this context he is identifying the Hamiltonian operator with the total energy operator.
- The red oval in `lecture_07_frame_03.png` is emphasis, not mathematics; it should not be transcribed as part of the formula.
- Nothing in the three frames directly settles operator-ordering issues, commutators, or zero-point-energy terms; those topics should not be reconstructed from the images alone.