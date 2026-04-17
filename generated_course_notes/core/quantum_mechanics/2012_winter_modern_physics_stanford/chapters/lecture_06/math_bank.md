# Math Bank
## Core Equations

- \(\leftrightarrow\) [visible]
- \(\langle x|y\rangle = 0\) [visible]
- \(|x\rangle = \begin{pmatrix}1\\0\end{pmatrix}\) [transcript-backed]
- \(|y\rangle = \begin{pmatrix}0\\1\end{pmatrix}\) [transcript-backed]
- \(\hat P_{xy}|x\rangle = +|x\rangle\) [transcript-backed]
- \(\hat P_{xy}|y\rangle = -|y\rangle\) [transcript-backed]
- \(P_{xy}=\begin{pmatrix}1&0\\0&-1\end{pmatrix}\) [transcript-backed]
- \(\begin{pmatrix}1&0\\0&-1\end{pmatrix}\begin{pmatrix}1\\0\end{pmatrix}\) [visible]
- \(\begin{pmatrix}1&0\\0&-1\end{pmatrix}\begin{pmatrix}1\\0\end{pmatrix}=\begin{pmatrix}1\\0\end{pmatrix}\) [standard reconstruction]
- \(|/\rangle=\frac{1}{\sqrt2}\bigl(|x\rangle+|y\rangle\bigr)\) [transcript-backed]
- \(|\backslash\rangle=\frac{1}{\sqrt2}\bigl(|x\rangle-|y\rangle\bigr)\) [transcript-backed]
- \(|\langle x|/\rangle|^2=\frac12,\qquad |\langle y|/\rangle|^2=\frac12\) [transcript-backed]
- \(P_{/\backslash}=\begin{pmatrix}0&1\\1&0\end{pmatrix}\) [standard reconstruction]
- \(|\theta\rangle=\cos\theta\,|x\rangle+\sin\theta\,|y\rangle\) [transcript-backed]
- \(|\theta+\pi/2\rangle=-\sin\theta\,|x\rangle+\cos\theta\,|y\rangle\) [transcript-backed]
- \(\langle \theta|\theta+\pi/2\rangle=\cos\theta(-\sin\theta)+\sin\theta\cos\theta=0\) [transcript-backed]
- \(P(\theta\to x)=|\langle x|\theta\rangle|^2=\cos^2\theta\) [transcript-backed]
- \(P(\theta\to y)=|\langle y|\theta\rangle|^2=\sin^2\theta\) [transcript-backed]
- \(\langle \beta|\alpha\rangle=\cos\alpha\cos\beta+\sin\alpha\sin\beta=\cos(\alpha-\beta)\) [transcript-backed]
- \(P(\alpha\to\beta)=|\langle \beta|\alpha\rangle|^2=\cos^2(\alpha-\beta)\) [transcript-backed]
- \(\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta\) [transcript-backed]
- \(\cos(\alpha-\beta)=\cos\alpha\cos\beta+\sin\alpha\sin\beta\) [transcript-backed]
- \(\sin(\alpha+\beta)=\sin\alpha\cos\beta+\sin\beta\cos\alpha\) [transcript-backed]
- \(\sin(\alpha-\beta)=\sin\alpha\cos\beta-\sin\beta\cos\alpha\) [transcript-backed]
- \(\cos 2\alpha=\cos^2\alpha-\sin^2\alpha\) [transcript-backed]
- \(\sin 2\alpha=2\sin\alpha\cos\alpha\) [transcript-backed]
- \(P(\theta\to x\to \theta+\pi/2)=\cos^2\theta\,\sin^2\theta\) [standard reconstruction]
- \(\hat P_\theta|\theta\rangle=+|\theta\rangle\) [transcript-backed]
- \(\hat P_\theta|\theta+\pi/2\rangle=-|\theta+\pi/2\rangle\) [transcript-backed]
- \(P_\theta=\begin{pmatrix}\cos 2\theta&\sin 2\theta\\ \sin 2\theta&-\cos 2\theta\end{pmatrix}\) [standard reconstruction]
- \(P_{\theta+\pi/2}=-P_\theta\) [transcript-backed]
- \(|c_+\rangle=\frac{1}{\sqrt2}\begin{pmatrix}1\\ i\end{pmatrix}\) [transcript-backed]
- \(|c_-\rangle=\frac{1}{\sqrt2}\begin{pmatrix}1\\ -i\end{pmatrix}\) [transcript-backed]
- \(\langle c_-|c_+\rangle=0\) [transcript-backed]
- \(\langle \theta|c_+\rangle=\frac{1}{\sqrt2}\bigl(\cos\theta+i\sin\theta\bigr)\) [transcript-backed]
- \(|\langle \theta|c_+\rangle|^2=\frac12\) [transcript-backed]
- \(E_y=\cos(z-ct),\qquad E_x=\cos(z-ct)\) gives linear polarization at \(45^\circ\) [transcript-backed]
- \(E_y=\cos(z-ct),\qquad E_x=\sin(z-ct)\) or \(E_x=-\sin(z-ct)\) gives the two circular polarizations [transcript-backed]
- \(K|n\rangle=\lambda_n|n\rangle\) [transcript-backed]
- \(\sum_n |n\rangle\langle n|=I\) [transcript-backed]
- \(\langle K\rangle_\psi=\langle\psi|K|\psi\rangle\) [transcript-backed]
- \(\langle\psi|K|\psi\rangle=\sum_n \lambda_n\,\langle\psi|n\rangle\langle n|\psi\rangle\) [transcript-backed]
- \(\langle\psi|K|\psi\rangle=\sum_n \lambda_n\,|\langle n|\psi\rangle|^2\) [transcript-backed]
- \(\langle P_{xy}\rangle_\theta=\cos^2\theta-\sin^2\theta=\cos 2\theta\) [transcript-backed]
- \(\langle x\rangle=0\) for the symmetric two-lump example [transcript-backed]

