# Math Bank
## Core Equations
- \(\mathcal{L}=\mathcal{L}\!\left(\phi,\partial_t\phi,\partial_x\phi,\ldots\right)=\mathcal{L}\!\left(\phi,\partial_\mu\phi\right)\). [visible]
- \(\frac{\partial}{\partial t}\frac{\partial \mathcal L}{\partial \dot\phi}+\frac{\partial}{\partial x}\frac{\partial \mathcal L}{\partial \phi_x}+\frac{\partial}{\partial y}\frac{\partial \mathcal L}{\partial \phi_y}+\frac{\partial}{\partial z}\frac{\partial \mathcal L}{\partial \phi_z}=\frac{\partial \mathcal L}{\partial \phi}\). [standard reconstruction]
- \(\mathcal L=\frac12\dot\phi^{\,2}-\frac12\left(\frac{\partial\phi}{\partial x}\right)^2-\frac12\left(\frac{\partial\phi}{\partial y}\right)^2-\frac12\left(\frac{\partial\phi}{\partial z}\right)^2-V(\phi)\). [transcript-backed]
- \(\mathcal L=\frac12\dot\phi^{\,2}-\frac12(\nabla\phi)^2-V(\phi)\). [transcript-backed]
- \(\ddot\phi-\nabla^2\phi=-\frac{\partial V}{\partial\phi}\). [transcript-backed]
- \(V(\phi)=\frac12 m^2\phi^2\). [transcript-backed]
- \(\ddot\phi-\nabla^2\phi=-m^2\phi\). [transcript-backed]
- \(\phi(x,t)\sim e^{i\omega t}e^{-i\mathbf k\cdot\mathbf x}\). [transcript-backed]
- \(\omega^2-k^2=m^2\). [transcript-backed]
- \(\omega^2=k^2+m^2\). [transcript-backed]
- \(E^2=p^2+m^2\). [transcript-backed]
- \(V(\phi)\supset g\phi^3\). [transcript-backed]
- \(\ddot\phi-\nabla^2\phi=-m^2\phi-3g\phi^2\). [transcript-backed]
- \(\mathcal L=\frac12(\partial_\mu\phi)^2+\frac12(\partial_\mu\rho)^2-V(\phi,\rho)\). [transcript-backed]
- \(V(\phi,\rho)=\frac12 m^2\phi^2+\frac12 M^2\rho^2+\rho\phi^2\). [transcript-backed]
- \(\ddot\phi-\nabla^2\phi=-m^2\phi-2\rho\phi\). [standard reconstruction]
- \(\ddot\rho-\nabla^2\rho=-M^2\rho-\phi^2\). [standard reconstruction]
- \(i\dot\Psi=i\alpha\frac{\partial\Psi}{\partial x}+m\beta\Psi\). [visible]
- \(i\dot\Psi=i\sum_i\alpha_i\frac{\partial\Psi}{\partial x_i}+m\beta\Psi\). [transcript-backed]
- \(i\left(\Psi^\dagger\frac{\partial\Psi}{\partial t}+\Psi^\dagger\alpha\frac{\partial\Psi}{\partial x}+\Psi^\dagger\beta\Psi\,m\right)\). [visible]
- \(\mathcal L_{\text{Dirac}}\sim i\left(\Psi^\dagger\frac{\partial\Psi}{\partial t}+\Psi^\dagger\alpha\frac{\partial\Psi}{\partial x}+m\Psi^\dagger\beta\Psi\right)\). [standard reconstruction]
- \(\mathcal L_{\text{int}}\propto \Psi^\dagger\beta\Psi\,\phi\). [transcript-backed]
- \(\phi\sim A^+ + A^-\). [transcript-backed]
- \(\partial_x\phi \sim \frac{\phi(x)-\phi(x')}{L}\). [transcript-backed]
- \(\frac12 m^2\phi^2\). [transcript-backed]
- \(\Psi \sim C^-_{\text{electron}}(+E)+C^+_{\text{positron}}(+E)\). [standard reconstruction]
- \(\Psi^\dagger \sim C^+_{\text{electron}}(+E)+C^-_{\text{positron}}(+E)\). [standard reconstruction]
- \(\mathcal L_{\text{QED,int}}=e\left(\Psi^\dagger\Psi\,A_0+\Psi^\dagger\alpha\Psi\cdot\mathbf A\right)\). [transcript-backed]
- \(\Psi\to e^{i\theta}\Psi,\qquad \Psi^\dagger\to e^{-i\theta}\Psi^\dagger,\qquad A\to A\). [transcript-backed]
- \(\prod_x\bigl(1+\mathcal L_I(x)\bigr)\). [transcript-backed]
- \(\Psi_p^\dagger\Psi_n\,\pi^+,\qquad \Psi_n^\dagger\Psi_p\,\pi^-,\qquad \Psi_p^\dagger\Psi_p\,\pi^0,\qquad \Psi_n^\dagger\Psi_n\,\pi^0\). [transcript-backed]
- \(\Psi_p^\dagger\Psi_p\,A\). [transcript-backed]
- \(H\phi^2\). [transcript-backed]
- \(\langle H\rangle \neq 0\). [transcript-backed]

## Definitions And Objects
- \(\mathcal L\): lecture’s local Lagrangian object; classically it generates equations of motion, quantum mechanically it codes local processes.
- \(\phi\): scalar field; first worked example throughout the opening half.
- \(\rho\): second scalar field in the coupled-field example.
- \(V(\phi)\), \(V(\phi,\rho)\), \(V(H)\): potential energy / field energy; in the scalar example the undifferentiated field enters only through \(V\).
- \(\dot\phi\): \(\partial\phi/\partial t\).
- \(\phi_x,\phi_y,\phi_z\): lecture shorthand for \(\partial\phi/\partial x\), \(\partial\phi/\partial y\), \(\partial\phi/\partial z\).
- \(\partial_\mu\phi\): compact relativistic shorthand for time and space derivatives.
- \(m\), \(M\): mass parameters; interpreted as masses of the quanta of \(\phi\) and \(\rho\).
- \(g\): generic coupling multiplying higher-order interaction terms such as \(\phi^3\).
- \(\Psi\): Dirac field; multi-component fermion field.
- \(\Psi^\dagger\): Hermitian conjugate used in the lecture’s noncovariant board formulas.
- \(\alpha_i,\beta\): Dirac matrices; \(\alpha\) denotes the spatial collection \((\alpha_1,\alpha_2,\alpha_3)\) when the lecture suppresses indices.
- \(A_0,\mathbf A\): time and spatial components of the electromagnetic vector potential.
- \(A\): photon field operator in the QED discussion; contains photon creation and annihilation pieces.
- \(A^+\), \(A^-\): schematic scalar-field creation and annihilation operator pieces.
- \(C^\pm\): schematic electron/positron creation-annihilation operator symbols used in the late QED board discussion.
- \(e\): electric charge of the electron; interpreted in the lecture as the amplitude for the basic QED vertex, with \(e^2\) setting the probability scale.
- “Quadratic terms”: terms quadratic in fields or derivatives; lecture interpretation is free propagation or same-point mass counting.
- “Nonlinear terms”: cubic or higher terms; lecture interpretation is interaction, scattering, creation, annihilation.
- Vacuum: baseline state in the late source-detector discussion; initial states are created above it, final states are absorbed back into it.

## Derivation Steps
Scalar field equation
1. Start from \(\mathcal L=\frac12\dot\phi^{\,2}-\frac12(\nabla\phi)^2-V(\phi)\).
2. Compute \(\partial \mathcal L/\partial \dot\phi=\dot\phi\).
3. Differentiate once more in time to get \(\partial_t(\partial \mathcal L/\partial \dot\phi)=\ddot\phi\).
4. Compute \(\partial \mathcal L/\partial \phi_x=-\phi_x\), and similarly for \(y,z\).
5. Differentiate in space to get \(-\partial_x^2\phi\), \(-\partial_y^2\phi\), \(-\partial_z^2\phi\).
6. Note that undifferentiated \(\phi\) appears only in \(V(\phi)\), so \(\partial \mathcal L/\partial \phi=-V'(\phi)\).
7. Assemble the Euler-Lagrange equation to obtain \(\ddot\phi-\nabla^2\phi=-V'(\phi)\).

Mass term to relativistic dispersion
1. Choose \(V(\phi)=\frac12 m^2\phi^2\).
2. Differentiate to get \(V'(\phi)=m^2\phi\).
3. Insert this into the field equation: \(\ddot\phi-\nabla^2\phi=-m^2\phi\).
4. Try a plane wave \(\phi\sim e^{i\omega t}e^{-i\mathbf k\cdot\mathbf x}\).
5. Two time derivatives give \(-\omega^2\phi\).
6. Two spatial derivatives give \(-k^2\phi\), so the minus sign in the equation yields \(+k^2\phi\).
7. Cancel \(\phi\) and get \(\omega^2-k^2=m^2\).
8. In \(\hbar=c=1\), identify \(\omega=E\) and \(k=p\), giving \(E^2=p^2+m^2\).

Nonlinearity from higher powers
1. Add a cubic term \(g\phi^3\) to the potential.
2. Differentiate with respect to \(\phi\) to get \(3g\phi^2\).
3. The field equation gains \(-3g\phi^2\).
4. The equation is no longer linear in the field.
5. The lecture reads this as the loss of superposition and the onset of scattering.

Coupled scalar fields
1. Introduce two scalar fields \(\phi\) and \(\rho\).
2. Give each field its own quadratic kinetic and mass terms.
3. Add a mixed interaction such as \(\rho\phi^2\).
4. Differentiate \(V(\phi,\rho)\) with respect to \(\phi\) to get \(m^2\phi+2\rho\phi\).
5. Differentiate \(V(\phi,\rho)\) with respect to \(\rho\) to get \(M^2\rho+\phi^2\).
6. Insert into the two Euler-Lagrange equations.
7. Conclude that the equations are coupled and, because of the mixed higher-order term, nonlinear.

Quantum reading of \(\phi^3(x)\)
1. Write the field schematically as \(\phi\sim A^+ + A^-\).
2. Cube it.
3. Identify the \( (A^-)^3 \) term as annihilating three particles.
4. Identify the \( (A^+)^3 \) term as creating three particles.
5. Identify mixed terms as \(2\to1\) and \(1\to2\) processes.
6. Read all of them as local processes at the same point \(x\).

Derivative term as propagation
1. Replace \(\partial_x\phi\) schematically by \([\phi(x)-\phi(x')]/L\).
2. Square the difference.
3. Separate same-point pieces from the cross-term connecting \(x\) and \(x'\).
4. Read same-point pieces as absorb-and-reemit at the same location.
5. Read the cross-term as remove at one neighboring point and reemit at the other.
6. Interpret quadratic derivative terms as local propagation / hopping.

Mass term as same-point process
1. Look at \(\frac12 m^2\phi^2\).
2. Treat it as quadratic but without a derivative.
3. Read it as absorption and re-emission at the same point.
4. Do not read it as transport between points.
5. Use this to distinguish “mass counting” from “motion.”

QED vertex expansion
1. Decompose \(\Psi\) schematically into electron-annihilation and positron-creation pieces.
2. Decompose \(\Psi^\dagger\) into electron-creation and positron-annihilation pieces.
3. Let \(A\) contribute photon creation and annihilation pieces.
4. Multiply the three factors.
5. Read off electron emission of a photon.
6. Read off electron absorption of a photon.
7. Read off electron-positron annihilation into a photon.
8. Read off photon conversion into an electron-positron pair.

Charge conservation from the interaction term
1. Inspect the QED interaction term and note one \(\Psi\) and one \(\Psi^\dagger\).
2. Use the lecture’s rule: \(\Psi\) raises charge by one unit, \(\Psi^\dagger\) lowers it by one unit.
3. The net charge change of the interaction term is zero.
4. Diagrammatically, enforce through-going fermion arrows.
5. Reject diagrams where negative charge turns directly into positive charge.

Local vertex vs conserved amplitude
1. Start from a local vertex that seems to allow many rotated-leg versions.
2. Notice that some of those local pictures look kinematically impossible.
3. Compute the local amplitude first.
4. Integrate over all spacetime positions of the vertex.
5. The spacetime integral enforces energy and momentum conservation.
6. Processes that violate those laws drop out of the physical amplitude.

Derivative acting on plane-wave factors, not operators
1. Expand the field as creation/annihilation operators times plane-wave factors.
2. Observe that the operators themselves do not depend on spacetime position.
3. Differentiate only the exponential factors.
4. Pull down \(k\) and \(\omega\) from those exponentials.
5. Keep the creation and annihilation operators untouched by the derivative.

Discrete-cell locality picture
1. Divide space or spacetime into small cells.
2. Replace derivatives by finite differences between neighboring cells.
3. Let quadratic terms move particles from one cell to a neighboring cell.
4. Let interaction terms absorb and emit particles within a single cell.
5. Build extended processes by repeating these local operations many times.
6. Take the continuum limit by shrinking cell size to zero.

Heuristic product of local factors
1. Introduce one factor \(1+\mathcal L_I(x)\) at each spacetime point or cell.
2. Multiply those factors over all points.
3. The \(1\) term means “nothing happens here.”
4. A single \(\mathcal L_I(x)\) term means one local interaction.
5. Products \(\mathcal L_I(x)\mathcal L_I(x')\) mean repeated local interactions at different points.
6. Read the full amplitude as the sum of all such allowed combinations.

## Notation Choices
- Use “Lagrangian,” not the transcript’s misheard “logarithm.”
- Write the central object as \(\mathcal L\) throughout.
- Use \(\phi\) for the main scalar field and \(\rho\) for the second scalar field.
- Preserve the lecture’s alternation between explicit component notation and compact relativistic notation:
  - explicit: \(\dot\phi,\phi_x,\phi_y,\phi_z\)
  - compact: \(\partial_\mu\phi\), \((\partial_\mu\phi)^2\)
- In explanatory derivations, prefer \(\nabla^2\phi\) once the lecture has already displayed the component form.
- Keep \(V(\phi)\) and \(V(\phi,\rho)\) as the potential notation; do not silently replace them with a different symbol.
- Use \(m\) and \(M\) exactly as the lecture does for the two mass parameters.
- Use \(\Psi\) and \(\Psi^\dagger\) in the main body when following the lecture’s board notation.
- If a Lorentz-invariant scalar-fermion coupling is typeset cleanly, keep the lecture-facing form \(\Psi^\dagger\beta\Psi\,\phi\); do not switch the main presentation to fully covariant \(\bar\Psi\Psi\,\phi\) unless explicitly flagged as a notation cleanup.
- Keep the Dirac matrices as \(\alpha_i\) and \(\beta\); when the lecture suppresses spatial indices, write \(\alpha\cdot\nabla\) or \(\sum_i\alpha_i\partial_i\) only if clarification is needed.
- In the QED section, prefer the mixed classroom notation \(A_0,\mathbf A\) rather than replacing the main text by \(A_\mu\).
- Use \(e\) as the QED coupling/charge coefficient.
- For schematic operator decompositions, keep \(A^\pm\) and \(C^\pm\) as intentionally schematic; do not promote them to a full normalized mode expansion.
- Keep arrows on fermion lines interpreted as charge flow, not merely geometric direction.
- Use \(\hbar=c=1\) when converting \(\omega,k\) to \(E,p\).
- Treat the proton-neutron-pion vertices as schematic effective-field terms, not as fundamental quark-level interactions.

## Uncertain Mathematics
- The full scalar Euler-Lagrange line on the board is cropped; the clean four-term field-theory version should be presented as a cautious completion, not as direct chalk transcription.
- The scalar field equation \(\ddot\phi-\nabla^2\phi=-V'(\phi)\) is transcript-secure, but the fully typeset compact form is still a cleaned reconstruction of a partially visible board derivation.
- The Dirac equation and Dirac Lagrangian are visibly on the board, but the lecture itself says the placement of \(i\)’s and parentheses may be off; final notes should not overclaim exact chalk fidelity.
- The scalar-fermion coupling term is conceptually clear, but the exact covariant form is only loosely handled in the lecture; keep \(\Psi^\dagger\beta\Psi\,\phi\) as the lecture-facing cautious choice.
- The late \(\Psi\), \(\Psi^\dagger\) operator decompositions are only partly visible; subscripts, plus/minus markers, and energy labels should stay schematic.
- The QED interaction should remain in mixed \(A_0\) and spatial-\(\mathbf A\) notation unless a covariant form is explicitly marked as a later cleanup.
- The heuristic product \(\prod_x(1+\mathcal L_I(x))\) is pedagogical, not a rigorous derivation of the path integral; it should be labeled as such if used.
- The proton-neutron-pion example is mathematically usable only after correcting the live charge-sign confusion on the board and in the speech.
- The Higgs coda is conceptual but only partially developed mathematically in this lecture; \(\langle H\rangle\neq 0\) and the role of \(H\phi^2\) should be stated as a lecture-guided sketch, not a full symmetry-breaking derivation.
- The late commutator discussion is loose and should not be canonized into a precise field-commutator theorem without extra care; the lecture’s point is qualitative measurement limitation, not a carefully stated microcausality result.