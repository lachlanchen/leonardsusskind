# Math Bank
## Core Equations
- [transcript-backed] For two particles constrained to one half of the room, the relevant fraction of configuration space is `\frac{1}{4}`.
- [transcript-backed] For `N` particles constrained to one half of the room, the relevant fraction is `\left(\frac{1}{2}\right)^N`.
- [transcript-backed] More generally, if all particles lie in a smaller spatial region of volume `v` inside a box of volume `V`, the fraction is
  `\left(\frac{v}{V}\right)^N`.
- [transcript-backed] The recurrence time is estimated as inverse probability:
  `\tau_{\mathrm{rec}} \sim \left(\frac{V}{v}\right)^N`.
- [transcript-backed] In entropy language, Susskind states the probability is proportional to
  `e^{-S_{\mathrm{eq}}}`.
- [visible] `n=\#\text{ of ups}, \qquad m=\#\text{ of downs}, \qquad n+m=N`.
- [visible] `E=(n-m)\mu H`.
- [transcript-backed] The multiplicity for fixed `n,m` is
  `\Omega(n,m)=\frac{N!}{n!\,m!}`.
- [visible] The partition function is written in board form as
  `Z=\sum e^{-\beta\mu H(n-m)}`.
- [visible] `x=e^{-\beta\mu H}, \qquad y=e^{+\beta\mu H}`.
- [standard reconstruction] The partition function in combinatorial form is
  `Z=\sum_{n=0}^{N}\frac{N!}{n!(N-n)!}x^n y^{N-n}`.
- [standard reconstruction] Binomial simplification:
  `Z=(x+y)^N`.
- [standard reconstruction] Restoring `x,y`,
  `Z=(e^{-\beta\mu H}+e^{+\beta\mu H})^N`.
- [standard reconstruction] Hyperbolic-function form:
  `Z=2^N\cosh^N(\beta\mu H)`.
- [visible] Corrected magnetization definition on the board:
  `M=\left\langle \frac{n-m}{N}\right\rangle`.
- [visible] Energy rewritten in terms of magnetization:
  `E=NM\mu H`.
- [transcript-backed] Thermodynamic identity:
  `\langle E\rangle=-\frac{\partial}{\partial\beta}\log Z`.
- [standard reconstruction] From the derived `Z`,
  `\langle E\rangle=-N\mu H\,\tanh(\beta\mu H)`.
- [transcript-backed] Therefore
  `M=-\tanh(\beta\mu H)`.
- [transcript-backed] Hyperbolic-function identities used in the lecture:
  `\cosh x=\frac{e^x+e^{-x}}{2}, \qquad \sinh x=\frac{e^x-e^{-x}}{2}, \qquad \tanh x=\frac{\sinh x}{\cosh x}`.
- [transcript-backed] Limiting behavior used in the plot discussion:
  `\tanh x \to 1 \text{ as } x\to+\infty, \qquad \tanh x \sim x \text{ near } x=0`.
- [visible] Two-spin Ising interaction:
  `E=-J\,\sigma_{(1)}\sigma_{(2)}`.
- [transcript-backed] One-dimensional nearest-neighbor extension:
  `E=-J\sum_n \sigma_n \sigma_{n+1}`.
- [transcript-backed] Global spin-flip symmetry:
  `\sigma_i \mapsto -\sigma_i \quad \text{for all } i`.

## Definitions And Objects
- Phase space: space of all particle coordinates and momenta; described in the lecture as `6N`-dimensional.
- Configuration-space volume for the gas: if the box volume is `V`, the full configuration-space volume scales as `V^N`.
- Special subregion volume for the gas: if the allowed spatial subregion has volume `v`, the corresponding configuration-space subregion scales as `v^N`.
- `N`:
  total number of particles in the gas discussion;
  total number of spins in the magnet discussion.
- `n`:
  number of up spins.
- `m`:
  number of down spins.
- `\sigma_i`:
  spin variable taking values `\pm 1`.
- `\mu`:
  magnetic moment of one spin.
- `H`:
  external magnetic field strength in the noninteracting spin model.
- `\mu H`:
  one-spin energy scale; Susskind often treats it as a single number for calculation.
- `Z`:
  partition function.
- `\beta`:
  inverse temperature; lecture uses `\beta=1/T` in effect.
- `M`:
  magnetization per spin, ultimately used as a Boltzmann average.
- `J`:
  Ising coupling constant; with the chosen minus sign, `J>0` favors aligned neighboring spins.
- Ground state:
  minimum-energy configuration.
- Symmetry in the Ising discussion:
  an operation on the spin variables that leaves the energy unchanged.

## Derivation Steps
Recurrence fraction and time
1. Start with two particles in one spatial dimension and ignore momentum.
2. Use coordinates `(x_1,x_2)` or `(x,y)` to describe the configuration.
3. The region where both particles lie in one half of the room occupies one quarter of the square.
4. Generalize: for `N` particles, the fraction becomes `\left(\frac{1}{2}\right)^N`.
5. Replace “half the room” by a smaller region of volume `v` inside a box of volume `V`.
6. Then the full configuration-space volume is `V^N` and the special region has volume `v^N`.
7. Therefore the fraction of time spent there is `\frac{v^N}{V^N}=\left(\frac{v}{V}\right)^N`.
8. Invert this small fraction to estimate the recurrence time.

