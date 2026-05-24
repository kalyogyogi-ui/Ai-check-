# Chapter 11: FIPS 203 — ML-KEM (Module-Lattice Key Encapsulation Mechanism)

## 11.1 Overview

ML-KEM (Module-Lattice-Based Key Encapsulation Mechanism), standardized as FIPS 203, is the primary post-quantum key encapsulation mechanism. It enables two parties to establish a shared secret key over an insecure channel, providing security against both classical and quantum adversaries.

ML-KEM is based on the Module Learning With Errors (MLWE) problem and provides IND-CCA2 security (indistinguishability under adaptive chosen-ciphertext attack) through the Fujisaki-Okamoto transform.

## 11.2 Mathematical Foundation

### Module-LWE

ML-KEM operates over the polynomial ring:
```
R_q = Z_q[X]/(X^256 + 1)  where q = 3329
```

Elements of R_q are polynomials of degree at most 255 with coefficients in Z_q.

The Module-LWE problem: Given random matrix **A** ∈ R_q^(k×k) and vector **b** = **A**·**s** + **e** (where **s**, **e** have small coefficients), distinguish **b** from uniform random.

### Why q = 3329?

The modulus q = 3329 is chosen because:
- 3329 ≡ 1 (mod 256): Enables efficient Number Theoretic Transform (NTT)
- 3329 is prime: Simplifies modular arithmetic
- 3329 fits in 12 bits: Efficient representation
- Provides good noise tolerance for the chosen parameters

### The Number Theoretic Transform (NTT)

The NTT is the finite-field analog of the Fast Fourier Transform:
- Converts polynomial multiplication from O(n²) to O(n log n)
- ML-KEM stores polynomials in NTT domain where possible
- Multiplication in NTT domain is pointwise (O(n))
- Critical for performance

## 11.3 Parameter Sets

ML-KEM defines three parameter sets:

| Parameter | ML-KEM-512 | ML-KEM-768 | ML-KEM-1024 |
|-----------|-----------|-----------|------------|
| Security Level | 1 | 3 | 5 |
| k (module rank) | 2 | 3 | 4 |
| n (polynomial degree) | 256 | 256 | 256 |
| q (modulus) | 3329 | 3329 | 3329 |
| η₁ (secret noise) | 3 | 2 | 2 |
| η₂ (encryption noise) | 2 | 2 | 2 |
| d_u (ciphertext compression) | 10 | 10 | 11 |
| d_v (ciphertext compression) | 4 | 4 | 5 |
| Public key size | 800 B | 1,184 B | 1,568 B |
| Secret key size | 1,632 B | 2,400 B | 3,168 B |
| Ciphertext size | 768 B | 1,088 B | 1,568 B |
| Shared secret | 32 B | 32 B | 32 B |

## 11.4 Algorithm Description

### Key Generation (ML-KEM.KeyGen)

```
1. d ← Random(32)                     // Random seed
2. (ρ, σ) ← G(d)                      // Expand seed using hash G
3. Â ← SampleMatrix(ρ)                // Generate public matrix from ρ
4. s ← SampleNoise(σ, η₁, k)          // Sample secret vector (small coefficients)
5. e ← SampleNoise(σ', η₁, k)         // Sample error vector (small coefficients)
6. ŝ ← NTT(s)                         // Convert to NTT domain
7. ê ← NTT(e)                         // Convert to NTT domain
8. t̂ ← Â · ŝ + ê                     // Compute public key in NTT domain
9. pk ← Encode(t̂, ρ)                  // Public key = (t̂, ρ)
10. sk ← Encode(ŝ, pk, H(pk), z)      // Secret key includes pk hash and implicit reject value z
```

### Encapsulation (ML-KEM.Encaps)

