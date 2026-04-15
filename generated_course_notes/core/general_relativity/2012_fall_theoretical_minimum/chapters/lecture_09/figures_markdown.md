# Figure Notes
## Image Inventory
- `lecture_09_figure_02.png` shows a partially written matrix-style energy-momentum tensor on the left half of the board, with visible entries including \(T^{00}\), \(T^{10}\), \(T^{11}\), \(T^{01}\), \(T^{02}\), and \(T^{03}\). A large partial conservation equation ending in \(=0\) appears at upper right. The lecturer blocks some middle and lower entries. A small `c=1` note is visible near the top.
- `lecture_09_figure_03.png` shows a clean three-line comparison of candidate left-hand sides for Einstein’s equation: a top line with \(G^{\mu\nu}\), then \(R^{\mu\nu}\), then \(g^{\mu\nu}R\), all aligned against the same \(8\pi G\,T^{\mu\nu}\) right-hand side. The lower two lines carry question marks.
- `lecture_09_figure_04.png` shows a long product-rule expansion stretched across the board for the covariant derivative of \(g^{\mu\nu}R\). The lecturer partly blocks the left side, but the middle term \((D_\mu g^{\mu\nu})R\) and the right term \(g^{\mu\nu}(D_\mu R)\) are visible.
- `lecture_09_figure_05.png` shows three related equations: a top rearranged Ricci-tensor form of Einstein’s equation, a middle partially cropped standard Einstein equation, and a bottom trace relation \(R=-8\pi G\,T\). The board is readable enough to preserve the algebraic progression.

## Blackboard Equations
- `lecture_09_figure_02.png`: \(T^{00},\;T^{10},\;T^{11},\;T^{01},\;T^{02},\;T^{03}\) [visible]
- `lecture_09_figure_02.png`: \(\dfrac{D T^{\nu\mu}}{D x^\mu}=0\) [partially visible]
- `lecture_09_figure_02.png`: \(D_\mu T^{\nu\mu}=0\) [standard reconstruction]
- `lecture_09_figure_02.png`: \(T^{\mu\nu}=\begin{pmatrix}T^{00}&T^{01}&T^{02}&T^{03}\\ T^{10}&T^{11}&T^{12}&T^{13}\\ T^{20}&T^{21}&T^{22}&T^{23}\\ T^{30}&T^{31}&T^{32}&T^{33}\end{pmatrix}\) [standard reconstruction]

- `lecture_09_figure_03.png`: \(G^{\mu\nu}=8\pi G\,T^{\mu\nu}\) [visible]
- `lecture_09_figure_03.png`: \(R^{\mu\nu}\stackrel{?}{=}8\pi G\,T^{\mu\nu}\) [visible]
- `lecture_09_figure_03.png`: \(g^{\mu\nu}R\stackrel{?}{=}8\pi G\,T^{\mu\nu}\) [visible]

- `lecture_09_figure_04.png`: \(D_\mu\!\left(g^{\mu\nu}R\right)=\left(D_\mu g^{\mu\nu}\right)R+g^{\mu\nu}\left(D_\mu R\right)\) [partially visible]
- `lecture_09_figure_04.png`: \(D_\mu g^{\mu\nu}=0\) [standard reconstruction]

- `lecture_09_figure_05.png`: \(R_{\mu\nu}=8\pi G\left(T_{\mu\nu}-\frac12 g_{\mu\nu}T\right)\) [visible]
- `lecture_09_figure_05.png`: \(R_{\mu\nu}-\frac12 g_{\mu\nu}R=8\pi G\,T_{\mu\nu}\) [partially visible]
- `lecture_09_figure_05.png`: \(R=-8\pi G\,T\) [visible]
- `lecture_09_figure_05.png`: \(T=g^{\mu\nu}T_{\mu\nu}\) [standard reconstruction]

## Diagram And Layout Reading
- `lecture_09_figure_02.png` is not a geometric diagram but a board-layout figure: Susskind is visually collecting separate densities and flows into a single bracketed \(4\times4\) tensor, while isolating the continuity equation off to the right. The matrix framing matters here more than any one individual entry.
- `lecture_09_figure_03.png` is organized as a vertical test list. The top line functions as the candidate Einstein tensor, and the next two lines are visibly tentative because the question marks are written before the equals signs. The alignment itself communicates “compare these possibilities.”
- `lecture_09_figure_04.png` is a single horizontal identity. The board organization matters because the middle term \((D_\mu g^{\mu\nu})R\) is the local conceptual target of the spoken question, not just part of a generic product rule.
- `lecture_09_figure_05.png` is a three-step algebra board: rearranged Ricci form at top, standard Einstein form in the middle, trace relation at bottom. The vertical stacking makes the derivation readable as a chain, even though the middle line is partly cropped.

## TeX Reconstruction Plan
- `lecture_09_figure_02.png` should remain visible. The screenshot is the evidence for the matrix-style collection of components into \(T^{\mu\nu}\), and the notes should place a clean displayed \(4\times4\) tensor nearby together with the continuity equation \(D_\mu T^{\nu\mu}=0\).
- `lecture_09_figure_03.png` should remain visible. The key value is the exploratory board layout of three candidate tensors, so the notes should reconstruct the same three lines in an aligned display, preserving the question marks on the lower two candidates.
- `lecture_09_figure_04.png` does not need TikZ. The notes should reconstruct the product-rule identity as a displayed equation and then explicitly use \(D_\mu g^{\mu\nu}=0\). The screenshot may remain as supporting board evidence, but the typeset equation should carry the mathematical load.
- `lecture_09_figure_05.png` should remain visible if the chapter wants to preserve the lecturer’s algebraic sequence from Einstein form to trace relation and back to the Ricci-form equation. In any case, the notes should typeset all three equations cleanly in sequence.
- No standalone TikZ redraw is needed for any of these four figures. The relevant “visual” content is equation layout, not geometry.
- In chapter structure, `lecture_09_figure_03.png` and `lecture_09_figure_04.png` naturally support a local obstacle-and-resolution rhythm: candidate tensors first, then the covariant-divergence test that eliminates naive choices.

## Caption Drafts
- `lecture_09_figure_02.png`: Energy-momentum tensor entries and continuity law
- `lecture_09_figure_03.png`: Candidate geometric tensors for Einstein’s equation
- `lecture_09_figure_04.png`: Product rule for \(D_\mu(g^{\mu\nu}R)\)
- `lecture_09_figure_05.png`: Trace relation and Ricci-form Einstein equation

## Uncertainties
- `lecture_09_figure_02.png` does not show the full matrix cleanly. The lower-right entries are blocked or off-frame, so any complete \(4\times4\) matrix must be treated as a standard completion rather than a direct transcription.
- `lecture_09_figure_02.png` only shows the right-hand continuity equation partially. The fraction-style derivative notation is suggested by the board, but the fully clean covariant form comes from reconstruction.
- `lecture_09_figure_03.png` has a stray `=` at the far left edge from earlier board work; it should not be folded into the reconstructed three-line comparison.
- `lecture_09_figure_04.png` is partially occluded by the lecturer. The left-hand side and the equality sign are not as clear as the middle and right terms, so the full product-rule identity should be reconstructed cautiously from the visible fragments and the nearby spoken explanation.
- `lecture_09_figure_05.png` has the middle Einstein-equation line cropped on the left. The intended line is clear from context, but the screenshot itself does not display every symbol cleanly.
- Across the images, index positions vary between upper and lower placement depending on the board moment. The notes should preserve what is visibly written in each local derivation rather than forcing an artificial uniformity too early.