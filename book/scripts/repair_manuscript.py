#!/usr/bin/env python3
"""Safe full implementation on manuscript — fixed anchors."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "Tokenomics_in_the_Quantum_Age_Complete_Book.md"
SUPP = ROOT / "supplements"


def r(name: str) -> str:
    return (SUPP / name).read_text(encoding="utf-8")


def load_exercises() -> dict[int, str]:
    raw = r("chapter_exercises_inline.md")
    parts = re.split(r"<!-- CH(\d+) -->", raw)
    return {int(parts[i]): parts[i + 1].strip() + "\n\n" for i in range(1, len(parts), 2)}


def main() -> None:
    text = BOOK.read_text(encoding="utf-8")

    # --- 1. Replace "How to Use" only (keep disclaimer) ---
    text = re.sub(
        r"## How to Use This Edition\n\n.*?(?=\n## Legal and Professional Disclaimer)",
        """## About This Book

Professional readers: protocol engineers, token economists, risk officers, investors, policymakers. Each chapter has **Chapter at a Glance**, **Chapter Exercises**, and **Appendix E** (solutions).

| Label | Meaning |
|-------|---------|
| **(Data, year)** | Verify before print |
| **(Estimate)** | Modelled illustration |
| **(Scenario)** | Stress-test assumption |

**Companion files:** `ART_BRIEF.md`, `FACT_CHECK_MANIFEST.md`, `tools/qri_stress_model.csv`.

""",
        text,
        count=1,
        flags=re.DOTALL,
    )

    # --- 2. Executive Summary after copyright, before About/Legal ---
    if "# Executive Summary" not in text:
        es = r("executive_summary.md") + "\n\n---\n\n"
        text = text.replace(
            "© 2026 Nagnath Savant. All rights reserved.\n\n---\n\n",
            "© 2026 Nagnath Savant. All rights reserved.\n\n---\n\n" + es,
            1,
        )

    # --- 3. Replace TOC block: from # Table of Contents through line before # Preface (real) ---
    preface_idx = text.find("\n# Preface\n")
    toc_idx = text.find("# Table of Contents")
    if toc_idx >= 0 and preface_idx > toc_idx:
        # build new toc
        detailed = ["# Table of Contents", "", "*Detailed outline (H1–H3).*", ""]
        skip = {"Table of Contents", "List of Figures", "List of Tables", "Chapter at a Glance", "Print Table of Contents"}
        body = text[preface_idx:]  # search headings only in body
        for m in re.finditer(r"^(#{1,3})\s+(.+)$", body, re.MULTILINE):
            lv = len(m.group(1))
            title = m.group(2).strip()
            if title in skip or lv > 3:
                continue
            a = re.sub(r"[^\w\s-]", "", title.lower())
            a = re.sub(r"\s+", "-", a)
            detailed.append("  " * (lv - 1) + f"- [{title}](#{a})")
        detailed.append("\n---\n\n")
        print_toc = ["# Print Table of Contents", ""]
        for m in re.finditer(
            r"^# (PART [IVX]+:[^\n]+|Chapter \d+:[^\n]+|Preface|Introduction|Appendix [A-Z]:[^\n]+)$",
            body,
            re.M,
        ):
            t = m.group(1)
            a = re.sub(r"[^\w\s-]", "", t.lower())
            a = re.sub(r"\s+", "-", a)
            print_toc.append(f"- [{t}](#{a})")
        print_toc.append("\n---\n\n")
        lof = """# List of Figures

- Figure 1.1, 1.2, 2.1, 4.1, 5.1, 6.1 (Mermaid in body; print specs in ART_BRIEF.md)

---
# List of Tables

- See chapter tables (1.1, 3.1, 5.2, etc.)

---

