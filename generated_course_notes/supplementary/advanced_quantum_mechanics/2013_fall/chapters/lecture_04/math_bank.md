# Math Bank
## Core Equations
- [transcript-backed] Harmonic-oscillator Hamiltonian in Susskind’s \(m=1\) convention:
  \[
  H=\frac{1}{2}p^{2}+\frac{1}{2}\omega^{2}x^{2}.
  \]
- [transcript-backed] Ladder operators in the lecture normalization:
  \[
  a_{\pm}=\frac{p\pm i\omega x}{\sqrt{2\omega}}.
  \]
- [transcript-backed] Number operator:
  \[
  N=a_{+}a_{-}.
  \]
- [transcript-backed] Ladder-operator commutator:
  \[
  [a_{-},a_{+}]=1.
  \]
- [transcript-backed] Energy with dropped additive constant:
  \[
  H=\omega N.
  \]
- [transcript-backed] Energy with zero-point term restored:
  \[
  H=\omega\left(N+\frac{1}{2}\right).
  \]
- [transcript-backed] Ground-state annihilation condition:
  \[
  a_{-}\lvert 0\rangle=0.
  \]
- [transcript-backed] Consequent number-operator eigenvalue on the bottom state:
  \[
  N\lvert 0\rangle=0.
  \]
- [transcript-backed] Position-space operator realization in \(\hbar=1\) convention:
  \[
  X\mapsto x,\qquad P\mapsto -i\,\frac{d}{dx}.
  \]
- [standard reconstruction] With \(\hbar\) restored in the momentum operator:
  \[
  P\mapsto -i\hbar\,\frac{d}{dx}.
  \]
- [transcript-backed] Time-independent Schrödinger equation for the oscillator:
  \[
  \left[-\frac{1}{2}\frac{d^{2}}{dx^{2}}+\frac{1}{2}\omega^{2}x^{2}\right]\psi(x)=E\,\psi(x).
  \]
- [transcript-backed] Square-integrability condition for admissible states:
  \[
  \int \psi^{*}(x)\psi(x)\,dx=1.
  \]
- [transcript-backed] Lowering-operator equation for the ground state:
  \[
  (p-i\omega x)\psi_{0}(x)=0.
  \]
- [transcript-backed] After substituting \(p=-i\,d/dx\):
  \[
  \left(\frac{d}{dx}+\omega x\right)\psi_{0}(x)=0.
  \]
- [transcript-backed] Exponential ansatz for the ground state:
  \[
  \psi_{0}(x)=e^{f(x)}.
  \]
- [transcript-backed] Equation for the exponent:
  \[
  \frac{df}{dx}+\omega x=0.
  \]
- [transcript-backed] Solution for the exponent up to an additive constant:
  \[
  f(x)=-\frac{1}{2}\omega x^{2}+C.
  \]
- [transcript-backed] Ground-state wavefunction up to normalization:
  \[
  \psi_{0}(x)\propto e^{-\omega x^{2}/2}.
  \]
- [transcript-backed] Ground-state energy:
  \[
  E_{0}=\frac{\omega}{2}.
  \]
- [standard reconstruction] Normalized ground state in the lecture convention:
  \[
  \psi_{0}(x)=\left(\frac{\omega}{\pi}\right)^{1/4}e^{-\omega x^{2}/2}.
  \]
- [transcript-backed] First excited state from the raising operator:
  \[
  \psi_{1}(x)\propto a_{+}\psi_{0}(x).
  \]
- [transcript-backed] First excited state in position space:
  \[
  \psi_{1}(x)\propto \left(-i\frac{d}{dx}+i\omega x\right)e^{-\omega x^{2}/2}.
  \]
- [transcript-backed] Structural form of the first excited state:
  \[
  \psi_{1}(x)\propto x\,e^{-\omega x^{2}/2}.
  \]
- [standard reconstruction] Higher states in compact textbook form, only if needed later:
  \[
  \psi_{n}(x)\propto H_{n}(\sqrt{\omega}\,x)\,e^{-\omega x^{2}/2}.
  \]

