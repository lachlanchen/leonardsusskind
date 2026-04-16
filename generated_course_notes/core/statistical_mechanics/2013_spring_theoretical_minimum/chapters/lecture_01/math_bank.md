# Math Bank
## Core Equations
- [visible] \(F(i)\,p(i)\)
- [visible] \(\dfrac{F(i)\,N(i)}{N}\)
- [transcript-backed] \(p(i)\ge 0\)
- [transcript-backed] \(\sum_i p(i)=1\)
- [transcript-backed] \(p(i)=\lim_{N\to\infty}\dfrac{N(i)}{N}\)
- [transcript-backed] \(\langle f\rangle=\sum_i f(i)\,p(i)\)
- [transcript-backed] \(\langle f\rangle=\lim_{N\to\infty}\dfrac{1}{N}\sum_i f(i)\,N(i)\)
- [transcript-backed] \(f(\text{heads})=+1\)
- [transcript-backed] \(f(\text{tails})=-1\)
- [transcript-backed] \(\langle f\rangle=0\) for a fair coin with the above assignment
- [visible] \(R\to B\)
- [visible] \(B\to Y\)
- [visible] \(Y\to G\)
- [visible] \(G\to O\)
- [visible] \(O\to P\)
- [visible] \(P\to R\)
- [standard reconstruction] \(R\to B\to Y\to G\to O\to P\to R\)
- [transcript-backed] \(p(R)=p(B)=p(Y)=p(G)=p(O)=p(P)=\dfrac{1}{6}\) for a single six-state cycle sampled at an unknown time
- [standard reconstruction] \(p(R)=p(B)=p(G)=\dfrac{p_{+}}{3}\)
- [standard reconstruction] \(p(Y)=p(O)=p(P)=\dfrac{p_{-}}{3}\)
- [transcript-backed] Good-law criterion: each state has one incoming arrow and one outgoing arrow
- [transcript-backed] Bad-law prototype: all states map to one state, schematically \(i\mapsto R\)
- [standard reconstruction] \(m\ddot x=-\gamma \dot x\)
- [transcript-backed] \(\dfrac{dE}{dt}=0\)
- [transcript-backed] \(\dfrac{dE_1}{dt}+\dfrac{dE_2}{dt}=0\)
- [transcript-backed] \(\dfrac{dE_1}{dt}=-\dfrac{dE_2}{dt}\)
- [transcript-backed] \(S=\log M\)
- [transcript-backed] \(S_{\max}=\log N\)
- [transcript-backed] \(S=-\sum_i p_i\log p_i\)
- [transcript-backed] \(\lim_{p\to 0^+} p\log p=0\)
- [transcript-backed] If \(p_i=\dfrac{1}{M}\) on \(M\) occupied states and \(p_i=0\) otherwise, then \(S=\log M\)
- [visible] \(P_i\) or \(P(i)\) as the graph-axis probability label, normalized in the notes as probability over states
- [visible] \(M\) as the width/occupied-span marker on the probability sketch
- [transcript-backed] \(S=n\log 2\) for \(n\) independent fair coins under complete ignorance
- [transcript-backed] \(S=0\) for complete knowledge of the state
- [transcript-backed] \(S=\log n\) for \(n\) coins with exactly one tail at unknown position
- [transcript-backed] \(S=\log V_{\Gamma}\) for a uniform occupied blob in phase space
- [transcript-backed] \(\int_{\Gamma} P\,d\Gamma =1\)
- [transcript-backed] \(S=-\int_{\Gamma} P\log P\,d\Gamma\)
- [transcript-backed] Liouville statement in lecture form: phase-space volume of the occupied region is preserved under allowed dynamics

## Definitions And Objects
- State label \(i\): element of a discrete space of outcomes or microscopic states.
- Probability \(p(i)\) or \(p_i\): probability assigned to state \(i\).
- \(N(i)\): number of trials or replicas yielding outcome \(i\).
- \(N\): total number of trials in the frequency discussion; later also total number of states in the entropy discussion. This must be normalized in the final notes.
- \(f(i)\): any quantity assigned to state \(i\).
- \(\langle f\rangle\): average of \(f\) over the probability distribution.
- Occupied states: states with nonzero probability, in the equal-probability setup.
- \(M\): number of occupied states in the discrete equal-probability setup; later also the schematic width/span of the drawn probability distribution.
- \(N\) in entropy discussion: total number of available states.
- Closed system: system isolated enough that the external world does not affect its evolution.
- Conservation law in discrete toy models: partition of configuration space into disjoint cycles that the dynamics cannot leave.
- Plus/minus sectors: two disconnected cycles labeled by a conserved quantity such as \(+1\) and \(-1\).
- Minus first law: Susskind’s name for conservation of information.
- Good law: reversible/update law with one arrow in and one arrow out of each state.
- Bad law: law that merges distinct initial states and loses track of where the system came from.
- Phase space \(\Gamma\): space of coordinates and momenta.
- \(d\Gamma\): phase-space volume element.
- Probability density \(P\): probability per unit cell in phase space.
- Occupied patch/blob: phase-space region with nonzero probability density.
- Entropy \(S\): function of a probability distribution, not a bare microscopic observable like energy or momentum.
- Correlation: learning the state of one part changes the probability distribution for another part.
- Additivity of entropy: valid for uncorrelated systems in the lecture’s closing remarks.

