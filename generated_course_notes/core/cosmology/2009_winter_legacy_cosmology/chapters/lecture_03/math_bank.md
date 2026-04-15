# Math Bank
## Core Equations
- \(\frac{1}{2}\dot a^2\) [visible]
- \(-\frac{4\pi G}{3}a^2\rho\) [standard reconstruction]
- \(\frac{1}{2}\dot a^2-\frac{4\pi G}{3}a^2\rho=\text{const}\) [standard reconstruction]
- \(\dot a^2=\frac{8\pi G}{3}a^2\rho-k\) [transcript-backed]
- \(-\frac{k}{a^2}\) [visible]
- \(\left(\frac{\dot a}{a}\right)^2=\frac{8\pi G}{3}\rho-\frac{k}{a^2}\) [standard reconstruction]
- \(R_{00}-\frac{1}{2}g_{00}R\propto T_{00}\) [transcript-backed]
- \(\left(\frac{\dot a}{a}\right)^2+\frac{k}{a^2}\propto \rho\) [transcript-backed]
- \(\rho_m=\frac{M}{a^3}\) [transcript-backed]
- \(\left(\frac{\dot a}{a}\right)^2=\frac{8\pi G}{3}\frac{M}{a^3}\) [transcript-backed]
- \(a(t)=Ct^p\) [transcript-backed]
- \(\frac{\dot a}{a}=\frac{p}{t}\) [transcript-backed]
- \(p=\frac{2}{3}\) [transcript-backed]
- \(a(t)\propto t^{2/3}\) [transcript-backed]
- \(C^3=6\pi GM\) [transcript-backed]
- \(E_\gamma=h\nu=\hbar\omega\) [transcript-backed]
- \(\nu=\frac{c}{\lambda}\) [transcript-backed]
- \(E_\gamma=\frac{hc}{\lambda}\) [transcript-backed]
- \(\lambda\propto a\) [transcript-backed]
- \(E_\gamma\propto a^{-1}\) [transcript-backed]
- \(E_{\text{box}}\propto a^{-1}\) [transcript-backed]
- \(\rho_r\propto a^{-4}\) [transcript-backed]
- \(\left(\frac{\dot a}{a}\right)^2=\frac{8\pi G}{3}\frac{M_r}{a^4}\) [standard reconstruction]
- \(p=\frac{1}{2}\) [transcript-backed]
- \(a(t)\propto t^{1/2}\) [transcript-backed]
- \(C^4=\frac{32\pi G}{3}M_r\) [transcript-backed]
- \(\rho_m\propto a^{-3}\) [transcript-backed]
- \(\rho_r\propto a^{-4}\) [transcript-backed]
- \(T\propto a^{-1}\) [transcript-backed]
- \(\frac{a_{\text{today}}}{a_{\text{ion}}}\sim 10^3\) [transcript-backed]
- \(\left(\frac{t_{\text{today}}}{t_{\text{ion}}}\right)^{2/3}\sim 10^3\) [transcript-backed]
- \(\frac{t_{\text{today}}}{t_{\text{ion}}}\sim 1000^{3/2}\sim 3\times 10^4\) [transcript-backed]
- \(t_{\text{ion}}\sim 3\times 10^5\ \text{yr}\) [transcript-backed]
- \(n_\gamma\propto T^3\) [transcript-backed]
- \(\rho_\gamma\propto T^4\) [transcript-backed]
- \(\frac{v^2}{r}=\frac{GM}{r^2}\) [transcript-backed]
- \(v(r)=\sqrt{\frac{GM}{r}}\) [transcript-backed]
- \(\frac{v^2}{r}=\frac{GM(r)}{r^2}\) [transcript-backed]
- \(v\approx \text{const}\Rightarrow M(r)\propto r\) [transcript-backed]
- \(M(R)\propto \int_0^R \rho(r)\,4\pi r^2\,dr\) [transcript-backed]
- \(M(R)\propto R\Rightarrow \rho(r)\propto r^{-2}\) [transcript-backed]
- \(M_{\text{galaxy}}\sim (7\text{ to }10)\,M_{\text{luminous}}\) [transcript-backed]

