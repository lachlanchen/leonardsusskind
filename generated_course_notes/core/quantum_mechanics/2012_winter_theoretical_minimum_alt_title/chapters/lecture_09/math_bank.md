# Math Bank
## Core Equations
- [transcript-backed] `\psi(x)=\int \frac{dp}{\sqrt{2\pi}}\,\widetilde{\psi}(p)\,e^{ipx}`
- [transcript-backed] `\widetilde{\psi}(p)=\int \frac{dx}{\sqrt{2\pi}}\,\psi(x)\,e^{-ipx}`
- [visible] `\int dx\,F(x)\,\delta(x-x')=F(x')`
- [transcript-backed] `f(x)\,\delta(x-x')=f(x')\,\delta(x-x')`
- [transcript-backed] `\int dx\,\delta(x-x')=1`
- [transcript-backed] `\int dx\,\delta(x-x')\,f(x)=f(x')`
- [visible] `\psi(x')=\int dx\left[\int \frac{dp}{2\pi}e^{ip(x'-x)}\right]\psi(x)`
- [standard reconstruction] `\int \frac{dp}{2\pi}\,e^{ip(x'-x)}=\delta(x'-x)`
- [transcript-backed] `\int \frac{dx}{2\pi}\,e^{ix(p-p')}=\delta(p-p')`
- [transcript-backed] `|\psi\rangle=\int dx\,\psi(x)\,|x\rangle`
- [transcript-backed] `\psi(x)=\langle x|\psi\rangle`
- [transcript-backed] `\langle x'|x\rangle=\delta(x-x')`
- [transcript-backed] `\langle \Psi|\Phi\rangle=\int dx\,\psi^*(x)\phi(x)`
- [transcript-backed] `\int dx\,|\psi(x)|^2=1`
- [visible] `(X\psi)(x)=x\,\psi(x)`
- [transcript-backed] `X\,\delta(x-x_0)=x_0\,\delta(x-x_0)`
- [visible] `P=-i\hbar D`
- [standard reconstruction] `P=-i\hbar\,\frac{d}{dx}`
- [visible] `(P\psi)(x)=-i\hbar\,\frac{d\psi}{dx}`
- [transcript-backed] `-i\hbar\,\frac{d\psi}{dx}=p_0\,\psi`
- [transcript-backed] `\psi_{p_0}(x)\propto e^{ip_0x/\hbar}`
- [standard reconstruction] `\psi_p(x)=\frac{1}{\sqrt{2\pi\hbar}}\,e^{ipx/\hbar}`
- [transcript-backed] `\frac{p_0}{\hbar}\lambda=2\pi`
- [transcript-backed] `\lambda=\frac{2\pi\hbar}{p_0}`
- [transcript-backed] `\langle p'|p\rangle=\delta(p-p')`
- [standard reconstruction] `\langle p'|p\rangle=\int dx\,\psi_{p'}^*(x)\psi_p(x)`
- [standard reconstruction] `\psi_p(x)=\frac{1}{\sqrt{2\pi}}e^{ipx}` after the lecture sets `\hbar=1`
- [transcript-backed] `\widetilde{\psi}(p)=\langle p|\psi\rangle`
- [transcript-backed] `\widetilde{\psi}(p)=\int \frac{dx}{\sqrt{2\pi}}\,e^{-ipx}\psi(x)` in the `\hbar=1` convention used later
- [transcript-backed] `|\widetilde{\psi}(p)|^2` is the momentum-space probability density
- [transcript-backed] `X=+i\hbar\,\frac{d}{dp}` in momentum space
- [transcript-backed] `X=+i\,\frac{d}{dp}` after setting `\hbar=1`
- [transcript-backed] `i\hbar\,\frac{\partial \psi}{\partial t}=H\psi`
- [transcript-backed] `H=cP`
- [transcript-backed] `i\hbar\,\frac{\partial\psi}{\partial t}=c\left(-i\hbar\frac{\partial}{\partial x}\right)\psi`
- [transcript-backed] `\frac{\partial\psi}{\partial t}=-c\,\frac{\partial\psi}{\partial x}`
- [transcript-backed] `\psi(x,t)=f(x-ct)`
- [transcript-backed] `H=\frac{P^2}{2m}`
- [transcript-backed] `i\hbar\,\frac{\partial\psi}{\partial t}=\frac{1}{2m}\left(-i\hbar\frac{\partial}{\partial x}\right)^2\psi`
- [transcript-backed] `i\hbar\,\frac{\partial\psi}{\partial t}=-\frac{\hbar^2}{2m}\,\frac{\partial^2\psi}{\partial x^2}`

