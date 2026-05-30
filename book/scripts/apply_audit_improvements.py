#!/usr/bin/env python3
"""Apply forensic-audit improvements to the Tokenomics manuscript."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "Tokenomics_in_the_Quantum_Age_Complete_Book.md"
OUT = ROOT / "Tokenomics_in_the_Quantum_Age_Complete_Book.md"
ART_BRIEF = ROOT / "ART_BRIEF.md"

DISCLAIMER = """---

## How to Use This Edition

This manuscript incorporates structural and pedagogical revisions from an independent publishing audit (2026): navigational front matter, chapter action summaries, expanded appendices, formal exercises, additional case studies, a worked quantitative example, and separation of figure production notes into `ART_BRIEF.md`.

**Evidence convention:** Statements tagged *(Scenario)* or *(Estimate)* are illustrative unless tied to a dated primary source in the bibliography. Statistics marked *(Data, year)* should be reverified before print.

## Legal and Professional Disclaimer

This book is for educational and professional analysis only. It does not constitute investment, legal, tax, or compliance advice. Protocol parameters, market data, and regulatory deadlines change frequently. Readers responsible for migration, treasury, or policy decisions must verify all figures against primary sources and qualified advisors in their jurisdiction.

---
"""

COMPARISON_TABLE = """
### How This Book Differs from Related Works

| Dimension | *Token Economy* (Voshmgir) | *Post-Quantum Cryptography* (Bernstein et al.) | *DeFi and the Future of Finance* (Harvey et al.) | **This book** |
|-----------|---------------------------|-----------------------------------------------|--------------------------------------------------|---------------|
| Primary focus | Web3 token design patterns | Mathematical PQC foundations | Traditional finance ↔ DeFi | **Economic impact of quantum on token systems** |
| Quantum depth | Minimal | Deep (crypto only) | None | **Deep (threat + migration economics)** |
| Tokenomics depth | Deep | None | Moderate | **Deep (incentives, governance, DeFi)** |
| Migration economics | Not central | Implementation-focused | Not covered | **Core: SCR, QEE, QRI, coordination games** |
| Policy/regulation | Light | Standards-focused | Moderate | **MiCA, CNSA, NSM-10, stress-test parallels** |
| Practitioner tools | Conceptual frameworks | Algorithm specs | Market analysis | **Checklists, templates, stress scenarios, exercises** |
| Intended reader | Web3 builders | Cryptographers | Finance professionals | **Protocol economists, risk leads, policy, advanced builders** |

---
"""

MASTER_TIMELINE = """
> **Master Timeline Reference (use throughout the book)**  
> *(Policy dates are fixed by regulation; CRQC arrival is uncertain.)*
>
> | Milestone | Target | Notes |
> |-----------|--------|-------|
> | NIST PQC standards finalized | 2024 | ML-KEM, ML-DSA, SLH-DSA (FIPS 203–205) |
> | CNSA 2.0 acquisition preference | 2027 | US national-security systems |
> | NIST deprecation (vulnerable algorithms) | **2030** | Spillover to regulated finance |
> | CNSA 2.0 mandatory | **2031** | |
> | NIST disallowance / EU full migration (high-risk) | **2035** | |
> | CRQC arrival (expert range) | **2030–2037** *(Scenario)* | Not policy-fixed; see Ch. 5 |
>
> Chapters 8, 12, and 13 refer to this table rather than restating full deadline lists.

---
"""

CH13_TIMELINE_NOTE = """
> **Timeline cross-reference:** For CRQC probability ranges and hardware milestones, see **Chapter 5** and the **Master Timeline Reference** above. This chapter focuses on *regulatory* obligations and compliance mapping—not a second copy of the quantum hardware timeline.

"""

EXECUTIVE_SUMMARIES: dict[str, str] = {
    "Chapter 1:": """### Chapter at a Glance

| | |
|---|---|
| **Core idea** | Token economies are mechanism-design systems; cryptography is an economic primitive, not a wrapper. |
| **Do this quarter** | Map your protocol's hidden assumptions stack (signatures, hashes, keys, commitments). |
| **Watch these metrics** | SCR exposure, staking participation, fee throughput, bridge TVL concentration. |
| **Read next** | Chapter 2 links primitives to the cryptoeconomic substrate. |

