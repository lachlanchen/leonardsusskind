# Math Bank
## Core Equations
- [transcript-backed]
  \[
  d\tau^2 = dt^2 - \frac{1}{c^2}\left(dx^2+dy^2+dz^2\right)
  \]
- [transcript-backed]
  \[
  d\tau^2 = 0
  \]
  for light rays.
- [transcript-backed]
  \[
  c^2 dt^2 = dx^2,\qquad c\,dt = \pm dx,\qquad \frac{dx}{dt}=\pm c
  \]
- [transcript-backed]
  \[
  ds^2 = g_{\mu\nu}\,dx^\mu dx^\nu
  \]
  with the lecture verbally using \(G_{\mu\nu}\).
- [transcript-backed]
  \[
  d\Omega^2 = d\theta^2 + \sin^2\theta\, d\phi^2
  \]
- [visible]
  \[
  d\tau^2 = dt^2 - \left(dr^2 + r^2 d\Omega^2\right)
  \]
- [visible]
  \[
  1-\frac{2MG}{c^2 r}
  \]
- [visible]
  \[
  1-\frac{R_s}{r}
  \]
- [standard reconstruction]
  \[
  d\tau^2
  =
  \left(1-\frac{2Gm}{c^2 r}\right)dt^2
  -
  \frac{dr^2}{1-\frac{2Gm}{c^2 r}}
  -
  r^2 d\Omega^2
  \]
- [transcript-backed]
  \[
  R_s=\frac{2Gm}{c^2},\qquad R_s=2Gm\ \text{when } c=1
  \]
- [transcript-backed]
  \[
  r=2Gm \quad \text{(horizon)},\qquad r=0 \quad \text{(singularity)}
  \]
- [transcript-backed]
  \[
  d\Omega^2=0
  \]
  for radial light rays.
- [standard reconstruction]
  \[
  \left(1-\frac{2Gm}{r}\right)dt^2
  =
  \frac{dr^2}{1-\frac{2Gm}{r}}
  \]
  in \(c=1\) units for radial null motion.
- [transcript-backed]
  \[
  dr=\pm\left(1-\frac{2Gm}{r}\right)dt,\qquad \frac{dr}{dt}=\pm\left(1-\frac{2Gm}{r}\right)
  \]
- [transcript-backed]
  \[
  \frac{dr}{dt}\to 0 \quad \text{as} \quad r\to 2Gm
  \]
  for the outgoing branch.
- [transcript-backed]
  \[
  dE = T\,dS
  \]
- [transcript-backed]
  \[
  E=cp
  \]
- [transcript-backed]
  \[
  p\sim \frac{h}{\lambda}
  \]
  with Susskind verbally wavering between \(h\) and \(\hbar\) and ignoring \(2\pi\) factors.
- [transcript-backed]
  \[
  E\sim \frac{ch}{\lambda}
  \]
- [transcript-backed]
  \[
  \lambda \sim R_s \sim 2Gm
  \]
  for the one-bit photon argument.
- [standard reconstruction]
  \[
  \Delta E \sim \frac{ch}{R_s}
  \]
- [standard reconstruction]
  \[
  \Delta m \sim \frac{h}{R_s c}
  \]
- [standard reconstruction]
  \[
  \Delta R_s \sim \frac{Gh}{R_s c^3}
  \]
- [standard reconstruction]
  \[
  R_s\,\Delta R_s \sim \frac{Gh}{c^3}
  \]
  so the horizon area changes by a Planck-scale area per bit.
- [standard reconstruction]
  \[
  \ell_P^2 \sim \frac{G\hbar}{c^3}
  \]
- [transcript-backed]
  \[
  T_H \sim \frac{ch}{Gm}
  \]
  as the lecture’s order-of-magnitude Hawking temperature.
- [transcript-backed]
  \[
  S_{\mathrm{BH}} \propto \frac{A\,c^3}{G\hbar}
  \]
- [standard reconstruction]
  \[
  S_{\mathrm{BH}}=\frac{A\,c^3}{4G\hbar}
  \]

