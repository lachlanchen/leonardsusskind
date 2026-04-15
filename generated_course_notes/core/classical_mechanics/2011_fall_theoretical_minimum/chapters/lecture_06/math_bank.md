# Math Bank
## Core Equations
- \(p_i \equiv \dfrac{\partial L}{\partial \dot q_i}\) [transcript-backed]
- \(\dot p_i = \dfrac{\partial L}{\partial q_i}\) [transcript-backed]
- If \(L=T-V\) and \(T\) has no explicit \(q_i\)-dependence, then \(\dot p_i = -\,\dfrac{\partial V}{\partial q_i}\) [standard reconstruction]
- For a symmetry \(\delta q_i=\epsilon f_i\), the associated conserved quantity is \(Q=\sum_i p_i f_i\) [transcript-backed]

- Wedge coordinates: \(X=\) horizontal position of the wedge corner, \(x=\) horizontal position of the particle relative to the corner [transcript-backed]
- Fixed wedge slope: \(\dfrac{y}{x}=\tan\alpha\) [transcript-backed]
- In the \(45^\circ\) simplification: \(y=x,\quad \dot y=\dot x\) [transcript-backed]
- \(T_{\text{wedge}}=\dfrac12 M\dot X^2\) [transcript-backed]
- \(T_{\text{particle}}=\dfrac m2\Big[(\dot X+\dot x)^2+\dot x^2\Big]\) [transcript-backed]
- \(V=mgx\) [transcript-backed]
- \(L=\dfrac12 M\dot X^2+\dfrac m2\Big[(\dot X+\dot x)^2+\dot x^2\Big]-mgx\) [transcript-backed]
- \(p_X=\dfrac{\partial L}{\partial \dot X}=M\dot X+m(\dot X+\dot x)\) [transcript-backed]
- \(p_x=\dfrac{\partial L}{\partial \dot x}=m(\dot X+\dot x)+m\dot x\) [transcript-backed]
- Translation symmetry for the whole wedge system: \(\delta X=\epsilon,\quad \delta x=0\) [transcript-backed]
- Since \(X\) is cyclic, \(\dot p_X=\dfrac{\partial L}{\partial X}=0\) [transcript-backed]
- For the \(x\)-equation in the \(45^\circ\) example: \(\dot p_x=\dfrac{\partial L}{\partial x}=-\,mg\) [transcript-backed]

