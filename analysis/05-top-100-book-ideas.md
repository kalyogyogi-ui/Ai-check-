# Phase 5 — Top 100 Future Book Ideas (Blockchain · Crypto · Quantum focus)

> *Concrete, commissionable book concepts with title, subtitle, audience, USP, suggested publisher, format, and Composite Opportunity Score — heavily weighted toward blockchain, cryptography, and quantum technology.*

These 100 ideas are calibrated to **2026-2030** publication windows. Distribution:

| Domain | Section | Count | Share |
|---|---|---|---|
| **Quantum** | A · B · C · D · E | **37** | 37% |
| **Cryptography** (PQC, QKD, programmable crypto) | F · G · H | **26** | 26% |
| **Blockchain & Web3** | I · J · K · L · M · N | **30** | 30% |
| **Cross-cuts** (AI × Crypto × Quantum) | O | **7** | 7% |

AI-only titles from the previous draft have been moved out of this list to make room for deeper BCQ coverage; the AI strategic context is preserved in [Phases 1–4](./00-executive-summary.md). AI appears here only at *genuine* convergence points (AI for quantum control, ZK-ML, AI smart-contract auditing, decentralized AI compute, sovereign-stack architecture).

Each entry uses the COS rubric from [Phase 4](./04-market-gaps.md):
`COS = 0.25·MO + 0.20·RP + 0.15·AI + 0.10·RR + 0.20·LV + 0.10·SC`

**Format key:** SPB = senior practitioner playbook · CB = cookbook · IA = in-action practitioner · GT = graduate textbook · UT = undergraduate textbook · RM = research monograph · EB = executive briefing · CP = certification prep · SV = survey/F&T monograph.

---

## Section A — Quantum Computing Systems & Engineering (#1–#12)

These are *fault-tolerant-era* and *hybrid-system* engineering books. The Qiskit/Cirq beginner shelf is saturated; the systems-engineering shelf for the FT transition is greenfield.

| # | Title / Subtitle | Audience | USP | Publisher | Format | COS |
|---|---|---|---|---|---|---|
| 1 | **Engineering a Quantum Compiler** — *Synthesis, Layout, and Optimization in the Fault-Tolerant Era* | CS grads, quantum compiler engineers | First textbook of FT-era compilation as a discipline; surface-code-aware layout, T-count optimization, magic-state routing. | Pearson-AW / Morgan Kaufmann | GT/SPB | **7.7** |
| 2 | **Building Quantum Software** — *A Systems Engineering Approach* | Working software engineers entering quantum | Treats quantum SW as a systems problem (state, scheduling, observability), not an algorithm problem. | O'Reilly / Apress | SPB | **7.4** |
| 3 | **The Fault-Tolerant Stack** — *From Logical Qubits to User Code* | Grad students, architects | A vertical slice through every layer of an FT computer with concrete numbers. | MIT / CUP | GT | **7.7** |
| 4 | **Quantum Resource Estimation** — *Magic States, T-Counts, and the Real Cost of Useful Quantum* | Researchers, architects | The honest accounting book for "when quantum actually helps". | Springer / Now Publishers | SPB+SV | **7.5** |
| 5 | **Quantum DevOps** — *CI/CD, Calibration, and Observability for Quantum Pipelines* | Quantum platform engineers | First DevOps book for quantum pipelines. | O'Reilly | SPB | **7.0** |
| 6 | **Hybrid Classical-Quantum Architecture** — *Designing Systems Where Both Sides Pull Their Weight* | Architects | Avoids the "QPU as exotic accelerator" trap; integrates with HPC schedulers, data planes, and storage. | Apress | SPB | **7.2** |
| 7 | **Quantum Algorithm Engineering** — *Implementation, Tuning, and Benchmarking on Real Hardware* | Practitioners | Algorithms-on-hardware, not algorithms-on-paper. | Manning / Apress | SPB | **7.2** |
| 8 | **Quantum Operating Systems** — *Scheduling, Multi-Tenancy, and Resource Isolation* | Systems researchers | First systems-textbook treatment of quantum OS challenges. | Springer | RM/GT | **7.0** |
| 9 | **Verifying Quantum Programs** — *Formal Methods for Quantum Code* | CS grads, verification researchers | Bridges quantum semantics, type systems, and program logic. | CUP / Springer | GT/RM | **7.0** |
| 10 | **Practical Surface-Code Engineering** — *Layout, Decoding, Distillation* | Quantum architects | Production-grade surface-code reference; post-Willow-class lessons. | CUP / Springer | GT | **7.4** |
| 11 | **The Quantum API Gateway** — *Scheduling, Multi-Tenancy, Pricing, SLAs* | Cloud-quantum engineers | First operational reference for QPU-as-a-service operators. | Apress | SPB | **6.9** |
| 12 | **Quantum Software Architecture** — *Patterns and Anti-Patterns for the FT Era* | Senior software architects | Patterns book in the GoF tradition for quantum systems. | Pragmatic / Apress | SPB | **6.8** |

