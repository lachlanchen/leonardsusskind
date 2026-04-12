# Figure Notes
## Image Inventory
- `lecture_01_figure_02.png`: Susskind stands in front of a two-part blackboard comparison. The left half is labeled `\(\alpha \ll 1\)` and contains a compact central scribble with several arrows or curved rays pointing outward and upward. The right half is labeled `\(\alpha \gg 1\)` and contains a tall, narrow vertical sketch with a small irregular feature near its lower part. The board is clearly organized as a weak-versus-strong coupling contrast.
- `lecture_01_figure_03.png`: Susskind is drawing a long horizontal asymmetric outline across the board. The shape has a beveled or slanted left end, a long upper and lower boundary, and a rounded termination at the far right. The middle is partially blocked by his body, but the intended asymmetry of the profile is visually clear.
- `lecture_01_figure_04.png`: Susskind stands in front of a more developed geometric sketch. On the left is a cylinder- or rolled-surface-like figure with an elliptical top and vertical side. A long upper contour runs across the board, and a slanted line extends from the central region toward the upper right. The image records the moment when he explicitly calls the construction “a geometrical picture.”
- `lecture_01_figure_06.png`: A later standing shot with the same cylindrical geometry still on the board. The left cylindrical form is still visible, and two long horizontal guide lines run across the upper board. No new explicit labels or point markers are legible, but the image preserves the layout of the reference picture used during the discussion of “specially symmetric points.”

## Blackboard Equations
- `lecture_01_figure_02.png` [visible]: \(\alpha \ll 1\)
- `lecture_01_figure_02.png` [visible]: \(\alpha \gg 1\)
- `lecture_01_figure_02.png` [standard reconstruction]: the board is presenting a side-by-side contrast of two coupling regimes rather than a full written equation.
- `lecture_01_figure_03.png` [visible]: no legible algebraic notation; this figure is diagrammatic.
- `lecture_01_figure_04.png` [visible]: no legible algebraic notation; this figure is diagrammatic.
- `lecture_01_figure_06.png` [visible]: no legible algebraic notation; this figure is diagrammatic.
- `lecture_01_figure_06.png` [standard reconstruction]: if the notes later formalize the “symmetric point” discussed in the transcript, it would be a transcript-backed completion such as equality of the two compactification scales, not a board-visible inscription.

## Diagram And Layout Reading
- `lecture_01_figure_02.png`: The board is laid out as a left-right comparison. The left sketch is compact and roughly point-centered, with several arrows or rays emerging from a small core; the right sketch is elongated and vertical. The visual rhetoric matches the lecture’s contrast between a simple object at weak coupling and a spread-out, heavy, structured object at strong coupling.
- `lecture_01_figure_02.png`: The central lecturer occlusion hides some lower chalk, but the regime labels and the basic contrast of “compact versus extended” remain readable enough to support note writing.
- `lecture_01_figure_03.png`: The asymmetrical horizontal shape spans nearly the whole board. Its most important visual feature is not a formula but the deliberate difference between the two compact directions: the left end is sharply beveled while the right end is rounded, so the figure should be read as an intentionally non-symmetric compactification cell or profile.
- `lecture_01_figure_04.png`: The left-hand geometry reads as a cylindrical or rolled compact direction attached to a more extended surrounding picture. The long upper contour and the slanted rightward line suggest that the object is embedded in or compared with a larger geometric setting, not drawn as an isolated cylinder.
- `lecture_01_figure_04.png`: The board organization matters: a localized cylinder-like form on the left, an oblique continuation toward the right, and empty surrounding board space that makes the sketch function as a conceptual geometric aid rather than as algebra.
- `lecture_01_figure_06.png`: This later frame uses the same geometry as a standing reference picture. The upper horizontal guide lines and the left cylindrical form are what matter; there are no newly legible point labels, so the image supports the existence of a previously drawn aspect-ratio picture more than it supports a new explicit marking of the “specially symmetric” case.
- `lecture_01_figure_06.png`: Relative to `lecture_01_figure_04.png`, this image is valuable less for new drawing content than for documenting that the same compactification geometry remains the active reference during the later Q&A about symmetry and aspect ratio.

