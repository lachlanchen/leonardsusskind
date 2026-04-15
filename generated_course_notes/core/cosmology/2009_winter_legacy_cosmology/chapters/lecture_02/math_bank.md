# Math Bank
## Core Equations
- \(v = H(t)\,d\) [transcript-backed]
- \(ds^2 = a(t)^2\left(dx^2 + dy^2 + dz^2\right)\) [visible]
- \(d\tau^2 = dt^2 - ds^2\) [transcript-backed]
- \(d\tau^2 = dt^2 - a(t)^2\left(dx^2 + dy^2 + dz^2\right)\) [visible]
- \(g_{\mu\nu} = \mathrm{diag}(1,-a^2,-a^2,-a^2)\) [standard reconstruction]
- \(dt = d\tau\) along a comoving galaxy worldline [transcript-backed]
- \(\frac{mv^2}{2}\) [visible]
- \(V(d) = -\frac{GMm}{d}\) [transcript-backed]
- \(E = \frac{mv^2}{2} - \frac{GMm}{d}\) [standard reconstruction]
- \(\frac{mv^2}{2} - \frac{mMG}{D}\) [visible]
- \(V(d) \propto \frac{1}{d}\) [standard reconstruction]
- \(V(d) \propto -\frac{1}{d}\) [standard reconstruction]
- \(d = a(t)\,x\) [transcript-backed]
- \(v = \dot d = \dot a\,x\) [transcript-backed]
- \(M(d) = \frac{4\pi}{3}\rho\,d^3\) [transcript-backed]
- \(M(d) = \frac{4\pi}{3}\rho\,a^3x^3\) [transcript-backed]
- \(\frac{v^2}{2} - \frac{GM(d)}{d} = \text{constant}\) [standard reconstruction]
- \(\dot a^{\,2}x^2 - \frac{8\pi G}{3}\rho\,a^2x^2 = \text{constant}(x)\) [standard reconstruction]
- \(\text{constant}(x) = -k\,x^2\) [transcript-backed]
- \(\dot a^{\,2} = \frac{8\pi G}{3}\rho\,a^2 - k\) [standard reconstruction]
- \(\left(\frac{\dot a}{a}\right)^2 = \frac{8\pi G}{3}\rho - \frac{k}{a^2}\) [transcript-backed]
- \(\rho = \frac{m_{\Box}}{a^3}\) [transcript-backed]
- \(\left(\frac{\dot a}{a}\right)^2 = \frac{8\pi G\,m_{\Box}}{3a^3}\) for \(k=0\) [transcript-backed]
- \(a(t) = c\,t^p\) [transcript-backed]
- \(\dot a = cp\,t^{p-1}\) [transcript-backed]
- \(\frac{\dot a}{a} = \frac{p}{t}\) [transcript-backed]
- \(\frac{p^2}{t^2} = \frac{8\pi G\,m_{\Box}}{3c^3\,t^{3p}}\) [transcript-backed]
- \(p = \frac{2}{3}\) [transcript-backed]
- \(c^3 = 6\pi G\,m_{\Box}\) [transcript-backed]
- \(a(t) = \left(6\pi G\,m_{\Box}\right)^{1/3} t^{2/3}\) [transcript-backed]
- More generally, \(a(t) \propto (t-t_0)^{2/3}\) [transcript-backed]
- \(H(t) = \frac{\dot a}{a} = \frac{2}{3t}\) [transcript-backed]
- \(t = \frac{2}{3H}\) [transcript-backed]
- \(\frac{\dot a^{\,2}}{a^2} - \frac{k}{a^2} = \frac{8\pi G}{3}\rho\) [transcript-backed]