**Standouts.** #1 is a generational textbook slot — once anchored, owns curriculum for a decade. #4 is the "anti-hype" book the field needs and is structurally easier to ship than a full algorithms textbook.

---

## Section B — Quantum Hardware (#13–#20)

Modality-specific engineering books. Each major hardware modality deserves a dedicated graduate text; today most are covered only in survey papers and conference proceedings.

| # | Title / Subtitle | Audience | USP | Publisher | Format | COS |
|---|---|---|---|---|---|---|
| 13 | **Superconducting Quantum Processors** — *Design, Fabrication, and Control* | EE/physics grads, hardware engineers | Comprehensive systems-view of the dominant modality through 2030. | Springer | GT | **7.6** |
| 14 | **Trapped-Ion Quantum Computers** — *From Lab to Production* | Physics/EE grads | First production-engineering text for the modality with the longest coherence times. | Springer / CUP | GT | **7.4** |
| 15 | **Photonic Quantum Computing in Practice** — *Measurement-Based Architectures and Cluster States* | Researchers, photonic engineers | Definitive monograph of the photonic FT path (PsiQuantum/Xanadu lineage). | Springer | GT/RM | **7.3** |
| 16 | **Neutral-Atom Quantum Architectures** — *Reconfigurable Arrays and Mid-Circuit Measurement* | Researchers | First full-length monograph of the modality (QuEra/Atom/Pasqal/Infleqtion lineage). | Springer | GT/RM | **7.3** |
| 17 | **Silicon-Spin Qubits** — *Toward Wafer-Scale Quantum* | Researchers, semiconductor engineers | Bridges spin-qubit physics and CMOS fabrication. | Springer | RM | **7.0** |
| 18 | **Cryogenic Control Electronics for Quantum Systems** — *Design, Fabrication, Integration* | EE grads, hardware engineers | The other half of the quantum stack that almost no book covers. | Springer / CRC | GT/SPB | **7.0** |
| 19 | **Quantum Hardware Calibration** — *Methods, Software, and Automation* | Hardware engineers | First systematic treatment of calibration-as-software. | Apress | SPB | **7.0** |
| 20 | **Topological and Majorana Qubits** — *A Critical Engineering Survey* | Researchers | Honest assessment of the modality after a decade of revisions. | Springer | RM | **6.7** |

**Standout.** #18 (cryogenic control) is structurally under-served — every quantum hardware company needs the talent it would credential, but the discipline has no anchor textbook.

---

## Section C — Quantum Algorithms & Applications (#21–#26)

The realistic-advantage era. Books here distinguish *theoretical* speedup from *end-to-end useful* speedup including I/O.

| # | Title / Subtitle | Audience | USP | Publisher | Format | COS |
|---|---|---|---|---|---|---|
| 21 | **Quantum Algorithms After NISQ** — *A Realistic Practitioner Guide* | CS grads, applied researchers | Algorithm portfolio across NISQ, early-FT, and full-FT regimes with honest end-to-end advantage analysis. | CUP | GT/SPB | **7.5** |
| 22 | **Quantum Chemistry at Industrial Scale** — *Algorithms, Pipelines, Validation* | Computational chemists, ML-meets-quantum engineers | Most realistic near-term quantum-advantage domain; pipeline-engineering view. | CUP / Wiley | GT/SPB | **7.5** |
| 23 | **Quantum Optimization** — *An Honest Field Guide* | Industry practitioners | Cuts through QAOA hype with a realistic optimization-engineering lens. | Manning / CUP | SPB | **7.0** |
| 24 | **Quantum Linear Algebra for Practitioners** — *HHL, Block-Encoding, QSVT* | CS/applied math grads | Bridges QLA papers and engineering implementation. | Springer | GT/SPB | **7.0** |
| 25 | **Quantum Simulation of Materials and Molecules** — *From Theory to Workflows* | Materials/chemistry grads | Cross-disciplinary text aligned with autonomous-lab workflows. | CUP / Springer | GT | **7.4** |
| 26 | **Quantum Machine Learning** — *A Skeptical Survey* | Researchers | The honest survey that 2026 needs after the QML hype cycle deflated. | Now Publishers F&T | SV/RM | **6.8** |

**Standout.** #21 is the textbook the field has been waiting for since 2024 — the existing canonical references either pre-date or oversell the FT transition.

---

## Section D — Quantum Networking & Sensing (#27–#31)

