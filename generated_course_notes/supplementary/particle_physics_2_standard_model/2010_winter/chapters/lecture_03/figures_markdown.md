# Figure Notes
## Image Inventory
- `lecture_03_figure_02.png`: A clean blackboard sketch showing three coordinate axes meeting at a common origin, together with a slanted arrow from the origin labeled by a visible \(\hat n\) and a nearby \(\theta\). No sphere is actually drawn in the frame.
- `lecture_03_figure_03.png`: A board close-up centered on the rotation-action formula. The main content is a handwritten matrix-times-vector equation involving \(R(\theta,\hat n)\), a vector component \(V_j\), and a transformed component \(V_i'\). A stray or earlier \(V_i\) appears above the equation.
- `lecture_03_figure_04.png`: A board shot showing the transition from the explicit transpose-plus-complex-conjugation form of the condition on \(U\) to the compact Hermitian-conjugate notation. The lecturer is in frame but does not block the main equations. Partial earlier matrix and spinor notation is still visible along the top.

## Blackboard Equations
- `lecture_03_figure_02.png`: \(\hat n\) [visible]
- `lecture_03_figure_02.png`: \(\theta\) [visible]

- `lecture_03_figure_03.png`: \(R_{ij}(\theta,\hat n)\,V_j = V_i'\) [visible]
- `lecture_03_figure_03.png`: \(V_i\) written above the main equation [partially visible]

- `lecture_03_figure_04.png`: \(\left(U^T\right)^*\,U = 1\) [visible]
- `lecture_03_figure_04.png`: \(U^\dagger U = 1\) [visible]
- `lecture_03_figure_04.png`: a partially visible \(2\times 2\) matrix \(U\) acting on a two-component column of \(\alpha\)'s [partially visible]
- `lecture_03_figure_04.png`: \(U^\dagger U = I\) as a cleaned notation if the chapter prefers the identity symbol \(I\) over the chalkboard \(1\) [standard reconstruction]

## Diagram And Layout Reading
- `lecture_03_figure_02.png` matters as a board sketch, not as a finished geometric diagram. The three axes establish ordinary space, and the slanted arrow identifies the rotation axis as a unit vector \(\hat n\). The nearby \(\theta\) labels the rotation angle, but there is no drawn arc marking the angle and no explicit unit sphere in the frame.
- `lecture_03_figure_03.png` is a layout bridge from geometric discussion to indexed matrix notation. The visual point is that the rotation is now being represented by a matrix \(R_{ij}\) acting on vector components \(V_j\) to produce transformed components \(V_i'\).
- `lecture_03_figure_04.png` preserves a two-step board organization: first the longer form using transpose and complex conjugation, then the shorter Hermitian-conjugate notation beneath it. That ordering matters pedagogically because the lower equation is a cleaned rewrite of the upper one, not a separate claim.

## TeX Reconstruction Plan
- `lecture_03_figure_02.png` should remain visible in the notes. Nearby, redraw the geometry in TikZ as a clean three-axis sketch with a radial arrow labeled \(\hat n\), and place \(\theta\) near the direction label. Do not add a full sphere unless a later passage explicitly requires it from the transcript.
- `lecture_03_figure_03.png` should remain visible and should be paired with a clean displayed equation, preferably
  \[
  R_{ij}(\theta,\hat n)\,V_j = V_i'
  \]
  or an equivalent consistent index placement such as \(V_i' = R_{ij}(\theta,\hat n)V_j\). No TikZ redraw is needed here.
- `lecture_03_figure_04.png` should remain visible and should be paired with a clean two-line display,
  \[
  \left(U^T\right)^* U = 1,
  \qquad
  U^\dagger U = 1,
  \]
  with an optional typographic standardization to \(I\) or \(\mathbf 1\) if the surrounding chapter uses that notation. The partially visible upper matrix-spinor line should not be reconstructed aggressively unless the surrounding prose already derives it from the transcript.

## Caption Drafts
- `lecture_03_figure_02.png`: Unit-vector axis sketch for a rotation
- `lecture_03_figure_03.png`: Rotation matrix acting on vector components
- `lecture_03_figure_04.png`: Unitary condition written in Hermitian-conjugate form

## Uncertainties
- In `lecture_03_figure_02.png`, the transcript mentions a unit sphere, but the sphere itself is not drawn in the frame; only the axis sketch, \(\hat n\), and \(\theta\) are secure visual evidence.
- In `lecture_03_figure_02.png`, the exact geometric role of \(\theta\) is transcript-clear but board-informal, since no explicit angular arc is drawn.
- In `lecture_03_figure_03.png`, the index placement is handwritten informally; the clean notes should standardize whether the transformed component is written as \(V_i'\) or \(V_i^{\prime}\), and whether the equation is presented as \(R_{ij}V_j=V_i'\) or \(V_i'=R_{ij}V_j\).
- In `lecture_03_figure_03.png`, the stray \(V_i\) above the main equation appears to be leftover or contextual notation rather than part of the final displayed formula.
- In `lecture_03_figure_04.png`, the upper matrix-and-column-vector context is cropped and only partly readable; the safe transcription is the unitarity condition itself.
- In `lecture_03_figure_04.png`, the board writes the identity as \(1\), while polished notes may prefer \(I\) or \(\mathbf 1\); that should be treated as a typographic cleanup, not as literal board text.