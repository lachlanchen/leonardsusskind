# Math Bank
## Core Equations
- [transcript-backed] \(F=\dfrac{GMm}{r^2}\).
- [transcript-backed] \(d\tau^2=\left(1-\dfrac{2MG}{r}\right)dt^2-\left(1-\dfrac{2MG}{r}\right)^{-1}dr^2-r^2\,d\Omega^2\).
- [transcript-backed] As spoken, \(d\Omega^2=d\theta^2+\cos^2\theta\,d\phi^2\).
- [transcript-backed] For a static clock, \(dr=d\Omega=0\), so \(d\tau=\sqrt{1-\dfrac{2MG}{r}}\,dt\), and for \(r\gg 2MG\), \(d\tau\approx dt\).
- [transcript-backed] \(\mathcal F(r)=1-\dfrac{2MG}{r},\qquad \mathcal G(r)=\mathcal F(r)^{-1}\).
- [standard reconstruction] \(S=-m\int d\tau=-m\int dt\,\sqrt{\mathcal F(r)-\mathcal G(r)\dot r^{\,2}-r^2\dot\theta^{\,2}}\).
- [standard reconstruction] \(\mathcal L=-m\sqrt{\mathcal F(r)-\mathcal G(r)\dot r^{\,2}-r^2\dot\theta^{\,2}}\).
- [visible] \(p_q=\dfrac{\partial\mathcal L}{\partial\dot q}\).
- [transcript-backed] \(p_r=\dfrac{\partial\mathcal L}{\partial\dot r}=\dfrac{m\mathcal G(r)\dot r}{\sqrt{\mathcal F(r)-\mathcal G(r)\dot r^{\,2}-r^2\dot\theta^{\,2}}}\).
- [transcript-backed] \(L=\dfrac{\partial\mathcal L}{\partial\dot\theta}=\dfrac{mr^2\dot\theta}{\sqrt{\mathcal F(r)-\mathcal G(r)\dot r^{\,2}-r^2\dot\theta^{\,2}}}\).
- [visible] For \(\dot r=0\), \(\dfrac{L}{m}=\dfrac{r^2\dot\theta}{\sqrt{\mathcal F(r)-r^2\dot\theta^{\,2}}}=\lambda\).
- [standard reconstruction] For circular motion, \(\dot\theta^{\,2}=\dfrac{\lambda^2\mathcal F(r)}{r^2(r^2+\lambda^2)}\).
- [transcript-backed] \(E=H=\sum_i p_i\dot q_i-\mathcal L\).
- [transcript-backed] \(E=\dfrac{\mathcal F(r)m}{\sqrt{\mathcal F(r)-\mathcal G(r)\dot r^{\,2}-r^2\dot\theta^{\,2}}}\).
- [visible] For \(\dot r=0\), \(E=\dfrac{\mathcal F(r)m}{\sqrt{\mathcal F(r)-r^2\dot\theta^{\,2}}}\).
- [standard reconstruction] After eliminating \(\dot\theta\), \(E(r,\lambda)=m\,\dfrac{\sqrt{\mathcal F(r)}\sqrt{r^2\lambda^2+r^4}}{r^2}=m\,\dfrac{\sqrt{\mathcal F(r)}\sqrt{r^2+\lambda^2}}{r}\).
- [transcript-backed] Photon limit: \(m\to 0,\quad \lambda\to\infty,\quad L=m\lambda\ \text{fixed}\).
- [standard reconstruction] In that limit, \(E_\gamma(r;L)=L\,\dfrac{\sqrt{1-\frac{2MG}{r}}}{r}\).
- [standard reconstruction] Stationary-orbit condition: \(\dfrac{d}{dr}\left(\dfrac{\sqrt{1-\frac{2MG}{r}}}{r}\right)=0\).
- [transcript-backed] \(r_{\mathrm{ph}}=3MG\).
- [transcript-backed] Near the horizon, after setting \(2MG=1\) and suppressing angular directions, \(d\tau^2=\left(1-\dfrac1r\right)dt^2-\left(1-\dfrac1r\right)^{-1}dr^2\).
- [transcript-backed] With \(\xi=r-1\), the near-horizon form becomes \(d\tau^2=\xi\,dt^2-\dfrac{d\xi^2}{\xi}\).
- [transcript-backed] \(X=\rho\cosh\omega,\qquad T=\rho\sinh\omega,\qquad X^2-T^2=\rho^2\).
- [transcript-backed] In these coordinates, \(d\tau^2=\rho^2\,d\omega^2-d\rho^2\).
- [transcript-backed] Matching change of variables: \(\rho^2=4\xi,\qquad \omega=\dfrac{t}{2}\).