Quantum-internet and quantum-sensing engineering is moving from research to early commercial pilots; the textbook lane is open.

| # | Title / Subtitle | Audience | USP | Publisher | Format | COS |
|---|---|---|---|---|---|---|
| 27 | **Quantum Networking** — *Engineering the Quantum Internet* | CS/physics grads | First comprehensive graduate textbook of the field. | CUP | GT | **7.4** |
| 28 | **Quantum Repeaters** — *Architectures, Protocols, Performance* | Researchers | Definitive monograph of the rate-distance bottleneck and the architectural responses. | Springer | RM | **7.0** |
| 29 | **Distributed Quantum Computing** — *Modular QPUs and Networked Workloads* | Architects, researchers | The architecture book for "many small QPUs" rather than "one big QPU". | Springer | GT/RM | **7.0** |
| 30 | **Quantum Sensing in Practice** — *Magnetometry, Gravimetry, and Precision Timing* | Engineers in defense/geophysics/biomed | Practitioner-grade reference for the quantum technology that pays today. | Springer / CRC | SPB+GT | **6.9** |
| 31 | **Quantum-Secured Networks** — *QKD + PQC Hybrid Architecture* | Network architects, telcos | The first hybrid-architecture playbook; aligns with EU EuroQCI rollout. | Apress | SPB | **7.2** |

---

## Section E — Quantum-Readiness Executive Books (#32–#37)

The *commercial* quantum books for 2026-2030 are CTO/CISO/CFO playbooks — not Qiskit tutorials.

| # | Title / Subtitle | Audience | USP | Publisher | Format | COS |
|---|---|---|---|---|---|---|
| 32 | **The Quantum-Ready Enterprise** — *PQC, Talent, Vendors, and Use-Case Discovery* | CTOs, CIOs, COOs | The CTO playbook the market wants instead of yet another Qiskit tutorial. | Wiley / Apress | EB | **8.0** |
| 33 | **The CTO's Quantum Briefing** — *What to Decide, What to Defer, What to Pilot* | C-suite | 90-page board-ready briefing format. | HBR Press | EB | **7.6** |
| 34 | **The CISO's Quantum Briefing** — *Crypto, Compliance, Continuity* | CISOs | Combines quantum threat assessment with PQC migration governance. | Wiley | EB | **7.8** |
| 35 | **Building a Corporate Quantum Center of Excellence** — *Charter, Roles, Budget, KPIs* | Innovation officers | Org-design playbook for in-house quantum capability. | Apress / Wiley | EB | **7.0** |
| 36 | **Quantum Vendor Selection & Procurement** — *RFPs, SLAs, Benchmarking, Contracts* | Procurement, technology buyers | The first serious procurement reference for QPU-as-a-service. | Apress | EB | **7.0** |
| 37 | **The Quantum-Ready CFO** — *Capex, Opex, Depreciation, and the Economics of Quantum Investment* | CFOs, finance leaders | Finance-side companion to #32. | Wiley / HBR | EB | **7.0** |

**Standout.** #32 is the single largest *commercial* quantum slot — broad C-suite buyer cohort, multi-language adaptable, durable through the entire NISQ-to-FT transition.

---

## Section F — PQC Migration & Cryptographic Agility (#38–#49)

The single most regulation-anchored, mandate-driven publishing lane in the entire 2026-2030 cycle. Every entry below targets a guaranteed buyer cohort created by NSM-10 / CNSA 2.0 / EU PQC mandates / BSI / ANSSI / NCSC / ASD / NICT timelines.

