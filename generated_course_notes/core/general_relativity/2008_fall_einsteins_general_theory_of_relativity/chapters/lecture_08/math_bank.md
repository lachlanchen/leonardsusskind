# Math Bank
## Core Equations
- \((\nabla_\mu V)^\alpha = \partial_\mu V^\alpha + \Gamma^\alpha{}_{\mu\beta} V^\beta\) [transcript-backed]
- \(\nabla_\mu = \partial_\mu + \Gamma_\mu\), with \((\Gamma_\mu)^\alpha{}_\beta = \Gamma^\alpha{}_{\mu\beta}\) [transcript-backed]
- \([A,B] = AB - BA\) [transcript-backed]
- \([\partial_x, F(x)] = \partial_x F(x)\) [transcript-backed]
- \([\nabla_\nu,\nabla_\mu] = (\partial_\nu+\Gamma_\nu)(\partial_\mu+\Gamma_\mu)-(\partial_\mu+\Gamma_\mu)(\partial_\nu+\Gamma_\nu)\) [transcript-backed]
- \(\Delta V^\alpha = R^\alpha{}_{\beta\mu\nu} V^\beta\, \delta x^\nu dx^\mu\) [standard reconstruction]
- \(R^\alpha{}_{\beta\mu\nu} = \partial_\mu \Gamma^\alpha{}_{\nu\beta} - \partial_\nu \Gamma^\alpha{}_{\mu\beta} + \Gamma^\alpha{}_{\mu\delta}\Gamma^\delta{}_{\nu\beta} - \Gamma^\alpha{}_{\nu\delta}\Gamma^\delta{}_{\mu\beta}\) [standard reconstruction]
- \(R_{\nu\mu\alpha\beta} = -R_{\mu\nu\alpha\beta}\) [transcript-backed]
- \(R_{\nu\mu\alpha\beta} = -R_{\nu\mu\beta\alpha}\) [transcript-backed]
- \(R_{\nu\mu\alpha\beta} = R_{\alpha\beta\nu\mu}\) [transcript-backed]
- \((R_{\nu\mu})^\alpha{}_\beta \sim ([\nabla_\nu,\nabla_\mu])^\alpha{}_\beta\) [transcript-backed]
- \(R_{\mu\beta} = g^{\alpha\nu} R_{\mu\nu\alpha\beta}\) [standard reconstruction]
- \(R = g^{\mu\nu} R_{\mu\nu}\) [transcript-backed]
- \(d\tau^2 = g_{\mu\nu}\, dx^\mu dx^\nu\) [transcript-backed]
- \(\dfrac{d^2 x^\mu}{d\tau^2} + \Gamma^\mu{}_{\sigma\lambda}\dfrac{dx^\sigma}{d\tau}\dfrac{dx^\lambda}{d\tau} = 0\) [transcript-backed]
- \(g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}\), with \(|h_{\mu\nu}|\ll 1\) [transcript-backed]
- \(\dfrac{dx^0}{d\tau} \approx 1\), \(\dfrac{d^2 x}{d\tau^2} \approx \dfrac{d^2 x}{dt^2}\) [transcript-backed]
- \(\dfrac{d^2 x}{dt^2} \approx -\Gamma^x{}_{00}\) [transcript-backed]
- \(\Gamma^x{}_{00} \approx \dfrac12 g^{xx}\!\left(2\,\partial_0 g_{x0}-\partial_x g_{00}\right)\) [standard reconstruction]
- \(\dfrac{d^2 x}{dt^2} \approx -\dfrac12 \dfrac{\partial g_{00}}{\partial x}\) [transcript-backed]
- \(\dfrac{d^2 x}{dt^2} = -\dfrac{\partial \phi}{\partial x}\) [visible]
- \(g_{00} = 2\phi + c\) [transcript-backed]
- \(\nabla \cdot A = -4\pi G \rho\) [visible]
- \(\nabla^2 \phi = 4\pi G \rho\) [transcript-backed]
- \(\nabla^2 \phi = \dfrac{\partial^2 \phi}{\partial x^2} + \dfrac{\partial^2 \phi}{\partial y^2} + \dfrac{\partial^2 \phi}{\partial z^2}\) [visible]
- \(\rho \leftrightarrow T^{00}\) in units \(c=1\) [transcript-backed]
- \(\nabla^2 \phi = 4\pi G T^{00}\) [visible]
- \(\nabla^2 g_{00} = 8\pi G T^{00}\) [visible]
- \(A\,R_{\mu\nu} + B\,g_{\mu\nu} R = 8\pi G\, T_{\mu\nu}\) [transcript-backed]

