# Figure Notes
## Image Inventory
- `lecture_58_figure_01.png`: A Stanford opening title card. It shows the red Stanford block `S` with the tree emblem, the text “STANFORD UNIVERSITY,” and the website line below. There is no lecturer, blackboard, equation, or diagram.
- `lecture_58_figure_02.png`: A clean whiteboard shot with a two-line force formula. The upper line gives the Lorentz-force form in terms of \(E\), \(V\), and \(B\); the lower line rewrites it schematically using \(F^{\mu\nu}\). The board is otherwise almost blank, so the equation is the sole visual content.
- `lecture_58_figure_03.png`: A partial but useful blackboard view of the electromagnetic field tensor written as an anti-symmetric matrix. The tensor label \(F^{\mu\nu}\) is at left; the matrix has headers \(t,x,y,z\), electric-field entries across the first row and first column, and circles marking diagonal or not-yet-filled entries.
- `lecture_58_figure_04.png`: A close-up of the one-dimensional wave equation. A hand points near the spatial derivative term. The equation is large and fills most of the frame, with almost no surrounding board context.
- `lecture_58_figure_05.png`: A later blackboard sketch of a sinusoidal wave drawn along a horizontal axis labeled \(z\). Several short vertical arrows indicate transverse oscillation. Susskind is visible at left, and there is some cropped, incomplete notation above the sketch.

## Blackboard Equations
- `lecture_58_figure_01.png`: no blackboard mathematics; only title-card text is present.
- `lecture_58_figure_02.png`: \(F = q(E + V \times B)\) [visible]
- `lecture_58_figure_02.png`: \(= q\,F^{\mu\nu}\) [visible]
- `lecture_58_figure_03.png`: \(F^{\mu\nu}\) [visible]
- `lecture_58_figure_03.png`: \(t,\ x,\ y,\ z\) [visible]
- `lecture_58_figure_03.png`: \(0,\ -E_x,\ -E_y,\ -E_z\) across the top row [visible]
- `lecture_58_figure_03.png`: \(+E_x,\ +E_y,\ +E_z\) down the first column below the top entry [visible]
- `lecture_58_figure_03.png`: diagonal zeros in the anti-symmetric matrix [visible]
- `lecture_58_figure_03.png`: \(F^{\mu\nu}=\begin{pmatrix}0&-E_x&-E_y&-E_z\\ +E_x&0&\cdots&\cdots\\ +E_y&\cdots&0&\cdots\\ +E_z&\cdots&\cdots&0\end{pmatrix}\) [standard reconstruction]
- `lecture_58_figure_04.png`: \(\frac{\partial^2 \phi}{\partial t^2}-\frac{\partial^2 \phi}{\partial z^2}=0\) [visible]
- `lecture_58_figure_05.png`: \(z\) [visible]
- `lecture_58_figure_05.png`: an incomplete upper expression ending in \(=0\) is present, but not secure enough to transcribe fully [partially visible]

## Diagram And Layout Reading
- `lecture_58_figure_01.png` has no mathematical layout. It is purely a branded intro card and does not help the notes.
- `lecture_58_figure_02.png` is useful because the board is visually stripped down to a single idea: the ordinary Lorentz-force expression is being turned into tensor language. The emptiness of the surrounding board actually helps, because it isolates the conceptual pivot from three-vector notation to covariant notation.
- `lecture_58_figure_03.png` preserves the layout of the field-tensor matrix. The top row and first column are the crucial visible structure: time first, then \(x,y,z\), with electric-field components sitting in the time-space slots and opposite signs across the diagonal. The circles in the matrix show that Susskind is using the anti-symmetry pattern and zero diagonal as a visual scaffold before or while filling the magnetic entries.
- `lecture_58_figure_04.png` is not a diagram but an equation close-up. It is valuable because the frame fixes exactly the one-dimensional reduction of the wave equation, with time derivatives opposed to \(z\)-derivatives.
- `lecture_58_figure_05.png` shows a transverse wave sketched along a horizontal \(z\)-axis. The vertical arrows at alternating parts of the sinusoid indicate oscillation transverse to the propagation direction. This is the kind of figure that would be clearer as a TikZ redraw, but the screenshot still matters as evidence of how Susskind staged the geometry on the board.