| # | Title / Subtitle | Audience | USP | Publisher | Format | COS |
|---|---|---|---|---|---|---|
| **38** | **The Post-Quantum Migration Playbook** — *ML-KEM, ML-DSA, SLH-DSA in Production* ★ | Security engineers, CISOs, GRC | The operational migration handbook the industry has been waiting for. | No Starch / Wiley | SPB | **9.1** |
| 39 | **Cryptographic Agility** — *Designing Systems for Algorithm Rotation* | Architects, security engineers | Re-keying, suite negotiation, certificate-lifecycle in a post-PQC world; the book that exists *because* PQC happened. | Apress | SPB | **8.2** |
| 40 | **Cryptographic Inventory and Discovery** — *Finding Every Crypto Use Before You Migrate* | Security teams, GRC | The discovery book that comes *before* the migration book. | Apress | SPB | **7.6** |
| 41 | **Hybrid TLS in Transition** — *Operating Mixed-Suite Networks 2026-2032* | Network/SRE engineers | Concrete operational guide for the dual-stack transition years. | Manning | SPB | **7.7** |
| 42 | **PQC for Embedded and IoT** — *Lightweight ML-KEM/ML-DSA on Microcontrollers* | Firmware engineers | The only PQC book targeted at constrained devices. | Apress | SPB | **7.9** |
| 43 | **PQC for the Web** — *TLS 1.3, QUIC, X.509, DNSSEC in Transition* | Web infrastructure engineers | Practitioner reference for web-scale PQC deployment. | Apress / O'Reilly | SPB | **7.7** |
| 44 | **PQC for HSMs and Smart Cards** — *Hardware-Bound Migration* | HSM operators, payments engineers | Bridges PCI-DSS / FIPS 140-3 hardware compliance and PQC. | Springer / Apress | SPB | **7.4** |
| 45 | **Hash-Based Signatures in Production** — *XMSS, LMS, SLH-DSA, Stateful vs Stateless* | Firmware/security engineers | The reference for the highest-assurance signature class. | Apress / Springer | SPB | **7.5** |
| 46 | **Lattice-Based Cryptography After Standardization** — *Successor to Peikert/Regev* | Cryptography grads | Aligned with FIPS 203, 204, and FN-DSA once finalized; first textbook of the post-standardization era. | CUP | GT | **7.9** |
| 47 | **Code-Based Cryptography After HQC** — *McEliece Lineage in the Standardization Era* | Cryptography grads | First textbook anchored on the HQC selection. | CUP / Springer | GT/RM | **7.2** |
| 48 | **The CTO's PQC Migration Plan** — *From Discovery to Cryptographic Agility in 36 Months* | CTOs, security executives | Executive companion to #38, board-ready framing. | Wiley | EB | **7.9** |
| 49 | **PQC Audit & Compliance Handbook** — *NSM-10, CNSA 2.0, BSI, ANSSI, NCSC, ASD Comparative* | Auditors, GRC, sovereign-customer security | First multi-jurisdiction PQC compliance reference. | Wiley / Sybex | EB+CP | **7.9** |

**Why this section dominates.** Of the 12 entries here, **8 score COS ≥ 7.7**, anchored by the #38 flagship at 9.1 — the highest-COS commissionable title in the entire 100. The cohort is mandated; the deadlines are public; the standards are stable; the books do not yet exist. Whoever ships #38 + #39 + #48 + #49 as a 4-title bundle in 2026-2027 owns the lane.

---

## Section G — Quantum Cryptography (QKD, QRNG, DI-QKD) (#50–#53)

Niche but durable — pairs naturally with PQC migration narratives in critical-infrastructure markets (telco, defense, banking, government).

| # | Title / Subtitle | Audience | USP | Publisher | Format | COS |
|---|---|---|---|---|---|---|
| 50 | **Quantum Key Distribution Engineering** — *Protocols, Hardware, Network Integration* | Telco engineers, defense | The first practitioner reference for deploying QKD in real networks. | Springer / Apress | GT/SPB | **6.9** |
| 51 | **Device-Independent QKD** — *From Theory to Deployment* | Researchers, advanced engineers | Tracks the most rigorous QKD branch through its early-deployment phase. | Springer / CUP | RM | **6.7** |
| 52 | **Quantum Random Number Generators in Practice** — *Sources, Validation, NIST Conformance* | Crypto engineers, hardware vendors | Bridges QRNG physics and FIPS 140-3 / SP 800-90B compliance. | Apress / Springer | SPB | **6.6** |
| 53 | **Continuous-Variable Quantum Cryptography** — *Foundations and Engineering* | Researchers | The CV branch monograph the field is missing. | Springer | RM | **6.5** |

---

## Section H — Programmable Cryptography: ZK, FHE, MPC, Threshold (#54–#63)

The convergence of ZK proofs, fully homomorphic encryption, multi-party computation, and threshold cryptography into a unified "programmable cryptography" stack is the most methodologically novel cryptographic development of the late 2020s.

