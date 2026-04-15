# Math Bank
## Core Equations
- \(d_{AB}=a(t)\,\Delta x_{AB}\). [transcript-backed]
- \(d_{AB}=a(t)\sqrt{(\Delta x)^2+(\Delta y)^2+(\Delta z)^2}\). [transcript-backed]
- \(v_{AB}=\dot a(t)\,\Delta x_{AB}\). [transcript-backed]
- \(\dfrac{v_{AB}}{d_{AB}}=\dfrac{\dot a}{a}\equiv H(t)\). [transcript-backed]
- \(v_{AB}=H(t)\,d_{AB}\). [transcript-backed]
- \(m_{\text{cell}}=\nu\,\Delta x\,\Delta y\,\Delta z\). [transcript-backed]
- \(V_{\text{cell}}=a^3\,\Delta x\,\Delta y\,\Delta z\). [transcript-backed]
- \(\rho=\dfrac{\nu}{a^3}\). [visible]
- \(R=\sqrt{x^2+y^2+z^2}\), \(\; d=a(t)R\). [transcript-backed]
- \(v=\dot a(t)R\), \(\;\ddot d=\ddot a(t)R\). [transcript-backed]
- \(\ddot x=-\dfrac{GM}{x^2}\). [visible]
- \(V_{\text{sphere}}=\dfrac{4\pi}{3}d^3=\dfrac{4\pi}{3}a^3R^3\). [visible]
- \(M=\dfrac{4\pi}{3}\rho\,d^3\). [standard reconstruction]
- \(M=\dfrac{4\pi}{3}\nu R^3\) for a fixed comoving sphere. [standard reconstruction]
- \(\ddot a(t)R=-\dfrac{GM}{d^2}\). [transcript-backed]
- \(\dfrac{\ddot a}{a}=-\dfrac{4\pi G}{3}\rho\). [visible]
- \(\dfrac{\ddot a}{a}=-\dfrac{4\pi G\nu}{3a^3}\). [visible]
- A static matter-filled universe requires \(\rho=0\); otherwise \(\ddot a\neq 0\). [transcript-backed]
- \(E=\dfrac12 mv^2-\dfrac{GMm}{x}\). [transcript-backed]
- \(E=0\;\Rightarrow\;\dfrac12 v^2=\dfrac{GM}{x}\). [transcript-backed]
- \(v_{\mathrm{esc}}^2=\dfrac{2GM}{x}\). [transcript-backed]
- \(E=\dfrac12 m\dot a^{\,2}R^2-\dfrac{GMm}{aR}\). [standard reconstruction]
- \(\left(\dfrac{\dot a}{a}\right)^2=\dfrac{8\pi G}{3}\rho\). [transcript-backed]
- \(\left(\dfrac{\dot a}{a}\right)^2=\dfrac{8\pi G\nu}{3a^3}\). [visible]
- \(\left(\dfrac{\dot a}{a}\right)^2=\dfrac{1}{a^3}\). [visible]
- \(a(t)=Ct^p\). [transcript-backed]
- \(\dot a=Cp\,t^{p-1}\). [transcript-backed]
- \(\dfrac{\dot a}{a}=\dfrac{p}{t}\). [transcript-backed]
- \(\dfrac{1}{a^3}=\dfrac{1}{C^3 t^{3p}}\). [transcript-backed]
- \(3p=2\). [transcript-backed]
- \(p^2=\dfrac{1}{C^3}\) in the normalized form \(\left(\dfrac{\dot a}{a}\right)^2=\dfrac{1}{a^3}\). [transcript-backed]
- \(a(t)\propto t^{2/3}\). [transcript-backed]

