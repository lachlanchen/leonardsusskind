# Math Bank
## Core Equations
- [visible] \(\vec E_M=-\frac{\partial \vec A}{\partial t}\)
- [transcript-backed] \((\vec E_M)_i=-\frac{\partial A_i}{\partial t}+\partial_iA_0\)
- [standard reconstruction] \((\vec E_L)_i=+\frac{\partial A_i}{\partial t}-\partial_iA_0=-(\vec E_M)_i\)
- [transcript-backed] \(\vec B=\nabla\times\vec A\)
- [standard reconstruction] Maxwell-side schematic equations used in the convention repair: \(\nabla\times\vec E_M=-\partial_t\vec B,\ \nabla\cdot\vec B=0,\ \nabla\times\vec B=\partial_t\vec E_M+\vec J_F,\ \nabla\cdot\vec E_M=\rho_F\)
- [standard reconstruction] Susskind-side schematic sign-converted version: \(\nabla\times\vec E_L=+\partial_t\vec B,\ \nabla\times\vec B=-\partial_t\vec E_L-\vec J_L,\ \nabla\cdot\vec E_L=\rho_L\)
- [visible] \(P_m=m\dot X_m\)
- [visible] \(L(q_i,\dot q_i)\)
- [transcript-backed] \(p_i=\frac{\partial L}{\partial \dot q_i}\)
- [transcript-backed] \(L=\frac12 m\dot x_i^2-e\,\dot x_iA_i\) as the magnetic-field example term structure, up to sign/\(c\)-convention details
- [transcript-backed] \(p_i=m\dot x_i-eA_i\) as the corresponding canonical momentum shift, up to sign convention
- [transcript-backed] \(Q=\sum_i p_i\,\delta q_i\)
- [transcript-backed] \(A=\int dt\,L(q,\dot q)\)
- [transcript-backed] \(H=\sum_i p_i\dot q_i-L\)
- [visible] \(L=\frac12 m\dot x^2-V(x)\)
- [visible] \(p=\frac{\partial L}{\partial \dot x}=m\dot x\)
- [transcript-backed] \(H=p\dot x-L=\frac12 m\dot x^2+V(x)\)
- [transcript-backed] \(A=\int dt\,L=\int dt\int d^3x\,\mathcal L\)
- [visible] \(\mathcal L=\frac12\dot\phi^2-\frac12\left(\frac{\partial\phi}{\partial x}\right)^2-V(\phi)\)
- [visible] \(\Pi_\phi=\frac{\partial\mathcal L}{\partial\dot\phi}=\dot\phi\)
- [transcript-backed] \(H=\int d^3x\,\bigl[\Pi_\phi\dot\phi-\mathcal L\bigr]\)
- [visible] \(H=\int dx\left[\frac12\dot\phi^2+\frac12\left(\frac{\partial\phi}{\partial x}\right)^2+V(\phi)\right]\)
- [transcript-backed] \(\frac{\partial^2\phi}{\partial t^2}-\frac{\partial^2\phi}{\partial x^2}=-\frac{dV}{d\phi}\)
- [transcript-backed] \(T^{00}=\Pi_\phi\dot\phi-\mathcal L\)
- [transcript-backed] \(T^{00}=\frac12\dot\phi^2+\frac12(\partial_x\phi)^2+V(\phi)\) for the scalar example
- [transcript-backed] \(T^{0m}=\Pi_\phi\,\partial_m\phi\)
- [transcript-backed] In one dimension, \(T^{0x}=\dot\phi\,\partial_x\phi\)
- [transcript-backed] \(A_\mu\to A_\mu+\partial_\mu S\)
- [transcript-backed] Gauge choice: \(A_0=0\)
- [transcript-backed] In that gauge, \(E_m=-\frac{\partial A_m}{\partial t}\)
- [transcript-backed] \(\mathcal L_{\mathrm{EM}}=-\frac14F_{\mu\nu}F^{\mu\nu}=\frac12E^2-\frac12B^2\)
- [transcript-backed] \(\Pi_m=\frac{\partial\mathcal L}{\partial\dot A_m}=\dot A_m=-E_m\) in Maxwell convention, with sign caution
- [transcript-backed] \(\mathcal H_{\mathrm{EM}}=\frac12E^2+\frac12B^2\)
- [transcript-backed] Intermediate Noether form for electromagnetic momentum density: \(\mathcal P_n\sim \Pi_m\,\partial_nA_m\)
- [transcript-backed] Integration-by-parts step used in the EM momentum derivation: \(\int d^3x\,E_m\,\partial_mA_n=-\int d^3x\,(\partial_mE_m)A_n\)
- [transcript-backed] Free-field condition used there: \(\nabla\cdot\vec E=0\)
- [standard reconstruction] \(\vec{\mathcal P}=\vec E\times\vec B\)
- [standard reconstruction] For a free electromagnetic wave, \(E\perp B\), \(|E|=|B|\), and the electric and magnetic contributions to \(\frac12(E^2+B^2)\) are equal

