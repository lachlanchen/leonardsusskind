# Math Bank
## Core Equations
- \(\text{Geometry}=\text{Energy}\) [visible]
- \(\left(\frac{\dot a}{a}\right)^2\) [visible]
- \(\frac{1}{a^2}\) [visible]
- \(F(L)=-\dfrac{dE(L)}{dL}\) [standard reconstruction]
- \(Q^2=0\) [transcript-backed]
- \(\rho=\rho_{\mathrm{matter}}+\rho_{\mathrm{radiation}}+\rho_{\mathrm{vacuum}}\) [transcript-backed]
- \(\rho_{\mathrm{matter}}=\rho_{\mathrm{ordinary}}+\rho_{\mathrm{dark}}\) [transcript-backed]
- \(\left(\frac{\dot a}{a}\right)^2 \pm \frac{1}{a^2}-\rho_{\mathrm{matter}}-\rho_{\mathrm{radiation}}-\rho_{\mathrm{vacuum}}=0\) [standard reconstruction]
- \(H_{\mathrm{tot}}=0\) [transcript-backed]
- \(\rho_{\mathrm{matter}}\propto a^{-3}\) [standard reconstruction]
- \(\rho_{\mathrm{radiation}}\propto a^{-4}\) [standard reconstruction]
- \(\rho_{\mathrm{vacuum}}=\text{constant}\) [transcript-backed]
- \(\alpha^{-1}_{\mathrm{em}}(E_U)\approx \alpha^{-1}_{\mathrm{ew}}(E_U)\approx \alpha^{-1}_{s}(E_U)\), with \(E_U\sim 10^{15}\text{--}10^{16}\,\mathrm{GeV}\) [standard reconstruction]
- \(\theta^2=0\) [transcript-backed]
- \(\bar\theta^2=0\) [transcript-backed]
- \(f(\theta)=a+b\theta\) [transcript-backed]
- \(\dfrac{d}{d\theta}\theta=1\) [transcript-backed]
- \(\int_{-\infty}^{\infty}\frac{dF}{dx}\,dx=F(\infty)-F(-\infty)=0\) [standard reconstruction]
- \(\int d\theta\,1=0\) [transcript-backed]
- \(\int d\theta\,\theta=1\) [transcript-backed]
- \(\int d\theta\,(a+b\theta)=b=\dfrac{d}{d\theta}(a+b\theta)\) [transcript-backed]
- \(f(\theta,\bar\theta)=a+\bar\theta\psi+\bar\psi\,\theta+b\,\bar\theta\theta\) [standard reconstruction]
- \(\int d\theta\,d\bar\theta\,\bar\theta\theta=1\) [transcript-backed]
- \(\int d\bar\theta\,d\theta\,\bar\theta\theta=-1\) [transcript-backed]
- \(\int d\theta\,d\bar\theta\,f(\theta,\bar\theta)=b\) [standard reconstruction]
- \(\Phi(x,\theta)=\phi(x)+\theta_\alpha\psi_\alpha(x)+\theta_\alpha\theta_\beta z_{\alpha\beta}(x)+\cdots+\theta_1\theta_2\theta_3\theta_4 D(x)\) [standard reconstruction]
- \(S=\int d^4x\,d^4\theta\,\mathcal{L}(x,\theta)\) [standard reconstruction]

## Definitions And Objects
- Vacuum energy: zero-point energy of quantum fields; equivalently the energy of empty space.
- Casimir energy: vacuum energy modified by boundary conditions such as reflecting plates.
- Supercharge \(Q\): fermionic generator of supersymmetry; acts by replacing one boson with one fermion or vice versa, not by converting an entire many-body state.
- Higgs self-energy: loop correction attached to the Higgs line; distinct from pure vacuum diagrams.
- LSP: lightest superpartner; the endpoint of a superpartner decay chain in the simple story told here.
- Running coupling: energy-dependent effective coupling, discussed mainly through the plotted inverse coupling \(\alpha^{-1}\).
- Scale factor \(a(t)\): radius/expansion factor of the universe in the cosmology detour.
- Curvature term: the \(1/a^2\)-type geometric contribution whose sign depends on open, closed, or flat spatial geometry.
- Superfield \(\Phi(x,\theta)\): field depending on ordinary coordinates and Grassmann coordinates.
- Grassmann coordinates \(\theta\): nilpotent anticommuting coordinates; in this lecture, effectively two complex or four real coordinates.
- Boson fields: ordinary-number-valued fields.
- Fermion fields: Grassmann-valued fields.
- Berezin integral: definite integral over Grassmann variables; operationally extracts the top component.

## Derivation Steps
One-theta Berezin integration
1. Assume linearity of the Grassmann integral.
2. Use the ordinary model \(\int dx\,\frac{dF}{dx}=0\) for functions that vanish at infinity.
3. Impose the Grassmann analogue \(\int d\theta\,\frac{d}{d\theta}f(\theta)=0\).
4. Take \(f(\theta)=\theta\), so \(\frac{d}{d\theta}\theta=1\), giving \(\int d\theta\,1=0\).
5. Choose the convention \(\int d\theta\,\theta=1\).
6. Since any one-variable function is \(a+b\theta\), the integral returns \(b\), the coefficient of the highest theta term.

Two-theta Berezin integration
1. Expand \(f(\theta,\bar\theta)\) as \(a+\bar\theta\psi+\bar\psi\,\theta+b\,\bar\theta\theta\).
2. Terms with no theta or only one theta integrate to zero.
3. The only surviving term is the quadratic top component.
4. Fix the sign by choosing a measure ordering; with \(d\theta\,d\bar\theta\), \(\int d\theta\,d\bar\theta\,\bar\theta\theta=1\).
5. Reversing the measure order flips the sign.
6. Therefore the two-theta integral extracts the coefficient \(b\).

