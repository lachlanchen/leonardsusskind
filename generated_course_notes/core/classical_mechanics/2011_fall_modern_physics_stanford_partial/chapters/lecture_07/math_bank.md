# Math Bank
## Core Equations
- \[
  \dot p_i=-\frac{\partial H}{\partial q_i},
  \qquad
  \dot q_i=\frac{\partial H}{\partial p_i}
  \]
  [transcript-backed]

- \[
  \frac{\partial v_x}{\partial x}=0
  \]
  [transcript-backed]

- \[
  \frac{\partial v_x}{\partial x}+\frac{\partial v_y}{\partial y}=0
  \]
  [transcript-backed]

- \[
  \sum_i \frac{\partial v_i}{\partial x_i}=0
  \]
  [standard reconstruction]

- \[
  \nabla\cdot \mathbf v = 0
  \]
  [standard reconstruction]

- \[
  \sum_i\left(\frac{\partial \dot p_i}{\partial p_i}+\frac{\partial \dot q_i}{\partial q_i}\right)=0
  \]
  [transcript-backed]

- \[
  L=\frac{\dot x^2}{2}
  \]
  [visible]

- \[
  P_x=\frac{\partial L}{\partial \dot x}=\dot x
  \]
  [standard reconstruction]

- \[
  y=\alpha x,
  \qquad
  x=\frac{y}{\alpha},
  \qquad
  \dot x=\frac{\dot y}{\alpha}
  \]
  [transcript-backed]

- \[
  L=\frac{\dot y^2}{2\alpha^2}
  \]
  [transcript-backed]

- \[
  p_y=\frac{\partial L}{\partial \dot y}=\frac{\dot y}{\alpha^2}=\frac{\dot x}{\alpha}=\frac{p_x}{\alpha}
  \]
  [transcript-backed]

- \[
  \Delta y\,\Delta p_y=\Delta x\,\Delta p_x
  \]
  [standard reconstruction]

- \[
  \mathbf F=q\,\mathbf v\times \mathbf B
  \]
  [transcript-backed]

- \[
  (\mathbf v\times \mathbf B)_z=v_xB_y-v_yB_x
  \]
  [transcript-backed]

- \[
  (\mathbf v\times \mathbf B)_x=v_yB_z-v_zB_y
  \]
  [standard reconstruction]

- \[
  (\mathbf v\times \mathbf B)_y=v_zB_x-v_xB_z
  \]
  [standard reconstruction]

- \[
  \mathbf B=\nabla\times \mathbf A
  \]
  [transcript-backed]

- \[
  (\nabla\times \mathbf A)_z=\frac{\partial A_y}{\partial x}-\frac{\partial A_x}{\partial y}
  \]
  [transcript-backed]

- \[
  (\nabla\times \mathbf A)_x=\frac{\partial A_z}{\partial y}-\frac{\partial A_y}{\partial z}
  \]
  [transcript-backed]

- \[
  (\nabla\times \mathbf A)_y=\frac{\partial A_x}{\partial z}-\frac{\partial A_z}{\partial x}
  \]
  [standard reconstruction]

- \[
  S=\int \frac12 mv^2\,dt+q\int A_i\,dx_i
  \]
  [standard reconstruction]

- \[
  S=\int\left(\frac12 m\dot x_i^2+qA_i\dot x_i\right)dt
  \]
  [standard reconstruction]

- \[
  \int \frac{mv^2}{2}\,dt + qA_i
  \]
  [visible]

- \[
  L=\frac12 m\dot x_i^2+qA_i\dot x_i
  \]
  [transcript-backed]

- \[
  p_i=\frac{\partial L}{\partial \dot x_i}=m\dot x_i+qA_i
  \]
  [transcript-backed]

- \[
  p_x=m\dot x+qA_x,
  \qquad
  p_y=m\dot y+qA_y,
  \qquad
  p_z=m\dot z+qA_z
  \]
  [transcript-backed]

- \[
  \frac{d}{dt}\frac{\partial L}{\partial \dot z}=\frac{\partial L}{\partial z}
  \]
  [transcript-backed]

- \[
  \frac{\partial L}{\partial z}
  =
  q\dot x\,\frac{\partial A_x}{\partial z}
  +
  q\dot y\,\frac{\partial A_y}{\partial z}
  +
  q\dot z\,\frac{\partial A_z}{\partial z}
  \]
  [standard reconstruction]

