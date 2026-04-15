# Visual Evidence
## Frame Inventory
- `lecture_05_figure_01.png`: Stanford University title card on a black background with no blackboard content; do not keep this in the final notes.
- `lecture_05_figure_02.png`: Early board view with the Minkowski proper-time formula, the spacelike interval formula, and a central double light-cone sketch; keep as a primary screenshot in the causal-structure section.
- `lecture_05_figure_03.png`: Split-board frame showing `T.L.`, `S.L.`, `L.L.`, part of the flat metric matrix, and on the right `g_{\mu\nu}(x)` with local cone sketches; keep as a primary screenshot in the metric-signature/local-light-cone section.
- `lecture_05_figure_04.png`: Alternate right-board view of `g_{\mu\nu}(x)` and a row of cone-like sketches, but visually mismatched with its listed subtitle timing; do not keep as a primary figure, though it may serve as optional duplicate evidence for the local-light-cone discussion.
- `lecture_05_figure_05.png`: Action-principle board state with the relativistic particle action across the top and a live rewrite into `A=\int L\,dt` below; keep as a primary screenshot in the action/Lagrangian transition.
- `lecture_05_figure_06.png`: Slightly later action-principle frame with the top action and a cleaner isolated Lagrangian line below; keep if space allows, especially to document the Lagrangian itself.

## Equation Extraction
- `lecture_05_figure_01.png`
  - No mathematical content.

- `lecture_05_figure_02.png`
  - [visible] \(d\tau^2 = dt^2 - dx^2 - dy^2 - dz^2\)
  - [visible] \(ds^2 = dx^2 + dy^2 + dz^2 - dt^2\)
  - [visible] \(ds^2 > 0\)
  - [partially visible] a cropped repeated start of \(d\tau^2\) appears at the far right edge

- `lecture_05_figure_03.png`
  - [visible] \(g_{\mu\nu}(x)\)
  - [visible] `T.L.`
  - [visible] `S.L.`
  - [visible] `L.L.`
  - [partially visible] a diagonal \(4\times 4\) matrix with one negative and three positive diagonal entries
  - [standard completion] \(\eta_{\mu\nu}=\mathrm{diag}(-1,1,1,1)\)

- `lecture_05_figure_04.png`
  - [visible] \(g_{\mu\nu}(x)\)
  - [standard completion] this frame belongs to the same local-light-cone sequence as `lecture_05_figure_03.png`, not to the later Euler–Lagrange moment indicated by the metadata

- `lecture_05_figure_05.png`
  - [partially visible] \(A=-m\int \sqrt{-\,g_{\mu\nu}(x)\,\frac{dx^\mu}{dt}\frac{dx^\nu}{dt}}\,dt\)
  - [visible] \(g_{\mu\nu}(x)\)
  - [visible] \(\frac{dx^\mu}{dt}\)
  - [visible] \(\frac{dx^\nu}{dt}\)
  - [partially visible] \(A=\int L\,dt\)
  - [partially visible] left-board remnants of earlier geodesic material, including \(\Gamma^\mu_{\sigma\rho}\) and \(\frac{dx}{dt}\)-type terms, are present but not clean enough to transcribe fully

- `lecture_05_figure_06.png`
  - [partially visible] \(A=-m\int \sqrt{-\,g_{\mu\nu}(x)\,\frac{dx^\mu}{dt}\frac{dx^\nu}{dt}}\,dt\)
  - [partially visible] \(L=-m\sqrt{-\,g_{\mu\nu}(x)\,\frac{dx^\mu}{dt}\frac{dx^\nu}{dt}}\)
  - [visible] \(g_{\mu\nu}(x)\)
  - [standard completion] the lower line is the same square-root integrand from the action, isolated and named as the Lagrangian

