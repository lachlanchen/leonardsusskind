# Math Bank
## Core Equations
- \(d=a\,\Delta x\) [transcript-backed]
- \(\dot d=\dot a\,\Delta x\) [transcript-backed]
- \(\dot d=\dfrac{\dot a}{a}\,d\) [transcript-backed]
- \(H(t)\equiv \dfrac{\dot a}{a}\) [transcript-backed]
- \(d=a\sqrt{(\Delta x)^2+(\Delta y)^2}\) [transcript-backed]
- \(d=a\sqrt{(\Delta x)^2+(\Delta y)^2+(\Delta z)^2}\) [transcript-backed]
- \(ds=a\,dx\) [transcript-backed]
- \(ds^2=a^2\,dx^2\) [transcript-backed]
- \(g_{xx}=a^2\) for the one-dimensional spatial metric [transcript-backed]
- \(d\tau^2=dt^2-a^2(t)\,dx^2\) [transcript-backed]
- \(g_{xx}=-a^2\) in the spacetime metric [transcript-backed]
- \(g_{tx}=g_{xt}=0\) [transcript-backed]
- \(d\tau^2=dt^2-a^2(t)\,dx^2-a^2(t)\,dy^2-a^2(t)\,dz^2\) [standard reconstruction]
- \(g_{\mu\nu}=\mathrm{diag}(1,-a^2,-a^2,-a^2)\) [standard reconstruction]
- \(B=3A \;\Rightarrow\; \dfrac{\dot B}{B}=\dfrac{\dot A}{A}\) [transcript-backed]
- \(a(t)\propto t\) [transcript-backed]
- \(a(t)\propto t^2\) [transcript-backed]
- \(a(t)\propto \log t\) [transcript-backed]
- \(2\pi a=L\) for the total distance around the circle [visible]
- \(d=a\,\Delta\theta\) [transcript-backed]
- \(ds^2=a^2\,d\theta^2\) [transcript-backed]
- \(ds^2=a^2(t)\,d\theta^2\) [transcript-backed]
- \(d\tau^2=dt^2-a^2(t)\,d\theta^2\) [transcript-backed]
- \(\dot d=\dot a\,\Delta\theta=\dfrac{\dot a}{a}\,d\) [transcript-backed]
- \(a(t)=\text{const}\) for the cylinder case [transcript-backed]
- \(a(t)\propto t\) for the cone case [transcript-backed]

## Definitions And Objects
- Comoving coordinates \(x,y,z\): labels attached to galaxies; they move with the galaxies rather than measuring physical distance directly.
- Finite coordinate separation \(\Delta x\): difference of galaxy labels.
- Infinitesimal coordinate separation \(dx\): calculus version of \(\Delta x\) for nearby points.
- Scale factor \(a(t)\): the physical distance between neighboring comoving galaxies in the line model.
- Hubble parameter \(H(t)\): the time-dependent ratio \(\dot a/a\); Susskind often says “Hubble constant,” but stresses its time dependence.
- Spatial distance \(d\) or \(ds\): physical distance, not raw coordinate difference.
- Proper time / spacetime interval \(d\tau\): interval along a worldline in the spacetime metric.
- Homogeneity: no dependence on spatial position; in metric language, coefficients do not depend on \(x,y,z\).
- Isotropy: no dependence on spatial direction; in metric language, the spatial coefficients are equal in different axes.
- One-dimensional isotropy: left-right symmetry.
- Circle coordinate \(\theta\): angular coordinate on the closed one-dimensional universe, taken in radians.
- Reference point \(\theta=0\): chosen origin on the circle.
- Periodicity on the circle: \(\theta\sim \theta+2\pi\).
- Closed and bounded: finite total extent without a boundary edge.
- Cylinder model: time-independent circle universe, \(a=\text{const}\).
- Cone model: linearly growing circle universe, \(a\propto t\).
- \(c=1\): units chosen so the speed of light is one light-year per year.

## Derivation Steps
One-dimensional Hubble law
1. Fix two galaxies, so \(\Delta x\) does not change with time.
2. Write the physical distance as \(d=a\,\Delta x\).
3. Differentiate with respect to time: \(\dot d=\dot a\,\Delta x\).
4. Multiply and divide by \(a\): \(\dot d=(\dot a/a)(a\,\Delta x)\).
5. Recognize \(a\,\Delta x=d\), so \(\dot d=(\dot a/a)d\).

Two- and three-dimensional extension
1. Assign physical leg lengths \(a\,\Delta x\), \(a\,\Delta y\), and \(a\,\Delta z\).
2. Apply the Pythagorean theorem to get \(d=a\sqrt{(\Delta x)^2+(\Delta y)^2}\) or \(d=a\sqrt{(\Delta x)^2+(\Delta y)^2+(\Delta z)^2}\).
3. Hold the coordinate differences fixed for a chosen pair of galaxies.
4. Differentiate only the factor \(a(t)\).
5. Rewrite the result as \(\dot d=(\dot a/a)d\).

