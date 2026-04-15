# Visual Evidence
## Frame Inventory
- `lecture_07_figure_02.png`: A sparse recap board showing canonical variables, the Hamiltonian as a function of those variables, and the momentum-side Hamilton equation; this screenshot should remain in the final notes because it is clear board evidence for the abstract setup.
- `lecture_07_figure_03.png`: A sparse worked-example board showing the special Hamiltonian \(H=pq\) and the first phase-space velocity relation for the \(p\)-direction; this screenshot should remain in the final notes because it captures the start of the example exactly where the lecture turns concrete.

## Equation Extraction
- `lecture_07_figure_02.png`: \(q_i,\ p_i\) [visible]
- `lecture_07_figure_02.png`: \(H(q,p)\) [partially visible]
- `lecture_07_figure_02.png`: \(\dot p_i=-\frac{\partial H}{\partial q_i}\) [visible]
- `lecture_07_figure_02.png`: \(\dot q_i=\frac{\partial H}{\partial p_i}\) [standard completion]
- `lecture_07_figure_03.png`: \(H=pq\) [visible]
- `lecture_07_figure_03.png`: \(v_p=\dot p=-\frac{\partial H}{\partial q}\) [visible]
- `lecture_07_figure_03.png`: \(\dot p=-p\) [standard completion]
- `lecture_07_figure_03.png`: \(\dot q=\frac{\partial H}{\partial p}=q\) [standard completion]

## Diagram Extraction
- Neither frame contains a geometric diagram, axis system, contour plot, or flow sketch that needs direct TikZ reproduction; both are equation-first board states.
- `lecture_07_figure_02.png` should be preserved as a screenshot rather than redrawn, because its value is the clean staging of the abstract Hamiltonian setup on the board.
- `lecture_07_figure_03.png` should also be preserved as a screenshot rather than redrawn, because its value is the visible transition from the named Hamiltonian \(H=pq\) to the first phase-space velocity equation.
- If the final chapter also includes a TikZ sketch of the \(H=pq\) area-preserving deformation, that redraw should be treated as transcript-driven supporting exposition, not as something directly extracted from these frames.

## Reconstruction Guidance
- Keep both screenshots visible in the final chapter and place clean displayed equations nearby; the screenshots provide the board evidence, while the LaTeX provides the legible final mathematical form.
- For `lecture_07_figure_02.png`, typeset the canonical-pair setup and the visible equation \(\dot p_i=-\frac{\partial H}{\partial q_i}\), then add the companion equation \(\dot q_i=\frac{\partial H}{\partial p_i}\) only as a transcript-backed standard completion, not as if it were already written on the board.
- For `lecture_07_figure_03.png`, typeset exactly what is visible first, namely \(H=pq\) and \(v_p=\dot p=-\frac{\partial H}{\partial q}\), then complete the worked example in surrounding text with \(\dot p=-p\) and \(\dot q=q\).
- Normalize handwriting into standard note notation: lowercase \(q_i,p_i\), partial derivatives with \(\partial\), and dotted variables in standard LaTeX form.
- Preserve the sparse board rhythm. These frames are useful because they show the lecture unfolding step by step, not because they summarize the entire derivation in one place.
- No TikZ redraw is needed for the content directly visible in these two frames; equation typesetting plus the original screenshots is the right combination here.

## Uncertainties
- In `lecture_07_figure_02.png`, the middle expression is best read as \(H(q,p)\), but the separator between \(q\) and \(p\) is slightly ambiguous.
- In `lecture_07_figure_02.png`, the handwritten \(p\) can briefly resemble an uppercase \(P\); standard typesetting should use lowercase canonical variables.
- In `lecture_07_figure_03.png`, the leftmost symbol is best read as \(v_p\), but the handwritten form is not perfectly crisp.
- In `lecture_07_figure_03.png`, the example has not yet been algebraically completed on the board, so \(\dot p=-p\) and \(\dot q=q\) must be treated as cautious standard completion from the transcript, not as visible board content.
- Neither frame shows the later geometric consequences of the \(H=pq\) example, such as a stretched-and-squeezed patch or a divergence calculation; those belong to later reconstruction, not direct figure extraction.