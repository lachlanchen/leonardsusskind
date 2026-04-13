# Math Bank
## Core Equations
- \(H=\boldsymbol{\sigma}\cdot\mathbf{p}\) [standard reconstruction]
- \(i\,\partial_t\psi=-\,i\,\boldsymbol{\sigma}\cdot\nabla\psi\) [transcript-backed]
- \(i\,\sigma^\mu \partial_\mu \psi=0\) [transcript-backed]
- \(\sigma^0=\mathbf{1}_{2\times 2}\) [transcript-backed]
- \(\{\!Q_\alpha^\dagger,Q_\beta\!\}=2\,(\sigma^\mu)_{\alpha\beta}P_\mu\) [transcript-backed]
- \(\{\!Q_\alpha^\dagger,Q_\beta\!\}=2i\,(\sigma^\mu)_{\alpha\beta}\partial_\mu\) [transcript-backed]
- \(\{Q_\alpha,Q_\beta\}=0\) [transcript-backed]
- \(\{Q_\alpha^\dagger,Q_\beta^\dagger\}=0\) [transcript-backed]
- \([Q_\alpha,P_\mu]=0,\qquad [Q_\alpha^\dagger,P_\mu]=0\) [transcript-backed]
- \([P_\mu,P_\nu]=0\) [transcript-backed]
- \(Q_\alpha=\dfrac{\partial}{\partial\theta_\alpha}+i\,(\bar\theta\sigma^\mu)_\alpha\,\partial_\mu\) [transcript-backed]
- \(\bar Q_\alpha=\dfrac{\partial}{\partial\bar\theta_\alpha}+i\,(\sigma^\mu\theta)_\alpha\,\partial_\mu\) [transcript-backed]
- \(D_\alpha=\dfrac{\partial}{\partial\theta_\alpha}-i\,(\bar\theta\sigma^\mu)_\alpha\,\partial_\mu\) [transcript-backed]
- \(\bar D_\alpha=\dfrac{\partial}{\partial\bar\theta_\alpha}-i\,(\sigma^\mu\theta)_\alpha\,\partial_\mu\) [transcript-backed]
- \(\bar D_\alpha \Phi=0\) [transcript-backed]
- \(y^\mu=x^\mu+i\,\bar\theta\sigma^\mu\theta\) [transcript-backed]
- \(\Phi=\Phi(y,\theta)\) [transcript-backed]
- \(\Phi(y,\theta)=\phi(y)+\psi(y)\theta+F(y)\theta^2\) [standard reconstruction]
- \(\Phi^\ast=\Phi^\ast(x^\mu-i\,\bar\theta\sigma^\mu\theta,\bar\theta)\) [transcript-backed]
- \(\theta^2\equiv \theta_1\theta_2\) [transcript-backed]
- \(\theta^4\equiv \theta^2\bar\theta^2\) as the product of the four independent Grassmann coordinates [transcript-backed]
- \(S=\displaystyle\int d^4x\,d^2\theta\,d^2\bar\theta\;\mathcal L_{\text{sup}}\) [transcript-backed]
- \(\mathcal L_{\text{sup}}=\Phi^\ast\Phi\) [transcript-backed]
- \(\mathcal L\sim \phi^\ast \Box\phi+\bar\psi\,\sigma^\mu\partial_\mu\psi+F^\ast F\) [standard reconstruction]
- \(\mathcal L\supset F^\ast F\) [visible]
- \(\dfrac{\partial \mathcal L}{\partial F}=0\Rightarrow F^\ast=0\), \(\dfrac{\partial \mathcal L}{\partial F^\ast}=0\Rightarrow F=0\) in the free case [transcript-backed]
- \(G_F(x-y)\propto \delta^{(4)}(x-y)\) for the auxiliary-field propagator in the no-derivative case [standard reconstruction]
- \(S_m=\displaystyle\int d^4x\,d^2\theta\;m\,\Phi^2+\text{c.c.}\) [transcript-backed]
- \(m\,\Phi^2\;\leadsto\; m\,F\phi+m\,\psi\psi+\text{c.c.}\) schematically [standard reconstruction]
- \(F^\ast+m\phi=0,\qquad F+m\phi^\ast=0\) [transcript-backed]
- \(\mathcal L_{\text{boson mass}}\sim m^2\,\phi^\ast\phi\) [transcript-backed]
- \(S_g=\displaystyle\int d^4x\,d^2\theta\;g\,\Phi^3+\text{c.c.}\) [transcript-backed]
- \(g\,\Phi^3\;\leadsto\; g\,\phi\,\psi\psi+g\,\phi^2F+\text{c.c.}\) schematically [standard reconstruction]
- Eliminating \(F\) from the cubic interaction induces a quartic bosonic term of schematic form \(g^2\,\phi^2\phi^{\ast 2}\) [transcript-backed]
- Supersymmetry enforces \(m_{\text{boson}}=m_{\text{fermion}}=m\) in the mass example [transcript-backed]
- The quartic bosonic coupling is tied to the square of the Yukawa coupling: \(\lambda_{\phi^4}\sim g^2\) [transcript-backed]