```
1. m ← Random(32)                     // Random message
2. (K̄, r) ← G(m ‖ H(pk))            // Derive shared secret and randomness
3. Â ← SampleMatrix(ρ)                // Reconstruct public matrix
4. r_vec ← SampleNoise(r, η₁, k)     // Encryption randomness
5. e₁ ← SampleNoise(r, η₂, k)        // Encryption error 1
6. e₂ ← SampleNoise(r, η₂, 1)        // Encryption error 2
7. u ← NTT⁻¹(Âᵀ · NTT(r_vec)) + e₁  // First ciphertext component
8. v ← NTT⁻¹(t̂ᵀ · NTT(r_vec)) + e₂ + Decompress(m)  // Second component
9. c₁ ← Compress(u, d_u)              // Compress and encode
10. c₂ ← Compress(v, d_v)             // Compress and encode
11. ct ← (c₁, c₂)                     // Ciphertext
12. K ← KDF(K̄ ‖ H(ct))              // Final shared secret
```

### Decapsulation (ML-KEM.Decaps)

```
1. u ← Decompress(c₁, d_u)           // Decompress ciphertext
2. v ← Decompress(c₂, d_v)           // Decompress ciphertext
3. m' ← Compress(v - NTT⁻¹(ŝᵀ · NTT(u)), 1)  // Decrypt message
4. (K̄', r') ← G(m' ‖ H(pk))        // Re-derive randomness
5. Re-encrypt using r' to get ct'     // Verification step
6. if ct = ct':                        // Check re-encryption matches
7.    K ← KDF(K̄' ‖ H(ct))           // Success: output real shared secret
8. else:
9.    K ← KDF(z ‖ H(ct))             // Failure: output pseudorandom (implicit rejection)
```

## 11.5 Security Mechanisms

### IND-CCA2 via Fujisaki-Okamoto

The FO transform provides CCA2 security by:
1. **Derandomization:** Encryption randomness is derived from message and public key
2. **Re-encryption check:** Decapsulation verifies the ciphertext is well-formed
3. **Implicit rejection:** Invalid ciphertexts produce a random-looking key (not an error)

This prevents:
- Chosen-ciphertext attacks (adaptive queries to decapsulation oracle)
- Decryption oracle attacks in protocol contexts
- Bleichenbacher-style padding oracle attacks

### Implicit Rejection

Unlike classical schemes that return ⊥ (failure) for invalid ciphertexts, ML-KEM returns a pseudorandom value derived from the secret key. This:
- Prevents timing side-channels from distinguishing valid/invalid ciphertexts
- Eliminates the need for error-handling code paths that differ
- Provides defense in depth against implementation errors

### Compression

Ciphertext compression reduces sizes by discarding least-significant bits:
- Compress_d: Map coefficient x to ⌈2^d · x / q⌋ mod 2^d
- Decompress_d: Map y to ⌈q · y / 2^d⌋
- Introduces small rounding errors (bounded, accounted for in parameters)

## 11.6 Noise Distributions

### Centered Binomial Distribution

ML-KEM samples errors from the Centered Binomial Distribution CBD_η:
```
Sample 2η random bits (b₁, ..., b₂η)
Output: Σᵢ₌₁^η bᵢ - Σᵢ₌η₊₁^²η bᵢ
```

Properties:
- Symmetric around 0
- Range: [-η, η]
- Easy to sample (no Gaussian sampling needed)
- Sufficient for security (approximates discrete Gaussian for parameter selection)

### Why Not Gaussian?

Discrete Gaussians provide tighter security reductions but:
- Harder to sample in constant time
- More complex implementation
- Rejection sampling introduces timing variations
- The CBD is sufficient for ML-KEM's security at chosen parameters

## 11.7 Implementation Guidance

### Constant-Time Requirements

