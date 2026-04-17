# Math Bank
## Core Equations
- \(\int K\,dA = +1\) for the sphere, \(\int K\,dA = 0\) for the torus, \(\int K\,dA = -1\) for a torus with two holes, and \(\int K\,dA = -2\) for a torus with three holes, in the lecture’s normalization. [transcript-backed]
- \(ds^2 = dx^2 + dy^2\) for the flat plane. [transcript-backed]
- In geodesic coordinates at a chosen point \(p\), \(g_{ij}(p)=\delta_{ij}\). [transcript-backed]
- In geodesic coordinates at \(p\), \(\partial_k g_{ij}(p)=0\). [transcript-backed]
- Therefore \(\Gamma^{i}{}_{jk}(p)=0\). [transcript-backed]
- \(R \sim \partial \Gamma + \Gamma\Gamma\). [visible]
- Schematically, \(R \sim \partial^2 g + (\partial g)^2\). [standard reconstruction]
- \(u^\nu \nabla_\nu u^\mu = 0\). [transcript-backed]
- \(\dfrac{d^2 x^\mu}{d\tau^2} + \Gamma^\mu_{\nu\rho}\dfrac{dx^\nu}{d\tau}\dfrac{dx^\rho}{d\tau}=0\). [standard reconstruction]
- \(S = -m \int d\tau\). [transcript-backed]
- \(d\tau^2 = g_{\mu\nu}(x)\,dx^\mu dx^\nu\). [transcript-backed]
- With \(x^0=t\), \(L = -m\sqrt{g_{00}+2g_{0i}\dot x^i+g_{ij}\dot x^i\dot x^j}\). [standard reconstruction]
- In the weak-field, low-velocity limit, \(L \approx -m\left(1+\dfrac{\delta g_{00}}{2}-\dfrac{\dot x^{\,2}}{2}\right)\). [visible]
- Board simplification: \(L \approx -m-\dfrac{\delta g_{00}}{2}+\dfrac{m\dot x^{\,2}}{2}\). [visible]
- Normalized weak-field expansion: \(L \approx -m-\dfrac{m\,\delta g_{00}}{2}+\dfrac{m\dot x^{\,2}}{2}\). [standard reconstruction]
- \(g_{00}\approx \text{const}+2\Phi\). [transcript-backed]
- Equivalently, \(\Phi \approx \dfrac{\delta g_{00}}{2}\). [transcript-backed]
- \(\Phi(r)=-\dfrac{GM}{r}\). [transcript-backed]
- Uniformly accelerated worldlines satisfy \(x^2-t^2=R^2\). [transcript-backed]
- The Rindler transformation is \(x=R\cosh\omega,\quad t=R\sinh\omega\). [transcript-backed]
- \(dx=\cosh\omega\,dR+R\sinh\omega\,d\omega\). [transcript-backed]
- \(dt=\sinh\omega\,dR+R\cosh\omega\,d\omega\). [transcript-backed]
- In \(1+1\) dimensions, \(d\tau^2=R^2\,d\omega^2-dR^2\). [standard reconstruction]
- Including transverse directions, \(d\tau^2=R^2\,d\omega^2-dR^2-dy^2-dz^2\). [standard reconstruction]
- For the unit sphere, \(d\Omega^2=d\phi^2+\sin^2\phi\,d\theta^2\). [transcript-backed]
- For flat three-space in spherical coordinates, \(ds^2=dr^2+r^2 d\Omega^2\). [transcript-backed]
- For flat spacetime in spherical coordinates, \(d\tau^2=dt^2-dr^2-r^2 d\Omega^2\). [transcript-backed]
- The Schwarzschild exterior metric is \(d\tau^2=\left(1-\dfrac{2GM}{r}\right)dt^2-\dfrac{dr^2}{1-\frac{2GM}{r}}-r^2 d\Omega^2\). [standard reconstruction]

