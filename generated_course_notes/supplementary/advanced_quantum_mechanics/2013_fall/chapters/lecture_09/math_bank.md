# Math Bank
## Core Equations
- [transcript-backed] \(H=\int dx\,\psi^\dagger(x)\left[-\frac{\nabla^2}{2m}+V(x)\right]\psi(x)\)
- [transcript-backed] \(n(x)=\psi^\dagger(x)\psi(x)\), \(\qquad N=\int dx\,n(x)\)
- [transcript-backed] \(V(x)=V_0 \;\Rightarrow\; \int dx\,V_0\,\psi^\dagger(x)\psi(x)=V_0\,N\)
- [transcript-backed] \(|\phi(t+\epsilon)\rangle=(1-i\epsilon H)|\phi(t)\rangle\)
- [transcript-backed] \(\psi(x)=\int \frac{dp}{\sqrt{2\pi}}\,\tilde\psi(p)e^{ipx}\), \(\qquad \psi^\dagger(x)=\int \frac{dq}{\sqrt{2\pi}}\,\tilde\psi^\dagger(q)e^{-iqx}\)
- [transcript-backed] \(\int dx\,e^{i(p-q)x}=\delta(p-q)\)
- [standard reconstruction] \(\int dx\,\psi^\dagger(x)\psi(x)=\int dp\,\tilde\psi^\dagger(p)\tilde\psi(p)\)
- [standard reconstruction] \(\int dx\,\psi^\dagger(x)\left(-\frac{\partial_x^2}{2m}\right)\psi(x)=\int dp\,\frac{p^2}{2m}\,\tilde\psi^\dagger(p)\tilde\psi(p)\)
- [transcript-backed] \(\delta\!\left(\sum_i p_i-\sum_j q_j\right)\) for a local product of fields integrated over \(x\)
- [standard reconstruction] \(\int dx\,\psi^\dagger(-\partial_x^2)\psi=\int dx\,(\partial_x\psi^\dagger)(\partial_x\psi)\) up to boundary terms
- [visible] \(H_{\text{contact}}=g\int dx\,\psi_e^\dagger(x)\psi_p^\dagger(x)\psi_e(x)\psi_p(x)\)
- [transcript-backed] \(H_{A\to B+C}=g\int dx\,\psi_B^\dagger(x)\psi_C^\dagger(x)\psi_A(x)+\text{h.c.}\)
- [transcript-backed] \(H=H^\dagger\)
- [standard reconstruction] \(|\phi(t+\epsilon)\rangle=\left(1-i\epsilon H-\frac{\epsilon^2}{2}H^2+\frac{i\epsilon^3}{3!}H^3+\cdots\right)|\phi(t)\rangle\)
- [standard reconstruction] \(E=\frac{p^2}{2m}\), \(\quad p\to -i\partial_x\), \(\quad E\to i\partial_t\), \(\quad i\partial_t\psi=-\frac{1}{2m}\partial_x^2\psi\)
- [transcript-backed] \(E^2=p^2+m^2\) with \(c=1\)
- [transcript-backed] \(-\partial_t^2\psi=(-\partial_x^2+m^2)\psi\)
- [transcript-backed] \(i\partial_t\psi=\sqrt{-\partial_x^2+m^2}\,\psi\)
- [visible] \(P=E\)
- [transcript-backed] \(i\partial_t\psi=-i\partial_x\psi\), equivalently \((\partial_t+\partial_x)\psi=0\)
- [transcript-backed] \(\psi(x,t)=f(x-t)\)
- [transcript-backed] \((\partial_t-\partial_x)\psi_2=0\), equivalently \(i\partial_t\psi_2=+i\partial_x\psi_2\)
- [visible] \(\Psi=\begin{pmatrix}\psi_1\\ \psi_2\end{pmatrix}\), \(\qquad \alpha=\begin{pmatrix}1&0\\0&-1\end{pmatrix}\), \(\qquad H=\alpha P\)
- [visible] \(i\partial_t\Psi=-i\alpha\,\partial_x\Psi\)
- [transcript-backed] \(H=\alpha p+\beta m\)
- [standard reconstruction] \(H^2=(\alpha p+\beta m)^2=\alpha^2p^2+\beta^2m^2+(\alpha\beta+\beta\alpha)\,pm\)
- [visible] \(\alpha^2=1\), \(\qquad \beta^2=1\), \(\qquad \alpha\beta+\beta\alpha=0\)
- [transcript-backed] \(\beta=\begin{pmatrix}0&1\\1&0\end{pmatrix}\)
- [transcript-backed] \(i\partial_t\Psi=\left(-i\alpha\partial_x+\beta m\right)\Psi\)
- [standard reconstruction] \(i\partial_t\psi_1=-i\partial_x\psi_1+m\psi_2\), \(\qquad i\partial_t\psi_2=+i\partial_x\psi_2+m\psi_1\)

