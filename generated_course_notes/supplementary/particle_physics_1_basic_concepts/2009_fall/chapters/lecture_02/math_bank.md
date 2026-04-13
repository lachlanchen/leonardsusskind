# Math Bank
## Core Equations
- \(\dfrac{d}{dx} e^{\alpha x} = \alpha e^{\alpha x}\) [transcript-backed]
- \(\dfrac{d}{dx}\sin(kx)=k\cos(kx)\) [transcript-backed]
- \(\dfrac{d}{dx}\cos(kx)=-k\sin(kx)\) [transcript-backed]
- \(e^{ikx}=\cos(kx)+i\sin(kx)\) [transcript-backed]
- \(\omega=2\pi f\) [visible]
- \(\lambda=\text{wavelength}\) [standard reconstruction]
- \(\lambda f=c\) [visible]
- \(\dfrac{f}{c}=\dfrac{1}{\lambda}\) [visible]
- \(\hbar=\dfrac{h}{2\pi}\) [visible]
- \(E=\hbar\omega=hf\) [transcript-backed]
- \(\vec p=m\vec v\) [visible]
- \(|p|=\dfrac{E}{c}\) [visible]
- \(p_{\text{photon}}=\dfrac{hf}{c}=\dfrac{h}{\lambda}\) [visible]
- \(p=\dfrac{h}{\lambda}\) [transcript-backed]
- \(E=\dfrac{1}{2}mv^2=\dfrac{p^2}{2m}\) [visible]
- \(hf=\dfrac{1}{2m}\left(\dfrac{h}{\lambda}\right)^2\) [transcript-backed]
- \(f=\dfrac{h}{2m\lambda^2}\) [visible]
- \(A^2\propto E_{\text{wave}}\) [transcript-backed]
- \(E_{\text{wave}}=n\hbar\omega\) for \(n\) photons of one frequency [transcript-backed]
- \(A^2\propto n\hbar\omega\) [transcript-backed]
- \(A\propto \sqrt{n}\) [transcript-backed]
- \(v_{\phi}=f\lambda\) for a monochromatic component [transcript-backed]
- \(\lambda_N=\dfrac{L}{N}\) [transcript-backed]
- \(p_N=\dfrac{Nh}{L}\) [transcript-backed]
- \(p_n=\dfrac{nh}{2\pi r}\) for a genuine circle of radius \(r\) [transcript-backed]
- \(J=rp_n=n\hbar\) [standard reconstruction]
- \([A,B]=AB-BA\) [transcript-backed]
- \([B,A]=-\,[A,B]\) [transcript-backed]
- \([x,p_x]=i\hbar\), \([y,p_y]=i\hbar\), \([z,p_z]=i\hbar\) [standard reconstruction]
- \([x_i,x_j]=0\) and \([p_i,p_j]=0\) [standard reconstruction]
- \([x_i,p_j]=0\) for \(i\neq j\) [standard reconstruction]
- \(E_n=n\hbar\omega\) with the ground state shifted to zero [transcript-backed]
- \(a_+|n\rangle=\sqrt{n+1}\,|n+1\rangle\) [transcript-backed]
- \(a_-|n\rangle=\sqrt{n}\,|n-1\rangle\) [transcript-backed]
- \(a_-|0\rangle=0\) [transcript-backed]
- \(a_+a_-|n\rangle=n|n\rangle\) [transcript-backed]
- \(a_-a_+|n\rangle=(n+1)|n\rangle\) [transcript-backed]
- \([a_-,a_+]=1\) [standard reconstruction]
- \(H=\hbar\omega\,a_+a_-\) in the shifted convention [transcript-backed]
- \(|n_1,n_2,n_3,\dots\rangle\) for a many-mode state [standard reconstruction]

## Definitions And Objects
- Field: something that varies throughout space.
- Wave: a field configuration oscillating in space and/or time.
- \(f\): ordinary frequency, measured in cycles per second.
- \(\omega\): angular frequency, measured in radians per second.
- \(\lambda\): wavelength.
- \(A\): wave amplitude.
- Photon: one quantum of an electromagnetic wave.
- \(\psi\): matter-wave notation for an electron or other particle wave.
- Wave packet: a localized superposition of nearly monochromatic waves with an envelope.
- Phase velocity: velocity of crests and troughs of a component wave.
- Group velocity: velocity of the packet envelope; identified with particle motion in the nonrelativistic discussion.
- Periodic space: one-dimensional space with identified endpoints; total length \(L\).
- \(N\): integer mode label counting how many wavelengths fit around the periodic space.
- \(n\): integer occupation number / oscillator level for one fixed mode.
- \(|n\rangle\): ket labeling the \(n\)-th energy state of one harmonic oscillator.
- \(a_+\), \(a_-\): raising/lowering operators; in field language, creation/annihilation operators for a fixed mode.
- Commutator \([A,B]\): operator measure of noncommutativity; used in the lecture as the test for simultaneous measurability.

