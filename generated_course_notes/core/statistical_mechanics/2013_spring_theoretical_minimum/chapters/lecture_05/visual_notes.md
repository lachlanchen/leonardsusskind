# Visual Evidence
## Frame Inventory
- `lecture_05_figure_03.png`: Wide board view showing the theorem setup with `E, S` on one side, `T, V` on the other, and the start of a partial-derivative expression; this screenshot should remain in the final notes because it documents the board layout and staging of the lemma.
- `lecture_05_figure_04.png`: Board view combining a piston sketch on the left with a partly obscured work/energy formula and a new derivative expression beginning on the right; this screenshot should remain in the final notes and be paired with a clean TikZ redraw.
- `lecture_05_figure_05.png`: Lower-board view showing the end of the ideal-gas derivation, with partition-function material on the left and the final equation of state on the right; this screenshot should remain in the final notes because it captures the finished result at the exact moment it is named.

## Equation Extraction
- `lecture_05_figure_03.png`: [visible] `E`
- `lecture_05_figure_03.png`: [visible] `S`
- `lecture_05_figure_03.png`: [visible] `T`
- `lecture_05_figure_03.png`: [visible] `V`
- `lecture_05_figure_03.png`: [visible] `\partial E`
- `lecture_05_figure_03.png`: [partially visible] `S=-\sum_i p_i \log p_i`
- `lecture_05_figure_03.png`: [partially visible] `E-TS`
- `lecture_05_figure_03.png`: [standard completion] `\left(\frac{\partial E}{\partial V}\right)_S`

- `lecture_05_figure_04.png`: [visible] `dx`
- `lecture_05_figure_04.png`: [visible] `A`
- `lecture_05_figure_04.png`: [visible] `dV`
- `lecture_05_figure_04.png`: [partially visible] `dE=-P\,dV`
- `lecture_05_figure_04.png`: [partially visible] `\partial`
- `lecture_05_figure_04.png`: [standard completion] `P=-\left(\frac{\partial E}{\partial V}\right)_S`

- `lecture_05_figure_05.png`: [visible] `PV=NT`
- `lecture_05_figure_05.png`: [visible] `P=\rho T`
- `lecture_05_figure_05.png`: [partially visible] `\log Z`
- `lecture_05_figure_05.png`: [partially visible] `T\frac{\partial \log Z}{\partial V}`
- `lecture_05_figure_05.png`: [standard completion] `T\left(\frac{\partial \log Z}{\partial V}\right)_T=\frac{NT}{V}=P`
- `lecture_05_figure_05.png`: [standard completion] `\log Z=N\log V+\text{const}`
- `lecture_05_figure_05.png`: [standard completion] `PV = N k_B T` in laboratory units

## Diagram Extraction
- `lecture_05_figure_03.png`: No TikZ redraw is needed; the value is the board organization itself, with dependent variables `E, S` visually separated from independent variables `T, V`.
- `lecture_05_figure_04.png`: The piston sketch should be redrawn in TikZ as a minimal cylinder/container with a movable top plate, an upward displacement `dx`, and base label `A`; the original screenshot should remain nearby as documentary evidence of how Susskind tied the sketch to the thermodynamic formula.
- `lecture_05_figure_04.png`: The screenshot also preserves the lecture’s board logic, with the mechanical picture on the left and the differential work/energy expression on the right; that left-to-right structure matters and should be retained in the notes.
- `lecture_05_figure_05.png`: No TikZ redraw is needed; this is an equation-documentary frame, useful because it shows both the left-hand partition-function route and the right-hand final equation of state.
- `lecture_05_figure_05.png`: The frame should be shown both as evidence and as a cue for nearby clean display equations, rather than as a source for a literal handwriting-style reproduction.

## Reconstruction Guidance
- For `lecture_05_figure_03.png`, keep the screenshot visible and typeset the actual lemma from the transcript nearby; the frame supports the variable layout and the start of `\partial E`, but not the full formula by itself.
- For `lecture_05_figure_03.png`, treat the left-board entropy and Helmholtz material as contextual carryover only; use it to signal continuity with earlier formulas, not to reconstruct every intermediate line from handwriting.
- For `lecture_05_figure_04.png`, preserve the screenshot and add a clean TikZ piston diagram plus the displayed equations `dE=-P\,dV` and `P=-\left(\frac{\partial E}{\partial V}\right)_S`; the equation should be reconstructed from transcript and standard thermodynamic form, not copied blindly from the partly blocked board.
- For `lecture_05_figure_04.png`, let the notes explicitly connect the geometry `dV=A\,dx` to the work relation, since that is the whole point of the sketch.
- For `lecture_05_figure_05.png`, preserve the screenshot and typeset the cleaned chain from `\log Z` to `P=T(\partial \log Z/\partial V)_T` to `PV=NT`; the image confirms the result and board rhythm, while the transcript supplies the safe full derivation.
- For `lecture_05_figure_05.png`, present `P=\rho T` as the number-density form with `\rho=N/V`, and keep the laboratory-units `k_B` version explicitly marked as a notation restoration rather than a literal board transcription.

## Uncertainties
- In `lecture_05_figure_03.png`, the right-hand derivative is unfinished; only `\partial E` is clearly visible, so the denominator and fixed-variable condition must be supplied from transcript-backed reconstruction.
- In `lecture_05_figure_03.png`, the lower-left boxed `E-TS` combination is only fragmentary, and the associated label `A` is not clean enough to trust as a stand-alone transcription.
- In `lecture_05_figure_04.png`, the beginning and middle of the top formula are obscured by the lecturer, so `dE=-P\,dV` should be treated as a cautious completion, not a fully visible board quote.
- In `lecture_05_figure_04.png`, the lower-right derivative notation is only beginning to be written and is not legible enough to reconstruct directly from the frame.
- In `lecture_05_figure_05.png`, the left-hand derivation is partly blocked by both Susskind and the upper sliding board, so the `\log Z` line and derivative formula are better treated as partial evidence than as exact literal transcription.
- In `lecture_05_figure_05.png`, the handwritten symbol in `P=\rho T` is not perfectly crisp from the image alone; the transcript is what secures that the intended symbol is the number density `\rho`.