# Math Bank
## Core Equations
- \(d\tau^2 = dt^2 - dx^2 - dy^2 - dz^2\) [standard reconstruction]
- \(d\tau^2 = dt^2 - a^2(t)\bigl(dx^2+dy^2+dz^2\bigr)\) [transcript-backed]
- \(d = a(t)\,\Delta x\) [transcript-backed]
- \(v = \dfrac{dd}{dt} = \dot a\,\Delta x = \dfrac{\dot a}{a}\,d\) [transcript-backed]
- \(H(t)=\dfrac{\dot a}{a}\) [transcript-backed]
- \(d\tau=0\) along a light ray [transcript-backed]
- For motion along the \(x\)-axis, \(dt=a(t)\,dx\) [transcript-backed]
- For motion along the \(x\)-axis, \(\dfrac{dx}{dt}=\dfrac{1}{a(t)}\) [transcript-backed]
- \(R=xa\) [visible]
- \(v=x\dot a\) [visible]
- \(E=\tfrac12 m v^2-\dfrac{GMm}{R}\) [standard reconstruction]
- Zero-energy case: \(\tfrac12 m v^2=\dfrac{GMm}{R}\) [standard reconstruction]
- \(M=\dfrac{4\pi}{3}\rho R^3\) [transcript-backed]
- \(\tfrac12 v^2=\dfrac{G}{R}\left(\dfrac{4\pi}{3}\rho R^3\right)\) [visible]
- \(\tfrac12 H^2=\dfrac{4\pi G}{3}\rho\) [standard reconstruction]
- \(H^2=\dfrac{8\pi G}{3}\rho\) [standard reconstruction]
- \(\left(\dfrac{\dot a}{a}\right)^2=\dfrac{8\pi G}{3}\rho(t)\) [standard reconstruction]
- \(\rho=\dfrac{M}{(\Delta x\,a)^3}\) [visible]
- \(\rho_{\text{today}}=\dfrac{C}{a_{\text{today}}^3}\) [visible]
- \(\rho(t)=\dfrac{C}{a^3(t)}\) [transcript-backed]
- \(\dfrac{\rho(t)}{\rho_{\text{today}}}=\dfrac{a_{\text{today}}^3}{a^3(t)}\) [transcript-backed]
- Matter dilution: \(\rho_{\mathrm m}\propto a^{-3}\) [transcript-backed]
- Matter-era equation: \(\left(\dfrac{\dot a}{a}\right)^2=\dfrac{C}{a^3}\) [transcript-backed]
- Equivalent form: \(\dot a^2=\dfrac{C}{a}\) [transcript-backed]
- Integrated form: \(a^{3/2}\propto t\) [transcript-backed]
- Matter-era solution: \(a(t)\propto t^{2/3}\) [transcript-backed]
- Matter-era Hubble law: \(H(t)=\dfrac{2}{3t}\) [transcript-backed]
- Photon energy: \(E=h\nu\) [transcript-backed]
- With \(\nu\propto 1/\lambda\), \(E\propto 1/\lambda\) [transcript-backed]
- Photon redshift scaling: \(E_\gamma\propto a^{-1}\) [transcript-backed]
- Radiation dilution: \(\rho_{\mathrm{rad}}\propto a^{-4}\) [transcript-backed]
- Radiation-era solution: \(a(t)\propto t^{1/2}\) [transcript-backed]
- Vacuum-energy law: \(\rho_{\mathrm{vac}}=\text{const}\) [transcript-backed]
- Vacuum-energy equation: \(\dfrac{\dot a}{a}=\sqrt{\dfrac{8\pi G}{3}\rho_{\mathrm{vac}}}\) [standard reconstruction]
- Vacuum-energy solution: \(a(t)\propto e^{Ht}\) [transcript-backed]
- Curvature-energy correspondence: \(E>0 \leftrightarrow k<0\), \(E=0 \leftrightarrow k=0\), \(E<0 \leftrightarrow k>0\) [transcript-backed]

