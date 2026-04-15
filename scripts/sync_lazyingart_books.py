#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


VIDEO_EXTS = {".mkv", ".mp4", ".webm"}

DEFAULT_SOURCE_ROOT = Path(
    "/home/lachlan/ProjectsLFS/YoutubeDownloader/downloads/PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG"
)
DEFAULT_TARGET_ROOT = Path("/home/lachlan/Nutstore Files/Projects/LazyingArtBooks")

CANONICAL_FILENAMES = {
    "core/classical_mechanics/2011_fall_modern_physics_stanford_partial": "classical_mechanics_stanford_partial.pdf",
    "core/classical_mechanics/2011_fall_theoretical_minimum": "classical_mechanics_theoretical_minimum.pdf",
    "core/cosmology/2009_winter_legacy_cosmology": "cosmology_legacy.pdf",
    "supplementary/advanced_quantum_mechanics/2013_fall": "advanced_quantum_mechanics.pdf",
    "supplementary/cosmology_and_black_holes/2011_winter_topics_in_string_theory": "topics_in_string_theory.pdf",
    "supplementary/higgs_boson/2012_summer": "demystifying_the_higgs_boson.pdf",
    "supplementary/particle_physics_1_basic_concepts/2009_fall": "particle_physics_1_basic_concepts.pdf",
    "supplementary/particle_physics_2_standard_model/2010_winter": "particle_physics_2_standard_model.pdf",
    "supplementary/particle_physics_3_supersymmetry_and_grand_unification/2010_spring": "particle_physics_3_supersymmetry_and_grand_unification.pdf",
    "supplementary/quantum_entanglement/2006_fall_part_1": "quantum_entanglement_part_1.pdf",
    "supplementary/quantum_entanglement/2006_fall_part_3": "quantum_entanglement_part_3.pdf",
    "supplementary/string_theory/2010_fall_string_theory_and_m_theory": "string_theory_and_m_theory.pdf",
}


def count_files(root: Path, suffix: str) -> int:
    if not root.exists():
        return 0
    return len([path for path in root.iterdir() if path.is_file() and path.suffix.lower() == suffix])


def count_videos(root: Path) -> int:
    if not root.exists():
        return 0
    return len([path for path in root.iterdir() if path.is_file() and path.suffix.lower() in VIDEO_EXTS])


def course_filename(course_rel: str) -> str:
    if course_rel in CANONICAL_FILENAMES:
        return CANONICAL_FILENAMES[course_rel]

    parts = Path(course_rel).parts
    subject = parts[1] if len(parts) > 1 else "course"
    run = parts[2] if len(parts) > 2 else ""
    subject = subject.strip().lower()
    run = run.strip().lower()

    if "theoretical_minimum" in run:
        return f"{subject}_theoretical_minimum.pdf"
    if "modern_physics_stanford_partial" in run:
        return f"{subject}_stanford_partial.pdf"
    if "modern_physics_stanford" in run:
        return f"{subject}_stanford.pdf"
    if run:
        return f"{subject}_{run}.pdf"
    return f"{subject}.pdf"


def finished_courses(repo_root: Path, source_root: Path, markdown_root: Path, subtitle_root: Path, output_root: Path) -> list[tuple[str, Path]]:
    courses: list[tuple[str, Path]] = []
    for course_pdf in sorted(output_root.glob("*/*/*/course.pdf")):
        if course_pdf.parent.name == "build":
            continue
        course_rel = str(course_pdf.parent.relative_to(output_root))
        md_count = count_files(markdown_root / course_rel, ".md")
        srt_count = count_files(subtitle_root / course_rel, ".srt")
        video_count = count_videos(source_root / course_rel)
        lecture_pdf_count = len(list((course_pdf.parent / "chapters").glob("*/lecture.pdf")))
        if video_count > 0 and video_count == md_count == srt_count == lecture_pdf_count:
            courses.append((course_rel, course_pdf))
    return courses


def parser() -> argparse.ArgumentParser:
    parsed = argparse.ArgumentParser(description="Sync finished Leonard Susskind course PDFs to LazyingArtBooks.")
    parsed.add_argument("--repo-root", type=Path, default=Path.cwd())
    parsed.add_argument("--source-root", type=Path, default=DEFAULT_SOURCE_ROOT)
    parsed.add_argument("--markdown-root", type=Path)
    parsed.add_argument("--subtitle-root", type=Path)
    parsed.add_argument("--output-root", type=Path)
    parsed.add_argument("--target-root", type=Path, default=DEFAULT_TARGET_ROOT)
    parsed.add_argument("--dry-run", action="store_true")
    return parsed


def main() -> int:
    args = parser().parse_args()

    repo_root = args.repo_root.resolve()
    source_root = args.source_root.resolve()
    markdown_root = (args.markdown_root or repo_root / "markdown").resolve()
    subtitle_root = (args.subtitle_root or repo_root / "subtitles").resolve()
    output_root = (args.output_root or repo_root / "generated_course_notes").resolve()
    target_root = args.target_root.resolve()

    target_root.mkdir(parents=True, exist_ok=True)
    manifest_path = target_root / ".leonardsusskind_books_manifest.json"
    previous_manifest: list[str] = []
    if manifest_path.exists():
        try:
            previous_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            previous_manifest = []

    current_manifest: list[str] = []
    for course_rel, course_pdf in finished_courses(repo_root, source_root, markdown_root, subtitle_root, output_root):
        output_name = course_filename(course_rel)
        current_manifest.append(output_name)
        target_pdf = target_root / output_name
        print(f"sync {course_rel} -> {target_pdf}")
        if not args.dry_run:
            shutil.copy2(course_pdf, target_pdf)

    stale = sorted(set(previous_manifest) - set(current_manifest))
    for stale_name in stale:
        stale_path = target_root / stale_name
        if stale_path.exists():
            print(f"remove stale {stale_path}")
            if not args.dry_run:
                stale_path.unlink()

    if not args.dry_run:
        manifest_path.write_text(json.dumps(sorted(current_manifest), indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
