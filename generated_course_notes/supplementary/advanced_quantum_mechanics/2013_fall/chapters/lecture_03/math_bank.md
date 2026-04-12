# Math Bank

## Core Equations
- \([\hat L_x,\hat L_y]=i\hbar \hat L_z\), with cyclic permutations \((x\to y\to z)\). [transcript-backed]
- \([\hat L_y,\hat L_z]=i\hbar \hat L_x,\quad [\hat L_z,\hat L_x]=i\hbar \hat L_y\). [transcript-backed]
- \(\hat L_z=-i\hbar\,\partial_\theta\), \(\hat L_z\psi=\hbar m\psi\), \(\psi=e^{im\theta}\chi(r)\), \(m\in\mathbb Z\). [transcript-backed]
- \(\psi(r,\theta,\phi)=R(r)\,\chi(\theta,\phi)\), and in standard angular basis
  \(\psi_{n\ell m}(r,\theta,\phi)=R_{n\ell}(r)Y_\ell^m(\theta,\phi)\). [transcript-backed]
- \(\hat L_\pm=\hat L_x\pm i\hat L_y\). [transcript-backed]
- \(\hat L_z|\ell,m\rangle=\hbar m|\ell,m\rangle,\ \hat L_\pm|\ell,m\rangle\propto|\ell,m\pm1\rangle\). [transcript-backed]
- Ladder termination:
  \(\hat L_+|\ell,\ell\rangle=0,\ \hat L_-|\ell,-\ell\rangle=0\). [transcript-backed]
- \(m=-\ell,-\ell+1,\dots,\ell\) and \(\text{multiplicity}=2\ell+1\). [standard reconstruction]
- \(\hat L^2=\hat L_x^2+\hat L_y^2+\hat L_z^2\). [transcript-backed]
- \(\hat L^2=\hat L_-\hat L_+ +\hat L_z^2+\hbar \hat L_z = \hat L_+\hat L_-+\hat L_z^2-\hbar\hat L_z\). [standard reconstruction]
- \(\hat L^2|\ell,m\rangle=\hbar^2\ell(\ell+1)|\ell,m\rangle\). [transcript-backed]
- \([\hat L^2,\hat L_\pm]=0,\ [\hat L^2,\hat L_z]=0\). [transcript-backed]
- \(p^2=p_r^2+p_\theta^2,\ \hat L=r\,\hat p_\theta,\ \hat p_\theta^2=\hat L^2/r^2\). [transcript-backed]
- Central-force Hamiltonian:
  \(\hat H=\frac{\hat p_r^2}{2\mu}+\frac{\hat L^2}{2\mu r^2}+V(r)\). [transcript-backed]
- In fixed-\(\ell\) sector:
  \(\hat H_{\ell,\text{rad}}=\frac{\hat p_r^2}{2\mu}+\frac{\hbar^2\ell(\ell+1)}{2\mu r^2}+V(r)\). [standard reconstruction]
- Radial eigenvalue equation (standard \(u(r)\) form):
  \[
    \left[-\frac{\hbar^2}{2\mu}\frac{d^2}{dr^2}+V(r)+\frac{\hbar^2\ell(\ell+1)}{2\mu r^2}\right]u_{n_r\ell}(r)=E_{n_r\ell}u_{n_r\ell}(r).
  \]
  [standard reconstruction]
- For fixed \(\ell\), node count ordering:
  \(n_r=0,1,2,\dots\) gives rising radial energy order. [standard reconstruction]
- HO setup:
  \(\hat H_{\text{HO}}=\frac{\hat p^2}{2m}+\frac12m\omega^2\hat x^2,\ [\hat x,\hat p]=i\hbar\). [transcript-backed]
- HO ladder:
  \(a_\pm=\frac{1}{\sqrt{2\hbar m\omega}}(\mp i\hat p+m\omega \hat x)\). [transcript-backed]
- \([a_-,a_+]=1,\quad N=a_+a_-\). [transcript-backed]
- \(\hat H_{\text{HO}}=\hbar\omega\left(N+\frac12\right)=\hbar\omega\left(a_+a_-+\frac12\right)\). [transcript-backed]
- \(N|n\rangle=n|n\rangle,\ a_+|n\rangle\propto|n+1\rangle,\ a_-|n\rangle\propto|n-1\rangle,\ a_-|0\rangle=0,\ n\in\mathbb N_0\). [transcript-backed]
- \(E_n=\hbar\omega\left(n+\frac12\right)\). [transcript-backed]

## Definitions And Objects
- \(\mathbf L\): angular momentum operator vector; components \((L_x,L_y,L_z)\).
- \(L^2\): total angular momentum squared operator, \(L^2=\mathbf L\cdot\mathbf L\).
- \(m\): magnetic quantum number (eigenvalue of \(L_z/\hbar\)); lecture sometimes writes \(M\).
- \(\ell\): orbital angular momentum quantum number (equivalent to Susskind’s fixed-multiplet “\(L\)” label in places).
- \(L_\pm\): angular momentum ladder operators.
- \(\chi(\theta,\phi)\), \(Y_\ell^m(\theta,\phi)\): angular part of fixed \((\ell,m)\) wavefunction sector.
- \(R_{n\ell}(r)\): radial wavefunction factor; \(n_r\) used for radial node index (bound-state ordering proxy).
- \(V(r)\): central potential.
- \(p_r,p_\theta\): radial and angular canonical momentum components in reduced coordinates.
- \(N\): harmonic oscillator number operator, \(N=a_+a_-\).
- \(a_\pm\): HO ladder operators.
- \(\omega\): oscillator angular frequency.
- \(p\): linear momentum operator in 1D HO analysis.
- \(\hbar\): reduced Planck constant; use explicitly in final equations.

