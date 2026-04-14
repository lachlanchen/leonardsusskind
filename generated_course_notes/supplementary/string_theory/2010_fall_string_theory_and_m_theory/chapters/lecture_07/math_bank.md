# Math Bank
## Core Equations
- \(S_{\mathrm{NR}}=\int dt\,\frac12 \dot{x}^{\,2}\) [transcript-backed]
- \(X^\mu=X^\mu(\tau)\) with \(\tau\) a parameter along the relativistic trajectory, taken as proper time in the lecture setup [transcript-backed]
- \(S_{\mathrm{rel}}\sim \int d\tau\,\frac{dX^\mu}{d\tau}\frac{dX_\mu}{d\tau}\) [transcript-backed]
- \(K(1\to 2)=\int \mathcal{D}x\,e^{iS[x]}\) [standard reconstruction]
- \(\exp\!\left(i\int_{t_1}^{t_2}dt\,\frac12 \dot{x}^{\,2}\right)\) [transcript-backed]
- \(\tau=\alpha s\) [transcript-backed]
- \(d\tau=\alpha\,ds\) [transcript-backed]
- \(\frac{dX}{d\tau}=\frac{1}{\alpha}\frac{dX}{ds}\) [transcript-backed]
- \(\int d\tau\,\Bigl(\frac{dX}{d\tau}\Bigr)^2=\frac{1}{\alpha}\int ds\,\Bigl(\frac{dX}{ds}\Bigr)^2\) [transcript-backed]
- choosing \(\alpha=-i\) gives a Euclidean weight of the form \(\exp\!\left(-\frac12\int ds\,\bigl(\frac{dX}{ds}\bigr)^2\right)\) [standard reconstruction]
- \(X^\mu=X^\mu(\sigma,\tau)\) [transcript-backed]
- \(\left(\frac{\partial X^\mu}{\partial \tau}\right)^2\) [visible]
- \(-\left(\cdots\right)^2\) [visible]
- \(\left(\frac{\partial X^\mu}{\partial \tau}\right)^2-\left(\frac{\partial X^\mu}{\partial \sigma}\right)^2\) [standard reconstruction]
- \(S_{\text{ws}}\sim \int d\tau\,d\sigma\left[\left(\partial_\tau X^\mu\right)^2-\left(\partial_\sigma X^\mu\right)^2\right]\) [standard reconstruction]
- \(\int \mathcal{D}X\,e^{iS_{\text{ws}}[X]}\) as the string path integral over surfaces [standard reconstruction]
- after Euclideanization, a positive-definite worldsheet weight of the form \(\exp\!\left(-\int d\tau\,d\sigma\left[(\partial_\tau X^\mu)^2+(\partial_\sigma X^\mu)^2\right]\right)\) [standard reconstruction]
- \(\partial_\tau^2 X-\partial_\sigma^2 X=0\) [transcript-backed]
- \(\frac{\partial^2 X}{\partial \tau^2}+\frac{\partial^2 X}{\partial \sigma^2}=0\) [visible]
- \([X(3)-X(2)]-[X(2)-X(1)]\) [partially visible]
- \(X(3)+X(1)-2X(2)\) [visible]
- \(\partial_\tau^2 X\leadsto X(1)+X(3)-2X(5)\) in the discrete two-dimensional picture [transcript-backed]
- \(\partial_\sigma^2 X\leadsto X(2)+X(4)-2X(5)\) in the discrete two-dimensional picture [transcript-backed]
- \(X(1)+X(2)+X(3)+X(4)-4X(5)=0\) [transcript-backed]
- \(X(5)=\frac14\bigl[X(1)+X(2)+X(3)+X(4)\bigr]\) [standard reconstruction]
- conformal transformations preserve infinitesimal squares, equivalently preserve angles [transcript-backed]
- analytic maps of a complex variable generate angle-preserving coordinate changes [transcript-backed]
- \(s=(k_1+k_2)^2\) [standard reconstruction]
- \(t=(k_1+k_3)^2\) [standard reconstruction]
- the four-point amplitude is symmetric under \(s\leftrightarrow t\) [transcript-backed]

