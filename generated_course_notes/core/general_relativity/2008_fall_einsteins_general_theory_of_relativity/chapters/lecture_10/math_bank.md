# Math Bank
## Core Equations
- \(\delta \propto m\) for the conical deficit angle of a point mass in \(2+1\) gravity [transcript-backed]
- \(F(r)\sim r^{-2},\,r^{-3},\,r^{-4}\) as the spatial dimension increases from \(3\) to \(4\) to \(5\) spatial dimensions in the lecture’s qualitative comparison [transcript-backed]
- \(\nabla_\mu G^{\mu\nu}=0\) [visible]
- \(\nabla_\mu g^{\mu\nu}=0\) [visible]
- \(G_{\mu\nu}=R_{\mu\nu}-\frac12 g_{\mu\nu}R\) [transcript-backed]
- \(R_{\mu\nu}-\frac12 g_{\mu\nu}R=k\,T_{\mu\nu}\) [transcript-backed]
- \(R_{\mu\nu}-\frac12 g_{\mu\nu}R+\lambda g_{\mu\nu}=k\,T_{\mu\nu}\) [transcript-backed]
- \(\nabla^2\Phi=4\pi G\,\rho\) [transcript-backed]
- \(\nabla^2 g_{00}\propto \rho\) in the weak, static limit, with \(g_{00}\) related to the Newtonian potential [standard reconstruction]
- \(\partial_t^2\phi=c^2\,\partial_x^2\phi\) [transcript-backed]
- \(\partial_t^2\phi=c^2\left(\partial_x^2+\partial_y^2+\partial_z^2\right)\phi\) [transcript-backed]
- \(\eta^{\mu\nu}\partial_\mu\partial_\nu\phi=0\) [transcript-backed]
- \(g^{\mu\nu}\partial_\mu\partial_\nu\phi=0\) as the naive but insufficient curved-space replacement [transcript-backed]
- \(\nabla_\mu\!\left(g^{\mu\nu}\partial_\nu\phi\right)=0\) [standard reconstruction]
- \(\nabla_\mu\nabla^\mu\phi=0\) after using metric compatibility [standard reconstruction]
- \(\nabla_\mu(AB)=(\nabla_\mu A)B+A(\nabla_\mu B)\) [transcript-backed]
- \(T_{\mu\nu}=\partial_\mu\phi\,\partial_\nu\phi-\frac12\eta_{\mu\nu}\,\partial_\alpha\phi\,\partial^\alpha\phi\) [visible]
- \(\partial^\mu T_{\mu\nu}=0\) for solutions of the flat-space wave equation [transcript-backed]
- \(T_{00}=\dot{\phi}^{\,2}-\frac12\left[\dot{\phi}^{\,2}-\left(\frac{\partial\phi}{\partial x}\right)^2-\left(\frac{\partial\phi}{\partial y}\right)^2-\left(\frac{\partial\phi}{\partial z}\right)^2\right]\) [standard reconstruction]
- \(T_{00}=\frac12\left[\dot{\phi}^{\,2}+\left(\frac{\partial\phi}{\partial x}\right)^2+\left(\frac{\partial\phi}{\partial y}\right)^2+\left(\frac{\partial\phi}{\partial z}\right)^2\right]\) [visible]
- \(\phi_\Lambda(\mathbf{x})=\frac{\lambda}{6}\left(x^2+y^2+z^2\right)\) as the Newtonian-style potential producing a constant Laplacian [standard reconstruction]
- \(\partial_x\phi_\Lambda=\frac{\lambda}{3}x,\quad \partial_y\phi_\Lambda=\frac{\lambda}{3}y,\quad \partial_z\phi_\Lambda=\frac{\lambda}{3}z\) [standard reconstruction]
- \(g_{\mu\nu}\to \eta_{\mu\nu}\) far away for asymptotically flat spacetime [transcript-backed]
- \(R\propto \lambda\) in vacuum with cosmological constant, with the exact sign depending on convention and on the lecture’s wavering sign choice [transcript-backed]

## Definitions And Objects
- \(g_{\mu\nu}\): spacetime metric.
- \(\eta_{\mu\nu}\): Minkowski metric used in the local flat limit and in flat-space field theory.
- \(R_{\mu\nu}\): Ricci tensor.
- \(R\): Ricci scalar, obtained by contracting the Ricci tensor with the metric.
- \(G_{\mu\nu}\): Einstein tensor, the special linear combination \(R_{\mu\nu}-\frac12 g_{\mu\nu}R\) whose covariant divergence vanishes.
- \(T_{\mu\nu}\): energy-momentum tensor; the right-hand side of Einstein’s equation.
- \(k\) or \(\kappa\): numerical coupling constant on the right-hand side; the lecture identifies it with \(8\pi G\) up to notation.
- \(\lambda\): cosmological constant.
- Covariant conservation: vanishing covariant divergence, e.g. \(\nabla_\mu G^{\mu\nu}=0\) or \(\nabla_\mu T^{\mu\nu}=0\).
- Metric compatibility: all covariant derivatives of the metric vanish.
- Geodesic: the “straightest possible” worldline in curved spacetime.
- Scalar field \(\phi\): the simple wave field used in place of Maxwell fields for the worked example.
- \(T_{00}\): energy density component.
- Pressure: in an isotropic rest frame, read from the diagonal spatial components of \(T_{\mu\nu}\).
- Shear stress: off-diagonal spatial components of \(T_{\mu\nu}\), or equivalently unequal diagonal stresses in a rotated basis.
- Asymptotically flat spacetime: a spacetime whose metric components approach \(\eta_{\mu\nu}\) far from localized sources.
- de Sitter / anti-de Sitter behavior: the non-asymptotically-flat vacuum geometry associated with nonzero cosmological constant.

