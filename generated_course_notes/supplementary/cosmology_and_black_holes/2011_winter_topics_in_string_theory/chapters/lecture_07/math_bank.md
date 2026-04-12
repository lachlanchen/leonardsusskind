# Math Bank
## Core Equations
- `c=\hbar=1` [visible]
- `E` [visible]
- `E \sim \dfrac{\hbar c}{\lambda}` [standard reconstruction]
- `m=\dfrac{E}{c^2}` [transcript-backed]
- `m\sim \dfrac{1}{\lambda}` in units `c=\hbar=1` [standard reconstruction]

- `a \sim \dfrac{G_N M}{R^2}` [transcript-backed]
- `G_N=\ell_p^2` [transcript-backed]

- `G_N \sim g_s^2 \ell_s^2` [transcript-backed]
- `\ell_p \sim g_s \ell_s` [transcript-backed]
- `g_s\,\ell_s=\ell_p` as board-style form [visible]

- `S_{\mathrm{str}} \sim \dfrac{L}{\ell_s}` [transcript-backed]
- `m_{\mathrm{seg}} \sim \dfrac{1}{\ell_s}` [transcript-backed]
- `M \sim \dfrac{L}{\ell_s^2}` [transcript-backed]
- `L \sim M \ell_s^2` [transcript-backed]
- `S_{\mathrm{str}} \sim M \ell_s` [transcript-backed]
- `S=\dfrac{L}{\ell_s}=M\ell_s` as board-style condensation [visible]
- `M=\dfrac{L}{\ell_s^2}` as board-style lower line [standard reconstruction]

- `S_{\mathrm{BH}}=\dfrac{A}{4G_N}` [transcript-backed]
- `S_{\mathrm{BH}} \sim \dfrac{A}{G_N} \sim \dfrac{A}{\ell_p^2}` [transcript-backed]
- `R_s \sim M G_N` [transcript-backed]
- `A \sim R_s^2 \sim M^2 G_N^2` [transcript-backed]
- `S_{\mathrm{BH}} \sim M^2 G_N \sim M^2 \ell_p^2` [transcript-backed]
- `S_{\mathrm{BH}} = f(M\ell_p)` with `M\ell_p` dimensionless [transcript-backed]

- `S=\text{const.}` under adiabatic variation of coupling [transcript-backed]
- `M g_s = M_0 g_{s,0}` along the isentropic curve at fixed `\ell_s` [transcript-backed]
- `R_s \sim \ell_s` as the crossover criterion [transcript-backed]
- `M G_N \sim \ell_s` at crossover [transcript-backed]
- `M g_s^2 \sim \dfrac{1}{\ell_s}` at crossover, using `G_N \sim g_s^2\ell_s^2` [transcript-backed]
- `M_\ast \ell_s \sim M_0^2 g_{s,0}^2 \ell_s^2 \sim M_0^2 G_{N,0}` [transcript-backed]

- `\Omega = 2^N` [transcript-backed]
- `N \sim \dfrac{V}{V_{\mathrm{cell}}}` [transcript-backed]
- `S_{\max}=\log \Omega \sim \dfrac{V}{V_{\mathrm{cell}}}\log 2` [transcript-backed]
- `S_{\mathrm{initial}} \le S_{\mathrm{final}}` [transcript-backed]
- `S_{\mathrm{final}}=\dfrac{A}{4G_N}` [transcript-backed]
- `S_{\max}=\dfrac{A}{4G_N}` for a region saturating the black-hole bound [transcript-backed]

- `ds^2=-dt^2+a(t)^2\,dx_i dx_i` [transcript-backed]
- `dx_i dx_i = dx^2+dy^2+dz^2` [transcript-backed]
- `d(t)=a(t)\,\Delta x` [transcript-backed]
- `v=\dot d=\Delta x\,\dot a` [transcript-backed]
- `v=\dfrac{\dot a}{a}\,d` [transcript-backed]
- `H=\dfrac{\dot a}{a}` [transcript-backed]
- `v=Hd` [transcript-backed]
- `d_H \sim \dfrac{1}{H}` in units `c=1` [transcript-backed]
- `\dot a = Ha` when `H` is constant [transcript-backed]
- `a(t)=a_0 e^{Ht}` [transcript-backed]
- `a(t)^2 \propto e^{2Ht}` [transcript-backed]