## Definitions And Objects
- Chiral massless fermion:
  - Two-component spinor field, denoted on the board by \(\psi_1,\psi_2\) or \(\psi_\alpha\).
  - Used as the physical model for what a spinorial object should look like in four dimensions.
- Chirality versus helicity:
  - Helicity is associated in the lecture with \(\sigma\cdot p\).
  - Chirality is associated verbally with \(\gamma_5\).
  - They coincide for the massless case being discussed.
- Grassmann coordinates:
  - \(\theta_\alpha\) and \(\bar\theta_\alpha\).
  - Two complex spinor components, or equivalently four real Grassmann components.
- General superfield:
  - Function of \(x^\mu,\theta,\bar\theta\).
  - Expands as a finite polynomial in Grassmann variables, terminating at fourth order.
- Chiral superfield:
  - Defined by the constraint \(\bar D\Phi=0\).
  - Depends on \(\bar\theta\) only through \(y^\mu=x^\mu+i\bar\theta\sigma^\mu\theta\).
  - Contains three component fields in the lecture’s simplified notation: \(\phi,\psi,F\).
- Component fields of \(\Phi\):
  - \(\phi\): complex scalar.
  - \(\psi\): fermionic two-component field.
  - \(F\): auxiliary complex scalar; algebraic, not an ordinary propagating degree of freedom.
- Supercharges:
  - Differential operators on superspace generating small supersymmetry variations of superfields.
- \(D\)-operators:
  - Differential operators built to anticommute with the \(Q\)-operators and therefore define supersymmetry-compatible constraints.
- Super Lagrangian versus ordinary Lagrangian:
  - \(\mathcal L_{\text{sup}}\) lives on superspace.
  - After Grassmann integration one gets the ordinary component Lagrangian \(\mathcal L\).
- Highest-component extraction:
  - \(d^2\theta\,d^2\bar\theta\) picks out the \(\theta^2\bar\theta^2\) term.
  - \(d^2\theta\) alone is used when the expression has no \(\bar\theta\)-dependence.

## Derivation Steps
`From \(H=\sigma\cdot p\) to the chiral Dirac equation`
1. Start from the massless chiral Hamiltonian \(H=\boldsymbol{\sigma}\cdot\mathbf p\).
2. Replace \(H\) by \(i\,\partial_t\).
3. Replace \(p_i\) by \(-i\,\partial_i\).
4. Obtain \(i\,\partial_t\psi=-\,i\,\sigma^i\partial_i\psi\).
5. Move everything to one side and rename \(t=x^0\).
6. Introduce \(\sigma^0=\mathbf1\).
7. Rewrite the equation as \(i\,\sigma^\mu\partial_\mu\psi=0\).

`From Lorentz invariance to the four-dimensional superalgebra`
1. Recall the earlier one-dimensional relation \(\{Q^\dagger,Q\}\sim H\).
2. Replace the isolated Hamiltonian by the four-momentum \(P_\mu\), because Lorentz invariance requires energy and momentum together.
3. Notice the index mismatch: the left-hand side has spinor indices \(\alpha,\beta\), while \(P_\mu\) carries a Lorentz index \(\mu\).
4. Insert \((\sigma^\mu)_{\alpha\beta}\) to soak up \(\mu\) and return the spinor indices.
5. Write \(\{Q_\alpha^\dagger,Q_\beta\}=2(\sigma^\mu)_{\alpha\beta}P_\mu\).
6. Translate \(P_\mu\) into derivative form to get the schematic operator identity \(2i\,(\sigma^\mu)_{\alpha\beta}\partial_\mu\).
7. Keep the same structural relations as before for \(\{Q,Q\}\), \(\{Q^\dagger,Q^\dagger\}\), and the commutators with \(P_\mu\).