## Definitions And Objects
- \(\psi^\dagger(x)\): creation operator for a particle at position \(x\).
- \(\psi(x)\): annihilation operator for a particle at position \(x\).
- \(\tilde\psi^\dagger(p)\), \(\tilde\psi(p)\): creation/annihilation operators for momentum \(p\).
- \(n(x)=\psi^\dagger(x)\psi(x)\): particle-density operator.
- \(N=\int dx\,n(x)\): total particle-number operator.
- Local integrated product of fields: translation-invariant Hamiltonian term whose spatial integral produces the momentum-conserving delta function.
- \(g\): coupling constant; interaction strength inferred experimentally.
- h.c.: hermitian-conjugate term, representing the reverse process required by hermiticity.
- Toy “electron” and “proton” fields in the interaction examples: bosonic stand-ins, not literal fermionic electron/proton fields.
- \(\Psi=(\psi_1,\psi_2)^T\): two-component one-particle wavefunction in the 1D Dirac discussion.
- \(\psi_1\), \(\psi_2\): right-moving and left-moving components in the massless limit.
- \(\alpha\): matrix distinguishing the two components; in 1D it is \(\sigma_3\), but Susskind calls it \(\alpha\), not spin.
- \(\beta\): second Dirac matrix; off-diagonal in the chosen 1D convention and responsible for coupling the two components.
- “Vertex”: one insertion of an interaction term in the perturbative expansion.
- “Self-energy”: process \(A\to B+C\to A\), interpreted as correcting the structure of the \(A\) particle.
- “Exchange diagram”: second-order process where scattering is mediated by an intermediate field created at one vertex and removed at another.

## Derivation Steps
Momentum conservation from \(\int dx\,\psi^\dagger\psi\)
1. Insert the Fourier expansions of \(\psi(x)\) and \(\psi^\dagger(x)\).
2. Multiply the operators and collect the phase \(e^{i(p-q)x}\).
3. Integrate over \(x\).
4. Replace the \(x\)-integral by \(\delta(p-q)\).
5. Use the delta function to set \(q=p\).
6. The operator removes and replaces a particle with the same momentum.

Kinetic term in momentum space
1. Start from \(\int dx\,\psi^\dagger(-\partial_x^2/2m)\psi\).
2. Expand the fields in momentum space.
3. Let \(-\partial_x^2\) act on the exponential.
4. Pull down a factor \(q^2\) from differentiating the phase.
5. Perform the \(x\)-integral to get \(\delta(p-q)\).
6. Set \(q=p\) and obtain the weight \(p^2/2m\) on the number operator.

Total momentum conservation for a local many-field term
1. Assign momenta \(p_i\) to annihilation operators and \(q_j\) to creation operators.
2. Multiply the associated exponentials.
3. Combine the phase into \(e^{i(\sum p_i-\sum q_j)x}\).
4. Integrate over \(x\).
5. Obtain \(\delta(\sum p_i-\sum q_j)\).
6. Conclude that only total incoming momentum equals total outgoing momentum.

Positivity of the kinetic term
1. Start from \(\int dx\,\psi^\dagger(-\partial_x^2)\psi\).
2. Integrate by parts once.
3. Move one derivative onto \(\psi^\dagger\).
4. Flip the sign from integration by parts.
5. Ignore boundary terms, as Susskind does in lecture.
6. Read the result as \(\int dx\,(\partial_x\psi^\dagger)(\partial_x\psi)\), manifestly positive.

Hermitian completion of the decay term
1. Write the decay operator \(\psi_B^\dagger\psi_C^\dagger\psi_A\).
2. Take the hermitian conjugate of each factor.
3. Reverse the operator order.
4. In this bosonic toy setting, reorder commuting distinct fields if needed.
5. Obtain the reverse process operator \(\psi_A^\dagger\psi_B\psi_C\).
6. Add both pieces to make the Hamiltonian hermitian.

Second-order processes from \(H^2\)
1. Expand time evolution to order \(\epsilon^2\).
2. Interpret \(H^2\) as two insertions of the interaction Hamiltonian.
3. One insertion can realize \(A\to B+C\).
4. A second insertion can realize \(B+C\to A\).
5. The combined process gives a self-energy contribution.
6. Other pairings of insertions give exchange or scattering contributions.
7. Each vertex contributes one factor of \(g\), so a two-vertex process carries \(g^2\).

