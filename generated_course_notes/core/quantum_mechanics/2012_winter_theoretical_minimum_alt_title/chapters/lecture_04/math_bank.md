# Math Bank
## Core Equations
- \(L|\lambda\rangle=\lambda|\lambda\rangle\) [transcript-backed]
- \(\langle \lambda_i|\lambda_j\rangle=\delta_{ij}\) for an orthonormal eigenbasis of a Hermitian \(L\) [transcript-backed]
- \(P(\lambda)=|\langle \lambda|A\rangle|^2\) [transcript-backed]
- \(P(\lambda)=\sum_a |\langle \lambda,a|A\rangle|^2\) for a degenerate eigenvalue \(\lambda\) [standard reconstruction]
- \(|A\rangle=\sum_i \alpha_i |\lambda_i\rangle\) [transcript-backed]
- \(P(\lambda_i)=|\alpha_i|^2=\alpha_i^*\alpha_i\) [transcript-backed]
- \(\sum_i |\alpha_i|^2=1\) for a normalized state [transcript-backed]
- \(\bar{\lambda}=\sum_i \lambda_i\,P(\lambda_i)=\sum_i \lambda_i |\alpha_i|^2\) [transcript-backed]
- \(\langle L\rangle=\langle A|L|A\rangle\) [transcript-backed]
- \(|\Psi(t)\rangle=U(t)|\Psi(0)\rangle\) [visible]
- \(|\Phi(t)\rangle=U(t)|\Phi(0)\rangle\) [visible]
- \(\langle \Psi(0)|\Phi(0)\rangle=0 \;\Rightarrow\; \langle \Psi(t)|\Phi(t)\rangle=0\) [standard reconstruction]
- \(\langle \Psi(t)|\Phi(t)\rangle=\langle \Psi(0)|\Phi(0)\rangle\) [transcript-backed]
- \(\langle \Psi(t)|=\langle \Psi(0)|\,U^\dagger(t)\) [standard reconstruction]
- \(\langle \Psi(0)|U^\dagger(t)U(t)|\Phi(0)\rangle=\langle \Psi(0)|\Phi(0)\rangle\) [transcript-backed]
- \(U^\dagger(t)U(t)=I\) [visible]
- \(U^\dagger(t)=U^{-1}(t)\) [transcript-backed]
- \(U(0)=I\) [transcript-backed]
- \(U(\epsilon)=I-i\epsilon H\) [visible]
- \(U^\dagger(\epsilon)=I+i\epsilon H^\dagger\) [standard reconstruction]
- \(U^\dagger(\epsilon)U(\epsilon)=I\) [transcript-backed]
- \(I+i\epsilon(H^\dagger-H)=I\) to first order in \(\epsilon\) [transcript-backed]
- \(H^\dagger=H\) [transcript-backed]
- \(|\Psi(\epsilon)\rangle=(I-iH\epsilon)|\Psi(0)\rangle\) [visible]
- \(\frac{1}{\epsilon}\bigl(|\Psi(\epsilon)\rangle-|\Psi(0)\rangle\bigr)=-iH|\Psi(0)\rangle\) [visible]
- \(\frac{d}{dt}|\Psi\rangle=-iH|\Psi\rangle\) [visible]
- \(i\hbar\,\frac{d}{dt}|\Psi\rangle=H|\Psi\rangle\) [transcript-backed]
- \(\frac{d}{dt}\langle \Psi|=i\langle \Psi|H\) in \(\hbar=1\) units [transcript-backed]
- \(\langle L\rangle_t=\langle \psi(t)|L|\psi(t)\rangle\) [transcript-backed]
- \(\frac{d}{dt}\langle L\rangle=i\langle HL-LH\rangle=i\langle [H,L]\rangle\) in \(\hbar=1\) units [transcript-backed]
- \(\frac{d}{dt}\langle L\rangle=\frac{i}{\hbar}\langle [H,L]\rangle=-\frac{i}{\hbar}\langle [L,H]\rangle\) [transcript-backed]
- \([H,L]=HL-LH\) [transcript-backed]
- \([L,H]=-[H,L]\) [transcript-backed]
- \([LM,H]=L[M,H]+[L,H]M\) [transcript-backed]
- \(\dot L=\{L,H\}_{\mathrm{PB}}\) in classical mechanics [transcript-backed]
- \(\{L,H\}_{\mathrm{PB}}=-\{H,L\}_{\mathrm{PB}}\) [transcript-backed]
- \(\{LM,H\}_{\mathrm{PB}}=\{L,H\}_{\mathrm{PB}}\,M+L\,\{M,H\}_{\mathrm{PB}}\) [transcript-backed]
- \([A,B]=i\hbar\,\{A,B\}_{\mathrm{PB}}\) as the late-lecture correspondence rule [transcript-backed]
- \(\frac{d}{dt}\langle H\rangle=\frac{i}{\hbar}\langle [H,H]\rangle=0\) [transcript-backed]

