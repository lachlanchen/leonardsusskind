# Math Bank
## Core Equations
- \((1+\epsilon)^p = 1 + p\epsilon + \dfrac{p(p-1)}{2}\epsilon^2 + \dfrac{p(p-1)(p-2)}{3!}\epsilon^3 + \cdots\) [transcript-backed]
- \(\sqrt{1-v^2} \approx 1-\dfrac{v^2}{2}\) for \(v\ll 1\) and \(c=1\) [transcript-backed]
- \(\dfrac{1}{\sqrt{1-v^2}} \approx 1+\dfrac{v^2}{2}\) for \(v\ll 1\) and \(c=1\) [transcript-backed]

- \(\Delta \tau^2=\Delta t^2-\Delta \vec{x}^{\,2}\) [transcript-backed]
- \(\Delta \tau^2=\Delta t^2-\dfrac{\Delta \vec{x}^{\,2}}{c^2}\) [standard reconstruction]
- \(\Delta \tau^2>0\) for timelike separation [transcript-backed]
- \(\Delta \tau^2<0\) for spacelike separation [transcript-backed]

- \(v^i=\dfrac{dx^i}{dt}\) [transcript-backed]
- \(u^\mu=\dfrac{dx^\mu}{d\tau}\) [transcript-backed]
- \(u^0=\dfrac{dt}{d\tau}=\dfrac{1}{\sqrt{1-v^2}}\) [transcript-backed]
- \(u^i=\dfrac{dx^i}{d\tau}=\dfrac{v^i}{\sqrt{1-v^2}}\) [transcript-backed]
- \(\dfrac{d\tau}{dt}=\sqrt{1-v^2}\) [transcript-backed]
- \(u_0^2-\vec{u}^{\,2}=1\) [visible]

- \(S=-m\int d\tau\) [transcript-backed]
- \(S=-m\int dt\,\sqrt{1-v^2}\) [transcript-backed]
- \(L=-m\sqrt{1-v^2}\) [transcript-backed]
- \(L\approx -m+\dfrac12 mv^2\) [transcript-backed]

- \(p_x=\dfrac{\partial L}{\partial \dot{x}}\) [visible]
- \(p_i=\dfrac{\partial L}{\partial \dot{x}^i}\) [standard reconstruction]
- \(p_x=\dfrac{mv_x}{\sqrt{1-v^2}}\) [transcript-backed]
- \(p_i=\dfrac{mv_i}{\sqrt{1-v^2}}=m u_i\) [transcript-backed]

- \(\vec{P}_{\mathrm{initial}}-\vec{P}_{\mathrm{final}}=0\) [visible]
- \(p_0=mu_0\) [transcript-backed]

- \(H=\sum_i \dot{x}^i p_i-L\) [standard reconstruction]
- \(H=\dfrac{m}{\sqrt{1-v^2}}=m u_0\) in \(c=1\) units [transcript-backed]
- \(E=H\) [transcript-backed]
- \(E\approx m+\dfrac12 mv^2\) in \(c=1\) units [transcript-backed]
- \(E=\dfrac{mc^2}{\sqrt{1-v^2/c^2}}\) [standard reconstruction]
- \(E\approx mc^2+\dfrac12 mv^2\) [standard reconstruction]

- \(E^2-p^2=m^2\) in \(c=1\) units [visible]
- \(E=\sqrt{p^2+m^2}\) in \(c=1\) units [transcript-backed]
- \(E^2=p^2c^2+m^2c^4\) [standard reconstruction]
- \(E=\sqrt{p^2c^2+m^2c^4}\) [standard reconstruction]

- \(E=\dfrac12 mv^2=\dfrac{p^2}{2m}\) in nonrelativistic mechanics [visible]
- \(E=|p|\) for \(m=0\) and \(c=1\) [transcript-backed]
- \(E=pc\) for \(m=0\) [standard reconstruction]

