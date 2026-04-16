# Figure Notes
## Image Inventory
- `lecture_06_figure_04.png`: The upper board line gives the total energy as a sum of kinetic terms plus a sum of pairwise potentials, with the pair term written as $U(|x_n-x_m|)$. The lower line begins the partition function with $Z=$, an integral over $dp\,dx$, an $N!$ beneath the measure, and an exponential containing the kinetic factor $-\beta p^2/2M$.
- `lecture_06_figure_05.png`: The upper board line shows a two-particle coordinate integral of the pair potential, beginning $\int d^3x_1\,d^3x_2\,U(|x_1-x_2|)=VU\ldots$, with the right edge cropped. The lower line recalls the Gaussian momentum factor as a square-root expression involving $2\pi m/\beta$ raised to the power $3N$.

## Blackboard Equations
- `lecture_06_figure_04.png` [visible]: $E=\sum_n \frac{p^2}{2M}+\sum_{n>m}U\!\left(|x_n-x_m|\right)$
- `lecture_06_figure_04.png` [visible]: $Z=\frac{1}{N!}\int dp\,dx\,e^{-\beta p^2/(2M)}$
- `lecture_06_figure_04.png` [standard reconstruction]: $E=\sum_n \frac{p_n^2}{2M}+\sum_{n>m}U\!\left(|x_n-x_m|\right)$
- `lecture_06_figure_04.png` [standard reconstruction]: $Z=\frac{1}{N!}\int dp\,dx\,e^{-\beta \sum_n p_n^2/(2M)}\,e^{-\beta U(X)}$
- `lecture_06_figure_05.png` [partially visible]: $\int d^3x_1\,d^3x_2\,U\!\left(|x_1-x_2|\right)=VU\ldots$
- `lecture_06_figure_05.png` [standard reconstruction]: $\int d^3x_1\,d^3x_2\,U\!\left(|x_1-x_2|\right)=V\,U_0$
- `lecture_06_figure_05.png` [visible]: $\left(\sqrt{\frac{2\pi m}{\beta}}\right)^{3N}$
- `lecture_06_figure_05.png` [standard reconstruction]: $\left(\frac{2\pi m}{\beta}\right)^{3N/2}$

## Diagram And Layout Reading
- `lecture_06_figure_04.png`: The board is arranged in two stacked derivation lines. The top line is the Hamiltonian-style energy decomposition. The lower line starts the partition-function derivation, with the measure and $N!$ grouped visually on the left and the exponential written as a separate factor on the right.
- `lecture_06_figure_05.png`: The board again has two separated displayed lines. The upper line recalls the coordinate-space pair-potential integral; the lower line recalls the Gaussian momentum result from the ideal-gas case. The spacing between them visually reinforces the factorization into position and momentum pieces.
- Neither image contains axes, arrows, particle sketches, or geometric diagrams. Their value is entirely in equation placement and board organization.

## TeX Reconstruction Plan
- Keep `lecture_06_figure_04.png` visible. It documents the transition from the many-particle energy formula to the partition-function setup, and that staging is useful evidence for the notes.
- Next to `lecture_06_figure_04.png`, reconstruct the energy formula as a clean displayed equation with explicit indexed momentum $p_n^2$. Reconstruct the full factorized Boltzmann weight only as a transcript-supported completion, not as a literal board transcription.
- Keep `lecture_06_figure_05.png` visible. It is a useful board snapshot because it places the recalled pair-potential integral and the Gaussian momentum factor on the same board.
- Next to `lecture_06_figure_05.png`, reconstruct the upper relation as $\int d^3x_1\,d^3x_2\,U(|x_1-x_2|)=V U_0$ and the lower Gaussian factor as $\left(2\pi m/\beta\right)^{3N/2}$.
- No TikZ redraw is needed for either asset. These should be treated as screenshot-plus-equation figures.

## Caption Drafts
- `lecture_06_figure_04.png`: Total energy split into kinetic and pair-potential terms, with the partition function begun below.
- `lecture_06_figure_05.png`: Recalled ingredients for the factorized partition function: the pair-potential integral and the Gaussian momentum factor.

## Uncertainties
- In `lecture_06_figure_04.png`, the board appears to write $p^2$ inside the sum rather than $p_n^2$; the indexed form is the likely intended mathematical completion.
- In `lecture_06_figure_04.png`, only the kinetic exponential is visibly present. The potential-energy factor is motivated by the transcript but is not legible in this frame.
- In `lecture_06_figure_05.png`, the right-hand side of the upper equation is cropped after `VU...`; the intended completion is very likely $V U_0$.
- In `lecture_06_figure_05.png`, the mass symbol is lowercase $m$, while `lecture_06_figure_04.png` uses uppercase $M$ in the kinetic term; this looks like board-level notation drift.
- The exponent in `lecture_06_figure_05.png` looks like $3N$ on the board, while the spoken transcript says “3n.” The chapter should normalize particle-count notation consistently.