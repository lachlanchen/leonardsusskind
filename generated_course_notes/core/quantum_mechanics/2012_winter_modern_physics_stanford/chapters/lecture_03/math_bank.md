# Math Bank
## Core Equations
- \(\hat K|A\rangle = |C\rangle\) [transcript-backed]
- \(\langle B|\hat K|A\rangle\) [transcript-backed]
- \(\langle m|\hat K|n\rangle\) [visible]
- \(|A\rangle = \sum_n A_n |n\rangle\) [transcript-backed]
- \(A_n = \langle n|A\rangle\) [transcript-backed]
- \(|A\rangle = \sum_n |n\rangle \langle n|A\rangle\) [transcript-backed]
- \(\sum_n |n\rangle\langle n| = \mathbb I\) [standard reconstruction]
- \(\langle n|\hat K|A\rangle = \sum_m \langle n|\hat K|m\rangle \langle m|A\rangle\) [visible]
- \(\sum_m K_{nm}A_m\) [visible]
- \(\langle n|\hat K|A\rangle = \sum_m K_{nm}A_m\) [standard reconstruction]
- \((KL)_{nm} = \sum_r K_{nr}L_{rm}\) [transcript-backed]
- \(\langle B|\hat H|A\rangle = \langle A|\hat H|B\rangle^*\) [standard reconstruction]
- \(\langle A|\hat H|A\rangle \in \mathbb R\) [transcript-backed]
- \(\hat H|\lambda\rangle = \lambda |\lambda\rangle\) [transcript-backed]
- \(\lambda \in \mathbb R\) for Hermitian \(\hat H\) [transcript-backed]
- \(\langle \lambda_1|\lambda_2\rangle = 0 \quad (\lambda_1 \neq \lambda_2)\) [transcript-backed]
- \(P(\lambda_n|A)=|\langle \lambda_n|A\rangle|^2\) [transcript-backed]
- \(\langle \phi|\psi\rangle=\int dx\,\phi^*(x)\psi(x)\) [transcript-backed]
- \((\hat x\psi)(x)=x\psi(x)\) [transcript-backed]
- \(x\,\psi(x)=\lambda \psi(x)\) [transcript-backed]
- \((x-\lambda)\psi(x)=0\) [transcript-backed]
- \(\langle x|\lambda\rangle = \delta(x-\lambda)\) [standard reconstruction]
- \(\langle x|\psi\rangle = \psi(x)\) [transcript-backed]
- \(\rho(x)=|\psi(x)|^2\) as the position probability density [standard reconstruction]
- \(\langle B|\hat A|A\rangle=-\langle A|\hat A|B\rangle^*\) [standard reconstruction]
- \(\hat K=-i\,\dfrac{d}{dx}\) [transcript-backed]
- \(\langle \psi|\hat K|\psi\rangle=\int dx\,\psi^*(x)\left(-i\,\dfrac{d\psi}{dx}\right)\) [transcript-backed]
- \(\int dx\,\psi^*(x)\left(-i\,\dfrac{d\psi}{dx}\right)= i\int dx\,\dfrac{d\psi^*}{dx}\,\psi\) [transcript-backed]
- \(-i\,\dfrac{d\psi}{dx}=k\psi\) [transcript-backed]
- \(\psi_k(x)\propto e^{ikx}=\cos(kx)+i\sin(kx)\) [transcript-backed]
- \(\psi_k^*(x)\psi_k(x)=\text{const.}\) [transcript-backed]
- \(kL=2\pi\) [transcript-backed]
- \(L=\dfrac{2\pi}{k}\) [transcript-backed]
- \(p=\dfrac{h}{L}=\hbar k\) [transcript-backed]
- \(\begin{pmatrix} H_{11} & H_{12} & \cdots \\ H_{21} & \cdots & \cdots \\ \vdots & & \ddots \end{pmatrix}\begin{pmatrix} A_1 \\ A_2 \\ \vdots \end{pmatrix}\) [standard reconstruction]

