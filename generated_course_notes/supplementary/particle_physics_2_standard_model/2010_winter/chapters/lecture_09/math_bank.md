# Math Bank
## Core Equations
- \(F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu\) [visible]
- \(\mathcal L_{\text{gauge}} \propto F_{\mu\nu}F^{\mu\nu}\) [transcript-backed]
- \(A_\mu \to A_\mu+\partial_\mu\theta\) [transcript-backed]
- \(\phi=\rho e^{i\alpha}\) [transcript-backed]
- \(\phi \approx F e^{i\alpha(x)}\) in the frozen-radial approximation [visible]
- \(D\phi=\partial\phi+iA\phi\) [visible]
- \(D_\mu\phi=(\partial_\mu+iA_\mu)\phi\) [standard reconstruction]
- \(D_\mu\phi \approx i(\partial_\mu\alpha+A_\mu)\,F e^{i\alpha}\) [standard reconstruction]
- \(|D_\mu\phi|^2 \approx F^2(\partial_\mu\alpha+A_\mu)(\partial^\mu\alpha+A^\mu)\) [standard reconstruction]
- \(A'_\mu \equiv A_\mu+\partial_\mu\alpha\) [transcript-backed]
- \(|D_\mu\phi|^2 \approx F^2 A'_\mu A'^\mu\) [standard reconstruction]
- \(F^2(\partial_\mu\alpha)(\partial^\mu\alpha)\) for the uncoupled phase mode [transcript-backed]
- \(i\left(\dfrac{\partial \Psi}{\partial t}+\alpha_i\dfrac{\partial \Psi}{\partial x_i}\right)=0\) [transcript-backed]
- \(i\left(\dfrac{\partial \Psi}{\partial t}+\alpha_i\dfrac{\partial \Psi}{\partial x_i}\right)=m\beta\Psi\) [visible]
- \(i\left(\dfrac{\partial \Psi_R}{\partial t}+ i\,\alpha_i\dfrac{\partial \Psi_R}{\partial x_i}\right)=m\Psi_L\) [standard reconstruction]
- \(i\left(\dfrac{\partial \Psi_L}{\partial t}- i\,\alpha_i\dfrac{\partial \Psi_L}{\partial x_i}\right)=m\Psi_R\) [standard reconstruction]
- \(\Psi_L \to e^{i\theta}\Psi_L\) [transcript-backed]
- \(\Psi_R \to \Psi_R\) [transcript-backed]
- \(\phi \to e^{i\theta}\phi\) [transcript-backed]
- \(\phi^* \to e^{-i\theta}\phi^*\) [transcript-backed]
- \(m\Psi_L \rightsquigarrow g\,\phi^*\,\Psi_L\) [transcript-backed]
- \(m\Psi_R \rightsquigarrow g\,\phi\,\Psi_R\) [transcript-backed]
- \(m_f=gF\) [transcript-backed]
- \(\phi \approx F+h\) with \(h\) the Higgs fluctuation [standard reconstruction]
- \(g_e \sim 10^{-5}\) [transcript-backed]
- \(g_t = \mathcal O(1)\) [transcript-backed]
- \(\nu_L \leftrightarrow \bar\nu_R\) as the neutrino mass-mixing pattern described in the lecture [transcript-backed]

## Definitions And Objects
- \(A_\mu\): gauge potential in the toy \(U(1)\) model; pedagogical stand-in for the weak gauge fields, not the literal photon in the physical interpretation.
- \(F_{\mu\nu}\): field-strength tensor built from derivatives of \(A_\mu\).
- `\(F^2\)`: lecture shorthand for the gauge-field kinetic/Lagrangian term; not a complete notational formula by itself.
- \(\phi\): charged Higgs-like complex scalar field.
- \(\rho\): radial magnitude of the Higgs field.
- \(\alpha\): phase field; the would-be Goldstone mode before coupling/gauge fixing.
- \(F\): vacuum magnitude of the Higgs field after spontaneous symmetry breaking; board often writes lower-case \(f\).
- \(D_\mu\): covariant derivative in the lecture’s suppressed-coupling toy model.
- \(A'_\mu\): gauge-shifted vector potential after absorbing \(\alpha\).
- Goldstone boson: massless phase mode before being absorbed by the gauge field.
- Higgs boson: radial excitation about the symmetry-broken minimum.
- \(\Psi\): Dirac field for an electron, muon, quark, or analogous fermion.
- \(\Psi_L,\Psi_R\): left- and right-handed components in the lecture’s rough handedness language.
- \(\alpha_i,\beta\): Dirac matrices in Susskind’s notation.
- \(m\): fermion mass parameter in the Dirac equation; interpreted as left-right mixing.
- \(g\): Yukawa coupling constant; species-dependent.
- Majorana particle: particle whose mass mixes it with its antiparticle, used here for the neutrino discussion.

## Derivation Steps
Gauge-boson mass from the broken Higgs phase
1. Start from a gauge-field Lagrangian built only from \(F_{\mu\nu}\), hence only from derivatives of \(A_\mu\).
2. Conclude that a homogeneous shift of \(A_\mu\) costs no energy, so the gauge boson is massless.
3. Introduce a charged scalar \(\phi=\rho e^{i\alpha}\).
4. Use the Mexican-hat potential to place the minimum at nonzero radius \(F\).
5. Freeze the radial mode: \(\rho \approx F\), leaving only \(\alpha(x)\) dynamical.
6. Compute \(D_\mu\phi\) for \(\phi \approx F e^{i\alpha}\).
7. Obtain the combination \((\partial_\mu\alpha+A_\mu)\).
8. Form \(|D_\mu\phi|^2\) and get \(F^2(\partial_\mu\alpha+A_\mu)(\partial^\mu\alpha+A^\mu)\).
9. Recognize \(A_\mu+\partial_\mu\alpha\) as a gauge transform of \(A_\mu\).
10. Rename \(A'_\mu=A_\mu+\partial_\mu\alpha\).
11. Read the term as \(F^2A'_\mu A'^\mu\), i.e. a no-derivative quadratic term for the gauge field.
12. Interpret \(\alpha\) as absorbed and the gauge boson as massive.

Why the \(A^2\) term counts as a mass term
1. Identify mass with energy at rest.
2. Translate “at rest” into field language as zero momentum.
3. Translate zero momentum into infinite wavelength.
4. Translate infinite wavelength into a homogeneous field shift.
5. Note that derivative-only terms vanish on homogeneous shifts.
6. Conclude that derivative-only dynamics implies masslessness.
7. Note that a term proportional to \(A_\mu A^\mu\) survives on a homogeneous shift.
8. Conclude that such a term stores nonzero energy at zero momentum.
9. Identify that stored energy as the mass.

Uncoupled Goldstone mode versus absorbed phase mode
1. Before coupling to \(A_\mu\), the phase dynamics is schematically \(F^2(\partial\alpha)^2\).
2. Because only derivatives of \(\alpha\) appear, a constant shift of \(\alpha\) costs no energy.
3. This makes the phase mode a massless Goldstone excitation.
4. After coupling, \(\partial_\mu\alpha\) appears only in the combination \(\partial_\mu\alpha+A_\mu\).
5. After the gauge redefinition, the independent \(\alpha\) mode is gone from the spectrum.

Fermion mass as left-right mixing
1. Start from the massless Dirac equation with only derivative terms.
2. Infer, by the same logic as before, that this corresponds to a massless field.
3. Split \(\Psi\) into \(\Psi_L\) and \(\Psi_R\).
4. Write the coupled first-order equations for \(\Psi_L\) and \(\Psi_R\).
5. Observe that the right-hand side of each equation contains the opposite-handed field.
6. Conclude that the mass term is exactly the coupling between left- and right-handed components.
7. Note that if \(m=0\), the left and right sectors decouple.

Why a bare fermion mass is forbidden in the toy weak-asymmetric world
1. Assume \(\Psi_L\) carries the relevant \(U(1)\) charge but \(\Psi_R\) does not.
2. Apply the transformation \(\Psi_L\to e^{i\theta}\Psi_L\), \(\Psi_R\to \Psi_R\).
3. Check the bare mass-coupling equations.
4. See that one side of the equation picks up a phase while the other does not.
5. Equivalently, interpret the left-right conversion as violating charge conservation.
6. Conclude that a direct bare mass term is not symmetry-allowed.

Yukawa rescue mechanism
1. Introduce a charged boson field \(\phi\) with transformation \(\phi\to e^{i\theta}\phi\).
2. Replace the bare mass term by a field-dependent coupling using \(\phi\) or \(\phi^*\).
3. Check the phases on both sides of the equations.
4. See that the phases cancel.
5. Conclude that the new coupling respects the symmetry.
6. Interpret the process as left-right conversion accompanied by emission or absorption of a charged boson.
7. Identify the coupling strength as the Yukawa coupling \(g\).

Fermion mass after spontaneous symmetry breaking
1. Take the Higgs field to sit near its broken-symmetry value \(F\).
2. Approximate \(\phi \approx F\) when the radial mode is frozen.
3. Replace \(g\phi\) by \(gF\).
4. Read the resulting coefficient as the effective fermion mass.
5. Conclude \(m_f=gF\).

Higgs-fermion interaction from restoring the fluctuation
1. Undo the strict freezing of the Higgs field.
2. Write the field schematically as \(\phi \approx F+h\).
3. Substitute into the Yukawa term.
4. Separate the constant piece \(gF\) from the fluctuation piece \(gh\).
5. Interpret \(gF\) as the fermion mass.
6. Interpret \(gh\) as the coupling of the physical Higgs boson to the fermion.
7. Conclude that heavier fermions couple more strongly to the Higgs.

Yukawa hierarchy estimate
1. Use the weak-boson mass scale to estimate \(F\).
2. Compare the electron mass with that scale.
3. Infer \(g_e \sim m_e/F \sim 10^{-5}\).
4. Compare the top-quark mass with the same scale.
5. Infer \(g_t\) is of order unity.
6. Conclude that the species dependence of fermion masses is encoded in the Yukawa couplings.

Neutrino mass logic in the lecture
1. Recall that fermion mass means left-right mixing.
2. For neutrinos, the available right-handed state can be the right-handed antineutrino.
3. Consider mixing \(\nu_L\) with \(\bar\nu_R\).
4. Note that this is allowed because the neutrino lacks the electric-charge obstruction that blocks the analogous electron process.
5. Identify this particle-antiparticle mixing pattern with the Majorana idea.

## Notation Choices
- Use \(F\) for the symmetry-breaking magnitude in the chapter body.
- Mention once that the board often writes lower-case \(f\), but do not alternate freely afterward.
- Use \(A_\mu\) and \(F_{\mu\nu}\) with Lorentz indices restored in the notes, even when the board suppresses them.
- Use \(D_\mu=\partial_\mu+iA_\mu\) as the lecture’s working convention, with the gauge coupling absorbed into \(A_\mu\).
- Do not introduce a separate explicit gauge coupling unless the local passage requires it; the lecture suppresses it throughout.
- Use \(A'_\mu=A_\mu+\partial_\mu\alpha\) for the absorbed/gauge-shifted field.
- Keep `\(F^2\)` as lecture shorthand only; when typesetting a real formula, write a tensor contraction or a prose description of the kinetic term.
- Use \(\Psi_L,\Psi_R\) for the fermion components, but note in prose elsewhere that the lecture is loose about helicity versus chirality.
- Keep Susskind’s matrix notation \(\alpha_i,\beta\) rather than rewriting everything immediately into \(\gamma^\mu\) notation.
- Use \(g\) for the Yukawa coupling because that is the lecture’s letter.
- Reserve \(h\) for the Higgs fluctuation if the chapter needs an explicit symbol for the physical Higgs mode.
- Keep the lecture in the toy \(U(1)\) setting at the equation level; do not prematurely rewrite the chapter into full \(SU(2)\times U(1)\) Higgs-doublet notation unless a later section explicitly upgrades it.

## Uncertain Mathematics
- The sign of the covariant derivative is unstable in the lecture. Susskind explicitly says he may have “blown the sign,” so the final notes should choose one convention and state it cleanly.
- The board writes \(D\phi=\partial\phi+iA\phi\) schematically, without Lorentz indices and without an explicit gauge coupling. Indexed formulas are reconstructions.
- The step from \(D\phi\) to \(|D_\mu\phi|^2\) is only partially written on the board. The indexed quadratic form is standard completion, not literal board transcription.
- The board’s \(f^2A^2\) omits indices and metric signature. The intended relativistic object is \(F^2A_\mu A^\mu\)-type, but the precise sign depends on convention.
- The normalization of the gauge kinetic term is not given in textbook form in the lecture. Avoid inserting \(-\tfrac14 F_{\mu\nu}F^{\mu\nu}\) unless the chapter explicitly flags it as a standard normalization choice.
- The exact split Dirac equations for \(\Psi_L,\Psi_R\) are notation-unstable on the board. The placement of the factors of \(i\) should be treated cautiously and standardized from transcript plus conventional cleanup.
- The lecture’s “left-handed” and “right-handed” language is physically motivated but not technically sharp; it slides between helicity-style language and chirality-style field decomposition.
- The neutrino discussion is schematic. The lecture gives the mixing logic for a Majorana interpretation but does not present a full neutrino mass Lagrangian.
- The value of the electroweak scale is discussed at two levels: \(W/Z\) masses near \(90\)–\(100\ \mathrm{GeV}\) and the symmetry-breaking scale \(F\) later quoted as about \(250\ \mathrm{GeV}\). Final notes should distinguish “order of the weak scale” from the literal gauge-boson masses.
- The historical Higgs-mass estimate and LHC remarks are lecture-time expectations, not stable present-day inputs for the mathematics.