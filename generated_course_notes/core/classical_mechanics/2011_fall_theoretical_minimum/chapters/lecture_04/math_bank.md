# Math Bank
## Core Equations
- [transcript-backed] \(\delta f=\frac{\partial f}{\partial x}\,\delta x+\frac{\partial f}{\partial y}\,\delta y\)
- [transcript-backed] \(\delta f=0\)
- [standard reconstruction] \(S=\int_{t_1}^{t_2}L(q,\dot q,t)\,dt\)
- [transcript-backed] \(\delta S=0\)
- [standard reconstruction] \(\frac{d}{dt}\frac{\partial L}{\partial \dot q_i}-\frac{\partial L}{\partial q_i}=0\)
- [transcript-backed] \(p_i=\frac{\partial L}{\partial \dot q_i}\)
- [transcript-backed] \(\dot p_i=\frac{\partial L}{\partial q_i}\)
- [transcript-backed] \(\frac{\partial L}{\partial q_i}=0 \;\Rightarrow\; \dot p_i=0\)

- [visible] \(\frac{m\dot x^{2}}{2}-V(x)\)
- [standard reconstruction] \(L=\frac{m\dot x^{2}}{2}-V(x)\)
- [transcript-backed] \(\frac{\partial L}{\partial \dot x}=m\dot x\)

