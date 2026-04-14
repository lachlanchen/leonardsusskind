# Math Bank
## Core Equations
- \(\mathbf{F}=-\nabla U\) [visible]
- \(\mathbf{B}=\nabla\times\mathbf{A}\) [visible]
- \(\mathbf{E}=-\nabla V\) [transcript-backed]
- \(U=qV\) [visible]
- \(m\ddot{\mathbf{x}}=q\mathbf{E}+q\,\dot{\mathbf{x}}\times\mathbf{B}\) [transcript-backed]
- \(\mathbf{v}\cdot(\mathbf{v}\times\mathbf{B})=0\) [standard reconstruction]
- \(S=\int \frac12 m(\dot x^2+\dot y^2)\,dt+q\int A_i\,dx_i-q\int V\,dt\) [standard reconstruction]
- \(S=\int\left[\frac12 m(\dot x^2+\dot y^2)+qA_i\dot x_i-qV\right]dt\) [standard reconstruction]
- \(L=\frac12 m(\dot x^2+\dot y^2)+qA_i\dot x_i-qV\) [standard reconstruction]
- \(L=\frac12 m(\dot x^2+\dot y^2)+q\,\mathbf{A}\cdot\mathbf{v}-qV\) [standard reconstruction]
- \(\mathbf{A}\to\mathbf{A}+\nabla\lambda\) [transcript-backed]
- \(\nabla\times(\nabla\lambda)=0\) [transcript-backed]
- \(\frac{d}{dt}\frac{\partial L}{\partial \dot x}=\frac{\partial L}{\partial x}\) [transcript-backed]
- \(p_x=\frac{\partial L}{\partial \dot x}=m\dot x+qA_x\) [transcript-backed]
- \(\frac{dA_x}{dt}=\frac{\partial A_x}{\partial x}\dot x+\frac{\partial A_x}{\partial y}\dot y\) [transcript-backed]
- \(B_z=\frac{\partial A_y}{\partial x}-\frac{\partial A_x}{\partial y}\) [transcript-backed]
- \(A_x=By,\quad A_y=0\) [transcript-backed]
- \(A_x=0,\quad A_y=-Bx\) [transcript-backed]
- \(p_x=m\dot x+qBy\) [transcript-backed]
- \(p_y=m\dot y-qBx\) [transcript-backed]
- \(\dot x=-\frac{qB}{m}y\) [transcript-backed]
- \(\dot y=\frac{qB}{m}x\) [transcript-backed]
- \(x=r\cos(\omega t),\quad y=r\sin(\omega t)\) [transcript-backed]
- \(\omega=-\frac{qB}{m}\) [transcript-backed]
- \(p_x=qB\,y_0\) [transcript-backed]
- \(p_y=-qB\,x_0\) [transcript-backed]
- \(m\ddot x+qB\,\dot y=qE\) [transcript-backed]
- \(m\ddot y-qB\,\dot x=0\) [transcript-backed]
- \(\dot x=0,\quad \dot y=\frac{E}{B}\) [transcript-backed]
- \(\dot q_i=\frac{\partial H}{\partial p_i},\quad \dot p_i=-\frac{\partial H}{\partial q_i}\) [standard reconstruction]
- \(\{A,B\}=\sum_i\left(\frac{\partial A}{\partial q_i}\frac{\partial B}{\partial p_i}-\frac{\partial A}{\partial p_i}\frac{\partial B}{\partial q_i}\right)\) [transcript-backed]
- \(\dot A=\{A,H\}\) [standard reconstruction]
- \(\{A,B\}=-\{B,A\}\) [transcript-backed]
- \(\{q_i,p_j\}=\delta_{ij}\) [transcript-backed]
- \(\{p_i,q_j\}=-\delta_{ij}\) [standard reconstruction]
- \(\{q_i,q_j\}=0\) [transcript-backed]
- \(\{p_i,p_j\}=0\) [transcript-backed]
- \(\{P,F\}=-\frac{\partial F}{\partial Q}\) [transcript-backed]
- \(\{Q,F\}=\frac{\partial F}{\partial P}\) [transcript-backed]
- \(\{\alpha A,B\}=\alpha\{A,B\}\) [transcript-backed]
- \(\{A+C,B\}=\{A,B\}+\{C,B\}\) [transcript-backed]
- \(\{AB,C\}=A\{B,C\}+B\{A,C\}\) [transcript-backed]