- \[
  = q\dot x\,\frac{\partial A_x}{\partial z}
  \]
  [visible]

- \[
  \dot A_z
  =
  \frac{\partial A_z}{\partial x}\dot x
  +
  \frac{\partial A_z}{\partial y}\dot y
  +
  \frac{\partial A_z}{\partial z}\dot z
  \]
  [transcript-backed]

- \[
  m\ddot z+q\dot A_z=\frac{\partial L}{\partial z}
  \]
  [transcript-backed]

- \[
  m\ddot z
  =
  q\dot x\left(\frac{\partial A_x}{\partial z}-\frac{\partial A_z}{\partial x}\right)
  +
  q\dot y\left(\frac{\partial A_y}{\partial z}-\frac{\partial A_z}{\partial y}\right)
  \]
  [standard reconstruction]

- \[
  m\ddot z=q(v_xB_y-v_yB_x)=q(\mathbf v\times\mathbf B)_z
  \]
  [standard reconstruction]

- \[
  H=\sum_i p_i\dot x_i-L
  \]
  [transcript-backed]

- \[
  H=p_x\dot x+p_y\dot y+p_z\dot z-L
  \]
  [transcript-backed]

- \[
  H=\frac12 mv^2
  \]
  [transcript-backed]

- \[
  \dot x=\frac{p_x-qA_x}{m},
  \qquad
  \dot y=\frac{p_y-qA_y}{m},
  \qquad
  \dot z=\frac{p_z-qA_z}{m}
  \]
  [transcript-backed]

- \[
  H=\frac{1}{2m}\left[(p_x-qA_x)^2+(p_y-qA_y)^2+(p_z-qA_z)^2\right]
  \]
  [standard reconstruction]

- \[
  H=\frac{1}{2m}(\mathbf p-q\mathbf A)^2
  \]
  [standard reconstruction]

- \[
  \mathbf p_{\mathrm{mech}}=m\mathbf v=\mathbf p-q\mathbf A
  \]
  [standard reconstruction]

## Definitions And Objects
- `Liouville’s theorem`: Hamiltonian flow in phase space is incompressible; phase-space volume is preserved. [transcript-backed]
- `Phase-space velocity`: the collection of \((\dot q_i,\dot p_i)\). [transcript-backed]
- `Divergence`: sum of derivatives of each velocity component with respect to its own coordinate. [transcript-backed]
- `Incompressible flow`: a flow preserving density/volume; in the lecture this is introduced first for ordinary fluids, then imported into phase space. [transcript-backed]
- `Canonical momentum`: \(p_i=\partial L/\partial \dot x_i\). [transcript-backed]
- `Mechanical momentum`: \(m\dot x_i\), contrasted explicitly with canonical momentum in the magnetic-field example. [transcript-backed]
- `Vector potential`: auxiliary vector field \(\mathbf A\) with \(\mathbf B=\nabla\times\mathbf A\); needed for Lagrangian/Hamiltonian formulation. [transcript-backed]
- `Magnetic field`: \(\mathbf B\), taken as divergence-free and derived from \(\mathbf A\). [transcript-backed]
- `Coarse-graining`: replacing exact phase points by finite cells/spheres representing limited distinguishability. [transcript-backed]
- `Entropy`: proportional to the logarithm of the detectable phase-space volume occupied by the system. [transcript-backed]
- `Canonical transformation`: transformation preserving phase-space area/volume structure; time evolution is stated to be one. [transcript-backed]
- `Invariant probability measure`: in the chaotic discussion, relative probability is tied to phase-space area. [transcript-backed]

## Derivation Steps
Liouville from incompressible flow
1. Start with a one-dimensional uniform distribution of points in a line.
2. Compare the number of points entering and leaving a small interval.
3. Conclude that incompressibility requires \(V_2-V_1=0\).
4. For a small interval, replace \(V_2-V_1\) by \((\partial v_x/\partial x)\Delta x\).
5. Infer \(\partial v_x/\partial x=0\).
6. Repeat in two dimensions for a rectangle of size \(\Delta x\Delta y\).
7. Count flux through left/right edges using \(v_x\); count flux through bottom/top edges using \(v_y\).
8. Add the net changes and factor out \(\Delta x\Delta y\).
9. Obtain \(\partial v_x/\partial x+\partial v_y/\partial y=0\).
10. Generalize to \(\sum_i \partial v_i/\partial x_i=0\).