## Definitions And Objects

- Photon polarization state space: a two-dimensional state space spanned by horizontal and vertical polarization states.
- \(|x\rangle\): horizontally polarized photon.
- \(|y\rangle\): vertically polarized photon.
- \(|/\rangle,|\backslash\rangle\): the \(45^\circ\) and orthogonal \(135^\circ\) linear polarization states.
- \(|\theta\rangle,|\theta+\pi/2\rangle\): arbitrary linear polarization basis associated with a polarizer at angle \(\theta\).
- \(\hat P_{xy}\): observable for polarization in the \(x/y\) basis, with outcomes encoded as \(+1\) and \(-1\).
- \(\hat P_\theta\): observable for polarization along angle \(\theta\), again with eigenvalues \(+1,-1\).
- \(c=\cos\theta,\ s=\sin\theta\): local shorthand used by Susskind during the \(P_\theta\) check.
- \(|c_+\rangle,|c_-\rangle\): neutral labels for the two circular polarization states; the lecture calls them left and right circular but treats handedness labels loosely.
- Amplitude: an inner product such as \(\langle \beta|\alpha\rangle\); probability is the modulus squared of the amplitude.
- Hermitian observable: an operator with real eigenvalues and orthogonal eigenvectors; for real matrices in this lecture, Hermitian reduces to symmetric.
- Average value / expectation value: \(\langle\psi|K|\psi\rangle\), interpreted as the weighted average of the observable’s eigenvalues in state \(|\psi\rangle\).

## Derivation Steps

Orthogonality and normalization of the \(x,y\) basis
1. Represent \(|x\rangle\) and \(|y\rangle\) as \(\begin{pmatrix}1\\0\end{pmatrix}\) and \(\begin{pmatrix}0\\1\end{pmatrix}\).
2. Compute \(\langle x|y\rangle=1\cdot 0+0\cdot 1=0\).
3. Check norms: \(1^2+0^2=1\) and \(0^2+1^2=1\).

Matrix form of \(\hat P_{xy}\)
1. Impose \(\hat P_{xy}|x\rangle=+|x\rangle\) and \(\hat P_{xy}|y\rangle=-|y\rangle\).
2. In the \((|x\rangle,|y\rangle)\) basis, the matrix with those eigenvectors and eigenvalues is \(\begin{pmatrix}1&0\\0&-1\end{pmatrix}\).
3. Check on \(|x\rangle\): \(\begin{pmatrix}1&0\\0&-1\end{pmatrix}\begin{pmatrix}1\\0\end{pmatrix}=\begin{pmatrix}1\\0\end{pmatrix}\).

