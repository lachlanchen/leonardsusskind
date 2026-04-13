# Math Bank
## Core Equations
- \(e^{ikL}=1\), hence \(kL=2\pi n\) and \(k=\dfrac{2\pi n}{L}\). `[transcript-backed]`
- \(k\lambda=2\pi\), hence \(k=\dfrac{2\pi}{\lambda}\). `[transcript-backed]`
- \(p=\hbar k\). `[transcript-backed]`
- \(n(k)\). `[visible]`
- \(a^{+}(k)\), \(a^{-}(k)\). `[visible]`
- \(a^{\dagger}(k)\,\big|\cdots,n(k),\cdots\big\rangle=\sqrt{n(k)+1}\,\big|\cdots,n(k)+1,\cdots\big\rangle\). `[standard reconstruction]`
- \(a(k)\,\big|\cdots,n(k),\cdots\big\rangle=\sqrt{n(k)}\,\big|\cdots,n(k)-1,\cdots\big\rangle\). `[standard reconstruction]`
- \(\psi(x)=\sum_k \alpha(k)e^{ikx}\). `[transcript-backed]`
- \(\psi^{*}(x)=\sum_k \alpha^{*}(k)e^{-ikx}\). `[transcript-backed]`
- \(\Psi(x)=\sum_k a(k)e^{ikx}\). `[visible]`
- \(\Psi^{\dagger}(x)=\sum_k a^{\dagger}(k)e^{-ikx}\). `[standard reconstruction]`
- \(a^{\dagger}(k)|0\rangle=|k\rangle\). `[standard reconstruction]`
- \(a(k)|0\rangle=0\). `[standard reconstruction]`
- \(\Psi(x)|0\rangle=0\). `[transcript-backed]`
- \(\Psi^{\dagger}(x)|0\rangle=\sum_k e^{-ikx}a^{\dagger}(k)|0\rangle=\sum_k e^{-ikx}|k\rangle\). `[visible]`
- \(a^{\dagger}(k_9)a(k_7)\,|k_7\rangle=|k_9\rangle\). `[transcript-backed]`
- \(a^{\dagger}(k_9)a^{\dagger}(k_{16})a(k_7)\,|k_7\rangle=|k_9,k_{16}\rangle\). `[transcript-backed]`
- \(\Psi^{\dagger}(x)\Psi^{\dagger}(x)\Psi(x)\,|k_{\mathrm{initial}}\rangle=\sum_{\ell,m}e^{i(k_{\mathrm{initial}}-\ell-m)x}\,|\ell,m\rangle\). `[standard reconstruction]`
- For the special channel \(\ell=m\), the second creation contributes a factor \(\sqrt{2}\). `[transcript-backed]`
- More generally, creating into an already occupied mode with occupation \(n_\ell\) contributes \(\sqrt{n_\ell+1}\). `[transcript-backed]`
- \([a^{\dagger}(k),a^{\dagger}(\ell)]=0\), \([a(k),a(\ell)]=0\). `[transcript-backed]`
- \([a(k),a^{\dagger}(\ell)]=\delta_{k\ell}\). `[transcript-backed]`
- \([A,B]=AB-BA\). `[transcript-backed]`
- \(\{A,B\}=AB+BA\). `[transcript-backed]`
- \(\int_0^L dx\,e^{i(\ell-k)x}=L\,\delta_{k\ell}\). `[transcript-backed]`
- \(\int_0^L dx\,\Psi^{\dagger}(x)\Psi(x)=L\sum_k a^{\dagger}(k)a(k)\). `[standard reconstruction]`
- \(\dfrac{1}{L}\int_0^L dx\,\Psi^{\dagger}(x)\Psi(x)=\sum_k a^{\dagger}(k)a(k)\equiv N\). `[standard reconstruction]`
- \(\Psi^{\dagger}(x)\Psi(x)\) is the particle-density operator. `[transcript-backed]`

