# Math Bank
## Core Equations
- [visible] \(\lvert x,y\rangle=-\lvert y,x\rangle\).
- [visible] \(\psi^\dagger(x)\psi^\dagger(y)=-\,\psi^\dagger(y)\psi^\dagger(x)\).
- [visible] \(\{\psi^\dagger(x),\psi^\dagger(y)\}=0\).
- [visible] \(\{\psi^\dagger(x),\psi^\dagger(x)\}=0\Rightarrow 2(\psi^\dagger(x))^2=0\Rightarrow (\psi^\dagger(x))^2=0\).
- [transcript-backed] \(\psi^\dagger(x)\psi^\dagger(y)=\psi^\dagger(y)\psi^\dagger(x)\) for the bosonic exchange step.
- [standard reconstruction] \([a,a^\dagger]=1\).
- [standard reconstruction] \(\{a,a^\dagger\}=1,\qquad a^2=(a^\dagger)^2=0\).
- [transcript-backed] \(n_{\text{boson}}=0,1,2,\dots\).
- [transcript-backed] \(n_{\text{fermion}}=0,1\).

- [transcript-backed] \(i\,\partial_t\psi=-\,i\,\partial_x\psi\).
- [transcript-backed] \(H=P\).
- [transcript-backed] \(E=p\).
- [transcript-backed] \(E^2=p^2+m^2\).
- [transcript-backed] \(H\psi_1=P\psi_1,\qquad H\psi_2=-P\psi_2\).
- [transcript-backed] \(H\psi=\alpha P\,\psi\).
- [transcript-backed] \(H=\alpha P+\beta m\).
- [transcript-backed] \(\alpha^2=1,\qquad \beta^2=1,\qquad \alpha\beta+\beta\alpha=0\).
- [transcript-backed] \(H^2=P^2+m^2\).

- [visible] \(H=\alpha\cdot P=\alpha_xP_x+\alpha_yP_y+\alpha_zP_z\).
- [transcript-backed] \(E^2=\mathbf p^2=p_x^2+p_y^2+p_z^2\).
- [transcript-backed] \(\alpha_x^2=\alpha_y^2=\alpha_z^2=1\).
- [transcript-backed] \(\alpha_i\alpha_j+\alpha_j\alpha_i=0\quad (i\neq j)\).
- [transcript-backed] \(\alpha_x=\sigma_x,\qquad \alpha_y=\sigma_y,\qquad \alpha_z=\sigma_z\).
- [visible] \(\sigma_z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}\).
- [visible] \(H=\sigma\cdot p\).
- [standard reconstruction] \(H=\boldsymbol{\sigma}\cdot\mathbf p\).
- [transcript-backed] \(\sigma_x=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad \sigma_y=\begin{pmatrix}0&-i\\ i&0\end{pmatrix},\qquad \sigma_z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}\).
- [standard reconstruction] \(\boldsymbol{\sigma}\cdot\mathbf p=|\mathbf p|\,(\boldsymbol{\sigma}\cdot\hat{\mathbf p})\), with eigenvalues \(\pm |\mathbf p|\).

- [transcript-backed] \(H=\boldsymbol{\sigma}\cdot\mathbf p+\beta m\) is the naive \(2\times2\) massive trial.
- [transcript-backed] \(\sigma_i\beta+\beta\sigma_i=0\quad\text{for all }i\) would be required.
- [transcript-backed] No \(2\times2\) matrix anti-commutes with all three Pauli matrices.
- [standard reconstruction] \(H=\boldsymbol{\alpha}\cdot\mathbf P+\beta m\) for the \(4\times4\) Dirac-matrix stage.
- [standard reconstruction] \(\{\alpha_i,\alpha_j\}=2\delta_{ij},\qquad \{\alpha_i,\beta\}=0,\qquad \beta^2=1\).
- [standard reconstruction] \(\alpha_i=\begin{pmatrix}\sigma_i&0\\0&-\sigma_i\end{pmatrix},\qquad \beta=\begin{pmatrix}0&I\\I&0\end{pmatrix}\).
- [standard reconstruction] \(\Sigma_i=\begin{pmatrix}\sigma_i&0\\0&\sigma_i\end{pmatrix}\) for the true spin operator, if explicitly needed.

