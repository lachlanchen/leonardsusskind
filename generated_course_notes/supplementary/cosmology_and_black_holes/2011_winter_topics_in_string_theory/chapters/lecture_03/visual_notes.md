# Visual Evidence
## Frame Inventory
- `lecture_03_figure_01.png`: Stanford title card over a campus shot; it should not remain in the final notes because it carries no mathematical or diagrammatic evidence.
- `lecture_03_figure_02.png`: Susskind at the board with a clearly visible top line element and the start of a second line; it should remain as a small supporting screenshot for the convention shift and the start of the Schwarzschild rewrite.
- `lecture_03_figure_03.png`: Side view of Susskind against an essentially blank board segment; it should not remain in the final notes.
- `lecture_03_figure_04.png`: Partial lower-board algebra with a visible \(\rho^2\) numerator over a denominator involving \(16M^2G^2\); it may remain as secondary screenshot evidence, but only if layout permits.
- `lecture_03_figure_05.png`: Strong board frame combining left-side coordinate equations with a central-right spacetime sketch; it should remain in the final notes and should anchor the TikZ redraw.

## Equation Extraction
- `lecture_03_figure_02.png` [visible]
  \[
  ds^2 = dt^2 - dx^2
  \]
- `lecture_03_figure_02.png` [partially visible]
  \[
  ds^2 =
  \]
- `lecture_03_figure_02.png` [standard completion]
  \[
  ds^2 = -\left(1-\frac{2MG}{r}\right)dt^2 + \frac{dr^2}{1-\frac{2MG}{r}} + \cdots
  \]
  This is the clean note-quality Schwarzschild line element in Susskind’s sign-flipped \(ds^2\) convention, with the angular sector suppressed as in the lecture.
- `lecture_03_figure_03.png` [visible]
  No usable equation is visible.
- `lecture_03_figure_04.png` [partially visible]
  \[
  \frac{\rho^2}{16M^2G^2}
  \]
- `lecture_03_figure_04.png` [standard completion]
  \[
  ds^2 = -\frac{\rho^2\,dt^2}{16M^2G^2} + d\rho^2
  \]
- `lecture_03_figure_05.png` [partially visible]
  \[
  \frac{t}{4MG} = \omega
  \]
- `lecture_03_figure_05.png` [partially visible]
  \[
  \frac{dt^2}{16M^2G^2} = d\omega^2
  \]
- `lecture_03_figure_05.png` [partially visible]
  \[
  r-2MG
  \]
  only as a cropped lower-right fragment.
- `lecture_03_figure_05.png` [standard completion]
  \[
  ds^2 = -\rho^2\,d\omega^2 + d\rho^2
  \]

## Diagram Extraction
- `lecture_03_figure_05.png` contains the only diagram that clearly deserves a TikZ redraw. The visible structure is a pair of crossing diagonal null lines, a marked point near the crossing, a newly drawn right-side curve or boundary, and hatched shading in the upper-right region.
- `lecture_03_figure_05.png` should be shown both ways: the original screenshot as evidence, and a clean TikZ redraw beside it for note readability.
- The TikZ redraw should preserve the lecture’s board logic rather than beautify it into a different construction: null boundaries, the special point corresponding to \(\rho=0\), and the added right-hand constant-\(r\) feature are the essential visual elements.
- `lecture_03_figure_02.png` does not need a separate redraw; its value is the board layout moment of a top reference line and a new line being started underneath.
- `lecture_03_figure_04.png` has no standalone diagram value; it is only equation-fragment evidence.
- `lecture_03_figure_01.png` and `lecture_03_figure_03.png` should not be used for diagrams or screenshots in the mathematical notes.

## Reconstruction Guidance
- Use `lecture_03_figure_02.png` as visual evidence for the sign-convention transition, but do not let the visible top line alone determine the final displayed equations. The polished notes should typeset the corrected Schwarzschild metric from the transcript, with the screenshot nearby as a process snapshot.
- Use `lecture_03_figure_04.png` only to support the intermediate near-horizon coefficient \(\rho^2/(16M^2G^2)\). The full equation should be typeset cleanly from cautious standard reconstruction rather than extracted literally from the cropped frame.
- Use `lecture_03_figure_05.png` as the main visual anchor for the near-horizon causal sketch. Keep the screenshot visible and place a TikZ redraw nearby, together with the coordinate rescaling equations \(\omega=t/(4MG)\), \(d\omega^2=dt^2/(16M^2G^2)\), and the resulting metric \(ds^2=-\rho^2 d\omega^2 + d\rho^2\).
- The near-horizon \(\rho\)-substitution should not be forced out of the frames, because it is not fully legible there. Typeset it from the transcript in clean form:
  \[
  \rho = \sqrt{8MG}\,\sqrt{r-2MG},
  \qquad
  \rho^2 = 8MG(r-2MG).
  \]
- Standardize notation to \(M\) and \(G\) in the notes even though the lecture transcript often reads as lowercase \(m\) and \(g\). The notes should mention this once and then stay consistent.
- Do not preserve `lecture_03_figure_01.png` or `lecture_03_figure_03.png` in the final chapter, because they add no mathematical evidence.

## Uncertainties
- `lecture_03_figure_02.png` captures a transitional board state, and the lower line is too incomplete to read directly as the final Schwarzschild metric.
- `lecture_03_figure_02.png` may also reflect a sign-correction moment rather than a final settled flat-space formula, so the transcript should control the polished equation.
- `lecture_03_figure_04.png` does not directly secure the full sign structure, the nearby \(dt^2\), or the full left-hand side of the equation.
- `lecture_03_figure_05.png` does not make the label of the newly drawn right-hand curve fully legible.
- `lecture_03_figure_05.png` only shows a fragment of the lower-right label, so \(r-2MG\) should be treated as partial evidence, not a complete board transcription.
- `lecture_03_figure_05.png` supports a near-horizon Minkowski/Rindler-style sketch, but by itself it does not justify a more elaborate Kruskal interpretation.
- `lecture_03_figure_01.png` and `lecture_03_figure_03.png` contain no reliable mathematical information and should not influence reconstruction decisions.