## Definitions And Objects
- State vector: ket \(|A\rangle\); states are vectors in a complex vector space.
- Observable: a measurable quantity; corresponds to a Hermitian operator.
- Linear operator: generic symbol \(\hat K\), \(\hat L\); acts on kets and returns kets.
- Matrix element: \(\langle B|\hat K|A\rangle\); number obtained by acting with \(\hat K\) on \(|A\rangle\) and then taking inner product with \(\langle B|\).
- Basis: orthonormal family \(\{|n\rangle\}\); mutually orthogonal, unit norm, complete.
- Components of a vector in basis \(\{|n\rangle\}\): \(A_n=\langle n|A\rangle\).
- Operator matrix entries in basis \(\{|n\rangle\}\): \(K_{nm}:=\langle n|\hat K|m\rangle\).
- Unit/completeness operator: \(\sum_n |n\rangle\langle n|\); “does nothing.”
- Hermitian operator: operator with bra-ket matrix elements related by interchange plus complex conjugation.
- Anti-Hermitian operator: same relation as Hermitian, but with an extra minus sign.
- Eigenvector/eigenfunction: nonzero vector left invariant in direction by operator action.
- Eigenvalue: scalar multiplying an eigenvector.
- Spectrum: collection of eigenvalues.
- Degeneracy: distinct eigenvectors sharing the same eigenvalue.
- Wavefunction: function \(\psi(x)\) representing a state in the position basis; later identified with \(\langle x|\psi\rangle\).
- Position operator: \(\hat x\), acting by multiplication by \(x\).
- \(k\)-operator: \(\hat K=-i\,d/dx\); Hermitian differential operator introduced before naming it physically.
- Dirac delta function: idealized spike centered at \(x=\lambda\), used heuristically for position eigenfunctions.
- Plane-wave eigenfunction: \(e^{ikx}\), delocalized eigenfunction of \(\hat K\).

## Derivation Steps
- Basis expansion and completeness
  1. Choose an orthonormal basis \(\{|n\rangle\}\).
  2. Expand an arbitrary vector as \(|A\rangle=\sum_n A_n|n\rangle\).
  3. Take inner product with \(\langle m|\) to get \(A_m=\langle m|A\rangle\).
  4. Substitute back to write \(|A\rangle=\sum_n |n\rangle\langle n|A\rangle\).
  5. Read \(\sum_n |n\rangle\langle n|\) as the unit operator.

- Operator action in components
  1. Start from the \(n\)-th component of \(\hat K|A\rangle\): \(\langle n|\hat K|A\rangle\).
  2. Insert the basis expansion of \(|A\rangle\).
  3. Use linearity to obtain \(\sum_m \langle n|\hat K|m\rangle\langle m|A\rangle\).
  4. Identify \(K_{nm}=\langle n|\hat K|m\rangle\) and \(A_m=\langle m|A\rangle\).
  5. Read the result as matrix acting on a column vector.

- Product of operators as matrix multiplication
  1. Begin with \(\langle n|\hat K\hat L|m\rangle\).
  2. Expand \(\hat L|m\rangle\) by inserting a complete basis \(\sum_r |r\rangle\langle r|\).
  3. Substitute into the matrix element.
  4. Use linearity to get \(\sum_r \langle n|\hat K|r\rangle\langle r|\hat L|m\rangle\).
  5. Identify the matrix product formula \((KL)_{nm}=\sum_r K_{nr}L_{rm}\).

- Position-operator eigenfunction
  1. Start from the eigenvalue equation \(x\psi(x)=\lambda\psi(x)\).
  2. Rewrite it as \((x-\lambda)\psi(x)=0\).
  3. For any \(x\neq \lambda\), the factor \(x-\lambda\) is nonzero.
  4. Therefore \(\psi(x)=0\) away from \(x=\lambda\).
  5. Replace the impossible ordinary function by a narrow spike near \(x=\lambda\).
  6. Take the spike limit as the Dirac delta function.

- Orthogonality of distinct position eigenfunctions
  1. Take two narrow spikes centered at \(\lambda\) and \(\lambda'\) with \(\lambda\neq\lambda'\).
  2. Their supports do not overlap.
  3. Their product is zero everywhere.
  4. Therefore their inner product vanishes.
  5. Normalization is not fixed here; only orthogonality is kept.

- Extracting \(\psi(x)\) as a basis component
  1. Take the inner product of the state with a position eigenstate centered at \(\lambda\).
  2. Write the result as an integral against \(\delta(x-\lambda)\).
  3. Over the narrow support of the delta spike, replace \(\psi(x)\) by \(\psi(\lambda)\).
  4. Pull \(\psi(\lambda)\) outside the integral.
  5. Use \(\int dx\,\delta(x-\lambda)=1\).
  6. Conclude \(\langle \lambda|\psi\rangle=\psi(\lambda)\), then relabel \(\lambda\) as \(x\).

- Position Born rule
  1. Use the fifth postulate: probability is the squared projection onto the relevant eigenvector.
  2. In the position basis, the projection is \(\langle x|\psi\rangle=\psi(x)\).
  3. Therefore the position probability density is \(|\psi(x)|^2\).

- Hermiticity of \(-i\,d/dx\)
  1. Define \(\hat K=-i\,d/dx\).
  2. Compute \(\langle \psi|\hat K|\psi\rangle=\int dx\,\psi^*(-i\,d\psi/dx)\).
  3. Integrate by parts.
  4. Drop the boundary term using the assumption that \(\psi(x)\to 0\) sufficiently fast at infinity.
  5. Obtain \(i\int dx\,(d\psi^*/dx)\psi\).
  6. Recognize this as the complex conjugate of the original expression.
  7. Conclude the expression is real.
  8. Therefore \(\hat K\) is Hermitian.

