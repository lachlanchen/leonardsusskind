# Math Bank
## Core Equations
- \(\dim \mathcal H=\max\{\text{number of linearly independent vectors in }\mathcal H\}\) [transcript-backed]
- \(\sum_i c_i |v_i\rangle=0 \;\Rightarrow\; c_i=0\ \text{for all }i\) as the linear-independence criterion [standard reconstruction]
- \(|n\rangle\) [visible]
- \(\langle m|n\rangle=\delta_{mn}\) [visible]
- \(|\psi\rangle=\sum_n a_n\,|n\rangle\) [visible]
- \(a_m=\langle m|\psi\rangle\) [transcript-backed]
- \(|\psi\rangle=\sum_n |n\rangle\langle n|\psi\rangle\) [transcript-backed]
- \(\sum_n |n\rangle\langle n| = I\) [transcript-backed]
- \((|a\rangle\langle b|)\,|\psi\rangle=\langle b|\psi\rangle\,|a\rangle\) [standard reconstruction]
- \(k|A\rangle=\lambda |A\rangle\) [transcript-backed]
- \(k|B\rangle=\lambda |B\rangle\) [transcript-backed]
- \(k(\alpha|A\rangle+\beta|B\rangle)=\lambda(\alpha|A\rangle+\beta|B\rangle)\) [transcript-backed]
- \(|uu\rangle\) [visible]
- \(|ud\rangle\) [transcript-backed]
- \(\Pi_{k=\lambda}=\sum_a |a\rangle\langle a|\) [transcript-backed]
- \(\Pi_k|\psi\rangle\) [visible]
- \(k\big(\Pi_{k=\lambda}|\psi\rangle\big)=\lambda\,\Pi_{k=\lambda}|\psi\rangle\) [transcript-backed]
- \(P(k=\lambda)=\langle\psi|\Pi_{k=\lambda}|\psi\rangle\) [transcript-backed]
- \(P(k=\lambda)=\sum_a \langle\psi|a\rangle\langle a|\psi\rangle=\sum_a |\langle a|\psi\rangle|^2\) [standard reconstruction]
- \(\Pi_{\sigma_3=+1}=|uu\rangle\langle uu|+|ud\rangle\langle ud|\) [transcript-backed]
- \(\Pi_{k=\lambda\ \wedge\ \ell=\mu}=P_kP_\ell=P_\ell P_k\) for commuting projectors [transcript-backed]
- \(P(k=\lambda,\ell=\mu)=\langle\psi|P_kP_\ell|\psi\rangle\) [transcript-backed]
- \(P_{k=\lambda\ \mathrm{or}\ \ell=\mu}=P_k+P_\ell\) in the lecture’s compatible-projector discussion [transcript-backed]
- \(\Pi_{\sigma_3=+1}=\dfrac{1+\sigma_3}{2}\) [transcript-backed]
- \(\Pi_{\tau_{45^\circ}=+1}=\dfrac{1+\frac{\tau_1+\tau_3}{\sqrt2}}{2}\) [transcript-backed]
- \(\Pi_{\sigma_{45^\circ}=+1}=\dfrac{1+\frac{\sigma_1+\sigma_3}{\sqrt2}}{2}\) [transcript-backed]
- \(\Pi_{\tau_1=+1}=\dfrac{1+\tau_1}{2}\) [transcript-backed]
- \(\Pi_{(\sigma_3=+1)\wedge(\tau_{45^\circ}=+1)}=\dfrac{1+\sigma_3}{2}\dfrac{1+\frac{\tau_1+\tau_3}{\sqrt2}}{2}\) [transcript-backed]
- \(\Pi_{(\sigma_{45^\circ}=+1)\wedge(\tau_1=+1)}=\dfrac{1+\frac{\sigma_1+\sigma_3}{\sqrt2}}{2}\dfrac{1+\tau_1}{2}\) [transcript-backed]
- \(\Pi_{(\sigma_3=+1)\wedge(\tau_1=+1)}=\dfrac{1+\sigma_3}{2}\dfrac{1+\tau_1}{2}\) [transcript-backed]
- \(|\Psi_{\mathrm{singlet}}\rangle=|ud\rangle-|du\rangle\) as spoken in the Bell recap [transcript-backed]
- \(|0\rangle \to |1\rangle+|-1\rangle\) [transcript-backed]
- \(|1\rangle \to \sum_n \psi_n |n\rangle\) [transcript-backed]
- \(|-1\rangle \to \sum_n \phi_n |n\rangle\) [transcript-backed]
- \(|1\rangle+|-1\rangle \to \sum_n (\psi_n+\phi_n)|n\rangle\) [transcript-backed]
- \(P_m=|\psi_m+\phi_m|^2\) [transcript-backed]
- \(P_m=|\psi_m|^2+|\phi_m|^2+\psi_m^*\phi_m+\phi_m^*\psi_m\) [transcript-backed]
- If \(\psi_0=\phi_0\), then \(P_0=4|\psi_0|^2\) [transcript-backed]
- If \(\phi_0=-\psi_0\), then \(P_0=0\) [transcript-backed]
- \(|0,d\rangle\) [transcript-backed]
- Upper-path record state: \(|1,u\rangle\) [transcript-backed]
- Lower-path record state: \(|-1,d\rangle\) [transcript-backed]
- With both slits open and a recording spin: \(|0,d\rangle \to |1,u\rangle+|-1,d\rangle\) [transcript-backed]
- \(|1,u\rangle \to \sum_n \psi_n |n,u\rangle\) [transcript-backed]
- \(|-1,d\rangle \to \sum_n \phi_n |n,d\rangle\) [transcript-backed]
- Final recorded state: \(\sum_n \psi_n |n,u\rangle+\sum_n \phi_n |n,d\rangle\) [transcript-backed]
- \(\langle u|d\rangle=0\) [transcript-backed]
- \(P_m=|\psi_m|^2+|\phi_m|^2\) after which-path recording, because the cross terms vanish [standard reconstruction]

