# Figure Notes
## Image Inventory
- `lecture_02_figure_01.png` shows the Stanford University title card on a dark background, with the red block `S`, green tree emblem, the text `STANFORD UNIVERSITY`, and the website `www.stanford.edu`. There is no lecturer, blackboard, equation, or diagram.
- `lecture_02_figure_02.png` shows Susskind standing at the left of a mostly blank whiteboard. On the board is a one-dimensional vector sketch: a long horizontal arrow labeled with a vector `R` and subscript `i`, a marked point at the right labeled `i`, and a smaller vector near the left labeled `A(x)` with an arrow over it.
- `lecture_02_figure_03.png` shows Susskind writing at the far right edge of the board. Across the top is a Gauss-theorem-style equation with a volume integral of `\nabla\cdot A` on the left and a surface integral on the right. Below it is an irregular closed region with a cross-hatched boundary patch labeled `A_\perp`.
- `lecture_02_figure_04.png` shows a later board state in the Gauss-law application. The top still carries the Gauss-theorem relation, the left side contains a large circular Gaussian surface with a smaller interior source region, and the right side shows a gravitational source term involving `-4\pi G`, an integral of `\rho\,d^3x`, and a lower line where the mass integral has been replaced by `M`.
- `lecture_02_figure_05.png` shows a concentric-sphere sketch used for the inside-the-Earth calculation: a larger outer circular boundary and a smaller inner red spherical surface. To the right appears the factor `G \frac{4\pi}{3} R^3 \rho =` or the same with lowercase `r`, with the right-hand side not yet visible.

## Blackboard Equations
- `lecture_02_figure_01.png`: no blackboard mathematics is present.
- `lecture_02_figure_02.png`: `\vec{R}_i` [visible]
- `lecture_02_figure_02.png`: `\vec{A}(x)` [visible]
- `lecture_02_figure_02.png`: `i` marking the source point [visible]
- `lecture_02_figure_02.png`: `\vec{R}_i = \vec{x}_i-\vec{x}` or the opposite convention [standard reconstruction]
- `lecture_02_figure_03.png`: `\int \nabla\!\cdot A\, dx\,dy\,dz = \int d\sigma` [visible]
- `lecture_02_figure_03.png`: `A_\perp` [visible]
- `lecture_02_figure_03.png`: `\int_V (\nabla\!\cdot \vec A)\, dV = \oint_{\partial V} A_\perp\, d\sigma` [standard reconstruction]
- `lecture_02_figure_04.png`: `\int \nabla\!\cdot A\, dx\,dy\,dz = \int d\sigma\, A_\perp` [partially visible]
- `lecture_02_figure_04.png`: `-4\pi G \int \rho\, d^3x` [visible]
- `lecture_02_figure_04.png`: `-4\pi G M = \cdots` [partially visible]
- `lecture_02_figure_04.png`: `\int \rho\, d^3x = M` [standard reconstruction]
- `lecture_02_figure_05.png`: `G\,\frac{4\pi}{3} R^3 \rho =` [visible]
- `lecture_02_figure_05.png`: `M(R)=\frac{4\pi}{3}R^3\rho` [standard reconstruction]
- `lecture_02_figure_05.png`: `4\pi R^2 A_\perp = -4\pi G\,\frac{4\pi}{3}R^3\rho` [standard reconstruction]
- `lecture_02_figure_05.png`: `A_\perp = -\frac{G\rho}{3}R` [standard reconstruction]

