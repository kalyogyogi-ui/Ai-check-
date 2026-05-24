# Book Proposal — *The Post-Quantum Migration Playbook*

**Subtitle:** *ML-KEM, ML-DSA, SLH-DSA in Production*

**From:** [Phase 5, item #38](../05-top-100-book-ideas.md) · COS **9.1** · the highest-ranked commissionable title in the entire BCQ landscape for 2026-2030.

**Suggested home:** No Starch (preferred) · Wiley (alternative for cert-prep alignment)
**Format:** Senior Practitioner Playbook · ~520 pages · ~95 code/config listings · ~40 figures
**Target manuscript delivery:** Q3 2026 · Print: Q1 2027 · Live edition: continuous through 2030

> *This proposal treats the book as a strategic publishing asset — not a tutorial. The thesis is that PQC migration is the largest mandated cryptographic transition in computing history, and that the field has produced extensive standards documents, vendor whitepapers, and academic surveys but no single operational handbook for the engineers who must execute. This book closes that gap.*

---

## 1. Executive synopsis

### The book in one paragraph

A 520-page operational playbook for the security engineers, architects, and CISOs who must migrate cryptographic systems from RSA / ECDSA / ECDH to NIST-standardized post-quantum algorithms — **ML-KEM** (FIPS 203), **ML-DSA** (FIPS 204), and **SLH-DSA** (FIPS 205), with forward coverage of **FN-DSA** (draft FIPS 206) and **HQC** as second-line algorithms. The book treats migration as a *program*, not a code change: discovery, inventory (CBOM), risk-based prioritization, hybrid-mode design, protocol-by-protocol rollout (TLS, PKI, SSH, IPsec, code signing, DNSSEC, S/MIME, smart cards, mobile, cloud KMS), operational telemetry, audit alignment (NSM-10 / CNSA 2.0 / OMB M-23-02 / BSI TR-02102 / ANSSI / NCSC / ASD / NICT), and rollback. Every chapter ends with a deliverable a reader can take to a board, an auditor, or a migration sprint.

### What it is NOT

Not a lattice-mathematics textbook. Not a cryptanalysis reference. Not a vendor product manual. Not a speculative "Q-Day" book. Not a beginner cryptography primer. Each of these has a different home and a different shelf life — this book is positioned squarely as a **migration-execution** reference, which is the unfilled slot.

### Composite Opportunity Score (recap)

| Axis | Score | Why |
|---|---|---|
| Market Opportunity (MO) | 10 | Mandated buyer cohort; CNSA 2.0 deadlines bind; every Fortune-2000 needs ≥1 copy per security team |
| Revenue Potential (RP) | 9 | Hardback + workbook + course + cert-prep + multi-language; institutional licensing path |
| Academic Impact (AI) | 8 | Will anchor PQC-engineering tracks in MS-Cyber programs |
| Research Relevance (RR) | 8 | Practitioner side of an active research front |
| Longevity (LV) | 9 | Standards-anchored = 5-7 year evergreen with planned 2nd edition at FIPS 206 / HQC finalization |
| Commercial Scalability (SC) | 9 | German / French / Japanese / Korean / Spanish co-editions natural |
| **COS** | **9.1** | **Highest-COS unfilled slot in deep-tech publishing today** |



---

## 2. The strategic case — why this book, why now

### The closing window

The PQC migration window is publicly defined by a stack of regulatory deadlines that did not exist when most current cryptography books were written. The book is timed to reach shelves *during* the active migration phase — neither too early (when standards were still drafts) nor too late (when the work is done).

| Authority | Anchor document | Binding milestone | Implication for the book |
|---|---|---|---|
| US NSA / CNSS | **CNSA 2.0** (Sept 2022, updated Nov 2024) | Software/firmware signing 2025 → web/server 2025-2027 → networking 2026-2030 → full transition by **2033** | The 2026-2030 window is the migration peak; the book is the field manual |
| US White House | **NSM-10** (May 2022) | Federal agencies inventory by 2023; full transition by **2035** | Agency CIOs and contractors are mandated buyers |
| US OMB | **M-23-02** | Annual migration progress reports | Audit-grade documentation is mandatory; the book provides templates |
| NIST | **FIPS 203, 204, 205** (Aug 2024); HQC selection (March 2025); **NIST SP 1800-38** (NCCoE migration practices); **NIST IR 8547** (transition guidance) | Standards now stable enough to commit to print | The book can confidently anchor on finalized standards |
| Germany BSI | **TR-02102-1** | Hybrid PQC recommended now, mandatory for high-assurance | German co-edition is a mandate-driven market |
| France ANSSI | **PQC position paper** (three-phase roadmap) | Hybrid required 2025-2030; native PQC post-2030 | French co-edition equally mandate-driven |
| UK NCSC | **PQC migration guidance** | Hybrid permitted until 2035 | UK / Commonwealth English market |
| Australia ASD | **ISM** updates | PQC integration ongoing | AUKUS-Pillar-II adjacency |
| Japan NICT / CRYPTREC | National PQC selection | Aligning with NIST + adding domestic algorithms | Japanese co-edition |
| EU | **NIS2** + ENISA guidance + EUDI Wallet PQC integration | Cascade through critical-infrastructure operators | Multi-language EU pressure |

### Why no comprehensive book exists yet

Three reasons, none of them temporary, all of them addressable:

1. **The standards finalized recently (Aug 2024).** Every prior book on PQC has had to hedge on parameters and APIs. With FIPS 203/204/205 stable, an authoritative practitioner book is finally possible.
2. **The cryptography-academic / security-engineering gap.** Existing PQC literature is written by lattice cryptographers for other lattice cryptographers. The audience executing migrations — security architects, PKI operators, platform engineers, GRC professionals — does not read STOC papers. The translation has not been done at book length.
3. **The migration discipline is itself new.** "Crypto migration as a program" did not exist as a named practice before NSM-10. The book partly *creates* the discipline it documents.

### Why this is the right book at the right moment

A book published in **2026-Q4 / 2027-Q1** lands precisely in the steepest part of the enterprise migration curve. Buyers will be mid-program — past the inventory phase, deep in protocol-by-protocol rollout, and starting to face audit deadlines. They need a single reference, not 47 vendor whitepapers and an arXiv folder. The book is also positioned for a planned **second edition in 2028-2029** when FIPS 206 (FN-DSA) and the HQC FIPS finalize, plus a **third edition around 2031** as enterprises move from hybrid to native PQC under CNSA 2.0 phase-out timelines.



---

## 3. Audience map

The book is deliberately written for *one* primary audience and consciously serves three secondary cohorts in clearly demarcated chapters. It refuses to chase a fourth.

### Primary — the people who must execute the migration
- **Security architects** (Principal / Staff level) leading enterprise crypto migration programs.
- **PKI and identity operators** running internal CAs, HSM fleets, certificate-lifecycle systems.
- **Platform / infrastructure engineers** who own TLS termination, mTLS, code-signing pipelines, KMS.
- **Application security engineers** facing protocol-by-protocol decisions in their own codebases.

These readers have 7-15+ years of experience, are comfortable with TLS internals and PKI, and need a *senior-engineer voice* that does not waste their time on basics. They typically buy 2-4 hardback technical references per year and pay $80-110 for them.

### Secondary cohort A — CISOs and security executives
The book has a dedicated **Chapter 2 (the strategic case)**, **Chapter 17 (governance & audit)**, and **Chapter 21 (board reporting)**. These chapters are written so a CISO can read three chapters and ten appendix tables and walk into a board meeting. The 30-page **Executive Annex** at the back is a stand-alone artefact a CISO can hand to a board director without expecting them to read the rest.

### Secondary cohort B — GRC, internal audit, compliance
The book provides explicit **control mappings** (NIST SP 800-53 Rev 5 / ISO 27001:2022 / SOC 2 / PCI-DSS 4.x / HIPAA / GDPR), audit evidence checklists, and the CBOM (cryptographic bill of materials) template. This is the cohort that drives institutional purchase orders.

### Secondary cohort C — Embedded / firmware / IoT engineers
Two chapters (constrained-device PQC; firmware signing with stateful hash-based schemes) serve this cohort directly. They read the book selectively and usually buy through corporate library licenses.

### Explicitly NOT served
- Academic cryptographers seeking lattice-mathematics depth — referred to Peikert/Regev/Lyubashevsky surveys.
- Beginners learning cryptography for the first time — referred to Boneh/Shoup, Katz/Lindell, Aumasson, *Real-World Cryptography*.
- Cryptanalysis researchers — referred to Crypto / Eurocrypt proceedings.
- Investment-thesis / "Q-Day" speculation readers — wrong shelf entirely.

This refusal is editorial discipline, not market loss. Books that try to serve cryptographers *and* CISOs *and* beginners satisfy none of them.


---

## 4. Comp title analysis

A book proposal lives or dies by its comp-title slot. The honest answer for this book is: *the slot is open*. There is no direct competitor at book-length. The closest neighbors illustrate the gap.

| Comp title | What it does well | What it leaves uncovered (i.e., this book's lane) |
|---|---|---|
| Bernstein, Buchmann, Dahmen — *Post-Quantum Cryptography* (Springer, 2009) | The foundational academic reference | Pre-NIST, pre-standards, mathematical not operational; 17+ years out of date for engineers |
| Hoffstein, Pipher, Silverman — *An Introduction to Mathematical Cryptography* (Springer, 2nd ed) | Strong mathematical foundation | Algebraic-number-theory voice; not migration-oriented |
| Christof Paar / Jan Pelzl — *Understanding Cryptography* (Springer) | Most-adopted classroom text | Pre-PQC; classroom voice; no migration program guidance |
| David Wong — *Real-World Cryptography* (Manning, 2021) | Best-in-class working-engineer voice for classical crypto | Touches PQC briefly; not a migration playbook; predates final FIPS |
| Aumasson — *Serious Cryptography* (No Starch, 2nd ed) | Rigorous, accessible, current | Reference rather than program guide; PQC chapter not migration-grade |
| NIST SP 1800-38 (NCCoE) | Formal migration practice guidance | Reference document, not narrative; lacks code, lacks case studies, hard to read end-to-end |
| Cloudflare / AWS / Google / Microsoft PQC blog series | Real production stories | Vendor-specific; fragmented; no longitudinal program view |
| Vendor whitepapers (Thales, Entrust, DigiCert, Venafi, Keyfactor) | Tactical product-aligned guidance | Sales-aligned; product-narrow; no enterprise-program scope |
| IETF drafts (TLS 1.3 hybrid KEMs, composite signatures) | Authoritative protocol specs | Spec-style; not engineering-program reading |

### The structural gap

There is no book on the shelf that answers, simultaneously: *(a) which algorithm do I use here, (b) what does my hybrid TLS handshake look like in production, (c) how do I inventory ten thousand crypto uses across a megacorp, (d) how do I migrate my PKI without breaking S/MIME, code signing, and HSM-bound private keys, (e) what evidence does my auditor want, and (f) how do I report progress to my board?* This is the slot the book fills, and it is large.

### Defensive moat

Once published, the book is hard to compete with for ~36 months because:
- Author profile required (senior crypto-engineer + PKI operator + standards-body voice) is rare.
- Companion artefacts (CBOM templates, lab repo, audit checklists) are an editorial program, not a one-author effort.
- Multi-language editions (German / French / Japanese / Korean / Spanish) compound the lead.
- Cert-prep tie-ins with the emerging PQC migration certifications create a recurring revenue layer.


---

## 5. Editorial principles ("the rules")

These rules are non-negotiable and appear inside the front cover of the manuscript. They protect the book from drifting into the comp-title traps above.

### Rule 1 — Standards-anchored, not vendor-anchored
Every algorithm reference cites the **finalized FIPS** (203 / 204 / 205) by section number, not a library README. Where IETF drafts are referenced (e.g., TLS 1.3 hybrid KEMs), the draft revision is pinned and the second edition will refresh. Vendor APIs are illustrated, never canonical.

### Rule 2 — Hybrid-by-default through 2030
The book treats hybrid (classical + PQC) as the production default for the 2026-2030 window, in line with BSI / ANSSI / NCSC guidance. Native-PQC-only configurations are covered but flagged as risk-asymmetric. This editorial stance ages well: even if NIST allows native-only earlier, the book remains correct; if hybrid extends past 2030, the book remains correct.

### Rule 3 — Migration-as-program, not migration-as-codepath
Every chapter ends with a **deliverable**: a CBOM section, an inventory query, a migration runbook, a test plan, an audit-evidence packet, a board-reporting one-pager. Readers can stitch the deliverables into a complete enterprise program.

### Rule 4 — Library-agnostic in the core, library-specific in the appendix
Core chapters use **OpenSSL 3.5+** (which gained ML-KEM/ML-DSA/SLH-DSA in April 2025) as the primary illustration, with parallel snippets in **AWS-LC**, **Bouncy Castle (Java)**, and **Cloudflare CIRCL (Go)**. Library-specific deep-dives go in **Appendix B**, not the chapter spine, because libraries change faster than the principles do.

### Rule 5 — No constants without context
Every parameter choice (ML-KEM-512 vs. 768 vs. 1024; ML-DSA-44 vs. 65 vs. 87; SLH-DSA fast vs. small) is justified against (a) **NIST security level**, (b) **CNSA 2.0** recommendation, (c) **BSI / ANSSI** position, (d) **operational footprint** (key/sig sizes, latency, MTU). No bare-number recommendations.

### Rule 6 — Performance numbers come from measurement
Where the book quotes a number ("~1.4× TLS handshake latency for hybrid X25519+ML-KEM-768 at p99"), the methodology is in **Appendix C** and the lab is in the GitHub companion repo. Readers can reproduce.

### Rule 7 — Embed the failure modes
Each protocol chapter contains a **"What breaks"** section before the **"What to do"** section. Decapsulation failures, certificate-chain bloat, MTU/fragmentation, FIPS 140-3 module re-validation, side-channel risk, downgrade attacks, hybrid-strip attacks — all named, all engineered for.

### Rule 8 — Live edition discipline
The book ships with a **live errata + tracking microsite** updated quarterly through 2030: standards drift, library version drift, regulatory deadline shifts. The print remains canonical; the microsite is the addendum. This is a Trust signal in a world of LLM-generated technical content.


---

## 6. The required author profile

This book is unusually authorship-constrained. The wrong author writes a book that fails at one or more of its three jobs (engineering depth, operational program, regulatory alignment). The right authoring team has, between two people, the following composite profile:

### Lead author — "the senior security engineer who has shipped a crypto migration"
- 12-20 years in security engineering with at least one of: a TLS 1.3 production rollout at scale, a FIPS 140-3 module submission cycle, a HSM fleet migration, an enterprise PKI operator role.
- Hands-on with **OpenSSL** (3.x preferred) and at least one of **AWS-LC** / **BoringSSL**, **Bouncy Castle**, **CIRCL**.
- IETF, NIST workshop, or RSA Cryptographers' Track speaking history.
- Strong narrative voice; prior published technical writing (book chapters, RFC editorial work, or a 5-year+ technical blog with 10k+ engaged readers).

### Co-author — "the cryptographer who has explained things outside the cryptanalysis community"
- PhD-level cryptographic depth, with publication track record on lattice / hash-based / code-based schemes or implementation cryptography.
- Demonstrated public-explanation work (blog, course, IETF participation, NIST PQC project work).
- Comfortable being the *technical-correctness* reviewer for parameter choices, security claims, side-channel reasoning.

### Optional third contributor — "the GRC / standards specialist"
- Author or contributor to one of: NIST SP 800-53 / SP 1800-38, ISO 27001 control frameworks, EU AI / cyber compliance guidance.
- Writes the audit-evidence chapters and the Executive Annex.

### Why two-or-three authors

A single author cannot cover all three job descriptions credibly. The market discounts a solo author of this book unless the author is one of ~30 publicly known senior PQC engineers globally — and most of them are employed by vendors and cannot author a vendor-neutral book. The two-author model (and the three-author model with a GRC voice) is editorially safer and is also how *the* successful comp titles in adjacent slots were written.

### Author candidates (profile sketch, not endorsement)

The book should be sourced from the population that overlaps:
- **Cloudflare Research / Google Crypto / AWS Crypto** alumni who shipped hybrid TLS at scale.
- **Microsoft PKI engineering** — the team that runs internal CAs for Office / Azure.
- **HSM vendor engineering leads** at Thales / Entrust / Marvell / nCipher who have shipped PQC firmware.
- **NIST PQC Project participants** with implementation track records.
- **BSI / ANSSI / NCSC** affiliates with public-facing technical writing.
- **IETF TLS WG, LAMPS WG, COSE WG** active contributors.

The acquisitions move is to identify two or three names from this overlap and approach them with a co-authoring pitch. The book is more attractive to authors than most because of its long shelf life and series potential — but the authoring window is short, because the same handful of senior people are about to be approached by multiple publishers.


---

## 7. Detailed table of contents

**Structure:** 9 parts · 24 chapters · ~520 pages · ~95 listings · ~40 figures · 6 appendices.

### Part I — The Migration Imperative *(why & what — 3 chapters, ~50 pages)*

#### Chapter 1 — Why Cryptography Has to Change
Shor's algorithm in operational terms (not number theory). Grover and symmetric-key sizing. The "harvest now, decrypt later" threat model and how to reason about it for *your* data shelf life. Distinguishing cryptographically relevant quantum computer (CRQC) timing speculation from the migration deadlines that bind today regardless. The framing: *the migration is happening because the standards exist, the regulations require it, and the data-shelf-life math demands it — not because we know when the quantum computer arrives.*

**Deliverable:** A one-page "data shelf-life vs. migration urgency" matrix the reader can use for any data class in their organization.

#### Chapter 2 — The Standards Landscape
A guided tour of FIPS 203, 204, 205, and the road to 206 (FN-DSA) and HQC; NIST SP 1800-38 (NCCoE), NIST IR 8547; the IETF tracks (TLS, LAMPS, JOSE, COSE, IPsecME, CFRG); the regulatory stack (NSM-10, CNSA 2.0, OMB M-23-02, BSI TR-02102, ANSSI roadmap, NCSC guidance, ASD ISM, NICT/CRYPTREC). Treats the documents as a *system* the reader can navigate, not a list to memorize.

**Deliverable:** A standards-and-regulations map keyed to chapter numbers in the rest of the book.

#### Chapter 3 — Algorithm Selection Without Tears
ML-KEM (FIPS 203): when to use 512 / 768 / 1024 — security level, performance, and what CNSA 2.0 / ANSSI / BSI actually recommend. ML-DSA (FIPS 204): when 44 / 65 / 87 — and why ML-DSA-65 is the *de facto* practitioner default. SLH-DSA (FIPS 205): when stateless hash-based makes sense; the SHA-2-vs-SHAKE choice; the fast-vs-small trade. FN-DSA (draft): tiny signatures, hard to implement safely. HQC: as a backup KEM. Stateful hash-based (XMSS, LMS) for firmware signing. Honest rejection of QKD as a substitute.

**Deliverable:** A 1-page algorithm decision tree with annotated exceptions, suitable for an architecture-review-board meeting.



### Part II — The Standards Toolkit *(deep-but-operational on each algorithm — 4 chapters, ~80 pages)*

#### Chapter 4 — ML-KEM in Production
What a KEM is and is not (the KEM-vs-KEX semantic gap is where most engineering bugs hide). ML-KEM internals at the level needed to debug, not to prove security: keygen, encapsulation, decapsulation, the implicit-rejection mechanism. Performance envelope: keygen / encap / decap on x86-64, ARMv8, ARMv9-with-SVE, and embedded Cortex-M4. Memory and stack footprints. Side-channel posture (constant-time requirements; FO-transform implications). Failure-mode catalogue: malformed ciphertext handling, decapsulation-failure handling, downgrade attacks. Worked examples in OpenSSL 3.5+, AWS-LC, and CIRCL.

#### Chapter 5 — ML-DSA in Production
Lattice signatures: keygen, sign, verify. The *deterministic vs. randomized* signing choice and why it matters for fault attacks. The hint mechanism. Public-key and signature size economics: a 3.3 KB ML-DSA-65 signature versus 64-byte ECDSA — what actually breaks. Latency on x86-64 vs. Cortex-M. Constant-time pitfalls. Composite-signature framing for hybrid certs.

#### Chapter 6 — SLH-DSA in Production
The hash-based signature family. Why SLH-DSA is *stateless* (no key-state to manage) and why that matters compared to XMSS/LMS. Choosing between SHA-2 and SHAKE backends; the fast vs. small parameter trade-off. The "long signing latency" reality and the systems-engineering responses. When SLH-DSA is the right choice (firmware roots-of-trust, long-life signatures, hardware that can't run lattice math safely).

#### Chapter 7 — Stateful Hash-Based Signatures (XMSS, LMS) for Firmware
The state-management problem and how to solve it operationally (HSM-bound state; one-shot signing services; air-gapped procedures). Total-signature budgets and how to size keys (2^20 vs. 2^32). NIST SP 800-208 conformance. When to use stateful HBS vs. SLH-DSA vs. ML-DSA for code/firmware signing. Real CNSA-2.0-compliant code-signing pipeline as a reference architecture.



### Part III — Discovery & Inventory *(you cannot migrate what you can't find — 2 chapters, ~50 pages)*

#### Chapter 8 — The Cryptographic Bill of Materials (CBOM)
The CBOM concept (CycloneDX 1.6+ extension), what it captures, and why it is the *only* foundation that a multi-year migration can be built on. Building a CBOM from heterogeneous inputs: source-code scans, binary analysis (cryptographic library symbol detection), runtime telemetry, network observation, certificate inventories, HSM key escrow records, supply-chain SBOMs. Schema, tooling (open-source + commercial landscape), governance (who owns the CBOM, how it's reviewed, how it's audited).

**Deliverable:** A working CBOM template (CycloneDX-CBOM JSON) with example entries for TLS, code-signing, and KMS use cases.

#### Chapter 9 — Crypto Discovery in Practice
Strategies and tools for the discovery phase by environment: source repositories (semgrep / CodeQL rules included), running services (eBPF-based runtime detection), TLS observation (passive + active scanning), certificate inventories (CT-log + internal-CA reconciliation), HSM enumeration, mainframe and legacy systems, vendor and SaaS dependencies. Risk-based prioritization: data shelf life × exposure × replacement cost. The "long tail" problem: the last 5% of crypto uses cost more to find than the first 95%, and this chapter prevents readers from giving up at 80% coverage.

**Deliverable:** A tiered discovery runbook and a risk-prioritization matrix.

### Part IV — Architecture & Crypto-Agility *(designing for change — 3 chapters, ~70 pages)*

#### Chapter 10 — The Crypto-Agility Pattern Catalogue
Crypto-agility as a discipline. The seven structural patterns (algorithm-neutral APIs, suite negotiation, key-bag indirection, certificate-suite tagging, KMS-of-KMS, dual-stack endpoints, observable rollback). Anti-patterns (hard-coded constants, version-coupled wire formats, key-format-coupled storage). Designing for a *post*-PQC migration: today's PQC choices are not the last; the next rotation is HQC or FIPS 206 or whatever standards add by 2030. The chapter argues that crypto-agility, not PQC itself, is the durable engineering investment.

#### Chapter 11 — Hybrid Modes Done Right
Why hybrid (classical || PQC) is the default for 2026-2030. The two valid hybrid constructions (concatenation KDFs vs. nested KEMs); the IETF/NIST consensus and the cases where vendors disagree. Hybrid TLS, hybrid IKEv2, hybrid certificates (composite signatures vs. parallel signatures vs. dual-cert-chains). Performance and bandwidth costs. The downgrade-prevention problem and how to engineer against it.

#### Chapter 12 — Identity, Keys, and Key Bags
Re-thinking key management for a multi-algorithm world. Key-bag architecture (one logical identity, multiple cryptographic representations). KMS implications (AWS KMS / Azure Key Vault / GCP KMS / HashiCorp Vault — capability matrix). HSM constraints (PKCS#11 v3.x mechanisms; vendor support reality). Hardware-binding tradeoffs (TPM 2.0, secure enclaves) when the algorithms inside them haven't caught up. Identity rotation runbooks.



### Part V — Protocol-Level Migration *(the work itself — 5 chapters, ~140 pages — the heart of the book)*

#### Chapter 13 — Migrating TLS and QUIC
TLS 1.3 hybrid key exchange: the **X25519MLKEM768** group as the deployed default; **SecP256r1MLKEM768** for FIPS-bound contexts. ClientHello sizing and the dreaded "first-flight fragmentation" problem (TLS 1.3 with hybrid groups can push ClientHello past the initial-data MTU on QUIC). Certificate-chain bloat: a typical chain with ML-DSA-65 leaf + intermediate goes from ~3 KB to ~12-20 KB; the operational consequences (TCP slow-start, QUIC initial-packet limits, CDN cache TTLs). Server-side configuration in OpenSSL 3.5+, BoringSSL/AWS-LC, Rustls; client-side (browsers, mobile clients); load-balancer and CDN deployment patterns; canary rollout strategy with observable rollback. The deployed reality from Cloudflare, Google, AWS, Apple iCloud (PQ3-class), Signal (PQXDH) — and what generalizes to enterprise contexts vs. what doesn't.

#### Chapter 14 — Migrating PKI and Certificate Lifecycle
Internal CAs: re-keying root CAs (CNSA 2.0 timeline), issuing PQC-capable subordinate CAs, dual-signing strategies during transition, S/MIME and document-signing implications. ACME flows for hybrid certificates. The composite-signature debate (LAMPS WG): operational implications of composite vs. parallel-cert-chain models. Certificate-store realities: Microsoft AD CS, EJBCA, Keyfactor, Venafi support matrix. CRL and OCSP under PQC sig-size pressure. Public CAs: state of WebPKI roots.

**Deliverable:** A 36-month enterprise PKI migration runbook with dependencies, decision points, and rollback gates.

#### Chapter 15 — Migrating SSH, IPsec, IKEv2, MACsec
OpenSSH PQC support trajectory (sntrup761x25519 → mlkem768x25519); enterprise-fleet migration via configuration management. IKEv2 hybrid KEMs (RFC pipeline). IPsec VPN concentrators and the vendor support matrix as of 2026. MACsec / 802.1X. The "remote access VPN" cohort that is structurally one of the easier migrations and the "site-to-site VPN" cohort that is structurally one of the harder ones.

#### Chapter 16 — Migrating Code Signing, Firmware, and Software Supply Chain
Why this chapter belongs in any serious PQC book: firmware signed today must verify in 2040+, and the "harvest now, decrypt later" threat applies *symmetrically* to "sign now, forge later" if signature schemes are broken in the meantime. Stateful hash-based (LMS / XMSS) for firmware roots-of-trust per NIST SP 800-208. SLH-DSA for general code signing. Supply-chain artifacts (Sigstore, in-toto, SLSA) and how their cryptography migrates. Concrete pipelines: secure boot, OTA updates, container-image signing, package-manager signing.

#### Chapter 17 — Migrating Other Protocols
DNSSEC under signature-size pressure (DNS UDP 512-byte / EDNS0 implications); the realistic timetable for DNSSEC PQC. S/MIME and email at scale. IoT/MQTT/CoAP. Kerberos. Mainframe (IBM Z PCIe HSMs and CCA / EP11 PQC roadmap). Bluetooth LE Secure Connections. Brief and honest treatment of WebAuthn/FIDO2 (which is largely orthogonal but worth a section).



### Part VI — Domain-Specific Migration *(the audiences with special constraints — 3 chapters, ~70 pages)*

#### Chapter 18 — PQC on Constrained Devices
Cortex-M0+ / M3 / M4 / M33 / RISC-V realities. ML-KEM-512 / ML-DSA-44 vs. SLH-DSA on flash / RAM budgets. Stack usage and interrupt-latency implications. Side-channel mitigations on devices without dedicated crypto coprocessors. PQC for automotive ECUs (ISO/SAE 21434, UNECE R155, AUTOSAR Crypto Stack realities). Industrial-control / OT environments where 20-year device lifecycles make migration uniquely difficult. The honest answer for the smallest devices: stateful HBS for verification, classical for now, plan a hardware refresh.

#### Chapter 19 — PQC in Cloud and Hyperscale
AWS, Azure, GCP, and Oracle Cloud current PQC posture across KMS, CloudHSM, ACM, certificate management, load-balancing, VPN, and SDK layers. Hyperscaler hybrid-TLS deployment status. Container and Kubernetes implications (mTLS in service meshes — Istio, Linkerd, Consul Connect; Envoy / nginx config). Serverless / managed-edge (CloudFlare Workers, Lambda@Edge, Vercel) PQC support. Multi-cloud key management under PQC. The "vendor-mandates-an-algorithm-but-CNSA-wants-a-different-one" tension, with concrete resolution patterns.

#### Chapter 20 — Mobile, Browser, and End-User Endpoints
iOS and Android crypto-stack PQC support trajectories. Apple iCloud Private Relay / iMessage PQ3 lessons. Android Keystore. WebAuthn/FIDO and the relyiability of physical-token vendors. Browser support matrix (Chrome / Edge / Firefox / Safari) for hybrid TLS — what works today, what's on the roadmap. Captive-portal / proxy implications. End-user device fleet management (MDM-driven crypto-policy rollout).

### Part VII — Operations *(running migrated systems in production — 2 chapters, ~50 pages)*

#### Chapter 21 — Telemetry, Monitoring, Performance, Rollback
Observability for PQC: metric design (handshake latency by algorithm, decapsulation-failure rates, certificate-chain-size percentiles, hybrid-strip alerts). Honest performance baseline numbers across cloud and on-prem (with methodology in Appendix C). Rollback gates: when a PQC rollout goes wrong, what telemetry signals it and how to bail out without breaking outstanding sessions. SLA and capacity planning with larger keys and signatures.

#### Chapter 22 — Incident Response and Crypto-Failure Modes
Incident classes specific to crypto-migration: hybrid-strip attacks, downgrade attempts, cipher-suite mis-negotiation, decapsulation-failure storms (memory-pressure DoS), HSM-binding mismatches under multi-algorithm key bags, certificate-chain-size DoS on weak clients. Runbooks for each. The role of crypto-agility in *enabling* incident response (rotate the algorithm, not the system).



### Part VIII — Governance, Audit, and Compliance *(making it auditable — 2 chapters, ~50 pages)*

#### Chapter 23 — Governance, Audit Evidence, and Control Frameworks
Mapping the migration to control frameworks the auditor expects: NIST SP 800-53 Rev 5 (SC-12, SC-13, SC-17, SC-28 and their PQC implications), ISO/IEC 27001:2022 / 27002, SOC 2, PCI-DSS 4.x, HIPAA Security Rule, GDPR Art. 32. The audit-evidence packet: what specifically the auditor wants to see (CBOM excerpts, migration-runbook artifacts, rollback-test evidence, sign-offs). FIPS 140-3 module-validation realities for PQC: the lag between standard finalization and module certification; how to plan procurement around it.

#### Chapter 24 — Reporting Up: Boards, Regulators, Customers
The 2-page board update template (and what *not* to put in it). The regulator-correspondence template. The customer-trust statement template (used for B2B SaaS where customers ask "are you PQC-ready?"). The CISO-to-CFO conversation about budget cycles relative to CNSA 2.0 deadlines. Vendor due-diligence questionnaires (the questions to ask of every vendor in your supply chain).

### Part IX — Case Studies *(narrative, anonymized, with permission — included as a closing arc, ~40 pages)*

The three case studies (subject to securing permissions; multiple candidates exist):

- **Case Study A — A regulated US bank** moving from RSA-2048 / ECDSA-P256 to hybrid TLS and ML-DSA-65 PKI under SR 11-7 model-risk and PCI-DSS pressures. Focus: governance, vendor management, audit evidence.
- **Case Study B — A European industrial OEM** migrating embedded-device firmware signing under the EU Cyber Resilience Act and BSI guidance. Focus: stateful hash-based key management, hardware refresh planning.
- **Case Study C — A US hyperscaler service** rolling out hybrid TLS to billions of connections and the operational lessons. Focus: telemetry, rollback, MTU/fragmentation engineering.

### Appendices *(reference material — ~80 pages)*

- **Appendix A** — Algorithm reference cards (one page per algorithm: parameters, sizes, performance envelopes, recommended use, regulatory positioning).
- **Appendix B** — Library reference (OpenSSL 3.5+, AWS-LC, BoringSSL, Bouncy Castle, CIRCL, liboqs, PQClean, Microsoft SymCrypt, Mbed TLS) — capability matrix, common pitfalls, version-pinning guidance.
- **Appendix C** — Performance methodology and reference numbers, with full reproduction instructions.
- **Appendix D** — Standards-and-regulations cross-reference (every chapter mapped to FIPS / SP / ISO / IETF documents).
- **Appendix E** — The CBOM template (CycloneDX-CBOM JSON), commented.
- **Appendix F** — Glossary, with explicit anti-glossary ("words you will hear in vendor pitches that mean nothing operationally").

### Front matter — the Executive Annex (30 pages, separately downloadable)

A self-contained executive briefing that maps to chapters 1, 2, 23, 24, and the case studies. Designed to be handed to a board director or audit committee chair. Distributed as a free PDF to drive paid-book sales — a known-good trade-publishing tactic.



---

## 8. Sample chapter — *Chapter 13: Migrating TLS and QUIC* (deep outline)

This is the chapter most reviewers will skim first; it is also the chapter with the most direct production payoff for the largest reader cohort. Below is the sample-chapter outline at the level of detail used during the manuscript phase.

### 13.1 — What we are actually migrating

Open with the engineering claim that drives the chapter: **TLS 1.3 is the migration's single largest surface** — it terminates almost everything else (HTTPS, gRPC, mTLS, service mesh, Kafka-over-TLS, database-over-TLS). Migrating TLS migrates *most* of an enterprise's encrypted-in-transit footprint by traffic volume, by handshake count, and by audit scope.

What we *aren't* migrating in this chapter: the symmetric record layer (AES-256-GCM is fine post-quantum modulo Grover's halving — a rule of thumb the chapter justifies but does not labor). This is the operational point: PQC migration in TLS is **handshake-only**.

### 13.2 — The hybrid key-exchange that won

A crisp explanation of how hybrid groups work in TLS 1.3: the named groups field carries one or more KEM identifiers; **X25519MLKEM768** concatenates the X25519 ECDH shared secret and the ML-KEM-768 encapsulated secret into the key schedule via the standard hybrid construction. Why this won (security retains classical guarantees if either KEM is broken; deployable inside TLS 1.3 unchanged; ML-KEM-768 hits the NIST Level 3 / CNSA 2.0 sweet spot at acceptable size). Why **SecP256r1MLKEM768** matters in FIPS-bound contexts (one approved curve + one approved KEM; ML-KEM-1024 variant exists for full CNSA 2.0 Level 5 alignment).

The exact byte counts the engineer needs:

| Group | Client KeyShare | Server KeyShare | Notes |
|---|---|---|---|
| X25519 (classical) | 32 B | 32 B | Baseline |
| **X25519MLKEM768** (hybrid) | 32 + 1184 = **1216 B** | 32 + 1088 = **1120 B** | Deployed default |
| **SecP256r1MLKEM768** (hybrid, FIPS) | 65 + 1184 = **1249 B** | 65 + 1088 = **1153 B** | FIPS-bound |
| ML-KEM-1024 only (Level 5) | 1568 B | 1568 B | CNSA 2.0 max |

### 13.3 — The first-flight problem

The single biggest operational gotcha in PQC TLS deployment, named explicitly:

> A TLS 1.3 ClientHello carrying an X25519MLKEM768 key share crosses the typical 1500-byte Ethernet MTU and pushes past the QUIC initial-packet 1200-byte ceiling. The result is fragmentation — and on QUIC, packet *coalescing* across multiple Initial datagrams that some middleboxes do not handle gracefully.

The chapter walks through the failure modes (TCP path-MTU blackholes, QUIC initial-packet drops, middlebox cipher-suite stripping), how to detect them (which telemetry signals fire), and the engineering responses (server-side `record_size_limit` extensions, QUIC initial-packet padding strategies, MSS clamping at ingress, hybrid-disable for known-bad client populations).



### 13.4 — The certificate-chain problem

A worked example: a typical 3-level chain (leaf + intermediate + cross-signed root) signed under ML-DSA-65 with ML-DSA-65 public keys grows from roughly 3 KB to **~12-18 KB** depending on chain shape, before adding SCTs for Certificate Transparency. The chapter quantifies the consequences in three dimensions:

1. **Latency** — TLS handshake bytes interact with TCP slow-start (initial congestion window typically 10 MSS = ~14.6 KB); chains that previously fit comfortably now graze the limit and add an RTT for new connections.
2. **CDN economics** — cache TTLs, edge-to-origin connection reuse, and TLS resumption all shift in significance because the cost-per-fresh-handshake rises.
3. **Constrained clients** — IoT and mobile-low-bandwidth clients can fail entirely against larger chains; the chapter provides a triage matrix.

Engineering responses: **chain truncation strategies** (cross-signing topologies that minimize chain length); **intermediate suppression** (RFC 7250 raw public keys for internal mTLS where appropriate); **session resumption hygiene** (session-ticket TTL tuning, 0-RTT economics under PQC); **post-handshake authentication** as an option for some workloads.

### 13.5 — Server-side configuration

OpenSSL 3.5+ configuration walked end-to-end (with the same configuration shown in AWS-LC and BoringSSL idioms in callout boxes):

- Compile-time: PQC providers / build flags
- Runtime: `SSL_CTX` configuration of named groups, signature algorithms, and certificate selection callbacks for hybrid-cert deployment
- nginx, Apache httpd, Envoy, HAProxy: configuration recipes with rationale
- Load balancer realities: AWS ALB / NLB current PQC posture; GCP HTTPS LB; Azure Front Door; F5 / Citrix on-prem

Each recipe is paired with the *telemetry* needed to know it's working — not just "tcpdump shows the bytes" but the production-grade metrics (handshake-by-named-group histogram, certificate-by-signature-algorithm counter, fallback events, error-class distribution).

### 13.6 — Client-side migration

Browsers (Chrome / Edge / Firefox / Safari): current PQC-hybrid posture, enterprise-policy levers, captive-portal compatibility. Mobile (iOS / Android): platform-API trajectories. Programmatic clients: curl, Go (`crypto/tls`), Rust (`rustls`, `s2n-tls`, `rusttls-pqc-fork`), Java (Bouncy Castle BCJSSE), Python (`cryptography`, `pyca/cryptography` PQC roadmap).

The hard cases get their own sub-section: legacy Windows clients, Java 8, embedded TLS stacks (mbedTLS, wolfSSL) and their PQC build flags.

### 13.7 — Canary and rollback

The production-grade rollout pattern: percentage-rollout by named group, observability gates that auto-pause at signal thresholds, the rollback-without-disconnecting-active-sessions trick (ticket-key rotation + group preference change), and the "permanent telemetry" the team keeps even after rollout completes (so a regression in 2028 is detectable).

### 13.8 — What CDNs and hyperscalers learned

A frank synthesis of the 2023-2026 deployments at Cloudflare (X25519Kyber768Draft00 → X25519MLKEM768), Google (Chrome + Google Front End), AWS (s2n-tls, ALB), Apple (PQ3 / iCloud Private Relay), Signal (PQXDH). What generalizes (the canary playbook; the telemetry stack; the fragmentation engineering) and what doesn't (most enterprises don't have CDN-scale telemetry). The "lesson translation matrix" closes the chapter.

### 13.9 — Chapter deliverable

A 12-page **TLS / QUIC migration runbook** the reader can fork and adapt: discovery questions, decision points, configuration templates, telemetry definitions, canary criteria, rollback gates, audit-evidence checklist. The runbook is also the chapter's GitHub artifact.



---

## 9. Standards & regulations mapping

Every chapter is anchored to the documents an auditor or architecture-review board cares about. This is the table the front matter prints in full and the rest of the book references chapter-by-chapter.

| Document | Author | Role in the book |
|---|---|---|
| **FIPS 203** — Module-Lattice-Based Key-Encapsulation Mechanism Standard | NIST (Aug 2024) | ML-KEM canonical reference (Ch 4, 11, 13, 15, 19) |
| **FIPS 204** — Module-Lattice-Based Digital Signature Standard | NIST (Aug 2024) | ML-DSA canonical reference (Ch 5, 14, 16, 17) |
| **FIPS 205** — Stateless Hash-Based Digital Signature Standard | NIST (Aug 2024) | SLH-DSA canonical reference (Ch 6, 16) |
| **FIPS 206** (draft) — FN-DSA | NIST (expected 2026-2027) | Forward coverage; pinned in 2nd edition |
| **NIST SP 800-208** — Stateful Hash-Based Signature Schemes | NIST | XMSS / LMS for firmware (Ch 7, 16) |
| **NIST SP 800-227** — Recommendations for Key Encapsulation Mechanisms | NIST (drafted) | KEM hygiene, decapsulation-failure handling (Ch 4, 11) |
| **NIST IR 8547** — Transition to Post-Quantum Cryptography | NIST | Migration framing (Ch 1-3) |
| **NIST SP 1800-38** — Migration to Post-Quantum Cryptography | NCCoE | Migration practices (Ch 8-12, 23) |
| **NIST SP 800-53 Rev 5** | NIST | Control mapping (Ch 23) |
| **NSM-10** | White House (May 2022) | Federal mandate (Ch 1, 23, 24) |
| **CNSA 2.0** (Sept 2022, updated Nov 2024) | NSA / CNSS | National-security migration timeline (Ch 1-3, 23) |
| **OMB M-23-02** | OMB (Nov 2022) | Federal-agency migration plan template (Ch 23, 24) |
| **EU AI Act / NIS2 / Cyber Resilience Act / EUDI Wallet specs** | EU | EU regulatory anchor for German/French/EU co-editions (Ch 14, 18, 23) |
| **BSI TR-02102-1** | German BSI | German recommendations + hybrid posture (Ch 11, 23) |
| **ANSSI PQC position paper** | French ANSSI | Three-phase French roadmap (Ch 11, 23) |
| **NCSC PQC migration guidance** | UK NCSC | Hybrid window through 2035 (Ch 11, 23) |
| **ASD ISM** | Australian ASD | AUKUS-Pillar-II adjacency (Ch 23) |
| **NICT / CRYPTREC** | Japan | Japanese alignment + JP co-edition basis (Ch 23) |
| **IETF — TLS 1.3 hybrid groups (draft-kwiatkowski-tls-ecdhe-mlkem)** | IETF TLS WG | TLS-specific (Ch 13) |
| **IETF — Composite signatures (draft-ietf-lamps-pq-composite-sigs)** | IETF LAMPS | Hybrid certs (Ch 14) |
| **IETF — IKEv2 hybrid KE (draft-ietf-ipsecme-ikev2-pqc-mixed)** | IETF IPSECME | VPN-specific (Ch 15) |
| **ISO/IEC 27001:2022, 27002:2022** | ISO | Audit-control mapping (Ch 23, 24) |
| **PCI-DSS 4.x** | PCI SSC | Cardholder-data crypto control mapping (Ch 23) |
| **CycloneDX 1.6 + CBOM extension** | OWASP / CycloneDX | CBOM artifact (Ch 8, App E) |

Where a document is in draft (e.g., FIPS 206, several IETF specs), the book pins to the revision used and the **live errata microsite** updates as standards finalize.



---

## 10. Companion artifacts

The book ships with a coordinated artifact bundle. These are designed for two reasons: (a) they make the book *useful* on Monday morning, and (b) they create durable institutional value that competitors cannot replicate without an equivalent multi-year effort.

| Artifact | Format | Purpose | Distribution |
|---|---|---|---|
| **GitHub companion repository** | Code, configs, runbooks | Reproducible labs for every protocol chapter (Docker Compose stacks for OpenSSL 3.5+, AWS-LC, BoringSSL, Bouncy Castle); benchmark harness; sample CBOMs | Public, MIT-licensed |
| **CBOM template** (CycloneDX-CBOM JSON) | JSON + reference docs | Drop-in starting point for enterprise CBOM programs | Inside repo |
| **Migration runbook templates** (TLS, PKI, SSH/IPsec, code signing, firmware) | Markdown + JSON | Forkable runbooks tied to chapter content | Inside repo |
| **Audit-evidence checklists** | PDF + spreadsheet | Mapped to NIST SP 800-53, ISO 27001, SOC 2, PCI-DSS 4.x | Free download with proof of book purchase |
| **Discovery rules** (semgrep, CodeQL) | Rule packs | Source-code crypto-discovery starter kit | Inside repo |
| **Live errata + standards-tracker microsite** | Web | Quarterly updates through 2030 on FIPS 206 / HQC FIPS / IETF drafts / vendor support | Free; drives book recurring relevance |
| **Executive Annex PDF** | PDF (30 pp.) | CISO/board-ready briefing | Free download — drives paid-book sales |
| **Workbook** (paid companion) | Print + ebook | Exercises + worked examples; cert-prep aligned | Sold separately at ~$35 |
| **Audio companion** | Podcast-style audio | 12-15 hours; not the book read aloud — separately produced expert dialogues per part | Sold separately or bundled |
| **Cert-prep guide** (paid companion) | Print + ebook | Maps to emerging PQC-migration certifications as they finalize | Sold separately |
| **Multi-language editions** | Print + ebook | German (DE), French (FR), Japanese (JP), Korean (KR), Spanish (ES, with LATAM reach) | 12-18 months after English release |

The artifact program triples per-buyer revenue versus a stand-alone book (the bundle economics are closer to a course program than to a single title) and creates a network effect — the CBOM and runbook templates become *de facto* community standards if the book hits its target adoption.



---

## 11. Production plan

### Manuscript milestones

| Phase | Window | Output |
|---|---|---|
| **Author engagement & co-author finalization** | Q2 2026 | Signed author agreement; preliminary outline (this proposal as base) |
| **Detailed outline + sample chapters (Ch 1, 13)** | Q2-Q3 2026 | Outline review; technical-reviewer panel formed |
| **Manuscript drafting Wave 1 — Parts I-III (Ch 1-9)** | Q3 2026 | First 200 pages; technical review pass 1 |
| **Manuscript drafting Wave 2 — Parts IV-V (Ch 10-17)** | Q3-Q4 2026 | The protocol-migration spine; technical review pass 2; companion repo v0.1 public |
| **Manuscript drafting Wave 3 — Parts VI-IX + appendices** | Q4 2026 - Q1 2027 | Manuscript complete; copy edit; production |
| **Production** | Q1 2027 | Page proofs; index; final tech review pass 3 |
| **Print release** | Q2 2027 | Hardback + ebook + early Live edition microsite |
| **Workbook and Cert-prep companion** | Q3 2027 | Paid bundle complete |
| **DE, FR, JP, KR, ES editions** | Q4 2027 - Q2 2028 | Localized editions, native-edited, regulatory references localized |
| **2nd edition** | 2028-2029 | Refresh for FIPS 206 / HQC FIPS finalization, live deployment lessons |
| **3rd edition** | 2030-2031 | Hybrid → native-PQC transition coverage, full CNSA 2.0 deadline alignment |

### Technical review panel

Three reviewer cohorts are signed before manuscript drafting:
1. **Standards reviewer** — IETF / NIST workshop participant.
2. **Production reviewer** — at least one engineer who has shipped a production hybrid TLS rollout.
3. **GRC reviewer** — internal-auditor or compliance-officer who has signed an audit report.

Three review passes (per Wave above) are budgeted; a fourth is on standby for regulatory-document drift.

### Page count, listings, figures

- **Body:** 440 pages
- **Appendices:** 80 pages
- **Listings:** ~95 (avg 8-25 lines; a handful longer in protocol chapters)
- **Figures:** ~40 (architecture diagrams, sequence diagrams, performance curves)
- **Tables:** ~60 (parameters, sizes, control mappings)
- **Total trim:** **~520 pages** at standard No Starch / Wiley Senior trim — substantive without being a doorstop

### Production tooling

- AsciiDoc-based source for cross-format generation (print, ebook, web).
- Listings auto-extracted from the GitHub companion repo (single source of truth — listings are tested in CI; broken listings fail the manuscript build).
- Diagrams in source (Excalidraw / D2 / PlantUML) so the figure pipeline is reproducible across editions.



---

## 12. Pricing and business case

The numbers below are *order-of-magnitude triangulations* using comparable senior-practitioner technical titles, multi-language adaptation economics, and the certification-economy revenue layers we have data on. They are not forecasts; they are the framework an acquisitions editor would use to size the deal.

### SKU and pricing strategy

| SKU | Format | Price (USD) | Notes |
|---|---|---|---|
| English hardback | Print | $79.99 | Senior-practitioner pricing band |
| English ebook | EPUB / PDF / Kindle | $59.99 | Library-friendly DRM-light option |
| English print + ebook bundle | Both | $89.99 | Default direct-from-publisher SKU |
| Workbook (paid companion) | Print + ebook | $34.99 | Sold separately; bundled at $109.99 |
| Cert-prep guide | Print + ebook | $39.99 | Activated when PQC cert finalizes |
| Audio companion | DRM streaming + DL | $29.99 | Bundle option only |
| **English "Migration Bundle"** (book + workbook + audio + Live edition) | All | **$149.99** | The B2B primary SKU |
| Localized editions (DE / FR / JP / KR / ES) | Print + ebook | Local pricing | Native-published; revenue-share with co-publisher |
| **Enterprise site license** (≥25 readers) | Digital | from $4,500 | The single largest revenue stream |
| Cert-prep program partnership | Recurring | TBD | Per-cert revenue share |

### Unit-volume frame (3-year, English-edition cumulative)

A senior-practitioner technical title in a regulation-mandated lane typically sees this shape (informally triangulated against analogous titles on PCI-DSS, GDPR, and previous standards-driven security migrations):

| Year | Print + ebook units (English) | Bundle units | Site licenses | Translation rights |
|---|---|---|---|---|
| Year 1 (2027) | 18-25k | 4-7k | 80-150 | 4-5 territories signed |
| Year 2 (2028) | 22-30k | 8-12k | 200-350 | All major territories live |
| Year 3 (2029) | 18-26k | 6-10k | 250-450 | 2nd edition launch |
| **3-yr total** | **58-81k** | **18-29k** | **530-950** | — |

### Revenue framing

Triangulating across SKU mix and license layers, **3-year gross revenue** to publisher is plausibly in the **$8-15M USD** range for the English program, plus **$3-7M USD** across the localized editions, plus enterprise license and cert-prep revenue extending the durable tail through 2031-2033. This puts the title in the *flagship* category for a niche-tech publisher — comparable to a single-title program at the upper end of No Starch's catalog or Wiley's Sybex flagship cert titles.

### Why the gross is unusually durable

- **Mandated buyers** (CNSA 2.0 / NSM-10 / OMB / NIS2 / EU CRA) sustain Year-2 and Year-3 demand long after most technical titles have decayed.
- **Site-license revenue** scales independently of unit sales — every Fortune-2000 security org represents a 25-150 reader institutional deal once the book hits the maturity point.
- **Cert-prep revenue** activates once the PQC migration certifications finalize (likely 2027-2028), creating a recurring revenue layer that did not exist at launch.
- **Multi-language editions** are unusually high-margin because regulatory framings translate well — German / French / Japanese editions are not redundant with English; they are *required* by local procurement.
- **Live edition microsite** keeps the book canonical through the 2nd-edition cycle, suppressing piracy and maintaining institutional relevance.



---

## 13. Marketing & launch strategy

### Launch arc (T-12 months → T+12 months from print)

| Phase | Activity | Outcome |
|---|---|---|
| T-12 mo | Author signing announcement; Substack / blog presence by author(s); IETF / RSA / Real World Crypto talk circuit | Author audience-building; pre-orders at T-3 |
| T-9 mo | Companion repo public (lab v0.1); CBOM template open-sourced | Community signaling; the artifact starts to be cited before the book exists |
| T-6 mo | Sample chapters (Ch 1, 13) published as free PDF; Executive Annex teased | Top-of-funnel; cert-program conversations open |
| T-3 mo | RSA Conference / Real World Crypto / IETF talks aligned to release; pre-order open; analyst briefings (Gartner, Forrester, Forrester Wave on PQC) | Launch-week visibility |
| **T-0 launch** | RSA Conference launch event ideal; coordinated with vendor partners (HSM / PKI / CDN) | Initial sales spike |
| T+1 mo | Black Hat Briefing / DEF CON Crypto-Privacy Village align if timing | Practitioner-community endorsement |
| T+3 mo | First enterprise site-license deals close; first cert-program partnership announced | Year-1 revenue ramp |
| T+6 mo | Localized editions begin shipping (DE first, then FR / JP / KR / ES) | Geographic expansion |
| T+12 mo | Year-1 retrospective; 2nd-edition outline locked | Publisher-side renewal of marketing budget |

### Key channels

1. **Conference circuit** — RSA Conference, Real World Crypto, USENIX Security, Black Hat / DEF CON, IETF (LAMPS / TLS / IPSECME / CFRG WG meetings), PQCrypto, Eurocrypt-adjacent industry day, RSA Cryptographers' Track, CISO Executive Network events.
2. **Practitioner community** — Cloudflare Research / Google Crypto / AWS Crypto blog posts; Cryptography Stack Exchange; r/crypto; Hacker News; the Substacks of *Latacora*-class consultancies, *Trail of Bits*, *NCC Group*, *Cryptosense*.
3. **Standards-body adjacency** — NIST Crypto Reading Club / NIST CRYPTO Forum mailing list; IETF TLS / LAMPS WG meetings; OASIS PKCS#11 TC; ETSI Quantum-Safe Cryptography ISG.
4. **Vendor co-marketing** — Cloudflare, AWS, Microsoft (Azure / Identity), Google Cloud, Thales, Entrust, DigiCert, Keyfactor, Venafi, HashiCorp, Okta. Each has a PQC story they are eager to anchor in a credible third-party reference. Co-marketing should be vendor-neutral on substance and vendor-coordinated on launch-week timing.
5. **Cert / standards bodies** — ISC2, ISACA, IAPP, (ISC)², SANS — for cert-prep partnerships and member-discount channels.
6. **Government / regulator channels** — NIST NCCoE, CISA, the EU Cybersecurity Atlas — institutional review copies in exchange for endorsements (subject to appropriate firewalls).
7. **Long-form podcasts** — Security Cryptography Whatever, Risky Business, The Cloudcast, Decipher, *Soatok*-class crypto culture spaces. Podcast endorsements move enterprise-buyer perception more than reviews.

### The "trust ladder"

Marketing for this book is fundamentally about establishing trust in a category increasingly polluted by AI-generated content. The book wins by visibly out-trusting alternatives:

- **Verified authors** (real people, real production migrations, named) over anonymized AI drafts.
- **Public review panel** (named technical reviewers, named GRC reviewer) listed in the front matter.
- **Reproducible labs** (CI-tested code) over screenshots of vendor consoles.
- **Live errata microsite** signaling continued maintenance.
- **Publisher attestation** of editorial process and any AI-assistance disclosure.



---

## 14. Risks and mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **FIPS 206 (FN-DSA) finalizes mid-manuscript** | High | Medium | Book is anchored on FIPS 203/204/205; FN-DSA covered in dedicated section flagged "draft until finalized"; live errata + 2nd edition catches up. |
| **HQC FIPS finalizes mid-manuscript** | High | Low-Medium | Treated as second-line KEM; book's hybrid framework already accommodates without rework. |
| **CNSA 2.0 deadlines shift** | Low | Medium | Book emphasizes program structure over specific dates; deadline-table in front matter is one editable page, easily refreshed. |
| **A novel attack on a NIST PQC scheme** (e.g., a new lattice cryptanalysis advance) | Low (now that standards are 2 years old) | High if it happens | Hybrid-default design defends against single-scheme failure; book's architectural framing remains valid; specific algorithm advice updates via live errata + emergency 2nd-edition. |
| **Library churn** (OpenSSL, AWS-LC, Bouncy Castle versions) | Very high | Low individually, medium cumulative | Library-agnostic core in chapters; library-specific detail in Appendix B (easily refreshed); listings auto-tested in CI. |
| **A competing comprehensive book ships first** | Medium | High | Aggressive author signing (Q2 2026), Q3 2026 sample-chapter release, T-9-month companion repo public — establish the canonical position before competitors. |
| **Author bandwidth collapse** (single author too busy mid-program) | Medium | High | Two-author structure as standard; technical-reviewer panel covers sustained drafting risk; AsciiDoc tooling lowers per-chapter cost. |
| **Vendor-disagreement on hybrid construction** | Medium | Low | Book documents both major hybrid constructions and presents IETF/NIST consensus path; vendor-deviation table in chapter 11 stays current via errata. |
| **AI-generated-book noise erodes discoverability** | High (industry-wide) | Medium | Verified-author program, public technical-reviewer panel, reproducible-lab attestation, conference launch, named institutional endorsements — collectively stand the book apart at the trust signal level. |
| **Regulatory deadline relaxes** (CNSA 2.0 dates slip) | Low-medium | Low | Even with relaxation, hybrid TLS deployment continues at hyperscalers; the migration is happening on technical merit independent of enforcement. |

---

## 15. Series strategy — what this book anchors

A successful publication of #38 unlocks a **named series** the publisher can build over 2027-2031. Candidates from [Phase 5](../05-top-100-book-ideas.md) that fit naturally:

| # | Title | Position in the series |
|---|---|---|
| **38** | *The Post-Quantum Migration Playbook* | **Series anchor / flagship** |
| 39 | *Cryptographic Agility* | Foundational companion (architecture for the *next* migration) |
| 40 | *Cryptographic Inventory and Discovery* | The pre-migration deliverable |
| 41 | *Hybrid TLS in Transition* | Deep-dive companion to the TLS chapter |
| 42 | *PQC for Embedded and IoT* | The constrained-device deep-dive |
| 43 | *PQC for the Web* | The web-scale deep-dive |
| 44 | *PQC for HSMs and Smart Cards* | The hardware-bound deep-dive |
| 45 | *Hash-Based Signatures in Production* | The firmware-signing deep-dive |
| 46 | *Lattice-Based Cryptography After Standardization* (textbook) | The academic-curriculum companion |
| 48 | *The CTO's PQC Migration Plan* | The executive-tier complement |
| 49 | *PQC Audit & Compliance Handbook* | The GRC / cert-prep tier |

The whole arc — **eleven titles** across three years — is the *Trust & Migration* series identified in the [Phase 5 summary](../05-top-100-book-ideas.md) and the [Phase 7 strategic recommendations](../07-strategic-recommendations.md). This book is the title that justifies launching the series.

---

[← Back to Phase 5: Top-100 Book Ideas](../05-top-100-book-ideas.md) · [Back to index](../README.md)
