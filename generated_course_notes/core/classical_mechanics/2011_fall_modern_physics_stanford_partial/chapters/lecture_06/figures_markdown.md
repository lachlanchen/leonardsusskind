# Figure Notes
## Image Inventory
- `lecture_06_figure_03.png`: Medium board view from the Legendre-transform-to-mechanics transition. Susskind stands in front of the left half of the board, while the right half clearly shows the derivative relation between the Lagrangian and momentum and, beneath it, the Hamiltonian written as a Legendre transform. A cropped remnant of earlier writing is visible at the far left edge.

## Blackboard Equations
- `\displaystyle \frac{\partial \mathcal{L}}{\partial V_i}=P_i` [visible]
- `\displaystyle H(P)=\sum_i P_i V_i-\mathcal{L}` [partially visible]
- `\displaystyle P(v)` or similar left-edge label [partially visible]

## Diagram And Layout Reading
- This is an equation board rather than a geometric diagram.
- The right side of the board is organized in two conceptual layers: an upper line giving the defining derivative relation, and a lower line giving the Hamiltonian as the Legendre transform.
- The lecturer blocks much of the left side, so the frame is primarily useful as evidence for the right-hand equations and for the lecture’s shift from abstract \(V,P\) variables to the mechanics notation.
- A vertical board seam is visible near the center, which helps explain why the useful mathematics is concentrated on the right half of the frame.
- No standalone sketch or axes are visible in this crop.

## TeX Reconstruction Plan
- `lecture_06_figure_03.png` should remain visible in the chapter. Its value is documentary: it shows the moment when the abstract Legendre-transform formulas are carried over into mechanics.
- Nearby, the notes should typeset the cleaned equations as displayed mathematics:
  \[
  \frac{\partial \mathcal{L}}{\partial V_i}=P_i,
  \qquad
  H(P)=\sum_i P_i V_i-\mathcal{L}.
  \]
- No TikZ redraw is needed for this figure, because the content is algebraic rather than geometric.
- If the surrounding chapter normalizes notation to lowercase \(v_i,p_i\), the screenshot should still be kept as board evidence, while the nearby typeset equations may note the normalization once in prose.

## Caption Drafts
- `lecture_06_figure_03.png`: Hamiltonian as the Legendre transform of the Lagrangian

## Uncertainties
- The far-left cropped writing is incomplete and cannot be transcribed confidently; it looks like a leftover label involving \(P\) and \(v\).
- There appears to be additional writing above the derivative line, possibly a heading or a function label such as \(\mathcal{L}(V)\), but it is too cropped to trust.
- The Hamiltonian line is readable in structure, but the rightmost \(\mathcal{L}\) sits close to the crop edge; the full formula is safest as a standard completion guided by the visible board structure and the nearby transcript.
- The summation index on the Hamiltonian line is not perfectly sharp in the crop, so \(\sum_i\) should be treated as a cautious standard completion.