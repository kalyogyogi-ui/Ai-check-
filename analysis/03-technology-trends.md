# Phase 3 — Technology Trend Analysis

> *For each sub-domain: where is it on the maturity curve, what is the publishing half-life, who is the addressable buyer, and what kind of book is the right book?*

This phase is a **topic-by-topic field guide** for acquisitions decisions. The right book is not the right book for every topic. A practitioner cookbook is right for a `GR` topic with a 2-year half-life; a graduate textbook is right for an `MT` topic with a 10-year half-life; a research monograph is right for an `EM` topic with high citation potential. Mismatching format to maturity is the single most common reason a technical title under-performs.

**Reading legend (recap):**
- Maturity: `EM` Emergent · `EA` Early adopter · `GR` Growth · `MT` Mature · `SAT` Saturated · `DEC` Declining.
- **Half-life (HL):** years until 50% of the book's content is materially obsolete. Use to choose format and pricing.
- **Right format (RF):** Cookbook (CB), In-Action practitioner (IA), Senior practitioner playbook (SPB), Graduate textbook (GT), Undergraduate textbook (UT), Research monograph (RM), Executive briefing (EB), Survey/F&T (SV), Cert prep (CP).

---

## 1. Artificial Intelligence

### 1.1 Generative AI (text, image, video, audio, 3D)
- **Maturity:** `SAT` (text); `GR` (video, 3D, audio); `EA` (long-form video, world models)
- **HL:** 18-24 months
- **Buyer:** Practitioners, product managers, marketing engineers
- **RF:** SPB, CB
- **Publishing read:** The "what is generative AI" beginner shelf is *over*. The advanced production-engineering shelf — fine-tuning, distillation, latency, cost, video pipelines — is **under**-served. Avoid yet another *Build with ChatGPT* book; commission *Production Video-Generation Pipelines* or *Cost-Optimal Image Pipelines for E-commerce*.
- **Contrarian:** Books on **provenance, watermarking, and content authenticity (C2PA + SynthID-class)** are vastly under-supplied relative to the regulatory pressure arriving 2026-2027.

### 1.2 LLM Engineering (prompting, fine-tuning, distillation, post-training)
- **Maturity:** `GR` → tipping into `MT` for foundations; `EA` for post-training (RLAIF, DPO/IPO/KTO descendants, process supervision)
- **HL:** 24-36 months for foundations; 12-18 for post-training specifics
- **Buyer:** ML engineers, applied scientists
- **RF:** SPB, GT
- **Publishing read:** The single most contested commissioning lane in 2026. Winners will be the books that **separate stable engineering principles from API-of-the-month details**. The "techniques that survive model generations" angle is the durable one.

### 1.3 AI Agents and Agentic Workflows
- **Maturity:** `GR` (frontier); the *concept* is hot; the *engineering discipline* is still being invented
- **HL:** 12-18 months for tooling; 4-7 years for principles
- **Buyer:** Engineers, product managers, CTOs
- **RF:** SPB (engineering) + EB (strategy)
- **Publishing read:** The framework-of-the-month problem is severe. Right approach: **two-book strategy**. (a) An opinionated *senior engineering* book on agent architecture as a discipline (state, memory, tool use, evaluation, supervision, observability) that survives framework churn. (b) A *cookbook companion* per major framework (LangGraph, AutoGen, CrewAI, Strands, OpenAI Agents SDK, Anthropic Agents SDK).
- **Contrarian:** **Multi-agent reliability engineering** — a book in the SRE tradition for agent fleets — is a category-creating slot.

### 1.4 Retrieval-Augmented Generation (RAG)
- **Maturity:** `MT` (basic) → `GR` (advanced retrieval, hybrid, agentic-RAG, GraphRAG)
- **HL:** 24-30 months
- **Buyer:** Application engineers
- **RF:** SPB
- **Publishing read:** Beginner RAG glut. Advanced retrieval — query rewriting, re-ranking, hybrid sparse-dense, graph + vector, eval-driven retrieval — is the under-supplied tier.