- Double pendulum coordinate choice: \((\theta,\alpha)\), with \(\alpha\) measured relative to the first rod [transcript-backed]
- First bob auxiliary coordinates: \(x=\sin\theta,\quad y=\cos\theta\) [transcript-backed]
- First bob velocities: \(\dot x=\dot\theta\cos\theta,\quad \dot y=-\dot\theta\sin\theta\) [transcript-backed]
- Second bob auxiliary coordinates: \(x'=\sin\theta+\sin(\theta+\alpha),\quad y'=\cos\theta+\cos(\theta+\alpha)\) [transcript-backed]
- Second bob velocity component shown in the derivation: \(\dot x'=\dot\theta\cos\theta+(\dot\theta+\dot\alpha)\cos(\theta+\alpha)\) [transcript-backed]
- First bob kinetic term: \(\dot x^{\,2}+\dot y^{\,2}=\dot\theta^{\,2}\) [transcript-backed]
- Board line near the \(\theta\)-equation: \(T-V=\dot\theta^{\,2}+\dfrac{(\dot\theta-\dot\alpha)^2}{2}+\dot\theta(\dot\theta-\dot\alpha)\cos\alpha\) [visible]
- Board momentum equation: \(\dot P_\theta=\dfrac{\partial L}{\partial \theta}\) [visible]
- In the no-gravity double pendulum, \(\dfrac{\partial L}{\partial \theta}=0\), so \(\dot p_\theta=0\) [transcript-backed]
- With gravity restored, the potential is built from the two heights and schematically involves \(\cos\theta+\cos(\theta+\alpha)\) [transcript-backed]

- Hamiltonian definition: \(H=\sum_i \dot q_i p_i-L\) [visible]
- Multivariable variation identity: \(\delta F=\sum_i \left(\dfrac{\partial F}{\partial q_i}\delta q_i+\dfrac{\partial F}{\partial p_i}\delta p_i\right)\) [transcript-backed]
- Expanded Hamiltonian variation before cancellation:
  \[
  \delta H=\sum_i \big(\dot q_i\,\delta p_i+p_i\,\delta \dot q_i\big)-\sum_i \left(\frac{\partial L}{\partial \dot q_i}\delta \dot q_i+\frac{\partial L}{\partial q_i}\delta q_i\right)
  \]
  [standard reconstruction]
- Reduced Hamiltonian variation:
  \[
  \delta H=\sum_i \dot q_i\,\delta p_i-\dot p_i\,\delta q_i
  \]
  [standard reconstruction]
- Hamilton’s equations:
  \[
  \frac{\partial H}{\partial p_i}=\dot q_i,\qquad \frac{\partial H}{\partial q_i}=-\dot p_i
  \]
  [visible]

- Standard oscillator Lagrangian: \(L=\dfrac12 m\dot x^2-\dfrac12 kx^2\) [transcript-backed]
- Oscillator frequency: \(\omega=\sqrt{\dfrac{k}{m}}\) [transcript-backed]
- Rescaling condition: \(\dfrac{\omega}{2}q^2=\dfrac{k}{2}x^2\) [transcript-backed]
- Hence \(q^2=\sqrt{km}\,x^2\) [transcript-backed]
- One consistent choice is \(q=(km)^{1/4}x\) [standard reconstruction]
- Then \(\dot q^{\,2}=\sqrt{km}\,\dot x^{\,2}\) [transcript-backed]
- Rescaled oscillator Lagrangian:
  \[
  L=\frac{1}{2\omega}\dot q^{\,2}-\frac{\omega}{2}q^2
  \]
  [visible]
- Conjugate momentum for the rescaled oscillator:
  \[
  p=\frac{\partial L}{\partial \dot q}=\frac{\dot q}{\omega}
  \]
  [transcript-backed]
- Equivalent first-order relation: \(\dot q=\omega p\) [transcript-backed]
- Oscillator Hamiltonian:
  \[
  H(q,p)=\frac{\omega}{2}(p^2+q^2)
  \]
  [transcript-backed]
- In original variables, the Hamiltonian would be
  \[
  H(x,p_x)=\frac{p_x^2}{2m}+\frac{k}{2}x^2
  \]
  [transcript-backed]
- Constant-energy shells in the rescaled variables:
  \[
  p^2+q^2=\frac{2H}{\omega}
  \]
  [standard reconstruction]
- Oscillator Hamilton equations:
  \[
  \dot q=\omega p,\qquad \dot p=-\omega q
  \]
  [standard reconstruction]
- Euler-Lagrange line on the board:
  \[
  \frac{d}{dt}\!\left(\frac{\dot q}{\omega}\right)=-\omega q
  \]
  [visible]
- Board second-order form:
  \[
  \frac{\ddot q}{\omega}=-\omega q
  \]
  [visible]
- Cleaned oscillator equation:
  \[
  \ddot q=-\omega^2 q
  \]
  [standard reconstruction]

## Definitions And Objects
- “Solving” a mechanics problem, in this lecture, means writing down the equations of motion; explicit integration can be postponed to numerical work.
- Generalized coordinates label instantaneous configuration, not the whole motion.
- A cyclic coordinate is a coordinate that does not appear explicitly in \(L\); its conjugate momentum is conserved.
- Canonical momentum means \(p_i=\partial L/\partial \dot q_i\), not automatically the naive mechanical \(mv\).
- In the wedge example, the constraint removes the need to solve explicitly for the contact forces.
- In the no-gravity double pendulum, the conserved \(p_\theta\) is the total angular momentum.
- In Hamiltonian mechanics, the basic variables are \(q_i\) and \(p_i\), not \(q_i\) and \(\dot q_i\).
- The Hamiltonian is to be regarded, after eliminating velocities, as a function \(H(q,p)\).
- Phase space is the space of the \(q\)’s and \(p\)’s; for one degree of freedom it is a plane with \(q\) horizontal and \(p\) vertical.
- In the rescaled oscillator example, \(q\) is not a physical length coordinate; it is an adapted coordinate chosen to make the Hamiltonian symmetric in \(q\) and \(p\).
- The geometric payoff of the rescaling is circles in \((q,p)\) space rather than ellipses in \((x,p_x)\) space.
- The phase-space “fluid” picture is an interpretive object for Hamiltonian flow: many initial points moving together under the same first-order law.

## Derivation Steps
Wedge Lagrangian and conserved momentum
1. Choose two coordinates: \(X\) for the wedge corner and \(x\) for the particle relative to that corner.
2. In the \(45^\circ\) simplification, use \(y=x\) and \(\dot y=\dot x\).
3. Write \(T_{\text{wedge}}=\frac12 M\dot X^2\).
4. Write \(T_{\text{particle}}=\frac m2[(\dot X+\dot x)^2+\dot x^2]\).
5. Write \(V=mgx\).
6. Form \(L=T-V\).
7. Compute \(p_X=\partial L/\partial \dot X\) and \(p_x=\partial L/\partial \dot x\).
8. Note that \(X\) does not appear explicitly in \(L\).
9. Conclude that \(X\) is cyclic and \(\dot p_X=0\).
10. For the translation symmetry, use \(\delta X=\epsilon,\ \delta x=0\), so the Noether quantity is just \(Q=p_X\).

Double pendulum coordinate choice and cyclic coordinate
1. Introduce \(\theta\) for the first rod and choose \(\alpha\) relative to the first rod, not relative to the vertical.
2. Suppress gravity temporarily so the full system has rotational symmetry.
3. Observe that under a global rotation, \(\theta\) shifts but \(\alpha\) stays fixed.
4. Introduce auxiliary Cartesian coordinates for the two bobs.
5. Rewrite the kinetic energy in terms of \(\theta,\alpha,\dot\theta,\dot\alpha\).
6. In the no-gravity case, inspect the result and note that \(\theta\) does not appear explicitly.
7. Conclude that \(\theta\) is cyclic and \(\dot p_\theta=0\).
8. Restore gravity and add the height-dependent potential.
9. Note that rotational symmetry is then broken, so the cyclic-coordinate argument no longer applies.

Hamilton’s equations from \(H=\sum_i \dot q_i p_i-L\)
1. Start from \(H=\sum_i \dot q_i p_i-L\).
2. Vary everything that can vary: \(q_i\), \(p_i\), and \(\dot q_i\).
3. Write
   \[
   \delta H=\sum_i(\dot q_i\,\delta p_i+p_i\,\delta\dot q_i)-\sum_i\left(\frac{\partial L}{\partial \dot q_i}\delta\dot q_i+\frac{\partial L}{\partial q_i}\delta q_i\right).
   \]
4. Use \(\partial L/\partial \dot q_i=p_i\).
5. Cancel the \(p_i\,\delta\dot q_i\) terms.
6. Use Euler-Lagrange: \(\partial L/\partial q_i=\dot p_i\).
7. Obtain \(\delta H=\sum_i \dot q_i\,\delta p_i-\dot p_i\,\delta q_i\).
8. Compare with the calculus identity
   \[
   \delta H=\sum_i\left(\frac{\partial H}{\partial q_i}\delta q_i+\frac{\partial H}{\partial p_i}\delta p_i\right).
   \]
9. Match coefficients of \(\delta p_i\) and \(\delta q_i\).
10. Read off
   \[
   \frac{\partial H}{\partial p_i}=\dot q_i,\qquad \frac{\partial H}{\partial q_i}=-\dot p_i.
   \]

Rescaling the harmonic oscillator
1. Begin with \(L=\frac12 m\dot x^2-\frac12 kx^2\).
2. Define \(\omega=\sqrt{k/m}\).
3. Choose a new coordinate \(q\) so that \(\frac{\omega}{2}q^2=\frac{k}{2}x^2\).
4. Infer \(q^2=\sqrt{km}\,x^2\).
5. Differentiate to get \(\dot q^{\,2}=\sqrt{km}\,\dot x^{\,2}\).
6. Rewrite the kinetic term \(\frac12 m\dot x^2\) as \(\frac{1}{2\omega}\dot q^{\,2}\).
7. Rewrite the potential term as \(\frac{\omega}{2}q^2\).
8. Obtain the rescaled Lagrangian \(L=\frac{1}{2\omega}\dot q^{\,2}-\frac{\omega}{2}q^2\).

Oscillator Hamiltonian and phase-space circles
1. Compute \(p=\partial L/\partial \dot q=\dot q/\omega\).
2. Solve for the velocity: \(\dot q=\omega p\).
3. Insert this into \(H=\dot q\,p-L\).
4. Simplify to \(H=\frac{\omega}{2}(p^2+q^2)\).
5. Set \(H=\text{const}\).
6. Divide by \(\omega/2\) to obtain \(p^2+q^2=\text{const}\).
7. Interpret the constant-energy trajectories as circles in phase space.

Hamiltonian first-order equations to the usual oscillator equation
1. Start from \(H=\frac{\omega}{2}(p^2+q^2)\).
2. Differentiate with respect to \(p\): \(\dot q=\partial H/\partial p=\omega p\).
3. Differentiate with respect to \(q\): \(\dot p=-\partial H/\partial q=-\omega q\).
4. Time-differentiate \(\dot q=\omega p\).
5. Get \(\ddot q=\omega \dot p\).
6. Substitute \(\dot p=-\omega q\).
7. Obtain \(\ddot q=-\omega^2 q\).

Euler-Lagrange form versus Hamiltonian form for the oscillator
1. From the rescaled Lagrangian, compute \(\partial L/\partial \dot q=\dot q/\omega\).
2. Differentiate with respect to time:
   \[
   \frac{d}{dt}\left(\frac{\dot q}{\omega}\right).
   \]
3. Compute \(\partial L/\partial q=-\omega q\).
4. Apply Euler-Lagrange:
   \[
   \frac{d}{dt}\left(\frac{\dot q}{\omega}\right)=-\omega q.
   \]
5. Rewrite as \(\ddot q/\omega=-\omega q\).
6. Multiply by \(\omega\) to recover \(\ddot q=-\omega^2 q\).
7. Interpret the Hamiltonian pair as two first-order equations equivalent to one second-order equation.

## Notation Choices
- Use lowercase \(p_i\) for canonical momenta in the prose and displayed equations.
- When discussing `lecture_06_figure_02.png`, note explicitly that the board writes uppercase \(P_\theta\).
- Keep the wedge coordinates as \(X\) and \(x\), with \(X\) the wedge coordinate and \(x\) the particle coordinate relative to the corner.
- Do not reuse the wedge slope angle \(\alpha\) outside the wedge subsection; the double pendulum’s \(\alpha\) is the important long-lived notation in the chapter.
- For the double pendulum, keep \((\theta,\alpha)\) as the main variables and mention \(\phi\) only as the rejected alternative coordinate.
- Treat the double-pendulum auxiliary coordinates \(x,y,x',y'\) as temporary kinematic variables, not independent degrees of freedom.
- Keep the Hamiltonian derivation in indexed form when giving the general equations: \(q_i,p_i\).
- Use \(\delta q_i,\delta p_i\) for infinitesimal variations in the Hamiltonian derivation.
- Use \(\epsilon\) for symmetry shifts in Noether-style transformations.
- Write Hamilton’s equations as
  \[
  \frac{\partial H}{\partial p_i}=\dot q_i,\qquad \frac{\partial H}{\partial q_i}=-\dot p_i
  \]
  with the minus sign attached to the \(q_i\)-derivative equation.
- In the oscillator section, distinguish carefully between the rescaled pair \((q,p)\) and the ordinary pair \((x,p_x)\).
- State explicitly that the oscillator \(p\) conjugate to the rescaled \(q\) is not the same object as the ordinary mechanical momentum \(p_x\).
- Keep phase-space axes as \(q\) horizontal and \(p\) vertical, matching the lecture.

## Uncertain Mathematics
- The double-pendulum kinetic-energy line has unstable sign conventions in the lecture. The safest screenshot-backed form is the visible board line, but it should not be over-normalized without a consistency check.
- In the double pendulum, the verbal description of the first angle and the auxiliary-coordinate formulas are not perfectly aligned. The formulas \(x=\sin\theta,\ y=\cos\theta\) should be treated as the primary kinematic definition.
- The gravity term for the double pendulum should be stated cautiously: the transcript clearly gives a sum of cosine terms, but the overall sign depends on the choice of vertical axis and on whether one is writing \(V\) or \(L=T-V\).
- The transcript region around roughly \(00{:}44{:}27\) to \(00{:}44{:}57\) is garbled; do not infer new formal mathematics from it.
- In the wedge example, the spoken identification of the conserved momentum with “the total momentum” is not fully clean relative to the earlier relative-coordinate choice. Keep \(p_X=\partial L/\partial \dot X\) as the safe formal statement.
- The intermediate Hamiltonian variation line is only partly legible on the board; \(\delta H=\sum_i \dot q_i\,\delta p_i-\dot p_i\,\delta q_i\) is a safe standard reconstruction, not a full direct transcription.
- The oscillator rescaling discussion is algebraically usable but verbally messy. Keep the essential relations \(\omega=\sqrt{k/m}\), \(\frac{\omega}{2}q^2=\frac{k}{2}x^2\), and \(L=\frac{1}{2\omega}\dot q^{\,2}-\frac{\omega}{2}q^2\); avoid overcommitting on the units discussion beyond “\(q\) is no longer a length.”
- The orbit direction in phase space is not stable in the lecture; Susskind verbally corrects himself between counterclockwise and clockwise. The safe content is circular motion at angular speed \(\omega\), not the orientation.
- The statement “forces are derivatives of the potential” should be presented with sign discipline: in coordinate form the safe mechanics statement is \(\dot p_i=\partial L/\partial q_i\), and only after specifying \(L=T-V\) does one recover the usual minus sign against \(\partial V/\partial q_i\).