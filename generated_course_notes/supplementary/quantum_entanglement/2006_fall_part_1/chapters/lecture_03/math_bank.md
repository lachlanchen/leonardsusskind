# Math Bank
## Core Equations
- \(z=x+iy\). [transcript-backed]
- \(x=r\cos\theta,\quad y=r\sin\theta\). [transcript-backed]
- \(z=r(\cos\theta+i\sin\theta)=re^{i\theta}\). [transcript-backed]
- \(e^{i\theta}=\cos\theta+i\sin\theta\). [transcript-backed]
- \(e^{i\theta}e^{i\phi}=e^{i(\theta+\phi)}\). [transcript-backed]
- \((e^{i\theta})^*=e^{-i\theta}\). [transcript-backed]
- \(e^{i\theta}e^{-i\theta}=1\). [transcript-backed]
- \(zz^*=x^2+y^2\). [transcript-backed]
- \(|\psi\rangle=\alpha|u\rangle+\beta|d\rangle\). [transcript-backed]
- \(\langle \psi|\psi\rangle=\alpha^*\alpha+\beta^*\beta=|\alpha|^2+|\beta|^2=1\). [transcript-backed]
- \(|u\rangle=\begin{pmatrix}1\\0\end{pmatrix},\quad |d\rangle=\begin{pmatrix}0\\1\end{pmatrix}\). [transcript-backed]
- \((M^T)_{ij}=M_{ji}\). [visible]
- \(M_{ij}=M_{ji}\) for a symmetric matrix. [transcript-backed]
- \(M^\dagger=(M^T)^*\). [transcript-backed]
- \(M_{ij}=(M_{ji})^*\) for a Hermitian matrix. [standard reconstruction]
- \(\langle B|A\rangle=\langle A|B\rangle^*\). [transcript-backed]
- \(\langle B|M|A\rangle=\big(\langle A|M^\dagger|B\rangle\big)^*\). [transcript-backed]
- For Hermitian \(M\): \(\langle B|M|A\rangle=\big(\langle A|M|B\rangle\big)^*\). [transcript-backed]
- For Hermitian \(M\): \(\langle A|M|A\rangle\in\mathbb R\). [transcript-backed]
- \(M|a\rangle=\lambda_a|a\rangle\). [visible]
- For Hermitian \(M\): \(\lambda_a=\dfrac{\langle a|M|a\rangle}{\langle a|a\rangle}\in\mathbb R\). [transcript-backed]
- \(\begin{pmatrix}m_{11}&0\\0&m_{22}\end{pmatrix}\begin{pmatrix}1\\0\end{pmatrix}=m_{11}\begin{pmatrix}1\\0\end{pmatrix}\). [standard reconstruction]
- \(\begin{pmatrix}m_{11}&0\\0&m_{22}\end{pmatrix}\begin{pmatrix}0\\1\end{pmatrix}=m_{22}\begin{pmatrix}0\\1\end{pmatrix}\). [visible]
- \(\sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix}\). [transcript-backed]
- \(\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix}\). [transcript-backed]
- \(\sigma_2=\begin{pmatrix}0&-i\\ i&0\end{pmatrix}\). [transcript-backed]
- \(\sigma_3\begin{pmatrix}1\\0\end{pmatrix}=+\begin{pmatrix}1\\0\end{pmatrix},\quad \sigma_3\begin{pmatrix}0\\1\end{pmatrix}=-\begin{pmatrix}0\\1\end{pmatrix}\). [transcript-backed]
- \(\sigma_1\frac{1}{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix}=+\frac{1}{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix}\). [standard reconstruction]
- \(\sigma_1\frac{1}{\sqrt2}\begin{pmatrix}1\\-1\end{pmatrix}=-\frac{1}{\sqrt2}\begin{pmatrix}1\\-1\end{pmatrix}\). [transcript-backed]
- \(\begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}1/\sqrt2\\1/\sqrt2\end{pmatrix}=\begin{pmatrix}1/\sqrt2\\1/\sqrt2\end{pmatrix}\). [standard reconstruction]
- \(\frac{1}{\sqrt2}\begin{pmatrix}1\\ i\end{pmatrix},\quad \frac{1}{\sqrt2}\begin{pmatrix}1\\ -i\end{pmatrix}\) are eigenvectors of \(\sigma_2\) with eigenvalues \(+1\) and \(-1\). [transcript-backed]
- \(\sigma_1^2=\sigma_2^2=\sigma_3^2=1\). [transcript-backed]
- \(\sigma_1\sigma_2+\sigma_2\sigma_1=0,\quad \sigma_2\sigma_3+\sigma_3\sigma_2=0,\quad \sigma_1\sigma_3+\sigma_3\sigma_1=0\). [transcript-backed]
- If \(M|A\rangle=\lambda_A|A\rangle\) and \(M|B\rangle=\lambda_B|B\rangle\), then \((\lambda_A-\lambda_B)\langle B|A\rangle=0\). [transcript-backed]
- Hence if \(\lambda_A\neq\lambda_B\), then \(\langle B|A\rangle=0\). [transcript-backed]
- \(P(\lambda_A|B)=|\langle A|B\rangle|^2=\langle A|B\rangle\langle B|A\rangle\). [transcript-backed]
- \(P(\sigma_1=+1\,|\,\sigma_3=+1)=\left|\left\langle \tfrac{1}{\sqrt2}\binom{1}{1}\middle|\binom{1}{0}\right\rangle\right|^2=\tfrac12\). [transcript-backed]
- \(P(\sigma_1=-1\,|\,\sigma_3=+1)=\tfrac12\). [transcript-backed]
- \(P(\sigma_2=+1\,|\,\sigma_1=+1)=\left|\left\langle \tfrac{1}{\sqrt2}\binom{1}{i}\middle|\tfrac{1}{\sqrt2}\binom{1}{1}\right\rangle\right|^2=\left|\tfrac12-\tfrac{i}{2}\right|^2=\tfrac12\). [transcript-backed]
- \(\sigma\cdot \hat n=n_1\sigma_1+n_2\sigma_2+n_3\sigma_3\). [transcript-backed]
- \(\sigma\cdot \hat n=\begin{pmatrix}n_3&n_1-in_2\\ n_1+in_2&-n_3\end{pmatrix}\). [standard reconstruction]
- \(n_1^2+n_2^2+n_3^2=1\). [transcript-backed]
- \((\sigma\cdot \hat n)^2=1\). [transcript-backed]
- Therefore the eigenvalues of \(\sigma\cdot \hat n\) are \(\pm1\). [transcript-backed]