Liouville from Hamilton’s equations
1. Identify phase-space coordinates as all \(q_i\) and \(p_i\).
2. Identify phase-space velocity components as \(\dot q_i\) and \(\dot p_i\).
3. Write the phase-space divergence as \(\sum_i (\partial \dot p_i/\partial p_i+\partial \dot q_i/\partial q_i)\).
4. Substitute \(\dot p_i=-\partial H/\partial q_i\).
5. Substitute \(\dot q_i=\partial H/\partial p_i\).
6. Differentiate to get mixed second derivatives of \(H\).
7. Use equality of mixed partial derivatives.
8. Observe pairwise cancellation between the \(p_i\)- and \(q_i\)-terms.
9. Conclude that the divergence vanishes.

Free-particle rescaling and invariant area
1. Start with \(L=\dot x^2/2\) and \(p_x=\partial L/\partial \dot x=\dot x\).
2. Introduce a new coordinate \(y=\alpha x\).
3. Rewrite \(x=y/\alpha\) and \(\dot x=\dot y/\alpha\).
4. Rewrite the Lagrangian as \(L=\dot y^2/(2\alpha^2)\).
5. Compute \(p_y=\partial L/\partial \dot y=\dot y/\alpha^2\).
6. Substitute \(\dot y=\alpha \dot x\) to get \(p_y=\dot x/\alpha=p_x/\alpha\).
7. Conclude that stretching the coordinate axis shrinks the conjugate momentum axis.
8. Infer that phase-space area is unchanged: \(\Delta y\,\Delta p_y=\Delta x\,\Delta p_x\).

Magnetic action to magnetic Lagrangian
1. Start from the free-particle action \(\int \frac12 mv^2\,dt\).
2. Add the magnetic coupling as a line integral \(q\int A_i\,dx_i\).
3. Write \(dx_i=\dot x_i\,dt\).
4. Convert the action to \(\int (\frac12 m\dot x_i^2+qA_i\dot x_i)\,dt\).
5. Read off the Lagrangian \(L=\frac12 m\dot x_i^2+qA_i\dot x_i\).

Canonical momentum in a magnetic field
1. Take \(L=\frac12 m\dot x_i^2+qA_i\dot x_i\).
2. Differentiate with respect to \(\dot x\), \(\dot y\), \(\dot z\).
3. Obtain \(p_x=m\dot x+qA_x\), and similarly for \(y,z\).
4. Separate the mechanical part \(m\dot x_i\) from the full canonical momentum.

\(z\)-component Euler–Lagrange derivation
1. Start with \(\frac{d}{dt}\frac{\partial L}{\partial \dot z}=\frac{\partial L}{\partial z}\).
2. Compute \(\partial L/\partial \dot z=p_z=m\dot z+qA_z\).
3. Differentiate in time to get \(m\ddot z+q\dot A_z\).
4. On the right-hand side, differentiate only the \(A_i\)-dependent terms with respect to \(z\).
5. Obtain \(q\dot x\,\partial_z A_x+q\dot y\,\partial_z A_y+q\dot z\,\partial_z A_z\).
6. Expand \(\dot A_z\) by the chain rule as \(\partial_xA_z\,\dot x+\partial_yA_z\,\dot y+\partial_zA_z\,\dot z\).
7. Cancel the common \(q\dot z\,\partial_zA_z\) term on both sides.
8. Group the coefficients of \(\dot x\) and \(\dot y\).
9. Recognize \(\partial_zA_x-\partial_xA_z=B_y\) and \(\partial_zA_y-\partial_yA_z=-B_x\).
10. Conclude \(m\ddot z=q(v_xB_y-v_yB_x)\), the \(z\)-component of \(q\mathbf v\times\mathbf B\).

