# Visual Evidence
## Frame Inventory
- `lecture_06_figure_03.png` shows the board slogan `Geometry = Energy`, a centered \(\left(\dot a/a\right)^2\) term, and the edge of a circular cosmology sketch; keep the screenshot in the final notes because it captures the conceptual board layout, not just a formula.
- `lecture_06_figure_04.png` shows the fuller Friedmann-style balance across the board, with geometry terms on the left, energy-content terms on the right, and a small branch under the matter term; keep the screenshot in the final notes because it is the strongest visual evidence for the equation layout and the matter/radiation/vacuum decomposition.
- `lecture_06_figure_05.png` shows the ordinary integral-of-a-derivative identity at top center, a lower endpoint-evaluation line, and partially blocked auxiliary integrals on the left; keep the screenshot in the final notes because it documents the exact board setup that motivates the later Grassmann-integration rule.

## Equation Extraction
- `lecture_06_figure_03.png`: \(\text{Geometry}=\text{Energy}\) [visible]
- `lecture_06_figure_03.png`: \(\left(\frac{\dot a}{a}\right)^2\) [visible]
- `lecture_06_figure_04.png`: \(\left(\frac{\dot a}{a}\right)^2\) [visible]
- `lecture_06_figure_04.png`: \(\frac{1}{a^2}\) [visible]
- `lecture_06_figure_04.png`: \(\left(\frac{\dot a}{a}\right)^2 \pm \frac{1}{a^2}\) [standard completion]
- `lecture_06_figure_04.png`: \(\rho_{\text{matter}}+\rho_{\text{radiation}}+\rho_{\text{vacuum}}\) [standard completion]
- `lecture_06_figure_04.png`: \(\rho_{\text{matter}}=\rho_{\text{ordinary}}+\rho_{\text{dark}}\) [standard completion]
- `lecture_06_figure_05.png`: \(\int \frac{dF}{dx}\,dx\) [visible]
- `lecture_06_figure_05.png`: \(\int_{-\infty}^{\infty}\frac{dF}{dx}\,dx = F(\infty)-F(-\infty)\) [standard completion]
- `lecture_06_figure_05.png`: \(\int_{-\infty}^{\infty}\frac{dF}{dx}\,dx = 0\) [standard completion]
- `lecture_06_figure_05.png`: additional left-side integral expressions [partially visible]

## Diagram Extraction
- `lecture_06_figure_03.png`: Preserve as a screenshot only. The partial circular sketch is too cropped to justify a standalone redraw, but the slogan-plus-equation arrangement is worth showing as visual evidence.
- `lecture_06_figure_04.png`: Show both ways. Keep the screenshot, and also redraw a clean schematic or TikZ-supported equation layout that separates geometry terms from matter, radiation, and vacuum-energy terms; if the ordinary/dark split under matter is useful in the notes, redraw that split as a simple branching annotation.
- `lecture_06_figure_05.png`: Preserve as a screenshot and pair it with clean typeset equations rather than a TikZ redraw. Its value is documentary and sequential: it shows the ordinary total-derivative identity in the form that leads into Berezin integration.

## Reconstruction Guidance
- For `lecture_06_figure_03.png`, keep the prose close to the board: use “geometry equals energy” as the organizing phrase, then typeset the visible term \(\left(\dot a/a\right)^2\) cleanly beneath or beside the screenshot. Do not try to promote the partial circular sketch into a formal figure.
- For `lecture_06_figure_04.png`, reconstruct the mathematics as a cautious Friedmann-style balance rather than as a fully normalized textbook equation. The screenshot supports the structural statement “geometry terms on the left, energy densities on the right,” while the transcript supports the cautious completion into matter, radiation, and vacuum energy, with matter split into ordinary and dark matter.
- If a cleaner equation is needed for the notes, prefer a structurally faithful form such as \(\left(\dot a/a\right)^2 \pm 1/a^2 \sim \rho_{\text{matter}}+\rho_{\text{radiation}}+\rho_{\text{vacuum}}\), or a conventional \(k/a^2\) version only if the prose explicitly says that this is a standard notation choice rather than something fully visible on the board.
- For `lecture_06_figure_05.png`, use the visible \(\int \frac{dF}{dx}\,dx\) as the board anchor and reconstruct the definite-integral statement from the transcript: first the endpoint evaluation, then the vanishing under the assumption that the function dies off at spatial infinity. This clean typeset identity should sit next to the screenshot and then feed directly into the Grassmann analogue.
- Across all three frames, keep the screenshots nearby whenever the board layout itself carries explanatory force. Use clean LaTeX to remove ambiguity, but do not replace the screenshots with polished reconstructions when the lecture’s sequencing or organization is part of the evidence.

## Uncertainties
- In `lecture_06_figure_03.png`, the circular sketch at the right edge is only partial and should not be treated as a recoverable standalone diagram.
- In `lecture_06_figure_04.png`, the sign and exact normalization of the curvature term are not reliably legible from the frame alone.
- In `lecture_06_figure_04.png`, the right-hand words are not crisp enough to claim as pure visual transcription; “matter,” “radiation,” and “vacuum” are best treated as cautious transcript-supported completions.
- In `lecture_06_figure_04.png`, the left-edge bracket or enclosure mark is visible but its formal meaning in the equation is unclear.
- In `lecture_06_figure_05.png`, the lower evaluation line is partly obscured by Susskind and is not reliable as a direct transcription.
- In `lecture_06_figure_05.png`, the auxiliary integrals on the left are too incomplete to reconstruct confidently and should not be overused in the notes.
- None of these frames securely fixes numerical coefficients such as \(8\pi G/3\), so such coefficients should only be introduced later if justified elsewhere in the transcript or by a clearly marked standard-form reconstruction.