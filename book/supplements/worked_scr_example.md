
## Worked Example: Signature Cost Ratio (SCR) for a Simple Transfer

*This section demonstrates the SCR framework step by step. Values are illustrative; substitute your chain's parameters before making decisions.*

**Definitions**

- \(S_{\text{legacy}}\) = bytes of signature + public key material per transaction (ECDSA secp256k1: ~64 + 33 ≈ 97 bytes signature/key payload; round to **100 B** for planning).
- \(S_{\text{pqc}}\) = ML-DSA-44 signature + public key (order of magnitude **~2,500–3,000 B**; use **2,420 B** signature + key overhead as in Chapter 8).
- \(\text{SCR} = S_{\text{pqc}} / S_{\text{legacy}}\)

**Step 1 — Compute SCR**

\[
\text{SCR} \approx 2420 / 100 = 24.2 \quad \text{(conservative planning: use 25× or 37× if including additional calldata/witness overhead)}
\]

The book often uses **37×** when full transaction weight (witness, verification gas, aggregation loss) is included—not signature bytes alone.

**Step 2 — Block capacity impact (Bitcoin-style weight limit)**

Assume block weight budget \(W = 4{,}000{,}000\) weight units and average legacy tx weight \(w_{\ell} = 400\) WU/tx.

- Legacy txs per block: \(N_{\ell} = W / w_{\ell} = 10{,}000\) *(theoretical upper bound; real average far lower)*.
- Post-PQC tx weight \(w_{p} \approx w_{\ell} \times \text{SCR} = 400 \times 37 = 14{,}800\) WU/tx.
- Post-PQC txs per block: \(N_{p} = W / w_{p} \approx 270\) txs.

**Throughput ratio:** \(N_{p} / N_{\ell} \approx 2.7\%\) — a **~37× reduction** in simple-transfer capacity unless block limits or aggregation change.

**Step 3 — Fee pressure (illustrative)**

If daily demand is 300,000 simple transfers and capacity drops by 37×, either:

1. **Fees rise** until demand matches supply (users pay more per inclusion), or  
2. **Demand migrates** to L2 / batching / alternative chains.

If median legacy fee was **$2** and supply shrinks 10× (partial mitigation via batching), a first-order stress fee might reach **$20+** for the same inclusion priority—*(Estimate)*, not a forecast.

**Step 4 — Staking revenue linkage (PoS)**

Validators earn \(R = \text{issuance} + \text{fees}\). If fee throughput falls 50% while validator opex rises 40% (hardware, bandwidth):

- Required yield uplift \(\Delta y\) to keep the same validator set depends on stake \(S\) and cost \(\Delta c\): rough breakeven \(\Delta y \approx \Delta c / S\) as a fraction of staked capital.
- Example: \(\Delta c = 0.7\%\) of stake per year → need **+0.7 pp** on nominal yield to hold validator count constant *(Estimate)*.

**Step 5 — Decision outputs**

| Output | Action |
|--------|--------|
| SCR > 20× | Trigger fee-market and L2 strategy review |
| Throughput ↓ > 50% | Model governance participation and oracle update costs |
| Validator opex ↑ > 25% | Revisit issuance, MEV redistribution, or minimum stake |

*Tag all forward projections as (Scenario) or (Estimate) in governance materials.*

---