## Definitions And Objects
- `Dimension`: the maximum number of linearly independent vectors in the space.
- `Linear dependence`: one vector can be expanded in terms of others; equivalently, a nontrivial linear combination can vanish.
- `Basis vectors`: mutually orthogonal unit vectors spanning the space.
- `Kronecker delta`: \(\delta_{mn}=1\) if \(m=n\), \(0\) otherwise.
- `Dyad`: an operator of the form \(|a\rangle\langle b|\).
- `Resolution of the identity`: the sum \(\sum_n |n\rangle\langle n|\) over a complete orthonormal basis.
- `Subspace`: a set of vectors closed under addition and scalar multiplication, itself a vector space of lower or equal dimension.
- `Eigensubspace`: the subspace of all states with the same eigenvalue of a Hermitian operator.
- `Property \(k=\lambda\)`: not generally a single vector; identified with the eigensubspace for eigenvalue \(\lambda\).
- `Projection operator`: the operator that returns the component of a state lying in a chosen subspace.
- `Compatible properties`: properties represented by commuting projection operators.
- `AND statement`: for commuting projectors, the product projector.
- `OR statement`: in this lecture’s working treatment, the sum of the compatible projectors.
- `Superposition`: one system in a linear combination of its own states.
- `Entanglement`: a composite-system state in which degrees of freedom of different subsystems are correlated and not separately specifiable.
- `Measurement`: in this lecture, the establishment of entanglement between the system and an apparatus.
- `Interference terms`: the cross terms \(\psi_m^*\phi_m+\phi_m^*\psi_m\) that survive only when no orthogonal record of the path is left.

## Derivation Steps
Basis coefficients from orthonormality
1. Start with \(|\psi\rangle=\sum_n a_n |n\rangle\).
2. Left-multiply by \(\langle m|\).
3. Use \(\langle m|n\rangle=\delta_{mn}\).
4. The sum collapses to one term.
5. Conclude \(a_m=\langle m|\psi\rangle\).

Resolution of the identity
1. Rewrite the expansion as \(|\psi\rangle=\sum_n |n\rangle\langle n|\psi\rangle\).
2. Regard \(\sum_n |n\rangle\langle n|\) as an operator acting on \(|\psi\rangle\).
3. Observe that it returns \(|\psi\rangle\) for arbitrary \(|\psi\rangle\).
4. Identify \(\sum_n |n\rangle\langle n|=I\).

