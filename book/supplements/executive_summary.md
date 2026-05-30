# Executive Summary

*Two-page overview for boards, regulators, and fund risk committees. Full analysis in the body and appendices.*

## The problem

Token economies treat cryptography as infrastructure, not packaging. A cryptographically relevant quantum computer (CRQC) breaks ECDLP-class signatures that underpin ownership, staking slashing evidence, governance votes, oracle attestations, and bridge thresholds. Engineering migration to post-quantum algorithms (PQC) is necessary but **insufficient**: larger signatures and uncertain timelines change fees, participation, legitimacy, and market confidence.

## What is at stake

- **Value exposure:** Coins and positions in addresses with exposed public keys; bridge and oracle TVL.  
- **Functional exposure:** Consensus, DeFi, governance, and interoperability.  
- **Policy exposure:** NIST-style **2030 deprecation** and **2035 disallowance** timelines overlap expert CRQC estimate windows (**2030–2037**, scenario).

## Core frameworks (book)

| Framework | Use |
|-----------|-----|
| **Cryptoeconomic substrate** | Map primitives → economic properties |
| **SCR** | Signature cost ratio for capacity and fees |
| **QEE / QRI** | Exposure inventory and readiness index |
| **Migration coordination game** | Align users, validators, issuers, regulators |

## Recommended 12-month program

| Quarter | Deliverable |
|---------|-------------|
| Q1 | Complete Appendix B QEE; assign RACI (Appendix F); baseline SCR |
| Q2 | Algorithm shortlist vs NIST FIPS 203–205; testnet PQC fork |
| Q3 | Governance tabletop (Ch. 10); publish migration triggers |
| Q4 | Public dashboard: % value migrated; regulatory mapping (App. D) |

## Decision principles

1. **Do not wait for certainty** — policy clocks are already moving.  
2. **Design for confidence**, not only correct math — markets fail before keys are exploited.  
3. **Coordinate vertically** — L1, L2, bridges, oracles, issuers, custodians.  
4. **Label uncertainty** — separate (Data), (Estimate), and (Scenario) in all external materials.

## Verdict for leadership

Organizations that treat PQC as a patch will face governance and economic failure modes that patches cannot fix. Organizations that run QEE-driven programs with explicit EMC budgets (Appendix G) and RACI ownership (Appendix F) can preserve incentive compatibility and institutional trust through cryptographic regime change.

---
