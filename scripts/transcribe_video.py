#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


DEFAULT_SOURCE_ROOT = Path(
    "/home/lachlan/ProjectsLFS/YoutubeDownloader/downloads/PLERGeJGfknBTR_nXt5QL88xJF5LhDZBnG"
)
DEFAULT_WHISPER_SCRIPT = Path(
    "/home/lachlan/ProjectsLFS/whisper_with_lang_detect/vad_lang_subtitle.py"
)
DEFAULT_CONDA_ENV = "whisper"
DEFAULT_MODEL = "large-v2"
VIDEO_EXTENSIONS = {".mp4", ".mkv", ".webm", ".m4a", ".mp3"}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Transcribe a single lecture video into repo-local subtitles and "
            "Markdown while preserving the source folder structure."
        )
    )
    parser.add_argument("--video", help="Absolute path to a single source video.")
    parser.add_argument(
        "--print-next",
        action="store_true",
        help="Print the next unprocessed source video and exit.",
    )
    parser.add_argument(
        "--repo-root",
        default=Path(__file__).resolve().parents[1],
        type=Path,
        help="Repository root that will receive markdown/ and subtitles/ outputs.",
    )
    parser.add_argument(
        "--source-root",
        default=DEFAULT_SOURCE_ROOT,
        type=Path,
        help="Root of the organized external lecture video tree.",
    )
    parser.add_argument(
        "--whisper-script",
        default=DEFAULT_WHISPER_SCRIPT,
        type=Path,
        help="Path to the whisper_with_lang_detect subtitle entrypoint.",
    )
    parser.add_argument(
        "--conda-env",
        default=DEFAULT_CONDA_ENV,
        help="Conda environment that can run the Whisper subtitle script.",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help="Whisper model name passed through to whisper_with_lang_detect.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Rebuild outputs even if subtitle and Markdown files already exist.",
    )
    return parser


def iter_videos(source_root: Path) -> list[Path]:
    videos: list[Path] = []
    for path in source_root.rglob("*"):
        if not path.is_file():
            continue
        if path.name.endswith(".part"):
            continue
        if path.suffix.lower() not in VIDEO_EXTENSIONS:
            continue
        videos.append(path)
    return sorted(videos)


def output_paths(repo_root: Path, source_root: Path, video_path: Path) -> tuple[Path, Path, Path]:
    rel = video_path.relative_to(source_root)
    subtitle_path = repo_root / "subtitles" / rel.with_suffix(".srt")
    markdown_path = repo_root / "markdown" / rel.with_suffix(".md")
    work_video = repo_root / ".transcription_tmp" / rel
    return subtitle_path, markdown_path, work_video


def next_unprocessed_video(repo_root: Path, source_root: Path) -> Path | None:
    for video in iter_videos(source_root):
        subtitle_path, markdown_path, _ = output_paths(repo_root, source_root, video)
        if not subtitle_path.exists() or not markdown_path.exists():
            return video
    return None


def clean_text(text: str) -> str:
    return " ".join(text.split())


def render_markdown(entries: list[dict], source_rel: Path) -> str:
    lines = [
        "# Transcript",
        "",
        f"Source: {source_rel.as_posix()}",
        "",
    ]
    for entry in entries:
        text = clean_text(str(entry.get("text", "")))
        if not text:
            continue
        start = str(entry.get("start", "")).strip()
        end = str(entry.get("end", "")).strip()
        lines.append(f"- [{start} - {end}] {text}")
    lines.append("")
    return "\n".join(lines)


def parse_srt_entries(srt_path: Path) -> list[dict]:
    entries: list[dict] = []
    content = srt_path.read_text(encoding="utf-8").strip()
    if not content:
        return entries
    for block in content.split("\n\n"):
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        if len(lines) < 3:
            continue
        if "-->" not in lines[1]:
            continue
        start, end = [part.strip() for part in lines[1].split("-->", 1)]
        text = " ".join(lines[2:])
        entries.append({"start": start, "end": end, "text": text})
    return entries


def cleanup_paths(paths: list[Path]) -> None:
    for path in paths:
        try:
            if path.is_symlink() or path.is_file():
                path.unlink()
        except FileNotFoundError:
            continue


def transcribe_video(
    *,
    repo_root: Path,
    source_root: Path,
    video_path: Path,
    whisper_script: Path,
    conda_env: str,
    model: str,
    force: bool,
) -> tuple[Path, Path]:
    video_path = video_path.resolve()
    source_root = source_root.resolve()
    repo_root = repo_root.resolve()

    if not video_path.is_file():
        raise FileNotFoundError(f"Video not found: {video_path}")
    try:
        source_rel = video_path.relative_to(source_root)
    except ValueError as exc:
        raise ValueError(f"{video_path} is not under source root {source_root}") from exc

    subtitle_path, markdown_path, work_video = output_paths(repo_root, source_root, video_path)
    subtitle_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)

    if subtitle_path.exists() and markdown_path.exists() and not force:
        print(f"SKIP {source_rel.as_posix()}")
        return subtitle_path, markdown_path

    if subtitle_path.exists() and not markdown_path.exists() and not force:
        entries = parse_srt_entries(subtitle_path)
        markdown_path.write_text(render_markdown(entries, source_rel), encoding="utf-8")
        print(f"MARKDOWN {markdown_path}")
        return subtitle_path, markdown_path

    work_video.parent.mkdir(parents=True, exist_ok=True)
    work_srt = work_video.with_suffix(".srt")
    work_json = work_video.with_suffix(".json")
    work_wav = work_video.with_suffix(".wav")

    cleanup_paths([work_video, work_srt, work_json, work_wav])
    work_video.symlink_to(video_path)

    command = [
        "conda",
        "run",
        "-n",
        conda_env,
        "python",
        str(whisper_script),
        "-t",
        str(work_video),
        "--whisper-model",
        model,
    ]

    try:
        subprocess.run(command, check=True)
        if not work_srt.exists():
            raise FileNotFoundError(f"Subtitle output not produced: {work_srt}")
        if not work_json.exists():
            raise FileNotFoundError(f"JSON output not produced: {work_json}")

        entries = json.loads(work_json.read_text(encoding="utf-8"))
        shutil.move(str(work_srt), str(subtitle_path))
        markdown_path.write_text(render_markdown(entries, source_rel), encoding="utf-8")
    finally:
        cleanup_paths([work_video, work_json, work_wav])

    print(f"VIDEO {video_path}")
    print(f"SUBTITLE {subtitle_path}")
    print(f"MARKDOWN {markdown_path}")
    return subtitle_path, markdown_path


def main() -> int:
    args = build_parser().parse_args()

    if args.print_next:
        next_video = next_unprocessed_video(args.repo_root, args.source_root)
        if next_video is not None:
            print(next_video)
        return 0

    if not args.video:
        raise SystemExit("--video is required unless --print-next is used")

    transcribe_video(
        repo_root=args.repo_root,
        source_root=args.source_root,
        video_path=Path(args.video),
        whisper_script=args.whisper_script,
        conda_env=args.conda_env,
        model=args.model,
        force=args.force,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
