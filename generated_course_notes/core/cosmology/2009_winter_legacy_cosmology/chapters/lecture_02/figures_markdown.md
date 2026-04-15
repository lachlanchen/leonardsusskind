# Figure Notes
## Image Inventory
- `lecture_02_figure_02.png`: Susskind stands with his back to the board. At left there is a partial expanding-grid or spacetime sketch with slanted vertical lines and two marked points on an upper horizontal segment. At right there are two partially visible line elements, an upper spatial one and a lower spacetime one.
- `lecture_02_figure_03.png`: A small concentric central source is drawn at left, a test mass labeled `m` sits to its right with an outward arrow, and the isolated kinetic-energy term `mv^2/2` appears at upper right.
- `lecture_02_figure_04.png`: The same source-and-test-mass sketch remains at left, now paired with the fuller energy expression showing the kinetic term minus a gravitational potential term. Susskind’s hand is low and does not significantly block the sketch.
- `lecture_02_figure_05.png`: Two qualitative graph sketches are visible. Near the top edge there is a partial graph with a horizontal axis labeled `D` at the right. Lower down there is a clearer cross-shaped set of axes with an upper nearly horizontal branch and a lower curved branch, which Susskind points to.
- `lecture_02_figure_06.png`: A later energy-equation frame showing `mv^2/2` minus the gravitational term, with Susskind pointing directly at the denominator of the potential term. The earlier source sketch is mostly cropped away, leaving only a bit of the leftward board context.

## Blackboard Equations
- `lecture_02_figure_02.png`: `ds^2 = a(t)^2\left(dx^2+dy^2+dz^2\right)` [partially visible]
- `lecture_02_figure_02.png`: `d\tau^2 = dt^2 - a(t)^2(\cdots)` [partially visible]
- `lecture_02_figure_02.png`: `g_{\mu\nu}=\mathrm{diag}(1,-a^2,-a^2,-a^2)` [standard reconstruction]
- `lecture_02_figure_03.png`: `\frac{mv^2}{2}` [visible]
- `lecture_02_figure_03.png`: `m` [visible]
- `lecture_02_figure_04.png`: `\frac{mv^2}{2} - \frac{mMG}{D}` [visible]
- `lecture_02_figure_04.png`: `m` [visible]
- `lecture_02_figure_05.png`: `\frac{1}{D}` [standard reconstruction]
- `lecture_02_figure_05.png`: `-\frac{1}{D}` [standard reconstruction]
- `lecture_02_figure_05.png`: `D` [visible, on the upper partial graph]
- `lecture_02_figure_06.png`: `\frac{mv^2}{2} - \frac{mMG}{D}` [visible]

## Diagram And Layout Reading
- `lecture_02_figure_02.png`: The board is organized in the lecture’s characteristic sequence: a sketch at left, then formulas at right. The left sketch appears to represent an expanding coordinate mesh or spacetime cartoon with a marked pair of neighboring points; the right side translates that picture into line-element form.
- `lecture_02_figure_03.png`: The left drawing is a minimal Newtonian setup: a central gravitating source, a small outward-moving test mass, and a radial arrow. The equation area is still sparse, which is important because this frame catches the stage before the potential term is added.
- `lecture_02_figure_04.png`: This frame preserves the same Newtonian source-test-mass geometry but now ties it to the full conserved-energy expression. It is the clearest combined board witness for the transition from pure kinetic energy to kinetic plus negative potential energy.
- `lecture_02_figure_05.png`: The lower graph is the important one for note writing. It is an upside-down version of the upper decreasing curve and is being used qualitatively to explain why an attractive force points toward decreasing potential energy. The lower graph should be read as the main visual target, with the upper partial graph serving as supporting context.
- `lecture_02_figure_06.png`: This is not a new derivation but a rhetorical emphasis frame. The equation is already on the board, and Susskind’s pointing gesture directs attention to the potential term as the dominant contribution when the initial velocity is small.

## TeX Reconstruction Plan
- `lecture_02_figure_02.png` must remain visible. Pair it with cleaned displayed equations for the spatial and spacetime line elements, and add a TikZ redraw of the left-hand expanding-grid sketch so the geometry is readable without relying on the cropped chalk lines.
- `lecture_02_figure_03.png` should remain visible if the notes preserve the live buildup from setup to formula. Nearby, redraw the source-test-mass sketch in TikZ and typeset `\frac{mv^2}{2}` cleanly as the kinetic term introduced before the potential term appears.
- `lecture_02_figure_04.png` must remain visible. It is the best screenshot for the full Newtonian energy formula, and it should be paired with a cleaned displayed equation such as `E=\frac{mv^2}{2}-\frac{GMm}{d}` or the lecture-order board form, depending on house notation.
- `lecture_02_figure_05.png` must remain visible and should be accompanied by a TikZ redraw of the qualitative `1/D` and `-1/D` graphs. The redraw should regularize the axes and asymptotic behavior, since the board version is schematic and partly cropped.
- `lecture_02_figure_06.png` should remain visible as the later emphasis shot if the notes explicitly preserve the beat that, for small initial velocity, the potential energy dominates. Use the screenshot for emphasis and the cleaned equation for mathematical authority.

## Caption Drafts
- `lecture_02_figure_02.png`: Spacetime interval and expanding-grid sketch
- `lecture_02_figure_03.png`: Outgoing test mass and kinetic energy
- `lecture_02_figure_04.png`: Kinetic plus negative gravitational potential
- `lecture_02_figure_05.png`: Qualitative plots of \(1/D\) and \(-1/D\)
- `lecture_02_figure_06.png`: Potential-energy term dominating the total energy

## Uncertainties
- `lecture_02_figure_02.png`: The rightmost part of the spacetime line element is cropped, and the metric-tensor matrix itself is not actually visible in this crop; the full diagonal form is transcript-supported rather than frame-legible.
- `lecture_02_figure_02.png`: The exact interpretation of the left-hand sketch is only partly secure from the image alone; it is clearly an expanding-grid or spacetime cartoon, but some chalk lines are truncated.
- `lecture_02_figure_03.png`: The concentric source is clear, but the small marks beneath it are not fully interpretable from the frame alone and should not be over-read in the redraw.
- `lecture_02_figure_04.png` and `lecture_02_figure_06.png`: The board writes the gravitational term in the order `mMG/D`, which is visually legible but not the conventional typeset ordering; the notes may regularize it while noting that the screenshot preserves the original board ordering.
- `lecture_02_figure_04.png` and `lecture_02_figure_06.png`: The denominator looks like uppercase `D`, consistent with the lecture’s spoken “distance,” but the notes should avoid overclaiming if a later house style prefers lowercase `d`.
- `lecture_02_figure_05.png`: The lower graph has no visible axis label in the frame, and the identification as `-1/D` comes from the lecture context plus the visible upper partial `D`-labeled graph, not from an explicit written formula on the lower plot.