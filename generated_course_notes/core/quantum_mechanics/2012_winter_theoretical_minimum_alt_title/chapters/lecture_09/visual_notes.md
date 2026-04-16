# Visual Evidence

## Frame Inventory
- `lecture_09_figure_02.png`: Upper-board delta-function sampling identity above the beginning of the substituted Fourier expression for `\psi(x')`; this screenshot should remain in the final notes because it documents the moment where the Fourier pair and delta rules are being combined.
- `lecture_09_figure_03.png`: Close crop of the key boxed inner momentum integral inside the outer `x`-integral, followed by its rewrite in terms of a delta-like kernel; this screenshot should definitely remain because it is the clearest visual evidence for the kernel-to-delta step.
- `lecture_09_figure_04.png`: Minimal two-line board comparing operator action on a ket with operator action on a wavefunction; this screenshot should remain because the board layout itself carries the pedagogical point.
- `lecture_09_figure_05.png`: Split-board transition from position-basis formulas on the left to the momentum-operator definition on the right; this screenshot should remain, though as a secondary figure, because it preserves the lecture’s pivot from `X` to `P`.
- `lecture_09_figure_06.png`: Momentum-space delta-normalization identity on the upper line with the momentum-space inner product beginning below it; this screenshot should remain because it shows the identity and the start of the next formula in their original board order.

## Equation Extraction
- `lecture_09_figure_02.png`: [partially visible] `\int dx\,F(x)\,\delta(x-x') = F(x')`
- `lecture_09_figure_02.png`: [partially visible] `\psi(x')=\int \frac{dp}{\sqrt{2\pi}}\,e^{ipx'}[\cdots]`
- `lecture_09_figure_02.png`: [standard completion] `\psi(x')=\int \frac{dp}{\sqrt{2\pi}}\,e^{ipx'}\left[\int \frac{dx}{\sqrt{2\pi}}\,\psi(x)\,e^{-ipx}\right]`

- `lecture_09_figure_03.png`: [visible] `\psi(x')=\int dx\left[\int \frac{dp}{2\pi}\,e^{ip(x'-x)}\right]\psi(x)`
- `lecture_09_figure_03.png`: [visible] `\int dx\,\Delta(x'-x)\,\psi(x)`
- `lecture_09_figure_03.png`: [standard completion] `\int dx\,\delta(x'-x)\,\psi(x)=\psi(x')`
- `lecture_09_figure_03.png`: [standard completion] `\int \frac{dp}{2\pi}\,e^{ip(x'-x)}=\delta(x'-x)`

- `lecture_09_figure_04.png`: [partially visible] `X\,|\psi\rangle`
- `lecture_09_figure_04.png`: [visible] `X\,\psi(x)`
- `lecture_09_figure_04.png`: [standard completion] `(X\psi)(x)=x\,\psi(x)`

- `lecture_09_figure_05.png`: [partially visible] `\langle x'|x\rangle=\delta(x-x')`
- `lecture_09_figure_05.png`: [partially visible] `P=-i\hbar D`
- `lecture_09_figure_05.png`: [partially visible] `P\,\psi(x)=-i\hbar\,\cdots`
- `lecture_09_figure_05.png`: [standard completion] `(P\psi)(x)=-i\hbar\,\dfrac{d\psi}{dx}`

- `lecture_09_figure_06.png`: [visible] `\int \frac{dx}{2\pi}\,e^{i(p-p')x}=\delta(p-p')`
- `lecture_09_figure_06.png`: [partially visible] `\langle \Psi|\Phi\rangle=\int \cdots`
- `lecture_09_figure_06.png`: [standard completion] `\langle \Psi|\Phi\rangle=\int dp\,\widetilde{\psi}^{\,*}(p)\,\widetilde{\phi}(p)`

## Diagram Extraction
- There are no genuine geometric diagrams, axes, particle sketches, or state-transition cartoons in this frame set; the useful visual content is blackboard structure rather than pictorial drawing.
- `lecture_09_figure_02.png` should be preserved as a screenshot, not redrawn in TikZ, because the important evidence is the stacked board arrangement: delta identity above, substituted Fourier expression below.
- `lecture_09_figure_03.png` should be preserved as a screenshot and also echoed typographically in the notes by using a displayed equation with a boxed inner kernel, for example via `\boxed{...}` rather than TikZ.
- `lecture_09_figure_04.png` should be preserved as a screenshot because its value is the two-line comparison between abstract state notation and wavefunction notation; no TikZ redraw is needed.
- `lecture_09_figure_05.png` should be preserved as a screenshot because the split-board layout shows the conceptual transition from position-space formulas to the momentum operator; no TikZ redraw is needed.
- `lecture_09_figure_06.png` should be preserved as a screenshot because the upper identity and lower emerging inner-product formula belong together in the original board sequence; no TikZ redraw is needed.

## Reconstruction Guidance
- Use the screenshots as documentary evidence, but typeset the full mathematics cleanly beside them. In particular, `lecture_09_figure_02.png` and `lecture_09_figure_03.png` should support a fully reconstructed nested-integral derivation that ends with the Fourier representation of the delta function.
- For `lecture_09_figure_03.png`, keep the screenshot nearby even after typesetting the cleaned equation, because the boxed inner `p`-integral is the best visual cue that Susskind is isolating a kernel and only then naming it as a delta function.
- For `lecture_09_figure_04.png`, the note-quality equation should be the clean operator statement `(X\psi)(x)=x\psi(x)`, while the screenshot preserves the board’s abstract-to-representation contrast.
- For `lecture_09_figure_05.png`, reconstruct the momentum operator as `P=-i\hbar\,d/dx` and `(P\psi)(x)=-i\hbar\,d\psi/dx`, but keep the screenshot because it shows that this definition is being introduced immediately after the position-basis discussion rather than in isolation.
- For `lecture_09_figure_06.png`, typeset the complete momentum-space inner product and keep the screenshot as evidence for the normalization identity above it; the lower line in the image is only the start of the formula, not the whole thing.
- Where visible notation is provisional or rough, separate the final cleaned equation from the board artifact. The notes should say the mathematics cleanly, while the screenshot preserves how the argument unfolded on the board.

## Uncertainties
- In `lecture_09_figure_02.png`, the delta symbol in the top line is handwritten roughly and could be misread at first glance, but it is most plausibly the ordinary Dirac delta.
- In `lecture_09_figure_02.png`, the left-hand argument of `\psi` appears to be `x'`, but the prime is not perfectly sharp in the frame; the transcript supports `\psi(x')`.
- In `lecture_09_figure_02.png`, the right half of the bracketed substitution is cropped, so the full nested integral is not directly visible.
- In `lecture_09_figure_03.png`, the lower line uses a provisional capital-delta-like symbol before the argument is identified with the standard Dirac delta; that intermediate label should not be overinterpreted.
- In `lecture_09_figure_03.png`, the sign order in the exponent is visible as `x'-x`, but nearby lecture discussion makes clear that `x-x'` versus `x'-x` is not ultimately significant for the delta function.
- In `lecture_09_figure_04.png`, the exact ket label on the top line is not fully secure from the image alone; the important point is that the upper line is abstract ket notation and the lower line is wavefunction notation.
- In `lecture_09_figure_05.png`, the second momentum-operator line is cut off on the right, so the derivative term must be completed from transcript context rather than from the image alone.
- In `lecture_09_figure_05.png`, the subtitle window refers to momentum eigenvectors, but the frame itself mainly captures the operator definition rather than the finished eigenfunction equation.
- In `lecture_09_figure_06.png`, only the beginning of the momentum-space inner product is visible; the integrand and measure are not yet fully written in the frame.