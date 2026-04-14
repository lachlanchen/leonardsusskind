# Figure Notes
## Image Inventory
- `lecture_09_figure_02.png`: Close crop of the left side of the board with Susskind turned toward the writing. The board shows a short vertical setup of definitions: a top line beginning `R =`, a second line beginning `V =`, and a lower line beginning with `\frac12 m`. The right-hand sides are partly blocked by the lecturer.
- `lecture_09_figure_03.png`: Tight board close-up centered on the key energy equation. Susskind points at the factor `G/R`. The left-hand side shows `\frac12 v^2`, and the right-hand side shows the enclosed-mass expression with `\frac{4\pi}{3}\rho R^3`.
- `lecture_09_figure_04.png`: Clean board close-up of the density discussion. At the top is a density formula with `\rho` expressed as mass over a cubic volume involving `\Delta x` and `a`. Beneath it is a present-day normalization of the form `\rho_{\text{today}} = C / a_{\text{today}}^3`, and at lower left Susskind has begun the next `\rho` line.
- `lecture_09_figure_05.png`: Medium shot of Susskind gesturing in front of the board. A boxed earlier energy equation remains visible at the top, while a lower line beneath it contains a Hubble-form relation with `\frac12 H^2` on the left and a density term involving `G\rho` on the right. The figure is useful mainly for the juxtaposition of the original boxed equation and its cosmological reformulation.

## Blackboard Equations
- `lecture_09_figure_02.png`: \(R = x a\) [partially visible]
- `lecture_09_figure_02.png`: \(V = x\dot a\) [standard reconstruction]
- `lecture_09_figure_02.png`: \(\tfrac12 m v^2\) [partially visible]
- `lecture_09_figure_02.png`: \(E=\tfrac12 m v^2-\dfrac{GMm}{R}\) [standard reconstruction]

- `lecture_09_figure_03.png`: \(\tfrac12 v^2 = \dfrac{G}{R}\,\dfrac{4\pi}{3}\rho R^3\) [visible]
- `lecture_09_figure_03.png`: \(\dfrac{4\pi}{3}\rho R^3\) [visible]

- `lecture_09_figure_04.png`: \(\rho = \dfrac{M}{(\Delta x\, a)^3}\) [visible]
- `lecture_09_figure_04.png`: \(\rho_{\text{today}} = \dfrac{C}{a_{\text{today}}^3}\) [partially visible]
- `lecture_09_figure_04.png`: \(\rho(t)=\dfrac{C}{a^3(t)}\) [standard reconstruction]
- `lecture_09_figure_04.png`: \(\dfrac{\rho(t)}{\rho_{\text{today}}}=\dfrac{a_{\text{today}}^3}{a^3(t)}\) [standard reconstruction]

- `lecture_09_figure_05.png`: \(\tfrac12 v^2 = \dfrac{G}{R}\,\dfrac{4\pi}{3}\rho R^3\) [partially visible]
- `lecture_09_figure_05.png`: \(\tfrac12 H^2 = \cdots\, G\rho\) [partially visible]
- `lecture_09_figure_05.png`: \(\tfrac12 H^2 = \dfrac{4\pi G}{3}\rho\) [standard reconstruction]
- `lecture_09_figure_05.png`: \(H^2=\dfrac{8\pi G}{3}\rho\) [standard reconstruction]

## Diagram And Layout Reading
- `lecture_09_figure_02.png` is not a diagram in the geometric sense, but it preserves the board rhythm of the setup: first define radius, then velocity, then begin the kinetic-energy term. It is a left-column derivation layout rather than a finished equation.
- `lecture_09_figure_03.png` is organized as a single-line identity. The left side is the kinetic term, the right side is the gravitational factor times the enclosed mass. Susskind’s pointing finger marks the `G/R` factor, which helps show how he is verbally unpacking the equation.
- `lecture_09_figure_04.png` is vertically organized in three steps: a general density formula at top, a present-day normalization in the middle, and the beginning of the time-dependent version at the bottom. That stacked layout is pedagogically useful because it shows the move from raw volume scaling to cosmological dilution as \(a^{-3}\).
- `lecture_09_figure_05.png` preserves a two-level board structure. The upper level is the boxed escape-velocity or zero-energy equation from the Newtonian derivation. The lower level is the simplified cosmological relation in terms of \(H\) and \(\rho\). The main value of the image is this transition from the original energy equation to the Hubble-form statement.

## TeX Reconstruction Plan
- `lecture_09_figure_02.png` should remain visible if the notes keep the step-by-step Newtonian setup. Nearby, the notes should typeset the cleaned definitions \(R=xa\) and \(v=x\dot a\), followed by the total-energy expression \(E=\tfrac12 mv^2-\dfrac{GMm}{R}\). The screenshot is mainly evidence for board order and setup, not for exact legibility.
- `lecture_09_figure_03.png` should remain visible and should be paired with a clean displayed equation
  \[
  \frac12 v^2=\frac{G}{R}\left(\frac{4\pi}{3}\rho R^3\right).
  \]
  No TikZ is needed; the board image is already the right kind of evidence.
- `lecture_09_figure_04.png` should remain visible and should be paired with the cleaned density-scaling formulas
  \[
  \rho=\frac{M}{(\Delta x\,a)^3},\qquad
  \rho(t)=\frac{C}{a^3(t)},\qquad
  \frac{\rho(t)}{\rho_{\text{today}}}=\frac{a_{\text{today}}^3}{a^3(t)}.
  \]
  The screenshot is valuable because it preserves the stacked board logic from raw dilution to normalization.
- `lecture_09_figure_05.png` should remain visible specifically as evidence for the pedagogical transition from the boxed energy equation to the Hubble-density form. Nearby, the notes should typeset the cleaned relation
  \[
  H^2=\frac{8\pi G}{3}\rho,
  \]
  and, if useful for the intermediate step,
  \[
  \frac12 H^2=\frac{4\pi G}{3}\rho.
  \]
  No TikZ is needed; the important thing is the board juxtaposition, not a geometric sketch.

## Caption Drafts
- `lecture_09_figure_02.png`: Radius, velocity, and energy setup on the board
- `lecture_09_figure_03.png`: Energy equation with the enclosed mass term
- `lecture_09_figure_04.png`: Matter density scaling as the universe expands
- `lecture_09_figure_05.png`: Boxed energy equation and its Hubble-form rewriting

## Uncertainties
- In `lecture_09_figure_02.png`, the right-hand sides of the `R =` and `V =` lines are partly hidden by Susskind, and the lower kinetic-energy line is only started. The full expressions should be normalized from the transcript rather than claimed from the frame alone.
- In `lecture_09_figure_03.png`, the board writes the right-hand side as a product rather than a carefully parenthesized mass factor. The grouped form \(\left(\frac{4\pi}{3}\rho R^3\right)\) is mathematically the intended reading, but the parentheses are a reconstruction.
- In `lecture_09_figure_04.png`, the handwritten `\text{today}` labels under \(\rho\) and \(a\) are small and somewhat rough. The lower time-dependent \(\rho\) line has only just begun, so \(\rho(t)=C/a^3(t)\) is a transcript-supported completion.
- In `lecture_09_figure_05.png`, the lower equation is partly blocked by the lecturer, and the exact numerical coefficient between \(\frac12 H^2\) and \(G\rho\) is not fully secure from the image alone. The normalized coefficient should come from the transcript derivation.
- In `lecture_09_figure_05.png`, the frame is more valuable for the board layout than for symbol-by-symbol transcription of the lower line. The upper boxed equation is clearer than the lower reformulated one.