## Definitions And Objects
- The horizon is at \(r=2MG\); the lecture treats it as a coordinate singularity, not a curvature singularity.
- The singularity is at \(r=0\); here curvature and tidal forces diverge.
- Proper time \(\tau\) is the time measured by a moving clock.
- Coordinate time \(t\) is the Schwarzschild time coordinate used to describe the whole geometry.
- \(\mathcal F(r)\) is the Schwarzschild factor; \(\mathcal G(r)\) is its inverse.
- A circular orbit means \(\dot r=0\).
- \(p_q\) denotes the momentum conjugate to a coordinate \(q\).
- \(L\) is ordinary angular momentum.
- \(\lambda:=L/m\) is the reduced angular momentum used in the orbit calculation.
- \(E\) is the conserved Hamiltonian energy.
- The photon sphere is the radius \(r=3MG\), the unstable circular photon orbit.
- After the unit choice \(2MG=1\), \(\xi=r-1\) measures signed distance from the horizon.
- \((X,T)\) are flat-spacetime Minkowski-like coordinates; \((\rho,\omega)\) are the associated hyperbolic/Rindler coordinates.

## Derivation Steps
Metric to orbit Lagrangian
1. Start from the Schwarzschild line element.
2. Restrict to motion with one angular variable on an equatorial orbit.
3. Rename \(1-\dfrac{2MG}{r}\) as \(\mathcal F(r)\) and its inverse as \(\mathcal G(r)\).
4. Write \(d\tau=dt\,\sqrt{\mathcal F(r)-\mathcal G(r)\dot r^{\,2}-r^2\dot\theta^{\,2}}\).
5. Multiply by \(-m\) to obtain the action integrand.
6. Read off \(\mathcal L=-m\sqrt{\mathcal F(r)-\mathcal G(r)\dot r^{\,2}-r^2\dot\theta^{\,2}}\).

Conjugate momenta and conserved quantities
1. Use \(p_q=\partial\mathcal L/\partial\dot q\).
2. Differentiate with respect to \(\dot\theta\) to get \(L\).
3. Differentiate with respect to \(\dot r\) to get \(p_r\).
4. Use \(E=\sum_i p_i\dot q_i-\mathcal L\).
5. Since \(\mathcal L\) has no explicit \(t\)-dependence, \(E\) is conserved.
6. Since \(\theta\) is cyclic, \(L\) is conserved.

Circular-orbit reduction
1. Set \(\dot r=0\).
2. Reduce the angular-momentum formula to \(\lambda=\dfrac{r^2\dot\theta}{\sqrt{\mathcal F-r^2\dot\theta^{\,2}}}\).
3. Square and solve for \(\dot\theta^{\,2}\).
4. Substitute the result into the circular-orbit energy.
5. Obtain \(E\) as a function of \(r\) and \(\lambda\) only.

Photon limit
1. Keep the physical angular momentum \(L\) fixed.
2. Send \(m\to 0\), so \(\lambda=L/m\to\infty\).
3. In \(E(r,\lambda)\), keep the leading large-\(\lambda\) term under the square root.
4. Replace \(m\lambda\) by \(L\).
5. Obtain \(E_\gamma(r;L)=L\,\dfrac{\sqrt{1-\frac{2MG}{r}}}{r}\).

Photon-sphere condition
1. Treat \(E_\gamma(r;L)\) as the effective radial potential at fixed \(L\).
2. Differentiate \(\dfrac{\sqrt{1-\frac{2MG}{r}}}{r}\) with respect to \(r\).
3. Set the derivative to zero.
4. Solve for \(r\) and get \(r=3MG\).
5. Note from the lecture’s sketch that this extremum is a maximum.
6. Interpret the result as an unstable circular photon orbit.

Near-horizon approximation
1. Suppress the angular part and focus on the \(t\)-\(r\) sector.
2. Set \(2MG=1\) as a temporary choice of units.
3. Rewrite \(1-\dfrac1r=\dfrac{r-1}{r}\).
4. Near \(r=1\), keep \(r-1\) in the numerator but replace the harmless denominator \(r\) by \(1\).
5. Obtain \(d\tau^2\approx (r-1)\,dt^2-\dfrac{dr^2}{r-1}\).
6. Define \(\xi=r-1\), with \(d\xi=dr\).
7. Get \(d\tau^2=\xi\,dt^2-\dfrac{d\xi^2}{\xi}\).