## Definitions And Objects
- Proper time: the relativistic interval \(d\tau\) between neighboring spacetime points.
- Null trajectory: a trajectory satisfying \(d\tau^2=0\); this is the invariant characterization of light motion.
- Metric tensor: the spacetime coefficient object \(g_{\mu\nu}\) or \(G_{\mu\nu}\) in the lecture.
- Spherical coordinates: \(r\) plus two angular coordinates summarized by \(\Omega\).
- Unit-sphere metric: \(d\Omega^2\), shorthand for the metric on the unit 2-sphere.
- Schwarzschild radius: \(R_s\), also called the horizon radius.
- Horizon: the locus \(r=2Gm\) in \(c=1\) units.
- Singularity: the locus \(r=0\).
- Outgoing / ingoing radial light rays: the \(+\) and \(-\) branches after taking the square root of the radial null equation.
- Coordinate time: the Schwarzschild \(t\) used in the light-ray slowdown discussion.
- Entropy \(S\): hidden or inaccessible information, treated qualitatively as a bit count.
- Temperature \(T\): energy cost of hiding one additional bit, leading to \(dE=T\,dS\).
- Planck area / Planck length: the universal area increment per bit and its square root in the Bekenstein argument.

## Derivation Steps
Flat-space light-ray condition:
1. Start from
   \[
   d\tau^2 = dt^2 - \frac{1}{c^2}(dx^2+dy^2+dz^2).
   \]
2. Restrict to motion along the \(x\)-direction, so \(dy=dz=0\).
3. Impose the light-ray rule \(d\tau^2=0\).
4. Rearrange to get \(c^2dt^2=dx^2\).
5. Take the square root to obtain \(c\,dt=\pm dx\).
6. Divide by \(dt\) to get \(\frac{dx}{dt}=\pm c\).

Flat space in spherical coordinates:
1. Replace Cartesian spatial increments by radial and angular increments.
2. Use the unit-sphere metric \(d\Omega^2=d\theta^2+\sin^2\theta\,d\phi^2\).
3. Write the spatial part as \(dr^2+r^2d\Omega^2\).
4. Insert this into the flat spacetime interval to get
   \[
   d\tau^2=dt^2-(dr^2+r^2d\Omega^2)
   \]
   in \(c=1\) units.

Radial light rays in Schwarzschild coordinates:
1. Start from the Schwarzschild metric.
2. Restrict to radial motion by setting \(d\Omega^2=0\).
3. Impose the light-ray condition \(d\tau^2=0\).
4. Move the \(dr^2\) term to the other side:
   \[
   \left(1-\frac{2Gm}{r}\right)dt^2=\frac{dr^2}{1-\frac{2Gm}{r}}.
   \]
5. Multiply through by \(1-\frac{2Gm}{r}\).
6. Take the square root:
   \[
   dr=\pm\left(1-\frac{2Gm}{r}\right)dt.
   \]
7. Divide by \(dt\):
   \[
   \frac{dr}{dt}=\pm\left(1-\frac{2Gm}{r}\right).
   \]
8. Read \(+\) as outgoing and \(-\) as ingoing.

Horizon slowdown in coordinate time:
1. Use the outgoing branch
   \[
   \frac{dr}{dt}=1-\frac{2Gm}{r}.
   \]
2. Far from the black hole, \(2Gm/r\ll 1\), so \(\frac{dr}{dt}\approx 1\).
3. As \(r\to 2Gm\), the factor \(1-\frac{2Gm}{r}\to 0\).
4. Conclude that outgoing light has vanishing coordinate speed at the horizon.
5. Use this as the basis for the \(t\)-\(r\) diagram where outgoing rays become vertical near the horizon.

Temperature from one hidden bit:
1. Use the lecture definition that hiding one bit changes the entropy by one unit.
2. Define temperature as the energy added per one-bit increase in hidden information.
3. Generalize from one bit to many bits.
4. Write the thermodynamic differential relation
   \[
   dE=T\,dS.
   \]