## Definitions And Objects
- `G_N`: Newton’s constant; use this for gravity, not bare `G`, in the final notes.
- `\ell_p`: Planck length, defined so that `G_N=\ell_p^2` in the lecture’s unit system.
- `g_s`: dimensionless string coupling; physically the amplitude for string splitting/rearrangement.
- `\ell_s`: fundamental string length; the scale of the random-walk step or elementary wiggle.
- `L`: total length of the long excited string.
- `m_{\mathrm{seg}}`: mass of one elementary string segment of length `\ell_s`.
- `M`: total mass of the long string or of the black hole, depending on context.
- `S_{\mathrm{str}}`: entropy of the long string.
- `S_{\mathrm{BH}}`: black-hole entropy.
- `R_s`: Schwarzschild radius, used only at scaling level here.
- `M_0, g_{s,0}, G_{N,0}`: target black-hole mass and couplings before the adiabatic deformation.
- `M_\ast, g_{s,\ast}`: mass and coupling at the crossover point where the object becomes string-like.
- `\Omega`: number of configurations in the volume-counting model.
- `N`: number of binary cells or degrees of freedom in the toy counting model.
- `a(t)`: cosmological scale factor.
- `H`: Hubble parameter; for constant `H`, this is the de Sitter case.
- `d(t)`: proper distance between two fixed-coordinate points.
- Dot notation: `\dot a = da/dt`.

## Derivation Steps
1. `m \sim 1/\text{length}` in natural units  
   1. Start from `E \sim \hbar c/\lambda`.  
   2. Convert energy to mass with `m=E/c^2`.  
   3. Set `c=\hbar=1`.  
   4. Conclude `m \sim 1/\lambda`.

2. `G_N` has dimensions of area  
   1. Use `a \sim G_N M/R^2`.  
   2. In `c=1` units, acceleration has units `L/T^2 \sim 1/L`.  
   3. Use `M \sim 1/L` and `R^2 \sim L^2`.  
   4. Solve for `[G_N] \sim L^2`.  
   5. Identify `G_N=\ell_p^2`.

3. Relation between gravity scale and string scale  
   1. The graviton-exchange cartoon says gravitational strength scales like `g_s^2`.  
   2. `g_s^2` is dimensionless, so a length scale must supply the area units.  
   3. The only available string-theory length is `\ell_s`.  
   4. Therefore `G_N \sim g_s^2 \ell_s^2`.  
   5. Taking the square root gives `\ell_p \sim g_s \ell_s`.

4. Long-string entropy  
   1. Model the highly excited string as a random walk on a lattice.  
   2. Entropy counts the number of elementary directional choices.  
   3. The number of steps is total length divided by step size: `L/\ell_s`.  
   4. Therefore `S_{\mathrm{str}} \sim L/\ell_s`.

5. Long-string mass  
   1. The elementary segment has length `\ell_s`.  
   2. Since mass scales as inverse length, `m_{\mathrm{seg}} \sim 1/\ell_s`.  
   3. The number of segments is `L/\ell_s`.  
   4. Multiply: `M \sim (L/\ell_s)(1/\ell_s)=L/\ell_s^2`.  
   5. Rearranging gives `L \sim M\ell_s^2`.  
   6. Substitute into entropy: `S_{\mathrm{str}} \sim M\ell_s`.

6. Black-hole entropy scaling  
   1. Start from `S_{\mathrm{BH}}=A/(4G_N)`.  
   2. At scaling level, `A \sim R_s^2`.  
   3. Use `R_s \sim M G_N`.  
   4. Then `A \sim M^2 G_N^2`.  
   5. Divide by `G_N` to get `S_{\mathrm{BH}} \sim M^2 G_N \sim M^2 \ell_p^2`.

7. Constant-entropy curve under adiabatic variation  
   1. Vary the coupling slowly so entropy is unchanged.  
   2. Black-hole entropy can depend only on the dimensionless combination `M\ell_p`.  
   3. Substitute `\ell_p \sim g_s\ell_s`.  
   4. Hold `\ell_s` fixed.  
   5. Therefore constant entropy means `M g_s = \text{const}`.  
   6. For the target object, `M g_s = M_0 g_{s,0}`.

8. String-black-hole transition curve  
   1. The crossover is taken to occur when `R_s \sim \ell_s`.  
   2. Use `R_s \sim M G_N`.  
   3. Then `M G_N \sim \ell_s`.  
   4. Substitute `G_N \sim g_s^2 \ell_s^2`.  
   5. Obtain `M g_s^2 \sim 1/\ell_s`.

9. Crossover relation used to recover black-hole entropy  
   1. Intersect the adiabat `M g_s = M_0 g_{s,0}` with the transition curve `M g_s^2 \sim 1/\ell_s`.  
   2. Eliminate `g_s`.  
   3. Get `M_\ast \ell_s \sim M_0^2 g_{s,0}^2 \ell_s^2`.  
   4. Replace `g_{s,0}^2 \ell_s^2` by `G_{N,0}`.  
   5. Therefore `M_\ast \ell_s \sim M_0^2 G_{N,0}`.  
   6. Since `S_{\mathrm{str},\ast} \sim M_\ast \ell_s` and entropy is unchanged, this reproduces the black-hole scaling.

