# Math Bank
## Core Equations
- \(\phi_1,\phi_2\) solutions \(\Rightarrow c\,\phi_1\) and \(\phi_1+\phi_2\) are also solutions [transcript-backed]
- \(m\ddot{x}=-kx\) [transcript-backed]
- \(m\ddot{x}_1=-k x_1,\qquad m\ddot{x}_2=-k x_2\) [transcript-backed]
- \(m\ddot{(x_1+x_2)}=-k(x_1+x_2)\) [transcript-backed]
- \(p\,x_1^2+p\,x_2^2\neq p(x_1+x_2)^2\) [transcript-backed]
- \(ds^2=dt^2-dx^2-dy^2-dz^2\) [transcript-backed]
- \(ds^2=dx^\mu dx_\mu=\eta_{\mu\nu}\,dx^\mu dx^\nu\) [transcript-backed]
- \(\eta_{\mu\nu}=\mathrm{diag}(1,-1,-1,-1)\) [transcript-backed]
- \(m\frac{d^2x}{dt^2}\) and related stacked second-derivative terms [visible]
- \(ds^2=dx^2+\left(\frac{dy}{100}\right)^2=dx^2+10^{-4}dy^2\) [transcript-backed]
- \(ds^2=a\,dx^2+b\,dy^2+c\,dx\,dy\) [transcript-backed]
- \(a_{11}\,dx^2+a_{22}\,dy^2+a_{12}\,dx\,dy\) [visible]
- \(\begin{pmatrix}a_{11}&a_{12}\\ a_{21}&a_{22}\end{pmatrix}\) [visible]
- \(ds^2=a_{11}\,dx^2+a_{12}\,dx\,dy+a_{21}\,dy\,dx+a_{22}\,dy^2\) [standard reconstruction]
- \(ds^2=g_{\mu\nu}(x)\,dx^\mu dx^\nu\) [transcript-backed]
- \(ds^2=a_{ij}(x)\,dx^i dx^j\) [transcript-backed]
- \(ds^2=dr^2+r^2\,d\theta^2\) [transcript-backed]
- \(x=r\cos\theta,\qquad y=r\sin\theta\) [transcript-backed]
- \(ds^2=d\theta^2+\sin^2\theta\,d\phi^2\) [transcript-backed]
- \(ds^2=R^2\left(d\theta^2+\sin^2\theta\,d\phi^2\right)\) [transcript-backed]
- \(g_{\text{sphere}}=\begin{pmatrix}R^2&0\\0&R^2\sin^2\theta\end{pmatrix}\) [standard reconstruction]
- \(d\tau^2=dt^2-a^2(t)\left(dx^2+dy^2+dz^2\right)\) [transcript-backed]
- \(d=a(t)\,\Delta x\) [transcript-backed]
- \(v=\dot d=\dot a\,\Delta x=\frac{\dot a}{a}\,d\) [transcript-backed]
- \(H(t)=\frac{\dot a}{a}\) [transcript-backed]
- \(d\tau^2=0\) along a light ray [transcript-backed]
- \(dt=a(t)\,dx\) [transcript-backed]
- \(dx=\frac{dt}{a(t)}\) [transcript-backed]
- \(\frac{dx}{dt}=\frac{1}{a(t)}\) [transcript-backed]
- \(t_{\text{age}}\sim H^{-1}\) [transcript-backed]

## Definitions And Objects
- Linear theory: equations contain the fields only to first power; no quadratic field terms; no products like field \(\times\) derivative of field.
- Nonlinear term: any quadratic or higher dependence, e.g. \(x^2\), \(E^2\), \(B^2\).
- Metric: the matrix of coefficients in the quadratic differential form for the interval.
- Proper time / interval: invariant separation between neighboring spacetime points.
- Lorentz transformations: coordinate changes preserving the Minkowski interval.
- Awkward coordinates: nonorthogonal, nonuniform, or mixed-unit coordinates that alter the form of the metric without changing flatness.
- Curvature: the obstruction to finding coordinates in which metric coefficients are constant everywhere.
- Homogeneous space: same from point to point in space; not the same thing as flat; not a statement about time-independence.
- Spatial flatness: at fixed cosmic time, large-scale spatial relations are Euclidean.
- Comoving coordinates: labels attached to the expanding coordinate mesh; galaxy labels stay fixed while physical distances change.
- Scale factor \(a(t)\): spatially uniform, time-dependent conversion factor from coordinate separations to physical distances.
- Hubble parameter \(H(t)\): proportionality factor relating recession speed to distance.
- Null line: path with zero proper time; light ray trajectory.
- Radius of curvature: length scale on which spatial curvature becomes detectable.
- Shell-theorem setup: in a homogeneous spherical mass distribution, only the enclosed matter affects the radial motion of a test galaxy; exterior matter cancels.

