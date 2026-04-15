# Math Bank
## Core Equations
- [transcript-backed] \(z' = z - L(t),\quad t' = t,\quad x' = x\)
- [transcript-backed] \(L(t)=vt,\quad z' = z-vt\)
- [visible] \(F = m\ddot z\)
- [transcript-backed] \(\ddot z' = \ddot z\)
- [transcript-backed] \(F = m\ddot z'\)
- [transcript-backed] \(L(t)=\tfrac12 gt^2,\quad \dot L = gt,\quad \ddot L = g\)
- [transcript-backed] \(z' = z - \tfrac12 gt^2\)
- [standard reconstruction] \(\ddot z' = \ddot z - g\)
- [standard reconstruction] \(F = m(\ddot z' + g)\)
- [standard reconstruction] \(m\ddot z' = F - mg\)
- [transcript-backed] \(x = ct,\quad z=0\)
- [standard reconstruction] \(z = z' + \tfrac12 gt^2\)
- [standard reconstruction] \(z' + \tfrac12 gt^2 = 0,\quad x=ct\)
- [transcript-backed] \(d\tau^2 = dt^2 - dx^2\)
- [transcript-backed] \(ds^2 = dx^2 - dt^2\)
- [transcript-backed] \(ds^2 = \sum_i (dx^i)^2\)
- [transcript-backed] \(ds^2 = \delta_{mn}\,dx^m dx^n\)
- [transcript-backed] \(ds^2 = R^2(d\theta^2 + \sin^2\theta\,d\phi^2)\)
- [transcript-backed] \(ds^2 = R^2(d\theta^2 + \cos^2\theta\,d\phi^2)\)
- [standard reconstruction] \(ds^2 = \sum_{m,n} g_{mn}(x)\,dx^m dx^n\)
- [transcript-backed] \(dy^m = \frac{\partial y^m}{\partial x^p}\,dx^p\)
- [transcript-backed] \(V'^m = \frac{\partial y^m}{\partial x^p}V^p\)
- [transcript-backed] \(W_m = \frac{\partial s}{\partial x^m}\)
- [transcript-backed] \(W'_m = \frac{\partial x^p}{\partial y^m}W_p\)
- [standard reconstruction] \(T^{mn} = V^mU^n\)
- [standard reconstruction] \(T'^{mn} = \frac{\partial y^m}{\partial x^p}\frac{\partial y^n}{\partial x^q}T^{pq}\)
- [transcript-backed] \(T'_{mn} = \frac{\partial x^p}{\partial y^m}\frac{\partial x^q}{\partial y^n}T_{pq}\)
- [transcript-backed] \(dx^m = \frac{\partial x^m}{\partial y^p}\,dy^p\)
- [transcript-backed] \(g_{mn} = \delta_{mn}\) in Cartesian coordinates of flat Euclidean space

## Definitions And Objects
- Equivalence principle: gravity and acceleration are locally indistinguishable for a sufficiently small system observed for a sufficiently short time.
- \(L(t)\): height of the elevator floor relative to the ground-based \(z\)-frame.
- Inertial frame: a frame related by uniform velocity to another inertial frame; Newton’s law keeps the same form there.
- Accelerated frame: a frame related by nonlinear time dependence in the coordinate transformation; fictitious gravitational terms appear in Newton’s law.
- Curvilinear coordinate transformation: a nonlinear coordinate change that does not, in general, send straight worldlines to straight worldlines.
- Tidal forces: differential stretching/squeezing effects on an extended freely falling body; these are the Newtonian diagnostic of real gravity in this lecture.
- \(d\tau^2\), \(ds^2\): invariant local interval in special relativity, with sign convention depending on author.
- Metric tensor \(g_{mn}(x)\): the position-dependent coefficient matrix in the local quadratic distance formula.
- Flat space: a space for which some coordinate transformation makes the metric equal to the Cartesian Kronecker delta everywhere.
- Curved space: a space for which no such global coordinate transformation exists.
- Intrinsic geometry: geometry determined by distances measured within the surface, independent of how the surface is embedded in a higher-dimensional space.
- Scalar \(s(x)\): a single coordinate-independent value attached to each point.
- Contravariant vector: an object whose components transform like coordinate differentials \(dx^m\).
- Covariant vector: an object whose components transform like a gradient \(\partial s/\partial x^m\).
- Rank-2 tensor: an object with two indices; in the lecture it is built first from products of vector components.

## Derivation Steps
Elevator, inertial case
1. Start from \(z' = z - L(t)\) with \(L(t)=vt\).
2. Differentiate twice with respect to time.
3. The second derivative of \(vt\) vanishes.
4. Conclude \(\ddot z' = \ddot z\).
5. Substitute into \(F=m\ddot z\).
6. Obtain the same form in the primed frame: \(F=m\ddot z'\).

Elevator, accelerated case
1. Replace \(L(t)\) by \(\tfrac12 gt^2\).
2. Write \(z' = z - \tfrac12 gt^2\).
3. Differentiate twice.
4. Use \(\frac{d^2}{dt^2}(\tfrac12 gt^2)=g\).
5. Conclude \(\ddot z' = \ddot z - g\).
6. Rewrite this as \(\ddot z = \ddot z' + g\).
7. Substitute into \(F=m\ddot z\).
8. Get \(F=m(\ddot z' + g)\).
9. Move the \(mg\) term to the force side to make the result look Newtonian: \(m\ddot z' = F-mg\).

Mass-cancellation point
1. In the accelerated frame the extra force term is proportional to \(m\).
2. A genuine gravitational force also has that mass-proportional form.
3. Insert such a force into \(F=m a\).
4. The mass cancels from the equation of motion.
5. Conclude that the trajectory does not depend on the mass of the falling object.

Light-bending argument
1. In the unprimed frame take the light ray to satisfy \(x=ct\) and \(z=0\).
2. Use the accelerated-frame relation \(z = z' + \tfrac12 gt^2\).
3. Substitute \(z=0\).
4. Obtain \(z' + \tfrac12 gt^2 = 0\).
5. Keep \(x=ct\) unchanged in this simple setup.
6. Conclude that the light ray is curved in the accelerated frame.
7. Read this, via the equivalence principle, as evidence that gravity bends light.

Euclidean distance to general metric
1. In Cartesian Euclidean coordinates write \(ds^2 = \sum_i (dx^i)^2\).
2. Re-express this as \(ds^2 = \delta_{mn}\,dx^m dx^n\).
3. Move to arbitrary coordinates on a curved or even flat surface.
4. Keep only the local distance between neighboring points.
5. Demand that the local distance remain quadratic in the coordinate differentials.
6. Introduce coefficient functions \(g_{mn}(x)\).
7. Obtain \(ds^2 = g_{mn}(x)\,dx^m dx^n\).

Sphere example
1. Parameterize neighboring points on the sphere by \((\theta,\phi)\).
2. Notice that the \(d\phi\) contribution depends on latitude.
3. Multiply the \(d\phi^2\) term by the appropriate trigonometric factor.
4. If \(\theta\) is measured from the pole, use \(\sin^2\theta\).
5. If \(\theta\) is measured from the equator, use \(\cos^2\theta\).
6. Conclude that the metric coefficients depend on position and on coordinate convention.

Flatness criterion
1. Start with a given metric \(g_{mn}(x)\) in one coordinate system.
2. Ask whether there exists another coordinate system in which the metric becomes \(\delta_{mn}\).
3. If such coordinates exist everywhere, call the space flat.
4. If no such global coordinates exist, call the space curved.
5. This is the geometric analogue of asking whether a gravitational field can be transformed away.

Contravariant transformation law
1. Take two coordinate systems \(x^m\) and \(y^m\).
2. Express the new differentials by the chain rule: \(dy^m = \frac{\partial y^m}{\partial x^p}dx^p\).
3. Interpret \(dx^p\) and \(dy^m\) as components of the same infinitesimal vector in different coordinates.
4. Abstract the pattern to any contravariant vector \(V^m\).
5. Define \(V'^m = \frac{\partial y^m}{\partial x^p}V^p\).

Covariant transformation law
1. Start with a scalar field \(s(x)\).
2. Define its gradient components \(W_m=\partial s/\partial x^m\).
3. Compute \(\partial s/\partial y^m\) by the chain rule.
4. Obtain \(W'_m = \frac{\partial x^p}{\partial y^m}W_p\).
5. Use this as the defining transformation law for a covariant vector.

Rank-2 tensor from vector products
1. Form the product of two contravariant vectors: \(T^{mn}=V^mU^n\).
2. Transform each factor separately with \(\partial y/\partial x\).
3. Multiply the two transformed factors together.
4. Collect the unprimed components into \(T^{pq}\).
5. Read off the two-index transformation law.
6. Repeat the same pattern for lower-index objects using \(\partial x/\partial y\).

Metric-transformation setup
1. Begin with \(ds^2 = g_{mn}(x)\,dx^m dx^n\).
2. Re-express \(dx^m\) in terms of \(dy^p\): \(dx^m = \frac{\partial x^m}{\partial y^p}dy^p\).
3. Substitute both differential factors into the interval.
4. Compare the result with the same quadratic form written in \(y\)-coordinates.
5. The lecture stops here and defers the full transformation law to the next lecture.

## Notation Choices
- Use \(L(t)\), not the ambiguous spoken lowercase \(l(t)\), for the elevator-floor height.
- Use \(z,z'\) for the Newtonian elevator discussion; use \(x\) for the horizontal light-ray direction; keep \(t'=t\) in the nonrelativistic opening setup.
- Use dot notation \(\dot{}\), \(\ddot{}\) only in the Newtonian time-evolution part.
- Use \(x^m\) and \(y^m\) for the general tensor-analysis coordinate change, following Susskind’s deliberate switch away from \(x'^m\).
- Use upstairs indices for contravariant objects: \(dx^m\), \(V^m\), \(T^{mn}\).
- Use downstairs indices for covariant objects: \(W_m\), \(T_{mn}\), \(g_{mn}\).
- Use \(m,n,p,q,\ell,r\) as abstract coordinate indices; use \(i\) for the simple Euclidean Cartesian sum.
- Use \(\partial/\partial x^m\) and \(\partial/\partial y^m\) for coordinate derivatives in the tensor section.
- Use Einstein summation once the pattern is established; an explicit \(\sum\) is acceptable the first time a formula is introduced.
- Use \(\delta_{mn}\) for the flat Cartesian metric.
- For the sphere metric, state the \(\theta\)-convention explicitly every time the formula is used.
- In the metric frames, interpret the visible horizontal axis label as \(x^1\), paired with \(x^2\), not as \(x'\).

## Uncertain Mathematics
- The accelerated-frame sign discussion is messy in the transcript. The clean result should be stated cautiously as a corrected reconstruction: \(\ddot z'=\ddot z-g\), hence \(m\ddot z'=F-mg\).
- The transcript garbles the light-ray substitution as something like \(z=z'+tg^2\). The intended result is almost certainly \(z=z'+\tfrac12 gt^2\).
- The metric line element on the board is only partially legible; the clean formula \(ds^2=g_{mn}(x)\,dx^m dx^n\) should be treated as a cautious reconstruction supported by both transcript and frame.
- The cropped right-edge board formula \(ds^2=R^2(\cdots)\) should not be used to fix the sphere metric; the transcript, not the frame crop, is the reliable source.
- The sphere formula depends on angle convention: \(\sin^2\theta\) from the pole, \(\cos^2\theta\) from the equator.
- In the spoken tensor discussion, index placement is sometimes lost in the transcript. The final notes should normalize this by writing contravariant products with upper indices and covariant ones with lower indices.
- One spoken line appears to mislabel the two-up tensor transformation as “covariant”; the transformation pattern itself matters more than that spoken label.
- The lecture’s statement that “the square of a small thing is zero” should not be copied literally. In the notes it should be rewritten as a local infinitesimal approximation statement, with higher-order terms neglected.
- The lecture only sets up the metric transformation argument; it does not complete the derivation of the full transformation law or derive curvature tensor formulas in this lecture.