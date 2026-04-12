# Figure Notes
## Image Inventory
- `lecture_08_figure_02.png`: Leonard Susskind stands in front of a mostly blank whiteboard. Two pieces of notation are visible: `G_{\mu\nu}` on the left side of the board and `g_{\mu\nu}(x)` near the top center. The rest of the board is empty, so this is mainly a setup shot for the geometric side of Einstein's equations.
- `lecture_08_figure_03.png`: Susskind stands in front of a partially visible two-line board state. Near the top left one can still see `g_{\mu\nu}(x)`. A cropped upper line contains the metric term ending in `a(t)^2 dx^2`, and a lower cropped line shows the Friedmann prefactor `8\pi G/3` multiplying `\rho(t)`. The left-hand sides of both lines are cut off.
- `lecture_08_figure_04.png`: Susskind stands to the left of a fuller, cleaner board state. The upper line clearly shows the expanding-universe metric, and the lower line clearly shows the Friedmann equation in terms of `\dot a / a` and `\rho(t)`. The notation `g_{\mu\nu}(x)` remains written above.

## Blackboard Equations
- `lecture_08_figure_02.png`: \(G_{\mu\nu}\) [visible]
- `lecture_08_figure_02.png`: \(g_{\mu\nu}(x)\) [visible]

- `lecture_08_figure_03.png`: \(g_{\mu\nu}(x)\) [visible]
- `lecture_08_figure_03.png`: \(dt^2 + a(t)^2\,dx^2\) [partially visible]
- `lecture_08_figure_03.png`: \(\dfrac{8\pi G}{3}\,\rho(t)\) [visible]
- `lecture_08_figure_03.png`: \(ds^2 = -dt^2 + a(t)^2\,dx^2\) [standard reconstruction]
- `lecture_08_figure_03.png`: \(\left(\dfrac{\dot a}{a}\right)^2 = \dfrac{8\pi G}{3}\,\rho(t)\) [standard reconstruction]

- `lecture_08_figure_04.png`: \(g_{\mu\nu}(x)\) [visible]
- `lecture_08_figure_04.png`: \(ds^2 = -dt^2 + a(t)^2\,dx^2\) [visible]
- `lecture_08_figure_04.png`: \(\left(\dfrac{\dot a}{a}\right)^2 = \dfrac{8\pi G}{3}\,\rho(t)\) [visible]

## Diagram And Layout Reading
- `lecture_08_figure_02.png` is not a diagram; it is a board-layout shot. Its value is documentary: Susskind has written the geometric tensor on one side and the metric tensor above, but has not yet filled in the full field equation. The emptiness of the board matters because it shows the lecture at the setup stage.
- `lecture_08_figure_03.png` preserves an intermediate board state in which the lecture has moved from abstract Einstein-tensor notation to a concrete cosmological metric and Friedmann equation. The board reads as a two-line stack: metric above, cosmological dynamics below. The left side is cropped, so the layout is more useful than the raw transcription alone.
- `lecture_08_figure_04.png` is the clearest equation-layout frame. The upper metric line and lower Friedmann line are aligned as a compact two-equation block, with `g_{\mu\nu}(x)` written above as a reminder of the underlying metric-tensor language. There are no axes, arrows, or sketches; this is purely an equation-column figure.

## TeX Reconstruction Plan
- `lecture_08_figure_02.png` should remain visible as a small documentary screenshot. It should be paired with nearby prose or displayed notation explaining that \(G_{\mu\nu}\) is the geometric side of Einstein's equations and that it is built from the metric tensor \(g_{\mu\nu}(x)\). Do not reconstruct a full Einstein equation from the image alone in the figure caption; the frame only supports the setup notation.
- `lecture_08_figure_03.png` should remain visible. Because the board is cropped, the notes should typeset the full metric and Friedmann equation nearby as clean displayed equations, using the screenshot as evidence for the in-progress board state rather than as the sole source of the formulas.
- `lecture_08_figure_04.png` should remain visible as the main equation screenshot for this stretch of the lecture. The same two equations should be reproduced cleanly in LaTeX in the surrounding text or immediately below the figure, since this frame is strong enough to support the final board organization.
- No TikZ redraw is needed for any of these three figures. They are equation-layout screenshots, not diagrammatic sketches.

## Caption Drafts
- `lecture_08_figure_02.png`: Geometric-side notation for Einstein's equations
- `lecture_08_figure_03.png`: Partial metric and Friedmann terms on the board
- `lecture_08_figure_04.png`: Expanding-universe metric and Friedmann equation

## Uncertainties
- `lecture_08_figure_02.png`: only \(G_{\mu\nu}\) and \(g_{\mu\nu}(x)\) are visible. The full Einstein field equation is not written out in the frame.
- `lecture_08_figure_03.png`: the left side of the upper metric line is cropped, so the leading \(ds^2=\) and the minus sign before \(dt^2\) must be supplied cautiously from the lecture context.
- `lecture_08_figure_03.png`: the left side of the lower line is also cropped, so \(\left(\dot a/a\right)^2\) is a transcript-backed completion rather than directly fully legible board text in this frame.
- `lecture_08_figure_04.png`: the shorthand \(dx^2\) is visible, but the frame does not itself expand this into \(dx^2+dy^2+dz^2\); that broader meaning comes from the lecture context.
- `lecture_08_figure_04.png`: there is a small partial mark at the far right edge of the board that does not belong to the main metric/Friedmann block and should not be used in reconstruction.