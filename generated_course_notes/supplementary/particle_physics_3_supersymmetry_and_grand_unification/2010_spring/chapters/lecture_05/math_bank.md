# Math Bank
## Core Equations
- \(\epsilon_i\epsilon_j+\epsilon_j\epsilon_i=0\) [transcript-backed]
- \(\epsilon_i^2=0\) [transcript-backed]
- \(\text{odd}\cdot\text{odd}=\text{even},\qquad \text{odd}\cdot\text{even}=\text{odd},\qquad \text{even}\cdot\text{even}=\text{even}\) [transcript-backed]
- \(f(\epsilon)=a+b\,\epsilon\) [transcript-backed]
- \(f(\epsilon_1,\epsilon_2)=a+b_1\epsilon_1+b_2\epsilon_2+c\,\epsilon_1\epsilon_2\) [transcript-backed]
- \(f(\theta,\bar\theta)=a+\bar b\,\theta+\bar\theta\,b+c\,\bar\theta\theta\) [standard reconstruction]
- \(\partial_\theta a=0\) [transcript-backed]
- \(\partial_\theta(a+\theta b)=b\) [transcript-backed]
- \(\{\partial_\theta,\theta\}=1\) [transcript-backed]
- \([\partial_x,x]=1\) [transcript-backed]
- \(\int d\theta\,f(\theta)=\partial_\theta f(\theta)\) [transcript-backed]
- \([G_i,G_j]=i\,c_{ijk}G_k\) [transcript-backed]
- \([H,G_i]=0\) [transcript-backed]
- \([a_+,a_+]=[a_-,a_-]=0,\qquad [a_-,a_+]=1\) [transcript-backed]
- \(\{c_+,c_+\}=\{c_-,c_-\}=0,\qquad \{c_-,c_+\}=1\) [transcript-backed]
- \(c_+^2=c_-^2=0\) [transcript-backed]
- \([a_\pm,c_\pm]=0\) and, more generally, every \(a\) commutes with every \(c\) [transcript-backed]
- \(Q=\sqrt{m}\,a_+c_-\) [transcript-backed]
- \(\bar Q=Q^\dagger=\sqrt{m}\,a_-c_+\) [transcript-backed]
- \(\{Q,\bar Q\}=H\) [visible]
- \(\{Q,Q\}=0,\qquad \{\bar Q,\bar Q\}=0\) [transcript-backed]
- \(N_B=a_+a_-,\qquad N_F=c_+c_-\) [transcript-backed]
- \(H=m(N_B+N_F)=m(a_+a_-+c_+c_-)\) [transcript-backed]
- \([Q,H]=0\) [transcript-backed]
- \(\frac{\partial}{\partial t}|\psi\rangle\) [standard reconstruction]
- \(i\,\frac{\partial}{\partial t}|\psi\rangle=H|\psi\rangle\) [standard reconstruction]
- \(e^{-iH\delta}\,|\psi(t)\rangle=|\psi(t+\delta)\rangle\) [standard reconstruction]
- \(t\to t+\delta\) [standard reconstruction]
- \(\psi(\theta,\bar\theta,t)\to \psi(\theta,\bar\theta,t)+\delta\,\frac{\partial\psi(\theta,\bar\theta,t)}{\partial t}\) [standard reconstruction]
- \(\theta\to\theta+\epsilon\) [transcript-backed]
- \(t\to t+i\,\bar\theta\,\epsilon\) [transcript-backed]
- \(\delta\psi=\epsilon\,\partial_\theta\psi-i\,\epsilon\,\bar\theta\,\partial_t\psi\) [standard reconstruction]
- \(q=\partial_\theta-i\,\bar\theta\,\partial_t\) [standard reconstruction]
- \(\bar q=\partial_{\bar\theta}+i\,\theta\,\partial_t\) [standard reconstruction]
- \(\{q,\bar q\}\propto \partial_t\) [transcript-backed]
- \(\{q,\bar q\}=-\,i\,\partial_t\) up to normalization/sign convention [standard reconstruction]

