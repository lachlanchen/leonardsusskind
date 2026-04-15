# Visual Evidence
## Frame Inventory
- `lecture_02_figure_02.png`: Recap board showing the solved matter-only case, with \(\frac{da}{dt}=\frac{1}{\sqrt a}\) visible and a boxed \(a=t^{2/3}\) partly visible; keep only as an optional small recap screenshot, not as a primary figure.
- `lecture_02_figure_03.png`: Board frame combining the non-zero-energy Friedmann discussion with the Newtonian enclosed-mass sphere sketch labeled \(M\), \(a\), and \(x=1\); this screenshot should remain in the final notes.
- `lecture_02_figure_04.png`: Single long Friedmann-style equation arranged as geometry on the left and source on the right, with Susskind pointing at the RHS; keep only if a contextual screenshot is wanted for the Einstein-equation interpretation.
- `lecture_02_figure_05.png`: Side-by-side blackboard comparison between curvature-form Friedmann notation and the density-substituted \(\nu/a^3\) form; this screenshot should remain because it records the notational transition.
- `lecture_02_figure_06.png`: Clean centered mixed matter-plus-radiation equation with \(a^{-3}\) and \(a^{-4}\) terms; the screenshot may remain, but the typeset equation is more important than the frame itself.

## Equation Extraction
- `lecture_02_figure_02.png`: [visible] \(\frac{da}{dt}=\frac{1}{\sqrt a}\)
- `lecture_02_figure_02.png`: [partially visible] \(\frac{dt}{da}=\sqrt a\)
- `lecture_02_figure_02.png`: [partially visible] \(a=t^{2/3}\)
- `lecture_02_figure_03.png`: [visible] \(V=\frac{4\pi}{3}a^3\)
- `lecture_02_figure_03.png`: [visible] \(M,\ a,\ x=1,\ D=a,\ V=\dot a\)
- `lecture_02_figure_03.png`: [partially visible] \(\left(\frac{\dot a}{a}\right)^2-\frac{8\pi G\rho}{3}=\frac{C}{a^2}\)
- `lecture_02_figure_03.png`: [standard completion] \(\left(\frac{\dot a}{a}\right)^2=\frac{8\pi G\rho}{3}+\frac{C}{a^2}\)
- `lecture_02_figure_04.png`: [partially visible] \(\left(\frac{\dot a}{a}\right)^2+\frac{C}{a^2}=\frac{8\pi G}{3}\rho\)
- `lecture_02_figure_05.png`: [partially visible] \(\left(\frac{\dot a}{a}\right)^2-\frac{K}{a^2}=\frac{8\pi G}{3}\rho\)
- `lecture_02_figure_05.png`: [visible] \(\left(\frac{\dot a}{a}\right)^2=\frac{8\pi G}{3}\frac{\nu}{a^3}-\frac{C}{a^2}\)
- `lecture_02_figure_06.png`: [visible] \(\left(\frac{\dot a}{a}\right)^2=\frac{C_1}{a^3}+\frac{C}{a^4}\)
- `lecture_02_figure_06.png`: [standard completion] \(\left(\frac{\dot a}{a}\right)^2=\frac{C_1}{a^3}+\frac{C_2}{a^4}\)
- `lecture_02_figure_06.png`: [standard completion] \(\left(\frac{\dot a}{a}\right)^2=\frac{C_m}{a^3}+\frac{C_r}{a^4}\)

## Diagram Extraction
- `lecture_02_figure_03.png`: The key redraw candidate is the Newtonian enclosed-mass construction: a large sphere, central concentrated mass \(M\), a test galaxy at the boundary with comoving label \(x=1\), and a radial segment of physical length \(a\); this should be shown both as the original screenshot and as a clean TikZ redraw.
- `lecture_02_figure_03.png`: The side annotations \(D=a\) and \(V=\dot a\) matter for the notes because they record how Susskind is identifying physical distance and radial velocity in the Newtonian picture.
- `lecture_02_figure_02.png`: There is no real diagram to redraw; the only visually distinctive feature is the boxed matter-only result, which is better reproduced typographically.
- `lecture_02_figure_04.png`: No diagram is present; the board structure is purely equation-as-layout.
- `lecture_02_figure_05.png`: No geometric figure is present, but the side-by-side board arrangement itself is useful documentary evidence and should be preserved if this transition is discussed visually.
- `lecture_02_figure_06.png`: No diagram is present; this is a pure equation frame.

## Reconstruction Guidance
- Reconstruct the mathematics in the transcript’s order: matter-only recap, then non-zero energy, then Einstein-style geometry/source rewrite, then mixed matter-plus-radiation.
- For `lecture_02_figure_02.png`, typeset the recap equations cleanly and treat the screenshot only as evidence that the board was summarizing the already-solved \(a\propto t^{2/3}\) case.
- For `lecture_02_figure_03.png`, typeset the non-zero-energy Friedmann equation cleanly and redraw the enclosed-mass sphere in TikZ; keep the screenshot nearby because it preserves the original blackboard layout and labels better than prose alone.
- For `lecture_02_figure_04.png`, use a clean displayed equation in the notes; the screenshot is secondary and should only support the “geometry on the left, source on the right” interpretation.
- For `lecture_02_figure_05.png`, typeset both the curvature form and the \(\nu/a^3\) substitution form as separate display equations; keep the screenshot because the board comparison is itself part of the lecture’s structure.
- For `lecture_02_figure_06.png`, typeset the mixed equation in cleaned notation, but note in surrounding prose that the board coefficient on the \(a^{-4}\) term is later corrected verbally.
- Disambiguate symbols when rewriting: the board uses \(V\) for both volume and velocity-like notation, so the final notes should not reproduce that ambiguity.
- Where a symbol or sign is hidden by Susskind’s body or hand, prefer cautious standard completion guided by the lecture rather than aggressive blackboard reconstruction.

## Uncertainties
- In `lecture_02_figure_02.png`, the intermediate inversion step is partly blocked, so \(\frac{dt}{da}=\sqrt a\) is a cautious completion rather than a fully clean reading.
- In `lecture_02_figure_02.png`, the boxed \(a=t^{2/3}\) is only partly visible, and any omitted prefactor should come from the transcript, not from the frame.
- In `lecture_02_figure_03.png`, the central term of the Friedmann equation is partly covered by Susskind’s hand, so the exact sign and ordering should not be claimed from pixels alone.
- In `lecture_02_figure_03.png`, \(V=\dot a\) is almost certainly “velocity,” while \(V=\frac{4\pi}{3}a^3\) is volume; the board uses the same letter for two different quantities.
- In `lecture_02_figure_04.png`, the subtitle mentions the energy-momentum tensor, but no explicit tensor notation is visible in the frame.
- In `lecture_02_figure_05.png`, the curvature symbol looks like \(K\), but the lecture later also discusses \(\kappa\); sign convention and naming should be standardized only in the cleaned notes.
- In `lecture_02_figure_06.png`, the second coefficient is written as plain \(C\), but the transcript later corrects this to a second constant such as \(C_2\), \(C_r\), or “radiation coefficient.”