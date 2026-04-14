# Math Bank
## Core Equations
- Aristotle’s intentionally wrong law: \(\vec F = m\vec v\) [visible]
- One-dimensional Aristotle law: \(F = m\dot x\) [transcript-backed]
- Discrete velocity approximation: \(\dot x(t) \approx \dfrac{x(t+\delta)-x(t)}{\delta}\) [transcript-backed]
- Aristotle update rule: \(x(t+\delta)=x(t)+\dfrac{\delta}{m}F(t)\) [transcript-backed]
- No-force Aristotle case: \(F=0 \Rightarrow \dot x=0\) [transcript-backed]
- Spring force: \(F(x)=-kx\) [transcript-backed]
- Aristotle spring update: \(x(t+\delta)=\left(1-\dfrac{k\delta}{m}\right)x(t)\) [transcript-backed]
- Continuous Aristotle spring equation: \(m\dot x=-kx\) [standard reconstruction]
- Aristotle spring solution: \(x(t)=x(0)e^{-kt/m}\) [transcript-backed]

- Newton’s second law in one dimension: \(F=m\ddot x\) [transcript-backed]
- Discrete acceleration approximation: \(\ddot x(t)\approx \dfrac{x(t+\delta)-2x(t)+x(t-\delta)}{\delta^2}\) [transcript-backed]
- Newton update rule in second-order form: \(x(t+\delta)=2x(t)-x(t-\delta)+\dfrac{\delta^2}{m}F(t)\) [standard reconstruction]

- Momentum definition: \(p=m\dot x\) [visible]
- Newton in momentum form on the board: \(F=\dot P\) [visible]
- Normalized momentum equation: \(\dot p=F\) [standard reconstruction]
- Vector momentum form: \(\vec F=\dfrac{d\vec p}{dt}\) [standard reconstruction]
- Position update from momentum: \(\dot x=\dfrac{p}{m}\) [standard reconstruction]

- Harmonic-oscillator equation: \(m\ddot x=-kx\) [transcript-backed]
- Normalized oscillator equation: \(\ddot x=-x\) [transcript-backed]
- Oscillator solution: \(x(t)=c\cos(t-t_0)\) [standard reconstruction]
- Corresponding momentum for \(m=1\): \(p(t)=-c\sin(t-t_0)\) [standard reconstruction]
- Phase-space invariant: \(x^2+p^2=c^2\) [transcript-backed]

- Time-reversal action on derivatives: \(t\mapsto -t,\ \dot x\mapsto -\dot x,\ \ddot x\mapsto \ddot x\) [transcript-backed]

- Newton’s third-law pair: \(\vec F_{ij}=-\vec F_{ji}\) [transcript-backed]
- Equation of motion for particle \(i\): \(\dot{\vec p}_i=\sum_{j\ne i}\vec F_{ij}\) [transcript-backed]
- Total momentum conservation: \(\dfrac{d\vec P_{\text{tot}}}{dt}=0\) [transcript-backed]

- One-dimensional potential-force relation: \(F(x)=-\dfrac{dV(x)}{dx}\) [visible]
- Potential from force: \(V(x)=-\int^x F(u)\,du+\text{const}\) [transcript-backed]
- One-dimensional energy: \(E=\dfrac12 m\dot x^2+V(x)\) [visible]
- Chain rule for the potential: \(\dfrac{dV}{dt}=\dfrac{dV}{dx}\dot x\) [transcript-backed]
- One-dimensional energy derivative: \(\dfrac{dE}{dt}=m\dot x\,\ddot x+\dfrac{dV}{dx}\dot x\) [standard reconstruction]
- Factored one-dimensional energy derivative: \(\dfrac{dE}{dt}=\dot x\!\left(m\ddot x+\dfrac{dV}{dx}\right)=0\) [standard reconstruction]

- Multidimensional Newton equation in components: \(F_i(\mathbf x)=m\ddot x_i\) [transcript-backed]
- Multidimensional conservative-force law: \(F_i(\mathbf x)=-\dfrac{\partial V(\mathbf x)}{\partial x_i}\) [visible]
- Gradient form: \(\vec F=-\nabla V\) [standard reconstruction]
- One-particle, many-coordinate energy: \(E=\dfrac12 m\sum_i \dot x_i^2+V(x_1,\dots,x_n)\) [transcript-backed]
- Multidimensional chain rule: \(\dfrac{dV}{dt}=\sum_i \dfrac{\partial V}{\partial x_i}\dot x_i\) [transcript-backed]
- Multidimensional energy derivative: \(\dfrac{dE}{dt}=\sum_i \dot x_i\!\left(m\ddot x_i+\dfrac{\partial V}{\partial x_i}\right)=0\) [standard reconstruction]

