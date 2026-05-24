# Chapter 12: FIPS 204 — ML-DSA (Module-Lattice Digital Signature Algorithm)

## 12.1 Overview

ML-DSA (Module-Lattice-Based Digital Signature Algorithm), standardized as FIPS 204, is the primary post-quantum digital signature standard. It provides existential unforgeability under chosen-message attacks (EUF-CMA), meaning an attacker who can obtain signatures on messages of their choice cannot forge a signature on any new message.

ML-DSA is based on the hardness of the Module-LWE and Module-SIS (Short Integer Solution) problems, using the Fiat-Shamir with Aborts paradigm.

## 12.2 Design Philosophy: Fiat-Shamir with Aborts

### Classical Fiat-Shamir

The Fiat-Shamir heuristic converts a three-round identification protocol into a signature scheme:
1. **Commit:** Prover generates randomness and sends commitment
2. **Challenge:** Verifier sends random challenge (in signature: derived from hash)
3. **Response:** Prover computes response using secret and challenge

### The Problem with Naive Lattice Signatures

In a naive lattice Schnorr-like scheme:
- Secret: **s**, Public: **t** = **A**·**s**
- Commit: **y** random, **w** = **A**·**y**
- Challenge: c = H(message, **w**)
- Response: **z** = **y** + c·**s**

The problem: **z** = **y** + c·**s** leaks information about **s** through its distribution. Over many signatures, an attacker can recover **s**.

### The Abort Solution (Lyubashevsky)

ML-DSA uses **rejection sampling** to ensure signatures are independent of the secret key:

1. Generate response **z** = **y** + c·**s**
2. Check if **z** is "too large" or correlates with **s**
3. If so: **reject and restart** (abort)
4. Only output signatures that look like they came from a uniform distribution

This ensures the distribution of valid signatures is independent of the specific secret key, achieving zero-knowledge.

## 12.3 Parameter Sets

| Parameter | ML-DSA-44 | ML-DSA-65 | ML-DSA-87 |
|-----------|----------|----------|----------|
| Security Level | 2 | 3 | 5 |
| (k, ℓ) | (4, 4) | (6, 5) | (8, 7) |
| n | 256 | 256 | 256 |
| q | 8380417 | 8380417 | 8380417 |
| d (dropped bits) | 13 | 13 | 13 |
| τ (challenge weight) | 39 | 49 | 60 |
| γ₁ (masking range) | 2^17 | 2^19 | 2^19 |
| γ₂ (decomposition) | (q-1)/88 | (q-1)/32 | (q-1)/32 |
| η (secret range) | 2 | 4 | 2 |
| β (rejection bound) | 78 | 196 | 120 |
| ω (hint ones) | 80 | 55 | 75 |
| Public key | 1,312 B | 1,952 B | 2,592 B |
| Secret key | 2,560 B | 4,032 B | 4,896 B |
| Signature | 2,420 B | 3,309 B | 4,627 B |

The naming convention "ML-DSA-44" refers to (k=4, ℓ=4), "ML-DSA-65" to (k=6, ℓ=5), etc.

## 12.4 Algorithm Description

### Key Generation (ML-DSA.KeyGen)

```
1. ξ ← Random(32)                          // Random seed
2. (ρ, ρ', K) ← H(ξ)                      // Expand into seeds
3. Â ← ExpandA(ρ)                          // Generate public matrix (k × ℓ)
4. (s₁, s₂) ← ExpandS(ρ')                 // Sample secret vectors
                                            // s₁ ∈ R_q^ℓ, s₂ ∈ R_q^k, coefficients in [-η, η]
5. t ← A · s₁ + s₂                        // Compute public key vector
6. (t₁, t₀) ← Power2Round(t, d)           // Split into high/low bits
7. pk ← (ρ, t₁)                           // Public key
8. sk ← (ρ, K, tr, s₁, s₂, t₀)           // Secret key (tr = Hash(pk))
```

### Signing (ML-DSA.Sign)

```
1. μ ← H(tr ‖ M)                          // Message representative
2. ρ' ← H(K ‖ μ)                          // Deterministic nonce (or with randomness)
3. κ ← 0                                   // Attempt counter
4. (z, h) ← ⊥                             // Initialize output
5. while (z, h) = ⊥:
   a. y ← ExpandMask(ρ', κ)               // Masking vector, coefficients in [-γ₁+1, γ₁]
   b. w ← A · y                           // Commitment
   c. w₁ ← HighBits(w, 2γ₂)              // High-order bits of commitment
   d. c̃ ← H(μ ‖ w₁)                     // Challenge hash
   e. c ← SampleInBall(c̃)                // Challenge polynomial (τ non-zero coefficients ±1)
   f. z ← y + c · s₁                     // Response
   g. if ‖z‖∞ ≥ γ₁ - β: restart          // Rejection: response too large
   h. r₀ ← LowBits(A·z - c·t, 2γ₂)
   i. if ‖r₀‖∞ ≥ γ₂ - β: restart         // Rejection: would reveal secret
   j. h ← MakeHint(w - c·s₂, w₁)         // Hint for verification
   k. if ones(h) > ω: restart             // Too many hint bits
   l. κ ← κ + 1
6. σ ← (c̃, z, h)                         // Signature
```

