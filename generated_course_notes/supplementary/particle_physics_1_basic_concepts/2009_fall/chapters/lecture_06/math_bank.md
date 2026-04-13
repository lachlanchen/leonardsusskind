# Math Bank
## Core Equations
- \( \psi(x,t)\sim e^{i(kx-\omega t)} \) [transcript-backed]
- \( \partial_x\psi+\partial_t\psi=0 \) [transcript-backed]
- \( \partial_t\psi_R=-\,\partial_x\psi_R \) [transcript-backed]
- \( \partial_t\psi_L=+\,\partial_x\psi_L \) [transcript-backed]
- \( \omega=k \) for the right-moving branch [transcript-backed]
- \( \omega=-k \) for the left-moving branch [transcript-backed]
- \( \Psi=\begin{pmatrix}\psi_R\\ \psi_L\end{pmatrix} \) [visible]
- \( \alpha=\begin{pmatrix}1&0\\0&-1\end{pmatrix} \) [visible]
- \( \dfrac{\partial \Psi}{\partial t}=-\alpha\,\dfrac{\partial \Psi}{\partial x} \) [visible]
- \( \omega=\alpha k \) as operator shorthand on plane waves [transcript-backed]
- \( \omega^2=k^2+m^2 \) [transcript-backed]
- \( v_g=\dfrac{d\omega}{dk}=\dfrac{k}{\sqrt{k^2+m^2}} \) [transcript-backed]
- \( \omega=\alpha k+\beta m \) [transcript-backed]
- \( \alpha^2=1 \) [transcript-backed]
- \( \beta^2=1 \) [transcript-backed]
- \( \alpha\beta+\beta\alpha=0 \) [transcript-backed]
- \( \beta=\begin{pmatrix}0&1\\1&0\end{pmatrix} \) [transcript-backed]
- \( i\,\dot{\Psi}=-\,i\alpha\,\partial_x\Psi+m\beta\Psi \) [standard reconstruction]
- \( i\,\dot{\psi}_R=-\,i\,\partial_x\psi_R+m\psi_L \) [transcript-backed]
- \( i\,\dot{\psi}_L=+\,i\,\partial_x\psi_L+m\psi_R \) [transcript-backed]
- \( i\,\dot{\psi}_R=m\psi_L \) at \(k=0\) [transcript-backed]
- \( i\,\dot{\psi}_L=m\psi_R \) at \(k=0\) [transcript-backed]
- \( \psi_+=\psi_R+\psi_L \) [transcript-backed]
- \( \psi_-=\psi_R-\psi_L \) [transcript-backed]
- \( i\,\dot{\psi}_+=m\psi_+ \) [visible]
- \( i\,\dot{\psi}_-=-m\psi_- \) [visible]
- \( \omega=+m \) [visible]
- \( \omega=-m \) [visible]
- \( m_{\mathrm{eff}}=g\,\phi_{\mathrm{vac}} \) or \(m_{\mathrm{eff}}=g\langle\phi\rangle\) [standard reconstruction]
- \( V(\phi)=V(-\phi) \) [standard reconstruction]
- \( \omega=\alpha_1k_1+\alpha_2k_2+\alpha_3k_3+\beta m \) [transcript-backed]
- \( \omega^2=k_1^2+k_2^2+k_3^2+m^2 \) [transcript-backed]
- \( \alpha_i^2=1 \) for \(i=1,2,3\) [transcript-backed]
- \( \beta^2=1 \) in the \(3+1\)-dimensional discussion as well [transcript-backed]
- \( \alpha_i\alpha_j+\alpha_j\alpha_i=2\delta_{ij} \) [standard reconstruction]
- \( \alpha_i\beta+\beta\alpha_i=0 \) [transcript-backed]
- \( \beta=\begin{pmatrix}I&0\\0&-I\end{pmatrix} \) [standard reconstruction]
- \( \alpha_i=\begin{pmatrix}0&\sigma_i\\ \sigma_i&0\end{pmatrix} \) [standard reconstruction]
- \( i\,\partial_t\Psi=\left(-\,i\,\alpha_i\partial_i+\beta m\right)\Psi \) [standard reconstruction]

