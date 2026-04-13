# Math Bank
## Core Equations
- \( \ket{S} \) [visible]
- \( R(2\pi)\ket{\psi}=\xi\ket{\psi} \) [transcript-backed]
- \( R(4\pi)\ket{\psi}=\xi^2\ket{\psi}=\ket{\psi} \) [transcript-backed]
- \( \xi^2=1,\qquad \xi=\pm1 \) [transcript-backed]
- \( R(2\pi)\ket{\psi_{\mathrm{boson}}}=+\ket{\psi_{\mathrm{boson}}},\qquad R(2\pi)\ket{\psi_{\mathrm{fermion}}}=-\ket{\psi_{\mathrm{fermion}}} \) [transcript-backed]
- \( \Psi=\psi_1+\psi_2 \) [transcript-backed]
- \( \Psi'=\psi_1-\psi_2 \) when only one branch acquires the fermionic minus sign [transcript-backed]
- \( |\Psi|^2 = (-\Psi)^*(-\Psi) \) [transcript-backed]
- \( \Psi(0)=0 \) for the odd recombined state when the two branches are reflection-symmetric [standard reconstruction]
- \( P_{12}\Psi(1,2)=+\Psi(1,2) \) for bosons [standard reconstruction]
- \( P_{12}\Psi(1,2)=-\Psi(1,2) \) for fermions [standard reconstruction]
- \( \Psi(1,2)=+\Psi(2,1) \) for bosons [standard reconstruction]
- \( \Psi(1,2)=-\Psi(2,1) \) for fermions [standard reconstruction]
- \( P_{12}\ket{\psi}=-\ket{\psi} \) [standard reconstruction]
- \( \operatorname{sign}(\text{two disconnected loops})=(\operatorname{sign}(\text{one loop}))^2=+1 \) [standard reconstruction]
- \( \operatorname{sign}(\text{one closed boson loop})=+1 \) [transcript-backed]
- \( \operatorname{sign}(\text{one closed fermion loop})=-1 \) [transcript-backed]
- \( m_{\text{partner}}=m_{\text{particle}} \) in exact supersymmetry [transcript-backed]
- \( Q_{\text{partner}}=Q_{\text{particle}} \) for the partner-matching examples discussed in the lecture [transcript-backed]
- \( \Delta E_{\mathrm{vac}}^{(b)}+\Delta E_{\mathrm{vac}}^{(f)}=0 \) for exactly matched boson-fermion partners [standard reconstruction]
- \( \Delta m_B^2\big|_{\text{boson loop}}+\Delta m_B^2\big|_{\text{fermion loop}}\approx 0 \) when partner masses and couplings are sufficiently aligned [standard reconstruction]
- \( j_{\text{superpartner}}=j\pm\tfrac12 \) [transcript-backed]
- \( m_\gamma=0 \Rightarrow m_{\tilde\gamma}=0 \) in an exactly supersymmetric world [transcript-backed]
- \( e^-_{\text{outer}}\to \tilde e^-+\tilde\gamma \) [standard reconstruction]

## Definitions And Objects
- \(R(\theta)\): rotation operator acting on the particle’s spin state.
- \(\xi\): scalar factor acquired by a state under a \(2\pi\) rotation.
- \(\ket{S}\): the lecturer’s initial notation for the spin state.
- \(\ket{\psi}\): generic state notation for rotation and exchange statements.
- \(\Psi(1,2)\): two-particle wavefunction for identical-particle exchange.
- \(P_{12}\): exchange operator that interchanges particles \(1\) and \(2\).
- \(\psi_1,\psi_2\): branch wavefunctions in the two-path interference setup.
- Closed loop: either a particle traveling around a closed spacetime loop or a particle-antiparticle pair created and then annihilated.
- Vacuum energy contribution: the sign-sensitive contribution of a closed vacuum loop.
- Boson self-energy / Higgs self-energy: radiative mass correction from loop diagrams.
- Superpartner: opposite-statistics partner of a particle with matching charge and other quantum numbers in the zeroth-order supersymmetry picture.
- Exact supersymmetry: exact boson-fermion partner matching, including mass degeneracy.
- Broken / approximate supersymmetry: partner structure survives, but masses are split.
- Photino \((\tilde\gamma)\): fermionic partner of the photon.
- Selectron \((\tilde e)\): bosonic partner of the electron.
- Higgsino: fermionic partner of the Higgs boson.
- LSP: lightest superpartner.
- Statistics: Susskind’s operative word for fermion-ness versus boson-ness.

## Derivation Steps
Rotation sign from \(4\pi\) triviality:
1. Assume a \(2\pi\) rotation acts on the spin state by multiplication: \(R(2\pi)\ket{\psi}=\xi\ket{\psi}\).
2. Apply the same rotation a second time.
3. Obtain \(R(4\pi)\ket{\psi}=\xi^2\ket{\psi}\).
4. Use the topological input that \(4\pi\) is equivalent to doing nothing.
5. Conclude \(\xi^2=1\).
6. Therefore \(\xi=\pm1\).
7. Identify bosons with \(+1\) and fermions with \(-1\).

Observability of the fermionic minus sign:
1. Split one electron into two coherent branches with total wavefunction \(\Psi=\psi_1+\psi_2\).
2. Rotate only one branch by \(2\pi\).
3. For a fermion, that branch changes sign.
4. The recombined state becomes \(\Psi'=\psi_1-\psi_2\).
5. If the two branches are otherwise symmetric, the odd combination vanishes at the center.
6. The interference pattern therefore shifts; maxima become minima.
7. If both branches are rotated together, only an overall sign appears, so no observable changes.

Closed fermion loop minus sign:
1. Start from two disconnected identical-particle loops.
2. Their overall sign is the product of the two one-loop signs, so it is positive.
3. Cut both loops at a time slice and compare the particle labels before reclosing.
4. Interchange the two identical particles at the cut.
5. Bosons pick up no sign; fermions pick up a minus sign.
6. After reclosing, the interchanged picture is a single loop.
7. Therefore a single closed fermion loop carries a minus sign, while a single closed boson loop carries a plus sign.

Vacuum-energy cancellation logic:
1. A boson vacuum loop contributes with one sign and a fermion vacuum loop with the opposite sign.
2. The magnitude depends on mass and other particle data.
3. If a boson and fermion have matching mass and matching relevant quantum numbers, their vacuum contributions can cancel.
4. This gives the first zeroth-order motivation for supersymmetry.

Boson self-energy cancellation logic:
1. Boson self-energy diagrams by themselves generate large mass corrections.
2. Fermion loops enter with the opposite sign from boson loops.
3. If bosons and fermions come in tightly matched partner pairs, their loop corrections can cancel.
4. Exact matching gives exact cancellation.
5. Near matching gives partial cancellation, which may still control the dangerous growth.

Naturalness constraint on superpartner masses:
1. Supersymmetry helps only if the cancellations remain effective.
2. Very heavy superpartners spoil the cancellations.
3. Then Higgs-sector self-energies are driven up toward the heavy scale.
4. Therefore the particle-partner mass splittings cannot be arbitrarily large if supersymmetry is supposed to solve the hierarchy problem.

Exact-supersymmetry chemistry argument:
1. In a lithium-like atom, the outer electron wants to drop to the lowest orbit.
2. Ordinary Pauli blocking prevents that drop.
3. In an exactly supersymmetric world, the electron can emit a photino.
4. After emitting a fermion, it becomes a bosonic selectron.
5. The selectron is not Pauli-blocked.
6. It falls to the lowest orbit.
7. Repeating this mechanism collapses valence structure inward.
8. Ordinary chemistry no longer survives in anything like its familiar form.

## Notation Choices
- Use \(R(\theta)\) for rotations and do not introduce full \(SU(2)\)/\(SO(3)\) representation machinery unless later needed.
- Use \(\ket{S}\) when echoing the lecture’s initial spin-state naming.
- Use \(\ket{\psi}\) for generic state identities once the discussion becomes abstract.
- Use \(\xi\) for the scalar factor under \(2\pi\) rotation.
- Use \(P_{12}\) for exchange of identical particles.
- Use \(\Psi(1,2)\) for the two-particle wavefunction in exchange-symmetry formulas.
- Use \(\psi_1,\psi_2\) for the two interference branches and \(\Psi\) for the recombined total state.
- Use tilde notation in compact equations, e.g. \(\tilde e\), \(\tilde\gamma\), but retain the lecture names in prose: selectron, photino, Higgsino, gravitino.
- Use “exact supersymmetry” for exact mass degeneracy plus partner matching.
- Use “broken” or “approximate” supersymmetry when the partner structure remains but masses split.
- Use \(j\) for spin only in the compact rule \(j_{\text{superpartner}}=j\pm\tfrac12\).
- Keep loop formulas schematic; the lecture tracks signs, matching conditions, and qualitative size control, not explicit loop integrals.

## Uncertain Mathematics
- The box-and-ball/string argument should remain a qualitative topological statement; the lecture does not present a formal homotopy proof.
- The derivation \(\xi=\pm1\) assumes that \(R(2\pi)\) acts by multiplication with a scalar factor on the state; that assumption should remain visible.
- Do not silently replace the lecture’s argument by the more general textbook formula \(e^{2\pi i s}\) unless marked as extra context.
- The exchange equations \(P_{12}\Psi=\pm\Psi\) and \(P_{12}\ket{\psi}=-\ket{\psi}\) are mathematically appropriate reconstructions, but the board frame only securely shows \(\ket{S}\).
- The statement \(\Psi(0)=0\) needs the additional symmetry assumption that the two recombining branches have the same shape about the center.
- The closed-loop sign proof here is an exchange argument, not a full functional-integral derivation; later notes should not blur those.
- The vacuum-energy and self-energy cancellation equations are schematic summaries; the lecture gives no explicit coefficients, loop integrals, or regulator dependence.
- The claim that some fixed fraction of particles get mass only from the Higgs mechanism is presented heuristically and should be treated as model-specific lecture talk, not as a general theorem.
- The “couple of hundred GeV” mass-scale language is a lecture-era phenomenological estimate, not a timeless quantitative bound.
- The exact emitted quantum in the atomic transition is transcript-backed as a photino; the board image itself only shows emitted radiation, not a legible particle label.