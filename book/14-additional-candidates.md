# Chapter 14: Additional Candidates and Round 4 Algorithms

## 14.1 Beyond the Primary Standards

While FIPS 203, 204, and 205 provide the foundation for post-quantum cryptography, NIST continues evaluating additional algorithms to provide diversity and address specific use cases. This chapter covers the algorithms still under consideration and those with specialized applications.

## 14.2 FN-DSA (FALCON)

### Overview

FN-DSA (Fast-Fourier Lattice-based Compact Signatures over NTRU) is a lattice-based signature scheme selected by NIST for standardization, pending due to implementation complexity.

### Construction

Based on the GPV framework (hash-and-sign over lattices):
- **Hard problem:** NTRU problem and Short Integer Solution (SIS) over NTRU lattices
- **Key:** A short basis of an NTRU lattice
- **Signing:** Sample a short vector close to a target (Gaussian sampling)
- **Verification:** Check that the signature vector is short and matches the message hash

### Gaussian Sampling Challenge

FN-DSA's main implementation complexity comes from its use of **discrete Gaussian sampling** over lattice cosets:
- Requires floating-point arithmetic with sufficient precision
- The "FALCON tree" precomputation enables efficient sampling
- Side-channel protection of Gaussian sampling is extremely difficult
- Constant-time implementations exist but are complex

### Parameters

| Parameter | FN-DSA-512 | FN-DSA-1024 |
|-----------|-----------|------------|
| Security Level | 1 | 5 |
| Dimension n | 512 | 1024 |
| Public key | 897 B | 1,793 B |
| Signature | ~666 B | ~1,280 B |
| Sign time | ~5 ms | ~10 ms |
| Verify time | ~0.5 ms | ~1 ms |

### Advantages Over ML-DSA

- **Much smaller signatures:** 666 B vs. 2,420 B (Level 1)
- **Smaller combined (pk + sig):** 1,563 B vs. 3,732 B
- **Fast verification**

### Disadvantages

- Complex implementation (floating-point Gaussian sampling)
- Side-channel vulnerability in sampling
- Larger public keys than SLH-DSA
- Implementation errors are more likely

### Status

FN-DSA is standardized separately from the primary three FIPS standards. It is recommended for applications where signature size is paramount and implementers have the expertise to handle its complexity.

## 14.3 Classic McEliece

### Overview

Classic McEliece is the most conservative KEM in the NIST process — a direct descendant of McEliece's 1978 cryptosystem with nearly 50 years of cryptanalytic history.

### Why It Wasn't the Primary KEM

- **Public keys are enormous:** 261 KB to 1.4 MB depending on security level
- Impractical for most protocol deployments (TLS, embedded)
- But: fastest decapsulation of any candidate

### Parameters

| Parameter Set | Level | PK Size | CT Size | Decaps |
|--------------|-------|---------|---------|--------|
| mceliece348864 | 1 | 261,120 B | 128 B | ~50 μs |
| mceliece460896 | 3 | 524,160 B | 188 B | ~80 μs |
| mceliece6688128 | 5 | 1,044,992 B | 240 B | ~120 μs |
| mceliece6960119 | 5 | 1,047,319 B | 226 B | ~120 μs |
| mceliece8192128 | 5 | 1,357,824 B | 240 B | ~140 μs |

### Ideal Use Cases

- **Long-term key pairs:** Where the key is stored once and used many times
- **Pre-distributed keys:** Government, military, or diplomatic channels
- **High-value key exchange:** Where bandwidth is not constrained but security is paramount
- **Archival encryption:** Encrypt-once, store-forever scenarios

### Status

Standardization is ongoing. Classic McEliece provides maximum confidence in quantum security but is impractical for most everyday applications.

## 14.4 HQC (Hamming Quasi-Cyclic)

### Overview

HQC was selected by NIST in 2024 for standardization as an additional KEM, providing code-based diversity alongside ML-KEM.

