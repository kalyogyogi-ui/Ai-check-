## Pre-Migration (Phase 0) — Discovery & Mandate

- [ ] Complete QEE assessment (Appendix B) with signed version ID
- [ ] Assign executive owner and migration program manager
- [ ] Inventory all signature schemes, curves, and hash functions in production
- [ ] Map dependency graph (oracles, bridges, multisigs, HSMs, L2s)
- [ ] Evaluate NIST PQC options against SCR and governance constraints
- [ ] Benchmark ML-DSA / SLH-DSA on target hardware (verify ms, bytes, gas)
- [ ] Legal/compliance review (jurisdictions: US, EU, UK, SG, etc.)
- [ ] Budget EMC (engineering, audits, incentives, comms, contingency)
- [ ] Publish draft migration principles (community / board)
- [ ] Align internal timeline to Master Timeline (Ch. 5): 2030 / 2035

---

## Infrastructure Deployment (Phase 1) — Dual-Stack Readiness

- [ ] Ship PQC libraries in testnet / staging
- [ ] Account abstraction or parallel verification paths (if applicable)
- [ ] HSM / KMS support for PQC keys
- [ ] Monitoring for algorithm version tags on-chain
- [ ] Shadow-fork or testnet migration drill #1
- [ ] Security audit of PQC integration (external firm)
- [ ] Update block explorer / indexer for new tx formats
- [ ] Wallet ecosystem outreach (SDK, hardware wallets)
- [ ] Document rollback criteria and safety switches

---

## Voluntary Migration (Phase 2) — Incentivized Adoption

- [ ] User-facing migration UI (rotate keys, new address types)
- [ ] Incentives for early migrators (fee rebates, reputation, airdrop guardrails)
- [ ] Validator / operator migration playbook
- [ ] Oracle and bridge operator coordination calls
- [ ] Governance vote: adopt PQC parameters and deprecation schedule
- [ ] Testnet migration drill #2 (governance + economic params)
- [ ] Public status dashboard (% migrated by value and by addresses)
- [ ] Incident response plan for migration bugs

---

## Mandatory Migration (Phase 3) — Cutover & Enforcement

- [ ] Hard fork or consensus rule enforcing PQC-only transactions (if required)
- [ ] Reject new ECDSA txs after cutoff (or rate-limit legacy)
- [ ] Freeze or sunset bridges still on legacy attestations
- [ ] Final security audit and bug bounty escalation
- [ ] Market communications: exchanges, custodians, regulators
- [ ] Post-migration drill: forged-key simulation on testnet
- [ ] Retrospective: EMC actual vs planned; update QRI
- [ ] Archive evidence pack for regulators (inventories, dates, votes)

---

## Ongoing (Phase 4) — Operate & Improve

- [ ] Quarterly QEE refresh
- [ ] Annual governance tabletop (Ch. 10)
- [ ] Track NIST/ETSI/BIS guidance updates
- [ ] Cryptographic agility test: swap algorithm in staging annually

**Program completion sign-off:** ___________________  Date: ___________

---