10. Ordinary maximum-entropy counting  
   1. Divide a region into `N` binary cells.  
   2. Count configurations: `\Omega=2^N`.  
   3. Take entropy as the logarithm of the number of states.  
   4. With `N\sim V/V_{\mathrm{cell}}`, get `S_{\max}\sim (V/V_{\mathrm{cell}})\log 2`.  
   5. This is the volume-scaling expectation that holography will overturn.

11. Holographic bound from shell collapse  
   1. Consider a region containing entropy `S_{\mathrm{initial}}` and mass below the black-hole threshold for that size.  
   2. Add a shell with just enough mass to make the final system collapse into a black hole filling the region.  
   3. The final entropy is `S_{\mathrm{final}}=A/(4G_N)`.  
   4. Use the second law: `S_{\mathrm{initial}} \le S_{\mathrm{final}}`.  
   5. Conclude `S_{\max}=A/(4G_N)` for the region.

12. Hubble law from the metric  
   1. Start with `ds^2=-dt^2+a(t)^2 dx_i dx_i`.  
   2. For fixed coordinate separation `\Delta x`, proper distance is `d(t)=a(t)\Delta x`.  
   3. Differentiate with respect to time: `v=\dot d=\Delta x \dot a`.  
   4. Replace `\Delta x` by `d/a`.  
   5. Get `v=(\dot a/a)d`.  
   6. Define `H=\dot a/a`, yielding `v=Hd`.

13. Constant `H` implies exponential expansion  
   1. Assume `H` is constant in time.  
   2. Then `\dot a = Ha`.  
   3. Solve to obtain `a(t)=a_0 e^{Ht}`.  
   4. Therefore distances grow exponentially.  
   5. The characteristic horizon scale is `d_H \sim 1/H`.

## Notation Choices
- Use `G_N` for Newton’s constant throughout the final chapter.  
  Board/transcript bare `G` may be mentioned only when describing what Susskind wrote or said.
- Use `g_s` for the string coupling.  
  This resolves the lecture’s frequent spoken blur between little `g` and big `G`.
- Use `\ell_s` and `\ell_p` for string and Planck lengths.  
  Prefer `\ell`, not `l`, in the final typeset notes.
- Use `S_{\mathrm{str}}`, `S_{\mathrm{BH}}`, and `S_{\max}` rather than bare `S` once multiple entropies coexist.  
  Bare `S` is acceptable only when following a local derivation that has not yet introduced a second entropy.
- Use `R_s` for Schwarzschild radius.  
  Keep `R_s \sim M G_N` at scaling level rather than inserting exact `2G_N M` unless later context demands it.
- Use `m_{\mathrm{seg}}` for the elementary string-segment mass.  
  Do not reuse Susskind’s ambiguous spoken “`M_string`” for both the segment and the total string.
- Use `M` for total mass, with subscripts or stars for role:
  `M_0` target black hole, `M_\ast` crossover value.
- Use `H=\dot a/a` and say explicitly that dot means derivative with respect to cosmological time `t`.
- Use `\log` for entropy counting and state once that it is the natural logarithm, matching the lecture’s convention.
- Use `\sim` for scaling statements where Susskind suppresses factors of `2`, `4`, and other order-one constants.  
  Reserve `=` for definitions and for formulas the lecture treats as exact, such as `S_{\mathrm{BH}}=A/(4G_N)`.

## Uncertain Mathematics
- `lecture_07_figure_02.png` only shows the setup `c=\hbar=1` and a standalone `E`; the explicit `E \sim \hbar c/\lambda` and `m=E/c^2` are transcript-based reconstructions.
- The spoken line that `G` is “the Planck area squared” should not be preserved literally; the consistent cleaned statement is `G_N=\ell_p^2`.
- `\ell_p \sim g_s \ell_s` is a scaling relation here, not a precision identity with tracked numerical coefficients.
- The random-walk model supplies entropy scaling, not exact combinatorial coefficients; do not overstate it as a rigorous lattice derivation.
- `M=L/\ell_s^2` and `S=M\ell_s` are reliable lecture formulas, but the lower board line in `lecture_07_figure_04.png` is partly occluded, so the board evidence for that line is incomplete.
- The transition criterion `R_s \sim \ell_s` is heuristic and marks a crossover, not a sharply derived phase boundary.
- The algebra at the graph-intersection stage is verbally messy in the transcript; the final notes should present only the cleaned scaling result, not the spoken false starts.
- The holographic argument is a physically motivated bound, not a full theorem proved from first principles inside the lecture.
- The cosmology section is intentionally limited to flat expanding space and constant-`H` exponential growth; the lecture does not derive the Einstein equations or the full Friedmann system here.