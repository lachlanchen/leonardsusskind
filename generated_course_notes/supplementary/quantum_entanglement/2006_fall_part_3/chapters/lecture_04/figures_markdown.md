# Figure Notes
## Image Inventory
- `lecture_04_figure_01.png`: A Stanford opening title card with the red block `S`, tree emblem, the text “STANFORD UNIVERSITY,” and the website line below. There is no lecturer, no board, and no mathematical content.
- `lecture_04_figure_02.png`: A whiteboard shot from the Galilean-relativity review. Near the upper left are the transformation equations, and a simple coordinate graph is being set up with a vertical axis labeled `t` and a horizontal axis labeled `x`. Susskind stands at the left edge of the frame.
- `lecture_04_figure_03.png`: A closer whiteboard shot of the spacetime diagram after the moving-frame worldline has been added. A slanted line rises from the origin; above it are labels identifying it with `x=vt`, `x'=0`, and `t'`. The original `t` axis is still visible at left.
- `lecture_04_figure_04.png`: A later classroom frame with Susskind leaning forward between two boards. On the left board there are partial algebraic expressions; on the right there is a more elaborate spacetime-style diagram with a vertical line and a skewed set of diagonal guide lines. The lecturer partly occludes the center.

## Blackboard Equations
- `lecture_04_figure_01.png`: no blackboard mathematics; only title-card text is present. [visible]
- `lecture_04_figure_02.png`: \(x' = x - vt\) [visible]
- `lecture_04_figure_02.png`: \(t' = t\) [visible]
- `lecture_04_figure_02.png`: \(t,\ x\) axis labels [visible]
- `lecture_04_figure_03.png`: \(x = vt\) [visible]
- `lecture_04_figure_03.png`: \(x' = 0\) [visible]
- `lecture_04_figure_03.png`: \(t'\) [visible]
- `lecture_04_figure_03.png`: \(t\) [partially visible]
- `lecture_04_figure_03.png`: the slanted line is the worldline of the primed origin, so \(x=vt\) and \(x'=0\) are being identified on the board as the same locus. [standard reconstruction]
- `lecture_04_figure_04.png`: \(-2xvt\) [partially visible]
- `lecture_04_figure_04.png`: \((1-v^2)x^2\) or a closely related algebraic term ending in \(x^2\) [partially visible]
- `lecture_04_figure_04.png`: additional left-board terms are present but too cropped and incomplete for reliable transcription. [partially visible]

## Diagram And Layout Reading
- `lecture_04_figure_01.png` has no mathematical layout. It is purely a source-video title image.
- `lecture_04_figure_02.png` preserves the setup of the Galilean spacetime sketch before the moving-frame construction is complete. The board organization matters: equations at upper left, then a clean `t`-vertical / `x`-horizontal graph occupying the main field of the board.
- `lecture_04_figure_03.png` is the most important diagram frame. It shows the same graph after the slanted line through the origin has been added. The board is making the standard identification that the moving observer’s spatial origin traces the line \(x=vt\), which is equivalently the line \(x'=0\), and this slanted line is labeled as the \(t'\)-axis.
- `lecture_04_figure_03.png` also preserves the pedagogical board layout: the original unprimed axes are not erased, so the primed construction is visibly being placed “on the same graph,” exactly as the lecture says.
- `lecture_04_figure_04.png` is more a layout witness than a clean mathematical transcription. The right board contains a developed skewed spacetime construction with diagonal interior lines, visually consistent with a discussion of asymmetric geometric comparison. The lecturer’s posture blocks the middle, so the figure is best read as evidence of board geometry, not of exact labeling.
- `lecture_04_figure_04.png` also records that the lecture has two simultaneous strands on the board at this moment: algebra on the left, diagram on the right. That split-board organization may matter if a later `Question & Answer` subsection preserves the asymmetry discussion.

## TeX Reconstruction Plan
- `lecture_04_figure_01.png` should not remain visible in the mathematical chapter. It is an opening title card and does not help the notes.
- `lecture_04_figure_02.png` should remain visible if the chapter includes the opening Galilean-relativity review. It should be paired with clean displayed equations
  \(x' = x - vt\) and \(t' = t\),
  and, if needed, a small TikZ redraw of the initial `t` and `x` axes nearby.
- `lecture_04_figure_02.png` is useful mainly as board-layout evidence rather than as a finished diagram. The notes should not pretend that the full primed-axis construction is already complete in this frame.
- `lecture_04_figure_03.png` should definitely remain visible. It is the strongest screenshot of the moving-frame worldline construction and should be paired with a clean TikZ spacetime diagram showing the unprimed axes, the slanted line \(x=vt\), the condition \(x'=0\), and the identification of that line with the \(t'\)-axis.
- `lecture_04_figure_03.png` should also be paired with a nearby displayed line such as
  \(x = vt \iff x' = 0\),
  because that equivalence is precisely what the board is teaching.
- `lecture_04_figure_04.png` is visually weaker. If the chapter preserves the later asymmetry question as a substantive `Question & Answer` subsection, this screenshot may be kept as secondary board evidence and paired with a TikZ redraw of the right-hand skewed diagram. It should not be used as the primary source for exact equations.
- `lecture_04_figure_04.png` should not be relied on for left-board algebra transcription beyond the few legible fragments. If it is used, the screenshot should remain near the redraw so the reader can see that the clean figure is an editorial reconstruction of a partially occluded board.
- No screenshot from this set should be used to typeset full Lorentz-transformation formulas beyond what is actually visible, unless the transcript supplies the full expression nearby.

## Caption Drafts
- `lecture_04_figure_01.png`: Stanford opening title card
- `lecture_04_figure_02.png`: Galilean axes with \(x' = x - vt\) and \(t' = t\)
- `lecture_04_figure_03.png`: Worldline \(x=vt\) identified with \(x'=0\) and \(t'\)
- `lecture_04_figure_04.png`: Asymmetric spacetime construction on the later board

## Uncertainties
- `lecture_04_figure_01.png` is not mathematically useful and should be omitted despite being visually clean.
- In `lecture_04_figure_02.png`, the finished \(t'\)-axis is not yet clearly present; the frame is best treated as the setup for the construction rather than its completion.
- In `lecture_04_figure_03.png`, Susskind’s hand comes close to the top labels, so spacing and punctuation between \(x=vt\), \(x'=0\), and \(t'\) should not be overinterpreted.
- In `lecture_04_figure_03.png`, the lower horizontal axis is only partly visible at the far right, so a clean redraw should use the transcript to normalize the full axis geometry.
- In `lecture_04_figure_04.png`, the algebra on the left board is too incomplete and cropped to reconstruct safely beyond short fragments like \(-2xvt\).
- In `lecture_04_figure_04.png`, the right-board diagram is useful as a geometric scaffold, but its precise labels and line roles are not fully legible; any TikZ reconstruction should therefore be guided by the transcript and presented cautiously.
- `lecture_04_figure_04.png` is also looser in timestamp-to-content alignment than `lecture_04_figure_02.png` and `lecture_04_figure_03.png`; if space is tight, it is the first of these mathematical frames that could be dropped.