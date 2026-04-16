# Math Bank
## Core Equations
- `[transcript-backed] \rho_A(A',A)=\sum_B \psi^*(A',B)\psi(A,B).`
- `[transcript-backed] \psi_M(b)=\sum_{b'} U_{bb'}\,\psi(b').`
- `[visible] \Psi_M(ab)=\sum_{b'} U_{bb'}\,\Psi(a b').`
- `[visible] \Psi_M^*(a' b)=\sum_{b''}\Psi^*(a' b'')\,U^\dagger_{b'' b}.`
- `[standard reconstruction] \Psi_M(a,b)=\sum_{b'} U_{bb'}\,\Psi(a,b').`
- `[standard reconstruction] \Psi_M^*(a',b)=\sum_{b''}\Psi^*(a',b'')\,U^\dagger_{b''b}.`
- `[transcript-backed] \rho_{A,M}(A',A)=\sum_b \Psi_M^*(A',b)\Psi_M(A,b).`
- `[transcript-backed] \sum_b U^\dagger_{b''b}U_{bb'}=\delta_{b''b'}.`
- `[transcript-backed] \rho_{A,M}(A',A)=\rho_A(A',A).`
- `[transcript-backed] |\alpha_u|^2+|\alpha_d|^2=1.`
- `[transcript-backed] P(+1)=|\alpha_u|^2,\qquad P(-1)=|\alpha_d|^2.`
- `[transcript-backed] \psi(x)=\langle x|\Psi\rangle.`
- `[transcript-backed] |\psi(x)|^2=\psi^*(x)\psi(x).`
- `[transcript-backed] \int dx\,\psi^*(x)\psi(x)=1.`
- `[transcript-backed] \langle x|x'\rangle=\delta(x-x').`
- `[transcript-backed] |\Psi\rangle=\int dx\,\psi(x)\,|x\rangle.`
- `[transcript-backed] \int dx'\,\delta(x-x')\,f(x')=f(x).`
- `[visible] \langle\psi|\phi\rangle=\sum_{q',q}\psi^*(q')\,\langle q'|\,\phi(q)\,|q\rangle.`
- `[standard reconstruction] \langle\psi|\phi\rangle=\sum_{a',a}\psi^*(a')\,\langle a'|a\rangle\,\phi(a)=\sum_a \psi^*(a)\phi(a).`
- `[transcript-backed] \langle\psi|\phi\rangle=\int dx\,\psi^*(x)\phi(x).`
- `[standard reconstruction] L=L^\dagger \iff \langle \phi|L|\psi\rangle=\langle \psi|L|\phi\rangle^*.`
- `[transcript-backed] \langle L\rangle_\psi=\langle \psi|L|\psi\rangle.`
- `[transcript-backed] (x\psi)(x)=x\,\psi(x).`
- `[transcript-backed] (D\psi)(x)=\dfrac{d\psi}{dx}.`
- `[transcript-backed] \int dx\,\phi^*(x)\,\dfrac{d\psi}{dx}=-\int dx\,\dfrac{d\phi^*}{dx}\,\psi(x)` assuming vanishing boundary terms.
- `[standard reconstruction] D^\dagger=-D.`
- `[transcript-backed] p=-i\,\dfrac{d}{dx}.`
- `[transcript-backed] \langle p\rangle_\psi=\int dx\,\psi^*(x)\left(-i\,\dfrac{d}{dx}\right)\psi(x)\in\mathbb{R}.`
- `[transcript-backed] [x,p]\psi(x)=i\,\psi(x).`
- `[transcript-backed] [x,p]=i.`
- `[transcript-backed] [x,p]=i\hbar` after restoring units.
- `[transcript-backed] \{x,p\}_{\mathrm{PB}}=1.`

