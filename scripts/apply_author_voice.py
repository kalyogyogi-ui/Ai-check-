#!/usr/bin/env python3
"""Apply author voice, figures, and notes to all manuscript chapters."""
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
    (r"\bThis book provides\b", "This chapter gives"),
    (r"\bthis book\b", "this text"),
    (r"\bcomprehensive exploration\b", "structured tour"),
    (r"\bcomprehensive overview\b", "structured overview"),
    (r"\bcomprehensive guide\b", "practical guide"),
    (r"\bhas never been greater\b", "is acute"),
]

# Chapter stem -> (subtitle for opener, author focus, default figure caption + mermaid)
CHAPTER_VOICE = {
    "01-introduction": (
        "Cryptography and the Quantum Threat",
        "We frame the quantum threat as a **migration and liability** problem for Indian and global digital infrastructure—not a science-fair project.",
        "Figure 1.1 — Stack at risk under Shor and Grover",
        """flowchart TB
  subgraph vuln [Quantum-vulnerable today]
    RSA[RSA]
    DH[DH / ECDH / ECDSA]
  end
  subgraph ok [Adjust strength only]
    AES[AES / ChaCha]
    SHA[SHA-2 / SHA-3]
  end
  TLS[TLS / SSH / VPN] --> vuln
  TLS --> ok""",
    ),
    "02-quantum-computing-fundamentals": (
        "Quantum Computing Fundamentals",
        "We keep physics intuition where it explains **why Shor wins**; we skip deep Hilbert-space formalism unless you are proving theorems.",
        "Figure 2.1 — Qubit vs classical bit (decision view)",
        """flowchart LR
  C[Classical: one of 2^n states] --> CQ[Deterministic evolution]
  Q[Quantum: superposition] --> QQ[Unitary + measure]
  QQ --> Shor[Enables period finding]""",
    ),
    "03-quantum-attacks": (
        "Shor's and Grover's Algorithms",
        "This is the **kill chain** chapter: which algorithms die, which shrink security margins, and what you must replace first.",
        "Figure 3.1 — Attack map to primitives",
        """flowchart TD
  Shor[Shor polynomial time] --> RSA[RSA factoring]
  Shor --> DLP[Finite-field DLP]
  Shor --> ECDLP[ECDLP]
  Grover[Grover sqrt speedup] --> SYM[Symmetric keys halved effective bits]""",
    ),
    "04-pqc-overview": (
        "Overview of Post-Quantum Cryptography",
        "We compare families the way architects do: **assumption, size, speed, maturity**—not fan-club loyalty.",
        "Figure 4.1 — Family → typical use",
        """flowchart LR
  L[Lattice] --> KEM[ML-KEM / ML-DSA]
  C[Code] --> MCE[McEliece / HQC]
  H[Hash] --> SLH[SLH-DSA / XMSS]
  M[Multivariate] --> UOV[UOV / MAYO eval]
  I[Isogeny] --> EXP[Research signatures]""",
    ),
    "05-lattice-based": (
        "Lattice-Based Cryptography",
        "Lattices won NIST for good reason; we explain **why Module-LWE is the workhorse** without drowning you in geometry.",
        "Figure 5.1 — LWE encryption intuition",
        """flowchart LR
  SK[Secret s] --> PK[t = As + e]
  MSG[Message m] --> CT[ciphertext noisy]
  PK --> CT
  SK --> DEC[Decrypt round]""",
    ),
    "06-code-based": (
        "Code-Based Cryptography",
        "McEliece is the **conservative safe** in the room—huge keys, old confidence. We use it when policy demands assumption diversity.",
        "Figure 6.1 — McEliece encode/decode roles",
        """flowchart LR
  E[Error vector e] --> SYN[s = He]
  PK[Public H] --> ENC[Syndrome / ciphertext]
  SK[Trapdoor Goppa] --> DEC[Decode]""",
    ),
    "07-hash-based": (
        "Hash-Based Signatures",
        "Hash signatures trade size for **minimal assumptions**—excellent for roots of trust if you respect state.",
        "Figure 7.1 — Merkle tree signature flow",
        """flowchart TB
  OTS[One-time keys leaves] --> TREE[Merkle root in pubkey]
  SIGN[Sign with leaf OTS] --> PROOF[Auth path]
  PROOF --> VERIFY[Verify to root]""",
    ),
    "08-multivariate": (
        "Multivariate Polynomial Cryptography",
        "Rainbow's break is a lesson in **structure leaks**; UOV survives because boring can be good.",
        "Figure 8.1 — Oil and vinegar partition",
        """flowchart LR
  V[Vinegar variables] --> LIN[Linear in oil after fix v]
  O[Oil variables] --> SOLVE[Solve small system]""",
    ),
    "09-isogeny-based": (
        "Isogeny-Based Cryptography",
        "SIDH taught us that **published torsion can be lethal**; we document survivors and label them experimental.",
        "Figure 9.1 — SIDH break lesson (conceptual)",
        """flowchart TD
  PUB[Publish auxiliary torsion] --> ATT[Castryck-Decru 2022]
  ATT --> DEAD[SIDH/SIKE broken]
  CSIDH[CSIDH: no torsion leak] --> OPEN[Still debated quantum cost]""",
    ),
    "10-nist-standardization": (
        "The NIST Post-Quantum Standardization Process",
        "NIST's process is the **global clock** for procurement—even when your data never leaves India.",
        "Figure 10.1 — NIST PQC phases",
        """timeline
  title NIST PQC (high level)
  2016 : Competition announced
  2022 : Rainbow SIKE breaks
  2024 : FIPS 203 204 205
  2025+ : FN-DSA HQC tracks""",
    ),
    "11-fips-203-ml-kem": (
        "FIPS 203 — ML-KEM",
        "We walk ML-KEM the way implementers need: **K-PKE, FO transform, implicit rejection**—with constant-time warnings baked in.",
        "Figure 11.1 — ML-KEM encaps/decaps",
        """sequenceDiagram
  participant A as Sender
  participant B as Receiver
  A->>B: ciphertext c
  Note over A,B: K = KDF(m) or KDF(z) on failure
  B->>B: Re-encrypt check FO""",
    ),
    "12-fips-204-ml-dsa": (
        "FIPS 204 — ML-DSA",
        "Rejection sampling is not a detail—it is **the reason ML-DSA is secure**. Budget signing latency accordingly.",
        "Figure 12.1 — Fiat–Shamir with aborts",
        """flowchart TD
  Y[Sample masking y] --> Z[Compute z = y + c s]
  Z -->|norm ok| OUT[Output signature]
  Z -->|reject| Y""",
    ),
    "13-fips-205-slh-dsa": (
        "FIPS 205 — SLH-DSA",
        "SLH-DSA is our choice when we want **hash-only assumptions** and can pay signature bytes.",
        "Figure 13.1 — SLH-DSA hypertree sketch",
        """flowchart TB
  FORS[FORS few-time sigs] --> WOTS[WOTS+ chains]
  WOTS --> HT[Hypertree layers]
  HT --> ROOT[Root in public key]""",
    ),
    "14-additional-candidates": (
        "Additional Candidates and Round 4 Algorithms",
        "Standards are not finished—**diversity algorithms** matter for insurance, not for day-one TLS.",
        "Figure 14.1 — Portfolio beyond FIPS 203–205",
        """flowchart LR
  CORE[FIPS 203 204 205] --> DIV[Diversity layer]
  DIV --> FN[FN-DSA]
  DIV --> HQC[HQC KEM]
  DIV --> MCE[Classic McEliece]""",
    ),
    "15-hybrid-schemes": (
        "Hybrid Cryptographic Schemes",
        "Hybrids are our default recommendation for production TLS until you have a written reason not to.",
        "Figure 15.1 — Hybrid shared secret combiner",
        """flowchart LR
  C1[X25519 ss] --> HKDF[HKDF-Extract/Expand]
  C2[ML-KEM-768 ss] --> HKDF
  HKDF --> KEYS[TLS handshake keys]""",
    ),
    "16-implementation": (
        "Implementation and Side-Channel Resistance",
        "Theory is IND-CCA; production is **constant-time or bust**. We have seen lattice leaks from careless NTT loops.",
        "Figure 16.1 — Implementation threat model",
        """flowchart TD
  CODE[Crypto code] --> TIME[Timing cache]
  CODE --> POWER[Power EM]
  LEAK[Leak bits] --> LATTICE[Lattice recovery]
  TIME --> LEAK
  POWER --> LEAK""",
    ),
    "17-performance": (
        "Performance Analysis and Benchmarking",
        "Never trust a microsecond table without **CPU, library version, and percentile**—we publish our methodology before our winners.",
        "Figure 17.1 — Benchmark dimensions",
        """flowchart LR
  CPU[Platform] --> LAT[Latency percentiles]
  CPU --> SIZE[Bytes on wire]
  SIZE --> COST[Cloud egress $]""",
    ),
    "18-pqc-protocols": (
        "PQC in TLS, PKI, and Network Protocols",
        "Protocols are where PQC wins or loses: **cert chains, UDP MTU, middleboxes**—especially on Indian mobile paths.",
        "Figure 18.1 — TLS 1.3 hybrid placement",
        """sequenceDiagram
  participant C as Client
  participant S as Server
  C->>S: ClientHello key_share hybrid
  S->>C: ServerHello + cert chain PQC sig""",
    ),
    "19-migration-strategies": (
        "Cryptographic Agility and Migration Strategies",
        "Migration is a **program**, not a library upgrade. We sequence discover → pilot → mandate → retire.",
        "Figure 19.1 — Migration program phases",
        """flowchart LR
  D[Discover] --> P[Prioritize HNDL]
  P --> I[Pilot hybrid]
  I --> S[Scale]
  S --> R[Retire RSA ECC]""",
    ),
    "20-cbom": (
        "Cryptographic Bill of Materials (CBOM)",
        "If you cannot list your algorithms, you cannot claim PQC readiness—CBOM is the **bill of health** for crypto debt.",
        "Figure 20.1 — CBOM data model",
        """flowchart TB
  APP[Application] --> LIB[Crypto library]
  LIB --> ALG[Algorithms + params]
  ALG --> QV[Quantum vulnerability flag]""",
    ),
    "21-industry-government": (
        "Industry and Government PQC Initiatives",
        "Policy sets deadlines; **your stack sets feasibility**. We map global mandates and India's parallel track.",
        "Figure 21.1 — Policy → engineering feedback loop",
        """flowchart LR
  POL[NIST FIPS / CNSA / EU] --> PROC[Procurement]
  PROC --> ENG[Engineering CBOM]
  ENG --> AUDIT[Audit evidence]""",
    ),
    "22-future-directions": (
        "Future Directions and Open Problems",
        "Standards froze **first-generation** PQC; research on FHE, ZK, and leaner signatures continues—read this chapter to avoid surprise.",
        "Figure 22.1 — Research → future standards funnel",
        """flowchart TD
  R[Research prototypes] --> E[Industry pilots]
  E --> N[NIST additional calls]
  N --> F[Future FIPS]""",
    ),
}

