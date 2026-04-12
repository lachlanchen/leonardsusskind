# Visual Evidence

## Frame Inventory

- `lecture_05_frame_01.png` shows the early shell-spectrum sketch: two vertical columns labeled `S` and `P`, with several marked `S` levels and one marked `P` level, used while Susskind counts available one-particle states.
- `lecture_05_frame_02.png` shows a later three-column state diagram with bottom labels that appear to be \(\psi_0,\psi_1,\psi_2\), dashed horizontal level markers, and the explicit one-particle expression \(\psi_0(x_1)\) written at the right.
- `lecture_05_frame_03.png` shows the exchange-symmetry board: an upper many-particle wavefunction written in position variables, a lower many-particle wavefunction written in position-plus-spin labels, and red circles/arrows indicating interchange of the full particle labels.

## Equation Extraction

- [visible] Frame 1 column labels:
  \(S,\ P\)

- [partially visible] Frame 1 spectrum structure:
  a vertical \(S\)-column with multiple marked levels and a vertical \(P\)-column with at least one marked level.
  This is diagrammatic rather than an explicit equation.

- [partially visible] Frame 2 bottom labels most plausibly read:
  \(\psi_0,\ \psi_1,\ \psi_2\)

- [visible] Frame 2 right-hand one-particle expression:
  \(\psi_0(x_1)\)

- [partially visible] Frame 3 upper many-particle wavefunction:
  \(\Psi(x_1,x_2,x_3,\ldots)\)

- [partially visible] Frame 3 lower many-particle wavefunction with spin labels:
  \(\Psi(x_1,\sigma_1,\ x_2,\sigma_2,\ \ldots)\)

- [standard completion] The red circles and arrows in Frame 3 support the exchange of complete particle labels:
  \[
  (x_1,\sigma_1)\ \leftrightarrow\ (x_2,\sigma_2)
  \]

- [standard completion] The clean note-quality exchange statement suggested by Frame 3, but not fully written on the board in the frame, is:
  \[
  \Psi(\ldots,x_1,\sigma_1,\ldots,x_2,\sigma_2,\ldots)
  =
  \pm
  \Psi(\ldots,x_2,\sigma_2,\ldots,x_1,\sigma_1,\ldots)
  \]
  with the sign determined later in the lecture by bosonic or fermionic statistics.

## Diagram Extraction

- `lecture_05_frame_01.png` should be redrawn in TikZ as a schematic shell-spectrum figure, not preserved as a raw image. The visible content is the existence of distinct \(S\) and \(P\) columns and their relative level-counting role, not precise energy spacing.
- `lecture_05_frame_02.png` should also be redrawn in TikZ. The important structure is the board layout: three one-particle state columns, several dashed level markers, and the annotation \(\psi_0(x_1)\) indicating how a single-particle orbital becomes a factor in a many-body construction.
- `lecture_05_frame_03.png` is worth preserving as an image in the notes, because the red hand-drawn circles and arrows are part of the explanation, not just decoration. It visually conveys that exchange acts on the whole particle label, including spin, which would be less vivid if reduced to text alone.
- For a companion clean schematic, Frame 3 can also support a minimal redraw with two circled label-blocks \((x_1,\sigma_1)\) and \((x_2,\sigma_2)\) connected by swap arrows, but this should supplement rather than replace the lecture frame if space permits.

## Reconstruction Guidance

- Use Frame 1 only to support a schematic level-counting diagram. In the notes, label the columns by orbital angular momentum class (\(S\) and \(P\)), and let the transcript supply the interpretation \(l=0\) and \(l=1\); do not infer exact numerical energies from the vertical spacing.
- Do not force Frame 1 to carry more detail than it visibly contains. The later \(D\)-wave discussion belongs in the text from the transcript, but \(D\) is not visibly present in this frame and should not be claimed as frame-backed.
- In Frame 2, preserve the distinction between one-particle orbitals and many-particle wavefunctions by keeping lowercase \(\psi_n\) notation for the orbital labels. The most reliable use of the frame is to stage the move from a one-particle state \(\psi_0\) to the factor \(\psi_0(x_1)\).
- Treat the three columns in Frame 2 as a state-layout diagram, not as a quantitatively accurate spectrum. The dashed horizontal segments are best redrawn as level guides, with the transcript carrying the meaning that these are candidate one-particle states available for occupation.
- In Frame 3, preserve the uppercase \(\Psi\) notation for the many-particle wavefunction. The board strongly suggests a pedagogical sequence: first \(\Psi(x_1,x_2,x_3,\ldots)\), then the refined label structure \(\Psi(x_1,\sigma_1,x_2,\sigma_2,\ldots)\).
- The red circles in Frame 3 should be interpreted as circling whole particle-label blocks, not isolated coordinates. This aligns with the transcript’s point that once spin is included, exchange swaps everything associated with particle 1 and particle 2.
- When converting Frame 3 into clean prose or equations, keep the board’s visual logic: “exchange” is not merely \(x_1\leftrightarrow x_2\), but \((x_1,\sigma_1)\leftrightarrow(x_2,\sigma_2)\).
- If the later notes introduce explicit bosonic and fermionic symmetry equations, those equations should be typeset cleanly from the transcript and standard notation, not claimed as fully visible in these frames.
- Preserve the notation hierarchy suggested by the frames: lowercase \(\psi\) for one-particle orbitals, uppercase \(\Psi\) for many-particle wavefunctions.

## Uncertainties

- In Frame 1, the exact number of horizontal level marks is not reliable enough to support a precise occupancy count by itself; the frame should only support the existence of multiple \(S\)-levels and at least one \(P\)-level.
- In Frame 2, the bottom labels are most likely \(\psi_0,\psi_1,\psi_2\), but they are not perfectly sharp. They should be treated as probable rather than absolutely certain visual readings.
- In Frame 2, the dashed horizontal markers may indicate equal-energy guides or simply level markers across different state-columns; the frame alone does not fix that interpretation.
- In Frame 3, the upper expression is clearly a many-particle \(\Psi\), but the commas and later arguments are partly obscured; \(\Psi(x_1,x_2,x_3,\ldots)\) is a faithful reading, though not every character is equally crisp.
- In Frame 3, the lower expression is visually strong enough to support the inclusion of spin labels, but the exact punctuation and spacing should be cleaned in typesetting rather than copied literally.
- The right-hand board content in Frame 3 is cropped and should not be used for equation extraction.
- None of these frames visibly contain the later normalized symmetrized or antisymmetrized two-particle combinations; if those are written in the notes, they should be marked as transcript-backed or standard completion rather than frame-visible.
- The frames do not provide direct visual support for the later \(J_z\), \(e^{i m \theta}\), or interferometer formulas, so those should not be attributed to the attached images.