- [transcript-backed] Angular-momentum commutator used to identify spin:
  \[
  [L_{z},L_{x}]=iL_{y},
  \]
  with cyclic permutations.
- [transcript-backed] Canonical Pauli matrices:
  \[
  \sigma_{z}=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
  \sigma_{x}=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
  \sigma_{y}=\begin{pmatrix}0&-i\\ i&0\end{pmatrix}.
  \]
- [visible] Matrix product used on the board:
  \[
  \begin{pmatrix}1&0\\0&-1\end{pmatrix}
  \begin{pmatrix}0&1\\1&0\end{pmatrix}
  =
  \begin{pmatrix}0&1\\-1&0\end{pmatrix}.
  \]
- [standard reconstruction] Corresponding identity:
  \[
  \sigma_{z}\sigma_{x}=i\sigma_{y}.
  \]
- [visible] Reverse-order matrix product, reconstructed from the board layout:
  \[
  \begin{pmatrix}0&1\\1&0\end{pmatrix}
  \begin{pmatrix}1&0\\0&-1\end{pmatrix}
  =
  \begin{pmatrix}0&-1\\1&0\end{pmatrix}.
  \]
- [standard reconstruction] Corresponding reverse-order identity:
  \[
  \sigma_{x}\sigma_{z}=-i\sigma_{y}.
  \]
- [transcript-backed] Pauli-matrix commutator:
  \[
  [\sigma_{z},\sigma_{x}]=2i\sigma_{y}.
  \]
- [visible] Spin-\(\tfrac12\) operators on the board:
  \[
  \frac{\sigma_{z}}{2}=\begin{pmatrix}\tfrac12&0\\0&-\tfrac12\end{pmatrix},\qquad
  \frac{\sigma_{x}}{2}=\begin{pmatrix}0&\tfrac12\\ \tfrac12&0\end{pmatrix},\qquad
  \frac{\sigma_{y}}{2}=\begin{pmatrix}0&-\tfrac{i}{2}\\ \tfrac{i}{2}&0\end{pmatrix}.
  \]
- [transcript-backed] Definition of spin operators:
  \[
  S_{i}=\frac{\sigma_{i}}{2}.
  \]
- [visible] Corrected spin commutator:
  \[
  [S_{z},S_{x}]=iS_{y},
  \]
  with cyclic permutations.
- [transcript-backed] Eigenvalues of \(S_{z}\):
  \[
  S_{z}\ \text{has eigenvalues}\ \pm \frac12.
  \]
- [visible] Total angular momentum:
  \[
  \mathbf{J}=\mathbf{L}+\mathbf{S}.
  \]

- [visible] Orbital-angular-momentum eigenvalue convention used on the board:
  \[
  L^{2}=\ell(\ell+1).
  \]
- [standard reconstruction] Fully restored units if needed outside the lecture convention:
  \[
  L^{2}=\hbar^{2}\ell(\ell+1).
  \]
- [visible] Orbital multiplicity:
  \[
  2\ell+1.
  \]
- [transcript-backed] Cumulative shell counts without spin in the idealized hydrogenic counting:
  \[
  1,\ 4,\ 9,\ 16,\ \dots = n^{2}.
  \]
- [standard reconstruction] Idealized shell counts with spin:
  \[
  2,\ 8,\ 18,\ 32,\ \dots = 2n^{2}.
  \]

- [transcript-backed] Two-particle wavefunction:
  \[
  \psi(x_{1},x_{2}).
  \]
- [transcript-backed] Swap action on the wavefunction:
  \[
  \psi(x_{1},x_{2})\longmapsto \psi(x_{2},x_{1}).
  \]
- [transcript-backed] Swap operator squared:
  \[
  S^{2}=1.
  \]
- [transcript-backed] Consequent swap eigenvalues:
  \[
  \lambda=\pm 1.
  \]
