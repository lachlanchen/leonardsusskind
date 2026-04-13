# Math Bank
## Core Equations
- \(x' = x - vt\) [visible]
- \(t' = t\) [visible]
- \(x = vt\) [visible]
- \(x' = 0\) [visible]
- \(x = vt \iff x' = 0\) [standard reconstruction]
- \(x = x' + vt = x' + vt'\), \(\quad t = t'\) [transcript-backed]
- \(x'=\dfrac{x-vt}{\sqrt{1-v^2}}\) [transcript-backed]
- \(t'=\dfrac{t-vx}{\sqrt{1-v^2}}\) [transcript-backed]
- \(x'=\dfrac{x-vt}{\sqrt{1-v^2/c^2}}\) [transcript-backed]
- \(t'=\dfrac{t-vx/c^2}{\sqrt{1-v^2/c^2}}\) [transcript-backed]
- \(y' = y,\qquad z' = z\) [transcript-backed]
- \(x'+t'=\dfrac{(x+t)(1-v)}{\sqrt{1-v^2}}=(x+t)\sqrt{\dfrac{1-v}{1+v}}\) [transcript-backed]
- \(t'-x'=\dfrac{(t-x)(1+v)}{\sqrt{1-v^2}}=(t-x)\sqrt{\dfrac{1+v}{1-v}}\) [standard reconstruction]
- \(s^2=x^2+y^2=x'^2+y'^2\) [transcript-backed]
- \(t'^2-x'^2=t^2-x^2\) [transcript-backed]
- \(t'^2-x'^2-y'^2-z'^2=t^2-x^2-y^2-z^2\) [transcript-backed]
- \(\tau^2=t^2-x^2\) [transcript-backed]
- \(\tau=\sqrt{t^2-x^2}\) in the time-like region [transcript-backed]
- \(x=\pm t\) on the light cone in \(c=1\) units [transcript-backed]
- \(x=0 \Rightarrow \tau=t\) [transcript-backed]
- Along the moving worldline \(x=vt\): \(\tau^2=t^2-v^2t^2=(1-v^2)t^2\) [transcript-backed]
- Along the moving worldline \(x=vt\): \(\tau=t\sqrt{1-v^2}\) [transcript-backed]
- For a clock comoving with the primed frame on \(x'=0\): \(t'=\tau\) [transcript-backed]
- Constant-\(t'\) slices satisfy \(t-vx=\text{const}\) in \(c=1\) units [transcript-backed]
- Constant-\(t'\) slices satisfy \(t-\dfrac{vx}{c^2}=\text{const}\) with \(c\) restored [standard reconstruction]
- For the twin paradox with equal outbound and inbound speed \(v\): \(\tau_{\text{stay}}=2T\) [transcript-backed]
- For the twin paradox with equal outbound and inbound speed \(v\): \(\tau_{\text{travel}}=2T\sqrt{1-v^2}\) [transcript-backed]
- For the one-meter stick example at \(t'=0\): \(x=1,\quad t=v\) [transcript-backed]
- At that same endpoint: \(-x'^2=v^2-1\), hence \(x'=\sqrt{1-v^2}\) [transcript-backed]
- For a rest length \(L=1\): \(L'=\sqrt{1-v^2}\) [transcript-backed]
- For general rest length \(L\): \(L'=L\sqrt{1-v^2}\) [standard reconstruction]

## Definitions And Objects
- `Unprimed frame`: the stationary observer’s coordinates \((x,t)\).
- `Primed frame`: the moving observer’s coordinates \((x',t')\).
- `Direction of motion`: always the \(x\)-direction.
- `\(t'\)-axis`: the worldline of the moving origin; equivalently the locus \(x'=0\), seen in the unprimed frame as \(x=vt\).
- `Constant-\(t'\) surface`: the moving observer’s notion of simultaneity.
- `Event`: a spacetime point where something happens; coincidence of events is invariant across frames.
- `Proper time`: the time read by a clock carried along a worldline; for a time-like separation from the origin, \(\tau=\sqrt{t^2-x^2}\).
- `Coordinate time`: the time measured by the synchronized stationary clocks of a chosen frame.
- `Time-like region`: \(t^2>x^2\) in \(1+1\) dimensions.
- `Light-like region`: \(t^2=x^2\); light rays lie here and have zero proper time.
- `Space-like region`: \(t^2<x^2\); the lecture says the “proper time” is imaginary here.
- `Proper distance / spacelike interval`: used verbally late in the lecture for the length-contraction calculation; the sign convention is handled flexibly there.
- `Ideal clock`: a sufficiently small, well-built clock whose rate is assumed to track proper time even under modest acceleration.
- `Meter-stick ribbon`: the spacetime strip swept out by a rod at rest in some frame.
- `Synchronous endpoints for length`: the two rod endpoints evaluated at the same instant of the observer’s own time.

## Derivation Steps
Lorentz transformation in null variables
1. Set \(c=1\).
2. Start from \(x'=\dfrac{x-vt}{\sqrt{1-v^2}}\) and \(t'=\dfrac{t-vx}{\sqrt{1-v^2}}\).
3. Add the two equations to get \(x'+t'=\dfrac{(x+t)(1-v)}{\sqrt{1-v^2}}\).
4. Rewrite \(\dfrac{1-v}{\sqrt{1-v^2}}=\sqrt{\dfrac{1-v}{1+v}}\).
5. Subtract in the complementary combination to get \(t'-x'=\dfrac{(t-x)(1+v)}{\sqrt{1-v^2}}\).
6. Rewrite the second factor as \(\sqrt{\dfrac{1+v}{1-v}}\).
7. Interpret \(x+t\) and \(t-x\) as coordinates along the two \(45^\circ\) lightlike directions.

Invariant interval
1. Square \(x'=\dfrac{x-vt}{\sqrt{1-v^2}}\).
2. Square \(t'=\dfrac{t-vx}{\sqrt{1-v^2}}\).
3. Form \(t'^2-x'^2\).
4. Cancel the cross terms \(-2xvt\).
5. Collect the \(t^2\) terms into \((1-v^2)t^2\).
6. Collect the \(x^2\) terms into \(-(1-v^2)x^2\).
7. Divide by \(1-v^2\) to obtain \(t'^2-x'^2=t^2-x^2\).

Proper time from the invariant interval
1. Compare Lorentz invariance with Euclidean rotational invariance \(x^2+y^2\).
2. Identify \(t^2-x^2\) as the invariant quantity to name.
3. Define \(\tau^2=t^2-x^2\) for a time-like separation.
4. Take \(\tau=\sqrt{t^2-x^2}\) with the positive square root in the future time-like region.
5. Note \(x=\pm t\) gives \(\tau=0\).
6. Note \(t^2<x^2\) gives an imaginary “proper time” in the lecture’s language.

Moving clocks measure proper time
1. For a stationary clock, the worldline is \(x=0\).
2. Substitute \(x=0\) into \(\tau=\sqrt{t^2-x^2}\) to get \(\tau=t\).
3. For a moving clock, go to the comoving frame where its worldline is \(x'=0\).
4. In that frame, \(\tau=\sqrt{t'^2-x'^2}=t'\).
5. Conclude that a comoving clock reads proper time.

Time dilation
1. Take the moving observer’s worldline: \(x'=0\), equivalently \(x=vt\).
2. Use invariance: \(t'^2-x'^2=t^2-x^2\).
3. Set \(x'=0\).
4. Substitute \(x=vt\).
5. Get \(t'^2=t^2-v^2t^2=(1-v^2)t^2\).
6. Take the positive square root: \(t'=t\sqrt{1-v^2}\).
7. Restore \(c\) if needed: \(t'=t\sqrt{1-v^2/c^2}\).

Relativity of simultaneity
1. Start from \(t'=\dfrac{t-vx}{\sqrt{1-v^2}}\).
2. Hold \(t'\) fixed.
3. Conclude \(t-vx=\text{const}\).
4. Therefore constant-\(t'\) lines are tilted relative to constant-\(t\) lines.
5. Use this to explain why each observer compares different pairs of events when saying the other clock runs slow.

Twin paradox
1. Let the stay-at-home twin follow a vertical worldline from birth to reunion.
2. Let the traveling twin follow two straight legs with equal speed magnitude \(v\).
3. Split the reunion time in the stay-at-home frame into two halves of duration \(T\).
4. For the home twin, \(\tau_{\text{stay}}=2T\).
5. For one traveling leg, use \(x=vT\) and \(\tau_{\text{leg}}=\sqrt{T^2-v^2T^2}=T\sqrt{1-v^2}\).
6. Double it for the return leg: \(\tau_{\text{travel}}=2T\sqrt{1-v^2}\).
7. Compare the two proper times.

Accelerated trajectory by small segments
1. Replace a curved worldline by many short nearly straight pieces.
2. Approximate each short piece by constant velocity.
3. Compute the proper time on each piece using the inertial formula.
4. Add the segment contributions.
5. Treat the ideal-clock assumption as the physical input that the clock records this sum.

Length contraction
1. Draw the spacetime ribbon of a rod at rest in the unprimed frame, with endpoints at \(x=0\) and \(x=1\).
2. To measure its length in the moving frame, pick the two rod endpoints on a single constant-\(t'\) slice.
3. Use the endpoint on the right rod worldline \(x=1\).
4. On the \(t'=0\) slice, use \(t=vx\), hence \(t=v\) at \(x=1\).
5. In the primed frame for that endpoint, \(t'=0\), so the interval from the origin is \(-x'^2\).
6. In the unprimed frame for that same endpoint, the interval is \(t^2-x^2=v^2-1\).
7. Equate them to get \(-x'^2=v^2-1\).
8. Conclude \(x'=\sqrt{1-v^2}\).
9. Read the contracted rod length as the primed spatial separation between \(x'=0\) and \(x'=\sqrt{1-v^2}\).

## Notation Choices
- Use \(c=1\) as the default inside derivations unless dimensional restoration is pedagogically important.
- Restore \(c\) explicitly in the Lorentz formulas and in the time-dilation factor when discussing the physical limit \(v \ll c\).
- Keep the lecture’s frame assignment: unprimed \(=\) stationary, primed \(=\) moving.
- Use \(x\) for the longitudinal spatial coordinate; treat \(y,z\) only as transverse spectators.
- Keep \(x'=0\) as the defining equation of the moving observer’s spatial origin.
- Use \(t'=\text{const}\) for moving-frame simultaneity slices.
- Use \(\tau\) for proper time in the final notes, even though the transcript usually says “proper time” verbally rather than introducing a symbol immediately.
- Use \(s^2=x^2+y^2\) only for the Euclidean rotation analogy; do not reuse \(s\) for the Minkowski interval.
- Avoid introducing \(\gamma\) unless a later editorial pass truly needs it; the lecture works directly with \(\sqrt{1-v^2}\) and \(\sqrt{1-v^2/c^2}\).
- For the twin paradox, keep \(T\) for the half-trip coordinate time in the stay-at-home frame if that section follows the lecture closely.
- For length contraction, keep the one-meter example first, then generalize to \(L\) only after the worked calculation.
- When the interval is space-like, prefer “proper interval” or “proper distance” in polished notes rather than calling \(\tau\) itself imaginary unless the passage is explicitly mirroring the lecture.

## Uncertain Mathematics
- The spoken time-dilation formula is garbled once or twice near the end of the derivation; the correct result is \(t'=t\sqrt{1-v^2}\), not “\(t\) times one minus square root of one minus \(v^2\).”
- The null-coordinate derivation toggles between \(x'-t'\) and \(t'-x'\); the cleaned notes should choose one convention and keep it fixed.
- The lecture is casual about “proper distance means \(t^2-x^2\) or \(x^2-t^2\), it doesn’t matter” during the length-contraction discussion; the final notes should separate time-like and space-like sign choices more carefully.
- The later compact-cylinder asymmetry question is not mathematically resolved in the lecture and should not be upgraded into a finished theorem.
- `lecture_04_figure_04.png` is too partial to support any exact left-board algebra beyond fragments like \(-2xvt\).
- The transcript contains a spoken slip where points outside the light cone are momentarily called “time-like”; the intended classification is clearly “space-like.”
- The moving-frame simultaneity surface is verbally unstable in the late length-contraction discussion; standardize it as \(t-vx=\text{const}\) in \(c=1\) units, with \(t'=0\Rightarrow t=vx\).
- The lecture uses “proper time” and “proper distance” somewhat interchangeably late in the rod calculation; the final notes should distinguish the spacelike interval from timelike proper time while preserving his computational move.