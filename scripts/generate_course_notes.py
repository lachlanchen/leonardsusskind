#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from collections import defaultdict
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from string import Template
from typing import Iterable


VIDEO_EXTS = (".mkv", ".mp4", ".webm")
SEGMENT_RE = re.compile(
    r"^- \[(?P<start>\d\d:\d\d:\d\d,\d{3}) - (?P<end>\d\d:\d\d:\d\d,\d{3})\] (?P<text>.*)$"
)
SRT_TIMESTAMP_RE = re.compile(r"(?P<start>\d\d:\d\d:\d\d,\d{3})\s*-->\s*(?P<end>\d\d:\d\d:\d\d,\d{3})")
LECTURE_NUMBER_RE = re.compile(r"\bLecture\s+(\d+)\b", re.IGNORECASE)
PREFIX_NUMBER_RE = re.compile(r"^(\d+)\s*-\s*")
TEXTTT_RE = re.compile(r"\\texttt\{([^{}]*)\}")
LATEX_SPECIAL_IN_TEXTTT_RE = re.compile(r"(?<!\\)([_%&#$])")

KEYWORD_WEIGHTS = {
    "equation": 5,
    "equals": 3,
    "equal": 2,
    "integral": 4,
    "derivative": 4,
    "lagrangian": 5,
    "hamiltonian": 5,
    "action": 3,
    "matrix": 5,
    "vector": 4,
    "tensor": 5,
    "metric": 5,
    "sigma": 4,
    "psi": 3,
    "wave": 2,
    "state": 2,
    "draw": 4,
    "diagram": 5,
    "graph": 4,
    "plot": 4,
    "circle": 2,
    "arrow": 3,
    "trajectory": 3,
    "orbit": 3,
    "potential": 4,
    "energy": 3,
    "momentum": 3,
    "probability": 3,
    "spin": 3,
    "symmetry": 3,
    "relativity": 2,
    "black hole": 3,
    "horizon": 3,
    "universe": 2,
}

STOPWORDS = {
    "about", "after", "again", "against", "almost", "also", "always", "among", "another",
    "because", "before", "being", "between", "could", "every", "first", "from", "have",
    "here", "into", "itself", "little", "maybe", "might", "other", "over", "really",
    "since", "still", "their", "there", "these", "thing", "think", "those", "through",
    "under", "until", "very", "what", "when", "where", "which", "while", "with", "would",
    "your", "just", "then", "than", "them", "they", "this", "that", "some", "more",
    "such", "like", "only", "onto", "each", "much", "many", "been", "were", "will",
    "shall", "should", "does", "did", "done", "make", "made", "take", "takes",
}

FFMPEG_BINARY_CACHE: str | None = None

REFERENCE_PDF_HINTS = {
    "classical_mechanics": ["Classical_Mechanics"],
    "quantum_mechanics": ["Quantum_Mechanics"],
    "advanced_quantum_mechanics": ["Quantum_Mechanics"],
    "quantum_entanglement": ["Quantum_Mechanics"],
    "special_relativity": ["Special_Relativity_and_Classical_Field"],
    "general_relativity": ["General_Relativity"],
    "cosmology": ["Cosmology"],
    "cosmology_and_black_holes": ["Cosmology"],
    "statistical_mechanics": ["Statistical_Mechanics"],
}


@dataclass
class LectureInfo:
    course_rel: str
    transcript_rel: str
    transcript_path: Path
    subtitle_path: Path
    video_rel: str
    video_path: Path
    lecture_number: int
    lecture_slug: str
    lecture_title: str
    course_title: str
    course_descriptor: str


@dataclass
class FrameSelection:
    asset_path: Path
    timestamp_seconds: float
    source_candidate: str
    recommended_use: str
    rationale: str
    subtitle_excerpt: str
    segment_start_seconds: float
    segment_end_seconds: float
    caption_hint: str


@dataclass
class SubtitleWindow:
    start_seconds: float
    end_seconds: float
    text: str


@dataclass
class FrameCandidate:
    path: Path
    timestamp_seconds: float
    window_start_seconds: float
    window_end_seconds: float
    subtitle_excerpt: str


def humanize_slug(value: str) -> str:
    return value.replace("_", " ").strip().title()


def parse_ts(value: str) -> float:
    hh, mm, rest = value.split(":")
    ss, ms = rest.split(",")
    return int(hh) * 3600 + int(mm) * 60 + int(ss) + int(ms) / 1000.0


def transcript_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def build_task_context(lecture: LectureInfo) -> str:
    return "\n".join(
        [
            f"- Final deliverable: a faithful, mathematically serious chapter for {lecture.course_title}, plus a per-course compiled PDF book.",
            "- Primary source of truth: the matching lecture transcript; preserve its order, rhythm, motivation, and narrative progression.",
            "- Visual evidence: selected lecture frames are only supporting evidence for equations, diagrams, and board layout; do not let them override the transcript.",
            "- Mathematical standard: reconstruct cautiously when the lecture is partial, but avoid generic textbook filler that was not motivated by the lecture.",
            "- Style target: notes should read like polished companion notes in a Susskind-like register, as though the mathematical argument is being unfolded by the lecturer on the page; allow a natural mix of first-person plural, occasional broader third-person or god-view framing, and direct explanatory prose without forcing a rigid persona.",
            "- Structural target: when the lecture naturally raises and resolves a local conceptual obstacle, preserve that rhythm with a standalone `Question & Answer` subsection inside the chapter rather than flattening it away.",
            "- Credit target: keep explicit credit to Leonard Susskind and curation by LazyingArt LLC; reserve the website URL for the generated front-matter credit, not the prose body.",
            "- Output discipline: each prompt stage should solve only its local subtask, but keep the full end goal in mind so downstream stages remain coherent.",
        ]
    )


def parse_source_rel(md_text: str) -> str:
    for line in md_text.splitlines():
        if line.startswith("Source: "):
            return line.split("Source: ", 1)[1].strip()
    raise ValueError("Transcript markdown is missing a Source line")


def strip_stem_label(stem: str) -> str:
    stem = PREFIX_NUMBER_RE.sub("", stem)
    stem = re.sub(r"\s*\[[^\]]+\]\s*$", "", stem)
    stem = stem.replace("｜", ":")
    stem = re.sub(r"\s+", " ", stem).strip()
    return stem


def parse_lecture_number(stem: str) -> int:
    match = LECTURE_NUMBER_RE.search(stem)
    if match:
        return int(match.group(1))
    prefix = PREFIX_NUMBER_RE.match(stem)
    if prefix:
        return int(prefix.group(1))
    return 0


def lecture_slug_from_number(number: int, stem: str) -> str:
    if number > 0:
        return f"lecture_{number:02d}"
    fallback = re.sub(r"[^a-z0-9]+", "_", strip_stem_label(stem).lower()).strip("_")
    return fallback or "lecture"


def build_course_meta(course_rel: str) -> tuple[str, str]:
    parts = Path(course_rel).parts
    track = humanize_slug(parts[0]) if len(parts) > 0 else "Course"
    subject = humanize_slug(parts[1]) if len(parts) > 1 else "Lecture Notes"
    run = humanize_slug(parts[2]) if len(parts) > 2 else ""
    course_title = subject
    course_descriptor = f"{track} track"
    if run:
        course_descriptor = f"{course_descriptor}, {run}"
    return course_title, course_descriptor


def video_files_by_course(source_root: Path) -> dict[str, list[Path]]:
    grouped: dict[str, list[Path]] = defaultdict(list)
    for path in sorted(source_root.rglob("*")):
        if path.is_file() and path.suffix.lower() in VIDEO_EXTS:
            grouped[str(path.parent.relative_to(source_root))].append(path)
    return grouped


def count_files(root: Path, suffix: str) -> int:
    if not root.exists():
        return 0
    return len([p for p in root.iterdir() if p.is_file() and p.suffix.lower() == suffix])