- \(p_{\gamma,1}=-p_{\gamma,2}\) for positronium at rest decaying to two photons [transcript-backed]
- \(E_{\text{init}}=mc^2\) for positronium at rest [transcript-backed]
- \(mc^2=2pc\) for the two-photon final state [transcript-backed]
- \(p=\dfrac{mc}{2}\) for each photon [transcript-backed]
- \(E_\gamma=pc=\dfrac{mc^2}{2}\) for each photon [standard reconstruction]

## Definitions And Objects
- Particle:
  treated mechanically through its center of mass; need not be elementary.
- World line:
  trajectory of a particle in spacetime.
- Proper time:
  \(\tau\), defined along timelike intervals by \(\Delta \tau^2=\Delta t^2-\Delta \vec{x}^{\,2}\) in \(c=1\) units.
- Ordinary velocity:
  \(v^i=dx^i/dt\), a three-vector.
- Four-velocity:
  \(u^\mu=dx^\mu/d\tau\), with \(\mu=0,1,2,3\).
- Time component of four-velocity:
  \(u^0=dt/d\tau\).
- Spatial components of four-velocity:
  \(u^i=dx^i/d\tau\).
- Free-particle action:
  invariant action built from proper time, \(S=-m\int d\tau\).
- Relativistic free-particle Lagrangian:
  \(L=-m\sqrt{1-v^2}\).
- Canonical momentum:
  \(p_i=\partial L/\partial \dot{x}^i\).
- Hamiltonian:
  \(H=\sum_i \dot{x}^i p_i-L\); identified in this lecture with the conserved energy.
- Four-momentum:
  \(p^\mu=m u^\mu\), with spatial part equal to relativistic momentum and zeroth component equal to energy in \(c=1\) units.
- Mass:
  invariant particle label; Susskind explicitly rejects “rest mass” as the preferred prose term.
- Massless-particle viewpoint:
  describe energy as a function of momentum rather than velocity.
- Composite-system mass:
  energy of the whole system in the frame where total momentum is zero.

## Derivation Steps
1. Binomial approximation for \(\sqrt{1-v^2}\)
   1. Start from \((1+\epsilon)^p\approx 1+p\epsilon\) for small \(\epsilon\).
   2. Set \(\epsilon=-v^2\) and \(p=\tfrac12\).
   3. Obtain \(\sqrt{1-v^2}\approx 1-\tfrac12 v^2\).

2. Binomial approximation for \((1-v^2)^{-1/2}\)
   1. Start from \((1+\epsilon)^p\approx 1+p\epsilon\).
   2. Set \(\epsilon=-v^2\) and \(p=-\tfrac12\).
   3. Obtain \((1-v^2)^{-1/2}\approx 1+\tfrac12 v^2\).

3. Four-velocity components from proper time
   1. Define \(u^\mu=dx^\mu/d\tau\).
   2. Use \(d\tau^2=dt^2-dx^2\).
   3. Factor out \(dt^2\) to get \(d\tau=dt\sqrt{1-v^2}\).
   4. Therefore \(d\tau/dt=\sqrt{1-v^2}\).
   5. Invert to get \(u^0=dt/d\tau=1/\sqrt{1-v^2}\).
   6. Write \(v^i=dx^i/dt=(dx^i/d\tau)(d\tau/dt)\).
   7. Hence \(u^i=v^i/\sqrt{1-v^2}\).

4. Constraint on four-velocity
   1. Begin with \(\Delta \tau^2=\Delta t^2-\Delta \vec{x}^{\,2}\).
   2. Divide by \(\Delta \tau^2\).
   3. Get \(1=(\Delta t/\Delta \tau)^2-(\Delta \vec{x}/\Delta \tau)^2\).
   4. Identify \(\Delta t/\Delta \tau=u^0\) and \(\Delta \vec{x}/\Delta \tau=\vec{u}\).
   5. Conclude \(u_0^2-\vec{u}^{\,2}=1\).

