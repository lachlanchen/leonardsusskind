# Figure Notes
## Image Inventory
- `lecture_02_figure_02.png` shows the left portion of the lower board at the moment Susskind identifies the average-energy equation. The visible board content is almost entirely algebraic: a top energy label, the normalization condition, and the expectation-value formula for energy. Susskind stands at the far right, leaving the equations mostly unobstructed, while the rest of the board is blank.
- `lecture_02_figure_03.png` shows a much fuller board layout spanning the upper and lower sliding boards. On the upper board there is a residual entropy sketch and the entropy formula with a Carnot-related factor. On the lower left there is a sketched box labeled by a state index and nearby expectation-value equations. On the lower right there is a freshly drawn set of axes labeled `\(P(i,E)\)`, with the horizontal axis ending at a small `\(i\)`.
- `lecture_02_figure_04.png` shows the same board after the right-hand graph has been developed. The upper entropy formula remains visible, the lower-left expectation-value notation is still partly readable, and the lower-right axes labeled `\(P(i,E)\)` now carry several smooth probability curves spread across the horizontal axis, with the axis label near the right appearing as `\(E(i)\)`.

## Blackboard Equations
- `lecture_02_figure_02.png`: [partially visible] `E_i`
- `lecture_02_figure_02.png`: [visible] `\sum_i P(i)=1`
- `lecture_02_figure_02.png`: [visible] `\sum_i P(i)E(i)=\langle E\rangle`

- `lecture_02_figure_03.png`: [partially visible] `S=-\sum_i p_i\log p_i=\frac{1}{k_B}S_{\mathrm{Carnot}}`
- `lecture_02_figure_03.png`: [partially visible] `E_i`
- `lecture_02_figure_03.png`: [partially visible] `\sum_i P(i)=1`
- `lecture_02_figure_03.png`: [partially visible] `\sum_i P(i)E(i)=\langle E\rangle`
- `lecture_02_figure_03.png`: [visible] `P(i,E)`
- `lecture_02_figure_03.png`: [visible] `i`

- `lecture_02_figure_04.png`: [partially visible] `S=-\sum_i p_i\log p_i=\frac{1}{k_B}S_{\mathrm{Carnot}}`
- `lecture_02_figure_04.png`: [partially visible] `\sum_i P(i,E)=1`
- `lecture_02_figure_04.png`: [partially visible] `\sum_i P(i)E(i)=\langle E\rangle`
- `lecture_02_figure_04.png`: [visible] `P(i,E)`
- `lecture_02_figure_04.png`: [partially visible] `E(i)`

## Diagram And Layout Reading
- `lecture_02_figure_02.png` is a pure equation board. The content is arranged vertically: first the energy label, then the normalization of probabilities, then the weighted average giving the mean energy. The right half of the frame is visually empty except for the lecturer, which makes the left-hand equations easy to isolate in the notes.
- `lecture_02_figure_03.png` has a meaningful multi-zone board layout. The upper board retains old entropy material, which situates the discussion in the larger theme of probability and entropy. The lower left board collects the state-space setup: a rectangular box with an interior `\(i\)` and scattered dots around it, alongside the normalization and average-energy equations. The lower right board starts a new schematic graph with vertical and horizontal axes and the label `\(P(i,E)\)`. This is the transition point where the lecture moves from abstract formulas to a visual family of probability distributions.
- `lecture_02_figure_04.png` is the developed version of the previous board. The same right-hand graph now contains several overlapping smooth curves with different widths and peak positions. They are not data plots; they are schematic distributions. The horizontal axis label shifts from the earlier discrete-state reading toward an energy reading, with `\(E(i)\)` written near the right end. The layout makes the lecture’s point graphically: different probability distributions correspond to different average energies.
- Across `lecture_02_figure_03.png` and `lecture_02_figure_04.png`, the board organization itself matters. The left side holds definitions and constraints, while the right side translates those constraints into a one-parameter family of distributions. That staged progression is worth preserving in the notes.

## TeX Reconstruction Plan
- `lecture_02_figure_02.png` should remain visible in the notes. It is the cleanest documentary evidence for the two key equations
  `\sum_i P(i)=1`
  and
  `\sum_i P(i)E(i)=\langle E\rangle`.
  Nearby TeX should typeset those equations cleanly as displayed mathematics. No TikZ redraw is necessary for this frame.
- `lecture_02_figure_03.png` should remain visible. It captures the transition from equations to a graph labeled `\(P(i,E)\)`, and the board layout is part of the lecture logic. It should be paired with:
  - displayed equations for normalization and average energy
  - a restrained TikZ redraw of the fresh axes labeled `\(P(i,E)\)` with the horizontal axis labeled either by `\(i\)` or, if the prose needs the later interpretation, by the energy of the `\(i\)`-th state
- `lecture_02_figure_04.png` should remain visible. It is the best documentary image for the family of distributions. It should be paired with a clean TikZ redraw showing several normalized-looking smooth curves over a shared horizontal axis labeled by energy, together with prose explaining that shifting weight to the right corresponds to larger average energy.
- The same TikZ style can be shared between `lecture_02_figure_03.png` and `lecture_02_figure_04.png`: the earlier figure can use the bare axes or a minimal setup, while the later figure can use the completed family of curves.
- The upper-board entropy formula visible in `lecture_02_figure_03.png` and `lecture_02_figure_04.png` need not drive the local exposition, but it is useful contextual evidence. If the chapter discusses the connection to entropy nearby, it can be typeset cleanly; otherwise the screenshots can simply preserve it as background board context.

## Caption Drafts
- `lecture_02_figure_02.png`: Normalization and average energy
- `lecture_02_figure_03.png`: Setting up the probability distribution \(P(i,E)\)
- `lecture_02_figure_04.png`: Family of probability distributions at different average energies

## Uncertainties
- In `lecture_02_figure_02.png`, the top energy label looks like `\(E_i\)`, but the punctuation or trailing mark is not completely sharp.
- In `lecture_02_figure_03.png` and `lecture_02_figure_04.png`, the upper entropy formula is readable in structure but not pixel-perfect in every symbol; the rightmost `\(S_{\mathrm{Carnot}}\)` identification is best treated as partially visible rather than exact transcription from the frame alone.
- In `lecture_02_figure_03.png`, the lower-left equations are partially occluded by Susskind’s body, so their full clean forms should come from cautious standard completion supported by the transcript.
- In `lecture_02_figure_03.png`, the right-hand horizontal axis ends with a small `\(i\)`, but the lecture immediately says the axis could also be read as plotting the energy of the `\(i\)`-th state; the notes should make that interpretive shift in prose rather than pretending the pixels alone settle it.
- In `lecture_02_figure_04.png`, the label near the right end of the horizontal axis looks like `\(E(i)\)`, but it is not maximally sharp.
- In both `lecture_02_figure_03.png` and `lecture_02_figure_04.png`, the small upper-left sketch and its label above the entropy formula are not fully legible and should not be overinterpreted.