## Definitions And Objects
- \(a(t)\): scale factor; physical length associated with one unit of co-moving coordinate separation.
- \(x,y,z\): co-moving coordinate labels; dimensionless in the lecture’s preferred convention.
- \(\Delta x\): co-moving separation between two points or between opposite sides of a tracked box.
- \(d\): physical distance between two co-moving points, used before the Newtonian sphere section.
- \(R\): physical radius from us to a chosen galaxy in the Newtonian cosmology argument.
- \(v\): recession speed of that galaxy relative to us.
- \(H(t)\): Hubble parameter, called “Hubble constant” in the lecture even though it varies with time.
- \(m\): mass of the single distant galaxy or projectile being followed.
- \(M\): total enclosed mass inside the sphere of radius \(R\).
- \(\rho(t)\): density of matter or, more broadly in units \(c=1\), energy density.
- \(\rho_{\text{today}}\): present-day density used to normalize the matter-dilution law.
- \(C\): normalization constant in \(\rho(t)=C/a^3(t)\); lecture uses a generic constant loosely.
- \(d\tau\): proper time element; null motion is characterized by \(d\tau=0\).
- “Matter-dominated”: regime with \(\rho\propto a^{-3}\).
- “Radiation-dominated”: regime with \(\rho\propto a^{-4}\).
- “Vacuum energy”: energy density that does not dilute as the universe expands.

## Derivation Steps
Hubble law
1. Start from the physical distance \(d=a\,\Delta x\).
2. Hold \(\Delta x\) fixed because galaxies are fixed in co-moving coordinates.
3. Differentiate with respect to \(t\): \(v=\dot a\,\Delta x\).
4. Multiply and divide by \(a\) to replace \(\Delta x\) by the physical distance \(d\).
5. Obtain \(v=(\dot a/a)\,d\).
6. Read off \(H(t)=\dot a/a\).

Light propagation in the expanding metric
1. Use the flat expanding metric with \(dy=dz=0\).
2. Impose the null condition \(d\tau=0\).
3. Set \(dt^2=a^2(t)\,dx^2\).
4. For motion along the positive \(x\)-direction, write \(dt=a(t)\,dx\).
5. Divide by \(dt\) to get \(dx/dt=1/a(t)\).
6. Interpret this as a coordinate effect, not a change in the local physical speed of light.

Newtonian cosmology to flat Friedmann form
1. Choose a sphere centered on us and a galaxy on its boundary.
2. Use the shell theorem: only the enclosed mass contributes to the net gravitational force.
3. Write \(R=xa\) and \(v=x\dot a\).
4. Write the energy of the chosen galaxy: \(E=\tfrac12 mv^2-\dfrac{GMm}{R}\).
5. Specialize to the zero-energy case.
6. Divide out the projectile mass \(m\).
7. Replace the enclosed mass by \(M=\dfrac{4\pi}{3}\rho R^3\).
8. Obtain \(\tfrac12 v^2=\dfrac{G}{R}\left(\dfrac{4\pi}{3}\rho R^3\right)\).
9. Use \(v=HR\).
10. Cancel the common factor of \(R^2\).
11. Get \(H^2=\dfrac{8\pi G}{3}\rho\).

Matter dilution
1. Track a co-moving box with fixed \(\Delta x,\Delta y,\Delta z\).
2. Let the number of particles in the box remain fixed.
3. Write the physical volume as proportional to \(a^3\).
4. Divide fixed total mass by growing volume.
5. Conclude \(\rho_{\mathrm m}\propto a^{-3}\).
6. Normalize with today’s values to get \(\rho(t)=\rho_{\text{today}}\dfrac{a_{\text{today}}^3}{a^3(t)}\).

Matter-era expansion law
1. Insert \(\rho=C/a^3\) into \(\left(\dot a/a\right)^2=\dfrac{8\pi G}{3}\rho\).
2. Absorb time-independent factors into one constant \(C\).
3. Rewrite as \(\dot a^2=C/a\).
4. Multiply by \(a\) and take a square root to get \(\sqrt a\,\dot a=\text{const}\).
5. Integrate with respect to time.
6. Obtain \(a^{3/2}\propto t\).
7. Conclude \(a(t)\propto t^{2/3}\).
8. Differentiate and divide by \(a\) to get \(H(t)=2/(3t)\).

