# Math Bank
## Core Equations
- \(\langle j|i\rangle=\delta_{ji}\) `[transcript-backed]`
- \(|A\rangle=\sum_i \alpha_i |i\rangle\) `[transcript-backed]`
- \(\alpha_i=\langle i|A\rangle\) `[transcript-backed]`
- \(|A\rangle=\sum_i |i\rangle\langle i|A\rangle\) `[transcript-backed]`
- \(\langle A|=\sum_i \langle A|i\rangle \langle i|\) `[transcript-backed]`
- \(M(z|A\rangle)=z\,M|A\rangle\) `[transcript-backed]`
- \(M(|A\rangle+|B\rangle)=M|A\rangle+M|B\rangle\) `[transcript-backed]`
- \(M|A\rangle=|B\rangle\) `[visible]`
- \(\langle i|M|A\rangle=\langle i|B\rangle=\beta_i\) `[visible]`
- \(\sum_j \langle i|M|j\rangle \langle j|A\rangle=\beta_i\) `[visible]`
- \(m_{ij}=\langle i|M|j\rangle\) `[transcript-backed]`
- \(\sum_j m_{ij}\alpha_j=\beta_i\) `[visible]`
- \(\begin{pmatrix} m_{11} & m_{12} & m_{13} & \cdots \\ m_{21} & m_{22} & \cdots & \cdots \\ \vdots & & & \\ \cdots & & & m_{NN} \end{pmatrix}\begin{pmatrix}\alpha_1\\ \alpha_2\\ \vdots\\ \alpha_N\end{pmatrix}=\begin{pmatrix}\beta_1\\ \beta_2\\ \vdots\\ \beta_N\end{pmatrix}\) `[visible]`
- \(\langle A|M|B\rangle=\sum_{ij}\alpha_i^*\,m_{ij}\,\beta_j\) `[standard reconstruction]`
- \((M^\dagger)_{ij}=(M_{ji})^*\) `[transcript-backed]`
- \(M=M^\dagger\) `[transcript-backed]`
- \(M_{ij}=(M_{ji})^*\) `[transcript-backed]`
- \(M|i\rangle=\lambda_i |i\rangle\) `[transcript-backed]`
- \(\lambda_i=\lambda_i^*\) for Hermitian \(M\) `[transcript-backed]`
- \((\lambda_i-\lambda_j)\langle j|i\rangle=0\) `[transcript-backed]`
- \(\lambda_i\neq\lambda_j \;\Rightarrow\; \langle j|i\rangle=0\) `[transcript-backed]`
- \(P(\lambda_i\mid |A\rangle)=|\langle i|A\rangle|^2=\langle i|A\rangle\langle A|i\rangle\) `[transcript-backed]`
- \(\sum_i |\langle i|A\rangle|^2=1\) `[transcript-backed]`
- \(\langle A|A\rangle=1\) `[transcript-backed]`
- \(\sum_i \alpha_i^*\alpha_i=1\) `[transcript-backed]`
- \(|A\rangle \mapsto e^{i\theta}|A\rangle\) leaves all probabilities unchanged `[transcript-backed]`
- \(\sigma_z|u\rangle=+|u\rangle\) `[transcript-backed]`
- \(\sigma_z|d\rangle=-|d\rangle\) `[transcript-backed]`
- \(\sigma_z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}\) `[transcript-backed]`
- \(\sigma_x|r\rangle=+|r\rangle\) `[transcript-backed]`
- \(\sigma_x|l\rangle=-|l\rangle\) `[transcript-backed]`
- \(|u\rangle=\dfrac{|l\rangle+|r\rangle}{\sqrt2}\) `[transcript-backed]`
- \(|d\rangle=\dfrac{|r\rangle-|l\rangle}{\sqrt2}\) `[transcript-backed]`
- \(|r\rangle=\dfrac{|u\rangle+|d\rangle}{\sqrt2}\) `[standard reconstruction]`
- \(|l\rangle=\dfrac{|u\rangle-|d\rangle}{\sqrt2}\) `[standard reconstruction]`
- \(\sigma_x=\begin{pmatrix}0&1\\1&0\end{pmatrix}\) `[transcript-backed]`
- \(\sigma_y|\text{in}\rangle=+|\text{in}\rangle\) `[transcript-backed]`
- \(\sigma_y|\text{out}\rangle=-|\text{out}\rangle\) `[transcript-backed]`
- \(|\text{in}\rangle=\dfrac{|u\rangle+i|d\rangle}{\sqrt2}\) `[standard reconstruction]`
- \(|\text{out}\rangle=\dfrac{|u\rangle-i|d\rangle}{\sqrt2}\) `[standard reconstruction]`
- \(\langle \text{in}|\text{out}\rangle=0\) `[transcript-backed]`
- \(\sigma_y=\begin{pmatrix}0&-i\\ i&0\end{pmatrix}\) `[transcript-backed]`

