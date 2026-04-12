# Visual Evidence
## Frame Inventory
- `lecture_02_figure_02.png`: Whiteboard frame with an upper flat-space spherical line element, a lower Schwarzschild-metric line centered on the factor \(1-\frac{2MG}{c^2 r}\), a small shorthand \(1-\frac{R_s}{r}\) at lower left, and an unlabeled concentric-circle radial sketch at far right; this screenshot should remain visible in the final notes.

## Equation Extraction
- `lecture_02_figure_02.png` [visible]:
  \[
  d\tau^2 = dt^2 - \left(dr^2 + r^2 d\Omega^2\right)
  \]
- `lecture_02_figure_02.png` [partially visible]:
  \[
  \left(1-\frac{2MG}{c^2 r}\right)
  \]
  appearing as the Schwarzschild factor on the lower line.
- `lecture_02_figure_02.png` [partially visible]:
  \[
  \left(1-\frac{2MG}{c^2 r}\right)dt^2
  \]
  as the time part of the lower metric.
- `lecture_02_figure_02.png` [partially visible]:
  \[
  \frac{dr^2}{\left(1-\frac{2MG}{c^2 r}\right)}
  \]
  as the radial part of the lower metric.
- `lecture_02_figure_02.png` [visible]:
  \[
  r^2 d\Omega^2
  \]
  as the angular term written on both the upper and lower lines.
- `lecture_02_figure_02.png` [visible]:
  \[
  1-\frac{R_s}{r}
  \]
  written separately below the main equations as shorthand for the same factor.
- `lecture_02_figure_02.png` [standard completion]:
  \[
  d\tau^2
  =
  \left(1-\frac{2Gm}{c^2 r}\right)dt^2
  -
  \frac{dr^2}{1-\frac{2Gm}{c^2 r}}
  -
  r^2 d\Omega^2
  \]
  This is the clean note-quality reconstruction that matches the upper flat-space line in the \(r\to\infty\) limit; the frame itself does not securely fix every sign.

## Diagram Extraction
- The board has a clear three-part layout that should be preserved conceptually: upper reference metric, lower Schwarzschild modification, and a separate sketch at far right.
- The far-right drawing is a small schematic of spherical symmetry: a compact central region shown by concentric circles, with a few radial lines or spokes extending outward. It should be shown both ways: keep the screenshot and add a simple TikZ redraw nearby.
- The screenshot itself matters because it shows how Susskind visually presented the Schwarzschild metric as a modification of the flat spherical line element, not as an isolated textbook formula.
- No labeled spacetime diagram is visible in this frame; the right-hand sketch should not be turned into a Penrose diagram or a null-ray diagram.

## Reconstruction Guidance
- Keep `lecture_02_figure_02.png` in the chapter as visual evidence at the point where Susskind introduces the Schwarzschild metric.
- Typeset the upper line element essentially as seen:
  \[
  d\tau^2 = dt^2 - \left(dr^2 + r^2 d\Omega^2\right).
  \]
- Typeset the lower Schwarzschild metric as a cautious standard reconstruction, using the transcript and the required flat-space limit to settle the cleaned sign convention. The screenshot supports the factor structure and board organization more strongly than it supports every sign.
- Preserve the visible shorthand \(1-\frac{R_s}{r}\) in nearby prose or as a short displayed relation, with the transcript supplying the interpretation \(R_s=\frac{2Gm}{c^2}\).
- Redraw the right-hand sketch as a minimal TikZ schematic: a central circular object or horizon, one or two concentric circles, and a few radial guide lines. Keep it deliberately schematic and unlabeled unless a later transcript segment supplies labels.
- If the final notes also define
  \[
  d\Omega^2 = d\theta^2 + \sin^2\theta\, d\phi^2,
  \]
  that definition should be sourced from the transcript’s earlier discussion, not from this frame alone.

## Uncertainties
- The left edge of the lower metric is partially occluded, so the full leading sign structure is not directly secure from the image.
- The lower-line sign convention is not fully reliable from the frame alone. In particular, the visible angular-term sign is hard to trust literally, because the cleaned Schwarzschild metric should reduce to the upper flat-space expression for large \(r\).
- The top metric symbol looks like \(d\tau^2\), but \(ds^2\) cannot be ruled out from handwriting alone.
- The handwritten mass symbol looks like uppercase \(M\) in the frame, while the transcript uses \(m\); this should be normalized consistently in the final notes.
- The right-hand sketch has no labels, axes, or arrows, so it should only be treated as evidence for a radial, spherically symmetric black-hole schematic.