## Derivation Steps
**Einstein tensor and cosmological-constant ambiguity**
1. Require the left-hand side of Einstein’s equation to be a two-index geometric tensor.
2. Start from the simplest available candidates built from the metric: \(R_{\mu\nu}\) and \(g_{\mu\nu}R\).
3. Demand covariant conservation so that the left-hand side matches the continuity equation expected for \(T_{\mu\nu}\).
4. Fix the coefficient of \(g_{\mu\nu}R\) to \(-\tfrac12\), giving \(G_{\mu\nu}=R_{\mu\nu}-\tfrac12 g_{\mu\nu}R\).
5. Use metric compatibility, \(\nabla_\mu g^{\mu\nu}=0\), to note that \(g_{\mu\nu}\) itself can be added without spoiling covariant conservation.
6. Conclude that the remaining ambiguity is \(+\lambda g_{\mu\nu}\).

**Weak-field / Newtonian correspondence**
1. Restrict to weak gravitational fields and slowly moving matter.
2. Focus on the \(00\)-component of Einstein’s equation.
3. On the right-hand side, \(T_{00}\) becomes the energy density \(\rho\).
4. On the left-hand side, the \(00\)-component reduces to a second spatial derivative of \(g_{00}\).
5. Use the relation between \(g_{00}\) and the Newtonian potential to recover a Poisson-type equation.
6. Interpret this as correspondence with Newton, not a first-principles derivation.

**Flat-space scalar wave equation**
1. Begin with one spatial dimension: \(\partial_t^2\phi=c^2\partial_x^2\phi\).
2. Extend to three spatial dimensions by adding \(\partial_y^2\phi\) and \(\partial_z^2\phi\).
3. Set \(c=1\) to use relativistic notation.
4. Rewrite the result as \(\eta^{\mu\nu}\partial_\mu\partial_\nu\phi=0\).

**Why the naive curved-space replacement fails**
1. Replace \(\eta^{\mu\nu}\) by \(g^{\mu\nu}\) as a first guess.
2. Observe that \(g^{\mu\nu}\partial_\mu\partial_\nu\phi=0\) is not a tensor equation.
3. Note that \(\partial_\nu\phi\) is a vector because \(\phi\) is a scalar.
4. Raise its index with the metric to obtain \(g^{\mu\nu}\partial_\nu\phi\), still a vector.
5. Recognize that differentiating a vector with an ordinary derivative does not produce a tensor.
6. Replace the outer ordinary derivative by a covariant derivative.
7. Obtain \(\nabla_\mu(g^{\mu\nu}\partial_\nu\phi)=0\).

**Simplification using metric compatibility**
1. Start from \(\nabla_\mu(g^{\mu\nu}\partial_\nu\phi)=0\).
2. Apply the Leibniz rule for covariant derivatives.
3. The term involving \(\nabla_\mu g^{\mu\nu}\) vanishes by metric compatibility.
4. The equation reduces to the covariant wave equation for the scalar field.

**Construction of the scalar-field stress-energy tensor**
1. Work first in flat spacetime.
2. Require a two-index tensor built from \(\phi\).
3. Use derivatives of \(\phi\) to create indexed objects.
4. Exclude terms odd in \(\phi\) by the physical requirement that energy not change sign under \(\phi\to-\phi\).
5. Keep quadratic derivative terms such as \(\partial_\mu\phi\,\partial_\nu\phi\).
6. Add the scalar contraction multiplied by \(\eta_{\mu\nu}\) with an unknown coefficient \(C\).
7. Impose \(\partial^\mu T_{\mu\nu}=0\) for fields satisfying the wave equation.
8. Differentiate the ansatz, use the Leibniz rule, and cancel the remaining terms.
9. Fix \(C=\tfrac12\).
10. Choose the overall normalization by convention for \(\phi\).