- [standard reconstruction] \(\dot L=i[H,L]\) in units \(\hbar=1\).
- [standard reconstruction] \([x,P_x]=i\).
- [transcript-backed] \(\dot x=\alpha_x\).
- [transcript-backed] \(\dot\alpha_x=i[H,\alpha_x]\neq0\).

- [standard reconstruction] \(E_{\text{hole}}=-E_{\text{negative electron}}>0\).
- [standard reconstruction] \(b^\dagger(p)\equiv a(-p)\) as the negative-energy reinterpretation.
- [standard reconstruction] \(\psi(x)\sim \int_0^\infty dp\,\big[a(p)e^{-ipx}+b^\dagger(p)e^{+ipx}\big]\).
- [transcript-backed] \(H_{\text{int}}\sim \psi^\dagger(x)\psi(x)A(x)\).

## Definitions And Objects
- \(\lvert x,y\rangle\): two-particle state with slot labels; \(x\) and \(y\) label particle positions, not Cartesian coordinates.
- \(\psi^\dagger(x)\), \(\psi(x)\): creation and annihilation operators at position \(x\); in later parts of the lecture \(\psi\) also denotes a single-particle wavefunction or spinor.
- \(\{A,B\}=AB+BA\): anti-commutator.
- \([A,B]=AB-BA\): commutator.
- \(a,a^\dagger\): single-mode bosonic or fermionic ladder operators used for the occupation-number comparison.
- \(\psi_1,\psi_2\): right-moving and left-moving one-dimensional components/species in the review construction.
- \(\alpha,\beta\): matrices introduced first in the one-dimensional Dirac review; \(\beta\) is the mass-coupling matrix.
- \(\boldsymbol{\alpha}=(\alpha_x,\alpha_y,\alpha_z)\): three-component matrix object used to form the rotational scalar \(\boldsymbol{\alpha}\cdot\mathbf p\).
- \(\sigma_x,\sigma_y,\sigma_z\): Pauli matrices supplying the \(2\times2\) massless three-dimensional solution.
- Chirality/helicity: the lecture uses this as the relation between spin direction and momentum direction; right-handed means aligned, left-handed means anti-aligned.
- Dirac sea: the historically motivated vacuum defined by filling all negative-energy fermion states.
- Hole/positron: excitation produced by removing a filled negative-energy electron.
- \(a(p)\): annihilation operator for a positive-energy electron mode.
- \(b^\dagger(p)\): creation operator for a positron mode after reinterpreting negative-energy electron annihilation.
- \(A(x)\): photon field/operator appearing schematically in the interaction term.

## Derivation Steps
Fermionic exchange to operator anti-commutation
1. Start from exchanged fermionic two-particle states differing by a minus sign.
2. Represent the two-particle state by two creation operators acting on the vacuum.
3. Swap the order of the creation operators to represent exchanged particles.
4. Demand the swapped state pick up a minus sign.
5. Move both terms to one side.
6. Read the result as a vanishing anti-commutator of creation operators.

Equal-point exclusion
1. Take the fermionic anti-commutator and set \(y=x\).
2. Both operator products become identical.
3. The anti-commutator becomes \(2(\psi^\dagger(x))^2\).
4. Set it equal to zero.
5. Conclude \((\psi^\dagger(x))^2=0\).
6. Interpret this as impossibility of placing two identical fermions in the same state.

Boson versus fermion ladder comparison
1. For bosons, use the infinite occupation ladder \(0,1,2,\dots\).
2. Note that creation and annihilation operators are not algebraically interchangeable because the ladder is not symmetric under turning it upside down.
3. For a single fermionic mode, use only \(0\) and \(1\).
4. Observe that creation kills the filled state and annihilation kills the empty state.
5. Conclude that the fermionic algebra is symmetric under exchanging filled and empty, even though the operators are still physically different.

