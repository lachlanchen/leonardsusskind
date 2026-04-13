# Figure Notes
## Image Inventory
- `lecture_02_figure_02.png`: A tight crop of the left blackboard column. The most prominent equation is `\lambda f = c`, with the reciprocal form written below. Above it are the wavelength and angular-frequency lines, but the crop trims the wider board context.
- `lecture_02_figure_03.png`: A wider shot of the board with Susskind gesturing toward the left column. The board is divided into two columns by a vertical line. The left column collects wave definitions and relations; the right column contains Planck-constant, energy, and momentum formulas.
- `lecture_02_figure_04.png`: A right-side board shot with Susskind standing at left. The upper-right region clearly shows the photon-momentum relation in two forms, with the middle fraction boxed. Earlier energy and momentum formulas remain partially visible to the left.
- `lecture_02_figure_05.png`: A right-board shot centered on the nonrelativistic energy formula and a boxed frequency-wavelength relation for a slow particle. Some earlier writing survives at the far left edge, including a partial `h/\lambda`.
- `lecture_02_figure_06.png`: A sparse board sketch: a long horizontal segment or path, a small marked point at the right end, and the label `L` beneath the line. Susskind stands to the right of the sketch.

## Blackboard Equations
- `lecture_02_figure_02.png`: `\omega = 2\pi f` [visible]
- `lecture_02_figure_02.png`: `\lambda = \text{wave len...}` [partially visible]
- `lecture_02_figure_02.png`: `\lambda = \text{wavelength}` [standard reconstruction]
- `lecture_02_figure_02.png`: `\lambda f = c` [visible]
- `lecture_02_figure_02.png`: `\frac{f}{c} = \frac{1}{\lambda}` [visible]

- `lecture_02_figure_03.png`: `f = \text{freq c/s}` [visible]
- `lecture_02_figure_03.png`: `f = \text{frequency}` [standard reconstruction]
- `lecture_02_figure_03.png`: `\omega = 2\pi f` [visible]
- `lecture_02_figure_03.png`: `\lambda = \text{wave len...}` [partially visible]
- `lecture_02_figure_03.png`: `\lambda = \text{wavelength}` [standard reconstruction]
- `lecture_02_figure_03.png`: `\lambda f = c` [visible]
- `lecture_02_figure_03.png`: `\frac{f}{c} = \frac{1}{\lambda}` [visible]
- `lecture_02_figure_03.png`: `\hbar = \frac{h}{2\pi}` [visible]
- `lecture_02_figure_03.png`: `E = \hbar\omega = \cdots` [partially visible]
- `lecture_02_figure_03.png`: `E = \hbar\omega = hf` [standard reconstruction]
- `lecture_02_figure_03.png`: `\vec p = m\vec v` [visible]
- `lecture_02_figure_03.png`: `|p| = \frac{E}{c}` [visible]

- `lecture_02_figure_04.png`: `\hbar = \frac{h}{2\pi}` [partially visible]
- `lecture_02_figure_04.png`: `E = \hbar\omega = hf` [partially visible]
- `lecture_02_figure_04.png`: `\vec p = m\vec v` [partially visible]
- `lecture_02_figure_04.png`: `|p| = \frac{E}{c}` [partially visible]
- `lecture_02_figure_04.png`: `p_{\text{photon}} = \frac{hf}{c} = \frac{h}{\lambda}` [visible]

- `lecture_02_figure_05.png`: `\psi` [visible]
- `lecture_02_figure_05.png`: `E = \frac{1}{2}mv^2 = \frac{1}{2}\frac{p^2}{m}` [visible]
- `lecture_02_figure_05.png`: `f = \frac{1}{2m}\frac{h}{\lambda^2}` [visible]
- `lecture_02_figure_05.png`: `\frac{h}{\lambda}` [partially visible]

- `lecture_02_figure_06.png`: `L` [visible]