**Energy density from \(T_{00}\)**
1. Set \(\mu=\nu=0\) in the scalar-field stress tensor.
2. Identify the first term as \(\dot{\phi}^{\,2}\).
3. Expand the contraction \(\partial_\alpha\phi\,\partial^\alpha\phi\) using the Minkowski signature.
4. Use the sign flip when raising or lowering spatial indices.
5. Combine the terms to obtain the manifestly positive sum of kinetic and gradient contributions.

**Localized source versus extended field**
1. Compare with Poisson’s equation \(\nabla^2\Phi=4\pi G\rho\).
2. Note that \(\rho\) may vanish outside the source region.
3. Recognize that the vanishing of the source does not imply the vanishing of the potential.
4. Instead, it constrains the derivatives of the potential in the exterior region.
5. The same logic is then carried over to curvature sourced by localized stress-energy.

**Newtonianized cosmological constant**
1. Treat the cosmological constant as equivalent to a uniform source term in the Newtonian analogy.
2. Ask for a function with constant Laplacian.
3. Use \(x^2+y^2+z^2\), whose Laplacian is \(6\).
4. Scale it to produce the desired constant source.
5. Differentiate the resulting potential.
6. Conclude that the force is proportional to distance, not inverse square.
7. Interpret this as a center-free expansion or contraction law, depending on the sign.

**Vacuum curvature with cosmological constant**
1. Set matter to zero in the Einstein equation with \(\lambda\).
2. Contract the equation with the metric.
3. Use \(g^{\mu\nu}R_{\mu\nu}=R\).
4. Use \(g^{\mu\nu}g_{\mu\nu}=4\) in four spacetime dimensions.
5. Solve for the scalar curvature in terms of \(\lambda\).
6. Keep the sign cautious because the lecture explicitly wavers over it.

## Notation Choices
- Use \(\nabla_\mu\) for covariant derivatives throughout, even where the board writes a triangular handwritten symbol.
- Use \(\partial_\mu\) for ordinary derivatives in flat-space sections.
- Use signature \(\eta_{\mu\nu}=\mathrm{diag}(1,-1,-1,-1)\), matching the lecture’s “one minus one minus one minus one.”
- Use \(x^0=t\).
- Use Greek indices \(\mu,\nu,\alpha,\beta,\sigma\) for spacetime indices \(0,1,2,3\).
- Use Roman spatial labels \(x,y,z\) when the lecture switches to component form.
- Use \(G_{\mu\nu}\) for the Einstein tensor, despite the transcript’s occasional spoken ambiguity between little \(g\) and big \(G\).
- Use \(k\) for the Einstein-equation coupling in displayed equations, with a note that the lecture also refers to \(\kappa\) and \(8\pi G\).
- Use \(\phi\) for the scalar field everywhere.
- Use dot notation only for time derivatives in the \(T_{00}\) expansion: \(\dot{\phi}=\partial_t\phi\).
- In flat spacetime, use \(\partial^\mu=\eta^{\mu\nu}\partial_\nu\).
- For the working bank, take \(T_{00}\) as energy density and treat the isotropic diagonal spatial components as pressure, while flagging sign-convention instability separately.
- Use “asymptotically flat” to mean \(g_{\mu\nu}\to\eta_{\mu\nu}\) far away from localized sources.

## Uncertain Mathematics
- The exact proportionality constant between deficit angle and mass in the conical \(2+1\)-dimensional discussion is not given in the lecture segment; keep only \(\delta\propto m\).
- The transcript is garbled in the detailed comparison of \(1/r^2\) and \(1/r^3\); preserve only the qualitative dimensional-force-law argument.
- The weak-field reduction of the \(00\)-component carries an admitted factor-of-two uncertainty in the lecture; state the Poisson correspondence cautiously.
- The cleaned curved-space wave equation \(\nabla_\mu(g^{\mu\nu}\partial_\nu\phi)=0\) is a standard reconstruction from the lecturer’s false starts and corrections.
- The equivalent form \(\nabla_\mu\nabla^\mu\phi=0\) is mathematically standard but not stated as cleanly in the transcript.
- The derivation of the scalar-field stress tensor is partially garbled around the construction of the quadratic ansatz; the final formula is strongly supported by the frame and by the conservation argument.
- The lecture briefly hesitates over the overall sign in the stress tensor before settling; keep the final formula but note the hesitation if narrating the derivation closely.
- Pressure-sign conventions are verbally unstable in the lecture; do not overstate whether \(T_{ii}=p\) or \(T_{ii}=-p\) without fixing a convention explicitly in the final chapter.
- The contraction of the vacuum equation with cosmological constant yields \(R=\pm 4\lambda\) depending on sign conventions; the lecture explicitly says the sign of \(\lambda\) may have changed.
- The Newtonian cosmological-constant potential \(\phi_\Lambda=\frac{\lambda}{6}(x^2+y^2+z^2)\) is a useful reconstruction of the board logic, not a directly written lecture formula.
- The late black-hole photon-orbit discussion should be treated qualitatively here; the exact radius belongs in the Schwarzschild lecture treatment, not in the present chapter bank.