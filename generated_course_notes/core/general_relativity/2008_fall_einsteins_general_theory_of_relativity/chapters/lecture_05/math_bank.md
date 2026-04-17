# Math Bank
## Core Equations
- \(V_n(y)=\dfrac{\partial x^r}{\partial y^n}V_r(x)\) [transcript-backed]
- \(T^m{}_n(y)=\dfrac{\partial y^m}{\partial x^r}\dfrac{\partial x^s}{\partial y^n}T^r{}_s(x)\) [transcript-backed]
- \(\dfrac{\partial \phi}{\partial y^n}=\dfrac{\partial x^m}{\partial y^n}\dfrac{\partial \phi}{\partial x^m}\) [transcript-backed]
- \(T_{mn}(x)\equiv \dfrac{\partial V_m(x)}{\partial x^n}\) [transcript-backed]
- \(T_{mn}(y)=\dfrac{\partial x^r}{\partial y^m}\dfrac{\partial x^s}{\partial y^n}\dfrac{\partial V_r(x)}{\partial x^s}\) under the temporary assumption that \(T_{mn}\) is a tensor [transcript-backed]
- \(V_m(y)=\dfrac{\partial x^r}{\partial y^m}V_r(x)\) [transcript-backed]
- \(\dfrac{\partial V_m(y)}{\partial y^n}=\dfrac{\partial x^r}{\partial y^m}\dfrac{\partial V_r(x)}{\partial y^n}+\dfrac{\partial}{\partial y^n}\!\left(\dfrac{\partial x^r}{\partial y^m}\right)V_r(x)\) [transcript-backed]
- \(\nabla_n V_m=\dfrac{\partial V_m}{\partial y^n}+\Gamma^r{}_{nm}V_r\) [visible]
- \(\dfrac{\partial V_m}{\partial y^n}+\Gamma^r{}_{nm}V_r=T_{mn}\) [visible]
- \(\nabla_p V_m=\dfrac{\partial V_m}{\partial y^p}+\Gamma^r{}_{pm}V_r\) [standard reconstruction]
- \(\dfrac{\partial V_m}{\partial y^p}+\Gamma^r{}_{pm}V_r=T_{mp}\) [partially visible]
- \(\nabla_p T_{mn}=\dfrac{\partial T_{mn}}{\partial y^p}+\Gamma^r{}_{pm}T_{rn}+\Gamma^r{}_{pn}T_{mr}\) [standard reconstruction]
- \(\nabla_m V^n=\dfrac{\partial V^n}{\partial y^m}+\Gamma^n{}_{mr}V^r\) [transcript-backed]
- \(V_\theta=0,\qquad V_r=1\) in polar coordinates [transcript-backed]
- \(\nabla_r g_{mn}=0\) [transcript-backed]
- \(\nabla_p g_{mn}=\dfrac{\partial g_{mn}}{\partial y^p}+\Gamma^r{}_{pm}g_{rn}+\Gamma^r{}_{pn}g_{mr}=0\) [standard reconstruction]
- \(\Gamma^A{}_{BC}=\dfrac12\,g^{AD}\!\left(\dfrac{\partial g_{DC}}{\partial x^B}+\dfrac{\partial g_{DB}}{\partial x^C}-\dfrac{\partial g_{BC}}{\partial x^D}\right)\) [standard reconstruction]
- \(\dfrac{d\phi}{ds}=\dfrac{\partial \phi}{\partial y^m}\dfrac{dy^m}{ds}\) [transcript-backed]
- \(t^m\equiv \dfrac{dy^m}{ds}\) [transcript-backed]
- \(\dfrac{D V^n}{Ds}=\nabla_m V^n\,\dfrac{dy^m}{ds}\) [transcript-backed]
- \(\dfrac{D V^n}{Ds}=\dfrac{dV^n}{ds}+\Gamma^n{}_{mr}V^r\dfrac{dy^m}{ds}\) [standard reconstruction]
- For the tangent vector \(t^n=\dfrac{dy^n}{ds}\),
  \[
  \dfrac{D t^n}{Ds}
  =\dfrac{d^2 y^n}{ds^2}+\Gamma^n{}_{mr}\dfrac{dy^m}{ds}\dfrac{dy^r}{ds}
  \]
  [standard reconstruction]
