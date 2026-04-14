# Math Bank
## Core Equations
- Regge-line statement: \(J \propto M^2\) for hadronic families, with approximately parallel trajectories across different families [transcript-backed]
- Quantized Regge-spacing statement: \(\Delta J = 1 \Rightarrow \Delta M^2 \approx \text{constant}\) along a trajectory [transcript-backed]
- Nonrelativistic particle energy with additive internal term: \(E_{\mathrm{nr}} = \dfrac{p^2}{2m} + B\) [transcript-backed]
- Relativistic particle energy with \(c\) restored: \(E = \sqrt{p^2 c^2 + m^2 c^4}\) [transcript-backed]
- Slow-particle expansion: \(E \approx mc^2 + \dfrac{p^2}{2m}\) for \(p^2 c^2 \ll m^2 c^4\) [transcript-backed]
- Longitudinal/transverse split after setting \(c=1\): \(E_i = \sqrt{P_{zi}^2 + p_{\perp i}^2 + m_i^2}\) with \(p_{\perp i}^2 = p_{xi}^2 + p_{yi}^2\) [transcript-backed]
- Board expansion for large longitudinal momentum: \(P_3\sqrt{1+\dfrac{p_x^2+p_y^2+m^2}{P_3^2}}\) [visible]
- Large-\(P_z\) expansion: \(E_i \approx P_{zi} + \dfrac{p_{\perp i}^2 + m_i^2}{2P_{zi}}\) [transcript-backed]
- Many-particle boosted energy: \(E = \sum_i P_{zi} + \sum_i \dfrac{p_{\perp i}^2}{2P_{zi}} + \sum_i \dfrac{m_i^2}{2P_{zi}}\) [visible]
- Hamiltonian/time-evolution identification: \(i\,\partial_t = H\) [visible]
- Transverse Hamiltonian after dropping the conserved additive constant: \(H = \sum_i \left(\dfrac{p_{\perp i}^2}{2P_{zi}} + \dfrac{m_i^2}{2P_{zi}}\right)\) [visible]
- Rotational-energy reminder used in the electron/hadron comparison: \(E_{\mathrm{rot}} \sim \dfrac{L^2}{2I}\) [transcript-backed]
- Moment of inertia scaling: \(I \sim M R^2\) [transcript-backed]
- Discrete open-string energy, board form: \(E = m\sum_i \dfrac{\dot X_i^2}{2} + \dfrac{k}{2}(X_i - X_{i+1})^2\) [visible]
- Discrete open-string energy, cleaned notation: \(E = \sum_i \left(\dfrac{\mu}{2}\dot X_i^2 + \dfrac{k}{2}(X_i - X_{i+1})^2\right)\) [standard reconstruction]
- Continuum replacement: \(X_i - X_{i+1} \rightarrow \dfrac{\partial X}{\partial \sigma}\) [visible]
- Continuum Hamiltonian, cautious cleaned form: \(E \sim \int_0^\pi d\sigma \left(\dfrac{\dot X^2(\sigma)}{2} + \left(\dfrac{\partial X}{\partial \sigma}\right)^2\right)\) [standard reconstruction]
- Internal-energy identification in the boosted frame: \(H_{\mathrm{int}} \propto M^2\) [transcript-backed]
- Uniformly stretched string estimate: \(\dfrac{\partial X}{\partial \sigma} \sim \dfrac{L}{\pi}\) [transcript-backed]
- Hooke-law scaling in the effective nonrelativistic description: \(H_{\mathrm{stretch}} \propto L^2\) [transcript-backed]
- Rest-frame tension scaling: \(E_{\mathrm{rest}} = M \propto L\) [transcript-backed]
- Constant-tension summary form: \(E_{\mathrm{rest}} = T\,L\) [standard reconstruction]
- Oscillator-spectrum implication: \(\Delta H_{\mathrm{int}} = \text{const} \Rightarrow \Delta M^2 = \text{const}\) [transcript-backed]

