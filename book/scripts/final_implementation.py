#!/usr/bin/env python3
"""Complete audit implementation pass on Tokenomics manuscript."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "Tokenomics_in_the_Quantum_Age_Complete_Book.md"
SUPP = ROOT / "supplements"


def read(name: str) -> str:
    return (SUPP / name).read_text(encoding="utf-8")


def load_chapter_exercises() -> dict[int, str]:
    raw = read("chapter_exercises_inline.md")
    parts = re.split(r"<!-- CH(\d+) -->", raw)
    out: dict[int, str] = {}
    for i in range(1, len(parts), 2):
        out[int(parts[i])] = parts[i + 1].strip() + "\n\n"
    return out


def build_print_toc(text: str) -> str:
    lines = [
        "# Print Table of Contents",
        "",
        "*Parts and chapters only. See Detailed Table of Contents for full outline.*",
        "",
    ]
    for m in re.finditer(
        r"^# (PART [IVX]+:[^\n]+|Chapter \d+:[^\n]+|Preface|Introduction|Appendix [A-Z]:[^\n]+)$",
        text,
        re.M,
    ):
        title = m.group(1).strip()
        anchor = re.sub(r"[^\w\s-]", "", title.lower())
        anchor = re.sub(r"\s+", "-", anchor)
        lines.append(f"- [{title}](#{anchor})")
    return "\n".join(lines) + "\n\n---\n\n"


def build_detailed_toc(text: str) -> str:
    lines = ["# Table of Contents", "", "*Detailed digital outline.*", ""]
    skip = {"Table of Contents", "List of Figures", "List of Tables", "Chapter at a Glance", "Print Table of Contents"}
    for m in re.finditer(r"^(#{1,3})\s+(.+)$", text, re.MULTILINE):
        level = len(m.group(1))
        title = m.group(2).strip()
        if title in skip or level > 3:
            continue
        anchor = re.sub(r"[^\w\s-]", "", title.lower())
        anchor = re.sub(r"\s+", "-", anchor)
        lines.append("  " * (level - 1) + f"- [{title}](#{anchor})")
    return "\n".join(lines) + "\n\n---\n\n"


def replace_front_matter(text: str) -> str:
    text = re.sub(
        r"## How to Use This Edition\n.*?(?=\n## Legal and Professional Disclaimer)",
        read("executive_summary.md").split("---")[0]
        + """## About This Book

This edition is for **professional readers**: protocol engineers, token economists, risk officers, investors, and policymakers. Each chapter includes **Chapter at a Glance**, **Chapter Exercises**, and pointers to **Appendix E** (solutions).

| Label | Meaning |
|-------|---------|
| **(Data, year)** | Verify before print |
| **(Estimate)** | Modeled illustration |
| **(Scenario)** | Stress-test assumption |

**Companion files:** `ART_BRIEF.md`, `FACT_CHECK_MANIFEST.md`, `tools/qri_stress_model.csv`.

""",
        text,
        count=1,
        flags=re.DOTALL,
    )
    if "# Executive Summary" not in text:
        es = read("executive_summary.md") + "\n\n---\n\n"
        text = text.replace(
            "## Legal and Professional Disclaimer",
            es + "## Legal and Professional Disclaimer",
            1,
        )
    return text


def replace_toc_block(text: str) -> str:
    start = text.find("# Table of Contents")
    if start < 0:
        return text
    end = text.find("# Preface")
    if end < 0:
        return text
    new_block = build_detailed_toc(text) + build_print_toc(text)
    lof = """# List of Figures

- Figure 1.1 — Anatomy of a token economy (Mermaid)
- Figure 1.2 — Hidden assumptions stack (Mermaid)
- Figure 2.1 — Cryptoeconomic substrate (Mermaid)
- Figure 4.1 — Governance legitimacy pillars (Mermaid)
- Figure 5.1 — CRQC timeline bands (Mermaid, Scenario)
- Figure 6.1 — Quantum threat surface map (Mermaid)