## Definitions And Objects
- \(x\): comoving coordinate.
- \(x=0\): our location, chosen only as a coordinate center.
- \(x=1\): chosen representative comoving galaxy or test particle.
- \(a(t)\): scale factor; physical distance to the particle at \(x=1\); distance to \(x=n\) is \(na(t)\).
- Dot notation: time derivative with respect to cosmic time \(t\).
- \(\rho\): energy density in the comoving frame; for matter at rest this is also the rest-mass density.
- \(M_{\rm enc}\): mass enclosed inside the sphere of physical radius \(a(t)\), \(M_{\rm enc}=\frac{4\pi}{3}a^3\rho\).
- \(M\): constant mass-energy content of a comoving unit cube in the matter-dominated case; not the mass of the test particle.
- \(M_r\): constant setting the radiation energy density scale in the radiation-dominated case; replaces the lecture’s recycled spoken \(m\).
- \(k\): curvature / integration constant in the cleaned Friedmann form; observationally very close to zero in the lecture.
- \(H\): Hubble parameter, \(H=\dot a/a\).
- Matter-dominated universe: energy density dominated by particles at rest in the comoving box; pressure taken as approximately zero.
- Radiation-dominated universe: energy density dominated by relativistic quanta, chiefly photons.
- \(\gamma\): photon symbol used verbally by Susskind.
- \(\nu\): photon frequency.
- \(\lambda\): photon wavelength.
- \(T\): radiation temperature; treated lecture-level as proportional to average photon energy.
- Ionizing temperature: lecture estimate \(T_{\rm ion}\sim 3000\,\mathrm K\).
- Surface of last scattering: fuzzy transition region where the plasma recombines and photons begin to free-stream.
- \(r\): galactic orbital radius in the dark-matter section.
- \(M(r)\): mass enclosed within a sphere of radius \(r\) in the galactic halo discussion.
- \(\rho(r)\): radial mass density profile in the halo discussion.

## Derivation Steps
**Newtonian FRW recap**
1. Place a representative comoving particle at \(x=1\), so its physical distance from us is \(a(t)\).
2. Set the particle’s mass to unity to simplify the energy bookkeeping.
3. Write kinetic energy as \(\frac{1}{2}\dot a^2\).
4. Compute enclosed mass inside the sphere of radius \(a\): \(M_{\rm enc}=\frac{4\pi}{3}a^3\rho\).
5. Write potential energy as \(-GM_{\rm enc}/a\).
6. Simplify the potential term to \(-\frac{4\pi G}{3}a^2\rho\).
7. Set total energy equal to a constant.
8. Multiply by \(2\) and divide by \(a^2\).
9. Rewrite the result as the cleaned Friedmann equation.

**Matter-dominated density law**
1. Take a comoving unit cube.
2. Its physical side length is \(a(t)\).
3. Assume the total mass \(M\) inside that cube stays constant.
4. The cube volume is \(a^3\).
5. Therefore \(\rho_m=M/a^3\).

**Matter-dominated solution**
1. Ignore \(k/a^2\) as a good approximation.
2. Start from \(\left(\dot a/a\right)^2=\frac{8\pi G}{3}\frac{M}{a^3}\).
3. Try \(a(t)=Ct^p\).
4. Then \(\dot a/a=p/t\).
5. The left-hand side scales as \(t^{-2}\).
6. The right-hand side scales as \(t^{-3p}\).
7. Match exponents: \(3p=2\).
8. Conclude \(p=2/3\).
9. Hence \(a(t)\propto t^{2/3}\).
10. Match coefficients to get \(C^3=6\pi GM\).

**Radiation density law**
1. Start from photon energy \(E_\gamma=h\nu=hc/\lambda\).
2. Assume photon wavelength stretches with the expansion: \(\lambda\propto a\).
3. Conclude \(E_\gamma\propto a^{-1}\).
4. Take a comoving unit box.
5. Assume the average number of photons in the box stays fixed.
6. Then total photon energy in the box scales as \(a^{-1}\).
7. Divide by the box volume \(a^3\).
8. Conclude \(\rho_r\propto a^{-4}\).

**Radiation-dominated solution**
1. Replace \(M/a^3\) by \(M_r/a^4\) in the Friedmann equation.
2. Again try \(a(t)=Ct^p\).
3. Then \(\dot a/a=p/t\), so the left-hand side scales as \(t^{-2}\).
4. The right-hand side scales as \(t^{-4p}\).
5. Match exponents: \(4p=2\).
6. Conclude \(p=1/2\).
7. Hence \(a(t)\propto t^{1/2}\).
8. Match coefficients to get \(C^4=\frac{32\pi G}{3}M_r\).

**Matter-radiation comparison**
1. Plot \(\rho_m\sim a^{-3}\) and \(\rho_r\sim a^{-4}\) against \(a\).
2. At small \(a\), \(\rho_r\) lies above \(\rho_m\).
3. At large \(a\), \(\rho_m\) lies above \(\rho_r\).
4. Therefore the early universe is radiation-dominated and the later universe matter-dominated.
5. Plot \(a\sim t^{1/2}\) and \(a\sim t^{2/3}\) against \(t\).
6. The real history interpolates continuously between them over a transition region.