- [transcript-backed] Lecture stopping point for identical particles:
  \[
  S\psi=\psi
  \qquad \text{or} \qquad
  S\psi=-\psi.
  \]

## Definitions And Objects
- Harmonic oscillator:
  - \(m=1\) is chosen for convenience.
  - \(\omega\) is both the oscillator frequency and the spring-frequency scale in this convention.
- Ladder operators:
  - \(a_{+}\): raising operator.
  - \(a_{-}\): lowering operator.
- Number operator:
  - \(N=a_{+}a_{-}\).
  - Integer eigenvalues begin at \(0\).
- Ground state:
  - Bottom state of the oscillator tower.
  - Denoted abstractly by \(\lvert 0\rangle\).
  - Position-space wavefunction denoted \(\psi_{0}(x)\).
- First excited state:
  - Denoted \(\psi_{1}(x)\).
  - Built from \(a_{+}\psi_{0}\).
- Honest physical state in the wave-function picture:
  - Square-integrable wavefunction.
  - Normalizable probability density.
- Pauli matrices:
  - Three \(2\times 2\) Hermitian matrices associated with the \(x,y,z\) directions.
- Spin-\(\tfrac12\) operators:
  - \(S_{i}=\sigma_{i}/2\).
  - Two-state angular-momentum system.
- Orbital angular momentum:
  - \(\mathbf L = \mathbf R \times \mathbf P\).
  - In atomic problems it is naturally defined about the nucleus.
- Total angular momentum:
  - \(\mathbf J=\mathbf L+\mathbf S\).
- Hydrogenic orbital counting:
  - For fixed \(\ell\), there are \(2\ell+1\) orbital states.
  - The lecture uses a schematic \(E\)-versus-\(\ell\) degeneracy pattern.
- Two-particle wavefunction:
  - \(\psi(x_{1},x_{2})\) with \(x_{1},x_{2}\) labeling particle slots, not spatial directions.
- Swap operator:
  - Called \(S\) in the lecture.
  - Exchanges particle slots \(1\leftrightarrow 2\).

## Derivation Steps
1. Oscillator algebra to quantized spectrum
   1. Define \(a_{\pm}=(p\pm i\omega x)/\sqrt{2\omega}\).
   2. Compute the commutator \([a_{-},a_{+}]=1\).
   3. Define \(N=a_{+}a_{-}\).
   4. Use the commutator to show \(a_{+}\) and \(a_{-}\) raise and lower \(N\)-eigenvalues by one unit.
   5. Conclude that the allowed \(N\)-eigenvalues are nonnegative integers.
   6. Write \(H=\omega N\) after dropping the additive constant.
   7. Restore the quantum correction to get \(H=\omega(N+\tfrac12)\).

2. Existence of the ground state
   1. Observe that \(H\) is built from \(p^{2}+\omega^{2}x^{2}\).
   2. Conclude that the Hamiltonian cannot have negative eigenvalues.
   3. Therefore the ladder cannot descend indefinitely.
   4. A lowest state must exist.
   5. The only way a lowest state can avoid being lowered further is
      \[
      a_{-}\lvert 0\rangle=0.
      \]
   6. Apply \(N=a_{+}a_{-}\) to that state.
   7. Conclude
      \[
      N\lvert 0\rangle=0.
      \]

3. Position-space realization
   1. Replace abstract states by wavefunctions \(\psi(x)\).
   2. Replace \(X\) by multiplication by \(x\).
   3. Replace \(P\) by \(-i\,d/dx\).
   4. Impose square integrability as the condition for an admissible state.
   5. Write the time-independent Schrödinger equation
      \[
      \left[-\frac12\frac{d^{2}}{dx^{2}}+\frac12\omega^{2}x^{2}\right]\psi=E\psi.
      \]
   6. Note that generic \(E\) gives formal solutions, but most are not normalizable.
   7. Keep only the square-integrable solutions.