def ordered_courses(course_map: dict[str, list[Path]]) -> list[str]:
    def key(course_rel: str) -> tuple[int, str]:
        parts = Path(course_rel).parts
        bucket = 2
        if parts:
            if parts[0] == "supplementary":
                bucket = 0
            elif parts[0] == "core":
                bucket = 1
        return (bucket, course_rel)

    return sorted(course_map.keys(), key=key)


def eligible_courses(source_root: Path, markdown_root: Path, subtitle_root: Path) -> list[str]:
    grouped = video_files_by_course(source_root)
    eligible: list[str] = []
    for course_rel in ordered_courses(grouped):
        video_count = len(grouped[course_rel])
        md_count = count_files(markdown_root / course_rel, ".md")
        srt_count = count_files(subtitle_root / course_rel, ".srt")
        if video_count > 0 and video_count == md_count == srt_count:
            eligible.append(course_rel)
    return eligible


def lecture_complete(output_root: Path, transcript_rel: str) -> bool:
    lecture = lecture_from_transcript_rel(
        repo_root=output_root.parent,
        source_root=Path("/unused"),
        markdown_root=output_root.parent / "markdown",
        subtitle_root=output_root.parent / "subtitles",
        transcript_rel=transcript_rel,
        source_rel_override=None,
        resolve_video=False,
    )
    pdf_path = output_root / lecture.course_rel / "chapters" / lecture.lecture_slug / "lecture.pdf"
    return pdf_path.exists()


def next_pending_transcript(
    repo_root: Path,
    source_root: Path,
    markdown_root: Path,
    subtitle_root: Path,
    output_root: Path,
    course_rel: str | None,
    allow_partial_course: bool,
) -> str:
    grouped = video_files_by_course(source_root)
    if course_rel:
        courses = [course_rel]
    else:
        courses = eligible_courses(source_root, markdown_root, subtitle_root)

    for current_course in courses:
        if current_course not in grouped:
            continue
        if not allow_partial_course and current_course not in eligible_courses(source_root, markdown_root, subtitle_root):
            continue
        md_dir = markdown_root / current_course
        if not md_dir.exists():
            continue
        for transcript in sorted(md_dir.glob("*.md")):
            transcript_rel = str(transcript.relative_to(markdown_root))
            if not lecture_complete(output_root, transcript_rel):
                return transcript_rel
    return ""


def lecture_from_transcript_rel(
    repo_root: Path,
    source_root: Path,
    markdown_root: Path,
    subtitle_root: Path,
    transcript_rel: str,
    source_rel_override: str | None = None,
    resolve_video: bool = True,
) -> LectureInfo:
    transcript_path = markdown_root / transcript_rel
    md_text = transcript_text(transcript_path)
    source_rel = source_rel_override or parse_source_rel(md_text)
    course_rel = str(Path(transcript_rel).parent)
    stem = transcript_path.stem
    lecture_number = parse_lecture_number(stem)
    lecture_slug = lecture_slug_from_number(lecture_number, stem)
    lecture_title = strip_stem_label(stem)
    course_title, course_descriptor = build_course_meta(course_rel)

    video_path = source_root / source_rel if resolve_video else Path(source_rel)
    subtitle_path = subtitle_root / Path(transcript_rel).with_suffix(".srt")
    return LectureInfo(
        course_rel=course_rel,
        transcript_rel=transcript_rel,
        transcript_path=transcript_path,
        subtitle_path=subtitle_path,
        video_rel=source_rel,
        video_path=video_path,
        lecture_number=lecture_number,
        lecture_slug=lecture_slug,
        lecture_title=lecture_title,
        course_title=course_title,
        course_descriptor=course_descriptor,
    )


def transcript_segments(md_text: str) -> list[tuple[float, str]]:
    segments: list[tuple[float, str]] = []
    for line in md_text.splitlines():
        match = SEGMENT_RE.match(line)
        if match:
            segments.append((parse_ts(match.group("start")), match.group("text").strip()))
    return segments


def subtitle_segments_from_srt(path: Path) -> list[SubtitleWindow]:
    if not path.exists():
        return []

    blocks = re.split(r"\n\s*\n", path.read_text(encoding="utf-8", errors="replace").strip())
    segments: list[SubtitleWindow] = []
    for block in blocks:
        lines = [line.strip("\ufeff").strip() for line in block.splitlines() if line.strip()]
        if len(lines) < 2:
            continue
        timestamp_line = lines[1] if lines[0].isdigit() and len(lines) > 1 else lines[0]
        match = SRT_TIMESTAMP_RE.match(timestamp_line)
        if not match:
            continue
        text_lines = lines[2:] if lines[0].isdigit() and len(lines) > 2 else lines[1:]
        text = re.sub(r"\s+", " ", " ".join(text_lines)).strip()
        if not text:
            continue
        start_seconds = parse_ts(match.group("start"))
        end_seconds = parse_ts(match.group("end"))
        if end_seconds <= start_seconds:
            end_seconds = start_seconds + 0.5
        segments.append(
            SubtitleWindow(
                start_seconds=start_seconds,
                end_seconds=end_seconds,
                text=text,
            )
        )
    return segments


def subtitle_windows_for_lecture(lecture: LectureInfo, md_text: str) -> list[SubtitleWindow]:
    srt_segments = subtitle_segments_from_srt(lecture.subtitle_path)
    if srt_segments:
        return srt_segments

    transcript = transcript_segments(md_text)
    if not transcript:
        return []
    windows: list[SubtitleWindow] = []
    for index, (start_seconds, text) in enumerate(transcript):
        next_start = transcript[index + 1][0] if index + 1 < len(transcript) else start_seconds + 4.0
        end_seconds = max(start_seconds + 0.5, next_start)
        windows.append(
            SubtitleWindow(
                start_seconds=start_seconds,
                end_seconds=end_seconds,
                text=text,
            )
        )
    return windows


def query_terms(lecture: LectureInfo, md_text: str) -> list[str]:
    title_tokens = re.findall(r"[A-Za-z]{4,}", strip_stem_label(lecture.lecture_title).lower())
    transcript_tokens = [
        token
        for token in re.findall(r"[A-Za-z]{4,}", md_text.lower())
        if token not in STOPWORDS
    ]
    counts = Counter(transcript_tokens)
    ranked = [token for token, _count in counts.most_common(20)]
    ordered: list[str] = []
    for token in title_tokens + ranked:
        if token not in ordered:
            ordered.append(token)
    return ordered[:24]


def pdf_reference_candidates(reference_pdf_dir: Path, lecture: LectureInfo) -> list[Path]:
    if not reference_pdf_dir.exists():
        return []
    parts = Path(lecture.course_rel).parts
    subject = parts[1] if len(parts) > 1 else ""
    hints = REFERENCE_PDF_HINTS.get(subject, [])
    matches: list[Path] = []
    for pdf in sorted(reference_pdf_dir.glob("*.pdf")):
        if any(hint in pdf.name for hint in hints):
            matches.append(pdf)
    return matches


def ensure_pdf_text(pdf_path: Path, cache_root: Path) -> Path:
    cache_root.mkdir(parents=True, exist_ok=True)
    txt_path = cache_root / f"{pdf_path.stem}.txt"
    if txt_path.exists():
        return txt_path
    run_command(["pdftotext", str(pdf_path), str(txt_path)])
    return txt_path


def normalize_pdf_paragraphs(text: str) -> list[str]:
    paragraphs: list[str] = []
    current: list[str] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            if current:
                paragraphs.append(" ".join(current))
                current = []
            continue
        current.append(line)
    if current:
        paragraphs.append(" ".join(current))
    cleaned = [re.sub(r"\s+", " ", paragraph).strip() for paragraph in paragraphs]
    return [paragraph for paragraph in cleaned if len(paragraph) > 120]