## Definitions And Objects
- \(\vec E_M\): Maxwell-convention electric field used in the later electromagnetic part of the lecture.
- \(\vec E_L\): Susskind’s earlier electric-field convention; opposite in sign to \(\vec E_M\).
- \(A_\mu=(A_0,\vec A)\): electromagnetic vector potential; \(A_0\) is the time component, \(A_m\) are spatial components.
- \(S\): scalar gauge function in \(A_\mu\to A_\mu+\partial_\mu S\).
- \(P_m\): mechanical momentum component; tied to mass times velocity / center-of-mass motion.
- \(p_i\): canonical momentum conjugate to \(q_i\).
- \(Q\): Noether conserved quantity associated with a continuous symmetry.
- \(q_i\): ordinary-mechanics canonical coordinates.
- \(x\): in field theory, a label of the degree of freedom, not the degree of freedom itself.
- \(\phi(x,t)\): scalar field value; the field-theory analogue of the canonical coordinate.
- \(\Pi_\phi(x,t)\): canonical momentum field conjugate to \(\phi(x,t)\).
- \(T^{00}\): energy density.
- \(T^{0m}\): density of the \(m\)-th component of momentum.
- \(T^{m0}\): flux of energy in the \(m\)-direction.
- \(\vec E\times\vec B\): Poynting vector; in this lecture it is both momentum density and energy flux for the free electromagnetic field.

## Derivation Steps
Electric-field convention repair
1. Start from Maxwell’s definition \((\vec E_M)_i=-\partial_tA_i+\partial_iA_0\).
2. Compare it with Susskind’s earlier choice \((\vec E_L)_i=+\partial_tA_i-\partial_iA_0\).
3. Record the relation \(\vec E_L=-\vec E_M\).
4. Propagate that sign flip through the Maxwell equations only to the extent needed for consistency.

Particle Hamiltonian warm-up
1. Take \(L=\frac12 m\dot x^2-V(x)\).
2. Compute \(p=\partial L/\partial\dot x=m\dot x\).
3. Form \(H=p\dot x-L\).
4. Simplify to \(H=\frac12 m\dot x^2+V(x)\).

Field theory as mechanics
1. Replace the discrete label \(i\) by the spatial label \(x\).
2. Replace \(q_i(t)\) by \(\phi(x,t)\).
3. Replace \(\sum_i\) by \(\int d^3x\).
4. Rewrite the action as \(A=\int dt\int d^3x\,\mathcal L\).

Scalar-field Hamiltonian
1. Start from \(\mathcal L=\frac12\dot\phi^2-\frac12(\partial_x\phi)^2-V(\phi)\).
2. Compute \(\Pi_\phi=\partial\mathcal L/\partial\dot\phi=\dot\phi\).
3. Form \(H=\int dx\,(\Pi_\phi\dot\phi-\mathcal L)\).
4. Simplify to \(H=\int dx\,[\frac12\dot\phi^2+\frac12(\partial_x\phi)^2+V(\phi)]\).

Why smooth fields cost less energy
1. Approximate \(\partial_x\phi\sim[\phi(x+\epsilon)-\phi(x)]/\epsilon\).
2. A fixed jump over smaller \(\epsilon\) makes \(|\partial_x\phi|\) larger.
3. The Hamiltonian contains \(+\frac12(\partial_x\phi)^2\).
4. Finite-energy configurations therefore suppress wildly jagged field profiles.

