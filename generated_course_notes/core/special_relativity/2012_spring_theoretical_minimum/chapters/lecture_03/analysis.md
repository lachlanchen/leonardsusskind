# Chapter Plan
## Lecture Arc
- The real spine of the lecture is practical before it is conceptual: we begin with the binomial expansions of \(\sqrt{1-v^2}\) and \((1-v^2)^{-1/2}\), because Susskind wants a reusable tool for checking that relativistic formulas reduce to Newtonian ones at low velocity.
- From that technical warm-up he pivots to a quick classical-mechanics recap: particles as center-of-mass objects, world lines in spacetime, and the action principle as the framework we will reuse rather than reinvent.
- The next movement is geometric and invariant: define proper time, distinguish timelike from spacelike separation, and then use \(d\tau\) to define four-velocity and derive the relation \(u_0^2-\vec u^{\,2}=1\).
- With that invariant machinery in hand, the lecture turns to dynamics: if the laws are to be frame-independent, the free-particle action should be built from proper time, hence \(S=-m\int d\tau\), and therefore \(L=-m\sqrt{1-v^2}\).
- He then checks the Newtonian limit explicitly, expanding the Lagrangian to recover \(-m+\frac12 mv^2\); this is the first major recap point, where the earlier binomial tool pays off.
- After that he declares the equations of motion themselves less interesting than the conserved quantities, and the lecture’s focus shifts sharply to momentum and energy.
- Canonical momentum is identified from the Lagrangian, then a conceptual tension is raised: ordinary momentum conservation is a vector equation, but not yet an invariant one. That tension is resolved by promoting it to four-momentum conservation and identifying the fourth component through the Hamiltonian.
- The lecture culminates in three linked consequences: \(E=mc^2\) from the low-velocity expansion of the Hamiltonian, the invariant relation \(E^2-p^2=m^2\) in \(c=1\) units, and the massless/positronium applications that show why energy and momentum, not naive mass sums, are the real conserved quantities.

## Section Outline
1. **Low-Velocity Expansions As Setup**  
   Open with the binomial-theorem expansions of \(\sqrt{1-v^2}\) and \(1/\sqrt{1-v^2}\), because the lecture uses them as the standing technical bridge from relativistic formulas back to classical mechanics.

2. **Particles, World Lines, And Proper Time**  
   Move from the classical reminder about particles and center of mass to spacetime trajectories, timelike versus spacelike intervals, and the invariant proper time \(\Delta\tau\) that will organize the rest of the lecture.

3. **Four-Velocity And Its Constraint**  
   Define \(u^\mu = dx^\mu/d\tau\), derive \(u^0\) and \(u^i\) in terms of ordinary velocity, and explain why the four components are constrained by \(u_0^2-\vec u^{\,2}=1\) rather than independent.

4. **Invariant Action And The Relativistic Lagrangian**  
   Build the free-particle action from proper time and convert it into the Lagrangian \(L=-m\sqrt{1-v^2}\), then expand it to recover the Newtonian form. Include a standalone `Question & Answer`: Why is proper time the right thing to build the action from, and why do the overall sign and constant factor not change the equations of motion?

5. **Canonical Momentum, Vector Conservation, And The Need For A Fourth Component**  
   Use \(p_i=\partial L/\partial \dot x_i\) to derive relativistic momentum, then preserve the lecture’s conceptual obstacle: \(\vec P_{\mathrm{i}}-\vec P_{\mathrm{f}}=0\) is a vector equation, but not yet a Lorentz-invariant law. Include a standalone `Question & Answer`: Why is three-momentum conservation by itself not enough, and why must it be completed to a four-vector statement?

6. **Hamiltonian, Energy, And The Meaning Of Mass**  
   Introduce \(H=\sum_i \dot x_i p_i-L\), identify it with the fourth momentum component, and expand it at low velocity to obtain \(E\approx m+\frac12 mv^2\) in \(c=1\) units and hence \(E\approx mc^2+\frac12 mv^2\) after restoring units. This is also where the notes should preserve Susskind’s terminological point that modern “mass” means what older books called “rest mass.”

7. **Mass Shell, Massless Particles, And Positronium Decay**  
   Derive \(E^2-p^2=m^2\), pass to the massless limit \(E=pc\), and then work through positronium decay as the lecture’s concrete payoff. Include a standalone `Question & Answer`: Why is velocity the wrong variable for massless particles, and why should we think in terms of energy as a function of momentum instead?

