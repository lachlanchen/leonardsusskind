# Figure Notes
## Image Inventory
- `lecture_05_figure_02.png`: Leonard Susskind stands at the lower left of the frame in front of a whiteboard. At the upper left of the board there is a short supersymmetry relation written clearly, while fragments of earlier writing remain at the far right edge. The useful content is the isolated top-left equation.
- `lecture_05_figure_03.png`: Susskind is writing on a mostly blank board. To the right, a ket \(|\psi\rangle\) is already written; to its left he is in the middle of writing a partial-derivative operator, with his hand covering part of the denominator. The value of the image is the staged introduction of a time derivative acting on a state vector.
- `lecture_05_figure_04.png`: A fuller whiteboard shot showing a small time-shift rule at the upper right and, below it, a first-order change-of-argument expansion for \(\psi\). Susskind points directly at the denominator of a \(\partial/\partial t\) term. The board organization makes the time-translation argument visually explicit.

## Blackboard Equations
- `lecture_05_figure_02.png`: \(\{Q\,\bar Q\}=H\) [visible]
- `lecture_05_figure_02.png`: \(\{Q,\bar Q\}=H\) [standard reconstruction]
- `lecture_05_figure_03.png`: \(|\psi\rangle\) [visible]
- `lecture_05_figure_03.png`: \(\dfrac{\partial}{\partial t}\) [partially visible]
- `lecture_05_figure_03.png`: \(\dfrac{\partial}{\partial t}|\psi\rangle\) [standard reconstruction]
- `lecture_05_figure_04.png`: \(t\to t+\delta\) [partially visible]
- `lecture_05_figure_04.png`: \(\delta\,\dfrac{\partial \psi}{\partial t}\) [visible]
- `lecture_05_figure_04.png`: \(\psi(\theta,\bar\theta,t)\to \psi(\theta,\bar\theta,t)+\delta\,\dfrac{\partial \psi(\theta,\bar\theta,t)}{\partial t}\) [standard reconstruction]

## Diagram And Layout Reading
- None of these figures contain geometric diagrams, axes, or sketches; their value is algebraic and organizational.
- `lecture_05_figure_02.png` is an isolated conclusion board. The important visual fact is that the supersymmetry anticommutator relation sits by itself at the upper left, separated from the more fragmentary remnants at the right edge. That isolation supports using it as a local milestone in the notes.
- `lecture_05_figure_03.png` is a process shot rather than a finished board. The ket is already in place and the derivative operator is being built to its left. This helps preserve the lecture’s rhythm: Susskind is not merely stating the time-evolution equation, he is writing the operator structure on the board step by step.
- `lecture_05_figure_04.png` has a two-level layout. At the top right is the symbolic time shift \(t\to t+\cdots\). Beneath it sits the first-order expansion of \(\psi\), with the derivative term singled out by Susskind’s pointing finger. For note writing, that hierarchy matters: first the time shift, then the induced change in the wavefunction.

## TeX Reconstruction Plan
- `lecture_05_figure_02.png` should remain visible. It is the main board evidence for the simple supersymmetry algebra closing onto the Hamiltonian. Nearby, typeset the normalized displayed equation \(\{Q,\bar Q\}=H\).
- `lecture_05_figure_03.png` should also remain visible, despite being incomplete. Its importance is documentary: it shows the lecture introducing the time derivative acting on a ket. Nearby, reconstruct the local mathematics cleanly as \(\frac{\partial}{\partial t}|\psi\rangle\), and, if the chapter needs the full statement from the transcript, place the completed relation \(i\,\frac{\partial}{\partial t}|\psi\rangle = H|\psi\rangle\) in the prose or as a separate displayed equation.
- `lecture_05_figure_04.png` should remain visible. It records both the small time-shift rule and the first-order expansion of \(\psi\). Nearby, typeset the clean reconstruction
  \[
  t\to t+\delta,
  \qquad
  \psi(\theta,\bar\theta,t)\to \psi(\theta,\bar\theta,t)+\delta\,\frac{\partial \psi(\theta,\bar\theta,t)}{\partial t}.
  \]
- No TikZ redraw is necessary for these three figures. The mathematics is best handled as screenshot-plus-equation rather than screenshot-plus-diagram.

## Caption Drafts
- `lecture_05_figure_02.png`: Supersymmetry anticommutator yielding the Hamiltonian.
- `lecture_05_figure_03.png`: Time derivative acting on a state vector.
- `lecture_05_figure_04.png`: First-order time translation of the wavefunction.

## Uncertainties
- `lecture_05_figure_02.png`: The top-left relation is clear, but the board does not visibly mark a comma between \(Q\) and \(\bar Q\); writing \(\{Q,\bar Q\}=H\) is a normalized reconstruction from the lecture context.
- `lecture_05_figure_02.png`: The right-edge markings are cropped and too fragmentary to reconstruct reliably. They should be treated as background context only.
- `lecture_05_figure_03.png`: Susskind’s hand covers part of the derivative denominator. The reading \(\partial/\partial t\) is strongly supported by the visible ket and the subtitle/transcript context, but the operator is not fully unobstructed in the image itself.
- `lecture_05_figure_03.png`: The frame does not itself show the full Schrödinger-type relation to the Hamiltonian; that must be supplied cautiously from the transcript rather than claimed as fully board-visible.
- `lecture_05_figure_04.png`: The shift parameter at the top right is not perfectly sharp; the transcript supports reading it as \(\delta\), but the image alone only securely shows \(t\to t+\cdots\).
- `lecture_05_figure_04.png`: The arguments of \(\psi\) are not all equally sharp. The transcript strongly suggests \(\psi(\theta,\bar\theta,t)\), but the image alone is safest as \(\psi(\ldots,t)\) unless the chapter wants the transcript-backed completion stated explicitly.