INDIA_NOTE = (
    "> **Author's note (India deployment):** Validate any regulatory reference "
    "(RBI, MeitY, CERT-In, DPDP retention) against the **current circular** before "
    "you bake it into contracts. We describe directionally what we see in the field, "
    "not legal advice.\n\n"
)

AUTHOR_NOTES = {
    "01-introduction": [
        ("## 1.4", "> **Author's note:** HNDL is the budget unlocker—archived TLS matters for years."),
        ("## 1.7", "> **Author's note:** Vendor refresh cycles dominate Indian timelines more than qubit counts."),
    ],
    "03-quantum-attacks": [("## 3.2", "> **Author's note:** Treat Shor-vulnerable keys as **expired** once CRQC exists—plan backward from data lifetime.")],
    "10-nist-standardization": [("## 10.3", "> **Author's note:** SIKE's weekend break is our board-slide cautionary tale.")],
    "15-hybrid-schemes": [("## 15.1", "> **Author's note:** Measure hybrid overhead on **your** POPs; Indian mobile RTT amplifies byte costs.")],
    "16-implementation": [("## 16.2", "> **Author's note:** We refuse greenfield lattice code without side-channel review—use audited libraries (liboqs, vendor HSM paths).")],
    "17-performance": [("## 17.2", "> **Author's note:** Report p50 **and** p99 for ML-DSA signing; means lie.")],
    "19-migration-strategies": [("## 19.2", "> **Author's note:** Agility means **ops can change algorithms** without a monolith redeploy.")],
    "21-industry-government": [("**India (NCIIPC", INDIA_NOTE)],
}


