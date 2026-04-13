# Math Bank
## Core Equations
- \[
  SU(3)\times SU(2)\times U(1)
  \]
  [transcript-backed]
- \[
  u \to d + W^+,
  \qquad
  d \to u + W^-
  \]
  [transcript-backed]
- \[
  W^- \to e^- + \bar{\nu}_e
  \]
  [transcript-backed]
- \[
  n \to p + e^- + \bar{\nu}_e
  \]
  [transcript-backed]
- \[
  c=\hbar=1
  \]
  [visible]
- \[
  [m]=[E]=[1/\text{length}]
  \]
  [visible]
- \[
  [m]=[E]=[p]=[1/\text{length}]
  \]
  [standard reconstruction]
- \[
  \Delta(d)\propto \frac{1}{d^2}
  \]
  for the massless-style power-law behavior emphasized in the lecture sketch [transcript-backed]
- \[
  \Delta(d)\ \text{falls exponentially for}\ d\gtrsim \frac{1}{m}
  \]
  [transcript-backed]
- \[
  d\sim \frac{1}{m}
  \]
  [transcript-backed]
- \[
  d\sim \frac{\hbar}{mc}
  \]
  [transcript-backed]
- \[
  \widetilde{\Delta}_W(k)=\frac{1}{k^2+m_W^2}
  \]
  [transcript-backed]
- \[
  \widetilde{\Delta}_\gamma(k)=\frac{1}{k^2}
  \]
  [transcript-backed]
- \[
  \widetilde{\Delta}_W(k)\approx \frac{1}{m_W^2}
  \qquad (k^2\ll m_W^2)
  \]
  [transcript-backed]
- \[
  \mathcal A_{\text{weak}}\sim \frac{g_w^2}{k^2+m_W^2}
  \]
  [standard reconstruction]
- \[
  \mathcal A_{\text{weak}}\sim \frac{g_w^2}{m_W^2}
  \]
  in the low-momentum regime [visible]
- \[
  P_{\text{weak}}\sim |\mathcal A_{\text{weak}}|^2 \sim \frac{g_w^4}{m_W^4}
  \]
  [transcript-backed]
- \[
  G_F \sim \frac{g_w^2}{m_W^2}
  \]
  as the historically measured low-energy combination [transcript-backed]
- \[
  \Delta E\,\Delta t<\hbar
  \]
  [standard reconstruction]
- \[
  \Delta t \lesssim \frac{\hbar}{\Delta E}
  \]
  [transcript-backed]
- \[
  \Gamma \propto |\mathcal A|^2,
  \qquad
  \tau \sim \Gamma^{-1}
  \]
  [transcript-backed]
- \[
  \dim SU(2)=3
  \]
  [standard reconstruction]
- \[
  N_{\text{gauge bosons of weak }SU(2)}=3
  \]
  [transcript-backed]

## Definitions And Objects
- `Fermion table`: quarks arranged horizontally by family and vertically by color; leptons repeat the family pattern but carry no color.
- `Color symmetry`: the \(SU(3)\) acting vertically on the red-green-blue triplet.
- `Flavor / family symmetry`: the weak \(SU(2)\) acting horizontally within doublets such as \((u,d)\), \((c,s)\), \((t,b)\), and analogously on lepton pairs.
- `Gauge boson as generator`: the lecture treats gluon or \(W\) emission as the physical enactment of an infinitesimal symmetry transformation.
- `Electric \(U(1)\)`: phase rotation of charged fields; photon emission is tied to this factor.
- `Weak coupling \(g_w\)`: coupling attached to each weak vertex; the transcript around its naming is garbled, but the substance is clear.
- `Strong coupling \(g_s\)` or `\(G_{\text{strong}}\)`: coupling attached to gluon emission.
- `Electric charge \(e\)`: the electromagnetic vertex coupling; \(e^2\) is discussed as the fine-structure-constant scale.
- `Propagator \(\Delta\)`: position-space amplitude for a particle to propagate from one spacetime point to another.
- `Fourier-transformed propagator \(\widetilde{\Delta}(k)\)`: momentum-space version used in Feynman rules; the lecture explicitly says the twiddle denotes Fourier transform.
- `\(k\)`: momentum carried by the exchanged \(W\), inferred from external momentum differences.
- `Real particle`: external incoming or outgoing particle in a Feynman diagram.
- `Virtual particle`: internal line in a Feynman diagram; not directly observed as an asymptotic state.
- `Available energy`: separate from coupling and propagator suppression; controls whether the initial and final states can match energetically.
- `\(G_F\)`: old low-energy Fermi constant, effectively the measured weak strength before momentum dependence could be resolved.
- `Spontaneous symmetry breaking`: symmetric microscopic rules, degenerate ground states, and selection of one vacuum by distant conditions or instability.
- `Explicit symmetry breaking`: the local energy function already favors one choice over the other.
- `Domain wall`: boundary between different symmetry-broken domains; used as the signal distinguishing spontaneous from explicit breaking.