One-dimensional massive Dirac construction
1. Begin with \(i\partial_t\psi=-i\partial_x\psi\), so \(H=P\) and \(E=p\).
2. Identify this as a massless right-mover.
3. Add a second species with \(H\psi_2=-P\psi_2\) to represent a left-mover.
4. Package \(\psi_1,\psi_2\) into a two-component object.
5. Introduce \(\alpha\) so its eigenvalues distinguish the two sectors.
6. Write the combined Hamiltonian as \(H=\alpha P\).
7. Add \(\beta m\).
8. Require \(\alpha^2=\beta^2=1\) and \(\{\alpha,\beta\}=0\).
9. Square \(H\) and use the anti-commutator to cancel the cross term.
10. Recover \(H^2=P^2+m^2\).

Three-dimensional massless construction
1. Demand a Hamiltonian linear in momentum but rotationally invariant.
2. Replace the one-dimensional \(\alpha\) by a vector of matrices \(\boldsymbol{\alpha}\).
3. Write \(H=\boldsymbol{\alpha}\cdot\mathbf p\).
4. Square \(H\).
5. Require each \(\alpha_i^2=1\) to reproduce the diagonal \(p_i^2\) terms.
6. Require \(\{\alpha_i,\alpha_j\}=0\) for \(i\neq j\) to kill the cross terms.
7. Recognize that the Pauli matrices satisfy exactly these relations.
8. Set \(\alpha_i=\sigma_i\).
9. Arrive at \(H=\boldsymbol{\sigma}\cdot\mathbf p\) with energies \(\pm |\mathbf p|\).

Failure of a \(2\times2\) mass term in three dimensions
1. Try to add \(\beta m\) to \(H=\boldsymbol{\sigma}\cdot\mathbf p\).
2. Square the Hamiltonian.
3. The cross term requires \(\{\beta,\sigma_i\}=0\) for all three \(i\).
4. Observe that no \(2\times2\) matrix satisfies this with all Pauli matrices.
5. Conclude that two components are insufficient for the massive three-dimensional theory.
6. Enlarge the matrix algebra to \(4\times4\).

Four-by-four Dirac-matrix construction
1. Keep three \(\alpha_i\) and one \(\beta\), now as \(4\times4\) matrices.
2. Require \(\alpha_i^2=1\), \(\beta^2=1\), \(\{\alpha_i,\alpha_j\}=0\) for \(i\neq j\), and \(\{\alpha_i,\beta\}=0\).
3. Use a block representation built from Pauli matrices and the identity.
4. Check that the block algebra inherits Pauli anti-commutation.
5. Obtain a Hamiltonian whose square is \(\mathbf P^2+m^2\).

Mass as chirality mixing
1. In the massless \(2\times2\) theory, positive-energy states have spin locked relative to momentum.
2. Interpret the two alignments as opposite handedness/chirality.
3. The \(4\times4\) enlargement introduces both chiral sectors.
4. The off-diagonal \(\beta m\) term connects upper and lower blocks.
5. Read the mass term as coupling left- and right-handed sectors.

Velocity operator and zitterbewegung
1. Use the Heisenberg equation for \(\dot L\).
2. Set \(L=x\).
3. Only \(P_x\) fails to commute with \(x\); the matrices commute with \(x\).
4. Pull \(\alpha_x\) outside the commutator.
5. Use the canonical commutator with \(P_x\).
6. Identify \(\dot x=\alpha_x\).
7. Then test \(\dot\alpha_x\) by commuting \(\alpha_x\) with \(H\).
8. Since \(H\) contains \(\alpha_y\) and \(\alpha_z\), the commutator is nonzero.
9. Conclude that the velocity operator is not conserved.
10. Interpret the resulting rapid oscillation as zitterbewegung.

