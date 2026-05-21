# Book Proposal: *Post-Quantum Blockchain Engineering*
### Bitcoin, Ethereum, Cosmos and the Migration Paths That Will Define Web3's Next Decade

> Status: Pre-acquisition proposal · Priority **P0** (ship within 6 months of contract)
> Compiled: May 2026 · All technical claims sourced; see Appendix.

---

## 1. Working title

**Post-Quantum Blockchain Engineering: A Practitioner's Guide to Migrating Bitcoin, Ethereum, and Cosmos**

Alternative subtitle: *NIST FIPS 203/204/205 Meets Web3 — The Engineering Playbook*

## 2. One-line hook

> "By the time a cryptographically relevant quantum computer exists, **6.9 million bitcoins worth roughly half a trillion dollars** will be sitting in addresses that anyone can drain — and Bitcoin's BIP-361 will give holders a hard deadline to move them. This is the engineer's manual for that migration, across the three chains that define modern Web3."

## 3. Detailed description (~250 words)

The post-quantum migration of public blockchains has moved from speculative whitepapers to **active, scheduled engineering work**. In August 2024, NIST FIPS 203 (ML-KEM), 204 (ML-DSA / CRYSTALS-Dilithium), and 205 (SLH-DSA / SPHINCS+) became effective US federal standards. In late 2025 a coalition led by Jameson Lopp filed **BIP-361**, "Post Quantum Migration and Legacy Signature Sunset," which proposes a three-phase plan that would freeze any un-migrated UTXO five years after activation. On **19 May 2026** — two days before this proposal — Vitalik Buterin announced the **Q-STARK hard fork**, targeting late Q3 2026 for Ethereum's migration via STARK-based account abstraction (EIP-8141) and the Hegota upgrade. Cosmos, Tezos (TzEL), Zcash, and Ripple have all published concrete roadmaps. Validator operators, custody platforms, exchanges, and wallet vendors must now ship real code against real deadlines.

Yet there is **no engineering book** that walks a working developer through the migration end-to-end. The two existing titles in this space — *Quantum Blockchain: An Emerging Cryptographic Paradigm* (Wiley, 2022) and *Quantum Protocols in Blockchain Security* (Springer, 2024) — are research-edited volumes targeting academics. Vendor blogs, EIP/BIP texts, and ethresear.ch threads cover fragments. Nothing covers the migration as a coherent engineering project across the three chains that hold most Web3 TVL.

This book is that manual. It is opinionated, code-first, and shipped with a versioned reference repository.

## 4. Target reader persona

**Primary:** protocol engineers, validator-operations engineers, custody-platform engineers, exchange security engineers, wallet developers, and on-chain auditors who must implement or evaluate PQ migration code.

**Secondary:** security architects at regulated enterprises with crypto-asset exposure, central-bank digital-currency teams, smart-contract auditors needing to evaluate PQ-related changes, and graduate students in applied cryptography.

