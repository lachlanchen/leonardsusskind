# Figure Notes
## Image Inventory
- `lecture_01_figure_03.png`: A blackboard state diagram for the two-state coin system. On the left are two self-loop arrows, one over `H` and one over `T`, indicating the earlier “stay the same” law. On the right is a new pair of state labels `H` and `T`, with a large curved arrow being drawn from the `H` point toward the `T` point. Susskind stands in front of the board and his hand partly overlaps the destination point, but the overall layout is clear.
- `lecture_01_figure_05.png`: A blackboard phase-space-style sketch for continuous deterministic motion. A long nearly horizontal line runs across the board and a marked point labeled `x` appears toward the right. Near the upper middle are several short arrows indicating local motion direction. Additional faint marks and partial letters are scattered elsewhere on the board, but the dominant content is the line, the local arrows, and the marked point.

## Blackboard Equations
- `lecture_01_figure_03.png`: `H` [visible]
- `lecture_01_figure_03.png`: `T` [visible]
- `lecture_01_figure_03.png`: `H \to T` [standard reconstruction]
- `lecture_01_figure_03.png`: `T \to H` [standard reconstruction]
- `lecture_01_figure_05.png`: `x` [visible]
- `lecture_01_figure_05.png`: phase-space flow arrows along a one-dimensional position line [standard reconstruction]

## Diagram And Layout Reading
- `lecture_01_figure_03.png` is organized in two stages across the board. The left side preserves the earlier “boring law” in which heads stays heads and tails stays tails; this is represented by a self-loop over each state. The right side begins the more interesting law described in the transcript, where heads goes to tails and tails goes to heads. The visible curved arrow is being drawn from the right-hand `H` toward `T`, so the screenshot captures the transition from self-loops to cross-transitions.
- In `lecture_01_figure_03.png`, the dots above the `H` and `T` labels function visually like state points. The large arc is more important than the exact dot style; for note purposes the state labels and arrow connectivity matter most.
- `lecture_01_figure_05.png` is not an equation board but a geometric flow sketch. The long line reads as the position axis described in the transcript, and the small arrows near the upper middle indicate where a point in phase space moves next. The marked point `x` on the right helps anchor the horizontal coordinate interpretation.
- In `lecture_01_figure_05.png`, the visible content corresponds to Susskind’s point that classical mechanics can be pictured as a phase space filled with little arrows telling you where the system goes next. The frame does not show a full coordinate grid, so it should be treated as a local schematic, not a complete axis diagram.
- The extra faint letters away from the main sketch in `lecture_01_figure_05.png` are too partial to organize the figure around. The central readable layout is the line, the directional arrows, and the point marked `x`.

## TeX Reconstruction Plan
- `lecture_01_figure_03.png` should remain visible in the notes. It is good evidence for the board layout that contrasts the self-loop law with the heads-to-tails transition law.
- Near `lecture_01_figure_03.png`, the notes should include a clean TikZ redraw of the two-state diagram. The redraw should show two labeled states `H` and `T`, self-loops for the “stay the same” law, and directed arrows `H \to T` and `T \to H` for the alternating law, with the transcript deciding the full symmetric pair even though the screenshot most clearly shows only one arc being drawn.
- `lecture_01_figure_05.png` should also remain visible in the notes. It is useful as evidence for the lecture’s board-level visualization of deterministic flow in phase space.
- Near `lecture_01_figure_05.png`, the notes should use TikZ rather than a displayed equation. The redraw should present a simple one-dimensional position line or phase-space slice with local arrows showing motion to the right or left depending on the state, keeping the board’s spareness rather than adding a heavy formal axis system.
- For `lecture_01_figure_05.png`, the transcript should supply the interpretation that the arrows encode “where you will be next,” while the screenshot supplies the local geometry and board placement.

## Caption Drafts
- `lecture_01_figure_03.png`: Two-state transition diagram for heads and tails
- `lecture_01_figure_05.png`: Local deterministic flow sketch in phase space

## Uncertainties
- In `lecture_01_figure_03.png`, the lecturer’s hand partly occludes the endpoint of the right-hand curved arrow, so the exact arrowhead placement at `T` is not perfectly visible.
- In `lecture_01_figure_03.png`, only one of the cross-arrows is clearly being drawn in this frame; the reverse arrow from `T` to `H` should come from the transcript, not from over-reading the image.
- In `lecture_01_figure_03.png`, the dots above `H` and `T` look like point markers, but they are too small to carry independent mathematical meaning.
- In `lecture_01_figure_05.png`, the faint additional letters and marks away from the main sketch are too incomplete to transcribe confidently.
- In `lecture_01_figure_05.png`, the board does not show a full labeled vertical axis, so the phase-space interpretation should be stated from the transcript but the redraw should remain visually modest.
- In `lecture_01_figure_05.png`, the small local arrows are clear enough to justify a flow reconstruction, but their exact number and spacing should not be treated as mathematically significant.