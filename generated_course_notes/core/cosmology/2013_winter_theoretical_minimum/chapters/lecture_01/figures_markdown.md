# Figure Notes
## Image Inventory
- `lecture_01_figure_02.png`: Leonard Susskind stands at the left edge of a mostly blank whiteboard. Near the center is a source point marked with an uppercase `M`, and to the right is a point with a rightward arrow above the kinetic-energy term. The only substantial formula visible is the kinetic term beneath the arrow.
- `lecture_01_figure_03.png`: A wide board view combining two parts of the lecture. On the left and center are boxed cosmology equations for \(\ddot a/a\), with residual derivation lines and a volume formula across the top. On the right is the Newtonian analogy: a circle, a point on a horizontal line with arrows, and an inverse-square force law.
- `lecture_01_figure_04.png`: A tighter crop of the same Newtonian-comparison board. The right side is emphasized: the inverse-square force law, a circle, and a radial point-on-line sketch are clear, while parts of the boxed cosmology equations remain visible at left and top.
- `lecture_01_figure_05.png`: The board now shows the Newtonian energy expression for the cosmology analogy. Above are the source mass `M` and the test particle `m`; below is a kinetic term followed by the beginning of the gravitational potential-energy term. Susskind’s pointing gesture tracks the potential-energy part.
- `lecture_01_figure_06.png`: A clean algebra board centered on the matter-dominated Friedmann scaling. The upper line shows \((\dot a/a)^2\) with constants and an \(a^{-3}\) dependence; the lower line simplifies the same relation to a normalized \(1/a^3\) form. A partial \(\rho\)-definition is visible at the far right.

## Blackboard Equations
- `lecture_01_figure_02.png`: \(M\) [visible]; \(\frac{1}{2} m v^2\) [visible].
- `lecture_01_figure_03.png`: \(\frac{\ddot a}{a}=-\frac{4\pi}{3}G\rho\) [visible]; \(\frac{\ddot a}{a}=-\frac{4\pi G \nu}{3a^3}\) [visible]; \(\ddot x=-\frac{MG}{x^2}\) [visible]; \(\mathrm{volume}=\frac{4}{3}\pi a^3 R^3\) [partially visible].
- `lecture_01_figure_04.png`: \(-\frac{MG}{D^2}=\ddot a(t)R\) [partially visible]; \(\frac{\ddot a}{a}=-\frac{4\pi}{3}G\rho\) [partially visible]; \(\ddot x=-\frac{MG}{x^2}\) [visible].
- `lecture_01_figure_05.png`: \(\frac{1}{2}m\dot a^{\,2}R^2\) [visible]; \(-mMG\) [visible]; \(\frac{1}{2}m\dot a^{\,2}R^2-\frac{mMG}{aR}\) [standard reconstruction].
- `lecture_01_figure_06.png`: \(\left(\frac{\dot a}{a}\right)^2=\frac{8\pi G\nu}{3a^3}\) [visible]; \(\left(\frac{\dot a}{a}\right)^2=\frac{1}{a^3}\) [visible]; \(\rho=\frac{\nu}{a^3}\) [partially visible].

## Diagram And Layout Reading
- `lecture_01_figure_02.png`: The board is intentionally sparse. The layout isolates the source mass on the left and the moving particle on the right, with only the kinetic term written. This emptiness matters: the lecture is verbally asking for the missing potential-energy term, and the board has not yet supplied it.
- `lecture_01_figure_03.png`: The board is organized as a left-to-right bridge from cosmology to Newtonian mechanics. The left and center boxes summarize the acceleration equations for the scale factor; the right side shifts to a one-particle gravitational picture with a circle and a horizontal line that functions as an unlabeled radial axis.
- `lecture_01_figure_04.png`: This is the cleaner witness for the Newtonian side of the argument. The circle and the point on a horizontal line with left-right arrows give a minimal radial sketch. The force law is written above it, while the boxed cosmology equations remain in the background as documentary context.
- `lecture_01_figure_05.png`: The mass labels and energy terms are stacked as a direct translation of the Newtonian particle problem into cosmological variables. The layout strongly suggests: source mass at center, test mass at distance \(aR\), kinetic term first, then gravitational potential term.
- `lecture_01_figure_06.png`: This board is purely algebraic. The upper line is the constant-bearing Friedmann relation; the lower line is the stripped-down matter-dominated scaling. The two-line layout is exactly what supports the spoken claim that the right-hand side stays positive and therefore the expansion rate does not cross through zero.

## TeX Reconstruction Plan
- `lecture_01_figure_02.png` should remain visible. It is the cleanest documentary witness for the kinetic-energy setup. It should be paired nearby with a typeset displayed equation for the total Newtonian energy, since the screenshot itself only shows the kinetic piece.
- `lecture_01_figure_03.png` should remain visible. It is the best broad board-layout witness joining the boxed cosmology equations to the Newtonian escape/force analogy. Nearby, typeset the boxed equations cleanly and, if desired, add a small TikZ redraw of the circle-plus-radial-particle sketch.
- `lecture_01_figure_04.png` should remain visible as the tighter Newtonian companion. It should sit near the cleaned equation \(\ddot x=-MG/x^2\) and, if space allows, a minimal TikZ sketch of a point mass, a test particle, and an unlabeled radial line.
- `lecture_01_figure_05.png` should remain visible. It is the key board witness for the transition from the Newtonian particle problem to the cosmological energy equation. It should be paired with a cleaned displayed equation of the form \(E=\frac12 m\dot a^{\,2}R^2-\frac{mMG}{aR}\), with a brief prose note that the denominator is reconstructed from the transcript and adjacent board context.
- `lecture_01_figure_06.png` should remain visible. It should be paired with clean displayed equations for \(\left(\frac{\dot a}{a}\right)^2=\frac{8\pi G}{3}\rho\) and \(\rho=\nu/a^3\), then the simplified matter-dominated form \(\left(\frac{\dot a}{a}\right)^2\propto a^{-3}\). No TikZ is needed here.

## Caption Drafts
- `lecture_01_figure_02.png`: Moving test mass and kinetic term
- `lecture_01_figure_03.png`: Boxed cosmology equations with Newtonian escape sketch
- `lecture_01_figure_04.png`: Inverse-square force law and radial particle sketch
- `lecture_01_figure_05.png`: Kinetic term with emerging potential energy
- `lecture_01_figure_06.png`: Matter-dominated Friedmann scaling

## Uncertainties
- `lecture_01_figure_02.png`: The subtitle asks about potential energy, but the screenshot itself does not yet show it. The figure should therefore be described as a kinetic-energy setup, not as evidence for the full energy formula.
- `lecture_01_figure_03.png`: The upper derivation line is cropped and partly obscured. The central boxed equation seems to involve \(\nu/a^3\), but the exact chalk placement is slightly rough. The right-side circle and horizontal sketch are unlabeled, so their interpretation comes from the lecture context rather than explicit board labels.
- `lecture_01_figure_04.png`: The residual top equation uses a distance symbol that could be read as \(D\) or \(d\). The boxed cosmology equation at left is only partly preserved in this crop, so it should be used as context rather than as the primary source for its full formula.
- `lecture_01_figure_05.png`: The visible potential-energy term is incomplete in the frame. Only \(-mMG\) is securely on the board; the denominator corresponding to the distance has not yet been written or is cropped away. The full \(-mMG/(aR)\) form therefore requires cautious transcript-backed completion.
- `lecture_01_figure_06.png`: The upper equation’s constants are arranged informally on the board, so the printed form should be normalized in standard notation. The far-right density formula is cropped, and only part of the \(\rho=\nu/a^3\) relation is visible.