### 1.5 Multimodal AI
- **Maturity:** `GR` (vision-language); `EA` (vision-language-action, VLA for robotics); `EM` (universal multimodal foundation models)
- **HL:** 24-36 months
- **RF:** GT, SPB
- **Publishing read:** Robotics × multimodal × world-models is the highest-upside intersection. Most "VLA for robotics" content is paper-form; one well-written graduate textbook owns the citation graph for 5-7 years.

### 1.6 Edge AI / On-Device AI
- **Maturity:** `GR` rising fast; `EA` for sub-1B param on-device LLMs, MLX, Apple Foundation Models, Qualcomm AI Hub, Snapdragon X-class
- **HL:** 24-36 months (hardware lineage drives durability)
- **Buyer:** Mobile/embedded engineers, hardware-aware ML engineers
- **RF:** SPB, CB
- **Publishing read:** The **mobile + embedded + automotive** edge-AI shelf is the most under-served high-demand lane in 2026 trade publishing. Books in *Apple-on-device LLM engineering*, *Qualcomm AI Hub deployment*, *automotive ECU LLMs*, *MLX for Apple silicon*, *embedded transformers in C++/Rust* — almost all greenfield.

### 1.7 AI Infrastructure (training, inference, serving, scheduling)
- **Maturity:** `GR` (advanced inference); `EA` (training at >10K GPU scale, MoE serving); `MT` (basic K8s ML)
- **HL:** 36-48 months for principles; 18 for vendor specifics
- **Buyer:** Platform engineers, ML platform teams, cloud architects
- **RF:** SPB, GT
- **Publishing read:** The **inference economics** book — KV-cache, speculative decoding, batching, MoE routing, attention kernel choice, quantization, multi-tenant scheduling — is the highest unmet demand among Series-B+ AI startups. Trade publishers have under-commissioned here because the audience *looks* small but its willingness to pay is exceptional.

### 1.8 AI Governance / Assurance / Audit
- **Maturity:** `EA` → `GR` (driven by EU AI Act, NIST AI RMF, ISO/IEC 42001, MAS Veritas)
- **HL:** 36-60 months (regulation-anchored = stable)
- **Buyer:** Compliance officers, GRC engineers, internal auditors, model-risk managers
- **RF:** EB, SPB, GT, CP
- **Publishing read:** **The AI assurance category is the single most strategically important publishing lane for 2026-2030.** It will drive certification programs (ISACA AAIA, IAPP AIGP, ISO 42001 lead-auditor) and corresponding cert-prep books worth tens of thousands of buyers each, plus enterprise reference works. *Whoever commissions a named "AI Assurance" series with 6-8 anchor titles in 2026 owns this category for 5+ years.*

### 1.9 AI Security / Adversarial ML / Red Teaming
- **Maturity:** `GR` (LLM-era); `EA` (agent attack surfaces)
- **HL:** 24-36 months (attacks evolve; principles older)
- **Buyer:** Security engineers, red teamers, ML engineers
- **RF:** SPB, CB, RM
- **Publishing read:** No Starch's structural lane (see Phase 2). Specific high-COS slots:
  - **Prompt injection and jailbreak as an engineering discipline**
  - **Agentic exploitation: attacking tool use, memory, planners**
  - **Model-extraction and inversion at scale**
  - **Supply-chain attacks on model weights and adapters**
  - **AI-SOC engineering: detecting AI-driven attackers**

### 1.10 Explainable AI and Mechanistic Interpretability
- **Maturity:** `GR` (XAI for tabular/CV); `EA` (mechanistic interpretability for LLMs — sparse autoencoders, circuits, attribution graphs)
- **HL:** 4-6 years for principles
- **RF:** GT, RM
- **Publishing read:** The mechanistic-interpretability research front is producing *the* methodologically novel ML literature of the late-2020s. Anthropic/DeepMind/EleutherAI threads will yield citation-graph-anchoring monographs by 2027-2028. First-mover graduate textbook commissioned in 2026 will own a decade of course adoption.

