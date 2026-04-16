# Math Bank
## Core Equations
- \(|\psi(t)\rangle = U(t)\,|\psi(0)\rangle\) [transcript-backed]
- \(U^\dagger U = I\) [transcript-backed]
- \(U(\epsilon)=I-i\epsilon H,\qquad U^\dagger(\epsilon)=I+i\epsilon H^\dagger\) [transcript-backed]
- \(H^\dagger=H\) [transcript-backed]
- \(L|i\rangle=l_i|i\rangle,\qquad M|i\rangle=m_i|i\rangle\) [transcript-backed]
- \(ML|i\rangle = M\,l_i|i\rangle = l_i\,M|i\rangle = l_i m_i |i\rangle\) [visible]
- \(LM|i\rangle = L\,m_i|i\rangle = m_i\,L|i\rangle = m_i l_i |i\rangle = l_i m_i |i\rangle\) [transcript-backed]
- \([L,M]\equiv LM-ML\) [transcript-backed]
- \([L,M]=0\) as the simultaneous-measurability condition [transcript-backed]
- \(\dfrac{|\psi(\epsilon)\rangle-|\psi(0)\rangle}{\epsilon}=-\,i\,H|\psi(0)\rangle\) [visible]
- \(\dfrac{d}{dt}|\psi\rangle=-\,i\,H|\psi\rangle\) [transcript-backed]
- \(H|E_i\rangle = E_i |E_i\rangle\) [transcript-backed]
- \(|i\rangle = |E_i\rangle\) [visible]
- \(|\psi(t)\rangle=\sum_j \alpha_j(t)\,|j\rangle\) [transcript-backed]
- \(\dot{\alpha}_j(t)=-\,i\,E_j\,\alpha_j(t)\) [transcript-backed]
- \(\alpha_j(t)=\alpha_j(0)e^{-iE_j t}\) [transcript-backed]
- \(|\psi(t)\rangle=\sum_j \alpha_j(0)e^{-iE_j t}|j\rangle\) [standard reconstruction]
- \(\langle L\rangle=\langle\psi|L|\psi\rangle\) [transcript-backed]
- \(\dfrac{d}{dt}\langle L\rangle=-\,i\,\langle [L,H]\rangle\) [visible]
- \(\dot L=-\,i[L,H]\) as lecture shorthand for the expectation-value equation [transcript-backed]
- \([A,B]=-[B,A]\) [transcript-backed]
- \([AB,C]=A[B,C]+[A,C]B\) [transcript-backed]
- \(\{L,H\}\leftrightarrow -\,i[L,H]\) in units with \(\hbar=1\) [transcript-backed]
- \(\{L,H\}\leftrightarrow -\,\dfrac{i}{\hbar}[L,H]\) when \(\hbar\) is restored [standard reconstruction]
- \(\dfrac{d}{dt}\langle H\rangle=-\,i\,\langle[H,H]\rangle=0\) [transcript-backed]
- \(\sigma_x=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad \sigma_y=\begin{pmatrix}0&-i\\ i&0\end{pmatrix},\qquad \sigma_z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}\) [transcript-backed]
- \(H=\dfrac{\omega}{2}\sigma_z\) [visible]
- \([\sigma_z,\sigma_x]=2i\sigma_y,\qquad [\sigma_x,\sigma_y]=2i\sigma_z,\qquad [\sigma_y,\sigma_z]=2i\sigma_x\) [transcript-backed]
- \(\dfrac{d}{dt}\langle \sigma_x\rangle = -\,i\,\dfrac{\omega}{2}\langle[\sigma_x,\sigma_z]\rangle,\qquad \dfrac{d}{dt}\langle \sigma_y\rangle = -\,i\,\dfrac{\omega}{2}\langle[\sigma_y,\sigma_z]\rangle,\qquad \dfrac{d}{dt}\langle \sigma_z\rangle = -\,i\,\dfrac{\omega}{2}\langle[\sigma_z,\sigma_z]\rangle\) [transcript-backed]
- \(\dot{\langle \sigma_x\rangle}=-\omega\langle \sigma_y\rangle,\qquad \dot{\langle \sigma_y\rangle}=+\omega\langle \sigma_x\rangle,\qquad \dot{\langle \sigma_z\rangle}=0\) [transcript-backed]
- \(H=aI+b_x\sigma_x+b_y\sigma_y+b_z\sigma_z\) [transcript-backed]
- \(H=\dfrac{\omega}{2}\,\sigma\cdot n,\qquad \sigma\cdot n \equiv n_x\sigma_x+n_y\sigma_y+n_z\sigma_z\) [transcript-backed]
- \(\sigma\cdot n=\begin{pmatrix} n_z & n_x-i n_y \\ n_x+i n_y & -n_z \end{pmatrix}\) [transcript-backed]
- \(\operatorname{tr}(\sigma\cdot n)=0,\qquad \det(\sigma\cdot n)=-(n_x^2+n_y^2+n_z^2)\) [transcript-backed]
- For unit \(n\): \(\det(\sigma\cdot n)=-1\) and the eigenvalues satisfy \(\lambda_1+\lambda_2=0,\ \lambda_1\lambda_2=-1\) [transcript-backed]
- \(\text{eigenvalues}(\sigma\cdot n)=\pm 1\) [transcript-backed]
- \(E_\pm=\pm \dfrac{\omega}{2},\qquad \Delta E=\omega\) [transcript-backed]
- \(\langle L\rangle(t)=\sum_{k,j}\alpha_k^*(0)\alpha_j(0)e^{i(E_k-E_j)t}L_{kj}\) [standard reconstruction]
- \(L_{kj}\equiv \langle k|L|j\rangle\) [transcript-backed]
- \(\mathbf B = B\,\mathbf n\) or equivalently magnetic field magnitude times unit direction \(n\) [transcript-backed]

