# Math Bank
## Core Equations
- \(\psi(x,t)=e^{i(kx-\omega t)}\) or \(\sin(kx-\omega t)\) [transcript-backed]
- \(kx-\omega t=\text{const}\) [transcript-backed]
- \(x=\dfrac{\omega}{k}\,t\) [transcript-backed]
- \(v_{\mathrm{phase}}=\dfrac{\omega}{k}=\dfrac{\lambda}{T}\) [transcript-backed]
- \(\omega=\dfrac{k^2}{2m}\) [transcript-backed]
- \(v_{\mathrm{phase}}=\dfrac{\omega}{k}=\dfrac{k}{2m}\) [transcript-backed]
- \(\omega(k)\to \omega(k)+c\) [transcript-backed]
- \(\psi(x,t)\to e^{-ict}\psi(x,t)\) [transcript-backed]
- \(\psi\psi^\ast\) is unchanged under \(\psi\to e^{-ict}\psi\) [transcript-backed]
- \((k-k')x=(\omega-\omega')t\) [transcript-backed]
- \(x=\dfrac{\omega-\omega'}{k-k'}\,t\) [transcript-backed]
- \(x=\dfrac{d\omega}{dk}\,t\) [transcript-backed]
- \(v_{\mathrm{group}}=\dfrac{d\omega}{dk}\) [visible]
- \(\omega=\dfrac{k^2}{2m}+c\) [visible]
- \(v_{\mathrm{group}}=\dfrac{d\omega}{dk}=\dfrac{k}{m}\) [visible]
- \(E=\sqrt{p^2+m^2}\) [visible]
- \(\omega=\sqrt{k^2+m^2}\) [visible]
- \(\hbar=c=1\) [visible]
- \(v_{\mathrm{phase}}=\dfrac{\omega}{k}=\sqrt{\dfrac{k^2+m^2}{k^2}}\) [transcript-backed]
- \(v_{\mathrm{group}}=\dfrac{d\omega}{dk}=\dfrac{k}{\sqrt{k^2+m^2}}=\sqrt{\dfrac{k^2}{k^2+m^2}}\) [transcript-backed]
- \(v_{\mathrm{phase}}v_{\mathrm{group}}=1\) for \(\omega=\sqrt{k^2+m^2}\) [transcript-backed]
- \(\omega\propto k\) implies no dispersion and \(v_{\mathrm{phase}}=v_{\mathrm{group}}\) [transcript-backed]
- \(\int dt\,e^{\,i(\sum \omega_{\text{out}}-\sum \omega_{\text{in}})t}\propto \delta\!\left(\sum \omega_{\text{out}}-\sum \omega_{\text{in}}\right)\) [transcript-backed]
- \(\int dx\,e^{\,i(\sum k_{\text{in}}-\sum k_{\text{out}})x}\propto \delta\!\left(\sum k_{\text{out}}-\sum k_{\text{in}}\right)\) [transcript-backed]
- \(\psi\to e^{i\lambda}\psi\) [transcript-backed]
- \(\psi(x)=\sum_k c(k)e^{ikx}\) [standard reconstruction]
- \(\psi^\dagger(x)=\sum_k c^\dagger(k)e^{-ikx}\) [standard reconstruction]
- \(c^\dagger|0\rangle=|1\rangle\) [transcript-backed]
- \(c^\dagger|1\rangle=0\) [transcript-backed]
- \(c|0\rangle=0\) [transcript-backed]
- \(c|1\rangle=|0\rangle\) [transcript-backed]
- \(\{c,c^\dagger\}=1\) [transcript-backed]
- \(\{c,c\}=0\) [transcript-backed]
- \(\{c^\dagger,c^\dagger\}=0\) [transcript-backed]
- \(\{c_k,c_{k'}^\dagger\}=\delta_{kk'}\) [transcript-backed]
- \(\{c_k,c_{k'}\}=0\) [transcript-backed]
- \(\{c_k^\dagger,c_{k'}^\dagger\}=0\) [transcript-backed]
- \(\psi^\dagger(0)\psi^\dagger(0)|0\rangle=0\) [standard reconstruction]
- \(\dfrac{1}{\sqrt2}\bigl(|N\rangle+|C\rangle\bigr)\) [transcript-backed]
- \(\dfrac{1}{\sqrt2}\bigl(|N\rangle-|C\rangle\bigr)\) [transcript-backed]
- \(k=\dfrac{2\pi n}{L}\) [transcript-backed]
- \(E=\dfrac{k^2}{2m}\) for the box-filling discussion [transcript-backed]
- \(\omega=\pm k\) [transcript-backed]
- \(\partial_t\psi=-\partial_x\psi\) [standard reconstruction]
- \(\partial_t\psi=+\partial_x\psi\) [transcript-backed]
- If \(\psi=e^{i(kx-\omega t)}\), then \(\partial_t\psi=-i\omega\psi\) and \(\partial_x\psi=ik\psi\) [transcript-backed]
- For \(\omega=k\), negative \(k\) gives negative \(\omega\) [transcript-backed]

## Definitions And Objects
- Phase velocity: velocity of constant phase or crest motion for a single plane wave.
- Group velocity: velocity of the moving locus of constructive interference; physically tied to packet motion and signal propagation.
- Wave packet: superposition of nearby plane waves producing a localized lump by destructive interference away from the center.
- Translation invariance in time: process can occur with equal amplitude at any time.
- Translation invariance in space: process can occur with equal amplitude at any point in space.
- Global phase symmetry: multiplying a field by an overall phase \(e^{i\lambda}\).
- Boson: particle with unrestricted occupancy of a single quantum state.
- Fermion: particle with occupancy numbers \(0\) or \(1\) in each state.
- Vacuum in the one-state fermion example: \(|0\rangle\), the empty state.
- Zero vector: literal \(0\), not the same object as the vacuum state \(|0\rangle\).
- Anticommutator: \(\{A,B\}=AB+BA\).
- Same quantum state: not merely same momentum; may require momentum plus spin, or more generally the same one-particle wavefunction.
- Boson condensate: many bosons occupying the lowest single-particle state.
- Fermi sphere: filled region of momentum space in the ground state of many fermions in a finite box.
- Fermi surface: boundary of the Fermi sphere.
- Fermi sea: filled interior of the Fermi sphere.
- Hole: missing electron below the Fermi surface, treated as a positively charged excitation with positive energy relative to the surface.
- Dirac sea in the toy model: all negative-energy fermion states filled and called the vacuum.

## Derivation Steps
Phase velocity and the additive-constant test
1. Start from \(\psi(x,t)=e^{i(kx-\omega t)}\) or \(\sin(kx-\omega t)\).
2. Hold the phase fixed: \(kx-\omega t=\text{const}\).
3. Solve for the moving point: \(x=(\omega/k)t\).
4. Identify \(v_{\mathrm{phase}}=\omega/k\).
5. For Schrödinger waves use \(\omega=k^2/(2m)\), giving \(v_{\mathrm{phase}}=k/(2m)\).
6. Shift every frequency by the same constant: \(\omega\to\omega+c\).
7. The field acquires a common factor \(e^{-ict}\).
8. Observables built from \(\psi\psi^\ast\) are unchanged.
9. Conclude that phase velocity is representation-dependent in this context.

Group velocity from two nearby waves
1. Superpose two nearby waves with \(k\) and \(k'\), and frequencies \(\omega(k)\) and \(\omega(k')\).
2. Ask where the two phases agree, since that is where constructive interference is strongest.
3. Set \(kx-\omega t=k'x-\omega' t\).
4. Rearrange to \((k-k')x=(\omega-\omega')t\).
5. Solve for the moving reinforcement point: \(x=\dfrac{\omega-\omega'}{k-k'}t\).
6. Take \(k'\to k\) to obtain \(x=\dfrac{d\omega}{dk}t\).
7. Read off \(v_{\mathrm{group}}=\dfrac{d\omega}{dk}\).
8. For \(\omega=\dfrac{k^2}{2m}+c\), differentiate to get \(v_{\mathrm{group}}=k/m\).
9. Note that the additive constant drops out.

Relativistic dispersion example
1. Use \(E=\sqrt{p^2+m^2}\) and \(\omega=\sqrt{k^2+m^2}\) with \(\hbar=c=1\).
2. Compute the phase velocity: \(v_{\mathrm{phase}}=\omega/k\).
3. Rewrite it as \(v_{\mathrm{phase}}=\sqrt{(k^2+m^2)/k^2}>1\).
4. Compute the group velocity: \(v_{\mathrm{group}}=d\omega/dk\).
5. Differentiate the square root to get \(v_{\mathrm{group}}=k/\sqrt{k^2+m^2}<1\).
6. Observe that \(v_{\mathrm{phase}}v_{\mathrm{group}}=1\) in this example.
7. Tie the difference between the two velocities to dispersion.

Energy and momentum conservation from integrals
1. Write the scattering amplitude with field factors carrying \(e^{-i\omega t}\) and \(e^{ikx}\).
2. At a fixed spatial point, only the time-dependent phase factors remain relevant.
3. Combine them into \(e^{\,i(\sum \omega_{\text{out}}-\sum \omega_{\text{in}})t}\).
4. Integrate over all time.
5. Obtain \(\delta(\sum \omega_{\text{out}}-\sum \omega_{\text{in}})\).
6. Interpret this as energy conservation from time-translation invariance.
7. Repeat the argument in space with \(e^{\,i(\sum k_{\text{in}}-\sum k_{\text{out}})x}\).
8. Integrate over all space.
9. Obtain \(\delta(\sum k_{\text{out}}-\sum k_{\text{in}})\).
10. Interpret this as momentum conservation from space-translation invariance.

Fermion algebra from the one-state problem
1. Restrict to a single fermionic state with basis \(|0\rangle, |1\rangle\).
2. Define the operator action: \(c^\dagger|0\rangle=|1\rangle\), \(c^\dagger|1\rangle=0\), \(c|0\rangle=0\), \(c|1\rangle=|0\rangle\).
3. Act with \(c^\dagger c\) and \(cc^\dagger\) on \(|0\rangle\) and \(|1\rangle\).
4. Show that \((c^\dagger c+cc^\dagger)\) returns the same state in both cases.
5. Conclude \(\{c,c^\dagger\}=1\).
6. Try \(c^\dagger c^\dagger\) on either basis state and get zero.
7. Conclude \(\{c^\dagger,c^\dagger\}=0\).
8. Likewise conclude \(\{c,c\}=0\).
9. Generalize to momentum labels: \(\{c_k,c_{k'}^\dagger\}=\delta_{kk'}\), others zero.

Same-position exclusion from the field operator
1. Create a fermion at position \(x\) with \(\psi^\dagger(x)\).
2. Ask what happens for two attempts at the same point.
3. Evaluate at \(x=0\) for simplicity so the plane-wave factors are \(1\).
4. Expand \(\psi^\dagger(0)\psi^\dagger(0)|0\rangle\) into a double sum over \(k,k'\).
5. Symmetrize the product inside the sum.
6. Recognize the bracket as an anticommutator of creation operators.
7. Use \(\{c_k^\dagger,c_{k'}^\dagger\}=0\).
8. Conclude \(\psi^\dagger(0)\psi^\dagger(0)|0\rangle=0\).

Ground states and low-energy fermion excitations
1. In a finite box, allowed momenta are discrete: \(k=2\pi n/L\).
2. For bosons, keep energy minimal by placing every particle in the \(k=0\) state.
3. For fermions, fill the lowest available momentum states one by one.
4. In many dimensions this fills a region in momentum space: the Fermi sphere.
5. To create a very low-energy excitation, do not move a deep electron.
6. Move an electron from just below the Fermi surface to just above it.
7. This creates a particle above the surface and a hole below it.
8. Measure both energies relative to the Fermi surface so both are positive.

Toy Dirac equation and negative-energy sea
1. Take the one-dimensional massless dispersion relation \(\omega=k\).
2. Ask for a first-order wave equation consistent with a plane wave \(e^{i(kx-\omega t)}\).
3. Use \(\partial_t\psi=-i\omega\psi\) and \(\partial_x\psi=ik\psi\).
4. For \(\omega=k\), obtain \(\partial_t\psi=-\partial_x\psi\).
5. Note that the opposite sign gives the left-moving equation.
6. Observe that \(k<0\) implies \(\omega<0\), hence negative energy states.
7. Identify the instability: electrons could radiate endlessly into lower and lower energies.
8. Invoke Fermi statistics and fill all negative-energy states.
9. Call that filled configuration the vacuum.
10. Remove one negative-energy electron and promote it to positive energy.
11. Interpret the missing electron as a positively charged hole, i.e. the antiparticle.

## Notation Choices
- Use \(\psi(x,t)\) for the wave or field throughout, but state locally whether it is being treated as a single-particle wavefunction or a second-quantized field.
- Use \(k\) for wave number / momentum label and \(\omega\) for frequency / energy label once \(\hbar=1\) is assumed.
- Keep \(\hbar=c=1\) explicit the first time the relativistic formulas are used.
- Use \(v_{\mathrm{phase}}\) and \(v_{\mathrm{group}}\) as the cleaned notation for the two velocities.
- Reserve \(a,a^\dagger\) or \(A_\pm\) for bosonic operators only when needed in comparison.
- Use \(c_k,c_k^\dagger\) for fermionic annihilation and creation operators, matching Susskind’s chosen relabeling away from \(a\).
- Prefer daggers over \(\pm\) notation in the final notes: \(c^\dagger,c\) rather than \(c_+,c_-\), except when paraphrasing the lecture’s spoken bookkeeping.
- Use \(\{A,B\}=AB+BA\) for anticommutators and \([A,B]=AB-BA\) only for boson comparison.
- Use \(|0\rangle\) for the vacuum / empty state and plain \(0\) for the zero vector or zero operator; keep that distinction explicit.
- Use \(|1\rangle\) for the occupied one-state fermion example.
- Use \(|N\rangle\) and \(|C\rangle\) for the Nevada and Connecticut basis states.
- Use “same quantum state” as the correct statement of Pauli exclusion; do not keep “same momentum” as the final formulation.
- Use “Fermi sphere,” “Fermi surface,” and “Fermi sea” distinctly.
- In the toy Dirac section, use \(\partial_t\psi=-\partial_x\psi\) for right-movers and \(\partial_t\psi=+\partial_x\psi\) for left-movers.

## Uncertain Mathematics
- The lecture briefly says \(\omega^2=k^2/(2m)\) and then corrects itself; final notes should keep only \(\omega=k^2/(2m)\).
- The two-wave interference algebra is garbled in the transcript around the rearrangement step; preserve only the reliable chain leading to \((k-k')x=(\omega-\omega')t\) and then \(d\omega/dk\).
- The conservation-law recap contains a spoken slip where “momentum” and “energy” are momentarily swapped; the cleaned delta functions should be stated directly.
- The exact normalization factors in the field expansions are omitted in the lecture; do not invent \(2\pi\), \(L^{-1/2}\), or measure factors unless the later chapter needs them and marks them as editorial completion.
- The exact board expression behind \(\psi^\dagger(0)\psi^\dagger(0)|0\rangle\) is only partially visible; the position argument \(0\) should be treated as a convenient lecture choice, not sacred notation.
- The symmetric rewriting of the double-creation-operator sum in the same-position argument is a standard reconstruction of what the lecture is doing, not a verbatim chalk transcription.
- The particle-hole energy discussion near \(1{:}32\) is transcript-corrupted and momentarily confused between “difference” and “sum”; the safe final statement is that excitation energies are measured relative to the Fermi surface and are positive.
- The toy Dirac equation is not the full Dirac equation; it is a one-dimensional, massless, one-direction-at-a-time simplification.
- The neutrino side remark at the end is not reliable and should not control the mathematics.