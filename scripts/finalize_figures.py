#!/usr/bin/env python3
"""Finalize figure placement: repair headings, remove opener duplicates, order section→para→figure."""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CH = ROOT / "manuscript" / "chapters"
UP = Path("/home/ubuntu/.cursor/projects/workspace/uploads")

FIG_BLOCK = re.compile(
    r"\n\*\*(Figure [\d.]+ — [^\n]+)\*\*\n\n"
    r"((?:```mermaid[\s\S]*?```\n\n)|(?:\|[^\n]+\|\n(?:\|[^\n]+\|\n)+))"
    r"\*([^*]+)\*\n\n",
    re.MULTILINE,
)

BROKEN_HEAD = re.compile(
    r"^(## (\d+\.\d+))\*\*(Figure [^\n]+)\*\*\n\n"
    r"((?:```mermaid[\s\S]*?```\n\n)|(?:\|[^\n]+\|\n(?:\|[^\n]+\|\n)+))"
    r"\*([^*]+)\*\n\n"
    r" ?([^\n#][^\n]*)\n",
    re.MULTILINE,
)


def heading_map(stem: str) -> dict[str, str]:
    path = next(UP.glob(f"{stem}_*.md"), None)
    if not path:
        return {}
    m = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            num = re.match(r"## (\d+\.\d+)", line)
            if num:
                m[num.group(1)] = line.strip()
    return m


def repair_broken_headings(text: str, hmap: dict) -> str:
    def repl(m):
        n, cap, body, ref, tail = m.group(2), m.group(3), m.group(4), m.group(5), m.group(6).strip()
        head = hmap.get(n) or (f"## {n} {tail}" if tail else f"## {n}")
        return f"{head}\n\n**{cap}**\n\n{body}*{ref}*\n\n"
    return BROKEN_HEAD.sub(repl, text)


def strip_opener_figures(text: str) -> str:
    """Remove figures between chapter title and first ## section."""
    m = re.search(r"^(# Chapter[^\n]+\n\n)", text, re.MULTILINE)
    if not m:
        return text
    first_sec = re.search(r"^## \d", text, re.MULTILINE)
    if not first_sec:
        return text
    opener = text[m.end() : first_sec.start()]
    cleaned = FIG_BLOCK.sub("\n", opener)
    if cleaned != opener:
        text = text[: m.end()] + cleaned + text[first_sec.start() :]
    return text


def move_figure_after_first_para(text: str) -> str:
    """If figure immediately follows ## heading, move after first paragraph."""
    pattern = re.compile(
        r"^(## \d+\.\d+[^\n]*)\n\n"
        r"(\*\*Figure [\d.]+ —[^\n]+\*\*\n\n"
        r"(?:```mermaid[\s\S]*?```\n\n|(?:\|[^\n]+\|\n)+)"
        r"\*[^*]+\*\n\n)"
        r"((?:[^\n].*\n\n)+?)",
        re.MULTILINE,
    )

    def repl(m):
        head, fig, para = m.group(1), m.group(2), m.group(3)
        if para.strip().startswith("**Figure"):
            return m.group(0)
        return f"{head}\n\n{para}{fig}"

    return pattern.sub(repl, text)


def dedupe_figure_ids(text: str) -> str:
    seen = set()
    def repl(m):
        cap = m.group(1)
        fid = re.search(r"Figure ([\d.]+)", cap)
        if not fid:
            return m.group(0)
        k = fid.group(1)
        if k in seen:
            return "\n"
        seen.add(k)
        return m.group(0)
    return FIG_BLOCK.sub(lambda m: repl(m) if False else m.group(0), text)


def dedupe_figures(text: str) -> str:
    blocks = []
    for m in FIG_BLOCK.finditer(text):
        blocks.append((m.group(0), m.group(1)))
    seen = set()
    for block, cap in reversed(blocks):
        fid = re.search(r"Figure ([\d.]+)", cap)
        if fid and fid.group(1) in seen:
            text = text.replace(block, "\n", 1)
        elif fid:
            seen.add(fid.group(1))
    return text


def process(path: Path):
    hmap = heading_map(path.stem)
    t = path.read_text(encoding="utf-8")
    t = repair_broken_headings(t, hmap)
    t = strip_opener_figures(t)
    t = move_figure_after_first_para(t)
    t = dedupe_figures(t)
    path.write_text(t, encoding="utf-8")


def main():
    for p in sorted(CH.glob("*.md")):
        process(p)
    print("Finalized", len(list(CH.glob("*.md"))), "chapters")


if __name__ == "__main__":
    main()