## Definitions And Objects
- Observable: a Hermitian linear operator.
- Measurable values of an observable: its eigenvalues.
- State left behind by a good measurement: an eigenvector of the measured observable.
- Simultaneous measurability: existence of a complete common eigenbasis for the relevant observables.
- `Basis` in this lecture: a complete orthogonal normalized basis, even though Susskind notes that mathematicians use a broader notion.
- \(U(t)\): time-evolution operator taking the state at \(t=0\) to the state at time \(t\).
- \(H\): Hermitian generator of time evolution; identified in the lecture with the quantum Hamiltonian and thus with energy.
- Time-dependent Schrödinger equation: evolution equation for the state vector.
- Time-independent Schrödinger equation: eigenvalue equation for energy eigenstates.
- \(L\): generic observable; not specifically angular momentum in this lecture.
- \(M\): second generic observable used in the commutativity theorem.
- \(l_i,m_i\): eigenvalues of \(L\) and \(M\) on the common eigenvector \(|i\rangle\).
- \(|E_i\rangle\): energy eigenstate with energy \(E_i\).
- \(\alpha_j(t)\): time-dependent expansion coefficients of a state in the energy basis.
- Expectation value / average: \(\langle\psi|L|\psi\rangle\); Susskind says “average” would be the better name, but keeps “expectation value.”
- \(L_{kj}\): matrix element of \(L\) in the chosen energy basis.
- \(\sigma_x,\sigma_y,\sigma_z\): Pauli matrices / spin components.
- \(\sigma\cdot n\): shorthand for the matrix built from the spin components projected along a unit vector \(n\).
- \(n\): unit vector specifying the direction of the magnetic field.
- \(\omega\): coefficient proportional to magnetic-field magnitude times magnetic moment, with lecture conventions absorbing constants.
- Free single spin: treated as having \(H=0\) up to an additive constant.
- Additive constant in \(H\): dynamically irrelevant in this lecture because the identity operator commutes with everything.

## Derivation Steps
Simultaneous measurability \(\Rightarrow [L,M]=0\)
1. Assume a complete orthonormal basis \(\{|i\rangle\}\) of simultaneous eigenvectors of \(L\) and \(M\).
2. Write \(L|i\rangle=l_i|i\rangle\) and \(M|i\rangle=m_i|i\rangle\).
3. Compute \(ML|i\rangle = l_i m_i |i\rangle\).
4. Compute \(LM|i\rangle = m_i l_i |i\rangle\).
5. Use that \(l_i m_i = m_i l_i\) because they are numbers.
6. Conclude \(ML\) and \(LM\) agree on every basis vector.
7. Extend by linearity to every superposition.
8. Therefore \(LM=ML\), i.e. \([L,M]=0\).

