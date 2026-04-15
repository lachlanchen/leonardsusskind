# Math Bank
## Core Equations
- \(E=mc^2\) and, with \(c=1\), mass and energy are identified. [transcript-backed]
- \(m\mathbf a=-m\nabla\phi\). [transcript-backed]
- \(\mathbf a=-\nabla\phi\). [transcript-backed]
- \(\nabla^2\phi=4\pi G\rho\). [transcript-backed]
- \(\phi=-\dfrac{GM}{r}\) outside a spherically symmetric source. [transcript-backed]
- \(g_{00}=1-\dfrac{2GM}{r}=1+2\phi\). [transcript-backed]
- \(\nabla^2 g_{00}\sim 8\pi G\rho\). [transcript-backed]
- \(\dot{\sigma}+\nabla\cdot \mathbf J=0\). [transcript-backed]
- \(J^\mu=(J^0,J^1,J^2,J^3)\) with \(J^0=\sigma\). [transcript-backed]
- \(\partial_\mu J^\mu=0\). [transcript-backed]
- \(D_\mu T^{0\mu}=0\). [transcript-backed]
- \(D_\mu T^{\nu\mu}=0\). [visible]
- \(T^{\mu\nu}=\begin{pmatrix}
T^{00}&T^{01}&T^{02}&T^{03}\\
T^{10}&T^{11}&T^{12}&T^{13}\\
T^{20}&T^{21}&T^{22}&T^{23}\\
T^{30}&T^{31}&T^{32}&T^{33}
\end{pmatrix}\). [standard reconstruction]
- \(T^{\mu\nu}=T^{\nu\mu}\). [transcript-backed]
- \(R^{\mu\nu}\stackrel{?}{=}8\pi G\,T^{\mu\nu}\). [visible]
- \(g^{\mu\nu}R\stackrel{?}{=}8\pi G\,T^{\mu\nu}\). [visible]
- \(G^{\mu\nu}=8\pi G\,T^{\mu\nu}\). [visible]
- \(\Gamma^\sigma_{\tau\nu}=\dfrac12 g^{\sigma\delta}\!\left(\partial_\tau g_{\delta\nu}+\partial_\nu g_{\delta\tau}-\partial_\delta g_{\nu\tau}\right)\). [standard reconstruction]
- \(R^\mu{}_{\nu\tau\sigma}=\partial_\tau\Gamma^\mu_{\nu\sigma}-\partial_\sigma\Gamma^\mu_{\nu\tau}+\Gamma^\mu_{\lambda\tau}\Gamma^\lambda_{\nu\sigma}-\Gamma^\mu_{\lambda\sigma}\Gamma^\lambda_{\nu\tau}\). [standard reconstruction]
- \(R_{\mu\nu}=R^\lambda{}_{\mu\lambda\nu}\). [standard reconstruction]
- \(R=g^{\mu\nu}R_{\mu\nu}\). [transcript-backed]
- \(D_\mu\!\left(g^{\mu\nu}R\right)=\left(D_\mu g^{\mu\nu}\right)R+g^{\mu\nu}(D_\mu R)\). [visible]
- \(D_\mu g^{\mu\nu}=0\). [transcript-backed]
- For a scalar, \(D_\mu R=\partial_\mu R\). [transcript-backed]
- \(D_\mu\!\left(g^{\mu\nu}R\right)=g^{\mu\nu}\partial_\mu R\). [transcript-backed]
- \(D_\mu R^{\mu\nu}=\dfrac12\,g^{\mu\nu}D_\mu R\). [transcript-backed]
- \(G_{\mu\nu}=R_{\mu\nu}-\dfrac12 g_{\mu\nu}R\). [transcript-backed]
- \(G_{\mu\nu}=8\pi G\,T_{\mu\nu}\). [transcript-backed]
- \(g^\mu{}_\nu=\delta^\mu{}_\nu\). [transcript-backed]
- \(\delta^\mu{}_\mu=4\). [transcript-backed]
- \(T=g^{\mu\nu}T_{\mu\nu}\). [transcript-backed]
- \(R=-8\pi G\,T\). [visible]
- \(R_{\mu\nu}=8\pi G\left(T_{\mu\nu}-\dfrac12 g_{\mu\nu}T\right)\). [visible]
- \(T_{\mu\nu}=0\Rightarrow R=0\Rightarrow R_{\mu\nu}=0\). [transcript-backed]
- \(T_{\mu\nu}^{(\Lambda)}=\lambda\,g_{\mu\nu}\). [transcript-backed]