## Definitions And Objects
- \( \psi_R \): right-moving field in the massless \(1+1\)-dimensional discussion; later better treated as the upper component once the mass term is present.
- \( \psi_L \): left-moving field in the massless \(1+1\)-dimensional discussion; later better treated as the lower component once the mass term is present.
- \( \Psi \): two-component column spinor formed from \( \psi_R \) and \( \psi_L \).
- \( \alpha \): diagonal matrix that distinguishes the two components by eigenvalues \(+1\) and \(-1\).
- \( \beta \): matrix that mixes the two components; in \(1+1\) dimensions the chosen example flips \( \psi_R \leftrightarrow \psi_L \).
- \( \psi_+,\psi_- \): linear combinations that diagonalize the rest-frame coupled equations.
- Dirac sea: the filled set of negative-energy fermion states, used as the vacuum reference state.
- Hole: absence of a negative-energy fermion in the filled sea; interpreted as an antiparticle excitation.
- \( \phi(x) \): Higgs/scalar field introduced in the mass digression.
- \( V(\phi) \): scalar-field potential energy density.
- \( \alpha_i \) for \(i=1,2,3\): three spatial Dirac matrices in the \(3+1\)-dimensional preview.
- Four-component \( \Psi \) in \(3+1\) dimensions: column with components \( \psi_1,\psi_2,\psi_3,\psi_4 \).
- Pauli matrices \( \sigma_i \): the \(2\times2\) matrices used in the block presentation of the \(3+1\)-dimensional Dirac matrices.
- Optional hidden indices in the final chapter, if needed for one sentence only: spinor indices \(p,q=1,\dots,4\).

## Derivation Steps
**Massless right-moving branch**
1. Start from \( \psi(x,t)\sim e^{i(kx-\omega t)} \).
2. Apply \( \partial_x \) to get \( ik\psi \).
3. Apply \( \partial_t \) to get \( -\,i\omega\psi \).
4. Insert into \( \partial_x\psi+\partial_t\psi=0 \).
5. Obtain \( ik-i\omega=0 \), hence \( \omega=k \).
6. Read this as the right-moving branch.

**Left-moving companion field**
1. Introduce a second field so the theory is left-right symmetric.
2. Reverse one sign in the first-order equation.
3. Use \( \partial_t\psi_L=+\partial_x\psi_L \).
4. Insert the same plane wave ansatz.
5. Obtain \( \omega=-k \ ).
6. Fill the negative-energy sea for left-movers as well as right-movers.

**Matrix packaging of the two first-order equations**
1. Define \( \Psi=\begin{pmatrix}\psi_R\\ \psi_L\end{pmatrix} \).
2. Choose \( \alpha=\mathrm{diag}(1,-1) \).
3. Write the pair of equations as \( \partial_t\Psi=-\alpha\,\partial_x\Psi \).
4. Emphasize that this is only a compact rewriting, not new physics.

**Operator shorthand**
1. On a plane wave, \( i\partial_t \) returns \( \omega \).
2. On a plane wave, \( -\,i\partial_x \) returns \( k \).
3. Therefore the matrix equation may be summarized as \( \omega=\alpha k \).
4. Treat this only as shorthand for operator action, not as an ordinary scalar identity.

**Adding a mass term in \(1+1\) dimensions**
1. Demand relativistic dispersion \( \omega^2=k^2+m^2 \).
2. Try the linear ansatz \( \omega=\alpha k+\beta m \).
3. Square it: \( \omega^2=\alpha^2k^2+\beta^2m^2+(\alpha\beta+\beta\alpha)km \).
4. Match the \(k^2\) term by requiring \( \alpha^2=1 \).
5. Match the \(m^2\) term by requiring \( \beta^2=1 \).
6. Remove the mixed term by requiring \( \alpha\beta+\beta\alpha=0 \).
7. Conclude that \( \alpha \) and \( \beta \) cannot be ordinary numbers; they must be matrices.