| # | Title / Subtitle | Audience | USP | Publisher | Format | COS |
|---|---|---|---|---|---|---|
| 54 | **Building ZK Circuits with Halo2** — *A Practitioner Cookbook* | ZK engineers | Toolchain-first practitioner reference for the dominant ZK framework. | Packt / No Starch | CB+SPB | **7.6** |
| 55 | **Plonky3 in Production** — *Recursive Proofs and the Engineering of Composition* | ZK engineers | First serious production-engineering book for the Plonky line. | Manning / Packt | SPB | **7.4** |
| 56 | **zkVM Engineering** — *SP1, Risc0, and the Future of Verifiable Compute* | Senior engineers, protocol designers | The first zkVM systems-engineering book. | O'Reilly / Manning | SPB | **7.7** |
| 57 | **Noir: ZK Application Development** — *Privacy-First dApps from Day One* | Web3 engineers | The first Noir-anchored development book. | Packt / Manning | IA+CB | **7.0** |
| 58 | **Folding Schemes Engineering** — *Nova, HyperNova, ProtoStar in Practice* | Cryptography engineers, researchers | Bridges the folding-schemes research front and the engineering tier. | Springer / CUP | GT/SPB | **7.3** |
| 59 | **Fully Homomorphic Encryption in Practice** — *TFHE, BGV, CKKS for Engineers* | ML and privacy engineers | Practitioner-grade FHE without the math-only ceiling of existing texts. | Apress / Springer | SPB | **7.4** |
| 60 | **Building MPC Protocols** — *Production Engineering of Secure Multi-Party Computation* | Crypto engineers, privacy teams | The "MPC in action" book the field is missing. | Apress | SPB | **7.3** |
| 61 | **Threshold Cryptography Engineering** — *Distributed Signing for Custody, Bridges, and Beyond* | Custody engineers, blockchain infrastructure | The first practitioner book unifying TSS / FROST / DKLs23-class designs. | Apress / Wiley | SPB | **7.5** |
| 62 | **Programmable Cryptography Architecture** — *When to Use ZK vs FHE vs MPC vs TEE* | Architects, CISOs | Decision-architecture guide for the four privacy-preserving primitives. | Apress | SPB+EB | **7.6** |
| 63 | **Verifiable Computation** — *Foundations and Engineering* | CS grads, researchers | The graduate textbook unifying SNARK theory and engineering. | CUP / Springer | GT | **7.5** |

**Standout.** #62 is the *category-creating* book of programmable cryptography — most teams pick a primitive based on what they know, not on what fits. The decision architecture is missing.

---

## Section I — Smart Contracts & Layer-2 (#64–#72)

Solidity beginner shelf is mature; the under-served tier is *security-by-design*, *formal verification*, *L2 internals*, and *post-bridge-hack-era cross-chain engineering*.

| # | Title / Subtitle | Audience | USP | Publisher | Format | COS |
|---|---|---|---|---|---|---|
| 64 | **Smart Contract Security by Design** — *A Foundry-Era Field Manual* | Smart-contract engineers | The opinionated security-first practitioner book — fuzzing-default, invariant-driven. | No Starch | SPB | **7.8** |
| 65 | **The Smart Contract Audit Engineering Handbook** — *Foundry-Fuzz, Halmos, Slither, Echidna, Certora* | Auditors, security engineers | Toolchain-first, vendor-neutral; aligns with the emerging audit-cert programs. | No Starch / Packt | SPB+CB | **7.7** |
| 66 | **Solidity for Senior Engineers** — *Patterns, Anti-Patterns, Upgradability* | Senior smart-contract engineers | The senior-engineering book the EVM ecosystem has lacked. | Manning | SPB | **7.0** |
| 67 | **Move and Cairo for EVM Engineers** — *A Comparative Practitioner Guide* | Smart-contract engineers expanding past EVM | Bridges the EVM-native engineer to Aptos/Sui (Move) and StarkNet (Cairo) without restarting from scratch. | Packt | SPB | **6.9** |
| 68 | **Building L2 Rollups** — *Sequencers, Provers, Data Availability, Fault Proofs* | Protocol engineers | The first systems-engineering book for rollups as software. | O'Reilly / Springer | SPB+GT | **7.7** |
| 69 | **Custom Rollup Stacks** — *OP Stack, Arbitrum Orbit, ZK Stack, Polygon CDK Compared* | Protocol engineers, app-chain teams | Comparative practitioner reference for the rollup-as-a-service era. | Packt / Manning | SPB+CB | **7.3** |
| 70 | **Account Abstraction in Production** — *ERC-4337, EIP-7702, Paymasters, Bundlers* | Smart-contract engineers, wallet teams | The practitioner reference for AA, after the EIP-7702 hardening of EOAs. | Manning | SPB | **7.4** |
| 71 | **Smart Contract Formal Verification** — *Solidity to Specifications to Proofs* | Senior engineers, security researchers | Bridges contract code, K/Certora-style specs, and SMT proofs. | Springer / Apress | GT/SPB | **7.3** |
| 72 | **The MEV Engineer's Handbook** — *Searching, Building, Mitigating, and the Post-PBS Order Flow* | Searchers, builders, validator operators | The first serious operational MEV reference. | O'Reilly / Manning | SPB | **7.4** |

---

## Section J — Tokenization & Real-World Assets (#73–#78)

The dominant institutional-blockchain story of 2026-2030 — BlackRock-tier flows, tokenized treasuries, regulated stablecoins, on-chain credit. **The largest unfilled slot in finance-tech publishing today.**

