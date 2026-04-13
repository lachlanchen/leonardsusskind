# Math Bank

## Core Equations

- \(U^\dagger U = 1\) [transcript-backed]
- \(\det U = 1\) [transcript-backed]
- \(\det(AB)=\det A\,\det B\) [transcript-backed]
- \(\det(U^\dagger)=(\det U)^*\) [transcript-backed]
- \(\det U = e^{i\theta}\) [transcript-backed]
- \(e^{-i\theta/2}U \in SU(2)\) [transcript-backed]
- \(U \sim -U\) [transcript-backed]
- \(U = 1 + i\epsilon T\) [transcript-backed]
- \((1+i\epsilon T)(1-i\epsilon T^\dagger)=1\) [visible]
- \(i\epsilon\,(T-T^\dagger)=0\) [visible]
- \(T=T^\dagger\) [visible]
- \(\det(1+\epsilon m)=1+\epsilon\,\operatorname{tr}m+O(\epsilon^2)\) [standard reconstruction]
- \(\operatorname{tr}T=0\) [transcript-backed]
- \(8-4-1=3\) [transcript-backed]
- \(18-9-1=8\) [transcript-backed]
- \(2\otimes2 = 1\oplus3\) [transcript-backed]
- \(\epsilon_{ij}\psi_i\phi_j=\psi_\uparrow\phi_\downarrow-\psi_\downarrow\phi_\uparrow\) [transcript-backed]
- \(\{\psi_\uparrow\phi_\uparrow,\ \psi_\downarrow\phi_\downarrow,\ \psi_\uparrow\phi_\downarrow+\psi_\downarrow\phi_\uparrow\}\) [transcript-backed]
- \(q=\begin{pmatrix}q_r\\ q_b\\ q_g\end{pmatrix}\) [transcript-backed]
- \(q' = Uq\) [transcript-backed]
- \(\bar q' = U^* \bar q\) [transcript-backed]
- \(3\otimes3=\bar 3\oplus6\) [visible]
- \(3\otimes\bar 3 = 1\oplus8\) [transcript-backed]
- \(3\otimes3\otimes3 \supset 1\) [transcript-backed]
- \(\epsilon_{ijk}q_i q_j q_k\) [transcript-backed]
- \(8\times8=1+63\) [visible]
- \(8\otimes8 = 1\oplus8\oplus8\oplus10\oplus\overline{10}\oplus27\) [standard reconstruction]

## Definitions And Objects

- Abstract group element: the symmetry operation itself, prior to specifying what it acts on.
- Representation: the matrix realization of that abstract operation on a chosen state space.
- Representation dimension: the number of mutually orthogonal states of the system being acted on.
- Spin examples: spin \(0\) gives a trivial \(1\times1\) representation, spin \(1/2\) a \(2\times2\) representation, spin \(1\) a \(3\times3\) representation, higher spin larger finite-dimensional representations.
- Orbital motion example: rotations can also act in infinite-dimensional representations.
- Infinitesimal group element: a group element very close to the identity.
- Generator \(T\): the operator appearing in \(U=1+i\epsilon T\); for the lecture these are the conserved quantities associated with the symmetry.
- For spatial rotations: the three linearly independent generators are the angular momentum operators.
- Traceless Hermitian \(2\times2\) generators: the three Pauli matrices span this space.
- Traceless Hermitian \(3\times3\) generators: eight linearly independent matrices; lecture names them as the Gell-Mann matrices.
- Triplet \(3\): the quark color representation.
- Anti-triplet \(\bar 3\): the complex-conjugate representation carried by anti-quarks.
- Octet \(8\): the adjoint representation; transforms the same way as the eight generators.
- Singlet \(1\): an invariant state; lecture treats this as the analog of a neutral object under the symmetry.
- Baryon: a color-singlet \(qqq\) state.
- Meson: a color-singlet \(q\bar q\) state.
- Glueball: a color-singlet state built purely from gluons.
- Gauge theory, at lecture level: a theory in which conserved quantities source photon-like fields.

## Derivation Steps

SU(2) parameter count

1. Start with a \(2\times2\) complex matrix: \(4\) complex entries \(=8\) real parameters.
2. Impose unitarity \(U^\dagger U=1\): this gives \(4\) real constraints.
3. Impose \(\det U=1\): this removes one more parameter.
4. The result has \(3\) real parameters, matching the three parameters of spatial rotations.

Removing the extra determinant phase

1. For a unitary matrix, \(\det U\) has modulus \(1\), so write \(\det U=e^{i\theta}\).
2. Multiply \(U\) by the scalar phase \(e^{-i\theta/2}\).
3. The determinant of the new matrix is \(e^{-i\theta}\det U=1\).
4. This isolates the special-unitary part relevant for the rotation discussion.
5. Keep the lecture caveat: \(SU(2)\) is only two-to-one over the ordinary rotation group.

Infinitesimal unitarity implies Hermiticity

1. Write a near-identity element as \(U=1+i\epsilon T\).
2. Take the adjoint: \(U^\dagger=1-i\epsilon T^\dagger\).
3. Multiply and keep only terms through first order in \(\epsilon\).
4. The \(1\) cancels against the identity on the right-hand side.
5. The first-order condition is \(i\epsilon(T-T^\dagger)=0\).
6. Conclude \(T=T^\dagger\).

Determinant one implies tracelessness

1. Use the near-identity expansion \(\det(1+\epsilon m)=1+\epsilon\,\operatorname{tr}m+O(\epsilon^2)\).
2. Apply it to the infinitesimal matrix \(U=1+i\epsilon T\).
3. Impose \(\det U=1\).
4. The first-order term must vanish.
5. Conclude \(\operatorname{tr}T=0\).

Warm-up: \(2\otimes2=1\oplus3\)

1. Form the two-particle object \(\psi_i\phi_j\).
2. There are \(4\) basis states: \(\uparrow\uparrow\), \(\uparrow\downarrow\), \(\downarrow\uparrow\), \(\downarrow\downarrow\).
3. Check the antisymmetric combination \(\psi_\uparrow\phi_\downarrow-\psi_\downarrow\phi_\uparrow\).
4. It does not mix with the other three under the \(SU(2)\) action.
5. Identify it as the singlet \(1\).
6. The remaining three states mix among themselves.
7. Identify them as the triplet \(3\), i.e. the spin-1 multiplet.

Two quarks: \(3\otimes3=\bar3\oplus6\)

1. Two quarks give \(3\times3=9\) color states.
2. Split these states by symmetry under interchange of the two color indices.
3. The antisymmetric part has dimension \(3\).
4. Identify that antisymmetric piece with the anti-triplet \(\bar3\).
5. The symmetric part has dimension \(6\).
6. Identify it with the sextet \(6\).

Quark plus anti-quark: \(3\otimes\bar3=1\oplus8\)

1. A quark and an anti-quark again give \(9\) states.
2. One linear combination is invariant: schematically \(r\bar r+b\bar b+g\bar g\).
3. Identify that invariant combination as the singlet \(1\).
4. The remaining \(8\) states mix into each other under color rotations.
5. Identify them as the octet \(8\), the adjoint representation.

Three quarks contain a singlet

1. First combine two quarks: \(3\otimes3=\bar3\oplus6\).
2. Then combine with the third quark.
3. The \(\bar3\otimes3\) branch gives \(1\oplus8\).
4. Therefore \(3\otimes3\otimes3\) contains a singlet.
5. Write the singlet as \(\epsilon_{ijk}q_i q_j q_k\).
6. The antisymmetric tensor forces \(i,j,k\) all to be different.

Two gluons

1. Two gluons give \(8\times8=64\) states in total.
2. One combination is a singlet.
3. The remaining \(63\) states split into non-singlet irreducible pieces.
4. In an appropriate basis, the two-gluon representation becomes block diagonal by irreducible sector.
5. The lecture-level cleaned decomposition is \(1\oplus8\oplus8\oplus10\oplus\overline{10}\oplus27\).

Confinement logic in lecture form

1. Colored objects source gluon fields through the \(SU(3)\) color generators.
2. Gluons themselves carry color, so the gluon field self-interacts.
3. The self-interaction bundles flux lines into tubes.
4. The field energy in the tube is roughly uniform per unit length.
5. Separating a quark from an anti-quark then costs energy growing roughly linearly with distance.
6. The system either pulls back together or produces a new \(q\bar q\) pair.
7. The observable outcome is color-singlet hadrons, not isolated quarks.

## Notation Choices

- Use \(U\) for a finite group element represented as a unitary matrix.
- Use \(T\) for the infinitesimal generator; if a basis is needed later, write \(T_a\).
- Use \(\epsilon\) for the small infinitesimal parameter in \(U=1+i\epsilon T\).
- Use \(\epsilon_{ij}\) and \(\epsilon_{ijk}\) only for antisymmetric tensors; rely on indices to distinguish them from the small parameter.
- Use \(\dagger\) for Hermitian conjugation in the clean notes, even though the board may show a superscript \(+\).
- Use \(\det U\) in the notes, not board-style vertical bars \(|U|\) or \(|M|\), except when explicitly quoting the screenshot.
- Use \(\operatorname{tr}\) for traces.
- Use \(\otimes\) for tensor products of representations.
- Use \(\oplus\) for decomposition into irreducible pieces.
- Preserve \(\times\) only when reproducing the literal board counting checkpoint \(8\times8=1+63\).
- Treat \(1\) contextually: identity matrix in matrix equations, singlet representation in decomposition formulas.
- Treat \(+\) in the spoken lecture’s decomposition formulas as cleaned-up \(\oplus\), not arithmetic addition.
- Use \(q=(q_r,q_b,q_g)^T\); the transcript momentarily stumbles on color names, but the stable lecture convention is red, blue, green.
- Use \(\bar3\) for the anti-triplet and \(\bar q\) for an anti-quark when a field symbol is needed.
- Use \(U^*\), not \(U^\dagger\), for the anti-quark’s complex-conjugate representation.
- For the \(SU(2)\) warm-up, use \(\psi_i\) and \(\phi_j\) for the two spin-\(1/2\) fields or creation operators.
- Optional \(1/\sqrt2\) normalizations can be added later to the singlet/triplet states, but the lecture itself does not insist on them.

## Uncertain Mathematics

- The board frame for the determinant expansion does not visibly show the trace term; \(\det(1+\epsilon m)=1+\epsilon\,\operatorname{tr}m+O(\epsilon^2)\) is a safe cleanup, not a literal transcription.
- The top line \((1+i\epsilon T)(1-i\epsilon T^\dagger)=1\) is partly occluded in the frame; the adjoint on the second factor is stabilized by the transcript and lower lines.
- The end of the \(SU(2)\) phase-removal discussion is transcript-garbled; keep only the clean points that \(\det U\) is a pure phase and that \(U\) and \(-U\) represent the same rotation.
- The verbal transition into \(SU(3)\) is damaged; rely on the clear parameter count \(18-9-1=8\), not on the repeated filler.
- The relation between generators in the \(3\) and \(\bar3\) representations is stated verbally as “negatives”; do not over-fix a precise matrix formula unless a later source pins down the convention.
- The lecture says “I think” when giving \(6\otimes3=8\oplus10\); if that branch is mentioned later, label it as cautious lecture-level material.
- The full \(8\otimes8\) decomposition is not board-derived in a stable way; it emerges from a remembered table during Q&A and should be marked as a cautious cleanup.
- The quark-antiquark singlet is only described schematically as \(r\bar r+b\bar b+g\bar g\); avoid over-specifying normalization or orthogonal octet basis states here.
- The late discussion of block-diagonalization does not settle formal jargon; “block diagonal in an appropriate basis” is safer than forcing a stronger term.
- The gauge-field/source passage near \(01{:}17{:}52\) to \(01{:}18{:}35\) is badly corrupted; keep only the secure claim that the eight color generators are the relevant color charges sourcing the eight gluon fields.
- The confinement picture is lecture-level dynamics; no explicit string tension or detailed potential formula is given in this lecture.