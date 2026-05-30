
### Case 7: Solana — High-Frequency Signing and Validator Set Scale *(Estimate)*

**Context:** Solana optimizes for throughput using Ed25519 signatures across validators, RPC infrastructure, and user wallets. High message volume increases **operational exposure** (more signatures per day) even when per-signature cryptography is unchanged.

**Quantum-relevant mechanisms:**

1. *Ed25519 / Shor* — Same ECDLP-class vulnerability as ECDSA for ownership and vote keys.  
2. *Validator set size* — Fewer active validators than Ethereum may lower the count of keys an adversary must target for consensus influence—but concentrates stake.  
3. *Dependent stacks* — SPL tokens, Marinade/Jito, Pyth, Wormhole endpoints inherit host-chain migration timing.

**Scenario B (accelerated CRQC):** Fee and compute pressure from PQC-sized signatures conflicts with Solana’s throughput brand; DeFi TVL *(Estimate)* contracts 35–50% in 60 days if migration path unclear.

| Dimension | Rating | Note |
|-----------|--------|------|
| Cryptographic | Inherited (Ed25519) | Must coordinate with ecosystem |
| Economic | Moderate-Low | Throughput identity at risk |
| Governance | Low–Moderate | Faster upgrades possible but less formal than Ethereum |
| Coordination | Low | Bridge + oracle dependencies |

**Actions:** Benchmark ML-DSA verify latency on Solana hardware profile; pre-publish guardian/oracle upgrade order with Wormhole partners.

---

### Case 8: Cosmos / IBC — Interchain Security and Relayer Keys *(Illustrative)*

**Context:** The Cosmos Hub and IBC-connected zones rely on Tendermint/CometBFT consensus, IBC light clients, and relayer-operated packets. Security is **multi-chain**: a quantum break on Zone A can poison trust assumptions on Zone B.

**Quantum pathways:**

1. *Validator keys* on each zone — standard ECDSA/secp256k1 exposure.  
2. *IBC client updates* — forged headers if signing keys compromised.  
3. *Relayer keys* — often overlooked; forged acknowledgements stall or drain cross-zone liquidity routes.

**Stress linkage:** Staggered zone migration → **wrapped ATOM / OSMO** on non-migrated zones trade at a quantum-discount until IBC proofs use PQC.

| Dimension | Rating |
|-----------|--------|
| Cryptographic | Low (multi-key surface) |
| Economic | Low under IBC halt |
| Governance | Moderate (zone sovereignty slows alignment) |
| Coordination | Very Low |

**Actions:** Inventory all IBC paths; require PQC client upgrade before accepting new connections; shared testnet for cross-zone migration.

---

### Case 9: USDC — Multi-Chain Issuer Mediation *(Illustrative)*

**Context:** Circle issues USDC on Ethereum, Solana, Base, Arbitrum, and other hosts *(Data, 2025 — verify deployments)*. Users experience “one USDC” but security is **bounded by each host chain’s** transaction and state proofs.

**Quantum pathways:**

1. *Issuer keys* — Contract upgrade and freeze functions; centralized rotation possible **faster** than UTXO migration.  
2. *Host-chain exposure* — PQC on Ethereum does not secure USDC on a non-migrated chain.  
3. *Attestation / proof-of-reserve* — Off-chain reports still need PQC for long-term archival signatures.

**Scenario:** Ethereum migrated, Solana lagging 18 months → **basis between “same” USDC** on different chains; arbitrageurs price quantum-basis risk.

| Dimension | Rating |
|-----------|--------|
| Cryptographic | Moderate (issuer agility) / Low (weakest host) |
| Economic | Moderate |
| Governance | High at issuer; Low on-chain per chain |
| Coordination | Low across 15+ deployments |

**Actions:** Publish per-chain quantum status page; cap minting on non-compliant hosts; align with GENIUS/MiCA operational resilience expectations.

---