## Definitions And Objects
- State space: a complex vector space of ket vectors; bras are the conjugate/dual objects paired with kets by inner product.
- Orthonormal basis \(\{|i\rangle\}\): mutually orthogonal, normalized basis vectors; dimension = maximum number of mutually orthogonal vectors.
- Components of a ket: \(\alpha_i\) in \(|A\rangle=\sum_i \alpha_i|i\rangle\).
- Components of an output ket: \(\beta_i\) in \(|B\rangle=\sum_i \beta_i|i\rangle\).
- Linear operator \(M\): maps ket vectors to ket vectors and obeys the two linearity rules.
- Matrix elements of \(M\): \(m_{ij}=\langle i|M|j\rangle\).
- Matrix representation of \(M\): square array of \(m_{ij}\) once a basis is chosen.
- \(M^\dagger\): the left-acting partner of \(M\); operator version of complex conjugation / Hermitian conjugation.
- Hermitian operator: operator equal to its own Hermitian conjugate.
- Eigenvector/eigenvalue pair: vector \(|i\rangle\) satisfying \(M|i\rangle=\lambda_i |i\rangle\).
- Eigendirection: lecture’s caution that overall rescaling of an eigenvector does not change the eigenvalue.
- Observable: measurable quantity represented by a Hermitian operator.
- Probability amplitude: \(\langle i|A\rangle\).
- Probability: modulus squared of the amplitude.
- Pauli matrices: \(\sigma_x,\sigma_y,\sigma_z\), representing spin components.

## Derivation Steps
**1. Coefficients from basis expansion**
1. Start with \(|A\rangle=\sum_i \alpha_i |i\rangle\).
2. Multiply on the left by \(\langle j|\).
3. Use \(\langle j|i\rangle=\delta_{ji}\).
4. Collapse the sum to one term.
5. Conclude \(\alpha_j=\langle j|A\rangle\).
6. Reinsert into the original expansion to get \(|A\rangle=\sum_i |i\rangle\langle i|A\rangle\).

**2. Operator action to component equation**
1. Start with \(M|A\rangle=|B\rangle\).
2. Multiply on the left by \(\langle i|\).
3. Identify \(\langle i|B\rangle=\beta_i\).
4. Expand \(|A\rangle=\sum_j \alpha_j |j\rangle\).
5. Substitute into \(\langle i|M|A\rangle\).
6. Pull the sum through to get \(\sum_j \langle i|M|j\rangle \alpha_j=\beta_i\).
7. Define \(m_{ij}=\langle i|M|j\rangle\).
8. Read the result as \(\sum_j m_{ij}\alpha_j=\beta_i\).
9. Package it as matrix times column vector equals output column vector.

