# Math Bank
## Core Equations
- \(\psi^\dagger(\cdots + \alpha_i \partial_i \psi - \beta m \psi)=\mathcal{L}\) [visible]
- \((\partial_t + \alpha_i \partial_i - \beta m)\psi = 0\) [transcript-backed]
- \(\mathcal{L}_D = \psi^\dagger(\partial_t + \alpha_i \partial_i - \beta m)\psi\) [standard reconstruction]
- \(\bar{\psi} = \psi^\dagger \beta = \psi^\dagger \gamma^0\) [transcript-backed]
- \(\gamma^0 \equiv \beta\) [transcript-backed]
- \(\gamma^i \equiv \beta \alpha_i\) [transcript-backed]
- \(\mathcal{L}_D = \bar{\psi}(\gamma^0 \partial_t + \gamma^i \partial_i + m)\psi\) [transcript-backed]
- \(\mathcal{L}_D = \bar{\psi}(i\gamma^\mu \partial_\mu - m)\psi\) [standard reconstruction]
- \(\bar{\psi}\psi\) is a scalar [transcript-backed]
- \(\bar{\psi}\gamma^\mu\psi\) is a four-vector [transcript-backed]
- \(\gamma_5^2 = 1\) [transcript-backed]
- \(\psi = \psi_L + \psi_R\) [standard reconstruction]
- \(\bar{\psi}\psi = \psi_L^\dagger \psi_R + \psi_R^\dagger \psi_L\) [visible]
- \(G_Y\big(\psi_L^\dagger \phi\,\psi_R + \psi_R^\dagger \phi^\dagger \psi_L\big)\) [standard reconstruction]
- \(\phi = F + H\) [transcript-backed]
- \(G_Y\big(\psi_L^\dagger \phi\,\psi_R + \psi_R^\dagger \phi^\dagger \psi_L\big) = G_YF\big(\psi_L^\dagger \psi_R + \psi_R^\dagger \psi_L\big) + G_YH\big(\psi_L^\dagger \psi_R + \psi_R^\dagger \psi_L\big)\) [transcript-backed]
- \(m_f = G_Y F\) [transcript-backed]
- \(F \sim 200\,\mathrm{GeV}\) [transcript-backed]
- \(V(\phi) = -\frac{\mu^2}{2}\phi^2 + \frac{\lambda}{4}\phi^4\) [transcript-backed]
- \(\frac{dV}{d\phi} = -\mu^2 \phi + \lambda \phi^3 = 0\) [transcript-backed]
- \(\phi^2 = \frac{\mu^2}{\lambda}\) at the minimum [transcript-backed]
- \(F^2 = \frac{\mu^2}{\lambda}\) [transcript-backed]
- \(V_{\text{Coulomb}}(r) \sim \frac{e^2}{r}\) [transcript-backed]
- \(F_{\text{Coulomb}}(r) \sim \frac{e^2}{r^2}\) [transcript-backed]
- \(e = e(r)\) or equivalently \(e=e(1/r)\) [transcript-backed]
- \(V_{\text{QCD}}(r) \propto r\) [transcript-backed]
- \(E \sim \frac{\hbar c}{r}\) [transcript-backed]
- \(F_G(r) \sim \frac{G E^2}{c^4 r^2}\) [standard reconstruction]
- \(F_G(r) \sim \frac{G\hbar^2}{c^2 r^4}\) after \(E\sim \hbar c/r\) [standard reconstruction]
- \(r_P \sim \sqrt{\frac{G\hbar}{c^3}}\) [standard reconstruction]
- \(\mu_{\text{unif}} \sim 10^{16}\,\mathrm{GeV}\) [transcript-backed]