Hamiltonian and energy in velocity variables
1. Start from \(H=\sum_i p_i\dot x_i-L\).
2. Substitute \(p_i=m\dot x_i+qA_i\).
3. Multiply each \(p_i\) by the corresponding \(\dot x_i\).
4. Subtract \(L=\frac12 m\dot x_i^2+qA_i\dot x_i\).
5. Observe cancellation of the \(qA_i\dot x_i\) terms.
6. Retain only the kinetic term \(\frac12 m\dot x_i^2\).
7. Conclude \(H=\frac12 mv^2\) in velocity variables.
8. Interpret this as the statement that magnetic fields do no work.

Hamiltonian in canonical momenta
1. Solve \(p_i=m\dot x_i+qA_i\) for \(\dot x_i\).
2. Substitute \(\dot x_i=(p_i-qA_i)/m\) into the kinetic expression.
3. Obtain \(H=\frac{1}{2m}\sum_i (p_i-qA_i)^2\).
4. Note that this is the form appropriate for Hamilton’s equations.

## Notation Choices
- Use `Liouville` throughout, not transcript spellings such as `Leavill` or `Leoville`.
- Use \(H\) for the Hamiltonian and \(L\) for the Lagrangian; prefer \(L\) over \(\mathcal L\) in this lecture since the board evidence only weakly supports the calligraphic form.
- Use \((q_i,p_i)\) for general canonical coordinates in the Liouville part.
- Use \((x_i)\) or explicitly \((x,y,z)\) in the magnetic-particle section.
- Use overdot notation for time derivatives: \(\dot x_i\), \(\dot q_i\), \(\dot p_i\), \(\dot A_z\).
- Use \(p_i\) for canonical momentum and explicitly name \(m\dot x_i\) as `mechanical momentum` when contrast is needed.
- Use boldface vector notation for compact statements:
  \(\mathbf v\), \(\mathbf B\), \(\mathbf A\), \(\mathbf p\).
- Use indexed component notation for derivations:
  \(A_i\dot x_i\), \(A_i\,dx_i\), with implicit or explicit sum over \(i\).
- Normalize the divergence notation as
  \(\nabla\cdot\mathbf v\) or \(\sum_i \partial v_i/\partial x_i\).
- Normalize curl notation as \(\nabla\times\mathbf A\), not verbal “del cross A” in final notes.
- In the free-particle scaling example, use \(P_x\) only if mirroring the board moment; otherwise standardize to \(p_x\) in the body text.
- Treat Planck’s constant as an area scale in phase space, not as \(\Delta x\) or \(\Delta p\) separately.

## Uncertain Mathematics
- The transcript statement of the general \(n\)-dimensional incompressibility condition is garbled; the clean form \(\sum_i \partial v_i/\partial x_i=0\) is a standard normalization.
- The transcript around Hamilton’s second equation is noisy; normalize to \(\dot q_i=\partial H/\partial p_i\).
- The frame `lecture_07_figure_02.png` visibly supports \(L=\dot x^2/2\) and the start of \(P_x=\), but the full derivative chain is not fully visible.
- The frame `lecture_07_figure_03.png` supports the kinetic term and the start of \(+qA_i\), but not the full \(dx_i\) or \(\mathbf A\cdot d\mathbf x\) structure by itself.
- The frame `lecture_07_figure_04.png` securely supports the first term \(q\dot x\,\partial A_x/\partial z\), but the full three-term \(\partial L/\partial z\) line is reconstructed from the transcript.
- The component formulas for \(\mathbf v\times\mathbf B\) and \(\nabla\times\mathbf A\) are verbally self-corrected and partially garbled in the transcript; final notes should present the cleaned standard component identities, not the spoken false starts.
- The explicit reduction from the Euler–Lagrange equation to \(m\ddot z=q(\mathbf v\times\mathbf B)_z\) should be stated as a cautious standard reconstruction, though it is strongly transcript-backed in structure.
- The fully compact Hamiltonian
  \[
  H=\frac{1}{2m}(\mathbf p-q\mathbf A)^2
  \]
  is not cleanly spoken in final polished form in the transcript; it should be treated as the standard cleaned reconstruction of what he is deriving.
- The lecture mentions nonuniqueness of \(\mathbf A\) but does not develop the gauge transformation formula; do not add gauge machinery beyond the minimal statement unless another source in the workflow requires it.
- The entropy statement is heuristic and pedagogical: it should remain tied to detectable coarse-grained phase-space volume, not be turned into a more formal statistical-mechanics derivation than the lecture gives.