# Math Bank
## Core Equations
- \(\mathbf F=\dfrac{d\mathbf p}{dt}\) [transcript-backed]
- \(\dfrac{d\mathbf p}{dt}=q(\mathbf E+\mathbf v\times\mathbf B)\) [transcript-backed]
- \(T_{mn}=A_mB_n\) [transcript-backed]
- \(A_mB_n-A_nB_m\) [transcript-backed]
- \(C_3=A_1B_2-A_2B_1\) [visible]
- \(C_1=A_2B_3-A_3B_2\) [visible]
- \(C_2=A_3B_1-A_1B_3\) [visible]
- \(\begin{pmatrix}0&C_3&-C_2\\-C_3&0&C_1\\C_2&-C_1&0\end{pmatrix}\) [standard reconstruction]
- \(B_{12}=-B_3,\qquad B_{13}=B_2,\qquad B_{23}=-B_1\) [transcript-backed]
- \(\begin{pmatrix}0&-B_3&B_2\\B_3&0&-B_1\\-B_2&B_1&0\end{pmatrix}\) [standard reconstruction]
- \((\mathbf v\times\mathbf B)_m=v_nB_{nm}\) [transcript-backed]
- \(F_m^{(\mathrm{mag})}=q\,v_nB_{nm}\) [transcript-backed]
- \(\dfrac{d}{dt}(v_mv_m)=2\,\dot v_m v_m\) [transcript-backed]
- \(\dfrac{d}{dt}(v_mv_m)\propto (\mathbf v\times\mathbf B)_m v_m=v_nB_{nm}v_m=0\) [transcript-backed]
- \(u^\mu=\dfrac{dx^\mu}{d\tau}\) [transcript-backed]
- \(\gamma=\dfrac{1}{\sqrt{1-v^2}}\) [transcript-backed]
- \(u^\mu=\gamma(v_x,v_y,v_z,1)\) [transcript-backed]
- \(p^\mu=mu^\mu\) [transcript-backed]
- \(\dfrac{dp^\mu}{d\tau}=f^\mu\) [transcript-backed]
- \(u_\mu u^\mu=1\) [transcript-backed]
- \(\dfrac{d}{d\tau}(u_\mu u^\mu)=0\) [transcript-backed]
- \(2\,\dfrac{du^\mu}{d\tau}u_\mu=0\) [standard reconstruction]
- \(f_\mu u^\mu=0\) [transcript-backed]
- \(f^\mu=q\,F^{\mu\nu}u_\nu\) [standard reconstruction]
- \(F^{\mu\nu}u_\nu u_\mu=0\) [visible]
- In the lecture’s \(1,2,3,0\) ordering,
  \[
  F_{\mu\nu}=
  \begin{pmatrix}
  0 & -B_3 & B_2 & E_1\\
  B_3 & 0 & -B_1 & E_2\\
  -B_2 & B_1 & 0 & E_3\\
  -E_1 & -E_2 & -E_3 & 0
  \end{pmatrix}
  \]
  [standard reconstruction]
