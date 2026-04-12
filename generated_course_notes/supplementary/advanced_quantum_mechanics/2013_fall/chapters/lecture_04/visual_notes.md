# Visual Evidence
## Frame Inventory
- `lecture_04_frame_01.png`: Partially obstructed board showing the explicit matrix products used to compare \(\sigma_z\sigma_x\) and \(\sigma_x\sigma_z\) and identify the Pauli-matrix commutator.
- `lecture_04_frame_02.png`: Clear summary board for spin-\(\tfrac12\), with the three matrices \(\sigma_i/2\), the corrected commutator in \(S\)-notation, and the total angular momentum relation \(J=L+S\).
- `lecture_04_frame_03.png`: Schematic hydrogen/orbital-angular-momentum board showing \(L^2=\ell(\ell+1)\), the multiplicity reminder \(2\ell+1\), and an \(E\)-versus-\(\ell\) sketch centered on the \(\ell=0\) tower.

## Equation Extraction
- [visible] `lecture_04_frame_01.png`: \(\begin{pmatrix}1&0\\0&-1\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix}=\begin{pmatrix}0&1\\-1&0\end{pmatrix}\).
- [standard completion] `lecture_04_frame_01.png`: \(\sigma_z\sigma_x=i\sigma_y\).
- [partially visible] `lecture_04_frame_01.png`: \(\begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}1&0\\0&-1\end{pmatrix}=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\).
- [standard completion] `lecture_04_frame_01.png`: \(\sigma_x\sigma_z=-i\sigma_y\).
- [standard completion] `lecture_04_frame_01.png`: \([\sigma_z,\sigma_x]=2i\sigma_y\).

- [visible] `lecture_04_frame_02.png`: \(\dfrac{\sigma_z}{2}=\begin{pmatrix}\tfrac12&0\\0&-\tfrac12\end{pmatrix}\).
- [visible] `lecture_04_frame_02.png`: \(\dfrac{\sigma_x}{2}=\begin{pmatrix}0&\tfrac12\\ \tfrac12&0\end{pmatrix}\).
- [visible] `lecture_04_frame_02.png`: \(\dfrac{\sigma_y}{2}=\begin{pmatrix}0&-\tfrac{i}{2}\\ \tfrac{i}{2}&0\end{pmatrix}\).
- [standard completion] `lecture_04_frame_02.png`: \(\left[\dfrac{\sigma_z}{2},\dfrac{\sigma_x}{2}\right]=i\,\dfrac{\sigma_y}{2}\).
- [visible] `lecture_04_frame_02.png`: \(S=\dfrac{\sigma}{2}\).
- [standard completion] `lecture_04_frame_02.png`: \(S_i=\dfrac{\sigma_i}{2}\).
- [visible] `lecture_04_frame_02.png`: \([S_z,S_x]=iS_y\).
- [visible] `lecture_04_frame_02.png`: \(J=L+S\).

- [visible] `lecture_04_frame_03.png`: \(L^2=\ell(\ell+1)\).
- [visible] `lecture_04_frame_03.png`: \(2\ell+1\).
- [visible] `lecture_04_frame_03.png`: axis labels \(E\) and \(\ell\), with \(\ell=0\) marked at the first column of the level sketch.
- [partially visible] `lecture_04_frame_03.png`: a stack of bound-state marks at \(\ell=0\), getting denser upward toward the top of the plot.
- [standard completion] `lecture_04_frame_03.png`: the handwritten \(2\ell+1\) is the reminder that a fixed orbital-angular-momentum multiplet has degeneracy \(2\ell+1\).

## Diagram Extraction
- `lecture_04_frame_01.png` should not be kept as a printed figure; it is best used as a TikZ/LaTeX reference for the two matrix multiplications leading to the Pauli commutator.
- `lecture_04_frame_02.png` is the only frame that is strong enough to preserve as an actual lecture-board image if a documentary figure is desired; it also serves as the best layout reference for a clean redraw with the three \(\sigma_i/2\) matrices in the left column and the commutator plus \(J=L+S\) in the right column.
- `lecture_04_frame_03.png` should be redrawn in TikZ as a schematic spectrum, not kept as a photo. The redraw should preserve the board logic: side reminders \(L^2=\ell(\ell+1)\) and \(2\ell+1\), vertical axis \(E\), horizontal axis \(\ell\), and the \(\ell=0\) tower of radial excitations.
- The late-hydrogen sketch in `lecture_04_frame_03.png` is only the beginning of the full degeneracy story. The later \(\ell=1\) and \(\ell=2\) columns and their alignments should be added from the transcript, not claimed as directly visible in this still.

## Reconstruction Guidance
- Use `lecture_04_frame_01.png` to preserve the lecture’s actual route through the calculation: explicit products first, commutator second, normalization fix third. In the notes, typeset the matrix products cleanly and then give the compact identities \(\sigma_z\sigma_x=i\sigma_y\), \(\sigma_x\sigma_z=-i\sigma_y\), and \([\sigma_z,\sigma_x]=2i\sigma_y\).
- Use `lecture_04_frame_02.png` as the canonical board summary for the spin section. The visible structure should be preserved: left column for the three component matrices, right column for the algebraic consequence and then the physical identification \(J=L+S\).
- When turning the board shorthand \(S=\sigma/2\) into note-quality mathematics, rewrite it as the componentwise statement \(S_i=\sigma_i/2\). That is the mathematically clean version of what is written on the board.
- In `lecture_04_frame_03.png`, redraw the spectrum schematically rather than metrically. The frame supports axis placement, the \(\ell=0\) label, and the existence of a tower of states, but not precise spacings.
- Typeset the orbital quantum number as \(\ell\), not handwritten \(l\), to avoid confusion with the numeral \(1\).
- Keep the lecture’s convention in mind: the board is using \(\hbar=1\)-style notation in this segment, so \(L^2=\ell(\ell+1)\) is the lecture convention, not the fully restored \(\hbar^2\ell(\ell+1)\) form.
- Do not use these frames to invent missing harmonic-oscillator formulas. The attached images only support the spin algebra and hydrogen-shell sketch, not the earlier oscillator derivations.

## Uncertainties
- In `lecture_04_frame_01.png`, the top leftover commutator line is cut off and cannot be transcribed reliably from the image alone.
- In `lecture_04_frame_01.png`, the lower matrix product is partly blocked by Susskind’s body and shadow; the sign structure is recoverable, but the frame is not clean enough to stand alone without standard completion.
- In `lecture_04_frame_02.png`, the top-right intermediate line is faint enough that the denominator on the right-hand side is best treated as reconstructed rather than fully legible; the transcript and the surrounding board make \(i\sigma_y/2\) the safe completion.
- In `lecture_04_frame_02.png`, \(S=\sigma/2\) is handwritten as shorthand, without explicit component indices or vector notation.
- In `lecture_04_frame_03.png`, only the \(\ell=0\) part of the spectrum is clearly established in the still; the later \(\ell=1\) and \(\ell=2\) degeneracy pattern discussed in the transcript is not fully visible here.
- In `lecture_04_frame_03.png`, the isolated mark to the right of the \(\ell=0\) column is not by itself enough to reconstruct the full next column without the transcript.
- No frame here provides direct visual support for the harmonic-oscillator equations, the Gaussian \(\psi_0\), or the first-excited-state wavefunction; those must come from the transcript, not from the images.