# Chapter Plan

Focus on the single mathematical spine of the lecture: from quantum state space to dynamics via unitary time evolution, then to symmetry as operator commutation with the Hamiltonian, with one fully worked continuous symmetry example (translations) and the link to conservation laws.

## Lecture Arc

Start with a compact but faithful reconstruction of last-quarter formalism (state vectors, bra-kets, inner products, observables as operators) and immediately specialize to particles, whose observables include position and momentum.

Next, build the concrete Hilbert-space picture in the position representation: state vectors become wavefunctions, and position eigenstates are singular basis elements (Dirac deltas). Momentum is introduced as the corresponding differential operator in this representation.

Then derive dynamics from first principles: continuous time evolution is represented by a linear unitary operator \(U(t)\), continuity implies \(U(\epsilon)\approx 1-i\epsilon H\), and unitarity fixes \(H\) Hermitian. This yields both TDSE and TISE with matching \(H\).

Finally, formalize symmetry as the compatibility of transformations with evolution. Show the commutator criterion \([V,H]=0\), specialize to continuous transformations with generator expansions, and close with the translation example where the generator is momentum (up to \(\hbar\)) and therefore conserved.

## Section Outline

1. **Review and Quantum Kinematics Setup**  
   Re-establish vector-space language, bra-ket notation, Hermitian observables, eigenvalues/eigenvectors as measurement outcomes, and inner-product language for distinguishability. State the operational meaning of orthogonality as “can be told apart with certainty.”

2. **Particle Hilbert Space in Position Representation**  
   Define position eigenstates \(|x\rangle\), wavefunction \(\psi(x)=\langle x|\psi\rangle\), and the probabilistic interpretation \(p(x)=\psi^*(x)\psi(x)\) (with normalization caveats later). Introduce position operator action as multiplication by \(x\).

3. **Momentum in the Same Representation**  
   Introduce momentum operator \(\hat p\) as the generator of translations in \(x\), in practice \(\hat p=-i\hbar\,\partial_x\) (or \(-i\partial_x\) under \(\hbar=1\)), then contrast position and momentum eigenbases and the uncertainty tradeoff.

4. **Unitary Time Evolution and Schrödinger Equations**  
   Define \(U(t)\), derive \(U^\dagger U=\mathbf1\), infer \(U(\epsilon)\approx \mathbf1-i\epsilon H\), and justify \(H\) Hermitian. Extend to finite \(t\) as \(U(t)=e^{-iHt}\), giving TDSE and TISE as linked eigenvalue/evolution statements.

5. **Symmetry as Commuting Unitary Operations**  
   Define symmetry transformations \(V\) as unitary maps preserving probabilities/logical distinction. Show equivalence “symmetry of dynamics” \(\Leftrightarrow\) \(VU(t)=U(t)V\) \(\Leftrightarrow\) \([V,H]=0\), with the conservation corollary.

6. **Continuous Symmetries and Translation Example**  
   Introduce infinitesimal form \(V(\epsilon)\approx \mathbf1-i\epsilon G\), deduce \([G,H]=0\), and work the particle translation case: \(\psi(x)\to\psi(x+\epsilon)\) leading to derivative expansion and generator proportional to momentum. Conclude for \(H=p^2/(2m)\): momentum conservation and translation symmetry coincide.

## Mathematical Content To Include

