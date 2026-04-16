# Math Bank
## Core Equations
- \(H=\frac{\omega}{2}\sigma_z\) [transcript-backed]
- \(E_\pm=\pm \frac{\omega}{2}\) [transcript-backed]
- \(E_+-E_-=\omega\), so the emitted photon energy is \(\omega\) when \(\hbar=1\) [transcript-backed]
- \(|\psi\rangle=\alpha|u\rangle+\beta|d\rangle\) [transcript-backed]
- \(P_{\mathrm{emit}}=|\alpha|^2,\quad P_{\mathrm{no\,emit}}=|\beta|^2,\quad \langle E_{\mathrm{emitted}}\rangle=|\alpha|^2\omega\) [transcript-backed]
- \(|\psi\rangle=\sum_i \alpha_i |\lambda_i\rangle,\quad L|\lambda_i\rangle=\lambda_i|\lambda_i\rangle\) [transcript-backed]
- measurement of \(L\) with outcome \(\lambda_k\): \(|\psi\rangle\to |\lambda_k\rangle\) [transcript-backed]
- \(S_{AI}=S_A\otimes S_I\) [visible]
- \(|a\rangle\otimes|i\rangle\leftrightarrow |a\,i\rangle\) [visible]
- \(\langle b\,j|a\,i\rangle=\delta_{ab}\delta_{ij}\) [visible]
- \(|\Psi\rangle=\sum_{a,i}\alpha_{ai}|a\,i\rangle\) [transcript-backed]
- \(|\Psi\rangle=\alpha_{uu}|uu\rangle+\alpha_{ud}|ud\rangle+\alpha_{du}|du\rangle+\alpha_{dd}|dd\rangle\) [transcript-backed]
- \(|R\rangle=\frac{1}{\sqrt2}(|u\rangle+|d\rangle)\) [transcript-backed]
- \(|u\rangle\otimes|R\rangle=\frac{1}{\sqrt2}(|uu\rangle+|ud\rangle)\) [transcript-backed]
- \((\alpha_u|u\rangle+\alpha_d|d\rangle)\otimes(\beta_u|u\rangle+\beta_d|d\rangle)\) [visible]
- \(\alpha_u\beta_u|uu\rangle+\alpha_u\beta_d|ud\rangle+\alpha_d\beta_u|du\rangle+\alpha_d\beta_d|dd\rangle\) [visible]
- general two-spin pure state: \(4\) complex coefficients \(\to 8\) real parameters \(\to 6\) after normalization and overall phase [transcript-backed]
- product-state family: \(2\) real parameters for \(\sigma\) plus \(2\) real parameters for \(\tau\), hence \(4\) real parameters total [transcript-backed]
- \(\sigma_x=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad \sigma_z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}\) [standard reconstruction]
- \(\sigma_y=\begin{pmatrix}0&-i\\ i&0\end{pmatrix}\) [standard reconstruction]
- \(\sigma_x|u\,i\rangle=|d\,i\rangle,\quad \sigma_x|d\,i\rangle=|u\,i\rangle\) [visible]
- \(\sigma_z|u\,i\rangle=|u\,i\rangle,\quad \sigma_z|d\,i\rangle=-|d\,i\rangle\) [transcript-backed]
- \(\tau_x|a\,u\rangle=|a\,d\rangle,\quad \tau_x|a\,d\rangle=|a\,u\rangle\) [visible]
- \(\tau_z|a\,u\rangle=|a\,u\rangle,\quad \tau_z|a\,d\rangle=-|a\,d\rangle\) [visible]
- \([\sigma_m,\tau_n]=0\) for \(m,n\in\{x,y,z\}\) [transcript-backed]
- \(|\mathrm{sing}\rangle=\frac{1}{\sqrt2}\bigl(|ud\rangle-|du\rangle\bigr)\) [transcript-backed]
- for any pure single-spin state \(|\psi\rangle\), there exists a direction \(\mathbf n\) such that \((\sigma\cdot\mathbf n)|\psi\rangle=|\psi\rangle\) [transcript-backed]
- \(\langle \mathrm{sing}|\sigma_x|\mathrm{sing}\rangle=\langle \mathrm{sing}|\sigma_y|\mathrm{sing}\rangle=\langle \mathrm{sing}|\sigma_z|\mathrm{sing}\rangle=0\) [transcript-backed]
- \(\langle \mathrm{sing}|\tau_x|\mathrm{sing}\rangle=\langle \mathrm{sing}|\tau_y|\mathrm{sing}\rangle=\langle \mathrm{sing}|\tau_z|\mathrm{sing}\rangle=0\) [transcript-backed]
- \(\langle \mathrm{sing}|\sigma_z\tau_z|\mathrm{sing}\rangle=-1\) [transcript-backed]
- \(\langle \mathrm{sing}|\sigma_x\tau_x|\mathrm{sing}\rangle=-1\) [transcript-backed]
- \(\langle \mathrm{sing}|\sigma_y\tau_y|\mathrm{sing}\rangle=-1\) [standard reconstruction]
- \(\langle \mathrm{sing}|\sigma_x\tau_z|\mathrm{sing}\rangle=0\) [transcript-backed]
- \((\sigma_z\tau_z)|\mathrm{sing}\rangle=-|\mathrm{sing}\rangle,\quad (\sigma_x\tau_x)|\mathrm{sing}\rangle=-|\mathrm{sing}\rangle\) [transcript-backed]
- \(|ud\rangle-|du\rangle=|LR\rangle-|RL\rangle=|{\rm in}\,{\rm out}\rangle-|{\rm out}\,{\rm in}\rangle\) up to the same normalization factor on each side [transcript-backed]