ML-KEM MUST be implemented in constant time:
- No secret-dependent branching
- No secret-dependent memory access patterns
- The comparison in decapsulation (ct == ct') must be constant-time
- NTT butterfly operations must not leak via timing

### Random Number Generation

- Key generation requires 32 bytes of high-quality randomness
- Encapsulation requires 32 bytes of randomness
- Use NIST-approved DRBGs (e.g., CTR_DRBG, HMAC_DRBG)
- Seed from hardware entropy source

### Key Validation

Before using a received public key:
- Verify encoding is well-formed
- Check coefficients are in range [0, q-1]
- Verify the public key length matches expected size

### Serialization

ML-KEM uses specific byte encoding:
- Polynomial coefficients packed into bytes (12 bits per coefficient for NTT form)
- Compressed coefficients use d_u or d_v bits per coefficient
- Big-endian byte ordering within coefficient encoding

## 11.8 Performance Characteristics

### Operation Counts (Approximate)

| Operation | ML-KEM-512 | ML-KEM-768 | ML-KEM-1024 |
|-----------|-----------|-----------|------------|
| KeyGen | ~50 μs | ~80 μs | ~120 μs |
| Encaps | ~60 μs | ~100 μs | ~150 μs |
| Decaps | ~70 μs | ~110 μs | ~160 μs |

*Times on modern x86-64 with AVX2; embedded platforms will be significantly slower.*

### Comparison with Classical Key Exchange

| Metric | ML-KEM-768 | X25519 (ECDH) | RSA-2048 |
|--------|-----------|--------------|----------|
| Public key | 1,184 B | 32 B | 256 B |
| Ciphertext/shared | 1,088 B | 32 B | 256 B |
| Total bandwidth | 2,272 B | 64 B | 512 B |
| Speed | ~100 μs | ~50 μs | ~1 ms |

ML-KEM is computationally fast but uses significantly more bandwidth than classical alternatives.

## 11.9 Known Attacks and Security Margin

### Primal Attack (BKZ + Sieving)

The primary attack strategy:
1. Construct a lattice from the MLWE instance
2. Apply BKZ with large block size to find short vectors
3. The short vector reveals the secret

For ML-KEM-768: Estimated attack cost > 2^180 classical, > 2^160 quantum.

### Dual Attack

An alternative approach:
1. Find a short vector in the dual lattice
2. Use it to distinguish LWE from random

Generally slightly less effective than the primal attack for ML-KEM parameters.

### Algebraic Attacks

Attacks exploiting the ring structure:
- No practical exploitation of the ring/module structure known
- Module-LWE with k ≥ 2 provides additional security margin over Ring-LWE

### Security Categories Achieved

| Parameter Set | NIST Level | Best Classical Attack | Best Quantum Attack |
|--------------|-----------|---------------------|-------------------|
| ML-KEM-512 | 1 | ~2^145 | ~2^125 |
| ML-KEM-768 | 3 | ~2^200 | ~2^175 |
| ML-KEM-1024 | 5 | ~2^265 | ~2^230 |

## 11.10 Deployment Considerations

### Protocol Integration

ML-KEM is designed for drop-in use in key exchange protocols:
- **TLS 1.3:** Hybrid key exchange combining ML-KEM with X25519
- **IKEv2/IPsec:** Post-quantum key exchange extensions
- **SSH:** Post-quantum key exchange methods
- **Signal:** PQXDH protocol using ML-KEM-1024

### Hybrid Mode

During transition, deploy ML-KEM in hybrid mode:
```
Shared_Secret = KDF(ML-KEM_Secret ‖ ECDH_Secret)
```
- Provides security if either algorithm remains unbroken
- Larger bandwidth but maximum security confidence
- Recommended by NIST, BSI, ANSSI during transition period

### Key Reuse

ML-KEM supports key reuse (same public key for multiple encapsulations):
- Safe due to IND-CCA2 security
- Important for ephemeral key exchange in TLS (one key pair per connection)
- Also safe for semi-static keys (e.g., in Signal's X3DH)

## 11.11 Key Takeaways

- ML-KEM (FIPS 203) is the primary post-quantum key encapsulation standard
- Based on Module-LWE with efficient NTT-based arithmetic
- Three security levels: ML-KEM-512/768/1024
- Fast operations (~100 μs) with moderate bandwidth overhead (~2 KB total)
- IND-CCA2 secure via Fujisaki-Okamoto transform with implicit rejection
- Must be implemented in constant time
- Deploy in hybrid mode (with ECDH) during transition
- Well-suited for TLS, VPN, SSH, and messaging protocols

---

*Next: [Chapter 12 — FIPS 204: ML-DSA](./12-fips-204-ml-dsa.md)*
