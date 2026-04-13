# Figure Notes
## Image Inventory
- `lecture_03_figure_02.png`: Susskind stands at the left side of the board, leaving the central chalk sketch visible. Near the center is a small loop attached to a short vertical line, consistent with a very simple loop or tadpole-like Feynman-diagram sketch. On the left side of the board are two energy formulas, with the upper one clearly in square-root form and the lower one in the massless form. On the right side is a partially cropped action-like expression beginning with `\int d^4x`, together with bracketed field-dimension notation below it.

## Blackboard Equations
- `E=\sqrt{p^2+m^2}` [visible]
- `E=|p|` [partially visible]
- `\int d^4x` [visible]
- `\frac{\partial \phi}{\partial x^\mu}` [partially visible]
- `\left(\frac{\partial \phi}{\partial x^\mu}\right)^2` [standard reconstruction]
- `[\phi]` [partially visible]
- `[\phi]=L^{-1}` [standard reconstruction]

## Diagram And Layout Reading
- The board is organized as a transition moment. The local focal point is the small loop sketch in the middle, while the left and right sides preserve material from the immediately preceding discussion of propagators, dimensions, and massless versus massive behavior.
- The central drawing looks like a short external line meeting a small closed loop, rather than a free-standing vacuum bubble. That makes it useful as evidence for the lecture’s move into a simple self-energy or tadpole-type correction diagram.
- The left-hand formulas visually support the nearby spoken contrast between the relativistic dispersion relation and the massless limit.
- The right-hand integral is not locally about the loop diagram itself, but it does preserve the blackboard context: Susskind is still working with field-theory action notation while transitioning into the Feynman-diagram discussion.

## TeX Reconstruction Plan
- `lecture_03_figure_02.png` should remain visible in the notes. Its main value is not just the small diagram in isolation, but the full board layout showing the diagram embedded between earlier kinematic and action-level formulas.
- The central loop sketch should be redrawn nearby in TikZ as a minimal tadpole-like scalar self-energy diagram: a short external line meeting a small closed loop. Keep it schematic and centered.
- The surrounding equations should be reconstructed as clean displayed LaTeX nearby only in a light-touch way:
  - definitely `E=\sqrt{p^2+m^2}` and `E=|p|`,
  - optionally the action fragment as `\int d^4x\,(\partial_\mu\phi)^2` if the chapter is explicitly recalling the dimensional-analysis setup.
- The screenshot should not be used as evidence for exact particle labels, coupling labels, or full propagator formulas. Those belong to transcript-backed prose and cautious reconstruction, not to literal image transcription.

## Caption Drafts
- `lecture_03_figure_02.png`: Simple loop correction with surrounding field-theory formulas.

## Uncertainties
- The central sketch is clearly loop-based, but the exact point of attachment between the short line and the loop is slightly ambiguous in the frame; it is safest to treat it as a simple tadpole-like correction diagram rather than over-specify the vertex structure.
- The lower left formula is strongly suggestive of `E=|p|`, but part of it is faint and partly occluded.
- The right-hand action expression is only partially legible. `\int d^4x` is secure, but the full integrand should be reconstructed cautiously from context rather than claimed as completely visible.
- The bracketed field-dimension notation below the integral is visibly present, but the full right-hand side is not cleanly readable from the frame alone.