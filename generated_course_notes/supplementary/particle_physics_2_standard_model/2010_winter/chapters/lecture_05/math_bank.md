# Math Bank
## Core Equations

- \(A_\mu=(A_0,\vec A)\) [visible]
- \(F_x = e\,\partial_x A_0\) [standard reconstruction]
- \(\mathbf E\) is determined by spatial derivatives of \(A_0\) [transcript-backed]
- \(\mathbf B=\nabla\times \mathbf A\) [transcript-backed]
- \(\mathbf E \perp \mathbf B\) [transcript-backed]
- \(|\mathbf E|=|\mathbf B|\) for the plane-polarized wave he is sketching [transcript-backed]
- \(q_i' = U_{ij}q_j\) [visible]
- \(q_i^{\prime *}=U_{ij}^*q_j^*\) [standard reconstruction]
- \(\operatorname{tr}A = A_{ii}=0\) [transcript-backed]
- \(\dim(\text{adjoint of }SU(N)) = N^2-1\) [transcript-backed]
- \(q_i \to q_j + A_{ij}\) [transcript-backed]
- \(A_{ij}\to A_{ik}+A_{kj}\) as the schematic gluon self-interaction pattern described in the lecture [transcript-backed]
- \(\psi \to e^{i\theta}\psi\) for the electric-charge phase symmetry [transcript-backed]
- \(P(\text{photon emission}) \propto e^2\) [transcript-backed]
- \(\alpha \sim \dfrac{e^2}{4\pi}\approx \dfrac{1}{137}\) [transcript-backed]
- \(E=\hbar\omega\) [transcript-backed]
- \(c=1\) [transcript-backed]
- \(\hbar=1\) [transcript-backed]
- \(E\sim \omega \sim \dfrac{1}{t}\) in units with \(\hbar=1\) [transcript-backed]
- \(x\sim t\sim E^{-1}\) in units with \(c=1\) [transcript-backed]
- \(1\ \mathrm{eV}^{-1}\sim 10^{-7}\,\mathrm m\) as the lecture’s order-of-magnitude conversion [transcript-backed]
- \(\text{atomic diameter}\sim 10^{-10}\,\mathrm m \sim (\mathrm{keV})^{-1}\) [transcript-backed]
- \(t_{\text{atomic transit}}\sim 10^{-18}\,\mathrm s\) [transcript-backed]
- \(t_{\text{atomic orbital}}\sim 10^{-16}\,\mathrm s\) [transcript-backed]
- \(t_{\text{atomic decay}}\sim 10^{-9}\,\mathrm s\) [transcript-backed]
- \(\text{hadronic diameter}\sim 10^{-15}\,\mathrm m\) [transcript-backed]
- \(t_{\text{hadronic transit}}\sim 10^{-23}\,\mathrm s\) [transcript-backed]
- \(t_{\text{hadronic orbital}}\sim 10^{-23}\,\mathrm s\) [transcript-backed]
- \(t_{\text{hadronic decay}}\sim 10^{-23}\,\mathrm s\) for strong hadronic decays of the kind he is discussing [transcript-backed]
- \(\alpha_{\mathrm{QCD}}\sim 0.2\) or “close to one” in the loose qualitative sense of the lecture [transcript-backed]
- \(n\to p+e^-+\bar\nu_e\) [transcript-backed]
- \(\tau_n \sim 12\ \text{minutes}\) [transcript-backed]
- \(\pi^- \to e^-+\bar\nu_e\) as the pedagogical channel first drawn [transcript-backed]
- \(\pi^- \to \mu^-+\bar\nu_\mu\) as the dominant channel later noted [transcript-backed]
- \(\tau_{\pi^\pm}\sim 10\ \text{ns}\) [transcript-backed]
- \((u,d),\ (c,s),\ (t,b)\) [standard reconstruction]
- \((\nu_e,e^-),\ (\nu_\mu,\mu^-),\ (\nu_\tau,\tau^-)\) [standard reconstruction]
- \(Q(u)-Q(d)=+1\) [transcript-backed]
- \(Q(\nu_\ell)-Q(\ell^-)=+1\) [transcript-backed]
- \(Q(W^- )=-1,\qquad Q(W^+)=+1\) [transcript-backed]
- \(e^- \to \nu_e + W^-\) [transcript-backed]
- \(d \to u + W^-\) [transcript-backed]
- \(s \to c + W^-\) [transcript-backed]
- \(\mu^- \to \nu_\mu + W^-\) [transcript-backed]
- \(\mu^- \to \nu_\mu + e^- + \bar\nu_e\) [transcript-backed]
- \(\pi^- \sim d\bar u\) [standard reconstruction]
- \(\pi^- \to W^- \to \mu^-+\bar\nu_\mu\) [standard reconstruction]
- \(\Delta E\,\Delta t \sim 1\) as the lecture-level energy-time uncertainty statement for off-shell intermediate states [transcript-backed]
- \(m_\pi \approx 140\,\mathrm{MeV}\) [transcript-backed]
- \(m_\mu \approx 100\,\mathrm{MeV}\) [transcript-backed]
- \(m_{\nu}\approx 0\) for the kinematic estimates used here [transcript-backed]
- \(m_n \approx 940\,\mathrm{MeV},\quad m_p \approx 939\,\mathrm{MeV},\quad m_e \approx 0.5\,\mathrm{MeV}\) [transcript-backed]

## Definitions And Objects

- `Gauge theory`: a field theory with Maxwell-like fields, corresponding sources, conservation laws, and associated symmetries.
- `Vector potential`: \(A_\mu\), with time component \(A_0\) and spatial part \(\vec A\).
- `Electrostatic potential`: \(A_0\).
- `Gauge field in QCD`: \(A_{ij}\), a matrix-valued field with one quark-type index and one anti-quark-type index.
- `Fundamental representation of SU(3)`: quark field \(q_i\), with \(i\in\{1,2,3\}\) for color.
- `Complex-conjugate representation`: anti-quark field \(q_i^*\), transformed by \(U^*\).
- `Adjoint representation`: the gluon representation, realized here as traceless \(A_{ij}\).
- `Trace-zero condition`: removal of the singlet part of \(A_{ij}\), leaving eight gluons.
- `Coupling constant`: the emission amplitude at a vertex; for QED this is the electric charge.
- `Fine-structure constant`: practical probability-scale parameter for photon emission.
- `Weak doublets`: horizontal particle pairs mixed by the weak symmetry.
- `W bosons`: charged weak gauge bosons associated with transitions between the two members of a weak doublet.
- `Purely leptonic process`: a weak process with no quarks, e.g. muon decay.
- `Beta decay`: weak decay involving an electron or positron, as used historically in the lecture.

## Derivation Steps

Maxwell Prototype
1. Start with six electromagnetic components: three electric and three magnetic.
2. Repackage them into a four-vector potential \(A_\mu\).
3. Interpret \(A_0\) as the electrostatic potential.
4. Obtain the electric force from derivatives of \(A_0\).
5. Obtain the magnetic field from derivatives of \(\vec A\), specifically its curl.
6. Conclude that electrodynamics can be described either by \((\mathbf E,\mathbf B)\) or by \(A_\mu\).

Gauss’s-Law Consequence For Charge
1. A charge produces field lines.
2. Field lines do not end except on charges.
3. The electric flux through a surrounding sphere is therefore fixed by the enclosed charge.
4. If an isolated charge disappeared, the field would have to disappear everywhere at once or end without a charge.
5. Both options are ruled out by the lecture’s causal and Gauss’s-law reasoning.
6. Conclusion: source conservation is built into the structure of the field theory.

Conjugate Representation In QCD
1. Begin with \(q_i' = U_{ij}q_j\).
2. Identify anti-particles with complex-conjugate fields.
3. Complex-conjugate the transformation law.
4. Obtain \(q_i^{\prime *}=U_{ij}^*q_j^*\).
5. Conclude that quarks and anti-quarks sit in different, conjugate representations.

Eight Gluons Rather Than Nine
1. Treat \(A_{ij}\) as an object with one quark index and one anti-quark index.
2. A generic \(3\times 3\) matrix has \(9\) components.
3. Remove the singlet by imposing \(\operatorname{tr}A=0\).
4. The remaining independent components are \(9-1=8\).
5. Generalize to \(SU(N)\): \(N^2-1\).

Gauge-Boson Emission Rule
1. Take a matter field \(q_i\) in the fundamental representation.
2. Allow a transition to another component \(q_j\).
3. Preserve the index flow through the interaction.
4. Associate the emitted gauge boson with the appropriate pair of indices.
5. Conclude schematically that \(q_i\) becomes \(q_j\) by emitting \(A_{ij}\).

Why Gluons Interact With Gluons
1. The photon does not transform under electric phase rotation.
2. The gluon field \(A_{ij}\) carries color indices.
3. Anything carrying the relevant charge can emit or absorb the corresponding gauge boson.
4. Therefore gluons can emit gluons.
5. This introduces self-interaction absent in QED.
6. The lecture’s qualitative consequence is flux-tube formation and confinement.

Charge As Emission Probability
1. Interpret the vertex factor for photon emission as the electric charge \(e\).
2. Convert amplitude to probability by squaring.
3. Package the practical dimensionless strength into \(\alpha \sim e^2/4\pi\).
4. Use small \(\alpha\) to explain the large hierarchy of electromagnetic timescales.

Atomic And Hadronic Scale Comparison
1. Set \(c=1\) so distance and time have the same units.
2. Set \(\hbar=1\) so energy is inverse time.
3. Estimate atomic size, transit time, orbital time, and decay time.
4. Observe that these scales are separated by powers of \(\alpha\).
5. Estimate hadronic size, transit time, orbital time, and decay time.
6. Observe that these scales are all of the same order.
7. Infer that the analog of \(\alpha\) in QCD must be much larger than in QED.

Construction Of \(W^-\)
1. Look for a weak gauge boson with the quantum numbers of a second-column particle plus an anti-first-column particle.
2. Use \(e^-+\bar\nu_e\) as the simplest example.
3. Read off electric charge \(-1\).
4. Name the resulting gauge boson \(W^-\).
5. Check consistency with \(d+\bar u\), which has the same charge pattern.
6. Conclude that the same \(W^-\) can mediate lepton and quark transitions between weak partners.

Pion Decay Through \(W^-\)
1. Identify \(\pi^-\) as \(d\bar u\).
2. Use the weak transition \(d+\bar u \to W^-\).
3. Let the \(W^-\) decay into a charged lepton and the corresponding antineutrino.
4. First draw the electron channel pedagogically.
5. Then note that the dominant channel is actually \(\mu^-+\bar\nu_\mu\).

Muon Decay
1. Start with \(\mu^-\).
2. Emit \(W^-\) and \(\nu_\mu\).
3. Let \(W^-\) decay into \(e^-+\bar\nu_e\).
4. Conclude \(\mu^- \to \nu_\mu + e^- + \bar\nu_e\).
5. Use the muon-electron mass gap to explain why the decay is kinematically allowed.

Neutron Beta Decay
1. Write the neutron as \(ddu\).
2. Reject \(u\to d+W\) because the resulting three-down-quark state is too heavy.
3. Use instead \(d\to u+W^-\).
4. Convert \(ddu\) into \(uud\), i.e. a proton.
5. Let the \(W^-\) decay into \(e^-+\bar\nu_e\).
6. Conclude \(n\to p+e^-+\bar\nu_e\).

Intermediate-State Energy Balance
1. Compare initial and final physical states for exact energy conservation.
2. Treat the internal \(W\) as an intermediate state.
3. Allow a temporary energy mismatch through the energy-time uncertainty principle.
4. Restrict the duration of that mismatch to a very short time.
5. For a pion at rest, assign the excess initial mass-energy to final-state kinetic energy.
6. Impose momentum conservation so the two outgoing particles leave back-to-back.

## Notation Choices

- Use \(A_\mu\) for the electromagnetic four-potential.
- Normalize the spatial part to \(\vec A\), not \(\vec A_{1,2,3}\), in polished notes.
- Use \(A_0\) rather than “\(A\) naught” once typeset.
- Use \(\mathbf E\) and \(\mathbf B\) for electric and magnetic fields.
- Use lowercase \(q_i\) for the quark field in equations, since the board evidence is closer to \(q\) than to uppercase \(Q\).
- Use indices \(i,j,k\) for color or generic fundamental-representation labels.
- Use \(U_{ij}\) for the group element acting on the fundamental representation.
- Use star notation in the reconstruction of the conjugate transformation, \(q^*\) and \(U^*\), because that matches the board and lecture flow.
- If representation names are needed in prose, use `fundamental`, `conjugate`, and `adjoint`; if a symbol is needed for the conjugate representation, prefer \(\bar 3\) or \(3^*\) only in explanatory prose.
- Use \(A_{ij}\) for the QCD gauge field throughout this lecture chapter, even though other texts may write \(G_\mu^a\).
- For the gluon-emission schematic, use \(q_i\to q_j + A_{ij}\) in the main text and note separately that Susskind briefly wavers on index order.
- Use weak doublets in the order \((u,d)\), \((c,s)\), \((t,b)\) and \((\nu_e,e^-)\), \((\nu_\mu,\mu^-)\), \((\nu_\tau,\tau^-)\), matching the lecture’s horizontal pairing logic.
- Use \(W^\pm\) for the charged weak bosons.
- Use \(\nu_e,\nu_\mu,\nu_\tau\) and \(\bar\nu_e,\bar\nu_\mu,\bar\nu_\tau\) explicitly rather than generic neutrino symbols once the decay channels are written out.
- Keep the lecture’s operational language that the weak symmetry acts “horizontally” and color acts “vertically.”

## Uncertain Mathematics

- The lower relation in `lecture_05_figure_02.png` is not fully legible; only the broad meaning “force component equals charge times derivative of the potential” is safe from the frame alone.
- The lecture states the electric field is determined by the gradient of \(A_0\), but does not emphasize the conventional minus sign; avoid overcommitting to a sign convention unless it is stated separately.
- The exact field symbol in the SU(3) transformation law is somewhat ambiguous between \(Q\) and \(q\); use \(q\) consistently but note the transcript’s looseness.
- The order of indices in the schematic gluon-emission rule is unstable in the lecture: he says \(IJ\), then \(JI\), then says it does not matter much for the present discussion. The chapter should pick one convention and flag that the spoken presentation was informal here.
- The self-interaction schematic \(A_{ij}\to A_{ik}+A_{kj}\) is a lecture-level index picture, not a full Yang-Mills derivation.
- The transcript’s quark-lepton table setup is garbled at the start; only the stable row/column structure should be reconstructed.
- The transcript contains a spoken slip on the down-quark charge; the correct value is \(-1/3\), not \(-2/3\).
- The lecture’s unit conversions are intentionally rough and should be presented as order-of-magnitude estimates, not precise numerical identities.
- The statement \(\alpha_{\mathrm{QCD}}\) is “close to one” and later “about \(0.2\)” is qualitative and scale-dependent in spirit; do not over-precision it in the chapter.
- The pion decay is first written through the electron channel for pedagogy, then corrected at the level of branching preference to the muon channel; do not erase that sequencing.
- The energy-time uncertainty relation is invoked heuristically for internal lines; keep it at that lecture level rather than turning it into a full formal treatment of virtual particles.