# Math Bank
## Core Equations
- \(t \approx \dfrac{h}{c}\), \(v \approx gt \approx \dfrac{gh}{c}\), so \(\dfrac{\Delta \nu}{\nu}\sim \dfrac{gh}{c^2}\) for the assigned elevator estimate; reverse sign for the upward beam. [standard reconstruction]
- \(\Delta \nu_{\text{grav}}+\Delta \nu_{\text{Doppler}}=0\) in a freely falling elevator, up to tidal effects. [transcript-backed]
- \(d\phi=\dfrac{\partial \phi}{\partial x^m}\,dx^m\). [transcript-backed]
- \(\dfrac{\partial \phi}{\partial y^n}=\dfrac{\partial \phi}{\partial x^m}\dfrac{\partial x^m}{\partial y^n}\). [transcript-backed]
- \(\phi(y)=\phi(x)\). [visible]
- \(dy^n=\dfrac{\partial y^n}{\partial x^m}\,dx^m\). [transcript-backed]
- \(V^n_{(y)}=\dfrac{\partial y^n}{\partial x^m}V^m_{(x)}\). [transcript-backed]
- \(A^{(y)}_{n}=\dfrac{\partial x^m}{\partial y^n}A^{(x)}_{m}\). [transcript-backed]
- \(T^{(y)}_{mn}=\dfrac{\partial x^r}{\partial y^m}\dfrac{\partial x^s}{\partial y^n}T^{(x)}_{rs}\). [visible]
- \(\delta_{mn}=\begin{cases}1,&m=n\\0,&m\neq n\end{cases}\). [transcript-backed]
- \(ds^2=\delta_{mn}\,dx^m dx^n\). [visible]
- \(dx^m=\dfrac{\partial x^m}{\partial y^r}\,dy^r\). [visible]
- \(ds^2=g_{mn}(x)\,dx^m dx^n=g_{rs}(y)\,dy^r dy^s\). [transcript-backed]
- \(g^{(y)}_{rs}=g^{(x)}_{mn}\dfrac{\partial x^m}{\partial y^r}\dfrac{\partial x^n}{\partial y^s}\). [standard reconstruction]
- \(x=r\cos\theta,\qquad y=r\sin\theta\). [transcript-backed]
- \(dx=\cos\theta\,dr-r\sin\theta\,d\theta,\qquad dy=\sin\theta\,dr+r\cos\theta\,d\theta\). [transcript-backed]
- \(ds^2=dr^2+r^2d\theta^2\). [transcript-backed]
- \(g_{rr}=1,\qquad g_{r\theta}=0,\qquad g_{\theta\theta}=r^2\). [transcript-backed]
- \(ds^2=d\phi^2+\sin^2\phi\,d\theta^2\) for the unit sphere. [standard reconstruction]

## Definitions And Objects
- Scalar: a tensor of rank \(0\); no directional components; invariant under coordinate change.
- Contravariant vector: an object with one upper index whose components transform with \(\partial y/\partial x\); the infinitesimal displacement \(dx^m\) is the archetype.
- Covariant vector: an object with one lower index whose components transform with \(\partial x/\partial y\); the gradient \(\partial \phi/\partial x^m\) is the archetype.
- Rank-two tensor: an object with two indices; in the lecture it is first motivated by products of vectors and then generalized by transformation law.
- Metric tensor \(g_{mn}\): the coefficient array in the line element \(ds^2=g_{mn}dx^m dx^n\); a covariant rank-two tensor.
- Kronecker delta \(\delta_{mn}\): the Cartesian metric in flat space.
- Flat space: a space for which some coordinate system makes \(g_{mn}=\delta_{mn}\).
- Curved space: a space with an obstruction to such a flattening.
- Dummy index: a repeated summed index; its letter is arbitrary as long as it does not collide with a free index.
- \(d\) versus \(\Delta\): \(d\) is first-order infinitesimal change; \(\Delta\) would denote finite difference.

## Derivation Steps
Approximate elevator redshift estimate
1. Take elevator height \(h\) and light travel time \(t\approx h/c\).
2. During that time, the detector acquires speed \(v\approx gt\approx gh/c\).
3. Apply the small-velocity Doppler formula.
4. Conclude a fractional frequency shift of order \(gh/c^2\).
5. Mark this as an assigned approximation, not as a fully blackboard-derived exact result.

Total differential of a scalar
1. Start with a scalar field \(\phi(x)\) and an infinitesimal displacement \(dx^m\).
2. Resolve the change in \(\phi\) into contributions from each coordinate direction.
3. Sum those directional contributions.
4. Write \(d\phi=\dfrac{\partial \phi}{\partial x^m}dx^m\).

