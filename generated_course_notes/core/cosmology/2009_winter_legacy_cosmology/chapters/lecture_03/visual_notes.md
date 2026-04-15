# Visual Evidence
## Frame Inventory
- `lecture_03_figure_02.png`: Shows a partially cropped dotted sphere with labeled points \(x=0\) and \(x=1\), a marked distance \(a\), and a Newtonian energy expression beginning \(\frac12\dot a^2\); the screenshot should remain in the final notes.
- `lecture_03_figure_03.png`: Shows Susskind in front of a partially obscured Friedmann-equation board where a boxed \(-k/a^2\) term is clearly emphasized; the screenshot should remain, but only as narrow evidence for the curvature term.
- `lecture_03_figure_05.png`: Shows the newly drawn axes of the energy-density plot before labels or curves are added; the screenshot should remain as board-layout evidence.

## Equation Extraction
- `lecture_03_figure_02.png`: \(\frac{1}{2}\dot a^2\) [visible]
- `lecture_03_figure_02.png`: \(-\frac{4\pi}{3}a^2\rho\) [partially visible]
- `lecture_03_figure_02.png`: \(-\frac{4\pi G}{3}a^2\rho\) [standard completion]
- `lecture_03_figure_02.png`: \(x=0\) [visible]
- `lecture_03_figure_02.png`: \(x=1\) [visible]
- `lecture_03_figure_02.png`: \(a\) [visible]
- `lecture_03_figure_03.png`: \(-k\) [visible]
- `lecture_03_figure_03.png`: \(-\frac{k}{a^2}\) [visible]
- `lecture_03_figure_03.png`: \(\rho-\frac{k}{a^2}\) [partially visible]
- `lecture_03_figure_03.png`: \(\left(\frac{\dot a}{a}\right)^2=\frac{8\pi G}{3}\rho-\frac{k}{a^2}\) [standard completion]
- `lecture_03_figure_05.png`: No algebraic notation is yet written; only axes are visible [visible]

## Diagram Extraction
- `lecture_03_figure_02.png`: The important diagram is the dotted spherical mass distribution centered on the observer at \(x=0\), with a selected boundary point or test galaxy at \(x=1\); this should be shown both ways, as the original screenshot and as a cleaned TikZ redraw.
- `lecture_03_figure_02.png`: The board structure itself matters: left-side sketch, right-side energy equation. The redraw should preserve that layout rather than isolating the picture from the formula.
- `lecture_03_figure_03.png`: This is mainly an emphasis frame, not a standalone diagram. It should be preserved as a screenshot because the box around the curvature term is part of the board rhetoric, but it does not need a separate TikZ figure.
- `lecture_03_figure_05.png`: The axes are the only visible geometry, but they matter because they fix the board orientation for the later comparison of matter and radiation energy densities. This should be shown both ways, as the original screenshot and as a later-completed TikZ plot.

## Reconstruction Guidance
- Turn `lecture_03_figure_02.png` into a clean displayed Newtonian energy-balance equation using the transcript to restore the standard coefficient and Newton constant \(G\), but keep the screenshot nearby because the image is the actual witness for the sphere sketch, the \(x=0\)/\(x=1\) labels, and the board’s left-right organization.
- Redraw the dotted sphere from `lecture_03_figure_02.png` in TikZ as a homogeneous filled region with a marked center and selected comoving point, but avoid inventing extra annotations that are not legible on the board.
- Use `lecture_03_figure_03.png` to justify highlighting the curvature term in the notes, but typeset the full Friedmann equation cleanly rather than pretending the whole formula is fully visible in the frame.
- Do not use `lecture_03_figure_03.png` as evidence for the full Einstein-tensor notation mentioned in the transcript; the image supports the Friedmann-side curvature emphasis much more securely than it supports \(R_{00}\), \(g_{00}\), or \(T_{00}\).
- Use `lecture_03_figure_05.png` as the visual anchor for the start of the energy-density comparison, then reconstruct the completed plot in TikZ from the transcript: horizontal axis \(a\), vertical axis energy density, one curve falling as \(a^{-3}\), the other as \(a^{-4}\), and a crossover point.
- When an equation is only partly visible, prefer a cautious standard completion aligned with the transcript over a literal but incomplete board fragment.

## Uncertainties
- In `lecture_03_figure_02.png`, the negative term is not fully secure from the image alone: the power of \(a\) and the presence of \(G\) are better reconstructed from the transcript than read directly from the chalk.
- In `lecture_03_figure_02.png`, the small extra boundary annotation next to the point labeled \(x=1\) is not reliably legible.
- In `lecture_03_figure_03.png`, the lecturer blocks enough of the board that only the curvature piece \(-k/a^2\) is clearly trustworthy; the left side of the boxed expression is cropped and partly hidden.
- In `lecture_03_figure_03.png`, the subtitle window concerns the time-time Einstein equation, but the frame itself does not visibly secure tensor indices or exact Einstein-side constants.
- In `lecture_03_figure_05.png`, no axis labels or curves are yet visible, so the identification of the horizontal axis as \(a\) and the vertical axis as energy density comes from the transcript, not from the chalk marks alone.