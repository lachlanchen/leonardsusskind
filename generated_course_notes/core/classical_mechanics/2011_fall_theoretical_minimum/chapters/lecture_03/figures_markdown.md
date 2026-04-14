# Figure Notes
## Image Inventory
- `lecture_03_figure_02.png`: Susskind stands at the board beside a clean one-dimensional equilibrium condition. The board shows a large derivative equation `dV(x)/dx = 0`, with a large blank area below where he is about to draw the graph of the potential.
- `lecture_03_figure_03.png`: The board contains a large smooth U-shaped curve with a marked point at each end, and a long shallow line drawn beneath it. Susskind points near the left side of the upper curve. Visually this reads as a hanging-chain or stationary-curve sketch rather than a symbolic equation board.
- `lecture_03_figure_04.png`: The right side of the board shows a partially cropped derivation involving derivatives of the Lagrangian. The upper visible term is a derivative with respect to `x_i`; beneath it is another line involving a derivative with respect to a velocity-like variable. Susskind is turned toward the audience, leaving the key symbols relatively unobstructed.
- `lecture_03_figure_05.png`: This is the clearest summary board of the lecture’s Newton-to-Lagrange comparison. At upper left is the potential-energy label with `V(x_i)`, below it the kinetic-energy sum, in the center a large `L = ... - V(x)`, and below that a component force law equating `m\ddot x_i` with `-\partial V/\partial x_i` and `F_i`.

## Blackboard Equations
- `lecture_03_figure_02.png`: `\frac{dV(x)}{dx}=0` [visible]

- `lecture_03_figure_03.png`: no explicit equation is legible [visible]
- `lecture_03_figure_03.png`: a stationary suspended curve between two fixed endpoints [standard reconstruction]

- `lecture_03_figure_04.png`: `\frac{\partial L}{\partial x_i}` [visible]
- `lecture_03_figure_04.png`: `\frac{1}{\epsilon}\frac{\partial L}{\partial v_i}` [partially visible]
- `lecture_03_figure_04.png`: `-\frac{d}{dt}\!\left(\frac{\partial L}{\partial \dot x}\right)+\frac{\partial L}{\partial x}` [standard reconstruction]
- `lecture_03_figure_04.png`: `\frac{d}{dt}\!\left(\frac{\partial L}{\partial \dot x}\right)=\frac{\partial L}{\partial x}` [standard reconstruction]

- `lecture_03_figure_05.png`: `V(x_i)` [visible]
- `lecture_03_figure_05.png`: `\sum_i \frac{m}{2}\dot x_i^2` [partially visible]
- `lecture_03_figure_05.png`: `L=\frac{m\dot x^2}{2}-V(x)` [visible]
- `lecture_03_figure_05.png`: `m\ddot x_i=-\frac{\partial V}{\partial x_i}=F_i(x)` [partially visible]
- `lecture_03_figure_05.png`: `L=T-V` [standard reconstruction]

## Diagram And Layout Reading
- `lecture_03_figure_02.png` is a setup frame. Its value is not only the equation itself but the board layout: the equilibrium condition is written high and large, with open space beneath it where the forthcoming graph of the potential will be drawn. That spatial organization supports the lecture’s move from derivative condition to geometric picture.
- `lecture_03_figure_03.png` is the only purely diagrammatic figure in this set. The upper curve is smooth, U-shaped, and fixed at two endpoints marked by dots. The long lower line beneath it is not clearly labeled; it may be a baseline or an earlier guide line rather than a true axis. The lecturer’s pointing gesture emphasizes the slope or local shape on the left side of the curve.
- `lecture_03_figure_04.png` is a derivation-layout frame. The board is organized vertically: an upper term for the derivative of the Lagrangian with respect to position, and a lower velocity-derivative term beneath it. The screenshot is useful less because every symbol is perfectly legible than because it documents the board’s structure at the moment the Euler-Lagrange ingredients are being separated.
- `lecture_03_figure_05.png` is a summary board. The left side defines the energy ingredients, the center states the Lagrangian as kinetic minus potential, and the lower line connects the potential derivative back to the Newtonian force law. This is the most pedagogically complete layout of the set, because it puts `PE`, `KE`, `L`, and the force equation into one visible board state.

## TeX Reconstruction Plan
- `lecture_03_figure_02.png` should remain visible. Pair it with a clean displayed equation
  \[
  \frac{dV(x)}{dx}=0
  \]
  and let the prose explain that the graph comes next. No TikZ redraw is needed from this frame alone.
- `lecture_03_figure_03.png` should remain visible. The screenshot should be paired with a small TikZ redraw of the suspended stationary curve between two fixed endpoints. The redraw should stay schematic: a smooth U-shaped curve with endpoint markers is enough. Do not force an axis or over-interpret the lower line unless later frames confirm its meaning.
- `lecture_03_figure_04.png` should remain visible as documentary evidence for the Euler-Lagrange derivation board. The actual mathematics in the notes should be carried by clean typeset equations nearby, preferably the finished Euler-Lagrange form rather than a literal transcription of every cropped intermediate term.
- `lecture_03_figure_05.png` should remain visible and should be paired with clean displayed formulas for the kinetic energy, the potential energy, the Lagrangian,
  \[
  L=T-V,
  \]
  and the component force law
  \[
  m\ddot x_i=-\frac{\partial V}{\partial x_i}=F_i.
  \]
  The screenshot is valuable because it preserves the lecture’s summary layout, not because the board notation is cleaner than typeset LaTeX.

## Caption Drafts
- `lecture_03_figure_02.png`: Stationary point condition for the potential
- `lecture_03_figure_03.png`: Suspended stationary curve between fixed endpoints
- `lecture_03_figure_04.png`: Derivative terms in the Euler-Lagrange construction
- `lecture_03_figure_05.png`: Lagrangian as kinetic minus potential energy

## Uncertainties
- In `lecture_03_figure_02.png`, the notation is clear, but it captures the setup just before the graph is drawn rather than the graph itself.
- In `lecture_03_figure_03.png`, the long lower line under the U-shaped curve is not clearly identified from the image alone. It may be a baseline, a guide line, or leftover board geometry rather than a labeled axis.
- In `lecture_03_figure_03.png`, the curve is clearly U-shaped and endpoint-fixed, but whether it should be interpreted as a literal chain profile, an abstract stationary curve, or a generalized “potential” sketch should be stated cautiously in the notes.
- In `lecture_03_figure_04.png`, the upper `\partial L/\partial x_i` term is readable, but the surrounding factors and the exact neighboring velocity-derivative terms are cropped or faint. This frame supports the derivation structure more reliably than it supports a complete literal transcription.
- In `lecture_03_figure_05.png`, the board mixes one-dimensional notation in the large central `L` formula with multi-index notation in the surrounding `V(x_i)` and `m\ddot x_i` lines. The notes should normalize this carefully rather than reproducing the mixed board notation mechanically.
- In `lecture_03_figure_05.png`, the left-side `KE` expression is only partly visible, so the sum notation should be restored from cautious standard completion rather than from the screenshot alone.