# Figure Notes
## Image Inventory
- `lecture_07_figure_02.png`: Susskind stands at the right edge while the board preserves two inequality lines on the upper panel. The upper line is cropped at the top but clearly shows a ratio involving \(h\nu\) over \(kT\) compared with \(1\). The second line is much clearer and reads as \(hc/(kT)>\lambda\). On the lower panel, the left side carries a `RHS:` label and some faint dimensional-analysis remnants, with additional washed-out symbols across the middle.
- `lecture_07_figure_03.png`: Susskind stands facing the board. The upper-right board clearly shows the large ratio of photon number to electron number, \(\frac{N_\gamma}{N_e}=10^8\). Near the center-left is the beginning of a Boltzmann-factor expression: a large `e`, a superscript minus sign, and a newly introduced \(\epsilon\). The lower board still carries a partial axis-and-curve sketch from the surrounding discussion.

## Blackboard Equations
- `lecture_07_figure_02.png`: \(\frac{h\nu}{kT}>1\) [partially visible]
- `lecture_07_figure_02.png`: \(\frac{hc}{kT}>\lambda\) [visible]
- `lecture_07_figure_02.png`: \(E=h\nu\) [standard reconstruction]
- `lecture_07_figure_02.png`: \(\mathrm{RHS}:\) [visible]

- `lecture_07_figure_03.png`: \(\frac{N_\gamma}{N_e}=10^8\) [visible]
- `lecture_07_figure_03.png`: \(e^{-\epsilon}\) [partially visible]
- `lecture_07_figure_03.png`: \(\epsilon\) [visible]
- `lecture_07_figure_03.png`: \(e^{-\epsilon/(kT)}\) [standard reconstruction]

## Diagram And Layout Reading
- `lecture_07_figure_02.png` is mostly an equation board rather than a diagram board. The useful visual structure is vertical: the upper board contains the main thermal-wavelength inequalities, while the lower board preserves the tail end of the earlier dimensional-analysis check. That split matters because it shows the lecture moving from units and consistency checks to the physically meaningful crossover condition.
- `lecture_07_figure_03.png` has a more layered board organization. The upper-right ratio \(\frac{N_\gamma}{N_e}=10^8\) gives the large abundance input. The center-left `e^{-\,\epsilon...}` start marks the transition to the Boltzmann tail argument. The lower board retains only a residual graph-like sketch with a horizontal baseline, a vertical axis, and a sloping curve; it is useful as context for the ongoing blackbody/distribution discussion, but not complete enough to serve as an independent diagram.

## TeX Reconstruction Plan
- `lecture_07_figure_02.png` must remain visible in the notes. It should be paired with a clean displayed reconstruction of
  \[
  \frac{h\nu}{kT}\gtrsim 1,
  \qquad
  \frac{hc}{kT}\gtrsim \lambda,
  \]
  together with a short prose line explaining that this is the board version of the quantum crossover or thermal-wavelength criterion.
- `lecture_07_figure_03.png` must remain visible in the notes. It should be paired with a clean displayed reconstruction of
  \[
  \frac{N_\gamma}{N_e}\sim 10^8,
  \qquad
  P(\epsilon)\propto e^{-\epsilon/(kT)},
  \]
  or equivalent prose-plus-equation language. The screenshot is important because it preserves both the huge photon-to-electron ratio and the moment when \(\epsilon\) is introduced as the photon energy.
- No TikZ redraw is required for either figure. The lower-board graph residue in `lecture_07_figure_03.png` is too incomplete to justify a standalone redraw; it is better treated as contextual board evidence only.

## Caption Drafts
- `lecture_07_figure_02.png`: Thermal-wavelength inequality on the board.
- `lecture_07_figure_03.png`: Photon-energy notation and the photon-to-electron ratio.

## Uncertainties
- In `lecture_07_figure_02.png`, the uppermost line is clipped by the frame edge, so \(\frac{h\nu}{kT}>1\) is readable but not perfectly clean. The lower-board `RHS:` region contains additional dimensional symbols, but they are too faint and incomplete to transcribe confidently.
- In `lecture_07_figure_03.png`, the subscript in the numerator of \(\frac{N_\gamma}{N_e}\) is best read as \(\gamma\) from the lecture context, though the handwriting is not typographically crisp. The center-left expression visibly begins \(e^{-\,\epsilon}\), but the denominator \(kT\) is not yet on the board in the frame and must therefore be supplied only as a cautious reconstruction from the surrounding lecture. The lower-board graph is partial and should not be over-read.