**3. Bra-side double-sum formula and bracket-independence**
1. Expand \(\langle A|=\sum_i \alpha_i^*\langle i|\).
2. Expand \(|B\rangle=\sum_j \beta_j |j\rangle\).
3. Insert both expansions into \(\langle A|M|B\rangle\).
4. Obtain the double sum \(\sum_{ij}\alpha_i^* m_{ij}\beta_j\).
5. Observe that the same double sum is obtained whether \(M\) is viewed as acting first on \(|B\rangle\) or first on \(\langle A|\).
6. Use this to justify removing brackets in expressions like \(\langle A|M|B\rangle\).

**4. Dagger matrix elements**
1. Let \(M|i\rangle=|i'\rangle\).
2. Then \(M_{ji}=\langle j|M|i\rangle=\langle j|i'\rangle\).
3. By definition of the left-acting conjugate operator, \(\langle i|M^\dagger=\langle i'|\).
4. Therefore \((M^\dagger)_{ij}=\langle i|M^\dagger|j\rangle=\langle i'|j\rangle\).
5. Reverse bra-ket order and complex conjugate.
6. Conclude \((M^\dagger)_{ij}=(M_{ji})^*\).

**5. Reality of Hermitian eigenvalues**
1. Assume \(M=M^\dagger\) and \(M|i\rangle=\lambda_i |i\rangle\).
2. Flip the equation to bra form: \(\langle i|M=\lambda_i^*\langle i|\).
3. Multiply the ket equation on the left by \(\langle i|\): \(\langle i|M|i\rangle=\lambda_i\langle i|i\rangle\).
4. Multiply the bra equation on the right by \(|i\rangle\): \(\langle i|M|i\rangle=\lambda_i^*\langle i|i\rangle\).
5. Compare the two results.
6. Since \(\langle i|i\rangle\neq 0\), conclude \(\lambda_i=\lambda_i^*\).

**6. Orthogonality of eigenvectors with distinct eigenvalues**
1. Start with \(M|i\rangle=\lambda_i|i\rangle\) and \(M|j\rangle=\lambda_j|j\rangle\).
2. Flip the second equation to bra form: \(\langle j|M=\lambda_j\langle j|\) because Hermitian eigenvalues are real.
3. Multiply the first equation on the left by \(\langle j|\): \(\langle j|M|i\rangle=\lambda_i\langle j|i\rangle\).
4. Multiply the bra equation on the right by \(|i\rangle\): \(\langle j|M|i\rangle=\lambda_j\langle j|i\rangle\).
5. Subtract the two equations.
6. Obtain \((\lambda_i-\lambda_j)\langle j|i\rangle=0\).
7. If \(\lambda_i\neq\lambda_j\), conclude \(\langle j|i\rangle=0\).

**7. Normalization from total probability**
1. Start with total probability \(\sum_i |\langle i|A\rangle|^2=1\).
2. Rewrite \( |\langle i|A\rangle|^2\) as \(\langle A|i\rangle\langle i|A\rangle\).
3. Sum over \(i\).
4. Recognize the completeness combination acting on \(|A\rangle\).
5. Conclude \(\langle A|A\rangle=1\).
6. Rewrite equivalently as \(\sum_i \alpha_i^*\alpha_i=1\).

**8. \(\sigma_z\) matrix in the up/down basis**
1. Use \(\sigma_z|u\rangle=|u\rangle\) and \(\sigma_z|d\rangle=-|d\rangle\).
2. Choose \(|u\rangle,|d\rangle\) as basis vectors.
3. Compute \(\langle u|\sigma_z|u\rangle=1\).
4. Use orthogonality to get \(\langle u|\sigma_z|d\rangle=\langle d|\sigma_z|u\rangle=0\).
5. Compute \(\langle d|\sigma_z|d\rangle=-1\).
6. Read off \(\sigma_z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}\).

**9. \(\sigma_x\) matrix in the up/down basis**
1. Use \(|r\rangle,|l\rangle\) as eigenvectors with eigenvalues \(+1,-1\).
2. Rewrite \(|u\rangle\) and \(|d\rangle\) in the \(r/l\) basis.
3. Compute the diagonal matrix elements \(\langle u|\sigma_x|u\rangle\) and \(\langle d|\sigma_x|d\rangle\); both vanish.
4. Compute the off-diagonal elements \(\langle u|\sigma_x|d\rangle\) and \(\langle d|\sigma_x|u\rangle\); both equal \(1\).
5. Read off \(\sigma_x=\begin{pmatrix}0&1\\1&0\end{pmatrix}\).

**10. \(\sigma_y\) from in/out eigenvectors**
1. Use \(|\text{in}\rangle,|\text{out}\rangle\) as eigenvectors with eigenvalues \(+1,-1\).
2. Use the normalized canonical forms \((|u\rangle\pm i|d\rangle)/\sqrt2\) cautiously.
3. Solve for \(|u\rangle,|d\rangle\) in the in/out basis.
4. Repeat the same matrix-element logic used for \(\sigma_x\).
5. Obtain \(\sigma_y=\begin{pmatrix}0&-i\\ i&0\end{pmatrix}\).

## Notation Choices
- Use uppercase \(M\) for the abstract operator; use lowercase \(m_{ij}\) for its matrix elements.
- Keep \(m_{ij}=\langle i|M|j\rangle\) as the standard notation in the chapter, even though the board handwriting sometimes looks like \(M_{ij}\).
- Use \(|A\rangle\) for the input state and \(|B\rangle\) for the output state in the operator section.
- Use \(\alpha_i\) for coefficients of \(|A\rangle\), and \(\beta_i\) for coefficients of \(|B\rangle\).
- Use \(i,j\) for basis indices in the generic finite-dimensional discussion.
- Standardize the generic finite-dimensional size to \(N\) in matrix displays to match the lecture frames; use \(N=2\) for the spin example.
- Standardize the Kronecker symbol as \(\delta_{ij}\) in final notes; transcript temporarily says \(\delta_{JI}\).
- Write operators acting on bras on the right: \(\langle A|M\), not \(M\langle A|\).
- Use \(M^\dagger\) for Hermitian conjugation throughout.
- In the eigenvalue section, do not mix “arbitrary basis label \(i\)” and “eigenvector label \(i\)” in the same local derivation without an explicit reset.
- For spin states, use \(|u\rangle,|d\rangle,|r\rangle,|l\rangle,|\text{in}\rangle,|\text{out}\rangle\) in equations, with prose aliases up/down/right/left/in/out.
- State explicitly when a matrix is written in the \(|u\rangle,|d\rangle\) basis.
- In prose, prefer “observable is represented by a Hermitian operator” over a strict equals sign.
- Probability amplitude = \(\langle i|A\rangle\); probability = modulus squared of that amplitude.

## Uncertain Mathematics
- The middle line in `lecture_03_figure_02.png` is not clean enough to certify every symbol placement; final notes should use the standard cleaned form \(\sum_j \langle i|M|j\rangle \alpha_j=\beta_i\).
- The bra-side derivation around 00:27–00:30 is transcript-garbled; \(\langle A|M|B\rangle=\sum_{ij}\alpha_i^*m_{ij}\beta_j\) is a cautious standard reconstruction.
- The exact numerical Hermitian-conjugation example around 00:40:50–00:41:54 is unstable in the transcript; use only a cleaned example or omit the exact original numbers.
- The transcript line “the diagonal elements are not the same” is inconsistent with the immediately following argument; the intended statement is that diagonal elements of a Hermitian matrix are real.
- The lecture’s \(\sigma_y\) segment is intrinsically unstable: Susskind says he may have written the wrong symbol, cannot remember which state is which, and omitted \(\sqrt2\) factors. Use canonical normalized \(y\)-basis states only with an explicit note that this is a stabilization.
- The late question about \(\cos\theta\) versus \(\cos^2\theta\) is not resolved in this lecture; do not write it up as if the derivation is present here.
- The final in/out correction depends on complex conjugating \(i\) in the bra; use it only to support orthogonality, not as evidence for a larger missing derivation.