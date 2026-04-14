# Visual Evidence
## Frame Inventory
- `lecture_06_figure_03.png`: Medium board view of the Legendre-transform-to-mechanics transition, with Susskind blocking the left half and the right half showing the key derivative relation and Hamiltonian formula; this screenshot should remain in the final notes as documentary evidence for that board moment.

## Equation Extraction
- \(\displaystyle \frac{\partial \mathcal{L}}{\partial V_i}=P_i\) [visible]
- \(\displaystyle H(P)=\sum_i P_i V_i-\mathcal{L}\) [partially visible]
- \(\displaystyle P(v)\) or a similar left-edge label involving \(P\) as a function of \(v\) [partially visible]
- \(\displaystyle H(P)=\sum_i P_i V_i-\mathcal{L}\) with a clearly typeset summation index and full final \(\mathcal{L}\) [standard completion]

## Diagram Extraction
- There is no standalone geometric figure, axis system, or board sketch in this frame that calls for a TikZ redraw.
- What matters visually is the board structure: the upper right line gives the derivative relation, and the lower right line gives the Hamiltonian as a Legendre transform.
- This frame should be preserved as a screenshot, not replaced by TikZ, because its value is evidential rather than diagrammatic.
- If the final notes want a cleaner presentation, the companion should be displayed equations beside the screenshot, not a reconstructed board drawing.

## Reconstruction Guidance
- Keep `lecture_06_figure_03.png` near the point in the chapter where the abstract \(V\)-\(P\) Legendre-transform discussion is specialized to mechanics.
- Typeset the cleaned equations nearby as note-quality mathematics:
  \[
  \frac{\partial \mathcal{L}}{\partial V_i}=P_i,
  \qquad
  H(P)=\sum_i P_i V_i-\mathcal{L}.
  \]
- Preserve the board’s uppercase \(V_i,P_i\) notation in the immediate figure discussion, since that is what the frame visibly supports.
- If the chapter later normalizes to lowercase \(v_i,p_i\) or to \(\dot q_i,p_i\), do that explicitly in prose rather than silently rewriting the screenshot-backed formulas.
- Do not infer extra intermediate steps from this frame alone; use it only to support the defining Legendre-transform relations that are actually visible.

## Uncertainties
- The far-left cropped writing is incomplete and cannot be trusted beyond “something like \(P(v)\).”
- There may be additional writing above the visible derivative relation, possibly a heading or function label, but it is too cropped to recover reliably.
- The Hamiltonian line is readable in structure, but the summation index is not perfectly sharp, so \(\sum_i\) is a cautious standard completion.
- The final \(\mathcal{L}\) on the Hamiltonian line is close to the crop edge and should be treated as secure in structure but not in every pen stroke.
- The frame does not show whether any surrounding \(q\)-dependence was written elsewhere on the board; that must come from the transcript, not from the image.