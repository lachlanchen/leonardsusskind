# Math Bank
## Core Equations
- `\int dy\,\delta(y-a)=1` `[standard reconstruction]`
- `\delta(y-a)=0 \quad \text{for } y\neq a` `[transcript-backed]`
- `\int_{-L/2}^{L/2} dx\,e^{ikx}=\begin{cases}L,&k=0\\0,&k\neq 0\end{cases}` `[transcript-backed]`
- `k_n=\dfrac{2\pi n}{L}` `[transcript-backed]`
- `\Delta k=\dfrac{2\pi}{L}` `[transcript-backed]`
- `\int_{-\infty}^{\infty} dx\,e^{ikx}=2\pi\,\delta(k)` `[transcript-backed]`
- `\int_{-\infty}^{\infty} dk\,e^{ikx}=2\pi\,\delta(x)` `[transcript-backed]`
- `\langle m|n\rangle=\delta_{mn}` `[transcript-backed]`
- `a^\dagger|n\rangle=\sqrt{n+1}\,|n+1\rangle` `[transcript-backed]`
- `a|n\rangle=\sqrt{n}\,|n-1\rangle` `[transcript-backed]`
- `\langle n|a^\dagger=\sqrt{n}\,\langle n-1|` `[transcript-backed]`
- `\langle n|a=\sqrt{n+1}\,\langle n+1|` `[transcript-backed]`
- `\langle n|a^\dagger a|n\rangle=n` `[transcript-backed]`
- `\hbar=1` `[visible]`
- `\vec p=\vec k` `[visible]`
- `E=\hbar\omega` `[visible]`
- `p=\hbar k` `[visible]`
- `E=\omega` `[transcript-backed]`
- `p=k` `[transcript-backed]`
- `\psi(x)=\sum_k a^\dagger(k)e^{-ikx}` `[transcript-backed]`
- `\psi^\dagger(x)=\sum_k a(k)e^{ikx}` `[transcript-backed]`
- `\psi(x,t)=\sum_k a^\dagger(k)e^{-ikx}e^{i\omega(k)t}` `[standard reconstruction]`
- `\psi^\dagger(x,t)=\sum_k a(k)e^{ikx}e^{-i\omega(k)t}` `[standard reconstruction]`
- `\omega(k)=\dfrac{k^2}{2m}` `[transcript-backed]`
- `\dot{\psi}(x,t)=\sum_k i\omega(k)\,a^\dagger(k)e^{-ikx}e^{i\omega(k)t}` `[standard reconstruction]`
- `\partial_x\psi(x,t)=\sum_k (-ik)\,a^\dagger(k)e^{-ikx}e^{i\omega(k)t}` `[standard reconstruction]`
- `\partial_x^2\psi(x,t)=\sum_k (-k^2)\,a^\dagger(k)e^{-ikx}e^{i\omega(k)t}` `[standard reconstruction]`
- `-i\dot{\psi}=\dfrac{1}{2m}\dfrac{\partial^2\psi}{\partial x^2}` `[visible]`
- `i\dot{\psi}=-\dfrac{1}{2m}\dfrac{\partial^2\psi}{\partial x^2}` `[standard reconstruction]`
- `\mathcal A_{i\to f}\propto \left\langle k_f\left|\,g\int dt\,\psi^\dagger(0,t)\psi(0,t)\,\right|k_i\right\rangle` `[standard reconstruction]`
- `\psi(0,t)=\sum_k a(k)e^{-i\omega(k)t}` `[transcript-backed]`
- `\psi^\dagger(0,t)=\sum_\ell a^\dagger(\ell)e^{i\omega(\ell)t}` `[transcript-backed]`
- `\mathcal A_{i\to f}\propto g\int dt\,e^{i(\omega_f-\omega_i)t}` `[transcript-backed]`
- `\mathcal A_{i\to f}\propto 2\pi g\,\delta(\omega_f-\omega_i)` `[transcript-backed]`
- `|\mathcal A_{i\to f}|^2\propto 4\pi^2 g^2` `[transcript-backed]`
- `\mathcal A(x_{\text{target}})\propto e^{i(k_i-k_f)x_{\text{target}}}` `[transcript-backed]`
- `\psi\to e^{i\alpha}\psi` `[transcript-backed]`
- `\psi^\dagger\to e^{-i\alpha}\psi^\dagger` `[transcript-backed]`
- `\psi^\dagger\psi` is phase-invariant `[transcript-backed]`
- `\psi^\dagger\psi^\dagger\psi\psi` is phase-invariant `[transcript-backed]`
- `\psi^\dagger\psi^\dagger\psi` is not phase-invariant `[transcript-backed]`
- `\psi+\psi^\dagger` is not phase-invariant `[transcript-backed]`

