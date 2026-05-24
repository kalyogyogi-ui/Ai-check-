# Chapter 16: Implementation Considerations and Side-Channel Resistance

## 16.1 The Implementation Gap

A cryptographic algorithm can be mathematically perfect yet completely insecure in practice due to implementation flaws. Post-quantum algorithms introduce new implementation challenges that differ from classical cryptography:

- **Larger state:** More memory required for keys and intermediate values
- **New operations:** NTT, polynomial arithmetic, rejection sampling
- **Different attack surfaces:** Timing from rejection loops, power from polynomial operations
- **Platform diversity:** PQC must work on everything from HSMs to microcontrollers

## 16.2 Constant-Time Programming

### Why Constant-Time Matters

Modern processors have numerous mechanisms that can leak secrets through timing:
- **Branch prediction:** Different execution time for taken/not-taken branches
- **Cache lines:** Memory access patterns observable through cache timing
- **Variable-time instructions:** Division, certain multiplication on some architectures
- **Speculative execution:** Transient execution may leak through microarchitectural state

### Principles of Constant-Time Code

1. **No secret-dependent branches:**
```c
// BAD: branches on secret value
if (secret_bit) { result = a; } else { result = b; }

// GOOD: constant-time conditional select
result = ct_select(a, b, secret_bit);
// Implemented as: result = (a & mask) | (b & ~mask);
```

2. **No secret-dependent memory access:**
```c
// BAD: table lookup indexed by secret
result = table[secret_index];

// GOOD: scan entire table (constant access pattern)
result = ct_lookup(table, table_size, secret_index);
```

3. **No variable-time arithmetic:**
```c
// BAD on some platforms: division by secret
result = a / secret_divisor;

// GOOD: use only constant-time operations (+, -, *, &, |, ^, shifts)
```

### ML-KEM Specific Requirements

- **Comparison in decapsulation:** `ct == ct_recomputed` must not short-circuit
- **NTT butterfly operations:** Modular reduction must be constant-time
- **Polynomial coefficient operations:** No branching on coefficient values
- **Compression/decompression:** Rounding operations must be uniform
- **Noise sampling:** CBD sampling must not depend on sampled values

### ML-DSA Specific Requirements

- **Rejection sampling loop:** The fact of rejection can leak (loop count is public), but rejected values must not persist in observable state
- **Polynomial norm checking:** ‖z‖∞ comparison must be constant-time
- **Hint computation:** Operations on secret s₂ must be protected
- **Challenge sampling:** SampleInBall must not reveal internal state

### SLH-DSA Specific Requirements

- **WOTS+ chain computation:** Must compute full chains regardless of digit values
- **FORS leaf access:** No secret-dependent memory access patterns
- **Tree traversal:** Authentication path computation must be uniform

## 16.3 Side-Channel Attacks

### Timing Attacks

**Threat:** Measure execution time to infer secret-dependent computations.

**PQC-specific concerns:**
- ML-DSA rejection sampling: Number of iterations (public but intermediate state must be cleared)
- FN-DSA Gaussian sampling: Floating-point operations may have data-dependent timing
- Polynomial reduction: Some modular reduction implementations have variable timing

**Mitigation:** Constant-time implementation, as described above.

### Power Analysis

**Simple Power Analysis (SPA):** Single execution trace reveals operations.
- Distinguish between different polynomial operations
- Identify rejection loop iterations
- Observe NTT butterfly patterns

**Differential Power Analysis (DPA):** Statistical analysis over many executions.
- Correlate power consumption with hypothesized intermediate values
- Target NTT computations where secret coefficients are processed
- Exploit leakage from polynomial multiplication

**Mitigation:**
- Masking (randomize intermediate values)
- Hiding (add random delays, shuffle operations)
- Balanced logic implementations

### Electromagnetic Emanation

Similar to power analysis but using EM probes:
- Can target specific chip regions
- More spatial resolution than power analysis
- Same mitigations as power analysis (masking, hiding)

### Fault Injection

**Voltage/clock glitching:** Cause computation errors to leak secrets.

**PQC-specific fault attacks:**
- **Skip rejection in ML-DSA:** Force output of signature that leaks s₁
- **Corrupt NTT computation:** Produce malformed output revealing key material
- **Fault WOTS+ chains:** Reveal intermediate chain values
- **Skip re-encryption check in ML-KEM:** Accept invalid ciphertexts, enable oracle attacks

**Mitigation:**
- Redundant computation (compute twice, compare)
- Signature verification before output
- Algorithm-level countermeasures (checksums, error detection)
- Hardware countermeasures (voltage monitors, light sensors)

### Cache-Timing Attacks

**Flush+Reload, Prime+Probe:** Observe which cache lines are accessed.

