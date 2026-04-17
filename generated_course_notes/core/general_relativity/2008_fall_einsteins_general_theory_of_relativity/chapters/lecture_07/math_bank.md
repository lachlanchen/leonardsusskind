# Math Bank
## Core Equations
- \(K=\lim_{\Delta A\to 0}\dfrac{\Delta\theta}{\Delta A}\) [transcript-backed]
- \(K_{\text{sphere}}=\dfrac{1}{a^{2}}\) for a sphere of radius \(a\) [transcript-backed]
- \(\dfrac{D V^\mu}{ds}=0\) [transcript-backed]
- \(\dfrac{D V^\mu}{ds}=\dfrac{dV^\mu}{ds}+\Gamma^\mu{}_{\alpha\beta}V^\alpha\dfrac{dx^\beta}{ds}\) [transcript-backed]
- \(\delta V^\mu=-\Gamma^\mu{}_{\alpha\beta}V^\alpha\,dx^\beta\) [standard reconstruction]
- \(\delta V^\rho = R^\rho{}_{\sigma\mu\nu}V^\sigma\,\delta x^\mu dx^\nu\) [standard reconstruction]
- \(R^{\rho}{}_{\sigma\mu\nu}=\partial_{\mu}\Gamma^{\rho}{}_{\nu\sigma}-\partial_{\nu}\Gamma^{\rho}{}_{\mu\sigma}+\Gamma^{\rho}{}_{\mu\lambda}\Gamma^{\lambda}{}_{\nu\sigma}-\Gamma^{\rho}{}_{\nu\lambda}\Gamma^{\lambda}{}_{\mu\sigma}\) [standard reconstruction]
- \(R^{\rho}{}_{\sigma\mu\nu}=\partial_{\mu}\Gamma^{\rho}{}_{\nu\sigma}-\partial_{\nu}\Gamma^{\rho}{}_{\mu\sigma}+\cdots\) [visible]
- \([\nabla_\mu,\nabla_\nu]V^\rho = R^\rho{}_{\sigma\mu\nu}V^\sigma\) [standard reconstruction]
- \(R_{\lambda\sigma\mu\nu}=g_{\lambda\rho}R^\rho{}_{\sigma\mu\nu}\) [transcript-backed]
- \(R_{\alpha\beta\gamma\delta}=-R_{\beta\alpha\gamma\delta}\) [standard reconstruction]
- \(R_{\alpha\beta\gamma\delta}=-R_{\alpha\beta\delta\gamma}\) [standard reconstruction]
- \(R_{\alpha\beta\gamma\delta}=R_{\gamma\delta\alpha\beta}\) [standard reconstruction]
- \(R_{\beta\delta}=g^{\alpha\gamma}R_{\alpha\beta\gamma\delta}\) [visible]
- \(R_{\beta\delta}=R_{\delta\beta}\) [transcript-backed]
- \(\rho_q=\dfrac{dq}{dV}\) [transcript-backed]
- \(q(V)=\displaystyle\int_V \rho_q\,dV\) [transcript-backed]
- \(J^\mu=(\rho_q,J_x,J_y,J_z)\) [transcript-backed]
- \(\partial_t\rho_q+\nabla\cdot\mathbf J=0\) [transcript-backed]
- \(\partial_t\rho_q+\partial_x J_x+\partial_y J_y+\partial_z J_z=0\) [transcript-backed]
- \(\partial_\mu J^\mu=0\) [transcript-backed]
- \(P^\mu=(P^0,P^1,P^2,P^3)=(E,p_x,p_y,p_z)\) [standard reconstruction]
- \(T^{00}\) [visible]
- \(T^{01}\) [visible]
- \(\partial_t T^{00}+\partial_x T^{01}+\partial_y T^{02}+\partial_z T^{03}=0\) [transcript-backed]
- \(\partial_t T^{10}+\partial_x T^{11}+\partial_y T^{12}+\partial_z T^{13}=0\) [transcript-backed]
- \(\partial_\mu T^{\nu\mu}=0\) [transcript-backed]
- \(\dfrac{D}{d\tau}\left(\dfrac{dx^\mu}{d\tau}\right)=0\) [transcript-backed]
- \(\dfrac{d^2x^\mu}{d\tau^2}+\Gamma^\mu{}_{\nu\sigma}\dfrac{dx^\nu}{d\tau}\dfrac{dx^\sigma}{d\tau}=0\) [transcript-backed]
- \(\dfrac{d^2x^i}{dt^2}\approx -\Gamma^i{}_{00}\) in the slow-motion weak-field limit [standard reconstruction]

