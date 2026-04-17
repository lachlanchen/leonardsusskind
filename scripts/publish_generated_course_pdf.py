#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
from pathlib import Path


CANONICAL_FILENAMES = {
    "core/classical_mechanics/2011_fall_modern_physics_stanford_partial": "classical_mechanics_stanford_partial.pdf",
    "core/classical_mechanics/2011_fall_theoretical_minimum": "classical_mechanics_theoretical_minimum.pdf",
    "core/cosmology/2009_winter_legacy_cosmology": "cosmology_legacy.pdf",
    "core/cosmology/2013_winter_theoretical_minimum": "cosmology_theoretical_minimum.pdf",
    "core/general_relativity/2008_fall_einsteins_general_theory_of_relativity": "general_relativity_2008_fall_einsteins_general_theory_of_relativity.pdf",
    "core/general_relativity/2012_fall_theoretical_minimum": "general_relativity_theoretical_minimum.pdf",
    "core/quantum_mechanics/2012_winter_modern_physics_stanford": "quantum_mechanics_modern_physics_stanford.pdf",
    "core/quantum_mechanics/2012_winter_theoretical_minimum_alt_title": "quantum_mechanics_theoretical_minimum.pdf",
    "core/special_relativity/2012_spring_theoretical_minimum": "special_relativity_theoretical_minimum.pdf",
    "core/statistical_mechanics/2013_spring_theoretical_minimum": "statistical_mechanics_theoretical_minimum.pdf",
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

ROOT_TRACK_DIRS = {
    "core/classical_mechanics": "core_classical_mechanics",
    "core/cosmology": "core_cosmology",
    "core/general_relativity": "core_general_relativity",
    "core/quantum_mechanics": "core_quantum_mechanics",
    "core/special_relativity": "core_special_relativity",
    "core/statistical_mechanics": "core_statistical_mechanics",
    "supplementary/advanced_quantum_mechanics": "supplemental_advanced_quantum",
    "supplementary/cosmology_and_black_holes": "supplemental_cosmology_and_black_holes",
    "supplementary/higgs_boson": "supplemental_higgs_boson",
    "supplementary/particle_physics_1_basic_concepts": "supplemental_particle_physics_1",
    "supplementary/particle_physics_2_standard_model": "supplemental_particle_physics_2",
    "supplementary/particle_physics_3_supersymmetry_and_grand_unification": "supplemental_particle_physics_3",
    "supplementary/quantum_entanglement": "supplemental_quantum_entanglement",
    "supplementary/relativity": "supplemental_relativity",
    "supplementary/string_theory": "supplemental_string_theory",
}

DEFAULT_NUTSTORE_ROOT = Path("/home/lachlan/Nutstore Files/Projects/LazyingArtBooks")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Publish one generated course PDF into root folders, all_notes, and Nutstore.")
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--course", required=True)
    parser.add_argument("--nutstore-root", type=Path, default=DEFAULT_NUTSTORE_ROOT)
    return parser.parse_args()


def course_filename(course_rel: str) -> str:
    return CANONICAL_FILENAMES[course_rel]


def root_track_dir(course_rel: str) -> str:
    parts = Path(course_rel).parts
    key = "/".join(parts[:2])
    return ROOT_TRACK_DIRS[key]


def hardlink_or_copy(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists() or dst.is_symlink():
        dst.unlink()
    try:
        os.link(src, dst)
    except OSError:
        shutil.copy2(src, dst)


def rebuild_course_pdf(course_dir: Path) -> Path:
    build_dir = course_dir / "build"
    build_dir.mkdir(parents=True, exist_ok=True)
    compile_log = build_dir / "publish_compile.log"
    with compile_log.open("w", encoding="utf-8") as log_handle:
        for _ in range(2):
            subprocess.run(
                [
                    "pdflatex",
                    "-interaction=nonstopmode",
                    "-halt-on-error",
                    "-file-line-error",
                    f"-output-directory={build_dir}",
                    "course.tex",
                ],
                cwd=course_dir,
                check=True,
                stdout=log_handle,
                stderr=subprocess.STDOUT,
            )
    built_pdf = build_dir / "course.pdf"
    if not built_pdf.exists():
        raise SystemExit(f"missing rebuilt pdf: {built_pdf}")
    shutil.copy2(built_pdf, course_dir / "course.pdf")
    return course_dir / "course.pdf"


def main() -> int:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    course_rel = args.course
    generated_dir = repo_root / "generated_course_notes" / course_rel
    source_pdf = rebuild_course_pdf(generated_dir)

    filename = course_filename(course_rel)
    run_name = Path(course_rel).parts[-1]
    root_dir = repo_root / root_track_dir(course_rel) / run_name
    all_notes_pdf = repo_root / "all_notes" / filename
    nutstore_pdf = args.nutstore_root.resolve() / filename

    hardlink_or_copy(source_pdf, root_dir / filename)
    hardlink_or_copy(source_pdf, all_notes_pdf)
    nutstore_pdf.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_pdf, nutstore_pdf)

    print(f"published {course_rel} -> {root_dir / filename}")
    print(f"all_notes -> {all_notes_pdf}")
    print(f"nutstore -> {nutstore_pdf}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