## Definitions And Objects
- Grassmann variables: \(\epsilon_i,\theta,\bar\theta\); these are odd elements.
- Ordinary numbers: \(n,m,\ldots\); these are even elements.
- Even object: commutes with both even and odd elements.
- Odd object: anticommutes with other odd elements.
- Function of finitely many Grassmann variables: always a finite polynomial because higher powers vanish.
- Even function vs odd function: coefficients must alternate parity so that each term has the same total parity.
- Left Grassmann derivative convention: before differentiating with respect to \(\theta\), move the relevant \(\theta\) next to the derivative; sign changes come from moving odd elements past odd elements.
- Continuous symmetry generators: \(G_i\), with closure encoded by commutators.
- Bosonic creation/annihilation operators: \(a_+,a_-\); even operators.
- Fermionic creation/annihilation operators: \(c_+,c_-\); odd operators.
- Supercharges in the oscillator model: \(Q,\bar Q\); odd generators exchanging bosons and fermions.
- Number operators in the toy model: \(N_B=a_+a_-\), \(N_F=c_+c_-\).
- Hamiltonian in the toy model: total rest energy of bosons plus fermions, assuming equal masses.
- Superspace wavefunction / field-like object: \(\psi(\theta,\bar\theta,t)\).
- Grassmann shift parameter: \(\epsilon\); odd, nilpotent, and therefore automatically “small” in the sense that \(\epsilon^2=0\).
- Differential-operator realization: lowercase \(q,\bar q\) acting on \(\psi(\theta,\bar\theta,t)\).

## Derivation Steps
1. `\{\partial_\theta,\theta\}=1`: start with a test function \(f(\theta)=a+b\theta\), with \(a\) even and \(b\) odd in the even case Susskind works out.
2. `\{\partial_\theta,\theta\}=1`: compute \(\theta\,\partial_\theta f\); since \(\partial_\theta f=b\), this gives \(\theta b=b\theta\) after the odd-odd sign is accounted for.
3. `\{\partial_\theta,\theta\}=1`: compute \(\partial_\theta(\theta f)=\partial_\theta(\theta a+\theta b\theta)\).
4. `\{\partial_\theta,\theta\}=1`: the \(\theta b\theta\) term vanishes because \(\theta^2=0\), so \(\partial_\theta(\theta f)=a\).
5. `\{\partial_\theta,\theta\}=1`: add the two orders; the result is \(a+b\theta=f\), hence \(\{\partial_\theta,\theta\}=1\).
6. `\{Q,\bar Q\}=H`: write \(Q\bar Q+\bar Q Q = m(a_+c_-a_-c_+ + a_-c_+a_+c_-)\).
7. `\{Q,\bar Q\}=H`: commute all \(a\)’s past all \(c\)’s, since even and odd operators commute with each other.
8. `\{Q,\bar Q\}=H`: rewrite as \(m(a_+a_-c_-c_+ + a_-a_+c_+c_-)\).
9. `\{Q,\bar Q\}=H`: use the fermionic anticommutator to combine \(c_-c_+ + c_+c_- = 1\), and the bosonic commutator to replace \(a_-a_+ - a_+a_- = 1\).
10. `\{Q,\bar Q\}=H`: identify the remaining pieces as boson and fermion number operators.
11. `\{Q,\bar Q\}=H`: multiply by the common mass \(m\) to obtain the total rest energy \(H=m(N_B+N_F)\).
12. `\{Q,Q\}=0`: \(Q^2\) contains \(c_-^2\), and \(c_-^2=0\), so the anticommutator of \(Q\) with itself vanishes.
13. `\{\bar Q,\bar Q\}=0`: similarly, \(\bar Q^2\) contains \(c_+^2\), hence vanishes.
14. `\([Q,H]=0\)`: act with \(QH-HQ\) on an energy eigenstate \(|E\rangle\).
15. `\([Q,H]=0\)`: if boson and fermion masses are equal, \(Q\) replaces one particle by another of the same mass, so \(Q|E\rangle\) has the same energy \(E\).
16. `\([Q,H]=0\)`: therefore \(HQ|E\rangle = E\,Q|E\rangle\), while \(QH|E\rangle = Q(E|E\rangle)=E\,Q|E\rangle\).
17. `\([Q,H]=0\)`: the two actions agree on every energy eigenstate; assuming the energy eigenstates form a complete basis, \([Q,H]=0\) as an operator.
18. Superspace generator: start from \(\psi(\theta,\bar\theta,t)\) and shift \(\theta\to\theta+\epsilon\), giving \(\delta\psi=\epsilon\,\partial_\theta\psi\) at first order.
19. Superspace generator: simultaneously shift \(t\to t+i\bar\theta\epsilon\), giving an additional contribution proportional to \(\epsilon\,\bar\theta\,\partial_t\psi\).
20. Superspace generator: factor out \(\epsilon\) and read the coefficient as an odd differential operator \(q\).
21. Superspace anticommutator: pair \(q\) with its conjugate \(\bar q\), containing \(\partial_{\bar\theta}\) and a \(\theta\,\partial_t\) term.
22. Superspace anticommutator: the derivative-derivative term vanishes, and the odd-coordinate–odd-coordinate term also vanishes.
23. Superspace anticommutator: the mixed terms survive because \(\{\partial_\theta,\theta\}=1\) and \(\{\partial_{\bar\theta},\bar\theta\}=1\).
24. Superspace anticommutator: the net result is proportional to \(\partial_t\), which Susskind identifies with the time-translation generator and hence with \(H\), up to sign and normalization conventions.