### 1.11 AI for Verticals
| Vertical | Maturity | Best play |
|---|---|---|
| Healthcare | `GR` | Clinical-AI deployment, FDA SaMD, AI radiology MLOps |
| Finance | `GR` | AI-trading risk, AI-compliance, model risk (SR 11-7 era) |
| Government / public sector | `EA` | OMB M-24-10 aligned AI ops handbooks (greenfield) |
| Defense | `EA` | AI-T&E, JADC2-aligned AI architecture (specialty market) |
| Manufacturing / industrial | `GR` | Industrial AI, MES integration, predictive maintenance |
| Energy | `EA` | AI-grid, AI-fusion, AI-for-petroleum operations |
| Legal | `GR` | Legal AI engineering, retrieval over caselaw |
| Education | `GR` | Tutoring agents, assessment integrity, curriculum AI |
| Agriculture | `EA` | AI-agronomy, sat-imagery + AI |
| Construction | `EM` | AI-BIM, robotic-construction-AI |
| Climate / sustainability | `GR` | AI-climate-modeling, carbon accounting AI |
| Pharma / drug discovery | `GR` | AlphaFold-era pipeline engineering |
| Retail / e-commerce | `MT` | Recsys agents, AI search, returns-AI |
| Media / entertainment | `GR` | AI-VFX, dubbing, music ops |

### 1.12 AI Ethics and Regulation
- **Maturity:** `GR` (regulation-driven)
- **HL:** 5-8 years
- **Buyer:** Policy professionals, lawyers, compliance, executives, students
- **RF:** EB, GT, RM
- **Publishing read:** OUP/CUP/MIT lane. Right plays: *EU AI Act in Practice*, *AI Litigation Handbook*, *AI Procurement for Public Buyers*, *AI in International Humanitarian Law*. Country-by-country AI law handbooks are an under-supplied series opportunity.

### 1.13 AI DevOps / MLOps / AgentOps
- **Maturity:** `MT` (MLOps); `GR` (LLMOps); `EA` (AgentOps)
- **HL:** 24-36 months
- **RF:** SPB
- **Publishing read:** "AgentOps" is the next "MLOps" — book lane is currently empty. First good book wins.

### 1.14 Industrial AI and Robotics
- **Maturity:** `EA` rising fast — humanoid platforms, VLA models
- **HL:** 4-6 years
- **RF:** GT, SPB
- **Publishing read:** Robotics-AI textbook lane is being rebuilt for the VLA era. The post-Russ-Tedrake graduate textbook anchored on VLAs is a generational slot.

### 1.15 AI Product Engineering
- **Maturity:** `GR`
- **HL:** 24-36 months
- **RF:** SPB
- **Publishing read:** The "PM-for-AI-products" shelf is over-supplied at the introductory level and *under*-supplied at the *engineering-PM hybrid* level. Best play: a senior IC + senior PM dual-author book on shipping AI features at platform scale.

---

## 2. Blockchain and Web3

### 2.1 Smart Contracts (EVM, Solana, Move, Cairo)
- **Maturity:** `MT` (EVM/Solidity); `GR` (Move — Aptos/Sui); `EA` (Cairo/StarkNet)
- **HL:** 36-48 months
- **RF:** SPB, CB
- **Publishing read:** Solidity practitioner shelf is mature; the *security-by-design* second-edition wave (post-Foundry, post-fuzzing-default) is the right next move. Move and Cairo are *open* lanes.

### 2.2 Layer 2 Systems (Optimistic and ZK rollups)
- **Maturity:** `GR` → `MT`
- **HL:** 30-42 months
- **RF:** SPB, GT
- **Publishing read:** The *engineering* book on building L2s (sequencers, proving infrastructure, data availability, fault proofs) is the highest-COS slot in this category. Most existing books are conceptual.

### 2.3 Zero-Knowledge Proofs (zk-SNARKs, STARKs, folding schemes, lookup arguments)
- **Maturity:** `GR` (math); `EA` (production engineering); `EM` (folding-schemes ecosystem)
- **HL:** 36-60 months for math; 18-24 for tooling
- **RF:** GT, RM, SPB, CB
- **Publishing read:** The lane is splitting into three: *theory* (CUP/Springer monographs), *circuit engineering* (Halo2, Plonky, Risc0, SP1, Noir cookbooks), and *ZK applications* (privacy, scaling, identity). All three under-supplied vs demand.