"""
    lot = "# List of Tables\n\n- See chapter tables (1.1, 3.1, 5.2, etc.)\n\n---\n\n"
    return text[:start] + new_block + lof + lot + text[end:]


def remove_figure_11_blockquote(text: str) -> str:
    pat = (
        r"(\*Figure 1\.1 — Anatomy of a token economy \(simplified\)\.\*\n\n)"
        r"(?:>\s*\n?>.*?"
        r"(?=\n### Supply Architecture))"
    )
    return re.sub(pat, r"\1", text, count=1, flags=re.DOTALL)


def inject_mermaid_figures(text: str) -> str:
    chunks = read("mermaid_figures.md")

    def fig(tag: str) -> str:
        return chunks.split(f"<!-- {tag} -->")[1].split("<!-- FIG")[0].strip()

    if "> **Figure 1.2:" in text and "Hidden assumptions" not in text[text.find("Figure 1.2") : text.find("Figure 1.2") + 600]:
        text = text.replace("> **Figure 1.2: The Hidden Assumptions Stack**", "> **Figure 1.2: The Hidden Assumptions Stack**\n\n" + fig("FIG 1.2"), 1)

    if "**[FIGURE 4.1" in text:
        text = re.sub(r"(\*\*\[FIGURE 4\.1:[^\]]+\]\*\*)", r"\1\n\n" + fig("FIG 4.1"), text, count=1)

    m51 = """```mermaid
flowchart LR
  subgraph peak [Scenario window]
    P[2030-2037 peak uncertainty]
  end
  D2030[NIST 2030 deprecation]
  D2035[NIST 2035 disallowance]
  peak --- D2030
  peak --- D2035
```
*Figure 5.1 — CRQC timeline bands (Scenario). See Master Timeline Reference.*"""

    text = re.sub(
        r"\*Figure 5\.1: Quantum Threat Probability Distribution \(Conceptual\)\*.*?"
        r"(?=\n\*Table 5\.2|\n---\n\n# Chapter 6)",
        "*Figure 5.1: Quantum Threat Probability Distribution (Conceptual)*\n\n" + m51 + "\n\n",
        text,
        count=1,
        flags=re.DOTALL,
    )
    text = re.sub(r"\n\*\[Description: A horizontal axis showing years from 2026.*?\]\*\n", "\n", text, flags=re.DOTALL)

    m61 = fig("FIG 6.1")
    text = re.sub(
        r"\*Figure 6\.1: Quantum Threat Surface Map \(Conceptual\)\*.*?"
        r"(?=\n## Shor)",
        "*Figure 6.1: Quantum Threat Surface Map (Conceptual)*\n\n" + m61 + "\n\n",
        text,
        count=1,
        flags=re.DOTALL,
    )
    text = re.sub(r"\n\*\[Description: A radial diagram with 'Token Economy'.*?\]\*\n", "\n", text, flags=re.DOTALL)
    return text


def insert_chapter_exercises(text: str, exercises: dict[int, str]) -> str:
    parts = re.split(r"(?=^# Chapter \d+:)", text, flags=re.MULTILINE)
    out = [parts[0]]
    for part in parts[1:]:
        m = re.match(r"^# Chapter (\d+):", part)
        if not m:
            out.append(part)
            continue
        n = int(m.group(1))
        if "## Chapter Exercises" not in part and n in exercises:
            part = part.rstrip() + "\n\n---\n\n" + exercises[n] + "---\n\n"
        out.append(part)
    return "".join(out)


def insert_cases_7_9(text: str) -> str:
    if "Case 7: Solana" in text:
        return text
    anchor = "## Monte Carlo Methods for Quantum Timeline Uncertainty"
    return text.replace(anchor, read("cases_7_9.md").strip() + "\n\n" + anchor, 1)


def trim_redundancy(text: str) -> str:
    ch8 = "# Chapter 8: The Post-Quantum Cryptographic Landscape"
    note = (
        "\n\n> **Cross-reference:** Institutional deadlines are in the **Master Timeline Reference** (Chapter 5). "
        "This chapter covers algorithm tradeoffs and implementation economics.\n\n"
    )
    if ch8 in text and "Cross-reference:** Institutional deadlines" not in text:
        text = text.replace(ch8 + "\n", ch8 + note, 1)
    text = re.sub(r"(hundreds of billions of dollars\.\s+){2,}", "hundreds of billions of dollars. ", text, flags=re.I)
    return text


def normalize_terminology(text: str) -> str:
    out = []
    for line in text.split("\n"):
        if line.startswith("#"):
            out.append(line)
            continue
        line = line.replace("Post-Quantum Cryptography Standardization", "post-quantum cryptography standardization")
        line = re.sub(r"\bPost-Quantum\b", "post-quantum", line)
        out.append(line)
    text = "\n".join(out)
    text = text.replace("# Chapter 8: The post-quantum Cryptographic Landscape", "# Chapter 8: The Post-Quantum Cryptographic Landscape")
    text = text.replace("# Tokenomics in the post-quantum Age", "# Tokenomics in the Quantum Age")
    return text


def reduce_em_dashes(text: str, fraction: float = 0.35) -> str:
    target = int(text.count("—") * fraction)
    done = 0
    lines = []
    for line in text.split("\n"):
        if done < target and "—" in line and not line.strip().startswith(("#", "|", "```")):
            nl, n = re.subn(r" — ", ", ", line, count=2)
            if n:
                done += min(2, line.count("—"))
                line = nl
        lines.append(line)
    return "\n".join(lines)


def add_footnotes(text: str) -> str:
    if "## Footnotes" in text:
        return text
    notes = """

