# Figure Notes
## Image Inventory
- `lecture_02_figure_01.png`: Opening Stanford title sequence. Large white title letters overlay a courtyard/campus view with red-roof buildings; there is no blackboard, lecturer-board interaction, or mathematical content.
- `lecture_02_figure_02.png`: Close-up of the right side of the board during the light-cone review. A vertical divider splits the board; to the right is a transverse-energy correction term, and beneath it Susskind is writing a new line beginning with `H =`.
- `lecture_02_figure_03.png`: Clean board shot showing a bead-chain sketch of an open string at upper left, the handwritten label `N mass points`, and below that a discrete energy formula with a large summation, a kinetic term, and a spring term.
- `lecture_02_figure_04.png`: Transitional board shot from the discrete model to the continuum Lagrangian. A leftover discrete sum appears at upper left, while the main new content is a continuum integral with prefactor `1/2\pi`, a visible `(\partial X/\partial \tau)^2` term, and the potential term being written with a minus sign.
- `lecture_02_figure_05.png`: Tight close-up of the discrete-to-continuum replacement near the string endpoint argument. The main visible object is `\partial X/\partial \sigma`, with a delta symbol beginning on the right; above it remain normalization notes involving `1/N` and a partially cropped spring constant scaling.
- `lecture_02_figure_06.png`: Board shot from the Fourier-mode analysis. The top line shows the derivative `\partial X/\partial \sigma` expanded as a sine-mode sum; a fainter lower line contains a separate quadratic mode expression from the earlier energy decomposition.

## Blackboard Equations
- `lecture_02_figure_01.png`: no blackboard equations.

- `lecture_02_figure_02.png`: `(E-P_z)=` [visible]
- `lecture_02_figure_02.png`: `\dfrac{p_x^2+p_y^2}{2P_z}` [visible]
- `lecture_02_figure_02.png`: `H=` [visible]
- `lecture_02_figure_02.png`: `E-P_z=\dfrac{p_x^2+p_y^2}{2P_z}+\dfrac{M^2}{2P_z}` [standard reconstruction]
- `lecture_02_figure_02.png`: `H=i\,\dfrac{d}{dt}` [standard reconstruction]

- `lecture_02_figure_03.png`: `E=` [visible]
- `lecture_02_figure_03.png`: `\sum \dfrac{m\dot X_i^2}{2}` [visible]
- `lecture_02_figure_03.png`: `k\,\dfrac{(\Delta X_i)^2}{2}` [partially visible]
- `lecture_02_figure_03.png`: `N\ \text{mass points}` [visible]
- `lecture_02_figure_03.png`: `E=\sum_i\left(\dfrac{m\dot X_i^2}{2}+\dfrac{k}{2}(\Delta X_i)^2\right)` [standard reconstruction]

- `lecture_02_figure_04.png`: `\dfrac{1}{2\pi}` [visible]
- `lecture_02_figure_04.png`: `\int_0^\pi` [visible]
- `lecture_02_figure_04.png`: `\left(\dfrac{\partial X}{\partial \tau}\right)^2` [visible]
- `lecture_02_figure_04.png`: `\left(\dfrac{\partial X}{\partial \sigma}\right)^2` [partially visible]
- `lecture_02_figure_04.png`: `L=\dfrac{1}{2\pi}\int_0^\pi d\sigma\left[\left(\dfrac{\partial X}{\partial \tau}\right)^2-\left(\dfrac{\partial X}{\partial \sigma}\right)^2\right]` [standard reconstruction]

- `lecture_02_figure_05.png`: `\mu=\dfrac{1}{N}` [partially visible]
- `lecture_02_figure_05.png`: `k=\dfrac{N}{\pi^2}` [partially visible]
- `lecture_02_figure_05.png`: `\dfrac{\partial X}{\partial \sigma}` [visible]
- `lecture_02_figure_05.png`: `\Delta X=\dfrac{\partial X}{\partial \sigma}\,\Delta\sigma` [standard reconstruction]

- `lecture_02_figure_06.png`: `\dfrac{\partial X}{\partial \sigma}=` [visible]
- `lecture_02_figure_06.png`: `-\sum_{n=0}^{\infty} nX_n\sin n\sigma` [partially visible]
- `lecture_02_figure_06.png`: lower quadratic mode sum involving `X_0` and `\sum_n \frac14 X_n^2` [partially visible]

