#!/usr/bin/env python3
"""Repair section headings broken by figure insertion."""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CH = ROOT / "manuscript" / "chapters"
UP = Path("/home/ubuntu/.cursor/projects/workspace/uploads")

BROKEN = re.compile(
    r"^(## (\d+\.\d+))\*\*(Figure [^\n]+)\*\*\n\n"
    r"((?:```mermaid[\s\S]*?```\n\n)|(?:\|[^\n]+\|\n(?:\|[^\n]+\|\n)+))"
    r"\*([^*]+)\*\n\n"
    r" ?([^\n#][^\n]*)\n",
    re.MULTILINE,
)


def load_heading_map(stem: str) -> dict[str, str]:
    path = next(UP.glob(f"{stem}_*.md"), None)
    if not path:
        return {}
    out = {}
    for m in re.finditer(r"^(## \d+\.\d+[^\n]*)", path.read_text(encoding="utf-8"), re.MULTILINE):
        num = re.match(r"## (\d+\.\d+)", m.group(1)).group(1)
        out[num] = m.group(1).strip()
    return out


def repair_file(path: Path):
    hmap = load_heading_map(path.stem)
    text = path.read_text(encoding="utf-8")

    def repl(m):
        sec_num = m.group(2)
        caption = m.group(3)
        body = m.group(4)
        ref = m.group(5).strip()
        tail = m.group(6).strip()
        heading = hmap.get(sec_num)
        if not heading:
            if tail and len(tail) > 3:
                heading = f"## {sec_num} {tail}"
            else:
                heading = f"## {sec_num}"
        elif tail and tail not in heading:
            # tail was section title split off
            if not heading.endswith(tail):
                heading = f"## {sec_num} {tail}" if not heading.split(maxsplit=2)[-1] == tail else heading
        fig = f"**{caption}**\n\n{body}*{ref}*\n\n"
        return f"{heading}\n\n{fig}"

    text = BROKEN.sub(repl, text)
    path.write_text(text, encoding="utf-8")


def main():
    for p in sorted(CH.glob("*.md")):
        repair_file(p)
    print("Done")


if __name__ == "__main__":
    main()
