# Math Bank

## Core Equations

- $\hat P_{xy}=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$ [transcript-backed]
- $|x\rangle=\begin{pmatrix}1\\0\end{pmatrix},\quad |y\rangle=\begin{pmatrix}0\\1\end{pmatrix}$ [transcript-backed]
- $\hat P_{45}=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ [transcript-backed]
- $|\theta\rangle=\begin{pmatrix}\cos\theta\\ \sin\theta\end{pmatrix}$ [transcript-backed]
- $|\theta+\pi/2\rangle\sim\begin{pmatrix}\sin\theta\\-\cos\theta\end{pmatrix}$ [standard reconstruction]
- $|45^\circ,+\rangle=\dfrac{1}{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix},\quad |45^\circ,-\rangle=\dfrac{1}{\sqrt2}\begin{pmatrix}1\\-1\end{pmatrix}$ [transcript-backed]
- $|C_+\rangle=\dfrac{1}{\sqrt2}\begin{pmatrix}1\\ i\end{pmatrix},\quad |C_-\rangle=\dfrac{1}{\sqrt2}\begin{pmatrix}1\\ -i\end{pmatrix}$ [transcript-backed]
- $\hat P_{\mathrm{circ}}=\begin{pmatrix}0&-i\\ i&0\end{pmatrix}$ [transcript-backed]
- $\hat P_{\mathrm{circ}}|C_\pm\rangle=\pm |C_\pm\rangle$ [transcript-backed]
- $\langle\psi|\hat K|\psi\rangle$ [transcript-backed]
- $P(a\to b)=|\langle b|a\rangle|^2=\langle a|b\rangle\langle b|a\rangle$ [transcript-backed]
- $\langle\psi|\psi\rangle=1$ [transcript-backed]
- $|\psi\rangle=\begin{pmatrix}\alpha\\ \beta\end{pmatrix}$ [transcript-backed]
- $\alpha^*\alpha+\beta^*\beta=1$ [transcript-backed]
- $z=e^{i\theta},\quad z^*=e^{-i\theta},\quad zz^*=1$ [transcript-backed]
- $|A\rangle$ and $e^{i\theta}|A\rangle$ are written side by side as mathematically different but physically equivalent state vectors [visible]
- $|\psi\rangle\sim e^{i\theta}|\psi\rangle$ only in the sense of “same physical significance,” not literal equality [standard reconstruction]
- $\alpha=a\in\mathbb R,\quad \beta=\sqrt{1-a^2}\,e^{i\phi}$ [transcript-backed]
- $|\psi\rangle=\begin{pmatrix}a\\ \sqrt{1-a^2}\,e^{i\phi}\end{pmatrix}$ [transcript-backed]
- $\langle\psi|\theta\rangle=a\cos\theta+\sqrt{1-a^2}\,e^{-i\phi}\sin\theta$ [standard reconstruction]
- $P_\theta(\psi)=|\langle\psi|\theta\rangle|^2$ [transcript-backed]
- $\langle B|A\rangle=0$ for orthogonal states, $\langle B|A\rangle=1$ for identical normalized states [transcript-backed]
- $\langle B'|A'\rangle=\langle B|A\rangle$ [transcript-backed]
- \(\sum_n |n\rangle\langle n|=I\) [transcript-backed]
- $\langle B|L|A\rangle$ [transcript-backed]
- $\langle n|L^\dagger|m\rangle=\langle m|L|n\rangle^*$ [transcript-backed]
- $(L^\dagger)_{nm}=L_{mn}^*$ [transcript-backed]
- $L=L^\dagger$ [transcript-backed]
- $L_{ii}\in\mathbb R$ for Hermitian $L$ [transcript-backed]
- $L_{ij}=(L_{ji})^*$ for Hermitian $L$ [transcript-backed]
- $\langle a|U^\dagger U|b\rangle=\langle a|b\rangle$ for all $|a\rangle,|b\rangle$ [transcript-backed]
- $U^\dagger U=I$ [transcript-backed]
- $U^\dagger=U^{-1}$ [transcript-backed]

## Definitions And Objects

