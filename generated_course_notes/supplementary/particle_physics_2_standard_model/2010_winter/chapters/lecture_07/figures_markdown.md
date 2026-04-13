# Figure Notes
## Image Inventory
- `lecture_07_figure_02.png`: Left board shows the complex \(\phi\)-plane with horizontal and vertical axes labeled by the real and imaginary components, a vector from the origin into the first quadrant, and a second nearby vector/arc suggesting a phase rotation. Beneath the sketch are the component formulas for \(\phi\) and \(\phi^*\). On the separate right board, the invariant combination \(\phi^*\phi\) is written by itself.
- `lecture_07_figure_03.png`: A wide whiteboard view with a quartic potential written at the top left, a rewritten Lagrangian in \(\rho,\alpha\) variables across the middle, a boxed low-energy angular term below, and a lightly drawn symmetry-breaking potential sketch on the right. The right-hand drawing includes both a surface-of-revolution view and a lower cross-section-like curve.
- `lecture_07_figure_04.png`: The lecturer stands in front of a red board sketch. The main visible content is a left vertical support/marker with a small open circle and a long, gently varying red line extending rightward behind him. Partial earlier equations remain at the far left and far right edges but are not the main point of the frame.
- `lecture_07_figure_05.png`: The right board contains the cleaned gauge-theory equations: covariant derivatives of \(\phi\) and \(\phi^*\), then a scalar kinetic-plus-potential line, and a final \(+F^2\) term below. The left board preserves partial intermediate phase-transformation algebra, including a visible phase factor and an \(A-\partial\theta\)-type shift.

## Blackboard Equations
- `lecture_07_figure_02.png`: \(\phi_R\) [visible]
- `lecture_07_figure_02.png`: \(\phi_I\) [visible]
- `lecture_07_figure_02.png`: \(\phi=\phi_R+i\phi_I\) [visible]
- `lecture_07_figure_02.png`: \(\phi^*=\phi_R-i\phi_I\) [visible]
- `lecture_07_figure_02.png`: \(\phi^*\phi\) [visible]

- `lecture_07_figure_03.png`: \(-a\,\phi^*\phi+b(\phi^*\phi)^2\) [visible]
- `lecture_07_figure_03.png`: \((\partial\rho)^2+\rho^2(\partial\alpha)^2-V(\rho)\) [standard reconstruction]
- `lecture_07_figure_03.png`: \(f^2(\partial\alpha)^2\) [partially visible]

- `lecture_07_figure_04.png`: \(\phi^*\phi\) [partially visible]
- `lecture_07_figure_04.png`: \(e^{i\alpha}\) [partially visible]
- `lecture_07_figure_04.png`: \(-a\,\phi^*\phi\) [partially visible]

- `lecture_07_figure_05.png`: \(D_\mu\phi=\partial_\mu\phi+iA_\mu\phi\) [standard reconstruction]
- `lecture_07_figure_05.png`: \(D_\mu\phi^*=\partial_\mu\phi^*-iA_\mu\phi^*\) [standard reconstruction]
- `lecture_07_figure_05.png`: \(D_\mu\phi\,D_\mu\phi^*-V(\phi^*\phi)\) [standard reconstruction]
- `lecture_07_figure_05.png`: \(+\,F^2\) [visible]
- `lecture_07_figure_05.png`: \(\phi e^{i\theta}\) [partially visible]
- `lecture_07_figure_05.png`: \(A-\partial\theta\) [partially visible]