## Diagram And Layout Reading
- `lecture_02_figure_01.png` is purely institutional and contributes no lecture geometry, board structure, or mathematical layout.
- `lecture_02_figure_02.png` is a clean board-layout frame for the gravitational-field geometry. The visual organization is simple and useful: the field point sits at the left, the source point `i` at the right, and the long displacement vector spans between them. The smaller vector labeled `A(x)` is anchored near the left point, so the board is juxtaposing source-to-field geometry with the local acceleration field.
- `lecture_02_figure_03.png` organizes the argument from left to right. The top line states Gauss’s theorem symbolically; below it the irregular region and cross-hatched boundary patch explain what the surface element means geometrically. The label `A_\perp` is attached to the patch rather than embedded in the equation, so the board is using the sketch to interpret the flux term.
- `lecture_02_figure_04.png` shows the transition from the abstract theorem to the gravitational application. The top line is still the theorem, but the main visual emphasis has shifted to a spherical source inside a larger enclosing circle and to the right-hand mass integral. The board layout suggests: theorem on top, source geometry on the left, gravitational specialization on the right.
- `lecture_02_figure_05.png` is a more specialized spherical-symmetry sketch. The larger outer circle represents the body or outer boundary, while the smaller inner red circle marks a Gaussian surface internal to the mass distribution. Susskind’s gesturing hand indicates the inner surface, so the frame is mainly documentary evidence for the geometry of the inside-the-Earth derivation rather than for a finished algebraic line.

## TeX Reconstruction Plan
- `lecture_02_figure_01.png` should not remain visible in the chapter body. It is only a title card and has no value for note writing beyond provenance.
- `lecture_02_figure_02.png` should remain visible. Pair it with a clean TikZ redraw of the source point, field point, displacement vector, and local field vector, plus a short displayed equation or prose note fixing the sign convention for `\vec R_i`. The screenshot is good documentary evidence, but the final notes should not rely on the ambiguous board arrow alone.
- `lecture_02_figure_03.png` should remain visible. Pair it with a cleaned displayed version of Gauss’s theorem, preferably in standard notation such as `\int_V (\nabla\cdot\vec A)\,dV = \oint_{\partial V} A_\perp\,d\sigma`. A separate TikZ redraw is optional rather than necessary, since the patch sketch is already legible.
- `lecture_02_figure_04.png` should remain visible if the chapter wants documentary support for the move from Gauss’s theorem to the gravitational mass integral. Pair it immediately with cleaned displayed equations showing the replacement of `\int \rho\,d^3x` by the enclosed mass `M`, and, if helpful, a small clean schematic of a spherical source inside a Gaussian sphere.
- `lecture_02_figure_05.png` should remain visible. Pair it with a clean TikZ redraw of the outer body and inner Gaussian sphere, and typeset the algebraic reconstruction nearby: the enclosed mass of a uniform sphere, the corresponding Gauss-law relation, and the resulting linear-in-radius interior field. The screenshot alone is not enough for the final derivation, but it is valuable evidence for the board layout and the concentric-sphere setup.

## Caption Drafts
- `lecture_02_figure_01.png`: Stanford title card
- `lecture_02_figure_02.png`: Field vector and source-point displacement
- `lecture_02_figure_03.png`: Surface-flux term in Gauss’s theorem
- `lecture_02_figure_04.png`: Gauss law with enclosed mass
- `lecture_02_figure_05.png`: Concentric spheres and enclosed-mass factor

## Uncertainties
- `lecture_02_figure_02.png`: the exact sign convention for `\vec R_i` is unstable in the surrounding lecture. The arrow direction in the frame and the spoken correction around it should be reconciled carefully in the notes rather than copied mechanically.
- `lecture_02_figure_02.png`: the left endpoint is not explicitly labeled in the frame; the interpretation as the field point `x` comes from the nearby `A(x)` label and the transcript context.
- `lecture_02_figure_03.png`: the right-hand side of the surface integral is still being written, so the complete formula is only partly visible even though the intended `A_\perp` factor is clear from the nearby patch label.
- `lecture_02_figure_04.png`: the lower line on the right is incomplete or cropped; it clearly involves replacing the density integral by `M`, but the full equality to the flux term is not fully legible in the frame.
- `lecture_02_figure_04.png`: the handwritten text at the top right looks like `Gauss The...`, but the full word is cut off.
- `lecture_02_figure_05.png`: the radius symbol could be read as uppercase `R` or lowercase `r`; the board is not crisp enough to force the notation.
- `lecture_02_figure_05.png`: the right-hand side of the equation after the equals sign is absent from the frame, so any full derivation must be reconstructed from transcript and surrounding mathematics, not claimed as directly visible.
- `lecture_02_figure_05.png`: the small mark near the top of the sphere sketch is too unclear to trust as a definitive label.