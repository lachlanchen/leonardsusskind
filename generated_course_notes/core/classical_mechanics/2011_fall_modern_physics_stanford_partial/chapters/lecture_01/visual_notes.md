# Visual Evidence
## Frame Inventory
- `lecture_01_figure_03.png`: A two-state coin diagram with visible self-loops over `H` and `T` on the left and a curved arrow being drawn from a right-hand `H` toward `T`; this screenshot should remain in the final notes because it preserves the board layout of the transition from the trivial law to the alternating law.
- `lecture_01_figure_05.png`: A sparse deterministic-flow sketch with a long horizontal line, a marked point labeled `x`, and several short directional arrows near the center; this screenshot should remain in the final notes because it records the lecture’s informal board picture of local evolution.

## Equation Extraction
- No full standalone equation is legible in these two frames; what is visible is mostly diagrammatic notation and labels.
- `lecture_01_figure_03.png`: `H` [visible]
- `lecture_01_figure_03.png`: `T` [visible]
- `lecture_01_figure_03.png`: `H \to H` [visible]
- `lecture_01_figure_03.png`: `T \to T` [visible]
- `lecture_01_figure_03.png`: `H \to T` [partially visible]
- `lecture_01_figure_03.png`: `T \to H` [standard completion]
- `lecture_01_figure_05.png`: `x` [visible]

## Diagram Extraction
- `lecture_01_figure_03.png`: The board is arranged in two beats. On the left, the “boring” law is shown by a self-loop above `H` and a self-loop above `T`; on the right, a second copy of the two-state setup is used to introduce the alternating law, with a large curved arrow being drawn from `H` toward `T`. This should be shown both as the original screenshot and as a clean TikZ redraw.
- `lecture_01_figure_05.png`: The board shows a long line that reads naturally as the position direction, a marked point `x` on the right, and short arrows near the middle indicating local motion or flow. This should also be shown both ways: keep the screenshot as evidence, and redraw a sparse TikZ schematic nearby.
- For `lecture_01_figure_05.png`, the redraw should stay modest. The image itself does not justify a full coordinate grid; it supports a local flow picture, not a heavy formal phase-plane drawing.

## Reconstruction Guidance
- For `lecture_01_figure_03.png`, redraw two separate two-state diagrams in TikZ: one with self-loops `H \to H` and `T \to T`, and one with cross-transitions `H \to T` and `T \to H`. The screenshot should stay nearby because it shows how Susskind actually laid the comparison out on the board.
- Complete the reverse arrow `T \to H` from the transcript, not from the frame alone. The image directly supports the self-loops and the partially completed `H \to T` arc, but not the entire symmetric alternating diagram by itself.
- For `lecture_01_figure_05.png`, redraw only the clearly supported geometry: a long line, a labeled point `x`, and a few local arrows indicating “where you go next.” Use prose from the transcript to explain that this is a deterministic flow picture.
- Do not manufacture an explicit equation from `lecture_01_figure_05.png`; none is legible there. If a fuller \((x,v)\) phase-space diagram appears elsewhere in the notes, it should be introduced as a transcript-backed conceptual reconstruction, not as a direct transcription of this frame.

## Uncertainties
- In `lecture_01_figure_03.png`, Susskind’s hand partly covers the endpoint of the curved arrow, so the exact arrowhead placement at `T` is not fully visible.
- In `lecture_01_figure_03.png`, the reverse transition `T \to H` is not clearly drawn in the frame and should not be claimed as directly visible.
- In `lecture_01_figure_03.png`, the dots above the labels are visible but too small to carry any precise independent meaning beyond marking state locations.
- In `lecture_01_figure_05.png`, the faint extra marks and letters away from the main line are not reliably legible.
- In `lecture_01_figure_05.png`, no full vertical axis label is visible, so any explicit phase-space interpretation beyond a local flow sketch must come from the transcript.
- In `lecture_01_figure_05.png`, the exact number and spacing of the small arrows should not be treated as mathematically significant.