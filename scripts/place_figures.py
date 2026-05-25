#!/usr/bin/env python3
"""Place figures inside correct sections with captions and in-text references."""
from __future__ import annotations
import re
from pathlib import Path

from figure_registry import FIGURES, block_mermaid

ROOT = Path(__file__).resolve().parents[1]
CH = ROOT / "manuscript" / "chapters"

FIGURE_BLOCK_RE = re.compile(
    r"\n\*\*Figure [^\n]+\*\*\n\n(?:```mermaid[\s\S]*?```\n\n|(?:\|[^\n]+\|\n)+(?:\n\|[^\n]+\|\n)*\n\n)",
    re.MULTILINE,
)

# Extend registry for all chapters (section = heading prefix)
EXTRA = {
    "04-pqc-overview": [
        ("## 4.2", "4.1", "Figure 4.1 — PQC algorithm families and typical roles",
         "Figure 4.1 is our family picker for standards committees and architecture boards.",
         block_mermaid("flowchart TB\n  L[Lattice] --> KEM[ML-KEM]\n  L --> SIG[ML-DSA]\n  C[Code] --> HQC[HQC / McEliece]\n  H[Hash] --> SLH[SLH-DSA]")),
        ("## 4.3", "4.2", "Figure 4.2 — Size/speed trade-off axes (conceptual)",
         "Figure 4.2 reminds teams that **bytes on the wire** often dominate Indian mobile latency more than CPU.",
         block_mermaid("flowchart LR\n  SIZE[Smaller keys/certs] --- SPEED[Faster verify]\n  LATTICE[Lattice] --> BAL[Balanced default]\n  HASH[Hash sigs] --> LARGE[Large signatures]")),
    ],
    "05-lattice-based": [
        ("## 5.2", "5.1", "Figure 5.1 — LWE public-key formation",
         "Figure 5.1 is the mental model for ML-KEM key generation: noisy linear structure hides the secret.",
         block_mermaid("flowchart LR\n  s[Secret s] --> t[t = As + e]\n  A[Public A] --> t\n  t --> pk[Public key]")),
        ("## 5.4", "5.2", "Figure 5.2 — Module rank k in ML-KEM",
         "Figure 5.2: increasing module rank k raises dimension without changing the ring R_q.",
         block_mermaid("flowchart TB\n  Rq[Ring Z_q[X]/(X^256+1)] --> Mod[Module dimension k]\n  Mod --> K512[k=2 ML-KEM-512]\n  Mod --> K768[k=3 ML-KEM-768]\n  Mod --> K1024[k=4 ML-KEM-1024]")),
    ],
    "06-code-based": [
        ("## 6.2", "6.1", "Figure 6.1 — McEliece: syndrome as ciphertext",
         "Figure 6.1 shows why decryption is easy with the Goppa trapdoor but hard without it.",
         block_mermaid("flowchart LR\n  e[Small error e] --> s[s = He]\n  H[Public H] --> s\n  s --> ct[Ciphertext]\n  trap[Goppa trapdoor] --> dec[Decode]")),
    ],
    "07-hash-based": [
        ("## 7.2", "7.1", "Figure 7.1 — Merkle tree one-time signature flow",
         "Figure 7.1 underpins XMSS/LMS and the hypertrees inside SLH-DSA.",
         block_mermaid("flowchart TB\n  OTS[OTS key at leaf] --> SIG[Sign message]\n  SIG --> PATH[Auth path to root]\n  PATH --> ROOT[Root in public key]")),
        ("## 7.4", "7.2", "Figure 7.2 — Stateful vs stateless deployment",
         "Figure 7.2 drives HSM requirements: stateful schemes need persistent index storage.",
         block_mermaid("flowchart LR\n  XMSS[XMSS/LMS] --> HSM[Must store index]\n  SLH[SLH-DSA] --> STATELESS[No index in HSM]")),
    ],
    "08-multivariate": [
        ("## 8.2", "8.1", "Figure 8.1 — Oil and vinegar variable split",
         "Figure 8.1 explains the trapdoor: fix vinegar, solve linear system in oil variables.",
         block_mermaid("flowchart LR\n  V[vinegar vars] --> LIN[Linear in oil]\n  O[oil vars] --> SOLVE[Easy solve]")),
        ("## 8.4", "8.2", "Figure 8.2 — Why Rainbow layers leaked structure (2022)",
         "Figure 8.2 is the lesson: extra layers for efficiency created algebraically exploitable structure.",
         block_mermaid("flowchart TD\n  LAY[Layered OV] --> REL[Inter-layer relations]\n  REL --> ATK[Beullens key recovery]")),
    ],
    "09-isogeny-based": [
        ("## 9.3", "9.1", "Figure 9.1 — SIDH auxiliary torsion → break",
         "Figure 9.1 documents why publishing torsion images was fatal to SIDH/SIKE.",
         block_mermaid("flowchart TD\n  PUB[Publish torsion images] --> CD[Castryck-Decru]\n  CD --> BR[Polynomial-time break]")),
        ("## 9.5", "9.2", "Figure 9.2 — Post-SIDH research map",
         "Figure 9.2: treat CSIDH/SQISign as **research**, not procurement defaults.",
         block_mermaid("flowchart LR\n  SIDH[Broken SIDH] --> CSIDH[CSIDH eval]\n  CSIDH --> SQI[SQISign research]")),
    ],
    "10-nist-standardization": [
        ("## 10.2", "10.1", "Figure 10.1 — NIST PQC timeline",
         "Figure 10.1 anchors procurement language to competition milestones.",
         block_mermaid("timeline\n  title NIST PQC milestones\n  2016 : Call for proposals\n  2022 : SIKE Rainbow breaks\n  2024 : FIPS 203 204 205")),
        ("## 10.4", "10.2", "Figure 10.2 — Round-down funnel",
         "Figure 10.2 shows why diversity algorithms survived as alternates.",
         block_mermaid("flowchart TD\n  R1[82 submissions] --> R2[26 round 2]\n  R2 --> F[7 finalists]\n  F --> STD[FIPS + ongoing HQC FN-DSA]")),
    ],
    "12-fips-204-ml-dsa": [
        ("## 12.2", "12.1", "Figure 12.1 — Fiat–Shamir with aborts (signing loop)",
         "Figure 12.1 is why ML-DSA signing time has variance—size clusters for p99.",
         block_mermaid("flowchart TD\n  Y[Sample y] --> Z[z = y + c s]\n  Z --> CHK{||z|| bound?}\n  CHK -->|no| Y\n  CHK -->|yes| OUT[Output sig]")),
        ("## 12.3", "12.2", "Figure 12.2 — ML-DSA parameter sets (k, ℓ)",
         "Figure 12.2 maps ML-DSA-44/65/87 to NIST levels 2/3/5.",
         block_mermaid("flowchart LR\n  D44[ML-DSA-44 k4 l4] --> L2[Level 2]\n  D65[ML-DSA-65 k6 l5] --> L3[Level 3]\n  D87[ML-DSA-87 k8 l7] --> L5[Level 5]")),
    ],
    "13-fips-205-slh-dsa": [
        ("## 13.2", "13.1", "Figure 13.1 — SLH-DSA hypertree",
         "Figure 13.1 connects FORS, WOTS+, and hypertree layers in one view.",
         block_mermaid("flowchart TB\n  FORS[FORS OTS layer] --> WOTS[WOTS+ chains]\n  WOTS --> HT[Hypertree]")),
        ("## 13.3", "13.2", "Figure 13.2 — Fast (f) vs small (s) parameter axis",
         "Figure 13.2 guides parameter pick: bandwidth vs CPU, not security level alone.",
         block_mermaid("flowchart LR\n  F[SHA2-128f] --> FAST[Faster larger sig]\n  S[SHA2-128s] --> SMALL[Smaller slower]")),
    ],
    "14-additional-candidates": [
        ("## 14.2", "14.1", "Figure 14.1 — Portfolio beyond core FIPS",
         "Figure 14.1 is the insurance layer—deploy after ML-KEM/ML-DSA baseline.",
         block_mermaid("flowchart TB\n  CORE[FIPS 203-205] --> DIV[Diversity]\n  DIV --> FN[FN-DSA]\n  DIV --> HQC[HQC]\n  DIV --> MCE[Classic McEliece]")),
        ("## 14.5", "14.2", "Figure 14.2 — Selection decision tree",
         "Use Figure 14.2 when a program demands non-lattice assumptions.",
         block_mermaid("flowchart TD\n  Q{Need diversity?}\n  Q -->|yes| ALT[Add FN-DSA / HQC / McEliece]\n  Q -->|no| CORE[Core FIPS only]")),
    ],
    "16-implementation": [
        ("## 16.2", "16.1", "Figure 16.1 — Side-channel attack surfaces",
         "Figure 16.1 is our implementation review checklist—timing before algebra.",
         block_mermaid("flowchart TD\n  CODE[Crypto implementation] --> T[Timing cache]\n  CODE --> P[Power EM]\n  T --> LEAK[Partial key bits]\n  P --> LEAK\n  LEAK --> LAT[Lattice recovery]")),
        ("## 16.4", "16.2", "Figure 16.2 — Constant-time selection pattern",
         "Figure 16.2: replace secret branches with cmov-style selects.",
         block_mermaid("flowchart LR\n  BR[Secret branch] --> BAD[Leak via cache]\n  CT[ct_select mask] --> OK[Data-independent access]")),
    ],
    "17-performance": [
        ("## 17.2", "17.1", "Figure 17.1 — Benchmark dimensions",
         "Figure 17.1 defines what we publish alongside any μs number.",
         block_mermaid("flowchart TB\n  HW[CPU model AVX] --> LAT[Latency p50 p99]\n  LIB[Library version] --> LAT\n  NET[Bytes handshake] --> COST[Egress cost]")),
        ("## 17.3", "17.2", "Figure 17.2 — Benchmark report template",
         "Figure 17.2 is mandatory metadata—without it, tables are not comparable.",
         block_mermaid("flowchart LR\n  ENV[Environment doc] --> RUN[Raw results]\n  RUN --> PCT[Percentiles]\n  PCT --> PUB[Published table]")),
    ],
    "19-migration-strategies": [
        ("## 19.2", "19.1", "Figure 19.1 — Enterprise migration phases",
         "Figure 19.1 is the program plan we map to steering committees.",
         block_mermaid("flowchart LR\n  D[Discover CBOM] --> P[Prioritize HNDL]\n  P --> I[Pilot hybrid]\n  I --> S[Scale]\n  S --> R[Retire classical PK]")),
        ("## 19.4", "19.2", "Figure 19.2 — Cryptographic agility architecture",
         "Figure 19.2: agility is an API/config layer, not a one-off library swap.",
         block_mermaid("flowchart TB\n  APP[Application] --> API[crypto_* API]\n  API --> CFG[Policy config]\n  CFG --> LIB[liboqs/provider]")),
    ],
    "20-cbom": [
        ("## 20.2", "20.1", "Figure 20.1 — CBOM entity model",
         "Figure 20.1 is the schema teams export to GRC tools.",
         block_mermaid("flowchart TB\n  SVC[Service] --> LIB[Crypto library v]\n  LIB --> ALG[Algorithm + params]\n  ALG --> Q[Quantum-vulnerable flag]")),
        ("## 20.5", "20.2", "Figure 20.2 — CBOM in CI/CD gate",
         "Figure 20.2 shows how CBOM blocks releases when RSA persists on HNDL paths.",
         block_mermaid("flowchart LR\n  BUILD[Build] --> SCAN[CBOM scan]\n  SCAN --> GATE{Policy pass?}\n  GATE -->|yes| REL[Release]\n  GATE -->|no| FAIL[Block]")),
    ],
    "21-industry-government": [
        ("## 21.1", "21.1", "Figure 21.1 — Policy → engineering loop",
         "Figure 21.1 links regulation to measurable engineering artifacts (CBOM, tests).",
         block_mermaid("flowchart LR\n  POL[Policy NIST/CNSA/EU] --> PROC[Procurement]\n  PROC --> ENG[Engineering evidence]\n  ENG --> AUD[Audit]")),
        ("**India (NCIIPC", "21.2", "Figure 21.2 — India PQC stakeholder map",
         "Figure 21.2 is the India-specific overlay—we verify each box against current circulars.",
         block_mermaid("flowchart TB\n  MeitY[MeitY NQM] --> Sect[CERT-In sectors]\n  RBI[RBI payments] --> Banks[Banks/UPI stack]\n  NCIIPC[NCIIPC CII] --> OPS[Critical infra ops]\n  STQC[STQC testing] --> Vendors[Certified products]")),
    ],
    "22-future-directions": [
        ("## 22.2", "22.1", "Figure 22.1 — Research → standards funnel",
         "Figure 22.1 sets expectations: FHE/ZK today are not TLS drop-ins.",
         block_mermaid("flowchart TD\n  R[Research] --> P[Pilot]\n  P --> N[NIST track]\n  N --> F[Future FIPS]")),
        ("## 22.4", "22.2", "Figure 22.2 — Generation-2 capability map",
         "Figure 22.2 separates deploy-now (KEM/sign) from lab-grade (FHE, PQC-ZK).",
         block_mermaid("flowchart LR\n  NOW[ML-KEM ML-DSA SLH] --> NEAR[FN-DSA HQC]\n  NEAR --> LAB[FHE PQC-ZK]")),
    ],
}

