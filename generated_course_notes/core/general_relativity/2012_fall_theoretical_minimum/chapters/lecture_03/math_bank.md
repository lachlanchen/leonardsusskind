# Math Bank
## Core Equations
- [visible] \(x^m = y^m + C^m{}_{nr}\, y^n y^r\)
- [standard reconstruction] \(x^m = y^m + C^m{}_{nr}\, y^n y^r + O(y^3)\)
- [visible] \(g_{mn} = \delta_{mn} \quad \text{at } x=0\)
- [visible] \(\partial_r g_{mn} = 0 \quad \text{at } x=0\)
- [visible] \(\partial_r \partial_s g_{mn} \neq 0\)
- [transcript-backed] \(ds^2 = g_{mn}\,dx^m dx^n\)
- [transcript-backed] \(g^{mr}g_{rn} = \delta^m{}_n\)
- [transcript-backed] \(V_n = g_{nm}V^m\)
- [transcript-backed] \(V^m = g^{mn}V_n\)
- [visible] \(\dfrac{\partial V_m}{\partial x^r} = 0\)
- [standard reconstruction] \(\nabla_r V_m = \partial_r V_m - \Gamma^{t}{}_{rm}V_t\)
- [standard reconstruction] \(\nabla_s T_{mn} = \partial_s T_{mn} - \Gamma^{t}{}_{sm}T_{tn} - \Gamma^{t}{}_{sn}T_{mt}\)
- [transcript-backed] \(\Gamma^{t}{}_{rm} = \Gamma^{t}{}_{mr}\)
- [transcript-backed] \(\Gamma^{t}{}_{rm}(x_0)=0\) in Gaussian normal coordinates at the chosen point
- [transcript-backed] \(0=\nabla_s g_{mn}=\partial_s g_{mn}-\Gamma^{t}{}_{sm}g_{tn}-\Gamma^{t}{}_{sn}g_{mt}\)
- [transcript-backed] \(\nabla_s g_{mn}=0\)
- [standard reconstruction] \(\Gamma^{t}{}_{mn}=\dfrac12 g^{ts}\!\left(\partial_m g_{sn}+\partial_n g_{sm}-\partial_s g_{mn}\right)\)
- [standard reconstruction] \((\nabla_s\nabla_r-\nabla_r\nabla_s)V_n = R^{t}{}_{nrs}V_t\)
- [standard reconstruction] \(R^{t}{}_{nrs}=\partial_r\Gamma^{t}{}_{sn}-\partial_s\Gamma^{t}{}_{rn}+\Gamma^{p}{}_{sn}\Gamma^{t}{}_{rp}-\Gamma^{p}{}_{rn}\Gamma^{t}{}_{sp}\)
- [transcript-backed] \(R^{t}{}_{nrs}=0\ \text{everywhere} \Longrightarrow \text{flat space}\)

## Definitions And Objects
- `Metric tensor` \(g_{mn}\): rank-\((0,2)\) tensor that defines squared line element \(ds^2\).
- `Inverse metric` \(g^{mn}\): matrix inverse of \(g_{mn}\), used to raise indices.
- `Flat metric` in lecture usage: not the statement \(g_{mn}=\delta_{mn}\) in arbitrary coordinates, but existence of coordinates in which this holds.
- `Gaussian normal coordinates`: local coordinates at a chosen point where the metric is Euclidean-looking up to first order, \(g_{mn}=\delta_{mn}\) and \(\partial_r g_{mn}=0\) at that point.
- `Local flatness`: every smooth metric can be made flat-looking at a point and through first derivatives, but not generically through second derivatives.
- `Covariant derivative` \(\nabla_r\): tensorial derivative defined operationally by differentiating first in Gaussian normal coordinates and transforming back.
- `Connection / Christoffel symbols` \(\Gamma^{t}{}_{rm}\): coordinate-variation coefficients that appear in covariant derivatives; they are not tensors.
- `Metric compatibility`: special property of the Levi-Civita connection, \(\nabla g=0\).
- `Riemann curvature tensor` \(R^{t}{}_{nrs}\): coefficient measuring failure of covariant derivatives to commute on a vector.
- `Conical deficit`: missing wedge angle in the flattened cone picture; geometric proxy for localized curvature.
- `Parallel transport` in the lecture’s operational language: move a vector while keeping its covariant derivative zero along the path.
- `Tidal forces`: physical manifestation of curvature; used as the gravity-side interpretation of the Riemann tensor.

## Derivation Steps
Gaussian normal counting argument

1. Choose the point of interest as a common origin for two coordinate systems, so \(x=0\) and \(y=0\) at the same point.
2. Expand the new coordinates in powers of the old ones: \(x^m = y^m + C^m{}_{nr}y^n y^r + \cdots\).
3. In four dimensions, there are 10 independent quadratic monomials \(y^n y^r\).
4. With the extra index \(m\), this gives 40 adjustable quadratic coefficients \(C^m{}_{nr}\).
5. The symmetric metric has 10 components, so the conditions \(\partial_r g_{mn}(0)=0\) supply 40 first-derivative equations.
6. Therefore one can solve to quadratic order and arrange \(g_{mn}(0)=\delta_{mn}\) together with \(\partial_r g_{mn}(0)=0\).
7. The next order cannot generically be eliminated, so the second derivatives of \(g\) are where curvature begins to show up.

Why ordinary derivatives fail

