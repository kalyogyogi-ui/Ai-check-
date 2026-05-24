# Chapter 22: Future Directions and Open Problems

## 22.1 The Evolving Landscape

Post-quantum cryptography is not a static field. The standardization of FIPS 203, 204, and 205 represents a critical milestone, but significant research challenges remain. This chapter explores the frontiers of PQC research and the open problems that will shape the next decade of cryptographic development.

## 22.2 Advanced Cryptographic Primitives from PQC

### Fully Homomorphic Encryption (FHE)

**The vision:** Compute on encrypted data without decryption.

**Current state:**
- All practical FHE schemes are lattice-based (inherently quantum-resistant)
- Performance improving exponentially (1,000,000x improvement over past decade)
- Standardization efforts underway (HomomorphicEncryption.org)
- Real applications emerging (private database queries, ML inference)

**Open problems:**
- Practical performance for general computation
- Reducing ciphertext expansion
- Efficient bootstrapping for deep circuits
- Hardware acceleration for FHE operations

### Zero-Knowledge Proofs from PQC Assumptions

**Current state:**
- Lattice-based ZK proofs exist but are large (~100 KB - 1 MB)
- Hash-based ZK (STARKs) are quantum-safe and practical
- ZK-SNARKs on lattice assumptions remain inefficient

**Open problems:**
- Compact lattice-based ZK proofs (sub-KB)
- Efficient PQC-based credentials and anonymous authentication
- PQC verifiable computation
- Post-quantum privacy-preserving identity systems

### Multi-Party Computation (MPC)

**Current state:**
- Oblivious Transfer from lattice assumptions (efficient)
- PQC-based secret sharing and threshold protocols
- Quantum-safe MPC frameworks emerging

**Open problems:**
- Round-efficient PQC MPC protocols
- Threshold PQC signatures (threshold ML-DSA)
- Practical PQC distributed key generation
- PQC-based private set intersection at scale

### Attribute-Based and Functional Encryption

**Current state:**
- Lattice-based ABE constructions exist (theoretical)
- Functional encryption from LWE (limited functions)
- Inner product functional encryption (practical for some uses)

**Open problems:**
- Efficient ABE for practical policy sizes
- Unbounded-attribute ABE from lattices
- Functional encryption for general circuits
- Practical key-policy and ciphertext-policy ABE

## 22.3 Signature Aggregation and Compression

### The Problem

PQC signatures are 30-100x larger than classical ECDSA. For applications processing many signatures (blockchain, certificate transparency, signed logs), this is a major scalability concern.

### Research Directions

**Aggregate signatures:** Combine n signatures into one compact signature
- Classical: BLS signatures aggregate trivially
- PQC: No efficient general aggregation known for lattice signatures
- Partial solutions: Sequential aggregation, specific constructions

**Batch verification:** Verify many signatures faster than individually
- ML-DSA supports batch verification (random linear combination)
- Speedup: 2-4x for batches of 10+
- Not the same as reducing signature size

**Structured compact signatures:**
- MAYO (multivariate): ~321 bytes at Level 1
- SQISign (isogeny): ~177 bytes at Level 1
- FN-DSA: ~666 bytes at Level 1
- Can we do better from well-studied assumptions?

### Open Problems

- Efficient aggregate signatures from lattice assumptions
- Compact multi-signatures for blockchain consensus
- Accountable-subgroup multi-signatures from PQC
- Signature size reduction without weakening assumptions

## 22.4 Post-Quantum Blockchain and Distributed Systems

### Challenges

- Transaction signatures dominate blockchain data
- State growth from larger public keys
- Smart contract verification of PQC signatures
- Consensus protocol adaptation

### Research Directions

- **Hash-based accumulators:** Replace Merkle trees with more efficient PQC structures
- **PQC-friendly consensus:** Design consensus around PQC constraints
- **State compression:** Techniques for managing PQC key/signature bloat
- **Layer-2 solutions:** Move PQC overhead off-chain where possible
- **Quantum-safe randomness beacons:** Public randomness from PQC assumptions

## 22.5 Lightweight PQC for IoT and Embedded

### Current Constraints

Many IoT devices have:
- < 32 KB RAM
- < 256 KB flash storage
- Clock speeds < 100 MHz
- Energy budgets < 1 mJ per crypto operation
- Bandwidth < 1 kbps

### Research Directions

**Lightweight lattice schemes:**
- Smaller parameters for lower security requirements
- Optimized NTT for small word sizes
- Memory-efficient key generation

**LPN/LWE-based lightweight protocols:**
- Authentication protocols from LPN
- Lightweight key exchange
- Challenge-response with minimal computation

**Hardware-software co-design:**
- Minimal crypto accelerators for PQC
- Application-specific instruction sets
- Energy-harvesting-compatible operations

### Open Problems

- ML-KEM on < 16 KB RAM devices
- PQC authentication for sub-$0.10 chips
- Battery-less PQC (energy harvesting contexts)
- PQC in RFID and NFC form factors

## 22.6 Cryptanalysis: What Could Go Wrong?

### Potential Threats to Current Standards

**New classical attacks on structured lattices:**
- Could algebraic structure of Module-LWE be exploited?
- What if Ring-LWE has a sub-exponential classical attack?
- Algebraic attacks on NTT-friendly moduli?

**Assessment:** No evidence of such attacks after 20+ years of study, but cannot be ruled out. SLH-DSA provides insurance.

**Quantum algorithm breakthroughs:**
- Could a quantum algorithm for LWE be discovered?
- New approaches beyond Shor's and Grover's?
- Quantum lattice reduction improvements?