Spatial metric from comoving distance
1. Replace the finite separation \(\Delta x\) by the infinitesimal \(dx\).
2. Write the neighboring physical distance as \(ds=a\,dx\).
3. Square it: \(ds^2=a^2\,dx^2\).
4. Read off the spatial metric coefficient \(g_{xx}=a^2\).

Spacetime metric from the expanding line
1. Use \(dt^2-(\text{spatial distance})^2\) for the interval.
2. Substitute \((\text{spatial distance})^2=a^2\,dx^2\).
3. Obtain \(d\tau^2=dt^2-a^2\,dx^2\).
4. Extend to higher dimensions by replacing \(dx^2\) with \(dx^2+dy^2+dz^2\).
5. Read off the diagonal metric with vanishing off-diagonal \(dt\,dx\)-type terms.

Scale-factor normalization does not matter
1. Redefine the scale factor by a constant multiple, e.g. \(B=3A\).
2. Differentiate: \(\dot B=3\dot A\).
3. Form the ratio: \(\dot B/B=3\dot A/3A\).
4. Conclude that \(\dot a/a\) is unchanged by constant rescaling of \(a\).

Circle metric and closed-universe Hubble law
1. Choose \(\theta\) as the coordinate and measure it in radians.
2. Set the total distance around the circle to \(2\pi a\).
3. Infer the arc length between nearby points: \(d=a\,\Delta\theta\).
4. Pass to infinitesimals: \(ds^2=a^2\,d\theta^2\).
5. Let \(a\) depend on time to get \(ds^2=a^2(t)\,d\theta^2\) and \(d\tau^2=dt^2-a^2(t)\,d\theta^2\).
6. Differentiate \(d=a\,\Delta\theta\) at fixed \(\Delta\theta\) to recover \(\dot d=(\dot a/a)d\).

Cylinder and cone identification
1. If \(a\) is constant in time, successive spatial circles have the same size.
2. The spacetime picture is a cylinder.
3. If \(a\propto t\), the spatial size grows linearly with time.
4. The spacetime picture is a cone.

## Notation Choices
- Use lowercase \(a(t)\) throughout the notes, even though the transcript often says “A” aloud.
- Use \(H(t)\) in formulas, with a short note that Susskind verbally calls it the “Hubble constant” while emphasizing that it depends on time.
- Use \(x,y,z\) as comoving coordinates by default; do not treat them as physical lengths.
- Use \(\Delta x,\Delta y,\Delta z\) for finite separations and \(dx,dy,dz\) for infinitesimal ones.
- Use \(d\) or \(ds\) for physical spatial distance; use \(d\tau\) for the spacetime interval / proper time.
- Keep the lecture’s signature convention \(+---\): spatial coefficients are positive in the purely spatial metric and negative in the spacetime metric.
- State explicitly that \(g_{xx}=a^2\) in the spatial metric but \(g_{xx}=-a^2\) in the spacetime metric.
- Use \(\theta\) for the circle coordinate and take it in radians.
- Use \(2\pi a\) for the circumference of the circle model; do not introduce a separate \(r\) parameter in the main notes.
- Keep \(c=1\) unless a note explicitly discusses unit conventions.
- When the notes discuss the circle model extrinsically, say “radius-like parameter \(a\)” rather than building extra notation that the lecture does not stabilize.

## Uncertain Mathematics
- The full three-dimensional line element and full diagonal metric matrix are only partly visible in `lecture_01_figure_02.png`; the clean forms should be presented as cautious standard completions.
- The small separation label in the left-hand spacetime sketch is not reliably legible; if mentioned, describe it only as a proper spatial separation marker.
- The lecture briefly wobbles in the circle discussion over whether the scale factor means the whole circumference or a radius-like quantity. The stable final relation is \(L=2\pi a\) together with local arc length \(a\,\Delta\theta\).
- The board in `lecture_01_figure_03.png` does not visibly show \(ds^2=a^2\,d\theta^2\); that formula is transcript-backed, not directly read from the frame.
- The algebra in the discussion of a non-unit time-time coefficient is transcribed poorly. The safe takeaway is the conceptual one: a time-only prefactor of \(dt^2\) can be absorbed by redefining the time coordinate.
- The cylinder/cone flatness remarks belong to the one-space, one-time toy model used in the lecture; they should not be generalized without qualification to realistic \(3+1\)-dimensional cosmology.
- The circle-version Hubble law is locally clean, but for separations comparable to the full circumference the lecture itself notes an ambiguity about “coming around the other side.”