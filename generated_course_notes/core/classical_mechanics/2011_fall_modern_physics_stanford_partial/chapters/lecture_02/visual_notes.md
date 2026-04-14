# Visual Evidence
## Frame Inventory
- `lecture_02_figure_02.png`: Left-board close-up of the energy review showing the kinetic-energy definition, `E=T+U`, and separate time-derivative lines; this screenshot should remain in the final notes.
- `lecture_02_figure_03.png`: Wider board view showing the same energy setup together with the combined `dE/dt` expression and the visual cancellation cue on the right; this screenshot should remain in the final notes.
- `lecture_02_figure_04.png`: In-progress transition shot where Susskind is rewriting Newton’s law into momentum language on an otherwise blank board; this screenshot may remain as a narrative transition image but should not carry the final equation by itself.
- `lecture_02_figure_05.png`: Clean close-up of the finished stacked momentum equations, from component form to vector form; this screenshot should remain in the final notes.
- `lecture_02_figure_06.png`: Wide board shot combining the left-column momentum equations with a central force-arrow sketch for the action-reaction discussion; this screenshot should remain in the final notes.

## Equation Extraction
- `lecture_02_figure_02.png`: \(T=\frac{1}{2}mv^2=\frac{1}{2}m(v_x^2+v_y^2)\) [standard completion]
- `lecture_02_figure_02.png`: \(\frac{1}{2}m\sum_i v_i^2\) [partially visible]
- `lecture_02_figure_02.png`: \(E=T+U\) [visible]
- `lecture_02_figure_02.png`: \(\frac{dT}{dt}=\sum_i m v_i a_i\) [visible]
- `lecture_02_figure_02.png`: \(\frac{dU}{dt}=\sum_i \frac{\partial U}{\partial x_i}v_i\) [visible]

- `lecture_02_figure_03.png`: \(T=\frac{1}{2}mv^2=\frac{1}{2}m(v_x^2+v_y^2)\) [standard completion]
- `lecture_02_figure_03.png`: \(\frac{1}{2}m\sum_i v_i^2\) [partially visible]
- `lecture_02_figure_03.png`: \(E=T+U\) [visible]
- `lecture_02_figure_03.png`: \(\frac{dT}{dt}=\sum_i m v_i a_i\) [visible]
- `lecture_02_figure_03.png`: \(\frac{dU}{dt}=\sum_i \frac{\partial U}{\partial x_i}v_i\) [visible]
- `lecture_02_figure_03.png`: \(\frac{dE}{dt}=\sum_i\left(m a_i+\frac{\partial U}{\partial x_i}\right)v_i\) [visible]
- `lecture_02_figure_03.png`: \((F_i-F_i)\) [partially visible]

- `lecture_02_figure_04.png`: \(F=\frac{d}{dt}(mv)\) [visible]
- `lecture_02_figure_04.png`: \(F=\frac{d}{dt}\,\cdots\) [partially visible]

- `lecture_02_figure_05.png`: \(F_i=m\frac{dv_i}{dt}\) [visible]
- `lecture_02_figure_05.png`: \(F=\frac{d}{dt}(mv)\) [visible]
- `lecture_02_figure_05.png`: \(\vec{F}=\frac{d\vec{P}}{dt}\) [visible]

- `lecture_02_figure_06.png`: \(F_i=m\frac{dv_i}{dt}\) [visible]
- `lecture_02_figure_06.png`: \(F=\frac{d}{dt}(mv)\) [visible]
- `lecture_02_figure_06.png`: \(\vec{F}=\frac{d\vec{P}}{dt}\) [visible]
- `lecture_02_figure_06.png`: force labels and short arrow labels in the central sketch, of the form \(F_{\cdots}\) [partially visible]

## Diagram Extraction
- `lecture_02_figure_02.png` and `lecture_02_figure_03.png` preserve a two-stage board layout rather than a standalone diagram: first the separate derivative ingredients are stacked vertically, then the right half of the board shows how they combine into a cancellation; these should be preserved as screenshots, not redrawn in TikZ.
- `lecture_02_figure_04.png` is mainly a process image showing the rewriting step from force to momentum language; preserve it only as a screenshot if the notes want the board rhythm.
- `lecture_02_figure_05.png` contains no geometric diagram, but its three-line hierarchy is pedagogically important and should be preserved as a screenshot next to clean displayed equations.
- `lecture_02_figure_06.png` contains the one genuinely diagrammatic element in this frame set: a qualitative many-particle or pairwise-force sketch with arrows and labels; this should be shown both as the original screenshot and as a modest TikZ redraw.
- The TikZ redraw for `lecture_02_figure_06.png` should clarify only the core logic of pairwise equal-and-opposite internal forces, not the exact hand-drawn geometry of the board.

## Reconstruction Guidance
- Use `lecture_02_figure_02.png` and `lecture_02_figure_03.png` together to reconstruct the energy-conservation review as a clean sequence of displayed equations: define \(T\), write \(E=T+U\), compute \(\frac{dT}{dt}\) and \(\frac{dU}{dt}\), then combine them into \(\frac{dE}{dt}\).
- Keep the screenshots near that derivation because the board order matters: the frames show that Susskind first builds the pieces and only afterward performs the cancellation.
- Treat the top symbol in the energy definition cautiously: the board can look like an `E`, but the transcript and the internal logic of the derivation support standardizing it to \(T\) in the notes.
- Use `lecture_02_figure_05.png` as the stable source for the momentum rewrite, and typeset the finished progression \(F_i=m\,dv_i/dt\), \(F=d(mv)/dt\), and \(\vec F=d\vec P/dt\) as clean aligned equations.
- Treat `lecture_02_figure_04.png` as evidence of the transition, not as the source for a finished transcription; its value is narrative, not completeness.
- For `lecture_02_figure_06.png`, keep the original screenshot visible and place a TikZ redraw nearby that labels a few particles and equal-and-opposite forces such as \(\vec F_{12}=-\vec F_{21}\); use the transcript for exact pair notation rather than over-reading the pixels.
- Do not invent additional algebra from the central sketch in `lecture_02_figure_06.png`; the redraw should clarify the force-cancellation idea already present, not add a more elaborate many-body formalism than the frame actually shows.

## Uncertainties
- In `lecture_02_figure_02.png` and `lecture_02_figure_03.png`, the first symbol on the top line is ambiguous by sight and needs cautious normalization to \(T\).
- In `lecture_02_figure_02.png` and `lecture_02_figure_03.png`, the intermediate line with \(\frac{1}{2}m\sum_i v_i^2\) is cramped and not fully cleanly legible.
- In `lecture_02_figure_03.png`, the small annotation below the right-hand bracket is low-resolution; it plausibly reads as a force-minus-force cancellation, but the exact subscripts are not secure from the image alone.
- In `lecture_02_figure_04.png`, the lower line is unfinished and partly blocked by Susskind’s hand and body.
- In `lecture_02_figure_05.png`, the component indexing is readable in substance but should still be normalized using the transcript, especially where the transcript itself confuses `v` and `V`.
- In `lecture_02_figure_06.png`, the central force labels are too small and too overlapped by Susskind’s hand to support a pixel-perfect transcription.
- In `lecture_02_figure_06.png`, the small marks in the upper middle and upper right look like particle or point labels, but they are not legible enough to preserve exactly from the frame alone.