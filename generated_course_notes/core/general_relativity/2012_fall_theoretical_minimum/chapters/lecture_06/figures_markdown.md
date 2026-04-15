# Figure Notes
## Image Inventory
- `lecture_06_figure_02.png`: Lecturer pointing at the calligraphic Lagrangian symbol on the right board. The board clearly shows a large calligraphic $\mathcal{L}$, an equals sign, a factor of $-m$, and the beginning of a square-root expression whose interior is cropped after the initial handwritten symbol and minus sign. A vertical board seam splits the frame; faint leftover writing from earlier discussion is visible at the far left edge.
- `lecture_06_figure_04.png`: Two-board view with the lecturer standing between them. The right board carries two stacked equations: an angular-momentum relation on top and an energy relation below, both sharing the same square-root denominator. The left board still shows residual generic mechanics notation, including a partial-derivative definition and a separate $-\mathcal{L}$ line.

## Blackboard Equations
- `lecture_06_figure_02.png`: [visible] $\mathcal{L}=-m\sqrt{\;\;}$ as the main line structure, with the square-root contents only beginning to appear.
- `lecture_06_figure_02.png`: [partially visible] $\mathcal{L}=-m\sqrt{\mathcal{F}-\cdots}$ or possibly $\mathcal{L}=-m\sqrt{f-\cdots}$; the first symbol under the root is legible only as a handwritten $f$-like or script-$F$ symbol followed by a minus sign.
- `lecture_06_figure_02.png`: [standard reconstruction] $\mathcal{L}=-m\sqrt{\mathcal{F}(r)-\mathcal{G}(r)\dot r^{\,2}-r^{2}\dot\theta^{\,2}}$.
- `lecture_06_figure_04.png`: [partially visible] $p_q=\dfrac{\partial\mathcal{L}}{\partial\dot q}$; the derivative expression is visible on the left board, while the leftmost $p_q$ is cropped or nearly cropped out.
- `lecture_06_figure_04.png`: [visible] $-\mathcal{L}$ on the left board as a leftover reminder term from the Hamiltonian construction.
- `lecture_06_figure_04.png`: [visible] $\dfrac{L}{m}=\dfrac{r^{2}\dot\theta}{\sqrt{\mathcal{F}-r^{2}\dot\theta^{\,2}}}=\Lambda$.
- `lecture_06_figure_04.png`: [partially visible] $E=\dfrac{\mathcal{F}(r)\,m}{\sqrt{\mathcal{F}-r^{2}\dot\theta^{\,2}}}$; the numerator and denominator are readable, though the handwritten $\mathcal{F}$ is not perfectly crisp.
- `lecture_06_figure_04.png`: [standard reconstruction] $E=\dfrac{\mathcal{F}(r)\,m}{\sqrt{\mathcal{F}(r)-r^{2}\dot\theta^{\,2}}}$.

## Diagram And Layout Reading
- There is no geometric sketch or axis diagram in either selected frame; both are equation-centered board shots.
- `lecture_06_figure_02.png` is primarily a transition frame: the lecturer is physically indicating the Lagrangian symbol, and the right board is being used to specialize the general mechanics discussion to the Schwarzschild orbit problem.
- `lecture_06_figure_02.png` preserves the board hierarchy more than the full formula: symbol first, then equality, then the square-root form of the relativistic particle Lagrangian.
- `lecture_06_figure_04.png` has a useful two-level layout on the right board: the angular-momentum equation sits above the energy equation, visually signaling that the first is to be solved and substituted into the second.
- In `lecture_06_figure_04.png`, the left board still carries generic mechanics scaffolding, while the right board carries the Schwarzschild-specific circular-orbit formulas. That separation is worth preserving in the prose explanation even if the typeset equations are cleaned up.

## TeX Reconstruction Plan
- `lecture_06_figure_02.png` should remain visible as a documentary screenshot, because it captures the moment where Susskind identifies the Lagrangian line he is about to differentiate. The mathematics next to it should be reconstructed as a clean displayed equation, since the square-root contents are too cropped to rely on the screenshot alone.
- For `lecture_06_figure_02.png`, reconstruct the full Lagrangian in display math, preferably with the same symbol choices used in the surrounding notes: $\mathcal{L}=-m\sqrt{\mathcal{F}(r)-\mathcal{G}(r)\dot r^{\,2}-r^{2}\dot\theta^{\,2}}$.
- `lecture_06_figure_04.png` should also remain visible, because it usefully preserves the stacked board layout of conserved angular momentum above conserved energy.
- For `lecture_06_figure_04.png`, reconstruct the two right-board formulas as a paired aligned display rather than prose math. That is the main mathematical payload of the figure.
- The left-board reminder $p_q=\partial\mathcal{L}/\partial\dot q$ need not be a separate figure equation unless the surrounding notes explicitly pause to restate the generic conjugate-momentum definition. If included, it should appear as a short reminder line before the Schwarzschild-specific formulas.
- No TikZ reconstruction is needed for this pair of images. These are screenshot-plus-equation figures, not diagram figures.

## Caption Drafts
- `lecture_06_figure_02.png`: Relativistic particle Lagrangian in square-root form.
- `lecture_06_figure_04.png`: Angular momentum and energy for circular Schwarzschild motion.

## Uncertainties
- In `lecture_06_figure_02.png`, the interior of the square root is cropped too aggressively to read the full sequence of terms directly from the image.
- In `lecture_06_figure_02.png`, the handwritten symbol under the root may be ordinary $f$ or script $\mathcal{F}$; the transcript strongly suggests script $\mathcal{F}$.
- In `lecture_06_figure_04.png`, the left edge of the generic momentum definition is cropped, so the full $p_q$ label is inferred rather than fully seen.
- In `lecture_06_figure_04.png`, the common denominator is readable in structure, but the first handwritten symbol again looks ambiguous between $f$ and script $\mathcal{F}$.
- The top equation in `lecture_06_figure_04.png` appears to end with $\Lambda$, but if symbol fidelity matters, the exact handwritten Greek form should be checked against adjacent frames.