5. Free-particle action and Lagrangian
   1. Demand an invariant action for frame-independent laws.
   2. Use additivity along the trajectory.
   3. Pick proper time as the invariant incremental quantity.
   4. Write \(S\propto \int d\tau\).
   5. Insert conventional factor \(-m\) to match nonrelativistic mechanics.
   6. Use \(d\tau=dt\sqrt{1-v^2}\).
   7. Read off \(L=-m\sqrt{1-v^2}\).

6. Newtonian limit of the Lagrangian
   1. Start from \(L=-m\sqrt{1-v^2}\).
   2. Use \(\sqrt{1-v^2}\approx 1-\tfrac12 v^2\).
   3. Get \(L\approx -m(1-\tfrac12 v^2)\).
   4. Therefore \(L\approx -m+\tfrac12 mv^2\).
   5. Treat the constant \(-m\) as dynamically irrelevant.
   6. Recover the usual free-particle Lagrangian \(\tfrac12 mv^2\).

7. Canonical momentum from the relativistic Lagrangian
   1. Use \(p_x=\partial L/\partial \dot{x}\).
   2. Differentiate \(L=-m\sqrt{1-v^2}\) with respect to \(\dot{x}=v_x\).
   3. The derivative of the square root contributes a factor \(1/(2\sqrt{1-v^2})\).
   4. The derivative of \(1-v^2\) contributes \(-2v_x\).
   5. Signs and factors cancel to give \(p_x=mv_x/\sqrt{1-v^2}\).
   6. Recognize \(v_x/\sqrt{1-v^2}=u_x\).
   7. Conclude \(p_x=mu_x\), and similarly \(p_i=mu_i\).

8. Why three-momentum conservation is not enough
   1. Write total momentum conservation as \(\vec{P}_{\mathrm{i}}-\vec{P}_{\mathrm{f}}=0\).
   2. Observe that this is only a three-vector statement.
   3. A subset of four-vector components vanishing is not itself Lorentz-invariant.
   4. To make the law invariant, identify a fourth component.
   5. The natural candidate is \(mu_0\).
   6. Check whether that fourth component is the conserved energy.

9. Hamiltonian calculation
   1. Start from \(H=\sum_i \dot{x}^i p_i-L\).
   2. Insert \(p_i=m\dot{x}^i/\sqrt{1-v^2}\).
   3. Then \(\sum_i \dot{x}^i p_i = mv^2/\sqrt{1-v^2}\).
   4. Insert \(L=-m\sqrt{1-v^2}\).
   5. So \(H=mv^2/\sqrt{1-v^2}+m\sqrt{1-v^2}\).
   6. Put both terms over the common denominator \(\sqrt{1-v^2}\).
   7. The numerator becomes \(mv^2+m(1-v^2)=m\).
   8. Therefore \(H=m/\sqrt{1-v^2}=mu_0\).

10. Low-velocity limit of the energy
   1. Start from \(E=H=m/\sqrt{1-v^2}\) in \(c=1\) units.
   2. Use \((1-v^2)^{-1/2}\approx 1+\tfrac12 v^2\).
   3. Obtain \(E\approx m+\tfrac12 mv^2\).
   4. Restore units by replacing the leading \(m\) with \(mc^2\).
   5. Get \(E\approx mc^2+\tfrac12 mv^2\).

11. Mass-shell relation
   1. Start from \(u_0^2-\vec{u}^{\,2}=1\).
   2. Multiply through by \(m^2\).
   3. Use \(p_0=mu_0=E\) in \(c=1\) units.
   4. Use \(\vec{p}=m\vec{u}\).
   5. Conclude \(E^2-p^2=m^2\).
   6. Rearrange to \(E=\sqrt{p^2+m^2}\).
   7. Restore units to \(E^2=p^2c^2+m^2c^4\).

12. Massless limit
   1. Start from \(E^2=p^2c^2+m^2c^4\).
   2. Set \(m=0\).
   3. Obtain \(E^2=p^2c^2\).
   4. Take the positive branch for energy.
   5. Conclude \(E=pc\).

