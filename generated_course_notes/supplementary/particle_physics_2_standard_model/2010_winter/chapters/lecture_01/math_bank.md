# Math Bank
## Core Equations
- [transcript-backed] \(\mathbf{E}=\mathbf{E}_1+\mathbf{E}_2\)
- [transcript-backed] \(U_{\text{field}}\propto \displaystyle \int d^3x\,\mathbf{E}^2\)
- [transcript-backed] \(U_{\text{field}}\propto \displaystyle \int d^3x\,\big(\mathbf{E}_1^2+\mathbf{E}_2^2+2\,\mathbf{E}_1\!\cdot\!\mathbf{E}_2\big)\)
- [standard reconstruction] \(U_{\text{int}}(r)\propto \displaystyle \int d^3x\,\mathbf{E}_1\!\cdot\!\mathbf{E}_2\)
- [transcript-backed] \(F_{\text{Coulomb}}(r)\propto \dfrac{q_1 q_2}{r^2}\)
- [standard reconstruction] \(F(r)=-\dfrac{dV}{dr}\)
- [standard reconstruction] \(\psi_+(x)\approx \dfrac{\psi_1(x)+\psi_2(x)}{\sqrt2}\)
- [transcript-backed] \(\gamma \leftrightarrow A\)
- [transcript-backed] \(Q(e^-)= -1,\qquad Q(e^+)=+1\)
- [transcript-backed] \(m_e \approx 0.51\,\mathrm{MeV}\)
- [transcript-backed] \(Q(u)=Q(c)=Q(t)=+\dfrac23,\qquad Q(d)=Q(s)=Q(b)=-\dfrac13\)
- [transcript-backed] \(B(q)=+\dfrac13,\qquad B(\bar q)=-\dfrac13\)
- [transcript-backed] \(p=uud,\qquad n=ddu\)
- [transcript-backed] \(Q_p=+1,\qquad Q_n=0\)
- [transcript-backed] \(n\to p+e^-+\bar\nu_e\)
- [transcript-backed] \(p\to e^+ + \gamma\) as a hypothetical baryon-violating decay
- [transcript-backed] \(m_u\sim 5\,\mathrm{MeV},\quad m_d\sim 10\,\mathrm{MeV},\quad m_s\sim 100\,\mathrm{MeV}\)
- [transcript-backed] \(m_c\sim 10^3\,\mathrm{MeV},\quad m_b\sim 5\,\mathrm{GeV},\quad m_t\sim 170\,\mathrm{GeV}\)
- [transcript-backed] \(|\bar u d\rangle,\ |u\bar d\rangle,\ |\bar u u\rangle,\ |\bar d d\rangle\) as the \(u,d\) meson flavor basis states used in the lecture
- [standard reconstruction] \(|\pi^-\rangle = |\bar u d\rangle,\qquad |\pi^+\rangle = |u\bar d\rangle\)
- [standard reconstruction] \(|\pi^0\rangle \approx \dfrac{|\bar u u\rangle-|\bar d d\rangle}{\sqrt2}\)
- [standard reconstruction] \(|\eta\rangle \approx \dfrac{|\bar u u\rangle+|\bar d d\rangle}{\sqrt2}\)
- [transcript-backed] \(m_\pi \approx 140\,\mathrm{MeV},\qquad m_\eta \approx 500\,\mathrm{MeV}\)
- [standard reconstruction] \(N_{q\bar q}=3\times 3=9\) for the light \(u,d,s\) quark-antiquark flavor combinations
- [visible] \(\gamma\)
- [visible] \(A\)

