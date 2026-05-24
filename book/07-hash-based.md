# Chapter 7: Hash-Based Signatures

## 7.1 The Appeal of Hash-Based Cryptography

Hash-based signature schemes hold a unique position in post-quantum cryptography: their security relies on the **minimal assumption** that a secure hash function exists. No algebraic structure, no lattice problems, no error-correcting codes — just the one-wayness and collision resistance of a hash function.

This minimal assumption provides:
- **Maximum confidence in quantum resistance:** Hash functions have only Grover's quadratic speedup as a known quantum attack
- **Conceptual simplicity:** The constructions are elegant and well-understood
- **Future-proofing:** If the hash function is replaced, the construction remains secure

The trade-off is performance — hash-based signatures are typically larger and slower than lattice-based alternatives.

## 7.2 One-Time Signatures: The Building Block

### Lamport Signatures (1979)

The simplest hash-based signature, proposed by Leslie Lamport:

**Key Generation:**
- For each bit i of the message hash (n bits total):
  - Generate two random values: (x_i^0, x_i^1)
  - Compute: (y_i^0, y_i^1) = (H(x_i^0), H(x_i^1))
- Secret key: All x values (2n random strings)
- Public key: All y values (2n hash values)

**Signing message m:**
- Compute hash h = H(m) with bits h₁, h₂, ..., hₙ
- Signature: (x_1^(h₁), x_2^(h₂), ..., x_n^(hₙ))

**Verification:**
- For each bit i, check that H(σᵢ) = y_i^(hᵢ)

**Properties:**
- Signature size: n × |hash output| (very large)
- One-time security: Each key pair signs exactly one message
- Conceptually simple but impractical alone

### Winternitz One-Time Signature (WOTS)

Winternitz signatures reduce size by signing multiple bits at once:

**Key Idea:** Instead of signing individual bits, sign base-w digits (w = 4, 16, or 256):
- Divide message hash into ℓ₁ = ⌈n/log₂(w)⌉ digits
- Add ℓ₂ checksum digits (prevents existential forgery)
- Total chains: ℓ = ℓ₁ + ℓ₂

**Hash Chains:**
- Secret key: Random values (x₁, ..., xℓ)
- Public key: End of chains (H^(w-1)(x₁), ..., H^(w-1)(xℓ))
- Signature: Intermediate chain values based on message digits

**WOTS+ (Used in SPHINCS+/SLH-DSA):**
- Uses randomized hashing with tweakable hash functions
- Adds bitmasks to prevent multi-target attacks
- Tighter security proof

**Trade-off Parameter w:**

| w | Signature Size | Signing Speed | Verification Speed |
|---|---------------|---------------|-------------------|
| 4 | Larger | Faster | Slower |
| 16 | Medium | Medium | Medium |
| 256 | Smaller | Slower | Faster |

Higher w means fewer chains (smaller signature) but longer chains (more hash computations).

## 7.3 Few-Time Signatures: HORST and FORS

### HORST (Hash to Obtain Random Subset Tree)

A variant where the signer reveals a subset of secret values determined by the message. Allows multiple signatures but has limited signing capacity.

### FORS (Forest of Random Subsets)

Used in SPHINCS+/SLH-DSA as the few-time signature component:

**Structure:**
- k trees, each with 2^a leaves
- Total secret: k × 2^a random values organized in k binary trees

**Signing:**
- Message hash determines one leaf from each of k trees
- Signature: k revealed leaves + k authentication paths (Merkle tree branches)

**Security:**
- Can sign multiple messages (few-time, not one-time)
- Security degrades with number of signatures (exponentially slow degradation)
- Parameterized for sufficient security given expected signature count

## 7.4 Merkle Trees: Managing Many Keys

The fundamental challenge: one-time/few-time signatures need fresh keys for each signature. Merkle trees (1979) solve this by managing many key pairs under a single public key.

### Construction

1. Generate N = 2^h one-time signature key pairs (leaves)
2. Build a binary hash tree:
   - Leaf nodes: Hash of each OTS public key
   - Internal nodes: Hash of concatenation of children
   - Root: The single public key for the entire tree
3. Height h determines capacity: 2^h signatures possible

### Authentication Path