## Diagram Extraction
- `lecture_05_figure_02.png`: The central double light cone should be shown both ways: preserve the screenshot as documentary evidence and redraw a clean TikZ light cone nearby. The redraw should include the event at the cone tip, future and past directions, and a representative spacelike direction.
- `lecture_05_figure_02.png`: The partial axis marks at the far left are not strong enough to deserve a separate figure, but they support a cleaned axis-based TikZ redraw if desired.
- `lecture_05_figure_03.png`: The right-board local cone sketch sequence should be shown both ways: keep the screenshot and redraw a simplified TikZ version of neighboring local cones attached to different points. The left/right split-board layout itself is also useful evidence for how Susskind visually moved from flat-space labels to \(g_{\mu\nu}(x)\).
- `lecture_05_figure_04.png`: The row of cone/hourglass sketches is useful as alternate evidence for the local-light-cone idea, but it should not anchor a separate section. If used at all, use it only as a supplemental screenshot beside the cleaner `lecture_05_figure_03.png`.
- `lecture_05_figure_05.png`: No TikZ redraw is needed. Its value is the staged board transition from the relativistic action to the standard action-as-integral form.
- `lecture_05_figure_06.png`: No TikZ redraw is needed. Its value is the cleaner board presentation of the isolated Lagrangian.
- `lecture_05_figure_05.png` and `lecture_05_figure_06.png`: If both are retained, they should appear close together so the reader can see the derivational rhythm and then the cleaned formula state.

## Reconstruction Guidance
- Use `lecture_05_figure_02.png` to typeset clean displayed equations for \(d\tau^2\), \(ds^2\), and the spacelike condition \(ds^2>0\). Keep the screenshot visible because it captures the lecture’s actual grouping of equations and cone sketch, not just the formulas in isolation.
- Use `lecture_05_figure_03.png` as the main visual anchor for the move from flat-space signature to a position-dependent metric \(g_{\mu\nu}(x)\). The notes should reconstruct \(\eta_{\mu\nu}\) cleanly from standard form, but only after making clear that the board itself shows the matrix only partially.
- Treat `lecture_05_figure_04.png` cautiously. It is not reliable evidence for the later action/Euler–Lagrange discussion, so it should not be cited there; at most it can reinforce the earlier local-light-cone section.
- For `lecture_05_figure_05.png`, reconstruct the action line and the relation \(A=\int L\,dt\) as clean display equations directly beside the screenshot. Normalize the action symbol to a standard \(A\) or \(S\) in the notes rather than preserving the unclear chalk label literally.
- For `lecture_05_figure_06.png`, typeset the isolated Lagrangian cleanly in note-quality notation. This frame is best used to justify the final cleaned Lagrangian after the transitional frame in `lecture_05_figure_05.png`.
- Where a formula is only partly legible but clearly intended, prefer cautious standard completion rather than literal reproduction of broken chalk marks. This is especially important for the action/Lagrangian lines and the partially visible flat metric matrix.
- Keep screenshots wherever the board layout or sequencing matters, not only where the formulas matter. In this set, that is true for the causal-structure board, the local-light-cone board, and the action-to-Lagrangian transition.

## Uncertainties
- `lecture_05_figure_01.png` contains no mathematical uncertainty because it contains no mathematics.
- In `lecture_05_figure_02.png`, the cropped notation at the far right looks like a restarted or repeated \(d\tau^2\), but it is too incomplete to use.
- In `lecture_05_figure_03.png`, the diagonal matrix on the left board is only partly visible; interpreting it as \(\eta_{\mu\nu}=\mathrm{diag}(-1,1,1,1)\) is well motivated but not literally fully readable from the frame.
- In `lecture_05_figure_03.png` and `lecture_05_figure_04.png`, the cone sketches are unlabeled. Their interpretation as local light cones with coordinate- or metric-dependent appearance comes from the lecture context, not from standalone annotations on the board.
- `lecture_05_figure_04.png` is visually mismatched with its metadata subtitle window. It should not be used as evidence for the “\(F=ma\)-type equations” transition.
- In `lecture_05_figure_05.png`, the leftmost chalk label for the action is unclear and should not be reproduced verbatim.
- In `lecture_05_figure_05.png`, the lower line is visibly mid-write, so \(A=\int L\,dt\) is supported partly by the frame and partly by cautious transcript-backed completion.
- In `lecture_05_figure_06.png`, the lower Lagrangian line is clearer than in `lecture_05_figure_05.png`, but the right side remains partly crowded by the lecturer and by cropping. The index placement and exact velocity factors should therefore be normalized from the intended standard form rather than copied mechanically.