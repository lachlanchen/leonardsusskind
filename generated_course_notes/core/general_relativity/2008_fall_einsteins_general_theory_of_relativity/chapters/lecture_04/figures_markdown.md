# Figure Notes
## Image Inventory
- `lecture_04_figure_02.png`: Susskind stands at the right edge of the lower board. The board shows a matrix-level identity at the top, `g^{-1} g = I`, and below it a boxed indexed relation identifying the upper-index metric components with the inverse matrix through contraction against `g_{rn}`. The upper board still contains remnants of earlier matrix notation.
- `lecture_04_figure_03.png`: A later, cleaner restatement of the same inverse-metric idea. The lower board again shows `g^{-1} g = I` above a large boxed indexed equation. Susskind stands to the left of the box rather than blocking it, so the boxed formula is more fully readable.
- `lecture_04_figure_04.png`: The upper board explicitly identifies `g_{mn}` with a matrix of entries such as `g_{11}, g_{12}, g_{13}` and so on. The lower board displays the contraction `g^{mr} g_{rn} = \delta^m_n`. The right edge shows the start of a `ds^2` expression on the neighboring board.
- `lecture_04_figure_05.png`: The lecturer has stepped out of the frame. The lower board contains the line-element calculation written in contracted index notation, including a circled term involving `dx^n g_{mn}` and the conclusion `ds^2` on the right. A small leftover note `1/r^2` remains at the lower right from an earlier example.
- `lecture_04_figure_06.png`: A wide board view. On the left is a flat-space line element written as a sum of two squared differentials. On the right is a skew-grid drawing: a black rectangular grid overlaid or accompanied by a slanted blue coordinate construction with a highlighted slanted segment and triangular shape. Susskind stands at the far left without blocking the main content.

## Blackboard Equations
- `lecture_04_figure_02.png`: `g^{-1} g = I` [visible]
- `lecture_04_figure_02.png`: `g^{mr} g_{rn} = \delta^m_{\ n}` [visible]
- `lecture_04_figure_03.png`: `g^{-1} g = I` [visible]
- `lecture_04_figure_03.png`: `g^{mr} g_{rn} = \delta^m_{\ n}` [visible]
- `lecture_04_figure_04.png`: `g_{mn} \leftrightarrow \begin{pmatrix} g_{11} & g_{12} & g_{13} \\ g_{21} & g_{22} & g_{23} \\ g_{31} & \cdots \end{pmatrix}` [partially visible]
- `lecture_04_figure_04.png`: `g^{mr} g_{rn} = \delta^m_{\ n}` [visible]
- `lecture_04_figure_05.png`: `dx^m dx_m` [visible]
- `lecture_04_figure_05.png`: `dx^n g_{mn}` [visible]
- `lecture_04_figure_05.png`: `dx^m (dx^n g_{mn}) = ds^2` [partially visible]
- `lecture_04_figure_05.png`: `dx_m = g_{mn} dx^n` [standard reconstruction]
- `lecture_04_figure_05.png`: `dx^m dx_m = g_{mn} dx^m dx^n = ds^2` [standard reconstruction]
- `lecture_04_figure_06.png`: `ds^2 = d{x'}^{\,2} + d{x''}^{\,2}` [partially visible]
- `lecture_04_figure_06.png`: `ds^2 = (dx^1)^2 + (dx^2)^2` [standard reconstruction]
- `lecture_04_figure_06.png`: `ds^2 = \delta_{mn}\,dx^m dx^n` [standard reconstruction]

## Diagram And Layout Reading
- `lecture_04_figure_02.png` is organized as a two-level argument: matrix language on the top line and indexed tensor language below. The box around the lower equation is important pedagogically. It visually marks the contraction identity as the operative definition of the upper-index metric.
- `lecture_04_figure_03.png` keeps the same structure but is cleaner. The box is more complete and the lecturer no longer points into it. This makes it especially useful as documentary evidence for the “metric tensor has an inverse” discussion.
- `lecture_04_figure_04.png` spreads the argument across the upper and lower boards. The top board says that the metric tensor is a matrix of components; the lower board says how its inverse is encoded in upper-index notation. The screenshot is useful not just for the formulas but for this top-to-bottom organization.
- `lecture_04_figure_05.png` is layout-driven rather than matrix-driven. The board uses a circled subexpression to emphasize the act of lowering an index: the circled factor is the lower-index version of the differential displacement. The right-hand `ds^2` is the geometric payoff.
- `lecture_04_figure_06.png` juxtaposes algebra and geometry. The left half states the Euclidean line element in a Cartesian-looking form, while the right half sketches two coordinate descriptions on the same plane: a regular orthogonal grid and a slanted coordinate construction. The point is not just the formula; it is that coordinate changes can preserve the form of the interval in flat space.

