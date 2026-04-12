# Math Bank

## Core Equations

- [transcript-backed] \(L_z=-i\hbar\,\partial_\theta\) in the two-dimensional prototype.
- [transcript-backed] \(L_z\,\psi(r,\theta)=\hbar \ell\,\psi(r,\theta)\).
- [transcript-backed] \(\psi(r,\theta)=\chi(r)e^{i\ell\theta}\), with \(\ell\in\mathbb Z\).
- [transcript-backed] \(\Psi(r,\theta,\phi)=R(r)\,Y_{\ell m}(\theta,\phi)\).
- [transcript-backed] \([L_x,L_y]=i\hbar L_z\), with cyclic permutations.
- [transcript-backed] \(L_\pm=L_x\pm iL_y\).
- [standard reconstruction] \(L_z\lvert \ell,m\rangle=\hbar m\,\lvert \ell,m\rangle\).
- [standard reconstruction] \(L_\pm\lvert \ell,m\rangle\propto \lvert \ell,m\pm1\rangle\).
- [transcript-backed] \(m=-\ell,-\ell+1,\dots,\ell\), so the multiplet size is \(2\ell+1\).
- [transcript-backed] \(L^2=L_x^2+L_y^2+L_z^2\).
- [standard reconstruction] \(L^2=L_z^2+\hbar L_z+L_-L_+\).
- [standard reconstruction] \(L^2=L_z^2-\hbar L_z+L_+L_-\).
- [visible] \(L^2=\ell(\ell+1)\) on the board, with \(\hbar\) suppressed.
- [transcript-backed] \(L^2\lvert \ell,\ell\rangle=\hbar^2\ell(\ell+1)\lvert \ell,\ell\rangle\).
- [transcript-backed] \(H=\dfrac{p^2}{2m}+V(r)\).
- [visible] \(H=\dfrac{p_r^2+p_\theta^2}{2m}+V(r)\).
- [transcript-backed] \(L=r\,p_\theta\), hence \(L^2=r^2p_\theta^2\) and \(p_\theta^2=\dfrac{L^2}{r^2}\).
- [visible] \(H=\dfrac{p_r^2}{2m}+\dfrac{L^2}{2mr^2}+V(r)\).
- [standard reconstruction] \(V_{\mathrm{eff}}(r)=\dfrac{L^2}{2mr^2}+V(r)\).
- [standard reconstruction] \(p_r=-i\hbar\,\dfrac{d}{dr}\).
- [visible] \(H\psi(r)=E\psi(r)\).
- [standard reconstruction] \(-\dfrac{\hbar^2}{2m}\dfrac{d^2\psi}{dr^2}+\dfrac{\hbar^2\ell(\ell+1)}{2mr^2}\psi+V(r)\psi=E\psi\).
- [transcript-backed] \(-\dfrac{\hbar^2}{2m}\left(\partial_x^2+\partial_y^2+\partial_z^2\right)\Psi+V(r)\Psi=E\Psi\).
- [transcript-backed] For fixed \(\ell\), each radial level carries degeneracy \(2\ell+1\).
- [transcript-backed] In the Coulomb case, shell degeneracies are \(1,4,9,16,\dots\).
- [transcript-backed] \(H=\dfrac{p^2}{2}+\dfrac{\omega^2x^2}{2}\) for the oscillator after setting \(m=1\) and \(k=\omega^2\).
- [transcript-backed] \(\dot x=\dfrac{\partial H}{\partial p}=p\), \(\dot p=-\dfrac{\partial H}{\partial x}=-\omega^2x\).
- [transcript-backed] \(\ddot x=-\omega^2x\).
- [transcript-backed] \([x,p]=i\hbar\).
- [standard reconstruction] \(H=\dfrac12(p+i\omega x)(p-i\omega x)+\dfrac12\hbar\omega\).
- [standard reconstruction] \(A_+=\dfrac{p+i\omega x}{\sqrt{2\hbar\omega}},\qquad A_-=\dfrac{p-i\omega x}{\sqrt{2\hbar\omega}}\).
- [transcript-backed] \([A_-,A_+]=1\).
- [transcript-backed] \(N=A_+A_-\).
- [standard reconstruction] \(H=\hbar\omega\left(N+\tfrac12\right)\).
- [transcript-backed] \(N\lvert n\rangle=n\lvert n\rangle\), with \(n=0,1,2,\dots\).
- [transcript-backed] \(N(A_+\lvert n\rangle)=(n+1)(A_+\lvert n\rangle)\).
- [transcript-backed] \(A_-\lvert 0\rangle=0\).
- [standard reconstruction] \(A_+\lvert n\rangle=\sqrt{n+1}\,\lvert n+1\rangle,\qquad A_-\lvert n\rangle=\sqrt n\,\lvert n-1\rangle\).
- [transcript-backed] \(E_n=\hbar\omega\left(n+\tfrac12\right)\).

