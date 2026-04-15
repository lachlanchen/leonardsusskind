# Figure Notes
## Image Inventory
- `lecture_01_figure_02.png`: Left board shows the already-written Newtonian motion law \(F = m\ddot z\) near the upper left; lower left contains cropped continuation marks and partial symbols. Susskind stands at the right board, which is still largely blank, beginning a fresh rewrite.
- `lecture_01_figure_03.png`: Mid-right board shows the general metric line element; near center-left are coordinate axes labeled \(x^2\) and \(x^1\). Above sits a small curvilinear-grid inset with a short arrow; below is a larger curved coordinate patch with two families of colored coordinate lines, a marked point, and short local arrows. A cropped spherical-example equation and globe-like sketch are visible at far right.
- `lecture_01_figure_04.png`: Same metric-tensor board state as the previous image, but with less body occlusion. The line element is clearer, the lower curved patch is more open, and the upper curvilinear-grid inset remains visible. The cropped right-hand sphere/example material is still present.
- `lecture_01_figure_05.png`: Same equation-and-diagram layout, but Susskind points directly at the metric factor in the line element. The axes, upper curvilinear-grid sketch, lower curved coordinate patch, and cropped right-hand example remain in frame.
- `lecture_01_figure_06.png`: Left board shows a wavy or folded surface sketch above a smoother wavy profile, with several long downward arrows beneath; right board retains the local axes \(x^2\) and \(x^1\), part of the lower curved coordinate patch, and only the beginning of a cropped \(ds^2=\) expression.

## Blackboard Equations
- `lecture_01_figure_02.png`: [visible] \(F = m\ddot z\)
- `lecture_01_figure_02.png`: [partially visible] isolated lower-board occurrences of \(\ddot z\) and continuation marks appear below the main line, but no full second equation is securely legible
- `lecture_01_figure_03.png`, `lecture_01_figure_04.png`, `lecture_01_figure_05.png`: [partially visible] \(ds^2 = \sum_{m,n} g_{mn}(x)\, dx^m dx^n\)
- `lecture_01_figure_03.png`, `lecture_01_figure_04.png`, `lecture_01_figure_05.png`: [visible] \(g_{mn}(x)\), \(dx^m\), \(dx^n\), \(x^1\), \(x^2\)
- `lecture_01_figure_03.png`, `lecture_01_figure_04.png`, `lecture_01_figure_05.png`: [partially visible] \(ds^2 = R^2(\cdots)\)
- `lecture_01_figure_06.png`: [visible] \(x^1,\; x^2\)
- `lecture_01_figure_06.png`: [partially visible] \(ds^2=\)
- For clean typesetting beside the metric figures: [standard reconstruction] \(ds^2 = \sum_{m,n} g_{mn}(x)\, dx^m dx^n\)

## Diagram And Layout Reading
- `lecture_01_figure_02.png` is a transition frame: an established equation survives on the left board while the right board is still empty. The value of the frame is not a finished derivation but the moment of specialization from the verbal “\(F=ma\)” to the vertical-coordinate form.
- `lecture_01_figure_03.png` and `lecture_01_figure_04.png` organize the board in three layers: a local axis sketch at left-center, a small abstract curvilinear-grid inset above, and a larger curved surface patch below. The line element sits over the lower patch, making the formula read as the metric attached to a coordinate net on a curved surface.
- In the lower patch of `lecture_01_figure_03.png` and `lecture_01_figure_04.png`, two coordinate families cross on a dome-like surface. There is a marked point and short local arrows, so the sketch reads as a local chart with differential directions rather than a global sphere picture.
- `lecture_01_figure_05.png` matters because the gesture fixes the demonstrative “here” to the metric factor \(g_{mn}(x)\). The screenshot is therefore evidence not only of the formula but of the lecturer’s emphasis on position dependence.
- `lecture_01_figure_06.png` splits the discussion spatially across the board. The left sketch looks like a surface or sheet with a fold/crease-like feature and a second reference profile below it; the right board keeps the local coordinate-chart material. This layout supports the lecture’s move toward intrinsic geometry and the difference between surface shape and coordinate description.
- The long downward arrows in `lecture_01_figure_06.png` are visually important board structure, but their exact mathematical role is not self-evident from the frame alone.

## TeX Reconstruction Plan
- `lecture_01_figure_02.png` should remain visible as a documentary screenshot. Pair it with a nearby displayed equation \(F = m\ddot z\); no TikZ redraw is needed.
- `lecture_01_figure_03.png` should remain visible. Reconstruct the line element as a clean displayed equation and redraw the lower curved coordinate patch in TikZ nearby. Keep the screenshot for the authentic board layout tying equation, axes, and patch together.
- `lecture_01_figure_04.png` can reuse the same displayed equation and the same TikZ patch as `lecture_01_figure_03.png`. If both images are kept, use this one for the cleaner “given one metric tensor” board state; if space is tight, it can substitute for `lecture_01_figure_03.png`.
- `lecture_01_figure_05.png` should remain visible because the pointing gesture is semantically important. Reuse the clean metric equation nearby, but do not draw a new diagram unless the prose explicitly discusses the dependence of \(g_{mn}(x)\) on position.
- `lecture_01_figure_06.png` should remain visible primarily as screenshot evidence. If the chapter needs a redraw, make it a simplified TikZ schematic of the left wavy/folded surface plus the right local chart, not a new standalone equation figure.
- Do not reconstruct the cropped right-hand sphere/example formula from these images alone as a displayed equation. If that example is needed in the notes, it should be taken from clearer neighboring evidence or from the transcript-supported lecture flow.

## Caption Drafts
- `lecture_01_figure_02.png`: Newton’s law specialized to the vertical coordinate
- `lecture_01_figure_03.png`: General line element over a local curved coordinate patch
- `lecture_01_figure_04.png`: One metric tensor in a chosen coordinate chart
- `lecture_01_figure_05.png`: Pointing to the position-dependent metric factor
- `lecture_01_figure_06.png`: Folded surface sketch and local coordinate patch

## Uncertainties
- In `lecture_01_figure_02.png`, the lower left lines beneath \(F = m\ddot z\) are too cropped to quote as complete equations.
- In `lecture_01_figure_03.png` through `lecture_01_figure_05.png`, the full structure of the metric line element is clear, but the handwritten placement of subscripts and the summation notation is crowded enough that a clean LaTeX reconstruction is preferable to a literal board transcription.
- The cropped right-hand expression \(ds^2 = R^2(\cdots)\) in `lecture_01_figure_03.png` through `lecture_01_figure_05.png` is not fully recoverable from the images alone. The lecture context suggests a sphere metric, but the crop does not securely determine the full formula or the sine-versus-cosine convention.
- In `lecture_01_figure_06.png`, the exact role of the long downward arrows and the relation between the upper and lower wavy profiles are not fully explicit from the frame alone.
- Some tiny labels inside the lower curved patch in `lecture_01_figure_03.png` through `lecture_01_figure_05.png` are too small to quote confidently.
- The horizontal axis label in the metric frames can initially look like \(x'\), but in context it is best read as \(x^1\).