- Plane-wave eigenfunction of \(\hat K\)
  1. Start from \(-i\,d\psi/dx=k\psi\).
  2. Solve to get \(\psi_k(x)\propto e^{ikx}\).
  3. Differentiate: \(d\psi_k/dx=ik\psi_k\).
  4. Multiply by \(-i\) to recover \(k\psi_k\).
  5. Conclude \(e^{ikx}\) is an eigenfunction with eigenvalue \(k\).

- Wavelength relation and de Broglie naming
  1. For \(e^{ikx}\), one full period occurs when \(kx\) changes by \(2\pi\).
  2. Therefore \(kL=2\pi\).
  3. Solve for wavelength: \(L=2\pi/k\).
  4. Invoke de Broglie’s relation \(p=h/L\).
  5. Substitute \(L=2\pi/k\).
  6. Obtain \(p=(h/2\pi)k=\hbar k\).
  7. Keep this as a naming/interpretive step, not yet a full physical derivation.

## Notation Choices
- Keep hats on operators throughout: \(\hat K,\hat L,\hat H,\hat x\).
- Use \(\hat K\) as the generic operator in the early linear-algebra discussion.
- Use \(\hat H\) as the generic Hermitian operator once the lecture turns to observables; note that here \(H\) means Hermitian, not yet Hamiltonian.
- Use discrete basis labels \(|n\rangle, |m\rangle, |r\rangle\) for finite-dimensional algebra.
- Define matrix entries by \(K_{nm}:=\langle n|\hat K|m\rangle\), consistent with the transcript’s component formula and the visible board work.
- Write vector components as \(A_n=\langle n|A\rangle\); think of \((A_1,A_2,\dots)^T\) as the concrete column-vector representation.
- Preserve the local switch to \(H_{ij}\) in the concrete Hermitian-matrix example tied to the later frame.
- Use \(|\lambda\rangle\) for a generic eigenvector of a Hermitian operator; use \(\lambda\) for the corresponding eigenvalue.
- For the position example, allow the lecture’s shift from generic \(\lambda\) to \(x\): standardize the basis ket as \(|x\rangle\), but keep the transcript logic that first treats \(\lambda\) as the eigenvalue.
- Use \(\psi(x)\) for the position-space wavefunction and \(\phi(x)\) for a second test function in inner products.
- Use \(\hat x\) as multiplication by \(x\), and \(\hat K=-i\,d/dx\) as the Hermitian differential operator.
- Use little \(k\) as the eigenvalue of \(\hat K\); do not silently replace it by \(p/\hbar\) in the main derivations.
- Keep the plane-wave normalization unspecified: write \(\psi_k(x)\propto e^{ikx}\), not an artificially normalized form.
- In the discrete postulates, write probabilities as \(P(\lambda_n|A)=|\langle \lambda_n|A\rangle|^2\); in the continuous position case, convert to a probability density \(\rho(x)=|\psi(x)|^2\).

## Uncertain Mathematics
- The first on-board statement of the Hermitian definition is badly garbled in the transcript; the final notes should use the standard bra-ket reconstruction, but mark internally that it is a reconstruction.
- The anti-Hermitian definition is also garbled, especially the missing star; use \(\langle B|\hat A|A\rangle=-\langle A|\hat A|B\rangle^*\) cautiously as a corrected standard form.
- The completeness relation is conceptually present in the transcript, but the explicit symbol \(\mathbb I\) is a clean modern reconstruction rather than a literal chalk transcription.
- The lecture treats the position eigenfunction as a narrow spike before invoking the Dirac delta; this should remain heuristic and not be upgraded silently into a full distribution-theoretic treatment.
- The position eigenfunctions are orthogonal in the lecture’s sense, but normalization is explicitly deferred; do not present them as ordinary normalized Hilbert-space vectors without comment.
- The proof that \(\hat K=-i\,d/dx\) is Hermitian assumes wavefunctions vanish sufficiently fast at infinity, but the later plane-wave eigenfunctions do not; the final chapter should state this tension openly.
- The sign choice for the Hermitian differential operator wobbles briefly between \(i\,d/dx\) and \(-i\,d/dx\); normalize to \(\hat K=-i\,d/dx\) in the final notes.
- The transcript’s “probability to detect a particle at position \(x\)” should be rendered as a probability density in mathematically serious notes.
- The matrix in the later frame is only partially visible; only the upper-left corner is direct evidence, and the full finite-dimensional layout should be treated as standard completion.
- The de Broglie step \(p=\hbar k\) is used to name the observable, not to prove from first principles that \(\hat K\) already has the full classical meaning of momentum.