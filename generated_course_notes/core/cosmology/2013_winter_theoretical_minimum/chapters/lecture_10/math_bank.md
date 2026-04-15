# Math Bank
## Core Equations
- [transcript-backed] \(\Delta x\,\Delta p \gtrsim \hbar\)
- [transcript-backed] \([c]=L/T,\quad [\hbar]=ML^2/T,\quad [G]=L^3/(MT^2)\)
- [transcript-backed] \(F=ma,\quad F=\dfrac{Gm_1m_2}{r^2}\)
- [transcript-backed] \(\ell=c^a\hbar^bG^c,\quad b=c,\quad a+3b=0,\quad a+5b=1\)
- [transcript-backed] \(\ell_P=\sqrt{\dfrac{\hbar G}{c^3}}\sim10^{-35}\,\mathrm{m},\quad t_P\sim \ell_P/c\sim10^{-43}\,\mathrm{s}\)
- [transcript-backed] \(mc^2\,t\sim\hbar,\quad m_P\sim \dfrac{\hbar}{c^2 t_P}\sim10^{-8}\,\mathrm{kg}\)
- [standard reconstruction] \(t_P=\sqrt{\dfrac{\hbar G}{c^5}},\quad m_P=\sqrt{\dfrac{\hbar c}{G}}\)
- [transcript-backed] \(c=\hbar=G=1\) in Planck units
- [transcript-backed] \(\dfrac{\delta T}{T}\sim10^{-5},\quad \dfrac{\delta\rho}{\rho}\sim10^{-5}\)
- [transcript-backed] \(\mathcal{H}_{\rm osc}=\dfrac{\dot x^{\,2}}{2}+\dfrac{\omega^2x^2}{2},\quad E_n=\left(n+\tfrac12\right)\hbar\omega\)
- [transcript-backed] \(x^2\sim \dfrac{\hbar}{\omega},\quad \dot x^{\,2}\sim \hbar\omega,\quad x(t)\sim \sqrt{\dfrac{\hbar}{\omega}}\,e^{i\omega t}\)
- [transcript-backed] \(\ddot x+\omega^2x=0,\quad \ddot x+\gamma\dot x+\omega^2x=0\)
- [transcript-backed] \(x\propto e^{\alpha t},\quad \alpha^2+\gamma\alpha+\omega^2=0,\quad \alpha=\dfrac{-\gamma\pm\sqrt{\gamma^2-4\omega^2}}{2}\)
- [transcript-backed] \(\gamma^2<4\omega^2\) underdamped,\quad \(\gamma^2>4\omega^2\) overdamped,\quad \(\gamma=2\omega\) critical
- [transcript-backed] \(\omega=0\Rightarrow x(t)=c_0+c_1e^{-\gamma t}\)
- [standard reconstruction] \(V'(\phi)\approx0\) on the inflationary plateau
- [visible] \(\dfrac{\partial^2\phi}{\partial t^2}-\dfrac{\partial^2\phi}{\partial x^2}=\cdots,\quad \dfrac{\partial^2\phi}{\partial t^2}+3H\cdots\)
- [transcript-backed] \(\dfrac{\partial^2\phi}{\partial t^2}-\nabla^2\phi=0,\quad \dfrac{\partial^2\phi}{\partial t^2}-\nabla^2\phi=-\dfrac{dV}{d\phi}\)
- [transcript-backed] \(\ddot\phi+3H\dot\phi=0,\quad \ddot\phi+3H\dot\phi-\dfrac{1}{a(t)^2}\nabla^2\phi=0\)
- [transcript-backed] \(d_{\rm prop}=a(t)\,\Delta x\)
- [transcript-backed] \(\phi(\mathbf{x},t)=e^{i\mathbf{k}\cdot\mathbf{x}}\phi_k(t),\quad \nabla^2 e^{i\mathbf{k}\cdot\mathbf{x}}=-k^2 e^{i\mathbf{k}\cdot\mathbf{x}}\)
- [transcript-backed] \(\ddot\phi_k+3H\dot\phi_k+\dfrac{k^2}{a(t)^2}\phi_k=0,\quad \gamma=3H,\quad \omega(t)=k/a(t)\)
- [transcript-backed] \(3H=2k/a,\quad a_{\rm cross}=2k/(3H)\)
- [transcript-backed] \(\lambda_{\rm com}=2\pi/k,\quad \lambda_{\rm phys}=a\,\lambda_{\rm com},\quad k=\dfrac{2\pi a}{\lambda_{\rm phys}}\)
- [transcript-backed] \(\lambda_{\rm phys}H\sim1,\quad \lambda_{\rm phys}\sim H^{-1},\quad v=Hd\)
- [transcript-backed] \(H\sim\sqrt{V}\) on the flat plateau, in Planck units / up to omitted normalization

## Definitions And Objects
- \(c,\hbar,G\): the three universal constants singled out in the opening scale-setting prelude.
- \(\ell_P,t_P,m_P\): Planck length, time, and mass; the lecture’s natural units of length, time, and mass.
- WMAP map: temperature map of the microwave background on the last-scattering shell.
- \(\delta T/T\): fractional temperature anisotropy on the sky.
- \(\delta\rho/\rho\): fractional energy-density perturbation, inferred from the temperature map and later used as the seed of structure.
- \(x\): comoving spatial coordinate in the inflation discussion; by Susskind’s convention here it is not a physical length and is effectively dimensionless.
- \(a(t)\): scale factor; converts comoving separations into physical ones via \(a(t)\Delta x\).
- \(H\): Hubble expansion rate during the inflationary plateau; treated as approximately constant while the field is high on the flat potential.
- \(\phi(\mathbf{x},t)\): inflaton scalar field.
- \(V(\phi)\): inflaton potential, sketched as a long flat plateau ending in a sharp cliff.
- \(V'(\phi)\): derivative of the potential; small on the plateau.
- \(\mathbf{k}\), \(k\): wavevector and wave number of a Fourier mode of the inflaton field.
- \(\phi_k(t)\): time-dependent amplitude of a single Fourier mode.
- \(\lambda_{\rm com}\): wavelength in comoving \(x\)-units.
- \(\lambda_{\rm phys}\): physical wavelength measured in actual length units.
- \(\gamma\): damping coefficient in the mechanical analog; later identified with \(3H\).
- \(\omega\): oscillator frequency / restoring-force scale in the analog; later identified with \(k/a\).
- \(H^{-1}\): Hubble distance or Hubble horizon in units with \(c=1\).

## Derivation Steps
Planck length from dimensional analysis

1. Start from \([c]=L/T\), \([\hbar]=ML^2/T\), \([G]=L^3/(MT^2)\).
2. Assume a fundamental length \(\ell=c^a\hbar^bG^c\).
3. Cancel mass dimensions: \(b=c\).
4. Cancel time dimensions: \(-a-b-2c=0\Rightarrow a+3b=0\).
5. Require one power of length: \(a+2b+3c=1\Rightarrow a+5b=1\).
6. Solve \(b=c=\tfrac12\), \(a=-\tfrac32\).
7. Conclude \(\ell_P=\sqrt{\hbar G/c^3}\).

Planck time and Planck mass

1. Use \(t_P=\ell_P/c\) as the light-travel time across a Planck length.
2. Use \(E=mc^2\) and the dimensional statement \(Et\sim\hbar\).
3. Set \(t=t_P\) to estimate \(m_P\sim \hbar/(c^2 t_P)\).
4. Substitute \(t_P\) to recover the standard closed form \(m_P=\sqrt{\hbar c/G}\).

Zero-point size of the oscillator

1. Start from the ground-state energy \(E_0=\tfrac12\hbar\omega\).
2. Use the time-averaged equality of kinetic and potential energy.
3. Set \(\tfrac12\omega^2x^2\sim \tfrac14\hbar\omega\), ignoring order-one factors as he does.
4. Read off \(x^2\sim \hbar/\omega\).
5. Differentiate \(x\sim \sqrt{\hbar/\omega}\,e^{i\omega t}\) to get \(\dot x^2\sim \hbar\omega\).

Damped oscillator and its regimes

1. Insert \(x\propto e^{\alpha t}\) into \(\ddot x+\gamma\dot x+\omega^2x=0\).
2. Obtain \(\alpha^2+\gamma\alpha+\omega^2=0\).
3. Solve \(\alpha=\dfrac{-\gamma\pm\sqrt{\gamma^2-4\omega^2}}{2}\).
4. If \(\gamma^2<4\omega^2\), the roots are complex and the motion oscillates with a decaying envelope.
5. If \(\gamma^2>4\omega^2\), both roots are real and negative and the motion decays without oscillating.
6. If \(\gamma=2\omega\), the system is critically damped.
7. If \(\omega=0\), then \(\alpha=0,-\gamma\) and \(x(t)=c_0+c_1e^{-\gamma t}\): the oscillator comes to rest at an arbitrary constant position.

Expanding-universe scalar-field equation

1. Start from the flat-space scalar wave equation \(\partial_t^2\phi-\nabla^2\phi=0\) when the potential is taken to be flat.
2. Recall the homogeneous expanding-universe equation \(\ddot\phi+3H\dot\phi=0\).
3. Reintroduce spatial variation of \(\phi\).
4. Note that the spatial derivative must be taken with respect to proper distance, not comoving \(x\).
5. Use \(d_{\rm prop}=a(t)\Delta x\).
6. Therefore \(\partial^2/\partial d_{\rm prop}^2=a^{-2}\partial^2/\partial x^2\).
7. Replace the gradient term accordingly to get \(\ddot\phi+3H\dot\phi-a^{-2}\nabla^2\phi=0\).

Mode decomposition and oscillator map

1. Take a single Fourier mode \(\phi(\mathbf{x},t)=e^{i\mathbf{k}\cdot\mathbf{x}}\phi_k(t)\).
2. Time derivatives act only on \(\phi_k(t)\).
3. Spatial derivatives give \(\nabla^2 e^{i\mathbf{k}\cdot\mathbf{x}}=-k^2 e^{i\mathbf{k}\cdot\mathbf{x}}\).
4. The minus sign in the wave equation turns this into \(+(k^2/a^2)\phi_k\).
5. Obtain \(\ddot\phi_k+3H\dot\phi_k+\dfrac{k^2}{a^2}\phi_k=0\).
6. Identify \(\gamma=3H\) and \(\omega=k/a\).
7. Since \(a(t)\) grows, the restoring force weakens with time.

Freeze-out / horizon exit

1. Use the critical-damping condition \(\gamma=2\omega\).
2. Substitute \(\gamma=3H\) and \(\omega=k/a\).
3. Get \(3H=2k/a\), or \(a_{\rm cross}=2k/(3H)\).
4. Write the comoving wavelength as \(\lambda_{\rm com}=2\pi/k\).
5. Convert to physical wavelength \(\lambda_{\rm phys}=a\lambda_{\rm com}\), equivalently \(k=2\pi a/\lambda_{\rm phys}\).
6. Substitute into the crossover condition and drop order-one factors.
7. Conclude \(\lambda_{\rm phys}H\sim1\), i.e. the mode freezes when its physical wavelength reaches the Hubble scale.

Reheating to density contrast

1. Let the classical inflaton roll slowly toward the cliff.
2. Superpose on this motion the frozen spatial noise from horizon-exited modes.
3. Different regions then reach the cliff at slightly different times.
4. Falling off the cliff converts potential energy into particles, heat, and ordinary matter/radiation.
5. Regions that reheated earlier have already diluted more.
6. Regions that reheated later are denser.
7. The result is a spatially varying \(\delta\rho/\rho\) that later seeds observed structure.

## Notation Choices
- Use \(\ell_P,t_P,m_P\) in the chapter even though the lecture often says “the time unit” or “the mass unit” verbally.
- Use \(\mathcal{H}_{\rm osc}\) or \(E_{\rm osc}\) for the oscillator Hamiltonian in the notes, to avoid confusion with the Hubble parameter \(H\).
- Use overdots for ordinary time derivatives in ODEs: \(\dot x,\ddot x,\dot\phi,\ddot\phi,\dot\phi_k,\ddot\phi_k\).
- Use partial derivatives in the PDE stage: \(\partial_t^2\phi\) and \(\nabla^2\phi\).
- Normalize the board’s one-dimensional spatial term to the chapter form \(-\nabla^2\phi\), with a note that Susskind first wrote the \(x\)-piece and then verbally added \(y\) and \(z\).
- Write the potential derivative as \(V'(\phi)\) and identify it with \(dV/d\phi\).
- Keep \(x\) as a comoving coordinate and say explicitly that it is not a physical distance in this lecture’s convention.
- Reserve \(d_{\rm prop}\) or “proper distance” for the actual measured separation \(a(t)\Delta x\).
- Use \(\mathbf{k}\) for the comoving wavevector and \(k=|\mathbf{k}|\); keep \(k\) dimensionless to match his \(x\)-convention.
- Use \(\lambda_{\rm com}=2\pi/k\) and \(\lambda_{\rm phys}=a\lambda_{\rm com}\) to resolve the lecture’s shifting use of “wavelength”.
- Use \(\phi_k(t)\) for a single mode and refer to the full field as a Fourier integral / continuous superposition when needed.
- Call \(H\) the Hubble parameter in the prose, while noting that Susskind often says “Hubble constant” during inflation because he is treating it as approximately constant on the plateau.
- If the chapter writes \(H\sim\sqrt{V}\), mark that as Planck-unit / normalization-suppressed shorthand rather than a fully normalized Friedmann equation.

## Uncertain Mathematics
- The lower-left chalk in `lecture_10_figure_02.png` is probably \(V'(\phi)=0\), but the frame does not secure it completely.
- The board only securely shows the beginning of the flat-space wave equation; the full \(\partial_t^2\phi-\nabla^2\phi=0\) should be justified from the transcript, not the frame alone.
- The sign convention for the potential term should be stated carefully: Susskind says “put on the right-hand side minus \(dV/d\phi\),” but equivalent conventions move the term to the left.
- The zero-point estimate \(x^2\sim\hbar/\omega\) is deliberately approximate; he explicitly drops factors of \(2\).
- The underdamped solution in the transcript is partly garbled, and his spoken envelope factor blurs the correct \(\tfrac12\) in the exponent. The mathematically correct decay envelope from the quadratic is \(e^{-\gamma t/2}\).
- The exact closed form \(m_P=\sqrt{\hbar c/G}\) is a safe standard reconstruction, but the lecture only derives Planck mass indirectly through \(Et\sim\hbar\) and \(t_P\).
- “\(H\) is basically the square root of the potential energy” is only schematic unless the chapter also fixes Planck units and Friedmann normalization.
- The exact crossover condition is \(3H=2k/a\); the simpler statement \(\lambda_{\rm phys}\sim H^{-1}\) is only up to order-one factors such as \(2\pi\) and \(2/3\).
- The lecture does not derive a formal power spectrum, spectral index, or the usual slow-roll amplitude formula. Those should not be imported unless another source in the project motivates them.
- The final reheating argument is qualitative: it explains how frozen field noise becomes density contrast, but it is not a full perturbation-theory derivation.