## Derivation Steps
1. Euler/exponential relation: start from \(\dfrac{d}{dx}\sin(kx)=k\cos(kx)\) and \(\dfrac{d}{dx}\cos(kx)=-k\sin(kx)\); differentiate \(\cos(kx)+i\sin(kx)\); factor the result as \(ik(\cos(kx)+i\sin(kx))\); identify it with \(e^{ikx}\).
2. Photon momentum: use \(E=hf\); use \(|p|=E/c\); substitute to get \(p=hf/c\); use \(\dfrac{f}{c}=\dfrac{1}{\lambda}\); conclude \(p=\dfrac{h}{\lambda}\).
3. Amplitude versus photon number: use the classical statement \(E_{\text{wave}}\propto A^2\); use the quantum statement \(E_{\text{wave}}=n\hbar\omega\) for many photons at one frequency; combine them to get \(A^2\propto n\hbar\omega\); for fixed frequency this gives \(A\propto \sqrt{n}\).
4. Slow matter-wave frequency: start with \(E=\dfrac{p^2}{2m}\); use \(E=hf\) for one particle and \(p=\dfrac{h}{\lambda}\); substitute \(p\) into the kinetic-energy formula; obtain \(hf=\dfrac{1}{2m}\left(\dfrac{h}{\lambda}\right)^2\); divide by \(h\); conclude \(f=\dfrac{h}{2m\lambda^2}\).
5. Phase/group-velocity contrast: use the component-wave relation \(v_{\phi}=f\lambda\); substitute the nonrelativistic \(f=\dfrac{h}{2m\lambda^2}\); obtain \(v_{\phi}=\dfrac{h}{2m\lambda}\); note that different \(\lambda\) give different component velocities; conclude that packet motion and crest motion separate, so group and phase velocities differ.
6. Schrödinger-equation connection: take the matter-wave relation between temporal frequency and spatial wavelength; interpret frequency as time dependence and wavelength as space dependence; identify the resulting relation as the free nonrelativistic Schrödinger equation in condensed form.
7. Momentum quantization on periodic space: impose periodicity on a line of total length \(L\); require an integer number of wavelengths to fit; write \(\lambda_N=\dfrac{L}{N}\); use \(p=\dfrac{h}{\lambda}\); conclude \(p_N=\dfrac{Nh}{L}\).
8. Angular momentum on a real circle: for circumference \(L=2\pi r\), rewrite the periodic momentum as \(p_n=\dfrac{nh}{2\pi r}\); multiply by \(r\); conclude \(J=rp_n=n\hbar\).
9. Oscillator ladder algebra: define \(a_+|n\rangle=\sqrt{n+1}|n+1\rangle\) and \(a_-|n\rangle=\sqrt{n}|n-1\rangle\); act with \(a_+a_-\) on \(|n\rangle\); get \(n|n\rangle\); act with \(a_-a_+\) on \(|n\rangle\); get \((n+1)|n\rangle\); read off the noncommutativity and the number-operator action.
10. Field as many oscillators: periodic space gives discrete mode labels \(N\); each allowed mode is one harmonic oscillator with frequency \(\omega_N\); each oscillator carries an occupation number \(n_N\); a field state is specified by the list \(|n_1,n_2,n_3,\dots\rangle\).

## Notation Choices
- Use \(f\) for ordinary frequency and \(\omega\) for angular frequency, with \(\omega=2\pi f\).
- Use \(\lambda\) for wavelength throughout.
- Use \(h\) and \(\hbar\) together, with \(\hbar=\dfrac{h}{2\pi}\); use whichever keeps the displayed equation closest to the lecture.
- Use \(p\) for one-dimensional momentum or momentum magnitude; use \(\vec p\) only when direction is explicitly discussed.
- Keep \(p=\dfrac{h}{\lambda}\) as the general de Broglie relation.
- Use \(\psi\) for the matter wave of an electron or other slow particle.
- Reserve capital \(N\) for the spatial mode index in periodic space.
- Reserve lowercase \(n\) for oscillator level / occupation number of a fixed mode.
- Use \(L\) only for the total length of the periodic spatial direction.
- Do not use \(L\) for angular momentum in the final notes; use \(J\) for the scalar angular momentum in the circular-wire aside to avoid the transcript’s collision.
- Use \(a_+\) and \(a_-\) in the main text to stay close to the lecture; note once that these are the raising/lowering or creation/annihilation operators.
- Use the shifted oscillator convention \(E_n=n\hbar\omega\); do not silently restore the \(\frac12\hbar\omega\) term.
- Use \(|n\rangle\) for one oscillator and \(|n_1,n_2,n_3,\dots\rangle\) for the many-mode field state.

## Uncertain Mathematics
- The board only partially shows \(\lambda=\text{wavelength}\); the clean wording is safe, but it is a completion rather than a fully visible transcription.
- The board crop of the energy line is incomplete; \(E=\hbar\omega=hf\) is secure from the transcript, not from a single frame alone.
- The amplitude discussion is only order-of-magnitude. Keep proportionalities, not exact normalization constants.
- The relation \(A^2\propto n\hbar\omega\) is lecture-faithful only for a fixed frequency and an implicitly fixed region such as one wavelength or one mode volume; do not present it as a universal exact equality.
- The phase/group-velocity passage is transcript-noisy. Keep only the stable mathematical content: \(v_{\phi}=f\lambda\), dispersion for the nonrelativistic matter-wave relation, and identification of group velocity with particle motion.
- The commutator formulas for positions and momenta beyond the explicitly discussed same-component cases are standard compact reconstructions.
- The photon-position subtlety is raised but not developed; do not overformalize it.
- The number-operator commutator \([a_-,a_+]=1\) is a clean reconstruction from the ladder-action rules, not something written explicitly on the board.
- In the periodic-space discussion, the sign of momentum is conceptually tied to direction of propagation, but the lecture mostly presents magnitudes and positive integers when discussing allowable wavelengths; handle the \(\pm p_N\) extension carefully if introduced.
- In the circle example, \(J=rp=n\hbar\) is mathematically standard and consistent with the lecture, but the transcript itself stumbles over symbol names.