def collect_reference_excerpt(
    lecture: LectureInfo,
    md_text: str,
    reference_pdf_dir: Path,
    runtime_root: Path,
) -> str:
    pdfs = pdf_reference_candidates(reference_pdf_dir, lecture)
    if not pdfs:
        return "No directly matching Susskind-authored PDF reference is available for this course."

    terms = query_terms(lecture, md_text)
    snippets: list[tuple[int, str, str]] = []
    cache_root = runtime_root / "pdf_text_cache"
    for pdf in pdfs:
        txt_path = ensure_pdf_text(pdf, cache_root)
        text = txt_path.read_text(encoding="utf-8", errors="replace")
        for paragraph in normalize_pdf_paragraphs(text):
            lowered = paragraph.lower()
            score = sum(lowered.count(term) for term in terms)
            if score > 0:
                snippets.append((score, pdf.name, paragraph))

    if not snippets:
        return "Matching Susskind-authored PDFs were found, but no strong topical excerpt was automatically matched for this lecture."

    snippets.sort(key=lambda item: (item[0], len(item[2])), reverse=True)
    selected: list[str] = []
    seen: set[tuple[str, str]] = set()
    total_chars = 0
    for score, pdf_name, paragraph in snippets:
        key = (pdf_name, paragraph)
        if key in seen:
            continue
        formatted = f"[{pdf_name}] {paragraph}"
        if total_chars + len(formatted) > 12000:
            continue
        selected.append(formatted)
        seen.add(key)
        total_chars += len(formatted)
        if len(selected) >= 6:
            break

    if not selected:
        return "Matching Susskind-authored PDFs were found, but no excerpt fit within the current prompt budget."
    return "\n\n".join(selected)


def keyword_score(text: str) -> int:
    lowered = text.lower()
    score = 0
    for keyword, weight in KEYWORD_WEIGHTS.items():
        if keyword in lowered:
            score += weight
    if "=" in text:
        score += 2
    if any(token in lowered for token in ("let's write", "suppose", "consider", "therefore")):
        score += 1
    return score


def trim_excerpt(text: str, limit: int = 220) -> str:
    compact = re.sub(r"\s+", " ", text).strip()
    if len(compact) <= limit:
        return compact
    head = compact[: limit - 3].rsplit(" ", 1)[0].strip()
    return f"{head or compact[: limit - 3]}..."


def window_midpoint(window: SubtitleWindow) -> float:
    return (window.start_seconds + window.end_seconds) / 2.0


def choose_figure_windows(windows: list[SubtitleWindow], max_frames: int) -> list[SubtitleWindow]:
    if not windows:
        return [SubtitleWindow(start_seconds=0.0, end_seconds=4.0, text="Opening lecture context.")]

    min_gap = 90.0
    ranked = sorted(
        enumerate(windows),
        key=lambda item: (keyword_score(item[1].text), len(item[1].text), -item[0]),
        reverse=True,
    )

    selected_indices: list[int] = []
    for index, window in ranked:
        midpoint = window_midpoint(window)
        if all(abs(midpoint - window_midpoint(windows[existing])) >= min_gap for existing in selected_indices):
            selected_indices.append(index)
        if len(selected_indices) >= max_frames:
            break

    if len(selected_indices) < max_frames:
        duration = max(window.end_seconds for window in windows)
        guide_points = [0.05, 0.18, 0.32, 0.48, 0.64, 0.8, 0.93]
        for fraction in guide_points:
            target = duration * fraction
            nearest_index = min(
                range(len(windows)),
                key=lambda idx: abs(window_midpoint(windows[idx]) - target),
            )
            midpoint = window_midpoint(windows[nearest_index])
            if nearest_index in selected_indices:
                continue
            if all(abs(midpoint - window_midpoint(windows[existing])) >= min_gap for existing in selected_indices):
                selected_indices.append(nearest_index)
            if len(selected_indices) >= max_frames:
                break

    if 0 not in selected_indices:
        selected_indices.insert(0, 0)

    ordered = sorted(set(selected_indices), key=lambda idx: windows[idx].start_seconds)
    return [windows[index] for index in ordered[:max_frames]]


def format_seconds(seconds: float) -> str:
    millis = int(round(max(0.0, seconds) * 1000))
    hh, rem = divmod(millis, 3600 * 1000)
    mm, rem = divmod(rem, 60 * 1000)
    ss, ms = divmod(rem, 1000)
    return f"{hh:02d}:{mm:02d}:{ss:02d}.{ms:03d}"


def candidate_timestamps_for_window(window: SubtitleWindow) -> list[float]:
    duration = max(0.6, window.end_seconds - window.start_seconds)
    midpoint = window_midpoint(window)
    if duration <= 1.5:
        raw = [midpoint - 0.35, midpoint - 0.1, midpoint + 0.1, midpoint + 0.35]
    else:
        raw = [
            window.start_seconds + min(duration * 0.12, 0.8),
            window.start_seconds + min(duration * 0.38, max(duration - 0.3, 0.0)),
            window.start_seconds + min(duration * 0.65, max(duration - 0.15, 0.0)),
            window.end_seconds - min(duration * 0.12, 0.6),
        ]

    deduped: list[float] = []
    for timestamp in raw:
        clamped = min(max(window.start_seconds, timestamp), window.end_seconds)
        if all(abs(clamped - existing) >= 0.15 for existing in deduped):
            deduped.append(clamped)
    return deduped or [midpoint]


def run_command(
    cmd: list[str],
    cwd: Path | None = None,
    stdout_path: Path | None = None,
    stderr_path: Path | None = None,
    stdin_text: str | None = None,
    check: bool = True,
) -> subprocess.CompletedProcess[str]:
    stdout_handle = open(stdout_path, "w", encoding="utf-8") if stdout_path else subprocess.PIPE
    stderr_handle = open(stderr_path, "w", encoding="utf-8") if stderr_path else subprocess.PIPE
    try:
        completed = subprocess.run(
            cmd,
            cwd=str(cwd) if cwd else None,
            input=stdin_text,
            text=True,
            stdout=stdout_handle,
            stderr=stderr_handle,
            check=False,
        )
    finally:
        if stdout_path:
            stdout_handle.close()
        if stderr_path:
            stderr_handle.close()

    if check and completed.returncode != 0:
        raise RuntimeError(f"Command failed ({completed.returncode}): {' '.join(cmd)}")
    return completed


def select_ffmpeg_binary() -> str:
    global FFMPEG_BINARY_CACHE
    if FFMPEG_BINARY_CACHE:
        return FFMPEG_BINARY_CACHE

    candidates: list[str] = []
    env_ffmpeg = os.environ.get("FFMPEG_BINARY")
    if env_ffmpeg:
        candidates.append(env_ffmpeg)
    for path in ("/usr/bin/ffmpeg", shutil.which("ffmpeg")):
        if path and path not in candidates:
            candidates.append(path)

    first_existing: str | None = None
    for candidate in candidates:
        if not Path(candidate).exists():
            continue
        if first_existing is None:
            first_existing = candidate
        try:
            completed = subprocess.run(
                [candidate, "-decoders"],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                check=False,
            )
        except OSError:
            continue
        if completed.returncode == 0 and re.search(r"\b(libdav1d|libaom-av1|av1)\b", completed.stdout):
            FFMPEG_BINARY_CACHE = candidate
            return candidate

    if first_existing is None:
        raise RuntimeError("No ffmpeg binary found in PATH or standard locations.")

    FFMPEG_BINARY_CACHE = first_existing
    return first_existing