## Definitions And Objects
- \(\psi\): Dirac spinor field.
- \(\psi^\dagger\): Hermitian conjugate used in the board-level construction of the Dirac Lagrangian.
- \(\bar{\psi}\): Dirac adjoint, taken in the notes as \(\psi^\dagger \gamma^0\).
- \(\alpha_i,\beta\): older Dirac-matrix notation kept briefly because the lecture starts there.
- \(\gamma^\mu\): covariant Dirac matrices after the notation change.
- \(\gamma_5\): chirality operator in the lecture; eigenvalues \(\pm 1\) correspond to right/left-handed components.
- \(\psi_L,\psi_R\): left- and right-chiral pieces of \(\psi\).
- Dirac mass term: the \(\bar{\psi}\psi\) term; lecture meaning is “flips chirality.”
- Weak-interaction charge assignment in the lecture: left-handed fermion charged under the relevant weak \(SU(2)\), right-handed fermion uncharged.
- \(\phi\): Higgs field; lecture keeps the simpler scalar notation instead of full doublet components.
- \(F\): nonfluctuating shifted value of the Higgs field; use uppercase consistently.
- \(H\): Higgs fluctuation about the shifted value.
- \(G_Y\): Yukawa coupling; a different pure number for each fermion species.
- \(\mu\): Higgs mass-scale parameter in the potential; dimension of mass.
- \(\lambda\): quartic Higgs self-coupling; dimensionless.
- Running charge: effective electromagnetic coupling depending on scale.
- Chromoelectric flux tube: lecture picture for long-distance QCD behavior.
- \(r_P\): Planck-length scale from the short-distance gravity estimate.
- \(\mu_{\text{unif}}\): qualitative unification scale where gauge couplings approximately meet.

## Derivation Steps
Dirac Lagrangian from the Dirac equation
1. Start from the older \(\alpha,\beta\) form of the Dirac equation.
2. Move the mass term to the left so the equation is written as something equal to zero.
3. Multiply the equation by \(\psi^\dagger\).
4. Treat the resulting expression as the Lagrangian density whose variation with respect to \(\psi^\dagger\) returns the Dirac equation.
5. Interpret derivative terms as kinetic/hopping terms and the mass term as a local absorption-emission term with no derivatives.

Covariant rewrite
1. Define \(\bar{\psi}=\psi^\dagger \beta\).
2. Rename \(\beta\) as \(\gamma^0\).
3. Rename \(\beta\alpha_i\) as \(\gamma^i\).
4. Rewrite the time and space derivative terms together as a \(\gamma^\mu \partial_\mu\) structure.
5. Standardize the final displayed form as \(\bar{\psi}(i\gamma^\mu\partial_\mu-m)\psi\) in the notes.

Chirality decomposition of the mass term
1. Introduce \(\gamma_5\) and its eigenvalues \(\pm 1\).
2. Split the field into \(\psi_L\) and \(\psi_R\).
3. Inspect the kinetic terms and note that they do not mix left and right.
4. Expand the scalar bilinear \(\bar{\psi}\psi\).
5. Obtain \(\bar{\psi}\psi=\psi_L^\dagger\psi_R+\psi_R^\dagger\psi_L\).
6. Read the Dirac mass term as the operator that flips chirality.

Weak-gauge obstruction and Higgs repair
1. Recall the lecture’s weak-coupling rule: the \(W\) couples only to left-handed fermions.
2. Conclude that \(\psi_L\) and \(\psi_R\) do not transform the same way under the relevant weak symmetry.
3. Therefore a bare \(\psi_L^\dagger\psi_R+\psi_R^\dagger\psi_L\) term is not gauge-legal in the chiral theory being discussed.
4. Insert a Higgs field \(\phi\) and \(\phi^\dagger\) so the weak charge mismatch is carried by the Higgs.
5. Write the Yukawa term \(G_Y(\psi_L^\dagger \phi\,\psi_R+\psi_R^\dagger \phi^\dagger\psi_L)\).

Mass generation after symmetry breaking
1. Use the shifted-field decomposition \(\phi=F+H\).
2. Substitute this into the Yukawa term.
3. Separate the result into an \(F\)-piece and an \(H\)-piece.
4. Identify the \(F\)-piece as the fermion mass term.
5. Identify the \(H\)-piece as the Higgs-fermion interaction vertex.
6. Read off \(m_f=G_YF\).

Higgs-potential minimum
1. Start from \(V(\phi)=-\mu^2\phi^2/2+\lambda\phi^4/4\).
2. Differentiate with respect to \(\phi\).
3. Set \(-\mu^2\phi+\lambda\phi^3=0\).
4. Divide by \(\phi\) away from the trivial origin.
5. Obtain \(\phi^2=\mu^2/\lambda\).
6. Identify the shifted vacuum value as \(F\), so \(F^2=\mu^2/\lambda\).

QED running-coupling logic
1. Use conductor and dielectric screening as the classical template.
2. Replace material polarization by vacuum polarization from virtual \(e^+e^-\) pairs.
3. Note that at large distance the charge is more screened.
4. Bring probes closer so larger screening clouds stop contributing.
5. Conclude that the effective charge grows as the distance decreases.
6. Re-express this as a slow logarithmic growth with inverse distance or energy.

