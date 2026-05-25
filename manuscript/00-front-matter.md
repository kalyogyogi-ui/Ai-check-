# Post-Quantum Cryptography: Engineering the Migration

## Securing Digital Infrastructure Beyond the Quantum Threat Model

---

**Author:** [Your Name]  
**Affiliation:** [Your Organization / Independent Consultant]  
**Edition:** First Edition, 2026  
**Subject:** Post-Quantum Cryptography · Standards · Implementation · Migration

---

## Author's Preface

I wrote this text for the teams who must **ship** quantum-safe cryptography—not only for researchers who already live in lattice papers. Over the past several years I have led readiness assessments for Indian financial institutions, telecommunications operators, and SaaS vendors, alongside global PKI and TLS migrations. The pattern repeats: executives ask for a qubit forecast; engineers need a **cipher-suite decision** by Friday.

This edition is opinionated where standards are silent. I default to **hybrid key exchange** during transition, **ML-KEM / ML-DSA** as primary algorithms, and **cryptographic inventory (CBOM)** before heroics in any single library. I call out India's policy and testing context (MeitY, RBI operational risk, NCIIPC sector guidance, STQC) without pretending to offer legal advice—verify circulars before you contract.

Figures and architecture diagrams appear in every chapter because cryptography is a systems discipline. If a diagram disagrees with a FIPS document, **trust FIPS** and file an erratum.

— *[Your Name], 2026*

---

## Conventions

- **Bold** — first use of a defined term  
- `Monospace` — code, parameters, algorithm names (NIST official names)  
- `> **Author's note:**` — practitioner judgment, deployment caveats  
- **Figure X.Y** — diagrams (Mermaid; print-friendly)  
- Security levels — NIST categories 1–5 unless stated otherwise  

---

## Table of Contents

See `manuscript/chapters/` and `manuscript/appendices/` for chapter files.

---

*Replace bracketed author fields before publisher submission.*