def extract_window_candidate_frames(
    lecture: LectureInfo,
    runtime_dir: Path,
    window_index: int,
    window: SubtitleWindow,
    force: bool,
) -> list[FrameCandidate]:
    candidates_dir = runtime_dir / "frame_probe_candidates"
    candidates_dir.mkdir(parents=True, exist_ok=True)
    ffmpeg_dir = runtime_dir / "ffmpeg_candidates"
    ffmpeg_dir.mkdir(parents=True, exist_ok=True)

    extracted: list[FrameCandidate] = []
    for candidate_index, timestamp in enumerate(candidate_timestamps_for_window(window), start=1):
        stamp = format_seconds(timestamp).replace(":", "").replace(".", "")
        basename = f"{lecture.lecture_slug}_window_{window_index:02d}_candidate_{candidate_index:02d}_{stamp}.png"
        out_path = candidates_dir / basename
        if force or not out_path.exists():
            ffmpeg_stdout = ffmpeg_dir / f"{basename}.stdout.log"
            ffmpeg_stderr = ffmpeg_dir / f"{basename}.stderr.log"
            cmd = [
                select_ffmpeg_binary(),
                "-y",
                "-loglevel",
                "error",
                "-ss",
                f"{timestamp:.3f}",
                "-i",
                str(lecture.video_path),
                "-frames:v",
                "1",
                str(out_path),
            ]
            run_command(cmd, stdout_path=ffmpeg_stdout, stderr_path=ffmpeg_stderr)
        extracted.append(
            FrameCandidate(
                path=out_path,
                timestamp_seconds=timestamp,
                window_start_seconds=window.start_seconds,
                window_end_seconds=window.end_seconds,
                subtitle_excerpt=trim_excerpt(window.text, limit=320),
            )
        )
    return extracted


def parse_json_payload(text: str) -> dict:
    cleaned = strip_code_fences(text)
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        start = cleaned.find("{")
        end = cleaned.rfind("}")
        if start >= 0 and end > start:
            return json.loads(cleaned[start:end + 1])
        raise


def build_asset_list_text(selections: list[FrameSelection]) -> str:
    lines = []
    for selection in selections:
        lines.append(
            " | ".join(
                [
                    f"- {selection.asset_path.name}",
                    f"frame {format_seconds(selection.timestamp_seconds)}",
                    f"subtitle {format_seconds(selection.segment_start_seconds)}-{format_seconds(selection.segment_end_seconds)}",
                    selection.recommended_use,
                    f"caption hint: {selection.caption_hint or 'none'}",
                    f"subtitle excerpt: {selection.subtitle_excerpt or 'none'}",
                    f"rationale: {selection.rationale or 'none'}",
                ]
            )
        )
    return "\n".join(lines) or "- none"


def cleanup_existing_lecture_figures(figures_dir: Path, lecture_slug: str) -> None:
    for pattern in (f"{lecture_slug}_figure_*.png", f"{lecture_slug}_frame_*.png"):
        for path in figures_dir.glob(pattern):
            if path.is_file():
                path.unlink()


def validate_selected_frames_with_codex(
    repo_root: Path,
    lecture: LectureInfo,
    runtime_dir: Path,
    model: str,
    reasoning: str,
    md_text: str,
    selections: list[FrameSelection],
) -> list[FrameSelection]:
    if not selections:
        return []

    prompt_text = read_template(repo_root / "scripts" / "prompts" / "lecture_notes" / "figure_validation_prompt.txt").substitute(
        task_context=build_task_context(lecture),
        course_title=lecture.course_title,
        course_descriptor=lecture.course_descriptor,
        lecture_title=lecture.lecture_title,
        transcript_rel=lecture.transcript_rel,
        video_rel=lecture.video_rel,
        asset_list=build_asset_list_text(selections),
        transcript_text=md_text,
    )
    validation_path = runtime_dir / "figure_validation.json"
    run_codex_prompt(
        repo_root=repo_root,
        prompt_text=prompt_text,
        output_path=validation_path,
        runtime_dir=runtime_dir,
        log_prefix="figure_validation",
        model=model,
        reasoning=reasoning,
        images=[selection.asset_path for selection in selections],
    )

    try:
        payload = parse_json_payload(validation_path.read_text(encoding="utf-8"))
        decisions = payload.get("decisions", [])
    except Exception:
        return selections

    decision_map = {
        str(item.get("asset", "")).strip(): item
        for item in decisions
        if str(item.get("asset", "")).strip()
    }
    filtered: list[FrameSelection] = []
    for selection in selections:
        verdict = str(decision_map.get(selection.asset_path.name, {}).get("verdict", "accept")).strip().lower()
        if verdict in {"accept", "keep", "use", "pass"}:
            filtered.append(selection)
            continue
        if selection.asset_path.exists():
            selection.asset_path.unlink()

    return filtered


