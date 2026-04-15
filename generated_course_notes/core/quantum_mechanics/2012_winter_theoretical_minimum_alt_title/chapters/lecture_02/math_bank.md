# Math Bank
## Core Equations
- `\sigma_z=\pm1` `[visible]`
- `\sigma_x=\pm1` `[visible]`
- `\sigma_y=\pm1` `[transcript-backed]`
- `\sigma_{\hat m}=\pm1` for any apparatus orientation `\hat m` `[standard reconstruction]`
- `\langle \sigma_m\rangle = n\cdot m` `[visible]`
- `\langle \sigma_{\hat m}\rangle = \hat n\cdot \hat m = \cos\theta_{nm}` `[standard reconstruction]`
- If the spin is prepared with `\sigma_z=+1`, then `\langle \sigma_x\rangle=0` and `\langle \sigma_y\rangle=0` `[transcript-backed]`
- `A:\sigma_z=+1,\qquad B:\sigma_x=+1` `[transcript-backed]`
- `\neg A = A^c,\qquad A\land B = A\cap B,\qquad A\lor B = A\cup B` `[transcript-backed]`
- In the order “measure `B` first, then `A`,” `P(\neg B \text{ and then } \neg A)=\frac14` `[transcript-backed]`
- `P_A P_B \neq P_B P_A` for the corresponding projection operators `[transcript-backed]`
- `\mathcal H_{\text{spin}} \cong \mathbb C^2` `[standard reconstruction]`
- `|A\rangle=\alpha_u|u\rangle+\alpha_d|d\rangle` `[transcript-backed]`
- `P(u)=|\alpha_u|^2,\qquad P(d)=|\alpha_d|^2` `[standard reconstruction]`
- `|\alpha_u|^2+|\alpha_d|^2=1` `[transcript-backed]`
- `\langle A|A\rangle=1` `[transcript-backed]`
- `\langle u|u\rangle=\langle d|d\rangle=1` `[transcript-backed]`
- `\langle u|d\rangle=0` `[transcript-backed]`
- `|r\rangle=\frac{1}{\sqrt2}\bigl(|u\rangle+|d\rangle\bigr)` `[transcript-backed]`
- `|l\rangle=\frac{1}{\sqrt2}\bigl(|u\rangle-|d\rangle\bigr)` `[transcript-backed]`
- `\langle r|l\rangle=0` `[transcript-backed]`
- `|u\rangle=\frac{1}{\sqrt2}\bigl(|r\rangle+|l\rangle\bigr)` `[transcript-backed]`
- `|d\rangle=\frac{1}{\sqrt2}\bigl(|r\rangle-|l\rangle\bigr)` `[transcript-backed]`
- `|i\rangle=\frac{1}{\sqrt2}\bigl(|u\rangle+i|d\rangle\bigr)` `[transcript-backed]`
- `|o\rangle=\frac{1}{\sqrt2}\bigl(|u\rangle-i|d\rangle\bigr)` `[transcript-backed]`
- `\langle i|o\rangle=0` `[transcript-backed]`
- `|u\rangle=\binom10,\qquad |d\rangle=\binom01` `[transcript-backed]`
- `|r\rangle=\frac{1}{\sqrt2}\binom11,\qquad |l\rangle=\frac{1}{\sqrt2}\binom1{-1}` `[transcript-backed]`
- `|i\rangle=\frac{1}{\sqrt2}\binom1{i},\qquad |o\rangle=\frac{1}{\sqrt2}\binom1{-i}` `[transcript-backed]`
- `\langle a|b\rangle=a_1^*b_1+a_2^*b_2` in the `u,d` basis `[standard reconstruction]`
- `(\alpha_u,\alpha_d)^T \mapsto e^{i\theta}(\alpha_u,\alpha_d)^T` leaves the physical state unchanged `[transcript-backed]`
- `4\text{ real parameters} - 1\text{ normalization} - 1\text{ overall phase} = 2\text{ real parameters}` `[transcript-backed]`