- Geodesic condition:
  \[
  \dfrac{D t^n}{Ds}=0
  \]
  [transcript-backed]

## Definitions And Objects
- Tensor criterion used throughout the lecture: if an object vanishes in one coordinate system and transforms tensorially, it vanishes in all coordinate systems.
- Covariant derivative: the corrected derivative operation that maps tensors to tensors.
- \(\Gamma^r{}_{nm}\): the correction term needed because coordinates “flop around” from point to point.
- Christoffel symbols / connection / affine connection: names used for \(\Gamma\).
- Important status claim: Christoffel symbols are not tensors.
- Tangent vector to a curve:
  \[
  t^m=\dfrac{dy^m}{ds}
  \]
  and it is a unit vector when \(s\) is arc length.
- Geodesic: a curve whose tangent vector is covariantly constant.
- Locally Cartesian coordinates: coordinates chosen near a point so that \(g_{mn}=\delta_{mn}\) at that point and, in the lecture’s discussion, the first derivatives of \(g\) can also be made to vanish there.
- Exterior derivative: mentioned only to distinguish it from covariant differentiation; in three dimensions Susskind identifies it with curl for a vector field.

## Derivation Steps
Ordinary derivative of a scalar transforms well:
1. Start from scalar invariance: \(\phi(x)=\phi(y)\).
2. Differentiate with respect to \(y^n\).
3. Apply chain rule to get \(\partial\phi/\partial y^n=(\partial x^m/\partial y^n)(\partial\phi/\partial x^m)\).
4. Conclude that \(\partial_n\phi\) transforms as a covariant vector.

Failed tensor test for \(\partial_n V_m\):
1. Define \(T_{mn}(x)\equiv \partial V_m(x)/\partial x^n\).
2. Assume temporarily that \(T_{mn}\) is a tensor.
3. Transform it to \(y\)-coordinates using the tensor transformation law.
4. Rewrite the transformed expression using \(V_m(y)=(\partial x^r/\partial y^m)V_r(x)\).
5. Differentiate \(V_m(y)\) with respect to \(y^n\).
6. Use the product rule.
7. Observe that one term matches the transformed tensor-like piece.
8. Observe the extra term \(\partial_{y^n}(\partial x^r/\partial y^m)\,V_r(x)\).
9. Conclude that \(\partial V_m/\partial y^n\) is not the \(y\)-component of a tensor.

Motivation for the covariant derivative:
1. Isolate the extra non-tensorial term from the failed transformation.
2. Name its coefficient \(\Gamma^r{}_{nm}\).
3. Add a compensating term \(\Gamma^r{}_{nm}V_r\) to the ordinary derivative.
4. Define the sum to be \(\nabla_n V_m\).
5. Demand that this new object transform tensorially.

General rule for lower-index tensors:
1. Begin with the ordinary derivative \(\partial_p T_{mn}\).
2. Treat one covariant index at a time as if the others were “just along for the ride.”
3. Add one gamma term for the \(m\)-slot: \(\Gamma^r{}_{pm}T_{rn}\).
4. Add one gamma term for the \(n\)-slot: \(\Gamma^r{}_{pn}T_{mr}\).
5. Generalize: one correction term for each lower index.

Metric compatibility to connection formula:
1. Impose \(\nabla_p g_{mn}=0\).
2. Expand it into \(\partial_p g_{mn}\) plus two \(\Gamma g\) terms.
3. Regard the resulting identity as an equation for \(\Gamma\).
4. Use inverse metric components to solve for the upper index on \(\Gamma\).
5. The cleaned result is the Christoffel-symbol formula built from first derivatives of \(g\).