To verify a signature:
1. Provide the OTS signature
2. Provide the OTS public key (leaf)
3. Provide the **authentication path**: h sibling nodes from leaf to root
4. Verifier recomputes the path from leaf to root and checks against the known root

Authentication path size: h × hash output size.

### Tree Traversal

Efficient tree management algorithms:
- **BDS traversal:** Computes authentication paths efficiently using O(h) storage
- **Fractal Merkle trees:** Reduce computation per signature
- **XMSS^MT (multi-tree):** Layers of smaller trees for very large signature counts

## 7.5 Stateful Hash-Based Signatures: XMSS and LMS

### XMSS (eXtended Merkle Signature Scheme)

XMSS (RFC 8391) is a standardized stateful hash-based signature:

**Structure:**
- Single Merkle tree of height h
- Uses WOTS+ for one-time signatures at leaves
- Total signatures: 2^h

**Parameters:**
- h = 10, 16, or 20 (1024, 65536, or 1048576 signatures)
- n = 32 bytes (hash output, security parameter)
- w = 16 (Winternitz parameter)

**Key sizes (h=10, n=32):**
- Public key: 64 bytes
- Secret key: ~132 bytes + state
- Signature: ~2,500 bytes

### XMSS^MT (Multi-Tree XMSS)

For applications needing more than 2^20 signatures:
- Stack d layers of XMSS trees
- Total height: h = h₁ + h₂ + ... + h_d
- Each tree at level i certifies the next level's trees
- Allows 2^(h₁+h₂+...+h_d) total signatures

### LMS (Leighton-Micali Signature)

LMS (RFC 8554) is another stateful hash-based signature standardized by NIST:
- Similar concept to XMSS with slightly different design choices
- Uses LM-OTS (Leighton-Micali One-Time Signature)
- HSS (Hierarchical Signature System) for multi-tree variants
- Approved by NIST in SP 800-208

### The State Management Problem

Stateful signatures have a critical requirement: **the signer must never reuse a one-time key.**

Reusing a WOTS key leaks the secret key. Therefore:
- The state (current leaf index) must be reliably persisted
- The state must survive crashes, backups, and cloning
- Multi-signer scenarios require coordination

This state management requirement makes stateful schemes unsuitable for most general-purpose applications but appropriate for:
- Firmware signing (controlled environment)
- Certificate authorities (limited, controlled signing)
- Code signing (infrequent, managed process)

## 7.6 Stateless Hash-Based Signatures: SPHINCS+ / SLH-DSA

### Motivation

To eliminate state management, SPHINCS+ (standardized as SLH-DSA in FIPS 205) uses a **hypertree** construction where the leaf selection is deterministic based on the message.

### Architecture

SLH-DSA combines three components:

1. **Hypertree:** A multi-layer Merkle tree structure
2. **WOTS+:** One-time signatures at internal tree levels
3. **FORS:** Few-time signatures at the leaves (directly signs messages)

### How It Works

1. **Index selection:** A pseudorandom function (PRF) derives a leaf index from the message and secret key. This is deterministic — the same message always uses the same leaf.

2. **FORS signature:** The message is signed using the FORS instance at the selected leaf.

3. **WOTS+ chain:** Each tree layer's root is signed by a WOTS+ instance in the layer above.

4. **Authentication paths:** Merkle authentication paths connect each level.

### Why Stateless Works

- Deterministic leaf selection means no state to track
- Same message → same signature (deterministic)
- FORS is a few-time signature: even if different messages map to the same leaf, security holds for a limited number of collisions
- The hypertree is large enough that collision probability is negligible

### Parameters (SLH-DSA)

| Parameter Set | Security Level | Signature Size | Public Key | Secret Key |
|--------------|---------------|---------------|------------|------------|
| SLH-DSA-128s | Level 1 | 7,856 bytes | 32 bytes | 64 bytes |
| SLH-DSA-128f | Level 1 | 17,088 bytes | 32 bytes | 64 bytes |
| SLH-DSA-192s | Level 3 | 16,224 bytes | 48 bytes | 96 bytes |
| SLH-DSA-192f | Level 3 | 35,664 bytes | 48 bytes | 96 bytes |
| SLH-DSA-256s | Level 5 | 29,792 bytes | 64 bytes | 128 bytes |
| SLH-DSA-256f | Level 5 | 49,856 bytes | 64 bytes | 128 bytes |

