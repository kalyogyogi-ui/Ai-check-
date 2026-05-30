#!/usr/bin/env python3
"""Insert supplements into manuscript after base audit script."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "Tokenomics_in_the_Quantum_Age_Complete_Book.md"


def read(name: str) -> str:
    return (ROOT / "supplements" / name).read_text(encoding="utf-8")


def replace_appendix_section(text: str, header: str, new_content: str, next_header: str) -> str:
    pat = rf"(# {re.escape(header)}.*?)(?=\n# {re.escape(next_header)}|\n# Glossary|\Z)"
    if not re.search(pat, text, re.DOTALL):
        return text
    return re.sub(pat, f"# {header}\n\n{new_content.strip()}\n\n", text, count=1, flags=re.DOTALL)


def main() -> None:
    text = BOOK.read_text(encoding="utf-8")

    # Worked example before case analyses
    marker = "## Applying the Framework: Case Analyses"
    if marker in text and "Worked Example: Signature Cost Ratio" not in text:
        text = text.replace(marker, read("worked_scr_example.md") + "\n" + marker)

    # Additional cases after Case 3
    anchor = "Aave's case illustrates a critical insight:"
    if anchor in text and "Case 4: Lido" not in text:
        insert_pos = text.find("## Monte Carlo Methods for Quantum Timeline Uncertainty")
        if insert_pos > 0:
            text = text[:insert_pos] + read("additional_case_studies.md") + "\n\n" + text[insert_pos:]

    # Replace Appendix B body (keep title line handled in replace)
    b = read("appendix_b_expanded.md")
    text = replace_appendix_section(
        text,
        "Appendix B: Quantum Economic Exposure Assessment Template",
        b,
        "Appendix C:",
    )

    c = read("appendix_c_expanded.md")
    text = replace_appendix_section(
        text,
        "Appendix C: Migration Planning Checklist",
        c,
        "Appendix D:",
    )

    # Append Appendix E before Glossary if not present
    if "# Appendix E:" not in text:
        exercises = read("appendix_e_exercises.md")
        gloss = text.find("\n# Glossary")
        if gloss > 0:
            text = text[:gloss] + "\n\n---\n\n" + exercises + "\n\n---\n" + text[gloss:]

    # Tag key statistics in Ch 6 opening if not tagged
    text = text.replace(
        "Approximately 6.04 million bitcoin",
        "Approximately 6.04 million bitcoin *(Data, 2026 — verify via Glassnode or equivalent before print)*",
        1,
    )

    BOOK.write_text(text, encoding="utf-8")
    print(f"Updated {BOOK} ({len(text.split())} words)")


if __name__ == "__main__":
    main()