### Verification (ML-DSA.Verify)

```
1. μ ← H(tr ‖ M)                          // Message representative (tr from pk)
2. c ← SampleInBall(c̃)                    // Reconstruct challenge polynomial
3. w₁' ← UseHint(h, A·z - c·t₁·2^d)     // Recover high bits of commitment
4. Check: ‖z‖∞ < γ₁ - β                   // Response within bounds
5. Check: c̃ = H(μ ‖ w₁')                 // Challenge matches
6. Check: ones(h) ≤ ω                      // Hint weight valid
```

## 12.5 Key Mechanisms Explained

### Rejection Sampling

The abort mechanism ensures security:
- Without rejection: signatures leak information about s₁ (after ~n signatures, full recovery possible)
- With rejection: distribution of z is statistically close to uniform in [-γ₁+1, γ₁]^(256ℓ)
- Average attempts per signature: ~4-7 depending on parameters

### The Hint Vector

A clever optimization:
- The verifier needs w₁ (high bits of A·y) but only has z (not y)
- The verifier can compute A·z - c·t = A·(y + c·s₁) - c·(A·s₁ + s₂) = A·y - c·s₂
- The hint h tells the verifier exactly which positions' high bits differ between A·z - c·t₁·2^d and the true w₁
- This avoids transmitting w₁ directly (saving bandwidth)

### Deterministic vs. Hedged Signing

ML-DSA supports two modes:
- **Deterministic:** ρ' derived only from secret key and message (reproducible signatures)
- **Hedged:** ρ' includes fresh randomness (protects against fault attacks but non-reproducible)

FIPS 204 mandates the hedged variant for general use, with deterministic available for specific applications.

### The Challenge Polynomial

The challenge c is not a random polynomial but a sparse one:
- Exactly τ non-zero coefficients (all ±1)
- Sampled from the hash using a rejection procedure
- Sparsity bounds ‖c·s₁‖ and ‖c·s₂‖, enabling the rejection condition

## 12.6 Security Analysis

### Module-LWE / Module-SIS Hardness

ML-DSA's security reduces to:
- **MLWE(k, ℓ, η):** Hiding the secret key in the public key
- **MSIS(k, ℓ+1, bound):** Difficulty of forging signatures (finding short vectors in a related lattice)

### EUF-CMA Security

Under the EUF-CMA model:
- Attacker can request signatures on polynomially many chosen messages
- Attacker must produce a valid signature on a new message
- Security holds in the (quantum) random oracle model

### Concrete Security Estimates

| Parameter Set | Classical Security | Quantum Security | NIST Level |
|--------------|-------------------|-----------------|-----------|
| ML-DSA-44 | ~2^128 | ~2^115 | 2 |
| ML-DSA-65 | ~2^192 | ~2^170 | 3 |
| ML-DSA-87 | ~2^256 | ~2^225 | 5 |

### Known Attack Vectors

1. **Key recovery via lattice reduction:** Apply BKZ to the lattice defined by (A, t) to find s₁, s₂
2. **Forgery via SIS:** Find a short vector that yields a valid signature without the secret
3. **Algebraic attacks on ring structure:** No practical exploitation of module structure known
4. **Side-channel attacks:** Implementation-dependent (not algorithmic)

## 12.7 Implementation Guidance

### Constant-Time Imperatives

Critical constant-time operations:
- **Rejection sampling loop:** The NUMBER of iterations may leak but not which iteration succeeded
- **Polynomial multiplication:** NTT operations must be constant-time
- **Norm checks:** Comparison with bounds must not branch on secret data
- **Hint computation:** Must not leak secret s₂ values

### The Signing Loop

The rejection loop is a unique implementation challenge:
- Average iterations: 4-7 (parameter dependent)
- Maximum iterations: Unbounded (but exponentially unlikely to be large)
- Iteration count is NOT secret (it can leak)
- But intermediate values (y, partial computations) from rejected iterations MUST be destroyed

### Random Number Generation

