# Math Bank
## Core Equations
- \(\displaystyle \frac{\partial \mathcal{L}}{\partial V_i}=P_i\) [visible]
- \(\displaystyle H(P)=\sum_i P_iV_i-\mathcal{L}\) [standard reconstruction]
- \(\displaystyle p_i=m\dot x_i,\qquad \dot x_i=\frac{p_i}{m},\qquad \dot p_i=F_i\) [standard reconstruction]
- \(\displaystyle \frac{dL}{dV}=P,\qquad \frac{dH}{dP}=V\) [transcript-backed]
- \(\displaystyle L(V)=\int_0^{V}P(V')\,dV',\qquad H(P)=\int_0^{P}V(P')\,dP'\) [transcript-backed]
- \(\displaystyle H+L=PV,\qquad H=PV-L\) [transcript-backed]
- \(\displaystyle \frac{\partial L}{\partial v_i}=p_i,\qquad H=\sum_i p_iv_i-L,\qquad \frac{\partial H}{\partial p_i}=v_i\) [transcript-backed]
- \(\displaystyle v_i=\dot q_i,\qquad p_i=\frac{\partial L}{\partial \dot q_i}=\frac{\partial L}{\partial v_i}\) [transcript-backed]
- \(\displaystyle H(q,p,t)=\sum_i p_i\dot q_i-L(q,\dot q,t)\) [transcript-backed]
- \(\displaystyle \dot q_i=\frac{\partial H}{\partial p_i},\qquad \dot p_i=-\frac{\partial H}{\partial q_i}\) [transcript-backed]
- \(\displaystyle L=\frac12 m\dot x^2-U(x),\qquad p=m\dot x,\qquad H=\frac{p^2}{2m}+U(x)\) [transcript-backed]
- \(\displaystyle \frac{\partial H}{\partial p}=\frac{p}{m}=\dot x,\qquad -\frac{\partial H}{\partial x}=-\frac{dU}{dx}=\dot p\) [transcript-backed]
- \(\displaystyle \frac{dH}{dt}=\sum_i\left(\frac{\partial H}{\partial p_i}\dot p_i+\frac{\partial H}{\partial q_i}\dot q_i\right)\) [transcript-backed]
- \(\displaystyle \frac{dH}{dt}=0\) for time-independent \(H\) [transcript-backed]
- \(\displaystyle \frac{dH}{dt}=\sum_i\left(\frac{\partial H}{\partial p_i}\dot p_i+\frac{\partial H}{\partial q_i}\dot q_i\right)+\frac{\partial H}{\partial t}\) [transcript-backed]
- \(\displaystyle \frac{dH}{dt}=\frac{\partial H}{\partial t}\) when \(H\) depends explicitly on time [transcript-backed]
- \(\displaystyle H\propto p^2+x^2,\qquad p^2+x^2=\text{const}\) for the harmonic-oscillator contours after suppressing constants [standard reconstruction]
- \(\displaystyle A=A(p,q),\qquad \frac{dA}{dt}=\sum_i\left(\frac{\partial A}{\partial p_i}\dot p_i+\frac{\partial A}{\partial q_i}\dot q_i\right)\) [transcript-backed]
- \(\displaystyle L_z=xp_y-yp_x\) [transcript-backed]
- \(\displaystyle \{A,B\}=\sum_i\left(\frac{\partial A}{\partial q_i}\frac{\partial B}{\partial p_i}-\frac{\partial A}{\partial p_i}\frac{\partial B}{\partial q_i}\right)\) [standard reconstruction]
- \(\displaystyle \frac{dA}{dt}=\{A,H\}\) [transcript-backed]
- \(\displaystyle \{q_i,H\}=\dot q_i,\qquad \{p_i,H\}=\dot p_i\) [transcript-backed]
- \(\displaystyle \{A,H\}=0\iff A\ \text{is conserved}\) [transcript-backed]
- \(\displaystyle H=P^3+X^3\) and \(\displaystyle \frac{\partial H}{\partial P}=3P^2=\dot X\) as a late illustrative nonstandard Hamiltonian example [transcript-backed]

## Definitions And Objects
- Phase space: the state space containing enough data that the present state determines both the next state and the previous state.
- Phase-space flow: the motion of points \((q,p)\) under Hamilton’s equations; Susskind repeatedly treats it as a fluid or dust moving through phase space.
- One-to-one \(V\leftrightarrow P\) relation: the Legendre transform requires that velocity-type and momentum-type variables determine each other uniquely.
- \(L\): generating function thought of as a function of velocity-type variables.
- \(H\): Legendre-transform partner of \(L\), thought of as a function of momentum-type variables; in mechanics it is then viewed as \(H(q,p,t)\).
- Canonical momentum: \(p_i=\partial L/\partial \dot q_i\); only in the simple particle example does this reduce to \(m\dot x\).
- Phase-space velocity: the pair \((\dot q_i,\dot p_i)\), not just the ordinary spatial velocity.
- Conserved quantity \(A(p,q)\): any phase-space function whose time derivative vanishes.
- Constant-energy contours/surfaces: subsets of phase space with fixed \(H\), along which the phase point moves when \(H\) has no explicit time dependence.
- Poisson bracket: bilinear operation on phase-space functions used to express time evolution and conservation laws.

## Derivation Steps
One-variable Legendre reciprocity
1. Assume \(P\) and \(V\) are one-to-one functions of each other.
2. Define \(L(V)\) by \(dL/dV=P\).
3. Define \(H(P)=PV-L\), with \(V\) understood as \(V(P)\).
4. Vary \(H\): \(\delta H=P\,\delta V+V\,\delta P-(dL/dV)\delta V\).
5. Replace \(dL/dV\) by \(P\).
6. Cancel the \(P\,\delta V\) terms.
7. Read off \(\delta H=V\,\delta P\), hence \(dH/dP=V\).

Many-variable Legendre transform
1. Define \(p_i=\partial L/\partial v_i\).
2. Set \(H=\sum_i p_iv_i-L\).
3. Vary: \(\delta H=\sum_i(p_i\delta v_i+v_i\delta p_i)-\sum_i(\partial L/\partial v_i)\delta v_i\).
4. Use \(p_i=\partial L/\partial v_i\).
5. Cancel the \(\delta v_i\) terms.
6. Conclude \(\delta H=\sum_i v_i\delta p_i\).
7. Read off \(\partial H/\partial p_i=v_i\).

Hamilton’s equations from \(L(q,v)\)
1. Take \(L=L(q,v)\) with \(v_i=\dot q_i\) and \(p_i=\partial L/\partial v_i\).
2. Define \(H(q,p)=\sum_i p_iv_i-L\), with \(v=v(q,p)\).
3. Vary \(H\): \(\delta H=\sum_i(p_i\delta v_i+v_i\delta p_i)-\sum_i(\partial L/\partial q_i)\delta q_i-\sum_i(\partial L/\partial v_i)\delta v_i\).
4. Cancel the \(\delta v_i\) terms using \(p_i=\partial L/\partial v_i\).
5. Obtain \(\partial H/\partial p_i=v_i=\dot q_i\).
6. Obtain \(\partial H/\partial q_i=-\partial L/\partial q_i\).
7. Use Lagrange’s equations \(d/dt(\partial L/\partial \dot q_i)=\partial L/\partial q_i\).
8. Replace \(d/dt(\partial L/\partial \dot q_i)\) by \(\dot p_i\).
9. Conclude \(\dot p_i=-\partial H/\partial q_i\).

Ordinary-particle check
1. Start with \(L=\tfrac12 m\dot x^2-U(x)\).
2. Compute \(p=m\dot x\).
3. Form \(H=p\dot x-L=\tfrac{p^2}{2m}+U(x)\).
4. Differentiate: \(\partial H/\partial p=p/m=\dot x\).
5. Differentiate: \(-\partial H/\partial x=-\,dU/dx=\dot p\).
6. Use \(p=m\dot x\) to recover \(m\ddot x=-\,dU/dx\).

Energy conservation
1. Assume \(H\) has no explicit time dependence.
2. Write \(\dot H=\sum_i[(\partial H/\partial p_i)\dot p_i+(\partial H/\partial q_i)\dot q_i]\).
3. Substitute \(\dot q_i=\partial H/\partial p_i\) and \(\dot p_i=-\partial H/\partial q_i\).
4. Get pairwise cancellation between the two terms.
5. Conclude \(\dot H=0\).

Explicit time dependence
1. If \(H=H(q,p,t)\), include the explicit time term in the chain rule.
2. Write \(\dot H=\sum_i[(\partial H/\partial p_i)\dot p_i+(\partial H/\partial q_i)\dot q_i]+\partial H/\partial t\).
3. Cancel the first two terms using Hamilton’s equations.
4. Conclude \(\dot H=\partial H/\partial t\).

Poisson-bracket evolution
1. Start with any \(A(p,q)\).
2. Write \(\dot A=\sum_i[(\partial A/\partial p_i)\dot p_i+(\partial A/\partial q_i)\dot q_i]\).
3. Substitute \(\dot p_i=-\partial H/\partial q_i\) and \(\dot q_i=\partial H/\partial p_i\).
4. Rearrange into \(\sum_i[(\partial A/\partial q_i)(\partial H/\partial p_i)-(\partial A/\partial p_i)(\partial H/\partial q_i)]\).
5. Define that combination to be \(\{A,H\}\).
6. Specialize to \(A=q_i\) and \(A=p_i\) to recover Hamilton’s equations.
7. Set \(\dot A=0\) to get the conservation criterion \(\{A,H\}=0\).

## Notation Choices
- Use \(q_i\) for generalized coordinates in the main notes.
- Use \(v_i=\dot q_i\) when following the Legendre-transform bridge; switch back to \(\dot q_i\) once the mechanics meaning is re-established.
- Use \(p_i\) for canonical momenta throughout; do not keep the lecture’s abandoned \(\pi_i\) notation.
- Reserve uppercase \(V,P\) for the one-variable abstract Legendre-transform discussion and for the screenshot-backed board formulas.
- Write \(L(q,v,t)\) or \(L(q,\dot q,t)\) and \(H(q,p,t)\); make explicit once that \(v=v(q,p,t)\) after inversion.
- Use partial derivatives once multiple variables are present; in the single-variable Legendre discussion total and partial derivatives coincide.
- Keep summations explicit as \(\sum_i\) in the working notes, even though the lecture often suppresses the summation sign verbally.
- Use the Poisson-bracket convention
  \[
  \{A,B\}=\sum_i\left(\frac{\partial A}{\partial q_i}\frac{\partial B}{\partial p_i}-\frac{\partial A}{\partial p_i}\frac{\partial B}{\partial q_i}\right),
  \]
  and note elsewhere that sign conventions can differ.
- Use \(x,p\) for the one-dimensional particle example, but do not let that replace the general \(q_i,p_i\) notation.
- Distinguish explicit time dependence in \(H(q,p,t)\) from implicit time dependence through \(q(t),p(t)\).

## Uncertain Mathematics
- The early Newton-to-first-order board algebra around \(00{:}17\)–\(00{:}19\) is garbled; the safe content is the standard reconstruction \(p_i=m\dot x_i\), \(\dot x_i=p_i/m\), \(\dot p_i=F_i\).
- The frame only certifies the uppercase board formulas \(\partial \mathcal{L}/\partial V_i=P_i\) and \(H=\sum_iP_iV_i-\mathcal{L}\); any nearby \(q\)-dependence comes from the transcript, not the image.
- The one-variable integral formulas for \(L\) and \(H\) are defined only up to additive constants; the lecture picks lower limit \(0\) for convenience, not necessity.
- The exchange around \(01{:}05\)–\(01{:}07\) about “where the Legendre transform is” is too corrupted for fine transcription; keep only the procedural point that \(H\) is obtained from \(L\) by changing variables from velocities to momenta.
- The clean Poisson-bracket formula is a cautious reconstruction from a partly tangled spoken definition; the final notes should state one convention clearly rather than reproduce the back-and-forth.
- The explicit-time-dependence derivation near \(01{:}44\)–\(01{:}46\) is noisy in its intermediate algebra; the safe final statement is \(\dot H=\partial H/\partial t\).
- The harmonic-oscillator contour formula should be stated with constants suppressed or after rescaling; the lecture only says “essentially \(p^2+x^2\).”
- The late illustrative Hamiltonians \(H=P^3+X^3\) and \(H=XP^2+\cdots\) are heuristic examples showing that \(p\) need not be proportional to \(\dot q\); they are not developed enough to serve as main worked examples.