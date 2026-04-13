# Math Bank
## Core Equations
- `|0\rangle \to |A\rangle + |B\rangle` `[transcript-backed]`
- `|A\rangle \to \sum_m \psi_m |m\rangle` `[visible]`
- `|B\rangle \to \sum_m \phi_m |m\rangle` `[visible]`
- `P_A(m)=\psi_m^*\psi_m` `[transcript-backed]`
- `P_B(m)=\phi_m^*\phi_m` `[transcript-backed]`
- `|A\rangle+|B\rangle \to \sum_n (\psi_n+\phi_n)|n\rangle` `[visible]`
- `P_m = |\psi_m+\phi_m|^2` `[transcript-backed]`
- `P_m=\psi_m^*\psi_m+\phi_m^*\phi_m+\psi_m^*\phi_m+\phi_m^*\psi_m` `[visible]`
- `\psi_m=\phi_m` at the symmetry point `[transcript-backed]`
- `\psi_m=-\phi_m \implies P_m=0` `[transcript-backed]`

- `|0,d\rangle \to |A,u\rangle + |B,d\rangle` `[transcript-backed]`
- `|A,u\rangle \to \sum_n \psi_n |n,u\rangle` `[standard reconstruction]`
- `|B,d\rangle \to \sum_n \phi_n |n,d\rangle` `[standard reconstruction]`
- `|\Psi_{\mathrm{final}}\rangle=\sum_n\big(\psi_n|n,u\rangle+\phi_n|n,d\rangle\big)` `[standard reconstruction]`
- `\Pi_m = |m,u\rangle\langle m,u| + |m,d\rangle\langle m,d|` `[visible]`
- `\langle u|d\rangle=0` `[transcript-backed]`
- `P_m=\langle \Psi_{\mathrm{final}}|\Pi_m|\Psi_{\mathrm{final}}\rangle = |\psi_m|^2+|\phi_m|^2` `[transcript-backed]`

- `P_m = |\psi_m|^2+|\phi_m|^2+\psi_m^*\phi_m\langle E_A|E_B\rangle+\phi_m^*\psi_m\langle E_B|E_A\rangle` `[standard reconstruction]`
- `\langle E_A|E_B\rangle=0` gives complete which-path loss of interference `[standard reconstruction]`
- `\langle E_A|E_B\rangle=1` gives full interference recovery `[standard reconstruction]`

- `|\Psi_{\mathrm{cat}}\rangle=\alpha\,|{\rm live},{\rm unfired}\rangle+\beta\,|{\rm dead},{\rm fired}\rangle` `[transcript-backed]`

- `S=\log n` for `n` equiprobable possibilities `[transcript-backed]`
- `p_i=\frac{1}{n}\ \text{for}\ i\in\mathcal N,\qquad p_i=0\ \text{for}\ i\notin\mathcal N` `[transcript-backed]`
- `S=-\sum_i p_i\log p_i` `[transcript-backed]`

- `\operatorname{Tr} M=\sum_i \langle i|M|i\rangle` `[transcript-backed]`
- `\sum_i |i\rangle\langle i| = I` `[transcript-backed]`
- `M\ \text{diagonal} \implies \operatorname{Tr}M=\sum_i \lambda_i` `[transcript-backed]`

- `\rho=\mathrm{diag}(\rho_1,\rho_2,\rho_3,\ldots)` `[transcript-backed]`
- `\operatorname{Tr}\rho=1` `[transcript-backed]`
- `\langle F\rangle=\operatorname{Tr}(F\rho)` `[transcript-backed]`
- `\operatorname{Tr}(F\rho)=\sum_{i,j}\langle i|F|j\rangle\langle j|\rho|i\rangle` `[transcript-backed]`
- `\rho\ \text{diagonal} \implies \operatorname{Tr}(F\rho)=\sum_i F_{ii}\rho_i` `[transcript-backed]`
- `\operatorname{Tr}(AB)=\operatorname{Tr}(BA)` `[transcript-backed]`

- `S=-\operatorname{Tr}(\rho\log\rho)` `[transcript-backed]`
- `\rho=\mathrm{diag}(\rho_1,\rho_2,\ldots)\implies \log\rho=\mathrm{diag}(\log\rho_1,\log\rho_2,\ldots)` `[transcript-backed]`
- `\rho\propto I \implies S=\log(\dim\mathcal H)` `[transcript-backed]`