## Definitions And Objects
- Triangle of correspondence: particles, the fields whose quanta they are, and forces associated with exchange processes involving those quanta.
- \(\mathbf{E}_1,\mathbf{E}_2\): electric fields produced by two charged particles.
- Self-energy terms: the \(\mathbf{E}_1^2\) and \(\mathbf{E}_2^2\) pieces, treated as part of the isolated particles’ masses.
- Interaction term: the cross-term \(2\,\mathbf{E}_1\!\cdot\!\mathbf{E}_2\), the only piece that depends on particle separation.
- \(\psi_1(x),\psi_2(x)\): localized electron wave functions centered near the left and right proton in the molecular example.
- \(\psi_+(x)\): approximate symmetric equilibrium state of the tunneling electron.
- \(V(r)\) or \(E(r)\): qualitative effective potential-energy curve versus proton separation.
- Photon: particle symbol \(\gamma\), field symbol \(A\) on the board, boson, spin \(1\), charge \(0\), baryon number \(0\), mass \(0\).
- Electron/positron pair: \(e^\pm\), field \(\psi_e\), fermion, charges \(\mp 1\), baryon number \(0\).
- QED elementary process: one charged electron line in, one charged electron line out, one photon line attached.
- Quark flavors: \(u,d,s,c,b,t\).
- Quark field naming: in the lecture, either generic \(Q\) or the same letter as the flavor itself.
- Baryon number \(B\): bookkeeping number normalized so \(B(p)=1\), hence \(B(q)=1/3\).
- Meson: quark-antiquark composite with baryon number \(0\).
- Pion multiplet: \(\pi^+,\pi^-,\pi^0\) from the charged \(u,d\) states plus one neutral linear combination.
- Eta meson: orthogonal neutral linear combination to the pion neutral state.
- Strange baryon: baryon obtained by replacing one or more down quarks by strange quarks while preserving charge patterns.
- Strange mesons / \(K\) mesons: mesons containing one strange or anti-strange quark.

## Derivation Steps
Classical field-energy route:
1. Start with one charge and its electric field \(\mathbf{E}_1\); its field energy is a self-energy.
2. Do the same for the second charge and \(\mathbf{E}_2\).
3. For the two-charge system, add fields before squaring: \(\mathbf{E}=\mathbf{E}_1+\mathbf{E}_2\).
4. Expand \(\mathbf{E}^2\) into two self-terms and one cross-term.
5. Treat the self-terms as position-independent contributions already absorbed into particle masses.
6. Identify the cross-term as the only separation-dependent part of the energy.
7. Read that separation-dependent energy as the origin of the force.
8. Recover the Coulomb behavior qualitatively from the overlap of the two fields.

Two-proton one-electron molecular route:
1. Start with two far-separated protons and one electron.
2. Build one hydrogenic ground-state wave function near the left proton.
3. By symmetry, build another state of the same energy near the right proton.
4. At finite separation, allow tunneling between the two localized states.
5. Form a long-time equilibrium state with support near both protons.
6. Normalize the first approximation as \((\psi_1+\psi_2)/\sqrt2\).
7. Correct that sum slightly in the overlap region; the exact equilibrium state is not exactly the naive sum.
8. Infer that the equilibrium energy is lower than at infinite separation.
9. Plot that lowered energy as a function of proton separation.
10. Interpret the slope of that curve as an effective attractive force.

From lowered energy to covalent bonding:
1. Treat the separation-dependent energy as an effective potential \(V(r)\).
2. Use the force-energy relation \(F=-dV/dr\).
3. Conclude that the lowered equilibrium energy produces attraction between the protons.
4. Add the caveat that Coulomb repulsion is still present.
5. Conclude that binding depends on competition between short-range exchange attraction and electrostatic repulsion.

Photon-exchange route back to electrodynamics:
1. Replace the classical field picture by a quantum picture of emitted and reabsorbed photons.
2. Treat a charged particle as dressed by a superposition of states with different photon content.
3. For two charged particles, allow a photon emitted by one to be absorbed by the other.
4. Identify that shared-photon process as the source of a separation-dependent energy shift.
5. Read the Coulomb interaction as the exchanged-photon version of the same logic used in the molecular example.

Baryon-number bookkeeping:
1. Fix \(B(p)=1\) and \(B(n)=1\) by convention.
2. Write the proton as three quarks.
3. Assign \(B(q)=1/3\) so that three quarks give baryon number \(1\).
4. Assign \(B(\bar q)=-1/3\) for antiquarks.
5. Treat baryon-number conservation as empirically excellent but not mathematically guaranteed to be absolute.
6. Use hypothetical proton decay to frame baryon violation as an open physical question.

