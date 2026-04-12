# Math Bank

## Core Equations

- `[visible]` $\psi_+ = \dfrac{\psi_L+\psi_R}{\sqrt{2}}$
- `[transcript-backed]` $\psi_- = \dfrac{\psi_L-\psi_R}{\sqrt{2}}$
- `[standard reconstruction]` $H\psi_+ = (E_1-\epsilon)\psi_+$
- `[standard reconstruction]` $H\psi_- = (E_1+\epsilon)\psi_-$
- `[transcript-backed]` $\psi_L = \dfrac{\psi_+ + \psi_-}{\sqrt{2}}$
- `[transcript-backed]` $\psi_R = \dfrac{\psi_+ - \psi_-}{\sqrt{2}}$
- `[standard reconstruction]` $\psi(t)=\dfrac{1}{\sqrt{2}}\left(e^{-i(E_1-\epsilon)t}\psi_+ + e^{-i(E_1+\epsilon)t}\psi_-\right)$
- `[standard reconstruction]` $\psi(t)=e^{-iE_1 t}\left[\psi_L\cos(\epsilon t)+ i\,\psi_R\sin(\epsilon t)\right]$
- `[visible]` $e^{-i\epsilon t}=-e^{i\epsilon t}$
- `[visible]` $e^{2i\epsilon t}=-1$
- `[transcript-backed]` $2\epsilon t=\pi$
- `[standard reconstruction]` $t_{L\to R}=\dfrac{\pi}{2\epsilon}$
- `[transcript-backed]` $|L_x\rangle = \dfrac{|\uparrow_z\rangle+|\downarrow_z\rangle}{\sqrt{2}}$
- `[standard reconstruction]` $|R_x\rangle = \dfrac{|\uparrow_z\rangle-|\downarrow_z\rangle}{\sqrt{2}}$
- `[transcript-backed]` $\mathbf d = q\,\boldsymbol{\ell}$
- `[standard reconstruction]` $\mathbf d_e \parallel \boldsymbol{\mu}_e \quad$ or $\quad \mathbf d_e \parallel \mathbf S$
- `[standard reconstruction]` $P:\ \mathbf d_e\to -\mathbf d_e,\ \boldsymbol{\mu}_e\to \boldsymbol{\mu}_e$
- `[standard reconstruction]` $T:\ \mathbf d_e\to \mathbf d_e,\ \boldsymbol{\mu}_e\to -\boldsymbol{\mu}_e$
- `[standard reconstruction]` $(P\ \text{exact})\ \text{or}\ (T\ \text{exact}) \Rightarrow \mathbf d_e=0$
- `[transcript-backed]` $J=0 \Rightarrow$ rotationally invariant ground state
- `[transcript-backed]` $P(x)=|\psi(x)|^2,\qquad P(p)=|\tilde\psi(p)|^2$
- `[transcript-backed]` $\tilde{\psi}(p)=\int dx\,\psi(x)\,e^{-ipx}/\sqrt{2\pi}$
- `[transcript-backed]` $\psi(x)=\int dp\,\tilde{\psi}(p)\,e^{ipx}/\sqrt{2\pi}$
- `[transcript-backed]` $H=\dfrac{p^2}{2m}$
- `[transcript-backed]` $\psi_p(x)\propto e^{ipx}$
- `[transcript-backed]` $\Psi_-(x)=\sum_i a_i\,\psi_i(x)$
- `[standard reconstruction]` $\Psi_+(x)=\sum_i a_i^\dagger\,\psi_i^*(x)$
- `[standard reconstruction]` $\Psi_-(x)=\int dp\,a(p)\,e^{ipx}/\sqrt{2\pi}$
- `[standard reconstruction]` $\Psi_+(x)=\int dp\,a^\dagger(p)\,e^{-ipx}/\sqrt{2\pi}$
- `[transcript-backed]` $a(p)=\int dx\,\Psi_-(x)\,e^{-ipx}/\sqrt{2\pi}$
- `[standard reconstruction]` $a^\dagger(p)=\int dx\,\Psi_+(x)\,e^{ipx}/\sqrt{2\pi}$
- `[transcript-backed]` $[a_i,a_j^\dagger]=\delta_{ij},\qquad [a_i,a_j]=[a_i^\dagger,a_j^\dagger]=0$
- `[standard reconstruction]` $[a(p),a^\dagger(p')]=\delta(p-p')$
- `[transcript-backed]` $[\Psi_-(x),\Psi_+(y)]=\delta(x-y),\qquad [\Psi_-(x),\Psi_-(y)]=[\Psi_+(x),\Psi_+(y)]=0$

## Definitions And Objects

- `\psi_L,\psi_R`: approximate localized states in the left and right wells when the barrier is high.
- `\psi_+,\psi_-`: symmetric and antisymmetric combinations; these are the exact energy eigenstates once tunneling is admitted.
- `E`: approximate one-sided ground-state energy used in the early sketches.
- `E_1`: central reference energy around which the tunneling split is written.
- `\epsilon`: half the tunnel splitting, so the full energy gap is `2\epsilon`.
- Node: a point where the wavefunction vanishes.
- Neutrino “type” states: electron-neutrino and muon-neutrino states play the role of `\psi_L,\psi_R`.
- Neutrino mass/energy eigenstates: play the role of `\psi_+,\psi_-`.
- Spin analogy: `z`-up and `z`-down are not the energy basis once the magnetic field points along `x`; the `x`-polarized states are.
- Electric dipole moment: a correlation between charge displacement and a chosen axis; for the electron, the axis is supplied by spin or magnetic moment.
- Magnetic moment: axial quantity associated in the lecture with a circulating current around the spin axis.
- `\psi(x)`: ordinary one-particle wavefunction.
- `\tilde\psi(p)`: momentum-space wavefunction.
- `\Psi_-(x),\Psi_+(x)`: annihilation and creation field operators in the lecture’s plus/minus notation.
- `a_i,a_i^\dagger`: annihilation and creation operators for discrete modes or energy eigenstates.
- `a(p),a^\dagger(p)`: annihilation and creation operators for momentum eigenmodes.
- `\delta(x-y)`: equal-time commutator kernel; zero away from coincidence, singular at coincidence.

## Derivation Steps

Double-well parity eigenstates and level splitting

1. Start from two approximate localized states, one in each well, valid when the barrier is high.
2. Use symmetry of the potential to require exact energy eigenstates to be even or odd under reflection.
3. Form the symmetric and antisymmetric combinations `\psi_\pm`.
4. Argue that the symmetric state is smoother through the barrier and therefore slightly lower in energy.
5. Argue that the antisymmetric state has a node and therefore slightly higher energy.
6. Encode the result as the split pair `E_1-\epsilon` and `E_1+\epsilon`.

Left-right oscillation

1. Prepare the initial state as `\psi(0)=\psi_L=(\psi_+ + \psi_-)/\sqrt{2}`.
2. Let each energy eigenstate acquire its own time phase.
3. Factor out the common phase `e^{-iE_1 t}`.
4. Track only the relative phase between the `\psi_+` and `\psi_-` pieces.
5. Demand the sign-flip condition `e^{-i\epsilon t}=-e^{i\epsilon t}`.
6. Rewrite that as `e^{2i\epsilon t}=-1`.
7. Solve the first transfer condition as `2\epsilon t=\pi`.
8. Conclude that the state becomes proportional to `\psi_R` at `t=\pi/(2\epsilon)`.

Spin-precession analogy

1. Start with `z`-up and `z`-down degenerate before any field is applied.
2. Turn on a magnetic field along the `x`-axis, so the energy eigenstates become `x`-polarized states.
3. Express those `x`-polarized states as superpositions of `z`-up and `z`-down.
4. Prepare an initial `z`-up state, which is not an energy eigenstate.
5. Let the two `x`-basis components accumulate different phases.
6. Read the resulting evolution as precession or up-down oscillation.

Quantum “sphere” issue from rotational states

1. Consider a lopsided dumbbell-like object in quantum mechanics.
2. Label rotational states by angular momentum about the center.
3. Note that the ground state of an integer-spin rotor has `J=0`.
4. Use `J=0` to infer rotational invariance of the wavefunction.
5. Distinguish a rotationally averaged quantum state from an instantaneous lopsided configuration.
6. Observe that a fast orientation measurement collapses the system into a definite-angle state.
7. Use the angle/angular-momentum uncertainty logic to explain why such a measurement necessarily kicks the angular momentum.
8. Conclude that “spherical or not” depends on the resolving power of the probe.

EDM symmetry argument

1. Define the electron EDM as charge displacement correlated with the spin or magnetic axis.
2. Under parity, the electric dipole changes sign while the magnetic moment does not.
3. Therefore a nonzero EDM aligned with the same electron would violate parity.
4. Under time reversal, the magnetic moment changes sign while the charge displacement does not.
5. Therefore a nonzero EDM also violates time reversal.
6. Since time-reversal violation in the standard model is tiny, the allowed electron EDM is correspondingly tiny.
7. Read the null experiment as support for standard-model-sized suppression, not as proof that the electron is spherical.

Field operators, Fourier transform, and locality

1. Begin with the ordinary Fourier pair between `\psi(x)` and `\tilde\psi(p)`.
2. Move from amplitudes to operators by replacing momentum-space amplitudes with `a(p)` and position-space objects with `\Psi(x)`.
3. Expand the field operator in plane-wave momentum modes.
4. Invert the transform to recover `a(p)` from the field operator.
5. Use the bosonic algebra of the mode operators.
6. Derive the equal-time field commutator `[\Psi_-(x),\Psi_+(y)]=\delta(x-y)`.
7. Note that the same-point singularity is the only obstruction; separated points commute.
8. Interpret commuting separated fields as independent measurements at different points.

## Notation Choices

- Use lowercase `\psi` only for one-particle wavefunctions.
- Use capital `\Psi` only for field operators.
- In the final notes, standardize `\Psi_-(x)\to \Psi(x)` and `\Psi_+(x)\to \Psi^\dagger(x)`, but mention Susskind’s live `+/-` notation once.
- Keep `\psi_L,\psi_R,\psi_+,\psi_-` exactly in the double-well discussion; they are frame-backed and transcript-backed.
- Use `\epsilon` as half the splitting, not the full gap.
- Use `E_1` as the midpoint reference energy in the split pair; do not leave the late board wobble unresolved.
- Use the standard Schrödinger convention `e^{-iEt}` in the cleaned notes.
- Reserve `P(x)` and `P(p)` for probabilities; keep lowercase `p` for momentum only.
- For the spin analogy, prefer `|L_x\rangle, |R_x\rangle` or `|\pm x\rangle` in the polished chapter to avoid confusion with left/right wells.
- For the EDM interlude, use vector notation `\mathbf d_e`, `\boldsymbol{\mu}_e`, `\mathbf S` explicitly.
- Keep the lecture’s bosonic operator notation `a_i,a_i^\dagger` and `a(p),a^\dagger(p)`.

## Uncertain Mathematics

- The time-dependent phase signs around `00:12` to `00:15` are unstable on the board and in speech; only the relative phase is reliable.
- The board visibly supports `(\psi_L+\psi_R)/\sqrt{2}`, but the full denominator on the antisymmetric line is not cleanly visible; it is supplied from the transcript.
- The statement near `00:19:23` that small `\epsilon` makes the transfer time small is a spoken slip; the derived formula gives a long transfer time when `\epsilon` is small.
- The spin “right” state is only implied verbally; `(|\uparrow_z\rangle-|\downarrow_z\rangle)/\sqrt{2}` is a standard completion.
- The EDM symmetry argument is transcript-backed in logic, but the clean transformation laws for `\mathbf d` and `\boldsymbol{\mu}` are reconstructed from the surrounding discussion because the transcript becomes garbled in places.
- The continuum momentum-mode normalization in the second-quantization segment is heavily corrupted in the transcript; the `1/\sqrt{2\pi}` factors should be treated as cleaned reconstruction.
- The lecture does not derive the relativistic neutrino-oscillation formula; do not import `\Delta m^2 L/(4E)` material into this chapter unless explicitly marked as beyond the lecture.
- The final fermion remarks are preview-level heuristic motivation, not a finished derivation of anticommutator locality.