**Check of the chosen \( \beta \)**
1. Take \( \beta=\begin{pmatrix}0&1\\1&0\end{pmatrix} \).
2. Compute \( \beta^2 \) and obtain the identity matrix.
3. Compute \( \alpha\beta \).
4. Compute \( \beta\alpha \).
5. Verify \( \alpha\beta=-\beta\alpha \).
6. Conclude that the chosen \( \beta \) satisfies the required algebra.

**Component form of the massive Dirac equation**
1. Start from \( i\dot{\Psi}=-\,i\alpha\partial_x\Psi+m\beta\Psi \).
2. Act with \( \alpha \) on the two components; the lower component picks up the minus sign.
3. Act with \( \beta \) on the two components; it swaps \( \psi_R \) and \( \psi_L \).
4. Read off
   \( i\dot{\psi}_R=-\,i\partial_x\psi_R+m\psi_L \),
   \( i\dot{\psi}_L=+\,i\partial_x\psi_L+m\psi_R \).
5. Interpret the mass term as coupling upper and lower components.

**Rest-frame decoupling**
1. Set \( k=0 \), equivalently discard spatial variation.
2. Reduce the coupled system to
   \( i\dot{\psi}_R=m\psi_L \),
   \( i\dot{\psi}_L=m\psi_R \).
3. Add the equations and define \( \psi_+=\psi_R+\psi_L \).
4. Obtain \( i\dot{\psi}_+=m\psi_+ \).
5. Subtract the equations and define \( \psi_-=\psi_R-\psi_L \).
6. Obtain \( i\dot{\psi}_-=-m\psi_- \).
7. Read off the rest-frame frequencies \( \omega=\pm m \).

**Higgs-origin mass term**
1. Replace the constant mass coefficient by a scalar-field coupling \( g\phi(x) \).
2. In empty space with \( \phi=0 \), the fermion remains massless.
3. If the vacuum settles at a constant nonzero value \( \phi_{\mathrm{vac}} \), then \( g\phi_{\mathrm{vac}} \) acts exactly like the mass term.
4. Identify the effective fermion mass as \( m_{\mathrm{eff}}=g\phi_{\mathrm{vac}} \).

**Potential and symmetry-breaking picture**
1. Introduce a scalar potential energy density \( V(\phi) \).
2. Impose the symmetry \( \phi\mapsto -\phi \), so \( V(\phi)=V(-\phi) \).
3. Compare a potential with minimum at \( \phi=0 \) against one with minima at nonzero \( \phi \).
4. If the minimum were at \( \phi=0 \), the fermion mass term from \( g\phi \) would vanish in the vacuum.
5. If the minimum is at nonzero \( \phi \), the vacuum provides a nonzero effective mass.
6. Small oscillations about the chosen minimum are the Higgs quanta.

**\(3+1\)-dimensional matrix algebra**
1. Generalize the linear ansatz to \( \omega=\alpha_1k_1+\alpha_2k_2+\alpha_3k_3+\beta m \).
2. Square the expression.
3. Match \(k_i^2\) terms by imposing \( \alpha_i^2=1 \).
4. Remove \(k_ik_j\) cross terms by imposing \( \alpha_i\alpha_j+\alpha_j\alpha_i=0 \) for \( i\neq j \).
5. Combine these into \( \alpha_i\alpha_j+\alpha_j\alpha_i=2\delta_{ij} \).
6. Remove \(k_im\) cross terms by imposing \( \alpha_i\beta+\beta\alpha_i=0 \).
7. Keep \( \beta^2=1 \).
8. Conclude that \(2\times2\) matrices are insufficient; the first working case is \(4\times4\).