## Derivation Steps
1. Probability from frequencies
   1. Start with many repeated trials or many replicas.
   2. Count how many times outcome \(i\) occurs: \(N(i)\).
   3. Divide by the total number of trials \(N\).
   4. Take the large-\(N\) limit.
   5. Identify the limiting ratio with \(p(i)\).

2. Expectation value formula
   1. Assign a quantity \(f(i)\) to each state.
   2. Weight each value by the probability of the corresponding state.
   3. Sum over all states.
   4. Obtain \(\langle f\rangle=\sum_i f(i)p(i)\).
   5. In frequency language, replace \(p(i)\) by \(N(i)/N\) in the large-\(N\) limit.

3. Equal probability on a single cycle
   1. Assume deterministic evolution through a six-state closed cycle.
   2. Assume each step occupies the same discrete time interval.
   3. Sample the system at an unknown instant.
   4. The system spends equal fractions of time in each state.
   5. Therefore each state has probability \(1/6\).

4. Probabilities on disconnected cycles
   1. Split the six states into two disconnected three-cycles.
   2. Within a chosen cycle, equal-time sampling gives probability \(1/3\) for each state in that cycle.
   3. Dynamics alone does not determine the probability of being in the \(+\) cycle or the \(-\) cycle.
   4. Introduce prior sector probabilities \(p_{+}\) and \(p_{-}\).
   5. Multiply the within-cycle \(1/3\) by the sector prior to get per-state probabilities.

5. Information conservation in the equal-probability discrete setup
   1. Start with \(M\) occupied states, each of probability \(1/M\), and \(N-M\) unoccupied states.
   2. Evolve with an allowed law that preserves distinctions between states.
   3. States may reshuffle, but they cannot merge.
   4. Therefore the number of occupied states remains \(M\).
   5. Equal probabilities remain equal under the reshuffling.

6. Entropy as \(\log M\) in the equal-probability case
   1. Identify \(M\) occupied states of equal probability.
   2. Interpret larger \(M\) as greater ignorance.
   3. Define entropy for that special case by \(S=\log M\).
   4. Read off special values: \(M=1\Rightarrow S=0\), \(M=N\Rightarrow S=\log N\).

7. General entropy formula reduces to \(\log M\)
   1. Start from \(S=-\sum_i p_i\log p_i\).
   2. For unoccupied states, use \(p_i=0\).
   3. Use \(\lim_{p\to 0^+}p\log p=0\) so those terms vanish.
   4. For occupied states, set \(p_i=1/M\).
   5. Each occupied term becomes \(-\dfrac{1}{M}\log\dfrac{1}{M}\).
   6. There are \(M\) identical terms.
   7. The factor of \(M\) cancels the \(1/M\).
   8. Use \(\log(1/M)=-\log M\).
   9. Obtain \(S=\log M\).

8. Why the minus sign appears in \(S=-\sum_i p_i\log p_i\)
   1. For probabilities \(0<p_i<1\), the logarithm is negative.
   2. Without an overall minus sign, the sum would be nonpositive.
   3. Insert the minus sign so entropy is nonnegative in the intended cases.

9. Continuous phase-space entropy from the discrete formula
   1. Replace discrete states by points in phase space.
   2. Replace probabilities by a probability density \(P\).
   3. Replace the sum over states by an integral over phase space.
   4. Keep the same algebraic structure as in the discrete formula.
   5. Obtain \(S=-\int_{\Gamma}P\log P\,d\Gamma\).