## Definitions And Objects
- \(S_A\), \(S_I\): abstract state spaces for two subsystems, introduced before the lecture specializes to two spins.
- \(S_{AI}\): the composite state space, defined as the tensor product of the two subsystem spaces.
- \(|a\,i\rangle\): a basis vector of the composite system, labeled by one basis choice from subsystem \(A\) and one from subsystem \(I\).
- \(\sigma\): the first spin system; its components are \(\sigma_x,\sigma_y,\sigma_z\).
- \(\tau\): the second spin system; its components are \(\tau_x,\tau_y,\tau_z\).
- \(|uu\rangle,|ud\rangle,|du\rangle,|dd\rangle\): the \(z\)-basis for the two-spin system, with first slot for \(\sigma\), second slot for \(\tau\).
- Product state: a state of the form \(|\psi_\sigma\rangle\otimes|\psi_\tau\rangle\), meaning each subsystem has its own state vector.
- Entangled state: a state in the composite space that cannot be written as a single product of subsystem states.
- Spectator index: the untouched slot in a composite ket when an operator acts only on one subsystem.
- Product observable: an operator such as \(\sigma_x\tau_x\), acting nontrivially on both subsystems and probing correlations rather than single-subsystem properties.
- Singlet state: the antisymmetric two-spin state \(\frac{1}{\sqrt2}(|ud\rangle-|du\rangle)\), presented here as the maximally entangled example.
- Triplet sector: the remaining three two-spin states alluded to when Susskind explains why the singlet is called a singlet.

## Derivation Steps
Photon emission from a superposed spin:
1. Start from \(H=\frac{\omega}{2}\sigma_z\), so the only energy levels are \(\pm \omega/2\).
2. A downward transition can only go from the upper level to the lower one.
3. Therefore any emitted photon carries the full level spacing \(\omega\), not \(\omega/2\).
4. If the initial state is \(\alpha|u\rangle+\beta|d\rangle\), only the \(|u\rangle\) component can emit.
5. Hence emission happens with probability \(|\alpha|^2\), and no emission with probability \(|\beta|^2\).
6. The average emitted energy is then \(|\alpha|^2\omega\).

Tensor-product construction:
1. Choose orthonormal bases \(\{|a\rangle\}\) for \(S_A\) and \(\{|i\rangle\}\) for \(S_I\).
2. Form paired basis vectors \(|a\,i\rangle\) for the combined system.
3. Count basis states: if \(\dim S_A=D_A\) and \(\dim S_I=D_I\), then \(\dim S_{AI}=D_A D_I\).
4. Define orthonormality by \(\langle b\,j|a\,i\rangle=\delta_{ab}\delta_{ij}\).
5. Declare the general composite vector to be any linear combination \(\sum_{a,i}\alpha_{ai}|a\,i\rangle\).

Product-state expansion and parameter count:
1. Write a general subsystem state for \(\sigma\): \(\alpha_u|u\rangle+\alpha_d|d\rangle\).
2. Write a general subsystem state for \(\tau\): \(\beta_u|u\rangle+\beta_d|d\rangle\).
3. Form the tensor product and expand into the four basis states.
4. Observe that the four composite coefficients factorize as products \(\alpha_\bullet\beta_\bullet\).
5. Count parameters for a general two-spin state: \(4\) complex numbers, minus normalization, minus overall phase, giving \(6\) real parameters.
6. Count parameters for product states: \(2\) real parameters for each spin, giving only \(4\) real parameters.
7. Conclude that most two-spin states are not product states.

Commutativity of separate-subsystem operators:
1. Act with \(\tau_x\) on a basis state such as \(|uu\rangle\); only the second slot flips.
2. Then act with \(\sigma_x\); only the first slot flips.
3. Reverse the order and note that the same final basis state appears.
4. Repeat the logic for another pair such as \(\sigma_x\) and \(\tau_z\).
5. Since the operators act on different slots, order does not matter on basis states.
6. Therefore \([\sigma_m,\tau_n]=0\).

