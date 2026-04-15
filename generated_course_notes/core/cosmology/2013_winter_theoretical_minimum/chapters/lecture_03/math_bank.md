# Math Bank
## Core Equations
- [transcript-backed] \(ds^2 = dx^2 + dy^2\)
- [visible] \(ds^2 = dx^2 + dy^2 + dz^2\)
- [transcript-backed] \(ds^2 = dr^2 + r^2 d\theta^2\)
- [visible] \(ds^2 = dr^2 + r^2 d\Omega^2\)
- [standard reconstruction] \(d\Omega_1^2 = d\theta^2\)
- [standard reconstruction] \(ds^2 = dr^2 + r^2 d\Omega_1^2\)
- [standard reconstruction] \(d\Omega_2^2 = dr^2 + \sin^2 r\, d\Omega_1^2\)
- [standard reconstruction] \(d\Omega_2^2 = dr^2 + \sin^2 r\, d\theta^2\)
- [transcript-backed] \(d\Omega_3^2 = dr^2 + \sin^2 r\, d\Omega_2^2\)
- [transcript-backed] \(ds^2 = dr^2 + r^2 d\Omega_2^2\) for flat \(3\)-space in polar form
- [transcript-backed] \(dh_2^2 = dr^2 + \sinh^2 r\, d\Omega_1^2\)
- [transcript-backed] \(dh_3^2 = dr^2 + \sinh^2 r\, d\Omega_2^2\)
- [transcript-backed] \(x^2 + y^2 = 1\)
- [transcript-backed] \(x^2 + y^2 + z^2 = 1\)
- [transcript-backed] \(T^2 - x^2 - y^2 = 1\)
- [standard reconstruction] \(d\ell_{\text{emb}}^2 = dT^2 - dx^2 - dy^2\) for the hyperboloid embedding argument
- [transcript-backed] \(\sin r = \dfrac{e^{ir} - e^{-ir}}{2i}\)
- [transcript-backed] \(\sinh r = \dfrac{e^r - e^{-r}}{2}\)
- [transcript-backed] \(d^2 = r^2 d\theta^2\)
- [transcript-backed] \(d\theta = \dfrac{d}{r}\)
- [transcript-backed] \(d^2 = \sin^2 r\, d\theta^2\)
- [transcript-backed] \(d\theta = \dfrac{d}{\sin r}\)
- [transcript-backed] \(d^2 = \sinh^2 r\, d\theta^2\)
- [transcript-backed] \(d\theta = \dfrac{d}{\sinh r}\)
- [transcript-backed] \(d\theta \sim \dfrac{2d}{e^r}\) for large \(r\)
- [standard reconstruction] \(ds^2_{\text{sphere},\,a} = a^2 d\Omega_n^2\)
- [standard reconstruction] \(ds^2_{\text{hyperbolic},\,a} = a^2 dh_n^2\)
- [standard reconstruction] \(ds^2_{\text{sphere},\,a} = a^2\left(dr^2 + \sin^2 r\, d\Omega_{n-1}^2\right)\)
- [standard reconstruction] \(ds^2_{\text{hyperbolic},\,a} = a^2\left(dr^2 + \sinh^2 r\, d\Omega_{n-1}^2\right)\)
- [transcript-backed] \(ds^2 = -dt^2 + dx^2 + dy^2 + dz^2\)
- [transcript-backed] \(ds^2 = 0\) for a light ray
- [standard reconstruction] \(-dt^2 + dx^2 = 0 \Rightarrow dx = \pm dt\)
- [transcript-backed] \(D = a\,\theta\)
- [transcript-backed] \(V = \dot a\,\theta\)
- [transcript-backed] \(V = \dfrac{\dot a}{a} D\)
- [transcript-backed] \(H = \dfrac{\dot a}{a}\)
- [standard reconstruction] \(ds^2 = -dt^2 + a(t)^2\left(dx^2 + dy^2 + dz^2\right)\)
- [transcript-backed] \(ds^2 = -dt^2 + a(t)^2 d\Omega_3^2\)
- [transcript-backed] \(ds^2 = -dt^2 + a(t)^2 dh_3^2\)
- [standard reconstruction] \(ds^2 = -dt^2 + a(t)^2 d\Omega_2^2\) for the \(2+1\)-dimensional visualization

