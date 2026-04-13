# Math Bank
## Core Equations
- \(\displaystyle |\psi_{\pm}\rangle=\frac{|ud\rangle\pm|du\rangle}{\sqrt2}\) [transcript-backed]
- \(\displaystyle \sigma_1|u\rangle=|d\rangle\) [visible]
- \(\displaystyle \sigma_1|d\rangle=|u\rangle\) [transcript-backed]
- \(\displaystyle \sigma_2|u\rangle=i|d\rangle\) [transcript-backed]
- \(\displaystyle \sigma_2|d\rangle=-i|u\rangle\) [transcript-backed]
- \(\displaystyle \sigma_3|u\rangle=|u\rangle\) [transcript-backed]
- \(\displaystyle \sigma_3|d\rangle=-|d\rangle\) [transcript-backed]
- \(\displaystyle \langle \sigma_i\rangle=0,\qquad \langle \tau_i\rangle=0\) [transcript-backed]
- \(\displaystyle \langle \psi_+|\sigma_3|\psi_+\rangle=0\) [transcript-backed]
- \(\displaystyle (\sigma_3+\tau_3)(|ud\rangle\pm|du\rangle)=0\) [transcript-backed]
- \(\displaystyle (\sigma_1+\tau_1)(|ud\rangle+|du\rangle)=2|uu\rangle+2|dd\rangle\) [transcript-backed]
- \(\displaystyle (\sigma_1+\tau_1)(|ud\rangle-|du\rangle)=0\) [transcript-backed]
- \(\displaystyle (\sigma_2+\tau_2)(|ud\rangle-|du\rangle)=0\) [transcript-backed]
- \(\displaystyle (\boldsymbol{\sigma}+\boldsymbol{\tau})\cdot \hat n\,|\psi_-\rangle=0\) [standard reconstruction]
- \(\displaystyle N(A,\neg B)+N(B,\neg C)\ge N(A,\neg C)\) [transcript-backed]
- \(\displaystyle P|\alpha\rangle=|\alpha_p\rangle\) [standard reconstruction]
- \(\displaystyle P_{\sigma_3=+1}\begin{pmatrix}\alpha\\ \beta\end{pmatrix}=\begin{pmatrix}\alpha\\ 0\end{pmatrix}\) [visible]
- \(\displaystyle P_{\sigma_3=-1}\begin{pmatrix}\alpha\\ \beta\end{pmatrix}=\begin{pmatrix}0\\ \beta\end{pmatrix}\) [visible]
- \(\displaystyle P_{\sigma_3=+1}=\begin{pmatrix}1&0\\0&0\end{pmatrix}=\frac{1+\sigma_3}{2}\) [transcript-backed]
- \(\displaystyle P_{\sigma_1=+1}=\frac{1+\sigma_1}{2}\) [transcript-backed]
- \(\displaystyle P_{\sigma\cdot \hat n=+1}=\frac{1+\sigma\cdot \hat n}{2}\) [transcript-backed]
- \(\displaystyle \tau\cdot \hat n_{45}=\frac{\tau_1+\tau_3}{\sqrt2}\) [transcript-backed]
- \(\displaystyle \mathrm{Prob}(\alpha\text{ true in }|\psi\rangle)=\langle \psi|P_\alpha|\psi\rangle\) [transcript-backed]
- \(\displaystyle P_{A\wedge \neg B}=\frac{1+\sigma_3}{2}\,\frac{1+\tau\cdot \hat n_{45}}{2}\) [transcript-backed]
- \(\displaystyle P(A,\neg B)=\frac14\left(1-\frac1{\sqrt2}\right)\) [transcript-backed]
- \(\displaystyle P(B,\neg C)=\frac14\left(1-\frac1{\sqrt2}\right)\) [transcript-backed]
- \(\displaystyle P(A,\neg C)=\frac14\) [transcript-backed]
- \(\displaystyle P(A,\neg B)+P(B,\neg C)=\frac12\left(1-\frac1{\sqrt2}\right)<\frac14=P(A,\neg C)\) [transcript-backed]
- \(\displaystyle |a\rangle\to |a'\rangle,\quad |b\rangle\to |b'\rangle \;\Rightarrow\; \alpha|a\rangle+\beta|b\rangle\to \alpha|a'\rangle+\beta|b'\rangle\) [transcript-backed]
- \(\displaystyle |u\rangle\to |uu\rangle,\qquad |d\rangle\to |dd\rangle\) [transcript-backed]
- \(\displaystyle |r\rangle=\frac{|u\rangle+|d\rangle}{\sqrt2}\) [transcript-backed]
- \(\displaystyle |r\rangle \to \frac{|uu\rangle+|dd\rangle}{\sqrt2}\) [transcript-backed]
- \(\displaystyle |rr\rangle=\frac12\bigl(|uu\rangle+|ud\rangle+|du\rangle+|dd\rangle\bigr)\) [standard reconstruction]

