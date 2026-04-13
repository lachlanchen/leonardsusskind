# Math Bank
## Core Equations
- \(U|\psi\rangle\) [visible]
- \(U^\dagger U = 1\) [standard reconstruction]
- \(U^\dagger = U^{-1}\) [transcript-backed]
- \(U(\epsilon)=1+i\epsilon L+O(\epsilon^2)\) [transcript-backed]
- \(L^\dagger=L\) [transcript-backed]
- \([L_x,L_y]=iL_z\) [transcript-backed]
- \([L_i,L_j]=i\epsilon_{ijk}L_k\) [transcript-backed]
- \(U_x(\epsilon)U_y(\delta)U_x^{-1}(\epsilon)U_y^{-1}(\delta)=1+i\epsilon\delta L_z+O(\epsilon^2,\delta^2)\) [standard reconstruction]
- \(T_x(\epsilon)=1+i\epsilon P_x\) [transcript-backed]
- \(T_y(\epsilon)=1+i\epsilon P_y\) [transcript-backed]
- \([P_i,P_j]=0\) [transcript-backed]
- \([L_i,P_j]=i\epsilon_{ijk}P_k\) [standard reconstruction]
- \(U|E\rangle\) [visible]
- \(H|E\rangle=E|E\rangle\) [visible]
- \(HU|E\rangle=E\,U|E\rangle\) [visible]
- \(E\,U|E\rangle=U\,E|E\rangle=UH|E\rangle\) [transcript-backed]
- \((HU-UH)|E\rangle=0\) [visible]
- \([U,H]=0\) [visible]
- \([L_i,H]=0\) [standard reconstruction]
- \([O,H]=0 \Rightarrow \dot O=0\) [standard reconstruction]
- \(E_{l,m}=E_l\) for fixed total angular momentum \(l\) [standard reconstruction]
- \(Q=C^\dagger A+A^\dagger C\) [transcript-backed]
- \(Q_\alpha\) [transcript-backed]
- \(Q|B\rangle\sim|F\rangle\) [transcript-backed]
- \(Q|F\rangle\sim|B\rangle\) [transcript-backed]
- \(Q|0\rangle=0\) [transcript-backed]
- \([A_i,A_j]=0\) [standard reconstruction]
- \([A_i^\dagger,A_j^\dagger]=0\) [standard reconstruction]
- \([A_i,A_j^\dagger]=\delta_{ij}\) [standard reconstruction]
- \(A_i^\dagger A_j^\dagger=A_j^\dagger A_i^\dagger\) [transcript-backed]
- \(\{C_i,C_j\}=0\) [standard reconstruction]
- \(\{C_i^\dagger,C_j^\dagger\}=0\) [standard reconstruction]
- \(\{C_i,C_j^\dagger\}=\delta_{ij}\) [standard reconstruction]
- \((C^\dagger)^2=0\) [transcript-backed]
- \(C_i^\dagger C_j^\dagger=-\,C_j^\dagger C_i^\dagger\) [transcript-backed]
- \(\alpha_i\alpha_j=\alpha_j\alpha_i\) [transcript-backed]
- \(\theta_i\theta_j=-\,\theta_j\theta_i\) [transcript-backed]
- \(\theta_i^2=0\) [transcript-backed]
- \(\alpha\theta=\theta\alpha\) [transcript-backed]
- \(f(\theta)=\alpha+\beta\theta\) [transcript-backed]
- \(f(\theta_1,\theta_2)=\alpha+\beta_1\theta_1+\beta_2\theta_2+\gamma\,\theta_1\theta_2\) [transcript-backed]
- \(\dfrac{\partial \alpha}{\partial\theta}=0\) [transcript-backed]
- \(\dfrac{\partial \theta}{\partial\theta}=1\) [transcript-backed]
- \(\partial_{\theta_1}f=\beta_1+\gamma\,\theta_2\) [transcript-backed]
- \(\partial_{\theta_2}f=\beta_2-\gamma\,\theta_1\) [transcript-backed]
- \(e^{a\theta}=1+a\theta\) [transcript-backed]
- \(e^{a\theta}e^{b\theta}=e^{(a+b)\theta}\) [transcript-backed]
- \(e^{\theta_1}e^{\theta_2}=(1+\theta_1)(1+\theta_2)=1+\theta_1+\theta_2+\theta_1\theta_2\) [transcript-backed]

