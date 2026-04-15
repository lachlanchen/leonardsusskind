# Figure Notes
## Image Inventory
- `lecture_07_figure_02.png`: Susskind stands at the left edge while the board shows a clean abstract Hamiltonian setup: canonical-variable labels at the top, the Hamiltonian written as a function of those variables, and the momentum-side Hamilton equation below.
- `lecture_07_figure_03.png`: Susskind stands left of a sparse worked-example board showing the specific Hamiltonian \(H=pq\) and the first equation for the \(p\)-component of the phase-space flow.

## Blackboard Equations
- `lecture_07_figure_02.png`: \(q_i,\ p_i\) [visible]
- `lecture_07_figure_02.png`: \(H(q,p)\) [partially visible]
- `lecture_07_figure_02.png`: \(\dot p_i=-\frac{\partial H}{\partial q_i}\) [visible]
- `lecture_07_figure_03.png`: \(H=pq\) [visible]
- `lecture_07_figure_03.png`: \(v_p=\dot p=-\frac{\partial H}{\partial q}\) [visible]

## Diagram And Layout Reading
- Neither screenshot contains a true geometric diagram, axis system, or flow sketch; both are equation-first blackboard states.
- `lecture_07_figure_02.png` has a clear vertical organization: canonical variables at the top, the Hamiltonian in the middle, and one Hamilton equation underneath. The surrounding blank board matters because it shows this is still the abstract recap stage.
- `lecture_07_figure_03.png` has the same sparse layout but now specialized to the example \(H=pq\). The board records the transition from a named Hamiltonian to the first component of the resulting phase-space velocity field.
- In both images, the large unused whiteboard area is useful evidence of pacing: these are unfolding steps, not crowded summary boards.

## TeX Reconstruction Plan
- Both screenshots should remain visible in the notes. They are legible and they preserve the lecture’s board layout and pacing.
- Near `lecture_07_figure_02.png`, reconstruct the visible mathematics as displayed equations, especially \(\dot p_i=-\frac{\partial H}{\partial q_i}\), and mention in prose that the Hamiltonian is being treated as a function of the canonical pairs \((q_i,p_i)\).
- Near `lecture_07_figure_03.png`, reconstruct the visible equations \(H=pq\) and \(v_p=\dot p=-\frac{\partial H}{\partial q}\) as clean displayed mathematics.
- Do not force later steps into the figure itself. The substitutions \(\dot p=-p\) and \(\dot q=q\) belong in the surrounding text or in subsequent displayed equations, not as claims about what is already written in these screenshots.
- No TikZ redraw is needed for these particular figures, since the useful content is the board writing itself rather than a geometric sketch.

## Caption Drafts
- `lecture_07_figure_02.png`: Generic Hamilton equation for the momentum variable
- `lecture_07_figure_03.png`: Beginning the \(H=pq\) phase-space flow example

## Uncertainties
- In `lecture_07_figure_02.png`, the middle notation is best read as \(H(q,p)\), but the punctuation between \(q\) and \(p\) is not perfectly clear.
- The handwritten \(p\) can momentarily resemble an uppercase \(P\); standard typesetting should normalize to lowercase canonical variables unless the surrounding chapter fixes another convention.
- In `lecture_07_figure_03.png`, the leftmost symbol is best read as \(v_p\), though the handwritten form is slightly ambiguous.
- Neither screenshot yet shows the second Hamilton equation \(\dot q_i=\frac{\partial H}{\partial p_i}\) or the completed example-specific substitutions; those should be added only from the transcript-backed lecture flow, not attributed directly to the images.