## Derivation Steps
Cosmological metric form
1. Assume large-scale homogeneity in space.
2. Assume large-scale spatial flatness at each fixed time.
3. Choose Cartesian comoving coordinates \(x,y,z\).
4. The spatial part must be proportional to \(dx^2+dy^2+dz^2\).
5. Homogeneity forces the proportionality factor to depend only on \(t\), not on position.
6. Keep the special-relativistic sign choice for the time part.
7. Write \(d\tau^2=dt^2-a^2(t)(dx^2+dy^2+dz^2)\).

Linear superposition for the oscillator
1. Start from \(m\ddot x=-kx\).
2. Let \(x_1\) and \(x_2\) each satisfy the same equation.
3. Add the two equations.
4. Use linearity of differentiation: \(\ddot x_1+\ddot x_2=\ddot{(x_1+x_2)}\).
5. Obtain \(m\ddot{(x_1+x_2)}=-k(x_1+x_2)\).
6. Conclude that the sum of two solutions is also a solution.

Failure of superposition in the nonlinear case
1. Modify the equation by adding a quadratic term of \(p x^2\)-type.
2. Let \(x_1\) and \(x_2\) solve the modified equation.
3. Add the two equations.
4. The quadratic contribution becomes \(p x_1^2+p x_2^2\).
5. Note that \(p x_1^2+p x_2^2\neq p(x_1+x_2)^2\).
6. Conclude that \(x_1+x_2\) is not generally a solution.

Metric matrix from nonorthogonal coordinates
1. Start with a flat plane but use skew coordinate axes.
2. The interval is no longer just \(dx^2+dy^2\).
3. Write the most general quadratic form with \(dx^2\), \(dy^2\), and a mixed term.
4. Split the mixed term symmetrically into \(dx\,dy\) and \(dy\,dx\).
5. Name the coefficients \(a_{ij}\).
6. Package the coefficients into a matrix.
7. Identify that matrix as the metric.

Polar-coordinate metric on the plane
1. Take neighboring points separated by \(dr\) and \(d\theta\).
2. Draw the local right triangle.
3. The radial leg is \(dr\).
4. The angular leg is arc length \(r\,d\theta\), not \(d\theta\).
5. Apply Pythagoras.
6. Obtain \(ds^2=dr^2+r^2d\theta^2\).
7. Transform back with \(x=r\cos\theta,\ y=r\sin\theta\).
8. Recover the flat Cartesian form.

Sphere metric
1. Use angular coordinates \(\theta\) and \(\phi\) on a unit sphere.
2. Along the meridional direction, the distance for \(d\theta\) is \(d\theta\).
3. Along the azimuthal direction, the local circle has radius \(\sin\theta\).
4. Therefore the transverse arc length is \(\sin\theta\,d\phi\).
5. Apply Pythagoras to the local differential triangle.
6. Obtain \(ds^2=d\theta^2+\sin^2\theta\,d\phi^2\).
7. For radius \(R\), multiply the whole expression by \(R^2\).

Curvature criterion
1. Observe that flat space can have nonconstant metric coefficients in awkward coordinates.
2. Therefore variable coefficients alone do not prove curvature.
3. Ask whether there exists any coordinate system making the metric coefficients constant everywhere.
4. If yes, the space is flat.
5. If no, the space is intrinsically curved.