1. Compare the same geometric vector using locally straight coordinates and superposed curvilinear coordinates.
2. Even if the vector itself is unchanged, its components change because the coordinate axes change from point to point.
3. Therefore \(\partial_r V_m\) can vanish in one coordinate system and fail to vanish in another.
4. An object with that behavior cannot be tensor components.
5. So ordinary coordinate derivatives of tensor components are not themselves tensorial.

Covariant derivative construction

1. To define a derivative at a point, choose Gaussian normal coordinates near that point.
2. In those coordinates, compare neighboring vectors by shifting one to the other base point while keeping its Gaussian-normal components fixed.
3. Use the ordinary derivative in those coordinates as the definition of the derivative at the point.
4. Transform that result back to arbitrary coordinates as a tensor.
5. The transformed answer contains the ordinary derivative term plus an extra term coming from coordinate variation.
6. Write the extra term with Christoffel symbols to obtain the covariant derivative formula.

Higher-rank tensor rule

1. Start from the vector formula for the covariant derivative.
2. For a tensor with several lower indices, expose one index at a time and treat the rest as spectators.
3. Add one Christoffel term for each lower index.
4. Each term acts on the slot corresponding to that index.
5. This gives the general lower-index pattern illustrated by \(\nabla_s T_{mn}\).

Christoffel symbols from metric compatibility

1. Write \(0=\nabla_s g_{mn}=\partial_s g_{mn}-\Gamma^{t}{}_{sm}g_{tn}-\Gamma^{t}{}_{sn}g_{mt}\).
2. Write the two index-permuted equations with \((s,m,n)\) rearranged.
3. Use the symmetry \(\Gamma^{t}{}_{sm}=\Gamma^{t}{}_{ms}\).
4. Add the equations with \(\partial_m g_{sn}\) and \(\partial_n g_{sm}\), then subtract the one with \(\partial_s g_{mn}\).
5. The unwanted Christoffel terms cancel pairwise.
6. The surviving terms give \(2\,\Gamma^{t}{}_{mn}g_{ts}\) on one side.
7. Multiply by the inverse metric to isolate \(\Gamma^{t}{}_{mn}\).

Curvature from the commutator

1. Compute \(\nabla_s\nabla_r V_n\).
2. Compute \(\nabla_r\nabla_s V_n\).
3. Subtract the two results.
4. The remaining expression is linear in \(V_t\).
5. Define the coefficient of \(V_t\) to be \(R^{t}{}_{nrs}\).
6. If the commutator vanishes for every vector everywhere, the space is flat.
7. If it does not vanish, the space has curvature.

Cone-to-commutator bridge

1. Flatten the side of a cone by cutting out a wedge; the missing wedge is the conical deficit.
2. Parallel-transport a vector around the tip while keeping it “as parallel as possible.”
3. When it returns, the vector is rotated.
4. Rephrase the same effect algebraically as a difference between transporting in \(r\)-then-\(s\) order and \(s\)-then-\(r\) order.
5. This is the geometric content of the nonzero commutator of covariant derivatives.

## Notation Choices
- Use lower-case Latin indices \(m,n,r,s,t,p\) throughout, matching the lecture’s board and transcript.
- Use Einstein summation convention consistently.
- Use \(x^m\) for the Gaussian-normal or locally straight coordinates and \(y^m\) for the original/arbitrary coordinates in the local-flattening construction.
- Use \(\partial_r\) as the normalized notation for ordinary derivative with respect to \(x^r\), even though the transcript often says “\(d_r\)” or “\(d/dx^r\).”
- Use \(\nabla_r\) as the normalized notation for the covariant derivative; Susskind’s temporary capital-\(D\) notation can be absorbed into \(\nabla\).
- Keep the crucial vector formulas in covariant-component form \(V_m\), since the boxed board equation and the later commutator discussion are both closest to that form.
- Use \(R^{t}{}_{nrs}\) so that the commutator is written as \((\nabla_s\nabla_r-\nabla_r\nabla_s)V_n = R^{t}{}_{nrs}V_t\).
- Normalize the spelling to `Christoffel` in the notes, while recognizing that the board writes `Cristoffel`.
- State Gaussian-normal identities at a chosen point \(x=x_0\); if the origin is shifted to that point, write `at \(x=0\)`.
- Keep this lecture in Riemannian signature language: positive-definite metric, all squared lengths positive.

## Uncertain Mathematics
- The transcript around 00:10:46–00:11:07 is too garbled to trust for any precise formula; only the invariant point should be retained: flatness is not diagnosed by a special-looking component matrix in arbitrary coordinates.
- The higher-rank covariant-derivative discussion around 01:00 contains visible index slips and chalk corrections; preserve the pattern, not the raw intermediate index order.
- The three expanded \(\nabla g=0\) equations used in the Christoffel derivation are partially scrambled in speech and should not be copied line-for-line from the transcript.
- The final Riemann-tensor formula near 01:38–01:39 is only partially legible in the transcript; use the canonical Levi-Civita form, but keep the lecture’s emphasis on “two derivative terms plus two quadratic terms.”
- The board shows \(\partial V_m/\partial x^r=0\) with a lower index on \(V\), but the surrounding lecture logic applies more generally to vector components.
- The board’s third Gaussian-normal condition does not visibly repeat `at \(x=0\)` even though locality is clearly intended.
- The symmetry \(C^m{}_{nr}=C^m{}_{rn}\) is implicit in the quadratic monomial counting, but it is not explicitly written on the board.
- The lecture’s temporary `capital D` notation is informal; the final notes should standardize to \(\nabla\) without pretending the board itself used that symbol consistently.