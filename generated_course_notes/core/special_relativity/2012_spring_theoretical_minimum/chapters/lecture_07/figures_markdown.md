# Figure Notes
## Image Inventory
- `lecture_07_figure_02.png`: a clean board frame centered on the nonrelativistic Lorentz-force law. The main visible content is the equation `ma = e[ E + v x B ]`, written large across the middle-right of the board. At the far left there is a cropped leftover sketch with slanted lines and pale colored traces, and at the lower left there is a partial fragment of earlier writing that looks like part of `dxdydz`.
- `lecture_07_figure_03.png`: a two-level blackboard view showing the action in ordinary-time form on the upper writing strip and the corresponding Lagrangian on the strip below. Susskind stands at the right, partially occluding the right-hand part of the lower formula. A residual `A_\mu` notation is visible on the lower board.

## Blackboard Equations
- `lecture_07_figure_02.png`: `ma = e\left[ E + v \times B \right]` `[visible]`
- `lecture_07_figure_02.png`: `dxdydz` or a close fragment thereof at lower left `[partially visible]`
- `lecture_07_figure_03.png`: `\int \left[-m\sqrt{1-\dot X^2} - e\left(A_0 + A_m \dot X^m\right)\right]\,dt` `[partially visible]`
- `lecture_07_figure_03.png`: `L := -m\sqrt{1-\dot X^2} - e\left(A_0(x,t) + A_m(x,t)\dot X^m\right)` `[partially visible]`
- `lecture_07_figure_03.png`: `A_\mu` `[visible]`
- `lecture_07_figure_03.png`: `S=\int dt\,\left[-m\sqrt{1-\dot X^2}-e\left(A_0+A_m\dot X^m\right)\right]` `[standard reconstruction]`
- `lecture_07_figure_03.png`: `L=-m\sqrt{1-\dot X^2}-e\left(A_0(x,t)+A_m(x,t)\dot X^m\right)` `[standard reconstruction]`

## Diagram And Layout Reading
- `lecture_07_figure_02.png`: the board is visually sparse, with the Lorentz-force equation isolated in a large open field. That isolation matters pedagogically: the equation is being presented as the target force law before the vector-potential construction is reintroduced.
- `lecture_07_figure_02.png`: the cropped left-edge sketch is not a complete diagram in its own right. It reads as residual board context rather than a figure to be independently interpreted.
- `lecture_07_figure_03.png`: the board is organized top-to-bottom as a rewrite. The upper strip gives the action in `dt` language; the lower strip extracts the Lagrangian from the integrand. This layout is the main visual value of the frame.
- `lecture_07_figure_03.png`: the lecturer partially blocks the right side of the lower equation, but the visual logic remains clear: first the action, then the explicit `L`.
- `lecture_07_figure_03.png`: the isolated `A_\mu` on the lower board reinforces that the vector potential remains the central object even as the discussion moves to the Euler-Lagrange machinery.

## TeX Reconstruction Plan
- `lecture_07_figure_02.png` should remain visible. It is the best board evidence for the target Lorentz-force law written in elementary form. Pair it with a clean displayed equation
  `m\mathbf a = e(\mathbf E + \mathbf v \times \mathbf B)`.
  No TikZ redraw is needed.
- `lecture_07_figure_02.png`: do not attempt to redraw the cropped left-edge sketch unless some later frame supplies the full diagram. In this figure, the sketch is secondary and should remain only as contextual residue in the screenshot.
- `lecture_07_figure_03.png` should remain visible. It is useful precisely because it shows the lecture’s board organization from action to Lagrangian. Pair it with clean displayed equations for both the ordinary-time action and the resulting Lagrangian.
- `lecture_07_figure_03.png`: the readable mathematics in the notes should come from typeset reconstruction, not from the screenshot alone, because the right side of the lower line is partly occluded and the top line is not perfectly complete at the image edges.
- Neither selected figure calls for TikZ. Screenshot-plus-equation treatment is the right approach for both.

## Caption Drafts
- `lecture_07_figure_02.png`: Lorentz force law on the board.
- `lecture_07_figure_03.png`: Action rewritten as the ordinary-time Lagrangian.

## Uncertainties
- `lecture_07_figure_02.png`: the lower-left `dxdydz` fragment is cropped and appears unrelated to the main Lorentz-force equation. It should not be overinterpreted.
- `lecture_07_figure_02.png`: the left-edge sketch is too incomplete to identify confidently as a meaningful standalone diagram.
- `lecture_07_figure_02.png`: the board writes the cross product with a handwritten `x`; the notes should typeset it as `\times`.
- `lecture_07_figure_03.png`: the upper action line is partially cropped at both ends, so the fully explicit integral form should be reconstructed cautiously from the visible pattern plus the transcript.
- `lecture_07_figure_03.png`: the lecturer obscures part of the lower line, especially the right-hand field term, so the full expression `A_m(x,t)\dot X^m` is safer as a standard reconstruction than as a pure image transcription.
- `lecture_07_figure_03.png`: the board alternates between bare `A_0`, `A_m` and explicit `(x,t)` dependence; the notes should normalize this carefully while preserving the lecture’s intent rather than the exact inconsistency of the handwriting.