## Notation Choices
- Use \(\bar Q\) as the main notation in the chapter, with one sentence noting that Susskind also says \(Q^\dagger\).
- Reserve uppercase \(Q,\bar Q\) for the oscillator / creation-annihilation realization.
- Reserve lowercase \(q,\bar q\) for the differential-operator realization on superspace.
- Use \(a_+,a_-\) and \(c_+,c_-\) exactly as in the lecture, not \(a^\dagger,a\) or \(b^\dagger,b\).
- Use \(\theta,\bar\theta\) for the Grassmann pair in the later part of the lecture; earlier \(\epsilon_i\) may be used in the review section.
- Use bars for complex conjugation in the Grassmann pair: \(\bar\theta\), \(\bar Q\), \(\bar b\).
- Use the left-derivative convention for \(\partial_\theta\) and \(\partial_{\bar\theta}\), with explicit note that one reorders factors before differentiating.
- Use \(H\) for the Hamiltonian and explicitly identify it as the generator of time translations.
- Use \(\delta\) for the ordinary small time shift, matching the board/transcript.
- Use \(\epsilon\) for the Grassmann shift parameter in superspace.
- When the chapter discusses energy-eigenstate arguments, use \(|E\rangle\) for an eigenstate and \(E\) for the eigenvalue.
- Keep the relation to time evolution anchored by \(i\,\partial_t|\psi\rangle=H|\psi\rangle\); treat bare identifications of \(H\) with \(\pm i\partial_t\) as convention-sensitive.

## Uncertain Mathematics
- The complex-pair expansion \(f(\theta,\bar\theta)=a+\bar b\,\theta+\bar\theta\,b+c\,\bar\theta\theta\) is the natural reconstruction, but the transcript is garbled at that point; if used, it should not be described as fully verbatim.
- The explicit derivatives of the two-variable Grassmann function depend on parity assignment and order convention; the lecture’s sign bookkeeping is clear in spirit but not always clean in transcription.
- The add-and-subtract manipulation inside the \(\{Q,\bar Q\}\) calculation is garbled in the transcript; preserve the setup, operator rearrangement, and final result, but do not overclaim intermediate algebraic wording.
- The board only visibly supports \(\{Q\,\bar Q\}=H\), not the whole derivation of that relation.
- The board only partially supports \(\frac{\partial}{\partial t}|\psi\rangle\); the full Schrödinger equation is transcript-backed and standard-completed.
- The board supports the time-shift structure, but the full argument list \(\psi(\theta,\bar\theta,t)\) is partly transcript-supplied.
- The superspace generator formulas \(q=\partial_\theta-i\bar\theta\partial_t\) and \(\bar q=\partial_{\bar\theta}+i\theta\partial_t\) are standard reconstructions; Susskind explicitly says he may have the sign wrong.
- The factor of \(2\) in \(\{q,\bar q\}\) is explicitly unstable in the lecture; he flags that the normalization may need adjustment.
- The identification of the superspace anticommutator with \(H\) should be stated as “proportional to the time-translation generator” unless a convention is fixed explicitly.
- The relation between \(H\) and \(\pm i\partial_t\) is loose in the late superspace discussion; use the Schrödinger equation as the safest anchor and avoid forcing an unqualified sign claim.