Construction of the \(45^\circ\) basis
1. Use equal likelihood through \(x\) and \(y\) polarizers to motivate \(|/\rangle=\frac1{\sqrt2}(|x\rangle+|y\rangle)\).
2. Choose an orthogonal partner \(|\backslash\rangle=\frac1{\sqrt2}(|x\rangle-|y\rangle)\).
3. Verify \(\langle /|\backslash\rangle=\frac12-\frac12=0\) and both norms equal \(1\).

Transmission probability for \(|/\rangle\) through an \(x\) or \(y\) polarizer
1. Take the amplitude \(\langle x|/\rangle=\frac1{\sqrt2}\).
2. Square it to get the probability \(1/2\).
3. Repeat with \(\langle y|/\rangle=\frac1{\sqrt2}\) to get the same answer.

Arbitrary-angle basis and \(x/y\) probabilities
1. Write \(|\theta\rangle=\cos\theta|x\rangle+\sin\theta|y\rangle\).
2. Write the orthogonal companion \(|\theta+\pi/2\rangle=-\sin\theta|x\rangle+\cos\theta|y\rangle\).
3. Compute \(\langle x|\theta\rangle=\cos\theta\) and \(P(\theta\to x)=\cos^2\theta\).
4. Compute \(\langle y|\theta\rangle=\sin\theta\) and \(P(\theta\to y)=\sin^2\theta\).
5. Add the two probabilities to recover \(1\).

General two-polarizer law
1. Represent the prepared state as \(|\alpha\rangle=\begin{pmatrix}\cos\alpha\\ \sin\alpha\end{pmatrix}\).
2. Represent the testing bra as \(\langle\beta|=\begin{pmatrix}\cos\beta&\sin\beta\end{pmatrix}\).
3. Multiply to get \(\langle\beta|\alpha\rangle=\cos\alpha\cos\beta+\sin\alpha\sin\beta\).
4. Use the trig identity to rewrite this as \(\cos(\alpha-\beta)\).
5. Square the amplitude to obtain \(P(\alpha\to\beta)=\cos^2(\alpha-\beta)\).

Intermediate-polarizer “assist”
1. First transmission: \(P(\theta\to x)=\cos^2\theta\).
2. After success, the state is reset to \(|x\rangle\), not left as \(|\theta\rangle\).
3. Second transmission: \(P(x\to \theta+\pi/2)=\sin^2\theta\).
4. Multiply successive conditional probabilities to get \(\cos^2\theta\,\sin^2\theta\).

Check of \(P_\theta\)
1. Take \(P_\theta=\begin{pmatrix}\cos 2\theta&\sin 2\theta\\ \sin 2\theta&-\cos 2\theta\end{pmatrix}\).
2. Apply it to \(|\theta\rangle=\begin{pmatrix}\cos\theta\\ \sin\theta\end{pmatrix}\).
3. Use \(\cos 2\theta=\cos^2\theta-\sin^2\theta\) and \(\sin 2\theta=2\sin\theta\cos\theta\).
4. Simplify the top entry to \(\cos\theta\) and the bottom entry to \(\sin\theta\).
5. Conclude \(P_\theta|\theta\rangle=|\theta\rangle\).
6. The same matrix should send \(|\theta+\pi/2\rangle\) to minus itself.

Circular polarization through a linear polarizer
1. Take one circular state as \(|c_+\rangle=\frac1{\sqrt2}\begin{pmatrix}1\\ i\end{pmatrix}\).
2. Compute the amplitude with \(|\theta\rangle\): \(\langle\theta|c_+\rangle=\frac1{\sqrt2}(\cos\theta+i\sin\theta)\).
3. Multiply by the complex conjugate: \(\frac12(\cos\theta+i\sin\theta)(\cos\theta-i\sin\theta)\).
4. Use \(\cos^2\theta+\sin^2\theta=1\) to get \(1/2\).

