# Math Bank
## Core Equations
- [visible] \(x'=\dfrac{x-vt}{\sqrt{1-v^2}}\)
- [visible] \(t'=\dfrac{t-vx}{\sqrt{1-v^2}}\)
- [transcript-backed] \(x=\dfrac{x'+vt'}{\sqrt{1-v^2}}\)
- [transcript-backed] \(t=\dfrac{t'+vx'}{\sqrt{1-v^2}}\)
- [transcript-backed] \(y'=y\)
- [transcript-backed] \(z'=z\)
- [transcript-backed] \(x'=0 \iff x=vt\)
- [visible] \(x''=\dfrac{x'-ut'}{\sqrt{1-u^2}}\)
- [visible] \(t''=\dfrac{t'-ux'}{\sqrt{1-u^2}}\)
- [transcript-backed] \(x''=\dfrac{\dfrac{x-vt}{\sqrt{1-v^2}}-u\,\dfrac{t-vx}{\sqrt{1-v^2}}}{\sqrt{1-u^2}}\)
- [transcript-backed] \(x''=\dfrac{(1+uv)x-(u+v)t}{\sqrt{1-v^2}\sqrt{1-u^2}}\)
- [transcript-backed] \(x''=0 \iff (1+uv)x-(u+v)t=0\)
- [transcript-backed] \(x=\dfrac{u+v}{1+uv}\,t\)
- [transcript-backed] \(w=\dfrac{u+v}{1+uv}\)
- [standard reconstruction] \(x''=\dfrac{x-wt}{\sqrt{1-w^2}}\)
- [standard reconstruction] \(t''=\dfrac{t-wx}{\sqrt{1-w^2}}\)
- [transcript-backed] \(w=\dfrac{u+v}{1+\dfrac{uv}{c^2}}\)
- [transcript-backed] \(u=1 \Longrightarrow w=1\)
- [transcript-backed] \(\tau^2=t^2-x^2\)
- [transcript-backed] \(\tau^2=t^2-x^2=t'^2-x'^2=t''^2-x''^2\)
- [transcript-backed] \(\tau^2=t^2-x^2-y^2-z^2\)
- [transcript-backed] \(t^2-x^2=0\) for a light ray in \(1+1\) dimensions
- [transcript-backed] \(t^2-x^2-y^2-z^2=0\) for a light ray in \(3+1\) dimensions
- [transcript-backed] \(x^\mu=(t,x,y,z)\)
- [transcript-backed] \(x^i=(x,y,z)\)
- [transcript-backed] \(\tau^2=(x^0)^2-(x^1)^2-(x^2)^2-(x^3)^2\)
- [transcript-backed] \(\Delta x^\mu=(\Delta t,\Delta x,\Delta y,\Delta z)\)
- [transcript-backed] \(\Delta\tau^2=\Delta t^2-\Delta x_i\Delta x_i\)
- [transcript-backed] \(\Delta\tau^2=\Delta t^2-\Delta x^2-\Delta y^2-\Delta z^2\)
- [transcript-backed] \(u^\mu=\dfrac{\Delta x^\mu}{\Delta\tau}\)
- [standard reconstruction] \(u^\mu=\dfrac{dx^\mu}{d\tau}\)

## Definitions And Objects
- Event: a spacetime occurrence at a point of space and time, assigned coordinates by each observer.
- Unprimed frame \((x,t)\): the stationary observer’s coordinates.
- Primed frame \((x',t')\): the passenger/train observer’s coordinates.
- Double-primed frame \((x'',t'')\): the kiddie-car observer’s coordinates.
- \(v\): velocity of the train relative to the stationary observer.
- \(u\): velocity of the kiddie car relative to the train/passenger.
- \(w\): velocity of the kiddie car relative to the stationary observer.
- Proper interval / proper time \(\tau\): invariant spacetime separation between two events.
- Future light cone: all spacetime points reachable by a light ray emitted from the origin event.
- Past light cone: all spacetime points that can send a light ray to the origin event.
- \(x^i\): spatial components only, with \(i\) running over space.
- \(x^\mu\): spacetime components, with \(\mu\) running over time and space.
- \(\Delta x^\mu\): small but initially discrete spacetime interval along a trajectory.
- Four-velocity \(u^\mu\): spacetime interval divided by invariant proper-time interval.
- Ordinary velocity: \(\Delta x/\Delta t\) limit, with only spatial components.
- Four-vector: any object transforming under Lorentz transformations the way \(x^\mu\) does.

## Derivation Steps
Velocity of the primed origin:
1. Start from the Lorentz transformation for \(x'\).
2. Set \(x'=0\) to pick out the origin of the primed frame.
3. Ignore the denominator for the purpose of finding where the numerator vanishes.
4. Solve \(x-vt=0\).
5. Conclude that the primed origin traces the worldline \(x=vt\) in the unprimed frame.

Velocity-addition law:
1. Write the second Lorentz transformation \(x''=\dfrac{x'-ut'}{\sqrt{1-u^2}}\).
2. Substitute \(x'=\dfrac{x-vt}{\sqrt{1-v^2}}\).
3. Substitute \(t'=\dfrac{t-vx}{\sqrt{1-v^2}}\).
4. Pull out the common denominator \(\sqrt{1-v^2}\sqrt{1-u^2}\).
5. Expand the numerator: \((x-vt)-u(t-vx)\).
6. Collect the \(x\)-terms to get \((1+uv)x\).
7. Collect the \(t\)-terms to get \(-(u+v)t\).
8. Set \(x''=0\) to locate the double-primed origin.
9. Drop the denominator and solve \((1+uv)x-(u+v)t=0\).
10. Obtain \(x=\dfrac{u+v}{1+uv}t\).
11. Read off the relative velocity \(w=\dfrac{u+v}{1+uv}\).

Restoring \(c\):
1. Start from \(w=\dfrac{u+v}{1+uv}\) in units with \(c=1\).
2. Notice that \(u+v\) has velocity units but \(1+uv\) is dimensionally inconsistent in ordinary units.
3. Insert \(c^2\) so that the denominator becomes dimensionless.
4. Write \(w=\dfrac{u+v}{1+\dfrac{uv}{c^2}}\).

Light speed as a fixed point of composition:
1. Set one of the velocities equal to the speed of light, \(u=1\) in relativistic units.
2. Substitute into \(w=\dfrac{u+v}{1+uv}\).
3. Compute \(w=\dfrac{1+v}{1+v}=1\).
4. Conclude that a light ray is still assigned speed \(1\) after composition of boosts.

Proper interval in more than one spatial dimension:
1. Start from the \(1+1\) formula \(\tau^2=t^2-x^2\).
2. Reinterpret \(x^2\) as spatial distance squared from the origin.
3. Put back the other directions using the Euclidean spatial distance \(x^2+y^2+z^2\).
4. Replace the single spatial term by the full squared spatial distance.
5. Obtain \(\tau^2=t^2-x^2-y^2-z^2\).
6. State that this remains invariant under Lorentz transformations together with ordinary spatial rotations.

Light cone from the null interval:
1. In \(1+1\) dimensions, a light ray satisfies \(x=t\) or \(x=-t\) in units with \(c=1\).
2. Substitute into \(\tau^2=t^2-x^2\).
3. Get \(\tau^2=0\).
4. In higher dimensions, replace \(x^2\) by \(x^2+y^2+z^2\).
5. Obtain \(t^2-x^2-y^2-z^2=0\).
6. Interpret the set of such points as the light cone.

Four-velocity:
1. Take a small spacetime interval \(\Delta x^\mu\) along a trajectory.
2. Define the invariant proper-time interval \(\Delta\tau\) by \(\Delta\tau^2=\Delta t^2-\Delta x_i\Delta x_i\).
3. Divide the spacetime interval by \(\Delta\tau\) instead of by \(\Delta t\).
4. Define \(u^\mu=\dfrac{\Delta x^\mu}{\Delta\tau}\).
5. In smooth notation, pass to \(u^\mu=\dfrac{dx^\mu}{d\tau}\).

## Notation Choices
- Use lowercase \(x\) consistently in the final notes, even though the board sometimes writes uppercase \(X\).
- Keep the lecture’s frame labels: unprimed \((x,t)\), primed \((x',t')\), double-primed \((x'',t'')\).
- Keep the lecture’s velocity symbols: \(v\) for train relative to station, \(u\) for kiddie car relative to train, \(w\) for kiddie car relative to station.
- Work primarily in relativistic units with \(c=1\), and restore \(c\) only when dimensional meaning is being discussed explicitly.
- Keep the lecture’s convention \(x^0=t\), not \(x^0=ct\).
- Use \(i\) for spatial indices only and \(\mu\) for spacetime indices.
- Write \(x^\mu=(t,x,y,z)\) in the order the lecture settles on.
- Keep \(\Delta x^\mu\) and \(\Delta\tau\) for the lecture-faithful first pass; introduce differential notation only as a later clean completion.
- Treat Lorentz transformations as linear maps on four-vectors, but do not force an explicit matrix formula unless the chapter needs it later.
- Use “proper interval” and “proper time” in the same locally flexible way the lecture does, but keep the formulas precise.

## Uncertain Mathematics
- The transcript briefly garbles the interpretation of \(x=vt\); the correct use is that \(x'=0\) identifies the primed origin, whose unprimed worldline is \(x=vt\).
- The transcript stumbles during the \(x''=0\) step; the consistent cleaned result is \((1+uv)x-(u+v)t=0\), hence \(x=\dfrac{u+v}{1+uv}t\).
- The board fragment at the left edge of `lecture_02_figure_04.png` is too cropped to use as direct algebraic evidence for the velocity-addition formula.
- Susskind momentarily writes the composed Lorentz form incorrectly before correcting himself; the stable final version is \(x''=\dfrac{x-wt}{\sqrt{1-w^2}}\), \(t''=\dfrac{t-wx}{\sqrt{1-w^2}}\).
- The arithmetic example with \(u=v=0.01\) contains a spoken slip: \(uv=0.0001\), not \(0.001\).
- The near-relativistic example should be written cleanly as \(w=\dfrac{0.9+0.9}{1+0.9^2}=\dfrac{1.8}{1.81}<1\).
- The verbal discussion of the Lorentz matrix is incomplete on the board; if a matrix is written later, it should be presented as a careful reconstruction rather than a direct transcript extraction.
- The visible notation near the highlighted event in `lecture_02_figure_02.png` is not legible enough to support a precise mathematical transcription.
- The label near the lower rightward arrow in `lecture_02_figure_04.png` looks like \(w\), but it is less secure than the clearly visible \(u\).