## Definitions And Objects
- External-field setup: the electric and magnetic fields are treated as given background fields, taken to be time-independent for this lecture.
- Equations of motion: second-order differential equations for coordinates, with \(F=ma\) as the baseline form.
- Principle of least action: the underlying variational principle from which the Euler-Lagrange equations are derived.
- Lagrangian form: equations obtained from \(L(q,\dot q)\) by Euler-Lagrange variation.
- Hamiltonian form: phase-space formulation in terms of \(p\) and \(q\), emphasized as less intuitive but structurally powerful.
- Lorentz force law: the electromagnetic force \(q\mathbf{E}+q\,\mathbf{v}\times\mathbf{B}\).
- Vector potential \(\mathbf{A}\): a vector field with \(\mathbf{B}=\nabla\times\mathbf{A}\).
- Electric potential \(V\): scalar field with \(\mathbf{E}=-\nabla V\).
- Potential energy \(U\): for a charge \(q\), \(U=qV\).
- Gauge transformation: change \(\mathbf{A}\to\mathbf{A}+\nabla\lambda\) leaving \(\mathbf{B}\) unchanged.
- Gauge invariance: redundancy of description in which the equations of motion do not depend on the particular \(\mathbf{A}\) chosen.
- Canonical momentum: \(p_i=\partial L/\partial \dot x_i\), not identical to mechanical momentum in a magnetic field.
- Cyclotron frequency: angular frequency \(\omega=qB/m\) up to sign convention.
- Phase space: space of canonical coordinates and momenta \((q_i,p_i)\).
- Poisson bracket: antisymmetric bilinear operation on phase-space functions controlling Hamiltonian time evolution.
- Kronecker delta \(\delta_{ij}\): equals \(1\) for \(i=j\) and \(0\) otherwise.

## Derivation Steps
Electric potential and potential energy:
1. Start from the electric-force part of the Lorentz law: force is \(q\mathbf{E}\).
2. Treat the electric force as conservative.
3. Write \(\mathbf{F}=-\nabla U\).
4. Since \(\mathbf{F}=q\mathbf{E}\), define \(\mathbf{E}=-\nabla V\).
5. Conclude \(U=qV\).

Action to Lagrangian form:
1. Begin with kinetic term \(\int \frac12 m(\dot x^2+\dot y^2)\,dt\).
2. Add scalar-potential term \(-q\int V\,dt\).
3. Add magnetic coupling \(q\int A_i\,dx_i\).
4. Replace \(dx_i\) by \(\dot x_i\,dt\).
5. Read off \(L=\frac12 m(\dot x^2+\dot y^2)+qA_i\dot x_i-qV\).
6. Rewrite \(A_i\dot x_i\) as \(\mathbf{A}\cdot\mathbf{v}\).

Gauge invariance of the magnetic field:
1. Take \(\mathbf{A}\to\mathbf{A}+\nabla\lambda\).
2. In components, \(A_i\to A_i+\partial_i\lambda\).
3. For the planar setup, write \(B_z=\partial_xA_y-\partial_yA_x\).
4. Under the transformation, the change in \(B_z\) is \(\partial_x\partial_y\lambda-\partial_y\partial_x\lambda\).
5. Mixed partial derivatives commute.
6. The extra terms cancel, so \(B_z\) is unchanged.