Radiation scaling and radiation-era law
1. Keep the number of photons in a co-moving box fixed.
2. Let the box size scale like \(a\), so each wavelength scales like \(a\).
3. Use \(E_\gamma\propto 1/\lambda\) to get \(E_\gamma\propto 1/a\).
4. Combine photon-number dilution \(a^{-3}\) with single-photon redshift \(a^{-1}\).
5. Get \(\rho_{\mathrm{rad}}\propto a^{-4}\).
6. Repeat the matter-era differential-equation analysis with \(a^{-4}\) instead of \(a^{-3}\).
7. Conclude \(a(t)\propto t^{1/2}\).

Vacuum-energy expansion law
1. Take \(\rho_{\mathrm{vac}}=\text{const}\).
2. Insert it into \(\left(\dot a/a\right)^2=\dfrac{8\pi G}{3}\rho\).
3. Take the square root: \(\dot a/a=\text{const}\).
4. Rewrite as \(\dot a=(\text{const})\,a\).
5. Solve the first-order differential equation.
6. Conclude \(a(t)\propto e^{Ht}\).

## Notation Choices
- Use \(a(t)\) throughout for the scale factor; do not switch to \(A(t)\) even though the transcript sometimes says “A.”
- Use \(x\) for co-moving position and \(R\) for physical radius in the Newtonian section; do not reuse \(R\) for curvature radius.
- Use \(d=a\,\Delta x\) before the sphere argument, then switch to \(R=xa\) when the lecture narrows to one chosen galaxy.
- Use overdots for derivatives with respect to cosmological time \(t\): \(\dot a=da/dt\).
- Use \(H(t)=\dot a/a\), but note that Susskind verbally says “Hubble constant.”
- Use \(m\) for the test galaxy and \(M\) for enclosed mass; preserve this distinction.
- Use \(\rho\) as density generically, with the lecture’s convention that in units \(c=1\) mass density and energy density may be identified.
- Use \(d\tau\) for proper time and null motion; if the final notes prefer \(ds^2\) for the metric, keep \(d\tau=0\) when discussing light rays.
- Keep \(\rho_{\text{today}}\) and \(a_{\text{today}}\) rather than converting immediately to \(\rho_0\) and \(a_0\), since that is closer to the board and transcript.
- Treat generic constants carefully: the lecture reuses “constant” and \(c/C\) loosely, so the final notes should define each constant locally if it survives beyond one displayed step.

## Uncertain Mathematics
- The early Minkowski-space formula is motivated clearly but the transcript is garbled in places; the final notes should write the standard clean metric without pretending every sign was perfectly legible from the raw transcript.
- In `lecture_09_figure_02.png`, the full right-hand sides of \(R=\cdots\) and \(V=\cdots\) are only partially visible; the final equations should be normalized from the transcript.
- In `lecture_09_figure_03.png`, the board writes the right-hand side as a running product; the parenthesized enclosed-mass factor is a mathematically safe reconstruction.
- In `lecture_09_figure_05.png`, the lower numerical coefficient is not secure from the frame alone; use the derivation, not the screenshot, to justify \(H^2=\dfrac{8\pi G}{3}\rho\).
- The lecture’s live algebra for the matter-era power law contains a false start; the final notes should present the corrected derivation cleanly, while perhaps mentioning that the argument was checked and repaired on the fly.
- The radiation case is motivated physically and its final scaling/result are stated, but the full intermediate ODE solution is not unfolded on the board in the same detail as the matter case; keep any written derivation short and clearly patterned on the earlier matter derivation.
- The vacuum-energy step is also presented in a compressed way; writing \(\dot a/a=\sqrt{8\pi G\rho_{\mathrm{vac}}/3}\) is a clean reconstruction of what the lecture is using.
- The correspondence between total-energy sign and curvature sign is explicitly attributed by Susskind to Einstein’s equations, not to the Newtonian derivation; the final notes should preserve that boundary.
- The late energy-conservation discussion is heuristic cosmological bookkeeping, not a precise theorem about globally conserved energy in arbitrary spacetimes.