**Not the audience:** non-technical executives (covered by *The Quantum Almanac* annual series), investors (covered by other planned titles), or readers needing a math-first introduction to lattice cryptography (covered by Peikert and by Paar/Pelzl's *Understanding Cryptography 2e*).

## 5. Prerequisites & reading level

- Working knowledge of public-key cryptography (ECDSA, EdDSA, hash functions, Merkle trees).
- One of: Solidity at the EVM-internals level, Bitcoin Script / Taproot, or Cosmos SDK / CometBFT.
- Comfortable reading Rust, Go, and Solidity. Most code samples are in Rust (Bitcoin reference, ML-DSA libraries, Cosmos modules), Go (`liboqs-go`, Cosmos SDK), and Solidity (verifier contracts).
- No quantum-physics background required. The book gives a self-contained 30-page "what you need to know about why this matters" cryptographic primer.

**Level:** Advanced-intermediate to advanced. Roughly equivalent to *Programming Bitcoin* (Song) and *Mastering Ethereum 2e* (Antonopoulos et al., 2025) in difficulty, but specialised.

## 6. Proposed table of contents (chapter-level)

> ~360 pages, 14 chapters + appendices.

### Part I — Foundations

1. **The Threat Model** — Why blockchains are uniquely exposed; the harvest-now-decrypt-later (HNDL) problem applied to permanent on-chain data; the Mosca inequality applied to multi-year migration windows; what Google's Willow chip and the December 2024 Nature surface-code paper actually changed about the timeline.
2. **The Standards** — NIST FIPS 203 (ML-KEM), FIPS 204 (ML-DSA), FIPS 205 (SLH-DSA), the FIPS 206 (Falcon/FN-DSA) draft, HQC selected March 2025; NIST SP 800-208 (XMSS, LMS, HSS, XMSS^MT — stateful hash-based); IETF `draft-ietf-cose-dilithium-11`; the Open Quantum Safe (OQS) ecosystem and `liboqs`.
3. **A Crypto Primer for Migration Engineers** — module-LWE / module-SIS, lattice problems, hash-based signatures, what "stateful" means in production, why signature size matters more on-chain than off-chain, why FALCON requires constant-time floating-point and why that hurts hardware portability.

### Part II — Bitcoin

4. **The Exposure Map** — How many UTXOs are quantum-vulnerable today; reused-key P2PK/P2PKH vs P2WPKH vs P2TR; the Satoshi-stash question; Citi's outsized-Bitcoin-vulnerability thesis.
5. **BIP-361 in Depth** — Lopp's three-phase soft-fork: Phase A (block new sends to legacy address types after ~3 years), Phase B (invalidate ECDSA and Schnorr signatures after ~5 years), Phase C (limited ZK-proof recovery tied to seed phrases). Off-chain debates: confiscation vs theft, the "frozen vs stolen" framing, opt-out controversy. Walks the proposed consensus changes, opcodes, and validator behaviour.
6. **Building a PQ Output Type** — A concrete walkthrough of a PQ output type built on SLH-DSA-128s (smaller signatures, stateless) and a comparison with ML-DSA-44; output-script construction; transaction-weight implications under current SegWit/Taproot economics; mempool policy; node-software compatibility.
7. **Migration Operations for Custody and Exchange Operators** — How a regulated custodian (Coinbase, Anchorage, BitGo, Fireblocks-class operators) plans the move: HSM/MPC vendor PQ readiness, signing-key rotation, KYC-reissue overhead, multi-sig re-derivation, customer notification, the inheritance / lost-wallet problem, the regulatory reporting angle.

### Part III — Ethereum

8. **The Q-STARK Hard Fork** — Vitalik's 19 May 2026 announcement; the late-Q3-2026 target; why Ethereum's path looks different from Bitcoin's (account abstraction at protocol level + STARK-based signatures inherit PQ security). Roadmap context (Strawmap to 2030).
9. **EIP-8141 and the Hegota Upgrade** — Native account abstraction at the protocol layer; programmable verification; how AA decouples signature scheme from address; what this means for ERC-4337 (which becomes a special case) and EIP-7702 (already live since Pectra, May 2025).
10. **Implementing PQ Signature Verification in Solidity** — Verifier contracts for ML-DSA-44 and SLH-DSA; gas-cost analysis at current and projected blob-fee levels; precompile candidates; STARK-recursive verification on-chain; trade-offs between native precompile, verifier-contract, and validity-proof approaches.
11. **Wallets and Smart Accounts in the Q-STARK Era** — Migration paths for Safe, Kernel/ZeroDev, Biconomy, and Pimlico stacks; session keys with PQ rotation policies; social recovery with PQ-friendly thresholds; the `eth_sendTransaction` flow after Q-STARK; cross-chain wallet portability.

### Part IV — Cosmos and the Long Tail

12. **Cosmos SDK Migration** — ADR-036 (arbitrary signatures) as the migration on-ramp; CometBFT block-signing key changes; IBC light-client implications; the IETF COSE Dilithium draft and its IBC mapping; concrete code in `cosmos-sdk` and a sample chain that uses ML-DSA-44 for validator and account signatures; benchmarks for block-time and storage growth.
13. **Comparative Chapter: Other Chains in Flight** — **Tezos TzEL** (post-quantum privacy on testnet), **Zcash** quantum-recoverable wallets, **Ripple/XRPL**'s four-phase plan to 2028, **Solana** PQ posture, **Polkadot** state of work, **Cardano** Hoskinson-led ZK and PQ activities, **NEAR**, **Stellar**. A scoring matrix on readiness.

### Part V — Cross-Cutting

14. **From Migration to Maintenance: Crypto-Agility Patterns for Web3** — Designing protocol upgrade paths so the *next* migration is configuration, not consensus change; CBOM (Cryptographic Bill of Materials) for blockchain stacks; observability, telemetry, and incident response; what to monitor; how to coordinate with HSM vendors; an inheritance-and-recovery design for un-migrated coin-holders.

### Appendices
- A. Reference benchmarks across ML-DSA-44/65/87, SLH-DSA-128s/192s/256s, FN-DSA, XMSS-SHA256-W16-H10, on commodity hardware.
- B. Signature and key-size tables (ECDSA / Schnorr vs ML-DSA / SLH-DSA / FN-DSA / XMSS).
- C. A glossary mapping NIST names to academic names (CRYSTALS-Dilithium = ML-DSA, SPHINCS+ = SLH-DSA, Falcon = FN-DSA, CRYSTALS-KYBER = ML-KEM).
- D. A migration-readiness checklist by stakeholder (validator operator, custodian, exchange, wallet vendor, dApp, smart-contract author).
- E. Source code layout of the companion repo.

## 7. Differentiator vs existing books

| Existing title | What it is | Why this book is different |
|---|---|---|
| *Quantum Blockchain: An Emerging Cryptographic Paradigm* (Wiley, 2022, ed. Dhanaraj, Rajasekar, Islam, Balusamy, Hsu) | Edited research volume of papers from academics in India, Taiwan, Bangladesh | Pre-FIPS 203/204/205, pre-BIP-361, pre-Q-STARK, pre-Pectra. Research papers, not engineering. |
| *Quantum Protocols in Blockchain Security* (Springer, Blockchain Technologies series, 2024) | Edited research volume | Same as above; not engineering, no working code, no chain-by-chain migration playbook. |
| *Real-World Cryptography* (Wong, Manning, 2021) | Practitioner cryptography textbook | One chapter on PQ, no blockchain specifics. |
| *Serious Cryptography 2e* (Aumasson, No Starch, 2024) | Practitioner cryptography reference | Updated PQC chapter, but not blockchain-specific and not migration-driven. |
| *The Quantum Almanac 2025-26* and *2026-27* | Annual board-level guides | Strategic governance, not engineering. Different audience. |
| *Mastering Bitcoin 3e* (Antonopoulos & Harding, 2023) | Bitcoin protocol bible | Predates BIP-361. Mentions quantum threat in passing. |
| *Mastering Ethereum 2e* (Antonopoulos, Wood, Parisi, Mazza, Pozzolini, 2025) | Ethereum protocol bible | Published before Q-STARK announcement; minimal PQ coverage. |
| BIP-361 / EIP-8141 / ADR-036 / ethresear.ch threads | Specifications and discussions | Source material for this book; not a synthesised practitioner guide. |

**This book is the only engineering-level, multi-chain, code-first treatment.**

## 8. Estimated market size & demand signals

> Demand is asserted with sources, not adjectives.

| Signal | Evidence |
|---|---|
| Bitcoin holders directly affected by BIP-361 timeline | ~6.9M BTC reported as quantum-vulnerable (ainvest, May 2026, citing recent Google qubit-requirement reduction). At BTC ~$80k that is ~$550B at risk. |
| Ethereum migration on a real schedule | Q-STARK hard fork announced 19 May 2026, targeting late Q3 2026; Strawmap roadmap to 2030. |
| Standards finalised | NIST FIPS 203/204/205 effective 14 August 2024; HQC selected as 5th algorithm 11 March 2025; FIPS 206 (FN-DSA) in development. |
| Active vendor/community work | Open Quantum Safe (`liboqs`); Cloudflare CIRCL; the IETF COSE Dilithium draft now at -11; multiple PQ-blockchain benchmarking arXiv papers (2510.09271 et al.). |
| Other chains shipping in parallel | Tezos TzEL on testnet, Zcash quantum-recoverable wallets, Ripple/XRPL four-phase plan to 2028. |
| Boardroom pressure | Citi report (May 2026) flags Bitcoin's outsized vulnerability due to slow upgrades; CISO concern at every regulated crypto-asset operator. |

**Buyer segments (where the book sells in volume):**

- Custody platforms (Coinbase Custody, Anchorage, BitGo, Fireblocks, Copper, Hex Trust, Bitstamp)
- Exchanges with cold-storage operations
- Validator-operations companies (Figment, Blockdaemon, Kiln, Allnodes, Coinbase Cloud, Chorus One, P2P.org)
- HSM and MPC vendors (Thales, Entrust, Fortanix, Sepior/Coinbase, Fireblocks)
- Layer-1 protocol teams (Cosmos chains, app-chains, OP Stack and Polygon CDK forks)
- Government and central-bank CBDC engineering teams
- Smart-contract audit firms (Trail of Bits, OpenZeppelin, Spearbit, Cyfrin, Halborn, Code4rena, Sherlock)
- Academic libraries and graduate programmes in applied crypto

**Volume estimate:** **[ESTIMATE]** Conservatively a 5,000–8,000-unit first-year run is achievable on the technical edition alone if marketed alongside the Bitcoin community fork debate, with corporate/training procurement often 3–5x the per-unit individual price. A small-format executive briefing companion (<=120pp, ~$30) is a natural co-product.

## 9. Suggested format

- **Primary:** trade technical handbook, ~360 pp print, 7"x9" (O'Reilly format) or comparable Manning trim.
- **Companion:** <=120pp executive briefing — *"What Boards and CTOs Need to Know About BIP-361 and Q-STARK"* — derived from Chapters 1, 4, 5, 8, and 14.
- **Digital:** EPUB, KF8, PDF; one-time purchase + opt-in updates as the standards and proposals move (FIPS 206, HQC, post-Q-STARK Ethereum upgrade specifics).

## 10. Companion assets

A versioned mono-repo (`pq-blockchain-engineering`) that is a first-class product:

- A **Bitcoin signet** branch running a node patched to recognise a SLH-DSA / ML-DSA output type, with reproducible Docker and Nix flakes.
- A **Cosmos SDK fork** that swaps validator and account signatures for ML-DSA-44, with `simd` benchmarks.
- An **Ethereum verifier-contract suite** (Foundry tests) for ML-DSA and SLH-DSA verification, with gas tables and integration with a sample ERC-4337 / EIP-7702 / EIP-8141-class smart account.
- **Reference benchmarks** scripts using `liboqs`, Cloudflare CIRCL, and `itzmeanjan/ml-dsa`, runnable on commodity hardware.
- **Migration-runbook templates** for custodians, exchanges, validator operators, and wallet vendors (markdown + ODT/DOCX, Apache-2.0 licensed for adaptation).
- **CBOM templates** in CycloneDX format pre-populated for typical Bitcoin/Ethereum/Cosmos validator stacks.

A modest amount of CI compute is required to keep benchmarks fresh as `liboqs` and the standards move; we recommend a paid GitHub Actions tier in the publisher's name with renewals tied to errata releases.

## 11. Suggested author archetype

A two-author hybrid is strongest:

- **Lead author (practitioner):** A protocol or custody engineer with shipped PQ work. Examples of the right archetype (not necessarily these individuals): a Blockstream / Spiral / Lightning Labs core developer who has reviewed BIP-361; a researcher from EF Geth / Erigon / Reth team active on the Q-STARK proposal; a Cosmos-SDK maintainer (Informal Systems, Binary Builders, Confio).
- **Co-author (cryptographer):** An applied cryptographer with PQ migration credentials. Examples of the right archetype: a former NIST PQC competition contributor, a member of the Open Quantum Safe project, or a senior cryptographer at PQShield / Sandbox AQ / Quantinuum / IBM Research.

Failing a hybrid pair, a practitioner with strong cryptographic literacy and a technical reviewer panel of three cryptographers (academic + industry) is the next-best option.

## 12. Priority tier

**P0** — ship within 6 months of contract.

The window is tight: by the time the book is in print, Q-STARK will likely have shipped on testnet (late 2026) or mainnet (Q3 2026 target, possibly slipping to 2027), BIP-361 will be in active community-vote phase, and Cosmos chains will be making validator-set decisions. **A 12-month book is half-stale on day one. A 6-month book lands in the migration window.**

## 13. Risk factors and mitigation

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Q-STARK hard-fork specifics change between writing and ship | High | High | Structure Chapters 8–11 around principles + a code-first reference branch tracked in the companion repo. Commit to a minor-version digital update tied to the actual fork specifics. |
| BIP-361 fails to activate or is replaced | Medium | Medium | Frame Part II around the *engineering work that any PQ Bitcoin migration requires*, not the BIP text. Even if BIP-361 is replaced, the SLH-DSA / ML-DSA output construction, custody-migration runbook, and exposure-map analysis remain valid. |
| Standards churn (FIPS 206 final, HQC final) | High | Low–Medium | Track standards in the companion repo. Print edition cites parameter sets as of date; digital edition updates. |
| Author scarcity | Medium | High | Co-author pairing strategy above; publisher-organised technical reviewer panel; academic acknowledgements section incentivises early peer review from key OQS / Cosmos / Bitcoin developers. |
| Competing book from a major publisher mid-cycle | Low–Medium | Medium | The 6-month P0 window is the moat. No other major publisher has a book in flight in this exact slot as of this proposal's compile date. |
| ZK-proof recovery in BIP-361 Phase C is socially/technically controversial | Medium | Low | Treat as a single chapter sub-section; present multiple positions; defer prescription to the practitioner reviewer panel. |
| Quantum threat timeline shifts (CRQC further out than Mosca-inequality assumes) | Medium | Low | The book is about *migration engineering* under finalised standards and proposed forks. Even a slower CRQC timeline does not invalidate the work; it lengthens the window. |
| Author/reviewer conflict of interest with named protocols | Medium | Medium | Disclose all affiliations. Use a balanced reviewer panel (one Bitcoiner, one Ethereum dev, one Cosmos engineer, one academic cryptographer, one custodian-side reviewer). |

## 14. Suggested marketing levers

- **Launch hook tied to BIP-361 and Q-STARK timing.** If BIP-361 reaches activation discussion or Q-STARK ships in 2026, the book is the practitioner reference.
- **Bundle with the executive briefing** and sell into corporate procurement at financial institutions, exchanges, and CBDC programmes.
- **Conference circuit:** present at IEEE Quantum Week (QCE26), Bitcoin++, EthCC, Cosmoverse, RWA Summit, Money 20/20, and the OWASP/RSA tracks on PQ migration.
- **Co-marketing with Open Quantum Safe** and a willing HSM/MPC vendor for a "post-quantum-ready custody" reference architecture.
- **Localisations:** Mandarin (PRC and Taiwan markets, large Bitcoin and Cosmos communities), Japanese (regulator-led PQ migration interest), Spanish/Portuguese (LATAM exchange and stablecoin operators), Hindi (India ecosystem under the National Quantum Mission).

---

## Appendix A — Sources for every non-trivial claim above

### Bitcoin / BIP-361
- [bips.dev/361](https://bips.dev/361/) — BIP-361 "Post Quantum Migration and Legacy Signature Sunset," authored by Jameson Lopp + co-authors. Three-phase plan with pre-announced sunset of legacy ECDSA/Schnorr signatures.
- [Cointelegraph, July 2025](https://cointelegraph.com/news/bitcoin-quantum-computing-threat-bip-post-quantum-migration) — initial coverage of BIP proposing legacy-signature retirement.
- [Yahoo Finance / Decrypt syndication](https://finance.yahoo.com/markets/crypto/articles/bitcoin-developers-might-permanently-freeze-101709642.html) — three-phase mechanism: Phase A blocks new sends to legacy P2PK/P2PKH for ~3 years; Phase B invalidates ECDSA/Schnorr after ~5 years; Phase C offers ZK-proof recovery tied to seed phrases.
- [Binance Square](https://www.binance.com/en/square/post/312754954390961) — same three-phase summary with timing.
- [MEXC News, May 2026](https://www.mexc.com/news/1031525) — "Bitcoin's quantum migration plan forces the network to choose between frozen and stolen coins."
- [postquantum.com migration roadmap](https://postquantum.com/quantum-threat-crypto/fixing-bitcoin-pqc-migration/) — technical roadmap covering Taproot key/script paths.
- [ainvest, May 2026](https://www.ainvest.com/news/quantum-threat-analysis-6-9m-btc-exposed-google-cuts-qubit-requirements-20-2605/) — 6.9M BTC reported as quantum-vulnerable; Google qubit-requirement reduction cited.
- [bitcoinworld / Citi report](https://bitcoinworld.co.in/citi-bitcoin-quantum-computing-vulnerability/) — Citi flagging Bitcoin's outsized vulnerability due to slow upgrades.

### Ethereum / Q-STARK / EIP-8141
- [SignalPlus, 2026-05-19](https://t.signalplus.com/crypto-news/detail/ethereum-q-stark-quantum-resistant-hard-fork) — Vitalik Buterin announces Q-STARK hard fork, targeting late Q3 2026.
- [BitcoinEthereumNews](https://bitcoinethereumnews.com/tech/vitalik-buterin-unveils-q-stark-hard-fork/) — same announcement.
- [crypto.news](https://crypto.news/vitalik-buterin-to-make-ethereum-quantum-resistant/) — coverage of EIP-8141 enabling EOAs to adopt PQ signature schemes.
- [1950.ai](https://www.1950.ai/post/vitalik-buterin-s-quantum-resistant-ethereum-how-eip-8141-and-hegota-upgrade-future-proof-the-block) — EIP-8141 + Hegota upgrade analysis.
- [panewslab](https://www.panewslab.com/en/articles/019d4e61-09dd-71c7-9832-f1dfb2d0b2c6) — EIP-8141 native account abstraction.
- [ethresear.ch, Dec 2024](https://ethresear.ch/t/so-you-wanna-post-quantum-ethereum-transaction-signature/21291) — early forum thread on PQ Ethereum signatures, in reaction to Google Willow.
- [coindesk, May 2026](https://www.coindesk.com/tech/2026/05/20/vitalik-buterin-outlines-ethereum-s-privacy-measures-here-is-what-it-means-for-the-network-and-eth) — Vitalik's three near-term Ethereum upgrades for native privacy.
- [KuCoin blog](http://www.kucoin.com/blog/Ethereum-3) — "Ethereum 3.0: Post-Quantum Cryptography and 2026 Roadmap."

### Cosmos / Standards / Libraries
- [cosmos-sdk ADR-036](https://github.com/cosmos/cosmos-sdk/blob/main/docs/architecture/adr-036-arbitrary-signature.md) — arbitrary signatures, the migration on-ramp.
- [datatracker.ietf.org draft-ietf-cose-dilithium-11](https://datatracker.ietf.org/doc/draft-ietf-cose-dilithium/) — IETF COSE Dilithium draft.
- [openquantumsafe.org / liboqs](https://openquantumsafe.org/liboqs/algorithms/sig/ml-dsa.html) — ML-DSA reference implementation.
- [arxiv 2510.09271](https://arxiv.org/html/2510.09271v1) — *Assessing the Impact of Post-Quantum Digital Signature Algorithms on Blockchains* — finds PQC algorithms have minor overhead at security level 1 and outperform ECDSA at higher security levels in some scenarios.
- [arxiv 2601.17785](https://arxiv.org/html/2601.17785) — *Performance Analysis of Quantum-Secure Digital Signature Algorithms in Blockchain.*
- [csrc.nist.gov FIPS 204 final](https://csrc.nist.gov/pubs/fips/204/final) — Module-Lattice-Based Digital Signature Standard.
- [csrc.nist.gov SP 800-208](https://csrc.nist.gov/pubs/sp/800/208/final) — XMSS, LMS, HSS, XMSS^MT recommendation.
- [NIST CSRC PQC project page](https://csrc.nist.gov/projects/post-quantum-cryptography/) — FIPS 203, 204, 205 effective 14 August 2024; HQC selected 11 March 2025; FIPS 206 in development.

### Other chains
- [Bitget / Yahoo: Tezos TzEL](https://tech.yahoo.com/cybersecurity/articles/tezos-tests-post-quantum-privacy-130103366.html) — Tezos launches TzEL, PQ privacy on testnet.
- [cryptobriefing: Zcash](https://cryptobriefing.com/zcash-quantum-recoverable-wallets-launch/) — Zcash plotting quantum-recoverable wallets.
- [crypto.news](https://crypto.news/is-bitcoin-quantum-safe/) — Ripple's four-phase plan to make XRPL quantum-proof by 2028; Ethereum Strawmap to 2030.

### Related books referenced in section 7
- [*Quantum Blockchain: An Emerging Cryptographic Paradigm* — Wiley](https://www.amazon.com/Quantum-Blockchain-Emerging-Cryptographic-Paradigm/dp/1119836220) (Dhanaraj, Rajasekar, Islam, Balusamy, Hsu, 2022, ISBN 1119836220).
- [*Quantum Protocols in Blockchain Security* — Springer](https://link.springer.com/book/10.1007/978-981-96-9148-7) (2024).
- [*Mastering Bitcoin 3e* — O'Reilly](https://www.oreilly.com/library/view/mastering-bitcoin-3rd/9781098150082/) (Antonopoulos & Harding, 2023).
- [*Mastering Ethereum 2e* — GitHub source repo](https://github.com/ethereumbook/ethereumbook) (Antonopoulos, Wood, Parisi, Mazza, Pozzolini, 2025, ISBN 1098168429).
- [*The Quantum Almanac 2026-2027* — press release](https://www.morningstar.com/news/accesswire/1146102msn/the-quantum-almanac-2026-2027-published-as-strategic-guide-to-the-post-quantum-security-transition).

---

## Appendix B — One-page elevator pitch (for acquisition meetings)

In **August 2024** the post-quantum cryptography era began: NIST published FIPS 203, 204, and 205 as effective US federal standards. In **May 2025** Ethereum activated EIP-7702, putting smart-account capability on every EOA. In **late 2025** Bitcoin saw the filing of **BIP-361**, a soft-fork proposal that would freeze any un-migrated UTXO five years after activation. On **19 May 2026** Vitalik Buterin announced the **Q-STARK hard fork** for Ethereum, targeting late Q3 2026. NIST selected HQC as the fifth PQC algorithm in March 2025 and is finalising FIPS 206 (Falcon/FN-DSA).

By the end of 2027, every regulated custody platform, exchange, validator operator, wallet vendor, and major Layer-1 will have made consequential decisions about their post-quantum migration. The two existing cross-domain books are research-edited Springer/Wiley volumes from before the standards even existed. There is no engineering practitioner manual.

This book is that manual. It is shipped with a versioned reference repository covering Bitcoin, Ethereum, and Cosmos. It is written by a protocol-engineer-and-cryptographer pair with a multi-disciplinary reviewer panel. It is **P0**: 6 months from contract to print, with a digital companion that updates as standards and forks ship.

The audience numbers in the tens of thousands of practising engineers worldwide and the hundreds at every regulated operator. The accompanying executive briefing addresses procurement budget. The book has a clear shelf life of 5–6 years (until the migration is mostly complete) and a clear successor in *crypto-agility* and *post-quantum maintenance* second editions.

---

*End of proposal.*
