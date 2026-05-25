#!/usr/bin/env python3
"""Second pass: stronger author voice, extra figures, phrase cleanup."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CH = ROOT / "manuscript" / "chapters"
AP = ROOT / "manuscript" / "appendices"

EXTRA_SUBS = [
    (r"\btruly staggering\b", "enormous"),
    (r"\bThe scale of cryptographic deployment is truly staggering\b", "Cryptographic deployment operates at enormous scale"),
    (r"\bthis text is designed as a comprehensive reference\b", "We structured this text as a layered reference"),
    (r"\bcomprehensive reference\b", "layered reference"),
    (r"\bcomprehensive treatment\b", "detailed treatment"),
    (r"\bcomprehensive survey\b", "structured survey"),
    (r"\bThe following provides a comprehensive\b", "Below we give a structured"),
    (r"\bThis chapter provides a comprehensive\b", "This chapter gives a structured"),
    (r"\bThis chapter examines\b", "We examine"),
    (r"\bThis chapter surveys\b", "We survey"),
    (r"\bThis chapter develops\b", "We develop"),
    (r"\bThis chapter addresses\b", "We address"),
    (r"\bThis chapter provides\b", "We provide"),
]

# Second figure per chapter (insert before second ## section)
SECOND_FIG = {
    "01-introduction": ("Figure 1.2 — HNDL timeline (author view)", """sequenceDiagram
  participant Attacker
  participant Network
  Attacker->>Network: Record ciphertext today
  Note over Attacker: Store years
  Attacker->>Attacker: Decrypt when CRQC exists"""),
    "11-fips-203-ml-kem": ("Figure 11.2 — FO transform wrapper", """flowchart LR
  CPA[K-PKE IND-CPA] --> FO[FO transform]
  FO --> CCA[ML-KEM IND-CCA2]"""),
    "18-pqc-protocols": ("Figure 18.2 — PKI chain with PQC signatures", """flowchart TB
  Root[Root CA ML-DSA] --> ICA[Issuing CA]
  ICA --> Leaf[Server cert]
  Leaf --> TLS[TLS handshake]"""),
    "19-migration-strategies": ("Figure 19.2 — CBOM-driven migration", """flowchart LR
  CBOM[CBOM inventory] --> RISK[Risk score]
  RISK --> ROAD[Roadmap]"""),
    "20-cbom": ("Figure 20.2 — CBOM in CI/CD", """flowchart LR
  Build[Build pipeline] --> SBOM[SBOM]
  SBOM --> CBOM[CBOM scan]
  CBOM --> Gate[Release gate]"""),
    "02-quantum-computing-fundamentals": ("Figure 2.2 — Quantum circuit abstraction", """flowchart LR
  Init[Initialize] --> U[Unitary gates]
  U --> M[Measure classical bits]"""),
    "03-quantum-attacks": ("Figure 3.2 — Grover impact on AES", """flowchart LR
  AES256[AES-256] --> Eff128[Effective ~128-bit quantum margin]
  AES128[AES-128] --> Eff64[Effective ~64-bit — inadequate]"""),
    "05-lattice-based": ("Figure 5.2 — Module-LWE module view", """flowchart TB
  Rq[Ring R_q] --> Mod[Module rank k]
  Mod --> MLKEM[ML-KEM / ML-DSA]"""),
    "07-hash-based": ("Figure 7.2 — Stateful vs stateless deployment", """flowchart LR
  XMSS[XMSS/LMS stateful] --> FW[Firmware trust anchors]
  SLH[SLH-DSA stateless] --> TLS[General signatures]"""),
    "08-multivariate": ("Figure 8.2 — Rainbow break lesson", """flowchart TD
  Layers[Multiple OV layers] --> Leak[Algebraic structure leak]
  Leak --> Break[Practical key recovery 2022]"""),
    "09-isogeny-based": ("Figure 9.2 — Post-SIDH landscape", """flowchart LR
  SIDH[Broken SIDH/SIKE] --> CSIDH[CSIDH research]
  CSIDH --> SQISign[SQISign signatures]"""),
    "10-nist-standardization": ("Figure 10.2 — Round funnel", """flowchart TD
  R1[69 schemes R1] --> R2[26 R2]
  R2 --> R3[Finalists + breaks]
  R3 --> FIPS[FIPS 203 204 205]"""),
    "13-fips-205-slh-dsa": ("Figure 13.2 — SLH-DSA variant axes (conceptual)", """flowchart LR
  FastF[SHA2-128f fast] --> BigSig[Larger signatures]
  SmallS[SHA2-128s small] --> SlowSig[Slower signing]"""),
    "14-additional-candidates": ("Figure 14.2 — When to reach beyond core FIPS", """flowchart TD
  Q{Need diversity or special size?}
  Q -->|yes| ALT[FN-DSA / HQC / McEliece]
  Q -->|no| CORE[FIPS 203-205 only]"""),
    "17-performance": ("Figure 17.2 — Measurement checklist", """flowchart LR
  HW[Document CPU] --> LIB[Library version]
  LIB --> PCT[Report p50 p99]
  PCT --> NET[Include bytes on wire]"""),
    "22-future-directions": ("Figure 22.2 — Research to production path", """flowchart LR
  Paper[Paper] --> PoC[PoC lib]
  PoC --> Pilot[Pilot]
  Pilot --> Std[Standard]"""),
}

MORE_NOTES: dict[str, list[tuple[str, str]]] = {
    "01-introduction": [
        ("## 1.4", "> **Author's note:** HNDL is the budget unlocker—archived TLS still matters years later.\n\n"),
        ("## 1.7", "> **Author's note:** Indian programs slip on vendor HSM roadmaps more than on lattice theory.\n\n"),
    ],
    "02-quantum-computing-fundamentals": [
        ("## 2.3", "> **Author's note:** Brief executives on **measurement collapse** before gate fidelities—otherwise qubits sound like magic.\n\n"),
    ],
    "04-pqc-overview": [
        ("## 4.2", "> **Author's note:** We keep a **diversity slot** (often SLH-DSA or a code KEM) because monocultures fail in clusters.\n\n"),
    ],
    "06-code-based": [
        ("## 6.2", "> **Author's note:** Classic McEliece keys are a **packet size** problem—validate MTU and CDN limits before edge TLS promises.\n\n"),
    ],
    "11-fips-203-ml-kem": [
        ("## 11.4", "> **Author's note:** Test **implicit rejection**—invalid ciphertexts must not leak via errors or timing.\n\n"),
    ],
    "12-fips-204-ml-dsa": [
        ("## 12.2", "> **Author's note:** Capacity-plan signing for **p99** latency; rejection sampling variance is not noise.\n\n"),
    ],
    "16-implementation": [
        ("## 16.2", "> **Author's note:** We block lattice KEM releases without constant-time NTT—non-negotiable in our reviews.\n\n"),
    ],
    "21-industry-government": [
        ("**India (NCIIPC", "> **Author's note:** Align engineering to **both** NIST timelines and India's NQM/RBI/NCIIPC tracks—not either-or.\n\n"),
    ],
}

SECTION_BRIDGES = {
    "## 1.1 ": "We begin with the societal layer because boards fund **risk stories**, not polynomial rings.\n\n",
    "## 3.1 ": "Classical hardness assumptions are the contract we have been living under—Shor voids that contract for public-key systems.\n\n",
    "## 16.1 ": "Every PQC proof we trust still fails when a single branch leaks key bits—implementation is the real battlefield.\n\n",
}


def insert_once(text: str, anchor: str, block: str) -> str:
    if block.strip() in text:
        return text
    i = text.find(anchor)
    return text if i < 0 else text[:i] + block + text[i:]


def second_section_anchor(text: str) -> str | None:
    secs = re.findall(r"^## \d+\.\d+[^\n]*", text, re.MULTILINE)
    return secs[1] if len(secs) > 1 else None


def process(path: Path):
    t = path.read_text(encoding="utf-8")
    stem = path.stem
    for pat, repl in EXTRA_SUBS:
        t = re.sub(pat, repl, t, flags=re.IGNORECASE)
    for anchor, bridge in SECTION_BRIDGES.items():
        if anchor in t and bridge not in t:
            t = insert_once(t, anchor, bridge)
    for anchor, note in MORE_NOTES.get(stem, []):
        t = insert_once(t, anchor, note)
    if stem in SECOND_FIG:
        cap, mer = SECOND_FIG[stem]
        a2 = second_section_anchor(t)
        if a2:
            block = f"\n**{cap}**\n\n```mermaid\n{mer}\n```\n\n"
            t = insert_once(t, a2, block)
    path.write_text(t, encoding="utf-8")


def process_ap(path: Path):
    t = path.read_text(encoding="utf-8")
    for pat, repl in EXTRA_SUBS:
        t = re.sub(pat, repl, t, flags=re.IGNORECASE)
    if "appendix-a" in path.stem:
        t = insert_once(t, "## A.1", "**Figure A.1 — Mathematical map to PQC chapters**\n\n```mermaid\nflowchart LR\n  NT[Number theory] --> LWE[LWE / lattices]\n  ALG[Abstract algebra] --> NTT[NTT rings]\n  LWE --> MLKEM[ML-KEM ML-DSA]\n```\n\n")
    if "appendix-c" in path.stem:
        t = insert_once(t, "## C.1", "**Figure C.1 — Typical deployment stack**\n\n```mermaid\nflowchart TB\n  App[Application] --> TLS[TLS library]\n  TLS --> liboqs[liboqs / provider]\n  liboqs --> HSM[HSM optional]\n```\n\n")
    path.write_text(t, encoding="utf-8")


def main():
    for p in CH.glob("*.md"):
        process(p)
    for p in AP.glob("*.md"):
        process_ap(p)
    print("Deepen pass complete")


if __name__ == "__main__":
    main()
