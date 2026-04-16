# Figure Notes
## Image Inventory
- `lecture_09_figure_02.png`: Mid-board view from the Fourier-transform derivation. The top line shows a delta-function sampling identity written across the upper board. The lower line begins a rewritten $\psi(x')$ expression as an integral over $p$, with a $1/\sqrt{2\pi}$ factor, an exponential $e^{ipx'}$, and the start of a bracketed substituted expression to the right. Susskind stands at the left, but the main equations remain readable.
- `lecture_09_figure_03.png`: Close crop of the key substitution step in which $\psi(x')$ is written as an outer $x$-integral containing a boxed inner $p$-integral. Beneath it, the same expression is rewritten using a capital delta-like symbol multiplying $\psi(x)$. This is the clearest board evidence for the Fourier kernel turning into a delta function.
- `lecture_09_figure_04.png`: Clean board showing a two-line comparison between state-vector notation and wavefunction notation. The upper line is an operator $X$ acting on a ket; the lower line is the same operator acting on $\psi(x)$. There are no extra equations around it, so the layout itself is the point.
- `lecture_09_figure_05.png`: Split-board transition frame. On the left board one still sees the tail end of the position-basis discussion, including part of $\langle x'|x\rangle=\delta(x-x')$ and a partial inner-product line. On the right board Susskind has begun the momentum-operator review: $P=-i\hbar D$ and a second line for the action of $P$ on $\psi(x)$.
- `lecture_09_figure_06.png`: Upper board showing the momentum-space delta-normalization identity $\int dx\,e^{i(p-p')x}/2\pi=\delta(p-p')$, with a new lower line beginning $\langle \Psi|\Phi\rangle = \int \cdots$. Susskind is writing the momentum-space inner product beneath the already established normalization formula.

## Blackboard Equations
- `lecture_09_figure_02.png`: [partially visible] $\int dx\,F(x)\,\delta(x-x') = F(x')$.
- `lecture_09_figure_02.png`: [partially visible] $\psi(x')=\int \frac{dp}{\sqrt{2\pi}}\,e^{ipx'}[\cdots]$.
- `lecture_09_figure_02.png`: [standard reconstruction] $\psi(x')=\int \frac{dp}{\sqrt{2\pi}}\,e^{ipx'}\left[\int \frac{dx}{\sqrt{2\pi}}\,\psi(x)\,e^{-ipx}\right]$.

- `lecture_09_figure_03.png`: [visible] $\psi(x')=\int dx\left[\int \frac{dp}{2\pi}\,e^{ip(x'-x)}\right]\psi(x)$.
- `lecture_09_figure_03.png`: [visible] $\int dx\,\Delta(x'-x)\,\psi(x)$.
- `lecture_09_figure_03.png`: [standard reconstruction] $\int dx\,\delta(x'-x)\,\psi(x)=\psi(x')$.
- `lecture_09_figure_03.png`: [standard reconstruction] $\int \frac{dp}{2\pi}\,e^{ip(x'-x)}=\delta(x'-x)$.

- `lecture_09_figure_04.png`: [partially visible] $X|\Psi\rangle$.
- `lecture_09_figure_04.png`: [visible] $X\,\psi(x)$.
- `lecture_09_figure_04.png`: [standard reconstruction] $(X\psi)(x)=x\,\psi(x)$.

- `lecture_09_figure_05.png`: [partially visible] $\langle x'|x\rangle=\delta(x-x')$.
- `lecture_09_figure_05.png`: [partially visible] $P=-i\hbar D$.
- `lecture_09_figure_05.png`: [partially visible] $P\,\psi(x)=-i\hbar\,\cdots$.
- `lecture_09_figure_05.png`: [standard reconstruction] $P\,\psi(x)=-i\hbar\,\dfrac{d\psi}{dx}$.

- `lecture_09_figure_06.png`: [visible] $\int \frac{dx}{2\pi}\,e^{i(p-p')x}=\delta(p-p')$.
- `lecture_09_figure_06.png`: [partially visible] $\langle \Psi|\Phi\rangle=\int \cdots$.
- `lecture_09_figure_06.png`: [standard reconstruction] $\langle \Psi|\Phi\rangle=\int dp\,\widetilde{\psi}^{\,*}(p)\,\widetilde{\phi}(p)$.

## Diagram And Layout Reading
- There are no true geometric diagrams, axes, or particle sketches in this figure set. The value is entirely in the board organization.
- `lecture_09_figure_02.png` uses a stacked layout: an upper delta-function identity, then a lower substituted Fourier expression. This pairing matters because the lecture is about combining the Fourier-transform pair with delta-function rules.
- `lecture_09_figure_03.png` has the most important board layout in the set. The inner $p$-integral is literally boxed, visually isolating it as an object to be named and then identified with a delta function. The lower line then rewrites the expression in reduced form. That box should be conceptually preserved in the notes, even if not graphically reproduced.
- `lecture_09_figure_04.png` is organized as a pure two-line comparison: abstract operator action on a ket above, corresponding operator action on a wavefunction below. The stripped-down layout is the point; it is a pedagogical contrast rather than a derivation.
- `lecture_09_figure_05.png` is a transition frame rather than a finished derivation. The split between the left and right boards matters: the left board still carries the position-basis formalism, while the right board begins the momentum-operator discussion. That physical board split reflects the conceptual pivot in the lecture.
- `lecture_09_figure_06.png` returns to the stacked layout. The upper line gives the normalization identity in momentum space; the lower line starts the inner-product formula that uses it. The frame is useful precisely because it shows the new equation being written under the previously established identity.

## TeX Reconstruction Plan
- `lecture_09_figure_02.png` should remain visible. Pair it with a clean displayed reconstruction of the substituted Fourier-transform formula for $\psi(x')$, not just the short fragment visible on the board.
- `lecture_09_figure_03.png` must remain visible. It is the strongest documentary evidence for the boxed Fourier kernel and for the move from the inner $p$-integral to the delta function. Place a clean displayed derivation immediately beside or below it:
  $\psi(x')=\int dx\left[\int \frac{dp}{2\pi}e^{ip(x'-x)}\right]\psi(x)=\int dx\,\delta(x'-x)\psi(x)=\psi(x')$.
- `lecture_09_figure_04.png` should remain visible as a small but important layout witness. Pair it with a typeset statement of the operator action on wavefunctions, for example $(X\psi)(x)=x\psi(x)$. No TikZ is needed.
- `lecture_09_figure_05.png` should remain visible, but it can be smaller than the others because it is transitional rather than self-contained. Pair it with a clean displayed reconstruction of the momentum-operator definition:
  $P=-i\hbar \dfrac{d}{dx}$ and $(P\psi)(x)=-i\hbar \dfrac{d\psi}{dx}$.
- `lecture_09_figure_06.png` should remain visible. Pair it with a clean displayed momentum-space inner product:
  $\langle \Psi|\Phi\rangle=\int dp\,\widetilde{\psi}^{\,*}(p)\widetilde{\phi}(p)$,
  and, if helpful, restate above it the normalization identity
  $\int \dfrac{dx}{2\pi}e^{i(p-p')x}=\delta(p-p')$.
- No TikZ redraw is needed for any figure in this set. All five are equation-and-layout evidence rather than geometric diagrams.

## Caption Drafts
- `lecture_09_figure_02.png`: Delta-function sampling rule above the substituted Fourier expression
- `lecture_09_figure_03.png`: Boxed Fourier kernel collapsing to a delta function
- `lecture_09_figure_04.png`: Position operator on a ket and on a wavefunction
- `lecture_09_figure_05.png`: Momentum operator introduced beside the position-basis formulas
- `lecture_09_figure_06.png`: Momentum-space delta normalization above the inner product

## Uncertainties
- In `lecture_09_figure_02.png`, the exact delta glyph in the top line is slightly rough; the board looks like the standard sampling identity, but the handwritten symbol has a faint extra mark. Typeset it as the ordinary Dirac delta.
- In `lecture_09_figure_02.png`, the right side of the lower substituted expression is cropped; only the left half of the bracketed insertion is visible. The full formula should therefore be reconstructed from the lecture context rather than over-claimed from the image alone.
- In `lecture_09_figure_03.png`, Susskind writes a temporary capital delta-like symbol on the lower line before identifying it with the ordinary delta function. In the notes, it is reasonable to typeset the final standard $\delta(x'-x)$ while mentioning that the board briefly labels the kernel as a separate function.
- In `lecture_09_figure_04.png`, the exact state symbol inside the upper ket is not perfectly clear from the image alone; it reads like a generic ket with $\Psi$-like labeling. The real point of the frame is the operator-on-ket versus operator-on-wavefunction contrast.
- In `lecture_09_figure_05.png`, the rightmost part of the second momentum-operator line is cut off, so the full differential expression is not directly legible end to end. The transcript supports the cautious completion $P\psi(x)=-i\hbar\,d\psi/dx$.
- In `lecture_09_figure_05.png`, the subtitle window mentions “the eigenvectors of the momentum,” but the frame itself mainly captures the operator definition rather than the later momentum-eigenfunction equation. It is best used as transition evidence, not as the primary figure for the eigenvector solution.
- In `lecture_09_figure_06.png`, only the beginning of the lower inner-product equation is visible. The full momentum-space integrand is not yet on the board in the frame and must be reconstructed cautiously from the lecture context.