## Definitions And Objects
- Pure phase: a unit-modulus complex number of the form \(e^{i\theta}\).
- Modulus-radius decomposition: any complex number is a positive real modulus times a pure phase.
- State vector: a vector in a complex vector space representing the prepared state of the system.
- Normalized state: a state satisfying \(\langle \psi|\psi\rangle=1\).
- Orthonormal basis: basis vectors that are mutually orthogonal and individually normalized.
- Observable: a measurable quantity; in this lecture it is represented by a Hermitian matrix/operator.
- Transpose: interchange rows and columns.
- Hermitian conjugate: transpose followed by complex conjugation.
- Symmetric matrix: a matrix equal to its transpose.
- Hermitian matrix: a matrix equal to its Hermitian conjugate; diagonal entries real, reflected off-diagonal entries complex conjugates.
- Matrix element: \(\langle B|M|A\rangle\).
- Expectation value: \(\langle A|M|A\rangle\).
- Eigenvector/eigenvalue pair: a nonzero vector \(|a\rangle\) and scalar \(\lambda_a\) satisfying \(M|a\rangle=\lambda_a|a\rangle\).
- \(\sigma_3,\sigma_1,\sigma_2\): the three Pauli matrices, interpreted here as spin observables along the 3-, 1-, and 2-axes.
- \(\hat n\): unit spatial direction with components \(n_1,n_2,n_3\).
- \(\sigma\cdot \hat n\): operator representing spin component along the direction \(\hat n\).
- Pointer: Susskind’s preferred word for an ordinary-space direction or classical spin/magnetic-moment direction.
- Orthogonal states: states with zero inner product; physically distinguishable in the lecture’s usage.