## Notation Choices
- Use \( \psi(x,t)\sim e^{i(kx-\omega t)} \) for the trial wave throughout the recap.
- Use \( \omega \) for frequency/energy and \( k \) for wave number/momentum in \(1+1\) dimensions.
- State explicitly that units are \( c=1 \) and effectively \( \hbar=1 \) when identifying \( \omega \) with energy.
- Write time derivatives as dots only after they have been introduced: \( \dot{\psi}=\partial_t\psi \).
- Use \( \psi_R,\psi_L \) for the two-component \(1+1\)-dimensional fields.
- Use \( \Psi \) for the two-component column vector, not \( \psi \), once the matrix notation is introduced.
- Use
  \( \alpha=\begin{pmatrix}1&0\\0&-1\end{pmatrix} \),
  \( \beta=\begin{pmatrix}0&1\\1&0\end{pmatrix} \)
  for the \(1+1\)-dimensional discussion.
- Keep the shorthand \( \omega=\alpha k \) and \( \omega=\alpha k+\beta m \) clearly labeled as operator/matrix shorthand acting on plane waves.
- Use \( \psi_\pm=\psi_R\pm\psi_L \) exactly as in the lecture; normalization factors like \(1/\sqrt2\) are optional and should not be inserted unless the surrounding text explicitly says the normalization choice is conventional.
- After the mass term is introduced, prefer “upper component” and “lower component” in explanatory remarks, with a note that \(R/L\) came from the massless interpretation.
- For the Higgs section, use \( \phi \) for the scalar field, \( g \) for the coupling, and \( V(\phi) \) for the scalar potential.
- In the \(3+1\)-dimensional preview, use \( k_i \) with \( i=1,2,3 \) and identify these with \(x,y,z\).
- Use \( \alpha_i \) and \( \beta \) for the \(4\times4\) matrices; reserve \( \sigma_i \) for the Pauli matrices.
- If component indices are ever needed in prose, use spinor indices \(p,q\), but prefer matrix notation and avoid index-heavy presentation.

## Uncertain Mathematics
- The earliest first-order equation is mistranscribed once as “\(d\psi/ds\)”; the mathematically safe form is \( \partial_x\psi+\partial_t\psi=0 \).
- The transcript briefly confuses the velocity ratio as \(k/\omega\) before correcting it; preserve only the sign logic, not the mistaken formula.
- The left-moving branch discussion around 00:14 is garbled. The reliable reconstruction is \( \partial_t\psi_L=+\partial_x\psi_L \) leading to \( \omega=-k \), but the intermediate spoken algebra should not be over-written as exact chalk.
- Around 00:27–00:28 the transcript momentarily muddles the ansatz verbally. The intended form is \( \omega=\alpha k+\beta m \), not any asymmetric variant with duplicated mass terms.
- The matrix expansion near 00:34–00:35 is too corrupted to trust line by line; use the compact matrix equation plus the later clean component equations instead.
- In the \(3+1\)-dimensional algebra, the transcript first omits the factor of \(2\) in the anticommutator formula and later corrects it. The final notes should use \( \alpha_i\alpha_j+\alpha_j\alpha_i=2\delta_{ij} \).
- The lecture’s explicit \(4\times4\) matrix entries are too noisy to rely on directly from the transcript. The safe presentation is the standard block form with Pauli matrices.
- The Higgs discussion contains several garbled stretches. Keep only the secure mathematical core:
  \( g\phi \) replacing the constant mass term,
  nonzero vacuum value \( \langle\phi\rangle \),
  symmetric potential \( V(\phi)=V(-\phi) \),
  minima away from zero,
  and Higgs particles as oscillations about the chosen minimum.
- The figure of \( V(\phi) \) does not by itself prove a full textbook double-well; it safely supports the contrast between a centered minimum and minima at nonzero \( \phi \).