Unitarity \(\Rightarrow H^\dagger=H\)
1. Start from orthogonality preservation of states under time evolution.
2. Infer \(U^\dagger U=I\).
3. For small \(\epsilon\), write \(U(\epsilon)=I-i\epsilon H\).
4. Conjugate to get \(U^\dagger(\epsilon)=I+i\epsilon H^\dagger\).
5. Substitute into \(U^\dagger U=I\).
6. Keep only terms through first order in \(\epsilon\).
7. Obtain \(H-H^\dagger=0\).
8. Conclude \(H\) is Hermitian.

Infinitesimal evolution \(\Rightarrow\) time-dependent Schrödinger equation
1. Apply \(U(\epsilon)\) to \(|\psi(0)\rangle\).
2. Get \(|\psi(\epsilon)\rangle=|\psi(0)\rangle-i\epsilon H|\psi(0)\rangle\).
3. Move \(|\psi(0)\rangle\) to the left-hand side.
4. Divide by \(\epsilon\).
5. Recognize the left-hand side as a difference quotient.
6. Take the limit \(\epsilon\to 0\).
7. Arrive at \(\dfrac{d}{dt}|\psi\rangle=-iH|\psi\rangle\).

Energy-basis solution of Schrödinger evolution
1. Choose an energy eigenbasis \(H|j\rangle=E_j|j\rangle\).
2. Expand \(|\psi(t)\rangle=\sum_j \alpha_j(t)|j\rangle\).
3. Differentiate: \(\dot{\psi}=\sum_j \dot{\alpha}_j |j\rangle\).
4. Apply \(-iH\) to the expansion: \(-iH|\psi\rangle=\sum_j (-iE_j\alpha_j)|j\rangle\).
5. Set the two sums equal using Schrödinger’s equation.
6. Match coefficients of the same basis vectors.
7. Obtain \(\dot{\alpha}_j=-iE_j\alpha_j\).
8. Solve to get \(\alpha_j(t)=\alpha_j(0)e^{-iE_j t}\).
9. Substitute back into the expansion for the full state.

Expectation-value evolution
1. Start from \(\langle L\rangle=\langle\psi|L|\psi\rangle\).
2. Differentiate with respect to time.
3. Use Schrödinger’s equation on the ket.
4. Use the conjugate equation on the bra, which flips the sign of \(i\).
5. Collect the two terms.
6. Rewrite them as the commutator \(LH-HL\).
7. Conclude \(\dfrac{d}{dt}\langle L\rangle=-i\langle[L,H]\rangle\).

Commutator product rule
1. Begin with \([AB,C]=ABC-CAB\).
2. Add and subtract \(ACB\).
3. Group as \(A(BC-CB)+(AC-CA)B\).
4. Identify \(BC-CB=[B,C]\).
5. Identify \(AC-CA=[A,C]\).
6. Conclude \([AB,C]=A[B,C]+[A,C]B\).

Energy conservation from the Heisenberg equation
1. Set \(L=H\) in \(\dfrac{d}{dt}\langle L\rangle=-i\langle[L,H]\rangle\).
2. Get \(\dfrac{d}{dt}\langle H\rangle=-i\langle[H,H]\rangle\).
3. Use that anything commutes with itself.
4. Conclude \(\dfrac{d}{dt}\langle H\rangle=0\).

Spin in a \(z\)-directed magnetic field
1. Postulate \(H=\dfrac{\omega}{2}\sigma_z\).
2. Use \(\dfrac{d}{dt}\langle \sigma_a\rangle = -i\left\langle [\sigma_a,H]\right\rangle\).
3. Compute \([\sigma_z,\sigma_x]=2i\sigma_y\), hence \([\sigma_x,\sigma_z]=-2i\sigma_y\).
4. Compute \([\sigma_y,\sigma_z]=2i\sigma_x\).
5. Note \([\sigma_z,\sigma_z]=0\).
6. Substitute into the expectation-value equation.
7. Cancel the factor of \(2\) against the denominator in \(H=\omega\sigma_z/2\).
8. Use the extra factor of \(i\) from the commutator to remove the explicit \(i\) in the evolution law.
9. Obtain \(\dot{\langle \sigma_x\rangle}=-\omega\langle \sigma_y\rangle\), \(\dot{\langle \sigma_y\rangle}=+\omega\langle \sigma_x\rangle\), \(\dot{\langle \sigma_z\rangle}=0\).