## Definitions And Objects
- \(\sigma_i\): Pauli operators acting on the first electron.
- \(\tau_i\): identical Pauli-family operators acting on the second electron.
- \(|ud\rangle\): first spin up, second spin down; the lecture suppresses the tensor-product symbol.
- \(|\psi_-\rangle\): the minus-sign state, called the singlet state.
- \(|\psi_+\rangle\): the plus-sign state, called the triplet state in this lecture.
- “Spin up at \(0^\circ\)”: spin up along the third axis.
- “Spin up at \(45^\circ\)”: spin up in the \(zx\)-plane halfway between the 3-axis and 1-axis.
- “Spin up at \(90^\circ\)”: spin up along the 1-axis, again in the \(zx\)-plane.
- \(A\): statement that spin 1 is up at \(0^\circ\).
- \(B\): statement that spin 1 is up at \(45^\circ\).
- \(C\): statement that spin 1 is up at \(90^\circ\).
- In the singlet state, \(\neg B\) and \(\neg C\) are re-expressed as positive statements about spin 2 in the opposite-correlated direction.
- Projection operator \(P\): operator projecting a vector onto a chosen subspace.
- For this lecture, propositions are represented by projection operators onto spin-up eigenspaces.
- The “and” of two compatible propositions is represented by the product of their commuting projectors.
- Late remark: one-spin pure states form a two-parameter family; general two-spin pure states form a six-parameter family, while unentangled two-spin states would only span a four-parameter family. This is used only as a closing comment about the richness of entangled states.

## Derivation Steps
Expectation value of one spin vanishes
1. Choose the plus state because the minus case was already discussed earlier.
2. Form \(\langle ud+du|\sigma_3|ud+du\rangle\), ignoring the overall \(\sqrt2\) since only vanishing is being checked.
3. Act with \(\sigma_3\) on the first spin: \(|ud\rangle\mapsto |ud\rangle\), \(|du\rangle\mapsto -|du\rangle\).
4. Use orthogonality: \(\langle ud|du\rangle=\langle du|ud\rangle=0\).
5. The remaining diagonal terms give \(1-1=0\).
6. Conclude that the expectation value is zero, not that zero is a possible measurement outcome.

Distinguishing plus and minus with total spin
1. Apply \(\sigma_3+\tau_3\) to \(|ud\rangle\) and to \(|du\rangle\).
2. In each basis state the \(+1\) from the up spin cancels the \(-1\) from the down spin.
3. Therefore both \(|\psi_+\rangle\) and \(|\psi_-\rangle\) are eigenvectors of \(\sigma_3+\tau_3\) with eigenvalue \(0\).
4. Move to \(\sigma_1+\tau_1\), where \(\sigma_1\) and \(\tau_1\) flip \(u\leftrightarrow d\).
5. On \(|ud\rangle+|du\rangle\), the terms add and produce \(2|uu\rangle+2|dd\rangle\), so the plus state is not annihilated.
6. On \(|ud\rangle-|du\rangle\), the same terms cancel exactly, so the minus state is annihilated.
7. Repeat with \(\sigma_2+\tau_2\); the \(i\)-factors again cancel for the minus state.
8. Conclude that the minus state has total spin zero in every direction.

Classical Bell inequality
1. Start with a classical set of objects carrying three properties \(A,B,C\).
2. Count the objects in \(A\wedge \neg B\), in \(B\wedge \neg C\), and in \(A\wedge \neg C\).
3. Partition the set into disjoint subregions.
4. Observe that the counts for \(A\wedge \neg B\) and \(B\wedge \neg C\) together contain every object counted by \(A\wedge \neg C\), plus possibly extra positive contributions.
5. Since all subregion counts are nonnegative, obtain \(N(A,\neg B)+N(B,\neg C)\ge N(A,\neg C)\).

Projector identity for \(\sigma_3=+1\)
1. Ask what projection onto “spin up along the third axis” does to \(\binom{\alpha}{\beta}\).
2. It keeps the up component \(\alpha\) and removes the orthogonal down component \(\beta\).
3. Therefore \(P_{\sigma_3=+1}\binom{\alpha}{\beta}=\binom{\alpha}{0}\).
4. The matrix accomplishing that is \(\begin{pmatrix}1&0\\0&0\end{pmatrix}\).
5. Since \(\sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix}\), one checks directly that \(\frac{1+\sigma_3}{2}=\begin{pmatrix}1&0\\0&0\end{pmatrix}\).

Bell probability \(P(A,\neg B)\)
1. Use the singlet state \(|\psi_-\rangle=(|ud\rangle-|du\rangle)/\sqrt2\).
2. Write the projector for \(A\) as \((1+\sigma_3)/2\).
3. Re-express \(\neg B\) using the singlet correlation as “spin 2 is up at \(45^\circ\)”.
4. Write the second projector as \(\bigl(1+(\tau_1+\tau_3)/\sqrt2\bigr)/2\).
5. Apply \((1+\sigma_3)/2\) first; it kills the \(|du\rangle\) term and leaves the \(|ud\rangle\) term.
6. In the later inner product with \(\langle\psi_-|\), the \(\tau_1\) piece creates \(|uu\rangle\), which is orthogonal to both \(\langle ud|\) and \(\langle du|\), so it does not contribute.
7. The surviving scalar and \(\tau_3\) pieces give \(\frac14(1-1/\sqrt2)\).
8. By rotational invariance of the singlet, \(P(B,\neg C)=P(A,\neg B)\).