## Definitions And Objects

- Angular momentum is treated as a statement about the angular dependence of the wavefunction, not its radial dependence.
- \(\chi(r)\): arbitrary radial factor in the two-dimensional eigenfunction \(e^{i\ell\theta}\chi(r)\).
- \(Y_{\ell m}(\theta,\phi)\): angular functions on the sphere; these are the spherical harmonics.
- Multiplet: the collection of states with fixed \(\ell\) and varying \(m\).
- Top state: the highest-\(m\) state in a multiplet, annihilated by \(L_+\).
- Bottom state: the lowest-\(m\) state in a multiplet, annihilated by \(L_-\).
- \(L^2\): square of total angular momentum; common to the whole multiplet.
- \(p_r\), \(p_\theta\): radial and angular components in the classical central-force reduction.
- Centrifugal barrier: the effective potential term \(L^2/(2mr^2)\).
- Bound state: discrete state localized in the effective potential well.
- Node: zero of the radial wavefunction; node count orders the bound states at fixed \(\ell\).
- \(A_+\), \(A_-\): oscillator ladder operators, Hermitian conjugates of each other.
- \(N=A_+A_-\): oscillator number operator after the additive zero-point term is isolated.
- Ground state: lowest oscillator state, annihilated by \(A_-\).
- Zero-point energy: the additive \(\tfrac12\hbar\omega\) left over from factorization.

## Derivation Steps

Angular momentum eigenfunctions in 2D

1. Start from the rotational generator \(L_z=-i\hbar\,\partial_\theta\).
2. Write the eigenvalue equation \(L_z\psi=\hbar\ell\,\psi\).
3. Note that the derivative is only with respect to \(\theta\), so \(r\) is a spectator.
4. Solve the \(\theta\)-dependence to get \(e^{i\ell\theta}\).
5. Impose single-valuedness around the circle to force \(\ell\in\mathbb Z\).
6. Conclude that the radial factor is arbitrary for angular-momentum purposes.

Multiplets and the \(L^2=\ell(\ell+1)\) result

1. Choose an \(L_z\) eigenbasis and label states by \(m\).
2. Use the commutators to show that \(L_+\) raises \(m\) by one and \(L_-\) lowers \(m\) by one.
3. Argue that a finite ladder must terminate when the next raising or lowering gives zero.
4. Use symmetry under \(z\to -z\) to force the ladder endpoints to be symmetric.
5. Conclude that finite multiplets are indexed by a top value \(\ell\), with \(m=-\ell,\dots,\ell\).
6. Count states to get \(2\ell+1\).
7. Rewrite \(L^2\) in ordered form, e.g. \(L^2=L_z^2+\hbar L_z+L_-L_+\).
8. Apply this to the top state \(\lvert \ell,\ell\rangle\).
9. Replace \(L_z\) by \(\hbar\ell\) and use \(L_+\lvert \ell,\ell\rangle=0\).
10. Obtain \(L^2\lvert \ell,\ell\rangle=\hbar^2\ell(\ell+1)\lvert \ell,\ell\rangle\).
11. Use \([L^2,L_i]=0\) to propagate the same \(L^2\) eigenvalue through the whole multiplet.

Central-force reduction and radial equation

1. Start from \(H=p^2/(2m)+V(r)\).
2. Use rotational symmetry to state that \(\mathbf L=\mathbf r\times\mathbf p\) is conserved.
3. In the classical picture, use the conserved orbital plane to work in that plane.
4. Decompose momentum into \(p_r\) and \(p_\theta\).
5. Write \(p^2=p_r^2+p_\theta^2\).
6. Use \(L=r\,p_\theta\) to replace \(p_\theta^2\) by \(L^2/r^2\).
7. Rewrite the Hamiltonian as \(p_r^2/(2m)+L^2/(2mr^2)+V(r)\).
8. Interpret the \(1/r^2\) term as the centrifugal barrier.
9. Quantize the radial kinetic term with \(p_r^2\to -\hbar^2\,d^2/dr^2\).
10. Replace \(L^2\) by \(\hbar^2\ell(\ell+1)\) on angular-momentum eigenstates.
11. Obtain the one-variable radial Schrödinger equation.

Spectral organization for central forces