Degenerate eigenvalues produce a subspace
1. Assume \(k|A\rangle=\lambda|A\rangle\) and \(k|B\rangle=\lambda|B\rangle\).
2. Form \(\alpha|A\rangle+\beta|B\rangle\).
3. Apply \(k\) linearly.
4. Pull out the common factor \(\lambda\).
5. Conclude every linear combination has the same eigenvalue.
6. Interpret the set of such combinations as the eigensubspace for \(k=\lambda\).

Projector onto a property subspace
1. Choose an orthonormal basis \(\{|a\rangle\}\) for the \(k=\lambda\) subspace.
2. Form \(\Pi_{k=\lambda}=\sum_a |a\rangle\langle a|\).
3. Act on a vector already in the subspace.
4. Recover the same vector.
5. Act on a vector outside the subspace.
6. Keep only its component inside the subspace.
7. Conclude \(\Pi_{k=\lambda}\) is the projection operator onto the property \(k=\lambda\).

Probability postulate in projector form
1. Start with the projector \(\Pi_{k=\lambda}=\sum_a |a\rangle\langle a|\).
2. Form the expectation value \(\langle\psi|\Pi_{k=\lambda}|\psi\rangle\).
3. Insert the dyad sum.
4. Get \(\sum_a \langle\psi|a\rangle\langle a|\psi\rangle\).
5. Read each term as the probability contribution from one orthogonal way of having the property.
6. Sum the orthogonal contributions to obtain the total probability for \(k=\lambda\).

AND statement for commuting projectors
1. Take two commuting projectors \(P_k\) and \(P_\ell\).
2. Apply \(P_k\) to any state; the result lies in the \(k\)-subspace.
3. Apply \(P_\ell\) as well.
4. Because they commute, the order does not matter.
5. The resulting vector lies in both subspaces.
6. Identify \(P_kP_\ell\) as the projector onto the simultaneous property \(k=\lambda\) and \(\ell=\mu\).
7. Take \(\langle\psi|P_kP_\ell|\psi\rangle\) for the corresponding probability.

Bell projector construction
1. Replace classical properties by quantum properties of a two-spin system.
2. Use \((1+\sigma_3)/2\) for “first spin up”.
3. Use \((1+(\tau_1+\tau_3)/\sqrt2)/2\) for “second spin along \(45^\circ\)”.
4. Multiply the relevant single-property projectors to get the AND projector for each experimental clause.
5. Evaluate expectation values in the chosen two-spin state.
6. Compare the resulting probabilities with the classical Bell inequality.

Two-slit interference from linearity
1. Assume \(|0\rangle \to |1\rangle+|-1\rangle\).
2. Assume \(|1\rangle \to \sum_n \psi_n|n\rangle\).
3. Assume \(|-1\rangle \to \sum_n \phi_n|n\rangle\).
4. Use linearity to evolve \(|1\rangle+|-1\rangle\).
5. Get \(\sum_n (\psi_n+\phi_n)|n\rangle\).
6. Read the amplitude at site \(m\) as \(\psi_m+\phi_m\).
7. Square its modulus to get the probability.
8. Expand the square and isolate the cross terms.

Constructive and destructive interference
1. Choose the symmetric screen point \(m=0\).
2. Use symmetry to set \(\psi_0=\phi_0\).
3. Compute \(P_0=|\psi_0+\phi_0|^2=|2\psi_0|^2\).
4. Conclude \(P_0=4|\psi_0|^2\): constructive interference.
5. Insert a relative sign change so that \(\phi_0=-\psi_0\).
6. Compute \(P_0=|\psi_0-\psi_0|^2=0\).
7. Conclude destructive interference.

Measurement as entanglement
1. Add an apparatus spin initially in state \(|d\rangle\).
2. Define the interaction so the upper path flips it to \(|u\rangle\), while the lower path leaves it \(|d\rangle\).
3. Get \(|0,d\rangle \to |1,u\rangle+|-1,d\rangle\) when both slits are open.
4. Evolve each branch to the screen: \(|1,u\rangle \to \sum_n \psi_n |n,u\rangle\), \(|-1,d\rangle \to \sum_n \phi_n |n,d\rangle\).
5. Form the final state \(\sum_n \psi_n |n,u\rangle+\sum_n \phi_n |n,d\rangle\).
6. Compute the probability for site \(m\).
7. Use \(\langle u|d\rangle=0\) to remove the cross terms.
8. Conclude that which-path recording destroys interference and makes probabilities add classically.