---

## Footnotes

[^1]: DefiLlama TVL — verify at https://defillama.com (**Data, year**).

[^2]: NIST FIPS 203–205 (2024), ML-KEM, ML-DSA, SLH-DSA.

[^3]: Bitcoin exposed-key statistics — replicate via Glassnode or equivalent (**Data, 2026**).

[^4]: Google Quantum AI / ECDSA resource estimates — confirm citation before print.

[^5]: NSM-10, NIST, CNSA 2.0, EU PQC roadmap — verify in primary legal texts.

[^6]: Chapter 11 case parameters are **(Scenario)** illustrations.

"""
    i = text.find("\n# Glossary")
    return text[:i] + notes + text[i:] if i > 0 else text + notes


def update_acknowledgments(text: str) -> str:
    if "Pre-publication review" in text:
        return text
    block = """
### Pre-publication review (assign before print)

| Role | Reviewer | Affiliation | Date |
|------|----------|-------------|------|
| Post-quantum cryptography | [Name] | [Institution] | [Date] |
| Protocol economics | [Name] | [Institution] | [Date] |
| Financial regulation | [Name] | [Institution] | [Date] |

"""
    return text.replace("## Acknowledgments\n", "## Acknowledgments\n" + block, 1)


def insert_appendices_fg(text: str) -> str:
    if "# Appendix F:" in text:
        return text
    block = "\n\n---\n\n" + read("appendix_f_raci.md") + "\n\n---\n\n" + read("appendix_g_emc.md") + "\n\n"
    i = text.find("\n# Glossary")
    return text[:i] + block + text[i:] if i > 0 else text


def update_manifest() -> None:
    p = ROOT / "FACT_CHECK_MANIFEST.md"
    t = p.read_text(encoding="utf-8")
    if "automated pass" not in t:
        t = t.replace("**OPEN**", "**IN PROGRESS** (2026-05-30)")
        t += "\n\nVerifier: complete F01–F15 against footnotes [^1]–[^6] and `tools/qri_stress_model.csv`.\n"
        p.write_text(t, encoding="utf-8")


def main() -> None:
    text = BOOK.read_text(encoding="utf-8")
    ex = load_chapter_exercises()

    text = replace_front_matter(text)
    text = replace_toc_block(text)
    text = remove_figure_11_blockquote(text)
    text = inject_mermaid_figures(text)
    text = insert_cases_7_9(text)
    text = trim_redundancy(text)
    text = insert_chapter_exercises(text, ex)
    text = normalize_terminology(text)
    text = reduce_em_dashes(text)
    text = update_acknowledgments(text)
    text = add_footnotes(text)
    text = insert_appendices_fg(text)

    BOOK.write_text(text, encoding="utf-8")
    Path("/workspace/Tokenomics_in_the_Quantum_Age_Complete_Book.md").write_text(text, encoding="utf-8")
    update_manifest()

    print("Words:", len(re.findall(r"\b[\w']+\b", text)))
    print("Chapter Exercises:", len(re.findall(r"^## Chapter Exercises", text, re.M)))
    print("Cases:", len(re.findall(r"^### Case \d+:", text, re.M)))
    print("Mermaid:", text.count("```mermaid"))
    print("Em-dash:", text.count("—"))


if __name__ == "__main__":
    main()
