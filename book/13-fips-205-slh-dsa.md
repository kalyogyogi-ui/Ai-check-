# Chapter 13: FIPS 205 — SLH-DSA (Stateless Hash-Based Digital Signature Algorithm)

## 13.1 Overview

SLH-DSA (Stateless Hash-Based Digital Signature Algorithm), standardized as FIPS 205, is the conservative post-quantum signature standard. Its security relies solely on the properties of the underlying hash function — the most minimal and well-understood assumption in cryptography.

SLH-DSA serves as a "backstop" in the PQC portfolio: if lattice-based algorithms are ever found to have unexpected weaknesses, SLH-DSA provides an independent line of defense based on entirely different mathematics.

## 13.2 Architecture: The Hypertree

SLH-DSA uses a layered structure called a **hypertree** that combines three building blocks:

```
                    [Root = Public Key]
                          |
            Layer d-1: XMSS tree (WOTS+ leaves)
                    /    |    \
         Layer d-2: XMSS trees (WOTS+ leaves)
                /    |    \
            ...more layers...
                /    |    \
         Layer 0: XMSS trees (FORS leaves)
                /    |    \
              FORS instances (sign messages)
```

### Components

1. **FORS (Forest of Random Subsets):** Few-time signature at the bottom layer — directly signs message digests
2. **WOTS+ (Winternitz One-Time Signature Plus):** One-time signature used within each XMSS tree to authenticate subtrees
3. **XMSS trees:** Merkle trees that authenticate collections of WOTS+ or FORS instances

### How They Compose

- The **message** is signed by a FORS instance at the bottom
- The FORS public key is authenticated by a WOTS+ signature in the bottom XMSS tree
- Each XMSS tree root is authenticated by a WOTS+ signature in the layer above
- The top XMSS tree's root is the permanent **public key**

## 13.3 Parameter Sets

SLH-DSA offers 12 parameter sets (6 hash-function instantiations × 2 optimization targets):

### SHA-256 Based

| Parameter Set | Level | Signature | PK | SK | Sign Time |
|--------------|-------|-----------|----|----|-----------|
| SLH-DSA-SHA2-128s | 1 | 7,856 B | 32 B | 64 B | ~60 ms |
| SLH-DSA-SHA2-128f | 1 | 17,088 B | 32 B | 64 B | ~5 ms |
| SLH-DSA-SHA2-192s | 3 | 16,224 B | 48 B | 96 B | ~120 ms |
| SLH-DSA-SHA2-192f | 3 | 35,664 B | 48 B | 96 B | ~10 ms |
| SLH-DSA-SHA2-256s | 5 | 29,792 B | 64 B | 128 B | ~250 ms |
| SLH-DSA-SHA2-256f | 5 | 49,856 B | 64 B | 128 B | ~20 ms |

### SHAKE-256 Based

| Parameter Set | Level | Signature | PK | SK | Sign Time |
|--------------|-------|-----------|----|----|-----------|
| SLH-DSA-SHAKE-128s | 1 | 7,856 B | 32 B | 64 B | ~80 ms |
| SLH-DSA-SHAKE-128f | 1 | 17,088 B | 32 B | 64 B | ~7 ms |
| SLH-DSA-SHAKE-192s | 3 | 16,224 B | 48 B | 96 B | ~160 ms |
| SLH-DSA-SHAKE-192f | 3 | 35,664 B | 48 B | 96 B | ~13 ms |
| SLH-DSA-SHAKE-256s | 5 | 29,792 B | 64 B | 128 B | ~350 ms |
| SLH-DSA-SHAKE-256f | 5 | 49,856 B | 64 B | 128 B | ~25 ms |

**"s" variants:** Optimized for small signatures (fewer, taller trees → smaller but slower)  
**"f" variants:** Optimized for fast signing (more, shorter trees → faster but larger signatures)

## 13.4 WOTS+ in Detail

### Construction

WOTS+ (Winternitz One-Time Signature Plus) is the fundamental one-time signature:

**Parameters:**
- n: Security parameter (hash output length in bytes)
- w: Winternitz parameter (typically 16)
- ℓ₁ = ⌈8n/log₂(w)⌉ (message chains)
- ℓ₂ = ⌊log₂(ℓ₁(w-1))/log₂(w)⌋ + 1 (checksum chains)
- ℓ = ℓ₁ + ℓ₂ (total chains)