**Assessment:** Possible but would require fundamental breakthroughs in quantum algorithms. Most researchers consider it unlikely but not impossible.

**Side-channel and implementation attacks:**
- Practical exploitation of timing/power leaks
- Fault injection attacks on deployed implementations
- Combined attacks (side-channel + mathematical)

**Assessment:** Most likely near-term threat. Continuous improvement in countermeasures needed.

### Monitoring and Response

The cryptographic community must maintain:
- Active cryptanalysis research on deployed standards
- Parameter adjustment capability if security margins erode
- Alternative algorithm readiness (SLH-DSA, code-based, etc.)
- Rapid response capability for algorithm compromise

## 22.7 Quantum Key Distribution (QKD) vs. PQC

### The Debate

**QKD proponents argue:**
- Information-theoretic security (provably unbreakable)
- No assumptions about computational hardness
- Security independent of future mathematical breakthroughs

**PQC proponents argue:**
- QKD requires dedicated quantum hardware and fiber
- QKD has distance limitations (~100 km without quantum repeaters)
- QKD cannot authenticate — needs classical/PQC crypto for authentication
- QKD does not replace all cryptographic functions (signatures, etc.)
- PQC runs on existing infrastructure

### Complementary Roles

The likely future uses both:
- **PQC:** General-purpose quantum-resistant cryptography for all applications
- **QKD:** Ultra-high-security point-to-point links (government, financial, military)
- **Hybrid PQC+QKD:** Maximum security for the most critical links

### Quantum Internet

Long-term vision:
- Quantum repeaters enable long-distance entanglement distribution
- Quantum network protocols for key establishment
- Integration with PQC for authentication and non-QKD functions
- Decades away from widespread deployment

## 22.8 Post-Quantum Random Oracles and Hash Functions

### Current Understanding

PQC security proofs often rely on the **Random Oracle Model (ROM)** or the **Quantum Random Oracle Model (QROM)**:
- QROM models adversaries making quantum queries to hash functions
- Some classical ROM proofs don't directly translate to QROM
- Ongoing work to prove security of NIST standards in QROM

### Open Problems

- Tighter QROM reductions for FO transform (ML-KEM)
- Understanding the gap between ROM and QROM security
- Hash function design for quantum security
- Instantiation of random oracles with concrete hash functions

### Hash Function Security

- Are SHA-256 and SHA-3 secure against all quantum attacks?
- Beyond Grover: Are there structural quantum attacks?
- Sponge construction security in the quantum setting
- Long-term hash function design principles

## 22.9 Formal Verification of PQC Implementations

### The Need

PQC implementations are complex — formal verification can provide mathematical proof of:
- Functional correctness (matches specification)
- Constant-time execution (no timing leaks)
- Memory safety (no buffer overflows)
- Protocol-level security properties

### Current State

- **Jasmin:** Formally verified assembly implementations of PQC
- **EasyCrypt:** Computer-aided cryptographic proofs
- **F*:** Verified implementation of TLS with PQC
- **Coq/Lean proofs:** Mathematical verification of core algorithms

### Open Problems

- Scaling formal verification to full library implementations
- Verified compilation from high-level to constant-time assembly
- Automated side-channel absence proofs
- Verification of PQC hardware implementations

## 22.10 The Long-Term Cryptographic Landscape

### 2025-2030: Deployment Era

- Widespread hybrid deployment across protocols
- Hardware acceleration for PQC operations
- Completion of certificate infrastructure migration
- IoT and embedded PQC solutions mature

### 2030-2040: Maturation Era

- PQC-only deployments become common
- Second-generation PQC standards (improved efficiency)
- Advanced PQC primitives (FHE, ZK, MPC) become practical
- Quantum computers approach cryptographic relevance

### 2040+: Quantum Era

- Cryptographically-relevant quantum computers exist
- PQC is standard; pre-PQC systems are legacy
- Quantum networking enables new cryptographic paradigms
- New hard problems may emerge from quantum complexity theory

## 22.11 Advice for Researchers

### High-Impact Open Problems

1. **Efficient PQC signature aggregation** — Would transform blockchain and IoT
2. **Compact lattice-based zero-knowledge proofs** — Enables privacy-preserving PQC
3. **Lightweight PQC for extreme constraints** — Opens IoT/RFID applications
4. **Tighter security reductions** — Could allow smaller parameters
5. **Better understanding of structured lattice security** — Foundation for all lattice PQC
6. **Post-quantum anonymous credentials** — Essential for privacy in PQC world
7. **Hardware-software co-design for PQC** — Practical acceleration approaches
8. **Side-channel resistant implementations at scale** — Secure for real deployment

### Underexplored Areas

- PQC for emerging computing paradigms (edge, fog, serverless)
- Post-quantum biometric authentication protocols
- Quantum-safe secure enclaves and TEEs
- PQC in operational technology (OT/ICS/SCADA)
- Post-quantum federated learning and AI security

## 22.12 Key Takeaways

- PQC standardization is a beginning, not an end — significant research continues
- Advanced primitives (FHE, ZK, MPC) from PQC assumptions are maturing
- Signature aggregation remains a critical open problem for scalability
- IoT and embedded PQC require further optimization research
- Cryptanalysis must continue vigilantly on deployed standards
- QKD and PQC serve complementary roles — both have a place
- Formal verification of PQC implementations is increasingly important
- The transition spans decades — we are in the early deployment phase
- The field offers numerous high-impact open research problems
- Organizations should deploy current standards while monitoring advances

---

*This concludes the main chapters. Continue to the appendices for mathematical prerequisites, glossary, tools, and further reading.*

*[Appendix A — Mathematical Prerequisites](./appendix-a-math.md)*