**Ionization-time estimate**
1. Use \(T\propto 1/a\).
2. Take \(T_{\rm today}\sim 3\,\mathrm K\) and \(T_{\rm ion}\sim 3000\,\mathrm K\).
3. Infer \(a_{\rm today}/a_{\rm ion}\sim 10^3\).
4. Assume the universe is matter-dominated between ionization and today.
5. Use \(a\propto t^{2/3}\).
6. Write \(\left(t_{\rm today}/t_{\rm ion}\right)^{2/3}\sim 10^3\).
7. Raise both sides to the \(3/2\) power.
8. Get \(t_{\rm today}/t_{\rm ion}\sim 3\times 10^4\).
9. Insert \(t_{\rm today}\sim 10^{10}\) years.
10. Conclude \(t_{\rm ion}\sim 3\times 10^5\) years.

**Blackbody scaling used in Q&A**
1. Treat temperature as proportional to the average photon energy.
2. Use average photon energy \(\sim T\).
3. Use photon number density \(\sim T^3\).
4. Multiply them to get radiation energy density \(\sim T^4\).

**Galactic rotation curve inference**
1. Start from Newton’s law for a circular orbit: \(F=ma\).
2. Use gravitational force \(GMm/r^2\).
3. Use centripetal acceleration \(v^2/r\).
4. Cancel the orbiting mass \(m\).
5. Get \(v=\sqrt{GM/r}\) for centrally concentrated mass.
6. Compare with observed galactic rotation curves, which are roughly flat.
7. Replace \(M\) by the enclosed mass \(M(r)\).
8. Write \(v^2/r=GM(r)/r^2\).
9. With \(v\approx\) constant, conclude \(M(r)\propto r\).
10. Impose spherical symmetry: \(M(R)\propto \int_0^R \rho(r)\,r^2dr\).
11. Differentiate with respect to \(R\).
12. Infer \(\rho(r)\propto r^{-2}\).

## Notation Choices
- Use \(a(t)\) uniformly for the scale factor; do not preserve transcript alternation between `A`, `a`, and ASR mistakes.
- Use \(G\) uniformly for Newton’s constant; do not preserve spoken/transcribed `g`.
- Use dot notation only for derivatives with respect to cosmic time \(t\).
- Use \(H=\dot a/a\) when convenient, but keep the full ratio visible in derivations because that is how Susskind speaks it through.
- Use \(\rho\) as energy density throughout; add “for nonrelativistic matter at rest, this is also rest-mass density” when needed.
- Use \(\rho_m\) and \(\rho_r\) only when comparing matter and radiation explicitly.
- Use \(M\) for the constant matter content of the comoving cube.
- Rename the radiation constant to \(M_r\) in the notes; the lecture reuses \(m\) with different units.
- Use \(k\) only in the cleaned Friedmann normalization after the multiply-by-two step.
- If the pre-normalized Newtonian energy constant is mentioned, call it “an integration constant” rather than forcing the same \(k\).
- Use \(x\) for comoving coordinate in the cosmology setup.
- Use \(r\) only in the galactic dynamics section for orbital radius.
- Use \(M(r)\) for enclosed galactic mass and \(\rho(r)\) for halo density profile.
- Treat “matter-dominated” as “rest-energy dominated, pressure approximately zero in the comoving frame.”
- Treat “radiation-dominated” as “relativistic energy density dominated, with \(\rho_r\propto a^{-4}\).”

## Uncertain Mathematics
- The board only securely shows \(\frac12\dot a^2\) and part of the negative density term; the full Newtonian energy equation should be stated as a cleaned reconstruction from the transcript.
- The exact sign and normalization of the constant \(k\) in the first Newtonian energy equation are not visually secure; the lecture itself shifts normalization after multiplying by \(2\).
- The full Einstein-equation coefficient structure is not secure from either the frame or the transcript; keep \(R_{00}-\frac12 g_{00}R \propto T_{00}\) schematic.
- The radiation segment around 00:28 to 00:31 is ASR-corrupted: `1 over 8` should be read as `1 over a`, and the spoken constant \(m\) is not matter mass in the earlier sense.
- The step “average number of photons in a comoving box stays fixed” is a lecture-level assumption in this derivation; do not overformalize it as a rigorous kinetic-theory proof.
- The matter-radiation equality time near \(10^4\) years is a lecture estimate, not a precision cosmological parameter.
- The recombination / ionization time near \(3\times 10^5\) years is an order-of-magnitude classroom estimate, built from rounded numbers.
- The statement \(T\propto 1/a\) is used at lecture level; no full thermodynamic derivation is given.
- The blackbody relations \(n_\gamma\propto T^3\) and \(\rho_\gamma\propto T^4\) appear in the Q&A but are not derived from Planck’s law in the lecture.
- The halo profile \(\rho(r)\propto r^{-2}\) is an inference from flat rotation curves under spherical symmetry; Susskind explicitly does not claim a deeper first-principles derivation of that profile.
- The rough mass ratio \(M_{\text{galaxy}}\sim 7\) to \(10\) times luminous mass is heuristic in the lecture and should not be sharpened.
- Spoken percentages for dark matter, dark energy, and luminous matter are muddled in the transcript and should not be elevated into a polished quantitative summary without outside course support.