## Definitions And Objects
- In two dimensions, Gaussian curvature is the single independent curvature component; Susskind treats it as the curvature scalar.
- Integrated curvature is a topological invariant in the lecture’s discussion; it is tied to the Euler number and does not change under mere bulging.
- A geodesic-coordinate system is built locally at a point by choosing perpendicular geodesics as axes and assigning nearby coordinates by geodesic distances.
- Christoffel symbols are built from first derivatives of the metric.
- The Riemann tensor has two schematic kinds of terms: derivatives of Christoffel symbols and quadratic products of Christoffel symbols.
- A geodesic, in the official sense used here, is a curve whose tangent vector is covariantly constant.
- The point-particle action is defined as minus mass times proper time along the trajectory.
- The resulting coordinate-time Lagrangian depends on position through the metric and on velocity through the pulled-back quadratic form.
- Proper acceleration means the acceleration measured in the observer’s instantaneous rest frame.
- A uniformly accelerated reference frame in special relativity is a family of hyperbolae, not a family of parallel Newtonian parabolas.
- In the lecture, the Rindler horizon is a one-way causal boundary: signals can enter from outside but cannot escape back out.
- \(d\Omega^2\) is shorthand for the metric on the unit two-sphere.
- Birkhoff’s theorem is used only in its exterior-field form: outside any bounded spherically symmetric source, the metric is the same as the black-hole exterior metric.

## Derivation Steps
Geodesic coordinates and local curvature
1. Choose a point \(p\) in curved space.
2. Construct two perpendicular geodesics through \(p\) and use them as local axes.
3. Assign nearby coordinates by dropping perpendicular geodesics and measuring distances along those axes.
4. In these coordinates, the metric at \(p\) becomes Euclidean: \(g_{ij}(p)=\delta_{ij}\).
5. The first derivatives of the metric vanish at \(p\): \(\partial_k g_{ij}(p)=0\).
6. Therefore all Christoffel symbols vanish at \(p\).
7. In \(R\sim \partial\Gamma+\Gamma\Gamma\), the quadratic \(\Gamma\Gamma\) term vanishes at \(p\).
8. The derivative term survives because \(\partial\Gamma\) contains second derivatives of the metric.
9. Conclusion: curvature is controlled locally by second derivatives of \(g\), not first derivatives.

Sphere minus a point and flattening
1. Place the sphere tangent to a plane.
2. For each point \(P\) on the sphere, draw the line from the north pole through \(P\) to the plane.
3. Use this to map sphere-minus-north-pole to the plane.
4. Start with the flat plane metric \(dx^2+dy^2\).
5. Pull those distances back to the sphere-minus-north-pole.
6. Near the missing north pole, image points run off to infinity on the plane.
7. Therefore the pulled-back metric components diverge near the missing point.
8. Conclusion: the sphere-minus-a-point can be flattened, but only with a singular metric at the removed point.

From proper time to the Lagrangian
1. Start with \(S=-m\int d\tau\).
2. Use \(d\tau^2=g_{\mu\nu}dx^\mu dx^\nu\).
3. Choose a time coordinate \(x^0=t\).
4. Expand the quadratic form into \(g_{00}dt^2+2g_{0i}dx^i dt+g_{ij}dx^i dx^j\).
5. Divide inside the square root by \(dt^2\).
6. Recognize \(\dot x^i=dx^i/dt\).
7. Read off a coordinate-time Lagrangian depending on \(x^i\) and \(\dot x^i\).
8. Euler-Lagrange equations from this \(L\) match the geodesic equation after rewriting \(\tau\)-derivatives in terms of \(t\)-derivatives.

Weak-field Newtonian limit
1. Assume \(g_{00}=1+\delta g_{00}\), \(g_{0i}=0\), and \(g_{ij}\approx -\delta_{ij}\).
2. Then the square-root argument becomes \(1+\delta g_{00}-\dot x^{\,2}\) to first order.
3. Use \(\sqrt{1+s}\approx 1+s/2\) for small \(s\).
4. Obtain \(L\approx -m\left(1+\delta g_{00}/2-\dot x^{\,2}/2\right)\).
5. Split this into rest, potential-like, and kinetic pieces.
6. Compare with Newtonian mechanics to identify \(\delta g_{00}/2\) with the gravitational potential up to sign and additive constant conventions.

Rindler metric
1. Reject the Newtonian parabola because constant coordinate acceleration would eventually imply superluminal speed.
2. Use the Lorentz-invariant hyperbola \(x^2-t^2=R^2\).
3. Parametrize it by \(x=R\cosh\omega\), \(t=R\sinh\omega\).
4. Differentiate to get \(dx\) and \(dt\).
5. Substitute into \(d\tau^2=dt^2-dx^2\).
6. The \(dR\,d\omega\) cross terms cancel.
7. Use \(\cosh^2\omega-\sinh^2\omega=1\).
8. Obtain \(d\tau^2=R^2 d\omega^2-dR^2\).
9. Add the unchanged transverse directions \(y,z\).