## Derivation Steps
1. Start from 2D rotation generator:
   1) Define \(\hat L_z=-i\hbar\partial_\theta\).  
   2) Solve \(\hat L_z\psi=\hbar m\psi\).  
   3) Single-valuedness under \(\theta\to\theta+2\pi\) gives \(m\in\mathbb Z\).
2. Generalize to 3D central coordinates:
   1) State is \(\psi(r,\theta,\phi)=R(r)\chi(\theta,\phi)\).  
   2) Identify \(\chi\to Y_\ell^m\): only angular dependence classifies angular momentum states.  
3. Reintroduce SU(2)-like algebra:
   1) Use \([L_x,L_y]=i\hbar L_z\) and cyclic analogues.  
   2) Define \(L_\pm=L_x\pm iL_y\).  
   3) Show \(\hat L_\pm\) shift \(m\) by one unit.
4. Build finite multiplet:
   1) Act repeatedly with \(L_+\) (or \(L_-\)) on an eigenstate.  
   2) Require termination at boundaries: \(L_+|\ell,\ell\rangle=0\), \(L_-|\ell,-\ell\rangle=0\).  
   3) Conclude \(m=-\ell,\dots,\ell\), so there are \(2\ell+1\) states; infer \(\ell\in\frac12\mathbb Z_{\ge0}\) from integer step size and symmetry.
5. Fix \(L^2\) on multiplet:
   1) Factor \(L^2=L_-L_+ +L_z^2+\hbar L_z\) (equiv. with \(L_+L_-\)).  
   2) Apply on top state \(|\ell,\ell\rangle\): second term vanishes by \(L_+|\ell,\ell\rangle=0\).  
   3) Read off eigenvalue \(L^2=\hbar^2\ell(\ell+1)\).  
   4) Use \([L^2,L_\pm]=0\) to propagate same \(L^2\) eigenvalue to all \(m\) in multiplet.
6. Central-force reduction:
   1) Decompose \(\mathbf p\) into \((p_r,p_\theta)\), with \(\mathbf p^2=p_r^2+p_\theta^2\).  
   2) Use \(L=r p_\theta\Rightarrow p_\theta^2=L^2/r^2\).  
   3) Write \(\hat H=\frac{p_r^2}{2\mu}+\frac{L^2}{2\mu r^2}+V(r)\).  
   4) Substitute \(L^2\to \hbar^2\ell(\ell+1)\), solve 1D radial equation in each \(\ell\)-sector.
7. Qualitative spectral structure from effective radial dynamics:
   1) For fixed \(\ell\), centrifugal term shifts each radial branch upward.  
   2) At given \(\ell\), radial node count \(n_r\) gives ordering: \(n_r=0,1,2,\dots\) increasing in energy.
8. Harmonic oscillator algebraic solution:
   1) Factor HO Hamiltonian into \(H=(p^2/2m)+m\omega^2x^2/2\).  
   2) Define \(a_\pm\) and verify \([a_-,a_+]=1\).  
   3) Rewrite \(H=\hbar\omega(a_+a_++\tfrac12)\equiv \hbar\omega(N+\tfrac12)\).  
   4) From commutators, \(a_+\) raises \(N\), \(a_-\) lowers \(N\).  
   5) Positivity of \(H\) gives lowest state \(a_-|0\rangle=0\), so \(N=0,1,2,\dots\).  
   6) Hence \(E_n=\hbar\omega(n+\tfrac12)\).

## Notation Choices
- Use operator notation with hats in derivations: \(\hat L_x,\hat L_y,\hat L_z,\hat L^2,\hat H,\hat N\).
- Use \(\ell\) for orbital quantum number (angular momentum magnitude) and \(m\) for magnetic quantum number; treat \(M\) in transcript as \(m\).
- Use \(L_\pm\) for ladder operators; reserve \(\ell\) for the fixed multiplet label.
- Use \(n_r\) for radial node index; use \(n\) only for HO number levels.
- Use \(N=a_+a_-\) for HO number operator and \(|n\rangle\) for HO eigenstates.
- Explicitly state \(\hbar=1\) as a temporary lecture convention when simplifying, then restore \(\hbar\) in final formulas.
- Keep sign/order conventions for \(a_\pm\) consistent with \( [x,p]=i\hbar\) and \(a_\pm=\frac{1}{\sqrt{2\hbar m\omega}}(\mp i p + m\omega x)\).

## Uncertain Mathematics
- Exact normalization constants in HO ladder relations are only partially written in transcript; use standard \(\sqrt{n+1}\), \(\sqrt{n}\) factors where needed.
- Some HO commutator-sign algebra steps in the spoken record are verbally muddled (OCR/transcription likely); standard convention \( [a_-,a_+]=1\) is the robust endpoint.
- In the transcript, the angular Hamiltonian decomposition around the line “\(p_r^2+p_\theta^2\)” has a few verbal slips; final reduced form is clear but coefficient placement is reconstructed.
- Exact bound-state node\(\leftrightarrow\)energy theorem statements are narrative-level in the lecture; do not encode as a strict theorem formula beyond standard 1D Schrödinger ordering.
- Diagram-dependent shapes/numerics (effective-potential plots, ladder-table spacings, level charts) were partially inaccessible; keep these as sketch-level descriptions, not exact geometric claims.