| # | Title / Subtitle | Audience | USP | Publisher | Format | COS |
|---|---|---|---|---|---|---|
| **73** | **Tokenizing Real-World Assets** — *Engineering, Custody, Compliance, Structuring* ★ | Banks, asset managers, fintech engineers | The first cross-disciplinary RWA reference (engineering + law + custody + compliance in one volume). | Wiley professional / Apress | EB+SPB | **8.4** |
| 74 | **Tokenized Treasuries and Money Markets** — *A Banker's Engineering Companion* | Banks, treasurers, regulators | First practitioner book on the largest live RWA category (BUIDL-class funds). | Wiley professional | EB | **8.0** |
| 75 | **Stablecoin Engineering** — *Reserves, Audits, Rails, Compliance* | Fintech engineers, banking teams | Bridges issuance economics, custody, and on-chain payment-rail engineering. | Apress / Wiley | SPB | **7.8** |
| 76 | **The Tokenized Bank** — *Operational Reference for On-Chain Banking* | Bank technology and operations leaders | The org-and-tech blueprint for the first generation of tokenized commercial banks. | Wiley professional | EB | **7.7** |
| 77 | **CBDC Implementation Handbook** — *Comparative: Digital Euro, e-CNY, e-HKD, DREX, Project Agorá* | Central-bank technologists, regulators | Country-by-country implementation reference; uniquely citable. | Wiley / OUP / CUP | EB+RM | **7.5** |
| 78 | **Tokenization for Treasury Teams** — *Stablecoins, Tokenized Funds, On-Chain Cash Management* | Corporate treasurers, CFOs | First treasury-side reference for on-chain assets. | Wiley professional | EB | **7.6** |

**Standout.** #73 is one of the four highest-impact slots in the entire 100. The author profile — a senior banker + senior smart-contract engineer co-authoring — is uniquely high-leverage.

---

## Section K — DeFi Engineering (#79–#82)

DeFi-mechanism beginner books are saturated; the under-served tier is *institutional risk*, *intent-based architecture*, and *restaking* engineering.

| # | Title / Subtitle | Audience | USP | Publisher | Format | COS |
|---|---|---|---|---|---|---|
| 79 | **Intent-Based DeFi** — *Solver Networks, Auctions, and the New Liquidity Stack* | DeFi engineers | The first systematic intent-architecture book. | Manning / Packt | SPB | **6.9** |
| 80 | **Liquid Staking and Restaking Engineering** — *EigenLayer-Class Architectures and AVS Operations* | Protocol/infra engineers | First serious technical reference for the LST/LRT layer. | Manning | SPB | **7.1** |
| 81 | **DeFi Risk Management for Institutions** — *Custody, Counterparty, Smart-Contract, and Oracle Risk* | Bank/asset-manager risk teams | Translates DeFi risks into the language of institutional risk management. | Wiley professional | EB+SPB | **7.6** |
| 82 | **Decentralized Derivatives Engineering** — *Perpetuals, Options, and Structured Products* | DeFi engineers, market-makers | The first book to unify perp/option/structured-product engineering on-chain. | Manning / Packt | SPB | **6.9** |

---

## Section L — Web3 Infrastructure (#83–#87)

The plumbing layer — RPC, indexers, oracles, decentralized storage, validator operations.

| # | Title / Subtitle | Audience | USP | Publisher | Format | COS |
|---|---|---|---|---|---|---|
| 83 | **Web3 Infrastructure** — *RPC, Indexers, Oracles, MEV-Aware Mempools* | Backend engineers, infra teams | First comprehensive infra-side practitioner reference. | O'Reilly | SPB | **7.2** |
| 84 | **Cross-Chain Engineering After the Bridge-Hack Era** — *Secure Messaging, Light Clients, Shared Sequencing* | Protocol engineers, security engineers | Hard-won lessons from Wormhole/Ronin/Nomad/Multichain era; secure-by-default architectures. | O'Reilly / No Starch | SPB | **7.4** |
| 85 | **Account-Abstraction Wallets at Scale** — *Custody, Recovery, UX, Session Keys* | Wallet engineers, fintech teams | Bridges AA protocol details and consumer-wallet UX engineering. | Apress / Manning | SPB | **7.0** |
| 86 | **Building Decentralized Storage Systems** — *Filecoin, Arweave, EigenDA, Avail Compared* | Infra engineers | Comparative practitioner reference for the DA / decentralized-storage layer. | Manning | SPB | **6.8** |
| 87 | **The Validator Operator's Handbook** — *PoS Engineering Across Ethereum, Solana, Cosmos, NEAR* | Validator operators, infra engineers | First multi-chain validator-ops reference. | Apress | SPB | **6.9** |

---

## Section M — Blockchain Security (#88–#90)

Forensics + audit + post-exploit recovery. Pairs naturally with section H (programmable crypto) and #65 (audit handbook).