## Definitions And Objects
- \(V^\alpha(x)\): components of a vector field, treated as a collection of functions on spacetime.
- Operator: any linear action on such functions; the lecture uses derivatives, multiplication by a function, and matrix multiplication as the three model cases.
- \(F(x)\): scalar function viewed as a multiplication operator.
- \(M^\alpha{}_\beta\): numerical matrix acting on vector components.
- \(\Gamma^\alpha{}_{\mu\beta}\): Christoffel symbols; in the operator discussion, for each fixed \(\mu\) they are viewed as a position-dependent matrix \(\Gamma_\mu\).
- \([\nabla_\nu,\nabla_\mu]\): operator measuring the failure of covariant derivatives to commute.
- \(R^\alpha{}_{\beta\mu\nu}\): Riemann curvature tensor; the object controlling the change of a vector after infinitesimal parallel transport around a loop.
- \(R_{\mu\nu}\): Ricci tensor obtained by mixed contraction of Riemann.
- \(R\): curvature scalar obtained by contracting Ricci with the metric.
- \(dx^\mu,\delta x^\nu\): infinitesimal displacements spanning the small loop / area element.
- \(\Delta V^\alpha\): change in vector components after transport around the loop.
- \(d\tau\): proper time along a trajectory.
- \(\dfrac{dx^\mu}{d\tau}\): tangent vector to a worldline.
- \(\phi\): Newtonian gravitational potential.
- \(A\): Newtonian acceleration field; transcript and board use it as the field whose divergence gives the source law.
- \(\rho\): mass density; identified with energy density in units \(c=1\).
- \(T^{\mu\nu}\): energy-momentum tensor; \(T^{00}\) is the energy-density entry used in the weak-field matching.
- Left-hand-side tensor candidate: an unknown two-index tensor built only from the metric and its derivatives, later to become the Einstein tensor.

