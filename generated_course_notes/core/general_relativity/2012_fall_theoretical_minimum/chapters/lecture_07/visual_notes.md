# Visual Evidence
## Frame Inventory
- `lecture_07_figure_02.png`: A sparse one-dimensional radial-axis sketch with a marked point at about `r=1` and a separate `r` label to the right; the screenshot should remain in the final notes as documentary evidence, but it needs a cleaner TikZ redraw for legibility.
- `lecture_07_figure_03.png`: A two-board view whose right panel shows the `(\rho,\omega)` metric form and the far-field limit `\lim_{\rho\to\infty}F(\rho)\rho^2=4`, while the left panel preserves fragments of the proper-time/proper-distance discussion; the screenshot should definitely remain in the final notes.
- `lecture_07_figure_04.png`: A causal sketch with a fan of slanted red lines, a black infalling trajectory labeled `Alice`, and a limiting line labeled `t=\infty`; the screenshot should remain and be paired with a simplified TikZ version.
- `lecture_07_figure_05.png`: A denser causal-ray board drawing with many converging slanted colored lines, a central marked vertical line, and several large black boundary curves; the screenshot should remain, but only as evidence alongside a heavily simplified TikZ reconstruction.

## Equation Extraction
- `lecture_07_figure_02.png`: [partially visible] `r=1`
- `lecture_07_figure_02.png`: [partially visible] `r`
- `lecture_07_figure_02.png`: [standard completion] A radial ordering sketch with `r=0` at the left, `r=1` at the horizon, and increasing `r` to the right.

- `lecture_07_figure_03.png`: [partially visible] `\rho(r)`
- `lecture_07_figure_03.png`: [visible] `\omega=\dfrac{t}{2}`
- `lecture_07_figure_03.png`: [visible] `F(\rho)\rho^2\,d\omega^2-d\rho^2-r(\rho)^2d\Omega^2`
- `lecture_07_figure_03.png`: [visible] `\lim_{\rho\to\infty}F(\rho)\rho^2=4`
- `lecture_07_figure_03.png`: [partially visible] `d\tau^2`
- `lecture_07_figure_03.png`: [partially visible] `-ds^2`
- `lecture_07_figure_03.png`: [standard completion] `d\tau^2 = F(\rho)\rho^2\,d\omega^2 - d\rho^2 - r(\rho)^2 d\Omega^2`

- `lecture_07_figure_04.png`: [visible] `t=\infty`
- `lecture_07_figure_04.png`: [visible] `Alice`

- `lecture_07_figure_05.png`: [partially visible] No reliable equation can be transcribed; the frame is diagram-dominant rather than formula-dominant.

## Diagram Extraction
- `lecture_07_figure_02.png`: Redraw the radial line in TikZ with a left endpoint, a marked horizon point at `r=1`, and outward increasing `r`; keep the screenshot nearby because it captures the board’s very spare coordinate setup.
- `lecture_07_figure_03.png`: Preserve the screenshot primarily as equation-and-board-layout evidence; this one does not require a TikZ figure, but the metric should be re-typeset cleanly as a displayed equation.
- `lecture_07_figure_04.png`: Redraw a simplified causal sketch with Alice’s worldline, several constant-time lines, and the limiting `t=\infty` line; keep the screenshot because it documents the board geometry that motivates the note version.
- `lecture_07_figure_05.png`: Redraw only the main causal structure in TikZ: the ray bundle, the central organizing line, and the major bounding curves; keep the screenshot because it shows Susskind’s blackboard method of answering observer questions by ray tracing.

## Reconstruction Guidance
- Treat `lecture_07_figure_02.png` as evidence for coordinate ordering, not as a self-sufficient final figure. The note-quality version should be a clean radial-axis TikZ sketch with labels supplied from the lecture context, while the screenshot remains as proof of the original board layout.
- Treat `lecture_07_figure_03.png` as the strongest direct evidence for the rewritten metric. The final notes should typeset the full equation cleanly, but mark the equality sign and full left-hand side as a cautious completion rather than pretending every symbol is fully legible in the frame.
- Treat `lecture_07_figure_04.png` as evidence for the statement that the horizon is reached only at `t=\infty` in Schwarzschild time. The TikZ redraw should stay minimal and only include elements that are actually secure in the image and transcript.
- Treat `lecture_07_figure_05.png` as evidence for causal reasoning by diagram, not for exact transcription of every stroke. The final redraw should simplify aggressively and preserve only the stable geometry that matters for note writing.
- In all cases, keep a strict separation between visible board content and standard completion. Use the transcript to disambiguate what the board is trying to say, but do not upgrade weakly legible marks into exact literal transcriptions.

## Uncertainties
- In `lecture_07_figure_02.png`, the leftmost label is too faint to trust fully; it is most naturally `r=0`, but the image alone does not prove it cleanly.
- In `lecture_07_figure_03.png`, the top-left label is plausibly `\rho(r)`, but the handwriting is not sharp enough to be certain.
- In `lecture_07_figure_03.png`, the left board fragments show `d\tau^2` and `-ds^2`, but not enough is visible to assert the full relation written there.
- In `lecture_07_figure_03.png`, the last term is best read as `-r(\rho)^2 d\Omega^2`, but the leading symbol should still be treated with mild caution.
- In `lecture_07_figure_04.png`, the roles of the unlabeled black curves and the exact status of each red line are not fully recoverable from the frame alone.
- In `lecture_07_figure_05.png`, many small point labels and colored strokes are too occluded or thin to support exact reproduction; the far-right turquoise curve may also belong to a larger board state than the core causal answer diagram.