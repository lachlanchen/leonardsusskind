# Math Bank
## Core Equations
- \(E=\hbar\omega,\qquad p=\hbar k\) [transcript-backed]
- \(\omega=ck\) for a massless wave in empty space [transcript-backed]
- \(E^2=c^2p^2+m^2c^4\), hence in \(c=1\) units \(E^2-p^2=m^2\) [transcript-backed]
- \(\phi=\phi_R+i\phi_I\) [transcript-backed]
- \(\phi^*=\phi_R-i\phi_I\) [visible]
- \(\phi=\rho e^{i\alpha},\qquad \phi^*=\rho e^{-i\alpha}\) [transcript-backed]
- \(\phi^*\phi=\rho^2=\phi_R^2+\phi_I^2\) [transcript-backed]
- \(\partial_\mu\phi^*\,\partial^\mu\phi=\partial_\mu\phi_R\,\partial^\mu\phi_R+\partial_\mu\phi_I\,\partial^\mu\phi_I\) [transcript-backed]
- \(\partial_\mu\phi^*\,\partial^\mu\phi=\partial_\mu\rho\,\partial^\mu\rho+\rho^2\,\partial_\mu\alpha\,\partial^\mu\alpha\) [standard reconstruction]
- \(V=V(\rho)\), equivalently \(V\) depends only on \(\phi^*\phi\) [transcript-backed]
- \(\rho=f+H\) [visible]
- \(\rho\approx f\ \Longrightarrow\ \mathcal L_{\text{Goldstone}}\approx f^2\,\partial_\mu\alpha\,\partial^\mu\alpha\) [transcript-backed]
- \(\beta=f\alpha\ \Longrightarrow\ \mathcal L_{\text{Goldstone}}\approx \partial_\mu\beta\,\partial^\mu\beta\) [transcript-backed]
- \(\phi'(x)=e^{i\theta(x)}\phi(x)\) [visible]
- \(\partial_\mu\phi'=e^{i\theta(x)}\big(\partial_\mu\phi+i(\partial_\mu\theta)\phi\big)\) [transcript-backed]
- \(\partial\phi^*\,\partial\phi\neq \partial\phi^{*\prime}\,\partial\phi'\) [standard reconstruction]
- \(D_\mu\phi=(\partial_\mu+iA_\mu)\phi,\qquad D_\mu\phi^*=(\partial_\mu-iA_\mu)\phi^*\) [transcript-backed]
- \(A'_\mu=A_\mu-\partial_\mu\theta\) [standard reconstruction]
- \(D'_\mu\phi'=e^{i\theta}D_\mu\phi,\qquad D'_\mu\phi^{*\prime}=e^{-i\theta}D_\mu\phi^*\) [standard reconstruction]
- \(F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu\) [transcript-backed]
- \(F'_{\mu\nu}=F_{\mu\nu}+\partial_\mu\partial_\nu\theta-\partial_\nu\partial_\mu\theta=F_{\mu\nu}\) [transcript-backed]
- \(\mathcal L=D_\mu\phi^*\,D^\mu\phi - V(\phi^*\phi) + F_{\mu\nu}F^{\mu\nu}\) [visible]
- \(A_\mu A^\mu\mapsto (A_\mu-\partial_\mu\theta)(A^\mu-\partial^\mu\theta)\neq A_\mu A^\mu\) [standard reconstruction]
- \(\phi\approx f e^{i\alpha}\) in the frozen-\(\rho\) limit [transcript-backed]
- \(D_\mu\phi\approx i f e^{i\alpha}\big(\partial_\mu\alpha + A_\mu\big)\) [standard reconstruction]
- \(|D_\mu\phi|^2\approx f^2\big(\partial_\mu\alpha + A_\mu\big)\big(\partial^\mu\alpha + A^\mu\big)\) [standard reconstruction]
- \(\theta=-\alpha\ \Longrightarrow\ \alpha'=0,\quad A'_\mu=A_\mu+\partial_\mu\alpha,\quad |D_\mu\phi|^2\to f^2A'_\mu A^{\mu\prime}\) [standard reconstruction]
- \(2\ \text{(photon pols)}+2\ \text{(real scalar components)}\to 3\ \text{(massive vector pols)}+1\ \text{(Higgs scalar)}\) [transcript-backed]

## Definitions And Objects
- \(k\): wave number, inverse wavelength up to \(2\pi\)-type convention.
- \(\omega\): frequency.
- Mass: the energy or frequency of the homogeneous \(k=0\) mode.
- Flat direction: a direction in field space along which the potential does not change, hence no restoring force and no mass.
- \(\phi\): complex scalar field.
- \(\phi_R,\phi_I\): real and imaginary components of \(\phi\).
- \(\rho,\alpha\): polar variables in field space; \(\rho\) is radial magnitude, \(\alpha\) is phase angle.
- \(H\): radial fluctuation around the broken minimum; the Higgs mode.
- \(f\): vacuum radius, the value of \(\rho\) at the minimum of the broken potential.
- Goldstone boson: the massless angular mode associated with broken continuous symmetry.
- \(U(1)\) symmetry: phase rotation of the charged field.
- Global \(U(1)\): same phase rotation everywhere in space-time.
- Local gauge transformation: space-time dependent phase rotation \(\theta(x)\).
- \(A_\mu\): compensating gauge field / vector potential.
- \(D_\mu\): covariant derivative replacing \(\partial_\mu\) in the gauge-invariant theory.
- \(F_{\mu\nu}\): field strength built from \(A_\mu\); gauge invariant for abelian \(U(1)\).

## Derivation Steps
Mass from dispersion relation
1. Start from \(E=\hbar\omega\) and \(p=\hbar k\).
2. For a massless excitation, \(\omega\to 0\) as \(k\to 0\).
3. For a massive excitation, \(E(k=0)=m\neq 0\).
4. Interpret \(k=0\) as a homogeneous shift of the whole field.
5. Conclude that mass is the oscillation frequency of the homogeneous mode.

Mass from potential curvature
1. Shift the field homogeneously away from equilibrium.
2. If the potential is curved there, the field oscillates back.
3. If the potential is flat there, the field does not respond.
4. Therefore curved direction \(\Rightarrow\) massive mode, flat direction \(\Rightarrow\) massless mode.

Complex scalar kinetic term in polar variables
1. Write \(\phi=\rho e^{i\alpha}\) and \(\phi^*=\rho e^{-i\alpha}\).
2. Differentiate both fields.
3. Multiply \(\partial_\mu\phi^*\) by \(\partial^\mu\phi\).
4. Cross terms cancel.
5. The kinetic term splits into radial and angular pieces: \((\partial\rho)^2+\rho^2(\partial\alpha)^2\).

Broken vacuum and low-energy limit
1. Choose a \(U(1)\)-symmetric potential minimized at \(\rho=f\).
2. Expand \(\rho=f+H\).
3. Treat \(H\) as heavy and freeze it at low energy: \(\rho\approx f\), \(\partial\rho\approx0\), \(V(\rho)\approx V(f)\).
4. The remaining dynamics are \(f^2(\partial\alpha)^2\).
5. Rescale \(\beta=f\alpha\) if canonical normalization is wanted.
6. Conclude that the Goldstone mode has derivative energy but no mass term.

Failure of local phase symmetry
1. Replace constant phase by \(\theta(x)\): \(\phi'=e^{i\theta(x)}\phi\).
2. Differentiate \(\phi'\).
3. An extra term proportional to \(\partial_\mu\theta\) appears.
4. Therefore the ordinary derivative term is not invariant.
5. This is the obstruction that motivates the gauge field.

Covariant derivative and gauge invariance
1. Define \(D_\mu\phi=(\partial_\mu+iA_\mu)\phi\).
2. Choose \(A'_\mu=A_\mu-\partial_\mu\theta\).
3. Compute \(D'_\mu\phi'\).
4. The \(\partial_\mu\theta\) terms cancel.
5. One gets \(D'_\mu\phi'=e^{i\theta}D_\mu\phi\).
6. Multiply by the conjugate to obtain gauge-invariant \(D_\mu\phi^*D^\mu\phi\).

Gauge invariance of \(F_{\mu\nu}\)
1. Define \(F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu\).
2. Transform \(A_\mu\to A_\mu-\partial_\mu\theta\).
3. The shifted \(F_{\mu\nu}\) picks up mixed second derivatives.
4. Commuting partial derivatives cancels them.
5. Therefore \(F_{\mu\nu}\) and \(F_{\mu\nu}F^{\mu\nu}\) are gauge invariant.

Higgs mechanism in the broken phase
1. Keep the scalar near the broken minimum: \(\phi\approx f e^{i\alpha}\).
2. Insert this into \(D_\mu\phi\).
3. The covariant derivative depends on \(\partial_\mu\alpha + A_\mu\).
4. Squaring gives \(f^2(\partial_\mu\alpha + A_\mu)^2\).
5. Choose gauge parameter \(\theta=-\alpha\).
6. The angular field is removed from the scalar.
7. The surviving term is \(f^2A_\mu A^\mu\), i.e. an effective vector mass term.
8. The Goldstone mode is reinterpreted as the longitudinal polarization of the now-massive vector boson.

## Notation Choices
- Use \(\phi_R,\phi_I\) for real and imaginary scalar components.
- Use \(\rho,\alpha\) for polar variables in field space.
- Use \(f\) for the radius of the broken minimum and \(H\) for the radial fluctuation.
- Use \(\theta(x)\) for the local gauge parameter.
- Restore Lorentz indices in the final chapter even when the board suppresses them: \(\partial\phi^*\,\partial\phi\) means \(\partial_\mu\phi^*\,\partial^\mu\phi\).
- Adopt one consistent abelian convention:
  \[
  \phi'=e^{i\theta(x)}\phi,\qquad
  D_\mu=\partial_\mu+iA_\mu,\qquad
  A'_\mu=A_\mu-\partial_\mu\theta.
  \]
- With that convention, the invariant broken-phase combination is \(\partial_\mu\alpha + A_\mu\).
- Write \(F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu\) explicitly.
- Keep \(F^2\) as lecture shorthand when referring to the board, but typeset \(F_{\mu\nu}F^{\mu\nu}\) in the actual derivation.
- If a gauge transformation is used to remove \(\alpha\), state the transformed field once and then drop the prime on \(A_\mu\) only after making the gauge choice explicit.

## Uncertain Mathematics
- The lecture flips sign conventions for \(D_\mu\) and \(A_\mu\to A'_\mu\pm\partial_\mu\theta\); the final notes must fix one convention and mention that the lecture wobbles.
- The board writes schematic \(F^2\) and \(D\phi^*D\phi\); exact index placement and normalization are not stable on the board.
- The lecture never commits to a specific quartic Higgs potential such as \(\lambda(\phi^*\phi-f^2)^2\); only the shape and the minimum at \(\rho=f\) are safe to preserve.
- The exact numerical coefficient of the induced photon mass is not reliable in the transcript; Susskind explicitly waves away factors of \(2\) and similar constants.
- The broken-phase covariant-derivative line in `lecture_08_figure_06.png` is incomplete; only the schematic dependence on \(\partial_\mu\alpha\) and \(A_\mu\) is safe.
- The statement around 00:15 that the Goldstone boson is eaten “resulting in giving the Higgs boson a mass” is a spoken slip; the later derivation supports gauge-boson mass plus the already-massive radial Higgs mode.
- The dispersion relation \(\omega^2=k^2+m^2\) is an inferred natural-units rewrite of the particle formula, not a line written verbatim on the board.
- The Cooper-pair discussion is garbled in the transcript; only the stable claim should be kept: superconductors realize the same abelian Higgs logic with a charged bosonic condensate.