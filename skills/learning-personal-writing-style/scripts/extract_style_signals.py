#!/usr/bin/env python3
"""Extract basic writing-style signals from .txt/.md files.

This script is intentionally lightweight. It does not "learn" a model; it
summarizes measurable hints an agent can combine with close reading.
"""

from __future__ import annotations

import argparse
import collections
import pathlib
import re
import statistics


SENTENCE_SPLIT = re.compile(r"[。！？!?]+")
PARA_SPLIT = re.compile(r"\n\s*\n+")
CN_PHRASE = re.compile(r"[\u4e00-\u9fff]{2,8}")


def read_files(root: pathlib.Path) -> list[tuple[pathlib.Path, str]]:
    files: list[tuple[pathlib.Path, str]] = []
    for path in sorted(root.rglob("*")):
        if path.suffix.lower() not in {".md", ".txt"}:
            continue
        try:
            files.append((path, path.read_text(encoding="utf-8")))
        except UnicodeDecodeError:
            files.append((path, path.read_text(encoding="utf-8", errors="ignore")))
    return files


def clean_markdown(text: str) -> str:
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", text)
    text = re.sub(r"\[[^\]]+\]\([^)]+\)", "", text)
    text = re.sub(r"^#{1,6}\s*", "", text, flags=re.M)
    return text.strip()


def summarize(files: list[tuple[pathlib.Path, str]]) -> str:
    all_text = "\n\n".join(clean_markdown(text) for _, text in files)
    paragraphs = [p.strip() for p in PARA_SPLIT.split(all_text) if p.strip()]
    sentences = [s.strip() for s in SENTENCE_SPLIT.split(all_text) if s.strip()]
    sentence_lengths = [len(s) for s in sentences]
    paragraph_lengths = [len(p) for p in paragraphs]
    punctuation = collections.Counter(ch for ch in all_text if ch in "，。；：！？、,.!?;:")
    phrases = collections.Counter(CN_PHRASE.findall(all_text))
    common_phrases = [(p, c) for p, c in phrases.most_common(40) if c >= 2]

    def avg(values: list[int]) -> str:
        return f"{statistics.mean(values):.1f}" if values else "0"

    lines = [
        "# Style Signal Summary",
        "",
        f"- Files: {len(files)}",
        f"- Paragraphs: {len(paragraphs)}",
        f"- Sentences: {len(sentences)}",
        f"- Average sentence length: {avg(sentence_lengths)} chars",
        f"- Median sentence length: {statistics.median(sentence_lengths) if sentence_lengths else 0} chars",
        f"- Average paragraph length: {avg(paragraph_lengths)} chars",
        "",
        "## Punctuation",
        "",
    ]
    for mark, count in punctuation.most_common():
        lines.append(f"- `{mark}`: {count}")

    lines.extend(["", "## Repeated Chinese Phrases", ""])
    for phrase, count in common_phrases[:30]:
        lines.append(f"- {phrase}: {count}")

    lines.extend(["", "## Files", ""])
    for path, text in files:
        lines.append(f"- {path}: {len(clean_markdown(text))} chars")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract basic style signals from .md/.txt samples.")
    parser.add_argument("sample_dir", type=pathlib.Path)
    parser.add_argument("--output", "-o", type=pathlib.Path)
    args = parser.parse_args()

    if not args.sample_dir.exists():
        raise SystemExit(f"Sample directory not found: {args.sample_dir}")
    files = read_files(args.sample_dir)
    if not files:
        raise SystemExit("No .md or .txt files found.")
    report = summarize(files)
    if args.output:
        args.output.write_text(report, encoding="utf-8")
    else:
        print(report)


if __name__ == "__main__":
    main()