- Many-particle energy: \(E=\sum_{i=1}^{3N}\dfrac12 m_i\dot x_i^2+V(x_1,\dots,x_{3N})\) [transcript-backed]
- Many-particle conservative-force form: \(F_i=-\dfrac{\partial V}{\partial x_i}\) [transcript-backed]

- Spring potential: \(V(x)=\dfrac{k}{2}x^2\) [transcript-backed]
- Oscillator energy: \(E=\dfrac12 m\dot x^2+\dfrac{k}{2}x^2\) [transcript-backed]
- Normalized oscillator energy: \(E=\dfrac12(\dot x^2+x^2)\) [standard reconstruction]

## Definitions And Objects
- Force in Aristotle’s test law is taken to be proportional to velocity, not acceleration; this law is studied as a deliberately wrong candidate law of motion.
- Momentum is introduced by definition as \(p=m\dot x\), with mass treated as constant in Newtonian mechanics.
- The Newtonian state of a one-dimensional particle is \((x,p)\), or equivalently \((x,\dot x)\).
- Phase space is the space of positions together with momenta; it is the space of initial data needed for prediction.
- A closed system is one with no external forces, only forces between the particles inside the system.
- In one dimension, if \(F\) depends only on position and is integrable, one can define a potential \(V(x)\) by \(F=-dV/dx\).
- Kinetic energy is \(T=\dfrac12 m\dot x^2\) in one dimension, and \(T=\dfrac12 m\sum_i \dot x_i^2\) for one particle in several coordinates.
- Total energy is \(E=T+V\).
- In several dimensions, a force is conservative when its components are derivatives of one scalar potential: \(F_i=-\partial V/\partial x_i\).
- For many particles, Susskind flattens all coordinates into a single list \(x_i\), \(i=1,\dots,3N\), with corresponding masses \(m_i\).

## Derivation Steps
Aristotle update law
1. Start from the wrong law \(F=m\dot x\).
2. Replace \(\dot x(t)\) by the discrete difference \(\dfrac{x(t+\delta)-x(t)}{\delta}\).
3. Multiply by \(\delta/m\).
4. Solve for \(x(t+\delta)\).
5. Obtain \(x(t+\delta)=x(t)+\dfrac{\delta}{m}F(t)\).

Aristotle spring decay
1. Insert the spring force \(F(x)=-kx\) into the Aristotle update rule.
2. Get \(x(t+\delta)=\left(1-\dfrac{k\delta}{m}\right)x(t)\).
3. Interpret the factor as slightly less than \(1\) for small \(\delta\).
4. Conclude that repeated updates shrink \(x\) geometrically toward the origin.
5. In the continuous version, solve \(m\dot x=-kx\) to obtain \(x(t)=x(0)e^{-kt/m}\).

Newton requires two pieces of initial data
1. Start from \(F=m\ddot x\).
2. Approximate \(\ddot x\) by a second finite difference.
3. Rearrange to solve for \(x(t+\delta)\).
4. Observe that the result depends on both \(x(t)\) and \(x(t-\delta)\).
5. Translate that into continuous language: one needs both position and velocity initially.

Newton as two first-order equations
1. Define momentum \(p=m\dot x\).
2. Rewrite Newton’s law as \(\dot p=F\).
3. Rewrite the momentum definition as \(\dot x=p/m\).
4. Treat \(x\) and \(p\) as separate dynamical variables.
5. Conclude that Newtonian mechanics is predictive once the state is taken to be \((x,p)\).

Harmonic oscillator in phase space
1. Start from \(m\ddot x=-kx\).
2. Normalize to \(m=k=1\), giving \(\ddot x=-x\).
3. Use the oscillatory solution \(x(t)=c\cos(t-t_0)\).
4. Differentiate to get the corresponding momentum/velocity.
5. Compute \(x^2+p^2\) and find the constant \(c^2\).
6. Interpret the motion as a circle in phase space rather than decay to a point.

Momentum conservation from Newton’s third law
1. For each particle, write \(\dot{\vec p}_i=\sum_{j\ne i}\vec F_{ij}\).
2. Sum over all particles \(i\).
3. Pair each \(\vec F_{ij}\) with \(\vec F_{ji}\).
4. Use \(\vec F_{ij}=-\vec F_{ji}\) to cancel every internal-force pair.
5. Conclude \(\dfrac{d\vec P_{\text{tot}}}{dt}=0\).

One-dimensional energy conservation
1. Assume \(F(x)=-dV/dx\).
2. Define \(E=\dfrac12 m\dot x^2+V(x)\).
3. Differentiate the kinetic term: \(\dfrac{d}{dt}\left(\dfrac12 m\dot x^2\right)=m\dot x\,\ddot x\).
4. Differentiate the potential term by the chain rule: \(\dfrac{dV}{dt}=\dfrac{dV}{dx}\dot x\).
5. Add the two derivatives.
6. Factor out \(\dot x\).
7. Use Newton’s law \(m\ddot x=F=-dV/dx\) to make the bracket vanish.
8. Conclude \(\dfrac{dE}{dt}=0\).

