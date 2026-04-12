# Math Bank
## Core Equations
- [visible]
  \[
  \omega=\frac{t}{4MG}
  \]

- [transcript-backed]
  \[
  \rho=0 \quad \text{when} \quad r=2MG
  \]

- [visible]
  \[
  ds^2=-\rho^2\,d\omega^2+d\rho^2
  \]

- [transcript-backed]
  \[
  ds^2=\rho^2\,d\theta^2+d\rho^2
  \]
  Euclidean polar comparison metric.

- [standard reconstruction]
  \[
  ds^2=-\left(1-\frac{2MG}{r}\right)dt^2+\frac{dr^2}{1-\frac{2MG}{r}}
  \]
  Radial-time Schwarzschild sector with consistent signs.

- [transcript-backed]
  \[
  ds^2\approx -dt^2+dr^2
  \qquad (r\gg 2MG)
  \]

- [transcript-backed]
  \[
  t=4MG\,\omega,
  \qquad
  dt^2=16M^2G^2\,d\omega^2
  \]

- [standard reconstruction]
  \[
  ds^2\approx -16M^2G^2\,d\omega^2+d\rho^2
  \qquad (r\gg 2MG,\ \rho\approx r)
  \]

- [transcript-backed]
  \[
  ds^2\sim \rho^2\,d\theta^2+d\rho^2
  \quad \text{near the tip of the cigar}
  \]

- [transcript-backed]
  \[
  ds^2\sim 16M^2G^2\,d\theta^2+d\rho^2
  \quad \text{far from the tip}
  \]

- [transcript-backed]
  \[
  \text{circumference} = 2\pi(4MG)=8\pi MG
  \]

- [transcript-backed]
  \[
  1-\frac{2MG}{r}>0 \quad \text{for} \quad r>2MG,
  \qquad
  1-\frac{2MG}{r}<0 \quad \text{for} \quad r<2MG
  \]

- [transcript-backed]
  \[
  r=0
  \]
  Singularity location.

- [standard reconstruction]
  \[
  i^+,\quad i^-,\quad i^0,\quad \mathscr{I}^+,\quad \mathscr{I}^-
  \]
  Clean Penrose-boundary notation for the flat-space diagram.

- [transcript-backed]
  \[
  ds^2_{\mathrm{inside}}=-dt^2+dx^2+dy^2+dz^2
  \]

- [transcript-backed]
  \[
  ds^2_{\mathrm{outside}}=\text{Schwarzschild}(M)
  \]

## Definitions And Objects
- \(\rho\): proper distance from the horizon, measured by “honest meter sticks” along the chosen spatial path.
- \(r\): Schwarzschild radial coordinate; not itself the proper distance from the horizon.
- \(\omega\): dimensionless time variable, Schwarzschild time measured in units of \(4MG\).
- Near-horizon geometry: the radial-time sector of Schwarzschild close to \(r=2MG\), written in \((\rho,\omega)\).
- Hyperbolic-angle interpretation: \(\omega\) plays the Lorentzian analogue of the Euclidean polar angle \(\theta\).
- Bifurcate horizon: the crossing point of the two null horizon lines in the local causal sketch.
- Event horizon: the full null surface beyond which no signal can escape to the exterior.
- Fixed-\(\rho\) curves: stationary outside observers hovering at constant proper distance from the horizon.
- Singularity: the \(r=0\) locus, treated in the lecture as a future boundary one reaches after crossing the horizon.
- Time-reversal invariance: Schwarzschild coefficients do not depend on \(t\), and \(dt^2\) is unchanged under \(t\to -t\).
- White hole: the time-reversed partner of the black hole, associated with a past singularity and past horizon.
- Penrose diagram: a compactified spacetime diagram preserving radial null lines at \(45^\circ\).
- \(i^\pm\): timelike future/past infinity.
- \(i^0\): spacelike infinity.
- \(\mathscr{I}^\pm\): future/past null infinity, “scri plus/minus.”
- Newton’s shell theorem: inside a spherical shell the Newtonian field vanishes; outside it equals the field of a point mass at the center.
- Birkhoff’s theorem: inside a spherically symmetric shell the spacetime is flat; outside it is Schwarzschild with the shell’s total mass.

## Derivation Steps
**Near-horizon recap**
1. Start from the Schwarzschild geometry.
2. Replace the Schwarzschild radial coordinate \(r\) by the proper-distance variable \(\rho\).
3. Define the dimensionless time variable \(\omega=t/(4MG)\).
4. Expand near \(r=2MG\), where \(\rho=0\).
5. Keep only the radial-time sector.
6. Obtain the near-horizon form \(ds^2=-\rho^2 d\omega^2+d\rho^2\).
7. Compare it to Euclidean polar coordinates to motivate the “hyperbolic angle” language.

**Far-away comparison**
1. Return to the Schwarzschild radial-time metric.
2. Take \(r\gg 2MG\), so \(1-2MG/r\to 1\).
3. Use \(r\approx \rho\) far from the hole.
4. Reduce the metric to flat radial-time form \(ds^2\approx -dt^2+dr^2\).
5. Substitute \(t=4MG\,\omega\).
6. Rewrite the time term as \(dt^2=16M^2G^2 d\omega^2\).
7. Conclude that the nontrivial change from near to far is in the coefficient of the time term.

