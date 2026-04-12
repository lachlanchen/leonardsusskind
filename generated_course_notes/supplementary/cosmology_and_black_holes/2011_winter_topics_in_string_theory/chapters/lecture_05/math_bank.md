# Math Bank
## Core Equations
- \(R_s \sim \lambda_{\text{thermal}}\) for the warm-up \(3\,\mathrm{K}\) estimate [transcript-backed]
- \(R_s \sim 1\,\mathrm{cm}\) for a black hole radiating centimeter-scale microwaves [transcript-backed]
- \(R_s = 2MG\) in the lecture’s \(c=1\) shorthand [transcript-backed]
- \(R_s = \dfrac{2GM}{c^2}\) [transcript-backed]
- \(M \propto R_s\) for Schwarzschild black holes [transcript-backed]
- \(E = mc^2\) [transcript-backed]
- \(M = \dfrac{E}{c^2}\) for the collapsing light shell as seen from far away [transcript-backed]
- \(E=M\) in the lecture’s natural-units simplification [transcript-backed]
- \(t=\infty\) on the compactified flat-space diagram [visible]
- \(r=0\) for the left timelike boundary of the reduced flat-space Penrose diagram [standard reconstruction]
- \(r=\infty\) on the Schwarzschild exterior diagram [visible]
- \(t=\infty\) on the Schwarzschild exterior diagram [visible]
- \(t=-\infty\) on the Schwarzschild exterior diagram [visible]
- \(r=2MG\) for the horizon-side boundary of the exterior Schwarzschild region [transcript-backed]
- \(r=6MG\) as a representative outer constant-\(r\) curve [transcript-backed]
- \(r=100MG\) as a far-out constant-\(r\) curve [transcript-backed]
- \(S_{\mathrm{BH}} \propto A_H\) [transcript-backed]
- \(\Delta A_H \sim \ell_P^2\) per added bit, in the lecture’s recap language of “one Planck unit of area” [transcript-backed]
- \(T_H=\dfrac{\hbar c^3}{8\pi GM}\) in the lecture’s convention with \(k_B=1\) [transcript-backed]
- \(T_H=\dfrac{\hbar c^3}{8\pi GM k_B}\) in SI-style units [standard reconstruction]
- \(T_H \propto \dfrac{1}{R_s}\) [transcript-backed]
- \(T_H=\dfrac{\hbar c}{4\pi R_s}\) with \(k_B=1\) [standard reconstruction]
- \(T(\rho)=\dfrac{1}{2\pi \rho}\) [transcript-backed]
- \(\lambda \lesssim \Delta x\) for position resolution [transcript-backed]
- \(p_\gamma \gtrsim \dfrac{\hbar}{\Delta x}\) [transcript-backed]
- \(E_\gamma=p_\gamma c\) [transcript-backed]
- \(\Delta t \sim \dfrac{\rho}{c}\) for the remaining fall time through a near-horizon layer of thickness \(\rho\) [transcript-backed]
- \(\lambda \lesssim \rho\) for resolving the atom in that near-horizon region [transcript-backed]
- \(E_\gamma \gtrsim \dfrac{\hbar c}{\rho}\) [standard reconstruction]
- \(E_\gamma \sim \dfrac{1}{\rho}\) in natural units [transcript-backed]

## Definitions And Objects
- Reduced spacetime coordinates \((t,r)\): time plus radial distance, with the angular \(S^2\) suppressed.
- Flat-space Penrose diagram: compactified \((t,r)\) half-plane with \(r\ge 0\), null rays at \(45^\circ\), and constant-\(r\)/constant-\(t\) families crowding near infinity.
- Eternal Schwarzschild Penrose diagram: two-diamond diagram with future and past singularities; only the ordinary exterior region is physically retained for collapse.
- Horizon in the eternal Schwarzschild recap: the boundary at \(r=2MG\) in the exterior diagram.
- Newton’s theorem: for a spherically symmetric mass distribution, the gravitational influence at radius \(r\) is determined only by enclosed mass; a hollow shell gives zero field inside.
- Birkhoff’s theorem: inside a spherically symmetric shell the spacetime is Minkowski; outside it is Schwarzschild with the shell’s total mass.
- Collapsing shell of light: an ingoing null spherical shell carrying total energy \(E\), treated as mass parameter \(M=E/c^2\).
- Event horizon: the boundary between events from which outgoing light can reach infinity and those from which it cannot.
- Proper distance \(\rho\): distance from the horizon in the near-horizon discussion.
- Hawking temperature \(T_H\): temperature measured by a thermometer far from the black hole.
- Local extrapolated temperature \(T(\rho)\): near-horizon temperature assigned to a thermometer lowered to proper distance \(\rho\).
- Ionization threshold: the temperature/energy scale at which the falling atom would be ionized in the hot near-horizon environment.
- Heisenberg measurement setup: a probe photon used to resolve an object within a short spatial or temporal window, thereby disturbing it.