**Hash Chains:**
Each chain is a sequence of w hash applications with different tweaks:
```
chain(x, start, steps, ADRS) = H(ADRS_steps || H(ADRS_{steps-1} || ... H(ADRS_start || x)...))
```

**Key Generation:**
- Secret key: ℓ random n-byte values (sk₁, ..., skℓ) — chain starting points
- Public key: ℓ n-byte values — chain endpoints: pkᵢ = chain(skᵢ, 0, w-1)
- Compressed public key: single hash of all endpoints

**Signing digit dᵢ ∈ {0, ..., w-1}:**
- σᵢ = chain(skᵢ, 0, dᵢ)

**Verification:**
- Compute chain(σᵢ, dᵢ, w-1-dᵢ) for each i
- Check that result matches public key

### The Checksum

Without a checksum, an attacker could trivially forge by extending chains (increasing digits). The checksum ensures that increasing any message digit forces decreasing a checksum digit, preventing forgery.

```
checksum = Σᵢ (w - 1 - mᵢ)
```

### Security

WOTS+ is existentially unforgeable for a **single** message. Using the same key to sign two different messages may leak enough chain values to enable forgery.

## 13.5 FORS in Detail

### Construction

FORS (Forest of Random Subsets) is a few-time signature:

**Parameters:**
- k: Number of trees
- a: Tree height (each tree has 2^a leaves)
- n: Hash output length

**Key Generation:**
- Secret key: k × 2^a random n-byte values (leaves of k binary trees)
- Public key: Hash of k tree roots

**Signing:**
1. Derive k indices from the message hash: i₁, ..., iₖ where iⱼ ∈ {0, ..., 2^a - 1}
2. For each tree j: Reveal leaf number iⱼ and its authentication path (a sibling hashes)
3. Signature: k leaves + k authentication paths

**Verification:**
1. For each tree j: Reconstruct root from revealed leaf + authentication path
2. Hash all k roots and compare with public key

### Few-Time Security

FORS is secure for signing a limited number of messages:
- Each signature reveals one leaf per tree
- After signing B messages, B leaves per tree are revealed
- Forgery requires guessing all k unrevealed positions
- Security: approximately (1 - B/2^a)^k per forgery attempt

In SLH-DSA, the hypertree structure limits each FORS instance to a manageable number of uses.

## 13.6 The Hypertree Structure

### Index Generation

The critical innovation making SLH-DSA stateless:
1. Compute idx = PRF(SK.seed, message) — deterministic pseudo-random index
2. Use idx to select which FORS instance and which path through the hypertree

Because the index is deterministic (same message → same index), no state tracking is needed.

### Tree Addressing

SLH-DSA uses an **ADRS (address)** structure to uniquely identify every hash invocation:
- Layer address: Which hypertree level
- Tree address: Which tree within that level
- Type: WOTS+, FORS, or tree hash
- Chain/leaf/height indices within the tree

This addressing prevents multi-target attacks and ensures domain separation.

### Signature Structure

A complete SLH-DSA signature contains:
```
σ = (idx, FORS signature, HT signature)
```

Where HT signature is:
```
HT_sig = (WOTS+_sig₀, AUTH₀, WOTS+_sig₁, AUTH₁, ..., WOTS+_sig_{d-1}, AUTH_{d-1})
```

Each layer contributes one WOTS+ signature and one Merkle authentication path.

## 13.7 Hash Function Instantiations

### SHA-256 Based

- Uses SHA-256 for the tweakable hash function
- Uses SHA-256 for PRF and message hashing
- Benefits from hardware SHA-256 acceleration (Intel SHA-NI, ARM Crypto Extensions)
- More widely deployed hardware support

### SHAKE-256 Based

- Uses SHAKE-256 (SHA-3 family) for all hash operations
- Simpler: single hash function for everything
- Benefits from Keccak hardware support where available
- Potentially more resistant to length-extension-like issues

### Security of Hash Instantiations

Both instantiations provide equivalent security levels. The choice depends on:
- Available hardware acceleration
- Existing infrastructure (SHA-2 vs SHA-3 support)
- Regulatory requirements (some may mandate specific hash families)

## 13.8 Security Analysis

### Minimal Assumptions

SLH-DSA requires only:
1. **Second-preimage resistance** of the hash function
2. **PRF security** of the pseudorandom function
3. **Interleaved target subset resilience** (implied by random oracle model for the hash)