## Definitions And Objects
- \(L\): generic observable operator; in this lecture it is taken to be Hermitian when discussing measurement.
- \(\lambda\): eigenvalue of \(L\); interpreted as a possible measurement outcome.
- \(|\lambda\rangle\): eigenvector associated with eigenvalue \(\lambda\); Susskind labels eigenvectors by their eigenvalues.
- Physically distinguishable states: states for which some experiment can unambiguously tell which preparation was given.
- Orthogonality: the vector-space representation of physical distinguishability.
- Overlap / inner product: \(\langle \psi|\phi\rangle\); treated as a measure of similarity between states.
- Probability amplitude: the inner product \(\langle \lambda|A\rangle\); probability is its absolute square.
- \(U(t)\): time-development operator; linear and the same operator for every initial state of the system.
- Unitary operator: an operator satisfying \(U^\dagger U=I\).
- \(H\): infinitesimal generator of time evolution; derived to be Hermitian and identified with the Hamiltonian.
- Hamiltonian: the observable that generates state-vector evolution; identified in the lecture with energy.
- Expectation value: really the average value of an observable in a given state, despite the standard name.
- Unit operator \(I\): the operator that returns the same vector unchanged.
- Commutator: \([A,B]=AB-BA\).
- Time translation invariance: the case where \(H\) has no explicit time dependence.
- Isolated-system caveat: the derived Schrödinger evolution is for a system not interacting with a measuring apparatus.

## Derivation Steps
**Observables and Hermitian structure**
1. Start from two lecture claims: measurement outcomes are real numbers, and states with different measurement outcomes are physically distinguishable.
2. Represent physically distinguishable states by orthogonal vectors.
3. Use the linear-algebra theorem Susskind invokes: operators with real eigenvalues and orthogonal eigenvectors are Hermitian.
4. Conclude that observables are represented by Hermitian operators.

**Born rule and degeneracy**
1. Expand the prepared state in the eigenbasis of \(L\): \(|A\rangle=\sum_i \alpha_i|\lambda_i\rangle\).
2. Read \(\alpha_i=\langle \lambda_i|A\rangle\) as the amplitude for the \(i\)-th eigenchannel.
3. Take the probability for outcome \(\lambda_i\) to be \(|\alpha_i|^2\).
4. If several orthogonal eigenvectors share the same eigenvalue \(\lambda\), square each overlap and add the resulting probabilities.
5. If the degenerate eigenvectors are not yet orthogonal, first choose an orthogonal basis inside the degenerate eigenspace.

**Unitarity from conserved overlap**
1. Postulate \(|\psi(t)\rangle=U(t)|\psi(0)\rangle\) with the same linear \(U(t)\) for all states.
2. Require orthogonal initial states to remain orthogonal.
3. Upgrade that to the stronger statement that arbitrary overlaps are time independent.
4. Write the bra equation as \(\langle \psi(t)|=\langle \psi(0)|U^\dagger(t)\).
5. Substitute both bra and ket evolutions into \(\langle \psi(t)|\phi(t)\rangle\).
6. Get \(\langle \psi(0)|U^\dagger(t)U(t)|\phi(0)\rangle=\langle \psi(0)|\phi(0)\rangle\) for all \(\psi,\phi\).
7. Conclude \(U^\dagger(t)U(t)=I\), so \(U\) is unitary.

**Hermitian \(H\) and the Schrödinger equation**
1. For small \(\epsilon\), write \(U(\epsilon)=I-i\epsilon H\) and drop higher powers of \(\epsilon\).
2. Hermitian-conjugate this to \(U^\dagger(\epsilon)=I+i\epsilon H^\dagger\).
3. Impose unitarity: \(U^\dagger(\epsilon)U(\epsilon)=I\).
4. Expand to first order to get \(I+i\epsilon(H^\dagger-H)=I\).
5. Cancel the identity terms and ignore \(O(\epsilon^2)\).
6. Conclude \(H^\dagger=H\).
7. Apply the infinitesimal update to a state: \(|\psi(\epsilon)\rangle=(I-iH\epsilon)|\psi(0)\rangle\).
8. Rearrange to \(|\psi(\epsilon)\rangle-|\psi(0)\rangle=-i\epsilon H|\psi(0)\rangle\).
9. Divide by \(\epsilon\) and interpret the quotient as a time derivative at an arbitrary time.
10. Obtain \(\frac{d}{dt}|\psi\rangle=-iH|\psi\rangle\), then restore units as \(i\hbar\,\partial_t|\psi\rangle=H|\psi\rangle\).