## Definitions And Objects
- \(U\): finite symmetry operator; unitary; may represent rotation, translation, isospin transformation, or another genuine symmetry of the system.
- \(L_i\): infinitesimal generators of rotations; for spatial rotations these are angular-momentum operators.
- \(P_i\): infinitesimal generators of spatial translations; physically the momentum operators.
- \(H\): Hamiltonian operator.
- \(|E\rangle\): energy eigenket.
- \(E\): scalar energy eigenvalue appearing in \(H|E\rangle=E|E\rangle\).
- \(|0\rangle\): vacuum state.
- \(0\): zero vector; distinct from the vacuum.
- \(Q\): prototype supersymmetry generator exchanging bosons and fermions.
- \(Q_\alpha\): spinor-indexed supersymmetry generator; the index carries half-integer spin information.
- \(A,A^\dagger\): bosonic annihilation and creation operators.
- \(C,C^\dagger\): fermionic annihilation and creation operators.
- \(\alpha,\beta,\gamma\): ordinary commuting coefficients.
- \(\theta_i\): Grassmann numbers; anticommuting bookkeeping variables.
- \([X,Y]\equiv XY-YX\): commutator.
- \(\{X,Y\}\equiv XY+YX\): anticommutator.
- \(m\) or \(M\): magnetic quantum number; \(z\)-component label inside a fixed angular-momentum multiplet.
- \(\epsilon_{ijk}\): Levi-Civita symbol.

## Derivation Steps
Symmetry operator is unitary
1. A symmetry acts on state vectors by an operator \(U\).
2. Probability conservation requires norms to be preserved for every state.
3. Norm preservation gives \(U^\dagger U=1\).
4. Therefore \(U^\dagger=U^{-1}\).

Infinitesimal symmetry transformation
1. No transformation corresponds to \(U=1\), not \(U=0\).
2. A very small transformation must therefore be \(U=1+\epsilon(\text{something})\).
3. Unitarity to first order requires the “something” to be \(iL\) with \(L\) Hermitian.
4. Hence \(U(\epsilon)=1+i\epsilon L+O(\epsilon^2)\).

Rotation commutator from the small loop
1. Take \(U_x=1+i\epsilon L_x\) and \(U_y=1+i\delta L_y\).
2. Form \(U_xU_yU_x^{-1}U_y^{-1}\).
3. First-order terms in \(\epsilon\) and \(\delta\) cancel.
4. Keep only terms of order \(\epsilon\delta\).
5. The surviving contribution is proportional to \([L_x,L_y]\).
6. Geometrically the lecture identifies the net effect as a small rotation about the \(z\)-axis by angle \(\epsilon\delta\).
7. Therefore the cleaned final relation is \([L_x,L_y]=iL_z\), and cyclically \([L_i,L_j]=i\epsilon_{ijk}L_k\).

Translations and momenta
1. Write an infinitesimal translation as \(T_i(\epsilon)=1+i\epsilon P_i\).
2. Translate in \(x\), then \(y\), then undo \(x\), then undo \(y\).
3. In Euclidean space the point returns to the same place.
4. Therefore \([P_i,P_j]=0\).

Rotation-translation commutator
1. Translate a point.
2. Rotate it.
3. Undo the translation along the original axis.
4. Undo the rotation.
5. The point does not return to its starting position.
6. Therefore rotations and translations do not commute.
7. The final notes may record this as \([L_i,P_j]=i\epsilon_{ijk}P_k\).

Symmetry criterion \([U,H]=0\)
1. Start with an energy eigenstate \(H|E\rangle=E|E\rangle\).
2. If \(U\) is a symmetry, \(U|E\rangle\) must have the same energy.
3. Therefore \(HU|E\rangle=E\,U|E\rangle\).
4. Since \(E\) is a scalar, \(E\,U|E\rangle=U\,E|E\rangle\).
5. Use \(E|E\rangle=H|E\rangle\) to get \(HU|E\rangle=UH|E\rangle\).
6. Hence \((HU-UH)|E\rangle=0\).
7. If this holds for every energy eigenstate and the energy eigenstates are complete, then \([U,H]=0\).

Generator criterion \([L_i,H]=0\)
1. Write \(U=1+i\epsilon L_i+O(\epsilon^2)\).
2. Impose \([U,H]=0\).
3. Since \([1,H]=0\), the first nontrivial term gives \([L_i,H]=0\).

Vacuum action of the supersymmetry generator
1. Take \(Q=C^\dagger A+A^\dagger C\).
2. Act on \(|0\rangle\).
3. \(A|0\rangle=0\) because there is no boson to annihilate.
4. \(C|0\rangle=0\) because there is no fermion to annihilate.
5. Therefore \(Q|0\rangle=0\).
6. This is the zero vector, not a new vacuum state.

Bosonic exchange symmetry
1. Bosonic creation operators commute.
2. Therefore \(A_i^\dagger A_j^\dagger=A_j^\dagger A_i^\dagger\).
3. A two-boson state is unchanged by exchanging the labels \(i\leftrightarrow j\).

Fermionic exclusion and antisymmetry
1. Fermionic creation operators anticommute.
2. For one mode, \(\{C^\dagger,C^\dagger\}=0\).
3. Hence \(2(C^\dagger)^2=0\), so \((C^\dagger)^2=0\).
4. This is the Pauli exclusion principle in operator form.
5. For two labels, \(C_i^\dagger C_j^\dagger=-C_j^\dagger C_i^\dagger\).
6. A two-fermion state changes sign under exchange of labels.

