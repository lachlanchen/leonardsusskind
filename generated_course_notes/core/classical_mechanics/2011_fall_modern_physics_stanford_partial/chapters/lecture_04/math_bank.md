# Math Bank

## Core Equations

- \(v_r=\dot r\) [transcript-backed]
- \(v_\theta=r\dot\theta\) [transcript-backed]
- \(T=\dfrac{m}{2}\left(v_r^2+v_\theta^2\right)=\dfrac{m}{2}\left(\dot r^{\,2}+r^2\dot\theta^{\,2}\right)\) [transcript-backed]
- \(\mathcal{L}=\dfrac{m}{2}\left(\dot r^{\,2}+r^2\dot\theta^{\,2}\right)-U(r)\) [visible]
- \(\pi_i=\dfrac{\partial \mathcal{L}}{\partial \dot q_i}\) [standard reconstruction]
- \(\dfrac{d\pi_i}{dt}=\dfrac{\partial \mathcal{L}}{\partial q_i}\) [standard reconstruction]
- \(\dfrac{d}{dt}\left(\dfrac{\partial \mathcal{L}}{\partial \dot q_i}\right)=\dfrac{\partial \mathcal{L}}{\partial q_i}\) [standard reconstruction]
- \(\pi_r=\dfrac{\partial \mathcal{L}}{\partial \dot r}=m\dot r\) [transcript-backed]
- \(m\ddot r=\dfrac{\partial \mathcal{L}}{\partial r}=mr\dot\theta^{\,2}-\dfrac{dU}{dr}\) [transcript-backed]
- \(\pi_\theta=\dfrac{\partial \mathcal{L}}{\partial \dot\theta}=mr^2\dot\theta\) [transcript-backed]
- \(\dfrac{d}{dt}\left(mr^2\dot\theta\right)=\dfrac{\partial \mathcal{L}}{\partial \theta}=0\) [transcript-backed]
- \(L\equiv mr^2\dot\theta=\text{constant}\) [transcript-backed]
- \(\dot\theta=\dfrac{L}{mr^2}\) [transcript-backed]
- \(m\ddot r=-\dfrac{dU}{dr}+mr\dot\theta^{\,2}\) [transcript-backed]
- \(m\ddot r=-\dfrac{dU}{dr}+\dfrac{L^2}{mr^3}\) [transcript-backed]
- \(\delta f=\sum_i \dfrac{\partial f}{\partial \alpha_i}\,\delta\alpha_i\) [transcript-backed]
- \(\delta f=0\quad\Longleftrightarrow\quad \dfrac{\partial f}{\partial \alpha_i}=0\ \text{for all }i\) [transcript-backed]
- \(\delta A=0\) [visible]
- \(A=\int \mathcal{L}\,dt\) [visible]
- \(\delta A=\int \sum_i\left(\dfrac{\partial \mathcal{L}}{\partial q_i}\,\delta q_i+\dfrac{\partial \mathcal{L}}{\partial \dot q_i}\,\delta \dot q_i\right)dt\) [standard reconstruction]
- \(\delta A=\int \sum_i\left(\dfrac{\partial \mathcal{L}}{\partial q_i}-\dfrac{d}{dt}\dfrac{\partial \mathcal{L}}{\partial \dot q_i}\right)\delta q_i\,dt+\left[\sum_i\dfrac{\partial \mathcal{L}}{\partial \dot q_i}\,\delta q_i\right]_{t_1}^{t_2}\) [standard reconstruction]
- \(\delta q_i=\epsilon f_i(q)\) [transcript-backed]
- \(Q=\sum_i \pi_i f_i(q)\) [transcript-backed]
- \(\dfrac{dQ}{dt}=0\) [transcript-backed]
- \(\delta x_i=\epsilon,\qquad \delta y_i=\delta z_i=0\) [transcript-backed]
- \(Q_x=\sum_i p_{x_i}\) [transcript-backed]
- \(\delta x=-\epsilon y,\qquad \delta y=\epsilon x\) [transcript-backed]
- \(f_x=-y,\qquad f_y=x\) [transcript-backed]
- \(Q_{\text{rot}}=xp_y-yp_x\) [transcript-backed]
- \(q_i(t)\mapsto q_i(t-\epsilon)\) [transcript-backed]
- \(\delta q_i=-\epsilon \dot q_i\) [transcript-backed]
- \(\delta \dot q_i=-\epsilon \ddot q_i\) [transcript-backed]
- \(A_{\text{overhang}}\approx \mathcal{L}(t_B)\,\epsilon,\qquad B_{\text{overhang}}\approx \mathcal{L}(t_A)\,\epsilon\) [transcript-backed]
- \(\mathcal{L}-\sum_i \dot q_i\,\dfrac{\partial \mathcal{L}}{\partial \dot q_i}=\text{constant}\) [transcript-backed]
- \(H\equiv \sum_i \dot q_i\,\pi_i-\mathcal{L}\) [transcript-backed]
- \(\mathcal{L}=\dfrac{1}{2}m\dot x^2-U(x)\) [transcript-backed]
- \(\pi_x=m\dot x\) [transcript-backed]
- \(H=\pi_x\dot x-\mathcal{L}=m\dot x^2-\left(\dfrac{1}{2}m\dot x^2-U(x)\right)=\dfrac{1}{2}m\dot x^2+U(x)\) [transcript-backed]
- \(\mathcal{L}=\mathcal{L}(q,\dot q,t)\ \text{explicitly}\Rightarrow\) time-translation symmetry fails \(\Rightarrow\) energy need not be conserved [transcript-backed]