## Definitions And Objects
- `2D curvature scalar`: local deflection angle per unit area from parallel transport around an infinitesimal loop.
- `Positive/negative curvature sign rule`: counterclockwise circumnavigation with counterclockwise rotation gives positive curvature; opposite rotation gives negative curvature.
- `Intrinsic geometry`: geometry detectable by an inhabitant using rulers, protractors, rollers, or gyroscopes that remain within the space.
- `Parallel transport`: transport law preserving vector length and preserving perpendicularity in Riemannian geometry.
- `Geodesic`: “straightest possible” path; operationally, keep the steering wheel fixed straight ahead.
- `Plane of excursion`: the two directions \((\mu,\nu)\) spanning the infinitesimal loop.
- `Plane of rotation`: the plane in which the transported vector rotates after the loop.
- `Riemann tensor`: the rank-4 tensor measuring failure of a vector to return unchanged after parallel transport around an infinitesimal loop.
- `All-lowered Riemann tensor`: lowered with the metric because the symmetry pattern is cleaner there.
- `Ricci tensor`: contraction of one excursion-plane index with one rotation-plane index of the Riemann tensor.
- `Charge density \(\rho_q\)`: charge per unit spatial volume.
- `Current \(\mathbf J\)`: charge flux through an oriented spatial window per unit time.
- `Four-current \(J^\mu\)`: unified object combining charge density and charge flux.
- `Total charge`: scalar invariant, unlike the components of the current.
- `Four-momentum \(P^\mu\)`: total energy and total momentum of a system packaged as a four-vector.
- `Stress-energy tensor \(T^{\mu\nu}\)`: array of densities and fluxes of energy and momentum.
- `Index meaning in \(T^{\mu\nu}\)`: first index says which conserved quantity is being discussed; second index says density or direction of flow.
- `Tangent vector to a worldline`: \(dx^\mu/d\tau\), with \(\tau\) proper time.

## Derivation Steps
`2D curvature from parallel transport`
1. Choose a very small closed loop on a surface.
2. Start with a vector tangent to the surface.
3. Parallel transport it around the loop.
4. Measure the small rotation \(\Delta\theta\) on return.
5. Divide by the enclosed area \(\Delta A\).
6. Take the limit \(\Delta A\to 0\).
7. Use the sign of circumnavigation versus rotation to assign the sign of curvature.

`Holonomy to Riemann tensor`
1. Choose two infinitesimal directions \(dx^\mu\) and \(\delta x^\nu\).
2. Form a small rectangle in the \((\mu,\nu)\)-plane.
3. Parallel transport a vector around the closed loop.
4. The net change must vanish if there is no enclosed area.
5. Therefore the first nontrivial change is proportional to area, hence to \(dx^\mu\delta x^\nu\).
6. The change must also be linear in the starting vector.
7. The coefficient of that linear map is the curvature tensor.

`Infinitesimal transport law`
1. Write the covariant derivative of a vector along a curve.
2. Set the covariant derivative equal to zero for parallel transport.
3. Solve for the first-order change in the vector over an infinitesimal displacement.
4. Compare transport along adjacent sides of the small rectangle.
5. The mismatch comes from variation of the Christoffel symbols from place to place.
6. This produces derivative terms in \(\Gamma\).
7. Repeated infinitesimal transports also produce quadratic \(\Gamma\Gamma\) terms.

`Why \(R\) is a tensor`
1. The left-hand side \(\delta V\) is the difference of two vectors at the same point.
2. A difference of vectors at the same point is a vector.
3. The displacements \(dx^\mu,\delta x^\nu\) are vectors.
4. The starting vector \(V^\sigma\) is arbitrary.
5. If one coefficient object makes the vector equation true for every \(V^\sigma\), that coefficient must transform tensorially.
6. Therefore the curvature object defined by the holonomy equation is a tensor.

`Ricci from Riemann`
1. Start with the all-lowered Riemann tensor.
2. Select one index associated with circumnavigation and one associated with vector rotation.
3. Contract those two indices with the metric.
4. The result has only two free indices.
5. By Riemann symmetries, the resulting two-index object is symmetric.

`Charge continuity equation`
1. Define charge density as charge per unit volume.
2. Define current as charge through an oriented window per unit time.
3. Ask how the charge in a fixed small volume changes with time.
4. Uniform through-flow does not change the amount inside.
5. Only net outward flow matters.
6. Net outward flow is measured by \(\nabla\cdot\mathbf J\).
7. Therefore time-change of density plus divergence of current equals zero.
8. Repackage \(\rho_q\) and \(\mathbf J\) into \(J^\mu\) to get \(\partial_\mu J^\mu=0\).