### 2.4 Tokenization of Real-World Assets
- **Maturity:** `EA` rapidly moving to `GR` (BlackRock BUIDL, regulated stablecoins, tokenized treasuries, RWA marketplaces)
- **HL:** 4-6 years
- **Buyer:** Asset managers, banks, fintech engineers, regulators
- **RF:** EB, SPB
- **Publishing read:** **Tokenization is the dominant institutional-blockchain story of 2026-2030.** The *RWA reference book* — combining law, structuring, custody, compliance, and engineering — is the largest unfilled slot in finance-tech publishing. Wiley professional + Apress hybrid is the natural home.

### 2.5 DeFi
- **Maturity:** `MT` (mechanisms — AMMs, CLMMs, lending); `GR` (intent-based, aggregators, LRTs); `EA` (institutional DeFi)
- **HL:** 24-36 months
- **RF:** SPB
- **Publishing read:** The "DeFi for institutional risk and compliance" shelf is empty. The "intent-based DeFi engineering" shelf is empty. The "DeFi macro economics" shelf is over-saturated.

### 2.6 DAOs and On-Chain Governance
- **Maturity:** `GR` → modest but durable
- **HL:** 4-6 years
- **RF:** EB, SPB, RM
- **Publishing read:** The "DAO operational governance" handbook (legal entity wrappers, treasury, voting design, sybil resistance) is a defensible niche — small market but very loyal buyers, and US/EU governance reform may amplify this.

### 2.7 Enterprise Blockchain
- **Maturity:** `MT` (Hyperledger lineage); `EA` (enterprise tokenization rails on public chains)
- **HL:** 4-6 years
- **RF:** EB, SPB
- **Publishing read:** Pivot from *permissioned-chain enterprise* (declining) to *enterprise-on-public-chain with privacy layers* (rising). Books that bridge this transition explicitly will outperform.

### 2.8 Blockchain Security
- **Maturity:** `GR`
- **HL:** 24-36 months
- **RF:** SPB, CB
- **Publishing read:** Smart-contract auditor handbooks (Foundry-fuzz, Halmos symbolic, Slither static, Echidna invariants) are an emerging cert-eligible category — first publisher to ship a strong "Smart Contract Audit Engineering" anchor + cookbook combo wins.

### 2.9 CBDC, Stablecoin Infrastructure
- **Maturity:** `EA` globally; `GR` regionally (Hong Kong e-HKD, China e-CNY, EU Digital Euro, Brazil DREX)
- **HL:** 4-6 years
- **RF:** EB, SPB, RM
- **Publishing read:** Central-bank-aligned reference books are a niche but under-served slot. CUP/OUP/MIT are best positioned. Country-specific CBDC implementation studies are uniquely citable.

### 2.10 Cross-chain Systems (bridges, interop, IBC, CCIP)
- **Maturity:** `GR` (bridges); `EA` (IBC outside Cosmos, secure messaging)
- **HL:** 24-36 months
- **RF:** SPB
- **Publishing read:** Books on *secure cross-chain engineering after the bridge-hack era* (lessons from Wormhole, Ronin, Nomad) are the high-credibility lane.

### 2.11 Blockchain Identity (DIDs, Verifiable Credentials, EUDI Wallet)
- **Maturity:** `EA` → `GR` driven by EU eIDAS 2.0 / EUDI Wallet rollouts
- **HL:** 5-7 years
- **RF:** SPB, EB
- **Publishing read:** EU eIDAS 2.0 mandates and the EUDI Wallet ecosystem create *guaranteed* enterprise integration demand from 2026-2027. Practitioner reference is greenfield. German + French + English co-editions especially.

### 2.12 Decentralized AI / Blockchain × AI Infra
- **Maturity:** `EA` → mostly speculation; some real plays (Bittensor, Akash GPU markets, Gensyn, Render)
- **HL:** 18-24 months for the speculative tier; uncertain
- **RF:** EB
- **Publishing read:** Be cautious. The category is hype-heavy and the durable-book risk is high. Best play is a *skeptical but rigorous* survey, not a how-to.