## Definitions And Objects

- Central-force problem: \(U\) depends only on \(r\), equivalently the physics is rotationally invariant.
- Generalized coordinates: \(q_i\); in the opening example, \(q_i=(r,\theta)\).
- Generalized velocities: \(\dot q_i\).
- Canonical momentum conjugate to \(q_i\): \(\pi_i=\partial \mathcal{L}/\partial \dot q_i\).
- Radial canonical momentum: \(\pi_r=m\dot r\).
- Angular canonical momentum: \(\pi_\theta=mr^2\dot\theta\), identified with angular momentum.
- Variation: a small change in variables or in a trajectory, denoted by \(\delta\).
- Action: \(A=\int \mathcal{L}\,dt\).
- Symmetry: a transformation of coordinates/trajectory that leaves the action unchanged.
- Infinitesimal symmetry: \(q_i\to q_i+\epsilon f_i(q)\), with \(\epsilon\) small and only first-order terms kept.
- Continuous vs. discrete symmetry: the theorem here is for infinitesimal continuous symmetries, not discrete cube-like symmetries.
- Noether charge: the conserved quantity \(Q=\sum_i \pi_i f_i(q)\) associated with a continuous symmetry.
- Generalized force language: the centrifugal term is treated as part of the generalized force; it is not coming from \(dU/dr\).
- Hamiltonian: defined from the conserved quantity for time translation, after Susskind flips the overall sign to standard convention.
- Energy in this lecture: the quantity conserved because of time-translation invariance; in standard \(T-U\) mechanics it reduces to \(T+U\).

## Derivation Steps

1. Polar-coordinate setup: choose \(r,\theta\); identify \(v_r=\dot r\) and \(v_\theta=r\dot\theta\); use orthogonal components to get \(v^2=\dot r^{\,2}+r^2\dot\theta^{\,2}\); write \(\mathcal{L}=T-U(r)\).

2. General Euler–Lagrange setup: define \(\pi_i=\partial\mathcal{L}/\partial \dot q_i\); state \(d\pi_i/dt=\partial\mathcal{L}/\partial q_i\); specialize afterward to \(r\) and \(\theta\).

3. Radial equation: compute \(\pi_r=\partial\mathcal{L}/\partial \dot r=m\dot r\); differentiate to get \(d\pi_r/dt=m\ddot r\); compute \(\partial\mathcal{L}/\partial r\) from the \(r^2\dot\theta^2\) term and from \(-U(r)\); obtain \(m\ddot r=mr\dot\theta^{\,2}-dU/dr\).