- [transcript-backed] State-space postulate: physical states are vectors (kets) in a complex vector space; bras are duals, and measurements are represented by operators.
- [transcript-backed] Observables are Hermitian (real-spectrum) operators; eigenvalues are possible measurement outcomes.
- [transcript-backed] Distinguishability criterion: orthogonal vectors (\(\langle\phi|\psi\rangle=0\)) are operationally distinct measurement-wise.
- [transcript-backed] Position eigenstates as a basis for particle state space, with \(\langle x|x'\rangle\) sharply peaked when \(x=x'\), and expansion coefficients interpreted as wavefunction values \(\psi(x)=\langle x|\psi\rangle\).
- [transcript-backed] Position representation of wavefunction and its probability density \(p(x)=\psi^*(x)\psi(x)\) for finding the particle near \(x\).
- [standard reconstruction] Clarify distributional status of \(|x\rangle\) and \(\delta\)-normalization, and add explicit normalization/measure conventions in a rigorous Hilbert-space appendix.
- [transcript-backed] Momentum operator action in position representation: \(\hat p\psi(x)=-i\hbar\partial_x\psi(x)\), with \(\hbar\) sometimes set to 1 in lecture shorthand.
- [transcript-backed] Momentum eigenvalue equation \(\hat p\phi_p(x)=p\,\phi_p(x)\) and plane-wave solutions, showing uniform position-space probability density.
- [transcript-backed] Unitary time evolution \(U(t)\), identity at \(t=0\), continuity in time, and infinitesimal expansion \(U(\epsilon)=\mathbf1-i\epsilon H\).
- [transcript-backed] Unitarity condition to first order gives \(H^\dagger=H\); finite-time form \(U(t)=e^{-iHt}\) (or \(e^{-iHt/\hbar}\) depending on convention).
- [transcript-backed] TDSE in both state-vector and wavefunction forms: \(\frac{d}{dt}|\psi\rangle=-iH|\psi\rangle\), \(\frac{\partial\psi}{\partial t}=-iH\psi\) (with units convention stated).
- [transcript-backed] TISE as eigenproblem \(H|E_n\rangle=E_n|E_n\rangle\), interpreted as stationary states and energy levels.
- [transcript-backed] Symmetry transformation operator \(V\) (unitary) preserving inner products; symmetry of dynamics condition \(V U(t)=U(t) V\).
- [transcript-backed] Reduced condition \([V,H]=0\) and equivalent interpretation for observables commuting with \(H\) (conserved quantities).
- [transcript-backed] Continuous symmetry parametrization \(V(\epsilon)=\mathbf1-i\epsilon G\), yielding generator criterion \([G,H]=0\).
- [transcript-backed] Translation by \(\epsilon\): \((T_\epsilon\psi)(x)=\psi(x+\epsilon)\approx \psi(x)+\epsilon\,\partial_x\psi(x)\), hence \(G\propto p_x\) (or \(p_x/\hbar\) under phase-exponential convention).
- [standard reconstruction] Present both sign conventions for the generator/exponential map and explain consistency of \(T_\epsilon=\exp(-i\epsilon \hat p/\hbar)\) vs equivalent sign choices.

## Diagram And Figure Plan

Use extracted frame images where they preserve readable board structure or instructor emphasis, but keep core formulas recreated in TikZ for uniform typography and LaTeX-grade math.  
Keep as images: `lecture_01_frame_01.png` (lecture context + notation setup), `lecture_01_frame_02.png` (if it shows early state/observable notation on board clearly), `lecture_01_frame_03.png` (time-evolution \(U\) expansion steps), `lecture_01_frame_04.png` (commutator/symmetry algebra chain if legible), `lecture_01_frame_05.png` and `lecture_01_frame_06.png` (translation/generator derivation and free-particle example, if equation density is high).  
Redraw in TikZ: all final equations, TDSE/TISE derivations, commutator implications \([V,H]=0\), and continuity/exponential derivation graphs, so that signs, constants, and operator placement are consistent across the chapter.  
For uncertain frames, do a one-pass visual triage: if handwritten text is noisy, archive them only as source references and typeset the cleaned result from standard reconstruction.

## Caution Notes

- Transcript contains repeated auto-transcription artifacts (“permission conjugate,” “anti-permission,” “Lennard equation,” “x-north/x-axis misread,” “zaxon”), and some symbols were likely missed; reconstruct formulas from context and notation consistency, not raw transcript alone.
- The sign in infinitesimal transformation formulas is repeatedly corrected in lecture; enforce a consistent convention early (e.g., \(U(t)=e^{-iHt/\hbar}\), \(T(\epsilon)=e^{-i\epsilon \hat p/\hbar}\)) and state it explicitly.
- The lecture alternates between \(\hbar=1\) and explicit \(\hbar\); notes should standardize one convention, then document all conversions.
- Dirac-delta eigenstates and unnormalizable plane waves are discussed heuristically; include explicit distribution/caveat text and optional boxed warning in notes.
- “What is \(\phi\) at this point?” transitions in notation are loose in audio; keep variable role tables (state, dual state, amplitude, transformed state) to avoid index and symbol collision.