# Chapter 4: Overview of Post-Quantum Cryptography

## 4.1 Design Principles of Post-Quantum Algorithms

Post-quantum cryptography aims to construct public-key algorithms whose security relies on mathematical problems for which no efficient quantum algorithm is known. The key design principles are:

1. **Quantum-resistant hardness assumptions:** The underlying mathematical problem should resist known quantum attacks
2. **Classical efficiency:** Algorithms must run efficiently on today's classical hardware
3. **Formal security proofs:** Security should be reducible to well-studied hard problems
4. **Practical parameters:** Key sizes, signature sizes, and computational costs must be manageable
5. **Implementation safety:** Algorithms should be resistant to side-channel attacks and implementation errors

## 4.2 The Five Families of PQC

Post-quantum cryptography encompasses five major algorithm families, each based on different mathematical foundations:

### 4.2.1 Lattice-Based Cryptography

**Foundation:** Hard problems on mathematical lattices — structured geometric objects in high-dimensional space.

**Key Problems:**
- Learning With Errors (LWE)
- Ring-LWE / Module-LWE
- Short Integer Solution (SIS)
- NTRU problem

**Standardized Algorithms:**
- ML-KEM (FIPS 203) — Key encapsulation
- ML-DSA (FIPS 204) — Digital signatures

**Strengths:**
- Strong theoretical security foundations
- Efficient implementations possible
- Versatile — supports encryption, signatures, and advanced constructions (FHE, ABE)
- Well-studied problems with decades of cryptanalytic history

**Challenges:**
- Larger key sizes compared to ECC
- Security of structured variants (Ring/Module) less established than plain LWE
- Parameter selection requires careful analysis

### 4.2.2 Code-Based Cryptography

**Foundation:** The hardness of decoding random linear error-correcting codes.

**Key Problems:**
- Syndrome Decoding Problem
- Learning Parity with Noise (LPN)
- Bounded Distance Decoding

**Notable Algorithms:**
- Classic McEliece — NIST Round 4 candidate (encryption/KEM)
- BIKE — NIST Round 4 candidate
- HQC — NIST additional selection for standardization

**Strengths:**
- Oldest PQC proposal (McEliece, 1978) — nearly 50 years of cryptanalysis
- Very fast encryption and decryption
- Well-understood security assumptions

**Challenges:**
- Very large public keys (hundreds of kilobytes to megabytes for McEliece)
- Limited flexibility (primarily encryption/KEM, not signatures)
- Structured variants trade security confidence for smaller keys

### 4.2.3 Hash-Based Signatures

**Foundation:** Security relies solely on the properties of cryptographic hash functions (one-wayness, collision resistance).

**Key Constructions:**
- Merkle trees for key management
- Winternitz One-Time Signatures (WOTS+)
- XMSS (stateful)
- SPHINCS+ / SLH-DSA (stateless)

**Standardized Algorithm:**
- SLH-DSA (FIPS 205) — Stateless hash-based digital signatures

**Strengths:**
- Minimal security assumptions — only requires a secure hash function
- Extremely well-understood security
- Conservative choice with highest confidence in quantum resistance
- Simple mathematical structure

**Challenges:**
- Large signatures (tens of kilobytes for stateless variants)
- Slower signing/verification compared to lattice-based alternatives
- Stateful variants require careful state management

### 4.2.4 Multivariate Polynomial Cryptography

**Foundation:** The hardness of solving systems of multivariate quadratic polynomial equations over finite fields (the MQ problem).

**Key Problems:**
- Multivariate Quadratic (MQ) problem
- Extended Isomorphism of Polynomials

**Notable Algorithms:**
- UOV (Unbalanced Oil and Vinegar) — Signatures
- Rainbow — Broken in 2022 (key recovery attack)
- GeMSS — NIST candidate (withdrawn)

**Strengths:**
- Very fast signature verification
- Small signatures
- Long history of study

**Challenges:**
- Large public keys
- Several schemes broken during NIST process
- Fewer viable candidates remaining
- Less confidence in security compared to lattice or hash-based approaches

### 4.2.5 Isogeny-Based Cryptography

**Foundation:** The hardness of computing isogenies between elliptic curves (maps that preserve group structure).

**Key Problems:**
- Supersingular Isogeny Problem
- Endomorphism Ring Problem

**Notable Algorithms:**
- SIKE/SIDH — Broken in 2022 (devastating attack by Castryck-Decru)
- CSIDH — Status uncertain
- SQISign — Signature scheme, still being studied

**Strengths:**
- Smallest key sizes of any PQC family
- Mathematically elegant
- Group-action structure enables interesting protocols

**Challenges:**
- SIDH/SIKE completely broken in 2022
- Remaining schemes are computationally expensive
- Youngest field — less cryptanalytic maturity
- Active research area with evolving security understanding

## 4.3 Comparison of PQC Families

| Property | Lattice | Code | Hash | Multivariate | Isogeny |
|----------|---------|------|------|--------------|---------|
| KEM/Encryption | ✓ | ✓ | ✗ | ✗ | ✓ (broken for SIKE) |
| Signatures | ✓ | Limited | ✓ | ✓ | ✓ |
| Public Key Size | Medium | Very Large | Small-Medium | Large | Small |
| Ciphertext/Sig Size | Small-Medium | Small | Large | Small | Small |
| Speed | Fast | Fast | Moderate | Fast verify | Slow |
| Security Confidence | High | Very High | Very High | Medium | Low (post-SIKE) |
| Maturity | High | Very High | High | Medium | Low |
| NIST Standard | FIPS 203, 204 | Ongoing | FIPS 205 | — | — |

## 4.4 NIST's Selection Rationale

NIST's standardization considered multiple factors in selecting algorithms:

### Primary Criteria
1. **Security:** Confidence in the underlying hardness assumption against quantum and classical attacks
2. **Performance:** Computational efficiency on diverse platforms
3. **Implementation characteristics:** Resistance to side-channel attacks, ease of correct implementation

### Secondary Criteria
4. **Key and ciphertext sizes:** Impact on bandwidth and storage
5. **Flexibility:** Ability to support different security levels
6. **Algorithm diversity:** Selecting from different mathematical families to hedge against breakthrough cryptanalysis

### The Final Selection

NIST selected algorithms from two families for their primary standards:
- **Lattice-based:** ML-KEM and ML-DSA (efficiency and versatility)
- **Hash-based:** SLH-DSA (conservative security, diversity)

Additional selections for standardization:
- **Code-based:** HQC (diversity for key encapsulation)
- **Lattice-based:** Additional signature schemes under evaluation

## 4.5 Security Levels

NIST defines five security strength categories for PQC algorithms:

| Level | Classical Equivalent | Quantum Equivalent | Reference |
|-------|---------------------|-------------------|-----------|
| 1 | AES-128 key search | Grover on AES-128 | 128-bit classical |
| 2 | SHA-256 collision | Quantum collision finding | 128-bit quantum |
| 3 | AES-192 key search | Grover on AES-192 | 192-bit classical |
| 4 | SHA-384 collision | Quantum collision finding | 192-bit quantum |
| 5 | AES-256 key search | Grover on AES-256 | 256-bit classical |

Most deployments will target Level 1 or Level 3, providing 128-bit or 192-bit quantum security respectively. Level 5 is reserved for the highest-security applications.

## 4.6 The PQC Ecosystem

### Libraries and Implementations

The PQC ecosystem has matured significantly:

- **liboqs (Open Quantum Safe):** C library with implementations of all NIST candidates
- **PQClean:** Clean, portable C implementations of PQC algorithms
- **CIRCL (Cloudflare):** Go implementations of PQC algorithms
- **pqcrypto:** Rust implementations
- **Bouncy Castle:** Java/C# implementations
- **wolfSSL:** Embedded-friendly PQC implementations
- **OpenSSL 3.5+:** Native support for FIPS 203/204/205

### Protocol Integration

PQC is being integrated into major protocols:
- **TLS 1.3:** Hybrid key exchange with ML-KEM (already deployed by Chrome, Cloudflare)
- **SSH:** Post-quantum key exchange and authentication
- **S/MIME:** Post-quantum encrypted email
- **Signal Protocol:** PQXDH with ML-KEM
- **WireGuard:** Experimental PQ variants

### Hardware Support

Hardware vendors are adding PQC support:
- **HSMs:** Thales, Entrust, and others supporting PQC algorithms
- **TPMs:** TCG specifications for PQC-capable TPMs
- **Smart cards:** PQC implementations for constrained devices
- **FPGA/ASIC:** Hardware acceleration for lattice operations

## 4.7 Choosing the Right Algorithm

The choice of PQC algorithm depends on application requirements:

### For Key Encapsulation / Key Exchange
- **Default choice:** ML-KEM-768 (Level 3) or ML-KEM-512 (Level 1)
- **Conservative choice:** Classic McEliece (Level 5, very large keys)
- **Hybrid deployment:** ML-KEM combined with X25519 or P-256

### For Digital Signatures
- **Default choice:** ML-DSA-65 (Level 3) or ML-DSA-44 (Level 2)
- **Conservative choice:** SLH-DSA (hash-based, minimal assumptions)
- **Constrained environments:** ML-DSA-44 (smallest lattice signature)
- **Stateful (specialized):** XMSS/LMS (for firmware signing, etc.)

### Decision Factors

| Factor | Recommendation |
|--------|---------------|
| Bandwidth-constrained | ML-KEM (small ciphertexts) |
| Storage-constrained | ML-KEM/ML-DSA (moderate keys) |
| Maximum security confidence | SLH-DSA or Classic McEliece |
| High-performance needs | ML-KEM + ML-DSA |
| Embedded/IoT | ML-KEM-512 + ML-DSA-44 |
| Long-term archival | SLH-DSA + hybrid |

## 4.8 Open Research Areas

Despite significant progress, several areas remain active research topics:

1. **Tighter security proofs:** Reducing the gap between theoretical security and practical parameters
2. **Efficient signatures from codes:** Finding practical code-based signature schemes
3. **Advanced constructions:** Building PQC versions of threshold signatures, ring signatures, zero-knowledge proofs
4. **Structured lattice security:** Better understanding the security of Module-LWE vs. plain LWE
5. **Side-channel resistance:** Developing efficient constant-time implementations
6. **Hybrid protocol design:** Optimal combination of classical and PQC algorithms
7. **Post-quantum anonymous credentials:** Building privacy-preserving systems from PQC
8. **Fully Homomorphic Encryption:** Practical PQ-secure FHE schemes

## 4.9 Key Takeaways

- Five major PQC families exist, each with different trade-offs
- NIST has standardized lattice-based (ML-KEM, ML-DSA) and hash-based (SLH-DSA) algorithms
- Lattice-based algorithms offer the best balance of performance and security for most applications
- Hash-based signatures provide the most conservative security guarantees
- Code-based schemes offer the longest cryptanalytic track record but have large keys
- The SIKE break in 2022 demonstrated that newer mathematical approaches carry higher risk
- Algorithm selection should consider security requirements, performance constraints, and risk tolerance
- The PQC ecosystem is maturing rapidly with library support, protocol integration, and hardware acceleration

---

*Next: [Chapter 5 — Lattice-Based Cryptography](./05-lattice-based.md)*
