#!/usr/bin/env python3
"""Apply author voice, figures, and notes across manuscript chapters."""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CH = ROOT / "manuscript" / "chapters"
AP = ROOT / "manuscript" / "appendices"

GLOBAL_SUBS = [
    (r"\bIt is important to note that\b", "Note that"),
    (r"\bIt is worth noting that\b", "Note that"),
    (r"\bFurthermore,\b", "Also,"),
    (r"\bMoreover,\b", "Also,"),
    (r"\bIn conclusion,\b", "To sum up,"),
    (r"\btruly staggering\b", "very large"),
    (r"\bThe scale of .+ is truly staggering\.\b", "The scale is enormous."),
    (r"\bThis book provides\b", "This chapter gives"),
    (r"\bthis book\b", "this text"),
    (r"\bcomprehensive exploration\b", "structured tour"),
    (r"\bcomprehensive overview\b", "structured overview"),
    (r"\bcomprehensive guide\b", "practical guide"),
]

# Per-file: (opener_paragraphs, list of (anchor_regex, insert_before_match), closing_author_section)
CHAPTER_META: dict[str, dict] = {}


def load_meta():
    """Metadata keyed by filename stem."""
    return {
        "01-introduction": {
            "opener": """# Chapter 1: Introduction to Cryptography and the Quantum Threat

*Draft voice pass — replace [Author Name] in front matter with your legal name before publication.*

We open this chapter the way we open every executive briefing in India and abroad: not with lattice algebra, but with a plain question—**what breaks, when, and what must you do this quarter?** Cryptography is the trust layer behind UPI rails, GSTN integrations, telco core networks, and the TLS every SaaS product sells as "enterprise-grade." If Shor's algorithm ever runs at cryptographic scale, the RSA and elliptic-curve keys protecting those systems do not degrade gracefully—they fail at once.

Our bias is practical. We explain the mathematics where it drives decisions (key sizes, hybrid TLS, HNDL risk), and we skip theatre about qubit counts that do not change your migration plan. Indian organizations face the same harvest-now-decrypt-later threat as any global bank; they also face tighter budgets, longer vendor refresh cycles, and heterogeneous stacks (mainframe + Kubernetes + mobile SDKs). Keep that lens as you read.

""",
            "inserts": [
                (r"^## 1\.4 The", r"""> **Author's note:** In RBI-regulated and critical-infrastructure workshops we run, HNDL is the argument that finally unlocks budget—not because executives fear quantum computers today, but because **recorded TLS and VPN traffic from 2018 may still matter in 2035**. Treat long-retention data as already at risk if it was encrypted with RSA or (EC)DH.\n\n"""),
                (r"^## 1\.6 What", r"""**Figure 1.1 — Trust stack affected by quantum attacks**

```mermaid
flowchart TB
  subgraph apps [Applications]
    UPI[Payments / APIs]
    Mail[Email / S/MIME]
    VPN[VPN / ZTNA]
  end
  subgraph proto [Protocols]
    TLS[TLS 1.2/1.3]
    SSH[SSH / IPsec]
  end
  subgraph pk [Public-key layer — Shor-vulnerable]
    RSA[RSA signatures & KEX]
    ECC[ECDH / ECDSA / EdDSA]
  end
  subgraph sym [Symmetric — Grover affects strength]
    AES[AES-GCM / ChaCha]
    HASH[SHA-2 / SHA-3]
  end
  apps --> proto --> pk
  proto --> sym
```

"""),
                (r"^## 1\.9 Global", r"""> **Author's note:** NIST standards are not "US-only." Indian procurement and STQC testing cycles increasingly reference FIPS-aligned modules. Plan for **ML-KEM / ML-DSA** as the default upgrade path unless you have a written exception (e.g., ultra-compact signatures).\n\n"""),
            ],
            "closer": """

## 1.12 Author's Closing Perspective

We have watched teams spend months debating qubit timelines while **TLS terminators still offer only RSA certificates**. The useful split is: (1) protect long-lived confidentiality with PQC or hybrid KEX now, (2) rotate signatures on a documented cadence, (3) instrument cryptography so you know what is deployed—topics we develop in Chapters 19–20. Mosca's inequality is not academic for Aadhaar ecosystem data, multi-year litigation holds, or DRDO program archives: if *x + y > z*, you are late.

**What we want you to carry forward:** treat PQC as **infrastructure migration**, not a research novelty. The algorithms exist; the work is inventory, vendors, and disciplined hybrid deployment.

---
""",
        },
    }


def apply_global_subs(text: str) -> str:
    for pat, repl in GLOBAL_SUBS:
        text = re.sub(pat, repl, text, flags=re.IGNORECASE)
    return text


def apply_inserts(text: str, inserts: list) -> str:
    for anchor, block in inserts:
        text = re.sub(anchor, block + r"\g<0>", text, count=1, flags=re.MULTILINE)
    return text


def strip_old_opener(text: str) -> str:
    """Remove title through first ## section (replaced by custom opener)."""
    m = re.search(r"^## \d", text, re.MULTILINE)
    if not m:
        return text
    return text[m.start():]


def strip_old_closer(text: str) -> str:
    text = re.sub(r"\n---\n\n\*Next:.*$", "", text, flags=re.DOTALL)
    text = re.sub(r"\n## 1\.11 Key Takeaways[\s\S]*$", "", text)
    return text.rstrip()


def transform_file(path: Path, meta: dict | None):
    text = path.read_text(encoding="utf-8")
    text = apply_global_subs(text)
    if not meta:
        # appendices: light touch + author framing paragraph
        if not text.startswith("> **Author's note:**"):
            note = "> **Author's note:** Use this appendix as a lab reference—definitions here are deliberately precise; chapters stay narrative.\n\n"
            text = note + text
        path.write_text(text, encoding="utf-8")
        return
    body = strip_old_opener(text)
    body = strip_old_closer(body)
    body = apply_inserts(body, meta.get("inserts", []))
    out = meta["opener"] + body + meta.get("closer", "")
    path.write_text(out, encoding="utf-8")


def main():
    meta_all = load_meta()
    for p in sorted(CH.glob("*.md")):
        transform_file(p, meta_all.get(p.stem))
    for p in sorted(AP.glob("*.md")):
        transform_file(p, None)
    print("Transformed", len(list(CH.glob('*.md'))), "chapters,", len(list(AP.glob('*.md'))), "appendices")


if __name__ == "__main__":
    main()