Expectation-value formula
1. Start from \(\langle\psi|K|\psi\rangle\).
2. Insert the identity \(\sum_n |n\rangle\langle n|=I\) between \(K\) and \(|\psi\rangle\).
3. Replace \(K|n\rangle\) by \(\lambda_n|n\rangle\).
4. Obtain \(\sum_n \lambda_n\,\langle\psi|n\rangle\langle n|\psi\rangle\).
5. Recognize \(\langle\psi|n\rangle\langle n|\psi\rangle=|\langle n|\psi\rangle|^2\).
6. Read the result as probability times eigenvalue, summed over all outcomes.

Expectation value for polarization in state \(|\theta\rangle\)
1. Form \(\langle\theta|P_{xy}|\theta\rangle\).
2. Multiply \(P_{xy}\begin{pmatrix}\cos\theta\\ \sin\theta\end{pmatrix}\) to get \(\begin{pmatrix}\cos\theta\\ -\sin\theta\end{pmatrix}\).
3. Take the inner product with \(\langle\theta|=(\cos\theta,\sin\theta)\).
4. Obtain \(\cos^2\theta-\sin^2\theta\).
5. Rewrite as \(\cos 2\theta\).

## Notation Choices

- Use kets for prepared states and bras for dual vectors: \(|x\rangle,\ |y\rangle,\ |/\rangle,\ |\backslash\rangle,\ |\theta\rangle\).
- Use \(\hat P_{xy}\) and \(\hat P_\theta\) for operators in prose; use \(P_{xy}\) and \(P_\theta\) for their matrix representatives when the basis is fixed.
- Keep the lecture’s \(\pm1\) eigenvalue convention for polarization observables; note that the choice is conventional but should remain fixed once introduced.
- Keep \(x,y\) for the basic linear polarization basis, not \(H,V\), because that is the lecture’s language.
- Use \(|/\rangle\) and \(|\backslash\rangle\) for the \(45^\circ\) pair if typography permits; otherwise explain once that these are the slash/backslash states.
- Use \(P(\alpha\to\beta)\) as shorthand for transmission probability from an \(\alpha\)-prepared photon to a \(\beta\)-analyzer.
- Use \(c=\cos\theta,\ s=\sin\theta\) only inside the local check of \(P_\theta\); elsewhere keep full trig functions.
- For circular polarization, prefer neutral symbols such as \(|c_+\rangle, |c_-\rangle\) in the working draft, then mention that the lecture informally calls them left/right circular.
- Treat \(\langle\psi|K|\psi\rangle\) as “average value” first; if “expectation value” is used, flag it as the lecture’s standard-but-misleading term.
- Preserve the double-arrow polarization mark as notation for an unsigned polarization axis, not as a directed vector.

## Uncertain Mathematics

- The slash/backslash observable matrix is not legible in the transcript around 00:33–00:35. \(P_{/\backslash}=\begin{pmatrix}0&1\\1&0\end{pmatrix}\) is the natural reconstruction from the stated eigenvector action, but it should be marked as reconstructed.
- The intermediate board algebra in the \(P_\theta\) check is partially garbled. The final cleaned matrix and the fact that it sends \(|\theta\rangle\) to itself are secure; many intermediate chalk lines are not.
- The lecture’s first observable has a custom board label tied to “polarization in the \(xy\) plane.” Standardizing this as \(\hat P_{xy}\) is editorial, not a literal board transcription.
- Handedness labels for the circular states are uncertain: Susskind explicitly says he may have left and right mixed up.
- If commutator notation such as \([P_\alpha,P_\beta]\neq 0\) is introduced in the final notes, that is explanatory notation rather than a visible board equation.
- The sign choice in \(|\backslash\rangle\) and the overall phase of circular states are physically inessential; the notes should state that these vectors are defined only up to overall phase/sign.
- The wave-equation examples for circular polarization are motivated verbally and schematically, not presented as a carefully normalized blackboard derivation.
- The two-lump wavefunction image supports the geometry of the example, but any labels such as \(x=0\) or \(\pm x_0\) should come from the transcript, not from the bitmap.