**PQC-specific concerns:**
- Table lookups in NTT (twiddle factors)
- Polynomial coefficient storage patterns
- FORS tree leaf access in SLH-DSA

**Mitigation:**
- Avoid lookup tables indexed by secrets
- Use bitwise operations instead of table lookups
- Access all cache lines regardless of actual need

## 16.4 Masking Countermeasures

### Boolean Masking

Split each secret value into random shares:
```
x = x₁ ⊕ x₂ ⊕ ... ⊕ xₙ
```

Operations are performed on shares without recombining:
- XOR: (a₁⊕b₁, a₂⊕b₂) — trivial
- AND: Requires interaction between shares (expensive)
- Addition: Requires secure conversion between arithmetic and Boolean masks

### Arithmetic Masking

For operations in Z_q (like ML-KEM/ML-DSA):
```
x = x₁ + x₂ + ... + xₙ (mod q)
```

- Addition: (a₁+b₁, a₂+b₂) — trivial
- Multiplication: Requires special protocols (ISW-style)
- NTT: Compatible with arithmetic masking (linear operation)

### Masking the NTT

The NTT is a linear operation over Z_q:
```
NTT(x₁ + x₂) = NTT(x₁) + NTT(x₂)
```

This means:
- NTT of masked value = NTT of shares separately
- Multiplication in NTT domain requires secure protocol
- Inverse NTT also preserves masking

### Masking Cost

| Order | Protection Against | Performance Overhead |
|-------|-------------------|---------------------|
| 1st order (2 shares) | SPA, 1st-order DPA | 2-4x |
| 2nd order (3 shares) | Up to 2nd-order DPA | 5-10x |
| Higher order | Higher-order DPA | Rapidly increasing |

For most applications, 1st-order masking provides adequate protection against DPA.

## 16.5 Platform-Specific Considerations

### x86-64 (Servers, Desktops)

**Available acceleration:**
- AVX2/AVX-512 for parallel polynomial operations
- AES-NI for pseudo-random generation (if using AES-based PRF)
- SHA-NI for hash-based operations (SLH-DSA)
- VPCLMULQDQ for polynomial multiplication

**Best practices:**
- Use AVX2 for NTT (4 parallel butterflies)
- Vectorize coefficient comparison for rejection checks
- Use SIMD for parallel hash computation in tree structures

### ARM (Mobile, Embedded)

**Available acceleration:**
- NEON SIMD for parallel operations
- Crypto extensions (SHA-256, AES) for hash operations
- SVE/SVE2 on newer processors for wider parallelism

**Considerations:**
- More limited SIMD width (128-bit NEON vs. 256-bit AVX2)
- Power constraints may limit clock speeds
- ARM Cortex-M (no SIMD) requires different optimization strategies

### Microcontrollers (IoT, Embedded)

**ARM Cortex-M4 (common PQC target):**
- 32-bit operations, no SIMD
- Limited RAM (64-256 KB typical)
- ML-KEM-512: ~30 KB RAM during operation
- ML-DSA-44: ~50 KB RAM during signing
- Clock speeds: 80-168 MHz

**Optimization strategies:**
- Stack-based computation (minimize heap)
- Streaming NTT (compute in-place)
- Lazy reduction (batch modular reductions)
- Memory-optimized signature generation

### Hardware Security Modules (HSMs)

**Requirements:**
- FIPS 140-3 validation
- Physical tamper resistance
- Side-channel countermeasures mandatory
- Key generation and storage within module

**PQC HSM challenges:**
- Larger key storage requirements
- More complex algorithms increase validation effort
- NTT hardware acceleration beneficial
- Side-channel testing for new operations

### FPGA/ASIC Acceleration

**Advantages of hardware implementation:**
- Dedicated NTT engines (pipelined, parallel)
- Constant-time by design (fixed datapath)
- Hash function acceleration co-located
- Suitable for high-throughput applications (network equipment)

**Common accelerated components:**
- NTT/INTT units
- Polynomial multiplication
- SHA-256/SHAKE-256 engines
- Random number generation

## 16.6 Random Number Generation

### Requirements

PQC algorithms require high-quality randomness for:
- Key generation (entropy source for seed)
- Encapsulation (ML-KEM randomness)
- Hedged signing (ML-DSA fresh randomness)

### Entropy Sources

- **Hardware RNG:** Intel RDRAND/RDSEED, ARM TRNG
- **OS entropy:** /dev/urandom (Linux), CryptGenRandom (Windows)
- **Physical entropy:** Ring oscillators, metastable circuits (embedded)

### DRBG (Deterministic Random Bit Generator)

After seeding from entropy:
- NIST SP 800-90A approved DRBGs: CTR_DRBG, HMAC_DRBG, Hash_DRBG
- Reseeding requirements: Periodic or after generating threshold amount
- Prediction resistance: Fresh entropy mixed in for each request