## Definitions And Objects
- \(\phi\): Newtonian gravitational potential.
- \(\rho\): mass density; in \(c=1\) units this is also energy density in the nonrelativistic source discussion.
- \(Q\): total electric charge.
- \(\sigma\): charge density; Susskind switches from the usual \(\rho\) to \(\sigma\) to avoid conflict with mass density.
- \(\mathbf J\) or \(J^i\): spatial charge current, defined as charge crossing an oriented infinitesimal window per unit area per unit time.
- \(J^\mu\): charge four-current, with time component equal to charge density.
- \(P^\mu\): total energy-momentum four-vector, with \(P^0=E\) and \(P^i\) the spatial momentum components.
- \(T^{00}\): energy density.
- \(T^{0i}\): flow of energy in the \(i\)-direction.
- \(T^{i0}\): density of the \(i\)-th component of momentum.
- \(T^{ij}\): flow of the \(i\)-th momentum component in the \(j\)-direction; later associated with stress/pressure.
- First index of \(T^{\mu\nu}\): which conserved quantity is being discussed (energy or a momentum component).
- Second index of \(T^{\mu\nu}\): density versus flow direction.
- Energy-momentum tensor: the symmetric rank-two tensor collecting all energy/momentum densities and fluxes.
- Christoffel symbols: non-tensorial objects built from first derivatives of the metric.
- Riemann tensor: curvature tensor built from derivatives of Christoffels plus quadratic Christoffel terms.
- Ricci tensor: contraction of the Riemann tensor; contains less information than the full Riemann tensor.
- Curvature scalar \(R\): contraction of the Ricci tensor with the metric.
- Einstein tensor \(G_{\mu\nu}\): the covariantly conserved combination \(R_{\mu\nu}-\frac12 g_{\mu\nu}R\).
- Trace \(T\): scalar obtained by contracting the energy-momentum tensor, \(T=g^{\mu\nu}T_{\mu\nu}\).
- Vacuum case: region with \(T_{\mu\nu}=0\).
- Ricci-flat: \(R_{\mu\nu}=0\); lecture explicitly distinguishes this from fully flat spacetime.

## Derivation Steps
Newtonian warm-up and weak-field mnemonic
1. Start from the Newtonian motion law \(m\mathbf a=-m\nabla\phi\).
2. Cancel the particle mass to get \(\mathbf a=-\nabla\phi\).
3. Use Poisson’s equation \(\nabla^2\phi=4\pi G\rho\).
4. For a spherically symmetric source, use \(\phi=-GM/r\) outside the source.
5. Recall Schwarzschild \(g_{00}=1-2GM/r\).
6. Rewrite this as \(g_{00}=1+2\phi\).
7. Therefore \(\nabla^2 g_{00}=2\nabla^2\phi\sim 8\pi G\rho\).
8. Keep this only as a mnemonic bridge, not as the actual Einstein equation.

Charge continuity
1. Define charge density \(\sigma\) as charge per unit volume.
2. Define spatial current \(J^i\) as charge crossing an oriented window per unit area per unit time.
3. Consider a small box.
4. Charge leaving the box per unit time is \(-\dot{\sigma}\).
5. Flux through the walls is \(\nabla\cdot \mathbf J\).
6. Equate loss inside to outward flux: \(\dot{\sigma}+\nabla\cdot\mathbf J=0\).
7. Package \(\sigma\) and \(J^i\) into \(J^\mu\) with \(J^0=\sigma\).
8. Rewrite the continuity law as \(\partial_\mu J^\mu=0\).
9. In curved-coordinate language, the lecture says the derivative should be promoted to a covariant derivative.

Energy-momentum tensor build-up
1. Treat energy and each momentum component as conserved quantities analogous to charge.
2. Define the density of energy as \(T^{00}\).
3. Define energy flow along spatial direction \(i\) as \(T^{0i}\).
4. Define density of the \(i\)-th momentum component as \(T^{i0}\).
5. Define flow of the \(i\)-th momentum component along direction \(j\) as \(T^{ij}\).
6. Collect all of these into a rank-two tensor \(T^{\mu\nu}\).
7. Use relativistic symmetry to take \(T^{\mu\nu}=T^{\nu\mu}\).
8. For each fixed first index \(\nu\), write a continuity equation.
9. Combine them into \(D_\mu T^{\nu\mu}=0\).