Proton-neutron comparison:
1. Write \(n=ddu\) and \(p=uud\).
2. Ignore electromagnetism and notice the near-symmetry under \(u\leftrightarrow d\).
3. Break that symmetry by \(m_d>m_u\).
4. Infer that the neutron should be slightly heavier.
5. Note the competing electromagnetic self-energy that would by itself tend to make the proton heavier.
6. Conclude that the observed mass ordering says the \(d-u\) mass difference wins.

Neutral-meson superposition route:
1. Start from the charged flavor states \(|\bar u d\rangle\) and \(|u\bar d\rangle\).
2. Write the neutral flavor basis states \(|\bar u u\rangle\) and \(|\bar d d\rangle\).
3. Form the normalized sum and difference.
4. Identify one neutral combination as part of the pion multiplet.
5. Identify the orthogonal neutral combination as the eta-like state.
6. Use mass proximity, not just charge counting, to justify grouping the pion triplet together.

## Notation Choices
- Use \(\mathbf{E}\) for electric field vectors and reserve plain \(E\) for energy.
- Use \(V(r)\) for the proton-separation curve in the chapter draft; mention in passing that the board image itself does not decide between \(V(r)\) and \(E(r)\).
- Use \(r\) for proton separation in qualitative force-energy formulas.
- Use \(\psi_1(x)\) and \(\psi_2(x)\) for the left- and right-localized molecular wave functions; use \(\psi_+(x)\) for the symmetric equilibrium state.
- Keep \(\gamma\) for the photon particle symbol.
- Keep \(A\) for the photon field on first presentation because that is what the board visibly shows.
- Upgrade to \(A_\mu\) only if the chapter explicitly labels that as a cleaned standard completion.
- Use \(e^-\) and \(e^+\) when charge matters; use \(e^\pm\) for table-style summary rows.
- Use \(\psi_e\) for the electron field.
- Use \(Q\) for electric charge, measured in units of the electron charge.
- Use \(B\) for baryon number.
- Use constituent notation \(uud\), \(ddu\), \(\bar u d\), \(u\bar d\) for composition statements.
- Use ket notation only when linear combinations matter, especially for neutral mesons.
- Keep the QED interaction notation schematic as a field product such as \(\psi_e^\dagger \psi_e A\) if needed for exposition; do not silently replace the lecture with the full textbook Dirac interaction term.
- Treat MeV and GeV as mass units with \(c=1\) implicitly understood, matching the lecture’s “mass as energy” usage.

## Uncertain Mathematics
- The transcript’s charge-factored electric-field notation with a hat is garbled; do not pretend the exact normalization or symbol is recoverable.
- The field-energy formula is used only schematically in the lecture; constants such as \(1/2\), \(\epsilon_0\), or unit-system factors should not be inserted unless explicitly marked as a standard cleanup.
- The cross-term is clearly the interaction piece, but the lecture does not derive its exact coefficient or carry the integral to a full Coulomb-potential formula on the board.
- The molecular equilibrium state is only approximately \((\psi_1+\psi_2)/\sqrt2\); the lecture explicitly says the exact wave function differs slightly in the middle region.
- The lower board graph in `lecture_01_figure_04.png` has no readable axis labels, so \(V(r)\) versus \(E(r)\) remains a note-writer choice.
- The QED interaction Lagrangian is not written explicitly in the transcript; a full expression such as \(\mathcal L_{\text{int}}=-e\,\bar\psi\gamma^\mu\psi A_\mu\) would be a standard completion, not a direct lecture transcription.
- The proton and neutron mass numbers are noisy in the transcript; retain only the stable claim that the neutron is slightly heavier by about \(1.3\) to \(1.4\,\mathrm{MeV}\).
- The meson-charge segment is verbally messy; reconstruct charges from flavor content, not from the raw line-by-line wording.
- The identification \(|\pi^0\rangle \sim (|\bar u u\rangle-|\bar d d\rangle)/\sqrt2\) and \(|\eta\rangle \sim (|\bar u u\rangle+|\bar d d\rangle)/\sqrt2\) is the standard reading consistent with the lecture, but the board does not visibly display these formulas.
- The strange-meson list is transcript-backed, but the charge ordering is easy to scramble; state those constituents carefully if they are written out later.