## Mathematical Content To Include
- \(\sqrt{1-v^2}\approx 1-\frac{v^2}{2}\) for small \(v\) [transcript-backed]
- \((1-v^2)^{-1/2}\approx 1+\frac{v^2}{2}\) for small \(v\) [transcript-backed]
- \(\Delta \tau^2=\Delta t^2-\Delta \vec x^{\,2}\) in \(c=1\) units [transcript-backed]
- \(\Delta \tau^2=\Delta t^2-\frac{\Delta \vec x^{\,2}}{c^2}\) when units are restored [standard reconstruction]
- Timelike interval: \(\Delta \tau^2>0\); spacelike interval: \(\Delta \tau^2<0\) [transcript-backed]
- \(u^\mu=\dfrac{dx^\mu}{d\tau}\) [transcript-backed]
- \(u^0=\dfrac{dt}{d\tau}=\dfrac{1}{\sqrt{1-v^2}}\) [transcript-backed]
- \(u^i=\dfrac{dx^i}{d\tau}=\dfrac{v^i}{\sqrt{1-v^2}}\) [transcript-backed]
- \(u_0^2-\vec u^{\,2}=1\) [frame-backed]
- \(S=-m\int d\tau\) [transcript-backed]
- \(S=-m\int dt\,\sqrt{1-v^2}\) [transcript-backed]
- \(L=-m\sqrt{1-v^2}\) [transcript-backed]
- \(L\approx -m+\frac12 mv^2\) [transcript-backed]
- \(p_x=\dfrac{\partial L}{\partial \dot x}\) [frame-backed]
- \(p_i=\dfrac{m v_i}{\sqrt{1-v^2}}=m u_i\) [transcript-backed]
- \(\vec P_{\mathrm{initial}}-\vec P_{\mathrm{final}}=0\) [frame-backed]
- \(H=\sum_i \dot x_i\,p_i-L\) [standard reconstruction]
- \(H=\dfrac{m}{\sqrt{1-v^2}}=m u_0\) in \(c=1\) units [transcript-backed]
- \(E\approx m+\frac12 mv^2\) in \(c=1\) units [transcript-backed]
- \(E=\dfrac{mc^2}{\sqrt{1-v^2/c^2}}\) [standard reconstruction]
- \(E\approx mc^2+\frac12 mv^2\) [standard reconstruction]
- Modern terminology: mass is invariant particle label; avoid “rest mass” in the prose body [transcript-backed]
- \(E^2-p^2=m^2\) in \(c=1\) units [frame-backed]
- \(E^2=p^2c^2+m^2c^4\) after restoring units [standard reconstruction]
- Massless limit: \(E=|p|\) in \(c=1\) units [transcript-backed]
- Massless limit: \(E=pc\) [standard reconstruction]
- Positronium at rest: \(p_{\gamma,1}=-p_{\gamma,2}\) [transcript-backed]
- Energy conservation for two photons: \(mc^2=2pc\) [transcript-backed]
- Therefore \(p=\dfrac{mc}{2}\) and each photon has \(E_\gamma=\dfrac{mc^2}{2}\) [transcript-backed]

## Diagram And Figure Plan
- Keep `lecture_03_figure_02.png` visible near the canonical-momentum derivation. It is the best frame-backed evidence that the lecture is explicitly defining momentum from the Lagrangian rather than assuming \(p=mv\).
- Keep `lecture_03_figure_03.png` visible near the transition from three-momentum conservation to the need for a four-vector conservation law. It preserves the board rhythm of “this is a vector equation” and should sit next to a clean displayed version of the equation.
- Keep `lecture_03_figure_05.png` visible near the invariant relations \(u_0^2-\vec u^{\,2}=1\) and \(E^2-p^2=m^2\). It is the strongest visual bridge between the four-velocity normalization and the energy-momentum mass-shell relation.
- Do not keep `lecture_03_figure_01.png` as a chapter figure; it is only a title card.
- Do not keep `lecture_03_figure_04.png` as a visible figure; it is only the start of `H=` and is too incomplete to help the reader.
- Do not keep `lecture_03_figure_06.png` as a visible figure; it does not reliably show the claimed energy approximation and is weaker than the transcript for that step.
- For this six-image asset set, no idea needs to be redrawn in TikZ. The useful frame-backed material is equation-centered rather than diagram-centered, so the final chapter should prefer screenshots plus nearby displayed equations, not screenshot-plus-TikZ pairings.
- If the chapter later adds a clean spacetime sketch of timelike/spacelike intervals or a positronium-decay worldline sketch, that should come only from separate, clearer frame evidence; these six assets do not provide a trustworthy visual basis for those TikZ diagrams.

## Caution Notes
- The lecture’s first substantial move is the binomial-expansion warm-up; do not compress it into a footnote, because later low-velocity expansions of both \(L\) and \(E\) depend on it narratively.
- `lecture_03_figure_02.png` supports the canonical-momentum step, but the right-hand side is blocked; typeset \(p_x=\partial L/\partial \dot x\) cleanly rather than pretending the screenshot is fully legible.
- `lecture_03_figure_03.png` clearly supports the vector-conservation point, but the exact board labels for “initial” and “final” are soft; standardize the notation in LaTeX.
- `lecture_03_figure_05.png` strongly supports \(E^2-p^2=m^2\), but the upper component formula is partly occluded; write \(u_0^2-\vec u^{\,2}=1\) in canonical form rather than overfitting the blurry handwriting.
- `lecture_03_figure_04.png` and `lecture_03_figure_06.png` are weak visual evidence; use the transcript, not the images, as the primary support for the Hamiltonian formula and the low-velocity energy expansion.
- Be careful when restoring factors of \(c\). The lecture oscillates between \(c=1\) and restored units, and the prose should announce the switch explicitly each time.
- Keep Susskind’s terminology point sharp: in the chapter prose, “mass” should mean invariant mass, not velocity-dependent “relativistic mass.”
- The transcript becomes garbled in several late audience exchanges, especially around 01:42:49 onward and again around 01:49:42–01:51:53. Preserve only the mathematically clear thread there: massless particles, energy-momentum formulas, and the clarification that \(E\approx m+\frac12 mv^2\) was only an approximation in \(c=1\) units.
- The late audience questions are useful, but not all should survive. Keep only the ones that sharpen the mathematical structure: action as an invariant, why three-momentum is not enough, why massless particles require \(E(p)\), and what exactly \(E=mc^2\) means for composite systems.
- The prose style should feel like Susskind unfolding the derivation with us: concrete, sequential, and motivated. Avoid rewriting the lecture into a detached encyclopedia entry.