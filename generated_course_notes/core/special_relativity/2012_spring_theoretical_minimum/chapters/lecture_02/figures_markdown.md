# Figure Notes
## Image Inventory
- `lecture_02_figure_02.png`: Susskind stands in front of a large cartoon-like board sketch of a train or car interior. The upper rectangular region is labeled `x,t`. Inside it, a small stick figure is marked near a label for the primed origin, and a separate highlighted event is marked with a primed-space/primed-time notation. A red dashed vertical line projects that event downward to a lower reference line with tick marks and a red `x`. A second observer sketch appears below the train floor.
- `lecture_02_figure_03.png`: a whiteboard filled with four stacked Lorentz-style transformation equations. The top pair relates primed coordinates to unprimed coordinates with velocity \(v\); the lower pair relates double-primed coordinates to primed coordinates with velocity \(u\). Susskind gestures toward the lower equations, especially the lower time equation.
- `lecture_02_figure_04.png`: a later, fuller version of the train-and-kiddie-car sketch. The left edge still shows part of the velocity-composition algebra from the previous board. The main right-board sketch shows the unprimed frame labeled `x,t`, the earlier primed observer, a red dashed vertical projection, and a car-like object to the right marked with double-prime notation and a rightward arrow labeled `u`. Susskind points directly at the double-primed car.

## Blackboard Equations
- `lecture_02_figure_02.png`
  - `x,t` [visible]
  - `x'=0` [visible]
  - `x',t'` with an equals-zero mark nearby [partially visible]
  - `x=vt` [standard reconstruction]
- `lecture_02_figure_03.png`
  - `X'=\dfrac{X-vt}{\sqrt{1-v^2}}` [visible]
  - `t'=\dfrac{t-vx}{\sqrt{1-v^2}}` [visible]
  - `X''=\dfrac{X'-ut'}{\sqrt{1-u^2}}` [visible]
  - `t''=\dfrac{t'-ux'}{\sqrt{1-u^2}}` [visible]
- `lecture_02_figure_04.png`
  - `x,t` [visible]
  - `x'=0` [visible]
  - `x'',t''` [partially visible]
  - `u` [visible]
  - `X=\dfrac{u+v}{1+uv}\,t` [partially visible]
  - `x''=0` [standard reconstruction]

## Diagram And Layout Reading
- `lecture_02_figure_02.png` preserves the lecture’s first train/station cartoon for Lecture 2. The board is organized as a large upper rectangle representing the moving carriage described in unprimed coordinates, with the primed observer drawn inside. The key visual message is that the primed origin sits at a definite place in the train and that an event inside the train is projected down to the station line below.
- The red dashed vertical line in `lecture_02_figure_02.png` matters: it ties an event in the upper moving system to a marked location on the lower line. The lower line with tick marks and the red `x` serves as the stationary reference line. This is more a conceptual layout sketch than a quantitative diagram.
- `lecture_02_figure_03.png` is laid out as a pure equation board. The top half repeats the standard Lorentz transformation between unprimed and primed coordinates. The bottom half introduces a second Lorentz transformation between primed and double-primed coordinates. The stacked format itself is important because it shows Susskind setting up composition of boosts.
- `lecture_02_figure_04.png` is the diagrammatic counterpart to the algebraic composition in `lecture_02_figure_03.png`. It extends the earlier train cartoon by adding the kiddie car on the right and a velocity arrow `u`, making the three-frame setup visible at once: stationary frame, train frame, and double-primed kiddie-car frame. Susskind’s finger locates the point corresponding to the double-primed origin.
- Across `lecture_02_figure_02.png` and `lecture_02_figure_04.png`, the board mixes a box-like train interior, observer doodles, event markers, and projection lines rather than clean analytic axes. For the notes, the geometry is schematic and explanatory, not literal spacetime plotting.

## TeX Reconstruction Plan
- `lecture_02_figure_02.png` should remain visible in the notes because it documents the train/station board layout and the lecture’s way of identifying the primed origin inside the moving carriage. It should be paired with a nearby clean reconstruction, preferably TikZ, that makes the same conceptual point more legibly: the moving observer at \(x'=0\) and the corresponding unprimed relation \(x=vt\).
- `lecture_02_figure_03.png` should remain visible as documentary evidence for the stacked transformation setup. The equations themselves should be typeset cleanly as displayed math next to or immediately after the screenshot. No TikZ redraw is needed for this image.
- `lecture_02_figure_04.png` should remain visible because it is the strongest board witness for the double-primed origin and the kiddie-car construction. It should be paired with both a clean displayed equation for the velocity-composition result and a TikZ redraw of the three-level train/passenger/kiddie-car sketch, with the double-primed origin marked explicitly.
- The notes should use the screenshots as evidence of board organization and live derivation flow, but not rely on them for final readability. In particular, the notation should be standardized in LaTeX even though the board alternates between uppercase `X` and lowercase `x`.
- A good local pairing strategy is:
  - `lecture_02_figure_02.png` + TikZ schematic + displayed \(x'=0 \iff x=vt\)
  - `lecture_02_figure_03.png` + displayed four-equation stack
  - `lecture_02_figure_04.png` + TikZ schematic + displayed \(w=\dfrac{u+v}{1+uv}\) and the condition \(x''=0\)

## Caption Drafts
- `lecture_02_figure_02.png`: Train-frame sketch with the primed origin marked inside.
- `lecture_02_figure_03.png`: Stacked Lorentz transformations for primed and double-primed frames.
- `lecture_02_figure_04.png`: Kiddie-car origin and the composed motion inside the train.

## Uncertainties
- In `lecture_02_figure_02.png`, the exact notation written near the highlighted event is not fully legible; it appears to mark a primed event or primed coordinate condition, but the full symbol string should be reconstructed from transcript context rather than trusted solely from the image.
- In `lecture_02_figure_02.png`, the lower red `x` mark is visible, but whether it is meant simply as the stationary coordinate location or as part of a longer label is not completely clear.
- In `lecture_02_figure_03.png`, the board uses uppercase `X` in some places and lowercase `x` in others. The cleaned notes should standardize this notation.
- In `lecture_02_figure_04.png`, the double-prime label beside the car is partly obscured by Susskind’s hand and body; the identification of the point as the double-primed origin is strongly supported by the subtitle and transcript, but the exact handwritten label is only partially readable in the image.
- In `lecture_02_figure_04.png`, only part of the left-board algebra is visible. The displayed relation involving \(\dfrac{u+v}{1+uv}t\) should be reconstructed from the transcript rather than transcribed exclusively from the cropped board edge.