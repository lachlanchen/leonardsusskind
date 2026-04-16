# Math Bank
## Core Equations
- [visible] \(S=-\sum_i P(i)\log P(i)\)
- [visible] \(\sum_i P(i)=1\)
- [visible] \(\sum_i P(i)E(i)=\langle E\rangle\)
- [standard reconstruction] For the equilibrium family under discussion, \(S\) is a monotonically increasing function of average energy: \(\dfrac{dS}{d\langle E\rangle}>0\)
- [transcript-backed] \(dE_A+dE_B=0\)
- [transcript-backed] \(dS_A+dS_B\ge 0\)
- [transcript-backed] \(dE=T\,dS\)
- [transcript-backed] \(dE_A=T_A\,dS_A,\qquad dE_B=T_B\,dS_B\)
- [transcript-backed] \(T_A\,dS_A+T_B\,dS_B=0\)
- [standard reconstruction] \(dS_B=-\dfrac{T_A}{T_B}\,dS_A\)
- [standard reconstruction] \(\left(1-\dfrac{T_A}{T_B}\right)dS_A\ge 0\)
- [standard reconstruction] \((T_B-T_A)dS_A\ge 0\) for \(T_B>0\)
- [transcript-backed] If \(T_B>T_A\), then \(dS_A>0\), hence \(dE_A=T_A\,dS_A>0\)
- [transcript-backed] Equilibrium condition: \(T_A=T_B\)
- [visible] \(P(i)=\dfrac{n_i}{N}\)
- [transcript-backed] \(\sum_i n_i=N\)
- [transcript-backed] \(\sum_i n_i e_i = N E\)
- [transcript-backed] \(n_i=NP_i\)
- [transcript-backed] \(\sum_i P_i=1\)
- [transcript-backed] \(\sum_i P_i E_i=E\)
- [transcript-backed] \(C=\dfrac{N!}{\prod_i n_i!}\)
- [transcript-backed] \(0!=1\)
- [transcript-backed] \(N!\approx N^N e^{-N}\)
- [transcript-backed] \(\log N!\approx \sum_{x=1}^N \log x\)
- [transcript-backed] \(\log N!\approx \int_1^N \log x\,dx\)
- [transcript-backed] \(\int \log x\,dx = x\log x-x\)
- [transcript-backed] \(\log N!\approx N\log N-N\)
- [standard reconstruction] \(C\approx \dfrac{N^N}{\prod_i n_i^{\,n_i}}\)
- [standard reconstruction] \(\log C = N\log N-\sum_i n_i\log n_i\)
- [transcript-backed] \(\log(P_iN)=\log P_i+\log N\)
- [transcript-backed] \(e^{N\log N}=N^N\)
- [standard reconstruction] \(\log C=-N\sum_i P_i\log P_i=NS\)
- [transcript-backed] Maximize \(S(P_i)=-\sum_i P_i\log P_i\) subject to \(\sum_i P_i=1\) and \(\sum_i P_iE_i=E\)
- [transcript-backed] Unconstrained stationarity: \(\dfrac{\partial F}{\partial x_i}=0\)
- [transcript-backed] One-constraint Lagrange setup: \(F'=F+\lambda G\)
- [transcript-backed] Worked example: \(F=\dfrac{x^2+y^2}{2},\qquad G=x+y-1\)
- [transcript-backed] \(F'=\dfrac{x^2+y^2}{2}+\lambda(x+y-1)\)
- [transcript-backed] \(\dfrac{\partial F'}{\partial x}=x+\lambda=0,\qquad \dfrac{\partial F'}{\partial y}=y+\lambda=0\)
- [transcript-backed] \(x=y=-\lambda\)
- [transcript-backed] \(x+y=1\Rightarrow -2\lambda=1\Rightarrow \lambda=-\dfrac12\)
- [transcript-backed] \(x=y=\dfrac12\)
- [transcript-backed] With several constraints, \(F'=F+\lambda_1G_1+\lambda_2G_2+\cdots\), together with \(G_a=0\)

## Definitions And Objects
- A state \(i\): as much as can be known about the system by an “infinitely powerful” observer, subject to the laws of physics.
- Probability distribution \(P(i)\) or \(P_i\): probability that the system is in state \(i\).
- State energy \(E(i)\) or \(E_i\): energy assigned to state \(i\).
- Average energy: \(\langle E\rangle=\sum_i P(i)E(i)\); later the lecture also writes the fixed average energy simply as \(E\).
- Entropy of a distribution: \(S=-\sum_i P_i\log P_i\).
- One-parameter equilibrium family: a family of distributions indexed by average energy; the board picture shows them broadening and shifting toward larger \(E\).
- Thermal equilibrium: a state in which heat does not flow; for a composite system, all parts have the same temperature.
- Temperature: introduced through the rate of change of energy with entropy, in differential form \(dE=T\,dS\).
- Heat bath / reservoir: a much larger system whose temperature changes negligibly when a small amount of energy is exchanged.
- Replica construction: replace the bath by \(N\) identical subsystems, one of which is the subsystem of interest.
- Occupation number \(n_i\): number of replicas occupying state \(i\).
- Multiplicity \(C\): number of arrangements of replicas realizing a fixed set \(\{n_i\}\).
- Coarse-graining: deliberate loss of detailed information; used to motivate broadening of probability distributions.

## Derivation Steps
Heat-flow derivation
1. Assume two subsystems \(A\) and \(B\) can exchange energy, with \(T_B>T_A\).
2. Use energy conservation: \(dE_A+dE_B=0\).
3. Use entropy increase: \(dS_A+dS_B\ge 0\).
4. Apply \(dE=T\,dS\) to each subsystem: \(dE_A=T_A dS_A\), \(dE_B=T_B dS_B\).
5. Substitute into energy conservation: \(T_A dS_A+T_B dS_B=0\).
6. Solve for \(dS_B\): \(dS_B=-(T_A/T_B)dS_A\).
7. Insert into the entropy inequality: \(dS_A-(T_A/T_B)dS_A\ge 0\).
8. Multiply by \(T_B>0\): \((T_B-T_A)dS_A\ge 0\).
9. Since \(T_B-T_A>0\), conclude \(dS_A>0\).
10. Multiply by \(T_A\): \(dE_A=T_A dS_A>0\).
11. Therefore subsystem \(A\) gains energy and \(B\) loses it: heat flows from hotter to colder.
12. When \(T_A=T_B\), the argument gives no further net flow; this is equilibrium.

Constraint rewrite from occupation numbers to probabilities
1. Define \(P_i=n_i/N\), so \(n_i=NP_i\).
2. Start from the number constraint \(\sum_i n_i=N\).
3. Substitute \(n_i=NP_i\): \(\sum_i NP_i=N\).
4. Divide by \(N\): \(\sum_i P_i=1\).
5. Start from the energy constraint \(\sum_i n_i e_i=NE\).
6. Substitute \(n_i=NP_i\): \(\sum_i NP_i e_i=NE\).
7. Divide by \(N\): \(\sum_i P_i e_i=E\).
8. Read \(E\) as the average energy per subsystem.

Multiplicity to entropy
1. For fixed occupation numbers, write the multiplicity as \(C=\dfrac{N!}{\prod_i n_i!}\).
2. Use \(0!=1\) to ignore unoccupied levels in the denominator.
3. Apply the simplified Stirling approximation to numerator and denominator.
4. Obtain \(C\approx \dfrac{N^N e^{-N}}{\prod_i n_i^{\,n_i} e^{-n_i}}\).
5. Use \(\sum_i n_i=N\) to cancel the exponential factors.
6. Get \(C\approx \dfrac{N^N}{\prod_i n_i^{\,n_i}}\).
7. Take the logarithm: \(\log C = N\log N-\sum_i n_i\log n_i\).
8. Substitute \(n_i=NP_i\).
9. Expand \(\log(NP_i)=\log N+\log P_i\).
10. Use \(\sum_i P_i=1\) to cancel the \(N\log N\) terms.
11. Arrive at \(\log C=-N\sum_i P_i\log P_i=NS\).
12. Therefore maximizing multiplicity is equivalent to maximizing entropy.

Lagrange-multiplier method in the worked example
1. Start with \(F=\dfrac{x^2+y^2}{2}\) and the constraint \(G=x+y-1=0\).
2. Form \(F'=F+\lambda G\).
3. Treat \(\lambda\) temporarily as an unknown constant and extremize \(F'\).
4. Set \(\partial F'/\partial x=0\) and \(\partial F'/\partial y=0\).
5. Get \(x+\lambda=0\) and \(y+\lambda=0\), hence \(x=y=-\lambda\).
6. Impose the original constraint \(x+y=1\).
7. Solve \(-2\lambda=1\), so \(\lambda=-1/2\).
8. Conclude \(x=y=1/2\).
9. General rule: for several constraints, add one multiplier per constraint and solve the stationarity equations together with all \(G_a=0\).

## Notation Choices
- Preserve the board notation \(P(i)\), \(E(i)\), and \(\langle E\rangle\) when directly discussing the screenshot.
- In cleaned derivations, standardize to \(P_i\) and \(E_i\) unless a local quotation from the board is being described.
- Use \(E\) for the fixed average energy per subsystem in the replica section, but explicitly identify it once with \(\langle E\rangle\) to avoid an apparent symbol change.
- Keep \(N\) for the total number of replicas / subsystems and \(n_i\) for occupation numbers.
- Keep \(C\) for the combinatorial multiplicity, since Susskind explicitly names it.
- Keep \(\log\) rather than switching to \(\ln\), unless the surrounding document already enforces \(\ln\).
- Write entropy as \(S(P_i)\) or \(S(\{P_i\})\) when emphasizing it as a function to be maximized.
- In the heat-flow derivation, use \(dE=T\,dS\) exactly as the lecture phrases it, not \(T=\partial E/\partial S\) as the main displayed form.
- For the constrained optimization problem, put constraints in zero form when introducing Lagrange multipliers:
  \(G_1=\sum_i P_i-1=0\), \(G_2=\sum_i P_iE_i-E=0\).

## Uncertain Mathematics
- The lecture strongly asserts monotonic growth of entropy with average energy only for the equilibrium family of distributions under discussion; it should not be stated as a theorem about arbitrary distributions.
- The ground-state distribution is described verbally as all probability concentrated at the minimum energy; a formula like \(P_i=\delta_{i,i_0}\) is only safe if nondegeneracy is explicitly assumed.
- The board writes \(E(i)\), while the later derivations naturally read better with \(E_i\); that is notation cleanup, not literal transcription.
- The simplified Stirling form \(N!\approx N^N e^{-N}\) omits endpoint corrections and the usual \(\sqrt{2\pi N}\) prefactor; the lecture explicitly treats those as subleading.
- Using Stirling in the denominator is justified only in the large-\(N\) regime where the relevant \(n_i\) scale proportionally with \(N\); this is argued heuristically in the lecture, not proved sharply.
- The algebra from \(\log C\) to \(NS\) is spoken somewhat loosely; the cleaned derivation should be presented as a cautious reconstruction of the intended steps.
- The sign discussion around entropy should be handled carefully: \(\log P_i<0\) for \(0<P_i<1\), so \(-P_i\log P_i>0\).
- The transcript is garbled around approximately `01:24` and again around `01:27`; those stretches should not be used as primary evidence for any new formula.