| # | Title / Subtitle | Audience | USP | Publisher | Format | COS |
|---|---|---|---|---|---|---|
| 88 | **Blockchain Forensics & On-Chain Compliance** — *Tracing, Sanctions, AML* | Compliance, law-enforcement, exchanges | The first comprehensive on-chain forensics + compliance reference. | Wiley / No Starch | SPB+EB | **7.4** |
| 89 | **Smart Contract Forensics** — *Post-Exploit Reconstruction and Recovery* | Incident response, security engineers | Methodology for the post-hack forensics discipline. | No Starch | SPB | **7.0** |
| 90 | **Bridge & L2 Security** — *Lessons from a Decade of Exploits* | Protocol engineers, security teams | Case-study-driven security reference; pairs with #84. | No Starch | SPB | **7.2** |

---

## Section N — Identity, DAOs, On-Chain Governance (#91–#93)

Decentralized identity is now regulation-driven (eIDAS 2.0 / EUDI Wallet); DAO governance is moving from speculation to legal-entity formalization.

| # | Title / Subtitle | Audience | USP | Publisher | Format | COS |
|---|---|---|---|---|---|---|
| 91 | **EUDI Wallet & Verifiable Credentials Engineering** — *eIDAS 2.0 in Code* | EU-market identity engineers | Anchor reference for the largest mandated identity rollout in history. | Apress / Springer | SPB | **7.6** |
| 92 | **Decentralized Identity Architecture** — *DIDs, VCs, Selective Disclosure, BBS+* | Identity/privacy engineers | The DID/VC reference targeted at engineers, not standards committees. | Apress | SPB | **7.0** |
| 93 | **DAO Operational Governance** — *Treasury, Voting Design, Sybil Resistance, Legal Wrappers* | DAO operators, on-chain treasuries | Bridges Wyoming-DAO-LLC / Marshall-Islands-DAO law and on-chain operations. | Wiley / Apress | EB+SPB | **6.9** |

---

## Section O — Cross-Cuts: AI × Crypto × Quantum Convergence (#94–#100)

The seven highest-COS books that sit *exactly* at the seam between two or three of the focus domains. Each is category-creating.

| # | Title / Subtitle | Audience | USP | Publisher | Format | COS |
|---|---|---|---|---|---|---|
| 94 | **AI for Quantum Control** — *RL Pulse Shaping, ML Decoders, Calibration* | Quantum researchers, ML researchers | Inverts the popular AI×Quantum framing — this is the *real* growing intersection (RL for pulse shaping, ML for QEC decoders, ML for calibration). First dedicated monograph. | Springer | RM/GT | **7.6** |
| 95 | **Quantum-Safe Blockchains** — *PQC Migration for Crypto Networks* | Protocol engineers, validator operators | The first systematic treatment of how Bitcoin/Ethereum/Solana etc. migrate to PQC signatures and what breaks. | Apress / No Starch | SPB | **7.5** |
| 96 | **ZK Machine Learning** — *Verifiable Inference at Scale* | ML engineers, ZK engineers | Bridges Halo2/Plonky/zkVM tooling with realistic ML inference (linear layers, attention, sparsification). | Manning / Springer | SPB+GT | **7.6** |
| 97 | **AI-Powered Smart Contract Auditing** — *LLMs in the Audit Pipeline* | Auditors, security engineers | The first responsible engineering book on LLM-assisted audit (with explicit failure-mode catalog). | No Starch | SPB | **7.4** |
| 98 | **Confidential Computing for Blockchain & AI** — *TEE-Backed Trust Layers* | Architects, infra engineers | The integration book for TEE-backed validators, sequencers, and AI inference. | Apress | SPB | **7.5** |
| 99 | **Decentralized AI Compute** — *A Skeptical Engineer's Guide to Bittensor, Akash, Render, Gensyn, io.net* | Engineers, evaluators, investors | The honest engineering survey of the decentralized-compute claim. Skeptical, not promotional. | O'Reilly / Apress | EB+SPB | **6.9** |
| **100** | **The Sovereign Stack** — *AI + PQC + Tokenization for Nation-States* ★ | Government CTOs, sovereign-AI strategists | The first integrated reference for sovereign-AI + sovereign-crypto + sovereign-finance as a single architectural story. | OUP / Wiley | EB | **7.7** |

**Standout.** #94 is the highest-defensibility academic-monograph slot in the cross-cut group. #100 is the highest-defensibility executive slot — every nation with a sovereign-AI strategy needs this reference, and none has been written.

---

## Summary of the 100

### Top-15 by COS (across all sections)

