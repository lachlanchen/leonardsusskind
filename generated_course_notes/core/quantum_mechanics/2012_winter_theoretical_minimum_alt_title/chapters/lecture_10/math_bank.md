# Math Bank
## Core Equations
- [transcript-backed] \(H=cP\)
- [transcript-backed] \(\psi_p(x)=e^{ipx}\)
- [transcript-backed] \(\psi(x)=\langle x|\psi\rangle\)
- [transcript-backed] \(\tilde{\psi}(p)=\langle p|\psi\rangle\)
- [transcript-backed] \(\psi(x)=\frac{1}{\sqrt{2\pi}}\int dp\,\tilde{\psi}(p)e^{ipx}\)
- [standard reconstruction] \(\tilde{\psi}(p)=\frac{1}{\sqrt{2\pi}}\int dx\,\psi(x)e^{-ipx}\)
- [visible] \((\Delta x)^2=\int dx\,\psi^*(x)\psi(x)\,x^2\)
- [visible] \((\Delta x)^2=\langle \psi|X^2|\psi\rangle\) when \(\langle X\rangle=0\)
- [standard reconstruction] \((\Delta x)^2=\langle X^2\rangle-\langle X\rangle^2\)
- [transcript-backed] \((\Delta p)^2=\int dp\,|\tilde{\psi}(p)|^2\,p^2\)
- [transcript-backed] \(P=-i\,\partial_x\)
- [transcript-backed] \(P^2=-\partial_x^2\)
- [transcript-backed] \((\Delta p)^2=\langle \psi|P^2|\psi\rangle=-\int dx\,\psi^*(x)\,\partial_x^2\psi(x)\)
- [visible] \((\Delta p)^2=\int dx\,(\partial_x\psi^*)(\partial_x\psi)\)
- [standard reconstruction] \(\langle A|A\rangle\,\langle B|B\rangle\ge |\langle A|B\rangle|^2\)
- [transcript-backed] \(|A\rangle=X|\psi\rangle\)
- [transcript-backed] \(|B\rangle=P|\psi\rangle\)
- [transcript-backed] \(A(x)=x\,\psi(x)\)
- [transcript-backed] \(B(x)=-i\,\partial_x\psi(x)\)
- [transcript-backed] \(\psi\,\partial_x\psi=\tfrac12\,\partial_x(\psi^2)\) in the simplified real-\(\psi\) proof
- [standard reconstruction] \(|\langle A|B\rangle|^2=\left|\int dx\,\psi(x)\,x\,\partial_x\psi(x)\right|^2\) in that same simplification
- [visible] \((\Delta x)(\Delta p)>\tfrac12\) on the board
- [standard reconstruction] \(\Delta x\,\Delta p\ge \tfrac12\) with \(\hbar=1\)
- [standard reconstruction] \(\Delta x\,\Delta p\ge \tfrac{\hbar}{2}\)
- [transcript-backed] \(i\,\frac{d}{dt}|\psi\rangle=H|\psi\rangle\)
- [transcript-backed] \(H=\frac{P^2}{2m}+V(X)\)
- [transcript-backed] \(i\,\partial_t\psi(x,t)=-\frac{1}{2m}\partial_x^2\psi(x,t)+V(x)\psi(x,t)\)
- [transcript-backed] \(\partial_t\psi(x,t)=\frac{i}{2m}\partial_x^2\psi(x,t)-i\,V(x)\psi(x,t)\)
- [transcript-backed] \(\partial_t\psi^*(x,t)=-\frac{i}{2m}\partial_x^2\psi^*(x,t)+i\,V(x)\psi^*(x,t)\)
- [transcript-backed] \(\frac{d}{dt}\langle X\rangle=\frac{\langle P\rangle}{m}\)
- [transcript-backed] \(\frac{d}{dt}\langle P\rangle=-\left\langle \frac{dV}{dx}\right\rangle\)
- [transcript-backed] \(F(x)=-\frac{dV}{dx}\)
- [transcript-backed] \(\langle F(X)\rangle\neq F(\langle X\rangle)\) in general
- [transcript-backed] For \(F(x)=x^2\) and a symmetric two-bump packet, \(F(\langle X\rangle)=0\) while \(\langle F(X)\rangle=\langle X^2\rangle>0\)
- [transcript-backed] \(\psi(t)\sim \int dE\,\phi(E)\,e^{-iEt}\) as the Fourier-type time-energy expansion used in the late discussion