### Construction

HQC is based on a quasi-cyclic variant of the syndrome decoding problem:
- Uses a random quasi-cyclic code as a "transport" mechanism
- Adds an inner error-correcting code (Reed-Muller or tensor product) for reliable decryption
- No decryption failures (guaranteed by the inner code's error-correction capability)

### Parameters

| Parameter Set | Level | PK Size | CT Size | Shared Secret |
|--------------|-------|---------|---------|--------------|
| HQC-128 | 1 | 2,249 B | 4,497 B | 64 B |
| HQC-192 | 3 | 4,522 B | 9,042 B | 64 B |
| HQC-256 | 5 | 7,245 B | 14,485 B | 64 B |

### Advantages

- **Clean security reduction** to quasi-cyclic syndrome decoding
- **No decryption failures** (guaranteed correct decryption)
- **Code-based diversity** from lattice-based ML-KEM
- **Moderate key sizes** (much smaller than Classic McEliece)

### Disadvantages

- **Larger ciphertexts** than ML-KEM (4.5 KB vs 1.1 KB at Level 1)
- **Slower** than ML-KEM for encapsulation
- **Less compact** overall than lattice-based alternatives

### Rationale for Selection

HQC provides insurance: if Module-LWE is broken (unexpected but possible), HQC offers an independently-secure alternative based on different mathematics.

## 14.5 BIKE (Bit Flipping Key Encapsulation)

### Overview

BIKE is a code-based KEM using quasi-cyclic moderate-density parity-check (QC-MDPC) codes:
- Compact keys (~1.5 KB public key)
- Based on syndrome decoding of QC-MDPC codes
- Iterative (bit-flipping) decoding algorithm

### Parameters (Level 1)

- Public key: 1,541 bytes
- Ciphertext: 1,573 bytes
- Shared secret: 32 bytes
- Decapsulation: ~1-2 ms

### Challenges

1. **Decryption Failure Rate (DFR):** Must be < 2^-128 for CCA security
   - Proving DFR bounds for iterative decoders is difficult
   - Empirical testing cannot reach 2^-128 probability
   - Analytical bounds are conservative

2. **Timing Side Channels:** Iterative decoders have variable iteration counts
   - Constant-time implementations fix maximum iterations
   - Performance penalty for constant-time compliance

### Status

BIKE remains under NIST evaluation. It offers competitive sizes but the DFR analysis complexity has delayed its standardization.

## 14.6 Additional Signature Candidates

NIST's call for additional signatures attracted diverse submissions:

### UOV (Unbalanced Oil and Vinegar)

- **Type:** Multivariate
- **Signature:** ~96-128 bytes (very small)
- **Public key:** ~44-96 KB (large)
- **Strengths:** Small signatures, fast operations, long track record
- **Weaknesses:** Large public keys

### MAYO

- **Type:** Multivariate (compressed UOV variant)
- **Signature:** ~321 bytes (Level 1)
- **Public key:** ~1.2 KB (Level 1)
- **Innovation:** Uses a "whipping" technique to compress the public key dramatically
- **Status:** Promising candidate under active evaluation

### SQISign

- **Type:** Isogeny-based
- **Signature:** ~177 bytes (smallest of any PQC signature)
- **Public key:** 64 bytes
- **Signing time:** ~5 seconds (very slow)
- **Strengths:** Smallest combined size of any PQC signature scheme
- **Weaknesses:** Very slow signing, complex implementation, young field

### CROSS

- **Type:** Code-based (zero-knowledge proof of code equivalence)
- **Signature:** ~5-13 KB
- **Public key:** ~50-100 bytes
- **Strengths:** Small public keys, code-based diversity
- **Weaknesses:** Large signatures

### LESS (Linear Equivalence Signature Scheme)

- **Type:** Code-based
- **Based on:** Linear code equivalence problem
- **Strengths:** Novel mathematical foundation, compact keys

### MEDS (Matrix Equivalence Digital Signature)

- **Type:** Based on matrix code equivalence
- **Strengths:** New mathematical problem, good parameter trade-offs
- **Status:** Under evaluation

## 14.7 Stateful Hash-Based Signatures (XMSS/LMS)

Already standardized in NIST SP 800-208:

### XMSS (eXtended Merkle Signature Scheme)

- RFC 8391
- Stateful: Must track which leaves have been used
- Very compact signatures (~2.5 KB)
- Limited signature count (configurable: 2^10 to 2^20)

### LMS (Leighton-Micali Signature)

- RFC 8554
- Similar to XMSS with different design choices
- HSS (Hierarchical Signature System) for multi-level trees
- Simpler implementation than XMSS

### Use Cases for Stateful Schemes

- **Firmware signing:** Controlled environment, limited signatures
- **Certificate authorities:** Known, limited signing frequency
- **Hardware Security Modules:** HSM manages state reliably
- **Secure boot:** Fixed chain of trust, few signatures needed

### State Management Best Practices

1. Never sign before persistently updating state
2. Use hardware-backed state storage where possible
3. Reserve leaf indices to handle crashes (skip ahead on restart)
4. Consider multi-tree (HSS/XMSS^MT) for large signature counts
5. Audit state management implementation thoroughly

## 14.8 Comparison of All PQC Signature Schemes

| Scheme | PK | Sig | Sign Time | Verify Time | Basis |
|--------|-----|------|-----------|-------------|-------|
| ML-DSA-44 | 1,312 B | 2,420 B | ~0.7 ms | ~0.2 ms | Lattice |
| ML-DSA-65 | 1,952 B | 3,309 B | ~1.1 ms | ~0.3 ms | Lattice |
| FN-DSA-512 | 897 B | 666 B | ~5 ms | ~0.5 ms | Lattice (NTRU) |
| SLH-DSA-128f | 32 B | 17,088 B | ~5 ms | ~1 ms | Hash |
| SLH-DSA-128s | 32 B | 7,856 B | ~60 ms | ~3 ms | Hash |
| XMSS (h=10) | 64 B | ~2,500 B | ~2 ms | ~0.5 ms | Hash (stateful) |
| UOV-I | ~44 KB | ~96 B | ~0.01 ms | ~0.02 ms | Multivariate |
| MAYO-1 | ~1.2 KB | ~321 B | ~0.1 ms | ~0.1 ms | Multivariate |
| SQISign-I | 64 B | ~177 B | ~5,000 ms | ~100 ms | Isogeny |

## 14.9 Algorithm Selection Guide

### For General-Purpose Signing
**First choice:** ML-DSA-65 (balanced performance and security)

### For Minimum Signature Size
**First choice:** FN-DSA-512 (666 B, if implementation expertise available)
**Alternative:** MAYO-1 (321 B, if standardized)

### For Maximum Security Confidence
**First choice:** SLH-DSA (hash-only assumptions)
**For stateful contexts:** XMSS/LMS

### For Constrained Devices
**First choice:** ML-DSA-44 (best size/speed balance at lower level)

### For Long-Term Document Archival
**First choice:** SLH-DSA + ML-DSA dual signature (defense in depth)

## 14.10 Key Takeaways

- FN-DSA provides the smallest lattice-based signatures but has implementation complexity
- Classic McEliece offers maximum security confidence for KEMs but with impractical key sizes
- HQC provides code-based diversity for key encapsulation (selected for standardization)
- Multiple additional signature schemes are under evaluation for diverse mathematical foundations
- Stateful signatures (XMSS/LMS) are already standardized for specialized use cases
- The PQC landscape continues evolving with new schemes and ongoing analysis
- Organizations should primarily deploy FIPS 203/204/205 while monitoring additional standards

---

*Next: [Chapter 15 — Hybrid Cryptographic Schemes](./15-hybrid-schemes.md)*