## Definitions And Objects
- `|0\rangle`: source state, electron localized at the initial source site.
- `|A\rangle, |B\rangle`: slit states at the two open holes.
- `|m\rangle`: screen-position basis state; `m` denotes a specific screen site.
- `\psi_m`: amplitude to arrive at screen site `m` starting from slit `A`.
- `\phi_m`: amplitude to arrive at screen site `m` starting from slit `B`.
- `|u\rangle, |d\rangle`: auxiliary detector/apparatus spin states; in the first half of the lecture this is not the electron’s intrinsic spin.
- `|m,u\rangle, |m,d\rangle`: basis states in the tensor-product space of electron position on the screen and detector record state.
- `\Pi_m`: projector onto the subspace “electron is at screen point `m`,” irrespective of detector spin orientation.
- “Measurement” in this lecture: establishment of a correlation strong enough that the apparatus record can in principle distinguish the alternatives.
- “Mark left on the system”: any retained record that carries route information; this is the operational criterion for interference loss.
- Product state: an unentangled composite state in which each subsystem has its own definite state.
- Density matrix `\rho`: statistical description used when the system was prepared in one of several states but the actual state is unknown.
- Trace: quantum analog of summing over classical configurations.
- Entropy `S`: measure of ignorance in the classical discussion, then measure associated with a density matrix in the quantum discussion.

## Derivation Steps
Two-slit interference without detector:
1. Start from the schematic source evolution `|0\rangle \to |A\rangle+|B\rangle`.
2. Evolve each slit state separately: `|A\rangle \to \sum_m \psi_m|m\rangle`, `|B\rangle \to \sum_m \phi_m|m\rangle`.
3. At fixed screen site `m`, the total amplitude is `\psi_m+\phi_m`.
4. Form the probability by multiplying by the complex conjugate.
5. Expand to get two direct terms and two mixed terms.
6. Identify the mixed terms as the interference terms.
7. Use `\psi_m=\phi_m` and `\psi_m=-\phi_m` as the two simple symmetry checks.

Which-path detector and disappearance of cross terms:
1. Enlarge the state space from electron position alone to electron position times apparatus spin.
2. Take the initial state as electron at the source with apparatus untriggered: `|0,d\rangle`.
3. Correlate the slit alternatives with detector states: `A\leftrightarrow u`, `B\leftrightarrow d`.
4. Evolve the two branches separately to the screen basis.
5. Combine them into `|\Psi_{\mathrm{final}}\rangle=\sum_n(\psi_n|n,u\rangle+\phi_n|n,d\rangle)`.
6. Represent the property “electron is at `m`” by `\Pi_m=|m,u\rangle\langle m,u|+|m,d\rangle\langle m,d|`.
7. Compute `\langle \Psi_{\mathrm{final}}|\Pi_m|\Psi_{\mathrm{final}}\rangle`.
8. Keep only terms with matching screen index and matching spin label.
9. Use `\langle u|d\rangle=0` to kill the mixed `\psi\phi` terms.
10. Conclude `P_m=|\psi_m|^2+|\phi_m|^2`.

Partial which-path information:
1. Replace ideal detector states `|u\rangle,|d\rangle` by general record states `|E_A\rangle,|E_B\rangle`.
2. Repeat the same projection calculation.
3. Find that the mixed terms survive with coefficients `\langle E_A|E_B\rangle` and its conjugate.
4. Read full interference loss as orthogonality of record states.
5. Read partial interference loss as incomplete distinguishability.

Classical entropy from the equal-probability case:
1. Assume the system is known to lie in `n` equally likely states and nowhere else.
2. Assign `p_i=1/n` inside that subset and `p_i=0` outside it.
3. Insert this into `-\sum_i p_i\log p_i`.
4. Drop the outside contribution using the standard limit `p\log p\to 0` as `p\to 0`.
5. Sum the `n` identical inside contributions.
6. Recover `S=\log n`.

Expectation value as `\operatorname{Tr}(F\rho)`:
1. Define trace by summing diagonal matrix elements in a basis.
2. Choose a basis in which `\rho` is diagonal.
3. Write `\operatorname{Tr}(F\rho)` by closing the operator product with basis bras and kets.
4. Insert the identity `\sum_j |j\rangle\langle j|=I` between `F` and `\rho`.
5. Obtain a double sum over `i,j`.
6. Use diagonality of `\rho` to force `i=j`.
7. Identify the result as `\sum_i F_{ii}\rho_i`.
8. Read this as expectation values of `F` weighted by preparation probabilities.