QCD opposite running
1. Recall that gluons self-interact.
2. Use the flux-tube picture to describe long-distance confinement.
3. Read the long-distance potential as approximately linear in separation.
4. Translate that behavior into an effective coupling that is larger at large distance.
5. Therefore, as inverse distance increases, the QCD coupling decreases.

Short-distance gravity heuristic
1. Start from the relativistic replacement of mass by energy in Newton’s force law.
2. Use uncertainty to estimate \(p\sim \hbar/r\) for particles localized within distance \(r\).
3. For relativistic particles, use \(E\sim pc\sim \hbar c/r\).
4. Insert this energy into the gravitational force estimate.
5. Find a short-distance growth stronger than the ordinary \(1/r^2\) law.
6. Compare the result with the electromagnetic force.
7. Extract the characteristic crossover length \(r_P\sim \sqrt{G\hbar/c^3}\).

## Notation Choices
- Use \(\mathcal{L}_D\) for the Dirac Lagrangian once the notes move from board reproduction to clean typesetting.
- Keep one displayed older-notation formula with \(\alpha_i,\beta\) before converting to \(\gamma^\mu\); do not erase that stage from the lecture.
- Use \(\bar{\psi}=\psi^\dagger\gamma^0\) as the note-standard definition.
- Use \(\mu=0,1,2,3\) for spacetime indices in the cleaned notes, even though the transcript is loose about counting.
- Use \(\partial_\mu\) rather than “\(d/dx_\mu\)” once the notes are stabilized.
- Use uppercase \(F\) for the Higgs-field shift throughout; do not alternate with lowercase \(f\).
- Use \(H\) for the Higgs fluctuation about the shifted vacuum.
- Use \(G_Y\) for Yukawa couplings, matching the lecture’s spoken notation.
- Use “chirality” rather than “helicity” for \(\gamma_5\); the lecture briefly slips and then corrects itself.
- Use \(\phi\) as the Higgs symbol in this chapter, since that is the lecture’s running notation.
- Mention that the Higgs is an \(SU(2)\) doublet, but do not expand into full component notation unless later transcript material demands it.
- For running couplings, use \(e(r)\) or \(e(\mu)\) consistently; if the chapter uses RG-style notation later, define \(\mu\sim 1/r\).
- Keep \(\hbar\) and \(c\) explicit in the Planck-length heuristic derivation; do not silently switch to strict natural units there.

## Uncertain Mathematics
- The board-level old Dirac equation and Lagrangian do not securely fix the \(i\)-factor and sign conventions; the final notes should state one convention explicitly and mention that the board form was schematic.
- The frame showing the covariant Dirac Lagrangian supports the structure but not the exact cleaned form; \(\bar{\psi}(i\gamma^\mu\partial_\mu-m)\psi\) is a note-level stabilization.
- The lecture’s spoken definition of \(\gamma_5\) omits the conventional extra factor of \(i\); if a canonical formula is written, flag it as a standard convention rather than literal board transcription.
- The decomposition \(\bar{\psi}\psi=\psi_L^\dagger\psi_R+\psi_R^\dagger\psi_L\) is strongly supported, but the exact projector formalism is not developed in the lecture and should not be imported unnecessarily.
- The Higgs-inserted chiral coupling is only partially legible in the frame; the placement of \(\phi^\dagger\) in the second term should be treated as cautious standard completion.
- The lecture talks schematically about weak charge and \(SU(2)\) transformation properties; do not over-specify hypercharge assignments or full Standard Model index contractions here.
- The numerical estimate \(F\sim 200\,\mathrm{GeV}\) is lecture-level and rough; do not turn it into an overly precise electroweak-fit statement.
- The spoken remarks about \(\lambda\) being “small but not absurdly small” are qualitative only; keep them qualitative.
- The transcript briefly says “\(f\) is dimensionless,” which is incorrect in context; the notes should silently correct this to “\(F\) has dimensions of mass.”
- The unification discussion gives approximate scales and qualitative curve behavior; keep the scale as order-of-magnitude, not as a precision result.
- The gravity section contains algebraic restarts and dimensional corrections; only the cleaned heuristic chain should survive into the notes.
- The transcript’s “one over \(r^3\)” remark refers to energy before being corrected to force as \(1/r^4\); the notes should present the corrected distinction cleanly.
- The garbled fragment near `01:18:55` should be ignored entirely.