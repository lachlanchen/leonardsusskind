# Math Bank
## Core Equations
- \(\mathbf F=-\nabla U(\mathbf x)\) [transcript-backed]
- \(U(\mathbf x)=e\,V(\mathbf x)\) [transcript-backed]
- \(\nabla=(\partial_x,\partial_y,\partial_z)\) [standard reconstruction]
- \(\nabla s=(\partial_x s,\partial_y s,\partial_z s)\) [transcript-backed]
- \(\nabla\cdot \mathbf A=\partial_x A_x+\partial_y A_y+\partial_z A_z\) [transcript-backed]
- \((\mathbf V\times \mathbf A)_x=V_yA_z-V_zA_y\) [visible]
- \((\mathbf V\times \mathbf A)_y=V_zA_x-V_xA_z\) [transcript-backed]
- \((\mathbf V\times \mathbf A)_z=V_xA_y-V_yA_x\) [transcript-backed]
- \((\mathbf V\times \mathbf A)_i=\epsilon_{ijk}V_jA_k\) [transcript-backed]
- \(V_iA_j-V_jA_i=\epsilon_{ijk}(\mathbf V\times\mathbf A)_k\) [transcript-backed]
- \(M_{ij}=-M_{ji}\) [standard reconstruction]
- \((\nabla\times \mathbf A)_x=\partial_yA_z-\partial_zA_y\) [transcript-backed]
- \((\nabla\times \mathbf A)_i=\epsilon_{ijk}\partial_jA_k\) [transcript-backed]
- \(\nabla\cdot(\nabla\times \mathbf A)=0\) [transcript-backed]
- \(\nabla\times(\nabla s)=0\) [transcript-backed]
- \(\nabla\cdot \mathbf B=0\) [transcript-backed]
- \(\mathbf B=\nabla\times\mathbf A\) [visible]
- \(\mathbf A'=\mathbf A+\nabla s\) [visible]
- \(\mathbf F=-e\,\nabla V+\dfrac{e}{c}\,\mathbf v\times\mathbf B\) [transcript-backed]
- \(\mathbf F_{\mathrm{Cor}}=2m\,\mathbf v\times\boldsymbol\omega\) [transcript-backed]
- \(\mathbf A=(0,Bx,0)\) [transcript-backed]
- \(\mathbf A=(-By,0,0)\) [standard reconstruction]
- Lagrangian with no fields: \(L_0=\dfrac{m}{2}\dot{\mathbf x}^{\,2}\) [transcript-backed]
- Magnetic coupling term: \(L_{\mathrm{mag}}=\dfrac{e}{c}\,\mathbf A(\mathbf x)\cdot\dot{\mathbf x}\) [transcript-backed]
- Blackboard action form: \(A=\int \cdots\,dt\) [visible]
- Clean action form: \(A=\int L\,dt\) [standard reconstruction]
- Final normalized action notation: \(S=\int L\,dt\) [standard reconstruction]
- Magnetic contribution to the action:
  \[
  \frac{e}{c}\int A_i\,\dot x^i\,dt
  \]
  [transcript-backed]
- Same term as a line integral:
  \[
  \frac{e}{c}\int A_i\,dx^i
  \]
  [transcript-backed]
- Gauge-induced change of the magnetic action term:
  \[
  \Delta S=\frac{e}{c}\int \partial_i s\,dx^i
  \]
  [standard reconstruction]
- Endpoint form of that change:
  \[
  \Delta S=\frac{e}{c}\bigl[s(\text{final})-s(\text{initial})\bigr]
  \]
  [standard reconstruction]

## Definitions And Objects
- Field: a quantity depending on space and time.
- Scalar field: a field with no directional components; lecture examples are temperature and pressure.
- Vector field: a field with magnitude and direction; lecture examples are wind velocity, electric field, magnetic field.
- Local measurability: to determine a field at a region, the experiment is performed in that region.
- Del / nabla: a “fake vector” of derivative operators acting on fields, not a geometric vector with magnitude and direction.
- Gradient: del acting on a scalar field, producing a vector field.
- Divergence: dot product of del with a vector field, producing a scalar field.
- Curl: cross product of del with a vector field, producing a vector field in three dimensions.
- Kronecker delta:
  \[
  \delta_{ij}=
  \begin{cases}
  1,& i=j\\
  0,& i\neq j
  \end{cases}
  \]
- Levi-Civita symbol \(\epsilon_{ijk}\): antisymmetric symbol taking values \(0,\pm 1\), zero when any two indices coincide.
- Antisymmetric matrix / 2-form viewpoint of the cross product: in three dimensions the antisymmetric object has three independent components, matching a vector.
- Vector potential \(\mathbf A\): a vector field whose curl is the magnetic field.
- Gauge transformation: replacement \(\mathbf A\mapsto \mathbf A+\nabla s\) with no change in \(\mathbf B\).
- Scalar potential \(V\): electrostatic potential; potential energy is \(U=eV\).
- Action: integral along the trajectory of the Lagrangian; Susskind writes it temporarily as \(A\) on the board.
- Lagrangian: a scalar function of positions and velocities, \(L=L(\mathbf x,\dot{\mathbf x})\).
- Line integral term: the magnetic action contribution is the integral of the component of \(\mathbf A\) along the trajectory.

## Derivation Steps
Cross product to Levi-Civita notation
1. Start from the component formulas for \((\mathbf V\times\mathbf A)_x\), \((\mathbf V\times\mathbf A)_y\), \((\mathbf V\times\mathbf A)_z\).
2. Encode the cyclic sign pattern with \(\epsilon_{ijk}\).
3. Sum over repeated \(j,k\).
4. Obtain \((\mathbf V\times\mathbf A)_i=\epsilon_{ijk}V_jA_k\).

Curl from cross product
1. Replace the first vector in \(\mathbf V\times\mathbf A\) by \(\nabla\).
2. Replace \(V_j\) by \(\partial_j\).
3. Read off the \(x\)-component:
   \[
   (\nabla\times\mathbf A)_x=\partial_yA_z-\partial_zA_y.
   \]
4. Cycle indices for the remaining components.
5. Summarize as \((\nabla\times\mathbf A)_i=\epsilon_{ijk}\partial_jA_k\).

Divergence of a curl
1. Begin with \(\nabla\cdot(\nabla\times\mathbf A)\).
2. Write out the components explicitly.
3. Pair terms with opposite signs.
4. Use equality of mixed partial derivatives.
5. Conclude the total sum is zero.

Curl of a gradient
1. Begin with \(\nabla\times(\nabla s)\).
2. Write the \(i\)-th component as \(\epsilon_{ijk}\partial_j\partial_k s\).
3. Exchange \(j\) and \(k\).
4. Use symmetry of mixed partials and antisymmetry of \(\epsilon_{ijk}\).
5. Conclude the result is zero.

Magnetic field as a curl
1. Use the physical input \(\nabla\cdot\mathbf B=0\).
2. Invoke the lecture’s divergence-free \(\Rightarrow\) curl statement.
3. Introduce a vector field \(\mathbf A\) such that \(\mathbf B=\nabla\times\mathbf A\).
4. Treat the converse as mathematically harder than the easy identity \(\nabla\cdot(\nabla\times\mathbf A)=0\).

Gauge invariance of \(\mathbf B\)
1. Define \(\mathbf A'=\mathbf A+\nabla s\).
2. Take the curl:
   \[
   \nabla\times\mathbf A'=\nabla\times\mathbf A+\nabla\times(\nabla s).
   \]
3. Use \(\nabla\times(\nabla s)=0\).
4. Conclude \(\nabla\times\mathbf A'=\nabla\times\mathbf A=\mathbf B\).

Uniform \(B\hat z\) from one vector potential
1. Choose \(A_x=0\), \(A_y=Bx\), \(A_z=0\).
2. Compute the curl.
3. The only nonzero derivative is \(\partial_xA_y=B\).
4. The \(z\)-component of the curl is \(B_z=\partial_xA_y-\partial_yA_x=B\).
5. The \(x\)- and \(y\)-components vanish.

Uniform \(B\hat z\) from a second vector potential
1. Choose \(A_x=-By\), \(A_y=0\), \(A_z=0\).
2. Compute the curl.
3. The only nonzero derivative is \(\partial_yA_x=-B\).
4. Then \(B_z=\partial_xA_y-\partial_yA_x=0-(-B)=B\).
5. The \(x\)- and \(y\)-components vanish.

Why the magnetic term in \(L\) uses \(\mathbf A\), not \(\mathbf B\)
1. The Lagrangian must be a scalar.
2. The magnetic force is proportional to charge and to velocity.
3. A scalar linear in velocity is naturally a dot product with another vector field.
4. Trying \(\mathbf B\cdot\dot{\mathbf x}\) gives the wrong structure in the equations of motion.
5. The lecture’s advocated choice is \(\mathbf A\cdot\dot{\mathbf x}\).

Magnetic action term as a line integral
1. Start from the Lagrangian term \(\dfrac{e}{c}A_i\dot x^i\).
2. Insert it into the action integral:
   \[
   \frac{e}{c}\int A_i\dot x^i\,dt.
   \]
3. Use \(\dot x^i=dx^i/dt\).
4. Cancel \(dt\).
5. Rewrite the term as \(\dfrac{e}{c}\int A_i\,dx^i\).

Gauge change of the action
1. Replace \(A_i\) by \(A_i+\partial_i s\) in the magnetic action term.
2. The change is
   \[
   \Delta S=\frac{e}{c}\int \partial_i s\,dx^i.
   \]
3. Recognize \(\partial_i s\,dx^i\) as the total differential \(ds\).
4. Integrate along the path.
5. Obtain \(\Delta S=\dfrac{e}{c}[s_f-s_i]\).

Why the equations of motion are unchanged under gauge transformation
1. The action changes only by an endpoint term.
2. In the action principle the endpoints are held fixed.
3. Endpoint values do not change when the interior path is varied.
4. Therefore the extra term contributes nothing to the Euler-Lagrange variation.
5. The equations of motion and physical trajectory are gauge invariant.

## Notation Choices
- Use \(\mathbf A\) for the vector potential and \(\mathbf B\) for the magnetic field.
- Use \(S\) for the action in the final notes, even though the lecture briefly writes \(A\) on the board.
- Use lowercase \(e\) for electric charge, not transcript-style capital \(E\).
- Reserve \(V\) for scalar potential and \(U=eV\) for potential energy.
- Use lowercase \(\mathbf v\) for particle velocity to avoid confusion with \(V\).
- Use \(\nabla\) rather than spelling out “del” once the notation is established.
- Use indices \(i,j,k\in\{1,2,3\}\), with \(1,2,3\leftrightarrow x,y,z\) when matching the lecture.
- Use Einstein summation convention only where it clarifies formulas already motivated in the lecture.
- Write \(\partial_i\equiv \partial/\partial x^i\).
- Treat cross product and curl as explicitly three-dimensional objects in the chapter body.
- When discussing the antisymmetric-matrix viewpoint, write it as an antisymmetric tensor or matrix, not as a literal board doodle.
- For the uniform-field example, write the field as \(\mathbf B=B\,\hat{\mathbf z}\) when convenient, with \(B\) the constant magnitude.
- For the magnetic action term, use both forms
  \[
  \frac{e}{c}\int A_i\dot x^i\,dt
  \qquad\text{and}\qquad
  \frac{e}{c}\int A_i\,dx^i
  \]
  since the lecture explicitly moves from the first to the second.

## Uncertain Mathematics
- The converse statements “divergence-free implies curl” and “curl-free implies gradient” should be stated locally or with a mild domain assumption; the lecture suppresses topology.
- The transcript around the alternative two-index cross-product formula is slightly rough, but the mathematically clean identity
  \[
  V_iA_j-V_jA_i=\epsilon_{ijk}(\mathbf V\times\mathbf A)_k
  \]
  matches the lecture’s point and can be used cautiously.
- The second uniform-\(B\hat z\) gauge choice is not written cleanly in the transcript; \(\mathbf A=(-By,0,0)\) is the cautious reconstruction that matches the curl computation.
- The action formula is only partially visible in the frame; \(A=\int L\,dt\) is transcript-backed but not fully image-legible.
- The transcript around 01:15 is garbled; keep only the clear claim that suitably chosen electric and magnetic fields can cancel fictitious rotating-frame forces for one chosen charge.
- The transcript around 01:32 is garbled; the endpoint-term derivation should be reconstructed only up to the secure statement that \(\int \partial_i s\,dx^i=s_f-s_i\).
- The lecture occasionally blurs “least action” and “stationary action”; the final notes should mention the distinction once, then proceed with stationary-action mathematics.
- The lecture’s spoken comments about whether one may add “a constant” to \(\mathbf A\) should not be separated from the gauge discussion; in ordinary \(\mathbb R^3\) this is already included within the broader zero-curl ambiguity.