## TeX Reconstruction Plan
- `lecture_58_figure_01.png` should not remain visible in the mathematical chapter. It is an opening title card and carries no blackboard evidence.
- `lecture_58_figure_02.png` should remain visible if the chapter includes the transition from the three-vector Lorentz-force law to covariant notation. It should be paired with a clean displayed equation nearby. Because the second line on the board is schematic and incomplete as written, the nearby typeset equation should follow the transcript-backed covariant form rather than reproducing the board shorthand as if it were complete.
- `lecture_58_figure_03.png` should remain visible in the section where the electromagnetic field tensor is introduced. It should be paired with a clean displayed \(4\times4\) anti-symmetric matrix reconstructed from the transcript. No TikZ redraw is necessary; typeset matrix form is the right reconstruction.
- `lecture_58_figure_04.png` should remain visible in the wave-equation review section. It should be paired with a clean displayed equation for the reduced one-dimensional wave equation. If the notes also state the full \(3+1\)-dimensional wave operator first, that should be typeset from the transcript, not inferred from the frame.
- `lecture_58_figure_05.png` should only remain visible if the chapter includes the later electromagnetic-wave geometry. If used, it should be paired with a TikZ redraw of a transverse sinusoidal wave propagating along \(z\), plus nearby transcript-backed equations such as a cosine profile or \(z\pm t\) wave form. Because the provided subtitle metadata says “anti-symmetric matrix” while the frame clearly shows a wave sketch, this asset should be treated as mis-indexed and used only with caution.

## Caption Drafts
- `lecture_58_figure_01.png`: Stanford opening title card
- `lecture_58_figure_02.png`: Lorentz force rewritten in field-tensor notation
- `lecture_58_figure_03.png`: Electromagnetic field tensor with electric-field entries
- `lecture_58_figure_04.png`: One-dimensional wave equation for \(\phi\)
- `lecture_58_figure_05.png`: Transverse wave profile propagating along \(z\)

## Uncertainties
- `lecture_58_figure_01.png` is not a lecture figure in the mathematical sense and should be excluded from the final notes unless one is documenting the video source itself.
- In `lecture_58_figure_02.png`, the lower line \(=q\,F^{\mu\nu}\) is visibly incomplete as a covariant force law. The transcript indicates that the tensor is multiplied by the four-velocity and tied to the \(\mu\)-component of the force, so the notes should not pretend that the board line alone is a complete formula.
- In `lecture_58_figure_02.png`, the symbol in the cross product is visibly written as \(V\), but the eventual notes may normalize it to the lecture’s standard velocity notation if the transcript confirms that.
- In `lecture_58_figure_03.png`, cropped notation above the matrix belongs to neighboring Maxwell-equation content and should not be used as direct evidence for the tensor discussion.
- In `lecture_58_figure_03.png`, the magnetic-field entries are not yet fully visible in the screenshot. The full anti-symmetric matrix must therefore be completed from the transcript, not from the image alone.
- In `lecture_58_figure_04.png`, the hand slightly crowds the lower part of the second derivative term, but the equation itself is still legible. If one wants the notation normalized, the standard typeset form \(\partial_t^2\phi-\partial_z^2\phi=0\) is the safe cleanup.
- In `lecture_58_figure_05.png`, the upper cropped formula is too incomplete to quote reliably.
- In `lecture_58_figure_05.png`, the image alone shows a transverse wave moving along \(z\), but it does not by itself securely identify whether the oscillating quantity is \(E\), \(B\), or a generic field variable. That identification must come from the transcript.
- `lecture_58_figure_05.png` appears mismatched to its supplied subtitle metadata. The frame belongs visually to the later wave-and-polarization discussion, not to the anti-symmetric-matrix moment.