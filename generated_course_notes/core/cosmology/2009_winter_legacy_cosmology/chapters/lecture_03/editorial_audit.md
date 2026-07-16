# Editorial Audit

- Status: **revise**
- Findings: 7

## Findings

- **critical / leakage** at `opening paragraph ending "with transcript and frame curation indebted to LazyingArt LLC and Video2Book."`: This is explicit workflow and provenance language in chapter prose, and it names entities that the editorial charter forbids in the body. It also shifts the opening away from the physics into production history. Repair: Delete the sentence entirely and remove all workflow, curation, and production-credit language from the chapter body.
- **high / voice** at `repeated lecturer-centered narration such as "Susskind opens by reminding us...", "Susskind pauses to say...", and "Susskind then draws..."`: The chapter repeatedly narrates the lecturer's behavior instead of presenting the physics directly in lecture order. The charter asks for direct exposition rather than tracking what the lecturer is doing. Repair: Rewrite these passages as direct physics exposition while preserving the lecture's sequence and emphases.
- **high / q_and_a** at `all "Question & Answer" subsections using \paragraph{Question.} and \paragraph{Answer.}`: Several real classroom exchanges are paraphrased into synthetic Q&A blocks rather than preserved as transcript-backed classroom exchanges with timestamps. This loses source fidelity and violates the chapter's required Q&A format. Repair: Convert genuine exchanges to `classroomqa` with transcript-backed wording and `\lecturetimestamp{...}`; fold any non-essential paraphrase back into prose instead of keeping synthetic Q&A blocks.
- **medium / structure** at `final section "Summary"`: The lecture does not close with a recap section. The added summary is an imposed structure rather than a lecture-determined ending. Repair: Remove the summary section and let the chapter end with the actual dark-matter close of the lecture.
- **medium / figure** at `captions such as "Clean reconstruction of the homogeneous sphere used in the lecture" and "Transcript-derived reconstruction of the energy-density comparison drawn in the lecture"`: These captions describe editorial process rather than the physics shown, and they introduce production-style wording into captions. The charter requires physics-only captions, with provenance moved elsewhere. Repair: Replace these with physics-only captions and move provenance to concise footnotes or the source map.
- **medium / provenance** at `the extra TikZ redraws for the homogeneous sphere, energy-density comparison, scale-factor transition, and rotation-curve comparison`: The redraws are not explicitly footnoted as editorial reconstructions. The energy-density redraw is acceptable as a companion to the axes screenshot, but the rotation-curve comparison has no attached board witness and currently reads like a lecture figure rather than a reconstruction from spoken argument. Repair: Add concise provenance footnotes for nontrivial redraws, and either remove the unsupported rotation-curve redraw or clearly mark it as an editorial reconstruction based on the transcript.
- **low / structure** at `dark-matter discussion after the derivation of rho(r) ~ 1/r^2`: The prose compresses a long cluster of useful classroom exchanges into generalized exposition. The argument survives, but some of the lecture's clarifying give-and-take is lost. Repair: Restore one or two of the strongest verified exchanges from this segment in `classroomqa`, especially the 1/r^2 question and the Bullet Cluster exchange.

## Source Uncertainties

- `equation "R_{00}-\frac{1}{2}g_{00}R \propto T_{00}"`: equation Check: named reference
- `the added rotation-curve comparison redraw`: unsupported addition Check: transcript
- `the redraw paired with lecture_03_figure_05`: attribution Check: audio