## Definitions And Objects
- `Periodic space`: a circle of length \(L\), introduced as a finite-volume trick that preserves momentum.
- `Allowed mode`: a plane wave \(e^{ikx}\) with \(k=\dfrac{2\pi n}{L}\), where \(n\in\mathbb Z\).
- `Wave number versus momentum`: \(k\) is the wave number; \(p=\hbar k\), and in \(\hbar=1\) units Susskind informally treats them as the same.
- `Occupation number`: \(n(k)\), the number of quanta in the mode labeled by \(k\).
- `Fock-state label`: the full state is specified by the entire list of occupations \( \{\ldots,n(-2),n(-1),n(0),n(1),n(2),\ldots\}\).
- `Vacuum`: \(|0\rangle\), the normalized state with no particles; not the zero vector.
- `One-particle momentum state`: \(|k\rangle=a^{\dagger}(k)|0\rangle\).
- `Local field operators`: \(\Psi(x)\) annihilates a particle at position \(x\); \(\Psi^{\dagger}(x)\) creates one at position \(x\).
- `Classical Fourier coefficients`: \(\alpha(k)\), \(\alpha^{*}(k)\); in quantization these are replaced by operators.
- `Bosons`: particles described here by oscillator-like creation and annihilation operators and commutators, with Bose enhancement.
- `Fermion preview`: same general setup, but commutators are replaced by anticommutators, enforcing Pauli exclusion.

## Derivation Steps
Periodic quantization.
1. Start with a plane wave \(e^{ikx}\) on a circle of circumference \(L\).
2. Impose periodicity: the wave must return to the same value after one circuit, so \(e^{ikL}=1\).
3. Conclude \(kL=2\pi n\) for some integer \(n\).
4. Therefore \(k=\dfrac{2\pi n}{L}\).
5. Re-express this as wavelength quantization via \(k\lambda=2\pi\).

Quantum field from classical Fourier data.
1. Write the classical field as \(\psi(x)=\sum_k \alpha(k)e^{ikx}\).
2. Write its complex conjugate as \(\psi^*(x)=\sum_k \alpha^*(k)e^{-ikx}\).
3. Identify the Fourier coefficients as the classical quantities to be quantized.
4. Replace \(\alpha(k)\) by annihilation operators and \(\alpha^*(k)\) by creation operators.
5. Obtain the operator-valued field expansions \(\Psi(x)\) and \(\Psi^\dagger(x)\).

Position-state creation from the vacuum.
1. Begin with the vacuum \(|0\rangle\).
2. Act with \(\Psi^\dagger(x)=\sum_k a^\dagger(k)e^{-ikx}\).
3. Use \(a^\dagger(k)|0\rangle=|k\rangle\).
4. Get \(\Psi^\dagger(x)|0\rangle=\sum_k e^{-ikx}|k\rangle\).
5. Recognize the sum over momentum eigenstates with phases \(e^{-ikx}\) as a position eigenstate at \(x\).

Local \(1\to 2\) process.
1. Choose the local operator product \(\Psi^\dagger(x)\Psi^\dagger(x)\Psi(x)\).
2. Let the initial state be a one-particle momentum state \(|k_{\mathrm{initial}}\rangle\).
3. Expand \(\Psi(x)\) as a sum over annihilation operators and keep only the term that matches the occupied mode.
4. This leaves the vacuum times the phase \(e^{ik_{\mathrm{initial}}x}\).
5. Expand the two \(\Psi^\dagger(x)\) factors with distinct dummy indices \(\ell\) and \(m\).
6. The result is a two-particle superposition \(\sum_{\ell,m} e^{i(k_{\mathrm{initial}}-\ell-m)x}|\ell,m\rangle\).

Bose enhancement and stimulated emission.
1. In the local \(1\to2\) example, inspect separately the special case \(\ell=m\).
2. The first creation puts one particle into that mode.
3. The second creation acts on an already occupied mode and brings in \(\sqrt{2}\).
4. Therefore the equal-momentum channel carries an extra Bose factor.
5. In the decay example with a pre-existing particle in mode \(\ell\), the same mechanism yields \(\sqrt{n_\ell+1}\).
6. Squaring amplitudes gives the enhanced probability factor \(n_\ell+1\).