4. Ground-state wavefunction from the lowering operator
   1. Start from the ground-state condition
      \[
      a_{-}\psi_{0}=0.
      \]
   2. Drop irrelevant overall numerical factors in \(a_{-}\).
   3. Use
      \[
      a_{-}\propto p-i\omega x.
      \]
   4. Substitute \(p=-i\,d/dx\).
   5. Obtain the first-order equation
      \[
      \left(\frac{d}{dx}+\omega x\right)\psi_{0}(x)=0.
      \]
   6. Try the ansatz \(\psi_{0}(x)=e^{f(x)}\).
   7. Differentiate to get \(\psi_{0}'=f'e^{f}\).
   8. Factor out \(e^{f(x)}\).
   9. Reduce the problem to
      \[
      f'(x)+\omega x=0.
      \]
   10. Integrate to get
       \[
       f(x)=-\frac12\omega x^{2}+C.
       \]
   11. Hence
       \[
       \psi_{0}(x)\propto e^{-\omega x^{2}/2}.
       \]
   12. Use the earlier algebra to identify the energy as \(E_{0}=\omega/2\).

5. First excited state
   1. Start from the abstract statement
      \[
      \psi_{1}\propto a_{+}\psi_{0}.
      \]
   2. Use \(a_{+}\propto p+i\omega x\).
   3. Substitute \(p=-i\,d/dx\).
   4. Act on the Gaussian ground state.
   5. Reuse the earlier ground-state relation to avoid a fresh full derivative calculation.
   6. Conclude that only an \(x\)-factor remains up to an overall constant.
   7. Therefore
      \[
      \psi_{1}(x)\propto x\,e^{-\omega x^{2}/2}.
      \]
   8. Read off that \(\psi_{1}\) is odd and has a node at the origin.

6. Higher excited-state qualitative structure
   1. Repeated application of \(a_{+}\) produces polynomial factors multiplying the Gaussian.
   2. Each higher level adds one node.
   3. Parity alternates between symmetric and antisymmetric.
   4. Higher levels are pushed farther from the origin.
   5. More wiggles correspond to larger momentum content.
   6. Greater support at large \(|x|\) corresponds to more potential energy.

7. Pauli matrices to spin-\(\tfrac12\) angular momentum
   1. Write the angular-momentum commutator
      \[
      [L_{z},L_{x}]=iL_{y}.
      \]
   2. Write the Pauli matrices.
   3. Multiply \(\sigma_{z}\sigma_{x}\) explicitly.
   4. Identify the result as \(i\sigma_{y}\).
   5. Reverse the order and find \(\sigma_{x}\sigma_{z}=-i\sigma_{y}\).
   6. Subtract to obtain
      \[
      [\sigma_{z},\sigma_{x}]=2i\sigma_{y}.
      \]
   7. Observe the mismatch by a factor of \(2\).
   8. Define
      \[
      S_{i}=\frac{\sigma_{i}}{2}.
      \]
   9. Then recover the correct angular-momentum algebra
      \[
      [S_{z},S_{x}]=iS_{y}.
      \]

8. Spin-\(\tfrac12\) eigenvalues
   1. Take \(\sigma_{z}\) diagonal.
   2. Its eigenvalues are \(+1\) and \(-1\).
   3. Divide by \(2\) in the definition \(S_{z}=\sigma_{z}/2\).
   4. Conclude that the spin-\(\tfrac12\) \(z\)-component eigenvalues are
      \[
      \pm \frac12.
      \]

9. Hydrogenic shell counting as used in the lecture
   1. For each orbital angular momentum \(\ell\), count \(2\ell+1\) states.
   2. Use the schematic degeneracies: first \(\ell=1\) with second \(\ell=0\), first \(\ell=2\) with third \(\ell=0\), and so on.
   3. Count states level by level.
   4. Obtain cumulative totals
      \[
      1,\ 4,\ 9,\ 16,\dots
      \]
      before including spin.
   5. Double them in the idealized shell picture once spin is included.