Ordinary total derivative to Grassmann total derivative
1. Start from \(\int_{-\infty}^{\infty}\frac{dF}{dx}\,dx=F(\infty)-F(-\infty)\).
2. Assume the function dies off at large positive and negative \(x\).
3. Conclude the definite integral of a total derivative vanishes.
4. Use this as the model for the Grassmann rule that the integral of a Grassmann derivative should vanish.

Casimir force logic
1. Reflecting plates modify the vacuum processes that would exist in empty space.
2. Therefore the vacuum energy depends on plate separation.
3. Any energy depending on separation acts like a potential energy.
4. The force is obtained by differentiating that energy with respect to the separation.

Higgs self-energy control
1. Vacuum loops attached to the Higgs line shift the Higgs mass.
2. Without a protecting mechanism, that shift is driven to a very high scale.
3. Since ordinary particle masses are responses to the Higgs sector, they are dragged upward with it.
4. Supersymmetry introduces boson-fermion cancellations in the loop corrections.
5. The naturalness claim depends on those cancellations appearing not too far above accessible energies.

Running-coupling unification logic
1. Electromagnetic screening makes the effective electric coupling increase at short distance, so \(\alpha^{-1}\) falls.
2. Strong interactions behave oppositely because of asymptotic freedom, so the inverse strong coupling rises.
3. In the ordinary Standard Model, the three trajectories tend toward one another but miss.
4. Adding superpartner loops changes the running.
5. If the superpartners are not too heavy, the three gauge couplings extrapolate to a common crossing at high energy.

Vacuum dominance in cosmology
1. Matter density decreases as the universe expands because the number of massive particles in a comoving region stays fixed while the volume grows.
2. Radiation density decreases faster because the photons are diluted and each wavelength is stretched.
3. Vacuum energy density does not dilute.
4. Therefore a component that starts subdominant can eventually dominate.
5. This is the lecture’s explanation for the late-time importance of vacuum energy.

Cosmological Hamiltonian constraint
1. Use the time-time Einstein equation.
2. Put geometry terms on the left: an expansion term involving \((\dot a/a)^2\) and a curvature term involving \(1/a^2\).
3. Put energy-density terms on the right: matter, radiation, and vacuum.
4. Move everything to one side.
5. Interpret the resulting quantity as the canonical Hamiltonian.
6. State the constraint as total energy equal to zero in this cosmological setting.

## Notation Choices
- Use \(a(t)\) for the cosmological scale factor throughout, even though the transcript alternates between spoken \(A\) and written \(a\).
- Use overdots for time derivatives: \(\dot a = da/dt\).
- Write the cosmological content as \(\rho_{\mathrm{matter}}, \rho_{\mathrm{radiation}}, \rho_{\mathrm{vacuum}}\), and decompose matter further as \(\rho_{\mathrm{ordinary}}+\rho_{\mathrm{dark}}\) when needed.
- Use \(Q\) for the supersymmetry generator and keep the algebra to the single lecture-backed identity \(Q^2=0\).
- Use \(\alpha\) for the fine-structure constant and discuss running mainly in terms of \(\alpha^{-1}\), matching the lecture’s plotting preference.
- For the other couplings, use \(\alpha_{\mathrm{ew}}\) and \(\alpha_s\) as note-writing labels only; the lecture itself is qualitative here.
- Use capital \(\Phi\) for a superfield and lowercase \(\phi,\psi,z,D\) for its components.
- For two Grassmann coordinates, use \(\theta,\bar\theta\); for the schematic four-coordinate expansion, use \(\theta_\alpha\).
- Adopt the Grassmann measure order \(d\theta\,d\bar\theta\) so that \(\int d\theta\,d\bar\theta\,\bar\theta\theta=1\).
- State explicitly that exchanging Grassmann variables or exchanging measure order changes the sign.
- Treat Grassmann integrals as definite integrals over full theta-space, never as indefinite integrals.
- Use \(\mathcal{L}(x,\theta)\) for the Lagrangian density and \(S\) for the action.

## Uncertain Mathematics
- The precise Casimir scaling with separation is not secure from the lecture; Susskind hesitates over the power law.
- The cosmological equation is only structurally secure here; exact coefficients such as \(8\pi G/3\) should not be inserted as lecture-backed.
- The sign and normalization of the curvature term are uncertain from the frame evidence and only secure up to the open/closed/flat distinction.
- The equality \(H_{\mathrm{tot}}=0\) should be framed as the cosmological Hamiltonian constraint in the lecture’s minisuperspace-style discussion, not as a universal GR formula.
- The unification claim is qualitative plus the approximate scale \(10^{15}\)–\(10^{16}\,\mathrm{GeV}\); do not add beta-function coefficients or MSSM normalization conventions.
- The superfield expansion is schematic; index contractions, combinatorial factors, and chirality constraints are not fixed in this lecture.
- The two-variable Grassmann sign conventions were corrected live at the board; the final notes should declare one convention and warn about the alternative sign.
- The ordinary total-derivative identity in the board image is only partly visible below the top line; the endpoint evaluation is a cautious transcript-backed completion.
- The scaling laws \(\rho_{\mathrm{matter}}\propto a^{-3}\) and \(\rho_{\mathrm{radiation}}\propto a^{-4}\) are mathematically appropriate completions of the spoken argument, not formulas explicitly written on the board.