# Visual Evidence
## Frame Inventory
- `lecture_06_figure_01.png`: Stanford title card on a black background with no board content; it should not remain in the final notes.
- `lecture_06_figure_02.png`: Susskind stands beside a cropped right-board review of the matter-dominated Hubble relation; it may remain as a secondary screenshot, but only as supporting evidence.
- `lecture_06_figure_03.png`: Susskind is writing the central-force equation while a circular-orbit sketch with a central mass remains visible on the left; it should remain in the final notes.
- `lecture_06_figure_04.png`: transitional board-layout frame showing `k=0`, a likely `\xi=r`, the older orbit sketch, and a cropped Hubble/Friedmann expression; it may remain as a contextual screenshot, but it is not strong enough to carry exact transcription.
- `lecture_06_figure_05.png`: split-board derivation frame combining a left-side `dN/dz` expression with right-side matter-dominated reminders `a\sim t^{2/3}`, `\dot a`, and `r(t)`; it should remain in the final notes.
- `lecture_06_figure_06.png`: strong summary board with a boxed matter-dominated Friedmann equation plus lower-board shell-growth expressions; it should remain in the final notes.

## Equation Extraction
- `lecture_06_figure_02.png`: \(\frac{1}{a^2}=H^2\) [visible]
- `lecture_06_figure_02.png`: \(a\sim t^{2/3}\) [partially visible]
- `lecture_06_figure_02.png`: \(\frac{\dot a}{a}=\frac{2}{3t}\) [standard completion]

- `lecture_06_figure_03.png`: \(\frac{MG}{\phantom{r^2}}\) [visible]
- `lecture_06_figure_03.png`: \(\frac{GM}{r^2}=\frac{v^2}{r}\) [standard completion]
- `lecture_06_figure_03.png`: \(\frac{G\,M(r)}{r^2}=\frac{v^2}{r}\) [standard completion]
- `lecture_06_figure_03.png`: \(M\) at the center of the orbit sketch [partially visible]

- `lecture_06_figure_04.png`: \(k=0\) [visible]
- `lecture_06_figure_04.png`: \(\xi=r\) [partially visible]
- `lecture_06_figure_04.png`: \(\left(\frac{\dot a}{a}\right)^2\) [partially visible]

- `lecture_06_figure_05.png`: \(\frac{dN}{dz}\) [visible]
- `lecture_06_figure_05.png`: \(\frac{dN}{dz}\sim \cdots\) [visible]
- `lecture_06_figure_05.png`: \(\xi(r)^2\) [partially visible]
- `lecture_06_figure_05.png`: \(a\sim t^{2/3}\) [visible]
- `lecture_06_figure_05.png`: \(\dot a=\frac{2}{3}t^{-1/3}\) [partially visible]
- `lecture_06_figure_05.png`: \(r(t)\) [visible]
- `lecture_06_figure_05.png`: \(\frac{dN}{dz}\propto \frac{\xi(r)^2}{(1+z)\dot a}\) [standard completion]

- `lecture_06_figure_06.png`: \(-\frac{k}{a^2}+\frac{8\pi G}{3}\rho=H^2\) [partially visible]
- `lecture_06_figure_06.png`: \(\frac{C_m}{a^3}-\frac{k}{a^2}=H^2\) [visible]
- `lecture_06_figure_06.png`: \(r^2\,dr\) [visible]
- `lecture_06_figure_06.png`: \(e^{2r}\,dr\) [visible]
- `lecture_06_figure_06.png`: \(\Omega_k=1\) [partially visible]

