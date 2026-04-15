# Visual Evidence
## Frame Inventory
- `lecture_09_figure_02.png` shows the board moment where the energy-momentum tensor is being assembled as a bracketed matrix, with several upper-left entries visible and a separate conservation equation at the right; this screenshot should remain in the final notes.
- `lecture_09_figure_03.png` shows the cleanest comparison of candidate left-hand sides for Einstein’s equation, with one accepted-looking line and two tentative lines marked by question marks; this screenshot should remain in the final notes.
- `lecture_09_figure_04.png` shows the product-rule expansion for the covariant derivative of \(g^{\mu\nu}R\), with the crucial middle and right terms visible even though the lecturer partly blocks the left; this screenshot should remain as supporting evidence near the derivation.
- `lecture_09_figure_05.png` shows the trace relation and the Ricci-form rewriting of Einstein’s equation in a vertically stacked algebra sequence; this screenshot should remain in the final notes.

## Equation Extraction
- `lecture_09_figure_02.png`: \(c=1\) [visible]
- `lecture_09_figure_02.png`: \(T^{00},\;T^{01},\;T^{02},\;T^{03},\;T^{10},\;T^{11}\) [visible]
- `lecture_09_figure_02.png`: \(\dfrac{D T^{\nu\mu}}{D x^\mu}=0\) [partially visible]
- `lecture_09_figure_02.png`: \(D_\mu T^{\nu\mu}=0\) [standard completion]
- `lecture_09_figure_02.png`: \(T^{\mu\nu}=\begin{pmatrix} T^{00}&T^{01}&T^{02}&T^{03}\\ T^{10}&T^{11}&T^{12}&T^{13}\\ T^{20}&T^{21}&T^{22}&T^{23}\\ T^{30}&T^{31}&T^{32}&T^{33}\end{pmatrix}\) [standard completion]

- `lecture_09_figure_03.png`: \(G^{\mu\nu}=8\pi G\,T^{\mu\nu}\) [visible]
- `lecture_09_figure_03.png`: \(R^{\mu\nu}\stackrel{?}{=}8\pi G\,T^{\mu\nu}\) [visible]
- `lecture_09_figure_03.png`: \(g^{\mu\nu}R\stackrel{?}{=}8\pi G\,T^{\mu\nu}\) [visible]

- `lecture_09_figure_04.png`: \(D_\mu\!\left(g^{\mu\nu}R\right)=\left(D_\mu g^{\mu\nu}\right)R+g^{\mu\nu}\left(D_\mu R\right)\) [partially visible]
- `lecture_09_figure_04.png`: \(D_\mu g^{\mu\nu}=0\) [standard completion]

- `lecture_09_figure_05.png`: \(R_{\mu\nu}=8\pi G\left(T_{\mu\nu}-\frac12 g_{\mu\nu}T\right)\) [visible]
- `lecture_09_figure_05.png`: \(R_{\mu\nu}-\frac12 g_{\mu\nu}R=8\pi G\,T_{\mu\nu}\) [partially visible]
- `lecture_09_figure_05.png`: \(R=-8\pi G\,T\) [visible]
- `lecture_09_figure_05.png`: \(T=g^{\mu\nu}T_{\mu\nu}\) [standard completion]

## Diagram Extraction
- `lecture_09_figure_02.png` is not a geometric sketch but a board-layout figure: the large matrix framing matters, because Susskind is visibly collecting densities and fluxes into one tensor while keeping the continuity equation separate at the right. Preserve the screenshot and typeset a clean matrix beside it; no TikZ is needed.
- `lecture_09_figure_03.png` functions as a compare-and-eliminate board diagram: the vertical stacking of \(G^{\mu\nu}\), \(R^{\mu\nu}\), and \(g^{\mu\nu}R\) is part of the argument. Preserve the screenshot and reproduce the same three-line layout in displayed math; no TikZ is needed.
- `lecture_09_figure_04.png` is a one-line algebra board rather than a true diagram. Preserve the screenshot as evidence for the product-rule step, but let the clean typeset equation carry the mathematical burden.
- `lecture_09_figure_05.png` is a three-step algebra layout: Ricci-form equation at top, standard Einstein equation in the middle, trace relation at bottom. Preserve the screenshot and typeset the three equations in sequence; no TikZ is needed.
- None of these frames contains a genuine spatial sketch or geometric construction that needs a standalone TikZ redraw.

## Reconstruction Guidance
- For `lecture_09_figure_02.png`, keep the screenshot visible and reconstruct the full \(4\times4\) energy-momentum tensor only as a cautious standard completion. The frame directly supports the matrix idea and several entries, but not every component.
- For `lecture_09_figure_03.png`, keep the board order exactly: accepted Einstein-tensor line first, then the two trial alternatives with question marks. The vertical comparison is part of the lecture’s logic and should survive in the notes.
- For `lecture_09_figure_04.png`, typeset the full product-rule identity cleanly and then explicitly use metric compatibility to remove \((D_\mu g^{\mu\nu})R\). The screenshot should stay nearby because it captures the local obstacle the lecturer is resolving.
- For `lecture_09_figure_05.png`, reconstruct the algebra as a short chain: standard Einstein equation, traced equation \(R=-8\pi G\,T\), then the Ricci-form rewriting \(R_{\mu\nu}=8\pi G(T_{\mu\nu}-\tfrac12 g_{\mu\nu}T)\). The top and bottom lines are strongly frame-backed; the middle line is a cautious restoration.
- Use ordinary displayed equations and matrix environments rather than inventing new visual diagrams. These frames are valuable mainly as evidence of board structure and sequencing.
- Do not add textbook digressions that are not motivated by the lecture. The reconstruction should stay close to the lecturer’s actual path: tensor source, candidate geometric tensors, divergence test, Einstein combination, trace.

## Uncertainties
- In `lecture_09_figure_02.png`, the lower-right part of the tensor is blocked or off-frame, so any full matrix is necessarily a standard completion.
- In `lecture_09_figure_02.png`, the continuity equation is only partially legible; the exact board notation looks fraction-style, while the clean covariant form comes from cautious reconstruction.
- In `lecture_09_figure_03.png`, there is a stray `=` at the far left from earlier board work; it should not be treated as part of the candidate list.
- In `lecture_09_figure_04.png`, the leftmost part of the equation is partially occluded, so the full identity should not be claimed as fully visible from the frame alone.
- In `lecture_09_figure_05.png`, the middle Einstein-equation line is cropped on the left, so the full displayed equation is partly transcript-supported rather than fully frame-visible.
- Across all four frames, Susskind’s index placement shifts between upper and lower positions from one board moment to another. The notes should normalize only when the surrounding derivation clearly warrants it.