4. Interpretation of the radial equation: read \(mr\dot\theta^{\,2}\) as a positive outward contribution; identify it as the centrifugal term; note that it arises from the \(r\)-dependence of the kinetic term, not from differentiating the potential.

5. Angular-momentum derivation: compute \(\pi_\theta=\partial\mathcal{L}/\partial \dot\theta=mr^2\dot\theta\); note that \(\partial\mathcal{L}/\partial\theta=0\) because \(U\) is independent of \(\theta\); conclude \(d\pi_\theta/dt=0\); rename the constant as \(L\).

6. Effective radial equation: solve \(\dot\theta=L/(mr^2)\); square it; insert into \(mr\dot\theta^{\,2}\); cancel factors of \(m\) and \(r\); obtain \(m\ddot r=-dU/dr+L^2/(mr^3)\).

7. Variation shorthand for ordinary functions: expand \(f(\alpha+\delta\alpha)-f(\alpha)\) to first order as \(\sum_i (\partial f/\partial \alpha_i)\delta\alpha_i\); require vanishing for arbitrary \(\delta\alpha_i\); conclude equivalence with vanishing partial derivatives.

8. First variation of the action: start from \(A=\int \mathcal{L}\,dt\); vary coordinates and velocities; write \(\delta A=\int \sum_i[(\partial\mathcal{L}/\partial q_i)\delta q_i+(\partial\mathcal{L}/\partial\dot q_i)\delta\dot q_i]dt\); integrate the second term by parts; isolate the bulk Euler–Lagrange term plus the endpoint term.

9. General Noether proof for ordinary continuous symmetries: start with a classical trajectory satisfying the equations of motion; apply a symmetry transformation that moves the whole trajectory and its endpoints; use symmetry to say \(\delta A=0\); use the equations of motion to kill the bulk integral; conclude the endpoint quantity \(\sum_i (\partial\mathcal{L}/\partial\dot q_i)\delta q_i\) is the same at two times; replace \(\delta q_i=\epsilon f_i(q)\); drop the common factor \(\epsilon\); obtain \(Q=\sum_i\pi_i f_i(q)\) conserved.

10. Translation example: choose translation along \(x\); set \(\delta x_i=\epsilon\), \(\delta y_i=\delta z_i=0\); equivalently \(f_{x_i}=1\), others \(0\); form \(Q=\sum_i \pi_{x_i}\); identify \(\pi_{x_i}=m_i\dot x_i=p_{x_i}\); conclude total \(x\)-momentum is conserved.

11. Rotation example in Cartesian form: use \(\delta x=-\epsilon y\), \(\delta y=\epsilon x\); read off \(f_x=-y\), \(f_y=x\); form \(Q=\pi_xf_x+\pi_yf_y\); rename \(\pi_x,\pi_y\) as \(p_x,p_y\); conclude \(Q=xp_y-yp_x\), the angular momentum component perpendicular to the plane.

12. Time-translation setup: assume no explicit time dependence in the system; shift the entire classical trajectory upward in time by \(\epsilon\); reinterpret the shifted curve at fixed time as a horizontal displacement in \(q\)-space; write the transformed trajectory as \(q(t-\epsilon)\); expand to first order to get \(\delta q=-\epsilon \dot q\).

13. Time-translation action difference on the overlapping interval: compare black and red trajectories over their common time interval; write the same first-variation integral as before; integrate by parts; use the equations of motion to kill the bulk term; keep the endpoint contribution because the endpoints moved.

14. Overhang correction: note that time translation also changes the time interval of the red path relative to the black path; define the two small overhang contributions; approximate each by \(\mathcal{L}\times \epsilon\) at the corresponding endpoint; add \(A_{\text{overhang}}-B_{\text{overhang}}\) to the endpoint term.

15. Conserved quantity from time translation: substitute \(\delta q_i=-\epsilon \dot q_i\) into the endpoint contribution; combine with the overhang pieces; factor out \(\epsilon\); conclude that \(\mathcal{L}-\sum_i \dot q_i(\partial\mathcal{L}/\partial \dot q_i)\) has equal values at the two endpoints; flip the sign to define \(H=\sum_i \dot q_i\pi_i-\mathcal{L}\).

