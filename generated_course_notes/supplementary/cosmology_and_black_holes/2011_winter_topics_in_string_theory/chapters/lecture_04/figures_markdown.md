# Figure Notes
## Image Inventory
- `lecture_04_figure_02.png`: Upper-left equation block on a mostly blank board. The visible content is the near-horizon metric in \((\rho,\omega)\) coordinates together with the rescaling \(\omega=t/(4MG)\). Susskind stands at lower right reading from notes, but he does not block the main equation.
- `lecture_04_figure_04.png`: A developed black-hole causal sketch fills the board. Two diagonals cross at a central point, with a wavy curve above and another below, a thick diagonal trajectory through the diagram, a second red diagonal segment, several arrows, and a visible label \(H\) near the middle-right.
- `lecture_04_figure_05.png`: A partial construction drawing on the left side of the board. It shows a left vertical boundary, several nearly horizontal lines, a few slanted guide lines, and one darker diagonal. This looks like an in-progress Penrose-grid or compactification sketch rather than a finished diagram.
- `lecture_04_figure_06.png`: A much more complete compactified spacetime diagram. A left vertical boundary is connected to a right-hand tip by upper and lower outer rays, with a fan of interior curves and transverse lines crowded toward the tip. Several blue labels are present but only partly legible.

## Blackboard Equations
- `lecture_04_figure_02.png` [visible]
  \[
  \omega=\frac{t}{4MG}
  \]
- `lecture_04_figure_02.png` [visible]
  \[
  ds^2=-\rho^2\,d\omega^2+d\rho^2
  \]
- `lecture_04_figure_04.png` [visible]
  \[
  H
  \]
- `lecture_04_figure_04.png` [partially visible]: a small upper annotation near the top wavy curve is present, but it is not legible enough to transcribe securely.
- `lecture_04_figure_05.png` [partially visible]
  \[
  \rho
  \]
  or a similar radial label appears near the left-center, but the exact character is faint.
- `lecture_04_figure_06.png` [partially visible]: the upper and lower blue labels look like null-infinity markers, consistent with
  \[
  \mathscr{I}^{+},\qquad \mathscr{I}^{-},
  \]
  but the image alone does not make the script letters fully secure.
- `lecture_04_figure_06.png` [partially visible]: the top and bottom of the left vertical boundary appear to be endpoint labels for timelike infinity, consistent with
  \[
  t=+\infty,\qquad t=-\infty,
  \]
  though the exact handwritten notation is not fully readable.
- `lecture_04_figure_06.png` [standard reconstruction]: the right tip is the compactified spatial endpoint discussed in the transcript, so the cleaned notes can label it as
  \[
  \rho=\infty
  \]
  or \(r=\infty\), but that label should come from the transcript rather than the screenshot alone.

## Diagram And Layout Reading
- `lecture_04_figure_02.png` is not a diagram frame; its value is the equation block and the uncluttered board layout. It is the cleanest visual evidence for the lecture’s recap that the near-horizon metric is flat spacetime in hyperbolic-polar form.
- `lecture_04_figure_04.png` is a genuine causal-structure board drawing. The central X-shaped crossing reads as null lines or horizon lines meeting at a bifurcate point. The upper and lower wavy curves read as singularity boundaries rather than smooth coordinate lines. The heavy diagonal and colored auxiliary lines suggest later discussion of trajectories, infall, or time-reversed motion.
- `lecture_04_figure_04.png` also preserves the board’s narrative layering: an original black diagram, later colored additions, and local labels added on top. That makes it valuable not just for the final geometry but for the way Susskind built the argument on the board.
- `lecture_04_figure_05.png` shows a construction phase rather than a finished figure. The left vertical boundary acts like a time axis or boundary line, the nearly horizontal slices look like constant-time lines before or during compactification, and the slanted lines look like null directions being preserved under the Penrose redraw.
- `lecture_04_figure_06.png` is the most complete diagram of the Penrose-introduction portion. The whole layout reads as a compactified flat-spacetime diagram: left vertical timelike axis, right spatial endpoint, upper and lower null boundaries, and a family of interior curves showing how the ordinary \((t,\rho)\) grid gets squashed into a finite region.
- `lecture_04_figure_06.png` matters because it captures the final board organization after the construction steps: the outer boundary, the crowded family of constant-\(\rho\) curves near the right tip, and the transverse family of time slices all appear together.

## TeX Reconstruction Plan
- `lecture_04_figure_02.png` must remain visible. It should be paired immediately with clean displayed equations for
  \[
  \omega=\frac{t}{4MG},
  \qquad
  ds^2=-\rho^2\,d\omega^2+d\rho^2,
  \]
  since those are both legible and central to the lecture’s recap.
- `lecture_04_figure_04.png` should remain visible as screenshot evidence for the causal sketch. A nearby TikZ redraw should simplify the board into a readable black-hole/white-hole style diagram with crossed null lines, a bifurcation point, future and past singularity curves, and the main trajectory lines that organize the later discussion.
- `lecture_04_figure_05.png` should remain visible, but as a smaller supporting screenshot. Its main role is to show the Penrose-diagram construction in progress. The nearby TikZ should reconstruct only the skeleton of the squashed grid and the preserved null directions, not pretend that this frame alone is the finished diagram.
- `lecture_04_figure_06.png` must remain visible and should carry the main Penrose-diagram exposition. A nearby TikZ redraw should present the completed compactified flat-spacetime diagram cleanly, with timelike infinity on the left endpoints, spatial infinity at the right tip, null infinity on the upper and lower slanted boundaries, and curved interior grid lines.
- `lecture_04_figure_05.png` and `lecture_04_figure_06.png` should be treated as a pair: the first is construction evidence, the second is the readable result. The notes should not collapse them into a single unlabeled figure.
- For `lecture_04_figure_04.png` and `lecture_04_figure_06.png`, labels such as \(r=0\), \(i^\pm\), \(i^0\), or \(\mathscr{I}^\pm\) should be added in the cleaned redraw only when the surrounding prose has already introduced them from the transcript.

## Caption Drafts
- `lecture_04_figure_02.png`: Near-horizon metric in \((\rho,\omega)\) coordinates.
- `lecture_04_figure_04.png`: Causal sketch with horizons, singularity curves, and trial trajectories.
- `lecture_04_figure_05.png`: Penrose-diagram construction grid on the board.
- `lecture_04_figure_06.png`: Compactified flat-spacetime Penrose diagram.

## Uncertainties
- `lecture_04_figure_04.png`: the upper and lower wavy curves are visually emphatic, but their exact labels are not legible from the screenshot alone. They are best interpreted through the transcript as singularity curves rather than transcribed directly from the image.
- `lecture_04_figure_04.png`: the small blue notation near the upper right is too faint to quote confidently.
- `lecture_04_figure_05.png`: the drawing is visibly partial. Its interpretation as a Penrose-construction step is strongly supported by the surrounding lecture, but the screenshot alone does not specify every line’s exact intended label.
- `lecture_04_figure_06.png`: the blue endpoint labels are present but too soft to read with certainty. The cleaned notes may use the standard \(i^\pm\), \(i^0\), and \(\mathscr{I}^\pm\) notation, but that should be justified by the transcript rather than by claiming direct visual legibility.
- `lecture_04_figure_06.png`: despite earlier shorthand descriptions, this frame is best read as the compactified flat-spacetime Penrose diagram that Susskind is about to use as the starting point for the black-hole redraw, not as the final black-hole Penrose diagram itself.