## Definitions And Objects
- `three-vector`: a vector in ordinary real three-dimensional space.
- `vector` without qualification: an element of an abstract vector space.
- `spin`: the renamed qubit; introduced operationally through what an apparatus measures.
- apparatus model: an oriented detector with a readout window; every measurement returns only `+1` or `-1`.
- axis convention used in the lecture: `z` up, `x` to the right, `y` out of the blackboard.
- `\sigma_z,\sigma_x,\sigma_y`: names for the measured spin component along the corresponding apparatus orientation.
- `\sigma_m` or `\sigma_{\hat m}`: component measured along a generic direction.
- averages are denoted by angle brackets `\langle \cdot \rangle`; lecture language prefers “average value,” while standard QM also says “expectation value.”
- propositions in the classical warmup: subsets of a state set.
- `\neg A`, `A\land B`, `A\lor B`: complement, intersection, inclusive union in the classical set model.
- `A:\sigma_z=+1`, `B:\sigma_x=+1`: the two key quantum propositions used to show order dependence.
- bras and kets: dual vector objects with inner product `\langle \phi|\psi\rangle`.
- orthogonality: inner product zero; physically interpreted here as unambiguous distinguishability by experiment.
- dimension: maximum number of mutually orthogonal vectors in the space.
- normalized vector: unit vector; used as the mathematical representative of a physical state.
- z-basis dictionary:
  `|u\rangle \leftrightarrow u \leftrightarrow + \leftrightarrow \uparrow \leftrightarrow \sigma_z=+1`
- z-basis dictionary:
  `|d\rangle \leftrightarrow d \leftrightarrow - \leftrightarrow \downarrow \leftrightarrow \sigma_z=-1`
- x-basis dictionary:
  `|r\rangle \leftrightarrow \rightarrow \leftrightarrow \sigma_x=+1`
- x-basis dictionary:
  `|l\rangle \leftrightarrow \leftarrow \leftrightarrow \sigma_x=-1`
- y-basis dictionary:
  `|i\rangle \leftrightarrow \text{in} \leftrightarrow \sigma_y=+1`
- y-basis dictionary:
  `|o\rangle \leftrightarrow \text{out} \leftrightarrow \sigma_y=-1`

## Derivation Steps
Average law `\langle \sigma_m\rangle = n\cdot m`
1. Prepare the spin by measuring along direction `n` and keeping the `+1` outcome.
2. Re-measure the same spin along direction `m`.
3. Each single run still gives only `+1` or `-1`.
4. Special cases fix the pattern: if `m=n`, the average is `+1`; if `m=-n`, the average is `-1`; if `m\perp n`, the average is `0`.
5. The lecture states the general average as the cosine of the angle between `n` and `m`.
6. Rewrite `\cos\theta_{nm}` as `n\cdot m`.

Order dependence of `A\lor B`
1. Let `A:\sigma_z=+1` and `B:\sigma_x=+1`.
2. Suppose the hidden preparation is actually `\sigma_z=+1`.
3. If `A` is checked first, it is immediately true, so `A\lor B` is true.
4. If `B` is checked first, the first result is `+1` or `-1` with probability `1/2`.
5. When the first result is an x-result, the measurement prepares the spin along the x-axis.
6. A subsequent z-measurement then gives `+1` or `-1` with probability `1/2`.
7. Therefore the probability that both `B` is false and then `A` is false is `\frac12\cdot\frac12=\frac14`.
8. So verification of `A\lor B` depends on the order of testing.

Right-state from the `u,d` basis
1. Because the state space is two-dimensional, write `|r\rangle=\alpha_u|u\rangle+\alpha_d|d\rangle`.
2. Physics says that if the spin is prepared rightward, measuring up/down gives probabilities `1/2` and `1/2`.
3. Hence `|\alpha_u|^2=|\alpha_d|^2=\frac12`.
4. Choose the simplest representative with equal positive coefficients.
5. Obtain `|r\rangle=\frac1{\sqrt2}(|u\rangle+|d\rangle)`.

Left-state as the orthogonal partner
1. `|l\rangle` must also be a linear combination of `|u\rangle` and `|d\rangle`.
2. It must be orthogonal to `|r\rangle` because right and left are unambiguously distinguishable by an x-measurement.
3. A candidate with the same magnitudes and opposite relative sign is `\frac1{\sqrt2}(|u\rangle-|d\rangle)`.
4. Compute the inner product with `|r\rangle`.
5. The two terms cancel, so the inner product is zero.
6. Take `|l\rangle=\frac1{\sqrt2}(|u\rangle-|d\rangle)` up to overall sign.

Inverse x/z basis relations
1. Start from `|r\rangle=\frac1{\sqrt2}(|u\rangle+|d\rangle)` and `|l\rangle=\frac1{\sqrt2}(|u\rangle-|d\rangle)`.
2. Add the two equations to isolate `|u\rangle`.
3. Subtract the two equations to isolate `|d\rangle`.
4. Obtain `|u\rangle=\frac1{\sqrt2}(|r\rangle+|l\rangle)` and `|d\rangle=\frac1{\sqrt2}(|r\rangle-|l\rangle)`.

