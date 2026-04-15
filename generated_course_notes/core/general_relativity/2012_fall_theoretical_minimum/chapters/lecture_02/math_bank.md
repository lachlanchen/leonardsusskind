# Math Bank
## Core Equations
- [transcript-backed] Scalar invariance: \(S'(y)=S(x)\).
- [transcript-backed] Contravariant vector transformation: \(V'^m(y)=\dfrac{\partial y^m}{\partial x^n}V^n(x)\).
- [transcript-backed] Model contravariant example: \(dy^m=\dfrac{\partial y^m}{\partial x^n}\,dx^n\).
- [transcript-backed] Covariant vector transformation: \(W'_m(y)=\dfrac{\partial x^n}{\partial y^m}W_n(x)\).
- [transcript-backed] Gradient as covariant vector: \(\dfrac{\partial S}{\partial y^m}=\dfrac{\partial x^n}{\partial y^m}\dfrac{\partial S}{\partial x^n}\).
- [transcript-backed] Vector expansion in basis vectors: \(V=V^mE_m\).
- [transcript-backed] Covariant component as projection: \(V_n=V\cdot E_n\).
- [transcript-backed] Metric from basis vectors: \(g_{mn}=E_m\cdot E_n\).
- [transcript-backed] Length formula in basis language: \(V\cdot V=g_{mn}V^mV^n\).
- [transcript-backed] Mixed rank-2 tensor transformation: \(T'^m{}_n=\dfrac{\partial y^m}{\partial x^p}\dfrac{\partial x^q}{\partial y^n}T^p{}_q\).
- [transcript-backed] Purely covariant rank-2 tensor transformation: \(W'_{mn}=\dfrac{\partial x^p}{\partial y^m}\dfrac{\partial x^q}{\partial y^n}W_{pq}\).
- [visible] Tensor subtraction: \(T^{m\cdots}{}_{\cdots p}-S^{m\cdots}{}_{\cdots p}=(T-S)^{m\cdots}{}_{\cdots p}\).
- [transcript-backed] Tensor equation form: \(T-S=0\) is meaningful only when both sides have the same index type and placement.
- [transcript-backed] Tensor product example: \(T^m{}_n=V^mW_n\).
- [transcript-backed] Contraction lemma: \(\dfrac{\partial x^b}{\partial y^m}\dfrac{\partial y^m}{\partial x^a}=\delta^b{}_a\).
- [transcript-backed] Scalar from contraction: \(V'^mW'_m=V^aW_a\).
- [standard reconstruction] Line element notation: \(ds^2=g_{mn}(x)\,dx^m dx^n\).
- [visible] Invariant squared length across coordinates: \(g_{mn}(x)\,dx^m dx^n=g'_{pq}(y)\,dy^p dy^q\).
- [visible] Coordinate substitutions used in the metric derivation: \(dx^m=\dfrac{\partial x^m}{\partial y^p}\,dy^p\), \(\quad dx^n=\dfrac{\partial x^n}{\partial y^q}\,dy^q\).
- [visible] Metric transformation law: \(g'_{pq}(y)=g_{mn}(x)\dfrac{\partial x^m}{\partial y^p}\dfrac{\partial x^n}{\partial y^q}\).
- [standard reconstruction] Metric symmetry: \(g_{mn}=g_{nm}\).
- [visible] Inverse metric identity: \(g_{mn}g^{np}=\delta_m{}^{p}\).
- [visible] \(2\times2\) matrix view: \(\begin{pmatrix} g_{11} & g_{12} \\ g_{21} & g_{22} \end{pmatrix}\begin{pmatrix} g^{11} & g^{12} \\ g^{21} & g^{22} \end{pmatrix}=I\).
- [transcript-backed] Example component equations from the \(2\times2\) inverse relation: \(g_{11}g^{11}+g_{12}g^{21}=1\), \(\quad g_{11}g^{12}+g_{12}g^{22}=0\).
- [transcript-backed] Lorentz-signature preview: \(ds^2=t^2-x^2-y^2-z^2\) or \(ds^2=x^2+y^2+z^2-t^2\).

## Definitions And Objects
- Scalar field: a quantity attached to each point whose value is the same in every coordinate system at that point.
- Tensor field: a point-dependent tensor; the lecture treats “field” simply as “can vary from point to point.”
- Contravariant vector \(V^m\): upper-index components; geometrically, expansion coefficients in \(V=V^mE_m\); model example \(dx^m\).
- Covariant vector \(V_m\): lower-index components; geometrically, projections \(V\cdot E_m\); model example \(\partial_m S\).
- Basis vectors \(E_m\): vectors pointing along coordinate directions; not assumed orthonormal in general coordinates.
- Metric tensor \(g_{mn}\): the object that converts contravariant displacement components into squared length; in the geometric interlude \(g_{mn}=E_m\cdot E_n\).
- Tensor type / index structure: the lecture organizes tensors by how many indices they have and whether each index is upstairs or downstairs.
- Rank: number of indices.
- Tensor product: juxtaposition/multiplication of tensors producing a higher-rank tensor, e.g. \(V^mW_n\).
- Contraction: identify one upper and one lower index and sum over it; lowers rank by two.
- Kronecker delta \(\delta^b{}_a\) or \(\delta_m{}^{p}\): identity tensor / identity matrix with one upper and one lower index.
- Inverse metric \(g^{mn}\): the tensor with upper indices defined as the matrix inverse of \(g_{mn}\).
- Tangent space: late-lecture clarification for where vectors and tensors “live” at a point of the manifold.

## Derivation Steps
Covariant vector from the gradient of a scalar:
1. Start from scalar invariance: \(S'(y)=S(x)\).
2. Differentiate with respect to \(y^m\).
3. Apply the chain rule: \(\partial/\partial y^m=(\partial x^n/\partial y^m)\partial/\partial x^n\).
4. Obtain \(\partial_m'S=(\partial x^n/\partial y^m)\partial_n S\).
5. Read this as the transformation law for a lower-index object.

Metric from basis vectors and the length formula:
1. Expand the vector as \(V=V^mE_m\).
2. Take the dot product with a basis vector: \(V_n=V\cdot E_n\).
3. Substitute the expansion: \(V\cdot E_n=V^m(E_m\cdot E_n)\).
4. Isolate the new object \(g_{mn}=E_m\cdot E_n\).
5. Compute the squared length: \(V\cdot V=(V^mE_m)\cdot(V^nE_n)=g_{mn}V^mV^n\).

Contraction lemma and scalar contraction:
1. Write the lemma \((\partial x^b/\partial y^m)(\partial y^m/\partial x^a)=\delta^b{}_a\).
2. Take a mixed tensor \(T^m{}_n=V^mW_n\).
3. Transform it: \(T'^m{}_n=(\partial y^m/\partial x^a)(\partial x^b/\partial y^n)V^aW_b\).
4. Contract the primed indices by setting \(m=n\) and summing.
5. The Jacobian product becomes \(\delta^b{}_a\) by the lemma.
6. The result reduces to \(V^aW_a\).
7. Conclude that the contraction has no free indices and is a scalar.

Why upper-upper contraction fails:
1. Start from an object with two upper indices, e.g. \(U^{mn}\).
2. Transform it with two factors of \(\partial y/\partial x\).
3. Illegitimately identify the two upper indices and sum.
4. The Jacobian structure becomes a product of two \(\partial y/\partial x\) factors.
5. No \((\partial x/\partial y)(\partial y/\partial x)\) pair appears.
6. Therefore no Kronecker delta emerges.
7. Conclude that upper-upper or lower-lower “contraction” does not preserve tensor character.

Metric transformation law:
1. Treat the squared length as a scalar: \(g_{mn}(x)dx^mdx^n=g'_{pq}(y)dy^pdy^q\).
2. Rewrite the unprimed differentials in terms of the primed ones: \(dx^m=(\partial x^m/\partial y^p)dy^p\), \(dx^n=(\partial x^n/\partial y^q)dy^q\).
3. Substitute both expressions into \(g_{mn}(x)dx^mdx^n\).
4. Factor out \(dy^pdy^q\).
5. Compare the coefficient of \(dy^pdy^q\) with the primed expression.
6. Identify the coefficient as \(g'_{pq}(y)\).
7. Read off \(g'_{pq}(y)=g_{mn}(x)(\partial x^m/\partial y^p)(\partial x^n/\partial y^q)\).

Inverse metric as matrix identity:
1. Regard \(g_{mn}\) as an \(N\times N\) symmetric matrix.
2. In the ordinary Riemannian discussion of the lecture, assume no zero eigenvalues.
3. Conclude the matrix is invertible.
4. Denote the inverse matrix by \(g^{mn}\).
5. Encode matrix inversion as \(g_{mn}g^{np}=\delta_m{}^{p}\).
6. In \(2\times2\), interpret this as four scalar equations, one per matrix entry.
7. Use those entrywise equations to clarify why the whole product is the identity matrix, not just the \(m=p\) case in isolation.

## Notation Choices
- Use \(x^m\) and \(y^m\) for coordinates, not transcript-style `xm`, `ym`.
- Use primes only to indicate components written in the \(y\)-coordinate system: \(V'^m\), \(g'_{pq}\), \(S'(y)\).
- Use \(\partial\), not \(d\), in Jacobian factors and coordinate derivatives: \(\partial y^m/\partial x^n\).
- Keep Einstein summation throughout; repeated one-up/one-down indices are summed.
- Do not write repeated upper-upper or lower-lower indices as a legal contraction.
- Use \(V^m\) / \(V_m\) for vector and covector components; keep “contravariant/covariant” in prose and “upstairs/downstairs” as informal explanatory language only.
- Keep \(E_m\) for basis vectors in the geometric interlude.
- Use lowercase \(g_{mn}\), \(g^{mn}\) in the notes, even though the transcript verbally sounds like capital \(G\) in places.
- Use \(\delta^b{}_a\) and \(\delta_m{}^{p}\) as mixed-index Kronecker deltas.
- Prefer \(ds^2\) for the squared interval in the final notes as a cautious cleanup of the spoken “squared length of the little \(dx\) vector.”
- Treat tensor product as juxtaposition in the main text to stay close to the lecture; reserve \(\otimes\) only if a later draft needs disambiguation.
- When the lecture says “frame,” read it as “coordinate system” in this chapter.
- Keep the metric-count examples exactly as used: 4D \(\to 10\), 3D \(\to 6\), 2D \(\to 3\); do not force a general formula unless needed later.

## Uncertain Mathematics
- The early “distinguish a fluid” transcript segment is garbled; the mathematical target is distinguishing truly flat geometry from merely funny coordinates.
- The transcript is corrupted around parts of the transformation-law discussion; use canonical tensor formulas only where the surrounding logic fixes them securely.
- The board only shows the subtraction example with ellipses; do not invent a definite full index pattern.
- The line element \(ds^2\) is a standard cleanup, not a literal board transcription.
- The symmetry \(g_{mn}=g_{nm}\) should be justified from the quadratic form \(dx^m dx^n\), not from the messy late exchange about why the matrix is symmetric.
- The statement “eigenvalues are never zero” belongs to the ordinary positive-metric discussion in this lecture; it must be paired with the later Lorentzian caveat.
- The \(2\times2\) matrix example on the board is unfinished; only the visible matrices and the identity interpretation are secure.
- The lecture suggests that \(g^{mn}\) is also a tensor, but the full proof is not developed here; present it as defined by matrix inversion and used as a tensor from this point on.
- The late tangent-space clarification is conceptually useful but not part of the main mathematical development; include it cautiously as a short clarification, not as a fully developed construction.
- The inner-product language is ordinary Euclidean/Riemannian language in this lecture; when the chapter later reaches Lorentzian signature, this language will need adjustment.