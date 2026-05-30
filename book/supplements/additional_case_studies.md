
### Case 4: Lido — Concentration and Liquid-Staking Risk *(Estimate)*

**Context:** Liquid staking concentrates delegated stake behind a small set of operators and governance interfaces. As of mid-2024, Lido held a large fraction of staked ETH *(Data, 2024 — verify before print)*.

**Quantum-relevant mechanisms:**

1. *Operator key exposure* — Compromised operator or withdrawal credentials threaten pooled stake, not only solo validators.  
2. *Governance choke points* — Token-weighted votes on upgrades and fee switches depend on ECDSA/EdDSA today.  
3. *Secondary market leverage* — stETH used as DeFi collateral propagates confidence shocks faster than native stake exits.

**Scenario B sketch:** SCR-driven fee stress + 30% market drawdown → exit queue lengthens → stETH discount widens → DeFi liquidations on stETH collateral → **governance emergency** to pause deposits or adjust fees.

**Resilience assessment:**

| Dimension | Rating | Note |
|-----------|--------|------|
| Cryptographic | Inherited from Ethereum | Cannot self-migrate first |
| Economic | Moderate-Low | Concentration amplifies tail risk |
| Governance | Moderate | High stake weight, low participation risk |
| Coordination | Low | Depends on Ethereum + node operator set |

**Action:** Model stETH discount vs exit-queue length under PQC fee shock; pre-authorize communication templates for discount/depeg events.

---

### Case 5: Wormhole-Style Bridge — Multisig and Guardian Set *(Illustrative)*

**Context:** Cross-chain bridges secure billions via validator/guardian attestations—often threshold signatures on ECDSA or EdDSA.

**Attack / stress logic:**

1. Forged attestations if threshold keys are quantum-compromised → **instant TVL loss**.  
2. *Pre-attack* phase: liquidity flees when guardian set is perceived vulnerable—even without exploit.  
3. Migration requires **coordinated key rotation** across chains with incompatible upgrade cadences.

**Scenario D (stealth CRQC):** Slow attribution of losses → delayed pause → maximum TVL at risk when revelation hits.

| Dimension | Rating |
|-----------|--------|
| Cryptographic | Low (threshold ECDSA) |
| Economic | Very Low under confidence shock |
| Governance | Low (multi-jurisdiction operators) |
| Coordination | Very Low |

**Action:** Pre-negotiate guardian rotation playbook; cap per-epoch transfer limits; insured reserve or circuit breaker tied to attestation algorithm version.

---

### Case 6: MakerDAO / DAI — Oracle and Governance Coupling *(Illustrative)*

**Context:** Stablecoin systems couple **price oracles**, **governance parameters** (collateral factors, rates), and **market confidence**.

**Quantum pathways:**

1. Oracle signer compromise → wrongful liquidations or under-collateralization.  
2. Governance key compromise → parameter changes draining reserves.  
3. HNDL on encrypted governance comms (off-chain) is secondary to **on-chain vote keys**.

**Stress linkage:** Ethereum SCR ↑ → governance participation ↓ → slower parameter response during oracle anomaly.

| Dimension | Rating |
|-----------|--------|
| Cryptographic | Inherited + oracle layer |
| Economic | Low during oracle/governance stress |
| Governance | Moderate if emergency spells exist |
| Coordination | Moderate within Ethereum ecosystem |

**Action:** Maintain oracle diversity; define PQC-era emergency spell triggers; stress-test liquidation engines with ±30% collateral shock under delayed governance.

---