13. Positronium decay at rest
   1. Put the positronium atom in its rest frame.
   2. Initial total momentum is zero.
   3. After decay to two photons, total momentum must still be zero.
   4. Therefore the photons emerge back-to-back with equal and opposite momenta.
   5. Let each photon have momentum magnitude \(p\).
   6. Initial energy is \(mc^2\).
   7. Each photon has energy \(pc\).
   8. Energy conservation gives \(mc^2=2pc\).
   9. Therefore \(p=mc/2\).
   10. Hence each photon has energy \(E_\gamma=mc^2/2\).

## Notation Choices
- Use \(c=1\) as the lecture’s default working convention, and restore \(c\) only when the chapter explicitly switches units.
- Use \(v^2=\vec v^{\,2}=v_x^2+v_y^2+v_z^2\).
- Use \(\dot{x}^i=dx^i/dt\); dot means derivative with respect to ordinary coordinate time \(t\), not proper time.
- Use \(u^\mu=dx^\mu/d\tau\) as the formal definition, but allow the lecture-style component notation \(u_0\), \(u_i\) when matching board formulas such as \(u_0^2-\vec u^{\,2}=1\).
- Use \(\mu=0,1,2,3\) for spacetime indices and \(i=1,2,3\) for spatial indices.
- Use \(p_i\) for single-particle canonical/relativistic momentum components.
- Use \(\vec P_{\mathrm{i}}\) and \(\vec P_{\mathrm{f}}\) for total initial and final three-momentum in conservation laws, since that matches the board-level distinction between system totals and component formulas.
- Use \(p_0\) for the fourth momentum component in \(c=1\) units and identify it with \(E\).
- Use \(H\) and \(E\) interchangeably only after the Hamiltonian has been identified as the conserved energy.
- In prose, use “mass” to mean invariant mass; mention “rest mass” only as historical terminology that the lecture rejects.
- For massless particles, prefer \(E(p)\) over \(E(v)\); this is a genuine lecture-level notation shift, not just a cosmetic one.
- Standardize the mass-shell relation as \(E^2-p^2=m^2\) in \(c=1\) units even though the board image shows uppercase \(P\).

## Uncertain Mathematics
- The canonical-momentum frame only clearly shows \(P_x=\); the full derivative expression is a safe reconstruction from transcript and standard Lagrangian mechanics, not fully legible on the board.
- The momentum-conservation frame clearly shows a vector equation ending in \(=0\), but the handwritten subscripts for “initial” and “final” are soft; typeset them cleanly.
- The right board in the momentum-conservation frame contains remnants of the low-velocity expansion, but only the endpoint \(-m+\tfrac12 mv^2\) is safe to preserve from the image alone.
- The Hamiltonian frame shows only \(H=\); the full formula \(H=\sum_i \dot{x}^i p_i-L\) is transcript-backed, not image-backed.
- The transcript around the Hamiltonian algebra has minor slips and spoken corrections; the clean derivation should preserve the intended cancellation, not the false starts.
- The frame with invariant relations clearly supports \(E^2-P^2=m^2\), but the upper component equation is faint; \(u_0^2-\vec u^{\,2}=1\) should be treated as cautious standardization of what is being written.
- Several late audience exchanges are garbled, especially around 01:42:49 onward and 01:49:42 to 01:51:53; preserve only the mathematically stable thread:
  the massless limit, the exact energy formula, and the clarification that \(E\approx m+\tfrac12 mv^2\) was only a low-velocity approximation in \(c=1\) units.
- The lecture’s spoken restoration of factors of \(c\) is sometimes heuristic and unit-driven; the final notes should present the restored formulas cleanly, but mark them as standard reconstruction where the transcript only gestures at the unit-fixing.
- The positronium numerical mass values mentioned in audience back-and-forth are not stable enough for note-quality preservation; keep the symbolic decay calculation, not the offhand numbers.
- The late discussion of wave-function phase involving \(mc^2\) is too fragmentary here to incorporate as chapter mathematics without separate verification.