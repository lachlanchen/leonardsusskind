# Math Bank
## Core Equations
- \(x_1-x_2=0\) [transcript-backed]
- \(\vec r_1=\vec r_2,\qquad \vec r_1-\vec r_2=\vec 0\) [transcript-backed]
- \(X_1^{\mu}=X_2^{\mu}\) or equivalently \(X_1^{\mu}-X_2^{\mu}=0\) [standard reconstruction]
- \(x'=\gamma(x-vt),\qquad y'=y,\qquad z'=z,\qquad t'=\gamma(t-vx)\) [standard reconstruction]
- \[
\begin{pmatrix}
x'\\ y'\\ z'\\ t'
\end{pmatrix}
=
\begin{pmatrix}
\cos\theta & \sin\theta & 0 & 0\\
-\sin\theta & \cos\theta & 0 & 0\\
0 & 0 & 1 & 0\\
0 & 0 & 0 & 1
\end{pmatrix}
\begin{pmatrix}
x\\ y\\ z\\ t
\end{pmatrix}
\] [standard reconstruction]
- \(X'^{\mu}=L^{\mu}{}_{\nu}X^{\nu}\) [visible]
- \[
\begin{pmatrix}
x'\\ y'\\ z'\\ t'
\end{pmatrix}
=
L
\begin{pmatrix}
x\\ y\\ z\\ t
\end{pmatrix}
\] [standard reconstruction]
- \(A'^{\mu}=L^{\mu}{}_{\nu}A^{\nu}\) [transcript-backed]
- \(A_{\mu}=\eta_{\mu\nu}A^{\nu}\) [transcript-backed]
- \(\eta_{\mu\nu}=\mathrm{diag}(-1,-1,-1,+1)\) [transcript-backed]
- \(A_{\mu}A^{\mu}=-A_1^2-A_2^2-A_3^2+A_0^2\) [transcript-backed]
- \(X_{\mu}X^{\mu}=t^2-x^2-y^2-z^2\) [transcript-backed]
- \(A_{\mu}B^{\mu}=\eta_{\mu\nu}A^{\mu}B^{\nu}\) [transcript-backed]
- \(d\tau^2=dx_{\mu}dx^{\mu}=dt^2-dx^2-dy^2-dz^2\) [transcript-backed]
- \(u^{\mu}=\dfrac{dx^{\mu}}{d\tau}\) [transcript-backed]
- \(u_{\mu}u^{\mu}=1\) [transcript-backed]
- \(\gamma(v)=\dfrac{1}{\sqrt{1-v^2/c^2}}\) [transcript-backed]
- \(u^{i}=\gamma v^{i},\qquad u^{0}=\gamma\) [standard reconstruction]
- \(p^{\mu}=mu^{\mu}\) [transcript-backed]
- \(\vec F=q(\vec E+\vec v\times\vec B)\) [transcript-backed]
- \(A^{\mu}B^{\nu}=\text{2nd rank tensor}\) [visible]
- \(T'^{\mu\sigma}=L^{\mu}{}_{\nu}L^{\sigma}{}_{\tau}T^{\nu\tau}\) [standard reconstruction]
- \(T^{\mu\nu}=T^{\nu\mu}\) [transcript-backed]
- \(T^{\mu\nu}=-T^{\nu\mu}\) [transcript-backed]
- \(\#\{\text{independent components of a symmetric rank-2 tensor in 4D}\}=10\) [transcript-backed]
- \(\#\{\text{independent components of an antisymmetric rank-2 tensor in 4D}\}=6\) [transcript-backed]
- \(E_1=f_{10},\qquad E_2=f_{20},\qquad E_3=f_{30}\) [transcript-backed]
- \(f_{12}=-B_3\) with the remaining spatial relations obtained by cyclic permutation of \(1,2,3\) [transcript-backed]

## Definitions And Objects
- Homogeneity of space: invariance under translations of the origin.
- Isotropy of space: invariance under rotations of the axes.
- Rotationally invariant collision rule: collision occurs when the particles occupy the same spatial point.
- Lorentz invariant collision rule: collision occurs when the particles occupy the same spacetime event.
- Scalar: a quantity unchanged by the frame change under discussion; lecture examples are temperature and spatial distance.
- Three-vector in ordinary space: \(\vec r,\vec v,\vec E,\vec B\).
- Four-vector: object with four components transforming exactly as \((x,y,z,t)\) does.
- Contravariant components: upstairs index, e.g. \(A^{\mu}\).
- Covariant components: downstairs index, e.g. \(A_{\mu}\), obtained from \(A^{\mu}\) by \(\eta_{\mu\nu}\).
- Proper time: \(d\tau\), defined by the invariant spacetime interval along a worldline.
- Proper four-velocity: \(u^{\mu}=dx^{\mu}/d\tau\).
- Four-momentum: \(p^{\mu}=mu^{\mu}\).
- Rank-0 tensor: scalar.
- Rank-1 tensor: four-vector.
- Rank-2 tensor: object with two indices transforming like a product of two four-vectors; board example \(A^{\mu}B^{\nu}\).
- Rank-3 tensor: object with three indices transforming like a product of three four-vectors; board example \(A^{\mu}B^{\nu}C^{\sigma}\).
- Symmetric rank-2 tensor: unchanged when the two indices are interchanged.
- Antisymmetric rank-2 tensor: changes sign when the two indices are interchanged; diagonal entries vanish.
- Electromagnetic field object: lecture denotes it by \(f_{\mu\nu}\), an antisymmetric rank-2 tensor built from \(\vec E\) and \(\vec B\).
- Three-dimensional accident: an antisymmetric \(3\times 3\) tensor has 3 independent components and can therefore be identified with an ordinary spatial vector; this does not extend to 4D.

## Derivation Steps
Rotationally invariant collision law
1. Start with the toy law \(x_1-x_2=0\).
2. Observe that this does not pick a preferred origin, so homogeneity is not the issue.
3. Rotate the axes and note that the law changes form, so isotropy is violated.
4. Repair the law by requiring equality of all spatial coordinates at once.
5. Rewrite that repair as \(\vec r_1-\vec r_2=\vec 0\).

Spacetime version of the same argument
1. Consider the Newtonian-looking rule “the two times are equal.”
2. Note that simultaneity is frame-dependent in special relativity.
3. Therefore a condition on only the time component cannot be Lorentz invariant.
4. Require instead that the full separation four-vector between the two events vanish.
5. Conclude that collision must mean coincidence at a single spacetime event.

Why vector equations survive frame changes
1. A single component being zero is not a frame-independent statement.
2. A whole vector being zero is frame-independent because all components transform coherently.
3. The same logic applies to equality of two vectors.
4. Therefore laws should be written as whole-vector equalities or whole-vector zero statements.

Lowering an index and building invariants
1. Introduce \(\eta_{\mu\nu}\) with three negative spatial signs and one positive time sign.
2. Define \(A_{\mu}=\eta_{\mu\nu}A^{\nu}\).
3. This flips the signs of the spatial components and leaves the time component unchanged.
4. Form \(A_{\mu}A^{\mu}\) to recover the Minkowski norm.
5. Use the same device to form bilinears \(A_{\mu}B^{\mu}\).

Why \(A_{\mu}B^{\mu}\) is invariant
1. If \(A^{\mu}\) and \(B^{\mu}\) are four-vectors, then \(A^{\mu}+B^{\mu}\) and \(A^{\mu}-B^{\mu}\) are also four-vectors.
2. The Minkowski norm of any four-vector is invariant.
3. Therefore \((A+B)_{\mu}(A+B)^{\mu}\) and \((A-B)_{\mu}(A-B)^{\mu}\) are both invariant.
4. Expand both expressions.
5. Subtract them to isolate the cross term \(A_{\mu}B^{\mu}\).
6. Conclude that \(A_{\mu}B^{\mu}\) is invariant.

Proper four-velocity
1. Start with the infinitesimal displacement \(dx^{\mu}\) along a worldline.
2. Define \(d\tau^2=dx_{\mu}dx^{\mu}\).
3. Divide \(dx^{\mu}\) by \(d\tau\) to define \(u^{\mu}=dx^{\mu}/d\tau\).
4. Compute \(u_{\mu}u^{\mu}=(dx_{\mu}dx^{\mu})/d\tau^2=1\).
5. Conclude that the four-velocity is a unit timelike four-vector.

Relation between \(u^{\mu}\) and ordinary velocity
1. Write \(u^{i}=dx^{i}/d\tau=(dx^{i}/dt)(dt/d\tau)=v^{i}(dt/d\tau)\).
2. Use \(d\tau^2=dt^2-dx^2-dy^2-dz^2\).
3. Divide by \(dt^2\) to get \((d\tau/dt)^2=1-v^2/c^2\).
4. Invert to obtain \(dt/d\tau=\gamma\).
5. Hence \(u^{i}=\gamma v^{i}\) and \(u^{0}=dt/d\tau=\gamma\).

Four-momentum
1. Ordinary \(m\vec v\) is not a four-vector.
2. Multiply the genuine four-vector \(u^{\mu}\) by rest mass \(m\).
3. Define \(p^{\mu}=mu^{\mu}\).
4. Read the first three components as relativistic momentum.
5. Read the final component as energy in the low-velocity limit.

Why electric and magnetic fields must mix
1. Start from the pre-Einstein law \(\vec F=q(\vec E+\vec v\times\vec B)\).
2. Imagine a frame in which only a magnetic field is present.
3. Move to the rest frame of the charged particle, so \(\vec v=0\).
4. The magnetic-force term disappears in that frame.
5. The acceleration cannot disappear merely by changing frame.
6. Therefore an electric field must appear in the new frame.
7. Conclude that \(\vec E\) and \(\vec B\) are not invariantly separate objects.

Rank-2 tensor transformation law
1. Begin with the product \(A^{\mu}B^{\sigma}\).
2. Transform \(A^{\mu}\) with one factor of \(L^{\mu}{}_{\nu}\).
3. Transform \(B^{\sigma}\) with one factor of \(L^{\sigma}{}_{\tau}\).
4. Multiply the transformed expressions.
5. Read off the pattern \(T'^{\mu\sigma}=L^{\mu}{}_{\nu}L^{\sigma}{}_{\tau}T^{\nu\tau}\).
6. Generalize this pattern as the defining transformation law for a second-rank tensor.

Counting symmetric and antisymmetric components
1. A generic \(4\times 4\) rank-2 tensor has 16 components.
2. For a symmetric tensor, entries reflected across the diagonal are equal.
3. Count 4 diagonal entries and 6 independent off-diagonal entries.
4. Obtain \(10\) independent components.
5. For an antisymmetric tensor, diagonal entries vanish.
6. Only one triangular half is independent.
7. Obtain \(6\) independent components.

Magnetic and electric pieces inside \(f_{\mu\nu}\)
1. Use antisymmetry to fill only one triangular half of the \(4\times 4\) matrix.
2. Place magnetic components in the purely spatial slots.
3. Place electric components in the slots involving the time index \(0\).
4. In three dimensions, the spatial antisymmetric block has 3 independent components and matches \(\vec B\).
5. In four dimensions, the full antisymmetric tensor has 6 independent components, matching \((\vec E,\vec B)\) together.

## Notation Choices
- Use Greek indices \(\mu,\nu,\sigma,\tau\) for spacetime indices.
- Use the lecture’s index ordering \((1,2,3,0)\), with \(0\) as the time index.
- Standardize the time component as \(0\), not \(4\), even when the transcript briefly drifts to \(a_4\).
- Use \(X^{\mu}\) for the spacetime position four-vector when writing generic transformation laws.
- Use \(L^{\mu}{}_{\nu}\) for the generic Lorentz/rotation transformation matrix.
- Use Einstein summation only when one repeated index is upstairs and the other is downstairs.
- Use \(\eta_{\mu\nu}=\mathrm{diag}(-1,-1,-1,+1)\); this lecture uses “space negative, time positive.”
- Use upstairs indices for contravariant components and downstairs indices for covariant components.
- Use \(u^{\mu}\) for proper four-velocity; reserve \(\vec v\) for ordinary three-velocity.
- Use \(p^{\mu}=mu^{\mu}\) for four-momentum.
- Use \(T^{\mu\nu}\) for a generic rank-2 tensor.
- Use \(f_{\mu\nu}\) for the electromagnetic field tensor to stay close to the lecture’s board language.
- Use \(\vec E\) and \(\vec B\) for ordinary spatial electric and magnetic fields.
- Treat products like \(A_{\mu}B^{\mu}\) as scalar contractions, not as a row/column-conversion story; the lecture explicitly warns not to lean too hard on that picture here.
- Keep \(c=1\) by default in the body of the chapter, restoring \(c\) only when clarifying units or low-velocity limits.

## Uncertain Mathematics
- The boost formulas are secure in standard form, but the transcript around the explicit \(t'\) equation is garbled; use the standard \(t'=\gamma(t-vx)\) cautiously as normalization.
- The rotation formulas around the \(z\)-axis are partly corrupted in the transcript; the standard \(4\times4\) rotation matrix is the right clean reconstruction.
- The matrix-to-index transition around \(00{:}25\)–\(00{:}26\) is garbled; keep only the secure cleaned law \(X'^{\mu}=L^{\mu}{}_{\nu}X^{\nu}\).
- The transcript briefly confuses \(a_4\) and \(a_0\); final notes should silently normalize to \(0\).
- The board/example column for lowered components is corrected live by a student; do not reproduce the inconsistent intermediate version.
- The exact full sign pattern of the electromagnetic tensor should be stated cautiously until checked against video or board context.
- The following are secure enough to keep: \(E_i=f_{i0}\), the purely spatial entries encode \(\vec B\), and the magnetic slots follow a cyclic pattern across \(1,2,3\).
- The exact component-by-component matrix reconstruction of \(f_{\mu\nu}\) should be verified before final LaTeX if the notes present the full \(4\times4\) array.
- The transcript’s proof of bilinear invariance is conceptually clear, but the spoken arithmetic factor in the subtraction is noisy; final notes should present the clean algebra rather than the garbled spoken coefficient.
- The phrase “Lorentz transformation” is momentarily used where “field tensor” is clearly intended in the electromagnetic discussion; final notes should correct that without fanfare.