Potential of the spring
1. Start from \(F=-kx\).
2. Impose \(F=-dV/dx\).
3. Obtain \(dV/dx=kx\).
4. Integrate with respect to \(x\).
5. Choose \(V(x)=\dfrac{k}{2}x^2\) up to an additive constant.

Multidimensional energy conservation
1. Assume \(F_i=-\partial V/\partial x_i\).
2. Define \(E=\dfrac12 m\sum_i \dot x_i^2+V(x_1,\dots,x_n)\).
3. Differentiate the kinetic term to get \(m\sum_i \dot x_i\ddot x_i\).
4. Differentiate the potential by the multivariable chain rule: \(\dfrac{dV}{dt}=\sum_i \dfrac{\partial V}{\partial x_i}\dot x_i\).
5. Combine the sums.
6. Factor \(\dot x_i\) in each term.
7. Use \(m\ddot x_i=-\partial V/\partial x_i\).
8. Conclude \(\dfrac{dE}{dt}=0\).

Many-particle extension
1. Replace one particle in several coordinates by all coordinates of all particles, flattened into \(x_i\), \(i=1,\dots,3N\).
2. Allow corresponding masses \(m_i\).
3. Assume the force components come from one scalar \(V(x_1,\dots,x_{3N})\).
4. Repeat the same energy-derivative computation coordinate by coordinate.
5. Obtain conservation of the total energy for the full system.

## Notation Choices
- Use lower-case \(x,v,p\) for position, velocity, and momentum in normalized chapter prose.
- Reserve upper-case \(V\) for potential energy; do not follow the board’s uppercase \(V\) for velocity.
- Use \(\vec F,\vec p,\vec x\) or bold equivalents for vectors; switch to components \(F_i,x_i\) when discussing gradients.
- Use overdots for time derivatives throughout: \(\dot x,\ddot x,\dot p\).
- Use \(\delta\) for the discrete time step; the transcript briefly wobbles between \(\epsilon\) and \(\delta\), but \(\delta\) is the cleaner choice.
- Use \(F_{ij}\) to mean “force on particle \(i\) due to particle \(j\),” and state that convention once.
- In the many-particle section, flatten coordinates into \(x_i\), \(i=1,\dots,3N\), exactly as Susskind does late in the lecture.
- Use \(T\) only when naming the standard decomposition \(E=T+V\); otherwise write the kinetic term explicitly to avoid conflict with time \(t\).
- Use \(c\) and \(t_0\) for the oscillator integration constants.
- Introduce \(\nabla V\) only after writing the component law \(F_i=-\partial V/\partial x_i\).
- Keep \(P_{\text{tot}}\) or \(\vec P_{\text{tot}}\) for total momentum, distinct from single-particle \(p\).

## Uncertain Mathematics
- The Aristotle discrete algebra is garbled in the transcript; the cleaned update rule is clear, but the spoken intermediate rearrangements should not be quoted too literally.
- The Newton finite-difference rearrangement also contains sign confusion and audience corrections; use the standard cleaned second-difference formula, not the unstable spoken line-by-line board algebra.
- The continuous Aristotle spring equation is sign-wobbly in the transcript; use the sign consistent with \(F=-kx\) and the decaying solution \(x(t)=x(0)e^{-kt/m}\).
- The oscillator solution is verbally loose about sine versus cosine and about the sign of the momentum/velocity relation; the safest invariant facts are “two constants of integration” and \(x^2+p^2=c^2\).
- The board writes uppercase \(P,V,X\) in places; the final notes should normalize without implying that the board capitalization had formal meaning.
- The third-law notation with indices is verbally messy; the chapter should use a clean convention and not preserve transcript confusion about index order.
- The “line of centers” part of Newton’s third law is discussed qualitatively and tied forward to angular momentum; it should not be overformalized here unless later lecture material supports it.
- In one dimension, the existence of \(V(x)\) is treated as automatic for sufficiently nice \(F(x)\); in several dimensions, the existence of a single scalar potential is explicitly not automatic and must be stated as a physical assumption.
- Near the end, Susskind informally says motion lies on curves of constant \(\dot x^2+V(x)\); for the final notes, restore the proper factors and write the conserved quantity as \(E=\frac12 m\dot x^2+V(x)\).
- In the normalized oscillator discussion, the transcript sometimes slides between \(p\) and \(\dot x\); the chapter should explain once when \(p=\dot x\) only because \(m=1\).