def get_title_line(text: str) -> str:
    m = re.match(r"^# Chapter \d+:\s*(.+)$", text, re.MULTILINE)
    return m.group(1).strip() if m else "Chapter"


def strip_header_and_footer(text: str) -> str:
    m = re.search(r"^## ", text, re.MULTILINE)
    if m:
        text = text[m.start():]
    text = re.sub(r"\n---\n\n\*Next:.*$", "", text, flags=re.DOTALL)
    text = re.sub(r"\n## \d+\.\d+ Key Takeaways[\s\S]*?(?=\n---|\Z)", "", text)
    text = re.sub(r"\n\*This concludes.*$", "", text, flags=re.DOTALL)
    return text.rstrip()


def make_opener(stem: str, ch_num: int) -> str:
    meta = CHAPTER_VOICE.get(stem)
    if meta:
        subtitle, focus, fig_cap, mermaid = meta
        title = f"Chapter {ch_num}: {subtitle}"
    else:
        title = get_title_line(Path(CH / f"{stem}.md").read_text(encoding="utf-8") if (CH / f"{stem}.md").exists() else "#")
        focus = "We connect theory to decisions you can defend in architecture review."
        fig_cap, mermaid = "Figure — Chapter overview", "flowchart LR\n  A[Read] --> B[Apply]"

    fig_block = f"**{fig_cap}**\n\n```mermaid\n{mermaid}\n```\n\n"
    return f"""# {title}

{focus}

{INDIA_NOTE if ch_num in (1, 18, 19, 21) else ""}{fig_block}---

"""