Chain rule under coordinate change
1. Introduce new coordinates \(y^n=y^n(x)\).
2. Ask for the change of \(\phi\) with respect to a chosen \(y^n\).
3. Differentiate \(\phi\) with respect to the \(x^m\).
4. Multiply by the response of \(x^m\) to \(y^n\).
5. Sum over \(m\) to obtain \(\dfrac{\partial \phi}{\partial y^n}=\dfrac{\partial \phi}{\partial x^m}\dfrac{\partial x^m}{\partial y^n}\).

Contravariant-vector transformation from displacement
1. Treat \(y^n\) itself as the scalar whose change is being computed.
2. Apply the total-differential rule to \(y^n(x)\).
3. Obtain \(dy^n=\dfrac{\partial y^n}{\partial x^m}dx^m\).
4. Abstract this into the definition of a contravariant vector transformation law.

Metric transformation law
1. Start in \(x\)-coordinates with \(ds^2=g^{(x)}_{mn}dx^m dx^n\).
2. Replace each \(dx^m\) by \(\dfrac{\partial x^m}{\partial y^r}dy^r\).
3. Collect the factors multiplying \(dy^r dy^s\).
4. Identify that parenthesized coefficient as \(g^{(y)}_{rs}\).
5. Read off \(g^{(y)}_{rs}=g^{(x)}_{mn}\dfrac{\partial x^m}{\partial y^r}\dfrac{\partial x^n}{\partial y^s}\).

Polar metric from Cartesian metric
1. Use \(x=r\cos\theta\) and \(y=r\sin\theta\).
2. Differentiate to get \(dx=\cos\theta\,dr-r\sin\theta\,d\theta\) and \(dy=\sin\theta\,dr+r\cos\theta\,d\theta\).
3. Substitute into \(ds^2=dx^2+dy^2\).
4. Collect the \(dr^2\) terms to get \((\cos^2\theta+\sin^2\theta)dr^2=dr^2\).
5. Collect the \(d\theta^2\) terms to get \(r^2(\sin^2\theta+\cos^2\theta)d\theta^2=r^2d\theta^2\).
6. Check that the cross terms cancel.
7. Conclude \(ds^2=dr^2+r^2d\theta^2\).

## Notation Choices
- Use \(x^m\) and \(y^n\) for general coordinates; use \(m,n,r,s\) for index letters.
- Treat superscripts on coordinates such as \(x^m\) and \(dx^m\) as coordinate labels, not powers.
- Use frame labels as superscripts in parentheses only when the distinction matters: \(V^m_{(x)}\), \(T^{(y)}_{mn}\), \(g^{(x)}_{mn}\).
- Standardize contravariant indices upstairs and covariant indices downstairs.
- Standardize Einstein summation so contractions always pair one upper with one lower index.
- Use \(\delta_{mn}\) for the Kronecker delta, with both indices downstairs when it is serving as the Cartesian metric.
- In the worked two-dimensional Cartesian example, it is acceptable to use plain \(x,y\) instead of \(x^1,x^2\), matching the lecture’s local simplification.
- Use \(r,\theta\) for the polar-coordinate example.
- Preserve \(\phi\) for the scalar field in the calculus section; if the sphere subsection also uses \(\phi\) as an angular coordinate, announce the notation reset explicitly.
- Standardize differential products as \(dy^r dy^s\), even if the chalk order or transcript occasionally swaps them.

## Uncertain Mathematics
- The elevator redshift formula of order \(gh/c^2\) is a cautious reconstruction from Susskind’s assigned exercise, not a board-written formula in the supplied frames.
- The exact free-fall cancellation is asserted in the transcript and tied to special relativity, but the full exact calculation is not performed on the board.
- The mid-board metric-transformation line in `lecture_03_figure_06.png` is only partially visible; the clean final equation should be presented as a standard completion of the visibly staged identification.
- The precise arrow notation on \(dx\) in `lecture_03_figure_03.png` is visually vectorial but typographically ambiguous.
- The transcript around the late covariant-rank-two discussion has local corruption; the clean transformation law is supported by the frame plus surrounding transcript, but the intermediate spoken derivation is not fully reliable line by line.
- The sphere discussion after roughly 01:49 becomes badly garbled; the unit-sphere metric may be retained, but the coordinate-description prose and intermediate derivation should be kept cautious.
- The lecture locally reuses symbols and occasionally self-corrects between “space” and “spacetime”; the final notes should clean this up without inventing new mathematical content.