Scalar-field momentum density from Noether
1. Use \(Q=\sum_i p_i\delta q_i\to\int dx\,\Pi_\phi\,\delta\phi\).
2. For a spatial translation, \(\delta\phi\propto\partial_x\phi\).
3. Divide out the translation parameter.
4. Read off \(T^{0m}=\Pi_\phi\,\partial_m\phi\).

Electromagnetic energy and momentum
1. Fix gauge with \(A_0=0\), so \(E_m=-\partial_tA_m\) and \(\vec B=\nabla\times\vec A\).
2. Write \(\mathcal L_{\mathrm{EM}}=\frac12E^2-\frac12B^2\).
3. Read off \(\Pi_m=\partial\mathcal L/\partial\dot A_m=\dot A_m=-E_m\), with convention-sensitive sign.
4. Flip the non-time-derivative term to get \(\mathcal H_{\mathrm{EM}}=\frac12E^2+\frac12B^2\).
5. Start the Noether momentum density from \(\mathcal P_n\sim \Pi_m\,\partial_nA_m\).
6. Add/subtract the curl-completing term, integrate by parts, and use \(\nabla\cdot\vec E=0\) for the free field.
7. Normalize the final result to the standard free-field form \(\vec{\mathcal P}=\vec E\times\vec B\).

Poynting-vector interpretation
1. Interpret \(T^{0m}\) as density of the \(m\)-component of momentum.
2. Interpret \(T^{m0}\) as flux of energy in the \(m\)-direction.
3. Use the asserted symmetry \(T^{0m}=T^{m0}\).
4. Conclude that momentum density equals energy flux.

## Notation Choices
- Use \(L\) for the ordinary-mechanics Lagrangian and \(\mathcal L\) for the Lagrangian density.
- Use Maxwell convention for the main electromagnetic formulas after the opening convention repair; keep Susskind’s opposite-sign convention only as a preliminary comparison.
- Use \(q_i\) for finite-dimensional coordinates; use \(\phi(x,t)\) for the field degree of freedom.
- Treat \(x\) as a spatial label in field theory, not as the canonical coordinate itself.
- Use \(\Pi_\phi\) and \(\Pi_m\) for field conjugate momenta; do not reuse \(p\) there.
- Use spatial indices \(m,n\in\{1,2,3\}\) when following the lecture’s component notation for fields and momentum density.
- Use \(\partial_t\), \(\partial_m\), \(\nabla\), \(\nabla\cdot\), and \(\nabla\times\) in the main body; mention \(F_{\mu\nu}\) only as the compact covariant shorthand.
- Typeset the energy-momentum entries as \(T^{00},T^{0m},T^{m0}\), even though the lecture speaks them as “T naught naught” and “T naught m.”
- Keep \(A_\mu\) explicit for the vector potential, since the lecture also uses \(A\) for the action.
- Normalize the spoken “pointing vector” to the historical name “Poynting vector” in the final notes.

## Uncertain Mathematics
- The early transcript window around the first electric-field definition is garbled; use the board frame and the later clean restatement as the source of truth.
- The full sign-converted Maxwell equations are only schematic in the lecture; the opening discussion is about convention bookkeeping, not a careful rederivation.
- The magnetic-field particle example has unstable sign bookkeeping and omitted \(c\)-factors; use it only to illustrate that canonical momentum differs from mechanical momentum.
- The clean formula \(p_i=\partial L/\partial\dot q_i\) is transcript-backed; the frame only shows it being written.
- In the scalar Hamiltonian discussion, occasional spoken slips toward \(V(x)\) should be normalized to \(V(\phi)\).
- The covariant scalar-field shorthand is only gestured at as “something like” \(\frac12\partial_\mu\phi\,\partial^\mu\phi\); use cautiously if included.
- The sign of \(\Pi_m\) relative to \(E_m\) is explicitly shaky in the lecture because Susskind keeps toggling conventions in his remarks.
- The electromagnetic momentum-density derivation loses the sign midstream; the final notes should present \(\vec E\times\vec B\) as the standard free-field result after stating the caution.
- The integration-by-parts simplification assumes vanishing boundary terms at spatial infinity and the free-field condition \(\nabla\cdot\vec E=0\).
- The symmetry \(T^{0m}=T^{m0}\) is asserted, not derived, in this lecture; it should not be presented as proved here.