- `State vector`: ket $|\psi\rangle$ with corresponding bra $\langle\psi|$.
- `Observable`: Hermitian operator; in this lecture the running examples are the polarization operators.
- `Expectation value`: sandwich $\langle\psi|\hat K|\psi\rangle$.
- `Transition probability`: squared overlap between eigenstates of different observables.
- `Phase`: a pure complex number of unit modulus, written $e^{i\theta}$.
- `Overall phase irrelevance`: multiplying the whole state vector by a pure phase does not change measurable content.
- `Physical photon polarization state`: normalized two-component complex vector modulo overall phase.
- `Plane polarization`: one-parameter family labeled by axis angle.
- `Elliptical polarization`: two-parameter family described heuristically by major-axis angle and eccentricity.
- `Signed eccentricity`: lecture-level device for encoding the two senses of rotation using one real parameter that can pass through zero and become negative.
- `Relationship between states`: inner product / overlap; operationally this is the relevant notion of sameness, difference, and partial similarity.
- `Hermitian conjugate`: transpose plus complex conjugation; operator acting on bras induced from the operator acting on kets.
- `Hermitian operator`: operator equal to its Hermitian conjugate.
- `Unitary operator`: operator preserving inner products, equivalently satisfying $U^\dagger U=I$.

## Derivation Steps

Phase cancellation in an expectation value:
1. Start from $\langle\psi|\hat K|\psi\rangle$.
2. Replace $|\psi\rangle$ by $e^{i\theta}|\psi\rangle$.
3. The corresponding bra becomes $\langle\psi|e^{-i\theta}$.
4. Pull the phase factors out as ordinary numbers.
5. Use $e^{-i\theta}e^{i\theta}=1$.
6. Conclude that the expectation value is unchanged.

Phase cancellation in a transition probability:
1. Start from $|\langle b|a\rangle|^2=\langle a|b\rangle\langle b|a\rangle$.
2. Multiply either $|a\rangle$ or $|b\rangle$ by an overall phase.
3. The corresponding bra picks up the conjugate phase.
4. The phase and conjugate phase multiply to $1$.
5. Conclude that the probability is unchanged.

Parameter count for a photon polarization state:
1. Begin with $|\psi\rangle=\begin{pmatrix}\alpha\\ \beta\end{pmatrix}$.
2. Count $\alpha,\beta$ as two complex numbers = four real parameters.
3. Impose normalization $\alpha^*\alpha+\beta^*\beta=1$.
4. Reduce from four real parameters to three.
5. Use overall phase freedom to make the upper component real.
6. Rename the real upper component $a$.
7. Solve $a^2+\beta^*\beta=1$ to get $|\beta|=\sqrt{1-a^2}$.
8. Write $\beta=\sqrt{1-a^2}\,e^{i\phi}$.
9. Conclude that only two real parameters remain: $a$ and $\phi$.

Overlap formula for probing the major axis:
1. Take the elliptic state in gauge-fixed form $|\psi\rangle=\begin{pmatrix}a\\ \sqrt{1-a^2}e^{i\phi}\end{pmatrix}$.
2. Take the linear-polarization state $|\theta\rangle=\begin{pmatrix}\cos\theta\\ \sin\theta\end{pmatrix}$.
3. Form the overlap $\langle\psi|\theta\rangle$.
4. Conjugate the phase in the bra component of $\langle\psi|$.
5. Obtain $\langle\psi|\theta\rangle=a\cos\theta+\sqrt{1-a^2}e^{-i\phi}\sin\theta$.
6. Square the modulus to get the transmission probability through a polarizer at angle $\theta$.
7. Maximize with respect to $\theta$.
8. Read off the major-axis direction from the maximizing angle.

Hermitian-conjugate matrix rule:
1. Define matrix elements by $L_{nm}=\langle n|L|m\rangle$.
2. Compare $\langle B|L|A\rangle$ with the reversed-order inner product involving $L^\dagger$.
3. Use the fact that reversed inner products are complex conjugates.
4. Interchange bras and kets and complex conjugate.
5. Deduce $\langle n|L^\dagger|m\rangle=\langle m|L|n\rangle^*$.
6. In matrix notation, deduce $(L^\dagger)_{nm}=L_{mn}^*$.