def select_frames_with_codex(
    repo_root: Path,
    lecture: LectureInfo,
    course_root: Path,
    runtime_dir: Path,
    model: str,
    reasoning: str,
    md_text: str,
    max_frames: int,
    force: bool,
) -> list[FrameSelection]:
    figures_dir = course_root / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)
    cleanup_existing_lecture_figures(figures_dir, lecture.lecture_slug)

    windows = choose_figure_windows(subtitle_windows_for_lecture(lecture, md_text), max_frames=max_frames)
    selected: list[FrameSelection] = []
    for window_index, window in enumerate(windows, start=1):
        candidates = extract_window_candidate_frames(
            lecture=lecture,
            runtime_dir=runtime_dir,
            window_index=window_index,
            window=window,
            force=force,
        )
        candidate_map = {candidate.path.name: candidate for candidate in candidates}
        candidate_lines = "\n".join(
            f"- {candidate.path.name} | {format_seconds(candidate.timestamp_seconds)} | subtitle: {candidate.subtitle_excerpt}"
            for candidate in candidates
        )
        selection_path = runtime_dir / f"figure_probe_{window_index:02d}.json"
        prompt_text = read_template(repo_root / "scripts" / "prompts" / "lecture_notes" / "frame_probe_prompt.txt").substitute(
            task_context=build_task_context(lecture),
            course_title=lecture.course_title,
            course_descriptor=lecture.course_descriptor,
            lecture_title=lecture.lecture_title,
            transcript_rel=lecture.transcript_rel,
            video_rel=lecture.video_rel,
            window_index=window_index,
            subtitle_start=format_seconds(window.start_seconds),
            subtitle_end=format_seconds(window.end_seconds),
            subtitle_excerpt=trim_excerpt(window.text, limit=480),
            candidate_list=candidate_lines,
        )
        run_codex_prompt(
            repo_root=repo_root,
            prompt_text=prompt_text,
            output_path=selection_path,
            runtime_dir=runtime_dir,
            log_prefix=f"frame_probe_{window_index:02d}",
            model=model,
            reasoning=reasoning,
            images=[candidate.path for candidate in candidates],
        )

        try:
            payload = parse_json_payload(selection_path.read_text(encoding="utf-8"))
        except Exception:
            payload = {}

        keep = bool(payload.get("keep", True))
        candidate_name = str(payload.get("chosen_candidate", "")).strip()
        if not keep and selected:
            continue
        if candidate_name not in candidate_map:
            fallback_index = min(len(candidates) // 2, len(candidates) - 1)
            candidate_choice = candidates[fallback_index]
        else:
            candidate_choice = candidate_map[candidate_name]
        timestamp_raw = payload.get("timestamp_seconds")
        try:
            timestamp_seconds = float(timestamp_raw) if timestamp_raw is not None else candidate_choice.timestamp_seconds
        except (TypeError, ValueError):
            timestamp_seconds = candidate_choice.timestamp_seconds

        asset_path = figures_dir / f"{lecture.lecture_slug}_figure_{len(selected) + 1:02d}.png"
        shutil.copyfile(candidate_choice.path, asset_path)
        selected.append(
            FrameSelection(
                asset_path=asset_path,
                timestamp_seconds=timestamp_seconds,
                source_candidate=candidate_choice.path.name,
                recommended_use=str(payload.get("recommended_use", "screenshot_plus_equation")).strip() or "screenshot_plus_equation",
                rationale=str(payload.get("reason", "")).strip() or str(payload.get("visible_content", "")).strip(),
                subtitle_excerpt=trim_excerpt(window.text, limit=320),
                segment_start_seconds=window.start_seconds,
                segment_end_seconds=window.end_seconds,
                caption_hint=trim_excerpt(str(payload.get("caption_hint", "")).strip() or window.text, limit=140),
            )
        )
        if len(selected) >= max_frames:
            break

    if not selected:
        fallback_window = windows[0]
        fallback_candidates = extract_window_candidate_frames(
            lecture=lecture,
            runtime_dir=runtime_dir,
            window_index=1,
            window=fallback_window,
            force=force,
        )
        if fallback_candidates:
            fallback_choice = fallback_candidates[min(len(fallback_candidates) // 2, len(fallback_candidates) - 1)]
            asset_path = figures_dir / f"{lecture.lecture_slug}_figure_01.png"
            shutil.copyfile(fallback_choice.path, asset_path)
            selected.append(
                FrameSelection(
                    asset_path=asset_path,
                    timestamp_seconds=fallback_choice.timestamp_seconds,
                    source_candidate=fallback_choice.path.name,
                    recommended_use="screenshot_plus_equation",
                    rationale="Fallback selection without successful figure-probe parse.",
                    subtitle_excerpt=fallback_choice.subtitle_excerpt,
                    segment_start_seconds=fallback_choice.window_start_seconds,
                    segment_end_seconds=fallback_choice.window_end_seconds,
                    caption_hint=trim_excerpt(fallback_choice.subtitle_excerpt, limit=140),
                )
            )

    return selected


def read_template(path: Path) -> Template:
    return Template(path.read_text(encoding="utf-8"))


def strip_code_fences(text: str) -> str:
    stripped = text.strip()
    if stripped.startswith("```"):
        lines = stripped.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        while lines and lines[-1].strip().startswith("```"):
            lines = lines[:-1]
        stripped = "\n".join(lines).strip()
    return stripped


def read_log_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def prompt_failure_summary(stdout_file: Path, stderr_file: Path) -> str:
    combined = "\n".join(part for part in (read_log_text(stdout_file), read_log_text(stderr_file)) if part.strip())
    lines = combined.strip().splitlines()
    return "\n".join(lines[-40:]).strip()


def is_context_overflow_error(text: str) -> bool:
    lowered = text.lower()
    patterns = (
        "ran out of room in the model's context window",
        "exceeds the context window",
        "input exceeds the context window",
        "context_length_exceeded",
        "failed to run pre-sampling compact",
    )
    return any(pattern in lowered for pattern in patterns)


def is_transient_prompt_error(text: str) -> bool:
    lowered = text.lower()
    patterns = (
        "transport channel closed",
        "dns error",
        "failed to lookup address information",
        "worker quit with fatal",
        "timed out",
        "temporarily unavailable",
        "connection reset",
        "connection refused",
        "internal server error",
        "bad gateway",
        "service unavailable",
        "gateway timeout",
    )
    return any(pattern in lowered for pattern in patterns)


def reset_shared_codex_session() -> None:
    session_file = os.environ.get("CODEX_SHARED_SESSION_FILE", "").strip()
    session_doc = os.environ.get("CODEX_SHARED_SESSION_DOC_FILE", "").strip()
    for raw_path in (session_file, session_doc):
        if not raw_path:
            continue
        path = Path(raw_path)
        if path.exists():
            path.unlink()


def run_codex_prompt(
    repo_root: Path,
    prompt_text: str,
    output_path: Path,
    runtime_dir: Path,
    log_prefix: str,
    model: str,
    reasoning: str,
    images: Iterable[Path] = (),
) -> None:
    prompt_file = runtime_dir / f"{log_prefix}.prompt.txt"
    stdout_file = runtime_dir / f"{log_prefix}.stdout.log"
    stderr_file = runtime_dir / f"{log_prefix}.stderr.log"
    temp_output_path = output_path.with_name(f".{output_path.name}.tmp")
    prompt_file.write_text(prompt_text, encoding="utf-8")

    cmd = [
        "bash",
        str(repo_root / "scripts" / "codex_prompt_to_file.sh"),
        str(repo_root),
        str(prompt_file),
        str(temp_output_path),
        model,
        reasoning,
    ]
    for image in images:
        cmd.append(str(image))

    max_attempts = 4
    for attempt in range(1, max_attempts + 1):
        if temp_output_path.exists():
            temp_output_path.unlink()

        completed = run_command(
            cmd,
            cwd=repo_root,
            stdout_path=stdout_file,
            stderr_path=stderr_file,
            stdin_text=prompt_text,
            check=False,
        )
        if completed.returncode == 0 and temp_output_path.exists():
            output_path.write_text(
                strip_code_fences(temp_output_path.read_text(encoding="utf-8")),
                encoding="utf-8",
            )
            temp_output_path.unlink()
            return

        failure_text = prompt_failure_summary(stdout_file, stderr_file)
        if attempt < max_attempts and (is_context_overflow_error(failure_text) or is_transient_prompt_error(failure_text)):
            time.sleep(min(20, 5 * attempt))
            continue

        detail = failure_text or f"exit code {completed.returncode}"
        raise RuntimeError(f"Command failed ({completed.returncode}): {' '.join(cmd)}\n{detail}")


def sanitize_texttt_literals(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        body = LATEX_SPECIAL_IN_TEXTTT_RE.sub(r"\\\1", match.group(1))
        return f"\\texttt{{{body}}}"

    return TEXTTT_RE.sub(repl, text)


def apply_local_compile_fixes(content_path: Path, compile_log: str) -> bool:
    if not content_path.exists():
        return False

    original = content_path.read_text(encoding="utf-8")
    fixed = original

    if "missing $ inserted" in compile_log.lower():
        fixed = sanitize_texttt_literals(fixed)

    if fixed == original:
        return False

    content_path.write_text(fixed, encoding="utf-8")
    return True


def commit_generated_step(
    repo_root: Path,
    runtime_dir: Path,
    log_prefix: str,
    commit_message: str,
    paths: Iterable[Path],
) -> None:
    pathspecs = [str(path.relative_to(repo_root)) for path in paths if path.exists()]
    if not pathspecs:
        return

    stdout_file = runtime_dir / f"{log_prefix}.stdout.log"
    stderr_file = runtime_dir / f"{log_prefix}.stderr.log"
    cmd = [
        "bash",
        str(repo_root / "scripts" / "codex_commit_push.sh"),
        str(repo_root),
        commit_message,
        *pathspecs,
    ]
    run_command(cmd, cwd=repo_root, stdout_path=stdout_file, stderr_path=stderr_file)


def write_metadata(lecture: LectureInfo, lecture_dir: Path, selections: list[FrameSelection]) -> None:
    metadata = {
        "course_rel": lecture.course_rel,
        "transcript_rel": lecture.transcript_rel,
        "video_rel": lecture.video_rel,
        "lecture_number": lecture.lecture_number,
        "lecture_slug": lecture.lecture_slug,
        "lecture_title": lecture.lecture_title,
        "assets": [
            {
                "name": selection.asset_path.name,
                "timestamp_seconds": selection.timestamp_seconds,
                "timestamp_hhmmss": format_seconds(selection.timestamp_seconds),
                "source_candidate": selection.source_candidate,
                "recommended_use": selection.recommended_use,
                "rationale": selection.rationale,
                "subtitle_excerpt": selection.subtitle_excerpt,
                "segment_start_seconds": selection.segment_start_seconds,
                "segment_start_hhmmss": format_seconds(selection.segment_start_seconds),
                "segment_end_seconds": selection.segment_end_seconds,
                "segment_end_hhmmss": format_seconds(selection.segment_end_seconds),
                "caption_hint": selection.caption_hint,
            }
            for selection in selections
        ],
    }
    (lecture_dir / "metadata.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")


def ensure_common_preamble(course_root: Path, template_path: Path) -> None:
    destination = course_root / "common_preamble.tex"
    shutil.copyfile(template_path, destination)


def write_lecture_wrapper(lecture: LectureInfo, lecture_dir: Path) -> None:
    wrapper = f"""\\documentclass[11pt,oneside]{{book}}
\\input{{../../common_preamble.tex}}
\\graphicspath{{{{../../figures/}}{{../../assets/}}}}
\\begin{{document}}
\\frontmatter
\\title{{{lecture.course_title}: {lecture.lecture_title}}}
\\author{{Leonard Susskind}}
\\date{{Transcript-derived notes curated by \\href{{https://lazying.art}}{{LazyingArt LLC}}}}
\\maketitle
\\begin{{center}}
\\small Original lecture by Leonard Susskind. Transcript-derived notes curated by \\href{{https://lazying.art}}{{LazyingArt LLC}}.
\\end{{center}}
\\clearpage
\\mainmatter
\\input{{content.tex}}
\\end{{document}}
"""
    (lecture_dir / "lecture.tex").write_text(wrapper, encoding="utf-8")


def write_course_book(course_root: Path, lecture_entries: list[LectureInfo]) -> None:
    graphics_path = "\\graphicspath{{figures/}{assets/}}\n"
    title_course = lecture_entries[0].course_title if lecture_entries else "Generated Course Notes"
    descriptor = lecture_entries[0].course_descriptor if lecture_entries else ""
    inputs = "\n".join(
        f"\\input{{chapters/{lecture.lecture_slug}/content.tex}}" for lecture in lecture_entries
    )
    content = f"""\\documentclass[11pt,oneside]{{book}}
\\input{{common_preamble.tex}}
{graphics_path}\\begin{{document}}
\\frontmatter
\\title{{{title_course}}}
\\author{{Leonard Susskind}}
\\date{{{descriptor} \\\\ Transcript-derived notes curated by \\href{{https://lazying.art}}{{LazyingArt LLC}}}}
\\maketitle
\\begin{{center}}
\\small Original lectures by Leonard Susskind. Transcript-derived course notes curated by \\href{{https://lazying.art}}{{LazyingArt LLC}}.
\\end{{center}}
\\clearpage
\\tableofcontents
\\mainmatter
{inputs}
\\end{{document}}
"""
    (course_root / "course.tex").write_text(content, encoding="utf-8")


def compile_tex(tex_name: str, cwd: Path, runtime_dir: Path, log_prefix: str, passes: int = 2) -> bool:
    build_dir = cwd / "build"
    build_dir.mkdir(parents=True, exist_ok=True)
    stdout_file = runtime_dir / f"{log_prefix}.stdout.log"
    stderr_file = runtime_dir / f"{log_prefix}.stderr.log"
    stdout_file.write_text("", encoding="utf-8")
    stderr_file.write_text("", encoding="utf-8")
    for _ in range(passes):
        completed = run_command(
            [
                "pdflatex",
                "-interaction=nonstopmode",
                "-halt-on-error",
                "-file-line-error",
                "-output-directory",
                str(build_dir),
                tex_name,
            ],
            cwd=cwd,
            stdout_path=stdout_file,
            stderr_path=stderr_file,
            check=False,
        )
        if completed.returncode != 0:
            return False
    built_pdf = build_dir / f"{Path(tex_name).stem}.pdf"
    final_pdf = cwd / f"{Path(tex_name).stem}.pdf"
    if not built_pdf.exists():
        return False
    if final_pdf.exists():
        final_pdf.unlink()
    shutil.move(str(built_pdf), str(final_pdf))
    return True


def compile_log_excerpt(runtime_dir: Path, log_prefix: str, max_lines: int = 120) -> str:
    stdout_file = runtime_dir / f"{log_prefix}.stdout.log"
    stderr_file = runtime_dir / f"{log_prefix}.stderr.log"
    lines: list[str] = []
    if stdout_file.exists():
        lines.extend(stdout_file.read_text(encoding="utf-8", errors="replace").splitlines())
    if stderr_file.exists():
        lines.extend(stderr_file.read_text(encoding="utf-8", errors="replace").splitlines())
    return "\n".join(lines[-max_lines:])


def fallback_merge_pdf(course_root: Path) -> None:
    chapter_pdfs = sorted(course_root.glob("chapters/*/lecture.pdf"))
    if not chapter_pdfs:
        return
    cmd = ["pdfunite", *[str(path) for path in chapter_pdfs], str(course_root / "course.pdf")]
    run_command(cmd, cwd=course_root)


def cleanup_build_artifacts(root: Path) -> None:
    for pattern in ("*.aux", "*.log", "*.out", "*.toc", "*.synctex.gz"):
        for path in root.glob(pattern):
            if path.is_file():
                path.unlink()


def generate_one_lecture(
    repo_root: Path,
    source_root: Path,
    markdown_root: Path,
    subtitle_root: Path,
    output_root: Path,
    runtime_root: Path,
    prompt_root: Path,
    template_path: Path,
    reference_pdf_dir: Path,
    transcript_rel: str,
    model: str,
    reasoning: str,
    max_frames: int,
    force: bool,
) -> None:
    lecture = lecture_from_transcript_rel(repo_root, source_root, markdown_root, subtitle_root, transcript_rel)
    md_text = transcript_text(lecture.transcript_path)
    lecture_key = f"{lecture.course_rel}/{lecture.lecture_slug}"

    course_root = output_root / lecture.course_rel
    lecture_dir = course_root / "chapters" / lecture.lecture_slug
    lecture_dir.mkdir(parents=True, exist_ok=True)
    course_runtime = runtime_root / lecture.course_rel / lecture.lecture_slug
    course_runtime.mkdir(parents=True, exist_ok=True)

    ensure_common_preamble(course_root, template_path)
    selections = select_frames_with_codex(
        repo_root=repo_root,
        lecture=lecture,
        course_root=course_root,
        runtime_dir=course_runtime,
        model=model,
        reasoning=reasoning,
        md_text=md_text,
        max_frames=max_frames,
        force=force,
    )
    selections = validate_selected_frames_with_codex(
        repo_root=repo_root,
        lecture=lecture,
        runtime_dir=course_runtime,
        model=model,
        reasoning=reasoning,
        md_text=md_text,
        selections=selections,
    )
    assets = [selection.asset_path for selection in selections]
    write_metadata(lecture, lecture_dir, selections)
    print(f"Step complete: extracted frames and metadata for {lecture_key}; committing and pushing.")
    commit_generated_step(
        repo_root=repo_root,
        runtime_dir=course_runtime,
        log_prefix="commit_assets",
        commit_message=f"Add note assets for {lecture_key}",
        paths=[course_root / "common_preamble.tex", course_root / "figures", lecture_dir / "metadata.json"],
    )
    book_reference_text = collect_reference_excerpt(lecture, md_text, reference_pdf_dir, runtime_root)

    asset_list_text = build_asset_list_text(selections)

    figures_markdown_path = lecture_dir / "figures_markdown.md"
    if assets:
        figures_prompt = read_template(prompt_root / "figures_markdown_prompt.txt").substitute(
            task_context=build_task_context(lecture),
            course_title=lecture.course_title,
            course_descriptor=lecture.course_descriptor,
            lecture_title=lecture.lecture_title,
            transcript_rel=lecture.transcript_rel,
            video_rel=lecture.video_rel,
            asset_list=asset_list_text,
            transcript_text=md_text,
        )
        run_codex_prompt(
            repo_root=repo_root,
            prompt_text=figures_prompt,
            output_path=figures_markdown_path,
            runtime_dir=course_runtime,
            log_prefix="figures_markdown",
            model=model,
            reasoning=reasoning,
            images=assets,
        )
    else:
        figures_markdown_path.write_text(
            "\n".join(
                [
                    "# Figure Notes",
                    "## Image Inventory",
                    "No validated mathematical screenshots were kept for this lecture.",
                    "## Blackboard Equations",
                    "No validated blackboard equations were extracted from screenshots.",
                    "## Diagram And Layout Reading",
                    "No validated diagram screenshots were kept.",
                    "## TeX Reconstruction Plan",
                    "Rely on the transcript and cautious standard reconstruction for this lecture.",
                    "## Caption Drafts",
                    "No screenshot captions are needed because no validated screenshots remain.",
                    "## Uncertainties",
                    "The validator rejected the available candidate screenshots as not sufficiently aligned with the lecture content.",
                    "",
                ]
            ),
            encoding="utf-8",
        )
    print(f"Step complete: wrote figure markdown for {lecture_key}; committing and pushing.")
    commit_generated_step(
        repo_root=repo_root,
        runtime_dir=course_runtime,
        log_prefix="commit_figures_markdown",
        commit_message=f"Add figure markdown for {lecture_key}",
        paths=[figures_markdown_path],
    )

    analysis_prompt = read_template(prompt_root / "analysis_prompt.txt").substitute(
        task_context=build_task_context(lecture),
        course_title=lecture.course_title,
        course_descriptor=lecture.course_descriptor,
        lecture_title=lecture.lecture_title,
        transcript_rel=lecture.transcript_rel,
        video_rel=lecture.video_rel,
        asset_list=asset_list_text,
        book_reference_text=book_reference_text,
        figures_markdown_text=figures_markdown_path.read_text(encoding="utf-8"),
        transcript_text=md_text,
    )
    analysis_path = lecture_dir / "analysis.md"
    run_codex_prompt(
        repo_root=repo_root,
        prompt_text=analysis_prompt,
        output_path=analysis_path,
        runtime_dir=course_runtime,
        log_prefix="analysis",
        model=model,
        reasoning=reasoning,
        images=assets,
    )
    print(f"Step complete: wrote chapter plan for {lecture_key}; committing and pushing.")
    commit_generated_step(
        repo_root=repo_root,
        runtime_dir=course_runtime,
        log_prefix="commit_analysis",
        commit_message=f"Add chapter plan for {lecture_key}",
        paths=[analysis_path],
    )

    visual_prompt = read_template(prompt_root / "visual_notes_prompt.txt").substitute(
        task_context=build_task_context(lecture),
        course_title=lecture.course_title,
        course_descriptor=lecture.course_descriptor,
        lecture_title=lecture.lecture_title,
        transcript_rel=lecture.transcript_rel,
        video_rel=lecture.video_rel,
        asset_list=asset_list_text,
        figures_markdown_text=figures_markdown_path.read_text(encoding="utf-8"),
        transcript_text=md_text,
    )
    visual_notes_path = lecture_dir / "visual_notes.md"
    run_codex_prompt(
        repo_root=repo_root,
        prompt_text=visual_prompt,
        output_path=visual_notes_path,
        runtime_dir=course_runtime,
        log_prefix="visual_notes",
        model=model,
        reasoning=reasoning,
        images=assets,
    )
    print(f"Step complete: wrote visual extraction notes for {lecture_key}; committing and pushing.")
    commit_generated_step(
        repo_root=repo_root,
        runtime_dir=course_runtime,
        log_prefix="commit_visual",
        commit_message=f"Add visual notes for {lecture_key}",
        paths=[visual_notes_path],
    )

    narrative_prompt = read_template(prompt_root / "narrative_map_prompt.txt").substitute(
        task_context=build_task_context(lecture),
        course_title=lecture.course_title,
        course_descriptor=lecture.course_descriptor,
        lecture_title=lecture.lecture_title,
        transcript_rel=lecture.transcript_rel,
        video_rel=lecture.video_rel,
        analysis_text=analysis_path.read_text(encoding="utf-8"),
        transcript_text=md_text,
    )
    narrative_map_path = lecture_dir / "narrative_map.md"
    run_codex_prompt(
        repo_root=repo_root,
        prompt_text=narrative_prompt,
        output_path=narrative_map_path,
        runtime_dir=course_runtime,
        log_prefix="narrative_map",
        model=model,
        reasoning=reasoning,
    )
    print(f"Step complete: wrote narrative map for {lecture_key}; committing and pushing.")
    commit_generated_step(
        repo_root=repo_root,
        runtime_dir=course_runtime,
        log_prefix="commit_narrative",
        commit_message=f"Add narrative map for {lecture_key}",
        paths=[narrative_map_path],
    )

    math_bank_prompt = read_template(prompt_root / "math_bank_prompt.txt").substitute(
        task_context=build_task_context(lecture),
        course_title=lecture.course_title,
        course_descriptor=lecture.course_descriptor,
        lecture_title=lecture.lecture_title,
        transcript_rel=lecture.transcript_rel,
        video_rel=lecture.video_rel,
        analysis_text=analysis_path.read_text(encoding="utf-8"),
        figures_markdown_text=figures_markdown_path.read_text(encoding="utf-8"),
        visual_notes_text=visual_notes_path.read_text(encoding="utf-8"),
        transcript_text=md_text,
    )
    math_bank_path = lecture_dir / "math_bank.md"
    run_codex_prompt(
        repo_root=repo_root,
        prompt_text=math_bank_prompt,
        output_path=math_bank_path,
        runtime_dir=course_runtime,
        log_prefix="math_bank",
        model=model,
        reasoning=reasoning,
        images=assets,
    )
    print(f"Step complete: wrote math bank for {lecture_key}; committing and pushing.")
    commit_generated_step(
        repo_root=repo_root,
        runtime_dir=course_runtime,
        log_prefix="commit_math_bank",
        commit_message=f"Add math bank for {lecture_key}",
        paths=[math_bank_path],
    )

    chapter_prompt = read_template(prompt_root / "chapter_tex_prompt.txt").substitute(
        task_context=build_task_context(lecture),
        course_title=lecture.course_title,
        course_descriptor=lecture.course_descriptor,
        lecture_title=lecture.lecture_title,
        lecture_number=lecture.lecture_number,
        transcript_rel=lecture.transcript_rel,
        video_rel=lecture.video_rel,
        asset_list=asset_list_text,
        book_reference_text=book_reference_text,
        analysis_text=analysis_path.read_text(encoding="utf-8"),
        figures_markdown_text=figures_markdown_path.read_text(encoding="utf-8"),
        visual_notes_text=visual_notes_path.read_text(encoding="utf-8"),
        narrative_map_text=narrative_map_path.read_text(encoding="utf-8"),
        math_bank_text=math_bank_path.read_text(encoding="utf-8"),
        transcript_text=md_text,
    )
    draft_path = lecture_dir / "draft.tex"
    run_codex_prompt(
        repo_root=repo_root,
        prompt_text=chapter_prompt,
        output_path=draft_path,
        runtime_dir=course_runtime,
        log_prefix="chapter_draft",
        model=model,
        reasoning=reasoning,
        images=assets,
    )
    print(f"Step complete: wrote chapter draft for {lecture_key}; committing and pushing.")
    commit_generated_step(
        repo_root=repo_root,
        runtime_dir=course_runtime,
        log_prefix="commit_draft",
        commit_message=f"Add chapter draft for {lecture_key}",
        paths=[draft_path],
    )

    refine_prompt = read_template(prompt_root / "refine_chapter_prompt.txt").substitute(
        task_context=build_task_context(lecture),
        course_title=lecture.course_title,
        course_descriptor=lecture.course_descriptor,
        lecture_title=lecture.lecture_title,
        lecture_number=lecture.lecture_number,
        transcript_rel=lecture.transcript_rel,
        video_rel=lecture.video_rel,
        asset_list=asset_list_text,
        analysis_text=analysis_path.read_text(encoding="utf-8"),
        figures_markdown_text=figures_markdown_path.read_text(encoding="utf-8"),
        visual_notes_text=visual_notes_path.read_text(encoding="utf-8"),
        narrative_map_text=narrative_map_path.read_text(encoding="utf-8"),
        math_bank_text=math_bank_path.read_text(encoding="utf-8"),
        draft_tex=draft_path.read_text(encoding="utf-8"),
        transcript_text=md_text,
    )
    content_path = lecture_dir / "content.tex"
    run_codex_prompt(
        repo_root=repo_root,
        prompt_text=refine_prompt,
        output_path=content_path,
        runtime_dir=course_runtime,
        log_prefix="chapter_refine",
        model=model,
        reasoning=reasoning,
        images=assets,
    )
    print(f"Step complete: refined chapter content for {lecture_key}; committing and pushing.")
    commit_generated_step(
        repo_root=repo_root,
        runtime_dir=course_runtime,
        log_prefix="commit_refine",
        commit_message=f"Refine chapter notes for {lecture_key}",
        paths=[content_path],
    )

    write_lecture_wrapper(lecture, lecture_dir)
    if not compile_tex("lecture.tex", lecture_dir, course_runtime, "lecture_compile"):
        compile_log = compile_log_excerpt(course_runtime, "lecture_compile")
        if apply_local_compile_fixes(content_path, compile_log):
            print(f"Step complete: applied local compile fixes for {lecture_key}; committing and pushing.")
            commit_generated_step(
                repo_root=repo_root,
                runtime_dir=course_runtime,
                log_prefix="commit_local_compile_fix",
                commit_message=f"Fix compile blockers for {lecture_key}",
                paths=[content_path],
            )

        if not compile_tex("lecture.tex", lecture_dir, course_runtime, "lecture_compile_local_retry"):
            fix_prompt = read_template(prompt_root / "compile_fix_prompt.txt").substitute(
                task_context=build_task_context(lecture),
                course_title=lecture.course_title,
                lecture_title=lecture.lecture_title,
                transcript_rel=lecture.transcript_rel,
                compile_log=compile_log_excerpt(course_runtime, "lecture_compile_local_retry"),
                current_tex=content_path.read_text(encoding="utf-8"),
            )
            run_codex_prompt(
                repo_root=repo_root,
                prompt_text=fix_prompt,
                output_path=content_path,
                runtime_dir=course_runtime,
                log_prefix="lecture_fix",
                model=model,
                reasoning=reasoning,
            )
            print(f"Step complete: rewrote chapter after compile failure for {lecture_key}; committing and pushing.")
            commit_generated_step(
                repo_root=repo_root,
                runtime_dir=course_runtime,
                log_prefix="commit_prompt_compile_fix",
                commit_message=f"Rewrite compile fix for {lecture_key}",
                paths=[content_path],
            )
            if not compile_tex("lecture.tex", lecture_dir, course_runtime, "lecture_compile_retry"):
                raise RuntimeError(f"Failed to compile lecture chapter: {transcript_rel}")
    cleanup_build_artifacts(lecture_dir)
    print(f"Step complete: compiled lecture PDF for {lecture_key}; committing and pushing.")
    commit_generated_step(
        repo_root=repo_root,
        runtime_dir=course_runtime,
        log_prefix="commit_lecture_pdf",
        commit_message=f"Compile lecture PDF for {lecture_key}",
        paths=[lecture_dir / "lecture.tex", lecture_dir / "lecture.pdf", lecture_dir / "content.tex"],
    )

    lecture_entries = []
    for chapter_dir in sorted((course_root / "chapters").glob("lecture_*")):
        content_file = chapter_dir / "content.tex"
        if not content_file.exists():
            continue
        metadata_file = chapter_dir / "metadata.json"
        if not metadata_file.exists():
            continue
        meta = json.loads(metadata_file.read_text(encoding="utf-8"))
        lecture_entries.append(
            LectureInfo(
                course_rel=lecture.course_rel,
                transcript_rel=meta["transcript_rel"],
                transcript_path=markdown_root / meta["transcript_rel"],
                subtitle_path=subtitle_root / Path(meta["transcript_rel"]).with_suffix(".srt"),
                video_rel=meta["video_rel"],
                video_path=source_root / meta["video_rel"],
                lecture_number=int(meta["lecture_number"]),
                lecture_slug=meta["lecture_slug"],
                lecture_title=meta["lecture_title"],
                course_title=lecture.course_title,
                course_descriptor=lecture.course_descriptor,
            )
        )
    lecture_entries.sort(key=lambda item: (item.lecture_number, item.lecture_slug))
    write_course_book(course_root, lecture_entries)
    if not compile_tex("course.tex", course_root, course_runtime, "course_compile"):
        fallback_merge_pdf(course_root)
    cleanup_build_artifacts(course_root)
    print(f"Step complete: rebuilt course book for {lecture.course_rel}; committing and pushing.")
    commit_generated_step(
        repo_root=repo_root,
        runtime_dir=course_runtime,
        log_prefix="commit_course_pdf",
        commit_message=f"Rebuild course notes for {lecture.course_rel}",
        paths=[course_root / "course.tex", course_root / "course.pdf"],
    )


def parser() -> argparse.ArgumentParser:
    default_repo_root = Path(__file__).resolve().parents[1]
    default_source_root = Path("/home/lachlan/ProjectsLFS/YoutubeDownloader/downloads/PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG")
    default_reference_pdf_dir = Path("/home/lachlan/ProjectsLFS/leonardsusskind/susskind-books-and-lecture-notes")

    parsed = argparse.ArgumentParser(description="Generate transcript-derived TeX lecture notes.")
    parsed.add_argument("--repo-root", type=Path, default=default_repo_root)
    parsed.add_argument("--source-root", type=Path, default=default_source_root)
    parsed.add_argument("--markdown-root", type=Path)
    parsed.add_argument("--subtitle-root", type=Path)
    parsed.add_argument("--output-root", type=Path)
    parsed.add_argument("--runtime-root", type=Path)
    parsed.add_argument("--reference-pdf-dir", type=Path, default=default_reference_pdf_dir)
    parsed.add_argument("--course", help="Restrict to a specific course rel path, e.g. supplementary/advanced_quantum_mechanics/2013_fall")
    parsed.add_argument("--lecture", help="Transcript rel path under markdown/, e.g. core/classical_mechanics/.../114 - ... .md")
    parsed.add_argument("--print-next", action="store_true")
    parsed.add_argument("--model", default="gpt-5.3-codex-spark")
    parsed.add_argument("--reasoning", default="xhigh", choices=["low", "medium", "high", "xhigh"])
    parsed.add_argument("--max-frames", type=int, default=6)
    parsed.add_argument("--allow-partial-course", action="store_true")
    parsed.add_argument("--force", action="store_true")
    return parsed


def main() -> int:
    args = parser().parse_args()

    repo_root = args.repo_root.resolve()
    markdown_root = (args.markdown_root or repo_root / "markdown").resolve()
    subtitle_root = (args.subtitle_root or repo_root / "subtitles").resolve()
    output_root = (args.output_root or repo_root / "generated_course_notes").resolve()
    runtime_root = (args.runtime_root or repo_root / ".lecture-notes-work").resolve()
    prompt_root = repo_root / "scripts" / "prompts" / "lecture_notes"
    template_path = repo_root / "scripts" / "templates" / "lecture_notes_common_preamble.tex"

    if args.print_next:
        next_rel = next_pending_transcript(
            repo_root=repo_root,
            source_root=args.source_root,
            markdown_root=markdown_root,
            subtitle_root=subtitle_root,
            output_root=output_root,
            course_rel=args.course,
            allow_partial_course=args.allow_partial_course,
        )
        if next_rel:
            print(next_rel)
        return 0

    if not args.lecture:
        raise SystemExit("--lecture is required unless --print-next is used")

    generate_one_lecture(
        repo_root=repo_root,
        source_root=args.source_root,
        markdown_root=markdown_root,
        subtitle_root=subtitle_root,
        output_root=output_root,
        runtime_root=runtime_root,
        prompt_root=prompt_root,
        template_path=template_path,
        reference_pdf_dir=args.reference_pdf_dir.resolve(),
        transcript_rel=args.lecture,
        model=args.model,
        reasoning=args.reasoning,
        max_frames=args.max_frames,
        force=args.force,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