## TeX Reconstruction Plan
- `lecture_04_figure_02.png` should remain visible. It is direct documentary evidence for the moment when Susskind identifies the inverse metric with an upper-index tensor. Place a clean displayed equation nearby:
  \[
  g^{mr} g_{rn} = \delta^m_{\ n}.
  \]
  The matrix shorthand `g^{-1}g=I` should also be typeset nearby in prose or display.
- `lecture_04_figure_03.png` should remain visible. Although it overlaps mathematically with figure 02, it captures the boxed inverse relation in a more finished state and supports the later narrative beat that the metric always has an inverse. Pair it with the same clean displayed contraction identity.
- `lecture_04_figure_04.png` should remain visible. It documents the upper-board move from tensor notation to an explicit matrix of components. Reconstruct both the matrix view and the inverse relation in typeset form nearby:
  \[
  g_{mn} \leftrightarrow (g_{ij}), \qquad g^{mr}g_{rn}=\delta^m_{\ n}.
  \]
- `lecture_04_figure_05.png` should remain visible. The circled term is part of the pedagogical logic, so the screenshot should not be replaced by typeset algebra alone. Reconstruct the mathematics cleanly nearby as
  \[
  dx_m = g_{mn}dx^n,
  \qquad
  dx^m dx_m = g_{mn}\,dx^m dx^n = ds^2.
  \]
- `lecture_04_figure_06.png` should remain visible and should be paired with both a typeset equation and a TikZ redraw. The equation on the left should be reconstructed cleanly as the flat Cartesian line element,
  \[
  ds^2=(dx^1)^2+(dx^2)^2=\delta_{mn}\,dx^m dx^n,
  \]
  while the right-hand grid sketch should be redrawn schematically in TikZ as an orthogonal grid together with a rotated or skew coordinate family and a highlighted segment. The screenshot should stay because the board’s asymmetric “equation on left, diagram on right” layout is itself useful evidence.

## Caption Drafts
- `lecture_04_figure_02.png`: Inverse metric contraction identity
- `lecture_04_figure_03.png`: Boxed inverse metric relation
- `lecture_04_figure_04.png`: Metric tensor as matrix and inverse
- `lecture_04_figure_05.png`: Lowering an index with the metric
- `lecture_04_figure_06.png`: Flat line element and skew Cartesian grids

## Uncertainties
- `lecture_04_figure_02.png`: The boxed left factor is slightly crowded. The image strongly supports the reading `g^{mr}`, but the visual link to the explicit matrix inverse on the line above means the prose should make clear that the upper-index metric is the inverse matrix.
- `lecture_04_figure_03.png`: The same ambiguity remains in principle, though the equation itself is cleaner. The upper-board identity matrix notation is partly cropped.
- `lecture_04_figure_04.png`: The top matrix is only partially visible. Enough entries are readable to show that Susskind is thinking of `g_{mn}` as an ordinary matrix, but the full array should be typeset in a normalized way rather than transcribed literally from every visible component.
- `lecture_04_figure_05.png`: The first line on the board is not a clean mathematical equality. The later transcript explicitly says Susskind did not mean an equals sign there, only a contraction step. The typeset notes should therefore not reproduce any misleading equality verbatim.
- `lecture_04_figure_05.png`: The small `1/r^2` at lower right appears to be leftover material from the earlier polar-coordinate inverse-metric discussion and should not be folded into the main derivation here.
- `lecture_04_figure_06.png`: The exact prime notation on the left-hand differentials is not perfectly legible; it is safer to reconstruct the clean flat-space formula from the transcript than to over-commit to the chalk primes.
- `lecture_04_figure_06.png`: The right-hand diagram has no fully legible axis labels. The redraw should therefore remain schematic unless the transcript supplies the coordinate names unambiguously.