Why the field equation must be tensorial
1. The Newtonian source term suggests energy density on the right-hand side.
2. But energy density is only one component of \(T_{\mu\nu}\).
3. A law true in every frame cannot equate only one component of a tensor to one component of another tensor.
4. Therefore the right-hand side must be the full symmetric rank-two tensor \(8\pi G\,T_{\mu\nu}\).
5. Hence the left-hand side must also be a symmetric rank-two tensor built from the metric and its derivatives.

Curvature candidates
1. The left-hand side must be geometric and built from the metric.
2. To resemble the Newtonian second-derivative structure, it should contain two derivatives of the metric.
3. Christoffel symbols contain first derivatives of \(g_{\mu\nu}\).
4. The Riemann tensor contains derivatives of Christoffels and quadratic Christoffel terms, hence second derivatives of \(g_{\mu\nu}\) plus squares of first derivatives.
5. The Riemann tensor has four indices, so it cannot directly match \(T_{\mu\nu}\).
6. Contract the Riemann tensor to obtain the Ricci tensor \(R_{\mu\nu}\).
7. Contract once more to obtain the scalar \(R\).
8. Form the two obvious rank-two candidates: \(R_{\mu\nu}\) and \(g_{\mu\nu}R\).

Failure of the naive left-hand sides
1. Demand local conservation on the right-hand side: \(D_\mu T^{\mu\nu}=0\).
2. Therefore the left-hand side must also have vanishing covariant divergence.
3. Test \(g^{\mu\nu}R\) using the product rule:
   \(D_\mu(g^{\mu\nu}R)=(D_\mu g^{\mu\nu})R+g^{\mu\nu}(D_\mu R)\).
4. Use metric compatibility \(D_\mu g^{\mu\nu}=0\).
5. Use the fact that \(R\) is a scalar, so \(D_\mu R=\partial_\mu R\).
6. Conclude \(D_\mu(g^{\mu\nu}R)=g^{\mu\nu}\partial_\mu R\), which is not zero in general.
7. Test \(R^{\mu\nu}\).
8. Use the board-level identity \(D_\mu R^{\mu\nu}=\frac12 g^{\mu\nu}D_\mu R\), also not zero in general.
9. Combine the two candidates so the nonzero terms cancel.
10. Obtain \(G_{\mu\nu}=R_{\mu\nu}-\frac12 g_{\mu\nu}R\), whose covariant divergence vanishes.

Matching to Newton
1. Allow an overall numerical multiple of the geometric tensor.
2. Take the weak-field, slow-motion, nonrelativistic limit.
3. On the right-hand side, \(T_{00}\sim \rho\) dominates.
4. On the left-hand side, the dominant terms reduce to second derivatives of the metric.
5. Compare with the Newtonian mnemonic \(\nabla^2 g_{00}\sim 8\pi G\rho\).
6. The required coefficient comes out to unity.
7. Write the field equation as \(G_{\mu\nu}=8\pi G\,T_{\mu\nu}\).

Trace in vacuum
1. Set \(T_{\mu\nu}=0\).
2. Then \(R_{\mu\nu}-\frac12 g_{\mu\nu}R=0\).
3. Rearrange to \(R_{\mu\nu}=\frac12 g_{\mu\nu}R\).
4. Contract \(\mu\) and \(\nu\).
5. Use \(g^\mu{}_\mu=\delta^\mu{}_\mu=4\).
6. Get \(R=\frac12(4)R=2R\).
7. Conclude \(R=0\).
8. Substitute back to obtain \(R_{\mu\nu}=0\).

Trace with sources and Ricci-form rewriting
1. Start from \(R_{\mu\nu}-\frac12 g_{\mu\nu}R=8\pi G\,T_{\mu\nu}\).
2. Contract the two free indices.
3. The left-hand side becomes \(R-\frac12(4)R=-R\).
4. The right-hand side becomes \(8\pi G\,T\), where \(T=g^{\mu\nu}T_{\mu\nu}\).
5. Therefore \(R=-8\pi G\,T\).
6. Substitute this back into the Einstein equation.
7. Move the \(-\frac12 g_{\mu\nu}R\) term to the right-hand side.
8. Obtain \(R_{\mu\nu}=8\pi G\left(T_{\mu\nu}-\frac12 g_{\mu\nu}T\right)\).

