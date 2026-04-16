# Figure Notes
## Image Inventory
- `lecture_01_figure_02.png` shows Susskind standing between two whiteboard regions. On the right board there is a vertical list of color-transition rules, each written as an arrow from one color to the next. On the left board there are leftover probability expressions involving \(F(i)\), \(p(i)\), and a frequency-like fraction with \(N(i)\) over \(N\).
- `lecture_01_figure_03.png` shows Susskind beside a large schematic of two adjacent regions connected by a narrow bottleneck. The left region is larger and drawn with a curved lower boundary; the right region is partly cropped but clearly connected through a thin neck.
- `lecture_01_figure_05.png` shows a probability graph on a whiteboard: a vertical axis labeled with a \(P\)-like symbol, a horizontal axis marked by ticks, and a smooth single-peaked curve. A bracketed interval below the axis is labeled \(M\). Part of a nearby entropy formula beginning with \(S=\) is cropped at the far right.
- `lecture_01_figure_06.png` shows essentially the same probability graph as `lecture_01_figure_05.png`, but at a later moment when Susskind is pointing at it with an eraser. The vertical label, the full peak, the tick marks, and the bracket labeled \(M\) remain visible.

## Blackboard Equations
- `lecture_01_figure_02.png`: [visible] \(F(i)\,p(i)\)
- `lecture_01_figure_02.png`: [visible] \(\dfrac{F(i)\,N(i)}{N}\)
- `lecture_01_figure_02.png`: [visible] \(R\to B\)
- `lecture_01_figure_02.png`: [visible] \(B\to Y\)
- `lecture_01_figure_02.png`: [visible] \(Y\to G\)
- `lecture_01_figure_02.png`: [visible] \(G\to O\)
- `lecture_01_figure_02.png`: [visible] \(O\to P\)
- `lecture_01_figure_02.png`: [visible] \(P\to R\)

- `lecture_01_figure_03.png`: [partially visible] \(P(i)\)

- `lecture_01_figure_05.png`: [partially visible] \(P_i\)
- `lecture_01_figure_05.png`: [visible] \(M\)
- `lecture_01_figure_05.png`: [partially visible] \(S=\cdots\)

- `lecture_01_figure_06.png`: [partially visible] \(P_i\)
- `lecture_01_figure_06.png`: [visible] \(M\)

## Diagram And Layout Reading
- `lecture_01_figure_02.png` has a meaningful two-column board layout. The right side is a purely dynamical update rule written as a six-step directed cycle in text form rather than yet as a drawn loop. The left side retains the earlier probability/frequency notation, so the frame records the transition from probabilistic bookkeeping to deterministic law-as-diagram.
- `lecture_01_figure_03.png` is a schematic rather than an equation board. The left and right compartments are drawn as two subsystems, with a narrow connecting passage between them. The asymmetry matters: the left container is visibly larger and its lower boundary is curved, which helps distinguish the sketch from a generic pair of rectangles. This is exactly the sort of board figure that should be redrawn cleanly in TikZ.
- `lecture_01_figure_05.png` lays out a one-dimensional family of states along a horizontal axis and plots a qualitative probability distribution above it. The distribution is unimodal, centered over a middle region, and the bracket beneath the axis marks a characteristic width or span labeled \(M\). The vertical axis label is written near the top and looks like \(P_i\), though the subscript is not completely crisp. The graph is schematic rather than data-like; the tick marks are evenly spaced and represent state labels, not measured coordinates.
- `lecture_01_figure_06.png` confirms the same graph and highlights the part of the lecturer’s spoken point that concerns width. The eraser gesture points into the peak and shoulder region, while the bracket \(M\) remains the visual marker for the spread. The frame is slightly more animated and therefore less clean as a primary figure, but it is useful corroboration of what part of the graph is being discussed.

## TeX Reconstruction Plan
- `lecture_01_figure_02.png` should remain visible in the notes. It is the strongest documentary record for the six-state update law before it is redrawn as a proper cycle. Nearby TeX should typeset the transition list cleanly and also include a TikZ directed cycle with nodes \(R,B,Y,G,O,P\). The leftover expressions \(F(i)p(i)\) and \(F(i)N(i)/N\) can be typeset nearby if the surrounding prose still refers to the earlier probability discussion, but they should not be overemphasized.
- `lecture_01_figure_03.png` should remain visible and should definitely be paired with a TikZ redraw. The screenshot preserves the lecture’s board evidence, while the TikZ version should render two connected subsystems with a narrow neck, matching the sketch’s asymmetry rather than replacing it with generic identical boxes.
- `lecture_01_figure_05.png` should remain visible as the primary screenshot for the probability-distribution discussion. It should be paired with a clean TikZ plot: vertical probability axis, tick-marked horizontal state axis, a smooth single-peaked curve, and a bracket underneath labeled \(M\). If the chapter later introduces the entropy formula nearby, the figure can sit next to the displayed formula rather than trying to extract more algebra from the screenshot itself.
- `lecture_01_figure_06.png` may also remain visible if the chapter wants a second supporting screenshot at the moment where the lecturer interprets the width of the distribution. It is best treated as supporting visual continuity rather than as the main source for the redraw, since `lecture_01_figure_05.png` is cleaner. If space is tight, the TikZ redraw and `lecture_01_figure_05.png` can do the main work and this later frame can be omitted.
- For the graph figures, the mathematics should be reconstructed in prose and displayed equations from the transcript, while the visuals should be reconstructed with TikZ rather than by trying to transcribe every tick and gesture literally.

## Caption Drafts
- `lecture_01_figure_02.png`: Color transition rule and probability notation
- `lecture_01_figure_03.png`: Two connected subsystems exchanging energy
- `lecture_01_figure_05.png`: Schematic probability distribution over states
- `lecture_01_figure_06.png`: Narrower probability distribution and width \(M\)

## Uncertainties
- In `lecture_01_figure_02.png`, the left-board expressions are partly cropped; \(F(i)\,p(i)\) and \(\frac{F(i)N(i)}{N}\) are readable, but any additional leading symbols at the far left are not secure.
- In `lecture_01_figure_02.png`, the right-board color list is clear, but the lecture later redraws it as a closed cycle; the screenshot itself shows the textual transition law, not the final node-and-arrow diagram.
- In `lecture_01_figure_03.png`, the partial \(P(i)\) at the far left appears to be leftover writing unrelated to the main subsystem sketch and should be treated cautiously.
- In `lecture_01_figure_03.png`, the right-hand subsystem is cropped, so the full outer contour is not completely visible even though the bottleneck structure is clear.
- In `lecture_01_figure_05.png` and `lecture_01_figure_06.png`, the vertical axis label looks like \(P_i\), but the exact subscript is not perfectly sharp. The transcript supports that the axis is probability, so the notes should normalize the label accordingly.
- In `lecture_01_figure_05.png`, the bracket label \(M\) is clear, but its precise interpretation should come from the transcript and nearby prose rather than from the image alone.
- In `lecture_01_figure_05.png`, the cropped expression at the right beginning with \(S=\) is not legible enough to reconstruct from the screenshot itself; it should be supplied only from the transcript where needed.