## Notation Choices
- Use \(\mathcal H\) for the full state space when a space label is needed; the lecture itself mostly just says “the space.”
- Keep the lecture’s lower-case \(k\) and \(\ell\) for observables when discussing properties \(k=\lambda\) and \(\ell=\mu\), even though a hat notation would be more textbook-standard.
- Use \(|n\rangle\) for an orthonormal basis of the full space, with \(n=1,\dots,d\) when the finite dimension is relevant.
- Use lower-case Roman \(a,b,c,\dots\) for basis vectors of a subspace, matching the projector construction \(\sum_a |a\rangle\langle a|\).
- Use \(\Pi_{k=\lambda}\) as the default projector notation in the chapter, because that is what the board frames support most clearly.
- Allow \(P_k\) and \(P_\ell\) as temporary shorthand only in the commuting-projector section, because Susskind shortens the notation there.
- Use \(\sigma_i\) for operators on the first spin and \(\tau_i\) for operators on the second spin.
- Use \(|uu\rangle, |ud\rangle, |du\rangle, |dd\rangle\) for two-spin product states, with the first slot belonging to the \(\sigma\)-spin and the second to the \(\tau\)-spin.
- Write the first-spin-up subspace example as spanned by \(|uu\rangle\) and \(|ud\rangle\).
- Use \(|0\rangle\) for the source state, \(|1\rangle\) and \(|-1\rangle\) for the two slit states, and \(|n\rangle\) for screen-site basis states.
- Use \(m\) for a selected final screen site where the probability is evaluated.
- In the detector-spin model, use \(|u\rangle, |d\rangle\) for apparatus-spin states and write composite kets with a comma, e.g. \(|n,u\rangle\), to avoid confusion with the two-spin basis \(|uu\rangle\).
- Treat \(\psi_n\) and \(\phi_n\) as amplitudes, not probabilities; their squared moduli contribute to probabilities.
- Preserve the lecture’s choice not to normalize the two-slit amplitudes explicitly; do not introduce unitarity notation in this chapter segment.

## Uncertain Mathematics
- The three-vector board sketch supports the linear-dependence discussion visually, but it does not determine a unique algebraic relation among the vectors; any explicit coefficient relation would be an added reconstruction.
- \(|ud\rangle\) in the frame is slightly smudged; the transcript settles the example, not the image alone.
- The board frames strongly suggest \(\Pi_{k=\lambda}\), but the full subscript is not perfectly legible in every shot; standardize to \(k=\lambda\) from the transcript.
- The full expectation-value formula \(\langle\psi|\Pi_{k=\lambda}|\psi\rangle\) is lecture-backed, but the complete line is reconstructed from the spoken argument rather than fully visible on the board.
- The OR statement as a sum of projectors should be kept exactly as the lecture’s local working rule for compatible properties, not upgraded silently into a fully general projection formula.
- Around the commuting-projector proof, the transcript is slightly repetitive and noisy; keep only the clear mathematical core that \(P_k|\psi\rangle\) lies in the \(k\)-subspace and that commutativity lets one exhibit both properties.
- The Bell-recap projectors are clear enough to use, but the lecture does not derive every algebraic simplification in detail; do not add a long Pauli-matrix computation unless later prompts require it.
- The singlet is spoken as \(|ud\rangle-|du\rangle\) without normalization; if a normalized singlet is used later, it should be flagged as a cleanup rather than presented as board-faithful notation.
- The two-slit segment overloads \(|1\rangle\), \(|-1\rangle\), \(|n\rangle\), and later \(|n,u\rangle\), \(|n,d\rangle\); the final notes should regularize this gently, but the bank should preserve the lecture’s sequencing.
- Around 01:25, Susskind speaks loosely about \(\psi_n,\phi_n\); the derivation itself clearly requires them to be amplitudes whose moduli squared enter probabilities.
- The detector-spin conclusion \(P_m=|\psi_m|^2+|\phi_m|^2\) is the correct cleaned result, but the lecture stops just before a full written derivation; the final notes should present it as the immediate consequence of orthogonality, not as a board-visible completed formula.
- Partial or weak measurement is only qualitative here; any explicit parametrized weak-measurement state should be marked as extrapolation unless a later lecture supplies it.