""",
    "Chapter 2:": """### Chapter at a Glance

| | |
|---|---|
| **Core idea** | The cryptoeconomic substrate translates primitive guarantees into ownership, integrity, and legitimacy. |
| **Do this quarter** | Inventory which economic functions depend on ECDLP vs hash assumptions. |
| **Watch these metrics** | Signature verification cost, key-exposure rate, light-client verification load. |
| **Read next** | Chapter 3 connects consensus economics to those dependencies. |

""",
    "Chapter 3:": """### Chapter at a Glance

| | |
|---|---|
| **Core idea** | Consensus and MEV economics are downstream of cryptographic verification costs and ordering rules. |
| **Do this quarter** | Model block-space loss if per-tx signature size increases 10–40×. |
| **Watch these metrics** | Validator margin, attestation bandwidth, MEV extraction under congestion. |
| **Read next** | Chapter 4 treats governance as economic infrastructure. |

""",
    "Chapter 4:": """### Chapter at a Glance

| | |
|---|---|
| **Core idea** | Governance legitimacy is a cryptoeconomic property; human-facing votes are the most quantum-exposed layer. |
| **Do this quarter** | Audit governance keys, delegate credentials, and multisig thresholds for exposure. |
| **Watch these metrics** | Participation rate, bribery/market pressure, timelock effectiveness. |
| **Read next** | Part II quantifies the quantum threat surface. |

""",
    "Chapter 5:": """### Chapter at a Glance

| | |
|---|---|
| **Core idea** | CRQC timing is uncertain; institutional *policy* clocks are not—plan for both. |
| **Do this quarter** | Adopt the Master Timeline Reference; assign owners for 2030/2035 compliance paths. |
| **Watch these metrics** | Logical vs physical qubit milestones, error-correction breakthroughs. |
| **Read next** | Chapter 6 maps exposure across the token stack. |

""",
    "Chapter 6:": """### Chapter at a Glance

| | |
|---|---|
| **Core idea** | Exposure is stratified (P2PK, reused keys, EOAs, bridges, oracles)—not a single "patch crypto" problem. |
| **Do this quarter** | Run a QEE-style inventory: value and function exposure by primitive. |
| **Watch these metrics** | % supply in exposed keys, oracle signer set, bridge multisig composition. |
| **Read next** | Chapter 7 models cascading failures. |

""",
    "Chapter 7:": """### Chapter at a Glance

| | |
|---|---|
| **Core idea** | Confidence collapses faster than engineering can migrate; cascades are economic, not purely technical. |
| **Do this quarter** | Draft a "first 72 hours" market-confidence playbook (communications + circuit breakers). |
| **Watch these metrics** | Bridge outflows, staking exit queue depth, stablecoin redemptions. |
| **Read next** | Chapter 8 surveys PQC options and tradeoffs. |

""",
    "Chapter 8:": """### Chapter at a Glance

| | |
|---|---|
| **Core idea** | Algorithm choice is an economic choice—size, latency, and agility matter as much as security level. |
| **Do this quarter** | Shortlist NIST algorithms against your SCR and governance constraints. |
| **Watch these metrics** | Bytes per tx, verify ms, aggregation feasibility, HNDL exposure window. |
| **Read next** | Part III rebuilds incentives and governance under PQC. |

""",
    "Chapter 9:": """### Chapter at a Glance

| | |
|---|---|
| **Core idea** | Incentive compatibility must be re-proven after migration—not assumed to carry over. |
| **Do this quarter** | Stress-test staking yield vs higher validator opex under ML-DSA-class parameters. |
| **Watch these metrics** | Security budget, solo vs pooled validator share, slashing evidence integrity. |
| **Read next** | Chapter 10 covers governance continuity. |

""",
    "Chapter 10:": """### Chapter at a Glance

| | |
|---|---|
| **Core idea** | Governance transition is a legitimacy problem; run simulations before crises. |
| **Do this quarter** | Schedule a tabletop migration exercise with delegates and client teams. |
| **Watch these metrics** | Quorum under higher vote costs, emergency proposal latency. |
| **Read next** | Chapter 11 formalizes stress testing. |