def make_closer(stem: str, ch_num: int) -> str:
    return f"""
---

## {ch_num}.99 Author's Closing Perspective

We have used this chapter in live architecture reviews: the question is never "is the math beautiful?" but **"what do we deploy Monday, with what fallback?"** Keep a written record of assumptions (hybrid on/off, parameter sets, library versions) so auditors—and future you—know why choices were made.

If you only act on one idea from Chapter {ch_num}, make it the figure at the top: turn it into a checklist for your environment.

---
"""


def insert_after_anchor(text: str, anchor: str, block: str) -> str:
    if anchor not in text:
        return text
    if block.strip() in text:
        return text
    idx = text.find(anchor)
    return text[:idx] + block + text[idx:]


def process_chapter(path: Path):
    stem = path.stem
    ch_num = int(stem.split("-")[0])
    raw = path.read_text(encoding="utf-8")
    for pat, repl in GLOBAL_SUBS:
        raw = re.sub(pat, repl, raw, flags=re.IGNORECASE)
    body = strip_header_and_footer(raw)
    opener = make_opener(stem, ch_num)
    closer = make_closer(stem, ch_num)
    for anchor, note in AUTHOR_NOTES.get(stem, []):
        body = insert_after_anchor(body, anchor, note + "\n\n")
    # Default mid-chapter note if none
    if stem not in AUTHOR_NOTES:
        m = re.search(r"^## \d+\.\d+", body, re.MULTILINE)
        if m:
            body = insert_after_anchor(
                body,
                body[m.start() : body.find("\n", m.start())],
                "> **Author's note:** When in doubt, **pilot hybrid TLS** on internal services first; external customer impact is where rollback plans matter.\n\n",
            )
    path.write_text(opener + body + closer, encoding="utf-8")


def process_appendix(path: Path):
    text = path.read_text(encoding="utf-8")
    for pat, repl in GLOBAL_SUBS:
        text = re.sub(pat, repl, text, flags=re.IGNORECASE)
    name = path.stem.replace("appendix-", "").upper()
    intro = f"""> **Author's note:** Appendix {name} is reference material—use it beside the narrative chapters, not instead of them.

"""
    if not text.startswith("> **Author's note:**"):
        text = intro + text
    path.write_text(text, encoding="utf-8")


def main():
    for p in sorted(CH.glob("*.md")):
        process_chapter(p)
    for p in sorted(AP.glob("*.md")):
        process_appendix(p)
    print("Done:", len(list(CH.glob("*.md"))), "chapters")


if __name__ == "__main__":
    main()