**Expectation value as a sandwich**
1. Define the average of measured values by \(\bar\lambda=\sum_i \lambda_i P(\lambda_i)\).
2. Expand \(|A\rangle=\sum_i \alpha_i|\lambda_i\rangle\) in the eigenbasis of \(L\).
3. Substitute \(P(\lambda_i)=|\alpha_i|^2\) into the average.
4. Compute \(\langle A|L|A\rangle\) by inserting the bra and ket expansions.
5. Use \(L|\lambda_i\rangle=\lambda_i|\lambda_i\rangle\) and \(\langle \lambda_j|\lambda_i\rangle=\delta_{ji}\).
6. Collapse the double sum to \(\sum_i \lambda_i |\alpha_i|^2\).
7. Conclude \(\langle L\rangle=\langle A|L|A\rangle\).

**Time evolution of averages and weak energy conservation**
1. Start from \(\langle L\rangle_t=\langle \psi(t)|L|\psi(t)\rangle\).
2. Differentiate with the product rule; only the state vectors carry time dependence.
3. Insert \(\partial_t|\psi\rangle=-iH|\psi\rangle\).
4. Insert \(\partial_t\langle \psi|=i\langle \psi|H\).
5. Collect the two terms to get \(i\langle HL-LH\rangle=i\langle[H,L]\rangle\).
6. Restore \(\hbar\) to obtain \(\frac{d}{dt}\langle L\rangle=\frac{i}{\hbar}\langle[H,L]\rangle\).
7. Set \(L=H\).
8. Use \([H,H]=0\).
9. Conclude \(\frac{d}{dt}\langle H\rangle=0\): the lecture’s weak energy-conservation statement.

## Notation Choices
- Use \(L\) for a generic observable/Hermitian operator, even though Susskind notes that \(L\) is also standard for angular momentum elsewhere.
- Use \(|\psi(t)\rangle\) as the default time-dependent state symbol in the dynamics sections.
- Use \(|A\rangle\) only where the lecture is explicitly phrased in terms of a state prepared in \(A\) for Born’s rule and expectation values.
- Standardize the second evolving state to \(|\Phi(t)\rangle\), not lowercase \(\phi\).
- Keep the lecture’s eigenvector-by-eigenvalue notation \(|\lambda\rangle\), while recognizing that it is notation abuse.
- Use \(I\) for the unit operator in the bank, since that matches the board/transcript; a later stylistic normalization to \(\mathbf{1}\) or \(\mathbb{I}\) is optional.
- Treat all state vectors and eigenvectors as normalized once Born’s rule is in play.
- Use \(\epsilon\) for an infinitesimal time step.
- Use \(H\) for the infinitesimal generator and Hamiltonian.
- Use bras as Hermitian conjugates of kets; in particular \(\langle \psi(t)|=(|\psi(t)\rangle)^\dagger\).
- Use \(\langle L\rangle\) as the primary notation for the average; \(\bar L(t)\) can appear only when mirroring the lecture’s temporary notation discussion.
- Fix the commutator convention as \([A,B]=AB-BA\), so \([H,L]=HL-LH\).
- Present the main derivations first in \(\hbar=1\) units, then explicitly restore \(\hbar\).

## Uncertain Mathematics
- The lower-right symbol in the orthogonality-preservation board frame is visually ambiguous between \(\Phi\) and \(\phi\); standardize to \(\Phi\).
- The bra-evolution line around 00:34:49–00:35:08 is garbled in the transcript; use the standard reconstruction \(\langle \psi(t)|=\langle \psi(0)|U^\dagger(t)\).
- The theorem “preserved orthogonality implies preserved overlap for arbitrary pairs of states” is only sketched verbally; the final notes should present it as a short linear-algebra argument, not as a fully board-derived proof.
- The conjugate infinitesimal expansion \(U^\dagger(\epsilon)=I+i\epsilon H^\dagger\) is partly occluded in the frame and should be treated as standard completion.
- The derivative line in the close-up frame is incomplete; the full Schrödinger equation should be anchored in the transcript and the boxed later frame.
- The late lecture toggles between \(\hbar=1\) and restored units; signs and \(\hbar\)-placement should be checked against the consistent final forms
  \(\;i\hbar\,\partial_t|\psi\rangle=H|\psi\rangle\),
  \(\;\frac{d}{dt}\langle L\rangle=\frac{i}{\hbar}\langle[H,L]\rangle\),
  \(\;[A,B]=i\hbar\{A,B\}_{\mathrm{PB}}\).
- The shorthand \(\dot L=i[H,L]\) is presented in the lecture as a loose, average-level or semiclassical shorthand; it should not be promoted uncritically to a literal Schrödinger-picture operator equation.
- The energy-conservation check is only for the average energy and only in the time-independent-\(H\) setting; the lecture explicitly says that explicit time dependence spoils conservation.
- Any degenerate-eigenspace notation with an extra label \(a\) is a cleanup for the notes, not lecture notation.