## Definitions And Objects
- `\rho_A`: Alice’s reduced density matrix; depends only on Alice’s indices because Bob’s index has been summed out.
- Locality in this lecture: Bob cannot alter Alice’s local statistical predictions by manipulating only Bob’s subsystem.
- `U`: Bob’s unitary evolution/manipulation operator.
- `\Psi_M`: manipulated composite-state wavefunction after Bob acts locally.
- Bra rule: if `U` acts on ket coefficients, `U^\dagger` acts on the corresponding bra coefficients.
- Single-spin simulator state: two complex amplitudes `\alpha_u,\alpha_d` stored classically and updated in time.
- Simulator measurement rule: use a classical random-number generator with Born probabilities, then reset amplitudes to the measured eigenstate.
- Entangled two-spin simulator state: four complex amplitudes `\alpha_{uu},\alpha_{ud},\alpha_{du},\alpha_{dd}` stored centrally if full correlations are to be preserved.
- `|x\rangle`: position-basis ket, the state “particle located at position `x`.”
- `\psi(x)`: position-space wavefunction; both the projection `\langle x|\Psi\rangle` and the expansion coefficient in the continuous basis.
- `\delta(x-x')`: Dirac delta, the continuous analogue of the Kronecker delta.
- Functions as vectors: wavefunctions are treated as vectors in a vector space of functions.
- `M`: Susskind’s generic “machine” notation for a linear operator on states/wavefunctions.
- Hermitian operators: observables; operator analogue of real quantities.
- `x`: multiplication operator, later identified with position.
- `D=\dfrac{d}{dx}`: differentiation operator; linear but not Hermitian.
- `p=-i\,\dfrac{d}{dx}`: Hermitian operator introduced as momentum in units with `\hbar=1`.
- Square-integrable wavefunctions: the implicit class of states for which normalization and integration by parts make sense.

## Derivation Steps
Locality proof
1. Start from the manipulated reduced density matrix `\rho_{A,M}(A',A)=\sum_b \Psi_M^*(A',b)\Psi_M(A,b)`.
2. Insert Bob’s unitary action on the composite ket coefficients.
3. Insert the complex-conjugated bra-side coefficients with a separate dummy index `b''`.
4. Rewrite the complex-conjugated matrix element as the Hermitian-conjugate element `U^\dagger_{b''b}`.
5. Sum over the shared Bob index `b`.
6. Recognize the contraction `\sum_b U^\dagger_{b''b}U_{bb'}=(U^\dagger U)_{b''b'}`.
7. Use unitarity to replace that contraction by `\delta_{b''b'}`.
8. Use the delta to set `b''=b'`.
9. Rename the remaining dummy index back to `b`.
10. Recover the original `\rho_A(A',A)`.
11. Note the failure mode: without unitarity, the contraction would not become the identity.

Consistency of the continuous expansion
1. Guess `|\Psi\rangle=\int dx'\,\psi(x')\,|x'\rangle`.
2. Act on both sides with `\langle x|`.
3. Replace `\langle x|x'\rangle` by `\delta(x-x')`.
4. Get `\langle x|\Psi\rangle=\int dx'\,\psi(x')\,\delta(x-x')`.
5. Apply the delta-function sampling rule.
6. Recover `\langle x|\Psi\rangle=\psi(x)`.
7. Conclude that the coefficient in the expansion is the same object as the projected wavefunction.

Continuous inner product from the discrete pattern
1. Start from the discrete expression `\langle\psi|\phi\rangle=\sum_{a',a}\psi^*(a')\langle a'|a\rangle\phi(a)`.
2. Replace discrete labels by continuous labels `x',x`.
3. Replace sums by integrals.
4. Replace the Kronecker delta by `\delta(x-x')`.
5. Collapse one integral with the delta function.
6. Obtain `\langle\psi|\phi\rangle=\int dx\,\psi^*(x)\phi(x)`.

Hermiticity of the multiplication operator `x`
1. Let `x` act on a wavefunction by multiplication: `(x\psi)(x)=x\psi(x)`.
2. Write `\langle \phi|x\psi\rangle=\int dx\,\phi^*(x)\,x\,\psi(x)`.
3. Interchange `\phi` and `\psi` and complex-conjugate the result.
4. Use that `x` is real, so `x^*=x`.
5. Recover the same integral.
6. Conclude that the operator `x` is Hermitian.

Why `D=\dfrac{d}{dx}` is not Hermitian
1. Define `(D\psi)(x)=\dfrac{d\psi}{dx}`.
2. Compare `\langle \phi|D\psi\rangle` with `\langle D\phi|\psi\rangle^*`.
3. Rewrite the conjugated second expression as an integral containing `\psi\,\dfrac{d\phi^*}{dx}`.
4. Integrate by parts.
5. Assume the boundary term vanishes because the states fall off sufficiently fast.
6. Pick up a minus sign when shifting the derivative.
7. Find that the two sides differ by an overall minus sign.
8. Conclude that `D` is anti-Hermitian rather than Hermitian.