The "s" variants are "small" (smaller signatures, slower signing).  
The "f" variants are "fast" (faster signing, larger signatures).

### Performance

| Operation | SLH-DSA-128f | ML-DSA-44 | ECDSA P-256 |
|-----------|-------------|-----------|-------------|
| Key generation | ~1 ms | ~0.1 ms | ~0.1 ms |
| Signing | ~5 ms | ~0.3 ms | ~0.1 ms |
| Verification | ~1 ms | ~0.3 ms | ~0.2 ms |
| Signature size | 17,088 B | 2,420 B | 64 B |
| Public key | 32 B | 1,312 B | 64 B |

SLH-DSA is slower and produces larger signatures but has the strongest security guarantees.

## 7.7 Hash Function Requirements

Hash-based signatures require hash functions with specific properties:

### Standard Properties
- **Preimage resistance:** Given y, hard to find x with H(x) = y
- **Second preimage resistance:** Given x, hard to find x' ≠ x with H(x) = H(x')
- **Collision resistance:** Hard to find any x ≠ x' with H(x) = H(x')

### Additional Requirements for SLH-DSA
- **Pseudorandom function (PRF):** For deterministic index generation
- **Tweakable hash function:** Parameterized by an address that prevents multi-target attacks
- **Interleaved target subset resilience:** Security property for FORS

### Instantiations

SLH-DSA supports multiple hash function instantiations:
- **SHA-256 based:** Using SHA-256 and SHAKE-256 for different components
- **SHAKE-256 based:** Using SHAKE-256 throughout
- **Haraka (optional):** Short-input optimized hash function

## 7.8 Security Analysis

### Tight Security Reductions

Hash-based signatures have notably tight security reductions:
- Security loss is minimal (logarithmic in the number of signatures)
- If the hash function is secure, the scheme is secure
- No gap between the theoretical proof and concrete security

### Multi-Target Attacks

A concern for hash-based schemes: an attacker targeting many different public keys or signatures gets a "multi-target" advantage. Mitigated by:
- Using tweakable hash functions (different hash for each position)
- Including public seed in hash computations
- SPHINCS+ addresses specifically prevent multi-target attacks

### Fault Attacks

Hash-based signatures can be vulnerable to fault injection:
- Faulting during WOTS+ signing could leak secret chain values
- Faulting Merkle tree computation could expose internal nodes
- Mitigated by signature verification before output and redundant computation

## 7.9 Use Cases for Hash-Based Signatures

### Ideal Applications
- **Firmware/software signing:** State management feasible, long-term security critical
- **Certificate authority roots:** Limited signing, maximum security needed
- **Document notarization:** Infrequent signing, permanence important
- **Timestamping services:** Conservative security for long-lived timestamps

### Less Ideal Applications
- **TLS authentication:** Large signatures impact handshake latency
- **IoT devices:** Signature size and verification speed problematic
- **High-frequency signing:** Performance overhead significant
- **Bandwidth-constrained links:** Signature size dominates

### SLH-DSA vs. ML-DSA Selection

Choose SLH-DSA when:
- Maximum security confidence is paramount
- You want the most conservative quantum-resistant option
- Bandwidth and latency are not primary constraints
- You need a "hedge" against lattice cryptanalysis breakthroughs

Choose ML-DSA when:
- Performance is important
- Bandwidth is constrained
- Key and signature sizes matter
- You're comfortable with lattice-based security assumptions

## 7.10 Key Takeaways

- Hash-based signatures have the strongest, most conservative security guarantees in PQC
- Security relies only on hash function properties — minimal assumptions
- Stateful schemes (XMSS, LMS) are highly efficient but require careful state management
- Stateless SLH-DSA eliminates state management at the cost of larger signatures
- The WOTS+ and FORS building blocks are combined via hypertrees in SLH-DSA
- SLH-DSA is standardized as FIPS 205 and recommended for high-security applications
- Performance and size trade-offs make hash-based signatures complementary to lattice-based schemes

---

*Next: [Chapter 8 — Multivariate Polynomial Cryptography](./08-multivariate.md)*
