# Figure Notes
## Image Inventory
- `lecture_09_figure_02.png`: A tight board crop during the Poisson-bracket review. The upper line shows a partial product-rule formula for Poisson brackets, cropped at the right edge. The lower line clearly shows the special case \(\{P,P\}=0\), with Susskind’s hand pointing toward it.
- `lecture_09_figure_03.png`: A local writing shot during the discussion of Poisson-bracketing a function of \(q\) with \(P\). The left-hand side \(\{F(q),P\}\) is on the board, followed by an equals sign, while the right-hand side is only just beginning to be written and is not yet legible.

## Blackboard Equations
- `lecture_09_figure_02.png`: \(\{AB,C\}=A\{B,C\}\) [partially visible]
- `lecture_09_figure_02.png`: \(\{P,P\}=0\) [visible]
- `lecture_09_figure_02.png`: \(\{AB,C\}=A\{B,C\}+B\{A,C\}\) [standard reconstruction]

- `lecture_09_figure_03.png`: \(\{F(q),P\}=\) [partially visible]
- `lecture_09_figure_03.png`: \(\{F(q),P\}=\dfrac{dF}{dq}\) [standard reconstruction]
- `lecture_09_figure_03.png`: \(\{F(q),P\}=\dfrac{\partial F}{\partial q}\) [standard reconstruction]

## Diagram And Layout Reading
- `lecture_09_figure_02.png` is not a geometric diagram; it is a two-level board layout. The upper line preserves the nearby abstract algebraic context, while the lower line isolates the concrete special case \(\{P,P\}=0\). The lecturer’s hand makes the lower equation the focus.
- `lecture_09_figure_03.png` is a derivation-in-progress layout rather than a finished board statement. The left-hand side is complete, the equals sign is already present, and the large blank region to the right records the transition from bracket notation to differentiation language.
- Neither image contains axes, arrows, or sketches that need independent TikZ treatment.

## TeX Reconstruction Plan
- `lecture_09_figure_02.png` should remain visible in the notes. It is good documentary evidence for the lecture’s move from the abstract product rule to the concrete consequence \(\{P,P\}=0\). Nearby, typeset the clean displayed equation
  \[
  \{P,P\}=0.
  \]
  If the chapter also discusses the product rule at that point, pair it with the cleaned form
  \[
  \{AB,C\}=A\{B,C\}+B\{A,C\}.
  \]
- `lecture_09_figure_03.png` should also remain visible. Its value is not a fully finished formula, but the board rhythm of writing \(\{F(q),P\}\) and then converting it into a derivative statement. Nearby, reconstruct the mathematics as a clean display, for example
  \[
  \{F(q),P\}=\frac{dF}{dq},
  \]
  or in partial-derivative notation if the surrounding text prefers it.
- No TikZ redraw is needed for either figure. Both are equation-board moments, so the notes should keep the screenshots and place cleaned equations beside them.

## Caption Drafts
- `lecture_09_figure_02.png`: Poisson bracket of \(P\) with itself
- `lecture_09_figure_03.png`: Poisson bracket with \(P\) as a derivative

## Uncertainties
- In `lecture_09_figure_02.png`, the upper product-rule line is cropped before the full second term is visible, so the completed formula must be restored from context rather than claimed as fully visible.
- In `lecture_09_figure_03.png`, the right-hand side of the equation is not yet legible in the screenshot; only the left-hand side and the equals sign are secure from the image itself.
- In `lecture_09_figure_03.png`, the exact letter case of the variable in \(F(q)\) versus \(F(Q)\) should be normalized from the lecture context; the image itself most naturally reads as \(F(q)\), but the transcript should settle the final notation.
- In `lecture_09_figure_03.png`, the derivative notation on the right may be written in the lecture as either \(dF/dq\) or \(\partial F/\partial q\); the frame alone does not determine that choice.