## Diagram Extraction
- `lecture_06_figure_03.png`: circular-orbit sketch around a central mass; this should be shown both ways, as the original screenshot and as a clean TikZ redraw, because the board pairing of sketch plus force law is central to the rotation-curve argument.
- `lecture_06_figure_04.png`: residual circular sketch with cross-axes and central mark; this should be preserved only as screenshot evidence if the frame is used at all, since it is a leftover board state rather than a clean standalone diagram.
- `lecture_06_figure_05.png`: no standalone geometric diagram, but the board structure itself is important because it visually separates observable-side `dN/dz` from model-side inputs `a(t)`, `\dot a(t)`, and `r(t)`; preserve as screenshot.
- `lecture_06_figure_06.png`: no explicit drawn geometry beyond board organization, but the lower board’s `r^2dr` versus `e^{2r}dr` acts like a compressed diagram of flat versus negatively curved shell growth; preserve as screenshot, and optionally restate the contrast in a clean displayed equation nearby rather than forcing a TikZ redraw.
- No current selected frame cleanly preserves the past-light-cone spacetime sketch described in the transcript, so that diagram should not be newly redrawn from these frames alone without making clear it is transcript-driven rather than frame-driven.

## Reconstruction Guidance
- Treat `lecture_06_figure_01.png` as rejected visual material. It contributes no note-worthy mathematics, notation, or board layout.
- For `lecture_06_figure_02.png`, keep the screenshot only if the notes explicitly discuss the matter-dominated relation between \(a(t)\) and the inverse age scale set by \(H\). The final notes should typeset the cleaned equations \(a(t)\propto t^{2/3}\) and \(\dot a/a=2/(3t)\) next to the frame rather than relying on the cropped board.
- For `lecture_06_figure_03.png`, use the screenshot as primary board evidence for the Newtonian rotation-curve setup, but typeset the clean equations separately. A TikZ redraw should simplify the orbit, radius, central mass, and tangential velocity; the screenshot should remain nearby so the reader sees the original board state that motivated the redraw.
- For `lecture_06_figure_04.png`, treat the frame as contextual evidence for the lecture’s “model = curvature plus expansion history” pivot. Do not lean on it for exact formula transcription beyond `k=0` and the probable flat-space label `\xi=r`.
- For `lecture_06_figure_05.png`, preserve the screenshot because it is the clearest visual bridge between the abstract observable \(dN/dz\) and the matter-dominated substitutions \(a(t)\), \(\dot a(t)\), and \(r(t)\). The cleaned formula for \(dN/dz\) should be typeset separately and explicitly marked as a cautious cleaned version of the board work.
- For `lecture_06_figure_06.png`, preserve the screenshot as a main evidence figure in the observational-fit section. The boxed equation should be re-typeset cleanly, and the shell-growth factors \(r^2dr\) and \(e^{2r}dr\) should be restated in a compact displayed form or brief explanatory paragraph.
- Across all frames, prefer this pattern: keep the screenshot when it captures the lecturer’s board logic or layout, but let the final notes carry the actual mathematical burden through clean LaTeX equations. The screenshot is evidence; the typeset equation is the authoritative readable form.

## Uncertainties
- `lecture_06_figure_02.png`: the exponent on \(t\) and the full right-hand side of the \(\dot a/a\) line are cropped, so the completion to \(t^{2/3}\) and \(2/(3t)\) is transcript-backed rather than fully legible in the frame.
- `lecture_06_figure_03.png`: only `MG` and the fraction bar are directly visible; the denominator and right-hand side need standard completion from the lecture argument.
- `lecture_06_figure_04.png`: the upper-left symbol that appears as `3 = r` is very likely \(\xi=r\), but the frame is not sharp enough to treat that as certain.
- `lecture_06_figure_04.png`: the right-board Hubble/Friedmann expression is too cropped to support aggressive transcription.
- `lecture_06_figure_05.png`: the left-side fraction is not fully legible, and the numerator involving \(\xi(r)^2\) is plausible but not perfectly crisp.
- `lecture_06_figure_05.png`: the cleaned denominator \((1+z)\dot a\) comes from cautious reconstruction of the transcripted derivation, not from a fully readable frame.
- `lecture_06_figure_06.png`: the boxed matter-dominated equation is clear, but the unboxed left-side Friedmann form is only partial, and the \(\Omega_k=1\) line is not fully secure.
- The board often contains remnants from slightly earlier steps, so any single frame may mix active derivation with leftover writing; the final notes should distinguish the active mathematical point from residual board content.