Number operator from the field.
1. Start from \(\int dx\,\Psi^\dagger(x)\Psi(x)\).
2. Substitute the Fourier expansions for \(\Psi^\dagger\) and \(\Psi\).
3. Collect the integral \(\int_0^L dx\,e^{i(\ell-k)x}\).
4. Use orthogonality to replace it by \(L\delta_{k\ell}\).
5. Collapse the double sum to \(L\sum_k a^\dagger(k)a(k)\).
6. Identify \(a^\dagger(k)a(k)\) as the occupation number in mode \(k\).
7. Conclude that, up to the explicit normalization convention, the integrated density counts total particle number.

## Notation Choices
- Use \(a^\dagger(k)\) and \(a(k)\) in the notes as the clean notation; mention once that the board often writes \(a^+(k)\), \(a^-(k)\).
- Use \(\Psi(x)\), \(\Psi^\dagger(x)\) for the quantum field operators.
- Use \(\psi(x)\), \(\psi^*(x)\) only for the classical field and its complex conjugate in the Fourier-coefficient discussion.
- Keep \(L\) for the spatial period / box size throughout.
- Keep \(k\) for wave number / momentum label, but explicitly remind the reader that \(k\) itself is not an integer; it is an integer multiple of \(2\pi/L\).
- Use bare \(n\in\mathbb Z\) only in \(k=\dfrac{2\pi n}{L}\); use \(n(k)\) for occupation number.
- When several summations appear together, use \(k_{\mathrm{initial}}\) for the fixed incoming momentum and \(\ell,m\) for dummy output indices.
- Use \(|0\rangle\) for the vacuum and reserve `zero vector` for the null vector in Hilbert space; do not blur them.
- Use \(|k\rangle\) for one-particle momentum states and \(|\ell,m\rangle\) for two-particle bosonic momentum states.
- Keep sums discrete until the infinite-volume limit is discussed; only then note the replacement \(\sum_k \to \int dk\).
- Keep the explicit factor of \(L\) in the number-operator discussion instead of silently renormalizing it away.

## Uncertain Mathematics
- The sign convention in the Fourier factors is unstable in the lecture. The working bank should adopt one consistent pair,
  \(\Psi(x)=\sum_k a(k)e^{ikx}\), \(\Psi^\dagger(x)=\sum_k a^\dagger(k)e^{-ikx}\),
  but the final notes should acknowledge that Susskind corrected himself on the fly.
- The identification \(\alpha(k)\leftrightarrow a(k)\), \(\alpha^*(k)\leftrightarrow a^\dagger(k)\) is eventually standardized, but he briefly flips the convention before settling it.
- The board supports \(a^\dagger(k)|0\rangle=|k\rangle\) conceptually, but that equality is inferred from the derivation layout rather than fully written as its own line.
- The local \(1\to2\) amplitude is safest as a standard reconstruction; the lecture clearly motivates the phase \(e^{i(k_{\mathrm{initial}}-\ell-m)x}\), but the exact displayed board form is only partly legible.
- The comparison between \(\ell=m\) and \(\ell\neq m\) channels should be stated carefully: the \(\sqrt{2}\) Bose factor is secure, but the full probability comparison is complicated by the fact that distinct \((\ell,m)\) channels appear in multiple orderings.
- The lecture’s normalization omits more standard factors such as \(1/\sqrt{L}\) or relativistic \(1/\sqrt{2\omega_k}\); do not import them unless the later chapter explicitly changes conventions.
- The photon examples are intentionally nonrelativistic simplifications. Do not infer a full relativistic Hamiltonian or exact energy-momentum-conserving QED vertex from these formulas.
- The relation between real/imaginary parts of \(\Psi\) and oscillator variables \(X,P\) is conceptually explicit but not stabilized as a single written formula; keep it explanatory rather than over-formalized.
- The fermion discussion is only a preview. The lecture clearly gives the anticommutator definition, but a full fermionic field expansion is not developed here and should not be invented.