\(x\)-component Euler-Lagrange derivation of the Lorentz force:
1. Compute \(p_x=\partial L/\partial\dot x=m\dot x+qA_x\).
2. Differentiate with respect to time: \(\dot p_x=m\ddot x+q\,dA_x/dt\).
3. Expand \(dA_x/dt\) using spatial dependence: \(dA_x/dt=(\partial_xA_x)\dot x+(\partial_yA_x)\dot y\).
4. Compute \(\partial L/\partial x=q(\partial_xA_x)\dot x+q(\partial_xA_y)\dot y-q\,\partial_xV\).
5. Apply Euler-Lagrange: \(m\ddot x+q(\partial_xA_x)\dot x+q(\partial_yA_x)\dot y=q(\partial_xA_x)\dot x+q(\partial_xA_y)\dot y-q\,\partial_xV\).
6. Cancel the \((\partial_xA_x)\dot x\) terms.
7. Recognize \(\partial_xA_y-\partial_yA_x=B_z\).
8. Use \(-\partial_xV=E_x\).
9. Obtain \(m\ddot x=qE_x+qB_z\dot y\), the \(x\)-component of the Lorentz force.

Conservation laws in the first gauge:
1. Choose \(A_x=By,\ A_y=0\), and temporarily set the electric field to zero.
2. Then \(L=\frac12 m(\dot x^2+\dot y^2)+qBy\,\dot x\).
3. Compute \(p_x=\partial L/\partial\dot x=m\dot x+qBy\).
4. Observe that \(L\) does not depend on \(x\).
5. Conclude \(p_x\) is conserved.
6. In the special case \(p_x=0\), solve for \(\dot x=-(qB/m)y\).

Conservation laws in the second gauge:
1. Choose \(A_x=0,\ A_y=-Bx\), again with zero electric field.
2. Then \(L=\frac12 m(\dot x^2+\dot y^2)-qBx\,\dot y\).
3. Compute \(p_y=\partial L/\partial\dot y=m\dot y-qBx\).
4. Observe that \(L\) does not depend on \(y\).
5. Conclude \(p_y\) is conserved.
6. In the special case \(p_y=0\), solve for \(\dot y=(qB/m)x\).

Circular motion from the conserved-quantity equations:
1. Combine \(\dot x=-(qB/m)y\) and \(\dot y=(qB/m)x\).
2. Recognize the form of uniform circular motion.
3. Use the ansatz \(x=r\cos(\omega t)\), \(y=r\sin(\omega t)\).
4. Differentiate to get \(\dot x=-r\omega\sin(\omega t)\), \(\dot y=r\omega\cos(\omega t)\).
5. Rewrite as \(\dot x=-\omega y\), \(\dot y=\omega x\).
6. Compare with the conserved-quantity equations.
7. Identify \(\omega=-qB/m\) up to orientation/sign convention.

Guiding-center interpretation:
1. Shift the circular orbit to center \((x_0,y_0)\).
2. Write \(x=x_0+r\cos(\omega t)\), \(y=y_0+r\sin(\omega t)\).
3. Keep \(\dot x,\dot y\) unchanged by the shift.
4. Substitute into \(p_x=m\dot x+qBy\) and use \(\omega=-qB/m\).
5. Time-dependent terms cancel.
6. Conclude \(p_x=qB\,y_0\).
7. Repeat in the second gauge to get \(p_y=-qB\,x_0\).
8. Interpret the conserved canonical momenta as the fixed center coordinates of the orbit.

Hall-drift solution:
1. Reintroduce an electric field in the \(x\)-direction.
2. Keep the two first-order equations in the form \(m\ddot x+qB\,\dot y=qE\) and \(m\ddot y-qB\,\dot x=0\).
3. Look for a solution with no acceleration: \(\ddot x=\ddot y=0\).
4. The second equation gives \(\dot x=0\).
5. The first equation then gives \(qB\,\dot y=qE\).
6. Cancel \(q\) and solve \(\dot y=E/B\).
7. Conclude the distinguished drift is perpendicular to the applied electric field.