## Definitions And Objects
- `Trajectory`: the particle history, described nonrelativistically by \(x(t)\) and relativistically by \(X^\mu(\tau)\).
- `Proper time \(\tau\)`: the scalar parameter along a relativistic particle trajectory in the opening setup.
- `Action`: the functional minimized classically and exponentiated in quantum mechanics.
- `Propagator`: the relativistic-particle amplitude to go from one spacetime point to another.
- `Worldsheet`: the two-dimensional history of a string; ribbon for open strings, tube for closed strings.
- `Worldsheet coordinates`: \((\sigma,\tau)\), both auxiliary parameters labeling the sheet rather than physical spacetime coordinates.
- `Embedding fields`: \(X^\mu(\sigma,\tau)\), the spacetime coordinates of the worldsheet point labeled by \((\sigma,\tau)\).
- `String path integral`: sum/integral over all surfaces interpolating between specified initial and final string configurations.
- `Topology change / holes`: worldsheet analog of higher-loop Feynman-diagram contributions.
- `Euclideanized worldsheet`: the \(\tau\to \pm i\tau\) version in which the oscillatory weight becomes exponentially damped.
- `Laplace equation on the worldsheet`: the Euclidean equation of motion for \(X^\mu\) after the Wick-rotation trick.
- `Discrete second derivative`: difference of first differences on a lattice of nearby points.
- `Discrete Laplacian`: sum of nearest-neighbor values minus four times the center in the square-lattice picture.
- `Conformal mapping`: coordinate transformation on the \((\sigma,\tau)\)-plane that preserves angles, equivalently infinitesimal squares up to local scale.
- `Band-aid / slit strip`: Susskind’s worldsheet picture of string splitting and joining from the previous lecture.
- `Disc picture`: conformally equivalent representation of the four-point open-string process.
- `Exceptional / special boundary points`: the four boundary points carrying the data of incoming and outgoing string states; later described via vertex operators.
- `Injection points`: Susskind’s temporary name for those special boundary points when discussing the one-parameter integral.
- `Channel duality`: the symmetry relating the direct \(s\)-channel and crossed \(t\)-channel interpretations of the same worldsheet amplitude.

## Derivation Steps
1. `Particle action to particle path integral`
1. Start with the classical free-particle action \(S_{\mathrm{NR}}=\int dt\,\frac12\dot{x}^{\,2}\).
2. Reinterpret the question: not which trajectory minimizes \(S\), but what amplitude connects fixed endpoints.
3. Attach the phase \(e^{iS[x]}\) to each trajectory.
4. Sum/integrate over all trajectories \(x(t)\) between the endpoints.

2. `Why Wick rotation helps for particles`
1. Observe that \(|e^{iS}|=1\), so wildly varying trajectories are not suppressed by magnitude.
2. Reparameterize \(\tau=\alpha s\).
3. Compute \(d\tau=\alpha ds\) and \(dX/d\tau=(1/\alpha)\,dX/ds\).
4. Rewrite the action with an overall factor \(1/\alpha\).
5. Choose \(\alpha=-i\) so that the phase \(iS\) turns into a negative real Euclidean action.
6. Conclude that large derivatives give a large positive action and hence exponential suppression.

3. `Particle picture to string picture`
1. Replace a point particle by a string.
2. Replace a worldline by a worldsheet.
3. Replace \(X^\mu(\tau)\) by \(X^\mu(\sigma,\tau)\).
4. Replace the one-dimensional action by a two-dimensional action with \(\tau\)- and \(\sigma\)-derivative terms.
5. Exponentiate the worldsheet action and sum over all interpolating surfaces.

4. `Worldsheet Wick rotation`
1. Start from the Lorentzian-sign worldsheet action density \((\partial_\tau X^\mu)^2-(\partial_\sigma X^\mu)^2\).
2. Change the worldsheet time variable by \(\tau\to \pm i\tau\).
3. Track the sign changes from \(d\tau\) and from the \(\tau\)-derivatives.
4. Choose the sign so that both derivative terms contribute positively inside the Euclidean action.
5. Pull the remaining minus sign into the exponential weight \(e^{-S_E}\).
6. Conclude that wildly fluctuating or stretched surfaces are suppressed.

5. `Action to equation of motion`
1. Note that an action quadratic in first derivatives produces an equation of motion with second derivatives.
2. Compare with the ordinary wave equation \(\partial_\tau^2 X-\partial_\sigma^2 X=0\).
3. After Euclideanization, replace the minus sign by a plus sign.
4. Identify the resulting equation as the two-dimensional Laplace equation.

6. `Discrete one-dimensional second derivative`
1. Discretize a line into neighboring points \(1,2,3\).
2. Approximate the first derivative by a difference such as \(X(3)-X(2)\), ignoring \(\epsilon\) for the conceptual argument.
3. Define the second derivative as a difference of first differences:
   \([X(3)-X(2)]-[X(2)-X(1)]\).
4. Simplify to \(X(3)+X(1)-2X(2)\).
5. Read this as “outer values minus twice the center.”

7. `Discrete Laplace equation on a square`
1. Discretize the \((\sigma,\tau)\)-plane near a point into a small square with neighbors \(1,2,3,4\) and center \(5\).
2. Write the \(\tau\)-second derivative as \(X(1)+X(3)-2X(5)\).
3. Write the \(\sigma\)-second derivative as \(X(2)+X(4)-2X(5)\).
4. Add them because the Euclidean equation is \(\partial_\tau^2 X+\partial_\sigma^2 X=0\).
5. Obtain \(X(1)+X(2)+X(3)+X(4)-4X(5)=0\).
6. Rewrite as \(X(5)=\frac14[X(1)+X(2)+X(3)+X(4)]\).
7. Interpret the Laplace equation as the local average-value property.