## Derivation Steps
Reality of expectation values
1. Start from \(\langle B|M|A\rangle=\big(\langle A|M^\dagger|B\rangle\big)^*\).
2. Specialize to Hermitian \(M\), so \(M^\dagger=M\).
3. Set \(B=A\).
4. Obtain \(\langle A|M|A\rangle=\big(\langle A|M|A\rangle\big)^*\).
5. Conclude \(\langle A|M|A\rangle\) is real.

Reality of Hermitian eigenvalues
1. Assume \(M|a\rangle=\lambda_a|a\rangle\) with \(M\) Hermitian.
2. Multiply on the left by \(\langle a|\).
3. Get \(\langle a|M|a\rangle=\lambda_a\langle a|a\rangle\).
4. Use that \(\langle a|M|a\rangle\) is real and \(\langle a|a\rangle>0\) is real.
5. Divide by \(\langle a|a\rangle\).
6. Conclude \(\lambda_a\in\mathbb R\).

Orthogonality of eigenvectors with distinct eigenvalues
1. Assume \(M|A\rangle=\lambda_A|A\rangle\) and \(M|B\rangle=\lambda_B|B\rangle\), with \(M\) Hermitian.
2. Multiply the first equation on the left by \(\langle B|\): \(\langle B|M|A\rangle=\lambda_A\langle B|A\rangle\).
3. Multiply the second equation on the left by \(\langle A|\): \(\langle A|M|B\rangle=\lambda_B\langle A|B\rangle\).
4. Complex-conjugate the second equation and use Hermiticity plus \(\langle A|B\rangle^*=\langle B|A\rangle\).
5. Get \(\langle B|M|A\rangle=\lambda_B\langle B|A\rangle\).
6. Compare with step 2.
7. Subtract to obtain \((\lambda_A-\lambda_B)\langle B|A\rangle=0\).
8. If \(\lambda_A\neq\lambda_B\), conclude \(\langle B|A\rangle=0\).

Diagonal-matrix eigenvector pattern
1. Take \(M=\begin{pmatrix}m_{11}&0\\0&m_{22}\end{pmatrix}\).
2. Act on \(\begin{pmatrix}1\\0\end{pmatrix}\) and obtain \(m_{11}\begin{pmatrix}1\\0\end{pmatrix}\).
3. Act on \(\begin{pmatrix}0\\1\end{pmatrix}\) and obtain \(m_{22}\begin{pmatrix}0\\1\end{pmatrix}\).
4. Read off eigenvectors as basis columns and eigenvalues as diagonal entries.
5. Generalize cautiously: for diagonal \(n\times n\) matrices, standard basis vectors are eigenvectors and diagonal entries are eigenvalues.

\(\sigma_1\) eigenvectors
1. Take \(\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix}\).
2. Test \(\frac{1}{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix}\).
3. Compute \(\sigma_1\frac{1}{\sqrt2}\binom{1}{1}=\frac{1}{\sqrt2}\binom{1}{1}\).
4. Read eigenvalue \(+1\).
5. Test \(\frac{1}{\sqrt2}\begin{pmatrix}1\\-1\end{pmatrix}\).
6. Compute \(\sigma_1\frac{1}{\sqrt2}\binom{1}{-1}=-\frac{1}{\sqrt2}\binom{1}{-1}\).
7. Read eigenvalue \(-1\).

Squares of Pauli matrices and allowed measurement values
1. Compute \(\sigma_3^2\) and \(\sigma_1^2\) explicitly.
2. Obtain the identity matrix in both cases.
3. State the same property for \(\sigma_2\).
4. Use the lecture’s reasoning: if the square of the observable is \(1\), its eigenvalues must satisfy \(\lambda^2=1\).
5. Conclude the measurable values are \(\pm1\).

