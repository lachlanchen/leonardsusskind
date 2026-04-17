# Math Bank
## Core Equations
- \(d\tau^2 = g_{\mu\nu}\,dx^\mu dx^\nu\) [visible]
- \(\eta_{\mu\nu}=\begin{pmatrix}1&0&0&0\\0&-1&0&0\\0&0&-1&0\\0&0&0&-1\end{pmatrix}\) [visible]
- \(d\tau^2 = dt^2 - dx^2 - dy^2 - dz^2\) in units \(c=1\) [transcript-backed]
- \(d\tau^2 = dt^2 - \dfrac{dx^2+dy^2+dz^2}{c^2}\) [standard reconstruction]
- \(d\tau \approx dt\) for slow motion \(|\mathbf v| \ll c\) [transcript-backed]
- \(\partial_s g_{mn}=0\) as the local flatness condition at a chosen point [transcript-backed]
- \(y^m = x^m + c^m{}_{rs}\,x^r x^s\) [visible]
- \(c^m{}_{rs}=c^m{}_{sr}\) [transcript-backed]
- \(\#(c^m{}_{rs}\text{ for fixed }m)=\dfrac{D(D+1)}{2}\) [visible]
- \(\#(c^m{}_{rs}\text{ total})=D\,\dfrac{D(D+1)}{2}=\dfrac{D^2(D+1)}{2}\) [standard reconstruction]
- \(\dfrac{\partial g_{mn}(y)}{\partial y^s}=0\) at the chosen point [visible]
- \(\dfrac{\partial g_{mn}(x)}{\partial x^r}=0\) at the chosen point [visible]
- \(\Gamma^r{}_{mn}=\dfrac12\,g^{rs}\!\left(\dfrac{\partial g_{sm}}{\partial x^n}+\dfrac{\partial g_{sn}}{\partial x^m}-\dfrac{\partial g_{mn}}{\partial x^s}\right)\) [visible]
- \(\Gamma^r{}_{mn}=0\) at a point if \(\partial g=0\) there [transcript-backed]
- \(\nabla_r g_{mn}=\partial_r g_{mn}-\Gamma^s{}_{rm}g_{sn}-\Gamma^s{}_{rn}g_{ms}\) [standard reconstruction]
- \(\nabla_r g_{mn}=0\) [standard reconstruction]
- \(t^p=\dfrac{dx^p}{ds}\) for the tangent vector to a curve [transcript-backed]
- \(\dfrac{D v^m}{Ds}=\dfrac{dv^m}{ds}+\Gamma^m{}_{np}v^n\dfrac{dx^p}{ds}\) [standard reconstruction]
- \(\dfrac{D v^m}{Ds}=0\) as the parallel-transport condition [standard reconstruction]
- \(dv^m=-\Gamma^m{}_{np}v^n\,dx^p\) [standard reconstruction]
- \(\dfrac{D}{Ds}\!\left(\dfrac{dx^m}{ds}\right)=0\) for a geodesic [transcript-backed]
- \(\dfrac{d^2 x^m}{ds^2}+\Gamma^m{}_{np}\dfrac{dx^n}{ds}\dfrac{dx^p}{ds}=0\) [standard reconstruction]
- \(\Delta\theta=\theta\) for parallel transport around the tip of a cone with angular deficit \(\theta\) [transcript-backed]
- \(\delta\theta \propto \delta A\) for sufficiently small loops on a smooth surface [transcript-backed]
- \(\delta\theta = R\,\delta A\) in the lecture’s two-dimensional small-loop curvature law [transcript-backed]
- \(\operatorname{sign}(\delta\theta)=\operatorname{sign}(\delta A)\) for positive curvature, and opposite sign for negative curvature [transcript-backed]

## Definitions And Objects
- Proper time \(d\tau\): the time recorded by a clock moving with the object along its worldline.
- Coordinate time \(dt\): the time coordinate in a chosen frame; not in general the clock reading along the trajectory.
- Metric tensor \(g_{\mu\nu}\) or \(g_{mn}\): the object that defines the interval; constant in special relativity, position-dependent in general geometry.
- Minkowski metric \(\eta_{\mu\nu}\): the flat space-time metric with one plus sign and three minus signs in this lecture.
- Flat space / flat space-time: a geometry for which one can choose coordinates making the metric constant; equivalently, derivatives of the metric can be made zero everywhere.
- Local inertial / locally flat coordinates: coordinates chosen at a single point so that first derivatives of the metric vanish there.
- Christoffel symbols \(\Gamma^r{}_{mn}\): connection coefficients built from first derivatives of the metric; not tensors.
- Covariant derivative along a curve: the corrected derivative that removes spurious coordinate variation and produces a tensorial notion of change along the curve.
- Tangent vector \(dx^p/ds\): the vector tangent to the curve and used inside the covariant derivative along the curve.
- Geodesic: a curve whose tangent vector is parallel transported along itself.
- Parallel transport: motion of a vector along a curve with vanishing covariant derivative along that curve.
- Curvature: operationally, failure of a vector to return to itself after parallel transport around a closed curve.
- Angular deficit \(\theta\): the wedge removed in constructing a cone; equal to the rotation acquired by a transported vector around the tip.
- Singular point: a point where no coordinate system makes the metric smooth; the cone tip is the lecture’s model example.
- Tangent space: the local linear space in which transported vectors are understood to live.
- Oriented area \(\delta A\): a small area together with a chosen orientation of its boundary, used to define the sign of curvature.
- Positive curvature: loop orientation and vector rotation have the same sign.
- Negative curvature: loop orientation and vector rotation have opposite signs.

## Derivation Steps
Local flattening at a point:
1. Start with coordinates \(x\) in which the metric has nonzero first derivatives at the chosen point.
2. Introduce new coordinates \(y^m=x^m+c^m{}_{rs}x^r x^s+\cdots\) with the same origin.
3. Treat \(c^m{}_{rs}\) as adjustable constants at that point.
4. Use symmetry \(c^m{}_{rs}=c^m{}_{sr}\) to count the available coefficients.
5. Compare that count with the number of conditions in \(\partial_s g_{mn}(y)=0\), which has three indices with \(m,n\) symmetric.
6. Conclude that there is just enough coordinate freedom to kill all first derivatives of the metric at one point.
7. Conclude separately that there is not enough freedom to kill all higher derivatives in general.

Vanishing first derivatives implies vanishing Christoffel symbols at a point:
1. Write \(\Gamma^r{}_{mn}\) in terms of first derivatives of the metric.
2. Choose coordinates at the point so that all first derivatives \(\partial g\) vanish there.
3. Substitute those vanishing derivatives into the Christoffel formula.
4. Conclude \(\Gamma^r{}_{mn}=0\) at that point.

Metric compatibility in the lecture’s logic:
1. Recall that \(\nabla_r g_{mn}\) is built from \(\partial_r g_{mn}\) plus one Christoffel term for each lower index.
2. In the locally flattened coordinates at a chosen point, both \(\partial g\) and \(\Gamma\) vanish there.
3. Therefore \(\nabla g=0\) at that point in that coordinate system.
4. Since \(\nabla g\) is a tensor, if it vanishes in one coordinate system at that point, it vanishes in all coordinate systems at that point.
5. Since the point was arbitrary, conclude \(\nabla g=0\) everywhere.
6. Keep the lecture’s caveat: this is presented as a consistency argument for the standard Levi-Civita construction, not as a fully clean noncircular derivation.

Geodesic equation from the general curve derivative:
1. Start from the covariant derivative of a contravariant vector along a curve.
2. Specialize the vector to the tangent vector \(v^m=dx^m/ds\).
3. Set the covariant derivative of that tangent vector equal to zero.
4. Recognize that \(d(dx^m/ds)/ds=d^2x^m/ds^2\).
5. Obtain the coordinate geodesic equation.

Incremental transport law:
1. Start from the parallel-transport condition \(D v^m/Ds=0\).
2. Expand the covariant derivative along the curve.
3. Move the Christoffel term to the other side.
4. Multiply by \(ds\).
5. Obtain \(dv^m=-\Gamma^m{}_{np}v^n dx^p\).
6. Interpret this as an update rule from one infinitesimal step on the curve to the next.

Curvature from path dependence:
1. Define parallel transport along a chosen curve by \(D v/Ds=0\).
2. Ask whether transport from one point to another is independent of the chosen curve.
3. Recast the question as transport around a closed loop.
4. In flat space, the vector returns unchanged.
5. In curved space, there exist loops for which the vector returns rotated.
6. Use that failure as the operational diagnosis of curvature inside the loop.

Cone example:
1. Construct a cone by removing a wedge from a flat sheet and identifying the cut edges.
2. Transport a vector around a closed loop that avoids the tip; on the flat opened sheet it comes back unchanged.
3. Transport a vector around a loop enclosing the tip; on the opened sheet the identified edges force a mismatch in final direction.
4. Measure the mismatch by the angular deficit \(\theta\).
5. Conclude that curvature is localized at the cone tip.

Small-loop curvature law on a smooth surface:
1. Replace the exact neighborhood of a small loop on a sphere by the tangent cone along that loop.
2. Use the cone intuition to see that the transport defect is small for small loops.
3. Note that the defect scales with the enclosed area, not with the perimeter alone.
4. Define the proportionality coefficient by \(\delta\theta=R\,\delta A\) in the two-dimensional local setting.

Sign of curvature:
1. Assign a sign to a small area by the orientation of its boundary.
2. Compare the direction of transport around the boundary with the direction of the resulting vector rotation.
3. Same sign gives positive curvature.
4. Opposite sign gives negative curvature.

## Notation Choices
- Use Greek indices \(\mu,\nu\) for space-time quantities in the opening recap.
- Use Latin indices \(m,n,r,s,p\) for ordinary-space geometry, curves, Christoffel symbols, and parallel transport once the lecture shifts back to spatial discussion.
- Use \(x^0=t\) and \(x^1,x^2,x^3\) for the space-time coordinate components when the interval is written in component form.
- Use \(d\tau^2\) for the space-time interval; reserve \(s\) for the parameter along a spatial curve.
- Use signature \((+---)\) throughout this lecture.
- Use \(g_{\mu\nu}\) or \(g_{mn}\) according to context; use \(\eta_{\mu\nu}\) only for the flat Minkowski metric.
- Use \(\Gamma^r{}_{mn}\) as the cleaned Christoffel notation.
- Use \(v^m\) for a contravariant vector being transported.
- Use \(dx^p/ds\) for the tangent vector; if a separate symbol is wanted, define \(t^p:=dx^p/ds\).
- Use \(\partial_r g_{mn}\) and \(\partial g_{mn}/\partial x^r\) interchangeably only when helpful; keep one form locally consistent inside a derivation.
- Use \(D\) for the dimension count in the coordinate-freedom argument if staying close to the board frame; if the chapter normalizes to lowercase \(d\), note the change once.
- Normalize “parallelly transported” to “parallel transported” in prose.
- Use \(\delta\theta\) and \(\delta A\) for the small-loop law.
- Use \(R\) only for the two-dimensional local curvature coefficient in this lecture; do not silently upgrade it to the later four-dimensional curvature tensors or Ricci scalar machinery.

## Uncertain Mathematics
- The lower interval formula in the opening frame is partly occluded; the cleaned \(c^2\)-denominator form is safe, but the exact board handwriting is not fully recoverable.
- The total count of \(c^m{}_{rs}\) coefficients is garbled in the transcript at one point; the mathematically consistent total is \(\dfrac{D^2(D+1)}{2}\).
- The exact index placement in the covariant derivative along a curve is reconstructed from standard Levi-Civita geometry; the lecture’s spoken notation is broken and inconsistent in that stretch.
- The full formula for \(\nabla_r g_{mn}\) is not written on the board; only the schematic “ordinary derivative plus one Christoffel term for each index” is explicit in the transcript.
- The claim \(\nabla g=0\) is handled by Susskind as a standard-consistency argument and is explicitly challenged as circular by a student; the final notes should preserve that caution.
- The lecture’s statement that the cone tip has “infinite curvature” is an intuitive singular-limit statement; if the final chapter wants stricter language, it should say that curvature is concentrated singularly at the tip.
- The relation \(\delta\theta=R\,\delta A\) is presented only for small loops on two-dimensional surfaces; it should not be used as if it were the general spacetime curvature law.
- The sign convention for curvature is given only in the two-dimensional oriented-area setting of the lecture; it should not be generalized without additional setup.
- The torsion remark in the geodesic-angle discussion is loose and undeveloped; it should not become a formal subsection.
- The Möbius-strip remarks are topological and intuitive, not part of the clean mathematical spine.
- The torus discussion mixes intrinsic flatness, embedding intuition, and integrated-curvature talk; it should be treated as side commentary rather than as a formal derivation.
- The post-lecture ambient-space question clarifies that parallel transport is not defined by keeping vectors parallel in the embedding space, but the lecture does not turn that into a formal theorem.