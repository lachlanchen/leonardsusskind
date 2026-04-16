# Visual Evidence
## Frame Inventory
- `lecture_04_figure_02.png`: This frame shows the three-step blackboard derivation from the Lagrange-multiplier stationarity condition to the boxed Boltzmann probability, and it should remain as a screenshot in the final notes.
- `lecture_04_figure_03.png`: This frame shows the right-hand board with the thermodynamic chain \(dE=T\,dS\), \(dE/dS=T\), \(1/T=dS/dE\), plus a cropped entropy formula above, and it should remain as a screenshot in the final notes.
- `lecture_04_figure_04.png`: This frame shows the ideal-gas energy extraction from the \(\beta\)-dependence of \(\log z\), with the left-hand partition-function factor and the right-hand energy summary both visible, and it should remain as a screenshot in the final notes.

## Equation Extraction
- `lecture_04_figure_02.png`: [partially visible] \(\dfrac{\partial F'}{\partial P_i}=\log P_i+1+\alpha+\beta E_i=0\)
- `lecture_04_figure_02.png`: [visible] \(\log P_i=-(1+\alpha)-\beta E_i\)
- `lecture_04_figure_02.png`: [visible] \(P_i=\dfrac{1}{Z}e^{-\beta E_i}\)
- `lecture_04_figure_03.png`: [partially visible] \(S=\beta E+\log z(\beta)\)
- `lecture_04_figure_03.png`: [visible] \(dE=T\,dS\)
- `lecture_04_figure_03.png`: [visible] \(\dfrac{dE}{dS}=T\)
- `lecture_04_figure_03.png`: [visible] \(\dfrac{1}{T}=\dfrac{dS}{dE}\)
- `lecture_04_figure_04.png`: [partially visible] \(\left(\dfrac{2m\pi}{\beta}\right)^{3N/2}\)
- `lecture_04_figure_04.png`: [partially visible] \(\log z=-\dfrac{3N}{2}\log\beta+\mathrm{const}\)
- `lecture_04_figure_04.png`: [visible] \(-\dfrac{\partial\log z}{\partial\beta}=+\dfrac{3N}{2}T\)
- `lecture_04_figure_04.png`: [standard completion] \(E=-\dfrac{d\log z}{d\beta}\)

## Diagram Extraction
- `lecture_04_figure_02.png`: There is no standalone diagram here; the important visual structure is the top-to-bottom derivation ending in a boxed final formula, so it should be preserved as a screenshot rather than redrawn.
- `lecture_04_figure_03.png`: There is no geometric figure here; the important visual structure is the vertical stacking of the three thermodynamic identities, with the cropped entropy box above them, so it should be preserved as a screenshot rather than redrawn.
- `lecture_04_figure_04.png`: There is no genuine graph or physical sketch here; the important visual structure is the split board layout, with the left-hand \(\beta\)-dependence of the partition function feeding the right-hand energy result, so it should be preserved as a screenshot rather than redrawn.
- Across all three frames, no TikZ redraw is required for the visible content itself; clean display equations are more faithful than trying to imitate the blackboard layout.

## Reconstruction Guidance
- Use `lecture_04_figure_02.png` as documentary evidence for the derivation of the canonical distribution, but typeset the mathematics cleanly in the notes as a three-line chain from the stationarity condition to \(p_i\propto e^{-\beta E_i}\).
- Use `lecture_04_figure_03.png` as documentary evidence for the temperature definition, but typeset the final note-quality version as \(dE=T\,dS\), \(\frac{dE}{dS}=T\), and \(\frac{1}{T}=\frac{dS}{dE}\), with \(S=\beta E+\log z\) included nearby only as a cautious completion of the cropped upper box.
- Use `lecture_04_figure_04.png` as documentary evidence that the ideal-gas energy is being extracted from the \(\beta\)-dependence of \(\log z\), but typeset the cleaned argument as \(E=-d\log z/d\beta\), \(\log z=-(3N/2)\log\beta+\mathrm{const}\), and \(E=(3N/2)T\).
- Standardize notation in the final notes even if the board is inconsistent; in particular, choose one convention for \(p_i\) versus \(P_i\) and one convention for \(z\) versus \(Z\), then keep the screenshots nearby as evidence of the original board usage.
- Do not invent any extra board content from these frames; where the frame is cropped or partly blocked, rely on cautious standard completion supported by the transcript rather than aggressive reconstruction.
- If a later chapter draft wants an auxiliary schematic such as a qualitative \(e^{-\beta E}\) falloff or a gas-in-a-box picture, that should be treated as transcript-backed exposition, not as something visually evidenced by these three accepted frames.

## Uncertainties
- In `lecture_04_figure_02.png`, the lecturer blocks part of the left-hand side of the top derivative equation, so the exact function label is not fully secure even though the intended stationarity condition is clear.
- In `lecture_04_figure_02.png`, the normalization symbol in the boxed final formula looks like an uppercase \(Z\), while the lecture transcript often uses lowercase \(z\).
- In `lecture_04_figure_03.png`, the upper boxed formula is cropped, so \(S=\beta E+\log z(\beta)\) is only partly visible in the image and should be treated as a cautious completion.
- In `lecture_04_figure_04.png`, the board uses a partial-derivative symbol in the upper-right summary equation, but the cleaned derivation in the notes may reasonably use an ordinary derivative if only \(\beta\) is varying.
- In `lecture_04_figure_04.png`, the lower \(\log z\) line is partly obscured, so the constant term is not literally visible and must remain schematic as \(\mathrm{const}\).
- In `lecture_04_figure_04.png`, the board handwriting for \(\log\) is abbreviated and can look like `lg`, so the notes should normalize this to \(\log\).