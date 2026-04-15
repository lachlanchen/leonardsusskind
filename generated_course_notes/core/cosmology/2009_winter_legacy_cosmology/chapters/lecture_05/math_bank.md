# Math Bank
## Core Equations
- `x^2+y^2=a^2`, with unit case `x^2+y^2=1` for the one-sphere [transcript-backed]
- `x^2+y^2+z^2=a^2`, with unit case `x^2+y^2+z^2=1` for the two-sphere [transcript-backed]
- `x^2+y^2+z^2+w^2=A^2`, with unit case `x^2+y^2+z^2+w^2=1` for the three-sphere [transcript-backed]
- `x^2=1` for the unit zero-sphere [transcript-backed]
- `ds^2=d\phi^2` for the unit one-sphere [transcript-backed]
- `ds^2=d\theta^2+\sin^2\theta\,d\phi^2` for the unit two-sphere [transcript-backed]
- `d\Omega_1^2=d\phi^2` [transcript-backed]
- `d\Omega_2^2=d\theta^2+\sin^2\theta\,d\Omega_1^2` [standard reconstruction]
- `d\Omega_3^2=d\alpha^2+\sin^2\alpha\,d\Omega_2^2` [transcript-backed]
- `d\Omega_n^2=d\alpha^2+\sin^2\alpha\,d\Omega_{n-1}^2` [standard reconstruction]
- `ds^2=A^2\,d\Omega_3^2` for a three-sphere of fixed radius `A` [transcript-backed]
- `d\tau^2=dt^2-a(t)^2\,d\Omega_3^2` for positively curved FRW [transcript-backed]
- `dx^2+dy^2+dz^2` as the visible flat-space spatial fragment on the board [visible]
- `d\tau^2=dt^2-a(t)^2\left(dx^2+dy^2+dz^2\right)` for flat FRW [transcript-backed]
- `d\mathcal H_n^2=d\alpha^2+\sinh^2\alpha\,d\Omega_{n-1}^2` for uniform negative curvature [standard reconstruction]
- `\sinh\alpha=\frac{e^\alpha-e^{-\alpha}}{2}` [transcript-backed]
- `d\tau^2=dt^2-a(t)^2\,d\mathcal H_3^2` for negatively curved FRW [transcript-backed]
- `k=+1,0,-1` for spherical, flat, and hyperbolic spatial geometry [transcript-backed]
- `p=w\rho` [transcript-backed]
- `w=0,\quad w=\tfrac13,\quad w=-1` for matter, radiation, and vacuum energy [transcript-backed]
- `\rho_m\propto a^{-3},\qquad \rho_r\propto a^{-4},\qquad \rho_{\Lambda}=\text{const.}` [transcript-backed]
- `R^{\mu\nu}-g^{\mu\nu}R=4\pi G\,T^{\mu\nu}` as written on the board [visible]
- `R^{\mu\nu}-\tfrac12 g^{\mu\nu}R=4\pi G\,T^{\mu\nu}` as the cleaned lecture form [standard reconstruction]
- `R^{00}-g^{00}\,\cdots=4\pi G\,\rho` as the visible `00`-component staging on the board [visible]
- `R^{00}-\tfrac12 g^{00}R=4\pi G\,\rho` as the cleaned `00` component [standard reconstruction]
- `\left(\frac{\dot a}{a}\right)^2+\frac{k}{a^2}=\frac{8\pi G}{3}\rho` [standard reconstruction]
- `\left(\frac{\dot a}{a}\right)^2=\frac{8\pi G}{3}\rho-\frac{k}{a^2}` [standard reconstruction]

## Definitions And Objects
- `S^1`, `S^2`, `S^3`: one-, two-, and three-spheres, first introduced as embedded loci, then reinterpreted intrinsically.
- `\Omega_n`: lecture notation for the `n`-sphere as a geometry; `d\Omega_n^2` is the metric of the unit `n`-sphere.
- `\mathcal H_n` or `H_n`: uniformly negatively curved `n`-dimensional space, the hyperbolic analog of the sphere.
- Homogeneous / uniform: same curvature and same local geometry at every point.
- Embedding “crutch”: auxiliary Euclidean coordinates used to define the sphere, not part of the intrinsic geometry.
- `A`: fixed radius for a static sphere.
- `a(t)`: time-dependent radius / scale factor in FRW cosmology.
- `\phi`: angular coordinate on the one-sphere.
- `\theta`: polar-type coordinate used to foliate the two-sphere by one-spheres.
- `\alpha`: extra radial-angle coordinate for the three-sphere; later treated as observer-centered radial coordinate on the unit sphere, and as the radial coordinate on hyperbolic space.
- `\mu,\nu`: spacetime indices; the lecture treats the four directions as `t,x,y,z`, with time component labeled `0`.
- `T^{\mu\nu}`: energy-momentum tensor.
- `T^{00}=\rho`: energy density.
- Space-space components of `T^{\mu\nu}`: pressure terms.
- `R^{\mu\nu}`: Ricci tensor in the lecture’s board notation.
- `R`: Ricci scalar.
- `G^{\mu\nu}=R^{\mu\nu}-\tfrac12 g^{\mu\nu}R`: Einstein tensor, named in the lecture even when not written with explicit `G^{\mu\nu}` notation.
- Natural-units convention: `c=1` is assumed once energy and mass density are identified.

## Derivation Steps
Unit two-sphere metric
1. Start from the unit one-sphere metric `d\phi^2`.
2. Regard the two-sphere as a family of one-spheres labeled by a second angle `\theta`.
3. Motion in the `\theta` direction contributes `d\theta^2`.
4. The radius of the latitude circle at fixed `\theta` is `\sin\theta`.
5. Motion around that circle contributes `\sin^2\theta\,d\phi^2`.
6. Add the two orthogonal pieces to get `d\theta^2+\sin^2\theta\,d\phi^2`.