1. Fix \(\ell\); this fixes the centrifugal term in the radial equation.
2. Solve the resulting radial problem as a one-dimensional bound-state problem.
3. Order states by node count: no nodes, one node, two nodes, and so on.
4. Use the standard bound-state ordering to identify higher node count with higher energy.
5. Attach degeneracy \(2\ell+1\) to each fixed-\(\ell\) radial level.
6. For generic attractive potentials, increasing \(\ell\) pushes the tower upward.
7. For Coulomb, note the special alignment: \(\ell=1\) zero-node aligns with \(\ell=0\) one-node, etc.
8. Sum the orbital degeneracies level by level to get \(1,4,9,16,\dots\).
9. Restore the missing factor of two later when spin is included.

Oscillator ladder construction

1. Set \(m=1\) and \(k=\omega^2\), so \(H=\frac12(p^2+\omega^2x^2)\).
2. Check classically that Hamilton’s equations give \(\ddot x=-\omega^2x\).
3. Try to factor \(p^2+\omega^2x^2\) using \(p\pm i\omega x\).
4. Notice that the naive factorization misses a commutator term because \(x\) and \(p\) do not commute.
5. Use \([x,p]=i\hbar\) to extract the additive \(\tfrac12\hbar\omega\).
6. Define the normalized operators \(A_+\) and \(A_-\).
7. Compute \([A_-,A_+]=1\).
8. Define \(N=A_+A_-\).
9. If \(N\lvert n\rangle=n\lvert n\rangle\), apply \(A_+\) and show the new state has eigenvalue \(n+1\).
10. Similarly, \(A_-\) lowers the eigenvalue.
11. Use positivity of \(N=A_+A_-\) to show the ladder cannot descend forever.
12. Identify the bottom state by \(A_-\lvert 0\rangle=0\).
13. Restore the dropped constant to get \(E_n=\hbar\omega(n+\tfrac12)\).

## Notation Choices

- Use \(L_x,L_y,L_z\) and \(L^2\) for operators; use \(\ell,m\) for quantum numbers.
- Use \(\lvert \ell,m\rangle\) when both labels matter; avoid bare \(\lvert m\rangle\) except in obvious shorthand.
- Treat \(\ell\) and \(m\) as dimensionless integers or half-integers; the operator eigenvalues carry the \(\hbar\).
- In the orbital central-force part, restrict to integer \(\ell\), because the angular functions are \(Y_{\ell m}\).
- Use \(\Psi(r,\theta,\phi)\) for the full three-dimensional wavefunction.
- Use \(\psi(r)\) for the lecture’s reduced radial unknown, but add a note if needed that this is simplified radial notation.
- If a mathematically cleaner notation is needed, identify \(\psi(r)\) with the reduced radial function \(u_\ell(r)\).
- Keep \(L_\pm\) as the main ladder-operator notation for angular momentum; the board also shows \(L^+\), \(L^-\) style.
- Keep \(A_+\), \(A_-\) for the oscillator in the lecture-facing exposition.
- If standard notation is preferred later, map \(A_+\to a^\dagger\) and \(A_-\to a\) once, then stay consistent.
- Use \(N\) for the oscillator number operator only after the zero-point term has been split off.
- Keep \(p_\theta\) in the classical reduction because that is the lecture’s notation; do not retrofit a full canonical 3D derivation into this stage.
- In final notes, use \(d/dr\) rather than \(\partial/\partial r\) for the reduced radial ODE.

## Uncertain Mathematics

- The transcript is garbled in the early counting passage near the example with seven states; preserve the logic, not the broken wording.
- The lecture begins with general angular-momentum algebra, where half-integer multiplets are allowed, but the later orbital discussion uses spherical harmonics and therefore integer \(\ell\) only.
- The spoken formula for \(p_r\) has the wrong sign; use the standard \(p_r=-i\hbar\,d/dr\), noting that only \(p_r^2\) is used in the actual reduction.
- The board radial equation is written as a pure second-derivative equation for \(\psi(r)\); rigorously this is the reduced radial equation, not the unreduced \(R_\ell(r)\) equation.
- The frame evidence for the radial equation omits at least some \(\hbar\) factors; restore them consistently.
- There is a brief spoken slip toward \(L^2=\ell(\ell-1)\); only the corrected \(L^2=\ell(\ell+1)\) belongs in the notes.
- The ordered identities for \(L^2\) depend on whether one places \(L_-L_+\) or \(L_+L_-\); both are valid, but the sign in front of \(L_z\) changes accordingly.
- The “Gegenbauer” label for the Coulomb radial solutions should be treated cautiously; do not hard-wire that special-function name without checking.
- The oscillator normalization factors \(\sqrt{n+1}\) and \(\sqrt n\) appear only as a late correction in a tired ending; use the clean standard formulas, but do not claim the lecture derived them cleanly.
- The degeneracy pattern \(1,4,9,16,\dots\) is the orbital Coulomb pattern before spin, relativistic corrections, and finite-size effects are included.