## Definitions And Objects
- Metric: the squared distance between neighboring points; once given, the geometry is fixed.
- Homogeneous space: every point is geometrically the same as every other point.
- Isotropic space: around a given point, all directions are equivalent.
- \(1\)-sphere / circle / \(\Omega_1\): a one-dimensional closed space with unit metric \(d\Omega_1^2 = d\theta^2\).
- Unit circle: intrinsic circumference \(2\pi\); not tied to appearing round in an ambient Euclidean drawing.
- \(2\)-sphere / \(\Omega_2\): the surface of an ordinary sphere, treated intrinsically as a two-dimensional homogeneous space.
- \(3\)-sphere / \(\Omega_3\): a three-dimensional homogeneous positively curved space; not to be described as the boundary of ordinary 3D space.
- Hyperbolic space / \(H_n\): uniformly negatively curved homogeneous space.
- Hyperboloid model: embedding description of \(H_2\) via \(T^2 - x^2 - y^2 = 1\) with Lorentz-signature ambient metric.
- Stereographic projection: projection from sphere or hyperboloid to a plane/disk for visualization; distorts size but not the intrinsic geometry.
- Radius of curvature \(a\): fixed curvature scale multiplying the unit metric by \(a^2\).
- Scale factor \(a(t)\): time-dependent version of the size of space in the cosmology section.
- Null ray: spacetime curve with \(ds^2 = 0\).
- Torus: flat space with periodic identifications; in \(2\)D represented by a rectangle with opposite sides identified.
- Ball vs sphere: “sphere” means boundary surface; “ball” means filled interior.

## Derivation Steps
1. Flat \(3\)-space metric
   1. Start from the flat plane: \(ds^2 = dx^2 + dy^2\).
   2. Add a third orthogonal Cartesian direction.
   3. Obtain \(ds^2 = dx^2 + dy^2 + dz^2\).

2. Flat polar metric in \(2\)D
   1. Choose coordinates \((r,\theta)\).
   2. Radial displacement contributes \(dr^2\).
   3. At fixed \(r\), angular arc length is \(r\,d\theta\).
   4. Square the angular piece and add orthogonal contributions.
   5. Get \(ds^2 = dr^2 + r^2 d\theta^2 = dr^2 + r^2 d\Omega_1^2\).

3. Unit-circle metric
   1. Restrict to a circle of unit radius.
   2. The only coordinate is the angular coordinate \(\theta\).
   3. Neighboring points differ by arc length \(d\theta\).
   4. Therefore the circle’s intrinsic metric is \(d\theta^2\).
   5. Rename this \(d\Omega_1^2\) because it will recur.

4. Positive-curvature \(2\)-sphere metric
   1. Use \(r\) as angular distance from the observer’s point.
   2. The surrounding circles have radius \(\sin r\), not \(r\).
   3. Check endpoints: \(\sin 0 = 0\), \(\sin \pi = 0\), maximum at \(r=\pi/2\).
   4. Keep the same radial part \(dr^2\).
   5. Replace \(r^2\) by \(\sin^2 r\) in the angular term.
   6. Get \(d\Omega_2^2 = dr^2 + \sin^2 r\, d\Omega_1^2\).

5. Positive-curvature \(3\)-sphere metric
   1. Repeat the same nested-shell logic one dimension up.
   2. The shells around the observer are now \(2\)-spheres.
   3. Their size is still controlled by \(\sin r\).
   4. Replace the circle metric by the \(2\)-sphere metric.
   5. Get \(d\Omega_3^2 = dr^2 + \sin^2 r\, d\Omega_2^2\).

6. Flat-space angular-size law
   1. Consider a galaxy of true size \(d\) at fixed radius \(r\).
   2. Along the transverse direction, \(dr=0\).
   3. The metric reduces to \(d^2 = r^2 d\theta^2\).
   4. Solve for the observed angle: \(d\theta = d/r\).

7. Spherical angular-size law
   1. Keep the same transverse setup at fixed \(r\).
   2. Use the spherical metric instead of the flat one.
   3. The transverse piece is \(d^2 = \sin^2 r\, d\theta^2\).
   4. Solve: \(d\theta = d/\sin r\).
   5. Because \(\sin r < r\) for \(0<r<\pi\), the observed angle is larger than in flat space at the same distance.
   6. Past \(r=\pi/2\), \(\sin r\) decreases, so apparent size turns around and increases.