Poisson-bracket time evolution:
1. Take any phase-space function \(A(q_i,p_i)\) with no explicit time dependence.
2. Differentiate along a trajectory: \(\dot A=\sum_i (\partial A/\partial q_i)\dot q_i+\sum_i (\partial A/\partial p_i)\dot p_i\).
3. Insert Hamilton’s equations \(\dot q_i=\partial H/\partial p_i\), \(\dot p_i=-\partial H/\partial q_i\).
4. Rearrange terms into the antisymmetric combination
   \(\sum_i \left(\frac{\partial A}{\partial q_i}\frac{\partial H}{\partial p_i}-\frac{\partial A}{\partial p_i}\frac{\partial H}{\partial q_i}\right)\).
5. Identify this combination as \(\{A,H\}\).
6. Conclude \(\dot A=\{A,H\}\).

## Notation Choices
- Use \(\mathbf{x}\) for the particle position and \(\mathbf{v}=\dot{\mathbf{x}}\) for velocity.
- Use boldface for vectors: \(\mathbf{E},\mathbf{B},\mathbf{A},\mathbf{F},\mathbf{v}\).
- Use \(x,y\) for planar coordinates and \(B_z\) for the out-of-plane magnetic component.
- Use lowercase \(q\) for charge in the final notes, even though the lecture often says “capital \(Q\)” aloud.
- Use \(V\) for electric potential and \(U\) for potential energy; do not let \(V\) double as velocity in final notation.
- Use \(A_i\dot x_i\) and \(\mathbf{A}\cdot\mathbf{v}\) interchangeably, but normalize displayed formulas to one form locally.
- Use \(\nabla\times\mathbf{A}\) and \(\nabla V\) for curl and gradient; in components write \(B_z=\partial_xA_y-\partial_yA_x\).
- Use the convention that the magnetic field points into the board in the planar examples; keep signs consistent with that choice.
- Omit explicit factors of \(c\) in the Lorentz force, matching the lecture’s unit convention; mention in prose that this is a units choice if needed.
- Use standard Hamiltonian sign conventions:
  \(\dot q_i=\partial H/\partial p_i\), \(\dot p_i=-\partial H/\partial q_i\).
- Use Poisson-bracket order \(\{q_i,p_j\}=\delta_{ij}\); then \(\{p_i,q_j\}=-\delta_{ij}\).

## Uncertain Mathematics
- The frame evidence for \(\mathbf{E}=-\nabla V\) is weaker than for \(\mathbf{B}=\nabla\times\mathbf{A}\) and \(U=qV\); keep it transcript-backed, not frame-only.
- The visible board formulas for the action/Lagrangian abbreviate the scalar-potential term; the final notes should keep the charge factor \(-qV\) even where the frame only suggests \(-V\).
- The transcript gives multiple equivalent gauge choices for uniform \(\mathbf B\), with sign flips between earlier examples and the later conservation-law derivation; use the later working pair consistently and note the equivalence.
- The circular-motion verification near 00:54 is garbled; only the cleaned ansatz, derivative comparison, and frequency identification should be reconstructed.
- The electric-potential sign for a field in the \(+x\)-direction is unstable in the transcript around 01:03–01:04; state the chosen \(V(x)\) convention carefully and keep \(\mathbf{E}=-\nabla V\) as the anchor.
- The Hall-drift direction sign depends on the sign of \(q\) and the orientation convention for \(\mathbf B\); the lecture’s main invariant takeaway is the transverse drift with speed magnitude \(E/B\).
- The transcript wobbles on Hamiltonian signs inside the Poisson-bracket section; the final notes should silently normalize to the standard signs.
- The lecture mentions the Hamiltonian of the charged particle but does not derive it in full; do not add a full Hamiltonian derivation here beyond what is explicitly motivated.