Massless 1D Dirac construction
1. Choose the right-moving massless branch \(E=P\).
2. Quantize with \(E\to i\partial_t\) and \(P\to -i\partial_x\).
3. Obtain \(i\partial_t\psi=-i\partial_x\psi\).
4. Rewrite as \((\partial_t+\partial_x)\psi=0\).
5. Identify solutions as \(f(x-t)\), rigid right-moving waves.
6. Note the two defects: negative-energy states and one-way propagation.
7. Introduce a second component for the left-moving branch.
8. Package the two amplitudes into \(\Psi\) and introduce \(\alpha\).
9. Write \(H=\alpha p\) and hence \(i\partial_t\Psi=-i\alpha\partial_x\Psi\).

Massive 1D Dirac construction
1. Add a mass term and assume \(H=\alpha p+\beta m\).
2. Square the Hamiltonian.
3. Use that \(\alpha\) commutes with \(p\) in this setup.
4. Demand the \(p^2\) coefficient be \(1\), giving \(\alpha^2=1\).
5. Demand the \(m^2\) coefficient be \(1\), giving \(\beta^2=1\).
6. Eliminate the cross-term by imposing \(\alpha\beta+\beta\alpha=0\).
7. Choose \(\beta\) as an off-diagonal Pauli matrix.
8. Substitute \(\alpha=\mathrm{diag}(1,-1)\), \(\beta=\sigma_1\).
9. Read off that the mass term swaps the two components.
10. Interpret mass as coupling left- and right-moving sectors.

## Notation Choices
- Use \(x\) as the displayed one-dimensional coordinate throughout the working notes; mention once that Susskind says \(dx\) may stand for all space.
- Use \(\nabla^2\) only in the opening Hamiltonian to match the lecture recap; switch to \(\partial_x^2\) in the explicit 1D derivations.
- In the QFT half, reserve \(\psi(x)\), \(\psi^\dagger(x)\) for field operators.
- Use \(\tilde\psi(p)\), \(\tilde\psi^\dagger(p)\) for momentum-space annihilation/creation operators.
- Use \(|\phi(t)\rangle\) for the many-body state vector; do not reuse \(\psi\) for the state.
- Keep density and counting operators in normal order: \(n(x)=\psi^\dagger(x)\psi(x)\).
- Follow the lecture convention that \(p\)-variables go with annihilation operators and \(q\)-variables go with creation operators in the delta-function derivation.
- In the relativistic half, switch to uppercase \(\Psi\) for the two-component Dirac wavefunction to avoid conflict with the earlier field operator \(\psi\).
- Use \(\psi_1\) for the right-moving component and \(\psi_2\) for the left-moving component in the massless limit.
- Adopt units \(\hbar=1\) throughout, and \(c=1\) in the relativistic section.
- Use \(p=-i\partial_x\) and \(E,H=i\partial_t\) in the one-particle equations.
- Fix the 1D Dirac matrices as \(\alpha=\sigma_3=\mathrm{diag}(1,-1)\) and \(\beta=\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix}\).

## Uncertain Mathematics
- The opening Hamiltonian is only partially visible in the frame; the full typeset version should remain transcript-backed, not frame-only.
- The oral discussion of Fourier normalization slips between \(\sqrt{2\pi}\) and \(2\pi\) bookkeeping; keep one convention consistently in the notes.
- In the momentum-space counting discussion, Susskind briefly slips on operator order and variable naming; final notes should keep daggers on the left and the \(p/q\) convention fixed.
- The combined two-species kinetic Hamiltonian for electron/proton fields is verbally garbled around masses and denominators; reconstruct only the obvious structure, not exact board wording.
- The generic \(H^2\) operator products around the decay example contain at least one student-flagged possible missing dagger; keep those formulas schematic unless re-derived cleanly.
- The electron-photon interaction operator is spoken rather than stabilized on the board; if included later, present it as schematic and not as a precisely transcript-fixed formula.
- The component form of the massive Dirac equation is partially garbled in the transcript; use frame-backed \(\alpha\), transcript-backed \(\beta\), and reconstruct the final pair cautiously.
- The Klein-Gordon equation is safest in the unsymmetrized operator form \(-\partial_t^2\psi=(-\partial_x^2+m^2)\psi\); avoid imposing a covariant sign convention not spelled out in lecture.
- The lecture does not solve the negative-energy problem; any final notes should stop short of implying otherwise.