## Definitions And Objects
- Dirac delta function: the limit of a lump-like function whose width goes to zero while the area stays fixed at `1`, localized where its argument vanishes.
- Discrete delta `\delta_{mn}`: the discrete analog of the Dirac delta, equal to `1` for `m=n` and `0` otherwise.
- Ket vectors: used here for initial states.
- Bra vectors: used here for final states.
- Inner product: bra-ket pairing that produces a number.
- Creation and annihilation operators: harmonic-oscillator operators used as the building blocks of the field.
- Simple field: one spatial coordinate `x` in the lecture derivation, with straightforward extension to three spatial dimensions.
- Conjugate field: Hermitian or complex conjugate field built from the opposite operator type and opposite phase factors.
- Operator-valued field: unlike the elementary one-particle wavefunction, `\psi` here acts on Fock-space states and changes particle occupation numbers.
- Coupling constant `g`: numerical measure of interaction strength in the fixed-target model.
- Fixed target model: target pinned at `x=0`, no recoil included in the mathematical description.
- Scattering amplitude: bra-operator-ket number whose modulus squared gives the probability.
- Time-translation symmetry in this lecture: “no special time” implemented by integrating over all times.
- Phase invariance in this lecture: invariance under a global constant phase redefinition of the field.

## Derivation Steps
Dirac delta from the periodic Fourier integral
1. Start with the periodic mode `e^{ikx}` on a circle of length `L`.
2. Restrict `k` to allowed values `k_n=2\pi n/L`.
3. Integrate over one full period, conveniently `x\in[-L/2,L/2]`.
4. For `k=0`, the integral gives `L`.
5. For `k\neq 0`, the oscillations cancel and the integral gives `0`.
6. View the result as a function of discrete `k`: height `L` at `k=0`, width `2\pi/L`.
7. The area is `L\cdot 2\pi/L=2\pi`.
8. In the large-`L` limit, identify this spike with `2\pi\delta(k)`.
9. By symmetry of `e^{ikx}`, infer `\int dk\,e^{ikx}=2\pi\delta(x)`.

Bra action of `a^\dagger` and `a`
1. Demand that operator action on bras be defined so that bra-ket numerical results match the corresponding action on kets.
2. Compute `\langle n|a^\dagger|m\rangle` by letting `a^\dagger` act on `|m\rangle`.
3. Since `a^\dagger|m\rangle=\sqrt{m+1}|m+1\rangle`, the matrix element is nonzero only when `n=m+1`.
4. Therefore the left action of `a^\dagger` must lower the bra index: `\langle n|a^\dagger=\sqrt{n}\langle n-1|`.
5. By the same logic, the left action of `a` must raise the bra index: `\langle n|a=\sqrt{n+1}\langle n+1|`.
6. This makes left-acting and right-acting computations agree.

Check of `\langle n|a^\dagger a|n\rangle`
1. Let `a` act rightward: `a|n\rangle=\sqrt{n}|n-1\rangle`.
2. Let `a^\dagger` act on the result: `a^\dagger|n-1\rangle=\sqrt{n}|n\rangle`.
3. Multiply the factors to get `n|n\rangle`.
4. Use `\langle n|n\rangle=1` to obtain `n`.
5. Repeat from the left: `\langle n|a^\dagger=\sqrt{n}\langle n-1|`.
6. Then `\langle n-1|a=\sqrt{n}\langle n|`.
7. Again obtain `n\langle n|n\rangle=n`.

Field equation from the dispersion relation
1. Write the time-dependent field as a mode sum with factor `e^{-ikx}e^{i\omega(k)t}`.
2. Differentiate with respect to time to pull down `i\omega(k)`.
3. Differentiate once with respect to space to pull down `-ik`.
4. Observe that one spatial derivative cannot match the time derivative because `\omega` is proportional to `k^2`, not `k`.
5. Differentiate a second time with respect to space to pull down `-k^2`.
6. Use the nonrelativistic relation `\omega(k)=k^2/(2m)`.
7. Replace `-k^2` by `-2m\,\omega(k)` inside the sum.
8. Compare the resulting expression with `\dot\psi`.
9. Rearrange the factor of `i` to get `-i\dot\psi=(1/2m)\partial_x^2\psi`.
10. Note the equivalent standard form `i\dot\psi=-(1/2m)\partial_x^2\psi`.

