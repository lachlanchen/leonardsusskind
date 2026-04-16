# Visual Evidence
## Frame Inventory
- `lecture_02_figure_02.png`: A train-and-station board sketch shows the unprimed frame label `x,t`, the primed observer inside the train marked near `x'=0`, and a dashed projection down to the station line; this screenshot should remain in the final notes as visual evidence for how Susskind identifies the primed origin geometrically.
- `lecture_02_figure_03.png`: A clean equation board shows four stacked Lorentz-transformation formulas, first for unprimed to primed coordinates and then for primed to double-primed coordinates; this screenshot should remain in the final notes as documentary evidence for the composed-boost setup.
- `lecture_02_figure_04.png`: A fuller train sketch adds the kiddie car, a rightward arrow labeled `u`, and the location Susskind points to when discussing `x''=0`; this screenshot should remain in the final notes as visual evidence for the three-frame construction and the meaning of the double-primed origin.

## Equation Extraction
- `lecture_02_figure_02.png`: [visible] \(x,t\)
- `lecture_02_figure_02.png`: [visible] \(x'=0\)
- `lecture_02_figure_02.png`: [partially visible] a primed event label near the highlighted point, plausibly \(x',t'\) or \((x',t')\)
- `lecture_02_figure_02.png`: [standard completion] \(x'=0 \iff x=vt\)

- `lecture_02_figure_03.png`: [visible] \(X'=\dfrac{X-vt}{\sqrt{1-v^2}}\)
- `lecture_02_figure_03.png`: [visible] \(t'=\dfrac{t-vx}{\sqrt{1-v^2}}\)
- `lecture_02_figure_03.png`: [visible] \(X''=\dfrac{X'-ut'}{\sqrt{1-u^2}}\)
- `lecture_02_figure_03.png`: [visible] \(t''=\dfrac{t'-ux'}{\sqrt{1-u^2}}\)

- `lecture_02_figure_04.png`: [visible] \(x,t\)
- `lecture_02_figure_04.png`: [visible] \(x'=0\)
- `lecture_02_figure_04.png`: [partially visible] \(x'',t''\) beside the kiddie car
- `lecture_02_figure_04.png`: [visible] \(u\)
- `lecture_02_figure_04.png`: [partially visible] \(w\) near the lower rightward arrow
- `lecture_02_figure_04.png`: [standard completion] \(x''=0\)
- `lecture_02_figure_04.png`: [standard completion] \(x=\dfrac{u+v}{1+uv}\,t\)
- `lecture_02_figure_04.png`: [standard completion] \(w=\dfrac{u+v}{1+uv}\)

## Diagram Extraction
- `lecture_02_figure_02.png`: The board is a schematic rather than a literal spacetime graph: a large rectangle represents the train interior, labeled in the unprimed coordinates, with a stick-figure passenger inside and a station observer below. This should be shown both ways: keep the screenshot and redraw the schematic in TikZ so the relation between the primed origin and the station line is legible.
- `lecture_02_figure_02.png`: The red dashed vertical line from the highlighted interior point down to the lower line is important and should be preserved in the redraw, because it visually ties the event in the train to a location on the stationary reference line.
- `lecture_02_figure_03.png`: The essential visual content is the stacked layout of the four equations, with the top pair and bottom pair clearly separated. This should remain as a screenshot and also be typeset as clean display math nearby, but it does not need a TikZ redraw.
- `lecture_02_figure_04.png`: The sketch expands the earlier train picture by adding the kiddie car at the right, the double-primed label, and a velocity arrow `u`; it should be shown both ways, with the screenshot kept and a TikZ redraw clarifying the three frames at once.
- `lecture_02_figure_04.png`: The lower station line with a second rightward arrow labeled `w` is useful as a visual bridge from the diagram to the velocity-addition formula, so the redraw should include it if the chapter presents the geometric interpretation of the kid’s worldline in the unprimed frame.

## Reconstruction Guidance
- Keep `lecture_02_figure_02.png` next to a clean TikZ schematic and a displayed statement \(x'=0 \iff x=vt\); the screenshot supplies the lecture’s live board layout, while the redraw supplies clarity.
- Keep `lecture_02_figure_03.png` next to clean display equations; transcribe the four visible formulas faithfully, but standardize notation in the notes to lowercase \(x\) unless there is a strong reason to preserve the board’s uppercase `X`.
- Keep `lecture_02_figure_04.png` next to a TikZ redraw of the train, passenger, kiddie car, and velocity arrows, and use the transcript to supply the clean mathematical interpretation \(x''=0\) and \(w=\dfrac{u+v}{1+uv}\).
- Treat the screenshots as evidence for board structure, labels, and the order in which the argument is built, not as the final readable form of the mathematics.
- When a symbol is only partly visible, prefer a cautious standard completion from the transcript and the known Lorentz-transformation pattern rather than pretending the board is fully legible.
- Preserve the lecture’s conceptual rhythm: first the primed origin \(x'=0\), then the second boost, then the double-primed origin \(x''=0\), then the composed velocity \(w\).

## Uncertainties
- In `lecture_02_figure_02.png`, the notation written beside the highlighted point near the dashed line is not reliably legible; it looks primed, but the exact symbol string should not be asserted from the image alone.
- In `lecture_02_figure_02.png`, the red `x` on the lower line is visible, but it is unclear whether it is just a marked coordinate position or part of a longer label.
- In `lecture_02_figure_03.png`, the board mixes uppercase `X` and lowercase `x`; this is visible, but it is almost certainly not mathematically meaningful and should be normalized in the notes.
- In `lecture_02_figure_04.png`, the double-primed label at the kiddie car is partly blocked by Susskind’s hand, so the exact handwriting is not fully recoverable from the frame alone.
- In `lecture_02_figure_04.png`, the left-edge algebra from the previous board state is too cropped to trust as a direct transcription; the velocity-addition formula should be reconstructed from the transcript, not from that fragment.
- The lower rightward arrow label in `lecture_02_figure_04.png` appears to be `w`, but it is not as secure as the clearly visible `u` on the upper arrow.