# Math Bank
## Core Equations
- \( \mathbf F = q(\mathbf E + \mathbf v \times \mathbf B) \) [visible]
- \( f^\mu = q\,F^{\mu}{}_{\nu}u^\nu \) [standard reconstruction]
- \( \partial_\mu \partial^\mu \phi = 0 \) [transcript-backed]
- \( \partial_t^2 \phi - \partial_x^2 \phi - \partial_y^2 \phi - \partial_z^2 \phi = 0 \) [transcript-backed]
- \( \frac{\partial^2 \phi}{\partial t^2} - \frac{\partial^2 \phi}{\partial z^2} = 0 \) [visible]
- \( \phi = f(z-t) \) [transcript-backed]
- \( \phi = g(z+t) \) [transcript-backed]
- \( \phi(z,t) = \cos\!\big(k(z-t)\big) \) [transcript-backed]
- \( \nabla \times \mathbf E = -\,\partial_t \mathbf B \) [transcript-backed]
- \( \nabla \cdot \mathbf B = 0 \) [transcript-backed]
- \( \nabla \times \mathbf B = \partial_t \mathbf E \) [transcript-backed]
- \( \nabla \cdot \mathbf E = 0 \) [transcript-backed]
- \( \nabla \cdot \mathbf E = \rho \) [transcript-backed]
- \( \nabla \times \mathbf B = \partial_t \mathbf E + \mathbf J \) [transcript-backed]
- \( F^{\mu\nu} \) with row/column order \(t,x,y,z\), first row \( (0,-E_x,-E_y,-E_z) \), first column \( (0,E_x,E_y,E_z)^{\mathsf T} \) [visible]
- \( F^{\mu\nu}=
\begin{pmatrix}
0 & -E_x & -E_y & -E_z\\
E_x & 0 & -B_z & B_y\\
E_y & B_z & 0 & -B_x\\
E_z & -B_y & B_x & 0
\end{pmatrix} \) [standard reconstruction]
- \( \partial_\mu F^{\mu\nu} = 0 \) [transcript-backed]
- \( \partial_\mu \tilde F^{\mu\nu} = 0 \) [transcript-backed]
- \( \partial_t^2 E_x - \partial_x^2 E_x - \partial_y^2 E_x - \partial_z^2 E_x = 0 \) [transcript-backed]
- \( E_x(z,t) = \cos(z-t) \) [transcript-backed]
- \( E_y = 0 \) [transcript-backed]
- \( \partial_z E_z = 0 \) [transcript-backed]
- \( \mathbf E \cdot \hat z = 0,\quad \mathbf B \cdot \hat z = 0,\quad \mathbf E \cdot \mathbf B = 0 \) [transcript-backed]
- \( \rho = \dfrac{dQ}{dV} \) [transcript-backed]
- \( Q = \int_V \rho\,dV \) [transcript-backed]
- \( \dfrac{dQ}{dt} = \mathbf J \cdot d\boldsymbol{\sigma} \) [transcript-backed]
- \( \dfrac{dQ_{\text{inside}}}{dt} = -\oint_{\partial V} \mathbf J \cdot d\boldsymbol{\sigma} \) [transcript-backed]
- \( \oint_{\partial V} \mathbf A \cdot d\boldsymbol{\sigma} = \int_V (\nabla \cdot \mathbf A)\,dV \) [transcript-backed]
- \( \partial_t \rho + \nabla \cdot \mathbf J = 0 \) [transcript-backed]
- \( J^\mu = (\rho, J_x, J_y, J_z) \) [transcript-backed]
- \( \partial_\mu J^\mu = 0 \) [transcript-backed]
- \( \partial_\mu F^{\mu\nu} = J^\nu \) [transcript-backed]

## Definitions And Objects
- Scalar field: \( \phi(x^\mu) \), one number at each spacetime point.
- Spacetime derivative: \( \partial_\mu = \dfrac{\partial}{\partial x^\mu} \), with \( \mu \in \{t,x,y,z\} \).
- Spatial derivative operators:
  \( \nabla \cdot \mathbf B = \partial_x B_x + \partial_y B_y + \partial_z B_z \),
  \( (\nabla \times \mathbf B)_x = \partial_y B_z - \partial_z B_y \), cyclic in \(x,y,z\).
- Dot product:
  \( \mathbf a \cdot \mathbf b = a_x b_x + a_y b_y + a_z b_z \).