In/out states from symmetry and orthogonality
1. Seek `|i\rangle=a|u\rangle+b|d\rangle` and `|o\rangle=a'|u\rangle+b'|d\rangle`.
2. Equal up/down probabilities require `|a|^2=|b|^2=\frac12`.
3. Orthogonality requires `\langle i|o\rangle=0`.
4. Symmetry with the other two basis pairs requires the same equal-modulus behavior when expanded in the `r,l` basis.
5. The lecture’s solution is `|i\rangle=\frac1{\sqrt2}(|u\rangle+i|d\rangle)` and `|o\rangle=\frac1{\sqrt2}(|u\rangle-i|d\rangle)`.

Orthogonality check for `|i\rangle` and `|o\rangle`
1. Write `|i\rangle=\frac1{\sqrt2}\binom1{i}` and `|o\rangle=\frac1{\sqrt2}\binom1{-i}`.
2. Conjugate one vector when forming the inner product.
3. The first term contributes `+\frac12`.
4. The second term contributes `-\frac12`.
5. The sum is zero.

Normalization from probabilities
1. For `|A\rangle=\alpha_u|u\rangle+\alpha_d|d\rangle`, the measurement probabilities are `|\alpha_u|^2` and `|\alpha_d|^2`.
2. Total probability must be one.
3. Therefore `|\alpha_u|^2+|\alpha_d|^2=1`.
4. With `|u\rangle` and `|d\rangle` orthonormal, this is exactly `\langle A|A\rangle=1`.
5. Physical states are therefore represented by normalized vectors.

Phase redundancy and parameter count
1. Two complex amplitudes contain four real parameters.
2. Normalization removes one real parameter.
3. Multiplying both amplitudes by the same phase factor `e^{i\theta}` changes no physics.
4. Overall phase removes one more real parameter.
5. Two real parameters remain.
6. The lecture identifies these with the two angles needed to specify a spatial direction.

## Notation Choices
- Use `\hat n,\hat m` for spatial unit vectors in clean exposition.
- Keep the board form `n\cdot m` near the figure or when echoing the lecture literally.
- Use `\sigma_z,\sigma_x,\sigma_y` as measured spin components with eigenvalues `\pm1`; do not yet identify them with explicit Pauli matrices.
- For a generic axis, prefer `\sigma_{\hat m}` in polished notes and mention that Susskind often says `\sigma_m`.
- Use `|u\rangle,|d\rangle` as the main basis notation once the vector-space discussion begins.
- Keep the lecture’s parallel naming once, as a dictionary: `u/d`, `+/-`, arrows, and `\sigma_z=\pm1`.
- Use `|r\rangle,|l\rangle` for x-basis states and `|i\rangle,|o\rangle` for y-basis states.
- Reserve bare `i` for the imaginary unit; when writing the in-state, always keep the ket `|i\rangle` so the typography disambiguates it.
- Use `\langle \cdot \rangle` with the wording “average value” as the primary lecture-faithful phrase; mention “expectation value” only secondarily if needed.
- Use inclusive OR for `\lor` in the logic discussion.
- If projection operators are mentioned, use placeholder notation such as `P_A,P_B`; do not expand operator formalism further in this chapter.
- Inner products should follow the usual conjugate-first-slot convention.
- Column-vector representations should be understood as written in the `u,d` basis.
- Use overall-phase equivalence only as `|\psi\rangle` and `e^{i\theta}|\psi\rangle` representing the same physical state; do not introduce projective-space language unless later needed.

## Uncertain Mathematics
- The board formula `\langle \sigma_m\rangle=n\cdot m` is visually strong but the first handwritten symbol can be misread; transcript support for `n` is strong.
- The lecture speaks about unit vectors with hats, but the surviving board writing omits them; final notes should be explicit about when hats are being added editorially.
- The transcript around the average/expected-value exchange is noisy and philosophically loose; preserve only the safe content that `\langle\cdot\rangle` is an ordinary average over repeated outcomes.
- The Born-rule wording in the transcript is garbled; the clean statement `P=|\alpha|^2` is a cautious standard reconstruction, not a verbatim transcript rendering.
- The live derivation of the in/out expansion into the left/right basis is messy and interrupted; do not rely on the spoken algebra there unless it is re-derived cleanly.
- The board shows `\sigma_z=1` and `\sigma_z=-1` without always visibly writing the plus sign; use `+1` and `-1` consistently in final notes.
- The brief statement that propositions correspond to projection operators is accurate but undeveloped; treat it as a forward pointer, not a full operator section.
- The lecture temporarily treats “orthogonal” and “perpendicular” as synonymous in ordinary space, but later insists that orthogonality in state space must not be confused with spatial geometry; final notes must separate those senses clearly.
- The ket column in the board frames is only partial; full bra-ket notation should be treated as transcript-backed, not frame-proven.
- The final third is heuristic by design; do not recast the `r,l,i,o` constructions as fully rigorous consequences of already-developed operator theory.