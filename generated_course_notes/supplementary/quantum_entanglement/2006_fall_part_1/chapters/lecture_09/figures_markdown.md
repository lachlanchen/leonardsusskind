# Figure Notes
## Image Inventory
- `lecture_09_figure_03.png`: A tight board crop showing a single displayed formula for the time derivative of the state vector as a difference quotient. No lecturer is visible. The rest of the board is blank, so the equation is isolated and easy to read.
- `lecture_09_figure_04.png`: Susskind stands in front of the board while a single key equation is written above his head. The visible mathematical content is the energy-eigenvalue relation in bra-ket notation.
- `lecture_09_figure_05.png`: A wider classroom view with Susskind leaning on the desk in front of two boards. The left board shows the energy-frequency relation; the right board preserves parts of the preceding stationary-state derivation, including a first-order differential equation and an exponential phase factor.
- `lecture_09_figure_06.png`: Susskind stands aside from a mostly blank board on which a single expansion in Hamiltonian eigenvectors has been written near the top. The summation and ket notation are the only mathematical content in the frame.

## Blackboard Equations
- `lecture_09_figure_03.png`: \(\dfrac{d}{dt}|\psi\rangle = \dfrac{|\psi(\epsilon)\rangle - |\psi(0)\rangle}{\epsilon}\) [visible]
- `lecture_09_figure_03.png`: \(\dfrac{d}{dt}|\psi(t)\rangle = \dfrac{|\psi(\epsilon)\rangle - |\psi(0)\rangle}{\epsilon}\) [standard reconstruction]

- `lecture_09_figure_04.png`: \(H|\psi\rangle = E|\psi\rangle\) [visible]

- `lecture_09_figure_05.png`: \(E=\hbar\omega\) [partially visible]
- `lecture_09_figure_05.png`: \(\dfrac{E}{\hbar}=\omega\) [partially visible]
- `lecture_09_figure_05.png`: \(\dot f = -\dfrac{iE}{\hbar}f(t)\) [partially visible]
- `lecture_09_figure_05.png`: \(e^{-iEt/\hbar}\) [partially visible]
- `lecture_09_figure_05.png`: \(|\psi(t)\rangle = e^{-iEt/\hbar}|\psi(0)\rangle\) [standard reconstruction]

- `lecture_09_figure_06.png`: \(\sum_n \alpha_n |\psi_n\rangle\) [visible]
- `lecture_09_figure_06.png`: \(|\psi\rangle = \sum_n \alpha_n |\psi_n\rangle\) [standard reconstruction]

## Diagram And Layout Reading
- `lecture_09_figure_03.png` is not a diagram in the geometric sense; its value is that the difference-quotient equation is given its own isolated line on an otherwise empty board. This makes it a strong visual witness for the moment where the lecture turns the infinitesimal evolution rule into a time derivative.
- `lecture_09_figure_04.png` preserves the board rhetoric of the lecture: the eigenvalue equation is written as a standalone line above the lecturer, functioning as the premise for the following stationary-state argument.
- `lecture_09_figure_05.png` is a split-board layout. The left panel carries the energy-frequency identification, while the right panel still contains remnants of the derivation from the scalar differential equation for \(f(t)\) to the exponential phase. The frame is useful less for exact transcription than for showing that the lecture is explicitly tying the phase-evolution calculation back to \(E=\hbar\omega\).
- `lecture_09_figure_06.png` again uses a sparse board layout: one expansion line near the top of an otherwise empty whiteboard. That emptiness matters, because it shows the lecture resetting to the abstract statement that an arbitrary state can be expanded in Hamiltonian eigenvectors before adding the time-dependent phases.

## TeX Reconstruction Plan
- `lecture_09_figure_03.png` should remain visible in the notes. It should be paired with a clean displayed equation for the finite-difference definition of the time derivative, regularized into the final notation used in the chapter.
- `lecture_09_figure_04.png` should remain visible in the section on stationary states. Nearby LaTeX should typeset the cleaned eigenvalue equation \(H|\psi\rangle = E|\psi\rangle\) and then proceed to the scalar-factor ansatz.
- `lecture_09_figure_05.png` should remain visible, but the mathematics should be retypeset more aggressively than copied. The notes should keep the screenshot as layout evidence and place nearby displayed equations for \(E=\hbar\omega\), \(\dot f = -(iE/\hbar)f\), and \(|\psi(t)\rangle = e^{-iEt/\hbar}|\psi(0)\rangle\).
- `lecture_09_figure_06.png` should remain visible in the discussion of expanding an arbitrary state in the Hamiltonian eigenbasis. The screenshot should be paired with a clean displayed equation for \(|\psi\rangle = \sum_n \alpha_n |\psi_n\rangle\), and if the notes continue immediately to time evolution, the next displayed equation can introduce the factors \(e^{-iE_n t/\hbar}\).
- None of these four figures calls for TikZ. Their mathematical role is equation evidence and board sequencing, not geometric illustration.

## Caption Drafts
- `lecture_09_figure_03.png`: Difference quotient for the state vector
- `lecture_09_figure_04.png`: Energy eigenvalue equation
- `lecture_09_figure_05.png`: Energy-frequency relation beside phase evolution
- `lecture_09_figure_06.png`: Expansion in Hamiltonian eigenvectors

## Uncertainties
- `lecture_09_figure_03.png`: The left-hand ket is written without an explicit time argument in the visible frame; whether one regularizes it to \(|\psi(t)\rangle\) should be decided in the typeset reconstruction.
- `lecture_09_figure_05.png`: The left-board formula is small and slightly soft, so the \(\hbar\) in \(E=\hbar\omega\) and the lower line \(\omega=E/\hbar\) should be treated as transcript-supported regularizations rather than literal frame-only transcription.
- `lecture_09_figure_05.png`: The right-board derivation is partly blocked by Susskind and partly cropped, so the differential equation for \(f(t)\) and the final exponential solution should be reconstructed cautiously from the lecture rather than lifted directly from the frame.
- `lecture_09_figure_06.png`: The coefficient is best read as \(\alpha_n\), but the subscript and the ket index are small enough that the exact handwriting should be treated with mild caution.
- Across these images, the lecture often records intermediate board states rather than polished final equations, so the screenshots should serve as local witnesses while the final mathematical statements are retypeset cleanly in LaTeX.