## TeX Reconstruction Plan
- `lecture_01_figure_02.png` should remain visible in the chapter. Pair it with a nearby clean typeset contrast
  \[
  \alpha \ll 1
  \qquad\text{versus}\qquad
  \alpha \gg 1
  \]
  and a small TikZ redraw of the two regimes. The redraw should stay schematic: a compact central object with outward arrows on the weak-coupling side, and an elongated vertical profile on the strong-coupling side. Do not over-derive equations from this board alone.
- `lecture_01_figure_03.png` should remain visible and should be paired with a TikZ redraw rather than with displayed equations. The redraw should preserve the asymmetric left-to-right profile: beveled left face, long stretched body, rounded right end. This is a shape argument, not an algebra argument.
- `lecture_01_figure_04.png` should remain visible and should be paired with a cleaned geometric TikZ sketch. The redraw should include the left cylindrical or rolled compact piece and the slanted continuation toward the right. If the surrounding text discusses compactification or geometric identification, the prose should supply that interpretation; the image itself does not fully spell it out.
- `lecture_01_figure_06.png` should remain visible if the chapter wants explicit visual evidence that the same geometry is still being referenced during the “specially symmetric points” discussion. It does not need a wholly new standalone diagram; a better approach is to reuse the earlier TikZ geometry from `lecture_01_figure_04.png` and, if needed, add a cautious transcript-backed annotation nearby explaining that the symmetric case corresponds to an equal-aspect configuration. That equality should be presented as interpretation from the lecture discussion, not as board transcription.
- Across all four figures, the original screenshots should stay in the main body, while the legible LaTeX and TikZ serve as cleaned companions rather than replacements.

## Caption Drafts
- `lecture_01_figure_02.png`: Small- and large-\(\alpha\) comparison sketches.
- `lecture_01_figure_03.png`: Asymmetric compactification profile.
- `lecture_01_figure_04.png`: Geometrical cylinder and slanted extension sketch.
- `lecture_01_figure_06.png`: Later reference frame for the compactification geometry.

## Uncertainties
- `lecture_01_figure_02.png`: The lower part of the right-hand sketch is partly hidden by Susskind’s body, so the exact nature of the small lower feature is unclear. It should not be overinterpreted beyond “a marked structure on a vertical profile.”
- `lecture_01_figure_02.png`: The left-hand arrows may be field lines, rays, or a generic “spread” sketch. The image strongly supports a compact-versus-extended contrast, but not a uniquely determined physics drawing without help from the transcript.
- `lecture_01_figure_03.png`: The middle of the long profile is occluded, and the lower boundary line is not continuously visible. The completed shape should therefore be reconstructed cautiously from the visible endpoints and the lecture’s statement that it is being drawn asymmetrically.
- `lecture_01_figure_03.png`: The left end may be read as a beveled face, a folded edge, or a simple perspective cue. A redraw should preserve the asymmetry without asserting unnecessary three-dimensional detail.
- `lecture_01_figure_04.png`: The left object looks cylinder-like or rolled, but the image alone does not determine whether Susskind intends a literal cylinder, a compactified circular direction, or a cut-open representation of one. The transcript should supply that interpretation.
- `lecture_01_figure_04.png`: The slanted rightward line and the long upper contour are clear, but the precise way they connect to the left-hand cylinder is partly hidden by the lecturer and should be redrawn schematically.
- `lecture_01_figure_06.png`: No explicit “special point” markers or aspect-ratio labels are legible in the screenshot itself. Any note that introduces a symmetric-point condition must come from the transcript discussion rather than from the chalk that is visible here.
- `lecture_01_figure_06.png`: Because it reuses the earlier geometry, it risks redundancy if the chapter already includes `lecture_01_figure_04.png`. Its best use is as corroborating evidence for the later Q&A, not as a wholly independent mathematical figure.