## Definitions And Objects
- \(a(t)\): scale factor; in the flat comoving grid it is the physical distance, measured in ordinary length units, between neighboring coordinate points separated by one coordinate unit.
- \(x,y,z\): comoving coordinates; fixed for galaxies that participate only in the uniform Hubble flow.
- \(d\) or \(D\): physical separation or radius.
- \(t\): cosmic time measured by clocks moving with the galaxies.
- \(\tau\): proper time.
- \(H(t)\): Hubble parameter; constant in space under homogeneity, generally time-dependent.
- \(m\): test mass in the Newtonian warm-up.
- \(M\): heavy gravitating source in the warm-up; later also enclosed cosmological mass inside radius \(d\).
- \(\rho(t)\): mass density of the homogeneous universe.
- \(k\): spatially uniform integration constant in the Friedmann equation; dimensionless in \(c=1\) units; may be positive, negative, or zero.
- \(m_{\Box}\): mass inside a unit comoving cube; this is the lecture’s later “mass in a cubic region one unit on a side.”
- Newton’s shell theorem as used here: for a particle at radius \(d\) in a spherically symmetric mass distribution, only the mass interior to radius \(d\) contributes to the force.

## Derivation Steps
1. Kinematics from homogeneity and isotropy
   1. Assume the universe is homogeneous and isotropic.
   2. Conclude that recession velocity is linear in distance at fixed time: \(v=H(t)d\).
   3. Introduce comoving coordinates in which galaxies sit at fixed \(x,y,z\).
   4. Encode physical distance by the flat spatial metric \(ds^2=a(t)^2(dx^2+dy^2+dz^2)\).
   5. Upgrade to spacetime: \(d\tau^2=dt^2-ds^2\).
   6. In the comoving frame, along a galaxy worldline, \(dt=d\tau\).

2. Newtonian warm-up
   1. Take a heavy mass \(M\) and a radially outgoing test mass \(m\).
   2. Write the kinetic energy as \(\frac12 mv^2\).
   3. Write the gravitational potential energy as \(-GMm/d\).
   4. Form the conserved total energy \(E=\frac12 mv^2-\frac{GMm}{d}\).
   5. Use the sign of \(E\) to classify motion into \(E>0\), \(E=0\), \(E<0\).

3. Cosmological reduction via shell theorem
   1. Choose an arbitrary galaxy as temporary center.
   2. Pick another galaxy at comoving coordinate \(x\).
   3. Use Newton’s shell theorem to replace all interior mass by a point mass at the center and ignore exterior mass.
   4. Write the physical radius of the second galaxy as \(d=ax\).
   5. Write its recession speed as \(v=\dot d=\dot a\,x\).
   6. Write the enclosed mass as \(M(d)=\frac{4\pi}{3}\rho d^3=\frac{4\pi}{3}\rho a^3x^3\).
   7. Insert these into the Newtonian energy equation.

4. Elimination of explicit galaxy label
   1. Divide the Newtonian energy equation by the test mass \(m\).
   2. Substitute \(v=\dot a\,x\), \(d=ax\), \(M(d)=\frac{4\pi}{3}\rho a^3x^3\).
   3. Simplify the potential term: \(\frac{GM(d)}{d}\to \frac{4\pi G}{3}\rho a^2x^2\).
   4. Observe that the left-hand side is proportional to \(x^2\).
   5. Conclude that the time-constant on the right must also be proportional to \(x^2\).
   6. Write that constant as \(-k\,x^2\).
   7. Divide through by \(x^2\).
   8. Obtain \(\dot a^{\,2}=\frac{8\pi G}{3}\rho a^2-k\).
   9. Divide by \(a^2\) to get \(\left(\frac{\dot a}{a}\right)^2=\frac{8\pi G}{3}\rho-\frac{k}{a^2}\).

5. Density law
   1. Consider a unit comoving cube.
   2. Let its fixed enclosed mass be \(m_{\Box}\).
   3. Its physical volume is \(a^3\).
   4. Therefore \(\rho = m_{\Box}/a^3\).

