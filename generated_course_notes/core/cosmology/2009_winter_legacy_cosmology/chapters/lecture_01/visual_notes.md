# Visual Evidence
## Frame Inventory
- `lecture_01_figure_02.png`: Shows a left-hand \(x\)-\(t\) spacetime sketch, a central expanding-universe line element, and the beginning of a matrix-style metric notation on the right; this screenshot should remain in the final notes because the board layout itself is informative.
- `lecture_01_figure_03.png`: Shows the closed one-dimensional circle model with labels \(\theta\), \(\theta=0\), a radial segment, and a separate straight segment labeled \(2\pi a\); this screenshot should remain in the final notes because it is the clearest evidence for the lecture’s circle construction.

## Equation Extraction
- `lecture_01_figure_02.png`: \(d\tau^2 = dt^2 - a^2\,dx^2 - a^2\,dy^2 - a^2\,dz^2\) [partially visible]
- `lecture_01_figure_02.png`: \(g_{xx}\) [visible]
- `lecture_01_figure_02.png`: a metric matrix with visible top entry \(1\) and lower entries of the form \(-a^2\) [partially visible]
- `lecture_01_figure_02.png`: \(g_{\mu\nu}=\mathrm{diag}(1,-a^2,-a^2,-a^2)\) [standard completion]
- `lecture_01_figure_02.png`: a small separation marker in the spacetime sketch, plausibly \(a\,dx\) or \(a\,\Delta x\) [partially visible]

- `lecture_01_figure_03.png`: \(2\pi a\) [visible]
- `lecture_01_figure_03.png`: \(\theta=0\) [visible]
- `lecture_01_figure_03.png`: \(\theta\) [visible]
- `lecture_01_figure_03.png`: a label on the radial segment, likely \(r\) [partially visible]
- `lecture_01_figure_03.png`: \(ds^2=a^2\,d\theta^2\) [standard completion]

## Diagram Extraction
- `lecture_01_figure_02.png`: The left side should be redrawn in TikZ as a spacetime sketch with vertical \(t\), horizontal \(x\), several nearly vertical comoving worldlines, and a marked spatial separation at fixed time. The screenshot should also be kept, because the lecture’s board structure matters: picture on the left, algebra in the middle, metric components on the right.
- `lecture_01_figure_02.png`: The right-side metric notation should be typeset cleanly as a displayed matrix or diagonal metric, not redrawn by hand, but the screenshot should stay nearby as evidence for how Susskind visually transitions from sketch to component form.
- `lecture_01_figure_03.png`: The dotted circle, angular labels, and circumference cue should be redrawn in TikZ as a clean circle model of a closed one-dimensional universe. The screenshot should also be kept, because it preserves the exact lecture framing and label placement that motivate the redraw.
- `lecture_01_figure_03.png`: The straight segment labeled \(2\pi a\) is not decorative; it should be incorporated into the redraw as an explicit circumference marker or nearby annotation, since it records the lecture’s move from abstract closed space to a plotted circle of radius-like parameter \(a\).

## Reconstruction Guidance
- For `lecture_01_figure_02.png`, typeset the cleaned spacetime line element as \(d\tau^2 = dt^2 - a^2(t)(dx^2+dy^2+dz^2)\), but treat this as a cautious cleanup of partially visible board writing rather than a verbatim transcription. Keep the screenshot visible beside the clean equation, because the frame is valuable precisely for showing the three-step progression from spacetime sketch to line element to metric components.
- For `lecture_01_figure_02.png`, if the notes include the metric tensor explicitly, present it cleanly as \(g_{\mu\nu}=\mathrm{diag}(1,-a^2,-a^2,-a^2)\). This is the right note-quality form, but it should be understood as a standard completion of a partly visible matrix, not as a fully legible direct read.
- For `lecture_01_figure_03.png`, use the frame to support a clean TikZ redraw of the circle with a marked origin \(\theta=0\), a nearby angle label \(\theta\), and a circumference annotation \(2\pi a\). Keep the screenshot nearby, because the board’s dotted circle and side labeling show how the lecturer is thinking pictorially, not just what the final cleaned diagram should look like.
- For `lecture_01_figure_03.png`, the metric itself should be presented in clean note form as \(ds^2=a^2\,d\theta^2\), with the notes making clear that this is reconstructed from the lecture’s spoken derivation rather than directly copied from visible chalk writing in the frame.
- In both cases, prefer a pair of artifacts in the final notes: the original screenshot as lecture evidence, and a cleaned typeset or TikZ version as the mathematically authoritative rendering.

## Uncertainties
- In `lecture_01_figure_02.png`, the far-right part of the line element is cut off and blurred, so the full set of spatial terms is not fully readable from the image alone.
- In `lecture_01_figure_02.png`, the metric matrix is only partially visible; the visible `1` and negative entries strongly suggest the standard diagonal form, but the full matrix should still be treated as a cautious completion.
- In `lecture_01_figure_02.png`, the small label marking spatial separation in the left-hand sketch is not securely legible.
- In `lecture_01_figure_03.png`, the radial-segment label looks like \(r\), but the lecture’s surrounding discussion uses \(a\) as the radius-like parameter in the plotted-circle picture, so the notes should not build a separate \(r\)-notation unless more evidence appears.
- In `lecture_01_figure_03.png`, the metric formula \(ds^2=a^2\,d\theta^2\) is not actually visible in the frame; it is a careful reconstruction from the lecture narrative.
- In `lecture_01_figure_03.png`, the circle outline is dotted and incomplete in places, especially near the lower part of the figure, so any TikZ redraw should regularize the shape without pretending every chalk irregularity is mathematically meaningful.