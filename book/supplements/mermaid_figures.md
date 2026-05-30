<!-- FIG 1.2 -->
```mermaid
flowchart TB
  subgraph H["Hidden assumptions"]
    C[Computational hardness]
    N[Network security model]
    B[Behavioral rationality]
    I[Institutional stability]
  end
  H --> E[Token economy behavior]
  E --> O[Observed outcomes: price, security, participation]
```
*Figure 1.2 — Hidden assumptions stack (digital edition).*

<!-- FIG 4.1 -->
```mermaid
flowchart TB
  subgraph P["Three pillars of governance legitimacy"]
    A[Authentication<br/>ECDSA / EdDSA]
    B[Integrity<br/>Hash functions]
    C[Non-repudiation<br/>PKI + ledger]
  end
  P --> L[Governance legitimacy]
  L --> CS[Cryptoeconomic substrate]
```
*Figure 4.1 — Governance legitimacy pillars (digital edition).*

<!-- FIG 5.1 -->
```mermaid
xychart-beta
    title "CRQC arrival — conceptual probability band (not statistical)"
    x-axis [2026, 2028, 2030, 2032, 2035, 2037, 2040, 2045]
    y-axis "Relative density (illustrative)" 0 --> 100
    line [5, 15, 45, 75, 90, 85, 60, 30]
```
*Figure 5.1 — Conceptual CRQC timeline density (Scenario). Policy lines: NIST 2030/2035.*

<!-- FIG 6.1 -->
```mermaid
flowchart TB
  TE[Token economy core]
  TE --> O[Ownership / UTXO & EOA exposure]
  TE --> S[Staking & consensus keys]
  TE --> G[Governance & multisig]
  TE --> D[DeFi & oracles]
  TE --> X[Bridges & IBC]
  O & S & G & D & X --> Q[Quantum threat surface]
```
*Figure 6.1 — Quantum threat surface map (digital edition).*
