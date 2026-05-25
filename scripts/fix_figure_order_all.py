#!/usr/bin/env python3
"""Move figures to after first paragraph in each ## section."""
from __future__ import annotations
import re
from pathlib import Path

CH = Path(__file__).resolve().parents[1] / "manuscript" / "chapters"

FIG = re.compile(
    r"(\*\*Figure [\d.]+ — [^\n]+\*\*\n\n"
    r"(?:(?:```mermaid[\s\S]*?```)|(?:\|[^\n]+\|\n(?:\|[^\n]+\|\n)+))\n\n"
    r"\*[^*]+\*\n\n)",
    re.MULTILINE,
)


def fix_section(body: str) -> str:
    """If figure is first content, move after first paragraph."""
    m = FIG.search(body)
    if not m or m.start() > 20:
        return body
    fig = m.group(1)
    rest = body[: m.start()] + body[m.end() :]
    pm = re.match(r"([^\n#\*][\s\S]*?\n\n)", rest.lstrip())
    if not pm:
        return body
    para = pm.group(1)
    after = rest.lstrip()[pm.end() :]
    return para + fig + after


def fix_chapter(text: str) -> str:
    parts = re.split(r"(^## [^\n]+\n\n)", text, flags=re.MULTILINE)
    if len(parts) < 2:
        return text
    out = [parts[0]]
    i = 1
    while i < len(parts):
        if i + 1 < len(parts):
            out.append(parts[i])
            out.append(fix_section(parts[i + 1]))
            i += 2
        else:
            out.append(parts[i])
            i += 1
    return "".join(out)


def main():
    for p in sorted(CH.glob("*.md")):
        t = p.read_text(encoding="utf-8")
        p.write_text(fix_chapter(t), encoding="utf-8")
    print("Fixed figure order in all chapters")


if __name__ == "__main__":
    main()
