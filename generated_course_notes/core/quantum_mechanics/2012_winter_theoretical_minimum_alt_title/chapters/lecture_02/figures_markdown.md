# Figure Notes
## Image Inventory
- `lecture_02_figure_02.png`: An otherwise blank board with a single small upward arrow near the upper center; Susskind stands at the left edge looking at the mark.
- `lecture_02_figure_03.png`: A sparse board showing the tail end of a right-pointing horizontal arrow with an `x` label at the far left, a cropped top line for `\sigma_z`, and a clear second line `\sigma_x = \pm 1`; Susskind stands clear of the writing.
- `lecture_02_figure_04.png`: The earlier `\sigma_z` and `\sigma_x` lines remain at upper left, and a larger central formula for the mean spin component appears as `\langle \sigma_m \rangle = n\cdot m` in handwritten form; a partial curved sketch is visible on the adjacent right board.
- `lecture_02_figure_05.png`: A new two-row notation layout is being built: upper row `u`, `+`, `\uparrow`; lower row `d`, `-`, `\downarrow`; Susskind is writing the first `\sigma_z` label at the right, partly covering the equality.
- `lecture_02_figure_06.png`: The two-row z-basis table is further developed with `u,+,\uparrow,\sigma_z=1` on the top row and `d,-,\downarrow,\sigma_z=-1` on the second; at far right partial ket notation appears; below, a horizontal left-right arrow pair is drawn and Susskind is writing the new `\sigma_x` notation.

## Blackboard Equations
- `lecture_02_figure_02.png`: `\uparrow` [visible]
- `lecture_02_figure_03.png`: `\sigma_z = \pm 1` [partially visible]
- `lecture_02_figure_03.png`: `\sigma_x = \pm 1` [visible]
- `lecture_02_figure_04.png`: `\sigma_z = \pm 1` [partially visible]
- `lecture_02_figure_04.png`: `\sigma_x = \pm 1` [visible]
- `lecture_02_figure_04.png`: `\langle \sigma_m \rangle = n \cdot m` [standard reconstruction]
- `lecture_02_figure_05.png`: `u \qquad + \qquad \uparrow` [visible]
- `lecture_02_figure_05.png`: `d \qquad - \qquad \downarrow` [visible]
- `lecture_02_figure_05.png`: `\sigma_z` [visible]
- `lecture_02_figure_05.png`: `\sigma_z = +1` [standard reconstruction]
- `lecture_02_figure_06.png`: `u \qquad + \qquad \uparrow` [visible]
- `lecture_02_figure_06.png`: `d \qquad - \qquad \downarrow` [partially visible]
- `lecture_02_figure_06.png`: `\sigma_z = 1` [visible]
- `lecture_02_figure_06.png`: `\sigma_z = -1` [visible]
- `lecture_02_figure_06.png`: `|u\rangle` [partially visible]
- `lecture_02_figure_06.png`: `|d\rangle` [partially visible]
- `lecture_02_figure_06.png`: `\sigma_x` [partially visible]
- `lecture_02_figure_06.png`: `\sigma_x = \pm 1` [standard reconstruction]

## Diagram And Layout Reading
- `lecture_02_figure_02.png` is not an equation board; it is a notation gesture. The visual point is simply that the spin is first being represented on the board as a tiny classical arrow.
- `lecture_02_figure_03.png` uses a very open layout: the symbolic outcome labels sit high on the board, while the left-edge right-pointing arrow with `x` serves as a directional cue rather than a full axis diagram.
- `lecture_02_figure_04.png` centers the expectation-value formula on the board, with the earlier `\sigma_z` and `\sigma_x` labels still lingering above. This is a transition from discrete outcome labels to an average-value statement.
- `lecture_02_figure_05.png` introduces a row-wise correspondence table. The board is organized horizontally: letter label, sign, arrow symbol, then the new operator-language label being added at the right.
- `lecture_02_figure_06.png` extends that table into a fuller basis dictionary. The top two rows encode the z-basis, while the lower horizontal arrows begin the x-basis row. The far-right ket notation suggests a later shift from pictorial/state-name labels into bra-ket notation.
- Across `lecture_02_figure_05.png` and `lecture_02_figure_06.png`, the visual structure matters as much as the symbols: these are not isolated equations, but parallel identifications of the same states written in several languages.

## TeX Reconstruction Plan
- `lecture_02_figure_02.png` must remain visible. Keep it as a small screenshot because its value is the lecturer’s first board gesture; pair it with a nearby typeset `\uparrow`, but do not replace the image with pure LaTeX.
- `lecture_02_figure_03.png` must remain visible. Reconstruct `\sigma_z=\pm1` and `\sigma_x=\pm1` as clean displayed equations, and add a tiny TikZ or glyph-based right-pointing x-direction cue nearby because the left-edge arrow is part of the board logic.
- `lecture_02_figure_04.png` should remain visible, but the mathematics should be reconstructed primarily as a displayed equation. Typeset `\langle \sigma_m \rangle = n\cdot m` cleanly next to the screenshot; do not force a full `n`/`m` geometry diagram unless a later frame shows those vectors explicitly.
- `lecture_02_figure_05.png` must remain visible. The screenshot captures the live introduction of the `\sigma_z` labeling while the hand still partly obscures the writing. Reconstruct the nearby two-row equivalence display in LaTeX as a clean aligned table.
- `lecture_02_figure_06.png` must remain visible. Reconstruct a clean z-basis block and a separate x-basis block, with left-right arrows redrawn in TikZ or symbol form and `\sigma_x=\pm1` typeset nearby. Keep the ket notation only if later screenshots confirm the full right-hand column unambiguously.
- For the notes, the screenshots should function as evidence of board sequencing and layout, while the equations and basis correspondences should appear in clean typeset form immediately adjacent to them.

## Caption Drafts
- `lecture_02_figure_02.png`: Spin introduced as a single upward arrow
- `lecture_02_figure_03.png`: Outcome labels for `\sigma_z` and `\sigma_x`
- `lecture_02_figure_04.png`: Average spin component written as `\langle \sigma_m \rangle`
- `lecture_02_figure_05.png`: Up/down notation translated into `\sigma_z` language
- `lecture_02_figure_06.png`: z-basis labels extended toward the x-basis states

## Uncertainties
- In `lecture_02_figure_03.png` and `lecture_02_figure_04.png`, the top `\sigma_z` line is slightly cropped at the upper edge; it is readable in context but not perfectly clean.
- In `lecture_02_figure_04.png`, the first vector symbol in `\langle \sigma_m \rangle = n\cdot m` is handwritten in a way that can look like `n` or `\eta`; the transcript strongly favors `n\cdot m`.
- In `lecture_02_figure_04.png`, the curved line on the right board is too partial to treat as a reconstructible diagram.
- In `lecture_02_figure_05.png`, Susskind’s hand obscures the right side of the first `\sigma_z` statement; the completion to `\sigma_z = +1` is transcript-supported rather than fully visible.
- In `lecture_02_figure_06.png`, the lower `\sigma_x` writing is still in progress, so the completed `\sigma_x = \pm 1` should be treated as a cautious standard completion from the spoken line.
- In `lecture_02_figure_06.png`, the far-right ket labels are cropped; `|u\rangle` is more secure than the second ket, which should not be overcommitted without later board evidence.