Vanishing one-spin expectations in the singlet:
1. Recall the single-spin fact: for any pure one-spin state, some \(\sigma\cdot\mathbf n\) has definite value \(+1\).
2. Therefore a pure one-spin state cannot have all three component expectation values equal to zero.
3. Take \(|\mathrm{sing}\rangle=\frac{1}{\sqrt2}(|ud\rangle-|du\rangle)\).
4. Compute \(\langle \mathrm{sing}|\sigma_z|\mathrm{sing}\rangle\) by acting with \(\sigma_z\) on the first slot and taking the inner product.
5. Cross terms vanish, and the remaining terms cancel, so the result is \(0\).
6. Compute \(\langle \mathrm{sing}|\sigma_x|\mathrm{sing}\rangle\) by flipping the first slot; the resulting kets are orthogonal to the bra components, so the result is \(0\).
7. The same flipping logic gives the \(\sigma_y\) result, and by symmetry the same holds for \(\tau\).
8. Conclude that the singlet cannot be a product state.

Same-axis correlations in the singlet:
1. Insert \(\sigma_z\tau_z\) into the singlet sandwich.
2. \(\tau_z\) contributes a sign from the second slot; \(\sigma_z\) contributes a sign from the first slot.
3. Each surviving diagonal term gives \(-1\), and cross terms vanish.
4. After the normalization factor, the expectation value is \(-1\).
5. The same logic with \(\sigma_x\tau_x\) flips both slots and returns the singlet with an overall minus sign.
6. Hence \(\langle \sigma_x\tau_x\rangle=-1\) as well.
7. Read this as perfect anti-correlation for equal spin components.

Mixed-axis correlation example:
1. Insert \(\sigma_x\tau_z\) into the singlet sandwich.
2. \(\tau_z\) changes only signs in the second slot.
3. \(\sigma_x\) flips only the first slot.
4. The resulting kets do not overlap with the bra components.
5. Therefore the expectation value is \(0\).
6. The lecture then verbally generalizes this to unequal components.

Basis-change invariance of the singlet form:
1. Rewrite \(|u\rangle\) and \(|d\rangle\) in the \(x\)-basis as linear combinations of \(|L\rangle\) and \(|R\rangle\).
2. Substitute those expressions into \(|ud\rangle-|du\rangle\).
3. Expand and cancel terms.
4. The antisymmetric form survives as \(|LR\rangle-|RL\rangle\).
5. The lecture states the same pattern again for another basis, schematically \(|{\rm in}\,{\rm out}\rangle-|{\rm out}\,{\rm in}\rangle\).

## Notation Choices
- Use \(|u\rangle\) and \(|d\rangle\) for the single-spin \(z\)-basis, with \(|u\rangle\) the \(+1\) eigenstate of \(\sigma_z\) and \(|d\rangle\) the \(-1\) eigenstate.
- Use \(\sigma\) for the first spin and \(\tau\) for the second spin throughout the concrete two-spin discussion.
- Fix slot order as \(|\sigma,\tau\rangle\), i.e. first slot belongs to \(\sigma\), second slot belongs to \(\tau\).
- In the abstract tensor-product section, keep \(A\) and \(I\) for generic subsystems and \(a,i\) for their basis labels; switch explicitly to \(\sigma,\tau\) when the lecture does.
- Write composite kets as \(|a\,i\rangle\) or \(|uu\rangle\), not with commas; the lecture treats the pair as a single basis label.
- In polished notes, it is consistent to read \(\sigma_m\) as \(\sigma_m\otimes I\) and \(\tau_n\) as \(I\otimes \sigma_n\), even though Susskind speaks in spectator-index language rather than tensor-product-operator notation.
- Use \(|R\rangle\) and \(|L\rangle\) for the \(x\)-basis if needed in the final notes; include the normalization factors even when the lecture suppresses them verbally.
- Standardize the singlet notation as \(|\mathrm{sing}\rangle\).
- Keep \(\hbar=1\) explicitly in the opening section.
- Do not preserve the brief curly-bracket experiment for the \(\tau\)-space notation; the lecture itself abandons it almost immediately.

## Uncertain Mathematics
- The transcript garbles the early identification of \(\alpha\) and \(\beta\) with up and down. The final notes should keep the standard convention and not imitate the garble.
- The spoken matrix entries for \(\sigma_x\), \(\sigma_y\), and \(\sigma_z\) are partially degraded. The standard Pauli matrices are safe conventional completions, but they are not all cleanly visible in the transcript.
- The \(\sigma_y\) action is only described verbally as “flip with an \(i\).” The exact sign convention should be taken from the standard matrix once the basis convention is fixed.
- The transcript appears to misstate the \(\sigma_y\tau_y\) expectation value at one point. The surrounding symmetry and the singlet structure strongly support \(-1\), but that should be presented as a cautious completion.
- The general claim that unequal-component products vanish is only explicitly worked out for \(\sigma_x\tau_z\); broader statements should be marked as lecture-level generalization unless fully derived elsewhere.
- The singlet \(\sigma_z\) sandwich includes a false start and self-correction. The final notes should use the cleaned derivation only.
- The linewidth discussion is verbal. If the final notes use a formula such as \(\Delta E\,\Delta t\sim 1\) or \(\Delta E\sim 1/\tau\), that is a standard reconstruction, not a board-backed lecture equation.
- The basis-change statement for the singlet is transcript-backed, but the lecture does not give a full algebraic proof on the board; any compact proof in the notes will be a reconstruction.