Fixed-target amplitude and energy conservation
1. Model scattering as annihilation of the incoming particle at `x=0` and immediate recreation at the same point.
2. Assume the event can occur at any time, so integrate over all `t`.
3. Insert the coupling constant `g` to measure interaction strength.
4. Project the resulting final state onto the one-particle final bra `\langle k_f|`.
5. Expand `\psi(0,t)` and `\psi^\dagger(0,t)` in momentum modes.
6. At `x=0`, the spatial exponentials drop out.
7. Only the `k=k_i` term in the annihilation sum survives on the initial state.
8. Only the `\ell=k_f` term in the creation sum survives on the final bra.
9. The operator algebra reduces to vacuum overlap `1`.
10. The amplitude becomes `g\int dt\,e^{i(\omega_f-\omega_i)t}`.
11. Evaluate the time integral as `2\pi\delta(\omega_f-\omega_i)`.
12. Read off energy conservation from the delta function.
13. Square the amplitude only schematically, retaining the proportionality to `4\pi^2 g^2`.

Target displacement and broken energy conservation
1. Move the target from `x=0` to `x=x_{\text{target}}`.
2. Restore the spatial exponentials in the amplitude.
3. Obtain an extra phase `e^{i(k_i-k_f)x_{\text{target}}}`.
4. On taking modulus squared, this pure phase cancels.
5. Conclude that target position affects the amplitude phase but not the probability.
6. If the target position becomes time-dependent, the time structure changes.
7. Then the simple energy-conserving delta function no longer follows.

Charge conservation from phase invariance
1. Consider interaction monomials built from `\psi` and `\psi^\dagger`.
2. Apply the global phase transformation `\psi\to e^{i\alpha}\psi`, `\psi^\dagger\to e^{-i\alpha}\psi^\dagger`.
3. Count the net phase factor of each monomial.
4. Equal numbers of `\psi` and `\psi^\dagger` give total phase `1`.
5. Unequal numbers give a nontrivial phase.
6. Use invariance under this phase change as the structural diagnostic of charge conservation.
7. Interpret the counting rule physically: each `\psi` annihilates one electron, each `\psi^\dagger` creates one electron.

## Notation Choices
- Use lowercase `p` for momentum in the notes, even though the board glyph can look like uppercase `P`.
- Use `a^\dagger` and `a` in clean notes; mention once that the board writes `a^+` and `a^-`.
- Use `\psi^\dagger` for the conjugate field throughout the chapter; avoid switching between `\psi^*` and `\psi^\dagger` except when explicitly discussing the lecture’s wording.
- Keep the lecture’s nonrelativistic time dependence during the derivation: `e^{-ikx}e^{+i\omega t}` for the displayed mode used on the board.
- Use `\dot\psi` when mirroring the board discussion, but typeset the final equation with `\partial_t\psi` or `\dot\psi` consistently, not both in the same displayed formula.
- Use one-dimensional `x` and `k` in the main derivation; add only a brief note that the lecture says the extension to three dimensions is straightforward.
- Use `k_i`, `k_f`, `\omega_i`, `\omega_f` for initial and final one-particle labels in the scattering section.
- Use `\mathcal A_{i\to f}` for the scattering amplitude and reserve “probability” for `|\mathcal A|^2`.
- In the process section, adopt the consistent convention `\psi` annihilates and `\psi^\dagger` creates, since this matches the fixed-target amplitude and the charge-counting discussion; note once that the lecture momentarily wobbles on this assignment.
- Use proportionality `\propto` rather than full equality in the scattering formulas unless all normalization factors are explicitly tracked.

## Uncertain Mathematics
- The explicit `dy` in `\int dy\,\delta(y-a)` is not visible in the frame; include it only as cautious completion.
- The transcript is garbled around the field-definition discussion near `00:35:14-00:35:45`; do not invent missing normalization factors or additional terms there.
- The lecture’s naming of `\psi` versus `\psi^\dagger` is unstable in the scattering setup; the final notes must pick one convention and announce it rather than pretending the chalk notation is fully stable.
- The field mode expansion shown on the board is partial; the clean formulas for `\psi(x,t)` and `\psi^\dagger(x,t)` are reconstructions from transcript plus later board state, not exact pixel transcription.
- The sign discussion in the Schrödinger-equation derivation is live and slightly messy; preserve the derivational tension, but print only a consistent final equation.
- The exact normalization of one-particle states and mode sums is not fully tracked in the lecture; do not silently import relativistic normalization factors such as `1/\sqrt{2\omega_k}`.
- The scattering amplitude should be stated up to proportionality unless the omitted normalization conventions are fixed elsewhere in the chapter.
- The treatment of `\delta(\omega_f-\omega_i)^2` is informal; the notes should preserve the conservation-law message and `g^2` scaling without presenting a rigorous distributional analysis.
- The “if `\omega=k` then `\dot\psi=-\partial_x\psi`” comparison is a pedagogical side case, not part of the main nonrelativistic derivation.
- The examples of allowed and forbidden operator monomials around `01:33` are partly corrupted in the transcript; use only the stable rule that equal numbers of `\psi` and `\psi^\dagger` are phase-invariant.