Born-rule examples
1. Prepare \(B=\begin{pmatrix}1\\0\end{pmatrix}\), the \(+1\) eigenstate of \(\sigma_3\).
2. Choose \(A=\frac{1}{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix}\), the \(+1\) eigenstate of \(\sigma_1\).
3. Compute \(\langle A|B\rangle=1/\sqrt2\).
4. Square the magnitude to get \(1/2\).
5. Repeat with \(\frac{1}{\sqrt2}\begin{pmatrix}1\\-1\end{pmatrix}\) and get the same result.
6. For the \(\sigma_1\) versus \(\sigma_2\) example, compute \(\langle A|B\rangle=\frac12-\frac{i}{2}\).
7. Multiply by its complex conjugate and get \(1/2\).

\((\sigma\cdot \hat n)^2=1\)
1. Write \(\sigma\cdot \hat n=n_1\sigma_1+n_2\sigma_2+n_3\sigma_3\).
2. Square it and expand all terms.
3. Collect diagonal terms: \(n_1^2\sigma_1^2+n_2^2\sigma_2^2+n_3^2\sigma_3^2\).
4. Replace \(\sigma_i^2\) by \(1\), giving \((n_1^2+n_2^2+n_3^2)1=1\).
5. Collect cross terms proportional to \(n_1n_2\), \(n_2n_3\), \(n_1n_3\).
6. Use \(\sigma_i\sigma_j+\sigma_j\sigma_i=0\) for \(i\neq j\).
7. Cancel all cross terms.
8. Conclude \((\sigma\cdot \hat n)^2=1\), hence eigenvalues \(\pm1\).

## Notation Choices
- Use bra-ket notation throughout: states as kets \(|A\rangle,|B\rangle\), duals as bras \(\langle A|,\langle B|\).
- Use \(M\) for a generic observable/operator; use \(M^\dagger\) for Hermitian conjugation and \(M^T\) for transpose.
- Use \(\lambda_a,\lambda_A,\lambda_B\) for eigenvalues; treat every \(\lambda\) as a scalar, never a vector.
- Use \(M_{ij}\) for matrix entries and write Hermitian condition as \(M_{ij}=(M_{ji})^*\).
- Use \(|u\rangle,|d\rangle\) or explicit columns \(\binom10,\binom01\) for the two-level basis; keep one choice consistent inside a local derivation.
- Use \(\sigma_1,\sigma_2,\sigma_3\) as the main lecture-faithful labels; note only in prose that these correspond to the three ordinary-space axes.
- Use \(1\) for the identity matrix only when the surrounding context is unmistakably matrix-valued; otherwise prefer “identity matrix” in prose.
- Use \(\hat n\) for a unit spatial direction and \(n_1,n_2,n_3\) for its components, with \(n_1^2+n_2^2+n_3^2=1\).
- Reserve “orthogonal” for states in Hilbert space and “perpendicular” for ordinary-space pointers/directions.
- Keep “expectation value” as \(\langle A|M|A\rangle\), matching the lecture even before a fuller statistical interpretation is developed.

## Uncertain Mathematics
- The transcript around the Hermitian-entry formula is garbled; the final notes should state \(M_{ij}=(M_{ji})^*\) cleanly and not imitate the noisy wording.
- The exact right-hand complex \(2\times2\) example on the board near the Hermitian discussion is not legible enough for literal use.
- The first diagonal eigenvector computation is not visible in the frame set; it should be included as a transcript-backed reconstruction.
- The \(\sigma_1\) equal-weight example in `lecture_03_figure_05.png` is only a setup frame; the completed right-hand side is a cautious completion, not literal board text.
- Susskind briefly mis-speaks as if \(\lambda\) were a vector; this should be normalized away in the final notes.
- The lecture states informally that Hermitian \(n\times n\) matrices have \(n\) eigenvectors/eigenvalues; do not expand this into a full spectral-theorem treatment beyond what is actually used.
- The Pauli-matrix multiplication segments in the transcript are noisy; use the canonical matrices and clean products, but keep only the identities the lecture explicitly motivates.
- The claim that \(\sigma_2^2=1\) is asserted and supported by analogy/brief discussion more than fully worked on the board; it is safe to state, but the notes should not pretend the lecture gave a full explicit multiplication there.