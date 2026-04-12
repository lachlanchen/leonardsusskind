# Figure Notes
## Image Inventory
- `lecture_05_figure_02.png`: Leonard Susskind stands to the left of a hand-drawn upper-half compactified spacetime diagram. The drawing is a triangular or fan-like Penrose-style wedge with a left vertical boundary, a sharp right tip, several bowed interior curves, and several transverse curves crossing them. A top label reading \(t=\infty\) is visible. The lower half is intentionally absent.
- `lecture_05_figure_03.png`: A more developed Schwarzschild Penrose diagram fills the board. Two adjacent diamond-like regions are visible, with a black dot at the central meeting point, a right-hand exterior diamond, and wavy top and bottom lines labeled like singularities. On the right-hand diamond, labels \(t=\infty\), \(t=-\infty\), and \(r=\infty\) are visible, along with a family of interior curves.
- `lecture_05_figure_05.png`: A transition-layout frame. On the far left, part of the earlier fan-shaped compactified flat-space diagram remains visible; on the right, part of the Schwarzschild Penrose diagram remains visible. Susskind stands between them. This image is mainly about board organization and the handoff from one diagrammatic ingredient to the next.

## Blackboard Equations
- `lecture_05_figure_02.png`
  - \(t=\infty\) [visible]
  - \(r=0\) for the left vertical boundary [standard reconstruction]

- `lecture_05_figure_03.png`
  - \(r=\infty\) [visible]
  - \(t=\infty\) [visible]
  - \(t=-\infty\) [visible]
  - \(\mathrm{sing}_+\) [partially visible]
  - \(\mathrm{sing}_-\) [partially visible]
  - \(r=2MG\) for the horizon-side edge of the right exterior region [standard reconstruction]
  - \(r=6MG\) as a representative outer constant-\(r\) curve [standard reconstruction]
  - \(r=100MG\) as a farther-out constant-\(r\) curve [standard reconstruction]

- `lecture_05_figure_05.png`
  - no new legible equations beyond reused diagram labels [visible board layout rather than equation content]

## Diagram And Layout Reading
- `lecture_05_figure_02.png` shows the upper half of the compactified flat-space \((t,r)\) picture. The left vertical edge is the timelike line \(r=0\), the top endpoint is labeled \(t=\infty\), and the right tip is the compactified large-\(r\) endpoint. The outer straight edges are null boundaries of the wedge. Inside, one family of curves bows toward the right tip and another family cuts across them, matching Susskind’s discussion of constant-\(r\) and constant-\(t\) lines crowding together under compactification.
- `lecture_05_figure_03.png` shows the eternal Schwarzschild layout as Susskind is using it before collapse construction: two diamonds side by side, a central black point where the horizons meet, and wavy top and bottom singularity boundaries. The right-hand diamond is the exterior region that he is actually discussing. Its left edge is the horizon, its right tip is \(r=\infty\), and its top and bottom vertices are \(t=\pm\infty\). The interior curves are a hand-drawn grid for the exterior Schwarzschild coordinates: a family of constant-\(r\) worldlines and a family of constant-time slices.
- `lecture_05_figure_05.png` records the board as a workspace rather than a finished figure. The old flat-space ingredient remains at left, the Schwarzschild ingredient remains at right, and the visual point is that Susskind is about to combine these ingredients into the collapsing-shell Penrose diagram. This frame is most useful for narrative placement and board layout, not for exact mathematics.

## TeX Reconstruction Plan
- `lecture_05_figure_02.png` should remain visible in the notes. It is good documentary evidence that Susskind deliberately drew only the upper half of the compactified flat-space diagram at that moment. Nearby, add a clean TikZ redraw of the same upper-half wedge with a left \(r=0\) boundary, top label \(t=\infty\), right compactified tip, and two qualitative curve families. Do not infer an exact analytic curve shape from the chalk drawing.
- `lecture_05_figure_03.png` should remain visible and should be paired with a clean TikZ reconstruction. The TikZ figure should show the eternal Schwarzschild Penrose diagram at least far enough to preserve the right exterior diamond, the central meeting point, the top and bottom singularity lines, and the representative constant-\(r\) family. In the clean redraw, annotate only the labels that matter for the lecture flow: \(t=\pm\infty\), \(r=\infty\), horizon at \(r=2MG\), and a small number of sample outer radii such as \(r=6MG\) and \(r=100MG\).
- `lecture_05_figure_05.png` should remain visible only as a transition screenshot. It should not carry the mathematical load by itself. In the notes, use it to mark the moment where Susskind moves from reviewing the two Penrose-diagram “working parts” to constructing the collapse geometry. Its mathematics should be reconstructed by the cleaner TikZ figures attached to `lecture_05_figure_02.png` and `lecture_05_figure_03.png`, rather than by a separate new diagram derived from this screenshot alone.
- For this set, the reconstruction burden is almost entirely TikZ, not displayed equations. The visible blackboard content is chiefly labels and diagram geometry.

## Caption Drafts
- `lecture_05_figure_02.png`: Upper half of the compactified flat-space Penrose diagram
- `lecture_05_figure_03.png`: Schwarzschild Penrose diagram with representative constant-\(r\) curves
- `lecture_05_figure_05.png`: Board layout before the collapsing-shell Penrose construction

## Uncertainties
- In `lecture_05_figure_02.png`, only \(t=\infty\) is clearly legible. The right tip is unlabeled in the image, though the transcript strongly suggests it is the compactified large-\(r\) endpoint.
- In `lecture_05_figure_02.png`, the dot on the left vertical boundary is visible but unlabeled. It is best read as a chosen reference time, not as a separately named conformal-infinity point.
- In `lecture_05_figure_03.png`, the singularity labels are readable only approximately as \(\mathrm{sing}_+\) and \(\mathrm{sing}_-\). For polished notes, “future singularity” and “past singularity” may be clearer.
- In `lecture_05_figure_03.png`, the exact count and shape of the interior grid curves should not be overinterpreted. They are qualitative board lines, not precise coordinate plots.
- The transcript mentions spoken \(2mg\), \(6mg\), and \(100mg\). In the notes these should be standardized to \(2MG\), \(6MG\), and \(100MG\).
- `lecture_05_figure_05.png` is cropped on both sides and is best used only for transition and board-layout evidence, not for extracting exact labels or full diagram topology.