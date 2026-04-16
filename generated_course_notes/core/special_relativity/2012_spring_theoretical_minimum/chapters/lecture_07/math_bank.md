# Math Bank
## Core Equations
- \(ds=\partial_\mu s\,dX^\mu\) `[transcript-backed]`
- \(X_\mu X^\mu=x^2+y^2+z^2-t^2\) `[transcript-backed]`
- \(I=\int dt\,L(X,\dot X)\) for a particle system `[transcript-backed]`
- \(I=\int d^4x\,\mathcal L(\phi,\partial_\mu\phi)\) for a field theory `[transcript-backed]`
- \(m\mathbf a=e\left(\mathbf E+\mathbf v\times\mathbf B\right)\) `[visible]`
- \(I_{\text{particle}}=-m\int d\tau-e\int A_\mu\,dX^\mu\) `[transcript-backed]`
- \(\dfrac{d\tau}{dt}=\sqrt{1-\dot X^2}\) `[transcript-backed]`
- \(\dot X^2=\dot x^2+\dot y^2+\dot z^2\) `[transcript-backed]`
- \(L=-m\sqrt{1-\dot X^2}-e\left(A_0(x,t)+A_m(x,t)\dot X^m\right)\) `[transcript-backed]`
- \(\dfrac{\partial L}{\partial \dot X^m}=\dfrac{m\dot X^m}{\sqrt{1-\dot X^2}}-eA_m\) `[transcript-backed]`
- \(\dfrac{d}{dt}\dfrac{\partial L}{\partial \dot X^m}=\dfrac{\partial L}{\partial X^m}\) `[transcript-backed]`
- \(\dfrac{\partial L}{\partial X^m}=-e\,\partial_m A_0-e\,(\partial_m A_n)\dot X^n\) `[transcript-backed]`
- \(E_m:=\partial_0A_m-\partial_mA_0\) `[transcript-backed]`
- \(B^i=(\nabla\times\mathbf A)^i\) `[transcript-backed]`
- \((\mathbf v\times\mathbf B)_m=(\partial_nA_m-\partial_mA_n)\dot X^n\) `[standard reconstruction]`
- \(U^\mu=\dfrac{dX^\mu}{d\tau}\) `[transcript-backed]`
- \(m\,\dfrac{dU^\mu}{d\tau}=e\,F^\mu{}_{\nu}U^\nu\) `[standard reconstruction]`
- \(F_{\mu\nu}=\partial_\nu A_\mu-\partial_\mu A_\nu\) `[standard reconstruction]`
- \(F_{\mu\nu}=-F_{\nu\mu}\) `[transcript-backed]`
- \(F_{\mu\nu}=
\begin{pmatrix}
0 & -E_x & -E_y & -E_z\\
E_x & 0 & B_z & -B_y\\
E_y & -B_z & 0 & B_x\\
E_z & B_y & -B_x & 0
\end{pmatrix}\) `[standard reconstruction]`
- \(\partial_t^2\phi-\nabla^2\phi=0\) `[transcript-backed]`
- \(\mathcal L_\phi=-\dfrac12\,\partial_\mu\phi\,\partial^\mu\phi\) `[standard reconstruction]`
- \(\partial_t^2\phi-\nabla^2\phi+\mu^2\phi=0\) `[transcript-backed]`
- \(\mathcal L_{\phi,\mu}=-\dfrac12\,\partial_\mu\phi\,\partial^\mu\phi-\dfrac{\mu^2}{2}\phi^2\) `[standard reconstruction]`
- \(A_\mu\to A_\mu+\partial_\mu S\) `[transcript-backed]`
- \(\int \partial_\mu S\,dX^\mu=S(2)-S(1)\) `[transcript-backed]`
- \(\delta F_{\mu\nu}=\partial_\nu\partial_\mu S-\partial_\mu\partial_\nu S=0\) `[transcript-backed]`