Unit three-sphere and recursive sphere metric
1. Regard the three-sphere as a family of two-spheres labeled by `\alpha`.
2. The new radial direction contributes `d\alpha^2`.
3. The radius of the two-sphere at fixed `\alpha` is `\sin\alpha`.
4. Multiply the lower-dimensional unit-sphere metric by `\sin^2\alpha`.
5. Obtain `d\Omega_3^2=d\alpha^2+\sin^2\alpha\,d\Omega_2^2`.
6. Read off the inductive rule `d\Omega_n^2=d\alpha^2+\sin^2\alpha\,d\Omega_{n-1}^2`.

Radius scaling and FRW promotion
1. A sphere of fixed radius `A` is obtained by multiplying the unit-sphere metric by `A^2`.
2. Replace the fixed radius by a time-dependent scale factor `a(t)`.
3. Add the time part of the spacetime interval as `dt^2`.
4. Use the lecture’s signature convention `dt^2-(\text{spatial metric})`.
5. Obtain the positively curved FRW form `d\tau^2=dt^2-a(t)^2 d\Omega_3^2`.

Negative curvature from the spherical recursion
1. Keep the same recursive structure used for the sphere.
2. Replace `\sin\alpha` by `\sinh\alpha`.
3. Rename the resulting metric `d\mathcal H_n^2`.
4. Change the range of the radial coordinate from a finite spherical interval to `\alpha\in[0,\infty)`.
5. Use the same FRW pattern to get `d\tau^2=dt^2-a(t)^2 d\mathcal H_3^2`.

Newtonian cosmology recap
1. Put us at the center and track a receding galaxy.
2. Use Newton’s shell theorem: only matter inside the sphere of that radius contributes.
3. Since distance to a fixed comoving galaxy is proportional to `a(t)`, kinetic energy is proportional to `\dot a^2`.
4. Express the source in terms of density `\rho`.
5. After dividing by `a^2`, the Newtonian energy equation has a density term plus a constant-energy term proportional to `1/a^2`.
6. The lecture reopens that dropped term and associates it with the later `k/a^2` contribution.

Einstein-equation specialization to FRW
1. Start from the FRW metric, whose only dynamical function is the scale factor.
2. Impose Einstein’s field equations on that ansatz.
3. By homogeneity and isotropy, one independent differential equation is enough for `a(t)`.
4. Choose the `00` component because `T^{00}` is the energy density `\rho`.
5. The geometry contributes a time-variation term proportional to `(\dot a/a)^2`.
6. Curved space contributes an additional term proportional to `k/a^2`.
7. After cleaning the lecture’s coefficient discussion, recover the Friedmann equation.

Operational curvature statement
1. In positively curved space, a standard ruler at fixed distance subtends a larger angle than it would in flat space.
2. In negatively curved space, the same ruler subtends a smaller angle.
3. This is the observational reason the lecture spends time on stereographic and disk pictures before returning to Einstein’s equations.

## Notation Choices
- Use `a(t)` as the chapter’s standard scale factor. Reserve `A` for a fixed sphere radius in the static geometry discussion.
- Use `d\tau^2` for spacetime intervals and `ds^2` for purely spatial metrics.
- Keep the lecture’s metric signature convention `(+,-,-,-)`, since every FRW line is written as `dt^2 - (\text{spatial part})`.
- Use `d\Omega_n^2` for the metric of the unit `n`-sphere throughout.
- Use `d\mathcal H_n^2` for the hyperbolic metric; note that the transcript wavers between spoken `H_n` and garbled `d\omega`/`d h` fragments.
- Keep `\phi,\theta,\alpha` in the order the lecture introduces them.
- Treat `\alpha` as an angular radial coordinate on the sphere and as an ordinary radial coordinate on hyperbolic space; explain the change of geometric meaning explicitly.
- Use `k\in\{+1,0,-1\}` once the scale factor has been normalized to the natural curvature radius convention.
- Preserve the lecture’s `4\pi G` normalization in the field equation section.
- Use overdots for derivatives with respect to cosmic time `t`: `\dot a = da/dt`.
- Keep time index `0` in the tensor equations so that `T^{00}=\rho` matches the lecture’s board staging.

## Uncertain Mathematics
- The board in `lecture_05_figure_05.png` does not visibly show the `\tfrac12` multiplying `g^{\mu\nu}R`; the cleaned notes should restore it, but the visual evidence alone does not.
- The lower `00`-component equation in the screenshot is partly blocked, so only the structure and right-hand side `4\pi G\,\rho` are visually secure.
- The transcript around the three-sphere coordinate range is garbled; one line sounds like `\alpha` runs from `0` to `2\pi`, but the spherical recursion requires the radial foliation coordinate to run from `0` to `\pi`.
- The transcript briefly says “you calculate the energy momentum tensor from the metric”; context shows he means the curvature / Einstein-tensor side from the metric. Do not reproduce that literally as a derivation claim.
- The coefficient discussion in the Einstein-to-Friedmann bridge is verbally unstable: first `4\pi G\rho`, then a missing half, then a `3/2` factor, then the cleaned `8\pi G/3`. The final chapter should present the cleaned equation and treat the intermediate coefficient talk cautiously.
- Index placement is not fully stable in the transcript. The board visually uses upper indices, but the prose should prioritize consistency over imitating every garbled spoken index.
- `k` is normalized to `+1,0,-1` only after choosing the natural curvature scale; the lecture explicitly notes that a rescaling of `a` would change that convention.
- The flat-board fragment in `lecture_05_figure_02.png` certifies only the spatial piece `dx^2+dy^2+dz^2`, not the full flat FRW metric on its own.