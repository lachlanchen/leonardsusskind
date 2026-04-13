# Figure Notes
## Image Inventory
- `lecture_06_figure_02.png`: whiteboard close-up from the propagator and dimensional-analysis discussion. At the top right the board reads `c = \hbar = 1`. Beneath it is a units relation written in bracket notation, and below that a separate line with `[p]`. To the right is a qualitative graph with a horizontal axis labeled `distance`, a black slowly falling curve, and a red curve that bends downward more sharply. The lecturer stands to the left of the key writing without covering it.
- `lecture_06_figure_03.png`: wider classroom shot showing both boards during the weak-interaction discussion. On the left board are two compact hand-drawn weak-process sketches with wavy lines and a visible `W^+` label. On the right board is a larger proton-centered reaction sketch with an oval interaction region, several labeled external lines, and a large `P`-type label near the top.
- `lecture_06_figure_04.png`: similar wide shot of the same weak-interaction board work, but now with a boxed fraction on the far right. The right board still contains the proton-centered diagram, while the boxed formula `g_w^2 / m_w^2` is clearly separated from it. A leftover `W^+` sketch remains cropped at the far left edge.
- `lecture_06_figure_06.png`: close-up of the tunneling analogy. At the far left edge only the end of an uncertainty-relation line remains visible. The main board content is a potential-energy curve with a left local minimum, a central barrier, a dashed horizontal level, and a descending right side. A small circled point sits in the left well, and the lecturer points to the matching point on the right slope.

## Blackboard Equations
- `lecture_06_figure_02.png`: \(c=\hbar=1\) [visible]
- `lecture_06_figure_02.png`: \([m]=[E]=[1/\text{length}]\) [visible]
- `lecture_06_figure_02.png`: \([p]\) [visible]
- `lecture_06_figure_02.png`: \([m]=[E]=[1/\text{length}]=[p]\) [standard reconstruction]

- `lecture_06_figure_03.png`: \(W^+\) [visible]
- `lecture_06_figure_03.png`: \(P_p\) [partially visible]
- `lecture_06_figure_03.png`: \(e\) [visible]
- `lecture_06_figure_03.png`: \(\bar{\nu}\) [partially visible]
- `lecture_06_figure_03.png`: \(d\) [visible]

- `lecture_06_figure_04.png`: \(\dfrac{g_w^2}{m_w^2}\) [visible]
- `lecture_06_figure_04.png`: \(e\) [visible]
- `lecture_06_figure_04.png`: \(\bar{\nu}\) [partially visible]
- `lecture_06_figure_04.png`: \(d\) [visible]
- `lecture_06_figure_04.png`: \(W^+\) [partially visible]

- `lecture_06_figure_06.png`: \(<\hbar\) [visible]
- `lecture_06_figure_06.png`: \(\Delta E\,\Delta t<\hbar\) [standard reconstruction]

## Diagram And Layout Reading
- `lecture_06_figure_02.png` is organized in two layers: a compact natural-units equation block at the upper right, and directly beneath it a qualitative distance plot. The horizontal axis is explicitly labeled `distance`. The black curve falls gradually with distance, while the red curve tracks it for a while and then drops much more steeply, matching the lecture’s contrast between massless-like power-law behavior and massive-particle exponential falloff.
- `lecture_06_figure_03.png` preserves the overall two-board layout of the weak-interaction discussion. The left board contains small branch-like weak sketches with wavy boson lines. The right board contains the more important documentary figure: a proton-centered hand-drawn reaction sketch with an oval interaction region, internal marked points, a dashed internal segment, and outgoing labeled lines. It is best read as board-layout evidence for the weak-process topology rather than as a fully legible standalone derivation.
- `lecture_06_figure_04.png` keeps the same reaction sketch but adds a cleanly separated formula block. The spatial separation matters: the boxed ratio is not part of the topology drawing but an estimate associated with it. This frame is therefore useful for pairing a typeset displayed equation with a nearby cleaned redraw of the reaction layout.
- `lecture_06_figure_06.png` is a classic potential-barrier sketch. The particle sits in the left well, a dashed horizontal line marks a common energy level, and the lecturer points to the corresponding point on the right slope where the potential energy matches the initial one. The barrier peak sits between them, so the board is visually encoding the tunneling comparison used for the virtual-\(W\) discussion.

## TeX Reconstruction Plan
- `lecture_06_figure_02.png` must remain visible. It should be paired with a clean displayed equation
  \[
  c=\hbar=1,
  \qquad
  [m]=[E]=[1/\text{length}]=[p].
  \]
  The graph should be redrawn nearby in TikZ as a qualitative propagator-versus-distance sketch, with the screenshot kept as evidence for the original board layout and color contrast between the two curves.
- `lecture_06_figure_03.png` should remain visible as documentary evidence of the weak-interaction board organization. The notes should not over-transcribe the ambiguous labels. If a clean figure is needed, redraw the right-hand reaction sketch in cautious TikZ, using the transcript to stabilize the particle content, while treating the left-hand `W^+` sketches as supporting layout rather than as the main mathematical figure.
- `lecture_06_figure_04.png` must remain visible. It should be paired with a clean displayed equation
  \[
  \frac{g_w^2}{m_W^2},
  \]
  where the typeset notes may normalize the board’s lowercase-looking \(w\) to the standard uppercase \(W\). If desired, the right-hand reaction sketch can be redrawn in TikZ nearby, but the screenshot should stay because it shows how Susskind juxtaposed the boxed estimate with the process picture.
- `lecture_06_figure_06.png` must remain visible. It should be paired with a clean displayed uncertainty relation
  \[
  \Delta E\,\Delta t<\hbar
  \]
  and with a TikZ redraw of the potential barrier, dashed equal-energy level, and corresponding right-hand point. The screenshot is important because it shows the board rhythm of the analogy and the exact location the lecturer indicates with his hand.

## Caption Drafts
- `lecture_06_figure_02.png`: Natural-units dimensional relations and propagator falloff.
- `lecture_06_figure_03.png`: Weak-interaction board sketches across both panels.
- `lecture_06_figure_04.png`: Weak-reaction estimate with boxed \(g_w^2/m_w^2\).
- `lecture_06_figure_06.png`: Potential barrier with equal-energy tunneling points.

## Uncertainties
- In `lecture_06_figure_02.png`, the inverse-length term is visually present but not written with perfectly standard typography; the transcript supports normalizing it to `length`. The left edge also contains leftover writing from neighboring material, including a partial \(g_w^2\), which should not be folded into the dimensional-analysis discussion.
- In `lecture_06_figure_03.png`, several labels in both diagrams are only partly legible. The large label near the top right looks like \(P_p\), but the exact subscript is uncertain. The neutrino label on the outgoing slanted line appears barred, but the bar is faint. The two vertical incoming lines on the right board likely carry \(u\)-type labels, though the frame alone does not make them fully secure.
- In `lecture_06_figure_04.png`, the boxed ratio is clear, but the case of the \(w/W\) symbols is not visually decisive; the polished notes should standardize this only cautiously. The left-edge `W^+` is residual neighboring board content, not part of the boxed estimate itself.
- In `lecture_06_figure_06.png`, only the tail end of the uncertainty relation is actually visible in the frame; the full \(\Delta E\,\Delta t<\hbar\) comes from transcript-supported completion. The vertical axis of the barrier diagram is not labeled in the image, so the notes should avoid pretending that the board itself explicitly names it, even though the lecture explains it verbally in terms of potential energy and the size of the effect.