- \(\dfrac{dp_x}{d\tau}=q(F_{xy}u_y+F_{xz}u_z+F_{x0}u_0)\) [transcript-backed]
- \(\dfrac{dp_x}{dt}=q(E_x+v_yB_3-v_zB_2)\) [transcript-backed]
- \(\dfrac{dp}{dt}=q(\mathbf E+\mathbf v\times\mathbf B)\) with \(p=m\gamma \mathbf v\) [transcript-backed]
- \(x_1'=\dfrac{x_1-vx_0}{\sqrt{1-v^2}},\qquad x_0'=\dfrac{x_0-vx_1}{\sqrt{1-v^2}},\qquad x_2'=x_2,\qquad x_3'=x_3\) [transcript-backed]
- \(F'_{01}=F_{01}\) for a boost along the \(1\)-axis [transcript-backed]
- \(E_2'=\gamma(E_2+vB_3)\) in the lecture’s convention for a boost along the \(1\)-axis [transcript-backed]
- \(\partial_\mu\phi=\dfrac{\partial\phi}{\partial x^\mu}\) [transcript-backed]
- \(\partial^\mu\phi\) is obtained by changing the sign of the spatial components of \(\partial_\mu\phi\) [transcript-backed]
- \(\partial^\mu\partial_\mu\phi=0\) [transcript-backed]
- \(\dfrac{\partial^2\phi}{\partial t^2}-\dfrac{\partial^2\phi}{\partial x^2}-\dfrac{\partial^2\phi}{\partial y^2}-\dfrac{\partial^2\phi}{\partial z^2}=0\) [transcript-backed]

## Definitions And Objects
- \(\mathbf E\): ordinary three-vector electric field, position- and time-dependent.
- \(\mathbf B\): ordinary three-vector magnetic field, position- and time-dependent.
- \(q\): electric charge.
- \(\mathbf p\): ordinary momentum; relativistically \( \mathbf p = m\gamma \mathbf v\).
- \(A_m,B_n\): temporary three-vector components used to rebuild the cross product as a tensor.
- \(T_{mn}=A_mB_n\): basic rank-two spatial tensor made from two vectors.
- \(A_mB_n-A_nB_m\): antisymmetric spatial tensor associated with the cross product.
- \(C_m\): components of \(\mathbf C=\mathbf A\times\mathbf B\), identified with the three independent entries of the antisymmetric tensor.
- \(B_{mn}\): antisymmetric spatial tensor representation of the magnetic field; lecture uses the historical extra minus sign convention.
- \(F_{\mu\nu}\): antisymmetric electromagnetic field tensor containing both \(\mathbf E\) and \(\mathbf B\).
- \(\tau\): proper time.
- \(u^\mu\): four-velocity.
- \(p^\mu\): four-momentum.
- \(f^\mu\): four-force, defined by \(dp^\mu/d\tau\).
- \(\gamma=(1-v^2)^{-1/2}\): Lorentz factor, with \(c=1\).
- \(\phi\): scalar field.
- \(\partial_\mu\phi\): covariant derivative components of a scalar field.
- \(\partial^\mu\): raised-index derivative operator, with spatial sign flip relative to \(\partial_\mu\).

## Derivation Steps
Cross product as antisymmetric tensor
1. Start from the rank-two spatial tensor \(T_{mn}=A_mB_n\).
2. Antisymmetrize it to get \(A_mB_n-A_nB_m\).
3. Note that all diagonal entries vanish.
4. Note that entries below the diagonal are negatives of the reflected entries above the diagonal.
5. Conclude that only three independent components remain.
6. Identify those three components with a vector \(C_m\).
7. Use the corrected cyclic formulas \(C_3,C_1,C_2\) to fix the sign pattern.
8. Read the cross product either as a vector or as the antisymmetric tensor carrying the same three degrees of freedom.

Magnetic force in tensor form
1. Start from the ordinary component formula, e.g. \((\mathbf v\times\mathbf B)_3=v_1B_2-v_2B_1\).
2. Replace \(B_2\) and \(B_1\) by tensor components using the lecture’s \(B_{mn}\) convention.
3. Add the vanishing diagonal term \(v_3B_{33}\).
4. Recognize the summed pattern \(v_nB_{nm}\).
5. Rewrite the magnetic part of the Lorentz force as \(F_m^{(\mathrm{mag})}=q\,v_nB_{nm}\).

Speed conservation in a pure magnetic field
1. Set \(\mathbf E=0\).
2. Differentiate \(v_mv_m\) with respect to time.
3. Obtain \(2\,\dot v_m v_m\).
4. Replace \(\dot v_m\) by the magnetic-force term, up to overall constants.
5. Use \((\mathbf v\times\mathbf B)_m=v_nB_{nm}\).
6. Get a contraction of the form \(v_nB_{nm}v_m\).
7. Note that \(v_nv_m\) is symmetric in \(n,m\), while \(B_{nm}\) is antisymmetric.
8. Conclude the contraction vanishes, so \(d(v^2)/dt=0\).

Frame-mixing argument for \(E\) and \(B\)
1. Take a frame with a magnetic field along one axis and a particle moving along a perpendicular axis.
2. Observe that \( \mathbf v\times \mathbf B\) gives a force along the third axis.
3. Introduce a second observer moving with the particle.
4. In that observer’s frame the particle is instantaneously at rest, so the magnetic term cannot account for the force.
5. Demand that the law of motion be the same in both frames.
6. Infer that an electric field must appear in the co-moving frame.
7. Conclude that electric and magnetic fields must mix under changes of frame.

Orthogonality of four-force
1. Start from the normalization \(u_\mu u^\mu=1\).
2. Differentiate with respect to \(\tau\).
3. Apply the product rule.
4. Use symmetry of the scalar product to combine the two terms.
5. Get \(2\,(du^\mu/d\tau)u_\mu=0\).
6. Multiply by \(m\) and identify \(m\,du^\mu/d\tau=dp^\mu/d\tau=f^\mu\).
7. Conclude \(f_\mu u^\mu=0\).

Covariant force ansatz from antisymmetry
1. Require a four-force built from charge, field data, and four-velocity.
2. Require it to satisfy \(f_\mu u^\mu=0\).
3. Recall the three-dimensional analogue: antisymmetric tensor contracted with the velocity.
4. Try \(f^\mu=q\,F^{\mu\nu}u_\nu\).
5. Contract with \(u_\mu\).
6. Obtain \(q\,F^{\mu\nu}u_\nu u_\mu\).
7. Use antisymmetry of \(F^{\mu\nu}\) and symmetry of \(u_\nu u_\mu\).
8. Conclude the contraction vanishes automatically.

Recovery of the ordinary Lorentz force
1. Compute a spatial component such as \(dp_x/d\tau=q(F_{xy}u_y+F_{xz}u_z+F_{x0}u_0)\).
2. Identify \(F_{x0}\) with the electric-field component.
3. Identify \(F_{xy}\) and \(F_{xz}\) with magnetic-field components using the lecture’s sign convention.
4. In the slow-velocity limit, replace \(u_i\) by \(v_i\) and \(u_0\) by \(1\).
5. Recover \(dp_x/dt=q(E_x+v_yB_3-v_zB_2)\).
6. Repeat cyclically to obtain \(d\mathbf p/dt=q(\mathbf E+\mathbf v\times\mathbf B)\).
7. Remove the slow-velocity shortcut by writing \(u_i=\gamma v_i\) and \(u_0=\gamma\).
8. Cancel the common gamma factor against \(dp^\mu/d\tau=\gamma\,dp^\mu/dt\).
9. Keep the relativistic correction in \( \mathbf p=m\gamma\mathbf v\), not in the formal shape of the Lorentz-force equation.

Boost transformation example
1. Write the boost along the \(1\)-axis for vector components.
2. Use a simple tensor \(a_\mu b_\nu\) as the model for tensor transformation.
3. Compute the transformed \(01\) component.
4. Replace the simple tensor entries by \(F_{\mu\nu}\).
5. Use antisymmetry to eliminate \(F_{00}\) and \(F_{11}\), and use \(F_{10}=-F_{01}\).
6. Conclude \(F'_{01}=F_{01}\), so the field component parallel to the boost is unchanged.
7. For a transverse component, compute the transformed \(02\) component.
8. Replace \(F_{02}\) by \(E_2\) and \(F_{12}\) by the corresponding magnetic component.
9. Conclude \(E_2'=\gamma(E_2+vB_3)\) in the lecture’s convention.

Scalar wave equation
1. Start with a scalar field \(\phi(x)\).
2. Form \(\partial_\mu\phi\), which transforms as a covariant four-vector.
3. Raise the derivative index to get \(\partial^\mu\).
4. Contract upper and lower indices to form a scalar.
5. Write the simplest invariant wave equation as \(\partial^\mu\partial_\mu\phi=0\).
6. Expand the contraction into one time derivative term and three spatial derivative terms with minus signs.

## Notation Choices
- Use \(\mu,\nu\) for spacetime indices with range \(0,1,2,3\).
- Use \(m,n\) for spatial indices with range \(1,2,3\).
- Keep repeated-index summation implicit.
- Keep \(c=1\) throughout the chapter unless explicitly restoring factors by dimensional analysis.
- Use boldface for ordinary three-vectors in the polished notes: \(\mathbf E,\mathbf B,\mathbf v,\mathbf p\).
- Use \(C_m\) for the components of \(\mathbf A\times\mathbf B\).
- Use \(B_{mn}\) for the antisymmetric spatial magnetic tensor.
- Use uppercase \(F_{\mu\nu}\) for the electromagnetic field tensor.
- Use lowercase \(f^\mu\) for four-force; do not overload \(f\) for both force and field tensor in the final notes.
- Use \(u^\mu\) for four-velocity and \(u_\mu\) for the lowered components.
- Use \(p^\mu=mu^\mu\) and \(\mathbf p=m\gamma\mathbf v\).
- Lowering an index means flipping the signs of the spatial components, consistent with the lecture’s \(+---\) signature convention.
- When reconstructing the electromagnetic matrix, note explicitly if the ordering is the lecture’s \(1,2,3,0\) rather than the more common \(0,1,2,3\).
- For the field-transformation formulas, mark them as being in the lecture’s sign convention if the chapter later standardizes notation.
- Use \(\partial_\mu\phi\) and \(\partial^\mu\phi\) rather than \(d\phi/dx^\mu\) once the final notes are cleaned, but keep a sentence acknowledging that Susskind speaks in derivative-component language.

## Uncertain Mathematics
- The temporary placement of \(C_2\) in the upper-right entry of the antisymmetric \(3\times 3\) matrix is a board-stage mistake; the final cleaned matrix should use \(-C_2\) there.
- The lower-left and lower-middle entries of the cross-product tensor are not fully legible from the frame alone; they should be filled by antisymmetry, not by direct visual transcription.
- The exact board-written index placement in the upper orthogonality line near `lecture_07_figure_05.png` is not secure; the clean form \(2\,(du^\mu/d\tau)u_\mu=0\) is a cautious normalization.
- The leftmost symbol in the force-ansatz frame is cropped; \(f^\mu=qF^{\mu\nu}u_\nu\) is transcript-supported but not fully image-visible.
- The lecture verbally oscillates between \(F\) and \(f\) notation for the field tensor / force object; the final notes should regularize this explicitly.
- The electromagnetic field-tensor matrix is transcript-backed but partly convention-driven; if translated into the standard \(0,1,2,3\) ordering, the displayed sign pattern must be recomputed consistently.
- The boost-transformation sign in formulas like \(E_2'=\gamma(E_2+vB_3)\) depends on the lecture’s field-tensor convention; do not silently merge it with a different textbook convention.
- The transcript has minor garbling in the cross-product correction stretch and in some tensor-transformation passages; the final notes should prefer the stabilized board formulas plus cautious standard cleanup.
- The wave-equation section is intentionally minimal; additional right-hand sides such as \(m^2\phi\) are mentioned only as possibilities, not developed as part of the main derivation.