Rindler comparison
1. In flat spacetime introduce \(X=\rho\cosh\omega\) and \(T=\rho\sinh\omega\).
2. Observe that \(X^2-T^2=\rho^2\), so constant \(\rho\) are hyperbolae.
3. Write the flat metric as \(d\tau^2=\rho^2 d\omega^2-d\rho^2\).
4. Redefine \(\rho^2=4\xi\) and \(\omega=t/2\).
5. Differentiate \(\rho^2=4\xi\) to get \(2\rho\,d\rho=4\,d\xi\).
6. Infer \(d\rho^2=\dfrac{d\xi^2}{\xi}\).
7. Recover \(d\tau^2=\xi\,dt^2-\dfrac{d\xi^2}{\xi}\), matching the near-horizon Schwarzschild form.

Inside-horizon interpretation
1. Continue \(\xi\) through zero from outside to inside the horizon.
2. In the Rindler analogy, positive and negative \(\xi\) lie in different wedges.
3. The coordinate proportional to \(r-2MG\) changes from spacelike to timelike.
4. Therefore \(r=0\) is in the future of every timelike trajectory inside the horizon.
5. That is the lecture’s sense in which the singularity is “a time, not a place.”

## Notation Choices
- Use \(\mathcal L\) for the Lagrangian and \(L\) for angular momentum; do not let these collide typographically.
- Use \(\lambda=L/m\) for reduced angular momentum in the main text. The board glyph may look like \(\Lambda\), but the transcript says “lambda.”
- Use \(\mathcal F(r)\) and \(\mathcal G(r)\), not plain \(f\) and \(g\), because that is the lecture’s intended normalization.
- Use a single orbit angle \(\theta\) in the orbit formulas, since that is what the board and later algebra use most consistently.
- Add a remark if needed that the spoken lecture briefly toggles between \(\theta\) and \(\phi\) after equatorial reduction.
- Keep overdots as derivatives with respect to Schwarzschild coordinate time \(t\): \(\dot r=dr/dt\), \(\dot\theta=d\theta/dt\).
- Keep the sign convention exactly as in the lecture: \(d\tau^2=(+)\,dt^2-(\text{spatial parts})\).
- Keep \(c=1\) implicit, but leave \(G\) explicit, matching the lecture.
- Prefer writing \(r=2MG\) directly rather than introducing a new symbol \(r_s\), unless a later chapter-wide notation policy requires it.
- In the near-horizon section, use \(\xi\) rather than the transcript’s fleeting spoken “C”/“c”-like symbol; \(\xi\) is the deliberate coordinate name he actually writes.
- Use \(E\) for the conserved energy after first identifying it with the Hamiltonian construction.

## Uncertain Mathematics
- The spoken angular metric \(d\Omega^2=d\theta^2+\cos^2\theta\,d\phi^2\) is nonstandard; if the final notes convert to the standard \(\sin^2\theta\) form, that conversion should be flagged explicitly.
- The frame showing the Lagrangian does not reveal the full square-root contents; the cleaned Lagrangian must be treated as transcript-supported reconstruction, not pure visual transcription.
- In the visible board formulas, the Schwarzschild factor looks like either \(f\) or \(\mathcal F\); the transcript favors \(\mathcal F\).
- The final symbol in the reduced-angular-momentum equation looks \(\Lambda\)-like on the board, but the lecture language points to \(\lambda\).
- The algebraic form Susskind speaks around the post-substitution energy formula is loose; the cleaned expression for \(E(r,\lambda)\) should be presented as a cautious reconstruction from his prescription, not as a verbatim board derivation.
- The near-horizon form \(d\tau^2=\xi\,dt^2-\dfrac{d\xi^2}{\xi}\) comes after two approximations: suppressing angular directions and replacing the harmless denominator \(r\) by its horizon value.
- The continuation from positive to negative \(\xi\) should be phrased geometrically and coordinately; one should not literally speak of real \(\rho\) becoming imaginary without explanation.
- The lecture gives qualitative optical and communication claims near and inside the photon sphere, but it does not supply a full analytic escape-cone derivation; those claims should remain qualitative unless a later prompt reconstructs them explicitly.