`Supersymmetry-compatible constraints`
1. Suppose a superfield obeys a constraint of the form \(\bar D\Phi=0\).
2. After a supersymmetry variation, the constrained field must remain constrained.
3. Therefore \(\bar D(Q\Phi)\) must also vanish whenever \(\bar D\Phi=0\).
4. A sufficient condition is that \(\bar D\) commute or anticommute with the supersymmetry generators.
5. This motivates constructing \(D\) and \(\bar D\) as sign-flipped versions of the \(Q\)-operators.
6. The lecture then uses \(\bar D\Phi=0\) as the defining chiral constraint.

`Solving \(\bar D\Phi=0\)`
1. First compare with the simpler case \(\partial\Phi/\partial\bar\theta=0\), which would force no \(\bar\theta\)-dependence at all.
2. For \(\bar D=\partial/\partial\bar\theta-i\,\sigma\theta\,\partial_x\), guess that \(\Phi\) depends on \(\bar\theta\) only through \(x+i\bar\theta\sigma\theta\).
3. Define \(y^\mu=x^\mu+i\bar\theta\sigma^\mu\theta\).
4. Differentiate \(\Phi(y,\theta)\) with respect to \(\bar\theta\); the chain rule produces a term proportional to \(i\,\sigma^\mu\theta\,\partial_\mu\Phi\).
5. The second piece in \(\bar D\) contributes the same expression with the opposite sign.
6. The two contributions cancel, so \(\bar D\Phi=0\).
7. Conclude that the general solution is \(\Phi=\Phi(y,\theta)\).

`Truncating the chiral superfield expansion`
1. Since a chiral superfield depends only on \(y\) and the two components of \(\theta\), only powers up to \(\theta^2\) survive.
2. Start with a scalar coefficient \(\phi(y)\).
3. Add the linear fermionic term \(\psi(y)\theta\).
4. Add the quadratic term \(F(y)\theta^2\).
5. Higher powers vanish because there are only two independent \(\theta\)-components.

`Free component Lagrangian from \(\Phi^\ast\Phi\)`
1. Start from \(\mathcal L_{\text{sup}}=\Phi^\ast\Phi\) and the action \(\int d^4x\,d^2\theta\,d^2\bar\theta\).
2. Write \(\Phi^\ast\) as a function of \(x-i\bar\theta\sigma\theta,\bar\theta\) and \(\Phi\) as a function of \(x+i\bar\theta\sigma\theta,\theta\).
3. Shift the integration variable \(x\) to remove the \(\bar\theta\sigma\theta\) dependence from one factor; the same shift doubles it in the other factor.
4. Expand the shifted factor in a Taylor series in \(\bar\theta\sigma\theta\).
5. Keep only terms that can contribute to the \(\theta^2\bar\theta^2\) component.
6. The \(\phi^\ast\) term multiplies the second \(x\)-derivative term to give the scalar kinetic piece.
7. The \(\bar\theta\psi\) term multiplies the \(\theta\theta\bar\theta\)-piece to give the fermion kinetic term with a sigma matrix.
8. The \(F^\ast\bar\theta^2\) term multiplies \(F\theta^2\) to give \(F^\ast F\).
9. After Grassmann integration, the surviving component Lagrangian is schematically \(\phi^\ast\Box\phi+\bar\psi\,\sigma^\mu\partial_\mu\psi+F^\ast F\).

`Mass term from \(d^2\theta\,m\Phi^2\)`
1. Use the chiral-field expansion \(\Phi=\phi+\psi\theta+F\theta^2\) in schematic lecture notation.
2. Since the expression has no \(\bar\theta\)-dependence, integrate only over \(d^2\theta\).
3. Multiply \(\Phi\) by itself and keep only the \(\theta^2\) coefficient.
4. The surviving terms are schematic \(F\phi\) and \(\psi\psi\).
5. Add the complex conjugate.
6. Interpret the \(\psi\psi\) term as a fermion mass term.
7. Combine \(F^\ast F\) with \(mF\phi+mF^\ast\phi^\ast\), solve the algebraic \(F\)-equation of motion, and recover the boson mass term \(m^2\phi^\ast\phi\).

`Interaction term from \(d^2\theta\,g\Phi^3\)`
1. Expand \(\Phi^3\) and retain only the \(\theta^2\) component.
2. One class of terms is schematic \(\phi\,\psi\psi\), giving a Yukawa interaction.
3. Another class is schematic \(\phi^2F\), plus the complex conjugate.
4. Because \(F\) is auxiliary, it cannot end a diagram by itself; it must be eliminated or connected locally.
5. Eliminating \(F\) converts the \(\phi^2F\) structure into a four-boson contact interaction of schematic size \(g^2\).
6. This is the lecture’s concrete example of supersymmetry relating apparently different interaction vertices.