- [visible] \(\frac{\dot q_1^{\,2}+\dot q_2^{\,2}}{2}-V(q_1-q_2)\)
- [standard reconstruction] \(L=\frac{\dot q_1^{\,2}+\dot q_2^{\,2}}{2}-V(q_1-q_2)\)
- [visible] \(\dot P_1=-V'(q_1-q_2)\)
- [standard reconstruction] \(\dot P_2=+V'(q_1-q_2)\)
- [standard reconstruction] \(\frac{d}{dt}(P_1+P_2)=0\)

- [transcript-backed] \(L=\frac{\dot q_1^{\,2}+\dot q_2^{\,2}}{2}-V(Aq_1+Bq_2)\)
- [standard reconstruction] \(\dot P_1=-A\,V'(Aq_1+Bq_2)\)
- [standard reconstruction] \(\dot P_2=-B\,V'(Aq_1+Bq_2)\)
- [standard reconstruction] \(\frac{d}{dt}(B P_1-A P_2)=0\)

- [transcript-backed] \(Q_1=\sqrt m\,X,\qquad Q_2=\sqrt M\,Y\)
- [transcript-backed] \(L=\frac{\dot Q_1^{\,2}}{2}+\frac{\dot Q_2^{\,2}}{2}-V\!\left(\frac{Q_1}{\sqrt m}-\frac{Q_2}{\sqrt M}\right)\)
- [transcript-backed] \(Q_2=-\sqrt M\,Y \;\Rightarrow\; V\!\left(\frac{Q_1}{\sqrt m}+\frac{Q_2}{\sqrt M}\right)\)

- [transcript-backed] \(L=\frac{\dot q^{2}}{2}\)
- [transcript-backed] \(q'=q+\delta,\qquad \dot q'=\dot q\)
- [transcript-backed] \(\delta L=0\)
- [transcript-backed] \(\dot p=0\)

- [transcript-backed] \(q_1'=q_1+\delta,\qquad q_2'=q_2+\delta\)
- [transcript-backed] \(q_1'=q_1+b\,\delta,\qquad q_2'=q_2-a\,\delta\)

- [transcript-backed] \(L=\frac{m}{2}\big(\dot x^2+\dot y^2\big)-V(x^2+y^2)\)
- [transcript-backed] \(x'=x\cos\theta+y\sin\theta,\qquad y'=-x\sin\theta+y\cos\theta\)
- [transcript-backed] \(\cos\delta\simeq 1,\qquad \sin\delta\simeq \delta\)
- [transcript-backed] \(\delta x=y\,\delta,\qquad \delta y=-x\,\delta\)
- [transcript-backed] \(\delta\dot x=\dot y\,\delta,\qquad \delta\dot y=-\dot x\,\delta\)
- [transcript-backed] \(\delta(x^2+y^2)=2x\,\delta x+2y\,\delta y\)
- [transcript-backed] \(\delta(x^2+y^2)=0\)
- [transcript-backed] \(\delta(\dot x^2+\dot y^2)=0\)

- [transcript-backed] \(\delta q_i=\delta\,f_i(q)\)
- [transcript-backed] \(\delta \dot q_i=\frac{d}{dt}\,\delta q_i\)
- [transcript-backed] \(\delta L=\sum_i \frac{\partial L}{\partial q_i}\,\delta q_i+\sum_i \frac{\partial L}{\partial \dot q_i}\,\delta\dot q_i\)
- [standard reconstruction] \(\delta L=\sum_i \dot p_i\,\delta q_i+\sum_i p_i\,\delta\dot q_i\)
- [standard reconstruction] \(\delta L=\frac{d}{dt}\sum_i p_i\,\delta q_i\)
- [standard reconstruction] \(\delta L=\delta\,\frac{d}{dt}\sum_i p_i f_i(q)\)
- [standard reconstruction] \(\delta L=0 \;\Rightarrow\; \frac{d}{dt}\sum_i p_i f_i(q)=0\)
- [standard reconstruction] \(Q=\sum_i p_i f_i(q)\)

- [transcript-backed] \(Q_{\text{rot}}=p_x\,y-p_y\,x\)
- [standard reconstruction] \(J=xp_y-yp_x\)

- [transcript-backed] \(L=\frac{\dot q^2}{2}-\frac{q^2}{2}\)
- [transcript-backed] \(p=\frac{\partial L}{\partial \dot q}=\dot q\)
- [transcript-backed] \(\dot p=-q\)
- [transcript-backed] \(\dot q=p\)

- [transcript-backed] \(q\mapsto -q,\qquad \dot q\mapsto -\dot q\)

- [transcript-backed] \(m\ddot x=-c\dot x\)
- [transcript-backed] \(\dot p=-\frac{c}{m}\,p\)
- [transcript-backed] \(p(t)\propto e^{-ct/m}\)

## Definitions And Objects
- The action \(S\): the time integral of the Lagrangian between two endpoints.
- First-order variation \(\delta\): the linear change under a small shift; terms of order \(\delta^2\) are dropped.
- Generalized coordinates \(q_i\): the lecture’s preferred coordinates once Cartesian \(x_i\) are abandoned.
- Canonical momentum \(p_i\): the momentum conjugate to \(q_i\), defined by \(p_i=\partial L/\partial \dot q_i\).
- Cyclic coordinate: a coordinate absent from \(L\), so that its conjugate momentum is conserved.
- Prime on the potential, \(V'(\cdot)\): derivative with respect to the argument of \(V\), not directly with respect to \(q_1\) or \(q_2\).
- Symmetry transformation: a change of coordinates or an active shift of the system that leaves \(L\) unchanged.
- Continuous symmetry: a symmetry built from infinitesimal steps.
- Discrete symmetry: a symmetry like \(q\to -q\) that is not built from infinitesimal steps in this lecture’s framework.
- Central potential: a potential depending only on distance from the origin, here represented as \(V(x^2+y^2)\).
- Conserved quantity \(Q\): in the general theorem, \(Q=\sum_i p_i f_i(q)\).
- Time-independent symmetry parameter: the lecture restricts the main derivation to fixed translations or fixed rotations, not explicitly time-dependent transformations.

## Derivation Steps
First-order variation and stationary condition
1. Introduce a universal infinitesimal parameter \(\delta\).
2. Write the first-order change of a function as \(\delta f=f_x\,\delta x+f_y\,\delta y\).
3. Discard all quadratic and higher powers of \(\delta\).
4. Impose stationarity by setting \(\delta f=0\).

Euler-Lagrange recap
1. Start from \(S=\int L(q,\dot q,t)\,dt\).
2. Vary the path slightly while fixing the endpoints.
3. Separate the variation into a coordinate part and a velocity part.
4. Set the first-order change \(\delta S\) equal to zero.
5. Read off the Euler–Lagrange equation \(\frac{d}{dt}\frac{\partial L}{\partial \dot q_i}-\frac{\partial L}{\partial q_i}=0\).
6. Define \(p_i=\partial L/\partial \dot q_i\) to rewrite it as \(\dot p_i=\partial L/\partial q_i\).

One-dimensional momentum check
1. Use \(L=\frac{m\dot x^2}{2}-V(x)\).
2. Differentiate with respect to \(\dot x\).
3. Obtain \(\partial L/\partial \dot x=m\dot x\).
4. Identify canonical momentum with ordinary momentum in this example.

Two-coordinate separation potential
1. Use \(L=\frac{\dot q_1^2+\dot q_2^2}{2}-V(q_1-q_2)\).
2. Differentiate with respect to \(q_1\) to get \(\dot P_1=-V'(q_1-q_2)\).
3. Differentiate with respect to \(q_2\); the chain rule adds an extra minus sign from \(q_1-q_2\), giving \(\dot P_2=+V'(q_1-q_2)\).
4. Add the two equations.
5. Conclude \(\frac{d}{dt}(P_1+P_2)=0\).

General \(Aq_1+Bq_2\) potential
1. Use \(L=\frac{\dot q_1^2+\dot q_2^2}{2}-V(Aq_1+Bq_2)\).
2. Differentiate with respect to \(q_1\) to pull out a factor \(A\): \(\dot P_1=-A\,V'(Aq_1+Bq_2)\).
3. Differentiate with respect to \(q_2\) to pull out a factor \(B\): \(\dot P_2=-B\,V'(Aq_1+Bq_2)\).
4. Multiply the first equation by \(B\) and the second by \(A\).
5. Subtract.
6. Conclude \(\frac{d}{dt}(BP_1-AP_2)=0\).

Translation symmetry
1. Start with the free-particle Lagrangian \(L=\dot q^2/2\).
2. Shift the coordinate by a constant: \(q\to q+\delta\).
3. Observe that \(\dot q\) does not change because \(\delta\) is constant.
4. Therefore \(L\) is unchanged: \(\delta L=0\).
5. Separately, because \(L\) has no \(q\)-dependence, \(\dot p=0\).

Common translation of two coordinates
1. Shift \(q_1\to q_1+\delta\) and \(q_2\to q_2+\delta\).
2. The velocities \(\dot q_1,\dot q_2\) are unchanged.
3. The difference \(q_1-q_2\) is unchanged.
4. Therefore both kinetic and potential terms are unchanged.
5. Match this symmetry to the conserved quantity \(P_1+P_2\).

Asymmetric translation for \(V(Aq_1+Bq_2)\)
1. Shift \(q_1\to q_1+b\delta\) and \(q_2\to q_2-a\delta\).
2. The velocities are unchanged because the shifts are constant.
3. The combination \(Aq_1+Bq_2\) changes by \(Ab\delta-Ba\delta=0\).
4. Therefore \(L\) is unchanged.
5. Match this symmetry to the conserved quantity \(BP_1-AP_2\).

Infinitesimal rotation
1. Start from \(x'=x\cos\theta+y\sin\theta\), \(y'=-x\sin\theta+y\cos\theta\).
2. Set \(\theta=\delta\) small.
3. Replace \(\cos\delta\) by \(1\) and \(\sin\delta\) by \(\delta\).
4. Read off \(\delta x=y\delta\), \(\delta y=-x\delta\).
5. Differentiate to get \(\delta\dot x=\dot y\,\delta\), \(\delta\dot y=-\dot x\,\delta\).
6. Compute \(\delta(x^2+y^2)=2x\,\delta x+2y\,\delta y=0\).
7. Repeat the same calculation for \(\dot x^2+\dot y^2\).
8. Conclude that both the potential and kinetic pieces are unchanged.

General symmetry to conserved quantity
1. Assume an infinitesimal transformation \(\delta q_i=\delta\,f_i(q)\).
2. Write \(\delta\dot q_i=d(\delta q_i)/dt\).
3. Expand \(\delta L=\sum_i (\partial L/\partial q_i)\delta q_i+\sum_i (\partial L/\partial \dot q_i)\delta\dot q_i\).
4. Use the equations of motion to replace \(\partial L/\partial q_i\) by \(\dot p_i\).
5. Use \(p_i=\partial L/\partial \dot q_i\).
6. Recognize \(\sum_i \dot p_i\,\delta q_i+\sum_i p_i\,\delta\dot q_i\) as \(\frac{d}{dt}\sum_i p_i\,\delta q_i\).
7. Substitute \(\delta q_i=\delta f_i(q)\).
8. Factor out the common infinitesimal \(\delta\).
9. If the transformation is a symmetry, set \(\delta L=0\).
10. Conclude \(\frac{d}{dt}\sum_i p_i f_i(q)=0\).

Recovering momentum and angular momentum
1. For common translation, take \(f_1=f_2=1\).
2. Insert into \(Q=\sum_i p_i f_i\).
3. Get \(Q=P_1+P_2\).
4. For the asymmetric example, take \(f_1=B\), \(f_2=-A\).
5. Get \(Q=BP_1-AP_2\).
6. For rotation, take \(f_x=y\), \(f_y=-x\).
7. Get \(Q=p_x y-p_y x\), i.e. angular momentum up to convention.

Harmonic oscillator in \(p\)-\(q\) space
1. Use \(L=\dot q^2/2-q^2/2\).
2. Define \(p=\partial L/\partial \dot q=\dot q\).
3. Compute \(\dot p=\partial L/\partial q=-q\).
4. Use the definition of \(p\) to write \(\dot q=p\).
5. Read the pair \(\dot q=p\), \(\dot p=-q\) as uniform circular motion in the \(p\)-\(q\) plane.

Viscous-drag counterexample
1. Consider \(m\ddot x=-c\dot x\).
2. Note that \(x\to x+\delta\) leaves \(\dot x\) and \(\ddot x\) unchanged.
3. Therefore the equation is translation invariant.
4. Rewrite with \(p=m\dot x\) as \(\dot p=-(c/m)p\).
5. Solve to get exponential decay, not conservation.
6. Conclude that symmetry alone is not enough; the least-action framework matters.

## Notation Choices
- Use \(q_i\) for generalized coordinates throughout the main chapter.
- Use \(x,y\) only when the lecture intentionally returns to Cartesian coordinates in the plane.
- Use lowercase \(p_i\) for the general derivation and general statements.
- Preserve uppercase \(P_1,P_2\) when presenting the two-coordinate board example close to the screenshots; note \(P_i\) is the same canonical momentum object.
- Use overdots for time derivatives everywhere.
- Use \(\delta\) in two roles, but distinguish them by context:
  the universal infinitesimal parameter;
  the induced first-order variation, as in \(\delta q_i\) or \(\delta L\).
- Use \(V'(u)\) to mean derivative of \(V\) with respect to its single argument \(u\).
- Use \(f_i(q)\) for the components of the infinitesimal generator in \(\delta q_i=\delta f_i(q)\).
- Use uppercase \(Q\) only for the conserved quantity from the symmetry derivation; do not let it collide with coordinate symbols \(q_i\).
- For angular momentum, choose one final convention in the notes and stick to it. Recommended: \(J=xp_y-yp_x\). Mention once that the lecture also writes the equivalent quantity in the reordered form \(p_x y-p_y x\).
- Keep the lecture restricted to time-independent symmetry parameters in the main theorem; do not insert extra time-dependent terms unless explicitly moving beyond this lecture.

## Uncertain Mathematics
- The transcript recap of Euler–Lagrange is garbled. The final notes should use the clean standard equation, not the ASR fragments.
- In the \(V(q_1-q_2)\) example, the sign discussion wobbles live. The mathematically consistent final form is \(\dot P_1=-V'(q_1-q_2)\), \(\dot P_2=+V'(q_1-q_2)\).
- In the \(V(Aq_1+Bq_2)\) example, the transcript briefly drifts toward \(BP_1+AP_2\), but the algebra and later verbal summary support \(BP_1-AP_2\).
- In the unequal-mass rescaling example, the change of variables is illustrative rather than fully polished. The final notes should present only the clean coordinate rescaling and the resulting argument dependence, not every spoken false start.
- Susskind explicitly says he may have the sine sign wrong in the finite rotation formulas. The final notes should use one mathematically consistent rotation convention and keep the infinitesimal formulas aligned with it.
- The angular-momentum sign/order is not stable in the spoken lecture. Resolve it once in the notes.
- The harmonic-oscillator phase-space orientation is axis-convention dependent. Only state clockwise/counterclockwise if the axes are explicitly fixed.
- The claim about reflection symmetry should be phrased carefully: the lecture’s point is not that reflection is physically meaningless, but that this infinitesimal continuous-symmetry derivation does not produce a conserved quantity for a discrete symmetry.
- The viscous-drag discussion should also be phrased carefully: it is not a counterexample to Noether’s theorem, but to the naive slogan “symmetry of any equation implies conservation.”
- The stationary-versus-least-action passage is conceptually clear but transcriptually messy. Keep the robust claim only: the action is generally stationary, often a saddle, not usually a minimum.