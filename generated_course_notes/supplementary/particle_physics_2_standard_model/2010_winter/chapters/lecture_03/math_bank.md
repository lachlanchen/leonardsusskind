# Math Bank
## Core Equations
- Rotation data: \((\hat n,\theta)\), with \(\hat n\) a unit vector and \(\theta\) the rotation angle [transcript-backed]
- \(V_i' = R_{ij}(\theta,\hat n)\,V_j\) [visible]
- \(V_i V_i = V_i' V_i'\) [transcript-backed]
- \(V_i' V_i' = R_{ij}R_{ik}V_jV_k\) [transcript-backed]
- \(R_{ij}R_{ik}=\delta_{jk}\) [transcript-backed]
- \(R^T R = \mathbf 1\) [transcript-backed]
- \(R^{-1}=R^T\) [transcript-backed]

- \(\begin{pmatrix}1\\0\end{pmatrix}\) = up, \(\begin{pmatrix}0\\1\end{pmatrix}\) = down [transcript-backed]
- \(\psi=\begin{pmatrix}\alpha_1\\\alpha_2\end{pmatrix}\) [transcript-backed]
- \(|\alpha_1|^2+|\alpha_2|^2=1\) [transcript-backed]
- \(\alpha_i' = U_{ij}\alpha_j\) [transcript-backed]
- \(\left(U^T\right)^*U=\mathbf 1\) [visible]
- \(U^\dagger U=\mathbf 1\) [visible]
- \(\det U = 1\) [transcript-backed]
- \(\det U^\dagger = (\det U)^*\) [transcript-backed]
- Before imposing \(\det U=1\): \(\det U = e^{i\phi}\), \(\det U^\dagger = e^{-i\phi}\) [transcript-backed]

- \(U = \mathbf 1 + \epsilon M + O(\epsilon^2)\) [transcript-backed]
- \(M^\dagger = -M\) [transcript-backed]
- Equivalent rewritten form: \(U = \mathbf 1 + i\epsilon M + O(\epsilon^2)\), with \(M^\dagger = M\) [transcript-backed]
- \(\det(\mathbf 1+\epsilon M)=1+\epsilon\,\operatorname{tr}M+O(\epsilon^2)\) [standard reconstruction]
- \(\operatorname{tr}M=0\) [transcript-backed]
- \(M\) is a linear combination of Pauli matrices [transcript-backed]
- \(M = a_x\sigma_x+a_y\sigma_y+a_z\sigma_z\) [standard reconstruction]

- \(q=\begin{pmatrix}\alpha_1\\\alpha_2\\\alpha_3\end{pmatrix}\) or \(q=\begin{pmatrix}r\\g\\b\end{pmatrix}\) [transcript-backed]
- \(q' = Uq\), with \(U\in SU(3)\) [transcript-backed]
- \(U^\dagger U=\mathbf 1\) for the \(3\times3\) color action [transcript-backed]
- \(18-9-1=8\) [transcript-backed]

## Definitions And Objects
- \(\hat n\): unit vector specifying the axis of rotation; lecture treats rotations as right-handed by convention.
- \(\theta\): rotation angle about \(\hat n\).
- Rotation group of space: continuous, non-abelian group under sequential composition of rotations.
- \(R_{ij}(\theta,\hat n)\): \(3\times3\) real rotation matrix acting on vector components.
- Vector representation: representation of rotations on the components of an ordinary spatial vector.
- Spin-1 representation: three-state quantum system transforming like a three-vector.
- Spin-0 representation: trivial representation; only the identity acts nontrivially.
- Spin-\(\tfrac12\) state / spinor: two-component complex column \((\alpha_1,\alpha_2)^T\).
- \(U\): \(2\times2\) complex matrix acting on spin-\(\tfrac12\) states; later also \(3\times3\) complex matrix acting on color states, dimension determined by context.
- Hermitian conjugate: \(U^\dagger = (U^T)^*\).
- Unitary matrix: matrix satisfying \(U^\dagger U=\mathbf 1\).
- \(U(n)\): group of \(n\times n\) unitary matrices.
- \(SU(n)\): group of \(n\times n\) unitary matrices with determinant \(1\).
- Small rotation generator \(M\): initially anti-Hermitian in \(U=\mathbf 1+\epsilon M\); after factoring out \(i\), Hermitian and traceless.
- Pauli matrices / sigmas: basis for traceless Hermitian \(2\times2\) matrices; generate infinitesimal \(SU(2)\) rotations.
- Color state: three-state system for quark color, organized as a three-component column.
- \(SU(3)\): special unitary symmetry acting on color triplets.

## Derivation Steps
1. Rotation matrix condition: start from \(V_i' = R_{ij}V_j\).
2. Rotation matrix condition: impose preservation of vector length, \(V_iV_i=V_i'V_i'\).
3. Rotation matrix condition: substitute \(V_i' = R_{ij}V_j\) into the primed norm.
4. Rotation matrix condition: obtain \(V_i'V_i' = R_{ij}R_{ik}V_jV_k\).
5. Rotation matrix condition: require equality with \(V_iV_i\) for every vector \(V\).
6. Rotation matrix condition: conclude \(R_{ij}R_{ik}=\delta_{jk}\).
7. Rotation matrix condition: rewrite in matrix form as \(R^TR=\mathbf 1\).
8. Rotation matrix condition: read off \(R^{-1}=R^T\).

9. Spinor unitarity: begin with \(\psi=\begin{pmatrix}\alpha_1\\\alpha_2\end{pmatrix}\) and \(|\alpha_1|^2+|\alpha_2|^2=1\).
10. Spinor unitarity: let the rotated state be \(\psi' = U\psi\).
11. Spinor unitarity: require the total probability to remain \(1\) after the transformation.
12. Spinor unitarity: this gives the complex analogue of the vector-length condition.
13. Spinor unitarity: the matrix condition is \((U^T)^*U=\mathbf 1\).
14. Spinor unitarity: identify \((U^T)^*\) as \(U^\dagger\).
15. Spinor unitarity: rewrite the condition as \(U^\dagger U=\mathbf 1\).

16. Parameter count for \(U(2)\): a \(2\times2\) complex matrix has \(4\) complex entries \(=8\) real parameters.
17. Parameter count for \(U(2)\): the matrix equation \(U^\dagger U=\mathbf 1\) gives \(4\) real constraints.
18. Parameter count for \(U(2)\): conclude a general unitary \(2\times2\) matrix has \(4\) real parameters.
19. Parameter count for \(SU(2)\): compare with the \(3\)-parameter rotation group.
20. Parameter count for \(SU(2)\): impose one additional condition, \(\det U=1\).
21. Parameter count for \(SU(2)\): use \(\det(AB)=\det A\,\det B\) to check closure is preserved.
22. Parameter count for \(SU(2)\): conclude the special unitary \(2\times2\) matrices form a \(3\)-parameter group.

23. Near-identity \(SU(2)\): write a small transformation as \(U=\mathbf 1+\epsilon M+O(\epsilon^2)\).
24. Near-identity \(SU(2)\): impose unitarity to first order.
25. Near-identity \(SU(2)\): obtain \(M^\dagger=-M\) in the unfactored convention.
26. Near-identity \(SU(2)\): rewrite instead as \(U=\mathbf 1+i\epsilon M+O(\epsilon^2)\).
27. Near-identity \(SU(2)\): in that convention, first-order unitarity gives \(M^\dagger=M\).
28. Near-identity \(SU(2)\): impose \(\det U=1\) near the identity.
29. Near-identity \(SU(2)\): use \(\det(\mathbf 1+\epsilon M)=1+\epsilon\,\operatorname{tr}M+O(\epsilon^2)\).
30. Near-identity \(SU(2)\): conclude \(\operatorname{tr}M=0\).
31. Near-identity \(SU(2)\): therefore \(M\) must be Hermitian and traceless.
32. Near-identity \(SU(2)\): identify the sigmas as the basis of such matrices.

33. \(SU(3)\) parameter count: start from a \(3\times3\) complex matrix, giving \(9\) complex entries \(=18\) real parameters.
34. \(SU(3)\) parameter count: impose \(U^\dagger U=\mathbf 1\), giving \(9\) real constraints at lecture level.
35. \(SU(3)\) parameter count: impose \(\det U=1\) for one more constraint.
36. \(SU(3)\) parameter count: conclude \(18-9-1=8\) parameters.

## Notation Choices
- Use \(\hat n\) rather than bare \(n\) in final displayed formulas when emphasizing that the axis is a unit vector.
- Use \(\theta\) for the rotation angle throughout.
- Use \(V_i\) and \(V_i'\) for vector components, with \(V_x,V_y,V_z\) only as explanatory examples.
- Standardize the rotation action as \(V_i' = R_{ij}(\theta,\hat n)V_j\), even though the board writes the same content in a slightly informal order.
- Use \(R\) for the real \(3\times3\) rotation matrix; reserve \(U\) for complex unitary matrices acting on spinor or color states.
- Use \(\psi\) for the two-component spinor when helpful, but keep \(\alpha_1,\alpha_2\) as the actual component names used in the lecture.
- Use \(U^\dagger=(U^T)^*\) as the operator definition; do not alternate between multiple dagger conventions.
- Typeset the identity as \(\mathbf 1\) in matrix equations; note that the board writes \(1\).
- Use “spinor” in the notes, even though the transcript occasionally says “spinner.”
- Use \(\sigma_x,\sigma_y,\sigma_z\) for the Pauli matrices; if \(S_i\) is mentioned, note only that the lecture recalls them as half the Pauli matrices.
- Use \(q\) or a three-component column for color states; specify explicitly when \(U\) is now \(3\times3\).
- Treat \(\epsilon\) as a real small parameter in the near-identity expansion, consistent with the lecture.

## Uncertain Mathematics
- The lecture’s axis-angle parameterization explicitly ignores the \(2\pi\) identification; final notes should not silently turn that into a full global classification of rotations.
- The transcript around the “Lie group” terminology is OCR-corrupted; preserve the concept, but do not quote the malformed spelling.
- The board-supported spinor equations are secure only for \((U^T)^*U=\mathbf 1\) and \(U^\dagger U=\mathbf 1\); the cropped upper matrix-spinor line should not be reconstructed unless needed from the transcript.
- The near-identity passage is partially garbled in the transcript; keep the secure logical outcome:
  - unfactored small matrix is anti-Hermitian,
  - after pulling out \(i\), the generator is Hermitian,
  - determinant one implies tracelessness.
- The determinant expansion was spoken through a board-level \(2\times2\) example, but the transcript contains obvious slips; use the clean first-order trace formula rather than literal OCR text like “\(m_{12}+m_{22}\).”
- When the lecture says the \(SU(2)\) family “is the rotation group,” retain the warning that a subtlety is being suppressed; do not silently upgrade this to a precise global group isomorphism statement.
- The mapping from a normalized spinor \((\alpha_1,\alpha_2)\) to a spatial direction is asserted but not derived; keep it as a lecture-level fact, not a full Bloch-sphere derivation unless another prompt asks for it.
- The explicit matrix that exchanges two color states in the later color discussion is not reliably available from the current evidence set; do not invent a concrete matrix there.
- The \(SU(3)\) parameter count is lecture-level and should stay at that level; the later relation to eight gluons is a motivational hint, not yet a full construction of the gauge theory.