# Visual Evidence
## Frame Inventory
- `lecture_02_figure_01.png`: Stanford title/campus opening shot with no blackboard mathematics or diagram content; this screenshot should not remain in the final notes.
- `lecture_02_figure_02.png`: Right side of the board during the light-front review, showing the transverse-energy term and a new line beginning `H=`; this screenshot should remain in the final notes as visual evidence.
- `lecture_02_figure_03.png`: Board shot of a bead-chain sketch labeled `N mass points` together with the discrete string energy; this screenshot should remain in the final notes.
- `lecture_02_figure_04.png`: Transitional board shot where the continuum string Lagrangian is being written with the kinetic term already visible and the minus potential term being added; this screenshot should remain in the final notes.
- `lecture_02_figure_05.png`: Tight close-up of the endpoint-force / continuum-limit step centered on `\partial X/\partial \sigma` and the beginning of the discrete increment replacement; this screenshot should remain in the final notes.
- `lecture_02_figure_06.png`: Board shot of the mode expansion for `\partial X/\partial \sigma` with a faint lower quadratic mode expression still visible; this screenshot should remain in the final notes.

## Equation Extraction
- `lecture_02_figure_02.png`: `(E-P_z)=` [visible]
- `lecture_02_figure_02.png`: `\dfrac{p_x^2+p_y^2}{2P_z}` [visible]
- `lecture_02_figure_02.png`: `H=` [visible]
- `lecture_02_figure_02.png`: `E-P_z=\dfrac{p_x^2+p_y^2}{2P_z}+\dfrac{M^2}{2P_z}` [standard completion]
- `lecture_02_figure_02.png`: `H=i\,\dfrac{d}{dt}` [standard completion]

- `lecture_02_figure_03.png`: `E=` [visible]
- `lecture_02_figure_03.png`: `\sum \dfrac{m\dot X_i^2}{2}` [visible]
- `lecture_02_figure_03.png`: `k\,\dfrac{(\Delta X_i)^2}{2}` [partially visible]
- `lecture_02_figure_03.png`: `E=\sum_i\left(\dfrac{m\dot X_i^2}{2}+\dfrac{k}{2}(\Delta X_i)^2\right)` [standard completion]

- `lecture_02_figure_04.png`: `\dfrac{1}{2\pi}` [visible]
- `lecture_02_figure_04.png`: `\int_0^\pi` [visible]
- `lecture_02_figure_04.png`: `\left(\dfrac{\partial X}{\partial \tau}\right)^2` [visible]
- `lecture_02_figure_04.png`: `\left(\dfrac{\partial X}{\partial \sigma}\right)^2` [partially visible]
- `lecture_02_figure_04.png`: `L=\dfrac{1}{2\pi}\int_0^\pi d\sigma\left[\left(\dfrac{\partial X}{\partial \tau}\right)^2-\left(\dfrac{\partial X}{\partial \sigma}\right)^2\right]` [standard completion]

- `lecture_02_figure_05.png`: `\mu=\dfrac{1}{N}` [partially visible]
- `lecture_02_figure_05.png`: `k=\dfrac{N}{\pi^2}` [partially visible]
- `lecture_02_figure_05.png`: `\dfrac{\partial X}{\partial \sigma}` [visible]
- `lecture_02_figure_05.png`: `\Delta X=\dfrac{\partial X}{\partial \sigma}\,\Delta\sigma` [standard completion]

- `lecture_02_figure_06.png`: `\dfrac{\partial X}{\partial \sigma}=` [visible]
- `lecture_02_figure_06.png`: `-\sum_{n=0}^{\infty} nX_n\sin n\sigma` [partially visible]
- `lecture_02_figure_06.png`: lower line with a center-of-mass term and a quadratic mode sum, schematically of the form `\dfrac{\dot X_0^2}{2}+\sum_n \dfrac{1}{4}\dot X_n^2` or nearby equivalent [partially visible]

