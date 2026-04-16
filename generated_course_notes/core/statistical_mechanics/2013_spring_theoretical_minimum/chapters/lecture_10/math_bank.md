# Math Bank
## Core Equations
- \(E_{\text{Ising}}=-J\sum_{\langle ij\rangle}\sigma_i\sigma_j+h\sum_i \sigma_i\)  [transcript-backed]
- \(\sigma_i=\pm 1\)  [transcript-backed]
- \(\Delta E_{\text{broken bond}}=2J\)  [transcript-backed]
- \(N_{\text{links}}=d\,N_{\text{sites}}\) for an infinite hypercubic lattice in \(d\) dimensions  [transcript-backed]
- \(A_{\text{MF}}=-2dJ\,\bar{\sigma}+h\)  [visible]
- \(E_{\text{MF}}(\sigma)=A_{\text{MF}}\sigma=(-2dJ\,\bar{\sigma}+h)\sigma\)  [transcript-backed]
- \(\langle \sigma\rangle=\dfrac{\sum_{\sigma=\pm1}\sigma\,e^{-\beta A_{\text{MF}}\sigma}}{\sum_{\sigma=\pm1}e^{-\beta A_{\text{MF}}\sigma}}=-\tanh(\beta A_{\text{MF}})\)  [standard reconstruction]
- \(\bar{\sigma}=\tanh\!\big[\beta(2dJ\,\bar{\sigma}-h)\big]\)  [standard reconstruction]
- \(y=2dJ\,\beta\,\bar{\sigma}\)  [transcript-backed]
- \(\dfrac{yT}{2dJ}=\tanh(y-\beta h)\)  [visible]
- \(\dfrac{yT}{2dJ}=\tanh y\qquad(h=0)\)  [transcript-backed]
- \(T_c=2dJ\)  [transcript-backed]
- \(Z=\sum_{N}\sum_{\text{conf}_N} e^{-\beta E+\beta\mu N}\)  [transcript-backed]
- \(\sigma_i=-1 \iff n_i=0\)  [visible]
- \(\sigma_i=+1 \iff n_i=1\)  [standard reconstruction]
- \(n_i=\dfrac{1+\sigma_i}{2}\)  [transcript-backed]
- \(\rho=\langle n_i\rangle=\dfrac{1+\bar{\sigma}}{2}=\dfrac12+\dfrac{\bar{\sigma}}{2}\)  [transcript-backed]
- \(E_{1\text{ particle}}=8J\) in \(d=2\)  [visible]
- \(E_{2\text{ particles, far}}=16J\) in \(d=2\)  [transcript-backed]
- \(E_{2\text{ particles, nn}}=12J\) in \(d=2\)  [visible]
- \(\Delta E_{\text{nn attraction}}=12J-16J=-4J\) in \(d=2\)  [transcript-backed]
- \(\Delta E_h=2h\) per occupied site when \(\sigma\) flips from \(-1\) to \(+1\)  [transcript-backed]
- \(E_{1\text{ particle}}=8J+2h\) in the \(d=2\) lattice-gas counting convention  [standard reconstruction]

## Definitions And Objects
- \(\sigma_i\): Ising spin at lattice site \(i\), taking values \(\pm1\).
- \(\langle ij\rangle\): nearest-neighbor link; the interaction sum is over links, not sites.
- \(J\): ferromagnetic coupling; controls how costly it is to break a bond.
- Broken bond: neighboring spins anti-parallel.
- Unbroken bond: neighboring spins parallel.
- \(h\): external field parameter in the lecture’s final notation; positive \(h\) favors \(\sigma=-1\) in the energy convention used.
- \(\beta=1/T\): inverse temperature, with \(k_B=1\) implicit.
- \(d\): lattice dimension; coordination number is \(2d\).
- \(\bar{\sigma}\): average spin / average magnetization per site; use this for the final notes rather than the temporary “double-bar” notation.
- \(A_{\text{MF}}\): one-spin mean-field coefficient multiplying \(\sigma\).
- \(y\): reduced mean-field variable used to rewrite the self-consistency equation for graphing.
- \(\mu\): chemical potential; one-body energy contribution associated with having a particle in the box.
- \(n_i\): lattice-gas occupancy variable, \(0\) or \(1\).
- \(\rho\): average particle density per lattice site.
- \(T_c\): critical temperature; “Curie temperature” only in the magnetic language.

## Derivation Steps
**Broken-bond energy cost**
1. Start from one link contribution \(-J\sigma_i\sigma_j\).
2. For parallel neighbors, \(\sigma_i\sigma_j=+1\), so the link energy is \(-J\).
3. For anti-parallel neighbors, \(\sigma_i\sigma_j=-1\), so the link energy is \(+J\).
4. The change from unbroken to broken is \(+J-(-J)=2J\).

**Mean-field one-spin problem**
1. Choose one spin \(\sigma\) and replace each of its \(2d\) neighbors by the average value \(\bar{\sigma}\).
2. Its interaction energy becomes \(-J(2d)\bar{\sigma}\,\sigma\).
3. Add the field term \(h\sigma\).
4. Write the one-spin energy as \(E_{\text{MF}}(\sigma)=(-2dJ\bar{\sigma}+h)\sigma\).
5. Compute the thermal average of this one-spin problem.
6. Impose self-consistency by setting that average equal to \(\bar{\sigma}\).