def merge_registry():
    for stem, items in EXTRA.items():
        if stem not in FIGURES:
            FIGURES[stem] = []
        for sec, fid, cap, ref, body in items:
            FIGURES[stem].append({
                "id": fid, "section": sec, "caption": cap, "ref": ref, "body": body,
            })


def strip_figures_and_opener_blocks(text: str) -> str:
    text = FIGURE_BLOCK_RE.sub("\n", text)
    # Remove orphan --- between title and first ##
    text = re.sub(
        r"^(# Chapter[^\n]+\n\n[^\n#][^\n]*\n\n)(?:> \*\*Author's note[^\n]*\n\n)?(?:---\n\n)?",
        r"\1",
        text,
        count=1,
        flags=re.MULTILINE,
    )
    # Remove India note duplicate at top if repeated before ## 
    return text


def format_figure(fig: dict) -> str:
    return (
        f"**{fig['caption']}**\n\n"
        f"{fig['body'].rstrip()}\n\n"
        f"*{fig['ref']}*\n\n"
    )


def insert_after_section(text: str, section: str, figure_md: str) -> str:
    if figure_md.strip() in text:
        return text
    # Full section heading line (avoid 1.1 matching 1.10)
    if section.startswith("##"):
        m = re.search(rf"^{re.escape(section)}(\s+[^\n]+)?\n\n", text, re.MULTILINE)
    else:
        m = re.search(rf"^{re.escape(section)}[^\n]*\n\n", text, re.MULTILINE)
    if not m:
        return text
    insert_at = m.end()
    rest = text[insert_at:]
    pm = re.match(r"([^\n#][\s\S]*?\n\n)", rest)
    if pm:
        insert_at += pm.end()
    return text[:insert_at] + figure_md + text[insert_at:]


def fix_figure_above_reference(text: str) -> str:
    return re.sub(r"\*\*Figure (\d+\.\d+) \(above\)\*\*", r"Figure \1", text)


def process_chapter(path: Path):
    stem = path.stem
    text = path.read_text(encoding="utf-8")
    text = strip_figures_and_opener_blocks(text)
    text = fix_figure_above_reference(text)
    for fig in FIGURES.get(stem, []):
        text = insert_after_section(text, fig["section"], format_figure(fig))
    path.write_text(text, encoding="utf-8")


def main():
    merge_registry()
    for p in sorted(CH.glob("*.md")):
        process_chapter(p)
    print("Placed figures in", len(FIGURES), "chapter configs")


if __name__ == "__main__":
    main()