## Definitions And Objects
- Position-space wave function: amplitude that the particle is at position \(x\), written \(\psi(x)=\langle x|\psi\rangle\).
- Momentum-space wave function: projection of the same state onto momentum eigenstates, written \(\tilde{\psi}(p)=\langle p|\psi\rangle\).
- Probability densities: \( |\psi(x)|^2\) in position space and \(|\tilde{\psi}(p)|^2\) in momentum space.
- Uncertainty after shifting the mean to zero: for a variable \(Q\) with \(\langle Q\rangle=0\), the squared uncertainty is \(\langle Q^2\rangle\).
- General variance when the mean is not shifted away: \((\Delta Q)^2=\langle Q^2\rangle-\langle Q\rangle^2\).
- Auxiliary vectors for the uncertainty proof: \(A=X|\psi\rangle\) and \(B=P|\psi\rangle\).
- Normalization assumption used repeatedly: \(\int dx\,|\psi(x)|^2=1\).
- Integration-by-parts rule used throughout: \(\int f\,g'\,dx=-\int f' g\,dx\) when boundary terms vanish.
- Potential operator in the \(x\)-representation: \(V(X)\) acts by multiplication, \(V(X)\psi(x)=V(x)\psi(x)\).
- Force function: \(F(x)=-V'(x)\).
- Heuristic identification at the end: for a reasonably localized packet, the packet center is identified with the expectation value \(\langle X\rangle\).
- Multi-coordinate extension: for several particles or several commuting coordinates, the wave function depends on all of those coordinates simultaneously.
- Mixed representations are allowed: some coordinates can remain in \(x\)-space while others are represented in momentum space.
- Simplifying proof assumption: \(\psi(x)\) is taken real only for the uncertainty-principle derivation on the board.

## Derivation Steps
Position uncertainty
1. Shift the spatial origin so that \(\langle X\rangle=0\).
2. Define the squared uncertainty as \((\Delta x)^2=\langle X^2\rangle\).
3. Write the expectation value in position space as \((\Delta x)^2=\int dx\,|\psi(x)|^2x^2\).
4. If the origin is not shifted, replace this by \(\langle X^2\rangle-\langle X\rangle^2\).

Momentum uncertainty in the \(x\)-representation
1. Start from \((\Delta p)^2=\langle P^2\rangle\) after shifting so that \(\langle P\rangle=0\).
2. Use \(P=-i\,\partial_x\), hence \(P^2=-\partial_x^2\).
3. Write \((\Delta p)^2=-\int dx\,\psi^*(x)\partial_x^2\psi(x)\).
4. Note the apparent sign problem.
5. Integrate by parts once, moving one derivative onto \(\psi^*\).
6. Discard the boundary term using decay of the normalized wave function at infinity.
7. Obtain \((\Delta p)^2=\int dx\,(\partial_x\psi^*)(\partial_x\psi)\).
8. Conclude that the result is real and nonnegative.

Uncertainty-principle proof used in the lecture
1. Assume \(\langle X\rangle=\langle P\rangle=0\).
2. Make the board simplification \(\psi(x)\in\mathbb{R}\).
3. Define \(A=X|\psi\rangle\) and \(B=P|\psi\rangle\).
4. Identify \(\langle A|A\rangle=(\Delta x)^2\) and \(\langle B|B\rangle=(\Delta p)^2\).
5. Apply \(\langle A|A\rangle\langle B|B\rangle\ge |\langle A|B\rangle|^2\).
6. Write \(\langle A|B\rangle\) as an integral proportional to \(\int dx\,\psi\,x\,\partial_x\psi\).
7. Use \(\psi\,\partial_x\psi=\tfrac12\,\partial_x(\psi^2)\).
8. Replace the integrand by \(x\,\tfrac12\,\partial_x(\psi^2)\).
9. Integrate by parts to move the derivative from \(\psi^2\) onto \(x\).
10. Use \(\partial_x x=1\).
11. Use normalization \(\int dx\,\psi^2=1\).
12. Obtain \(|\langle A|B\rangle|^2=\tfrac14\).
13. Conclude \((\Delta x)^2(\Delta p)^2\ge \tfrac14\).
14. Take square roots to get \(\Delta x\,\Delta p\ge \tfrac12\).
15. Restore units at the end to get \(\Delta x\,\Delta p\ge \hbar/2\).

Position-space Schrödinger equation
1. Start from the abstract law \(i\,\frac{d}{dt}|\psi\rangle=H|\psi\rangle\).
2. Choose \(H=\frac{P^2}{2m}+V(X)\).
3. Move to the \(x\)-representation.
4. Replace \(P^2\) by \(-\partial_x^2\).
5. Interpret \(V(X)\) as multiplication by \(V(x)\).
6. Obtain \(i\,\partial_t\psi(x,t)=-\frac{1}{2m}\partial_x^2\psi(x,t)+V(x)\psi(x,t)\).
7. Write the complex conjugate equation for \(\psi^*(x,t)\) because both are used later.

Derivation of \(\frac{d}{dt}\langle X\rangle=\frac{\langle P\rangle}{m}\)
1. Start from \(\langle X\rangle=\int dx\,\psi^*\,x\,\psi\).
2. Differentiate in time; \(x\) itself is time-independent.
3. Get one term with \(\dot{\psi}^*\) and one term with \(\dot{\psi}\).
4. Use the fact that the two terms are complex conjugates.
5. Keep one term and add its conjugate, equivalently keep twice the real part.
6. Substitute \(\dot{\psi}^*\) from the conjugate Schrödinger equation.
7. Observe that the \(V(x)\) contribution is pure imaginary and cancels in the final real answer.
8. Integrate by parts on the kinetic term.
9. When the derivative hits \(x\), it produces \(1\).
10. The remaining term is proportional to \(\int dx\,\psi^*(-i\,\partial_x)\psi\).
11. Recognize this as \(\langle P\rangle\).
12. Conclude \(\frac{d}{dt}\langle X\rangle=\frac{\langle P\rangle}{m}\).

Derivation of \(\frac{d}{dt}\langle P\rangle=-\left\langle \frac{dV}{dx}\right\rangle\)
1. Start from \(\langle P\rangle=\int dx\,\psi^*(-i\,\partial_x)\psi\).
2. Differentiate in time.
3. Rearrange one term by integration by parts so the pair is easier to compare under complex conjugation.
4. Substitute the Schrödinger equations for \(\dot{\psi}\) and \(\dot{\psi}^*\).
5. Track the kinetic pieces and use integration by parts plus conjugation to show the surviving contribution from that part is purely imaginary and drops out of the final real equation.
6. Keep the potential contribution.
7. Combine the potential terms into \(V(x)\big(\psi\,\partial_x\psi^*+\psi^*\,\partial_x\psi\big)\).
8. Recognize the bracket as \(\partial_x(\psi^*\psi)\).
9. Integrate by parts once more, moving \(\partial_x\) from \(\psi^*\psi\) onto \(V(x)\).
10. Drop the boundary term.
11. Obtain \(-\int dx\,|\psi(x)|^2\,V'(x)\).
12. Recognize this as \(-\left\langle \frac{dV}{dx}\right\rangle\).
13. Conclude \(\frac{d}{dt}\langle P\rangle=-\left\langle \frac{dV}{dx}\right\rangle\).

Classical-limit comparison at the end
1. Exact quantum mechanics gives \(\frac{d}{dt}\langle P\rangle=\langle F(X)\rangle\) with \(F=-V'\).
2. Classical mechanics for the packet center would need \(\frac{d}{dt}\langle P\rangle\approx F(\langle X\rangle)\).
3. These are not equal in general.
4. Use the two-bump packet with \(F(x)=x^2\): \(\langle X\rangle=0\), so \(F(\langle X\rangle)=0\), but \(\langle X^2\rangle>0\).
5. Therefore the exact Ehrenfest-type equations do not by themselves give classical mechanics.
6. The extra approximation is that the packet remains narrow enough in a smooth enough potential that \(\langle F(X)\rangle\approx F(\langle X\rangle)\).

## Notation Choices
- Use uppercase \(X,P,H\) for operators and lowercase \(x,p\) for variables or eigenvalues.
- Use \(|\psi\rangle\) for the abstract state and \(\psi(x)\), \(\tilde{\psi}(p)\) for the wave functions in specific representations.
- Use \(\tilde{\psi}(p)\) in the final notes even though the transcript often says “psi of p” or “psi twiddle of p.”
- Typeset expectation values in bra-ket form: \(\langle X\rangle=\langle\psi|X|\psi\rangle\), \(\langle P^2\rangle=\langle\psi|P^2|\psi\rangle\).
- Replace the lecture’s informal \(A\cdot B\) by \(\langle A|B\rangle\) in the polished notes, with a short note that Susskind is using vector-space dot-product language.
- Replace the lecture’s “triangle inequality” by the cleaned Hilbert-space inequality \(\langle A|A\rangle\langle B|B\rangle\ge |\langle A|B\rangle|^2\), while noting that this is the mathematical ingredient he invokes.
- Use \(\partial_x\) and \(\partial_t\) in the final notes once time-dependent wave functions appear, even if the lecture says \(d/dx\) and \(d/dt\) aloud.
- State explicitly where \(\hbar=1\) is being used, and restore \(\hbar\) in the final uncertainty bound.
- Use \(V'(x)\) and \(\frac{dV}{dx}\) interchangeably only if the chapter stays in one variable; otherwise standardize to \(V'(x)\) in prose and displayed equations.
- Keep the real-\(\psi\) assumption local to the uncertainty-proof subsection; do not let it leak into the general chapter notation.
- Do not write \(\psi^2\) unless the text has already announced the temporary assumption that \(\psi\) is real.
- For many-particle remarks, use a conventional notation such as \(\psi(x_1,\dots,x_N)\) rather than the transcript’s verbal “function of \(10^{23}\) coordinates.”

## Uncertain Mathematics
- The general variance formula is garbled in the transcript; the intended cleaned formula is \((\Delta x)^2=\langle X^2\rangle-\langle X\rangle^2\).
- The momentum-space uncertainty formula is also noisy in the transcript; the safe cleaned form is \((\Delta p)^2=\int dp\,|\tilde{\psi}(p)|^2p^2\).
- The board shows a strict inequality \(>\), but the mathematically correct final statement is non-strict \(\ge\).
- The lecture repeatedly says “triangle inequality,” but the clean note form should be Cauchy-Schwarz for inner products; preserve his language only as a pedagogical remark.
- In the \(A\cdot B\) part of the proof, Susskind deliberately suppresses some minus signs and factors of \(i\) because he takes an absolute value at the end; the polished derivation should restore the structure carefully.
- The real-\(\psi\) simplification is not the general theorem; the final notes should mark it as a pedagogical restriction used only to shorten the board algebra.
- The transcript around the transition from the inequality to the choice of \(A\) and \(B\) is badly corrupted; reconstruct that bridge from the surrounding legible math rather than the garbled words.
- The full abstract equation \(i\,\frac{d}{dt}|\psi\rangle=H|\psi\rangle\) is only partially visible in the frame; its clean form should be taken from the transcript.
- The time-energy uncertainty discussion is suggestive and Fourier-based, not a full formal derivation in this lecture; do not overstate it.
- The angle-angular-momentum uncertainty remark is brief and secondary; keep it as an analogue, not as a developed derivation.
- The assertion that one can shift both \(\langle X\rangle\) and \(\langle P\rangle\) to zero is made verbally but not proved in detail here; treat it as an asserted setup move, not a derived theorem inside this chapter.
- The late relation \(\Delta v\,\Delta x\sim \hbar/m\) is heuristic, tied to near-saturation and macroscopic reasoning, not a new exact theorem of the lecture.
- The exact result is \(\frac{d}{dt}\langle P\rangle=-\langle V'(X)\rangle\); the replacement by \(-V'(\langle X\rangle)\) is only a classical-limit approximation for localized packets in smooth potentials.