Derivative along a curve:
1. Parameterize the curve by arc length \(s\).
2. Define the tangent vector \(t^m=dy^m/ds\).
3. For a scalar, contract \(\partial_m\phi\) with \(dy^m/ds\) to get \(d\phi/ds\).
4. For a vector, replace the ordinary derivative by the covariant derivative.
5. Define \(DV^n/Ds=\nabla_m V^n\,(dy^m/ds)\).

Geodesic equation:
1. Set \(V^n=t^n=dy^n/ds\).
2. Compute \(D t^n/Ds\).
3. The first term becomes \(d^2 y^n/ds^2\).
4. The second term becomes \(\Gamma^n{}_{mr}(dy^m/ds)(dy^r/ds)\).
5. Set the whole covariant derivative to zero.
6. Interpret the result as the condition for the tangent vector to be covariantly constant.

## Notation Choices
- Use \(x\)-coordinates for Cartesian / flat-coordinate calculations and \(y\)-coordinates for general curvilinear coordinates, matching the lecture’s main contrast.
- Use lower-index vector components \(V_m\) for the board-backed covariant-derivative formula, since that is what the frames show.
- Use \(\nabla_n\) for the covariant derivative operator; describe it as “upside-down triangle with an index downstairs.”
- Keep the lecture’s visible lower-index formula with a plus sign:
  \[
  \nabla_n V_m=\partial_n V_m+\Gamma^r{}_{nm}V_r
  \]
  and annotate later if the chapter normalizes to a different covector sign convention.
- Use \(p\) as the derivative index in the two-index tensor example, since Susskind explicitly reletters that index mid-derivation.
- Use \(r,s\) as dummy summation indices in transformation laws and gamma terms.
- Use \(A,B,C,D\) in the Christoffel formula, matching the lecture’s late switch to alphabetic indices.
- Use \(s\) for arc length / path parameter along a curve.
- Use \(t^m\) or directly \(dy^m/ds\) for the tangent vector; the lecture mostly writes the latter explicitly.
- Preserve the distinction:
  - “covariant derivative” names the operator,
  - “covariant vector” refers to lower-index components.
- Preserve the lecture’s index-bookkeeping rule:
  - dummy repeated indices may be renamed,
  - free indices may not be swapped unless symmetry is separately known.

## Uncertain Mathematics
- The transcript around the transformation-law derivation is verbally messy; the logical structure is clear, but some spoken index labels are corrupted and should not be copied verbatim.
- The board-backed lower-index formula uses a plus \(\Gamma V\) term. This conflicts with many standard conventions for covectors, so the final chapter must either follow Susskind’s lecture convention consistently or explicitly note any normalization.
- In `lecture_05_figure_03.png`, \(T_{mp}\) on the right-hand side is the best reconstruction but is partially occluded.
- The shorthand \(\nabla_n V_m\) and \(\nabla_p V_m\) beneath the main board line are only partially visible and should be treated as supportive reconstruction, not exact clean transcription.
- The index-heavy section from roughly 00:47 to 00:55 includes ASR corruption; the general rule for \(\nabla_p T_{mn}\) is reliable, but local spoken corrections must be normalized carefully.
- In the polar-coordinate discussion, Susskind appears to misspeak one metric component near the end; the standard flat polar metric is
  \[
  ds^2=dr^2+r^2 d\theta^2,
  \]
  so the relevant nonconstant component is \(g_{\theta\theta}=r^2\), not \(g_{rr}\).
- The transcript’s spoken metric-compatibility expansion is fragmentary; the cleaned form with two \(\Gamma g\) terms is the safe reconstruction.
- The Christoffel formula should be presented as the cleaned endpoint of the lecture’s argument, not as a verbatim transcript equation, because the spoken line-reading is partially garbled.
- The pathwise covariant derivative is clear conceptually in the transcript, but the lecture writes some later curve formulas for contravariant components while the board screenshots earlier show lower-index components; the chapter writer should keep the two contexts separate rather than blending them.