Negative energy, Dirac sea, and positrons
1. Return to the simplest right-moving massless case \(H=P\).
2. Allow negative momentum, hence negative energy.
3. Note that a vacuum with no particles would be unstable if arbitrarily many negative-energy particles could be added.
4. Use fermionic exclusion to cap occupation at one per state.
5. Fill all negative-energy states and declare that filled configuration to be the vacuum.
6. Remove one negative-energy electron.
7. Interpret the missing negative charge as positive charge.
8. Interpret removal of negative energy as addition of positive energy.
9. Identify the hole as a positron.

Field-operator split and process content
1. Start from a momentum integral for the fermion field over all \(p\).
2. Split the integral into positive-momentum and negative-momentum pieces.
3. Reinterpret annihilation of a negative-energy electron as creation of a positron.
4. Rewrite the field as electron-annihilation plus positron-creation pieces.
5. Insert this split into the schematic interaction \(\psi^\dagger\psi A\).
6. Read off electron emission, electron-positron annihilation, and pair-creation contributions from one operator structure.

## Notation Choices
- Use \(H\) for the Hamiltonian operator throughout.
- Use \(P\) for the one-dimensional momentum operator in the review section, matching the lecture’s \(H=P\) and \(H=\alpha P+\beta m\).
- Use \(p\) for momentum eigenvalues and for component labels in dispersion relations.
- Use \(\mathbf p=(p_x,p_y,p_z)\) and \(\mathbf P=(P_x,P_y,P_z)\) for three-dimensional momentum vectors.
- Use boldface \(\boldsymbol{\alpha}\) and \(\boldsymbol{\sigma}\) for the three-component matrix objects in three dimensions.
- Keep \(\psi(x)\) as the lecture’s symbol, but distinguish in prose when it means a single-particle wavefunction versus a field operator.
- Use \(\psi_1,\psi_2\) for the two-component one-dimensional review; introduce four-component notation only after the \(2\times2\) mass obstruction.
- Use \(\{A,B\}\) for both field and matrix anti-commutators, with context stated explicitly.
- Normalize the transcript’s “Dirac C” and “Fermi C” to “Dirac sea” and “Fermi sea.”
- Normalize the transcript slip “massless term” to “mass term” in the chirality discussion.
- Use units \(\hbar=1\) when writing the Heisenberg equation and the canonical commutator.
- If the genuine spin operator is written explicitly, denote it by \(\Sigma_i\) to keep it separate from the velocity matrices \(\alpha_i\).

## Uncertain Mathematics
- The equal-point anti-commutator passage is verbally garbled; the clean algebra \(\{\psi^\dagger(x),\psi^\dagger(x)\}=0\Rightarrow(\psi^\dagger(x))^2=0\) should be taken from the board plus cautious reconstruction.
- The transcript corruption around \(00{:}31{:}43\)–\(00{:}32{:}02\) breaks the “spin emerges from Dirac’s linearization” discussion; that logic should be reconstructed from surrounding remarks rather than quoted literally.
- In the three-dimensional massless discussion, the spoken squared relation repeats \(p_y^2\); the intended final term is clearly \(p_z^2\).
- The clean \(4\times4\) anti-commutation family is mathematically right, but one transcript stretch repeats factors in a corrupted way; the final notes should present only the cleaned relations.
- The explicit block representation of \(\alpha_i\) and \(\beta\) is only partially legible from the transcript; it is usable, but as a cautious standard representation rather than a verbatim transcription.
- The true spin operator is only described by contrast with \(\alpha\); if \(\Sigma_i=\mathrm{diag}(\sigma_i,\sigma_i)\) is written, it should be marked as a standard reconstruction.
- Susskind is openly unsure of the sign convention in the Heisenberg equation; only the conclusion \(\dot x=\alpha_x\) is stable in the lecture.
- The field-operator plane-wave phases are verbally loose; the split into \(a(p)e^{-ipx}\) and \(b^\dagger(p)e^{+ipx}\) should be kept as a cautious reconstruction with normalization and time dependence suppressed.
- The interaction term \(\psi^\dagger\psi A\) is schematic and should not be promoted into a fully covariant QED formula at this stage.
- The quaternion detour is too muddled to support any formal theorem beyond a brief remark that Pauli matrices are related to quaternionic structure.