# Figure Notes
## Image Inventory
- `lecture_08_figure_02.png`: Susskind stands with his back to the board while beginning a Feynman-style sketch. At the top center there is a horizontal line labeled `P`. On the far left, a leftover baryon-number expression remains from the previous discussion.
- `lecture_08_figure_03.png`: Susskind is writing a new line beginning `C = ...` beneath a clearly visible baryon-number formula at the top. The upper formula is complete enough to read; the lower line is mid-word and records the introduction of charge conjugation notation.
- `lecture_08_figure_04.png`: Susskind is writing at the upper left of the board. A partial Schrödinger-equation fragment is visible, while on the right there is a large circular or oval sketch containing several directed paths connecting a left junction to a right junction.
- `lecture_08_figure_06.png`: Susskind stands in front of a clear force-potential relation board. The notation `V(\phi)` appears above `F = -\,dV/d\phi`. On the far left there is a simple contextual sketch: a circled point above a downward arrow.

## Blackboard Equations
- `lecture_08_figure_02.png`: `P` [visible]
- `lecture_08_figure_02.png`: `\dfrac{N_q - N_{\bar q}}{3}` [partially visible]
- `lecture_08_figure_02.png`: `p \to e^+ + \gamma` [standard reconstruction]

- `lecture_08_figure_03.png`: `B = \dfrac{N_q - N_{\bar q}}{3}` [visible]
- `lecture_08_figure_03.png`: `C = \text{charge conjugation symmetry}` [standard reconstruction]
- `lecture_08_figure_03.png`: `C = \text{Ch}\cdots` [partially visible]

- `lecture_08_figure_04.png`: `i\,\dfrac{\partial \psi}{\partial t}` [partially visible]
- `lecture_08_figure_04.png`: `i\,\dfrac{\partial \psi}{\partial t} = \cdots` [standard reconstruction]

- `lecture_08_figure_06.png`: `V(\phi)` [visible]
- `lecture_08_figure_06.png`: `F = -\,\dfrac{dV}{d\phi}` [visible]

## Diagram And Layout Reading
- `lecture_08_figure_02.png` is mainly valuable for board sequencing. The new diagram starts at the top center with a labeled incoming proton line, while the left side preserves the tail end of the baryon-number discussion. The decay branches themselves are not yet on the board.
- `lecture_08_figure_03.png` has a clean two-level layout: the upper line gives the baryon-number definition, and the middle line begins the new symmetry notation. This is a strong board snapshot for the transition from baryon-number conservation to discrete symmetries.
- `lecture_08_figure_04.png` has a split visual structure. The upper-left writing records the time-reversal discussion through the Schrödinger-equation cue, while the right side carries a large closed multi-path sketch with arrows. The right-hand drawing looks more like a contextual board sketch than a finished, caption-ready standalone diagram.
- `lecture_08_figure_06.png` is the cleanest equation board of the set. The main mathematical payload is centered in the force-potential pair, while the left-side circled-point-and-arrow sketch gives the falling-stone intuition that motivates the later friction analogy.

## TeX Reconstruction Plan
- `lecture_08_figure_02.png` must remain visible. It should be paired with a clean TikZ redraw of the proton-decay schematic, using the transcript-backed process `p \to e^+ + \gamma`. The screenshot should be treated as evidence for the board layout and the initial incoming `P` line, not as the full source of the final decay diagram.
- `lecture_08_figure_03.png` must remain visible. Near it, include a clean displayed reconstruction of the baryon-number formula and a prose or displayed line introducing `C` as charge conjugation symmetry. This figure is better preserved as a screenshot plus cleaned equation than replaced by TikZ.
- `lecture_08_figure_04.png` must remain visible. Pair it with a clean displayed reconstruction of the time-reversal cue `i\,\partial_t\psi = \cdots`. If the right-hand circular multi-path sketch is used pedagogically, redraw it only as a schematic TikZ context figure nearby, not as a definitive transcription of the board.
- `lecture_08_figure_06.png` must remain visible. Pair it with the clean displayed equations
  `V(\phi)` and `F = -\,dV/d\phi`.
  The left-side falling-object sketch can remain screenshot-only unless the chapter wants a small pedagogical redraw of the stone-in-potential analogy.

## Caption Drafts
- `lecture_08_figure_02.png`: Opening line of the proton-decay sketch.
- `lecture_08_figure_03.png`: Baryon number and charge-conjugation notation.
- `lecture_08_figure_04.png`: Time-reversal equation cue and loop sketch.
- `lecture_08_figure_06.png`: Potential and force for the falling-stone analogy.

## Uncertainties
- In `lecture_08_figure_02.png`, the leftover baryon-number formula is only partial, and the handwritten subscript is easier to confirm from `lecture_08_figure_03.png` than from this frame alone.
- In `lecture_08_figure_02.png`, the actual decay branches are not yet present; the full process `p \to e^+ + \gamma` comes from the transcript, not from this frame by itself.
- In `lecture_08_figure_03.png`, the word after `C =` is incomplete on the board. The full phrase `charge conjugation symmetry` is transcript-backed rather than fully visible.
- In `lecture_08_figure_04.png`, the equation is heavily occluded by Susskind’s head and writing hand; only the left portion is really visible. The denominator and the unfinished right-hand side require cautious standard completion from the transcript.
- In `lecture_08_figure_04.png`, the meaning of the large circular arrow sketch is not fully recoverable from the image alone. It should not be overinterpreted without nearby lecture context.
- In `lecture_08_figure_06.png`, the field symbol is handwritten in a way that could be read as either `\phi` or `\varphi`, though the transcript supports `\phi`.
- In `lecture_08_figure_06.png`, the simple left-side sketch is unlabeled and should be treated as contextual intuition rather than a source for precise mathematical notation.