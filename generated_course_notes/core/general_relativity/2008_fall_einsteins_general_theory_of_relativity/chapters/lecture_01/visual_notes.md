# Visual Evidence
## Frame Inventory
- `lecture_01_figure_01.png` shows the Stanford title card with logo and website only; it should not remain in the final notes.
- `lecture_01_figure_02.png` shows Susskind beside a mostly blank board with the handwritten equation `F = ma`; it may remain only as a small documentary screenshot if the chapter wants a visual opening for Newton’s setup.
- `lecture_01_figure_03.png` shows a point-source sketch labeled `M` together with the scalar inverse-square law; it should remain in the final notes as evidence for the transition from force magnitude to vector form.
- `lecture_01_figure_04.png` shows a partly erased many-body force board with a left-side vector sketch and a right-side summation formula; it is weak as a main figure and should remain only if no cleaner witness exists.
- `lecture_01_figure_05.png` shows the divergence formula and its component expansion clearly across the board; it should remain in the final notes.
- `lecture_01_figure_06.png` shows the arrow-field sketch used to explain local divergence intuitively; it should remain in the final notes and be paired with a redraw.

## Equation Extraction
- `lecture_01_figure_02.png`: \(F=ma\) [visible]
- `lecture_01_figure_02.png`: \(\vec F = m\vec a\) [standard completion]
- `lecture_01_figure_03.png`: \(F=\frac{mMG}{R^2}\) [visible]
- `lecture_01_figure_03.png`: \(M\) [visible]
- `lecture_01_figure_03.png`: \(\vec F=-\frac{GmM}{r^3}\,\vec r\) [standard completion]
- `lecture_01_figure_04.png`: \(\vec F_i=\sum_{j\ne i}\cdots\) [partially visible]
- `lecture_01_figure_04.png`: \(R_{ij}^3\) in the denominator [partially visible]
- `lecture_01_figure_04.png`: \(\vec F_i=\sum_{j\ne i} G\,m_i m_j\,\frac{\vec r_j-\vec r_i}{|\vec r_j-\vec r_i|^3}\) [standard completion]
- `lecture_01_figure_05.png`: \(\vec\nabla\cdot\vec A = \partial_x A_x + \partial_y A_y + \partial_z A_z\) [visible]
- `lecture_01_figure_05.png`: \(\frac{\partial A_x}{\partial x}+\frac{\partial A_y}{\partial y}+\frac{\partial A_z}{\partial z}\) [visible]
- `lecture_01_figure_06.png`: the arrows represent the vector field \(A\) rather than the scalar divergence [standard completion]

## Diagram Extraction
- `lecture_01_figure_02.png` is not really a diagram; its value is the bare board layout at the moment Newton’s law is first introduced, so if it is kept, it should remain only as a screenshot.
- `lecture_01_figure_03.png` contains a source-mass sketch with a central marked point, the label `M`, and a directional arrow; it should be shown both as a screenshot and as a clean TikZ redraw with the radial vector and inward gravitational force made explicit.
- `lecture_01_figure_04.png` contains a many-body layout with one particle receiving contributions from others; if used, it should be shown as a screenshot only as supporting evidence and accompanied by a clean redraw, because the frame itself is mid-erasure.
- `lecture_01_figure_05.png` is algebraic rather than geometric; it should remain as a screenshot, with the clean note-quality version rendered in LaTeX rather than redrawn as TikZ.
- `lecture_01_figure_06.png` is a schematic flow or field picture with arrows of different lengths across the board; it should be shown both as a screenshot and as a TikZ redraw that adds the small circle or control region described in the lecture.
- No useful mathematical diagram is present in `lecture_01_figure_01.png`.

## Reconstruction Guidance
- Exclude `lecture_01_figure_01.png` from the chapter body entirely; it belongs only to source provenance, not the mathematical notes.
- Treat `lecture_01_figure_02.png` as evidence that Susskind starts from the stripped-down Newtonian equation. In the notes, typeset the clean vector version \(\vec F=m\vec a\) and explain that the screenshot catches the moment before the vector arrows are visibly added.
- Use `lecture_01_figure_03.png` to anchor the move from scalar inverse-square force to vector force law. Keep the screenshot nearby, but reconstruct the actual note equation cleanly with a declared radial-vector convention so the sign is unambiguous.
- Do not trust `lecture_01_figure_04.png` as a clean source for final notation. If it is kept at all, use it only to justify board structure, then present a standardized many-body formula with explicit vector differences and a fixed sign convention.
- Use `lecture_01_figure_05.png` as the primary visual witness for divergence notation. Preserve the screenshot, but typeset the divergence formula cleanly in standard LaTeX, since the final notes should not inherit uneven board handwriting.
- Use `lecture_01_figure_06.png` as documentary evidence for the local “in versus out” intuition behind divergence. The final notes should redraw the arrows in TikZ and add the missing circle or small boundary element mentioned in the transcript, because that interpretive feature is not actually visible in the frame.
- Keep the chapter’s notation internally consistent even when the frames are not. In particular, choose one radial symbol system and one many-body vector convention, then note briefly when the board evidence is approximate or transitional rather than definitive.

## Uncertainties
- `lecture_01_figure_02.png` does not visibly show vector arrows over \(F\) and \(a\), even though the lecture at that moment is already talking about a vector equation.
- `lecture_01_figure_03.png` is partly blocked by Susskind’s paper, and the exact intended relation between the drawn arrow and the source point is not fully recoverable from the frame alone.
- `lecture_01_figure_03.png` visibly uses an uppercase \(R\) in the denominator, while the lecture elsewhere often speaks in terms of lowercase \(r\); the final notes should normalize this cautiously.
- `lecture_01_figure_04.png` is interrupted by erasure, so the masses, indices, and sign are not reliably readable from the image alone.
- `lecture_01_figure_04.png` sits exactly in the portion of the lecture where Susskind corrects his sign convention after a student objection, so any final equation taken from this frame alone would be risky.
- `lecture_01_figure_05.png` is clear overall, but the handwriting style mixes compact derivative notation and full fraction notation, and the last denominator is slightly soft even though it is best read as \(z\).
- `lecture_01_figure_06.png` contains small marks at lower left that are not legible enough to use as labels.
- `lecture_01_figure_06.png` does not actually show the small circle between arrows that the transcript describes, so that part must be added as a cautious reconstruction rather than claimed as directly visible.