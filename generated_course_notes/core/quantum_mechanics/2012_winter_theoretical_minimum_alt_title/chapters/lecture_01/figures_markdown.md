# Figure Notes
## Image Inventory
- `lecture_01_figure_02.png` shows the early qubit-notation board. At upper left there is a vertical `H` over `T`; near the top center are the labels `\sigma=1` and `\sigma=-1`; to the right are a clear upward arrow and downward arrow. Susskind stands in front of the board but the key notation remains visible.
- `lecture_01_figure_03.png` shows the later measurement-layout board. The earlier `H/T` and `\sigma=\pm1` notation still survives at left, a large standalone upward arrow appears in the middle, and at right there are two apparatus sketches: an upright box with a circled `+1`, and below it a sideways box with a central oval/window and horizontal arrows, labeled `A`.
- `lecture_01_figure_05.png` shows the abstract vector-space board. The top half gives componentwise addition of two two-entry column vectors, and the lower half gives multiplication of a two-entry column vector by a complex number `z`. A short note at the top indicates that the entries are complex.

## Blackboard Equations
- `lecture_01_figure_02.png`: `H` over `T` [visible]
- `lecture_01_figure_02.png`: `\sigma=1` [visible]
- `lecture_01_figure_02.png`: `\sigma=-1` [partially visible]
- `lecture_01_figure_02.png`: `\uparrow` [visible]
- `lecture_01_figure_02.png`: `\downarrow` [visible]
- `lecture_01_figure_02.png`: `\sigma=1 \leftrightarrow \uparrow` [standard reconstruction]
- `lecture_01_figure_02.png`: `\sigma=-1 \leftrightarrow \downarrow` [standard reconstruction]

- `lecture_01_figure_03.png`: `H` over `T` [visible]
- `lecture_01_figure_03.png`: `\sigma=1` [visible]
- `lecture_01_figure_03.png`: `\sigma=-1` [partially visible]
- `lecture_01_figure_03.png`: `+1` inside the upper apparatus display [visible]
- `lecture_01_figure_03.png`: `A` beside the lower apparatus [visible]

- `lecture_01_figure_05.png`: `\alpha = \text{complex}` or equivalent shorthand note [partially visible]
- `lecture_01_figure_05.png`: `\begin{pmatrix}\alpha_1\\ \alpha_2\end{pmatrix}+\begin{pmatrix}\beta_1\\ \beta_2\end{pmatrix}=\begin{pmatrix}\alpha_1+\beta_1\\ \alpha_2+\beta_2\end{pmatrix}` [visible]
- `lecture_01_figure_05.png`: `z\begin{pmatrix}\alpha_1\\ \alpha_2\end{pmatrix}=\begin{pmatrix}z\alpha_1\\ z\alpha_2\end{pmatrix}` [visible]
- `lecture_01_figure_05.png`: `\alpha_1,\alpha_2,\beta_1,\beta_2,z\in\mathbb{C}` [standard reconstruction]

## Diagram And Layout Reading
- `lecture_01_figure_02.png` is laid out as three parallel notational systems for the same two-state qubit: heads/tails at left, `\sigma=\pm1` in the middle, and up/down arrows at right. There are no explicit connecting lines; the correspondence is conveyed by spatial grouping and lecture narration.
- `lecture_01_figure_03.png` has a strong left-to-right pedagogical layout. The surviving qubit labels remain at left, the large central upward arrow marks the prepared “up” state, and the right side contains the measurement-apparatus sketches. The upper sketch is an upright detector with a displayed `+1`; the lower sketch is a rotated detector with a central window/oval and horizontal probing arrows, matching the discussion of a horizontal component.
- In `lecture_01_figure_03.png`, the upper apparatus suggests “this side up” orientation, while the lower apparatus shows the detector turned sideways. The sketch is conceptually important because it marks the transition from vertical preparation to horizontal measurement.
- `lecture_01_figure_05.png` is organized in two rows: the top row defines vector addition componentwise, and the bottom row defines scalar multiplication by a complex number. The board functions as a concrete realization of a two-dimensional complex vector space.

## TeX Reconstruction Plan
- `lecture_01_figure_02.png` should remain visible in the notes. Place it near the introduction of the qubit’s three equivalent notations, and typeset a clean display nearby such as `\sigma=1 \leftrightarrow \uparrow` and `\sigma=-1 \leftrightarrow \downarrow`. No TikZ redraw is necessary.
- `lecture_01_figure_03.png` should remain visible in the notes. It should be paired with a clean TikZ redraw of the two detector orientations: upright apparatus versus sideways apparatus, with the prepared upward state shown separately. The screenshot is valuable as blackboard evidence; the redraw should do the explanatory work.
- `lecture_01_figure_03.png` may also be paired with short prose rather than a formal displayed equation, since the key content is geometric and operational rather than algebraic.
- `lecture_01_figure_05.png` should remain visible in the notes and should be paired with clean displayed equations for componentwise addition and scalar multiplication of two-component complex columns. No TikZ redraw is needed.
- For `lecture_01_figure_05.png`, normalize the notation in print to standard column-vector LaTeX, while keeping the screenshot as evidence that Susskind introduced the vector-space operations concretely through two-entry complex columns.

## Caption Drafts
- `lecture_01_figure_02.png`: Qubit labels `\sigma=\pm1` and up/down notation
- `lecture_01_figure_03.png`: Upright and sideways qubit-apparatus sketches
- `lecture_01_figure_05.png`: Two-component complex column-vector operations

## Uncertainties
- In `lecture_01_figure_02.png`, the lower `\sigma=-1` line is partly occluded by Susskind, though the intended label is strongly supported by the transcript and by the visible board structure.
- In `lecture_01_figure_02.png`, the `H/T` at left is visible but not explicitly glossed on the board as “heads/tails” in the frame itself; that identification comes from the lecture narration.
- In `lecture_01_figure_03.png`, the text along the top of the upper apparatus is cropped and only partially legible; it appears to be an orientation cue such as “this side up,” but the exact wording should not be transcribed literally without caution.
- In `lecture_01_figure_03.png`, the lower horizontal-arrow sketch is lecture-evidence for the sideways detector, but the exact arrow directions are not fully trustworthy as a final diagram, especially since the transcript later mentions a correction from the audience. A cleaned TikZ redraw should therefore prioritize the explained geometry over the exact chalk orientation.
- In `lecture_01_figure_05.png`, the top note about complex entries is abbreviated and not perfectly sharp. The safe print version is to normalize the mathematics to the statement that the components and scalar belong to `\mathbb{C}`.
- In `lecture_01_figure_05.png`, the rightmost result column is visible but close enough to the frame edge that careful typeset reconstruction is preferable to literal visual transcription of every stroke.