- Cross product:
  \( (\mathbf b \times \mathbf a)_x = b_y a_z - b_z a_y \), cyclic in \(x,y,z\).
- Electromagnetic field tensor: anti-symmetric rank-2 tensor built from \(\mathbf E\) and \(\mathbf B\).
- Dual field tensor: \(\tilde F^{\mu\nu}\), introduced by the lecture via the replacement rule \(E \mapsto -B\), \(B \mapsto E\), up to the chosen sign convention.
- Charge density: local continuum charge per unit volume.
- Current density: vector giving charge flow per unit area per unit time.
- Surface element vector: \( d\boldsymbol{\sigma} \), normal to the surface element, magnitude equal to the area.
- Four-current: \( J^\mu \), combining charge density and current density.
- Vacuum Maxwell equations: source-free equations with \( \rho = 0 \), \( \mathbf J = 0 \).
- Polarized plane wave in this lecture: wave moving along \(z\) with electric field chosen along \(x\).

## Derivation Steps
Vacuum Maxwell equations to covariant form
1. Start from the source-free equations \( \nabla\cdot \mathbf E=0 \), \( \nabla\times \mathbf B=\partial_t \mathbf E \), \( \nabla\cdot \mathbf B=0 \), \( \nabla\times \mathbf E=-\partial_t \mathbf B \).
2. Package \(\mathbf E\) and \(\mathbf B\) into the anti-symmetric tensor \(F^{\mu\nu}\).
3. Ask for a first-derivative tensor equation with one free index.
4. Use the natural contraction \( \partial_\mu F^{\mu\nu} \).
5. Set \( \partial_\mu F^{\mu\nu}=0 \).
6. Check \( \nu=t \): obtain \( \nabla\cdot \mathbf E=0 \).
7. Check spatial \( \nu=i \): obtain \( \nabla\times \mathbf B=\partial_t \mathbf E \).
8. Introduce \( \tilde F^{\mu\nu} \) and write \( \partial_\mu \tilde F^{\mu\nu}=0 \).
9. Recover \( \nabla\cdot \mathbf B=0 \) and \( \nabla\times \mathbf E=-\partial_t \mathbf B \).

Wave equation for a component of \(\mathbf E\)
1. Begin with \( \nabla\times \mathbf B=\partial_t \mathbf E \).
2. Differentiate with respect to time: \( \partial_t^2 \mathbf E = \nabla\times \partial_t \mathbf B \).
3. Use \( \partial_t \mathbf B = -\,\nabla\times \mathbf E \).
4. Obtain \( \partial_t^2 \mathbf E = -\,\nabla\times(\nabla\times \mathbf E) \).
5. Take the \(x\)-component.
6. Expand the \(x\)-component of \( \nabla\times(\nabla\times \mathbf E) \) in partial derivatives.
7. Add and subtract \( \partial_x^2 E_x \) to expose \( \partial_x E_x + \partial_y E_y + \partial_z E_z \).
8. Replace that bracket by \( \nabla\cdot \mathbf E \).
9. Use \( \nabla\cdot \mathbf E = 0 \).
10. Conclude \( \partial_t^2 E_x - \partial_x^2 E_x - \partial_y^2 E_x - \partial_z^2 E_x = 0 \).

Plane-wave geometry and transversality
1. Choose a wave traveling along \(z\): \( E_x(z,t)=\cos(z-t) \).
2. Set \( E_y=0 \) for simplicity.
3. Use \( \nabla\cdot \mathbf E=0 \): only \( \partial_z E_z \) can survive.
4. Conclude \( \partial_z E_z=0 \), so the wave part of \(E_z\) vanishes.
5. Therefore the propagating electric field is transverse to \(z\).
6. Compute the possible components of \( \nabla\times \mathbf E \).
7. With \(E_x(z,t)\) nonzero and \(E_y=E_z=0\) for the wave part, only the \(y\)-component survives.
8. Use \( \nabla\times \mathbf E = -\,\partial_t \mathbf B \).
9. Infer that the magnetic field points along \(y\).
10. Conclude \( \mathbf E \perp \mathbf B \perp \hat z \).