## Definitions And Objects
- \(X^\mu=(t,x,y,z)\), with \(\mu,\nu=0,1,2,3\).
- Spatial indices \(m,n=1,2,3\).
- A repeated upper-lower index means summation.
- Coordinates and coordinate differences are carried with upper indices in the lecture recap.
- Derivatives with respect to coordinates are carried with lower indices.
- Lowering an index changes the sign of the time component and leaves spatial components unchanged.
- \(A_\mu\) is the electromagnetic four-vector potential.
- \(A_0\) is the time component of the vector potential; \(A_m\) are the spatial components.
- \(\mathbf A\) is the spatial three-vector potential used when taking curl.
- \(d\tau\) is proper time along the particle worldline.
- \(U^\mu=dX^\mu/d\tau\) is the four-velocity.
- \(dU^\mu/d\tau\) is the proper-acceleration four-vector.
- \(F_{\mu\nu}\) is the antisymmetric electromagnetic field tensor.
- Mixed space-time components of \(F_{\mu\nu}\) encode electric field; space-space components encode magnetic field.
- Gauge transformation means adding the four-gradient of a scalar to \(A_\mu\).
- Gauge-invariant quantities are the physically meaningful ones in this lecture’s formulation.

## Derivation Steps
From worldline action to ordinary-time Lagrangian

1. Start from \(I_{\text{particle}}=-m\int d\tau-e\int A_\mu\,dX^\mu\).
2. Rewrite the first term as \(-m\int (d\tau/dt)\,dt\).
3. Use \(d\tau/dt=\sqrt{1-\dot X^2}\).
4. Rewrite the interaction term as \(-e\int A_\mu(dX^\mu/dt)\,dt\).
5. Use \(dX^0/dt=1\) and \(dX^m/dt=\dot X^m\).
6. Read off \(L=-m\sqrt{1-\dot X^2}-e(A_0+A_m\dot X^m)\).

Euler-Lagrange recovery of the Lorentz force

1. Compute \(\partial L/\partial\dot X^m=m\dot X^m/\sqrt{1-\dot X^2}-eA_m\).
2. Differentiate with respect to \(t\): \(d/dt(\partial L/\partial\dot X^m)=m\,dU^m/dt-e\,dA_m/dt\).
3. Expand \(dA_m/dt\) by the chain rule: \(dA_m/dt=\partial_0A_m+(\partial_nA_m)\dot X^n\).
4. Compute \(\partial L/\partial X^m=-e\,\partial_mA_0-e\,(\partial_mA_n)\dot X^n\).
5. Set \(d/dt(\partial L/\partial\dot X^m)=\partial L/\partial X^m\).
6. Move terms to the right-hand side and group the velocity-independent terms into \(\partial_0A_m-\partial_mA_0\).
7. Group the velocity-dependent terms into \((\partial_nA_m-\partial_mA_n)\dot X^n\).
8. Identify the first group as \(E_m\).
9. Identify the second group as the \(m\)-component of \(\mathbf v\times\mathbf B\).

Proper-time rewrite and covariant packaging

1. Recognize \(m\dot X^m/\sqrt{1-\dot X^2}=mU^m\).
2. The left-hand side is \(m\,dU^m/dt\), not yet a proper-time derivative.
3. Use \(dU^m/dt=(dU^m/d\tau)(d\tau/dt)\).
4. Multiply the equation by \(dt/d\tau\).
5. Convert \(\dot X^n(dt/d\tau)\) into \(dX^n/d\tau=U^n\).
6. Obtain the spatial equation \(m\,dU^m/d\tau=e\,F_{m\nu}U^\nu\).
7. Promote it to a four-vector equation by Lorentz invariance.

Free scalar-field invariance example

1. Start from the free wave equation \(\partial_t^2\phi-\nabla^2\phi=0\).
2. Replace \(\phi\) by \(\phi+c\), with \(c\) constant.
3. Derivatives of \(c\) vanish, so the equation of motion is unchanged.
4. In the action, a Lagrangian built only from derivatives of \(\phi\) is likewise unchanged.
5. Conclude that constant shifts are a symmetry of the free scalar theory.

Loss of invariance with a mass term

1. Add the term \(\mu^2\phi\) to the equation of motion, equivalently a \(\phi^2\) term to the Lagrangian.
2. Replace \(\phi\) by \(\phi+c\).
3. The derivative terms remain unchanged.
4. The \(\mu^2\phi\) or \(\phi^2\) term changes.
5. Conclude that the constant-shift invariance is broken.

Total-derivative lesson from \(\phi\to\phi+x\)

1. Consider replacing \(\phi(x,t)\) by \(\phi(x,t)+x\).
2. Second derivatives of \(x\) vanish, so the wave equation still holds.
3. The Lagrangian changes by a constant term and a total \(x\)-derivative term.
4. A constant added to the Lagrangian is irrelevant.
5. A total derivative contributes only boundary terms after integration.
6. This is the local warm-up for gauge invariance.

