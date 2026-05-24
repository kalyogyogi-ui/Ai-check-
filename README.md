# Post-Quantum Cryptography: A Comprehensive Guide

A complete book covering Post-Quantum Cryptography (PQC) — from mathematical foundations through NIST standardization to practical migration strategies.

## About

This repository contains a comprehensive, structured book on Post-Quantum Cryptography organized into 22 chapters and 4 appendices covering:

- **Foundations** — Quantum computing, quantum attacks on cryptography, and the PQC landscape
- **Core Algorithms** — Lattice-based, code-based, hash-based, multivariate, and isogeny-based cryptography
- **NIST Standards** — Detailed coverage of FIPS 203 (ML-KEM), FIPS 204 (ML-DSA), and FIPS 205 (SLH-DSA)
- **Implementation** — Hybrid schemes, side-channel resistance, performance analysis, and protocol integration
- **Migration** — Cryptographic agility, CBOM, industry initiatives, and future directions

## Structure

```
book/
├── 00-front-matter.md          — Title, table of contents, prerequisites
├── 01-introduction.md          — Cryptography and the quantum threat
├── 02-quantum-computing-fundamentals.md
├── 03-quantum-attacks.md       — Shor's and Grover's algorithms
├── 04-pqc-overview.md          — Overview of PQC algorithm families
├── 05-lattice-based.md         — LWE, Ring-LWE, Module-LWE
├── 06-code-based.md            — McEliece, BIKE, HQC
├── 07-hash-based.md            — WOTS+, FORS, Merkle trees, SPHINCS+
├── 08-multivariate.md          — UOV, Rainbow (broken), MQ problem
├── 09-isogeny-based.md         — SIDH/SIKE (broken), CSIDH, SQISign
├── 10-nist-standardization.md  — The 8-year standardization process
├── 11-fips-203-ml-kem.md       — ML-KEM specification and analysis
├── 12-fips-204-ml-dsa.md       — ML-DSA specification and analysis
├── 13-fips-205-slh-dsa.md      — SLH-DSA specification and analysis
├── 14-additional-candidates.md — FN-DSA, Classic McEliece, HQC, others
├── 15-hybrid-schemes.md        — Combining classical and PQC
├── 16-implementation.md        — Side-channels, constant-time, platforms
├── 17-performance.md           — Benchmarks and optimization
├── 18-pqc-protocols.md         — TLS, PKI, SSH, VPN, email, blockchain
├── 19-migration-strategies.md  — Agility, planning, execution
├── 20-cbom.md                  — Cryptographic Bill of Materials
├── 21-industry-government.md   — Global initiatives and mandates
├── 22-future-directions.md     — Open problems and research frontiers
├── appendix-a-math.md          — Mathematical prerequisites
├── appendix-b-glossary.md      — Glossary of terms
├── appendix-c-tools.md         — Reference implementations and tools
└── appendix-d-resources.md     — Further reading and resources
```

## Key Topics Covered

- Why quantum computers break RSA, ECC, and Diffie-Hellman (Shor's algorithm)
- NIST Post-Quantum standards: ML-KEM (FIPS 203), ML-DSA (FIPS 204), SLH-DSA (FIPS 205)
- Mathematical foundations: Lattices, LWE, error-correcting codes, hash constructions
- Real-world deployment: TLS 1.3 hybrid, Signal PQXDH, Chrome/Cloudflare PQC
- Migration planning: Inventory, risk assessment, phased deployment
- Government mandates: CNSA 2.0, OMB M-23-02, EU/BSI/ANSSI guidelines

## Who This Book Is For

- Software engineers implementing quantum-resistant cryptography
- Security architects planning PQC migration
- Researchers studying post-quantum constructions
- IT leaders making strategic decisions about cryptographic readiness
- Students seeking a comprehensive PQC reference

## License

This work is provided as an educational resource.