Bell probability \(P(A,\neg C)\)
1. Keep the same first projector \((1+\sigma_3)/2\).
2. Re-express \(\neg C\) as “spin 2 is up at \(90^\circ\)”, i.e. along the 1-axis.
3. Use the second projector \((1+\tau_1)/2\).
4. Again \((1+\sigma_3)/2\) kills the \(|du\rangle\) component of the singlet.
5. The \(\tau_1\) term sends \(|ud\rangle\) to \(|uu\rangle\), which is orthogonal to the singlet bra and drops out.
6. Only the scalar \(1/2\) piece survives.
7. The normalization factors then give \(P(A,\neg C)=1/4\).
8. Therefore the quantum probabilities violate the classical Bell inequality.

No-cloning from linearity
1. Assume a machine clones a chosen basis: \(|u\rangle\to |uu\rangle\) and \(|d\rangle\to |dd\rangle\).
2. Introduce the right-pointing state \(|r\rangle=(|u\rangle+|d\rangle)/\sqrt2\).
3. Apply linearity of time evolution to the input \(|r\rangle\).
4. The machine must then output \((|uu\rangle+|dd\rangle)/\sqrt2\).
5. Exact cloning would instead require \(|r\rangle\otimes |r\rangle=\frac12(|uu\rangle+|ud\rangle+|du\rangle+|dd\rangle)\).
6. These two outputs are different.
7. Therefore one machine cannot clone both the \(u/d\) basis and the \(r/l\) basis.
8. Conclude that no universal machine can clone an arbitrary unknown quantum state.

## Notation Choices
- Use \(|u\rangle, |d\rangle\) for \(\sigma_3\) eigenstates, matching the lecture’s board language.
- Use \(|ud\rangle\) as shorthand for \(|u\rangle_1\otimes |d\rangle_2\); define this once and then suppress the tensor symbol.
- Reserve \(\sigma_i\) for the first spin and \(\tau_i\) for the second throughout; do not switch to \(S_i^{(1)},S_i^{(2)}\).
- When summarizing the singlet compactly, \(|\psi_-\rangle\) is acceptable, but the lecture’s primary concrete form is \((|ud\rangle-|du\rangle)/\sqrt2\).
- Use “singlet” only for the minus state and “triplet” for the plus state in this chapter.
- Keep Susskind’s directional language but standardize it:
  \(0^\circ\to\) third axis,
  \(45^\circ\to\) \(zx\)-plane halfway between axes 3 and 1,
  \(90^\circ\to\) first axis.
- For the \(45^\circ\) unit vector, use \(\hat n_{45}=(\hat x+\hat z)/\sqrt2\).
- Write projectors as \(P_{\sigma_3=+1}\), \(P_{\sigma_1=+1}\), and \(P_{\sigma\cdot \hat n=+1}\); keep the \(+1\) explicit.
- Use \(P_\alpha\) for the projector associated with proposition \(\alpha\).
- When writing Bell probabilities, use \(P(A,\neg B)\) for the probability and \(P_{A\wedge \neg B}\) for the corresponding projector.
- For the no-cloning section, define \(|r\rangle\) explicitly; do not assume “right” is already established from previous lectures.
- If tensor products are shown in the cloning section, use them only once to clarify the composite-state construction, then return to the lecture’s juxtaposition notation.

## Uncertain Mathematics
- The chalk frame for the zero-expectation discussion does not fix the sign in \((|ud\rangle\pm|du\rangle)/\sqrt2\); the transcript shows that the explicit check at that moment is for the plus state.
- The lecture sometimes speaks loosely as if “the spin of \(\sigma_i\) is zero”; the final notes should state this as vanishing expectation value, not as an eigenvalue statement.
- In the Bell set-theory proof, the spoken region bookkeeping contains self-corrections; keep the final inequality, but do not overcommit to every intermediate region label unless you reconstruct the diagram cleanly.
- The Bell-angle narration briefly slips between planes; the final notes should standardize the setup to the \(zx\)-plane, which is what the later operator formulas require.
- The projector calculation around 01:06–01:08 is partially garbled; the clean result \(\frac14(1-1/\sqrt2)\) is stable, but some intermediate spoken coefficients should be treated as reconstructed.
- The decimal estimates \(0.075\), \(0.15\), and \(0.25\) are informal sanity checks only; preserve the exact algebraic expressions as primary.
- The generic notation \(P|\alpha\rangle=|\alpha_p\rangle\) is visually plausible and conceptually right, but the precise subscript on the projected ket is not fully legible in the frame.
- The late parameter-count remark about one-spin versus two-spin state spaces is transcript-backed but conversational; if used, it should be stated carefully as a pure-state parameter count modulo normalization and overall phase.
- The laser discussion is not developed mathematically enough to deserve a formal theorem in the chapter; at most it supports a cautious remark about approximate cloning and added noise.