Bekenstein one-bit photon argument:
1. Ask for the simplest extra object that adds only one bit to the black hole.
2. Choose a photon whose position uncertainty is as large as possible while still allowing absorption.
3. Set its wavelength to the black-hole scale:
   \[
   \lambda \sim R_s.
   \]
4. Use photon kinematics:
   \[
   E=cp,\qquad p\sim \frac{h}{\lambda},
   \]
   so
   \[
   \Delta E \sim \frac{ch}{R_s}.
   \]
5. Convert energy to mass:
   \[
   \Delta m \sim \frac{\Delta E}{c^2} \sim \frac{h}{R_s c}.
   \]
6. Use \(R_s\propto Gm/c^2\) to infer
   \[
   \Delta R_s \sim \frac{Gh}{R_s c^3}.
   \]
7. Multiply by \(R_s\) to get
   \[
   R_s\Delta R_s \sim \frac{Gh}{c^3}.
   \]
8. Interpret this as a universal area increment per bit.
9. Conclude that the entropy is proportional to horizon area in Planck units.

Area law refinement:
1. The lecture argument gives proportionality \(S_{\mathrm{BH}}\propto A/( \text{Planck area})\).
2. Bekenstein argued for the proportionality but not the exact coefficient.
3. Hawking fixes the coefficient to \(1/4\).
4. The cleaned final form is
   \[
   S_{\mathrm{BH}}=\frac{A\,c^3}{4G\hbar}.
   \]

## Notation Choices
- Use \(m\) for the black-hole mass in the notes, even though the frame handwriting can look like \(M\).
- Use \(R_s\) for the Schwarzschild radius throughout.
- Use \(d\tau^2\) in the lecture-flow equations, since that is Susskind’s spoken and visible convention most of the time.
- Use \(ds^2=g_{\mu\nu}dx^\mu dx^\nu\) only for the general tensor statement; note silently that the lecture says \(G_{\mu\nu}\).
- Use \(d\Omega^2\) for the unit 2-sphere metric and define it explicitly once by
  \[
  d\Omega^2=d\theta^2+\sin^2\theta\,d\phi^2.
  \]
- After the early setup, default to \(c=1\) inside the lecture flow; restore \(c\) only in cleaned summary formulas where dimensional clarity matters.
- Keep \(S\) as entropy in the lecture’s bit-count normalization; do not introduce \(k_B\) into the main lecture reconstruction.
- Use \(\sim\) for the Bekenstein one-bit estimates.
- Normalize final standard formulas with \(\hbar\), but explicitly preserve the lecture’s indifference to factors of \(2\pi\).
- Use \(+\) for outgoing and \(-\) for ingoing in the radial null equation.

## Uncertain Mathematics
- The lower Schwarzschild line in the frame does not securely determine every sign; the clean metric should be reconstructed from the transcript plus the flat-space limit.
- The interval symbol in the frame may be \(d\tau^2\) or \(ds^2\); \(d\tau^2\) is the best reading, but not guaranteed.
- The transcript is badly garbled around 00:26:10 during the radial null-ray manipulation; that algebra must be reconstructed from the surrounding clean statements.
- Susskind alternates between \(h\) and \(\hbar\) and explicitly ignores \(2\pi\) factors; the one-bit and temperature estimates are order-of-magnitude arguments, not exact formulas.
- The statement that the area changes by \(Gh/c^3\) per bit is heuristic in the lecture; strictly, he is using proportionality between area and \(R_s^2\) and ignoring factors like \(4\pi\) and \(2\).
- The Planck length / Planck area discussion is also approximate in the lecture because of the \(h\) versus \(\hbar\) looseness.
- The exact coefficient \(1/4\) in
  \[
  S_{\mathrm{BH}}=\frac{A\,c^3}{4G\hbar}
  \]
  is not derived in the lecture’s handwaving argument; it is reported as Hawking’s correction.
- The entropy variable is treated as hidden-information count rather than standard thermodynamic entropy with full statistical-mechanics normalization; keep that lecture convention explicit.