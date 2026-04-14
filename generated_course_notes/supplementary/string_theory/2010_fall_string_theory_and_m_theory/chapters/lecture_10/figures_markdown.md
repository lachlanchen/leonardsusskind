# Figure Notes
## Image Inventory
- `lecture_10_figure_03.png`: A board-only mathematics frame with Susskind cropped to the far left edge. Two stacked integral expressions are visible. The lower line begins with `W =` and then a prefactor `1/r` multiplying an integral of `dY/d\sigma`. The upper line shows a left-hand fraction beginning with `n` over a horizontal bar, then an equals sign, then an integral of `dY/d\tau`. At the far right edge a partial circular compact-direction sketch is cropped into the frame.
- `lecture_10_figure_04.png`: Susskind stands in front of the board while the Kaluza–Klein metric decomposition is visible. On the left one sees `g_{\mu 5}` with a downward arrow to `A_\mu`. Near the center one sees `g_{55}` and, below it, a scalar symbol drawn as `\Phi`. The ordinary `g_{\mu\nu}` part is not visible in this crop.
- `lecture_10_figure_05.png`: A cylinder-style space sketch occupies the left side of the board. The circular cross-section is drawn at the left end, with `y` indicated around the compact direction and `x` along the long direction of the tube. Inside the cylinder a curved open-string-like line with endpoint dots is drawn. On the right Susskind is writing `\partial x / \partial \sigma =`, with the equals sign just being added.

## Blackboard Equations
- `lecture_10_figure_03.png`: `W = \frac{1}{r}\int \frac{dY}{d\sigma}` [visible]
- `lecture_10_figure_03.png`: `\int \frac{dY}{d\tau}` [visible]
- `lecture_10_figure_03.png`: `\frac{n}{\cdots} = \cdots \int \frac{dY}{d\tau}` [partially visible]
- `lecture_10_figure_03.png`: `\frac{n}{r} \sim \int \frac{dY}{d\tau}` [standard reconstruction]
- `lecture_10_figure_04.png`: `g_{\mu 5}` [visible]
- `lecture_10_figure_04.png`: `A_\mu` [visible]
- `lecture_10_figure_04.png`: `g_{55}` [visible]
- `lecture_10_figure_04.png`: `\Phi` [visible]
- `lecture_10_figure_04.png`: `g_{\mu 5} \mapsto A_\mu` [standard reconstruction]
- `lecture_10_figure_04.png`: `g_{55} \mapsto \Phi` [standard reconstruction]
- `lecture_10_figure_05.png`: `\frac{\partial x}{\partial \sigma} =` [visible]
- `lecture_10_figure_05.png`: `\frac{\partial x}{\partial \sigma} = 0` [standard reconstruction]

## Diagram And Layout Reading
- `lecture_10_figure_03.png` is organized as a pair of vertically stacked formulas, clearly separating momentum-like and winding-like quantities. The lower line is the cleaner one. The partial circle at the right edge is not a standalone diagram, but it confirms that the formulas are being discussed in the context of a compact circular direction.
- `lecture_10_figure_04.png` is a component-reading board rather than a full derivation. The left side emphasizes the mixed metric component descending to a four-dimensional vector potential, while the center isolates the purely fifth-direction component as a scalar. The board layout itself supports a decomposition picture: vector on one side, scalar in the middle.
- `lecture_10_figure_05.png` is a geometry-plus-boundary-condition board. The left sketch shows a compact direction wrapped into a cylinder and a long direction running along its axis. The internal curved line with endpoint dots reads as an open string drawn inside that ambient space. The equation on the right is spatially separated from the sketch and functions like a boundary-condition statement attached to the picture.

## TeX Reconstruction Plan
- `lecture_10_figure_03.png` should remain visible in the notes. It should be paired with clean displayed equations nearby. The lower winding-number formula can be typeset directly in standard form. The upper momentum formula should be reconstructed cautiously from the transcript and surrounding discussion rather than from the partially cropped pixels alone.
- `lecture_10_figure_04.png` should remain visible in the notes. Nearby LaTeX should present a clean Kaluza–Klein-style decomposition of the five-dimensional metric into the ordinary metric, the vector component, and the scalar component. The screenshot is especially valuable as evidence for the board grouping `g_{\mu5} \to A_\mu` and `g_{55} \to \Phi`.
- `lecture_10_figure_05.png` should remain visible in the notes. It should be paired with both a clean displayed boundary-condition equation and a TikZ redraw of the cylinder/open-string geometry. The equation in the screenshot is unfinished, so the final `=0` should come from the transcript, not from the pixels. The TikZ redraw should clarify the compact `y` direction, the long `x` direction, and the open string with endpoints.

## Caption Drafts
- `lecture_10_figure_03.png`: Momentum and winding integrals on the board
- `lecture_10_figure_04.png`: Five-dimensional metric components and their four-dimensional fields
- `lecture_10_figure_05.png`: Cylinder sketch with open-string boundary condition

## Uncertainties
- In `lecture_10_figure_03.png`, the upper left-hand fraction is not fully legible. The `n` is clear, but its denominator and any prefactor before the upper integral are too weak to trust from the image alone.
- In `lecture_10_figure_03.png`, the variable in the numerator appears as `Y` or `y`; the transcript should determine the final case convention used in the notes.
- In `lecture_10_figure_03.png`, the circular sketch at the far right is cropped and should not be used as the sole basis for a redraw.
- In `lecture_10_figure_04.png`, the screenshot does not show the full list of five-dimensional metric components; it only shows the mixed and purely fifth-direction pieces. The ordinary `g_{\mu\nu}` part belongs in the notes only because the transcript supplies it.
- In `lecture_10_figure_04.png`, the scalar symbol under `g_{55}` reads naturally as `\Phi`, but the board does not show a full sentence equating the two.
- In `lecture_10_figure_05.png`, the equation is caught mid-writing. The equals sign is visible, but the final `0` is not yet present in the frame.
- In `lecture_10_figure_05.png`, the internal curved line and dots strongly suggest an open string with endpoints, but the exact interpretation should still follow the transcript’s discussion of open-string boundary conditions rather than the sketch alone.