## Derivation Steps
**Three-degree black hole estimate**
1. Take the relevant thermal wavelength for \(3\,\mathrm{K}\) radiation to be of order centimeters.
2. Use the lecture heuristic that a black hole radiates photons with wavelength of order its own size.
3. Infer a Schwarzschild radius of order \(R_s\sim 1\,\mathrm{cm}\).
4. Compare with a solar-mass black hole of radius of order kilometers.
5. Use \(R_s\propto M\) to infer a mass about \(10^5\) times smaller than the Sun.
6. Conclude an order-of-magnitude mass around Earth or Moon scale.

**Flat-space to Schwarzschild comparison**
1. In flat space, reduced radial null rays enter and leave at \(45^\circ\).
2. Compactify the \((t,r)\) half-plane into a finite Penrose wedge.
3. Read off constant-\(r\) and constant-\(t\) curves from the compactified grid.
4. Repeat for Schwarzschild exterior, marking \(r=\infty\), \(t=\pm\infty\), and the horizon at \(r=2MG\).
5. Compare the two pictures: far away they look similar, near \(r=0\) they differ because flat-space rays bounce off the center while Schwarzschild rays hit the singularity.

**Newton/Birkhoff shell logic**
1. Start with a spherically symmetric mass distribution.
2. Use Newton’s theorem to say that only the enclosed mass contributes to the field at a given radius.
3. Apply the special case of a hollow shell: inside, the gravitational field is zero.
4. Translate this to general relativity with Birkhoff’s theorem.
5. Conclude that inside a spherical shell the metric is flat Minkowski spacetime.
6. Conclude that outside the shell the metric is Schwarzschild with the shell’s total mass.

**Collapse Penrose construction**
1. Model the infalling matter as a spherically symmetric shell of light coming in from infinity.
2. Assign it energy \(E\) and mass parameter \(M=E/c^2\).
3. Draw the ingoing null shell on the flat-space Penrose diagram.
4. Use Birkhoff: below/inside the shell, keep the flat-space geometry.
5. Use Birkhoff: above/outside the shell, replace the geometry by the Schwarzschild exterior.
6. Discard the white-hole region and second asymptotic exterior of the eternal Schwarzschild diagram.
7. Match the shell endpoint at the center with the \(r=0\) singular endpoint.

**Locating the true event horizon**
1. Abandon the temporary identification “horizon = \(r=2MG\)” as a definition.
2. Define the horizon causally as the boundary between events that can and cannot send outgoing light to infinity.
3. In the collapse diagram, trace the outgoing null line that just fails to escape.
4. Extend that null boundary backward into the region that is still flat spacetime.
5. Conclude that the event horizon forms before the shell arrives locally.
6. Read off that the horizon’s associated sphere grows from zero size to the usual Schwarzschild size \(2MG\).

**Rewriting Hawking temperature**
1. Start from the lecture formula \(T_H=\hbar c^3/(8\pi GM)\).
2. Insert \(R_s=2GM/c^2\).
3. Replace \(GM\) by \(R_s c^2/2\).
4. Conclude that \(T_H\) scales like \(1/R_s\).
5. Use this to stress that large black holes are cold.

**Near-horizon local temperature**
1. Interpret \(T_H\) as the temperature read by a thermometer far away.
2. Use gravitational redshift reasoning to infer that the locally measured temperature rises closer to the horizon.
3. Introduce proper distance \(\rho\) from the horizon.
4. State the near-horizon result \(T(\rho)=1/(2\pi \rho)\).
5. Conclude that the local temperature diverges as \(\rho\to 0\).