Hermitian-matrix component conditions:
1. Start from $L=L^\dagger$.
2. On the diagonal, require $L_{ii}=L_{ii}^*$.
3. Conclude $L_{ii}$ is real.
4. Off the diagonal, require $L_{ij}=(L^\dagger)_{ij}=L_{ji}^*$.
5. Conclude reflected entries across the diagonal are complex conjugates.

Unitary condition from preserved relations:
1. Let $U|a\rangle=|a'\rangle$ and $U|b\rangle=|b'\rangle$.
2. Then bras transform with $U^\dagger$: $\langle a'|=\langle a|U^\dagger$.
3. Impose preservation of inner products: $\langle a'|b'\rangle=\langle a|b\rangle$.
4. Substitute transformed bra and ket: $\langle a|U^\dagger U|b\rangle=\langle a|b\rangle$.
5. Require this for all $|a\rangle,|b\rangle$.
6. Conclude $U^\dagger U=I$.
7. Read this as $U^\dagger=U^{-1}$.

## Notation Choices

- Use $|x\rangle, |y\rangle$ for horizontal and vertical polarization basis states.
- Use $\hat P_{xy}$, $\hat P_{45}$, and $\hat P_{\mathrm{circ}}$ for the three polarization observables; the lecture’s spoken names are loose, so the chapter should regularize them.
- Reserve $\theta$ for linear-polarization analyzer angle.
- Use $\phi$ for the relative phase in the gauge-fixed photon state; do not reuse $\theta$ there once the lecture notices the collision.
- Write normalized state vectors as kets and their conjugates as bras: $|\psi\rangle$, $\langle\psi|$.
- Use $a\in\mathbb R$ for the gauge-fixed upper component after quotienting by overall phase.
- Use the matrix-element convention $L_{nm}=\langle n|L|m\rangle$.
- Write Hermitian conjugation with a dagger: $L^\dagger$.
- Prefer the cleaned statement “same physical significance as” over introducing a permanent dotted-equals symbol in the final notes.
- For the overlap formula, keep one convention throughout:
  $\langle\psi|\theta\rangle=a\cos\theta+\sqrt{1-a^2}e^{-i\phi}\sin\theta$.
  If the writer instead prefers $\langle\theta|\psi\rangle$, conjugate the phase accordingly.
- If labels are needed for circular states, use neutral descriptive labels rather than inventing ornate notation not used in the lecture.

## Uncertain Mathematics

- The exact sign choice for the orthogonal partner to $|\theta\rangle$ is not fixed by the lecture and is explicitly treated as physically unimportant.
- The exact handwritten relation in the phase frame is not fully legible; the clean mathematical content is the comparison of $|A\rangle$ with $e^{i\theta}|A\rangle$.
- The bra-ket order in the overlap formula is not fully secure from the frame alone; the transcript controls the cleaned choice.
- The phase sign in the overlap formula is corrected mid-lecture; the final notes should present the corrected conjugated factor cautiously.
- The eccentricity discussion is heuristic. The lecture does not give a formal analytic definition of signed eccentricity beyond the geometric story of passing through zero and reversing handedness.
- The extraction of eccentricity from probability differences is only sketched; do not add a finished closed-form relation unless it is derived elsewhere.
- The theorem “$\langle\psi|L|\psi\rangle$ real for all $\psi$ implies $L$ Hermitian” is asserted but not proved in detail here.
- One spoken line says Hermitian operators have eigenvectors that “are real”; that should not be preserved literally without qualification. The mathematically reliable point is real eigenvalues and mutually orthogonal eigenvectors for distinct eigenvalues.
- The lecture ends before deriving the unit-modulus property of unitary eigenvalues; that should not be presented as having been shown in this lecture.
- The early transcript around the rotated linear-polarization observable is partially garbled; the matrix $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ is recoverable from the later Hermitian check and should be treated as transcript-supported but not as a pristine verbatim transcription.