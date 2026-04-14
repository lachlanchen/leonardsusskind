# Visual Evidence
## Frame Inventory
- `lecture_03_figure_02.png`: This frame shows a large Euler–Lagrange time-derivative term on the left board and a cropped qualitative trajectory sketch on the right board, and the screenshot should remain in the final notes.
- `lecture_03_figure_03.png`: This frame isolates the definition of the canonical momentum-like quantity \(\pi_i\) or \(\Pi_i\) as a derivative of the Lagrangian, and the screenshot should remain in the final notes.
- `lecture_03_figure_04.png`: This frame shows the two-coordinate kinetic-energy line across the top and a simple near-Earth coordinate sketch on the left while new writing is still being added on the far right, and the screenshot should remain in the final notes.

## Equation Extraction
- `lecture_03_figure_02.png`: \(\displaystyle \frac{d}{dt}\left(\frac{\partial \mathcal{L}}{\partial \dot q_i}\right)\) [visible]
- `lecture_03_figure_02.png`: \(\displaystyle \frac{d}{dt}\left(\frac{\partial \mathcal{L}}{\partial \dot q_i}\right)=\frac{\partial \mathcal{L}}{\partial q_i}\) [standard completion]
- `lecture_03_figure_03.png`: \(\displaystyle \Pi_i=\frac{\partial \mathcal{L}}{\partial \dot q_i}\) [visible]
- `lecture_03_figure_03.png`: \(\displaystyle \pi_i=\frac{\partial \mathcal{L}}{\partial \dot q_i}\) [standard completion]
- `lecture_03_figure_04.png`: \(\displaystyle \frac12 m\dot x^{\,2}+\frac12 m\dot y^{\,2}\) [partially visible]
- `lecture_03_figure_04.png`: \(\displaystyle T=\frac12 m\dot x^{\,2}+\frac12 m\dot y^{\,2}\) [standard completion]

## Diagram Extraction
- `lecture_03_figure_02.png`: The right board contains a qualitative path sketch with a slanted lower segment and a curved upper line; if used in the notes, it should be shown both as the original screenshot and as a restrained TikZ redraw of a local trajectory or variation picture.
- `lecture_03_figure_02.png`: The main visual value is the board structure itself, with formal algebra on the left and geometric intuition on the right, so the screenshot matters even if the TikZ redraw is minimal.
- `lecture_03_figure_03.png`: There is no independent diagram here; this should be preserved as a screenshot-backed notation witness rather than redrawn as a figure.
- `lecture_03_figure_04.png`: The left side shows a simple setup sketch that reads as a horizontal surface, a vertical direction, and a particle above the surface; this should be shown both as the original screenshot and as a clean TikZ redraw.
- `lecture_03_figure_04.png`: The far-right writing is in progress and should not be redrawn from the frame; only the stable left sketch and top kinetic-energy line should drive the visual reconstruction.

## Reconstruction Guidance
- For `lecture_03_figure_02.png`, keep the screenshot beside a clean displayed Euler–Lagrange term, or the full Euler–Lagrange equation if the surrounding text has already established the right-hand side from the transcript.
- If the trajectory sketch from `lecture_03_figure_02.png` is redrawn in TikZ, keep it qualitative rather than metrically exact; its role is to support the local-versus-global trajectory discussion, not to encode data.
- For `lecture_03_figure_03.png`, regularize the equation in the notes to the standard notation \(\pi_i=\partial \mathcal{L}/\partial \dot q_i\), but keep the screenshot nearby because it records the moment when Susskind names the quantity as canonical momentum.
- For `lecture_03_figure_04.png`, typeset the kinetic-energy formula cleanly and redraw the near-Earth \(x\)-\(y\) setup in TikZ, but derive the potential term \(U=mgy\) from the transcript rather than from the unfinished right edge of the frame.
- In all three cases, use the screenshot as evidence for board layout, emphasis, and notation, and use standard completion only where the transcript clearly stabilizes what the board is trying to say.

## Uncertainties
- In `lecture_03_figure_02.png`, the denominator index is not perfectly crisp, though the lecture context strongly supports \(\dot q_i\).
- In `lecture_03_figure_02.png`, the right-hand sketch is cropped and too loose to support a precise geometric reconstruction.
- In `lecture_03_figure_03.png`, the leading symbol looks visually like uppercase \(\Pi_i\), while the transcript and standard mechanics notation suggest lowercase \(\pi_i\).
- In `lecture_03_figure_04.png`, the frame does not securely show whether the kinetic-energy line begins with an explicit \(T=\).
- In `lecture_03_figure_04.png`, the coordinate labels in the left sketch are faint enough that the transcript is needed to regularize them as horizontal \(x\) and vertical \(y\).
- In `lecture_03_figure_04.png`, the new writing on the far right should be treated as incomplete process, not as a reliable source for an equation.