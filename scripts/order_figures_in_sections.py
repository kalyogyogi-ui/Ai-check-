#!/usr/bin/env python3
"""Place each figure after the first paragraph of its section."""
from __future__ import annotations
import re
from pathlib import Path

CH = Path(__file__).resolve().parents[1] / "manuscript" / "chapters"

FIGURE_BLOCK = re.compile(
    r"\n(\*\*Figure [\d.]+ — [^\n]+\*\*\n\n"
    r"(?:(?:\|[^\n]+\|\n)+|```mermaid[\s\S]*?```\n\n)+"
    r"\*[^*]+\*\n\n)",
    re.MULTILINE,
)


def split_sections(text: str) -> list[tuple[str, str]]:
    """Return list of (heading_line, body) for each ## section."""
    parts = re.split(r"(^## [^\n]+\n\n)", text, flags=re.MULTILINE)
    out = []
    if parts[0]:
        out.append(("", parts[0]))
    i = 1
    while i < len(parts):
        if i + 1 < len(parts):
            out.append((parts[i], parts[i + 1]))
            i += 2
        else:
            out.append((parts[i], ""))
            i += 1
    return out


def first_paragraph(body: str) -> tuple[str, str, str]:
    """Return (before, first_para, after) where first_para ends at double newline."""
    m = re.match(r"(\*\*Figure[\s\S]*?(?=\n(?:[^\n#]|\*\*Figure)))?", body)
    # Remove leading figure if present
    body = FIGURE_BLOCK.sub("", body, count=1).lstrip()
    m = re.match(r"([\s\S]*?\n\n)", body)
    if not m:
        return "", "", body
    return "", m.group(1), body[m.end() :]


def reorder_section(body: str) -> str:
    fig_m = FIGURE_BLOCK.search(body)
    if not fig_m:
        return body
    fig = fig_m.group(1)
    rest = body[: fig_m.start()] + body[fig_m.end() :]
    _, para, after = first_paragraph(rest)
    if not para.strip():
        return fig + rest
    return para + fig + after


def strip_pre_section_figures(text: str) -> str:
    m = re.search(r"^## \d", text, re.MULTILINE)
    if not m:
        return text
    head, tail = text[: m.start()], text[m.start() :]
    head = FIGURE_BLOCK.sub("\n", head)
    return head + tail


def process(text: str) -> str:
    text = strip_pre_section_figures(text)
    sections = split_sections(text)
    rebuilt = []
    for heading, body in sections:
        if heading.startswith("## "):
            body = reorder_section(body)
        rebuilt.append(heading + body)
    return "".join(rebuilt)


def main():
    for p in sorted(CH.glob("*.md")):
        t = p.read_text(encoding="utf-8")
        p.write_text(process(t), encoding="utf-8")
    print("Ordered figures in sections")


if __name__ == "__main__":
    main()
