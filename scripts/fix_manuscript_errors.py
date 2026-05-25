#!/usr/bin/env python3
"""Remove botched voice-pass artifacts; restore publishable structure."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CH = ROOT / "manuscript" / "chapters"

GENERIC_NOTE = re.compile(
    r">\s*\*\*Author's note:\*\*\s*When in doubt, \*\*pilot hybrid TLS\*\* on internal services first;[^\n]*\n\n",
    re.IGNORECASE,
)

CLOSING_99 = re.compile(
    r"\n---\n\n## \d+\.99 Author's Closing Perspective[\s\S]*?---\s*$",
    re.MULTILINE,
)

CHAPTER_SUMMARY = """---

## Chapter Summary

**Technical takeaway:** {takeaway}

**Deployment takeaway:** {deploy}

*Figures in this chapter are planning aids—verify all algorithm names and byte sizes against the current NIST FIPS PDF before implementation.*

---
"""

TAKEAWAYS = {
    "01-introduction": (
        "Public-key trust rests on problems Shor breaks; symmetric algorithms need strength bumps, not full replacement.",
        "Start inventory and hybrid KEX for long-lived data; do not wait for a public CRQC milestone.",
    ),
    "02-quantum-computing-fundamentals": (
        "Quantum advantage is structural (superposition, interference), not 'infinitely fast classical cores.'",
        "Brief leadership on CRQC uses logical qubits and error correction overhead, not marketing qubit counts.",
    ),
    "03-quantum-attacks": (
        "Shor targets RSA, finite-field DH/DSA, and ECDLP; Grover halves effective symmetric key strength.",
        "Prioritize replacing Shor-vulnerable primitives in protocols that protect long-retention data.",
    ),
    "04-pqc-overview": (
        "Lattice schemes are the default deployment path; hash, code, multivariate, and isogeny families fill diversity niches.",
        "Pick algorithms by assumption diversity, bytes on the wire, and library maturity—not family politics.",
    ),
    "05-lattice-based": (
        "Module-LWE/LWE hardness underpins ML-KEM and ML-DSA; NTT makes ring arithmetic practical.",
        "Treat implementation leakage as the primary risk—use audited libraries and constant-time NTT.",
    ),
    "06-code-based": (
        "Code-based KEMs offer long confidence horizons; Classic McEliece and HQC differ sharply in key size.",
        "Validate network MTU and storage before promising McEliece at the TLS edge.",
    ),
    "07-hash-based": (
        "Hash signatures minimize assumptions; stateful (XMSS/LMS) vs stateless (SLH-DSA) drives operations design.",
        "Never deploy stateful schemes without hardware or HSM state discipline.",
    ),
    "08-multivariate": (
        "MQ hardness is strong in theory; structured traps (Rainbow layers) created practical breaks.",
        "Treat NIST additional-signature candidates as evolving—monitor cryptanalysis releases.",
    ),
    "09-isogeny-based": (
        "SIDH failed because published torsion points enabled polynomial-time recovery; CSIDH/SQISign remain research-grade for production.",
        "Do not plan production on isogeny KEX until standards and mature libraries exist.",
    ),
    "10-nist-standardization": (
        "NIST's open competition model produced FIPS 203–205; breaks during the process validated public review.",
        "Align procurement language to FIPS names (ML-KEM) not legacy submission names (Kyber) in new contracts.",
    ),
    "11-fips-203-ml-kem": (
        "ML-KEM is IND-CCA2 via FO transform with implicit rejection—test invalid ciphertext paths.",
        "Use ACVP/KAT vectors; document whether you expose decapsulation oracles in your API.",
    ),
    "12-fips-204-ml-dsa": (
        "ML-DSA security requires rejection sampling; signing time has variance—capacity-plan p99.",
        "Prefer ML-DSA-65/87 where policy allows; match parameter set to certificate hierarchy depth.",
    ),
    "13-fips-205-slh-dsa": (
        "SLH-DSA trades signature size for hash-only assumptions; pick fast vs small parameter sets deliberately.",
        "Embed SLH-DSA where conservative assumptions outweigh bandwidth (roots of trust, some firmware).",
    ),
    "14-additional-candidates": (
        "FN-DSA, HQC, and Classic McEliece extend the portfolio—none replace day-one ML-KEM/ML-DSA deployment.",
        "Reserve diversity algorithms for second-wave migration after core FIPS rollout.",
    ),
    "15-hybrid-schemes": (
        "Hybrid KEX concatenates classical and PQC shared secrets; security is at least as strong as the better component under standard combiners.",
        "Default to hybrid for customer-facing TLS until your threat model and policy allow pure PQC.",
    ),
    "16-implementation": (
        "PQC implementations fail on side channels before they fail on math—constant-time NTT and rejection handling are mandatory.",
        "Mandate audited libraries; block custom lattice code without independent review.",
    ),
    "17-performance": (
        "PQC performance is multidimensional: CPU, bytes on the wire, and tail latency (especially ML-DSA signing).",
        "Publish benchmark methodology before numbers; never compare μs figures without library and CPU disclosure.",
    ),
    "18-pqc-protocols": (
        "TLS integrates PQC at key exchange first; PKI signature migration follows with cert chain size constraints.",
        "Test middleboxes and CDN paths—especially mobile networks in India—before enabling PQC ciphers broadly.",
    ),
    "19-migration-strategies": (
        "Migration is a program: CBOM → prioritize HNDL → pilot → scale → retire classical PK.",
        "Cryptographic agility is configuration and ownership—not a one-time library upgrade.",
    ),
    "20-cbom": (
        "CBOM extends SBOM with algorithms, parameters, and quantum-vulnerability flags.",
        "Automate CBOM in CI/CD; tie findings to owners and migration waves.",
    ),
    "21-industry-government": (
        "Policy sets deadlines; engineering determines feasibility—map both for your jurisdiction.",
        "Indian teams should track NIST FIPS and domestic initiatives (NQM, NCIIPC, RBI) in parallel.",
    ),
    "22-future-directions": (
        "FIPS 203–205 are generation one; FHE, ZK, and leaner signatures remain research-to-product pipelines.",
        "Build agility so future algorithm drops do not repeat today's migration pain.",
    ),
}


def fix_ch1_figure_placement(text: str) -> str:
    """Move Figure 1.2 from mid-1.1 to start of 1.4."""
    fig2 = re.search(
        r"\n\n\*\*Figure 1\.2[\s\S]*?```\n\n",
        text,
    )
    if not fig2:
        return text
    block = fig2.group(0)
    text = text.replace(block, "\n", 1)
    if "## 1.4" in text and "Figure 1.2" not in text[text.find("## 1.4") : text.find("## 1.4") + 800]:
        text = text.replace("## 1.4", block + "## 1.4", 1)
    return text


def process(path: Path):
    t = path.read_text(encoding="utf-8")
    t = GENERIC_NOTE.sub("", t)
    stem = path.stem
    if stem == "01-introduction":
        t = fix_ch1_figure_placement(t)
    m = CLOSING_99.search(t)
    if m:
        t = t[: m.start()]
    tk = TAKEAWAYS.get(stem, ("Review chapter claims against primary standards.", "Pilot changes in non-production first."))
    t = t.rstrip() + CHAPTER_SUMMARY.format(takeaway=tk[0], deploy=tk[1])
    t = re.sub(r"\bcomprehensive governmental\b", "coordinated federal", t)
    t = re.sub(r"\bcomprehensive CBOM\b", "full CBOM", t)
    t = re.sub(r"\bA comprehensive CBOM\b", "A full CBOM", t)
    path.write_text(t, encoding="utf-8")


def main():
    for p in sorted(CH.glob("*.md")):
        process(p)
    print("Fixed", len(list(CH.glob("*.md"))), "chapters")


if __name__ == "__main__":
    main()