Schwarzschild motivation
1. Start from flat spacetime in spherical coordinates: \(d\tau^2=dt^2-dr^2-r^2d\Omega^2\).
2. Use the weak-field correspondence \(g_{00}\approx \text{const}+2\Phi\).
3. Insert the Newtonian potential \(\Phi=-GM/r\).
4. Propose \(g_{00}=1-2GM/r\) by asymptotic flatness and Newtonian matching.
5. Keep the angular term as \(-r^2d\Omega^2\).
6. Use Einstein’s equations for the remaining radial coefficient.
7. Obtain \(g_{rr}=-(1-2GM/r)^{-1}\).
8. Check that all coefficients reduce to flat-space values as \(r\to\infty\).

## Notation Choices
- Use \(K\) for the two-dimensional Gaussian curvature/scalar curvature in the opening topology discussion.
- Use \(p\) for the distinguished point where geodesic coordinates are constructed.
- Use Latin indices \(i,j,k\) for spatial/local-coordinate indices and Greek indices \(\mu,\nu,\rho\) for spacetime indices.
- Use the signature \(+---\), consistent with \(d\tau^2=dt^2-dx^2-dy^2-dz^2\).
- Use \(x^0=t\) for the time coordinate once the action is rewritten in coordinate time.
- Use \(\Gamma^\mu_{\nu\rho}\) for Christoffel symbols and keep \(R\sim\partial\Gamma+\Gamma\Gamma\) schematic when following the board.
- Use \(u^\mu=dx^\mu/d\tau\) for the tangent vector.
- Use \(m\) for the test-particle mass in the action and Lagrangian.
- Use \(M\) for the gravitating source mass and \(G\) for Newton’s constant, even though the lecture’s blackboard speech often blurs these into expressions like \(mg/r\).
- Use \(\Phi\) for the Newtonian gravitational potential, reserving \(\phi\) for the spherical polar angle.
- Use \(\delta g_{00}=g_{00}-1\) in asymptotically flat weak-field formulas; in prose note that Susskind’s broader point is “deviation from the additive constant.”
- Use \(\phi\) as the polar angle measured from the north pole and \(\theta\) as the azimuthal angle around the equator.
- Use \(d\Omega^2=d\phi^2+\sin^2\phi\,d\theta^2\) consistently once notation is fixed.
- Use \(R\) for the Rindler radial coordinate and \(\omega\) for Rindler time.
- Use \(r\) for the ordinary spherical radial coordinate in flat spherical space and Schwarzschild.

## Uncertain Mathematics
- The integrated-curvature normalization is lecture-specific; keep the explicit sample values rather than silently replacing them with a fully normalized Gauss-Bonnet formula.
- The board formula \(R=\partial\Gamma+\Gamma\Gamma\) is schematic and suppresses all indices, signs, and contractions.
- The statement “Riemann involves only second derivatives of the metric” is local to geodesic coordinates at the chosen point, not a global coordinate-free formula in that simple form.
- The fully indexed coordinate geodesic equation is not cleanly spoken in the transcript at the relevant moment; use the standard formula cautiously.
- The transcript does not fully carry out the conversion from Euler-Lagrange equations in \(t\) to the geodesic equation in \(\tau\); the equivalence is asserted more than explicitly derived.
- In the weak-field board simplification, the middle term appears without an explicit factor of \(m\); the normalized algebra would usually include it.
- The sign relation between \(\delta g_{00}\) and \(\Phi\) is discussed loosely on the board; preserve the additive-constant caveat and avoid overconfident sign fixing.
- The lecture temporarily wavers between \(\phi\) and \(\theta\) for the polar angle on the sphere; the final notes should stabilize the convention once.
- The spoken component summary of the Rindler metric becomes confused; rely on the line element obtained from the coordinate transformation, not on the off-the-cuff component labels.
- The \(c\)-restoration for the Schwarzschild metric is heuristic in the lecture; the clean bank should prefer the \(c=1\) form and mention \(2GM/(rc^2)\) cautiously when restoring dimensions.
- The stereographic-flattening discussion is secure, but the exact statement about whether the resulting geodesics are or are not great circles is hesitant in the transcript and should be stated carefully.