10. Uniform blob in phase space
   1. Assume \(P\) is constant on an occupied phase-space region and zero outside.
   2. Normalize \(P\) by \(\int_{\Gamma}P\,d\Gamma=1\).
   3. The relevant analog of the discrete count \(M\) is the phase-space volume \(V_{\Gamma}\) of the blob.
   4. In this simple case, identify the entropy as \(S=\log V_{\Gamma}\).

11. Additive-energy two-subsystem relation
   1. Assume a closed system composed of two interacting parts.
   2. Under the additive-energy approximation, write \(E=E_1+E_2\).
   3. Differentiate with respect to time.
   4. Use total energy conservation \(dE/dt=0\).
   5. Conclude \(dE_1/dt=-dE_2/dt\).

12. Correlation example with one unknown tail
   1. Start with \(n\) coins and the information that exactly one is tails.
   2. Before any measurement, each coin is equally likely to be the tail.
   3. Measure one coin.
   4. If it is tails, all others are known to be heads.
   5. If it is heads, the tail must lie among the remaining \(n-1\) coins.
   6. Update the probability for each remaining coin to \(1/(n-1)\).
   7. Use this as the lecture’s model of correlation.

## Notation Choices
- Use \(p(i)\) and \(p_i\) interchangeably only when matching the lecture; prefer \(p_i\) inside sums and \(p(i)\) in explanatory prose.
- Use \(i\) for discrete microscopic states throughout the discrete part.
- Reserve \(n\) for the number of coins in the coin examples.
- Reserve \(N\) for the total number of discrete states in the entropy discussion.
- In the frequency discussion, if \(N\) is already needed for total states later, rename the total number of trials to \(N_{\text{trials}}\) or state explicitly that the letter is being reused in the lecture.
- Use \(M\) for the number of occupied states in the equal-probability entropy setup.
- In the graph figure, label the vertical axis by \(P_i\) or \(p_i\); prefer \(p_i\) in the final notes for consistency with the entropy formula unless figure styling strongly prefers uppercase.
- Use \(\langle f\rangle\) for expectation values, matching Susskind’s bracket notation.
- Use \(E_i\) when explicitly referring to energy as a function of state.
- Use \(\Gamma\) for phase space and \(d\Gamma\) for its volume element.
- Use \(P(\Gamma)\) or \(P(x,p)\) only when necessary; otherwise use \(P\) for the phase-space density and define it once.
- Normalize the transcript’s slips between \(x\) and \(q\) by using coordinates \(q\) or \(x\) consistently and momenta \(p\); the lecture explicitly permits either coordinate letter.
- Normalize “Leoville” to `Liouville`.
- State explicitly that “entropy” here is attached to a probability distribution, not to a pure microstate by itself.
- If the two disconnected cycles are used in equations, denote their prior weights by \(p_{+}\) and \(p_{-}\) with \(p_{+}+p_{-}=1\).

## Uncertain Mathematics
- The discussion around 00:32:34–00:33:24 is garbled. The safe mathematical content is only:
  - sector probabilities do not follow from the within-cycle dynamics alone;
  - within a chosen three-cycle, probabilities are \(1/3\) each;
  - overall per-state probabilities are sector prior times \(1/3\).
- The friction differential equation around 00:46:04–00:46:48 is not reliably transcribed. The cautious final-note version should use a standard viscous-drag form such as \(m\ddot x=-\gamma \dot x\) and explain that it is a reconstruction of the example, not a verbatim board equation.
- The projection argument around 01:03:20–01:05:20 is conceptually clear but textually garbled. The safe claim is that apparent collapse in visible variables is a projection of a higher-dimensional volume-preserving evolution.
- In the equal-probability rectangular graph discussion, the transcript momentarily says the probability is \(1/n\) where the width marker is really the number of occupied states \(M\). The final notes should normalize this to \(1/M\) for the occupied states.
- The graph-axis label in `lecture_01_figure_05.png` and `lecture_01_figure_06.png` is not perfectly sharp. It should be normalized from the transcript as probability over state labels, not treated as an exact pixel-level transcription.
- The visible `S=\cdots` near the probability graph is too cropped to use as image evidence. Any displayed entropy formula there must come from the transcript, not the screenshot.
- In the phase-space section, Susskind briefly slips between \(x\) and \(q\). This should be cleaned in the final notes without making it sound like two distinct constructions.
- The transcript phrase about the units of phase-space volume is unstable and partly malformed. Do not overstate dimensional-analysis details there unless independently checked.
- The late discussion of Boltzmann versus Shannon is partly garbled. The secure mathematical content is only:
  - same entropy formula up to logarithm base and sign convention;
  - no direct relation to Heisenberg uncertainty is intended here.