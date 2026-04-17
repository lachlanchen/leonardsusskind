# Figure Notes
## Image Inventory
- `lecture_05_figure_02.png`: A close board shot showing Susskind at the lower left while a single displayed equation runs across the upper board. The left term is a partial derivative of a covariant vector component, the middle term is a Christoffel-symbol correction multiplying \(V_r\), and the right-hand side is labeled as a rank-two tensor \(T\) with two lower indices. A smaller, lower-board shorthand line is partially visible beneath the main equation.
- `lecture_05_figure_03.png`: A later close board shot of essentially the same formula, now written with a different derivative index. Susskind stands farther to the right, so the left and middle parts of the equation are clearer, while the right-hand side tensor label is still partly encroached on by his body. A lower shorthand notation appears again beneath the main line.

## Blackboard Equations
- `lecture_05_figure_02.png`: \(\dfrac{\partial V_m}{\partial y^n} + \Gamma^r{}_{nm} V_r = T_{mn}\) [visible]
- `lecture_05_figure_02.png`: \(\nabla_n V_m\) [partially visible]
- `lecture_05_figure_03.png`: \(\dfrac{\partial V_m}{\partial y^p} + \Gamma^r{}_{pm} V_r = T_{mp}\) [partially visible]
- `lecture_05_figure_03.png`: \(\nabla_p V_m\) [partially visible]
- `lecture_05_figure_03.png`: \(\Gamma^r{}_{pm} V_r\) [visible]

## Diagram And Layout Reading
- Neither image contains a geometric sketch; their value is the board organization of a single formula.
- In both images the upper board is used for the full displayed equation, with the derivative term on the left, the Christoffel-symbol correction in the middle, and the tensor label on the right.
- The lower board appears to carry a compact shorthand version of the same statement, likely the covariant-derivative notation \(\nabla V\), but it is only partially visible.
- `lecture_05_figure_02.png` is the cleaner documentary frame for the full line as a definition-like statement.
- `lecture_05_figure_03.png` is useful as a second beat because it shows the same structure after the lecture has shifted notation to the index \(p\), matching the later audience discussion about index placement and non-interchangeability.

## TeX Reconstruction Plan
- `lecture_05_figure_02.png` should remain visible in the notes. It is good evidence for the moment when Susskind writes the covariant derivative of a lower-index vector as an ordinary derivative plus a connection term. Pair it with a clean displayed equation:
  \[
  \nabla_n V_m = \frac{\partial V_m}{\partial y^n} + \Gamma^r{}_{nm} V_r,
  \qquad
  \text{or equivalently } T_{mn}.
  \]
- `lecture_05_figure_03.png` should also remain visible if the notes preserve the later Q\&A beat about index placement. Pair it with the same formula in the later index notation:
  \[
  \nabla_p V_m = \frac{\partial V_m}{\partial y^p} + \Gamma^r{}_{pm} V_r,
  \]
  and, if context requires, mention that the resulting object is a tensor \(T_{mp}\).
- No TikZ redraw is needed for either image; these are equation-and-layout figures, not diagrams.
- The screenshots should serve as documentary support, while the typeset equations nearby should normalize the notation and remove the minor occlusion from the lecturer.

## Caption Drafts
- `lecture_05_figure_02.png`: Covariant derivative of a lower-index vector
- `lecture_05_figure_03.png`: Reindexed covariant-derivative formula

## Uncertainties
- In `lecture_05_figure_02.png`, the denominator coordinate label is cramped; it reads most naturally as \(y^n\), consistent with the lecture’s surrounding notation, but the superscript is tight on the board.
- In `lecture_05_figure_03.png`, the right-hand side tensor label is partly blocked by Susskind; \(T_{mp}\) is the most plausible reading, but the screenshot alone is slightly less decisive than the left and middle terms.
- The lower shorthand notation in both images is only partially visible. It strongly suggests \(\nabla_n V_m\) in the first frame and \(\nabla_p V_m\) in the second, but that shorthand should be treated as cautious reconstruction rather than fully clean transcription.
- The equation in the second frame is visually the same structural rule as in the first, but its lecture role is slightly different: it sits in the middle of an audience question about swapping indices. The notes should therefore avoid making the screenshot carry more conceptual weight than the transcript gives it.