### 2.13 Web3 Infrastructure
- **Maturity:** `GR` (RPC, indexers, account abstraction); `EA` (intents, solver networks)
- **HL:** 24-36 months
- **RF:** SPB, CB
- **Publishing read:** Account abstraction (ERC-4337 + 7702) is the highest unmet practitioner-book demand in the Ethereum ecosystem.

---

## 3. Quantum Technology

### 3.1 Quantum Computing (gate-model)
- **Maturity:** `EA` (NISQ); `EM` (early fault-tolerant)
- **HL:** 5-8 years for principles; 2-3 for SDKs
- **RF:** UT, GT, RM
- **Publishing read:** The Qiskit/Cirq beginner shelf is *over-supplied*. The undersupplied tiers are: (a) **early fault-tolerant algorithms** (post-2024 surface-code, post-magic-state-distillation-revolution material), (b) **hardware-aware compilation**, (c) **quantum + classical hybrid systems engineering** at the data-center level.

### 3.2 Quantum Algorithms
- **Maturity:** `GR` (QML claims fading); `EA` (quantum chemistry, optimization realism); `EM` (cryptanalysis-relevant algorithms)
- **HL:** 6-10 years
- **RF:** GT, RM
- **Publishing read:** *Realistic* quantum-advantage textbooks — explicitly distinguishing theoretical advantage from end-to-end advantage including I/O — are needed. The "quantum will solve everything" tone has dated badly; an honest successor textbook is overdue.

### 3.3 Quantum Cryptography (QKD, QRNG)
- **Maturity:** `EA` (commercial QKD products); `MT` (QKD theory); `EM` (device-independent QKD)
- **HL:** 6-10 years
- **RF:** RM, GT
- **Publishing read:** Niche but durable. Combine with PQC migration narratives for broader market access.