Quantum entropy from diagonal `\rho`:
1. Start from `S=-\operatorname{Tr}(\rho\log\rho)`.
2. Go to a basis in which `\rho` is diagonal.
3. Replace `\log\rho` by the diagonal matrix of logarithms of eigenvalues.
4. Evaluate the trace as `-\sum_i \rho_i\log\rho_i`.
5. Check the pure case: one eigenvalue `1`, all others `0`, so `S=0`.
6. Check the maximally ignorant case: uniform eigenvalues, so `S=\log(\dim\mathcal H)`.

## Notation Choices
- Use kets throughout for the discrete two-slit setup: `|0\rangle`, `|A\rangle`, `|B\rangle`, `|m\rangle`.
- Preserve the lecture’s shorthand in the early state `|0\rangle \to |A\rangle+|B\rangle`; do not silently normalize it without comment.
- Use `m` for a fixed screen point under discussion and `n` for a dummy summation index.
- Use `\psi_m` and `\phi_m` exactly for the amplitudes from `A` and `B` to the screen.
- Use `u,d` rather than `\uparrow,\downarrow` in the detector formulas when matching the board notation: `|m,u\rangle`, `|m,d\rangle`.
- Treat the auxiliary spin as an apparatus degree of freedom, not the electron’s intrinsic spin, except when reporting Susskind’s remark that it could have been the electron’s spin.
- Use `\Pi_m` as the projector symbol in the notes even though the board mainly shows the dyadic sum without a named operator.
- Use `P_m` for total probability at screen site `m`.
- `P_A(m)` and `P_B(m)` are acceptable note-writing conveniences for one-hole-open cases, even though the lecture often leaves the route dependence verbal.
- In the entropy section, resolve the lecture’s overloaded `n` notation by using `\mathcal N` for the subset of allowed states and `n=|\mathcal N|` for its size.
- Use `M` for a generic matrix/operator in the trace discussion and `F` for the observable in the density-matrix expectation-value discussion.
- Use `\rho_i` for classical probabilities of basis-state preparation and `\rho` for the density matrix built from them.
- Keep `\log` unspecified unless a later document convention forces a base; the lecture does not fix the base consistently.
- For the cat example, use descriptive composite-state labels such as `|{\rm live},{\rm unfired}\rangle` rather than inventing opaque abbreviations.
- Reserve reduced-density-matrix notation for the next lecture unless absolutely needed for a transition sentence.

## Uncertain Mathematics
- The transcript is badly garbled around `00:01:54`–`00:02:26`; do not reconstruct equations from that stretch.
- The board evidence for `|A\rangle \to \sum_m \psi_m|m\rangle` and `|B\rangle \to \sum_m \phi_m|m\rangle` is strong, but the arrows and some indices are only partially visible; keep the final typesetting transcript-led.
- The compact final entangled screen state `\sum_n(\psi_n|n,u\rangle+\phi_n|n,d\rangle)` is a safe reconstruction from the lecture logic, but it is not preserved as a single clean board line.
- The partial-measurement overlap formula with `|E_A\rangle,|E_B\rangle` is not explicit lecture notation; include it only as a cautious organizing reconstruction.
- The recoil and emitted-photon discussions are qualitative; the lecture gives the orthogonality criterion, not a full dynamical model.
- The cat/gun example is schematic: coefficients are mentioned, but no normalization, relative phase, or operator model is developed.
- The entropy passage around `01:09`–`01:17` is partially garbled; keep only the stable results `S=\log n`, `S=-\sum_i p_i\log p_i`, and the equal-probability check.
- The trace discussion near `01:23` wanders into a muddled inverse/diagonal exchange; keep basis independence and “trace equals sum of eigenvalues” for diagonalizable/Hermitian operators, and omit the confused detour.
- The lecture does not yet derive a reduced density matrix for subsystem `A`; it only announces that this is where density matrices become useful for entanglement in the next lecture.
- The statement that “any real quantum mechanical state of the usual kind has zero entropy” refers here to pure-state entropy in the density-matrix sense and should be phrased carefully to avoid conflating intrinsic quantum uncertainty with statistical mixing.