## Definitions And Objects
- Isotropy: same in every direction after averaging over large enough patches of sky. 
- Homogeneity: same from place to place on sufficiently large scales.
- Cosmological principle: the universe is approximately homogeneous and isotropic on large scales.
- Comoving coordinates \(x,y,z\): grid labels attached to galaxies; not physical lengths.
- Coordinate separations \(\Delta x,\Delta y,\Delta z\): fixed for galaxies frozen into the grid.
- Scale factor \(a(t)\): converts coordinate separations into physical distances.
- Hubble parameter \(H(t)\): \(H(t)=\dot a/a\); independent of position, dependent on time.
- \(\nu\): mass per unit coordinate volume; constant when matter moves with the grid.
- \(\rho\): physical mass density; mass per physical volume.
- \(R\): fixed comoving radial label of a representative galaxy from the chosen origin.
- \(d\): physical radial distance of that galaxy, \(d=aR\).
- \(M\): enclosed gravitating mass inside the sphere of radius \(d\).
- \(m\): test mass, either the Earth-problem particle or the representative galaxy.
- \(x\) in the Earth analogy: radial distance from the Earth; not the comoving \(x\)-coordinate.
- \(E\): conserved Newtonian total energy.
- Critical / zero-energy case: the escape-velocity threshold separating turnaround from no turnaround.

## Derivation Steps
Comoving kinematics
1. Attach the coordinate grid to galaxies so their coordinate positions stay fixed.
2. Postulate that physical separations are one common scale factor times coordinate separations.
3. Differentiate the physical distance with respect to time.
4. Use the fact that \(\Delta x_{AB}\), \(\Delta y_{AB}\), \(\Delta z_{AB}\) are fixed in comoving coordinates.
5. Divide velocity by distance so the coordinate separation cancels.
6. Identify the common ratio as \(H(t)=\dot a/a\).

Density dilution
1. Take a coordinate cell of size \(\Delta x\,\Delta y\,\Delta z\).
2. Put mass \(\nu\,\Delta x\,\Delta y\,\Delta z\) in that cell.
3. Convert each coordinate edge into a physical edge by multiplying by \(a(t)\).
4. Obtain the physical cell volume \(a^3\Delta x\,\Delta y\,\Delta z\).
5. Divide mass by physical volume.
6. Get \(\rho=\nu/a^3\).

Newtonian acceleration equation
1. Choose an origin and look at one representative galaxy at fixed comoving radius \(R\).
2. Write its physical distance as \(d=aR\).
3. Differentiate once and twice to get velocity \(\dot a R\) and acceleration \(\ddot a R\).
4. Use Newton’s theorem: only the mass inside the sphere of radius \(d\) contributes.
5. Write the enclosed mass as \(M=\frac{4\pi}{3}\rho d^3\).
6. Write the inward gravitational acceleration as \(-GM/d^2\).
7. Set \(\ddot a R=-GM/d^2\).
8. Substitute \(d=aR\) and \(M=\frac{4\pi}{3}\rho d^3\).
9. Cancel \(R\).
10. Obtain \(\ddot a/a=-4\pi G\rho/3\).

Density-substituted acceleration equation
1. Start from \(\ddot a/a=-4\pi G\rho/3\).
2. Substitute \(\rho=\nu/a^3\).
3. Obtain \(\ddot a/a=-4\pi G\nu/(3a^3)\).

Earth escape-velocity criterion
1. Write the conserved Newtonian energy \(E=\frac12 mv^2-\frac{GMm}{x}\).
2. Specialize to the threshold case \(E=0\).
3. Cancel the test mass \(m\).
4. Solve \(\frac12 v^2=\frac{GM}{x}\).
5. Multiply by \(2\).
6. Obtain \(v_{\mathrm{esc}}^2=2GM/x\).

Zero-energy Friedmann equation
1. Write the cosmological energy of a representative galaxy as \(E=\frac12 m\dot a^{\,2}R^2-\frac{GMm}{aR}\).
2. Set \(E=0\) for the critical case.
3. Cancel the test mass \(m\).
4. Rearrange so that \(a^3R^3\) appears in a denominator.
5. Multiply by \(\frac{4\pi}{3}\) on both sides to convert \(a^3R^3\) into a sphere volume.
6. Recognize \(M/\text{volume}=\rho\).
7. Move the kinetic term to the left.
8. Obtain \(\left(\dot a/a\right)^2=8\pi G\rho/3\).