## Definitions And Objects
- Regge trajectory: a family of hadronic states whose angular momentum and \(M^2\) lie approximately on a straight line.
- Universal Regge slope: the empirical claim that different hadronic families have approximately the same slope in the \(J\) versus \(M^2\) plot.
- World line: the one-dimensional spacetime history of a point particle.
- World sheet: the two-dimensional spacetime history replacing the world line for a string.
- Infinite-momentum frame / light-cone frame: the highly boosted frame in which all constituents carry large positive longitudinal momentum \(P_z\).
- Transverse momentum: \(p_\perp = (p_x,p_y)\), with \(p_\perp^2 = p_x^2 + p_y^2\).
- Internal or binding energy in the boosted description: the part of the Hamiltonian independent of transverse center-of-mass motion, identified with \(M^2\) rather than \(M\).
- Open string: a string with two endpoints; in this lecture its internal coordinate is taken as \(\sigma \in [0,\pi]\).
- Discrete string model: a chain of point masses connected by Hooke-law springs.
- Continuum limit: the limit in which the bead spacing goes to zero, the bead masses go to zero appropriately, and the spring constant scales so the continuum energy stays finite.
- String stretching term: the contribution controlled by \(\partial_\sigma X\), interpreted as potential energy.
- String tension: constant energy per unit length in the rest-frame flux-tube picture.
- Whole-string mass \(M\): the rest mass of the composite string-like particle, including internal vibrational and stretching energy.
- Bead mass \(\mu\): the mass assigned to each discretized point in the chain model; should be separated notationally from \(M\).

## Derivation Steps
Nonrelativistic expansion of relativistic energy
1. Start from \(E = \sqrt{p^2 c^2 + m^2 c^4}\).
2. Assume \(p^2 c^2 \ll m^2 c^4\).
3. Factor out \(m^2 c^4\): \(E = mc^2 \sqrt{1 + \dfrac{p^2}{m^2 c^2}}\).
4. Use \(\sqrt{1+\epsilon} \approx 1 + \epsilon/2\) for small \(\epsilon\).
5. Obtain \(E \approx mc^2 + \dfrac{p^2}{2m}\).
6. Read \(mc^2\) as the additive rest or internal term and \(\dfrac{p^2}{2m}\) as the nonrelativistic kinetic term.

Large-\(P_z\) or infinite-momentum expansion
1. Set \(c=1\) after the initial relativistic discussion.
2. Split momentum into longitudinal and transverse pieces: \(p^2 = p_z^2 + p_\perp^2\).
3. Boost the entire system so every constituent has large positive \(P_z\), while \(p_\perp\) and \(m\) remain fixed.
4. Write \(E_i = \sqrt{P_{zi}^2 + p_{\perp i}^2 + m_i^2} = P_{zi}\sqrt{1+\dfrac{p_{\perp i}^2+m_i^2}{P_{zi}^2}}\).
5. Expand for large \(P_{zi}\): \(E_i \approx P_{zi} + \dfrac{p_{\perp i}^2 + m_i^2}{2P_{zi}}\).
6. Sum over particles to get \(E = \sum_i P_{zi} + \sum_i \dfrac{p_{\perp i}^2}{2P_{zi}} + \sum_i \dfrac{m_i^2}{2P_{zi}}\).
7. Drop \(\sum_i P_{zi}\) as a conserved additive constant.
8. Interpret the remainder as the Hamiltonian governing slow transverse evolution.

Interpretation of the boosted Hamiltonian
1. Compare \(H = \sum_i \left(\dfrac{p_{\perp i}^2}{2P_{zi}} + \dfrac{m_i^2}{2P_{zi}}\right)\) with a nonrelativistic Hamiltonian.
2. Identify \(P_{zi}\) as the effective transverse inertia.
3. Identify the \(m_i^2\) term as the analog of internal or binding energy.
4. Use \(i\partial_t = H\) to explain why energies become small when \(P_z\) is large: evolution is time-dilated.
5. Conclude that the boosted relativistic system behaves nonrelativistically in the transverse plane.

Discrete string to continuum string
1. Model the open string as beads with nearest-neighbor spring interactions.
2. Write \(E = \sum_i \left(\dfrac{\mu}{2}\dot X_i^2 + \dfrac{k}{2}(X_i - X_{i+1})^2\right)\).
3. Let the bead spacing go to zero.
4. Let the bead masses go to zero in a correlated way so the total string mass remains finite.
5. Scale the spring constant so the continuum limit remains nontrivial.
6. Introduce a continuous coordinate \(\sigma\) along the string.
7. Choose \(\sigma \in [0,\pi]\) for the open string.
8. Replace \(\sum_i \rightarrow \int_0^\pi d\sigma\).
9. Replace \(X_i - X_{i+1}\) by \(\partial_\sigma X\).
10. Obtain the continuum Hamiltonian \(E \sim \int_0^\pi d\sigma \left(\dfrac{\dot X^2}{2} + (\partial_\sigma X)^2\right)\), up to normalization choices.

From continuum internal energy to \(M^2\)
1. Treat the string as a composite object with center-of-mass motion plus internal vibrational/stretching motion.
2. Separate overall motion from internal motion.
3. Use the light-cone or infinite-momentum argument to identify internal energy with \(M^2\), not \(M\).
4. Read the continuum Hamiltonian as the internal Hamiltonian of the whole string-like particle.
5. Conclude that oscillator-like excitation of the string gives evenly spaced increments in \(M^2\).