## Diagram And Layout Reading
- `lecture_02_figure_02.png` preserves only the left-hand derivation stack. The large central `\lambda f = c` is the visual anchor, with the reciprocal form directly below it. The crop shows that this relation is being isolated and reused algebraically.
- `lecture_02_figure_03.png` is the most informative board-layout image. The vertical divider splits the board into a left review column and a right application column. On the left are wave definitions; on the right are quantum and momentum formulas. Susskind’s gesture makes the left column the immediate focus.
- `lecture_02_figure_04.png` shows a new emphasis on the upper-right board. The boxed `hf/c` serves as an intermediate expression, and the equality to `h/\lambda` is written to its right. The remaining partial formulas at left show that this result is being extracted from the earlier list rather than introduced from nowhere.
- `lecture_02_figure_05.png` has a clear top-to-bottom hierarchy: the nonrelativistic energy identity is written above, and the boxed lower formula is the takeaway. The layout strongly suggests a derivation from energy and momentum to a frequency-wavelength relation for slow particles.
- `lecture_02_figure_06.png` is not a literal geometric circle. It is a one-dimensional path sketch: a long line, a marked end, and a length label `L`. The sparseness matters, because the lecture is explicitly abstracting away from ordinary geometry and moving toward periodic identification.

## TeX Reconstruction Plan
- `lecture_02_figure_02.png` must remain visible as the documentary crop for the wave relations used in the photon-momentum step. Nearby, the notes should typeset clean display equations for `\lambda f = c` and `\frac{f}{c}=\frac{1}{\lambda}` or equivalently `f=\frac{c}{\lambda}`. No TikZ redraw is needed.
- `lecture_02_figure_03.png` must remain visible because it records the two-column board organization: general wave definitions on the left and quantum-momentum formulas on the right. Nearby, the notes should typeset a compact clean summary of these formulas, but the screenshot should remain as board-layout evidence.
- `lecture_02_figure_04.png` must remain visible as the blackboard evidence for the general momentum relation written in wavelength form. Nearby, the notes should typeset the clean equation `p=\frac{hf}{c}=\frac{h}{\lambda}` or `p=\frac{h}{\lambda}` and, if useful, remind the reader of `E=hf` and `|p|=\frac{E}{c}`.
- `lecture_02_figure_05.png` must remain visible as the documentary evidence for the nonrelativistic derivation. Nearby, the notes should typeset the chain
  `E=\frac{1}{2}mv^2=\frac{p^2}{2m}`,
  `p=\frac{h}{\lambda}`,
  and then
  `f=\frac{h}{2m\lambda^2}`.
  No TikZ redraw is needed.
- `lecture_02_figure_06.png` must remain visible, but it should be paired with a TikZ redraw. The screenshot preserves the blackboard fact that Susskind first represents the periodic world by a labeled path of total length `L`, not by a polished geometric circle. The TikZ figure nearby should make the endpoint identification explicit and can be drawn either as a line with identified ends or as a schematic loop, while stating clearly in the prose that the geometry is only schematic.

## Caption Drafts
- `lecture_02_figure_02.png`: Wave relations used in the photon-momentum step
- `lecture_02_figure_03.png`: Two-column board of wave and momentum formulas
- `lecture_02_figure_04.png`: Photon momentum written as `hf/c = h/\lambda`
- `lecture_02_figure_05.png`: Nonrelativistic energy and matter-wave frequency relation
- `lecture_02_figure_06.png`: Schematic path of total length `L`

## Uncertainties
- In `lecture_02_figure_02.png` and `lecture_02_figure_03.png`, the word after `\lambda =` is only partially legible as `wave len...`; `\lambda = \text{wavelength}` is supported by the lecture but not fully by the pixels alone.
- In `lecture_02_figure_03.png`, the shorthand `f = \text{freq c/s}` is visibly abbreviated. The intended meaning is frequency in cycles per second, but the exact handwriting is compressed.
- In `lecture_02_figure_03.png`, the right-column energy line is cropped after `E=\hbar\omega=`; completing it to `hf` requires transcript-backed standard reconstruction.
- In `lecture_02_figure_04.png`, the handwritten label to the left of the upper-right formula looks like `P_{photon}` or a similar note. It is safest in the notes to typeset the cleaned relation as `p_{\text{photon}}`.
- In `lecture_02_figure_04.png`, the left-side boxed annotation appears to include something like `Non Rel`, but it is not crisp enough to rely on as a formal label.
- In `lecture_02_figure_05.png`, the boxed lower formula is legible as `f = \frac{1}{2m}\frac{h}{\lambda^2}`, but the spacing is handwritten and should be regularized in the typeset version.
- In `lecture_02_figure_06.png`, the screenshot itself does not show the endpoint-identification trick explicitly; it only shows the path and the label `L`. The periodic interpretation comes from the surrounding lecture, so any LaTeX redraw should make clear that the closed or identified topology is a cautious reconstruction, not something fully drawn in the frame.