Matter-dominated form
1. Start from \(\left(\dot a/a\right)^2=8\pi G\rho/3\).
2. Substitute \(\rho=\nu/a^3\).
3. Obtain \(\left(\dot a/a\right)^2=8\pi G\nu/(3a^3)\).
4. Absorb the positive constant \(8\pi G\nu/3\) by normalization if desired.
5. Use the simplified working form \(\left(\dot a/a\right)^2=1/a^3\).

Power-law solution
1. Try \(a(t)=Ct^p\).
2. Differentiate to get \(\dot a=Cp\,t^{p-1}\).
3. Divide by \(a\) to get \(\dot a/a=p/t\).
4. Square to get \((\dot a/a)^2=p^2/t^2\).
5. Compute \(1/a^3=1/(C^3 t^{3p})\).
6. Match time powers: \(2=3p\).
7. Conclude \(p=2/3\).
8. Match coefficients in the normalized equation: \(p^2=1/C^3\).
9. Conclude \(a(t)\propto t^{2/3}\).

## Notation Choices
- Use \(a(t)\) throughout, not uppercase \(A\), even when the transcript drifts.
- Use overdots for time derivatives: \(\dot a=\frac{da}{dt}\), \(\ddot a=\frac{d^2a}{dt^2}\).
- Use \(H(t)=\dot a/a\) and call it the Hubble parameter in expository prose; mention “Hubble constant” only when reflecting the lecture’s spoken terminology.
- Use \(\nu\) for mass per unit coordinate volume; do not replace it with Latin \(v\).
- Use \(\rho\) for physical mass density.
- Use \(R\) for a fixed comoving radial label in the Newtonian cosmology part.
- Use \(d=aR\) for the corresponding physical distance from the chosen origin.
- Use \(\Delta x_{AB}\), \(\Delta y_{AB}\), \(\Delta z_{AB}\) for coordinate separations between galaxies.
- Use \(x\) only after the Earth-projectile pivot, where it denotes radial distance from the Earth.
- Use \(M\) for enclosed source mass and \(m\) for the test particle / representative galaxy.
- Keep the Newtonian sign convention: inward gravitational force or acceleration is negative.
- Print the zero-energy Friedmann equation as \(\left(\dot a/a\right)^2\), not as \(\dot a/a^2\); the lecture transcript is verbally rough here but the intended structure is the square of the Hubble parameter.
- Distinguish clearly between coordinate volume \(\Delta x\,\Delta y\,\Delta z\) and physical volume \(a^3\Delta x\,\Delta y\,\Delta z\).

## Uncertain Mathematics
- The full cosmological energy formula is not fully legible on the board in `lecture_01_figure_05.png`; only the kinetic term and the numerator \(-mMG\) are clearly visible. The denominator \(aR\) should be presented as transcript-backed reconstruction.
- The partially visible force relation in `lecture_01_figure_04.png` has an ambiguous distance symbol, visually close to \(D\) or \(d\); do not preserve that symbol as authoritative.
- The transcript around the zero-energy Friedmann derivation is verbally rough: phrases like “a dot over a squared” should be normalized to \(\left(\dot a/a\right)^2\), because the board and the algebra require parentheses.
- The upper derivation line in `lecture_01_figure_03.png` is cropped; do not reconstruct intermediate algebra from the screenshot alone.
- The constant-matching relation \(p^2=1/C^3\) holds only after the lecture’s normalization that sets the prefactor \(8\pi G\nu/3\) to \(1\); before normalization the coefficient relation is \(p^2=(8\pi G\nu/3)/C^3\).
- The nonzero-energy extension of the Friedmann equation is only verbally previewed in this lecture. Its explicit extra term should not be stated as though it were derived here unless it is clearly marked as a cautious forward reconstruction from subsequent material.
- The transcript’s Earth-analogy force equation is slightly garbled in spots; the clean form \(\ddot x=-GM/x^2\) is supported by both the lecture logic and the visible board.