8. Hyperbolic angular-size law
   1. Keep the same transverse setup at fixed \(r\).
   2. Use \(dh_2^2 = dr^2 + \sinh^2 r\, d\theta^2\).
   3. Set \(dr=0\) along the object’s size.
   4. Obtain \(d^2 = \sinh^2 r\, d\theta^2\).
   5. Solve: \(d\theta = d/\sinh r\).
   6. For large \(r\), use \(\sinh r \approx e^r/2\).
   7. Conclude \(d\theta \approx 2d\,e^{-r}\): distant objects shrink exponentially fast.

9. Radius-of-curvature rescaling
   1. Start from a unit metric.
   2. Rescale all lengths by a factor \(a\).
   3. Squared lengths scale by \(a^2\).
   4. Therefore multiply the entire unit metric by \(a^2\).

10. Hubble-law derivation from expanding geometry
   1. Take two points at fixed angular separation \(\theta\).
   2. Their actual distance is \(D = a(t)\theta\).
   3. Differentiate with respect to time at fixed \(\theta\).
   4. Get \(V = \dot a\,\theta\).
   5. Substitute \(\theta = D/a\).
   6. Obtain \(V = (\dot a/a)D\).
   7. Identify \(H = \dot a/a\).

11. FRW-style metric assembly
   1. Start from Minkowski space: time part plus flat spatial part.
   2. Keep the time term \(-dt^2\).
   3. Replace the flat spatial metric by one of the homogeneous spatial metrics.
   4. Allow the overall spatial scale to depend on time through \(a(t)^2\).
   5. Produce flat, spherical, and hyperbolic cosmological metrics.

## Notation Choices
- Use \(d\Omega_n^2\) for the metric of the unit \(n\)-sphere.
- Use \(dh_n^2\) for the metric of the unit \(n\)-dimensional hyperbolic space.
- In the flat polar section, write \(d\Omega_1^2 = d\theta^2\); note separately that the board screenshot shows only \(d\Omega^2\).
- Use \(r\) in three different local senses, but reset it explicitly in the prose:
  - flat-space radial distance in polar coordinates;
  - angular-distance coordinate on the unit sphere, with \(0 \le r \le \pi\);
  - radial coordinate on hyperbolic space, with \(0 \le r < \infty\).
- Use \(\theta\) for angular separation around a circle and for fixed comoving angular separation in the Hubble-law discussion.
- Use lowercase \(a\) for fixed radius of curvature in the static-geometry discussion.
- Use \(a(t)\) for the time-dependent scale factor in the spacetime section.
- Use capital \(T\) for the hyperboloid embedding coordinate to avoid confusion with physical cosmological time \(t\).
- Use “unit circle” and “unit sphere” intrinsically, not as statements about a Euclidean drawing.
- Use “sphere” for the bounding surface and “ball” for the filled interior when discussing the Poincaré picture and terminology.
- Keep “null ray” as the lecture’s term for a light ray with \(ds^2=0\).

## Uncertain Mathematics
- The board frames `lecture_03_figure_03.png` and `lecture_03_figure_05.png` show \(d\Omega^2\) without a legible subscript; the cleaned \(d\Omega_1^2\) is transcript-supported, not directly visible.
- The lower spherical line in `lecture_03_figure_05.png` is incomplete; write \(ds^2 = dr^2 + \sin^2 r\, d\Omega_1^2\) only as a cautious reconstruction.
- The transcript around `00:15:41–00:15:48` appears garbled: the intended geometric facts are \(r=\pi/2\) at the equator and \(\sin(\pi/2)=1\), not “\(\sin(\pi/2)=\pi/2\)”.
- The transcript around `00:49:12–00:49:27` is messy; restore the \(3\)-dimensional hyperbolic metric as \(dh_3^2 = dr^2 + \sinh^2 r\, d\Omega_2^2\).
- The hyperboloid ambient metric is spoken with sign slips; use one consistent convention, preferably \(dT^2 - dx^2 - dy^2\), and note that this is only an embedding device.
- The static radius-\(a\) sphere discussion is truncated around `01:07:32–01:08:09`; derive the full formula by scaling the unit metric rather than quoting the broken transcript literally.
- The null-ray calculation in the transcript drops a sign in speech; restore it from \(-dt^2 + dx^2 = 0\), not from the garbled phrasing.
- The \(2+1\)-dimensional visualization line near `01:26:07–01:26:12` is missing the minus sign in the transcript; the intended spacetime metric is \(-dt^2 + d\Omega_2^2\), then \(-dt^2 + a(t)^2 d\Omega_2^2\).
- The torus question-and-answer region around `01:20:03–01:20:30` is badly garbled; preserve only the mathematically clear claim that a torus is equivalent to flat periodic space with repeated images.