## Derivation Steps
Weakness of weak interactions from a heavy \(W\):
1. Start from neutron beta decay as a Feynman diagram with two weak vertices and one exchanged \(W\).
2. Assign a factor \(g_w\) to each vertex, giving a net vertex factor \(g_w^2\).
3. Insert the \(W\)-propagator factor \(\widetilde{\Delta}_W(k)=1/(k^2+m_W^2)\).
4. In beta decay, the transferred momentum is tiny compared with \(m_W\), so \(k^2\) can be neglected at leading order.
5. Replace the propagator by \(1/m_W^2\).
6. Conclude that the amplitude scales like \(g_w^2/m_W^2\).
7. Square the amplitude to get a rate/probability scale \(g_w^4/m_W^4\).
8. Therefore the weak interaction is weak here because \(m_W\) is large, not because \(g_w\) is extraordinarily small.

Distance scale from natural units and dimensional analysis:
1. Set \(c=\hbar=1\).
2. Use \(E=mc^2\) to identify the units of mass and energy.
3. Use the uncertainty-principle discussion to identify momentum and inverse distance as carrying the same units.
4. Conclude that \([m]=[E]=[p]=[1/\text{length}]\).
5. The only length scale that can be built from a particle mass is \(1/m\).
6. Therefore the distance at which the propagator’s mass dependence becomes important must be of order \(1/m\).
7. Restoring constants gives the Compton-length scale \(\hbar/(mc)\).

From position-space propagator to momentum-space propagator:
1. Treat the propagator first as a function of spacetime separation between emission and absorption points.
2. Note its qualitative behavior: large at short distance, massless power-law tail, massive exponential suppression.
3. Observe that experiments usually determine momenta rather than spacetime separations.
4. Pass from the distance-space propagator to its Fourier transform.
5. Name the momentum carried by the exchanged \(W\) as \(k\).
6. State the momentum-space rule \(\widetilde{\Delta}_W(k)=1/(k^2+m_W^2)\).

Historical emergence of \(G_F\):
1. At low energies, experiments could not vary \(k^2\) enough to see momentum dependence in the denominator.
2. The exchanged particle was always the same \(W\), so the denominator effectively looked constant.
3. What was empirically accessible was the combination \(g_w^2/m_W^2\).
4. That effective low-energy constant was called \(G_F\).

Virtual \(W\) and the uncertainty relation:
1. In neutron decay there is not enough available energy to create a real on-shell \(W\) as an external particle.
2. The intermediate state can nevertheless contain an apparent excess energy \(\Delta E\) for a short time.
3. The lecture encodes this by \(\Delta E\,\Delta t\lesssim \hbar\).
4. Thus a heavy virtual \(W\) can exist only over a very short interval.
5. It must then either be reabsorbed or convert rapidly into lighter final particles such as \(e^-+\bar\nu_e\).
6. Exact energy conservation holds between the full initial and final states; only the internal description is off-shell.

Tunneling analogy:
1. Consider a particle initially at rest in a potential well.
2. The far side of the barrier is chosen to have the same potential energy as the starting point.
3. Classically, the barrier region is forbidden because the particle would need extra energy there.
4. Quantum mechanically, tunneling allows the particle to appear on the other side.
5. The barrier region is interpreted as an intermediate state with an apparent energy mismatch.
6. The duration of that mismatch is limited by \(\Delta E\,\Delta t\lesssim \hbar\).
7. The lecture uses this as the analog of the short-lived virtual \(W\).