- Key generation: 32 bytes of entropy required
- Hedged signing: Additional randomness per signature
- Deterministic signing: No additional randomness (derived from key + message)
- Nonce reuse with deterministic mode: Different messages always produce different ρ' (safe)

### Batch Verification

ML-DSA supports efficient batch verification:
- Verify multiple signatures simultaneously
- Random linear combination technique reduces computation
- Speedup: ~2-4x for batches of 10+ signatures
- Particularly useful for blockchain and certificate chain verification

## 12.8 Performance Characteristics

### Operation Timing (x86-64 with AVX2)

| Operation | ML-DSA-44 | ML-DSA-65 | ML-DSA-87 |
|-----------|----------|----------|----------|
| KeyGen | ~150 μs | ~250 μs | ~400 μs |
| Sign (average) | ~700 μs | ~1,100 μs | ~1,500 μs |
| Verify | ~200 μs | ~300 μs | ~450 μs |

### Comparison with Classical Signatures

| Metric | ML-DSA-65 | Ed25519 | RSA-2048 | ECDSA P-256 |
|--------|----------|---------|----------|-------------|
| Public key | 1,952 B | 32 B | 256 B | 64 B |
| Signature | 3,309 B | 64 B | 256 B | 64 B |
| Sign time | ~1.1 ms | ~50 μs | ~1 ms | ~60 μs |
| Verify time | ~300 μs | ~120 μs | ~30 μs | ~120 μs |

ML-DSA is moderately slower with significantly larger keys/signatures compared to elliptic curve schemes.

## 12.9 Comparison with Other PQC Signatures

| Metric | ML-DSA-65 | SLH-DSA-192s | FN-DSA-512 |
|--------|----------|-------------|-----------|
| Public key | 1,952 B | 48 B | 897 B |
| Signature | 3,309 B | 16,224 B | 666 B |
| Sign time | ~1.1 ms | ~200 ms | ~5 ms |
| Verify time | ~300 μs | ~5 ms | ~0.5 ms |
| Security basis | Module-LWE/SIS | Hash functions | NTRU lattice |
| Implementation complexity | Low | Low | High |

ML-DSA offers the best balance of size and speed for most applications.

## 12.10 Use Cases and Deployment

### Ideal Applications for ML-DSA

- **TLS certificate authentication:** Moderate signature size acceptable
- **Code signing:** Performance suitable for signing and verification
- **Document signatures:** Standard PDF/document signing workflows
- **Authentication tokens:** JWT-like token signing
- **API authentication:** Request signing for web services

### Considerations for Specific Scenarios

**Certificate chains:**
- Each certificate contains a signature (~3.3 KB for Level 3)
- A 3-certificate chain adds ~10 KB to TLS handshake
- Acceptable for most connections; concern for very constrained links

**Blockchain/Distributed ledger:**
- Larger signatures increase block size
- Batch verification helps throughput
- Storage implications for historical signatures

**Embedded/IoT:**
- ML-DSA-44 feasible on ARM Cortex-M4 (~10 ms sign, ~3 ms verify)
- RAM requirements: ~30 KB for signing
- Public key storage may be constraining

## 12.11 Deterministic Signatures and Nonce Safety

### Why Nonce Quality Matters

In schemes like ECDSA, a bad nonce is catastrophic (full key recovery from one bad signature). ML-DSA's design provides better resilience:

- Deterministic mode: Nonce derived from (K, message) — no randomness needed
- Even with deterministic mode, the secret K is per-key (not message-dependent)
- No "nonce reuse" vulnerability in the ECDSA sense

### Hedged Mode Benefits

The hedged mode (ρ' includes randomness) provides:
- Protection against fault injection that forces nonce reuse
- Side-channel resistance: Different randomness each time limits DPA effectiveness
- Defense in depth if hash function has weaknesses

## 12.12 Key Takeaways

- ML-DSA (FIPS 204) is the primary post-quantum signature standard
- Based on Module-LWE/SIS with Fiat-Shamir with Aborts
- Three parameter sets: ML-DSA-44 (Level 2), ML-DSA-65 (Level 3), ML-DSA-87 (Level 5)
- Rejection sampling ensures zero-knowledge (signatures don't leak the key)
- Signatures are ~2.4-4.6 KB; public keys are ~1.3-2.6 KB
- Signing involves a probabilistic loop (average 4-7 iterations)
- Well-suited for most signature applications (TLS, code signing, authentication)
- Hedged signing mode recommended for general use
- Constant-time implementation required for side-channel resistance

---

*Next: [Chapter 13 — FIPS 205: SLH-DSA](./13-fips-205-slh-dsa.md)*