From Hooke-law stretching to rest-frame tension
1. Consider a uniformly stretched string of physical length \(L\).
2. Estimate \(\partial_\sigma X \sim L/\pi\).
3. Insert this into the potential term of the continuum Hamiltonian.
4. Infer \(H_{\mathrm{stretch}} \propto L^2\) in the effective nonrelativistic boosted description.
5. Use the identification \(H_{\mathrm{int}} \propto M^2\).
6. Deduce \(M^2 \propto L^2\), hence \(M \propto L\).
7. Reinterpret \(M\) as rest-frame energy to get a constant-tension picture \(E_{\mathrm{rest}} \propto L\).

Why hadrons show rotational excitations but electrons do not
1. Use \(E_{\mathrm{rot}} \sim \dfrac{L^2}{2I}\).
2. Use \(I \sim M R^2\).
3. For a very small object, \(R\) is tiny, so \(I\) is tiny.
4. Therefore \(1/I\) is huge, and the first excitation costs a large energy.
5. Hadrons, being much larger, have much larger \(I\), so their low-lying rotational excitations are accessible.
6. Electrons, being much smaller, would have excitations far beyond accessible collision energies.

## Notation Choices
- Use \(J\) for the vertical axis of the Regge plot in the final notes, with a brief remark that the lecture informally alternates between angular momentum, spin, and \(L\).
- Use \(M\) for the total rest mass of the string-like particle throughout the later sections.
- Do not reuse \(m\) for both whole-string rest mass and bead mass in the written chapter.
- Replace the bead mass \(m\) in the board formula by \(\mu\) or \(m_0\) in cleaned derivations.
- Standardize the large longitudinal momentum as \(P_z\), not \(P_3\), while noting once that the board shows both.
- Define \(p_\perp^2 = p_x^2 + p_y^2\) and use that notation consistently after the first split.
- Use \(X_i(t)\) for the discrete transverse coordinate of bead \(i\).
- Use \(X(\sigma,t)\) for the continuum transverse coordinate.
- Use \(\dot X = \partial_t X\).
- Use \(\partial_\sigma X\) rather than \(dX/d\sigma\) once the continuum field notation is adopted.
- Keep \(\sigma \in [0,\pi]\) for open strings, matching the lecture’s convention and later motivation for closed strings on \([0,2\pi]\).
- Write the quantum-mechanical time-evolution identity as \(i\,\partial_t = H\) with an explicit note that \(\hbar=1\) is being used there; the lecture verbally half-restores \(\hbar\), but the board does not.
- Distinguish clearly between the conserved additive term \(\sum_i P_{zi}\) and the dynamical Hamiltonian that remains after it is dropped.

## Uncertain Mathematics
- The lecture does not write an explicit Regge formula with slope and intercept such as \(J=\alpha' M^2+a\); if that form is introduced later, it should be marked as a standard reconstruction, not as board-backed lecture notation.
- The exact particle labels in the scattering diagrams are not secure from the frames; the math bank should preserve only the channel logic, not overcommit to line labels.
- In the frames, the upper boosted-energy line alternates between \(P_3\) and \(P_z\); the final notes should choose one notation and mention the normalization choice once.
- The exact placement of summation signs in the many-particle Hamiltonian is not perfectly legible on the board; the transcript supports the intended summed structure, but the final notes should not imply the photograph fully fixes every delimiter.
- The operator identity is verbally “\(i\hbar\,d/dt\), probably,” while the board suggests \(i\,\partial_t = H\); the final notes should explicitly state the units choice rather than pretend the lecture was fully consistent here.
- The discrete string board equation is partially occluded and uses a single \(m\) that is ambiguous between bead mass and whole-string mass; the cleaned derivation must rename the bead mass.
- The continuum Hamiltonian coefficients are not fully recoverable from the board alone; Susskind explicitly says he has absorbed constants and normalized \(k\) conventionally.
- In the lower continuum integral, the potential term is mid-writing in the frame; the square on \((\partial_\sigma X)^2\) is supported by the lecture logic and the upper-right arrow, but not cleanly by the lower line itself.
- The relation “internal energy corresponds to \(M^2\)” is lecture-central, but the exact proportionality constants and factors of \(2P_z\) are partly absorbed into conventions and rescalings.
- The statement that there are no independent longitudinal degrees of freedom is made qualitatively in this lecture; do not promote it here into a fully written constraint equation unless later lectures derive it.