Why \(SU(2)\) requires more than \(W^\pm\):
1. The weak symmetry mixing a two-component doublet is identified with \(SU(2)\).
2. The gauge bosons correspond one-to-one with the generators.
3. \(SU(2)\) has three generators.
4. Two charged bosons, \(W^+\) and \(W^-\), are therefore not enough.
5. The lecture concludes that a third weak gauge boson must exist, later identified with the \(Z\)-related neutral boson.

Spontaneous versus explicit symmetry breaking:
1. Build a lattice system with two locally equivalent orientations and lower energy for aligned neighbors.
2. The lowest-energy configurations are degenerate: all one way or all the other way.
3. Distant boundary conditions can select one of these vacua without changing the local rules.
4. That is the spontaneous case.
5. If one orientation had intrinsically lower local energy, the symmetry would already be broken in the Hamiltonian.
6. That is explicit symmetry breaking.
7. Domain walls are possible only in the spontaneous case with competing asymptotic choices.

## Notation Choices
- Use \(g_w\) for the weak coupling throughout, even though the transcript section where he names it is corrupted.
- Use \(g_s\) or \(G_{\text{strong}}\) only when explicitly comparing to the strong coupling; otherwise keep the focus on \(g_w\).
- Use \(e\) for the electromagnetic coupling and note that \(e^2\) is only the fine-structure-constant scale up to conventional factors.
- Use uppercase \(W\) and \(m_W\) in typeset notes, even where the board looks lowercase.
- Use \(\Delta\) for the position-space propagator and \(\widetilde{\Delta}\) for its Fourier transform.
- Use \(d\) for spatial distance in the propagator sketch and \(k\) for the momentum flowing through the exchanged \(W\).
- Use the lecture’s simplified low-energy sign convention \(\widetilde{\Delta}(k)=1/(k^2+m_W^2)\), not the full Minkowski-signature propagator, unless a later editorial note explicitly changes conventions.
- Use \(\bar{\nu}_e\) for neutron beta decay when the electron flavor is clear; the lecture often says only “anti-neutrino.”
- Use \(\mathcal A\) for amplitude, \(P\) or rate-scale language for the squared quantity, and \(\Gamma,\tau\) only when discussing decay-rate interpretation.
- Keep \(G_F\) as an effective low-energy constant, not as the exact fully normalized electroweak relation.
- Do not introduce Pauli matrices, covariant derivatives, or explicit weak-isospin operators here; the lecture does not develop them in this session.
- For spontaneous symmetry breaking, keep the discussion at the level of ground states, local interaction energies, and domain walls; do not impose an Ising Hamiltonian unless later editorial work explicitly marks it as auxiliary reconstruction.

## Uncertain Mathematics
- The naming of the weak coupling is garbled around 00:20:56–00:21:19; only the stable content “call the weak coupling \(g_w\)” should survive.
- The board clearly shows \(g_w^2/m_w^2\), but the lecture uses it as a low-energy scaling estimate, not a fully normalized Standard Model formula.
- The short-distance statement \(\Delta(d)\propto 1/d^2\) is part of the lecture’s qualitative explanation and sketch; it should not be over-sold as a complete derived propagator formula for all cases.
- The exponential falloff in distance space is qualitative in the lecture; no exact Bessel-function expression is worked out.
- The momentum-space propagator is presented in a simplified sign convention because the relevant exchange is “mostly spacelike”; this should be preserved as a lecture-local convention.
- The full uncertainty relation is only partially visible on the board; \(\Delta E\,\Delta t<\hbar\) is a transcript-supported completion.
- The interpretation “\(\Delta^2\) is the probability that the particle can go that far” is pedagogical lecture language, not a careful general QFT probability formula.
- The exact numerical estimates for \(g_w^2\), the weak suppression factor, and the real \(W\) lifetime are rough and partly garbled; preserve only the order-of-magnitude intent.
- The historical relation between \(G_F\), \(g_w\), and \(m_W\) should be stated with proportionality, not equality with exact prefactors.
- The spontaneous-symmetry-breaking section contains no explicit Hamiltonian or domain-wall tension formula; do not invent one unless it is marked as auxiliary reconstruction outside the lecture proper.