## Definitions And Objects
- `e^{ipx}`: plane wave; initially a mathematical wave-like factor, not yet a physical momentum eigenfunction.
- `\psi(x)`: wavefunction in the position basis; coefficient of `|x\rangle` in the continuous basis expansion.
- `\widetilde{\psi}(p)`: wavefunction in the momentum basis; also the Fourier transform of `\psi(x)`.
- `\delta(x-x')`: Dirac delta; used both as a sampling operation and as the continuum analog of the Kronecker delta.
- `|x\rangle`: generalized eigenvector of position with definite position `x`.
- `|p\rangle`: generalized eigenvector of momentum with definite momentum `p`.
- `X`: position operator; acts by multiplication in the `x`-representation.
- `P`: momentum operator; acts by differentiation in the `x`-representation.
- `D`: derivative operator from the previous lecture; here `P=-i\hbar D`.
- `\psi_p(x)`: position-space representative of a momentum eigenstate; distinct from the momentum-basis wavefunction `\widetilde{\psi}(p)`.
- `\lambda`: wavelength associated with a momentum eigenfunction.
- `H`: Hamiltonian operator; generator of time evolution and quantum analog of energy.
- `c`: constant used in the toy Hamiltonian `H=cP`; chosen suggestively as the speed of light.
- `m`: mass in the free-particle Hamiltonian `H=P^2/2m`.

## Derivation Steps
Fourier pair to delta kernel
1. Start from `\psi(x')=\int \frac{dp}{\sqrt{2\pi}}\widetilde{\psi}(p)e^{ipx'}`.
2. Substitute `\widetilde{\psi}(p)=\int \frac{dx}{\sqrt{2\pi}}\psi(x)e^{-ipx}`.
3. Combine the two `1/\sqrt{2\pi}` factors into `1/2\pi`.
4. Combine exponentials into `e^{ip(x'-x)}`.
5. Interchange the `x` and `p` integrals.
6. Isolate the inner kernel `\int \frac{dp}{2\pi}e^{ip(x'-x)}`.
7. Observe that the resulting expression has the sampling property of a delta function.
8. Identify the kernel with `\delta(x'-x)`.

Position eigenfunction of `X`
1. Define the action `(X\psi)(x)=x\psi(x)`.
2. Guess that a state localized at `x_0` should be represented by `\delta(x-x_0)`.
3. Apply `X` to that function: `X\,\delta(x-x_0)=x\,\delta(x-x_0)`.
4. Use the delta-function property `x\,\delta(x-x_0)=x_0\,\delta(x-x_0)`.
5. Read off eigenvalue `x_0` and eigenfunction `\delta(x-x_0)`.

Momentum eigenfunction in position space
1. Define `P=-i\hbar\,d/dx`.
2. Write the eigenvalue equation `P\psi=p_0\psi`.
3. Rewrite it as `-i\hbar\,d\psi/dx=p_0\psi`.
4. Move constants to get `d\psi/dx=(ip_0/\hbar)\psi`.
5. Solve the first-order ODE to obtain `\psi_{p_0}(x)\propto e^{ip_0x/\hbar}`.

Wavelength relation
1. Start from `\psi_{p_0}(x)\propto e^{ip_0x/\hbar}`.
2. Define the wavelength as the shift in `x` that changes the phase by `2\pi`.
3. Set `(p_0/\hbar)\lambda=2\pi`.
4. Conclude `\lambda=2\pi\hbar/p_0`.

Momentum-state normalization
1. Start from the unnormalized momentum eigenfunction `e^{ipx}` after setting `\hbar=1`.
2. Compute `\langle p'|p\rangle` using the position-space inner-product formula.
3. Obtain an oscillatory integral of the form `\int dx\,e^{i(p-p')x}`.
4. Compare it with the previously derived identity `\int \frac{dx}{2\pi}e^{ix(p-p')}=\delta(p-p')`.
5. Insert the factor `1/\sqrt{2\pi}` in each eigenfunction so the inner product becomes `\delta(p-p')`.

