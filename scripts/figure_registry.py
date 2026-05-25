# Figure registry: (chapter_stem) -> list of {id, section, caption, body, ref_sentence}
# section = exact ## heading prefix to match (first match in file)

def block_mermaid(code: str) -> str:
    return f"```mermaid\n{code.strip()}\n```\n"

FIGURES = {
    "01-introduction": [
        {
            "id": "1.1",
            "section": "## 1.1",
            "caption": "Figure 1.1 — Cryptographic trust stack under quantum attack",
            "ref": "Figure 1.1 summarizes which layers Shor and Grover affect; we use it in every architecture review.",
            "body": block_mermaid("""
flowchart TB
  subgraph apps [Application layer]
    WEB[HTTPS / APIs]
    VPN[VPN / ZTNA]
    SIGN[Code & firmware signing]
  end
  subgraph proto [Protocol layer]
    TLS[TLS 1.2/1.3]
    SSH[SSH / IPsec]
  end
  subgraph pk [Public-key — broken by Shor at scale]
    RSA[RSA encrypt/sign]
    ECC[ECDH ECDSA EdDSA]
  end
  subgraph sym [Symmetric / hash — Grover halves margin]
    AEAD[AES-GCM ChaCha20]
    HASH[SHA-2 SHA-3]
  end
  apps --> proto --> pk
  proto --> sym
"""),
        },
        {
            "id": "1.2",
            "section": "## 1.4",
            "caption": "Figure 1.2 — Harvest now, decrypt later (HNDL)",
            "ref": "Figure 1.2 is the threat model we use when arguing for hybrid KEX before CRQC exists.",
            "body": block_mermaid("""
sequenceDiagram
  autonumber
  participant A as Adversary
  participant N as Network tap
  participant S as Storage
  A->>N: Record TLS/IPsec ciphertext
  N->>S: Archive years cheaply
  Note over A,S: No decryption today
  A->>A: Later: CRQC + Shor
  A->>S: Retrospective decrypt
"""),
        },
        {
            "id": "1.3",
            "section": "## 1.5",
            "caption": "Figure 1.3 — Mosca inequality (planning)",
            "ref": "Use Figure 1.3 when prioritizing systems: if x + y > z, migration is already late for that data class.",
            "body": block_mermaid("""
flowchart LR
  x[x: confidentiality years] --> Q{x + y > z ?}
  y[y: migration years] --> Q
  z[z: CRQC horizon] --> Q
  Q -->|yes| R[At risk now]
  Q -->|no| OK[Window remains]
"""),
        },
    ],
    "02-quantum-computing-fundamentals": [
        {
            "id": "2.1",
            "section": "## 2.1",
            "caption": "Figure 2.1 — Classical bit vs qubit (conceptual)",
            "ref": "Figure 2.1 contrasts state space: one classical string versus amplitudes over 2^n basis states.",
            "body": block_mermaid("""
flowchart TB
  subgraph classical [Classical n-bit register]
    C1[Exactly one of 2^n states]
  end
  subgraph quantum [Quantum n-qubit register]
    Q1[Superposition over 2^n amplitudes]
    Q2[Measure → one n-bit string]
  end
  classical -.->|not parallel search| quantum
"""),
        },
        {
            "id": "2.2",
            "section": "## 2.2",
            "caption": "Figure 2.2 — Quantum circuit model",
            "ref": "Figure 2.2 is the abstraction Shor's algorithm instantiates: unitary evolution then measurement.",
            "body": block_mermaid("""
flowchart LR
  INIT[|0…0⟩ prepare] --> U[Unitary gates U]
  U --> INT[Interference builds peaks]
  INT --> MEAS[Measure → classical bits]
"""),
        },
        {
            "id": "2.3",
            "section": "## 2.4",
            "caption": "Figure 2.3 — Physical vs logical qubit",
            "ref": "Figure 2.3 explains why marketing qubit counts ≠ cryptographically relevant logical qubits.",
            "body": block_mermaid("""
flowchart TB
  PHY[10^6 physical qubits] --> QEC[Quantum error correction]
  QEC --> LOG[Thousands of logical qubits]
  LOG --> CRQC[CRQC needs millions logical for Shor on RSA-2048]
"""),
        },
    ],
    "03-quantum-attacks": [
        {
            "id": "3.1",
            "section": "## 3.1",
            "caption": "Figure 3.1 — Classical hard problems → deployed crypto",
            "ref": "Figure 3.1 links IFP, DLP, and ECDLP to the protocols you must replace.",
            "body": block_mermaid("""
flowchart LR
  IFP[Integer factorization] --> RSA[RSA]
  DLP[Finite-field DLP] --> DH[DH DSA]
  ECDLP[ECDLP] --> ECC[ECDH ECDSA]
"""),
        },
        {
            "id": "3.2",
            "section": "## 3.2",
            "caption": "Figure 3.2 — Shor pipeline (high level)",
            "ref": "Figure 3.2 is the path from period finding to broken public-key trust.",
            "body": block_mermaid("""
flowchart LR
  P[Period finding QFT] --> F[Factor / DLP / ECDLP]
  F --> B[Break RSA DH ECC]
"""),
        },
        {
            "id": "3.3",
            "section": "## 3.3",
            "caption": "Figure 3.3 — Grover impact on symmetric keys",
            "ref": "Figure 3.3 drives AES-256 policy: Grover halves effective key strength in the quantum query model.",
            "body": block_mermaid("""
flowchart LR
  AES128[AES-128] --> G128[~64-bit quantum margin]
  AES256[AES-256] --> G256[~128-bit quantum margin]
"""),
        },
    ],
    "15-hybrid-schemes": [
        {
            "id": "15.1",
            "section": "## 15.2",
            "caption": "Figure 15.1 — Hybrid TLS shared-secret architecture",
            "ref": "Figure 15.1 shows the combiner every production hybrid profile must implement.",
            "body": block_mermaid("""
flowchart TB
  subgraph client [Client]
    C1[X25519 ephemeral]
    C2[ML-KEM encaps]
  end
  subgraph server [Server]
    S1[X25519 ephemeral]
    S2[ML-KEM ciphertext]
  end
  C1 --> SS1[classical ss]
  S1 --> SS1
  C2 --> SS2[pqc ss]
  S2 --> SS2
  SS1 --> HKDF[HKDF-Extract transcript]
  SS2 --> HKDF
  HKDF --> KEYS[TLS handshake keys]
"""),
        },
        {
            "id": "15.2",
            "section": "## 15.3",
            "caption": "Figure 15.2 — Hybrid signature verification",
            "ref": "Figure 15.2: a hybrid signature is valid only if **both** classical and PQC verify.",
            "body": block_mermaid("""
flowchart LR
  M[Message] --> CS[Classical sig verify]
  M --> PS[ML-DSA verify]
  CS --> AND{Both OK?}
  PS --> AND
  AND -->|yes| OK[Accept]
  AND -->|no| REJ[Reject]
"""),
        },
    ],
    "18-pqc-protocols": [
        {
            "id": "18.1",
            "section": "### Hybrid Key Exchange in TLS 1.3",
            "caption": "Figure 18.1 — TLS 1.3 hybrid key exchange (RFC 8446 + hybrid groups)",
            "ref": "Figure 18.1 maps where hybrid bytes appear in the handshake flight.",
            "body": block_mermaid("""
sequenceDiagram
  participant C as Client
  participant S as Server
  C->>S: ClientHello + key_share (X25519 + ML-KEM-768)
  S->>C: ServerHello + key_share + EncryptedExtensions
  Note over C,S: ss = HKDF(X25519_ss || ML-KEM_ss)
  C->>S: Finished
  S->>C: Finished
"""),
        },
        {
            "id": "18.2",
            "section": "## 18.2",
            "caption": "Figure 18.2 — X.509 PKI chain with PQC signatures",
            "ref": "Figure 18.2 shows why intermediate CA certificates dominate handshake size growth.",
            "body": block_mermaid("""
flowchart TB
  ROOT[Root CA ML-DSA-87 offline] --> INT[Intermediate ML-DSA-65]
  INT --> EE[End-entity ML-DSA-44/65]
  EE --> TLS[TLS Certificate message]
  TLS --> CV[CertificateVerify signature]
"""),
        },
    ],
    "11-fips-203-ml-kem": [
        {
            "id": "11.1",
            "section": "## 11.3",
            "caption": "Figure 11.1 — ML-KEM-768 object sizes (wire format)",
            "ref": "Size budget for hybrid TLS lives in Figure 11.1—account for key_share growth on mobile paths.",
            "body": """| Object | Bytes (ML-KEM-768) | Notes |
|--------|-------------------:|-------|
| `ek` (public key) | 1,184 | Often in ClientHello key_share |
| `dk` (secret key) | 2,400 | HSM-only; never log |
| `c` (ciphertext) | 1,088 | Server → client in hybrid KEX |
| Shared secret | 32 | Input to HKDF with classical ss |

""",
        },
        {
            "id": "11.2",
            "section": "## 11.5",
            "caption": "Figure 11.2 — IND-CCA2 via Fujisaki–Okamoto (implicit rejection)",
            "ref": "Figure 11.2 is the decapsulation path your implementation must match byte-for-byte in tests.",
            "body": block_mermaid("""
flowchart TD
  IN[ciphertext c] --> DEC[Decrypt m']
  DEC --> RE[Re-encrypt c']
  RE --> CMP{c == c' ?}
  CMP -->|yes| K1[KDF K' || H(c)]
  CMP -->|no| K2[KDF z || H(c) pseudorandom]
"""),
        },
    ],
}

# Default second-figure placement: map stem -> list of improved figures for remaining chapters
# Will be merged in place_figures.py from existing mermaid in files if not in registry