No lattice hardness, no number-theoretic assumptions, no algebraic structure.

### Quantum Security

- Grover's algorithm halves the hash function security: n-byte hash → n/2 bytes quantum security
- Parameters are chosen to maintain target security level even after Grover's speedup
- BHT algorithm for multi-target attacks is accounted for in parameter selection

### Multi-Target Attacks

The tweakable hash function construction prevents multi-target attacks:
- Each hash invocation uses a unique address (ADRS)
- Attacker cannot combine effort across different positions
- Equivalent to independent hash functions at each position

### Fault Attack Resistance

SLH-DSA can verify its own signatures before outputting:
- Compute signature, then verify it
- If verification fails (due to fault injection), abort
- This provides protection against faults that could leak the secret key

## 13.9 Performance Optimization

### Parallelism

SLH-DSA has significant parallelism opportunities:
- FORS trees are independent: k trees can be computed in parallel
- Merkle tree leaves can be computed independently
- WOTS+ chains are partially parallelizable

### Hardware Acceleration

- SHA-256: Intel SHA-NI provides ~3-5x speedup
- SHAKE-256: Some platforms have Keccak accelerators
- Tree computations: SIMD (AVX2/AVX-512) for parallel hashing

### Verification Optimization

Verification is typically 5-10x faster than signing:
- Only recomputes one path through each tree (not entire tree)
- Authentication path verification is mostly sequential hashing
- Can be further optimized with precomputation of public key data

## 13.10 Comparison: "s" vs. "f" Variants

The choice between small and fast variants involves:

| Aspect | "s" (small) | "f" (fast) |
|--------|------------|-----------|
| Signature size | ~7.8 KB (L1) | ~17 KB (L1) |
| Signing time | ~60 ms | ~5 ms |
| Verification time | ~3 ms | ~1 ms |
| Hypertree structure | Fewer, taller trees | More, shorter trees |
| Best for | Bandwidth-limited | Latency-sensitive |

## 13.11 Use Cases

### When to Choose SLH-DSA

**Strong recommendations:**
- Certificate Authority root keys (maximum security, infrequent signing)
- Long-term document signing (decades of verifiability)
- Firmware signing (security-critical, infrequent, can tolerate size)
- Regulatory compliance requiring hash-only security

**Acceptable choices:**
- General code signing
- Timestamping services
- Archival signatures

**Not recommended:**
- High-throughput TLS (large signatures slow handshakes)
- Constrained IoT devices (size and speed constraints)
- Real-time authentication (latency-sensitive)
- Bandwidth-limited protocols

### Combining with ML-DSA

Organizations can use both:
- ML-DSA for day-to-day operations (faster, smaller)
- SLH-DSA for root trust anchors (maximum security confidence)
- Dual signatures for critical documents (belt-and-suspenders)

## 13.12 Implementation Considerations

### Memory Requirements

Signing requires storing tree state during computation:
- Bottom tree computation: O(h × n) memory for authentication path
- WOTS+ signature: O(ℓ × n) memory
- Total: Several KB of working memory

### Deterministic Signing

SLH-DSA uses deterministic signing:
- Same message + same key → same signature
- No randomness needed during signing (only in key generation)
- Optional randomized variant adds fresh randomness (recommended for fault resistance)

### Key Storage

Secret keys are compact:
- SK = (SK.seed, SK.prf, PK.seed, PK.root)
- 128-bit: 64 bytes total
- 192-bit: 96 bytes total
- 256-bit: 128 bytes total

Public keys are also small:
- PK = (PK.seed, PK.root)
- 32/48/64 bytes depending on security level

## 13.13 Key Takeaways

- SLH-DSA (FIPS 205) provides hash-only security — the most conservative PQC signature
- Security relies solely on hash function properties (no algebraic assumptions)
- Hypertree structure combines FORS, WOTS+, and Merkle trees
- Stateless operation via deterministic index derivation from message
- Larger signatures (8-50 KB) and slower signing than ML-DSA
- Very small keys (32-128 bytes) — smallest of any PQC signature
- Serves as insurance against lattice cryptanalysis breakthroughs
- Ideal for high-security, low-frequency signing (CAs, firmware, documents)
- Two optimization targets: "s" for small signatures, "f" for fast signing

---

*Next: [Chapter 14 — Additional Candidates and Round 4 Algorithms](./14-additional-candidates.md)*
