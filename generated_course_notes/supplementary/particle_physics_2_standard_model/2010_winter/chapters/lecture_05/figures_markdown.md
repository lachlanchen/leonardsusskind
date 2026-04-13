# Figure Notes
## Image Inventory

- `lecture_05_figure_02.png`: whiteboard close-up from the Maxwell-theory introduction. The top line shows the four-vector potential written as a time component together with a spatial vector part. Beneath it is a shorter line relating a force component to a derivative-like symbol acting on the potential, with a downward arrow pointing to `E`. Susskind stands at the left edge of the frame but does not block the main writing.
- `lecture_05_figure_03.png`: sparse whiteboard from the SU(3) representation discussion. On the right are two transformation lines: the first uses a matrix `U_{ij}` acting on a field with index `j` to produce a primed field; the second repeats the pattern with a starred matrix and starred field. On the left sits an isolated leftover `A_{ij}` from the adjacent gluon-field discussion.
- `lecture_05_figure_04.png`: weak-interaction decay sketch on the board. An incoming `\pi^-` line runs horizontally into a vertex labeled `W^-`, then splits into two outgoing lines. The pion line carries stacked quark labels inside it, and the two outgoing branches are labeled as a charged lepton and an antineutrino. Additional side notes from the surrounding discussion remain visible at the left and top of the board.

## Blackboard Equations

- `lecture_05_figure_02.png`: \(A_\mu = (A_0,\vec A_{1,2,3})\) [visible]
- `lecture_05_figure_02.png`: \(F_x = e\,\nabla A\) [partially visible]
- `lecture_05_figure_02.png`: \(\downarrow\,E\) [visible]
- `lecture_05_figure_02.png`: \(F_x = e\,\partial_x A_0\) [standard reconstruction]

- `lecture_05_figure_03.png`: \(A_{ij}\) [visible]
- `lecture_05_figure_03.png`: \(U_{ij}\,q_j \to q_i'\) [visible]
- `lecture_05_figure_03.png`: \(U_{ij}^{*}\,q_j^{*}\) [visible]
- `lecture_05_figure_03.png`: \(q_i^{\prime *}=U_{ij}^{*}q_j^{*}\) [standard reconstruction]

- `lecture_05_figure_04.png`: \(\pi^- \sim d\bar u\) [standard reconstruction]
- `lecture_05_figure_04.png`: \(W^-\) [visible]
- `lecture_05_figure_04.png`: \(\mu^-\) [partially visible]
- `lecture_05_figure_04.png`: \(\bar\nu_\mu\) [visible]
- `lecture_05_figure_04.png`: \(\pi^- \to W^- \to \mu^-+\bar\nu_\mu\) [standard reconstruction]

## Diagram And Layout Reading

- `lecture_05_figure_02.png` is organized vertically. The top line introduces the four-vector potential. The lower line is not a full derivation but a board checkpoint connecting derivative notation to the electric field, emphasized by the downward arrow to `E`. The frame is documentary evidence for notation and board rhythm rather than for a complete formula set.
- `lecture_05_figure_03.png` has a clean two-tier layout on the right: first the original representation, then directly underneath the complex-conjugate one. The left-side `A_{ij}` is spatially separated and should be read as residue from the neighboring gluon-field discussion, not part of the conjugation argument itself.
- `lecture_05_figure_04.png` is essentially a hand-drawn Feynman-style decay sketch with time running left to right. The incoming pion line carries quark-content labels inside the line itself. The central vertex is explicitly marked `W^-`. The outgoing branches separate the charged-lepton line from the antineutrino line, matching the lecture’s discussion of pion decay and of intermediate-state energy balance.

## TeX Reconstruction Plan

- `lecture_05_figure_02.png` should remain visible in the chapter. It is the main visual evidence for the lecture’s notation \(A_\mu\) and for the fact that Susskind is expressing the electromagnetic field in terms of derivatives of the vector potential. Nearby, the notes should typeset a cleaned displayed equation \(A_\mu=(A_0,\vec A)\). Any more explicit derivative relation should be given cautiously from transcript support rather than treated as fully legible board transcription.
- `lecture_05_figure_03.png` must remain visible. It cleanly documents the passage from the fundamental SU(3) action to the complex-conjugate action. The notes should pair it with a cleaned displayed pair such as \(q_i'=U_{ij}q_j\) and \(q_i^{\prime *}=U_{ij}^*q_j^*\). No TikZ redraw is needed.
- `lecture_05_figure_04.png` must remain visible and should also be redrawn nearby in TikZ. The screenshot preserves the lecture-room board layout and the hand-drawn decay topology, while the TikZ version should give a clean decay diagram for \(\pi^- \to W^- \to \mu^-+\bar\nu_\mu\). If the pion’s quark content is included, it should be added as a small annotation such as \(d\bar u\), clearly presented as the lecture’s particle-content reminder rather than as a separate algebraic derivation.

## Caption Drafts

- `lecture_05_figure_02.png`: Four-vector potential and derivative relation on the board.
- `lecture_05_figure_03.png`: Complex-conjugate SU(3) transformation rule.
- `lecture_05_figure_04.png`: Pion decay through an intermediate \(W^-\).

## Uncertainties

- In `lecture_05_figure_02.png`, the lower equation is not fully legible. The exact derivative symbol and the exact argument of the derivative are unclear on the board, and the frame does not itself cleanly display the magnetic-field curl relation mentioned in the subtitle window.
- In `lecture_05_figure_02.png`, the spatial part of the four-vector is written with an arrow and what appears to be `1,2,3`; for polished notes this should be normalized to the standard \(\vec A\) notation.
- In `lecture_05_figure_03.png`, the field symbol looks like \(q\), but the handwriting is loose enough that one should rely on transcript context before making a hard symbol-choice in the final prose.
- In `lecture_05_figure_03.png`, the second line visibly shows the starred matrix and starred field, but the final primed output is not written as explicitly as in the top line; that should be completed in the LaTeX reconstruction.
- In `lecture_05_figure_04.png`, the lower outgoing label \(\bar\nu_\mu\) is clearer than the upper outgoing label; the identification of the upper branch as \(\mu^-\) is supported by the lecture context.
- In `lecture_05_figure_04.png`, the side notes such as `12 minutes` and the faint note above the incoming pion line belong to the surrounding weak-decay discussion and should not be mistaken for part of the decay topology itself.