## Diagram And Layout Reading
- `lecture_07_figure_02.png` is organized around the complex-field picture. The left board is a coordinate plane with \(\phi_R\) on the horizontal axis and \(\phi_I\) on the vertical axis. A vector from the origin and a nearby curved arrow/second vector show the geometric meaning of multiplying \(\phi\) by a phase: rotation in the \((\phi_R,\phi_I)\) plane. The isolated \(\phi^*\phi\) on the right board visually separates the rotationally invariant quantity from the component decomposition.
- `lecture_07_figure_03.png` combines algebra and geometry on one board. The left half moves from the quartic potential to the \(\rho,\alpha\) decomposition of the Lagrangian and then to the low-energy fixed-radius term. The right half is the important visual companion: a lightly drawn Mexican-hat style surface above and a lower radial slice beneath it, showing a central high point and lower-energy off-origin minima. The lower curve appears to pick out radial motion about a chosen minimum.
- `lecture_07_figure_04.png` is mainly a red wave/profile sketch rather than an equation frame. The visible drawing shows a left vertical post or boundary marker, a small open circle near its top, and a gently varying red line stretching to the right. The lecture context suggests a long-wavelength Goldstone-wave analogy; the image itself reads as a slowly varying one-dimensional deformation. The lecturer blocks the right half, so the screenshot documents board rhythm more reliably than full geometry.
- `lecture_07_figure_05.png` has a split layout that matters pedagogically. The left board retains the phase-transformation work, while the right board presents the cleaned final formulas. This makes the figure useful not only for individual equations but also for showing how Susskind moves from the transformation law to the covariant derivative and then to the gauge-invariant Lagrangian.

## TeX Reconstruction Plan
- `lecture_07_figure_02.png` must remain visible. Pair it with a clean displayed block
  \[
  \phi=\phi_R+i\phi_I,
  \qquad
  \phi^*=\phi_R-i\phi_I,
  \qquad
  \phi^*\phi=\phi_R^2+\phi_I^2,
  \]
  and a TikZ redraw of the complex \(\phi\)-plane with a rotated vector and small angular arc.
- `lecture_07_figure_03.png` must remain visible. Typeset the cleaned equations for the quartic potential and the \(\rho,\alpha\) Lagrangian nearby, and redraw the potential sketch in TikZ: one surface-of-revolution or Mexican-hat schematic plus a radial cross-section if both views are useful.
- `lecture_07_figure_04.png` should remain visible if this Goldstone-wave example is kept in the chapter, but it needs a clean TikZ redraw for readability. Do not rely on the screenshot alone for the full geometry, because the right endpoint and some of the line are obscured by the lecturer. Treat the residual equations at the margins as incidental leftovers, not the main mathematical content of the figure.
- `lecture_07_figure_05.png` must remain visible. Pair it with a clean aligned equation block for the covariant derivatives and the resulting gauge-invariant Lagrangian term. No TikZ redraw is necessary; the main value here is the readable equation layout and the two-board transition from derivation to final form.

## Caption Drafts
- `lecture_07_figure_02.png`: Complex field components and phase rotation on the \(\phi\)-plane.
- `lecture_07_figure_03.png`: Polar-field Lagrangian and symmetry-breaking potential.
- `lecture_07_figure_04.png`: Long-wavelength Goldstone-wave sketch.
- `lecture_07_figure_05.png`: Covariant derivatives and gauge-invariant gauge-field terms.

## Uncertainties
- In `lecture_07_figure_02.png`, the curved arrow and second radial segment are clear in intent but not fully labeled; the image suggests a phase rotation, but the angle itself is not explicitly written.
- In `lecture_07_figure_02.png`, the far-left edge contains cropped leftover notation that should not be over-transcribed.
- In `lecture_07_figure_03.png`, the derivative notation is handwritten loosely; the standard completion to \(\partial\rho\) and \(\partial\alpha\) is transcript-supported rather than perfectly typographically legible from the image alone.
- In `lecture_07_figure_03.png`, the lower right labels on the potential sketch are faint and should not be quoted too confidently; the geometry matters more than the tiny labels.
- In `lecture_07_figure_03.png`, the 3D surface and the lower curve are both lightly drawn; the notes should redraw them cleanly rather than treat the screenshot as fully legible on its own.
- In `lecture_07_figure_04.png`, the red profile is partly blocked by the lecturer, and the right endpoint/support is not securely visible in this selected frame.
- In `lecture_07_figure_04.png`, the subtitle mentions spin waves, but the visible sketch reads more generally as a long-wavelength wave analogy; the notes should avoid claiming more specific board detail than the image actually preserves.
- In `lecture_07_figure_05.png`, the right-board formulas are legible in structure, but some trailing factors are soft enough that the fully normalized expressions should be treated as cautious standard reconstructions.
- In `lecture_07_figure_05.png`, the left-board transformation algebra is incomplete in frame and should be used only as layout evidence, not as a stand-alone transcription target.