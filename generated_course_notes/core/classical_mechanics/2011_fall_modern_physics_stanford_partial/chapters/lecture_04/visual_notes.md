# Visual Evidence

## Frame Inventory

- `lecture_04_figure_02.png`: Upper-left board view showing the polar-coordinate Lagrangian, a small polar-angle sketch labeled `\theta`, and the start of a derivative-with-respect-to-\(\dot q_i\) expression; this screenshot should remain in the final notes.
- `lecture_04_figure_03.png`: Mid-board notation view showing the canonical-momentum definition in progress and a lower line beginning `d\pi_i/dt =`; this screenshot should remain in the final notes.
- `lecture_04_figure_04.png`: Close board view showing `\delta A=0`, `A=\int \mathcal{L}\,dt`, a curved-path sketch on the left, and the beginning of a variation formula; this screenshot should remain in the final notes.
- `lecture_04_figure_05.png`: Wider board view preserving the same variational setup with the trajectory sketch, action formula, and a more extended variation expression across the board; this screenshot should remain in the final notes.

## Equation Extraction

- `lecture_04_figure_02.png`: \(\mathcal{L}=\dfrac{m}{2}\left(\dot r^{\,2}+r^{2}\dot\theta^{\,2}\right)-U(r)\) [visible]
- `lecture_04_figure_02.png`: \(\theta\) as the angle label in the small upper-left sketch [visible]
- `lecture_04_figure_02.png`: \(\dfrac{\partial \mathcal{L}}{\partial \dot q_i}\) [partially visible]
- `lecture_04_figure_02.png`: \(\pi_i=\dfrac{\partial \mathcal{L}}{\partial \dot q_i}\) [standard completion]

- `lecture_04_figure_03.png`: \(\dfrac{\partial \mathcal{L}}{\partial \dot q_i}\) [visible]
- `lecture_04_figure_03.png`: \(\pi_i\) [visible]
- `lecture_04_figure_03.png`: \(\pi_i=\dfrac{\partial \mathcal{L}}{\partial \dot q_i}\) [standard completion]
- `lecture_04_figure_03.png`: \(\dfrac{d\pi_i}{dt}=\) [visible]
- `lecture_04_figure_03.png`: \(\dfrac{d\pi_i}{dt}=\dfrac{\partial \mathcal{L}}{\partial q_i}\) [standard completion]

- `lecture_04_figure_04.png`: \(\delta A=0\) [visible]
- `lecture_04_figure_04.png`: \(A=\int \mathcal{L}\,dt\) [visible]
- `lecture_04_figure_04.png`: \(\delta A=\int \cdots\) [partially visible]
- `lecture_04_figure_04.png`: \(\delta A=\int \sum_i\left(\dfrac{\partial \mathcal{L}}{\partial q_i}\,\delta q_i+\dfrac{\partial \mathcal{L}}{\partial \dot q_i}\,\delta \dot q_i\right)dt\) [standard completion]

- `lecture_04_figure_05.png`: \(\delta A=0\) [visible]
- `lecture_04_figure_05.png`: \(A=\int \mathcal{L}\,dt\) [visible]
- `lecture_04_figure_05.png`: \(\delta A=\int \left(\dfrac{\partial \mathcal{L}}{\partial q_i}-\dfrac{d}{dt}\dfrac{\partial \mathcal{L}}{\partial \dot q_i}\right)\delta q_i\,dt+\cdots\) [partially visible]
- `lecture_04_figure_05.png`: \(\delta A=\int \left(\dfrac{\partial \mathcal{L}}{\partial q_i}-\dfrac{d}{dt}\left(\dfrac{\partial \mathcal{L}}{\partial \dot q_i}\right)\right)\delta q_i\,dt+\left[\dfrac{\partial \mathcal{L}}{\partial \dot q_i}\,\delta q_i\right]_{t_1}^{t_2}\) [standard completion]

## Diagram Extraction

- `lecture_04_figure_02.png`: Small polar-coordinate sketch with a radial line and angle marker `\theta`; it should be shown both as the original screenshot and as a small TikZ redraw.
- `lecture_04_figure_03.png`: No independent diagram, only board layout for notation; preserve as screenshot, with no separate TikZ figure needed.
- `lecture_04_figure_04.png`: Curved trajectory sketch with a nearby displaced path and short transverse strokes; it should be shown both ways, because the screenshot gives the original board context while TikZ can clarify the geometry.
- `lecture_04_figure_05.png`: Wider version of the same variational trajectory picture together with the action formulas; it should be shown both ways, especially if the final notes want a cleaner schematic of the classical path and nearby varied path.
- For the left-hand trajectory sketches in `lecture_04_figure_04.png` and `lecture_04_figure_05.png`, the interpretation “vertical direction is time, horizontal direction stands in for generalized coordinates” is transcript-backed rather than explicitly axis-labeled in the frame.

## Reconstruction Guidance

- Use `lecture_04_figure_02.png` as evidence for the concrete-to-general transition: the notes should typeset the full polar-coordinate Lagrangian cleanly, then typeset the canonical-momentum definition beside it, while keeping the screenshot to preserve the actual board sequence.
- Use `lecture_04_figure_03.png` to justify a clean displayed pair of equations, \(\pi_i=\partial \mathcal{L}/\partial \dot q_i\) and \(d\pi_i/dt=\partial \mathcal{L}/\partial q_i\); the board is a notation witness here, so the typeset equations should do most of the mathematical work.
- Use `lecture_04_figure_04.png` to anchor the moment where the action is restated as \(A=\int \mathcal{L}\,dt\) and the first-variation calculation begins. The lower line should be reconstructed cautiously in standard form, not overread from the chalk strokes.
- Use `lecture_04_figure_05.png` for the cleaner integrated-by-parts structure and overall board layout. In the final notes, pair it with a typeset endpoint-term formula and a qualitative TikZ redraw of the varied trajectory picture.
- When a diagram is redrawn, keep the screenshot nearby if the board layout itself matters to the lecture’s rhythm. Here that is true for `lecture_04_figure_02.png`, `lecture_04_figure_04.png`, and `lecture_04_figure_05.png`.
- Normalize notation in the notes even when the board is partial: use \(\mathcal{L}\) consistently for the Lagrangian, \(\pi_i\) for canonical momentum, and a clean endpoint notation such as \([\,\cdot\,]_{t_1}^{t_2}\).

## Uncertainties

- In `lecture_04_figure_02.png`, the denominator in the lower derivative is not fully secure from the frame alone, though \(\dot q_i\) is the natural and transcript-supported completion.
- In `lecture_04_figure_03.png`, the equality linking \(\pi_i\) to \(\partial \mathcal{L}/\partial \dot q_i\) is partly obscured by the lecturer’s body and is better treated as a standard completion than a direct chalk transcription.
- In `lecture_04_figure_03.png`, the right-hand side of `d\pi_i/dt =` is not legible in the frame itself.
- In `lecture_04_figure_04.png`, the lower variation formula is only partly present, so the sum over \(i\), the exact placement of parentheses, and the full integrand should not be claimed as directly visible.
- In `lecture_04_figure_05.png`, the endpoint contribution is visible in structure but not sharply enough to trust every bracket and index exactly.
- In `lecture_04_figure_04.png` and `lecture_04_figure_05.png`, the trajectory sketch is qualitative rather than metric; it should support the variational argument, not be treated as an exact geometric construction.