`Stress-energy continuity`
1. Treat energy as one conserved quantity and each momentum component as another.
2. For each conserved quantity, introduce a density and three spatial flows.
3. Arrange the four sets of four quantities into \(T^{\mu\nu}\).
4. For a fixed first index \(\nu\), the second index runs over density and spatial flux.
5. Write a continuity equation for each row.
6. Compress the four row equations into \(\partial_\mu T^{\nu\mu}=0\).

`Geodesic equation to Newtonian preview`
1. Take the tangent vector \(dx^\mu/d\tau\).
2. Set its covariant derivative along the worldline to zero.
3. Expand to obtain the Christoffel-symbol form of the geodesic equation.
4. Assume weak fields and slow motion.
5. Then spatial components of \(dx^\mu/d\tau\) are small, while the time component is approximately \(1\).
6. Keep only the dominant \((00)\)-term.
7. The remaining Christoffel symbol controls ordinary gravitational acceleration.

## Notation Choices
- Use \(K\) for the two-dimensional curvature scalar; do not call it simply \(R\) in the final notes, because the lecture later reserves \(R\) for curvature tensors.
- Use \(V^\mu\) for the vector being parallel transported, even though the transcript often says “\(v\).”
- Use \(R^\rho{}_{\sigma\mu\nu}\) as the canonical Riemann notation.
- Use \(\mu,\nu\) for the excursion-plane indices and \(\rho,\sigma\) for the vector/rotation indices.
- When writing the holonomy formula, distinguish the two displacements as \(\delta x^\mu\) and \(dx^\nu\); do not write two indistinguishable \(dx\)’s.
- Use \(\partial_\mu\) for ordinary derivatives and \(\nabla_\mu\) for covariant derivatives.
- Use the convention \(x^0=t\), with \(c=1\) throughout.
- Use Latin indices \(i,j\) only for spatial components in the Newtonian-limit remark.
- Use \(R_{\alpha\beta\gamma\delta}=g_{\alpha\rho}R^\rho{}_{\beta\gamma\delta}\) for the all-lowered tensor before stating symmetries.
- Write the Ricci tensor as \(R_{\beta\delta}=g^{\alpha\gamma}R_{\alpha\beta\gamma\delta}\), matching the board evidence.
- Use \(J^\mu=(\rho_q,J_x,J_y,J_z)\) for four-current.
- Use \(P^\mu=(E,p_x,p_y,p_z)\) for four-momentum, with the first equality \(P^\mu=(P^0,P^1,P^2,P^3)\) implicit if needed.
- Use \(T^{\mu\nu}\) with raised indices, matching the visible board entries \(T^{00}\) and \(T^{01}\).
- In continuity equations for stress-energy, keep the lecture’s index order \(\partial_\mu T^{\nu\mu}=0\): the derivative contracts with the second tensor index.
- Interpret index \(0\) in \(T^{\mu\nu}\) as the time/density slot and indices \(1,2,3\) as spatial flow directions.

## Uncertain Mathematics
- The opening recap is verbally garbled; preserve only the clean mathematical content: small-loop holonomy, sign convention, and local curvature.
- The infinitesimal transport formula is spoken with scrambled index placement; typeset it canonically rather than verbatim.
- The holonomy formula for \(\delta V\) is conceptually clear but indexwise unstable in the transcript; use a cautious canonical reconstruction.
- The full Riemann formula is visually supported, but the rightmost quadratic terms are not perfectly legible in the frame; treat the fully typeset version as a supported reconstruction.
- The symmetry discussion of the Riemann tensor includes on-the-fly corrections; only the cleaned standard symmetries should survive into the final notes.
- The lecture’s count of “independent components” in dimensions \(2,3,4\) should not be treated as reliable final mathematics; do not elevate those numbers into a theorem without checking independently.
- The statement that locally flat coordinates make first and second derivatives of the metric vanish is mathematically unsafe as stated; keep only the intended intuition of locally inertial coordinates.
- The loop-closure discussion is partly garbled; the safe takeaway is only that failure to close is higher order and does not alter the leading curvature formula.
- The slow-motion Newtonian link is stated verbally as “acceleration is the Christoffel symbol”; the exact sign and reduced equation should be derived carefully in the final chapter.
- The four-momentum notation is only partially visible in the frame; \(P^\mu=(E,p_x,p_y,p_z)\) should be treated as transcript-backed standard reconstruction, not as image transcription.
- The visible stress-energy board evidence supports only the earliest entries \(T^{00}\) and \(T^{01}\); the full \(4\times4\) layout is transcript-backed reconstruction.
- The symmetry \(T^{\mu\nu}=T^{\nu\mu}\) is not cleanly established by the surviving frame evidence here; if it is used later, it should be justified from transcript or course context rather than inferred from the images alone.