Why `p=-iD` is Hermitian
1. Replace `D` by `-iD` in the previous comparison.
2. Complex conjugation changes `-i` to `+i`.
3. Integration by parts still contributes a minus sign.
4. The conjugation sign flip and the integration-by-parts minus sign cancel.
5. The Hermitian condition now holds.
6. Rename the operator `p=-i\,\dfrac{d}{dx}`.

Reality of the momentum expectation value
1. Start from `\langle p\rangle_\psi=-i\int dx\,\psi^*(x)\dfrac{d\psi}{dx}`.
2. Integrate by parts.
3. Move the derivative onto `\psi^*`.
4. Pick up a minus sign from integration by parts.
5. Turn `-i` into `+i` in the transformed expression.
6. Recognize the transformed expression as the complex conjugate of the original one.
7. Since the transformed expression is equal to the original one, `\langle p\rangle_\psi` is real.

Commutator calculation
1. Compute `px\,\psi=-i\,\dfrac{d}{dx}(x\psi)`.
2. Use the product rule to get `px\,\psi=-i\,\psi-i\,x\,\dfrac{d\psi}{dx}`.
3. Compute `xp\,\psi=x\left(-i\,\dfrac{d\psi}{dx}\right)=-i\,x\,\dfrac{d\psi}{dx}`.
4. Form the commutator in the lecture’s order: `[x,p]\psi=xp\,\psi-px\,\psi`.
5. Cancel the common `-i\,x\,\dfrac{d\psi}{dx}` terms.
6. Get `[x,p]\psi=i\,\psi`.
7. Since this holds for arbitrary `\psi`, conclude `[x,p]=i`.
8. Reinsert units at the end to get `[x,p]=i\hbar`.

## Notation Choices
- Use uppercase `\Psi` for abstract or composite states when clarity benefits; use lowercase `\psi,\phi` for wavefunctions or basis coefficients.
- Use `A,B` or `a,b` for Alice/Bob subsystem indices; use `b',b''` exactly in the locality proof where the dummy-index bookkeeping matters.
- Use `x,x'` for the continuous position basis.
- Keep `q,q'` only when quoting figure 05 literally; otherwise prefer a generic discrete label such as `a,a'`.
- Standardize the board’s ambiguous matrix glyph to `U`.
- Use `\Psi_M` for the manipulated composite state after Bob’s local action.
- Write the reduced density matrix as `\rho_A(A',A)` to preserve the lecture’s matrix-index order.
- Restore full Dirac notation in cleaned equations even where the board omits a vertical bar.
- Default continuous integrals are over the whole line; write limits explicitly only where needed for emphasis.
- Use `D=\dfrac{d}{dx}` only as a temporary auxiliary operator; the observable carried forward is `p=-iD`.
- Take `\hbar=1` through the main derivations and only restore `\hbar` when Susskind explicitly comments on units.
- State the integration-by-parts assumption as “wavefunctions vanish sufficiently fast at infinity” or “square-integrable states with harmless boundary terms.”

## Uncertain Mathematics
- The lower-left side of the bra transformation in figures 02 and 03 is partly blocked; the clean formula should be marked as a cautious standard completion rather than a fully legible transcription.
- In figures 02 and 03, the board symbol can look like `L`; transcript and context strongly favor `U`.
- The subscript `M` on `\Psi_M` is weak in figure 02 and clearer in figure 03.
- Figure 05 visibly shows `q,q'` as indices, but the lecture elsewhere often uses more generic discrete labels; the chapter can standardize while noting that the screenshot uses `q,q'`.
- The figure-05 lower line omits or weakens a Dirac bar; the cleaned equation should restore `\langle q'|q\rangle`.
- The cropped top normalization formula in figure 05 is incomplete and should not be treated as a principal equation without transcript support.
- The transcript around the student question near `00:18:29–00:18:38` is corrupted; preserve the conceptual issue, not the exact wording.
- The transcript contains contamination around `01:12` and `01:17`; do not use those fragments as mathematical evidence.
- The continuous-basis discussion is intentionally heuristic; the notes should say plainly that the delta-function manipulations are physicist’s distributional shorthand.
- The integration-by-parts arguments for `D` and `p` implicitly assume boundary terms vanish; that hypothesis should be stated when the derivation is written cleanly.
- Susskind points toward identifying `p=-i\,d/dx` with momentum through later wave-packet dynamics; that physical identification is motivated here but not fully established in this lecture alone.