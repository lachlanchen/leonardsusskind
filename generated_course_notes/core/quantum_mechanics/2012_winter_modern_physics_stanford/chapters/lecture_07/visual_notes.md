# Visual Evidence

## Frame Inventory

- `lecture_07_figure_02.png` shows a phase-circle sketch with horizontal and vertical diameters, a marked point on the circumference, and a right-hand comparison between `|A\rangle` and a phase-shifted copy; this screenshot should remain in the final notes.
- `lecture_07_figure_03.png` shows a multi-board layout with a bra-ket overlap formula, a second line containing trigonometric factors and a phase, a lower-left radial/star-like sketch, and a right-board axis sketch; this screenshot should also remain in the final notes.

## Equation Extraction

- `lecture_07_figure_02.png`: `|A\rangle` [visible]
- `lecture_07_figure_02.png`: `e^{i\theta}` [visible]
- `lecture_07_figure_02.png`: `e^{i\theta}|A\rangle` [standard completion]
- `lecture_07_figure_02.png`: visual comparison between `|A\rangle` and `e^{i\theta}|A\rangle` rather than a long completed handwritten equation [standard completion]

- `lecture_07_figure_03.png`: `\langle \theta | \psi \rangle` or `\langle \psi | \theta \rangle` [partially visible]
- `lecture_07_figure_03.png`: `= a\cos\theta + \sqrt{1-a^2}\,e^{\cdots i\phi}\sin\theta` [partially visible]
- `lecture_07_figure_03.png`: `a`, `\cos\theta`, `\sqrt{1-a^2}`, `e^{i\phi}`, and `\sin\theta` are individually visible as ingredients of the lower line [partially visible]
- `lecture_07_figure_03.png`: `\langle \psi | \theta \rangle = a\cos\theta + \sqrt{1-a^2}\,e^{-i\phi}\sin\theta` [standard completion]

## Diagram Extraction

- `lecture_07_figure_02.png`: the left-hand circle should be treated as a phase or unit-circle sketch, with crossed axes and a marked phase point; it should be shown both as the original screenshot and as a clean TikZ redraw.
- `lecture_07_figure_02.png`: the right-hand vertical placement of the ket expressions should be preserved by keeping the screenshot, while the actual mathematics is better typeset as clean display equations nearby.
- `lecture_07_figure_03.png`: the screenshot should remain visible because the blackboard layout matters here; the formula sits on the left board while geometric intuition is distributed across the lower-left and right boards.
- `lecture_07_figure_03.png`: the right-board axis-and-direction sketch is clear enough to redraw conservatively in TikZ, but the original screenshot should stay nearby as evidence.
- `lecture_07_figure_03.png`: the lower-left star-like sketch is too ambiguous for a confident full reconstruction; if used at all, it should be redrawn only as a minimal schematic and never treated as a precise derived figure.

## Reconstruction Guidance

- For `lecture_07_figure_02.png`, keep the screenshot in the phase-indifference part of the chapter and typeset the clean comparison between a state and the same state multiplied by a pure phase. The TikZ redraw should isolate the unit-circle geometry, while the bra-ket relation should be presented as clean LaTeX rather than as handwriting.
- For `lecture_07_figure_03.png`, use the screenshot as board-layout evidence, but reconstruct the overlap amplitude as a clean displayed equation. The transcript-backed correction about complex conjugation should control the final sign in the phase factor.
- Any TikZ redraw should stay close to the corresponding screenshot. The screenshot shows how Susskind organized the argument on the board; the redraw exists only to make the mathematics and geometry readable.
- Prefer conservative completion. Where the frame shows only fragments of a derivation, reconstruct the canonical clean formula that matches the spoken lecture, but do not invent additional intermediate steps not supported by the board or transcript.

## Uncertainties

- In `lecture_07_figure_02.png`, the small label above the circle is not reliably legible.
- In `lecture_07_figure_02.png`, the board clearly indicates a comparison between `|A\rangle` and a phase-shifted copy, but the exact handwritten spacing does not itself give a perfectly complete equation.
- In `lecture_07_figure_03.png`, the bra-ket order in the top expression is not fully secure from the bitmap alone.
- In `lecture_07_figure_03.png`, the sign in the exponent is not secure from the frame; the transcript indicates a correction to the conjugated phase, which is why the clean completion should be treated as cautious rather than literal.
- In `lecture_07_figure_03.png`, the far-right cropped symbols are too incomplete to transcribe.
- In `lecture_07_figure_03.png`, the lower-left radial/star-like sketch is visibly intentional but not self-explanatory enough to support a detailed geometric reconstruction on its own.