| Rank | # | Title (short) | Section | Format | COS |
|---|---|---|---|---|---|
| 1 | 38 | The Post-Quantum Migration Playbook | F · PQC | SPB | **9.1** |
| 2 | 73 | Tokenizing Real-World Assets | J · RWA | EB+SPB | **8.4** |
| 3 | 39 | Cryptographic Agility | F · PQC | SPB | **8.2** |
| 4 | 32 | The Quantum-Ready Enterprise | E · Exec | EB | **8.0** |
| 5 | 74 | Tokenized Treasuries & Money Markets | J · RWA | EB | **8.0** |
| 6 | 42 | PQC for Embedded and IoT | F · PQC | SPB | **7.9** |
| 6 | 46 | Lattice Crypto After Standardization | F · PQC | GT | **7.9** |
| 6 | 48 | The CTO's PQC Migration Plan | F · PQC | EB | **7.9** |
| 6 | 49 | PQC Audit & Compliance Handbook | F · PQC | EB+CP | **7.9** |
| 10 | 64 | Smart Contract Security by Design | I · SC | SPB | **7.8** |
| 10 | 75 | Stablecoin Engineering | J · RWA | SPB | **7.8** |
| 10 | 34 | The CISO's Quantum Briefing | E · Exec | EB | **7.8** |
| 13 | 1 | Engineering a Quantum Compiler | A · Q-Eng | GT | **7.7** |
| 13 | 3 | The Fault-Tolerant Stack | A · Q-Eng | GT | **7.7** |
| 13 | 41 | Hybrid TLS in Transition | F · PQC | SPB | **7.7** |
| 13 | 43 | PQC for the Web | F · PQC | SPB | **7.7** |
| 13 | 56 | zkVM Engineering | H · Prog-Crypto | SPB | **7.7** |
| 13 | 65 | Smart Contract Audit Handbook | I · SC | SPB+CB | **7.7** |
| 13 | 68 | Building L2 Rollups | I · SC | SPB+GT | **7.7** |
| 13 | 76 | The Tokenized Bank | J · RWA | EB | **7.7** |
| 13 | 100 | The Sovereign Stack | O · Cross | EB | **7.7** |

**Six of the top-15 are PQC-related.** Five are tokenization/RWA. Three are quantum-readiness/quantum-engineering. Two are smart-contract security. One is sovereign-stack convergence.

### Distribution by suggested publisher (top homes)

| Publisher | Suggested-as-home count |
|---|---|
| Apress | 22 |
| Wiley (incl. Sybex / professional) | 21 |
| Springer | 19 |
| No Starch | 11 |
| Manning | 11 |
| O'Reilly | 8 |
| CUP | 12 |
| Packt | 8 |
| HBR Press | 3 |
| OUP | 3 |
| MIT Press | 2 |
| Pearson-AW / Morgan Kaufmann | 1 |
| CRC | 3 |
| Now Publishers / F&T | 2 |
| Pragmatic Bookshelf | 1 |

(Multiple-home titles counted once per credited home; counts therefore exceed 100.)

**Apress's structural fit** — practitioner-meets-research hybrid voice + Springer distribution — makes it the natural home for the largest share (22 titles), particularly across PQC operational migration, programmable cryptography, and quantum-software engineering. **Wiley professional** dominates the institutional-finance and audit/cert tier (21 titles). **Springer** anchors the academic side (19 titles, mostly hardware modality monographs and graduate textbooks). **No Starch** owns the offensive-security and smart-contract-security shelf (11 titles).

### Three programmatic recommendations from the 100

1. **A "Trust & Migration" series** — bundle #38 + #39 + #40 + #41 + #43 + #44 + #48 + #49 plus #62 (programmable-crypto decision architecture). Nine anchor titles, multi-language editions, 36-month rollout. **The single highest-ROI publishing program in the entire field for 2026-2030**, anchored on regulator-mandated demand and 5+ year shelf life.
2. **A "Tokenized Finance" series** — bundle #73 + #74 + #75 + #76 + #77 + #78 plus #61 (threshold cryptography for custody). The first comprehensive institutional-finance + on-chain reference shelf. Wiley professional is structurally positioned to anchor.
3. **A "Quantum Engineering" series** — bundle #1 + #3 + #4 + #10 + #13 + #18 + #21 + #32 + #94. Nine titles spanning compiler-through-CTO. Springer + MIT/CUP joint, with executive companion through Wiley. Establishes a generational moat in quantum-trade publishing.

A publisher executing all three programs over 2026-2029 captures roughly $30-60M in cumulative net revenue (very rough order-of-magnitude triangulation) and a defensible 5-10 year catalog moat in the BCQ space.

---

[← Phase 4: Market Gaps](./04-market-gaps.md) · [Back to index](./README.md) · [Next: Phase 6 — Forecasts →](./06-forecasts.md)