10. Exchange operator and identical-particle statistics
   1. Describe two identical particles by \(\psi(x_{1},x_{2})\).
   2. Define the swap operator \(S\) by exchanging the particle slots.
   3. Therefore
      \[
      S:\psi(x_{1},x_{2})\mapsto \psi(x_{2},x_{1}).
      \]
   4. Swap twice.
   5. Conclude
      \[
      S^{2}=1.
      \]
   6. Use unitarity of state-space transformations.
   7. Infer that the eigenvalues of \(S\) are \(\pm1\).
   8. Reach the lecture’s stopping point: identical-particle states are classified by whether swapping gives the same wavefunction or its negative.

## Notation Choices
- Use \(\hbar=1\) for the main flow of this chapter section, because that is the lecture convention for most formulas.
- When needed, note explicitly where \(\hbar\) would be restored rather than silently mixing conventions.
- Use \(a_{+}\) and \(a_{-}\) as the lecture-faithful ladder-operator notation.
- Use \(N=a_{+}a_{-}\), with \(N\) uppercase for the operator.
- Use \(\lvert 0\rangle\) for the abstract ground state and \(\psi_{0}(x)\) for its position-space wavefunction.
- Use \(X,P\) for operators and \(x,p\) for c-number variables only when the distinction matters; the lecture tries to maintain this.
- Use \(\psi_{n}(x)\) for oscillator energy eigenfunctions.
- Use \(\sigma_{i}\) for Pauli matrices and \(S_{i}=\sigma_{i}/2\) for spin operators.
- Use boldface vectors for total angular momentum:
  \[
  \mathbf J=\mathbf L+\mathbf S.
  \]
- Typeset orbital angular momentum with \(\ell\), not handwritten \(l\).
- In the final notes, avoid overloading \(S\):
  - keep \(\mathbf S\) or \(S_{i}\) for spin,
  - rename the swap operator to \(P_{12}\), \(\mathcal P_{12}\), or \(\mathsf S_{\mathrm{swap}}\),
  - but note that the lecture itself calls the swap operator \(S\).
- For two-particle coordinates, keep \(x_{1},x_{2}\) and state explicitly that these label particle slots, not directions in space.
- Treat the hydrogen spectrum drawing as schematic: axis labels \(E\) and \(\ell\), but not to scale.

## Uncertain Mathematics
- The transcript around \(00{:}33{:}43\)–\(00{:}34{:}35\) is garbled.
- The statement “the first excited state has no nodes” should not be repeated; it conflicts with
  \[
  \psi_{1}(x)\propto x e^{-\omega x^{2}/2}
  \]
  and with the surrounding spoken logic. State cautiously that the intended meaning is one node at the origin.
- The compact higher-state polynomial formulas are not actually derived on the board in this lecture. If Hermite polynomials are mentioned later, mark them as a standard completion, not a directly lectured derivation.
- The lecture verbally oscillates between \(H=\omega N\) and \(H=\omega(N+\tfrac12)\). Preserve that as a deliberate distinction about dropping or keeping the additive constant.
- The precise locations of \(\hbar\) in the ladder operators are not written cleanly in the transcript. Any fully restored \(\hbar\)-dependent formulas should be treated as standard reconstruction.
- The board confirms the spin commutator structure, but the faint intermediate denominator in the top-right of the spin frame is not fully legible. The clean statement
  \[
  [S_{z},S_{x}]=iS_{y}
  \]
  is safe.
- The hydrogenic degeneracy sketch is schematic, not a quantitative spectrum. Preserve the degeneracy pattern and counting logic, not literal level spacing.
- The shell totals \(2,8,18,32,\dots\) are useful as idealized continuation, but the lecture itself warns that the many-electron shell picture breaks down quickly once electron-electron interactions matter.
- The lecture stops at
  \[
  S\psi=\pm\psi
  \]
  for identical particles. Do not include a full boson/fermion many-body formalism in this chapter unless a later prompt explicitly extends beyond the lecture stopping point.