**Heisenberg reminder**
1. To localize a particle within \(\Delta x\), probe it with wavelength \(\lambda\lesssim \Delta x\).
2. Therefore the photon momentum must satisfy \(p_\gamma \gtrsim \hbar/\Delta x\).
3. Scattering such a photon imparts recoil of order \(p_\gamma\).
4. A subsequent velocity measurement no longer recovers the pre-measurement state.
5. Therefore the experiment creates the condition it was meant to test against.

**Near-horizon operational measurement argument**
1. Consider the layer where the local temperature reaches the ionization scale.
2. A freely falling atom entering that layer has only \(\Delta t\sim \rho/c\) before crossing the horizon.
3. To determine its state during that interval, an external observer must resolve it over a scale \(\rho\).
4. That requires a probe with \(\lambda\lesssim \rho\).
5. Hence the probe energy must satisfy \(E_\gamma \gtrsim \hbar c/\rho\).
6. This energy scale matches the local thermal scale \(1/\rho\).
7. Therefore the act of measuring is energetic enough to ionize or disrupt the atom.
8. Conclude that no external experiment can verify “the atom was not heated” without causing heating itself.

## Notation Choices
- Use \(M\) for black-hole mass, not the transcript’s spoken “\(m\)” or “\(mg\)” shorthand.
- Use \(G\) explicitly for Newton’s constant.
- Write \(R_s=2GM/c^2\) in SI-style expressions and \(R_s=2MG\) only when explicitly following the lecture’s \(c=1\) shorthand.
- Use \(r\) for Schwarzschild areal radius and for the reduced radial coordinate on Penrose diagrams.
- Reserve \(\rho\) for proper distance from the horizon in the near-horizon thermodynamic discussion.
- Use \(T_H\) for the asymptotic Hawking temperature.
- Use \(T(\rho)\) for the local extrapolated near-horizon temperature.
- Use \(A_H\) for horizon area if a symbol is needed; do not introduce the full Bekenstein-Hawking formula unless another lecture motivates it.
- Use “future singularity” and “past singularity” in polished notes; \(\mathrm{sing}_\pm\) can be mentioned only as board shorthand.
- Treat each point of the reduced Penrose diagram as an \(S^2\), especially when describing shells and horizon size.
- Use “ingoing null shell” or “shell of light” for the collapsing matter model.
- When quoting formulas like \(T(\rho)=1/(2\pi\rho)\), state once that natural units \(c=\hbar=k_B=1\) are in force.

## Uncertain Mathematics
- The opening \(3\,\mathrm{K}\) estimate is only order-of-magnitude; \(\lambda\sim R_s\) is a lecture heuristic, not an exact thermal relation.
- The Earth-mass versus Moon-mass outcome depends on omitted numerical constants; keep the estimate qualitative.
- The board-visible labels \(r=6MG\) and \(r=100MG\) are transcript-motivated sample radii, not precisely placed coordinate curves.
- The exact compactifying coordinate transformation for the flat-space Penrose diagram is never given; do not invent one in the chapter unless explicitly needed.
- The lecture’s rewrite of \(T_H\) in terms of radius includes verbal hesitation over factors of \(2\), \(4\), and \(\pi\); use the canonical formula in the final notes and mention only the scaling \(T_H\propto 1/R_s\) if necessary.
- The local formula \(T(\rho)=1/(2\pi\rho)\) is stated, not derived. Present it as a near-horizon result rather than a full derivation from first principles.
- The statement that photons “lose energy climbing out” is used heuristically; the exact redshift factor is not worked out in this lecture.
- The “13 electron volts \(\sim 3000\) degrees” exchange is numerically inconsistent if interpreted literally; keep the ionization discussion qualitative or retain \(13.6\,\mathrm{eV}\) as the safer benchmark.
- The near-horizon experimental argument is an operational uncertainty-principle estimate, not a rigorous theorem phrased in full operator language.
- The appeal to “time-energy uncertainty” near the end is heuristic; the more solid content in the lecture is the spatial-resolution argument \(\lambda\lesssim \rho\).
- The horizon-growth discussion is geometric and causal, not an explicit calculation of area as a function of time.