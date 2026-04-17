# Visual Evidence
## Frame Inventory
- `lecture_07_figure_01.png`: Stanford title card with logo and website, with no blackboard mathematics or lecture layout visible, so it should not remain in the chapter body.
- `lecture_07_figure_02.png`: Board shot of the Riemann-tensor formula with Susskind partly occluding the board but leaving the identifying left-hand side and derivative terms visible, and it should remain as a screenshot in the final notes.
- `lecture_07_figure_03.png`: Board shot of the Ricci-tensor contraction with the left-hand side and the metric contraction visible despite partial occlusion, and it should remain as a screenshot in the final notes.
- `lecture_07_figure_04.png`: Nearly blank board with only the start of a parenthesized four-momentum notation visible, so it should not remain as a substantive mathematical figure in the chapter.
- `lecture_07_figure_05.png`: Sparse board shot showing the first visible stress-energy components written separately on the board, and it should remain if the chapter wants documentary support for the step-by-step introduction of \(T^{\mu\nu}\).

## Equation Extraction
- `lecture_07_figure_02.png`: \(R^{\rho}{}_{\sigma\mu\nu}=\partial_{\mu}\Gamma^{\rho}{}_{\nu\sigma}-\partial_{\nu}\Gamma^{\rho}{}_{\mu\sigma}+\cdots\) [visible]
- `lecture_07_figure_02.png`: \(R^{\rho}{}_{\sigma\mu\nu}=\partial_{\mu}\Gamma^{\rho}{}_{\nu\sigma}-\partial_{\nu}\Gamma^{\rho}{}_{\mu\sigma}+\Gamma^{\rho}{}_{\mu\lambda}\Gamma^{\lambda}{}_{\nu\sigma}-\Gamma^{\rho}{}_{\nu\lambda}\Gamma^{\lambda}{}_{\mu\sigma}\) [standard completion]
- `lecture_07_figure_03.png`: \(R_{\beta\delta}=R_{\alpha\beta\gamma\delta}\,g^{\alpha\gamma}\) [visible]
- `lecture_07_figure_03.png`: \(R_{\beta\delta}=R_{\delta\beta}\) [standard completion]
- `lecture_07_figure_04.png`: \((P^{0}\) [partially visible]
- `lecture_07_figure_04.png`: \((P^{0},P^{1},P^{2},P^{3})\) [standard completion]
- `lecture_07_figure_05.png`: \(T^{00}\) [visible]
- `lecture_07_figure_05.png`: \(T^{01}\) [visible]

## Diagram Extraction
- `lecture_07_figure_02.png` is not a geometric sketch, but it preserves useful board structure: the tensor name at the left and the derivative terms extending horizontally, so it should be preserved as a screenshot rather than redrawn in TikZ.
- `lecture_07_figure_03.png` is likewise not a diagram but an argument-layout frame: output tensor on the left, four-index tensor in the middle, and contracting metric on the right, so it should be preserved as a screenshot rather than redrawn in TikZ.
- `lecture_07_figure_05.png` records the component-by-component board introduction of the stress-energy tensor, and it is better shown as a screenshot plus a clean typeset array than as a TikZ figure.
- None of the attached frames contains a genuine board sketch that demands TikZ redrawing; the surviving visual evidence is equation layout, not geometry drawing.
- If the finished chapter later needs explanatory sketches, the small-loop holonomy picture or a current-through-a-window picture would be optional pedagogical reconstructions from the transcript, not redraws of surviving frame evidence.

## Reconstruction Guidance
- Use `lecture_07_figure_02.png` as documentary evidence for the Riemann-tensor discussion, but typeset the full formula cleanly in standard notation; the screenshot should support the lecture rhythm, not carry the final mathematical burden by itself.
- Use `lecture_07_figure_03.png` beside a clean displayed Ricci-contraction formula; the frame is strong evidence for the contraction pattern, while the clean equation should resolve the cramped indices.
- Treat `lecture_07_figure_05.png` as evidence for the lecture’s row-by-row unfolding of \(T^{\mu\nu}\), then typeset a short matrix or array nearby so the reader sees more than the two visible entries.
- Do not let `lecture_07_figure_04.png` determine the notation of four-momentum; reconstruct \(P^\mu\) from transcript and standard relativistic notation, and keep the frame out of the main mathematical exposition unless a documentary aside is needed.
- Do not use `lecture_07_figure_01.png` as mathematical evidence at all; if retained anywhere, it belongs only in front-matter or archival documentation.
- Prefer screenshot-plus-equation for `lecture_07_figure_02.png`, `lecture_07_figure_03.png`, and `lecture_07_figure_05.png`; no frame-backed TikZ redraw is necessary for these assets.

## Uncertainties
- In `lecture_07_figure_02.png`, the rightmost Christoffel-product terms are not fully readable, so the complete Riemann formula should be treated as a standard completion rather than a pure visual transcription.
- In `lecture_07_figure_03.png`, the four-index tensor in the middle is partly blocked by Susskind’s body and hand, so the contraction indices are read with help from context rather than from perfect legibility.
- In `lecture_07_figure_04.png`, only the initial parenthesis and \(P^{0}\) are visible, so the full four-vector cannot be claimed from the frame alone.
- In `lecture_07_figure_05.png`, only the earliest entries are visible, so the full \(T^{\mu\nu}\) array must be reconstructed from transcript rather than inferred from the image.
- The images do not preserve the lecture’s earlier conceptual sketches about loops, planes, or current flow, so any such figures in the notes would be transcript-based reconstructions rather than frame-based extractions.