16. Simple one-dimensional Hamiltonian check: take \(\mathcal{L}=\frac12 m\dot x^2-U(x)\); compute \(\pi_x=m\dot x\); form \(H=\pi_x\dot x-\mathcal{L}\); simplify; obtain \(H=\frac12 m\dot x^2+U(x)\); identify this with the familiar total energy.

## Notation Choices

- Use \(\mathcal{L}\) for the Lagrangian throughout. Do not use plain \(L\) for the Lagrangian, because \(L\) is also angular momentum in the lecture.
- Use \(A\) for the action in the main chapter body when following this lecture closely; the frames visibly support \(A\), not \(S\).
- Use \(U(r)\) for the potential in the polar example. Do not write \(U(r,\theta)\) unless explicitly discussing the non-central case as a contrast.
- Use \(q_i\) for generic generalized coordinates and \(\dot q_i\) for their velocities.
- Use \(\pi_i\) for canonical momenta in general formulas; when specializing to Cartesian mechanics, allow \(p_x,p_y,p_z\) as the standard linear-momentum names.
- Use \(L\) for angular momentum in the central-force example: \(L=mr^2\dot\theta\).
- Write derivatives carefully:
  - \(\partial/\partial q_i\), \(\partial/\partial \dot q_i\) for partial derivatives of \(\mathcal{L}\).
  - \(d/dt\) for total time derivative along the trajectory.
- Use explicit summation \(\sum_i\) in note-quality equations; the transcript sometimes suppresses it verbally.
- For the first-variation formula, use endpoint notation \([\,\cdot\,]_{t_1}^{t_2}\) in the final chapter, not Susskind’s muddled \(t_A,t_B,A,B\) labels.
- For infinitesimal symmetries, write \(\delta q_i=\epsilon f_i(q)\) and define \(f_i\) as coordinate-dependent generators.
- For time translation, keep both viewpoints:
  - trajectory shift: \(t\to t+\epsilon\),
  - induced coordinate change at fixed time: \(q_i(t)\to q_i(t-\epsilon)\), hence \(\delta q_i=-\epsilon \dot q_i\).
- Prefer “stationary action” in polished notes when making the formal statement, but preserve the lecture’s spoken use of “least action” or “minimum” when narratively important.

## Uncertain Mathematics

- The transcript garbles the general Euler–Lagrange statement around 00:06:53–00:07:03. The clean equation should be written in standard form, not transcribed literally from that line.
- The full equality \(\pi_i=\partial\mathcal{L}/\partial \dot q_i\) is only partly visible on the board; treat the displayed clean formula as a cautious reconstruction supported by sequence and context.
- The first-variation and integrated-by-parts formulas in the later frames are structurally clear but not fully legible symbol-by-symbol; use standard clean notation rather than claiming literal board transcription.
- Susskind verbally says “minimum” several times for action and for ordinary functions. The final notes should avoid overcommitting to literal minimum when stationarity is the safer mathematical statement.
- The early student question is transcribed as “Is \(u(r)\) theta?” The intended mathematical point is that \(U\) depends only on \(r\), not on \(\theta\).
- The rotation-sign discussion wobbles before settling. Use the stabilized convention \(\delta x=-\epsilon y\), \(\delta y=\epsilon x\).
- The time-translation derivation contains confused labels for the overhang pieces and endpoints. Keep the logic, but relabel endpoints cleanly in the final notes.
- The overhang estimates \(\mathcal{L}(t)\epsilon\) assume \(\epsilon\) is small enough that \(\mathcal{L}\) does not vary appreciably over the interval and that no singular behavior intervenes; that assumption is stated in the lecture and should remain explicit if the derivation is written carefully.
- Do not insert stronger standard results not actually derived here, especially \(\dot H=-\partial \mathcal{L}/\partial t\). The lecture only states the qualitative conclusion that explicit time dependence breaks energy conservation.
- The admissibility condition on a Lagrangian is only gestured at near the end: the map between velocities and canonical momenta should be single-valued/invertible. Do not elaborate beyond that without later lecture support.