### PQC-Specific Considerations

- ML-KEM requires 32 bytes of randomness per encapsulation
- ML-DSA hedged mode requires randomness per signature
- SLH-DSA deterministic mode: Randomness only at key generation
- Poor randomness in ML-KEM could enable complete key recovery

## 16.7 Testing and Validation

### Known Answer Tests (KATs)

NIST provides KAT vectors for all standardized algorithms:
- Fixed random seed → deterministic key pair
- Fixed randomness + message → deterministic signature/ciphertext
- Essential for verifying correct implementation

### Algorithm Validation Program (CAVP/ACVP)

NIST's Automated Cryptographic Validation Protocol:
- Automated testing infrastructure
- Tests for various parameter sets
- Verifies correctness across many test vectors
- Required for FIPS 140-3 validation

### Interoperability Testing

Implementations must interoperate:
- Keys generated by one implementation work in another
- Ciphertexts/signatures cross-validate
- Different platforms produce consistent results
- Test across: C, Rust, Java, Go, Python implementations

### Side-Channel Testing

- **Test Vector Leakage Assessment (TVLA):** Statistical test for first-order leakage
- **t-test analysis:** Compare power traces for different inputs
- **Correlation analysis:** Check for input-dependent power patterns
- **Tools:** ChipWhisperer, Langer, Riscure Inspector

## 16.8 Common Implementation Pitfalls

### Mistake 1: Non-Constant-Time Comparison

```c
// WRONG: memcmp returns early on mismatch
if (memcmp(ct, ct_recomputed, ct_len) == 0) { ... }

// RIGHT: constant-time comparison
if (ct_compare(ct, ct_recomputed, ct_len) == 0) { ... }
```

### Mistake 2: Leaking Rejection Count Details

```c
// WRONG: timing reveals which check failed
if (norm_check_1) { goto restart; }
if (norm_check_2) { goto restart; }

// RIGHT: combine all checks, clear state uniformly
int reject = norm_check_1 | norm_check_2 | hint_check;
if (reject) { secure_clear(state); goto restart; }
```

### Mistake 3: Failing to Clear Sensitive State

```c
// WRONG: rejected intermediate values remain on stack
while (rejected) { compute_signature(); check(); }

// RIGHT: explicitly clear all intermediate state on rejection
while (rejected) { compute_signature(); check(); secure_clear(intermediates); }
```

### Mistake 4: Incorrect Modular Reduction

```c
// WRONG: conditional subtraction leaks information
if (x >= q) x -= q;

// RIGHT: constant-time conditional subtraction
uint32_t mask = -(uint32_t)(x >= q);  // all 1s if true, 0 if false
x -= q & mask;
```

### Mistake 5: Insufficient Randomness

```c
// WRONG: using time-based seed
srand(time(NULL));
for (int i = 0; i < 32; i++) seed[i] = rand();

// RIGHT: cryptographic entropy source
getrandom(seed, 32, GRND_RANDOM);  // or equivalent
```

## 16.9 Reference Implementations and Libraries

### Production-Quality Libraries

| Library | Language | Algorithms | Side-Channel Protection |
|---------|----------|-----------|------------------------|
| liboqs | C | All NIST | Varies by implementation |
| PQClean | C | All NIST | Clean, portable, basic CT |
| pqcrypto (SUPERCOP) | C | Many | Reference quality |
| OpenSSL 3.5+ | C | ML-KEM, ML-DSA, SLH-DSA | Production quality |
| BouncyCastle | Java/C# | All NIST | Java limitations |
| CIRCL | Go | ML-KEM, ML-DSA | Go limitations |
| pqcrypto-rs | Rust | ML-KEM, ML-DSA | Memory safety benefits |
| wolfSSL | C | ML-KEM, ML-DSA | Embedded-focused |

### Choosing an Implementation

Consider:
1. Language/platform requirements
2. Side-channel protection level
3. FIPS validation status
4. Maintenance and update frequency
5. Performance optimization level
6. Memory constraints

## 16.10 Key Takeaways

- Constant-time implementation is mandatory for all PQC algorithms
- Side-channel attacks (timing, power, EM, fault) require specific countermeasures
- Masking provides DPA protection at 2-10x performance cost
- Different platforms (x86, ARM, MCU, FPGA) require different optimization strategies
- High-quality randomness is critical — especially for ML-KEM and hedged ML-DSA
- Testing must cover correctness (KATs), interoperability, and side-channel resistance
- Common pitfalls include non-constant comparisons, state leakage, and insufficient entropy
- Use established libraries rather than implementing from scratch

---

*Next: [Chapter 17 — Performance Analysis and Benchmarking](./17-performance.md)*
