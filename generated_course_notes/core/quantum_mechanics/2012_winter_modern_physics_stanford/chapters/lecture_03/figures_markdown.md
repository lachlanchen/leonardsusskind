# Figure Notes
## Image Inventory
- `lecture_03_figure_02.png` shows Leonard Susskind standing beside a simple three-arrow sketch on the blackboard. Three rays emerge from a common origin: one upward, one to the right, and one down-left. No symbolic labels are visible.
- `lecture_03_figure_03.png` shows a clean bra-ket matrix element written prominently on the board: a bracketed expression centered in the frame, with a cropped remnant of earlier notation above.
- `lecture_03_figure_04.png` shows two related lines of board work. The upper line is a bra-ket expansion for the action of an operator on a state, and the lower line rewrites the same content as an indexed sum involving \(K_{nm}\) and \(A_m\). Susskind points at the final coefficient term.
- `lecture_03_figure_06.png` shows a parenthesized matrix on the left and a parenthesized column vector on the right. The visible matrix entries begin with \(H_{11}\) and \(H_{12}\), while the vector entries begin with \(A_1\) and \(A_2\).

## Blackboard Equations
- `lecture_03_figure_03.png`: \(\langle m|\hat K|n\rangle\) [visible]
- `lecture_03_figure_04.png`: \(\langle n|\hat K|A\rangle = \sum_m \langle n|\hat K|m\rangle \langle m|A\rangle\) [visible]
- `lecture_03_figure_04.png`: \(\sum_m K_{nm} A_m\) [visible]
- `lecture_03_figure_06.png`: \(\begin{pmatrix} H_{11} & H_{12} & \cdots \\ H_{2\cdots} & \cdots \end{pmatrix}\) [partially visible]
- `lecture_03_figure_06.png`: \(\begin{pmatrix} A_1 \\ A_2 \\ \vdots \end{pmatrix}\) [visible]
- `lecture_03_figure_06.png`: \(\begin{pmatrix} H_{11} & H_{12} & \cdots \\ H_{21} & \cdots & \cdots \\ \vdots & & \ddots \end{pmatrix}\begin{pmatrix} A_1 \\ A_2 \\ \vdots \end{pmatrix}\) [standard reconstruction]

## Diagram And Layout Reading
- In `lecture_03_figure_02.png`, the board contains a deliberately ordinary geometric sketch rather than quantum notation. The three arrows from a common origin function as a real-space stand-in for a basis, matching the spoken point that complex vector spaces are hard to draw directly.
- In `lecture_03_figure_03.png`, the blackboard layout isolates a single matrix element in the middle of the writing surface. The cropped notation above is secondary; the figure’s value is the centered, readable bra-ket expression itself.
- In `lecture_03_figure_04.png`, the board is organized as a translation from abstract operator notation to component notation. The upper line carries the bra-ket derivation, while the lower line compresses it into the concrete matrix-times-components form.
- In `lecture_03_figure_06.png`, the board shows the concrete matrix picture very explicitly: a parenthesized array on the left and a separate parenthesized column vector on the right, spaced so the multiplication is visually clear even though no equals sign or resulting vector is shown in-frame.
- The left edge of `lecture_03_figure_06.png` still contains cropped remnants of earlier notation, but the central matrix-vector layout is the main usable content.

## TeX Reconstruction Plan
- `lecture_03_figure_02.png` must remain visible. It should be paired with a clean TikZ redraw of the three-arrow sketch, kept unlabeled unless the surrounding prose introduces labels from the transcript.
- `lecture_03_figure_03.png` must remain visible. Nearby, the notes should typeset the displayed equation \(\langle m|\hat K|n\rangle\) cleanly in LaTeX rather than relying on the screenshot alone.
- `lecture_03_figure_04.png` must remain visible. The notes should reconstruct the upper bra-ket line and the lower indexed sum as clean displayed equations, since this figure is valuable both as board evidence and as a bridge between the two notations.
- `lecture_03_figure_06.png` must remain visible. The notes should typeset a cleaned matrix-times-column-vector product beside it, using a standard finite-dimensional matrix layout with ellipses, since the board only shows the upper-left corner and the opening entries of the column.
- Only `lecture_03_figure_02.png` calls for TikZ. The other three figures are better supported by displayed equations rather than diagram redraws.

## Caption Drafts
- `lecture_03_figure_02.png`: Ordinary three-vector basis sketch
- `lecture_03_figure_03.png`: Matrix element \(\langle m|\hat K|n\rangle\)
- `lecture_03_figure_04.png`: Operator action rewritten in components
- `lecture_03_figure_06.png`: Matrix acting on a column vector

## Uncertainties
- `lecture_03_figure_02.png` contains no legible labels, so any symbolic naming of the three arrows would be a transcript-guided addition rather than a direct visual transcription.
- `lecture_03_figure_03.png` includes a cropped line of earlier notation above the main expression; that upper material should not be reconstructed from the image alone.
- In `lecture_03_figure_04.png`, the upper line is readable, but the far-left edge is slightly tight, so a clean LaTeX rendering should normalize spacing and bracket shape rather than imitate the chalk exactly.
- In `lecture_03_figure_06.png`, only the first few matrix entries are securely visible. The lower rows and full pattern of ellipses are implied by the layout and subtitle context, so the full matrix product should be treated as a cautious standard reconstruction rather than a literal full transcription.
- The leftmost cropped chalk fragments in `lecture_03_figure_06.png` are unrelated leftovers from previous writing and should not be incorporated into the note reconstruction.