Gauge invariance from the action

1. Apply \(A_\mu\to A_\mu+\partial_\mu S\).
2. The interaction action changes by \(-e\int \partial_\mu S\,dX^\mu\).
3. Recognize \(\partial_\mu S\,dX^\mu=dS\) along the worldline.
4. Integrate to \(-e[S(2)-S(1)]\).
5. Endpoint terms do not affect the stationary-action problem with fixed endpoints.
6. Conclude that the particle dynamics are unchanged.

Gauge invariance of the field tensor

1. Start from \(F_{\mu\nu}=\partial_\nu A_\mu-\partial_\mu A_\nu\).
2. Under \(A_\mu\to A_\mu+\partial_\mu S\), compute \(\delta F_{\mu\nu}\).
3. Get \(\delta F_{\mu\nu}=\partial_\nu\partial_\mu S-\partial_\mu\partial_\nu S\).
4. Use commutativity of partial derivatives.
5. Conclude \(\delta F_{\mu\nu}=0\).

## Notation Choices
- Use \(X^\mu\) for spacetime coordinates and \(X^0=t\).
- Use \(m,n\) only for spatial indices.
- Use \(\partial_\mu:=\partial/\partial X^\mu\), with \(\partial_0=\partial/\partial t\).
- Use \(\dot X^m=dX^m/dt\) and \(\dot X^2=\sum_{m=1}^3(\dot X^m)^2\).
- Use \(U^\mu=dX^\mu/d\tau\) for four-velocity; avoid switching between \(u^\mu\), \(u_m\), and \(x_m\)-dot in the final notes.
- Use \(I\) for the action and reserve \(S(X)\) for the gauge scalar, since the lecture uses “action” and later uses \(S\) as the gauge function.
- Use \(A_\mu(X)\) when the spacetime dependence matters and \(A_0, A_m\) when discussing components.
- Use boldface \(\mathbf E,\mathbf B,\mathbf A,\mathbf v,\mathbf a\) for three-vectors.
- Use \(F_{\mu\nu}=\partial_\nu A_\mu-\partial_\mu A_\nu\) consistently, so that \(F_{0m}=-E_m\) and \(F_{m0}=E_m\).
- Do not lean on mixed-index antisymmetry in the final notes; keep tensor statements mostly with both indices up or both down.
- Use \(c=1\) units throughout.
- For the scalar-field warm-up, use \(\mu\) as the mass parameter and not as a tensor index in the same displayed equation.

## Uncertain Mathematics
- The derivative discussion around 00:11–00:12 is garbled in the transcript. Keep only the secure statements: derivatives carry lower indices, and raising/lowering flips the time sign.
- The lecture hesitates over the sign and order in the definition of \(F_{\mu\nu}\). The final notes must choose one convention and derive all \(E\)- and \(B\)-identifications from it.
- The sign connecting \(A_0\) to the ordinary scalar potential is not stabilized explicitly in the lecture. Do not import an external convention silently.
- The exact matrix entries for mixed-index versions such as \(F^\mu{}_{\nu}\) are not reliable from the spoken discussion; only the all-lower or all-upper antisymmetric tensor should be treated as secure.
- The equality \((\partial_nA_m-\partial_mA_n)\dot X^n=(\mathbf v\times\mathbf B)_m\) is asserted before being checked in detail. It is safe as a standard vector-calculus identity, but it is not derived line by line in the lecture.
- The free scalar-field Lagrangian normalization and overall sign are spoken loosely. The final notes should normalize them conventionally and not claim that the lecture fixed the prefactor carefully.
- The theorem that no Lorentz-invariant local action for a charged particle can be written directly in terms of \(\mathbf E\) and \(\mathbf B\) is asserted but not proved.
- The lecture’s discussion of one-upper/one-lower versions of the field tensor becomes uncertain near 01:13–01:14. That part should be stated cautiously or omitted.
- The lecture says \(A_\mu\) is not measurable and only gauge-invariant features are measurable. In the final notes, do not expand this with later quantum subtleties unless another lecture motivates them.
- The board and transcript sometimes alternate between bare \(A_0,A_m\) and explicit \(A_0(x,t),A_m(x,t)\). The final notes should standardize this without pretending the lecture was typographically consistent.