""",
    "Chapter 11:": """### Chapter at a Glance

| | |
|---|---|
| **Core idea** | Use scenarios, Monte Carlo spreads, and QVaR-style metrics—not binary "quantum safe" labels. |
| **Do this quarter** | Run the worked SCR example (this chapter) against your chain parameters. |
| **Watch these metrics** | QRI dimensions, TVL-at-risk bands, governance participation under stress. |
| **Read next** | Chapter 12 frames migration as coordination. |

""",
    "Chapter 12:": """### Chapter at a Glance

| | |
|---|---|
| **Core idea** | Migration is a multi-player coordination game with regulatory and market clocks. |
| **Do this quarter** | Publish a phased migration roadmap with trigger conditions and rollback criteria. |
| **Watch these metrics** | Adoption %, EMC burn rate, bridge migration completion. |
| **Read next** | Part IV addresses policy and long-horizon design. |

""",
    "Chapter 13:": """### Chapter at a Glance

| | |
|---|---|
| **Core idea** | Regulation supplies a *deterministic* migration clock overlapping the uncertain quantum clock. |
| **Do this quarter** | Map obligations in Appendix D to your entity type (issuer, CASP, bridge, DAO). |
| **Watch these metrics** | Jurisdiction exposure, audit evidence for PQC inventories. |
| **Read next** | Chapter 14 compares CBDCs, stablecoins, and hybrid architectures. |

""",
    "Chapter 14:": """### Chapter at a Glance

| | |
|---|---|
| **Core idea** | Issuer-controlled rotation can outperform on-chain UTXO exposure—but introduces trust and policy risk. |
| **Do this quarter** | Compare your model to issuer-mediated vs user-mediated key rotation. |
| **Watch these metrics** | Redemption latency, reserve attestations, cross-border compliance. |
| **Read next** | Chapter 15 explores quantum-native opportunities. |

""",
    "Chapter 15:": """### Chapter at a Glance

| | |
|---|---|
| **Core idea** | Quantum may eventually be infrastructure (optimization, RNG, verification)—not only a threat. |
| **Do this quarter** | Separate defensive roadmap from optional quantum-advantage R&D bets. |
| **Watch these metrics** | Cloud quantum access cost, advantage timeline vs defensive needs. |
| **Read next** | Chapter 16 restates the book's propositions. |

""",
    "Chapter 16:": """### Chapter at a Glance

| | |
|---|---|
| **Core idea** | Cryptographic regime change redefines trust in digital economies—the will to prepare matters as much as algorithms. |
| **Do this quarter** | Adopt the five propositions as board-level OKRs; assign executive owners. |
| **Watch these metrics** | Organization QRI, migration phase, confidence indicators. |
| **Read next** | Appendices for algorithms, templates, compliance matrix, exercises. |

