# Chapter 1: Introduction to Cryptography and the Quantum Threat

## 1.1 The Role of Cryptography in Modern Society

Cryptography is the invisible foundation of our digital civilization. Every time you send a message, make a payment, access a website, or verify your identity online, cryptographic algorithms work silently to ensure confidentiality, integrity, and authenticity. The scale is staggering: billions of TLS connections are established every day, trillions of dollars in financial transactions are protected by public-key cryptography, and the entire fabric of internet commerce depends on the mathematical hardness of a handful of problems.

Modern public-key cryptography relies on three fundamental hard problems:

1. **Integer Factorization** — The difficulty of factoring the product of two large primes (RSA)
2. **Discrete Logarithm Problem** — The difficulty of computing logarithms in finite groups (Diffie-Hellman, DSA)
3. **Elliptic Curve Discrete Logarithm** — The discrete logarithm problem on elliptic curve groups (ECDH, ECDSA)

These problems have withstood decades of cryptanalytic effort from the world's best mathematicians. On a classical computer, the best known algorithms for factoring (General Number Field Sieve) and computing discrete logarithms (Index Calculus methods) have sub-exponential running time, making properly-sized keys computationally infeasible to break.

## 1.2 The Quantum Computing Revolution

Quantum computing represents a fundamentally different model of computation. Rather than processing information as classical bits (0 or 1), quantum computers use **quantum bits (qubits)** that can exist in superpositions of states. Through the phenomena of superposition, entanglement, and interference, quantum computers can solve certain problems exponentially faster than any known classical algorithm.

The development timeline of quantum computing has accelerated dramatically:

| Year | Milestone |
|------|-----------|
| 1981 | Feynman proposes quantum computing concept |
| 1994 | Shor develops polynomial-time factoring algorithm |
| 1996 | Grover develops quadratic-speedup search algorithm |
| 2019 | Google claims quantum supremacy with 53 qubits |
| 2023 | IBM unveils 1,121-qubit Condor processor |
| 2024 | Multiple systems exceed 1,000 logical qubits |
| 2025-2026 | Error-corrected systems approaching practical thresholds |

While today's quantum computers cannot yet break production cryptographic keys, the trajectory is clear. The question is not *if* but *when* a cryptographically relevant quantum computer (CRQC) will exist.

## 1.3 The "Harvest Now, Decrypt Later" Threat

Perhaps the most urgent concern is the **"Harvest Now, Decrypt Later" (HNDL)** attack model. Adversaries — particularly nation-states — are already collecting encrypted communications today with the intention of decrypting them once quantum computers become available.

This means that data with long-term confidentiality requirements is already at risk:

- **Government classified communications** — Secrets that must remain classified for 25-75 years
- **Medical records** — Patient data protected under decades-long privacy requirements
- **Financial transactions** — Banking and trade secrets with long-term competitive value
- **Intellectual property** — Patents, trade secrets, and research data
- **Infrastructure plans** — Critical infrastructure designs with multi-decade lifespans

The shelf life of encrypted data often exceeds the estimated timeline for quantum computers. If data encrypted today must remain confidential for 20 years, and a CRQC arrives in 10-15 years, then that data is already vulnerable.

## 1.4 Defining the Quantum Threat Timeline

The cryptographic community uses several frameworks for estimating quantum risk:

### Mosca's Theorem

Michele Mosca formalized the urgency with a simple inequality. If:
- **x** = the number of years data must remain secure
- **y** = the number of years needed to migrate cryptographic infrastructure  
- **z** = the number of years until a CRQC exists

Then if **x + y > z**, your organization is already at risk.

For many organizations:
- x = 10-30 years (data lifetime)
- y = 5-15 years (migration timeline)
- z = 10-20 years (CRQC arrival estimate)

The math is concerning for virtually every organization handling sensitive data.

### NIST's Timeline Assessment

NIST has operated under the assumption that a CRQC could arrive within 10-20 years, and that migration to quantum-resistant algorithms is a multi-year process requiring immediate action. This motivated their standardization effort, which began in 2016 and produced final standards in 2024.

## 1.5 What is Post-Quantum Cryptography?

**Post-Quantum Cryptography (PQC)**, also called quantum-resistant or quantum-safe cryptography, refers to cryptographic algorithms that are believed to be secure against attacks by both classical and quantum computers. Critically, PQC algorithms run on classical computers — they do not require quantum hardware.

PQC is distinct from:
- **Quantum Key Distribution (QKD)** — Uses quantum mechanics to distribute keys; requires specialized hardware and quantum channels
- **Quantum Random Number Generation (QRNG)** — Uses quantum processes to generate randomness

The key families of PQC algorithms include:

| Family | Hard Problem | Use Cases |
|--------|-------------|-----------|
| Lattice-based | Learning With Errors (LWE), Ring-LWE | KEM, Signatures |
| Code-based | Syndrome Decoding | KEM |
| Hash-based | Hash function properties | Signatures |
| Multivariate | Solving multivariate quadratic systems | Signatures |
| Isogeny-based | Computing isogenies between curves | KEM (largely broken) |

## 1.6 The Urgency of Action

The transition to post-quantum cryptography is one of the largest infrastructure changes in the history of computing. Consider what must be updated:

- Every TLS library and web server
- Every VPN implementation
- Every PKI system and certificate authority
- Every encrypted storage system
- Every digital signature scheme
- Every authentication protocol
- Every hardware security module (HSM)
- Every smart card and embedded device

The NIST standards finalized in 2024 (FIPS 203, 204, 205) provide the algorithmic foundation, but the implementation, testing, deployment, and migration work spans years. Organizations that begin now will be positioned to complete their migration before quantum computers threaten their infrastructure.

## 1.7 Structure of This Book

This book is organized into five parts:

**Part I (Chapters 1-4)** establishes foundations — the quantum threat, quantum computing basics, how quantum algorithms break current cryptography, and an overview of PQC approaches.

**Part II (Chapters 5-9)** provides deep technical exploration of each major PQC algorithm family — the mathematical constructions, security proofs, and design rationale.

**Part III (Chapters 10-14)** covers the NIST standardization process and the specific algorithms selected as standards — ML-KEM, ML-DSA, and SLH-DSA.

**Part IV (Chapters 15-18)** addresses practical implementation — hybrid schemes, side-channel resistance, performance, and protocol integration.

**Part V (Chapters 19-22)** covers migration strategy — cryptographic agility, inventory management, industry initiatives, and future research directions.

## 1.8 Key Takeaways

- Current public-key cryptography (RSA, ECC, DH) will be completely broken by quantum computers
- The "Harvest Now, Decrypt Later" threat means sensitive data is already at risk
- Post-quantum cryptography provides quantum-resistant algorithms that run on classical hardware
- NIST has standardized three PQC algorithms (FIPS 203, 204, 205) as of 2024
- Migration is a multi-year process that should begin immediately
- This book provides the complete technical foundation for understanding and implementing PQC

---

*Next: [Chapter 2 — Quantum Computing Fundamentals](./02-quantum-computing-fundamentals.md)*