Partition function for independent spins in an external field
1. Fix `n` up spins and `m` down spins with `n+m=N`.
2. Write the energy as `E=(n-m)\mu H`.
3. Count the number of configurations with those counts:
   `\Omega(n,m)=\frac{N!}{n!\,m!}`.
4. Sum Boltzmann weights over all configurations:
   `Z=\sum \Omega(n,m)e^{-\beta\mu H(n-m)}`.
5. Introduce `x=e^{-\beta\mu H}` and `y=e^{+\beta\mu H}`.
6. Rewrite the summand as `\Omega(n,m)x^n y^m`.
7. Use `m=N-n` and recognize the binomial expansion.
8. Conclude `Z=(x+y)^N=(e^{-\beta\mu H}+e^{+\beta\mu H})^N`.
9. Rewrite as `Z=2^N\cosh^N(\beta\mu H)`.

Average energy and magnetization
1. Use the thermodynamic identity `\langle E\rangle=-\partial_\beta \log Z`.
2. From `Z=2^N\cosh^N(\beta\mu H)`, drop the `N\log 2` term when differentiating.
3. Differentiate `N\log\cosh(\beta\mu H)` with respect to `\beta`.
4. Use `\frac{d}{dx}\log\cosh x=\tanh x` and the chain-rule factor `\mu H`.
5. Obtain `\langle E\rangle=-N\mu H\,\tanh(\beta\mu H)`.
6. Divide by `N\mu H` to extract magnetization.
7. Obtain `M=-\tanh(\beta\mu H)`.

Shape of the magnetization curve
1. Use `\tanh x=\sinh x/\cosh x`.
2. For large positive `x`, the `e^{-x}` terms are negligible in both `\sinh x` and `\cosh x`.
3. Therefore `\tanh x\to 1`, so `M\to -1` at low temperature.
4. Near `x=0`, expand `e^x` and `e^{-x}` to first order.
5. Then `\sinh x\sim x` and `\cosh x\sim 1`.
6. Therefore `\tanh x\sim x`, so `M\to 0` as `\beta\to 0`.

Sign choice for the Ising interaction
1. Start with a two-spin product `J\sigma_{(1)}\sigma_{(2)}`.
2. Notice that without the minus sign this is lower for anti-aligned spins.
3. Susskind wants aligned spins to have lower energy.
4. Insert an overall minus sign.
5. Obtain `E=-J\sigma_{(1)}\sigma_{(2)}`.
6. Extend to a chain by summing over neighboring pairs once.

## Notation Choices
- Use standard hyperbolic notation `\sinh`, `\cosh`, `\tanh`, not the transcript’s garbled phonetic spellings.
- Use `\langle \cdot \rangle` for Boltzmann/ensemble averages.
- In the magnet section, use `n` and `m` for up/down counts and `N` for the fixed total number of spins.
- Treat `M` as the average magnetization in the polished notes, so that `\langle E\rangle = N\mu H\,M` is the clean final relation.
- Keep `\mu H` explicit in displayed equations, because the board repeatedly uses that product; mention only in prose that one could combine it into a single parameter.
- Use `\sigma_i=\pm1` as the main notation in the prose derivation, while preserving `\sigma_{(1)}`, `\sigma_{(2)}` when referring directly to the board frame.
- In the Ising section, keep the explicit minus sign and take `J>0` so that “aligned spins lower energy” is transparent.
- Use `v` and `V` for small and large spatial volumes in the recurrence discussion, matching the lecture’s heuristic scaling argument.
- If the chapter mixes gas and spin sections closely, clarify locally that `N` is being reused in two different examples rather than introducing new symbols not motivated by the lecture.
- For the recurrence discussion, treat the formulas as configuration-space estimates unless the text explicitly returns to full phase space.

## Uncertain Mathematics
- The recurrence formulas are heuristic scaling estimates, not a formal Poincare theorem derivation; the lecture suppresses prefactors, measure-theoretic issues, and momentum dependence.
- `P\propto e^{-S_{\mathrm{eq}}}` is transcript-backed in spirit, but the exact normalization is not developed carefully and should be presented cautiously.
- The recurrence time `\tau_{\mathrm{rec}}` is only estimated up to order of magnitude; no canonical microscopic time unit is fixed.
- In the spin model, Susskind verbally wavers about the field orientation, but the board equation `E=(n-m)\mu H` is the safer anchor.
- The partition-function algebra near the `x,y` substitution is garbled in the transcript; the clean binomial steps should be treated as cautious standard reconstruction supported by the board.
- The magnetization definition is briefly misstated with an extra `\mu H`; final notes should keep the corrected form `M=\left\langle \frac{n-m}{N}\right\rangle`.
- The transcript around averages confuses `N`, `M`, and “average magnetization”; final notes should regularize this consistently.
- The board only directly shows the local Ising interaction `E=-J\sigma_{(1)}\sigma_{(2)}`; the full chain sum is transcript-backed, not frame-visible.
- Boundary conditions for the one-dimensional Ising chain are not specified in this lecture segment.
- The lecture’s `\tanh` discussion is mathematically clear, but any plotted figure in the notes would be transcript-driven rather than frame-backed.