"""
        new_front = "\n".join(detailed) + "\n".join(print_toc) + lof
        text = text[:toc_idx] + new_front + text[preface_idx + 1 :]

    # --- 4. Fig 1.1 dedupe ---
    text = re.sub(
        r"(\*Figure 1\.1 — Anatomy of a token economy \(simplified\)\.\*\n\n)"
        r"(?:>\s*\n?>.*?"
        r"(?=\n### Supply Architecture))",
        r"\1",
        text,
        count=1,
        flags=re.DOTALL,
    )

    # --- 5. Mermaid injections ---
    chunks = r("mermaid_figures.md")
    f12 = chunks.split("<!-- FIG 1.2 -->")[1].split("<!-- FIG")[0].strip()
    f41 = chunks.split("<!-- FIG 4.1 -->")[1].split("<!-- FIG")[0].strip()
    f61 = chunks.split("<!-- FIG 6.1 -->")[1].strip()
    m51 = """```mermaid
flowchart LR
  P[2030-2037 scenario window]
  D30[NIST 2030 deprecation]
  D35[NIST 2035 disallowance]
  P --- D30
  P --- D35
```
*Figure 5.1 — CRQC timeline bands (Scenario).*"""

    if "flowchart TB" not in text[text.find("Figure 1.2") : text.find("Figure 1.2") + 500]:
        text = text.replace("> **Figure 1.2: The Hidden Assumptions Stack**", "> **Figure 1.2: The Hidden Assumptions Stack**\n\n" + f12, 1)
    text = re.sub(r"(\*\*\[FIGURE 4\.1:[^\]]+\]\*\*)", r"\1\n\n" + f41, text, count=1)
    text = re.sub(
        r"\*Figure 5\.1: Quantum Threat Probability Distribution \(Conceptual\)\*.*?(?=\n\*Table 5\.2)",
        "*Figure 5.1: Quantum Threat Probability Distribution (Conceptual)*\n\n" + m51 + "\n\n",
        text,
        count=1,
        flags=re.DOTALL,
    )
    text = re.sub(r"\n\*\[Description: A horizontal axis showing years from 2026.*?\]\*\n", "\n", text, flags=re.DOTALL)
    text = re.sub(
        r"\*Figure 6\.1: Quantum Threat Surface Map \(Conceptual\)\*.*?(?=\n## Shor)",
        "*Figure 6.1: Quantum Threat Surface Map (Conceptual)*\n\n" + f61 + "\n\n",
        text,
        count=1,
        flags=re.DOTALL,
    )
    text = re.sub(r"\n\*\[Description: A radial diagram with 'Token Economy'.*?\]\*\n", "\n", text, flags=re.DOTALL)

    # --- 6. Cases 7-9 ---
    if "Case 7: Solana" not in text:
        text = text.replace(
            "## Monte Carlo Methods for Quantum Timeline Uncertainty",
            r("cases_7_9.md").strip() + "\n\n## Monte Carlo Methods for Quantum Timeline Uncertainty",
            1,
        )

    # --- 7. Ch8 cross-ref ---
    ch8 = "# Chapter 8: The Post-Quantum Cryptographic Landscape"
    if "Master Timeline Reference" in text and "Cross-reference:** Institutional" not in text:
        text = text.replace(ch8 + "\n", ch8 + "\n\n> **Cross-reference:** See **Master Timeline Reference** (Chapter 5) for policy dates.\n\n", 1)

    # --- 8. Chapter exercises ---
    parts = re.split(r"(?=^# Chapter \d+:)", text, flags=re.M)
    rebuilt = [parts[0]]
    ex = load_exercises()
    for part in parts[1:]:
        m = re.match(r"^# Chapter (\d+):", part)
        if m and "## Chapter Exercises" not in part:
            n = int(m.group(1))
            if n in ex:
                part = part.rstrip() + "\n\n---\n\n" + ex[n] + "---\n\n"
        rebuilt.append(part)
    text = "".join(rebuilt)

    # --- 9. Appendices F, G ---
    if "# Appendix F:" not in text:
        block = "\n\n---\n\n" + r("appendix_f_raci.md") + "\n\n---\n\n" + r("appendix_g_emc.md") + "\n\n"
        gi = text.find("\n# Glossary")
        if gi > 0:
            text = text[:gi] + block + text[gi:]

    # --- 10. Footnotes ---
    if "## Footnotes" not in text:
        notes = """

---

## Footnotes

[^1]: DefiLlama TVL — verify at https://defillama.com (**Data, year**).
[^2]: NIST FIPS 203–205 (2024).
[^3]: Bitcoin exposed-key stats — replicate on-chain (**Data, 2026**).
[^4]: Google Quantum AI ECDSA estimates — confirm before print.
[^5]: NSM-10 / NIST / CNSA / EU dates — primary legal texts.
[^6]: Chapter 11 cases are **(Scenario)**.

"""
        gi = text.find("\n# Glossary")
        text = text[:gi] + notes + text[gi:] if gi > 0 else text

    # --- 11. Acknowledgments reviewers ---
    if "Pre-publication review" not in text:
        text = text.replace(
            "## Acknowledgments\n",
            "## Acknowledgments\n\n### Pre-publication review (assign before print)\n\n| Role | Reviewer | Affiliation | Date |\n|------|----------|-------------|------|\n| PQC | [Name] | [Institution] | [Date] |\n| Economics | [Name] | [Institution] | [Date] |\n| Policy | [Name] | [Institution] | [Date] |\n\n",
            1,
        )

    # --- 12. Terminology (body only) ---
    lines = []
    for line in text.split("\n"):
        if line.startswith("#"):
            lines.append(line)
        else:
            line = re.sub(r"\bPost-Quantum\b", "post-quantum", line)
            lines.append(line)
    text = "\n".join(lines)
    text = text.replace("# Chapter 8: The post-quantum Cryptographic Landscape", "# Chapter 8: The Post-Quantum Cryptographic Landscape")

    # --- 13. Em-dash ---
    target = int(text.count("—") * 0.34)
    done = 0
    nl = []
    for line in text.split("\n"):
        if done < target and " — " in line and not line.strip().startswith(("#", "|", "```")):
            line, n = re.subn(r" — ", ", ", line, count=2)
            done += n
        nl.append(line)
    text = "\n".join(nl)

    # --- 14. Inline footnote on first DefiLlama preface cite ---
    if "[^1]" not in text[:8000]:
        text = text.replace("[DefiLlama, 2025]", "[DefiLlama, 2025][^1]", 1)

    BOOK.write_text(text, encoding="utf-8")
    Path("/workspace/Tokenomics_in_the_Quantum_Age_Complete_Book.md").write_text(text, encoding="utf-8")

    print("OK words", len(re.findall(r"\b[\w']+\b", text)))
    print("exercises", len(re.findall(r"^## Chapter Exercises", text, re.M)))
    print("cases", len(re.findall(r"^### Case \d+:", text, re.M)))
    print("mermaid", text.count("```mermaid"))
    print("audit meta gone", "independent publishing audit" not in text)
    print("exec summary", "# Executive Summary" in text)
    print("appendix F", "# Appendix F:" in text)


if __name__ == "__main__":
    main()