Momentum-basis wavefunction as Fourier transform
1. Define the momentum-space wavefunction by projection: `\widetilde{\psi}(p)=\langle p|\psi\rangle`.
2. Use the general inner-product formula in the position representation.
3. Insert the position-space representative of `|p\rangle`, namely `\psi_p(x)=e^{ipx}/\sqrt{2\pi}` in the `\hbar=1` convention.
4. Complex-conjugate that factor in the bra to get `e^{-ipx}/\sqrt{2\pi}`.
5. Multiply by `\psi(x)` and integrate over `x`.
6. Recognize the result as exactly the Fourier transform of `\psi(x)`.

`H=cP` Schrödinger equation
1. Start from `i\hbar\,\partial_t\psi=H\psi`.
2. Choose `H=cP`.
3. Replace `P` by `-i\hbar\,\partial_x`.
4. Cancel the common `i\hbar`.
5. Obtain `\partial_t\psi=-c\,\partial_x\psi`.
6. Recognize that any function of `x-ct` solves the equation.
7. Interpret the solution as rigid translation to the right with velocity `c`.

`H=P^2/2m` free-particle Schrödinger equation
1. Start from `i\hbar\,\partial_t\psi=H\psi`.
2. Choose `H=P^2/2m`.
3. Replace `P` by `-i\hbar\,\partial_x`.
4. Square the operator to get `(-i\hbar)^2\partial_x^2=-\hbar^2\partial_x^2`.
5. Obtain `i\hbar\,\partial_t\psi=-(\hbar^2/2m)\partial_x^2\psi`.
6. Note the qualitative consequence stated in the lecture: different wavelengths move differently, so a packet spreads.

## Notation Choices
- Use lowercase `x`, `p`, `x'`, `p'`, `x_0`, `p_0` for eigenvalues, integration variables, and definite measured values.
- Use uppercase `X`, `P`, `H`, `D` for operators.
- Write position-basis states as `|x\rangle` and momentum-basis states as `|p\rangle`.
- Use `\psi(x)` for the position-space wavefunction and `\widetilde{\psi}(p)` for the momentum-space wavefunction.
- Keep `\phi(x)` or `\Phi` only when a second arbitrary state is needed for inner products.
- Distinguish carefully:
  `\psi_p(x)` = position-space representative of a momentum eigenstate.
  `\widetilde{\psi}(p)` = momentum-basis wavefunction of an arbitrary state.
- Keep the lecture’s symmetric Fourier normalization `1/\sqrt{2\pi}`.
- Preserve the lecture’s temporary explicit `\hbar` in the operator and eigenfunction discussion, then explicitly announce when the lecture sets `\hbar=1`.
- For the final chapter, prefer one of two consistent policies:
  keep `\hbar` throughout and note the lecture’s later simplification, or
  switch to `\hbar=1` only after an explicit sentence marking that change.
- Use `\delta(x-x')` as the final standard symbol even if the board briefly uses a capital-delta-like temporary label.
- Use ordinary derivatives in one dimension: `d/dx` or `\partial/\partial x` only when time and space appear together; do not mix them carelessly.

## Uncertain Mathematics
- The board evidence for the full substituted Fourier expression in the `\psi(x')` derivation is partial; the complete nested integral should be treated as transcript-backed reconstruction.
- The sign in the Fourier kernel alternates between `x'-x` and `x-x'` during the lecture; the final notes should state that the delta function is even, so the distinction does not matter in the final identity.
- The board briefly names the kernel with a capital-delta-like symbol before identifying it with the Dirac delta; this should be presented as a temporary label, not a new object.
- The exact ket label in the `X|\cdot\rangle` screenshot is not secure from the image alone; only the operator-on-ket versus operator-on-wavefunction contrast is visually reliable.
- The second line of the momentum-operator frame is cropped; `(P\psi)(x)=-i\hbar\,d\psi/dx` is supported by the transcript rather than fully visible in the frame.
- The normalization of momentum eigenstates is heuristic in the lecture; the transcript explicitly admits that the oscillatory integrals are not rigorously convergent as written.
- The rigorous justification for `\langle p'|p\rangle=\delta(p-p')` should be stated cautiously: start from a finite interval or periodic box, normalize there, then take the infinite-volume limit.
- The transcript in the `H=cP` and especially `H=P^2/2m` sections is noisy and repetitive; the final notes should keep only the standard equations he lands on, not every intermediate false start.
- The lecture asks the reader to accept for now that the operator named `P` really is physical momentum; early in the chapter it should still be described as an observable that later earns that interpretation.