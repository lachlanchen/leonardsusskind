# Visual Evidence
## Frame Inventory
- `lecture_06_figure_02.png`: Susskind is pointing at the calligraphic Lagrangian on the right board, where `\mathcal{L}=-m\sqrt{\cdots}` is visible but the square-root contents are cropped; the screenshot should remain in the final notes as documentary evidence for the Lagrangian setup.
- `lecture_06_figure_04.png`: Two-board shot with the circular-orbit angular-momentum equation above the energy equation on the right board and generic Lagrangian-mechanics reminders on the left; the screenshot should remain in the final notes because the stacked board layout is part of the derivational logic.

## Equation Extraction
- `lecture_06_figure_02.png`: [visible] `\mathcal{L}=-m\sqrt{\phantom{\cdots}}`
- `lecture_06_figure_02.png`: [partially visible] `\mathcal{L}=-m\sqrt{\mathcal{F}-\cdots}` or possibly `\mathcal{L}=-m\sqrt{f-\cdots}`
- `lecture_06_figure_02.png`: [standard completion] `\mathcal{L}=-m\sqrt{\mathcal{F}(r)-\mathcal{G}(r)\dot r^{\,2}-r^{2}\dot\theta^{\,2}}`

- `lecture_06_figure_04.png`: [partially visible] `p_q=\dfrac{\partial \mathcal{L}}{\partial \dot q}` with the left-hand side cropped or nearly cropped
- `lecture_06_figure_04.png`: [visible] `-\mathcal{L}`
- `lecture_06_figure_04.png`: [visible] `\dfrac{L}{m}=\dfrac{r^{2}\dot\theta}{\sqrt{\mathcal{F}-r^{2}\dot\theta^{\,2}}}=\Lambda`
- `lecture_06_figure_04.png`: [standard completion] `\dfrac{L}{m}=\dfrac{r^{2}\dot\theta}{\sqrt{\mathcal{F}(r)-r^{2}\dot\theta^{\,2}}}=\lambda`
- `lecture_06_figure_04.png`: [partially visible] `E=\dfrac{\mathcal{F}(r)\,m}{\sqrt{\mathcal{F}-r^{2}\dot\theta^{\,2}}}`
- `lecture_06_figure_04.png`: [standard completion] `E=\dfrac{\mathcal{F}(r)\,m}{\sqrt{\mathcal{F}(r)-r^{2}\dot\theta^{\,2}}}`

## Diagram Extraction
- There is no standalone geometric sketch, axis figure, orbit drawing, or causal diagram visible in these two frames; both are equation-centered blackboard shots.
- `lecture_06_figure_02.png` should be preserved as a screenshot rather than redrawn in TikZ, because its main value is the board moment: Susskind indicating the Lagrangian line he is about to differentiate.
- `lecture_06_figure_04.png` should also be preserved as a screenshot rather than redrawn in TikZ, because its main value is the board structure: generic mechanics residue on the left, Schwarzschild-specific circular-orbit formulas on the right, with angular momentum visibly stacked above energy.
- For the final notes, the mathematics from both frames should also be reproduced as clean display equations near the screenshots, but not as TikZ figures.

## Reconstruction Guidance
- Use `lecture_06_figure_02.png` as visual evidence for the existence and form of the square-root Lagrangian, but reconstruct the full interior of the root from the transcript rather than from the cropped image.
- Typeset the Lagrangian cleanly in lecture notation as `\mathcal{L}=-m\sqrt{\mathcal{F}(r)-\mathcal{G}(r)\dot r^{\,2}-r^{2}\dot\theta^{\,2}}`, since that is the cautious completion supported by the spoken derivation.
- Use `lecture_06_figure_04.png` to preserve the order of operations on the board: first the reduced angular-momentum relation, then the energy relation with the same denominator.
- In the notes, present the right-board content as an aligned display rather than inline prose, because the frame shows that Susskind is organizing the derivation vertically.
- The left-board reminder `p_q=\partial\mathcal{L}/\partial\dot q` should be included only if the surrounding prose explicitly recalls the conjugate-momentum definition at that point; otherwise it can remain implicit.
- Do not infer any missing geometric orbit sketch from these frames alone. If the chapter later includes a photon-sphere or orbit diagram, that should come from other visual evidence or directly from the transcript, not from these two images.
- Keep both screenshots near the reconstructed equations in the final chapter whenever possible: the screenshots show the lecture’s board rhythm, while the typeset equations provide the legible mathematical payload.

## Uncertainties
- In `lecture_06_figure_02.png`, the square-root contents are too cropped to read term-by-term from the image itself.
- In `lecture_06_figure_02.png`, the first symbol under the root is ambiguous between ordinary `f` and script `\mathcal{F}`; the transcript favors `\mathcal{F}`.
- In `lecture_06_figure_04.png`, the left edge of the conjugate-momentum reminder is cropped, so `p_q=` is inferred rather than fully secured by the frame.
- In `lecture_06_figure_04.png`, the common denominator is readable in structure, but the first symbol inside it is again visually ambiguous between `f` and `\mathcal{F}`.
- In `lecture_06_figure_04.png`, the final reduced-angular-momentum symbol looks like a handwritten capital-Lambda or lambda-like symbol; the transcript calls the reduced quantity “lambda,” so the exact typeset choice should be normalized by the chapter’s notation.