# Visual Evidence
## Frame Inventory
- `lecture_05_figure_02.png`: A nearly empty board showing the first line of the Pauli-action list being written at the upper left; this screenshot should remain in the final notes as visual evidence for the start of the operator table.
- `lecture_05_figure_03.png`: A partially occluded board with a normalized two-spin superposition at upper left, small spin sketches across the top, and a lower line moving toward an equals-zero statement; this screenshot should remain in the final notes because the board layout matters even where legibility is imperfect.
- `lecture_05_figure_04.png`: A projection-operator board with partial ket notation on the left and a clear geometric projection sketch on the right; this screenshot should remain and should be paired with a TikZ redraw of the geometric figure.
- `lecture_05_figure_05.png`: A stronger algebraic projection-operator frame showing explicit projector action on a spinor and the beginning of the operator’s matrix form; this screenshot should remain in the final notes as the clearest visual evidence for the projector formulas.

## Equation Extraction
- `lecture_05_figure_02.png`: \(\sigma_1 |u\rangle =\) [visible]
- `lecture_05_figure_02.png`: \(\sigma_1 |u\rangle = |d\rangle\) [standard completion]

- `lecture_05_figure_03.png`: \(\dfrac{|ud\rangle \pm |du\rangle}{\sqrt{2}}\) [partially visible]
- `lecture_05_figure_03.png`: \(=0\) at the end of the lower line [visible]
- `lecture_05_figure_03.png`: \(\langle \sigma_i \rangle = 0\) [standard completion]

- `lecture_05_figure_04.png`: \(P|\alpha\rangle = |\alpha_p\rangle\) [partially visible]
- `lecture_05_figure_04.png`: \(|\alpha\rangle\) and a projected ket resembling \(|\alpha_p\rangle\) [partially visible]

- `lecture_05_figure_05.png`: \(P|\alpha\rangle = |\alpha_p\rangle\) [partially visible]
- `lecture_05_figure_05.png`: \(P_{\sigma_3=1}\begin{pmatrix}\alpha\\ \beta\end{pmatrix}=\begin{pmatrix}\alpha\\ 0\end{pmatrix}\) [visible]
- `lecture_05_figure_05.png`: \(P_{\sigma_3=-1}\begin{pmatrix}\alpha\\ \beta\end{pmatrix}=\begin{pmatrix}0\\ \beta\end{pmatrix}\) [visible]
- `lecture_05_figure_05.png`: \(P_{\sigma_3=1}=\begin{pmatrix}1&0\\0&0\end{pmatrix}\) [standard completion]
- `lecture_05_figure_05.png`: \(P_{\sigma_3=+1}=\dfrac{1+\sigma_3}{2}\) [standard completion]

## Diagram Extraction
- `lecture_05_figure_02.png`: No independent diagram is present; the value is the board placement of the first Pauli-action equation, so the screenshot should be preserved rather than redrawn.
- `lecture_05_figure_03.png`: The small spin doodles and the layered layout of state-plus-conclusion are visually useful, but they are too partial to serve as a standalone cleaned diagram; preserve the screenshot and use typeset equations nearby instead of a literal redraw.
- `lecture_05_figure_04.png`: The right-hand figure should be redrawn in TikZ and also preserved as a screenshot. Visually it is a projection picture: an origin-centered coordinate sketch, a one-dimensional slanted subspace or axis, and a vector whose component along that subspace is being picked out.
- `lecture_05_figure_05.png`: This frame is primarily algebraic, not geometric; preserve it as a screenshot and typeset the equations cleanly, but a TikZ redraw is not necessary.

## Reconstruction Guidance
- For `lecture_05_figure_02.png`, keep the screenshot adjacent to a clean displayed equation \(\sigma_1|u\rangle=|d\rangle\). If the full Pauli-action table is included in the notes, it should be reconstructed from the transcript and standard convention, not from this frame alone.
- For `lecture_05_figure_03.png`, use the screenshot as evidence of the board organization and the local claim that a one-spin quantity vanishes. The notes should typeset the normalized two-spin superposition and the cleaned zero-expectation statement rather than relying on literal chalk transcription.
- For `lecture_05_figure_04.png`, typeset the generic projection statement cleanly and redraw the right-hand projection geometry in TikZ. Keep the screenshot nearby because it shows that Susskind is explicitly pairing operator notation on the left with geometric intuition on the right.
- For `lecture_05_figure_05.png`, typeset the projector-action formulas and the explicit matrix/operator form as clean display math. Keep the screenshot because it captures the lecture’s progression from “what the projector does to a spinor” to “what matrix the projector is.”
- Any completed formula that depends on hidden or blurred chalk should be treated as a cautious completion from the transcript and standard spin-\(\tfrac12\) notation, not as a pure visual transcription.

## Uncertainties
- In `lecture_05_figure_02.png`, the right-hand ket is blocked by the lecturer’s hand, so the completion \(|d\rangle\) is not directly visible.
- In `lecture_05_figure_03.png`, the sign in the two-spin superposition is not recoverable from the frame alone, and the lower line is too occluded to prove that the exact left-hand expression is \(\langle \sigma_i\rangle\).
- In `lecture_05_figure_04.png`, the subscript on the projected ket is not fully sharp; \(|\alpha_p\rangle\) is the most plausible reading but not visually certain character by character.
- In `lecture_05_figure_04.png`, the projection sketch is clear in structure but not in explicit labels; the axes and the projected direction are mostly geometric rather than textual.
- In `lecture_05_figure_05.png`, the top generic projection line is only partly crisp, and the right-hand operator expression is mid-write rather than fully settled.
- The exact typographic form of the projector subscript in `lecture_05_figure_05.png` is readable in substance but not perfectly sharp, so the cleaned notation should be standardized rather than overfit to every chalk mark.