Hubble law
1. Fix two galaxies with constant comoving separation \(\Delta x\).
2. Define physical distance \(d=a(t)\Delta x\).
3. Differentiate with respect to time.
4. Since \(\Delta x\) is fixed, \(v=\dot d=\dot a\,\Delta x\).
5. Multiply and divide by \(a\).
6. Use \(a\Delta x=d\).
7. Obtain \(v=(\dot a/a)d\).
8. Identify \(H(t)=\dot a/a\).

Null-ray equation in the expanding metric
1. Restrict attention to motion along the \(x\)-axis.
2. Set \(d\tau^2=0\) for a light ray.
3. Substitute the cosmological metric.
4. Get \(0=dt^2-a^2(t)dx^2\).
5. Solve for the coordinate relation.
6. Obtain \(dt=a(t)dx\), equivalently \(dx=dt/a(t)\).
7. Read off the coordinate velocity \(dx/dt=1/a(t)\).

Age estimate from the Hubble law
1. Approximate the backward motion by constant recession velocity.
2. Use \(t\approx d/v\).
3. Insert \(v=Hd\).
4. Cancel the distance.
5. Obtain \(t\approx 1/H\).
6. Keep Susskind’s correction: this is a rough estimate, not an exact age formula.

## Notation Choices
- Use \(x^\mu\) for spacetime coordinates, with \(\mu,\nu=0,1,2,3\).
- Use \(x^0=t\) implicitly; keep \(t,x,y,z\) when the lecture is concrete.
- Use \(ds^2\) for the generic interval in geometric examples.
- Use \(d\tau^2\) when Susskind is explicitly speaking of proper time in spacetime and in the cosmology metric.
- Keep the lecture’s sign convention \(+---\): time positive, spatial pieces negative.
- Use \(\eta_{\mu\nu}\) for the Minkowski metric and \(g_{\mu\nu}(x)\) for the general spacetime metric.
- Use \(a_{ij}\) only for the pedagogical 2D coefficient-matrix example on the plane.
- Use \(\theta\) and \(\phi\) for sphere coordinates, with \(\theta\) taken as polar angle from the north pole in the lecture.
- Use \(r,\theta\) for polar coordinates on the plane.
- Use overdots for time derivatives: \(\dot a = da/dt\).
- Use \(\Delta x\) for fixed comoving separation and \(d\) for physical distance.
- Treat cosmological \(x,y,z\) as comoving labels; later prose can note that Susskind likes to think of them as dimensionless labels with \(a(t)\) carrying the distance units.
- Prefer “Hubble parameter” for \(\dot a/a\); note that the lecture sometimes says “Hubble constant” informally.
- Use “null line” and “light ray” interchangeably when \(d\tau^2=0\).

## Uncertain Mathematics
- The transcript is badly garbled around the early “multiply a solution by a number” discussion; keep only the standard linearity claim, not any garbled sentence-level detail.
- The exact board equations in `lecture_08_figure_02.png` are not fully legible; normalize \(x_1,x_2\) oscillator equations from the transcript, not from the frame alone.
- The nonlinear oscillator modification is conceptually clear, but the exact written arrangement of \(p\) and any extra coefficient beyond the basic \(p x^2\)-type term should be kept minimal.
- In `lecture_08_figure_03.png`, the full symmetrized mixed term is not completely visible; \(a_{21}\,dy\,dx\) is a reconstruction justified by the transcript.
- In `lecture_08_figure_04.png`, the clean full sphere metric should be taken from the transcript; the frame only secures \(ds^2\), \(d\theta^2\), and the \(\sin^2\theta\) structure.
- In `lecture_08_figure_05.png`, the exact left-board repeated-index expression is not secure symbol by symbol; preserve only the general transition to \(g_{\mu\nu}\)-notation.
- The lecture oscillates between “distance,” “interval,” and “proper time”; later notes should standardize gently without implying a different derivation.
- The \(H^{-1}\) age estimate must be stated with the lecture’s correction: the approximation is tied to constant recession velocity in the backward extrapolation, not to literally constant \(H(t)\).
- The explicit Newtonian evolution equation for \(a(t)\) is not derived in this lecture; only the shell-theorem reduction is set up for next time.
- The late horizon/light-propagation sketch is incomplete; do not promote it into a finished integral calculation in this lecture’s chapter.