Continuity equation from charge conservation
1. Define charge in a fixed region \(V\): \( Q_V = \int_V \rho\,dV \).
2. Net outward charge flow per unit time through the boundary is \( \oint_{\partial V} \mathbf J \cdot d\boldsymbol{\sigma} \).
3. Charge conservation gives \( \dfrac{dQ_V}{dt} = -\oint_{\partial V} \mathbf J \cdot d\boldsymbol{\sigma} \).
4. Move the time derivative inside the volume integral: \( \dfrac{dQ_V}{dt} = \int_V \partial_t \rho\,dV \).
5. Apply Gauss’s theorem to the surface integral.
6. Get \( \int_V \partial_t \rho\,dV = -\int_V (\nabla\cdot \mathbf J)\,dV \).
7. Since the equality holds for any region \(V\), equate integrands.
8. Obtain \( \partial_t \rho + \nabla\cdot \mathbf J = 0 \).
9. Package \( (\rho,\mathbf J) \) into \( J^\mu \).
10. Rewrite as \( \partial_\mu J^\mu = 0 \).

Sourced covariant Maxwell equations
1. Restore the source terms in Maxwell’s equations: \( \rho \) in Gauss’s law, \( \mathbf J \) in Ampère-Maxwell.
2. Introduce the four-current \( J^\mu = (\rho,J_x,J_y,J_z) \).
3. Replace the vacuum equation \( \partial_\mu F^{\mu\nu}=0 \) by \( \partial_\mu F^{\mu\nu}=J^\nu \).
4. Check \( \nu=t \): recover \( \nabla\cdot \mathbf E=\rho \).
5. Check spatial \( \nu=i \): recover \( \nabla\times \mathbf B=\partial_t \mathbf E+\mathbf J \).
6. Keep \( \partial_\mu \tilde F^{\mu\nu}=0 \) unchanged for the other half.

## Notation Choices
- Use boldface for ordinary three-vectors: \( \mathbf E, \mathbf B, \mathbf J, \mathbf v \).
- Use \( f^\mu \) for the four-force and reserve \(F^{\mu\nu}\) for the field tensor.
- Use \( x^\mu = (t,x,y,z) \) in the lecture’s time-first order, matching the board layout.
- Use \( \partial_\mu \) for spacetime derivatives and \( \nabla \) only for spatial operators.
- Use \(c=1\) throughout the chapter unless a brief editorial remark explicitly restores \(c\).
- Use the field-tensor sign convention fixed by the visible board matrix:
  top row \( (0,-E_x,-E_y,-E_z) \),
  first column \( (0,E_x,E_y,E_z)^{\mathsf T} \).
- Use the mixed-index Lorentz-force form \( f^\mu = q\,F^\mu{}_\nu u^\nu \) to avoid unnecessary metric-sign ambiguity.
- Use \( d\boldsymbol{\sigma} \) for the vector surface element, not bare \(d\sigma\), once the notes are typeset cleanly.
- Use \( Q_V \) or \( Q_{\text{inside}} \) for charge in a fixed region, and reserve \(Q\) alone for a total charge when the region is obvious.
- Use \( J^\mu = (\rho,J_x,J_y,J_z) \) exactly as in the lecture’s \(c=1\) normalization; do not insert extra factors of \(c\).

## Uncertain Mathematics
- The board line \( = q\,F^{\mu\nu} \) in `lecture_58_figure_02.png` is incomplete; the missing four-velocity contraction is not visible and must be supplied cautiously.
- The full matrix for \(F^{\mu\nu}\) is only partially visible in the frame; the magnetic entries come from transcript-backed completion, not direct image transcription.
- The explicit matrix for \( \tilde F^{\mu\nu} \) should be treated cautiously. Susskind verbally corrects himself while describing the replacement rule, so the final notes should fix one sign convention and state it consistently.
- The transcripted component formulas for the cross product are garbled in places. Use standard component formulas rather than reproducing the transcript verbatim.
- The transcripted component-by-component verification of \( \partial_\mu F^{\mu\nu}=0 \) is garbled around 00:38:30–00:41:00; preserve the logic of the check, not the corrupted wording.
- The long curl-curl expansion in the wave-equation derivation is messy on the board. The final chapter should preserve the algebraic strategy, but it does not need to reproduce every intermediate term exactly as spoken.
- Around 01:01:47 the transcript says “the z component of the magnetic field” where the argument is clearly still about the electric field; correct this silently in the later chapter.
- The lecture does not visibly write a full explicit formula for the magnetic plane wave, only its direction and geometric relation to \(\mathbf E\) and the propagation axis. If the final notes write an explicit \(B_y(z,t)\), it should be presented as a clean consequence of the chosen convention, not as a directly quoted board formula.
- `lecture_58_figure_05.png` contains a cropped upper expression ending in \(=0\), but it is not reliable enough to use as mathematical evidence.