### 3.4 Post-Quantum Cryptography (PQC) — *the* breakout category
- **Maturity:** `GR` rapidly (NIST FIPS 203/204/205 finalized; HQC selected; CNSA 2.0; NSM-10 deadlines; EU PQC mandates following)
- **HL:** 6-10 years (standards-anchored)
- **Buyer:** Security engineers, cryptographers, GRC, CISOs, sovereign customers
- **RF:** SPB, GT, CP, RM, EB
- **Publishing read:** **PQC is the highest composite-opportunity-score topic across the entire deep-tech publishing landscape, period.** Specifically:
  - *PQC migration handbook* for enterprise security teams — empty slot, mandatory deadlines, willing-to-pay buyers, multi-year shelf life. (See [Phase 5 #38](./05-top-100-book-ideas.md).)
  - *Cryptographic agility engineering* — empty slot.
  - *Hybrid TLS / PKI in transition* — empty slot.
  - *Lattice cryptography graduate textbook successor* — CUP lane.
  - *PQC for embedded / IoT / automotive* — under-served, highly defensible.

### 3.5 Quantum Networking and Quantum Internet
- **Maturity:** `EM` → `EA` regionally
- **HL:** 8-12 years
- **RF:** RM, GT
- **Publishing read:** Long-shelf monograph slot. Springer/CUP lane.

### 3.6 Quantum Machine Learning (QML)
- **Maturity:** `EA` and **deflating** (the 2020-2023 hype peaked; advantage claims being walked back)
- **HL:** 4-6 years
- **RF:** RM
- **Publishing read:** The honest survey monograph is more valuable than another optimistic textbook. Now Publishers F&T is a natural home.

### 3.7 Quantum Hardware
- **Maturity:** `GR` (superconducting, trapped ions); `EA` (photonic, neutral atoms, topological); `EM` (silicon-spin, nuclear-spin)
- **HL:** 6-10 years
- **RF:** GT, RM
- **Publishing read:** Modality-specific graduate textbooks (especially photonic and neutral-atom) are an underexploited series opportunity for Springer.

### 3.8 Quantum Programming Languages and Compilers
- **Maturity:** `EA` (Q#, Quipper, Catalyst, OpenQASM 3, QIR)
- **HL:** 4-7 years
- **RF:** SPB, GT
- **Publishing read:** "Compiling for fault-tolerant quantum computers" is the next decade's defining systems-engineering subfield. Generational textbook slot.

### 3.9 Quantum Simulation
- **Maturity:** `GR` (chemistry-as-driver)
- **HL:** 6-10 years
- **RF:** GT, RM
- **Publishing read:** Chemistry/materials × quantum is the most realistic-near-term application; cross-disciplinary textbooks have a defensible academic adoption path.

### 3.10 Quantum Cloud / "QCaaS"
- **Maturity:** `GR` (IBM Quantum, AWS Braket, Azure Quantum, IonQ, Quantinuum, QuEra)
- **HL:** 24-36 months for vendor specifics
- **RF:** CB
- **Publishing read:** Vendor-cookbook segment, not flagship. Packt-style.

### 3.11 Enterprise Quantum Adoption / Quantum Readiness
- **Maturity:** `EA`
- **HL:** 4-6 years
- **RF:** EB, SPB
- **Publishing read:** The *quantum-readiness CTO playbook* combining PQC migration, talent strategy, vendor selection, and use-case discovery is the *commercial-quantum* book that will sell broadly. This is a different book from the Qiskit tutorial — and a vastly more lucrative one.

---

## 4. Cross-Cuts and Convergence Topics

### 4.1 AI × Cybersecurity
- **Maturity:** `GR` (AI-for-defense); `GR` (AI-for-offense); `EA` (AI-SOC, autonomous response)
- **HL:** 24-36 months
- **RF:** SPB, CB, EB, CP
- **Publishing read:** The full eight-quadrant matrix (AI-for/against × red/blue × defender/attacker × strategic/operational) deserves *eight* books. Currently maybe *two* exist.

### 4.2 AI × Blockchain (decentralized AI; on-chain inference)
- **Maturity:** `EA` and speculative
- **RF:** EB, RM
- **Publishing read:** Hype-aware survey, not how-to. (See 2.12.)

### 4.3 Quantum × AI (quantum ML *and* AI-for-quantum-control)
- **Maturity:** `EA` (QML, deflating); `GR` (AI-for-quantum-control — actually working)
- **RF:** GT, RM
- **Publishing read:** Inverted from the popular framing. **AI-for-quantum-control** (RL for pulse shaping, ML for error decoding, ML for QEC) is the real and growing intersection. The book lane is currently *empty*.

### 4.4 AI × Climate / Sustainability
- **Maturity:** `GR`
- **RF:** GT, EB
- **Publishing read:** "AI for climate" textbook is overdue; will be adopted in environmental-science programs globally.

### 4.5 AI × Biology / Pharma
- **Maturity:** `GR` accelerating (post-AlphaFold-3, ESM-3, Boltz-class models)
- **RF:** GT, SPB
- **Publishing read:** The "ML-for-biology pipeline engineer" book is the breakout.

### 4.6 Edge × AI × Privacy (Federated Learning, Confidential Computing for ML)
- **Maturity:** `GR`
- **RF:** SPB, GT
- **Publishing read:** Drives by EU AI Act + healthcare privacy regimes; multilingual demand.

### 4.7 AI × Hardware (accelerator architecture, custom silicon, neuromorphic)
- **Maturity:** `GR` (transformer accelerators, NPUs); `EA` (neuromorphic — Loihi-class, IBM NorthPole-class)
- **RF:** GT, RM
- **Publishing read:** A *generational* AI-hardware textbook that supersedes Hennessy-Patterson chapters on AI accelerators is overdue. Pearson-AW lane.

### 4.8 Decentralized Systems beyond Blockchain
- **Maturity:** `MT` (CRDTs, conflict-free); `GR` (local-first software, sync engines)
- **RF:** GT, SPB
- **Publishing read:** Local-first software engineering is having a quiet renaissance and lacks an anchor textbook.

### 4.9 Synthetic Data / Data-Centric AI
- **Maturity:** `GR`
- **RF:** SPB, GT
- **Publishing read:** Evaluating, generating, and governing synthetic data is regulation-driven and currently under-booked.

### 4.10 AI-Native Software Engineering (engineering with AI in the loop)
- **Maturity:** `GR` accelerating fast
- **HL:** 24 months for tools; 4+ years for principles
- **RF:** SPB
- **Publishing read:** The successor to *The Pragmatic Programmer* for the agentic-IDE era is one of the largest commercial slots in the entire field. Pearson-AW or Pragmatic Bookshelf.

---

## 5. Topic-level Composite Opportunity Score (top 25)

Score axes recap: `0.25·MO + 0.20·RP + 0.15·AI + 0.10·RR + 0.20·LV + 0.10·SC` (all 1-10).

| Rank | Topic | MO | RP | AI | RR | LV | SC | **COS** |
|---|---|---|---|---|---|---|---|---|
| 1 | PQC migration & cryptographic agility | 10 | 9 | 8 | 8 | 9 | 9 | **8.95** |
| 2 | AI assurance / governance / audit | 10 | 9 | 9 | 7 | 9 | 9 | **8.95** |
| 3 | Agentic systems senior playbook | 10 | 9 | 8 | 8 | 7 | 9 | **8.55** |
| 4 | AI-native software engineering | 10 | 9 | 7 | 7 | 8 | 8 | **8.40** |
| 5 | Inference economics & serving | 9 | 9 | 7 | 8 | 8 | 8 | **8.30** |
| 6 | RWA tokenization reference | 9 | 9 | 7 | 7 | 9 | 8 | **8.35** |
| 7 | AI red teaming / agent security | 9 | 8 | 7 | 8 | 7 | 8 | **8.00** |
| 8 | Mechanistic interpretability GT | 7 | 7 | 10 | 10 | 9 | 7 | **8.00** |
| 9 | Quantum-readiness CTO playbook | 8 | 8 | 6 | 6 | 8 | 8 | **7.50** |
| 10 | EU AI Act in practice | 9 | 8 | 8 | 6 | 8 | 7 | **7.95** |
| 11 | EUDI wallet / VC engineering | 8 | 7 | 7 | 7 | 8 | 8 | **7.55** |
| 12 | AI-hardware textbook successor | 7 | 7 | 10 | 9 | 9 | 7 | **7.95** |
| 13 | VLA robotics graduate text | 7 | 7 | 10 | 10 | 9 | 7 | **8.00** |
| 14 | AgentOps / multi-agent SRE | 9 | 8 | 6 | 7 | 7 | 8 | **7.55** |
| 15 | Foundational AI textbook successor | 9 | 9 | 10 | 8 | 10 | 8 | **9.10** |
| 16 | Smart-contract audit engineering | 8 | 7 | 7 | 7 | 7 | 8 | **7.30** |
| 17 | Sovereign-AI architecture | 8 | 8 | 7 | 6 | 8 | 8 | **7.55** |
| 18 | Realistic quantum-advantage GT | 6 | 6 | 10 | 10 | 9 | 7 | **7.55** |
| 19 | Account-abstraction practitioner | 8 | 7 | 6 | 6 | 7 | 7 | **6.95** |
| 20 | AI-finance regulated playbook | 8 | 9 | 7 | 7 | 8 | 8 | **7.85** |
| 21 | AI-pharma pipeline engineering | 8 | 8 | 8 | 8 | 8 | 8 | **8.00** |
| 22 | Local-first software | 7 | 7 | 7 | 7 | 9 | 6 | **7.20** |
| 23 | Edge LLM (mobile/embedded) SPB | 9 | 8 | 7 | 7 | 7 | 8 | **7.80** |
| 24 | Digital-government reference (eEstonia) | 7 | 6 | 7 | 6 | 9 | 6 | **6.95** |
| 25 | AI for engineering with AI | 9 | 8 | 7 | 7 | 8 | 8 | **8.00** |

The *foundational AI textbook successor* tops every COS calculation but is also the highest-effort book to commission and ship. The *PQC migration* and *AI assurance* slots are the best risk-adjusted opportunities — large guaranteed buyer cohorts, clear regulatory deadlines, and shorter time-to-market.

---

[← Phase 2: Publisher Catalogs](./02-publisher-catalogs.md) · [Back to index](./README.md) · [Next: Phase 4 — Market Gap Analysis →](./04-market-gaps.md)