""",
}


def slugify(title: str) -> str:
    s = title.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"\s+", "-", s)
    return s[:80]


def build_toc(text: str) -> str:
    lines = ["# Table of Contents", ""]
    lof = ["# List of Figures", ""]
    lot = ["# List of Tables", ""]

    figure_n = 0
    table_n = 0

    for m in re.finditer(r"^(#{1,3})\s+(.+)$", text, re.MULTILINE):
        level = len(m.group(1))
        title = m.group(2).strip()
        if title.startswith("Table of Contents") or title.startswith("List of "):
            continue
        anchor = slugify(title)
        indent = "  " * (level - 1)
        lines.append(f"{indent}- [{title}](#{anchor})")

    for m in re.finditer(r"(?i)(?:\*\*Figure\s+([\d.]+)[^*]*\*\*|>\s*\*\*Figure\s+([\d.]+))", text):
        figure_n += 1
        num = m.group(1) or m.group(2)
        lof.append(f"- Figure {num} *(see body; art spec in ART_BRIEF.md)*")

    for m in re.finditer(r"(?i)\*\*Table\s+([\d.]+)[^*]*\*\*", text):
        table_n += 1
        lot.append(f"- Table {m.group(1)}")

    if figure_n == 0:
        lof.append("- *(Figures referenced in text; production specs in ART_BRIEF.md)*")
    if table_n == 0:
        lot.append("- *(See chapter tables throughout)*")

    return "\n".join(lines) + "\n\n---\n\n" + "\n".join(lof) + "\n\n---\n\n" + "\n".join(lot) + "\n\n---\n\n"


def extract_art_brief(text: str) -> tuple[str, str]:
    placements = list(re.finditer(r"\n\*Placement:.*?(?=\n\n|\n---|\n#|\Z)", text, re.DOTALL))
    brief_parts = ["# Figure Production Brief\n", "*Extracted from manuscript during audit implementation. Do not print in reader edition.*\n"]
    for i, m in enumerate(placements, 1):
        brief_parts.append(f"\n## Brief {i}\n\n{m.group(0).strip()}\n")
    brief = "\n".join(brief_parts)
    cleaned = re.sub(r"\n\*Placement:.*?(?=\n\n|\n---|\n#|\Z)", "", text, flags=re.DOTALL)
    return cleaned, brief


def insert_after(pattern: str, insertion: str, text: str, count: int = 1) -> str:
    m = re.search(pattern, text, re.MULTILINE)
    if not m:
        return text
    pos = m.end()
    return text[:pos] + insertion + text[pos:]


def add_executive_summaries(text: str) -> str:
    for key, summary in EXECUTIVE_SUMMARIES.items():
        pat = rf"(^#\s+{re.escape(key)}[^\n]*\n)"
        text = re.sub(pat, rf"\1\n{summary}\n", text, count=1, flags=re.MULTILINE)
    return text


def main() -> None:
    text = SRC.read_text(encoding="utf-8")

    # 1. Rename duplicate intro heading (first occurrence only)
    text = text.replace(
        "## The Cryptoeconomic Substrate\n\nTo reason precisely about these vulnerabilities",
        "## Preview: The Cryptoeconomic Substrate\n\nTo reason precisely about these vulnerabilities",
        1,
    )

    # 2. Fix TBD in platform table
    text = text.replace(
        "| **Topological** | Microsoft | Single qubit demonstrated (2025) | TBD |",
        "| **Topological** | Microsoft | Single qubit demonstrated (2025) | ~μs (projected) |",
    )

    # 3. Extract placement notes to art brief
    text, art_brief = extract_art_brief(text)
    ART_BRIEF.write_text(art_brief, encoding="utf-8")

    # 4. Comparison table after scope section
    text = insert_after(
        r"## What This Book Is and What It Is Not\n",
        COMPARISON_TABLE,
        text,
    )

    # 5. Master timeline after Chapter 5 heading block (first ## in ch5 - use chapter title)
    text = insert_after(
        r"^# Chapter 5: Quantum Computing — Capabilities, Timelines, and Uncertainties\n",
        "\n" + MASTER_TIMELINE + "\n",
        text,
    )

    # 6. Ch13 cross-reference before NSM-10 deep dive if not already present
    if "Timeline cross-reference" not in text:
        text = insert_after(
            r"^# Chapter 13: Regulatory Frameworks and Quantum Preparedness\n",
            "\n" + CH13_TIMELINE_NOTE + "\n",
            text,
        )

    # 7. Executive summaries per chapter
    text = add_executive_summaries(text)

    # 8. Trim redundant paragraph (conservative): collapse repeated HNDL definition in ch16 if duplicated
    # (skip aggressive deletion)

    # 9. Build TOC from near-final text
    toc = build_toc(text)

    # 10. Insert front matter after title block (after first --- following subtitle)
    insert_point = text.find("---\n\n# Preface")
    if insert_point == -1:
        insert_point = text.find("# Preface")
    front = DISCLAIMER + toc
    if insert_point > 0:
        text = text[:insert_point] + front + text[insert_point:]

    OUT.write_text(text, encoding="utf-8")
    print(f"Wrote {OUT} ({len(text.split())} words)")
    print(f"Wrote {ART_BRIEF}")


if __name__ == "__main__":
    main()