## Diagram And Layout Reading
- `lecture_02_figure_01.png` is not a lecture board at all. It is an intro/title visual and should not inform the mathematics or chapter layout.
- `lecture_02_figure_02.png` has a pedagogically important split layout: the older boosted-energy derivation remains on the right, while a new line beginning `H=` is being introduced below it. The vertical divider visually marks the shift from kinematics to Hamiltonian interpretation.
- `lecture_02_figure_03.png` combines diagram and formula on one board: a lumpy chain of small circles at upper left represents the discretized string, while the equation below gives the corresponding discrete mechanical energy. This pairing is worth preserving because it shows Susskind moving directly from picture to formula.
- `lecture_02_figure_04.png` is a derivational board rather than a finished display equation. The left side still contains remnants of the discrete sum, while the right side presents the continuum integral. The lecturer’s hand is writing the minus-sign potential term, so the frame captures the moment kinetic-minus-potential is being formed.
- `lecture_02_figure_05.png` is a close-up of a local endpoint-force argument. The layout is not a full equation but a replacement rule: discrete difference on one side, continuum derivative with a small-spacing factor on the other. The cropped normalization notes at the top are part of the same continuum-limit bookkeeping.
- `lecture_02_figure_06.png` has a two-tier structure. The top line is the main object: the sigma-derivative written as a Fourier sine expansion. The lower line is a separate, fainter quadratic mode expression left over from the previous step, useful as context but not the main figure content.

## TeX Reconstruction Plan
- `lecture_02_figure_01.png` should not be kept in the mathematical chapter. It is only an opening title/campus visual and contributes nothing to equation or board reconstruction.
- `lecture_02_figure_02.png` should remain visible as a screenshot. Pair it with a clean displayed equation for the boosted-energy correction and a short displayed Hamiltonian identification nearby. Do not redraw it in TikZ.
- `lecture_02_figure_03.png` must remain visible. Reconstruct the discrete string energy as a clean displayed equation, and redraw the bead-chain/open-string sketch in TikZ nearby so the diagram becomes legible while the screenshot preserves the original board evidence.
- `lecture_02_figure_04.png` should remain visible. Pair it with a cleaned continuum Lagrangian in displayed math, explicitly showing the `1/2\pi` prefactor, the `\tau`-derivative kinetic term, and the minus `\sigma`-derivative potential term. No TikZ is needed.
- `lecture_02_figure_05.png` should remain visible as a screenshot-only evidence frame for the discrete-to-continuum replacement. Pair it with a short displayed equation such as `\Delta X=(\partial X/\partial \sigma)\Delta\sigma`; no TikZ is necessary.
- `lecture_02_figure_06.png` should remain visible. Pair it with a cleaned displayed mode expansion for `\partial_\sigma X`; if the surrounding text later needs the quadratic mode expression, typeset that separately from transcript-backed reconstruction rather than relying on the faint lower line in the screenshot.

## Caption Drafts
- `lecture_02_figure_01.png`: Stanford opening title sequence
- `lecture_02_figure_02.png`: Hamiltonian form of the boosted energy
- `lecture_02_figure_03.png`: Discrete string as mass points and springs
- `lecture_02_figure_04.png`: Continuum string Lagrangian
- `lecture_02_figure_05.png`: Discrete difference becomes derivative times spacing
- `lecture_02_figure_06.png`: Mode expansion of the sigma derivative

## Uncertainties
- `lecture_02_figure_01.png` has no mathematical uncertainty because it should simply be omitted from the note-writing figure set.
- In `lecture_02_figure_02.png`, the left-hand factorization or prior algebra is cropped, and the full mass term on the right is not fully visible. The `H=` identification is clear, but the `i\,d/dt` part is not actually written out in the frame.
- In `lecture_02_figure_03.png`, the board writes a plain handwritten `m` for the bead mass; later prose should distinguish this from the relativistic string mass, likely by renaming it `\mu` in the cleaned derivation. The exact placement of the `i` subscript on `\Delta X_i` is not perfectly stable.
- In `lecture_02_figure_04.png`, the leftmost symbol preceding the integral is partly obscured by the lecturer, so whether the board explicitly shows `L=` there is not completely secured by the image alone. The measure `d\sigma` is also not fully clean in the frame.
- In `lecture_02_figure_05.png`, the leading handwritten `N` near `\partial X/\partial \sigma` is ambiguous in role, and the top-board spring-constant normalization is cropped on the right. The frame shows the beginning of the replacement rule, but the full equality should be stabilized from the transcript.
- In `lecture_02_figure_06.png`, the upper summation appears to start at `n=0`, even though the `n=0` term vanishes after differentiation; the cleaned notes may wish to start at `n=1` with a brief remark if needed. The lower quadratic expression is too faint and partial to use without transcript-backed completion.