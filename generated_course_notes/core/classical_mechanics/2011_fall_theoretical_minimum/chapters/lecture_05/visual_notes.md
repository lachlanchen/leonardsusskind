# Visual Evidence
## Frame Inventory
- `lecture_05_figure_02.png`: Close-up of the board at the start of the `dL/dt` calculation, showing only the derivative operator and the Lagrangian arguments; the screenshot should remain in the final notes as visual evidence for the opening of the derivation.
- `lecture_05_figure_03.png`: Summary board with `L(q,\dot q,t)`, the canonical-momentum definition, and the beginning of the `\dot p` equation; the screenshot should remain because it preserves the recap layout clearly.
- `lecture_05_figure_04.png`: Isolated board statement of the Hamiltonian time-derivative relation with little surrounding clutter; the screenshot should remain because it functions as a clean board takeaway.
- `lecture_05_figure_05.png`: Two-board frame combining the Hamiltonian time-dependence formula with a pendulum sketch and cropped remnants of earlier recap formulas; the screenshot should remain, and it is the one frame that also supports a clean redraw.
- `lecture_05_figure_06.png`: Close-up of the nonstandard-Lagrangian example showing the left-over potential term and the differentiated left-hand side of the equation of motion; the screenshot should remain because it captures an intermediate algebra step rather than just the finished result.

## Equation Extraction
- `lecture_05_figure_02.png`: [visible] `\frac{d}{dt}L(q_i,\dot q_i)`
- `lecture_05_figure_02.png`: [standard completion] `\frac{dL}{dt}=\sum_i \frac{\partial L}{\partial q_i}\dot q_i+\sum_i \frac{\partial L}{\partial \dot q_i}\ddot q_i`
- `lecture_05_figure_03.png`: [visible] `L(q,\dot q,t)`
- `lecture_05_figure_03.png`: [visible] `P=\frac{\partial L}{\partial \dot q}`
- `lecture_05_figure_03.png`: [visible] `\dot P`
- `lecture_05_figure_03.png`: [standard completion] `\dot p_i=\frac{\partial L}{\partial q_i}`
- `lecture_05_figure_04.png`: [visible] `\frac{dH}{dt}=-\frac{\partial \mathcal{L}}{\partial t}`
- `lecture_05_figure_05.png`: [visible] `\frac{dH}{dt}=-\frac{\partial \mathcal{L}}{\partial t}`
- `lecture_05_figure_05.png`: [partially visible] `Q=\sum_i p_i f_i(q)`
- `lecture_05_figure_05.png`: [partially visible] `\dot Q=0`
- `lecture_05_figure_05.png`: [partially visible] `\sum_i p_i \dot q_i - L`
- `lecture_05_figure_05.png`: [standard completion] `H=\sum_i p_i \dot q_i-L`
- `lecture_05_figure_06.png`: [visible] `-\frac{q^2}{2}`
- `lecture_05_figure_06.png`: [visible] `q^2\ddot q+2q\dot q^2=`
- `lecture_05_figure_06.png`: [standard completion] `\frac{\partial L}{\partial q}=q\dot q^2-q`
- `lecture_05_figure_06.png`: [standard completion] `q^2\ddot q+2q\dot q^2=q\dot q^2-q`
- `lecture_05_figure_06.png`: [standard completion] `q^2\ddot q+q\dot q^2=-q`

## Diagram Extraction
- `lecture_05_figure_05.png` contains the only real diagram worth redrawing: a two-link pendulum or double-pendulum-style sketch with a top pivot, a first rod to an intermediate mass, a second rod to a lower mass, vertical reference lines, and angle labels near the rods.
- That pendulum sketch should be shown both ways: preserve the original screenshot as evidence of the lecture board state, and redraw it in TikZ as a clean schematic for the notes.
- `lecture_05_figure_03.png` and `lecture_05_figure_04.png` do not need TikZ redraws, but their board layout matters: `lecture_05_figure_03.png` is a stacked recap board, while `lecture_05_figure_04.png` is a single-equation conclusion.
- `lecture_05_figure_02.png` and `lecture_05_figure_06.png` are best preserved as screenshots only, since what matters there is the visible intermediate stage of a derivation rather than a geometric figure.

## Reconstruction Guidance
- For `lecture_05_figure_02.png`, keep the screenshot beside a typeset chain-rule expansion; the image shows the start of the calculation, but the full equation should come from cautious reconstruction supported by the transcript.
- For `lecture_05_figure_03.png`, preserve the top-to-bottom board rhythm in the notes: first `L(q_i,\dot q_i,t)`, then `p_i=\partial L/\partial \dot q_i`, then `\dot p_i=\partial L/\partial q_i`; normalize the board’s capital-looking `P` to standard canonical notation in the prose.
- For `lecture_05_figure_04.png`, typeset `\frac{dH}{dt}=-\frac{\partial L}{\partial t}` cleanly, but keep the screenshot because the lecture presents it visually as an isolated summary statement.
- For `lecture_05_figure_05.png`, use the right board as evidence for the Hamiltonian time-dependence formula and use the lower-right sketch as the basis for a TikZ redraw; do not rely on the faint left-board fragments alone for definitive transcription, even though they help identify the surrounding recap.
- For `lecture_05_figure_06.png`, keep the screenshot to preserve the working step `q^2\ddot q+2q\dot q^2=` and then typeset both the completed Euler-Lagrange equation and its simplified form in the notes.
- Throughout, treat the transcript as the primary source of truth and use the frames mainly to preserve notation, board ordering, and the lecturer’s visual pacing.

## Uncertainties
- In `lecture_05_figure_02.png`, the argument list of `L` is legible in intent but not sharp enough to settle every index and punctuation mark purely from the image.
- In `lecture_05_figure_03.png`, the bottom line is only the beginning of the equation of motion; the finished form `\dot p_i=\partial L/\partial q_i` is a standard completion supported by the transcript, not fully written in the frame.
- In `lecture_05_figure_04.png` and `lecture_05_figure_05.png`, the symbol on the right-hand side looks script-like; it is safest to normalize it to the chapter’s chosen notation for the Lagrangian.
- In `lecture_05_figure_05.png`, the left-board formulas are cropped and faint, so the exact presence of `H=` versus only `\sum_i p_i\dot q_i-L` is not fully reliable from the frame alone.
- In `lecture_05_figure_05.png`, the upper angle label in the pendulum sketch is plausibly `\theta`, while the lower label is likely `\phi` or `\varphi`, but the handwriting is not crisp enough to be certain.
- In `lecture_05_figure_06.png`, the right-hand side after the equals sign is off-frame, so the full Euler-Lagrange equation must be completed from the transcript rather than inferred from the screenshot alone.
- The subtitle attached to `lecture_05_figure_02.png` mentions the potential and kinetic energy of the Lagrangian, but that phrase is not itself written on the board in the frame.