Vacuum interpretation
1. In vacuum, \(T_{\mu\nu}=0\), so \(R_{\mu\nu}=0\).
2. This is Ricci-flatness, not full flatness.
3. Schwarzschild exterior satisfies \(R_{\mu\nu}=0\) away from the singularity.
4. Gravitational waves also satisfy \(R_{\mu\nu}=0\) while retaining nonzero curvature.

## Notation Choices
- Use \(c=1\) throughout unless explicitly restoring powers of \(c\) for qualitative discussion.
- Use roman \(G\) for Newton’s constant.
- Use \(G_{\mu\nu}\) for the Einstein tensor; do not let transcript ambiguity between “G” and “g” blur these.
- Use \(\nabla\) and \(\nabla^2\) only in the Newtonian spatial discussion.
- Use \(\partial_\mu\) for the flat-spacetime charge continuity equation.
- Use \(D_\mu\) for covariant derivatives in the GR discussion, matching the lecture’s board notation.
- Reserve \(\rho\) for mass/energy density and \(\sigma\) for charge density, following Susskind’s choice.
- Use \(J^\mu\) for charge four-current, with \(J^0=\sigma\).
- Use \(P^\mu\) for total energy-momentum four-vector, with \(P^0=E\).
- Keep \(T^{00}\), \(T^{0i}\), \(T^{i0}\), \(T^{ij}\) when discussing the tensor’s physical entries, because that is how the board develops it.
- Keep the candidate comparison with upper indices when reproducing the board layout:
  \(R^{\mu\nu}\), \(g^{\mu\nu}R\), \(G^{\mu\nu}\).
- Use lower indices for the final traced and Ricci-form equations if that makes the algebra cleaner, since the lecture itself shifts index placement locally.
- Use \(g^\mu{}_\nu=\delta^\mu{}_\nu\) in contractions; use \(\delta^\mu{}_\mu=4\) in four dimensions.
- Use \(T\) only for the trace \(g^{\mu\nu}T_{\mu\nu}\), not for the full tensor.

## Uncertain Mathematics
- The explicit Christoffel-symbol and Riemann-tensor component formulas are too garbled in the transcript to quote verbatim; only the standard Levi-Civita and Riemann forms should be inserted, and only as standard reconstructions.
- The product-rule section around 01:06:24–01:09:15 is transcript-corrupted; the safe payload is:
  \(D_\mu(g^{\mu\nu}R)\) expands by the product rule,
  \(D_\mu g^{\mu\nu}=0\),
  \(D_\mu R=\partial_\mu R\),
  and the surviving scalar-derivative term shows \(g^{\mu\nu}R\) is not conserved by itself.
- The line near 01:05:43 suggesting that \(D_\mu g^{\mu\nu}=0\) “follows” from \(D_\mu T^{\mu\nu}=0\) should not be preserved as a derivation; metric compatibility is an independent geometric fact.
- The board evidence for the full \(4\times4\) matrix \(T^{\mu\nu}\) is incomplete; the full matrix should be treated as a clean completion, not a literal transcription.
- The continuity equation visible in `lecture_09_figure_02.png` is only partial; the fully clean form \(D_\mu T^{\nu\mu}=0\) is a cautious reconstruction supported by the lecture.
- The historical statement that Einstein first tried \(R_{\mu\nu}=8\pi G\,T_{\mu\nu}\) is partly garbled in the transcript; present it cautiously as the failed naive candidate, not as a precise historical quotation.
- The uniqueness claim should stay at lecture level: within the search for symmetric rank-two geometric tensors built from the metric and two derivatives, the covariantly conserved combination is \(R_{\mu\nu}-\frac12 g_{\mu\nu}R\) up to an overall factor.
- The lecture’s board-level identity \(D_\mu R^{\mu\nu}=\frac12 g^{\mu\nu}D_\mu R\) should be preserved in that form if one wants to mirror the lecture; a more polished textbook rewrite can be deferred.
- Do not state or imply that vacuum means vanishing full curvature; the lecture’s payoff is precisely that \(R_{\mu\nu}=0\) still allows Schwarzschild exterior curvature and gravitational waves.