6. Critical case \(k=0\)
   1. Set \(k=0\) in the Friedmann equation.
   2. Get \(\left(\frac{\dot a}{a}\right)^2=\frac{8\pi G\,m_{\Box}}{3a^3}\).
   3. Guess a power-law solution \(a(t)=ct^p\).
   4. Compute \(\dot a=cp\,t^{p-1}\).
   5. Compute \(\dot a/a=p/t\).
   6. Substitute to obtain \(\frac{p^2}{t^2}=\frac{8\pi G\,m_{\Box}}{3c^3 t^{3p}}\).
   7. Match time powers: \(3p=2\), hence \(p=2/3\).
   8. Match coefficients: \(p^2=\frac{8\pi G\,m_{\Box}}{3c^3}\).
   9. With \(p=2/3\), solve for \(c^3=6\pi G\,m_{\Box}\).
   10. Conclude \(a(t)=\left(6\pi G\,m_{\Box}\right)^{1/3}t^{2/3}\), up to a time shift \(t\to t-t_0\).

7. Hubble-time relation
   1. Start from \(a(t)=ct^{2/3}\).
   2. Differentiate: \(\dot a=\frac23 ct^{-1/3}\).
   3. Divide: \(H=\dot a/a=\frac{2}{3t}\).
   4. Invert: \(t=\frac{2}{3H}\).
   5. Note that the constant \(c\), hence the dependence on \(m_{\Box}\), cancels.

## Notation Choices
- Use \(a(t)\) for the scale factor throughout.
- Use \(H(t)\) rather than “Hubble constant” in equations; reserve “Hubble constant” for quoted lecture phrasing.
- Use \(d\) for physical distance in cleaned equations; mention that the board often shows uppercase \(D\).
- In the Newtonian warm-up, keep \(m\) for the outgoing test mass and \(M\) for the heavy source.
- In the cosmology derivation, write enclosed mass as \(M(d)\) to distinguish it from the warm-up source.
- For the unit comoving cube mass, use \(m_{\Box}\) in the working notes to avoid collision with the test mass \(m\).
- Use overdots for \(d/dt\), with \(t\) the comoving cosmic time.
- Adopt \(c=1\) when discussing units, matching the lecture’s convention.
- Use mostly-minus signature in the spacetime interval: \(d\tau^2=dt^2-a(t)^2(dx^2+dy^2+dz^2)\).
- Keep the historical Friedmann form with \(-k/a^2\) on the right when following the lecture’s board order.
- When discussing the board frame literally, allow the lecture-order product \(mMG/D\); when presenting cleaned mathematics, regularize to \(GMm/d\).

## Uncertain Mathematics
- The transcript is corrupted in the cosmological energy rewrite around 00:55:21–00:56:18; the clean form \(\frac{v^2}{2}-\frac{GM(d)}{d}=\text{constant}\) and its doubled version should be reconstructed from the earlier warm-up and the later Friedmann result.
- The transcript is also corrupted around 00:57:24–00:58:26; the clean substitutions \(d=ax\) and \(v=\dot a x\) should be treated as transcript-supported standard cleanup.
- The matrix form \(g_{\mu\nu}=\mathrm{diag}(1,-a^2,-a^2,-a^2)\) is not visible on the board frame; it is a standard completion from the spoken description.
- The board writes the gravitational term as \(\frac{mMG}{D}\); this is visually secure, but the cleaned note version should probably use \(\frac{GMm}{d}\).
- The exact sign bookkeeping around the constant and the introduction of \(-k\) is lecture-driven rather than rigorously normalized; preserve the final form \(\left(\frac{\dot a}{a}\right)^2=\frac{8\pi G}{3}\rho-\frac{k}{a^2}\) and avoid overcommitting to intermediate constants beyond the needed \(x^2\) scaling.
- The statement near 01:21:59 that the marginal-escape distance grows logarithmically should be flagged as unreliable for the final mathematical notes; the lecture’s actual solved cosmological critical solution is \(a(t)\propto t^{2/3}\).
- The late arbitrariness discussion mixes \(A\), \(m\), density, and fiducial box conventions in unstable notation; the safest mathematical invariant to emphasize is the density \(\rho=m_{\Box}/a^3\), with the warning that \(a\) and \(m_{\Box}\) depend on the grid convention separately.
- The lecture informally identifies the Newtonian \(k\)-term with spatial curvature only at the end and defers the full justification; this identification should be stated cautiously until the next lecture’s Einstein-equation treatment is available.