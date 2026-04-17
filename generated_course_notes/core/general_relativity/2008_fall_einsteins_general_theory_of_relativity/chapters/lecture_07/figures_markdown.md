# Figure Notes
## Image Inventory
- `lecture_07_figure_01.png`: A Stanford University opening title card with the red Stanford “S” and tree logo, the text “STANFORD UNIVERSITY,” and the website `www.stanford.edu`. No lecture blackboard is visible.
- `lecture_07_figure_02.png`: A board shot from the Riemann-tensor discussion. Susskind stands in front of the board, but the left-hand side of the displayed formula and the derivative terms are still visible.
- `lecture_07_figure_03.png`: A board shot from the Ricci-tensor contraction discussion. Susskind is turned toward the board and pointing near the left-hand side of the equation. The contraction with the metric is visible on the right.
- `lecture_07_figure_04.png`: A close shot of a nearly blank board while Susskind begins writing a new parenthesized expression. Only the beginning of the notation is visible.
- `lecture_07_figure_05.png`: A sparse board shot showing two early stress-energy tensor components written side by side, with a large amount of blank board around them.

## Blackboard Equations
- `lecture_07_figure_01.png`: No blackboard equations or notation are visible.
- `lecture_07_figure_02.png`: $R^{\rho}{}_{\sigma\mu\nu}=\partial_{\mu}\Gamma^{\rho}{}_{\nu\sigma}-\partial_{\nu}\Gamma^{\rho}{}_{\mu\sigma}+\cdots$ [visible]
- `lecture_07_figure_02.png`: $R^{\rho}{}_{\sigma\mu\nu}=\partial_{\mu}\Gamma^{\rho}{}_{\nu\sigma}-\partial_{\nu}\Gamma^{\rho}{}_{\mu\sigma}+\Gamma^{\rho}{}_{\mu\lambda}\Gamma^{\lambda}{}_{\nu\sigma}-\Gamma^{\rho}{}_{\nu\lambda}\Gamma^{\lambda}{}_{\mu\sigma}$ [standard reconstruction]
- `lecture_07_figure_03.png`: $R_{\beta\delta}=R_{\alpha\beta\gamma\delta}\,g^{\alpha\gamma}$ [visible]
- `lecture_07_figure_03.png`: $R_{\beta\delta}=R_{\delta\beta}$ [standard reconstruction]
- `lecture_07_figure_04.png`: $(P^{0}$ [partially visible]
- `lecture_07_figure_04.png`: $(P^{0},P^{1},P^{2},P^{3})$ [standard reconstruction]
- `lecture_07_figure_05.png`: $T^{00}$ [visible]
- `lecture_07_figure_05.png`: $T^{01}$ [visible]

## Diagram And Layout Reading
- `lecture_07_figure_01.png` has no mathematical layout. It is purely an institutional intro card.
- `lecture_07_figure_02.png` is valuable mainly for board organization rather than for a pristine full formula. The left side identifies the object as the Riemann tensor, and the board then runs horizontally into the derivative terms. The screenshot documents that Susskind is answering a question about tensor character while still standing under the already-written curvature formula.
- `lecture_07_figure_03.png` has no geometric sketch, but it does preserve the argumentative layout of the Ricci contraction. The output tensor $R_{\beta\delta}$ sits at the left, the Riemann tensor with all lower indices is placed in the middle, and the contracting metric $g^{\alpha\gamma}$ sits at the right. Susskind’s pointing gesture emphasizes the equality and the resulting two-index object.
- `lecture_07_figure_04.png` does not yet contain a usable board layout. It is the beginning of a new line of notation, with the lecture moving to the energy-momentum four-vector, but the image catches only the start of the writing.
- `lecture_07_figure_05.png` is diagrammatic in a minimal sense: it records the component-by-component introduction of the energy-momentum tensor. The two visible entries, $T^{00}$ and $T^{01}$, are spaced apart on the board, showing that Susskind is beginning to enumerate components rather than writing a single long equation.

## TeX Reconstruction Plan
- `lecture_07_figure_01.png` should not be used as mathematical evidence in the lecture notes. If it is kept at all, it belongs only in prefatory or documentary material, not in the chapter body.
- `lecture_07_figure_02.png` should remain visible if the chapter wants documentary support for the Riemann-tensor formula. It should be paired with a clean displayed equation giving the full standard formula in typeset LaTeX. No TikZ redraw is needed.
- `lecture_07_figure_03.png` should remain visible. It is good evidence for the Ricci tensor being obtained by contraction of the Riemann tensor. It should sit beside a clean displayed formula for $R_{\beta\delta}=R_{\alpha\beta\gamma\delta}g^{\alpha\gamma}$, and if the surrounding prose discusses the point, one may typeset the symmetry statement $R_{\beta\delta}=R_{\delta\beta}$ nearby.
- `lecture_07_figure_04.png` is too incomplete to support a useful standalone figure in the chapter. The notes should prefer a transcript-backed typeset reconstruction of the four-momentum vector rather than relying on this screenshot. If it is kept at all, it should be kept only as a very minor documentary frame.
- `lecture_07_figure_05.png` can remain visible if the notes want to preserve the lecture’s step-by-step board rhythm in introducing $T^{\mu\nu}$ by components. It should be paired with a clean typeset display or short array showing the first few stress-energy tensor components, rather than left to carry the mathematics alone.
- None of these selected images calls for a TikZ redraw. The useful reconstructions here are equation cleanups and, in the case of the stress-energy discussion, possibly a simple typeset component layout.

## Caption Drafts
- `lecture_07_figure_01.png`: Stanford opening title card
- `lecture_07_figure_02.png`: Riemann tensor formula on the board
- `lecture_07_figure_03.png`: Ricci tensor as a contraction of the Riemann tensor
- `lecture_07_figure_04.png`: Beginning of the four-momentum notation
- `lecture_07_figure_05.png`: First stress-energy tensor components

## Uncertainties
- In `lecture_07_figure_02.png`, the right-hand Christoffel-product terms are not fully clean in the frame, so the full formula should be treated as a standard completion supported by the lecture rather than as a perfect raw transcription of the image.
- In `lecture_07_figure_03.png`, the middle Riemann tensor term is somewhat cramped and partly blocked by Susskind’s hand and body, but the contraction pattern with $g^{\alpha\gamma}$ is clear enough when read together with the visible indices.
- In `lecture_07_figure_04.png`, only the beginning of a parenthesized expression and $P^{0}$ are visible. The full four-vector cannot be recovered from the image alone without transcript support.
- In `lecture_07_figure_05.png`, the minimalist handwriting could in principle look like a bare “T” with superscripts, but in context it is most plausibly read as $T^{00}$ and $T^{01}$ from the stress-energy tensor discussion.
- `lecture_07_figure_01.png` is not a lecture-board frame at all, so it should not be allowed to influence the mathematical reconstruction of the chapter.