Eigenvalues of \(\sigma\cdot n\)
1. Write \(\sigma\cdot n\) as the \(2\times2\) matrix with entries \(n_z\), \(n_x\pm i n_y\), and \(-n_z\).
2. Assume \(n\) is a unit vector: \(n_x^2+n_y^2+n_z^2=1\).
3. Compute the trace and get \(\lambda_1+\lambda_2=0\).
4. Compute the determinant and get \(\lambda_1\lambda_2=-1\).
5. Solve the two conditions simultaneously.
6. Conclude \(\lambda_{1,2}=\pm1\).
7. Therefore the Hamiltonian \(\dfrac{\omega}{2}\sigma\cdot n\) has energies \(\pm \omega/2\).

## Notation Choices
- Normalize the state symbol to \(\psi\), not a mix of \(\psi\) and \(\Psi\).
- Use \(I\) for the identity operator throughout.
- Use \([A,B]=AB-BA\) consistently.
- Use \(|E_i\rangle\) for energy eigenstates in polished notes.
- Allow \(|i\rangle\) only in local derivations where Susskind is using a generic basis, or when explicitly stating \(|i\rangle=|E_i\rangle\).
- Use \(l_i\) and \(m_i\) for eigenvalues of generic observables \(L\) and \(M\), matching the lecture.
- Use \(\langle L\rangle\) for expectation value, with prose occasionally reminding the reader that Susskind means statistical average.
- Keep explicit sum signs; do not use Einstein summation. The lecture explicitly says repeated indices are not automatically summed here.
- Use \(\alpha_j(t)\) for expansion coefficients, with \(\alpha_j(0)\) as the initial-data coefficients.
- Use \(\hbar=1\) in the main derivations, but restore \(\hbar\) in editorial remarks where energy-frequency relations are mentioned.
- When writing the spin evolution equations in final notes, prefer \(\langle \sigma_x\rangle,\langle \sigma_y\rangle,\langle \sigma_z\rangle\) explicitly, even though the lecture temporarily drops the brackets.
- Keep \(L\) as a generic observable, not angular momentum; if angular momentum is mentioned, name it separately.
- Write \(\sigma\cdot n = n_x\sigma_x+n_y\sigma_y+n_z\sigma_z\), but note in prose that this is matrix shorthand, not a literal classical vector dot product.
- Use `basis` in the Susskind sense only if the prose makes clear that he means a complete orthonormal basis.

## Uncertain Mathematics
- The middle lines of the \(ML|i\rangle\) board derivation are partly occluded in the frame; the cleaned displayed chain is secure, but the exact handwriting order of the intermediate equalities is not fully visible.
- The converse theorem, \([L,M]=0 \Rightarrow\) complete common eigenbasis, is stated but not proved in the lecture; keep it as a stated fact, not a rederived result.
- The coefficient derivation near \(00{:}58\)–\(01{:}02\) contains several spoken self-corrections and index repairs; present only the resolved equation \(\dot{\alpha}_j=-iE_j\alpha_j\), but do not pretend the lecture gave a perfectly smooth board derivation.
- The full displayed formula \(|\psi(t)\rangle=\sum_j \alpha_j(t)|j\rangle\) is mathematically secure from transcript plus context, but the selected frame does not cleanly expose the full left-hand side or the coefficient symbol.
- The double-sum formula for \(\langle L\rangle(t)\) is transcript-backed in substance, but the compact final notation with \(L_{kj}\) and grouped phase factor is a cleanup step.
- The lecture’s identification of Poisson brackets with \(-i\) times commutators is schematic at first and only later qualified by \(\hbar\); in final notes, separate the \(\hbar=1\) convention from the dimensionful statement.
- The physical sign of the magnetic interaction is not derived from dipole physics in detail; the lecture simply postulates the convenient form \(H=\omega\sigma_z/2\) with the constants absorbed into \(\omega\).
- The late transcript around the explicit \(\sigma\cdot n\) matrix has garbling in the spoken entries, but the intended standard matrix is clear from the Pauli matrices and the rest of the argument.
- The shorthand \(\dot L=-i[L,H]\) should be stated cautiously: in this lecture it is still an equation for expectation values unless and until a fuller Heisenberg-picture treatment is introduced.
- The statement that a free spin has \(H=0\) is lecture-level and meant up to an additive constant; it is not a general relativistic or field-theoretic claim.