## Diagram Extraction
- `lecture_02_figure_01.png`: No usable mathematical diagram; omit entirely.
- `lecture_02_figure_02.png`: The important visual feature is board structure rather than a diagram: an older formula remains on the upper right while a new `H=` line starts below it. Preserve as a screenshot, not as TikZ.
- `lecture_02_figure_03.png`: The bead-chain/open-string sketch should be redrawn in TikZ as a chain of mass points connected by springs, but the original screenshot should also be preserved nearby because it shows the exact board pairing of sketch and energy formula.
- `lecture_02_figure_04.png`: No separate geometric diagram is needed; preserve the screenshot as evidence of the transitional board state while typesetting the cleaned continuum Lagrangian.
- `lecture_02_figure_05.png`: The local endpoint-force picture is implicit rather than fully drawn. A small TikZ schematic of the last two masses and their connecting spring would help the notes, but the screenshot should remain because it is the actual visual evidence for the `\Delta X \to (\partial_\sigma X)\Delta\sigma` step.
- `lecture_02_figure_06.png`: No TikZ figure is necessary; preserve the screenshot and typeset the cleaned sine-mode derivative expansion.

## Reconstruction Guidance
- Treat `lecture_02_figure_02.png` as evidence for the conceptual move from boosted relativistic energy to an effective Hamiltonian. In the notes, typeset the full displayed formula cleanly and keep the screenshot to show that the lecturer explicitly paused to reinterpret the expression as `H`.
- Treat `lecture_02_figure_03.png` as the anchor for the discrete mechanical model. The notes should typeset the discrete energy in clean summation form and also redraw the bead-chain as TikZ, but keep the screenshot because the board makes the picture-to-equation transition explicit.
- Treat `lecture_02_figure_04.png` as a transitional derivation frame rather than a finished board theorem. The notes should present a polished continuum Lagrangian with explicit measure and signs, while the screenshot remains as evidence for the moment where the minus potential term is introduced.
- Treat `lecture_02_figure_05.png` as local evidence for the continuum-limit replacement used in the endpoint-force argument. The clean notes should state the replacement as a short displayed equation and, if helpful, accompany it with a small endpoint schematic; use the transcript to stabilize the exact equality.
- Treat `lecture_02_figure_06.png` as evidence for the derivative of a cosine-mode expansion becoming a sine-mode expansion with an extra factor of `n` and a minus sign. The notes should typeset the cleaned formula as `\partial_\sigma X=-\sum_{n\ge 1} nX_n\sin n\sigma`, with the screenshot kept nearby as visual support.
- Use the transcript, not the frames alone, to settle hidden indices, overall summation ranges, and whether a given displayed quantity is an energy or a Lagrangian. The frames are strongest when they confirm a sign, a prefactor, a board layout transition, or the existence of a sketch.

## Uncertainties
- In `lecture_02_figure_02.png`, the full left-hand algebra is cropped, and the mass term on the right is not fully visible; `H=i\,d/dt` is lecture-supported but not literally completed on the board in this frame.
- In `lecture_02_figure_03.png`, the subscript on `\Delta X_i` is not perfectly crisp, and the handwritten `m` should be treated cautiously because later lecture prose distinguishes the analog bead mass from the relativistic string mass.
- In `lecture_02_figure_04.png`, the leading symbol before the integral is partly obscured by the lecturer, so whether the board explicitly shows `L=` is not guaranteed by the image alone.
- In `lecture_02_figure_05.png`, the top normalization data are cropped on the right, the role of the isolated handwritten `N` near `\partial X/\partial \sigma` is unclear, and only the beginning of the discrete increment is visible.
- In `lecture_02_figure_06.png`, the lower expression is too faint and incomplete to trust verbatim, and the upper summation visually appears to begin at `n=0` even though the cleaned differentiated formula should normally start at `n=1` because the zero mode drops out.
- The transcript itself is garbled in a few nearby stretches, especially around some continuum-limit and later quantization passages, so any aggressive completion beyond the standard and lecture-motivated formulas should be avoided.