**Cigar analogy**
1. Replace the Lorentzian time variable \(\omega\) by an ordinary angle \(\theta\).
2. Near the origin, keep the polar form \(\rho^2 d\theta^2+d\rho^2\).
3. Far away, replace the angular coefficient by the constant \(16M^2G^2\).
4. Interpret this as a geometry whose circular direction approaches constant circumference.
5. Read the resulting surface as a cigar: flat near the tip, cylindrical far away.
6. Use the asymptotic circumference \(8\pi MG\) to argue qualitatively that larger \(M\) means smaller curvature near the tip.

**Horizon as one-way barrier**
1. Draw radial null lines at \(45^\circ\).
2. Identify the fixed-\(\rho\) hyperbolae as outside stationary observers.
3. Mark the null surface through the bifurcation point as the event horizon.
4. Follow inward null rays: they cross the horizon.
5. Follow outward null rays launched from inside: they never reach the exterior region.
6. Conclude that signals can enter but not leave.

**Schwarzschild sign flip**
1. Inspect the factors \(1-2MG/r\) and \((1-2MG/r)^{-1}\).
2. For \(r>2MG\), the \(dt^2\) coefficient is negative and the \(dr^2\) coefficient positive.
3. For \(r<2MG\), both signs reverse.
4. Read this as an interchange of the coordinate roles of \(t\) and \(r\) inside the horizon.
5. Treat the interchange as a coordinate feature, not as a local singularity at the horizon.

**Locating the singularity**
1. Continue inward past \(r=2MG\).
2. Follow the coordinate continuation until \(r\to 0\).
3. Identify \(r=0\) as the genuinely singular locus.
4. Connect the \(r=0\) points in the sketch into a hyperbola-like future boundary.
5. Interpret this not as an ordinary place one can orbit around, but as a future endpoint reached after horizon crossing.

**Time reversal to white hole**
1. Note that Schwarzschild is time independent.
2. Replace \(t\to -t\); the metric is unchanged.
3. Therefore the time reverse of any allowed history is also mathematically allowed.
4. Reverse the history of infall through the future horizon.
5. Obtain emergence through a past horizon from a past singularity.
6. Name this time-reversed object a white hole.
7. Keep the physical status separate from the mathematical status.

**Flat-space Penrose compactification**
1. Start from the \(t\)-\(\rho\) half-plane with \(\rho\ge 0\).
2. Draw the ordinary grid of constant \(t\) and constant \(\rho\).
3. Demand a coordinate transformation that maps the infinite domain to a finite region.
4. Impose the rule that radial null lines remain at \(45^\circ\).
5. Compactify spacelike infinity to a point on the right.
6. Compactify timelike past/future infinity to the lower and upper ends of the left boundary.
7. Compactify null past/future infinity to the lower and upper slanted edges.

**Collapse setup from shell theorems**
1. Take a spherically symmetric shell of fixed total mass.
2. In Newtonian language, the field inside vanishes and the outside field is the same as a point mass.
3. In GR language, replace “vanishing field inside” by flat Minkowski spacetime inside.
4. Replace “point-mass field outside” by Schwarzschild spacetime outside.
5. Allow the shell radius to change with time while keeping total mass fixed.
6. Use this inside/outside patching as the setup for the next lecture’s collapse construction.

## Notation Choices
- Standardize every spoken \(m,g\) to \(M,G\) in the notes.
- Use lowercase \(\omega\), not \(\Omega\), because the board equation is visibly lowercase.
- Use \(\rho\) exclusively for proper distance from the horizon; do not let it drift into ordinary areal radius.
- Use \(r\) exclusively for the Schwarzschild radial coordinate.
- Use signature convention
  \[
  ds^2=-(\text{time part})+(\text{space part})
  \]
  throughout the cleaned chapter.
- Suppress the angular \(r^2 d\Omega_2^2\) sector whenever following the lecture’s two-dimensional radial-time discussion.
- Treat “bifurcate horizon” as the central crossing point in the local sketch, and “event horizon” as the full null boundary.
- For the Penrose section, use conventional \(i^\pm,i^0,\mathscr{I}^\pm\) in the clean redraw, but only after the prose has introduced Susskind’s spoken labels.
- Use \(H\) only as a frame-local board label; do not promote it into standard notation unless the chapter text explicitly defines it.
- Keep \(c=1\) implicit, matching the lecture.

## Uncertain Mathematics
- The transcript’s spoken Schwarzschild metric signs are inconsistent; the cleaned radial-time Schwarzschild formula should be marked as a standard reconstruction.
- The lecture does not give the explicit analytic relation \(\rho(r)\); do not invent a derivation for it.
- The statement “clocks close to the black hole read \(\rho\omega\)” is heuristic spoken language; the exact mathematical content is the metric coefficient \(-\rho^2 d\omega^2\), not a standalone clock formula.
- The cigar discussion is qualitative about curvature scale; the lecture does not provide an explicit curvature scalar, so the chapter should not add one unless clearly marked as extra.
- The singularity is described on the sketch as a hyperbola-like locus; preserve that causal picture, but do not overclaim a new exact coordinate formula from the board drawing alone.
- The Penrose-grid construction segment is partly garbled in the transcript; keep only the secure rules: compactify to a finite region and preserve radial null \(45^\circ\) lines.
- The eternal Schwarzschild Penrose diagram should be treated as a cautious standard reconstruction from transcript plus figures, not as a direct transcription of one fully legible board frame.
- The white-hole discussion is mathematically tied to time reversal, but the lecture’s physical verdict is entropic improbability rather than a strict no-go theorem.
- The virtual-graviton digression is conceptually loose and should not be elevated into formal mathematical notes.