**Reduced equation**
1. Start from \(\bar{\sigma}=\tanh[\beta(2dJ\bar{\sigma}-h)]\).
2. Define \(y=2dJ\beta\bar{\sigma}\).
3. Replace \(\bar{\sigma}\) on the left by \(yT/(2dJ)\).
4. Obtain \(\dfrac{yT}{2dJ}=\tanh(y-\beta h)\).

**Critical-temperature condition**
1. Set \(h=0\) to get \(\dfrac{yT}{2dJ}=\tanh y\).
2. Interpret the left-hand side as a straight line through the origin with slope \(T/(2dJ)\).
3. Use \(\left.\dfrac{d}{dy}\tanh y\right|_{y=0}=1\).
4. The transition occurs when the line is tangent to \(\tanh y\) at the origin.
5. Set \(T/(2dJ)=1\).
6. Conclude \(T_c=2dJ\).

**Two-dimensional lattice-gas counting**
1. Declare the all-down state to be the empty lattice and subtract its constant ground-state energy.
2. Flip one spin up to represent one particle.
3. In \(d=2\), that breaks four bonds.
4. Each broken bond costs \(2J\), so one particle costs \(4\times 2J=8J\).
5. Two far-separated particles break eight bonds total, so the cost is \(16J\).
6. Two nearest-neighbor particles leave their mutual bond unbroken and break only six bonds total.
7. The nearest-neighbor pair therefore costs \(6\times 2J=12J\).
8. Compare \(12J\) with \(16J\) to read off an attractive energy \(-4J\) at one-bond separation.

**Field term as chemical-potential control**
1. In the lattice-gas interpretation, adding a particle flips \(\sigma\) from \(-1\) to \(+1\).
2. The field term \(h\sum_i \sigma_i\) therefore changes by \(+2h\) for each added particle.
3. This acts as a tunable one-body energy.
4. The field thus shifts the effective chemical potential while \(J\) keeps the interaction strength fixed.

**Density from magnetization**
1. Occupancy is \(n_i=0\) when \(\sigma_i=-1\) and \(n_i=1\) when \(\sigma_i=+1\).
2. The linear formula matching both cases is \(n_i=(1+\sigma_i)/2\).
3. Average over sites or ensembles.
4. Obtain \(\rho=(1+\bar{\sigma})/2\).

## Notation Choices
- Use \(h\) in the chapter, not \(B\) and not capital \(H\), even though the spoken lecture drifts among them.
- Keep the lecture’s energy convention \(E_{\text{field}}=h\sum_i \sigma_i\), so positive \(h\) lowers the energy of \(\sigma=-1\).
- Use \(\bar{\sigma}\) for the mean magnetization throughout; do not keep the transient “\(\sigma\) double bar” notation.
- Use \(\langle ij\rangle\) for nearest-neighbor links and say explicitly that the interaction sum is over links.
- Use \(T\) and \(\beta=1/T\) with \(k_B=1\).
- Use \(y=2dJ\beta\bar{\sigma}\) so that the frame-visible reduced equation stays exactly \(\dfrac{yT}{2dJ}=\tanh(y-\beta h)\).
- In the lattice-gas language, use \(n_i\in\{0,1\}\) and reserve \(\rho\) for the average density.
- Keep the \(8J,16J,12J\) counting explicitly labeled as the two-dimensional case.
- If the one-spin mean-field energy is written as \(A_{\text{MF}}\sigma\), keep the separate identity \(\langle\sigma\rangle=-\tanh(\beta A_{\text{MF}})\) visible somewhere in the drafting notes to avoid sign mistakes.
- Use \(T_c\) as the generic symbol; mention “Curie temperature” only as the magnetic special case.

## Uncertain Mathematics
- The raw uncancelled self-consistency equation on the board is cropped in `lecture_10_figure_02.png`; the clean chapter should derive it from the one-spin average and anchor the final sign choice to the visible reduced equation in `lecture_10_figure_03.png`.
- The transcript around the introduction of \(y\) contains live sign corrections and OCR noise. The safest stable pair is
  \[
  y=2dJ\beta\bar{\sigma},\qquad \frac{yT}{2dJ}=\tanh(y-\beta h).
  \]
- The lecture verbally fumbles the sign in the \(\tanh\) argument and the definition of \(y\); the final notes should not reproduce those false starts except perhaps in a brief explanatory comment.
- The relation between field and chemical potential is only clean up to an additive offset. In \(d=2\), the natural one-body cost is \(8J+2h\), but the lecture also treats constant energy shifts as irrelevant, so any final chemical-potential formula should be stated with that caveat.
- The OCR transcript reads the offset near `01:06:39-01:06:43` as “AJ”; this is almost certainly an offset tied to the isolated-particle energy, but it should not be quoted verbatim in the chapter.
- The grand-canonical partition function is only sketched. No measure factors, indistinguishability factors, or pressure formula are worked out in the lecture.
- The potential-versus-separation picture for the lattice gas is described verbally; no usable plotted formula is given on the board.
- The critical-exponent discussion is qualitative only. The lecture does not derive exponent values or scaling laws in usable detail.
- From `01:24:13` onward the recording is no longer part of the statistical-mechanics chapter; none of that later material belongs in the mathematical core of these notes.