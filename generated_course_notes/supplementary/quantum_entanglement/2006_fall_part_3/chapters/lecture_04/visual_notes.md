# Visual Evidence
## Frame Inventory
- `lecture_04_figure_01.png`: Stanford title card only, with no board mathematics or diagram content, so this screenshot should not remain in the final notes.
- `lecture_04_figure_02.png`: Early whiteboard setup for the Galilean-relativity picture, showing \(x' = x-vt\), \(t' = t\), and the initial \(t\)-\(x\) axes, and this screenshot should remain in the final notes as board-layout evidence.
- `lecture_04_figure_03.png`: Strong spacetime-diagram frame showing the slanted moving-origin worldline labeled by \(x=vt\), \(x'=0\), and \(t'\), and this screenshot should remain in the final notes as primary visual evidence.
- `lecture_04_figure_04.png`: Later two-board frame with partial algebra on the left and a more developed skewed spacetime sketch on the right, and this screenshot should remain only as a secondary figure if the asymmetry discussion is kept.

## Equation Extraction
- `lecture_04_figure_02.png`: \(x' = x - vt\) [visible]
- `lecture_04_figure_02.png`: \(t' = t\) [visible]
- `lecture_04_figure_02.png`: \(t\) as the vertical-axis label [visible]
- `lecture_04_figure_02.png`: \(x\) as the horizontal-axis label [visible]
- `lecture_04_figure_03.png`: \(x = vt\) [visible]
- `lecture_04_figure_03.png`: \(x' = 0\) [visible]
- `lecture_04_figure_03.png`: \(t'\) [visible]
- `lecture_04_figure_03.png`: \(t\) on the original vertical axis [partially visible]
- `lecture_04_figure_03.png`: \(x = vt \iff x' = 0\) for the slanted worldline of the primed origin [standard completion]
- `lecture_04_figure_04.png`: \(-2xvt\) [partially visible]
- `lecture_04_figure_04.png`: a term of the form \((1-v^2)x^2\), or a closely related \(x^2\)-term, on the left board [partially visible]
- `lecture_04_figure_04.png`: additional left-board algebra is present but too cropped to transcribe reliably [partially visible]

## Diagram Extraction
- `lecture_04_figure_02.png` should be shown both as a screenshot and as a TikZ redraw: the frame preserves the board structure of the Galilean setup, while the redraw can cleanly show the unprimed \(t\)- and \(x\)-axes before the moving-frame construction is completed.
- `lecture_04_figure_03.png` should be shown both as a screenshot and as a TikZ redraw: the screenshot is the clearest evidence that the lecturer identifies the slanted line with both \(x=vt\) and \(x'=0\), and the redraw can make the geometry legible.
- `lecture_04_figure_03.png` is the key frame for preserving the original board logic that the primed construction is being drawn on top of the unprimed axes, not on a separate diagram.
- `lecture_04_figure_04.png` should be used, if at all, as a screenshot-plus-TikZ pair: the right-hand board is useful as qualitative evidence of a later asymmetric spacetime sketch, but the redraw should be explicitly treated as cautious editorial cleanup because the lecturer blocks part of the figure.
- `lecture_04_figure_01.png` should be omitted entirely from the mathematical notes.

## Reconstruction Guidance
- For `lecture_04_figure_02.png`, keep the screenshot nearby and typeset the clean equations
  \(x' = x-vt\) and \(t' = t\)
  as displayed mathematics; the screenshot is evidence for the board order and the axis layout, not for a polished final figure.
- For `lecture_04_figure_03.png`, keep the screenshot nearby and redraw the spacetime diagram with unprimed axes, the slanted worldline through the origin, and the labels \(x=vt\), \(x'=0\), and \(t'\); this is the frame where the board most clearly supports the identification of the moving origin with the primed time axis.
- The clean note version should standardize the geometry using the transcript where needed, especially the idea that the primed origin satisfies \(x'=0\) and appears in the unprimed frame as \(x=vt\).
- For `lecture_04_figure_04.png`, use the screenshot only as evidence that the lecture had a right-board skewed spacetime construction and simultaneous left-board algebra; do not build exact displayed equations from it beyond the few legible fragments.
- If the asymmetry discussion is retained, redraw only the qualitative diagrammatic structure from `lecture_04_figure_04.png` and keep the screenshot beside it so the reader can see which parts are genuinely visible and which parts are cautious completion.
- Full Lorentz-transformation formulas, invariant-interval algebra, or length-contraction derivations should be reconstructed from the transcript and standard formulas, not inferred aggressively from these frames alone.

## Uncertainties
- `lecture_04_figure_02.png` does not yet show a finished \(t'\)-axis clearly enough to treat the frame as the completed Galilean grid.
- In `lecture_04_figure_03.png`, Susskind’s hand comes very close to the upper labels, so the exact spacing and placement of \(x=vt\), \(x'=0\), and \(t'\) should not be overread.
- In `lecture_04_figure_03.png`, the lower horizontal axis is only partly visible, so a clean redraw should normalize the axis lengths rather than copying the crop literally.
- In `lecture_04_figure_04.png`, the left-board algebra is incomplete and partly cut off; the exact sign structure and coefficients beyond fragments like \(-2xvt\) are not reliable from the image alone.
- In `lecture_04_figure_04.png`, the right-board diagram has visible structure but not fully legible labels, so any TikZ version should be presented as a cautious reconstruction rather than a verbatim transcription.
- `lecture_04_figure_01.png` is visually clean but mathematically useless, so it should not be allowed to influence the note structure at all.