## Derivation Steps
Operator commutator lemma:
1. Treat \(F(x)\) as the operator “multiply by \(F\)” acting on a test function \(V(x)\).
2. Compute \(\partial_x(FV)=F'V+FV'\).
3. Compute \(F(\partial_x V)=FV'\).
4. Subtract the two actions.
5. Conclude \([\partial_x,F]V = F'V\).
6. Therefore \([\partial_x,F(x)] = \partial_x F(x)\).

Small loop to commutator:
1. Pick infinitesimal displacements \(dx^\mu\) and \(\delta x^\nu\) spanning a tiny loop \(A\to B\to C\to D\to A\).
2. Parallel transport \(V_A\) around the loop and call the returned vector \(V_A'\).
3. Form an engineered difference-of-differences so that interior terms cancel.
4. After cancellation, the surviving quantity is \(V_A - V_A'\).
5. Replace each finite difference by a covariant derivative times the corresponding infinitesimal displacement.
6. Obtain a second-order difference proportional to \((\nabla_\nu\nabla_\mu-\nabla_\mu\nabla_\nu)V\).
7. Interpret the coefficient \(\delta x^\nu dx^\mu\) as the infinitesimal area element.

Commutator expansion to Riemann:
1. Write \(\nabla_\mu=\partial_\mu+\Gamma_\mu\).
2. Expand \([\nabla_\nu,\nabla_\mu]\) into derivative-derivative, derivative-\(\Gamma\), and \(\Gamma\Gamma\) pieces.
3. Drop \([\partial_\nu,\partial_\mu]\) because ordinary derivatives commute.
4. Convert \([\partial_\mu,\Gamma_\nu]\) and \([\partial_\nu,\Gamma_\mu]\) into derivatives of \(\Gamma\) using the lemma.
5. Keep \([\Gamma_\nu,\Gamma_\mu]\) because the \(\Gamma\)'s are matrices and need not commute.
6. Restore matrix indices \(\alpha,\beta\) and the summed intermediate index \(\delta\).
7. Read off the Riemann tensor from the coefficient of \(V^\beta\).

Contractions to Ricci and scalar curvature:
1. Lower indices when discussing symmetry properties.
2. Try contracting \(\mu\) with \(\nu\); it vanishes because a symmetric metric contracts an antisymmetric pair.
3. Try contracting \(\alpha\) with \(\beta\); it also vanishes for the same reason.
4. Contract one index from the first antisymmetric pair with one from the second pair.
5. Define the resulting nonzero two-index object as the Ricci tensor.
6. Contract Ricci once more with the metric to define the curvature scalar.

Weak-field geodesic to Newtonian force law:
1. Start from the geodesic equation.
2. Assume a weak field: \(g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu}\), with small \(h_{\mu\nu}\).
3. Assume slow motion: spatial components of \(dx^\mu/d\tau\) are small, while \(dx^0/d\tau\approx1\).
4. Replace \(\tau\) by \(t\) to leading order.
5. Keep only the dominant \(00\) term in the Christoffel contribution to the spatial equation.
6. Identify the spatial acceleration as \(d^2x/dt^2\approx-\Gamma^x{}_{00}\).
7. Expand \(\Gamma^x{}_{00}\) and neglect time-derivative terms in the Newtonian regime.
8. Reduce the result to a derivative of \(g_{00}\).
9. Compare with Newtonian acceleration \(d^2x/dt^2=-\partial_x\phi\).
10. Infer that \(g_{00}\) is related to \(\phi\) by a constant shift and a factor of \(2\).

Poisson equation to weak-field source equation:
1. Recall Newtonian source law for the acceleration field: \(\nabla\cdot A = -4\pi G\rho\).
2. Use \(A\) as the gradient of \(\phi\) to rewrite this as a Poisson equation for \(\phi\).
3. Identify \(\rho\) with energy density, hence with \(T^{00}\) in units \(c=1\).
4. Rewrite the source law as \(\nabla^2\phi = 4\pi G T^{00}\).
5. Substitute \(\phi = \tfrac12 g_{00}\) in the weak-field relation.
6. Move the factor of \(1/2\) to the right-hand side.
7. Obtain \(\nabla^2 g_{00} = 8\pi G T^{00}\).
8. Observe that this is only a weak-field component equation, not yet a tensor equation.

Tensor-candidate step:
1. Demand a two-index tensor on the left because the right-hand side is \(T_{\mu\nu}\).
2. Demand that it be made only from the metric and its second derivatives.
3. Use the curvature construction as the source of such tensors.
4. Note the two available two-index candidates: \(R_{\mu\nu}\) and \(g_{\mu\nu}R\).
5. Write the most general linear combination \(A R_{\mu\nu}+B g_{\mu\nu}R\).
6. Require its \(00\)-component to reproduce the weak-field equation in the slow-motion limit.

## Notation Choices
- Use \(\nabla_\mu\) in the final notes for covariant derivative, even though the transcript often says or writes “del” or `delta`; reserve \(\partial_\mu\) for ordinary derivatives.
- Use \(D_\mu\) only when discussing the lecturer’s blackboard/operator shorthand; normalize back to \(\partial_\mu\) in the chapter.
- Use matrix shorthand \((\Gamma_\mu)^\alpha{}_\beta=\Gamma^\alpha{}_{\mu\beta}\) when explaining the operator viewpoint.
- Use \(\Delta V^\alpha\) for the loop-induced change of the vector, not \(\delta V^\alpha\), to avoid confusion with the lecturer’s use of “delta” for infinitesimal displacements and covariant derivatives.
- Use \(R^\alpha{}_{\beta\mu\nu}\) as the primary explicit formula in clean notes; use fully lowered \(R_{\nu\mu\alpha\beta}\) when discussing symmetries and contractions, since that matches the lecture’s symmetry discussion.
- Use Ricci contraction in standard clean form \(R_{\mu\nu}=R^\alpha{}_{\mu\alpha\nu}\); mention the equivalent lowered-index contraction when relating it to the board image.
- Use signature \(\eta_{\mu\nu}=\mathrm{diag}(1,-1,-1,-1)\), since the transcript explicitly recalls \(dt^2-dx^2\).
- Use \(x^0=t\) once the weak-field slow-motion regime is introduced.
- Keep \(c=1\) throughout the working bank; note separately that the constant in \(g_{00}=2\phi+c\) becomes \(1\) far from sources.
- Use \(T^{00}\) for the source slot in the weak-field equations; the board index placement is partly visual, but the transcript’s logic is clearly energy density.
- Write the general tensor candidate with \(g_{\mu\nu}R\), not \(\delta_{\mu\nu}R\), even though the spoken transcript briefly drifts toward delta-style language.

## Uncertain Mathematics
- Exact sign in the weak-field relation \(d^2x/dt^2 \sim \pm \tfrac12 \partial_x g_{00}\): the transcript openly loses the sign, so the final chapter should narrate that instability and then present the cleaned conventional relation cautiously.
- Exact sign convention for the Newtonian field \(A\) versus \(\nabla\phi\): the board and transcript wobble between “gradient” and “minus gradient.”
- Exact sign in Poisson’s equation during the spoken derivation: the lecture says “or maybe with a minus sign,” so the final notes should keep the conventional cleaned form but acknowledge the lecture’s uncertainty.
- Exact index placement in the contraction visible in `lecture_08_figure_02.png`: the board clearly shows a metric contraction with Riemann, but the clean final indexing should follow standard conventions, not the partial screenshot alone.
- Exact lowered-index form of the Riemann formula as spoken on the board: the lecture suppresses and reintroduces matrix indices informally, so the final notes should typeset the canonical expression explicitly.
- Garbled transcript stretch around 01:36 on energy-momentum language: only the surrounding logic is secure, namely that \(T^{00}\) is the energy-density source entering the weak-field equation.
- The lecture mentions the numerical coefficients “one and minus a half” for the final tensor combination, but does not derive the full Einstein tensor cleanly in this lecture; if that formula is mentioned, it should be flagged as preview rather than completed derivation.
- The coordinate count of independent Riemann components is not part of the main derivation and should not be over-emphasized unless needed for a side remark.