`Auxiliary-field triviality and propagator picture`
1. In the free Lagrangian, \(F\) appears only algebraically as \(F^\ast F\).
2. Its Euler–Lagrange equation is algebraic, not differential.
3. Therefore \(F\) is not an ordinary propagating mode.
4. In diagrammatic language, the corresponding propagator does not spread between separated points.
5. The lecture interprets it as a contact or delta-function propagator.

`Loop-cancellation logic`
1. The Yukawa vertex carries a coupling \(g\).
2. The induced quartic bosonic interaction carries a coupling of schematic size \(g^2\).
3. The bosonic self-energy and fermionic self-energy loop diagrams therefore enter with matched coupling strength.
4. The loop integrals are paired by the supersymmetric relations among masses and couplings.
5. Fermion loops and boson loops come with opposite signs.
6. The paired contributions cancel, and the lecture states that this structure persists to all orders.

## Notation Choices
- Use \(\boldsymbol{\sigma}=(\sigma^1,\sigma^2,\sigma^3)\) and \(\sigma^0=\mathbf1\).
- Use the shorthand \(\bar\theta\sigma^\mu\theta\) for the spinor contraction, and avoid forcing detailed index placement unless it clarifies a specific point.
- Write the chiral wave equation as \(i\sigma^\mu\partial_\mu\psi=0\), matching the lecture’s final covariant form.
- Keep \(Q,\bar Q,D,\bar D\) as differential operators on superspace; use the compact shorthand forms rather than fully indexed expanded contractions unless needed.
- Use \(\Phi\) for the chiral superfield and \(\Phi^\ast\) for its complex conjugate, since the lecture verbally treats the chiral superfield as complex.
- Use \(\phi,\psi,F\) for the component fields.
- Write \(\theta^2\) for the product of the two independent \(\theta\)-components and \(\theta^4\) for the product of all four independent Grassmann coordinates.
- Keep the component expansion schematic: \(\Phi=\phi+\psi\theta+F\theta^2\).
- Use \(\mathcal L_{\text{sup}}\) for the super-Lagrangian and \(\mathcal L\) for the ordinary component Lagrangian.
- Keep \(F^\ast F\) in that explicit form rather than replacing it by \(|F|^2\), because that is the board-facing notation.
- For the scalar kinetic term, prefer \(\phi^\ast\Box\phi\) in the working bank, since that is closer to the board and transcript flow; an integrated-by-parts version can be chosen later during chapter writing.
- For the mass and interaction terms, suppress combinatorial coefficients such as \(1/2\), \(2\), or \(3\) unless they are explicitly secure from the transcript.
- For spinor bilinears in the mass and Yukawa terms, use schematic notation like \(\psi\psi\) in the bank, and note in the final chapter that Susskind’s spoken notation there is loose.

## Uncertain Mathematics
- The exact index ordering on \((\sigma^\mu)_{\alpha\beta}\), \(Q_\alpha\), \(\bar Q_\beta\), \(D_\alpha\), and \(\bar D_\beta\) is unstable in the lecture and partially debated aloud.
- The sign convention relating \(P_\mu\) to \(i\partial_\mu\) versus \(-i\partial_\mu\) is not fully stabilized by the transcript alone; preserve the lecture’s schematic \(2i\,\sigma^\mu\partial_\mu\) form when quoting it.
- The chirality-versus-helicity discussion is conceptually clear but verbally messy; the final notes should be careful not to overclaim exact operator equalities beyond the massless case emphasized in the lecture.
- The chiral superfield expansion is stated in a very schematic form, including phrases like “psi bar theta”; the final notes should normalize the notation but mention that Susskind is suppressing indexology.
- The exact numerical coefficients in the free component Lagrangian from \(\Phi^\ast\Phi\) are intentionally not tracked by Susskind on the board.
- The exact combinatorial factors in the \(\Phi^2\) and \(\Phi^3\) component expansions are not reliable from the transcript and should be presented schematically unless later checked independently.
- The precise normalized form of the quartic bosonic interaction induced after eliminating \(F\) is not derived with coefficient care in the lecture.
- The exact notation on the board at the far right of the component derivation may indicate either the ordinary Lagrangian \(\mathcal L\) or the integrated ordinary Lagrangian.
- The auxiliary-field propagator is described qualitatively as a delta function/contact object; the transcript motivates that interpretation clearly, but the precise normalization of the propagator is not provided.