Grassmann square is zero
1. Grassmann numbers satisfy \(\theta_i\theta_j=-\theta_j\theta_i\).
2. Set \(i=j\).
3. Then \(\theta_i\theta_i=-\theta_i\theta_i\).
4. So \(2\theta_i^2=0\).
5. Hence \(\theta_i^2=0\).

Grassmann derivatives
1. For one variable, \(f(\theta)=\alpha+\beta\theta\).
2. Define \(\partial_\theta \alpha=0\) and \(\partial_\theta\theta=1\).
3. Then \(\partial_\theta f=\beta\).
4. For two variables, \(f=\alpha+\beta_1\theta_1+\beta_2\theta_2+\gamma\theta_1\theta_2\).
5. Differentiate with respect to \(\theta_1\) as in ordinary calculus to get \(\beta_1+\gamma\theta_2\).
6. Differentiate with respect to \(\theta_2\) using the lecture’s sign rule that the derivative operator itself is Grassmann-odd.
7. Passing \(\partial_{\theta_2}\) through \(\theta_1\) introduces a minus sign.
8. Therefore \(\partial_{\theta_2}f=\beta_2-\gamma\theta_1\).

Single-Grassmann exponential
1. Expand \(e^{a\theta}\) in a power series.
2. Since \(\theta^2=0\), all terms beyond first order vanish.
3. Therefore \(e^{a\theta}=1+a\theta\).
4. Multiply \((1+a\theta)(1+b\theta)\).
5. The \(ab\theta^2\) term vanishes.
6. Therefore \(e^{a\theta}e^{b\theta}=1+(a+b)\theta=e^{(a+b)\theta}\).

## Notation Choices
- Use \(U\) for a finite symmetry operator.
- Use \(U(\epsilon)=1+i\epsilon L+O(\epsilon^2)\) for an infinitesimal transformation.
- Use \(L_i\) as the default notation for rotation generators; specialize to \(L_x,L_y,L_z\) only in the rotation commutator example.
- Use \(P_i\) for translation generators.
- Use \(|E\rangle\) for the energy eigenket and plain \(E\) for the scalar eigenvalue; add a brief clarifying sentence in the chapter because the lecture overloads the symbol.
- Use \([U,H]=0\) and then \([L_i,H]=0\) as the standardized symmetry criteria.
- Use \(\epsilon\) and \(\delta\) for the two small rotation parameters in the worked commutator example.
- Use \(Q\) in the first prototype discussion, then switch to \(Q_\alpha\) once the spinor-index issue is introduced.
- Use \(|0\rangle\) for the vacuum and explicitly distinguish it from the zero vector.
- Use \(A,A^\dagger\) for bosonic annihilation/creation and \(C,C^\dagger\) for fermionic annihilation/creation throughout.
- Use \([X,Y]=XY-YX\) and \(\{X,Y\}=XY+YX\) explicitly once, then rely on standard notation.
- Use \(\theta_i\) for Grassmann variables and \(\alpha,\beta_i,\gamma\) for commuting coefficients.
- Use \(m\) in final formulas for the magnetic quantum number, with a note that the lecture refers to it verbally as “M”.
- For Grassmann differentiation, adopt the sign convention implied by the lecture: the derivative operator is Grassmann-odd; the displayed formulas above correspond to a left-derivative convention.

## Uncertain Mathematics
- \(U|\psi\rangle\) in `lecture_04_figure_02.png` is only partially visible; do not infer more than the secure transformed-ket notation.
- The lower line in `lecture_04_figure_02.png` is best normalized as \(U^\dagger U=1\), but the board could have ended with \(1\) or \(I\).
- The exact intermediate combinatorics of the small-rotation calculation are messy in the transcript and include a factor-of-two confusion; keep only the cleaned final result in display math.
- The spoken mixed commutator between rotations and translations is rough and partially garbled; \([L_i,P_j]=i\epsilon_{ijk}P_k\) should be presented as a cautious standard reconstruction.
- The lower commutator in `lecture_04_figure_06.png` is not perfectly sharp; standardize it as \([L_i,H]=0\), but note that the board may have shown \([L,H]=0\).
- The lecture’s operator identities for bosons and fermions are sometimes given in single-mode form and sometimes in labeled multi-mode form; the \(\delta_{ij}\) versions are a cleanup, not always literally written.
- The statement “Grassmann times Grassmann is ordinary” should be phrased carefully in the chapter. For example, \(\theta_1\theta_2\) is commuting in the graded sense, but it is not an ordinary numerical scalar in the naive sense because it can still be nilpotent.
- The transcript around 01:11:35–01:12:15 is corrupted and should not be used as evidence for fine mathematical claims.
- The multi-Grassmann exponential discussion is unresolved in this lecture. Do not state \(e^{\theta_1}e^{\theta_2}=e^{\theta_1+\theta_2}\) as an established result here.
- Likewise, do not impose a polished general BCH-style Grassmann exponential law that the lecture itself does not settle.