8. `Average-value property to conformal invariance`
1. Express the Laplace equation geometrically: at the center of an infinitesimal square, the field equals the average of the corner values.
2. Note that rotation of the square does not change the statement.
3. Ask which coordinate changes preserve this geometric form.
4. Answer: transformations that take infinitesimal squares to infinitesimal squares.
5. Reformulate this as angle preservation.
6. Identify the resulting class as conformal transformations.

9. `Band-aid worldsheet to disc modulus`
1. Recall the slit-strip worldsheet for string joining and splitting.
2. Use conformal invariance to map that region to a disc.
3. Carry the four asymptotic external-string data to four special boundary points on the disc.
4. Use residual conformal freedom to move boundary points around.
5. Conclude that only one real parameter remains after quotienting by conformal transformations.
6. Interpret that parameter as the counterpart of the joining-splitting time interval.
7. Integrate over that one-parameter family to obtain the four-point amplitude / beta-function structure.

10. `One modulus to channel duality`
1. Examine one extreme of the modulus where two incoming points become adjacent.
2. Interpret it as the long-lived direct-channel intermediate string.
3. Examine the opposite extreme where a different pair becomes adjacent.
4. Interpret it as the crossed-channel picture.
5. Since both limits arise from one integral over one modulus, the amplitude is symmetric under interchange of the channel interpretations.
6. State this as \(s\)-\(t\) channel duality.

## Notation Choices
- Use \(X^\mu\) for spacetime embedding coordinates throughout; do not switch between \(x^\mu\) and \(X^\mu\) unless quoting the lecture’s earlier particle notation.
- Use lowercase \(x(t)\) only in the introductory nonrelativistic particle discussion.
- Use \(\tau\) for the worldline/worldsheet parameter that plays the role of internal time.
- Use \(\sigma\) for the internal spatial coordinate along the string.
- Reserve \(S\) for action in the notes, even though the lecture verbally collides several uses of “s”.
- When discussing the Wick-rotated auxiliary variable for the particle, use \(s\) only locally and explicitly warn that it is not the action and not the Mandelstam variable.
- When discussing scattering, reserve \(s\) and \(t\) for Mandelstam invariants only.
- Write derivatives as \(\partial_\tau X^\mu\), \(\partial_\sigma X^\mu\), \(\partial_\tau^2 X\), \(\partial_\sigma^2 X\).
- In the discrete finite-difference section, keep the lecture’s point labels \(1,2,3,4,5\) and function values \(X(1),\dots,X(5)\).
- Treat the board’s plus-sign PDE as Euclidean/Laplace-form notation, not as the Lorentzian wave equation.
- Use “worldsheet” as the default term; mention “ribbon” and “tube” only when matching the lecture’s motivating pictures.
- Use “vertex operators” only as a forward reference attached to the special boundary points; do not develop their formalism here.
- Use “conformal transformation” in the lecture’s geometric sense: angle-preserving, infinitesimal-square-preserving, local rescaling allowed.

## Uncertain Mathematics
- The full worldsheet action in the lecture is verbally and visually incomplete; keep any overall normalization, tension factor, \(1/2\), or \(2\pi\alpha'\) factor out unless supplied from surrounding course conventions.
- The Wick-rotation sign bookkeeping is unstable live on the board. Present one consistent Euclidean convention in the final notes and mention that the lecture sorted the sign choice in real time.
- The board frame for the string action only securely shows the derivative structure and the minus sign; it does not fix integration limits or coefficients.
- The handwritten PDE in the frames clearly has a plus sign, but the transcript also explicitly mentions the Lorentzian wave equation for comparison. The final notes must separate these two contexts cleanly.
- The discrete line in the frames is unlabeled as \(\tau\) or \(\sigma\); the assignment comes from the spoken derivation, not directly from the image.
- The right-hand finite-difference expression in `lecture_07_figure_04.png` is truncated; the second bracket should be identified as a cautious completion from the algebraic logic.
- The late Mandelstam discussion in the transcript is partially garbled. The robust content is:
  - \(s\) is the direct / center-of-mass channel.
  - \(t\) is the crossed channel.
  - the integral is symmetric under their interchange.
- The exact formula Susskind half-recalls for \(t\) in terms of scattering angle should not be stated confidently from this lecture alone.
- The disc with four insertion points is transcript-backed but not frame-backed; any explicit placement of those points in later notes should be presented as a cleaned reconstruction.
- The Nambu-Goto / Polyakov / Liouville remarks are naming/contextual asides, not part of the lecture’s main derived mathematical chain.