# Figure Notes
## Image Inventory
- `lecture_03_figure_02.png` shows Susskind standing beside a black rectangular coordinate grid overlaid with a red rotated or skewed coordinate construction. A red point is marked inside the grid, and several red slanted guide lines and segments pass through it. The frame is mainly diagrammatic rather than algebraic.
- `lecture_03_figure_03.png` shows a mostly clean whiteboard with the scalar relation `\phi(y)=\phi(x)` written across the top, an arrowed `dx` notation below, and two short free arrows drawn at different locations on the board. Susskind’s hand is partly in frame at left, but the visible content is still legible.
- `lecture_03_figure_04.png` shows a clean board carrying a rank-two tensor transformation law with lower indices on the tensor and two Jacobian factors multiplying the old-coordinate tensor components. No diagram is present; this is pure equation evidence.
- `lecture_03_figure_05.png` shows Susskind next to the line-element formula in Cartesian coordinates, with a circled Kronecker delta factor multiplying two differential coordinate factors. The equation is the main content; there is slight residual writing above left from an earlier board state.
- `lecture_03_figure_06.png` shows a more developed board state for the metric under coordinate change. At the top is a differential transformation for `dx^m` in terms of derivatives with respect to `y` and `dy`; below is an expression for `ds^2` with a large circled parenthesized coefficient, and beneath that a second circled symbol identifying the transformed metric components.

## Blackboard Equations
- `lecture_03_figure_02.png`: no fully legible equation is present; the content is geometric/diagrammatic rather than algebraic. [visible]
- `lecture_03_figure_03.png`: `\phi(y)=\phi(x)` [visible]
- `lecture_03_figure_03.png`: `d\vec{x}` or arrowed `dx` [visible]
- `lecture_03_figure_04.png`: `T^{(y)}_{mn}=\dfrac{\partial x^r}{\partial y^m}\dfrac{\partial x^s}{\partial y^n}T^{(x)}_{rs}` [visible]
- `lecture_03_figure_05.png`: `ds^2=\delta_{mn}\,dx^m dx^n` [visible]
- `lecture_03_figure_06.png`: `dx^m=\dfrac{\partial x^m}{\partial y^r}\,dy^r` [visible]
- `lecture_03_figure_06.png`: `ds^2=\left(g^{(x)}_{mn}\dfrac{\partial x^m}{\partial y^r}\dfrac{\partial x^n}{\partial y^s}\right)dy^r dy^s` [partially visible]
- `lecture_03_figure_06.png`: `g^{(y)}_{rs}` [visible]
- `lecture_03_figure_06.png`: `g^{(y)}_{rs}=g^{(x)}_{mn}\dfrac{\partial x^m}{\partial y^r}\dfrac{\partial x^n}{\partial y^s}` [standard reconstruction]

## Diagram And Layout Reading
- `lecture_03_figure_02.png` organizes the board as a comparison between two coordinate systems on the same plane. The black grid provides the original rectangular reference frame, while the red slanted family of lines represents the transformed coordinates. The marked interior point and red connecting segments indicate that a single geometric vector or point is being described relative to more than one coordinate system. This is the key visual evidence for the lecture’s move from “a vector as a geometric object” to “components depend on coordinates.”
- `lecture_03_figure_03.png` is laid out very economically. The top line states that a scalar has the same value in the `x` and `y` descriptions. Below that, the arrowed `dx` indicates a geometric displacement vector. The repeated short arrows at separated locations visually support Susskind’s statement that the vector itself is a geometric object independent of where it is drawn on the board.
- `lecture_03_figure_04.png` is purely formula-centered. The left-hand side is a tensor in the `y` frame with two lower indices; the right-hand side factors into two Jacobians and a tensor in the `x` frame. The layout is already sufficiently clean that no auxiliary diagram is needed.
- `lecture_03_figure_05.png` uses a single centered expression to identify the Cartesian metric. The Kronecker delta is visually emphasized by circling, which signals that Susskind is naming it as the metric tensor in this special coordinate system.
- `lecture_03_figure_06.png` has a deliberate top-to-bottom pedagogical structure. The top equation gives the differential coordinate change. The middle equation substitutes that into the line element. The large circled parenthesized factor is the important extracted object, and the lower circled `g^{(y)}_{rs}` indicates that the parenthesized coefficient is being recognized as the new metric tensor. The board is effectively performing identification by visual grouping.

## TeX Reconstruction Plan
- `lecture_03_figure_02.png` must remain visible. It is valuable documentary evidence for the rotated/skew coordinate-grid setup. It should be paired with a clean TikZ redraw showing an original rectangular grid, a transformed skew grid, and a marked point or vector. The screenshot should not be asked to carry exact algebra; it supports the board layout and geometric idea.
- `lecture_03_figure_03.png` must remain visible. It should be paired with a clean displayed scalar relation `\phi(y)=\phi(x)` and a small TikZ sketch or inline figure showing the same free vector drawn at two different locations. The screenshot is useful because it combines equation and geometric cue in one board moment.
- `lecture_03_figure_04.png` should remain visible as equation evidence. It should also be typeset cleanly nearby as a displayed equation for the rank-two covariant tensor transformation law. No TikZ is needed here.
- `lecture_03_figure_05.png` should remain visible as equation evidence. It should be paired with a clean displayed formula `ds^2=\delta_{mn}\,dx^m dx^n`, with brief prose noting that in Cartesian coordinates the metric tensor is the Kronecker delta. No redraw is necessary.
- `lecture_03_figure_06.png` must remain visible. It should be paired with a clean displayed derivation or two-step display: first the differential coordinate transformation `dx^m=(\partial x^m/\partial y^r)\,dy^r`, then the transformed line element, and finally the identification `g^{(y)}_{rs}=g^{(x)}_{mn}(\partial x^m/\partial y^r)(\partial x^n/\partial y^s)`. The screenshot is particularly useful because the circling on the board documents the identification step.

## Caption Drafts
- `lecture_03_figure_02.png`: Skew coordinate grid and vector construction
- `lecture_03_figure_03.png`: Scalar equality and free vector
- `lecture_03_figure_04.png`: Rank-two tensor transformation law
- `lecture_03_figure_05.png`: Metric tensor in Cartesian coordinates
- `lecture_03_figure_06.png`: Metric tensor under coordinate change

## Uncertainties
- `lecture_03_figure_02.png`: the diagram is clear as a coordinate-system comparison, but exact labels for axes or components are not visible. The redraw should therefore remain schematic rather than over-labeled.
- `lecture_03_figure_03.png`: the arrowed `dx` is visible, but whether Susskind intended the notation explicitly as `d\vec{x}` or an arrow placed over `dx` should be preserved cautiously. The idea is clear even if the precise chalk styling is not.
- `lecture_03_figure_04.png`: the equation is legible, but the superscript labels indicating the coordinate frame are small; the transcript strongly supports reading them as `(y)` on the left and `(x)` on the right.
- `lecture_03_figure_05.png`: the circled metric factor is clear, but faint residual writing above left could distract from the main equation. The notes should ignore that leftover material.
- `lecture_03_figure_06.png`: the middle line is partly crowded by Susskind’s body and the board’s cropping, so the full transformed line element should be completed cautiously in standard notation. The identification of the parenthesized coefficient with `g^{(y)}_{rs}` is strongly indicated by the circles, but the exact final equality is better treated as a standard reconstruction from what is visibly staged on the board.