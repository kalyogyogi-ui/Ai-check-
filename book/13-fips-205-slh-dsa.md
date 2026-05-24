# Chapter 13: FIPS 205 — SLH-DSA (Stateless Hash-Based Digital Signature Algorithm)

## 13.1 Overview

SLH-DSA (Stateless Hash-Based Digital Signature Algorithm), standardized as FIPS 205 by NIST in August 2024, represents the most conservative approach to post-quantum digital signatures. Derived from the SPHINCS+ submission, SLH-DSA occupies a unique position in the NIST post-quantum portfolio: its security rests solely on the well-understood properties of cryptographic hash functions — specifically second-preimage resistance and pseudorandomness — without relying on any algebraic or number-theoretic hardness assumptions.

This minimal assumption profile makes SLH-DSA fundamentally different from lattice-based schemes like ML-DSA or FN-DSA. If a breakthrough were to undermine the hardness of lattice problems (whether through improved classical algorithms, novel quantum algorithms beyond Shor's, or unexpected algebraic weaknesses in cyclotomic rings), SLH-DSA would remain completely unaffected. Its security would only be compromised if the underlying hash function itself were broken — a scenario that cryptographers consider extremely unlikely for well-designed functions like SHA-256 and SHAKE-256.

The trade-off for this extraordinary security conservatism is performance: SLH-DSA produces significantly larger signatures (7-50 KB versus 2-5 KB for ML-DSA) and requires more computation for signing (5-350 ms versus ~1 ms for ML-DSA). These penalties make SLH-DSA unsuitable as a general-purpose replacement for existing signature schemes in performance-sensitive contexts. Instead, it serves as the cryptographic "backstop" — the scheme of last resort for applications where absolute confidence in long-term security outweighs operational efficiency.

SLH-DSA achieves the remarkable property of being stateless despite being built from inherently stateful primitives. Classical hash-based signature schemes like XMSS and LMS require the signer to maintain a counter that tracks which one-time keys have been used; reusing a key compromises security catastrophically. SLH-DSA eliminates this state management requirement through a deterministic indexing mechanism that derives the signing path from the message itself, making deployment substantially simpler and eliminating an entire class of operational failure modes.

## 13.2 Architecture: The Hypertree

SLH-DSA employs a sophisticated layered structure called a hypertree that composes three distinct cryptographic building blocks into a single unified signature scheme. Understanding this architecture requires examining each component and how they interconnect.

### The Three Building Blocks

**1. FORS (Forest of Random Subsets):** A few-time signature scheme that occupies the bottom of the hypertree and directly signs message digests. FORS is specifically designed to tolerate a limited number of signatures under the same key without catastrophic security degradation, which is essential for the stateless construction.

**2. WOTS+ (Winternitz One-Time Signature Plus):** A one-time signature scheme that provides authentication within the Merkle tree layers. Each WOTS+ instance signs exactly one message (the root of a lower-level tree), and its one-time nature is guaranteed by the hypertree structure, which ensures each WOTS+ leaf is used at most once.

**3. XMSS trees (eXtended Merkle Signature Scheme trees):** Binary Merkle trees that authenticate collections of WOTS+ public keys (or FORS public keys at the bottom layer). Each XMSS tree has 2^h' leaves, where h' is the tree height for that layer, and its root serves as a compact commitment to all the public keys it contains.

### Hierarchical Composition

The hypertree stacks d layers of XMSS trees, creating a tree of trees:

```
                        [PK.root = Top XMSS Root]
                                  |
              Layer d-1:    XMSS Tree (height h')
                           /    |    \
              Leaves:   WOTS+₁  WOTS+₂ ... WOTS+_{2^h'}
                          |       |            |
              Layer d-2:  XMSS   XMSS   ...  XMSS
                           /|\    /|\          /|\
                          ...    ...          ...
                           |      |            |
              Layer 1:   XMSS   XMSS   ...  XMSS
                          /|\    /|\          /|\
              Leaves:   WOTS+  WOTS+  ...  WOTS+
                          |      |            |
              Layer 0:   XMSS   XMSS   ...  XMSS
                          /|\    /|\          /|\
              Leaves:   FORS   FORS   ...  FORS
                          |      |            |
                       [Sign messages here]
```

The total tree height is h = d × h', meaning the system can address 2^h distinct FORS instances. Each FORS instance can safely sign a limited number of messages (determined by its parameters), and the stateless construction ensures that each message is deterministically mapped to a specific FORS instance.

### How Signing Traverses the Hypertree

When a message is signed, the signature contains a complete authentication chain from the FORS instance at the bottom up through every layer to the root:

1. **Bottom:** A FORS signature authenticating the message digest
2. **Layer 0:** A WOTS+ signature authenticating the FORS public key, plus a Merkle authentication path from the WOTS+ leaf to the Layer 0 XMSS root
3. **Layer 1:** A WOTS+ signature authenticating the Layer 0 root, plus a Merkle authentication path to the Layer 1 XMSS root
4. **...continuing through all layers...**
5. **Layer d-1:** A WOTS+ signature authenticating the Layer d-2 root, plus a Merkle authentication path to the top-level root (which equals the public key)

Verification reverses this chain: starting from the FORS signature, it reconstructs each tree root and verifies the WOTS+ signatures linking layers together, ultimately checking that the chain terminates at the known public key.

## 13.3 Parameter Sets

SLH-DSA offers twelve parameter sets, providing flexibility across three security levels, two hash function families, and two optimization targets:

### SHA-256 Based Parameter Sets

| Parameter Set | NIST Level | n | h | d | h' | a | k | Sig Size | PK | SK |
|--------------|-----------|---|---|---|----|----|---|----------|----|----|
| SLH-DSA-SHA2-128s | 1 | 16 | 63 | 7 | 9 | 12 | 14 | 7,856 B | 32 B | 64 B |
| SLH-DSA-SHA2-128f | 1 | 16 | 66 | 22 | 3 | 6 | 33 | 17,088 B | 32 B | 64 B |
| SLH-DSA-SHA2-192s | 3 | 24 | 63 | 7 | 9 | 14 | 17 | 16,224 B | 48 B | 96 B |
| SLH-DSA-SHA2-192f | 3 | 24 | 66 | 22 | 3 | 8 | 33 | 35,664 B | 48 B | 96 B |
| SLH-DSA-SHA2-256s | 5 | 32 | 64 | 8 | 8 | 14 | 22 | 29,792 B | 64 B | 128 B |
| SLH-DSA-SHA2-256f | 5 | 32 | 68 | 17 | 4 | 9 | 35 | 49,856 B | 64 B | 128 B |

### SHAKE-256 Based Parameter Sets

| Parameter Set | NIST Level | n | h | d | h' | a | k | Sig Size | PK | SK |
|--------------|-----------|---|---|---|----|----|---|----------|----|----|
| SLH-DSA-SHAKE-128s | 1 | 16 | 63 | 7 | 9 | 12 | 14 | 7,856 B | 32 B | 64 B |
| SLH-DSA-SHAKE-128f | 1 | 16 | 66 | 22 | 3 | 6 | 33 | 17,088 B | 32 B | 64 B |
| SLH-DSA-SHAKE-192s | 3 | 24 | 63 | 7 | 9 | 14 | 17 | 16,224 B | 48 B | 96 B |
| SLH-DSA-SHAKE-192f | 3 | 24 | 66 | 22 | 3 | 8 | 33 | 35,664 B | 48 B | 96 B |
| SLH-DSA-SHAKE-256s | 5 | 32 | 64 | 8 | 8 | 14 | 22 | 29,792 B | 64 B | 128 B |
| SLH-DSA-SHAKE-256f | 5 | 32 | 68 | 17 | 4 | 9 | 35 | 49,856 B | 64 B | 128 B |

### Understanding the Parameter Structure

**n (security parameter):** The hash output length in bytes. Determines the fundamental security level: n=16 for 128-bit, n=24 for 192-bit, n=32 for 256-bit post-quantum security.

**h (total tree height):** The total number of levels in the hypertree, determining how many FORS instances can be addressed. Larger h means more FORS instances available, reducing the probability that any single instance is overloaded.

**d (hypertree layers):** The number of XMSS tree layers. Each layer has height h' = h/d. More layers mean shorter individual trees (faster to traverse) but more WOTS+ signatures in the final signature (larger output).

**h' (per-layer height):** Height of each individual XMSS tree within a layer, computed as h/d. Determines how many leaves (WOTS+ or FORS instances) each tree authenticates.

**a (FORS tree height):** Each of the k FORS trees has 2^a leaves. Larger a means larger FORS key space, improving the few-time security.

**k (FORS trees):** Number of independent trees in each FORS instance. Together with a, determines the FORS security level: forging requires guessing k correct leaves simultaneously.

### The "s" vs "f" Design Choice

The two optimization targets represent fundamentally different tree geometries:

**"s" (small signature) variants:** Use fewer hypertree layers (d=7 or 8), meaning each layer is taller (h'=8 or 9). Taller trees have more leaves per WOTS+ authentication path, but fewer layers means fewer WOTS+ signatures total. The FORS parameters are also chosen with larger a (deeper trees), meaning each FORS signature reveals less of the secret space. The result: smaller total signatures but slower signing (more computation to build the taller trees).

**"f" (fast signing) variants:** Use many more hypertree layers (d=17 or 22), making each layer very short (h'=3 or 4). Short trees are quick to compute, and the FORS uses smaller a with more trees k, optimized for speed rather than size. The result: much faster signing but significantly larger signatures.

The size ratio between "s" and "f" variants is approximately 2-2.5x, while the speed ratio is approximately 10-15x. This makes the choice highly application-dependent.

## 13.4 WOTS+ in Detail

### Construction and Rationale

WOTS+ (Winternitz One-Time Signature Plus) is a hash-based one-time signature scheme that forms the internal authentication mechanism of the hypertree. Its security relies solely on the second-preimage resistance of the hash function, making it perfectly aligned with SLH-DSA's minimal-assumption philosophy.

The core idea of Winternitz signatures is to trade signature size for computation: rather than using one hash chain per bit of the message (as in Lamport signatures), WOTS+ uses longer chains to encode multiple bits per chain, dramatically reducing the number of chains needed.

**Parameters:**
- n: Hash output length (security parameter in bytes)
- w: Winternitz parameter, typically 16, controlling the time-space trade-off
- ℓ₁ = ⌈8n / log₂(w)⌉: Number of chains encoding the message (for n=16, w=16: ℓ₁ = 32)
- ℓ₂ = ⌊log₂(ℓ₁(w-1)) / log₂(w)⌋ + 1: Number of chains encoding the checksum (typically 3-4)
- ℓ = ℓ₁ + ℓ₂: Total number of hash chains

### Hash Chain Construction

Each hash chain in WOTS+ consists of w-1 iterated applications of a tweakable hash function. The "Plus" in WOTS+ refers to the use of random bitmasks (or equivalently, tweakable hash functions with unique addresses) at each step, which provides tighter security bounds than plain iterated hashing.

A single chain computation proceeds as:

```
chain(x, start, steps, ADRS):
    tmp ← x
    for i from start to start + steps - 1:
        ADRS.setHashAddress(i)
        tmp ← F(PK.seed, ADRS, tmp)
    return tmp
```

Here F is a tweakable hash function parameterized by a public seed and an address structure. The address uniquely identifies this particular hash invocation within the entire SLH-DSA scheme, ensuring that each hash call is effectively independent.

**Key generation** produces ℓ chains, each of length w-1:
- Secret key: ℓ random n-byte values (sk₀, sk₁, ..., sk_{ℓ-1}) — the chain starting points
- Public key: The ℓ chain endpoints: pk_i = chain(sk_i, 0, w-1, ADRS) for each i
- Compressed public key: A single n-byte hash of all ℓ endpoints, denoted WOTS_PK

### Signing Process

To sign an n-byte message M with WOTS+:

1. **Base-w encoding:** Convert M into ℓ₁ digits in base w: (m₀, m₁, ..., m_{ℓ₁-1}) where each m_i ∈ {0, 1, ..., w-1}
2. **Checksum computation:** C = Σᵢ (w - 1 - mᵢ), converted to ℓ₂ base-w digits: (c₀, c₁, ..., c_{ℓ₂-1})
3. **Concatenated message:** B = (m₀, ..., m_{ℓ₁-1}, c₀, ..., c_{ℓ₂-1}) — a total of ℓ digits
4. **Signature generation:** For each digit b_i in B: σᵢ = chain(sk_i, 0, b_i, ADRS)

The signature σ = (σ₀, σ₁, ..., σ_{ℓ-1}) consists of ℓ intermediate hash chain values, each n bytes long.

### Verification Process

Given message M and signature σ:

1. Re-encode M as base-w digits and compute the checksum (same as signing steps 1-3)
2. For each digit b_i: Extend the chain from the signature value to the endpoint:
   pk'_i = chain(σ_i, b_i, w-1-b_i, ADRS)
3. Compress all pk'_i values into a single hash and compare with the known public key

If the signature is valid, each σ_i is exactly b_i steps along the chain from sk_i, so extending by w-1-b_i more steps reaches pk_i. If any σ_i is incorrect, the chain endpoint will differ from the true pk_i with overwhelming probability.

### The Checksum Mechanism

The checksum is essential for security. Without it, an attacker who observes a signature (σ₀, ..., σ_{ℓ₁-1}) for message digits (m₀, ..., m_{ℓ₁-1}) could forge a signature for any message whose digits are component-wise greater than or equal to the original. This is because chain(σ_i, m_i, m'_i - m_i) = chain(sk_i, 0, m'_i) for any m'_i ≥ m_i — the attacker simply extends the chain further.

The checksum defeats this by ensuring that if any message digit increases, at least one checksum digit must decrease. Since decreasing a digit requires inverting hash function applications (finding preimages), which is computationally infeasible, the checksum makes forgery equivalent to breaking the hash function.

Formally: C = Σᵢ(w-1-mᵢ). If m_j increases by δ, the sum decreases by δ, meaning at least one checksum digit must decrease to compensate. Decreasing a checksum digit c_k to c'_k < c_k requires computing chain(sk_{ℓ₁+k}, 0, c'_k) from chain(sk_{ℓ₁+k}, 0, c_k), which is a preimage computation.

### Security Properties and Limitations

WOTS+ provides existential unforgeability for a **single** message signature. The security reduction is tight: forging a WOTS+ signature is exactly as hard as finding a second preimage of the tweakable hash function F. This is optimal — no hash-based one-time signature can be more secure than the underlying hash function.

The critical limitation is the one-time nature: signing two different messages with the same WOTS+ key reveals chain values at two different positions. An attacker can then extend from whichever revealed value is further along the chain, potentially forging signatures for messages whose digits are component-wise between the two signed messages. This is why the hypertree structure must guarantee that each WOTS+ key is used exactly once.

## 13.5 FORS in Detail

### Construction and Design Goals

FORS (Forest of Random Subsets) is a few-time signature scheme specifically designed for SLH-DSA. Unlike WOTS+ which can only sign one message, FORS can safely sign multiple messages under the same key (up to a parameter-dependent limit) with graceful security degradation. This few-time property is crucial: in the stateless SLH-DSA construction, the deterministic indexing may map multiple messages to the same FORS instance, so the bottom-layer scheme must tolerate reuse.

**Parameters:**
- k: Number of independent binary trees (typically 14-35 depending on the parameter set)
- a: Height of each tree (each tree has 2^a leaves, typically 6-14)
- n: Hash output length (security parameter)
- Total FORS key size: k × 2^a × n bytes of secret data

### Key Generation

A FORS key pair consists of:
- **Secret key:** k × 2^a random n-byte values, organized as k binary trees each with 2^a leaves. Each leaf value is a secret random string.
- **Public key:** Computed by hashing up each tree to obtain k root hashes, then hashing all k roots together into a single n-byte public key: PK_FORS = H(root₀ ‖ root₁ ‖ ... ‖ root_{k-1})

The tree structure is a standard binary Merkle tree: each internal node is the hash of its two children, and the root commits to all 2^a leaf values. This allows any individual leaf to be authenticated using an authentication path of a sibling hashes.

### Signing Process

To sign a message digest md (of length k·a bits) with FORS:

1. **Index extraction:** Partition md into k groups of a bits each. Each group defines an index i_j ∈ {0, ..., 2^a - 1} selecting one leaf from tree j.
2. **Leaf revelation:** For each tree j, reveal the secret leaf value at position i_j: val_j = SK_FORS[j][i_j]
3. **Authentication paths:** For each tree j, provide the Merkle authentication path from leaf i_j to the root of tree j (a sibling hashes per path)
4. **Signature:** σ_FORS = (val₀, auth₀, val₁, auth₁, ..., val_{k-1}, auth_{k-1})

The signature size is k × (n + a × n) = k × n × (1 + a) bytes.

### Verification Process

Given message digest md and FORS signature σ_FORS:

1. Extract the k indices from md (same as signing step 1)
2. For each tree j:
   a. Start with the revealed leaf value val_j
   b. Hash it to get the leaf node: leaf = H(ADRS, val_j)
   c. Use the authentication path auth_j to reconstruct the root of tree j
3. Hash all k reconstructed roots together: PK' = H(root'₀ ‖ ... ‖ root'_{k-1})
4. Compare PK' with the known FORS public key

### Few-Time Security Analysis

FORS security degrades gracefully with the number of signatures produced under the same key:

**After signing B messages with the same FORS key:**
- B leaves per tree have been revealed (not necessarily distinct — collisions are possible)
- The probability that a random target message has all k of its indices among the revealed leaves is approximately (B/2^a)^k
- An attacker's forgery success probability is bounded by: P_forge ≤ (B/2^a)^k

**Concrete example (SLH-DSA-SHA2-128s: k=14, a=12):**
- After B=1 signing: P_forge ≤ (1/4096)^14 ≈ 2^{-168} — overwhelmingly secure
- After B=100 signings: P_forge ≤ (100/4096)^14 ≈ 2^{-74} — still very secure
- After B=1000 signings: P_forge ≤ (1000/4096)^14 ≈ 2^{-28} — marginal

The hypertree structure with h=63 provides 2^63 distinct FORS instances. Even if an adversary can induce collisions in the index derivation (which requires breaking the PRF), the expected number of messages mapping to any single FORS instance grows only logarithmically with the number of signatures produced, keeping B well within safe bounds for any realistic workload.

### Information-Theoretic Perspective

Each FORS signature reveals exactly k leaf values out of a total of k × 2^a secrets. The information leaked is k × n bytes per signature. After B signatures, at most B × k distinct leaf values are known (less if there are index collisions). The remaining unleaked leaves form the basis of security: forging requires guessing the correct leaf value for at least one unrevealed position, which has probability 0 (the values are random and independent).

This is fundamentally different from WOTS+, where leaking intermediate chain values partially compromises security for related messages. FORS leakage is all-or-nothing per leaf: either a leaf is known (fully compromised for that position) or it is unknown (fully secure).

## 13.6 The Hypertree Structure

### Stateless Operation via Deterministic Indexing

The central innovation that makes SLH-DSA practical is its stateless design. Classical hash-based schemes (XMSS, LMS) maintain a counter that increments with each signature, ensuring each one-time key is never reused. This state management introduces operational challenges: the counter must be persisted reliably, synchronized across distributed signers, and never rolled back. Failure to maintain state correctly leads to catastrophic security failure.

SLH-DSA eliminates state entirely through deterministic index derivation:

```
SLH-DSA.Sign(SK, M):
1.  opt ← random or zeros (hedged vs deterministic)
2.  R ← PRF_msg(SK.prf, opt, M)          // Pseudorandom value bound to message
3.  digest ← H_msg(R, PK.seed, PK.root, M)  // Message digest
4.  idx ← digest[0..⌈h/8⌉]              // Extract tree/leaf index from digest
5.  [Sign using FORS instance at position idx]
6.  [Authenticate up through hypertree layers]
```

The index idx determines:
- Which FORS instance signs the message (bottom layer)
- Which path through each XMSS tree layer provides authentication
- Which WOTS+ key at each layer produces the connecting signature

Because idx is derived deterministically from (SK, M), the same message always maps to the same FORS instance. Different messages map to (pseudo)random positions in the 2^h address space with overwhelming probability (by the PRF security of the hash function). This guarantees that FORS instances are not overloaded unless many more than 2^h messages are signed, which is operationally infeasible for h=63-68.

### The ADRS (Address) Structure

Every hash function invocation in SLH-DSA receives a unique address that specifies its exact position within the overall structure. The ADRS is a 32-byte structured value containing:

- **Layer address (4 bytes):** Which hypertree layer (0 to d-1)
- **Tree address (12 bytes):** Which XMSS tree within that layer
- **Type (4 bytes):** What kind of operation:
  - 0: WOTS+ hash chain
  - 1: WOTS+ public key compression
  - 2: Hash tree (Merkle tree internal node)
  - 3: FORS tree
  - 4: FORS tree roots
  - 5: WOTS+ PRF (key generation)
  - 6: FORS PRF (key generation)
- **Type-specific fields (12 bytes):** Chain address, hash address, tree height, tree index, or key-pair address depending on the type

This addressing serves multiple critical purposes:

**Domain separation:** Every hash invocation has unique input even if the data being hashed happens to be identical. This prevents an attacker from transferring a successful attack at one position to another position.

**Multi-target attack prevention:** Without unique addresses, an attacker could search for preimages that are valid at any of the 2^h positions simultaneously, gaining a factor of 2^h speedup. The per-position addresses force the attacker to target each position independently.

**Parallel security:** The tweakable hash construction T(PK.seed, ADRS, M) with unique ADRS values makes each invocation behave as an independent random function, enabling tight security reductions.

### Complete Signature Structure

A full SLH-DSA signature contains the following components:

```
σ_SLH-DSA = (R, σ_FORS, σ_HT)
```

Where:
- **R** (n bytes): The randomization value used in message hashing
- **σ_FORS** (k(1+a)n bytes): The FORS signature on the message digest
- **σ_HT**: The hypertree signature authenticating the FORS public key up to the root

The hypertree signature σ_HT consists of d layers, each containing:
```
σ_HT = [(σ_WOTS₀, AUTH₀), (σ_WOTS₁, AUTH₁), ..., (σ_WOTS_{d-1}, AUTH_{d-1})]
```

Each (σ_WOTSᵢ, AUTHᵢ) pair contains:
- σ_WOTSᵢ: A WOTS+ signature (ℓ × n bytes) authenticating the lower layer's tree root
- AUTHᵢ: A Merkle authentication path (h' × n bytes) from the WOTS+ leaf to the layer's tree root

**Total signature size calculation:**
- R: n bytes
- FORS: k × (1 + a) × n bytes
- HT: d × (ℓ × n + h' × n) = d × (ℓ + h') × n bytes
- Total: n + k(1+a)n + d(ℓ+h')n bytes

For SLH-DSA-SHA2-128s: 16 + 14×13×16 + 7×(35+9)×16 = 16 + 2,912 + 4,928 = 7,856 bytes.

## 13.7 Hash Function Instantiations

### SHA-256 Based Construction

The SHA-256 instantiation uses the following hash function assignments:

- **Tweakable hash F(PK.seed, ADRS, M₁):** SHA-256 with compressed ADRS and PK.seed as part of the input. For n=16, the output is truncated to 16 bytes; for n=24 and n=32, full SHA-256 output or HMAC-based constructions are used.
- **Tweakable hash H(PK.seed, ADRS, M₁ ‖ M₂):** Same construction for 2n-byte inputs (used in Merkle tree nodes)
- **PRF(SK.seed, ADRS):** HMAC-SHA-256 keyed with SK.seed, message is the ADRS
- **PRF_msg(SK.prf, opt, M):** HMAC-SHA-256 for message-dependent randomness
- **H_msg(R, PK.seed, PK.root, M):** MGF1-SHA-256 (mask generation function) for variable-length message hashing

The SHA-256 instantiation benefits from ubiquitous hardware support:
- **Intel SHA-NI:** Dedicated SHA-256 instructions providing 3-5x speedup over software
- **ARM Crypto Extensions:** SHA-256 acceleration on modern ARM processors (Cortex-A53 and later)
- **Dedicated accelerators:** Many SoCs include hardware SHA-256 engines for full-speed operation

For the 128-bit security level (n=16), using truncated SHA-256 output introduces a subtlety: the internal state of SHA-256 is 256 bits, but only 128 bits are used. This is safe because finding a second preimage of the truncated function is still 2^128-hard (birthday attacks do not apply to second preimage resistance), though it requires careful analysis of multi-target scenarios.

### SHAKE-256 Based Construction

The SHAKE-256 instantiation uses the SHA-3 family's extendable output function for all operations:

- **Tweakable hash F and H:** SHAKE-256(PK.seed ‖ ADRS ‖ M) truncated to n bytes
- **PRF:** SHAKE-256(SK.seed ‖ ADRS) truncated to n bytes
- **PRF_msg:** SHAKE-256(SK.prf ‖ opt ‖ M) truncated to n bytes
- **H_msg:** SHAKE-256(R ‖ PK.seed ‖ PK.root ‖ M) with output length as needed

The SHAKE-256 instantiation offers several advantages:

**Simplicity:** A single primitive (Keccak/SHAKE-256) serves all roles. This simplifies implementation, reduces code size, and eliminates potential issues arising from interactions between different hash functions.

**Sponge construction benefits:** The Keccak sponge naturally supports variable-length output (no need for MGF1 or similar constructions), arbitrary-length input (no need for HMAC's key padding), and domain separation through suffix bits.

**No length-extension vulnerability:** Unlike SHA-256 (Merkle-Damgård construction), SHAKE-256 is not susceptible to length-extension attacks. While SLH-DSA's design already prevents exploitation of this property, the sponge construction provides an additional safety margin.

**Hardware considerations:** Keccak hardware accelerators are becoming more common (particularly in FPGA implementations and newer ASIC designs), though SHA-256 hardware support remains more ubiquitous as of 2024.

### Security Equivalence

Both instantiations target identical security levels. The choice between SHA-256 and SHAKE-256 should be based on practical considerations rather than security differences:

| Consideration | SHA-256 | SHAKE-256 |
|--------------|---------|-----------|
| Hardware acceleration availability | Very widespread | Growing |
| Software performance (without HW) | Comparable | Comparable |
| Software performance (with HW) | Faster (SHA-NI) | Depends on platform |
| Implementation complexity | Moderate (multiple constructions) | Lower (single primitive) |
| Existing infrastructure compatibility | Higher (SHA-2 deployed everywhere) | Lower (SHA-3 newer) |
| Regulatory preference | FIPS 180-4 (long-established) | FIPS 202 (newer) |
| Resistance to theoretical advances | Good | Good |

## 13.8 Security Analysis

### Minimal Cryptographic Assumptions

SLH-DSA's security proof requires only three properties from the underlying hash function:

**1. Second-preimage resistance (SPR) of the tweakable hash:** Given a random input x and address ADRS, it should be infeasible to find x' ≠ x such that F(PK.seed, ADRS, x) = F(PK.seed, ADRS, x'). This protects the Merkle tree structure (prevents replacing authenticated nodes) and the WOTS+ chains (prevents extending signatures).

**2. Pseudorandomness (PRF) of the keyed function:** Given a secret key SK.seed, the function PRF(SK.seed, ·) should be indistinguishable from a random function. This protects the secret key material: an attacker who doesn't know SK.seed cannot predict WOTS+ or FORS secret values.

**3. Interleaved target subset resilience (ITSR) / Undetectability:** A property ensuring that the tweakable hash function behaves "randomly enough" that multi-target attacks cannot be mounted efficiently. In the random oracle model, this is implied by the hash function behaving as an independent random function at each address.

These properties are strictly weaker than collision resistance. A hash function could have known collisions (violating collision resistance) while still satisfying SPR and PRF, and SLH-DSA would remain secure. This is remarkable: even SHA-1, whose collision resistance is broken, likely still satisfies the properties needed for SLH-DSA (though no one would recommend using it at this point for reasons of caution).

### Quantum Security Analysis

Quantum computers affect hash function security through Grover's algorithm, which provides a quadratic speedup for unstructured search:

**Single-target preimage/second-preimage:** Grover's algorithm finds a preimage of an n-byte hash in O(2^{4n}) queries instead of O(2^{8n}) classically. For n=16 (128-bit), quantum second-preimage resistance is ~2^{64}... but SLH-DSA parameters are set assuming the quantum threat, so n=16 provides 2^{128} classical / 2^{64} quantum security at the hash level, which matches NIST Level 1.

Wait — this requires clarification. NIST Level 1 is defined as "at least as hard to break as AES-128 against a quantum adversary." Grover's algorithm reduces AES-128's security to 2^{64} quantum queries, setting the bar. SLH-DSA-128s/f targets this level, meaning finding a second preimage of the 16-byte hash requires at least 2^{64} quantum hash evaluations (matching the Grover-on-AES-128 bound).

**Multi-target considerations:** The BHT (Brassard-Høyer-Tapp) algorithm can find one collision among 2^t targets in time O(2^{(n-t)/3}) quantumly. The ADRS mechanism in SLH-DSA prevents this: each hash position uses a unique address, so targets at different positions are effectively different functions, and multi-target speedups do not apply.

**Overall quantum security mapping:**
- SLH-DSA-128s/f: At least as hard as breaking AES-128 quantumly (NIST Level 1)
- SLH-DSA-192s/f: At least as hard as breaking AES-192 quantumly (NIST Level 3)
- SLH-DSA-256s/f: At least as hard as breaking AES-256 quantumly (NIST Level 5)

### Multi-Target Attack Prevention Through Addressing

Without the ADRS mechanism, SLH-DSA would be vulnerable to devastating multi-target attacks. Consider a hypertree with h=63 and d=7 layers: there are 2^63 FORS instances, each with k=14 trees of 2^12=4096 leaves. An attacker attempting to forge a signature for a chosen message needs to find the correct leaf values for 14 specific positions.

Without unique addressing, the attacker could simultaneously search for valid leaf values across all 2^63 × 14 × 4096 ≈ 2^{88} leaf positions in the entire tree, potentially finding one that matches a target in dramatically less time than attacking a single position.

The ADRS construction prevents this entirely: each leaf value is computed as PRF(SK.seed, ADRS_specific_to_that_leaf). Since ADRS is different for every leaf, and PRF is pseudorandom, knowing the value at one position provides zero information about values at other positions. The attacker is forced to attack each position independently.

### Fault Attack Resistance

SLH-DSA provides natural resistance to certain classes of fault attacks, and can be hardened further:

**Self-verification:** After computing a signature, the signer can verify it before releasing it. If a fault caused any component to be computed incorrectly, verification will fail, and the faulty signature (which might leak secret key information) is never output. The computational overhead of self-verification is modest (verification is typically 5-10x faster than signing).

**Tree computation integrity:** If a fault corrupts a hash computation during tree construction, the resulting incorrect node propagates up to produce an incorrect root. The WOTS+ signature at the next layer will sign this incorrect root, but verification against the known public key root will fail. Thus, faults produce invalid (detectable) signatures rather than leaking secrets.

**Randomized signing:** The optional randomized mode (including random bytes in the R computation) ensures that each signing operation uses completely different internal values, preventing differential fault analysis that compares correct and faulty executions of the same operation.

### Comparison with Lattice-Based Security

| Security Aspect | SLH-DSA | ML-DSA |
|----------------|---------|--------|
| Underlying assumption | Hash function properties | Module-LWE/SIS hardness |
| Years of cryptanalysis | 30+ years (hash functions) | ~15 years (lattice problems) |
| Quantum algorithm risk | Only Grover (quadratic) | Unknown (no poly-time known) |
| Algebraic structure risk | None (no algebraic structure) | Ring/module structure present |
| Assumption minimality | Extremely minimal | Moderate (structured lattice) |
| Confidence in long-term security | Very high | High |

## 13.9 Performance Optimization

### Parallelism in Tree Computation

SLH-DSA's tree structure offers extensive opportunities for parallel execution:

**FORS tree parallelism:** The k trees in a FORS instance are completely independent. On a k-core processor, all trees can be computed simultaneously, providing up to k× speedup for FORS signing and verification. Even with k=14-35, modern multi-core CPUs can exploit significant parallelism.

**Merkle tree leaf parallelism:** Within a single Merkle tree of height h', all 2^{h'} leaves can be computed independently (each leaf is a WOTS+ public key derived from the secret). Computing up the tree from leaves to root has log₂(2^{h'}) = h' sequential steps, but at each level, all nodes at that level can be computed in parallel.

**WOTS+ chain parallelism:** The ℓ hash chains in a WOTS+ computation are independent of each other (they share no intermediate values). All ℓ chains can be computed simultaneously, bounded only by available hash function hardware.

**Inter-layer parallelism (limited):** Hypertree layers are sequential — you cannot compute layer i until layer i-1's root is known. However, during signing, the tree traversal within each layer offers parallelism.

**Practical speedup on multi-core systems:**
- 4 cores: ~3.5x speedup (bounded by tree serialization)
- 8 cores: ~5-6x speedup
- 16+ cores: ~8-10x speedup (diminishing returns from sequential dependencies)

### Hardware Acceleration

**SHA-256 acceleration (Intel SHA-NI):**
SHA-NI provides dedicated SHA-256 instructions (SHA256RNDS2, SHA256MSG1, SHA256MSG2) that compute rounds directly in hardware. For SLH-DSA, which is dominated by hash function calls:
- Without SHA-NI: Each SHA-256 call takes ~300-400 cycles
- With SHA-NI: Each SHA-256 call takes ~60-80 cycles
- Net speedup: 4-5x for the overall signature generation

**SIMD vectorization (AVX2/AVX-512):**
Multiple independent hash computations can be interleaved using SIMD registers. Using 256-bit AVX2, four SHA-256 computations can execute in parallel. Using 512-bit AVX-512, eight can execute simultaneously. This combines multiplicatively with the algorithmic parallelism:
- AVX2 with 4 cores: Effective ~14-16x speedup over scalar single-core
- AVX-512 with 8 cores: Effective ~40-50x speedup

**ARM implementations:**
ARM Cortex-A series processors with Crypto Extensions provide SHA-256 acceleration comparable to Intel SHA-NI. For IoT applications on Cortex-M series (without crypto extensions), software implementation remains practical but significantly slower.

**FPGA and ASIC acceleration:**
For high-throughput applications (timestamping servers, CA operations), custom hardware can compute many hash chains simultaneously:
- Dedicated pipeline per hash chain
- Tree computation with hardwired routing
- Throughput: potentially thousands of signatures per second at Level 1

### Verification Performance

Verification is inherently faster than signing because it traverses only one path through each structure rather than computing entire trees:

**Signing computes:**
- Full FORS trees (k trees of height a): k × 2^a leaf hash + k × (2^a - 1) internal hashes
- WOTS+ public keys for multiple leaves
- Full authentication paths

**Verification computes:**
- k single paths through FORS trees: k × a hashes per path
- One WOTS+ verification per layer: ℓ × (average w/2) hashes per verification
- Authentication path verification: h' hashes per layer

The ratio is dominated by the FORS component: signing computes all k × 2^a leaves while verification only needs k paths of length a, giving a factor of 2^a/a speedup (e.g., 4096/12 ≈ 341 for SLH-DSA-SHA2-128s).

In practice, additional overheads reduce this ratio to approximately 5-15x:

| Parameter Set | Sign Time | Verify Time | Ratio |
|--------------|-----------|-------------|-------|
| SLH-DSA-SHA2-128s | ~60 ms | ~4 ms | 15x |
| SLH-DSA-SHA2-128f | ~5 ms | ~1 ms | 5x |
| SLH-DSA-SHA2-192s | ~120 ms | ~8 ms | 15x |
| SLH-DSA-SHA2-192f | ~10 ms | ~2 ms | 5x |
| SLH-DSA-SHA2-256s | ~250 ms | ~15 ms | 17x |
| SLH-DSA-SHA2-256f | ~20 ms | ~3 ms | 7x |

### Precomputation and Caching

For applications where the same key signs many messages, precomputation can amortize costs:

**Caching the top layers:** The upper layers of the hypertree are shared across all signatures. Their WOTS+ keys and tree structures can be precomputed once during key generation (or first use) and cached. This eliminates the cost of recomputing these layers for each signature.

**Partial tree precomputation:** Some intermediate tree nodes can be precomputed and stored, trading storage for computation time. For the "s" variants with tall trees (h'=9), caching internal nodes at height 5 reduces per-signature computation by approximately 2^4 = 16 hash computations per cached node.

**Trade-offs:** Precomputation storage scales as O(2^{h_cache} × n × d) bytes, where h_cache is the cached depth. For moderate caching (h_cache = h'/2), this adds several KB to tens of KB of storage per key, which is acceptable for server deployments but may be prohibitive for constrained devices.

## 13.10 Detailed Comparison: "s" vs. "f" Variants

The choice between small-signature and fast-signing variants deserves careful analysis across multiple dimensions:

### Structural Differences

| Structural Parameter | "s" variant (128-bit) | "f" variant (128-bit) |
|---------------------|----------------------|----------------------|
| Total height h | 63 | 66 |
| Layers d | 7 | 22 |
| Per-layer height h' | 9 | 3 |
| FORS trees k | 14 | 33 |
| FORS height a | 12 | 6 |
| Leaves per XMSS tree | 512 | 8 |
| Total FORS instances | 2^63 | 2^66 |

### Performance Comparison

| Metric | SLH-DSA-SHA2-128s | SLH-DSA-SHA2-128f | Ratio (f/s) |
|--------|-------------------|-------------------|-------------|
| Signature size | 7,856 B | 17,088 B | 2.2x larger |
| Signing time | ~60 ms | ~5 ms | 12x faster |
| Verification time | ~4 ms | ~1 ms | 4x faster |
| Key generation time | ~15 ms | ~1 ms | 15x faster |
| Signing hash calls | ~500,000 | ~40,000 | 12x fewer |
| Verification hash calls | ~5,000 | ~4,000 | Similar |

### Decision Framework

**Choose "s" when:**
- Bandwidth is expensive or limited (satellite links, metered connections)
- Signatures are stored long-term (archival, blockchain)
- Signing is infrequent (root CA key, annual code signing)
- The application can tolerate 50-350 ms signing latency
- Signature verification happens rarely (each signature verified few times)

**Choose "f" when:**
- Signing latency is critical (online services, real-time systems)
- Bandwidth is plentiful (datacenter-to-datacenter communication)
- Signatures are ephemeral (session authentication, short-lived tokens)
- High signing throughput is needed (timestamping service)
- The application signs frequently but transmits signatures rarely

**Hybrid approach:** Some deployments use "f" variants for operational signatures (frequent, latency-sensitive) and "s" variants for archival or trust-anchor signatures (infrequent, size-sensitive).

## 13.11 Use Cases and Deployment Strategies

### When to Choose SLH-DSA Over ML-DSA

The decision between SLH-DSA and ML-DSA should be driven by the threat model and operational requirements:

**Certificate Authority root keys:** Root CA keys protect the entire PKI hierarchy for decades. A compromise would be catastrophic. SLH-DSA's minimal assumptions provide maximum confidence that the root key will remain secure regardless of advances in lattice cryptanalysis. Root keys sign rarely (only to issue intermediate CA certificates), so the signing performance penalty is irrelevant. The "s" variant is ideal here, as root certificates are stored in trust stores (not transmitted frequently).

**Long-term document signing:** Legal documents, contracts, and government records may need to be verifiable for 50-100 years. Over such timescales, the risk of lattice-problem breakthroughs is non-negligible. SLH-DSA provides assurance that signatures will remain valid as long as the underlying hash function remains secure — a much safer bet over multi-decade horizons.

**Firmware and BIOS signing:** Firmware signatures protect the lowest level of system integrity. A break would allow persistent, undetectable compromise of entire device fleets. The extreme security conservatism of SLH-DSA is appropriate here, and firmware images are large enough that the signature overhead is proportionally insignificant. Updates happen infrequently, so signing speed is not a concern.

**Critical infrastructure SCADA systems:** Industrial control systems have extreme longevity requirements (20-30 year deployment cycles) and cannot be easily updated. The conservative security of SLH-DSA, combined with its simple security assumptions that are unlikely to be invalidated, makes it suitable for protecting systems that must remain secure far into the future.

**Regulatory compliance:** Some regulatory frameworks may specifically require or prefer hash-based signatures due to their minimal-assumption security profile. Government agencies dealing with classified information may mandate SLH-DSA for the highest-assurance applications.

### When NOT to Choose SLH-DSA

**High-throughput TLS:** Web servers handling thousands of TLS connections per second cannot afford 60-350 ms per signature. Even the "f" variants at 5-20 ms are significantly slower than ML-DSA's ~1 ms. Furthermore, the large signatures (8-50 KB) would noticeably increase TLS handshake times on slower connections.

**Bandwidth-constrained IoT:** Devices communicating over LoRaWAN, NB-IoT, or similar low-bandwidth protocols cannot efficiently transmit 8-50 KB signatures. ML-DSA's 2.4-4.6 KB signatures are already challenging for these environments.

**High-frequency authentication:** Systems requiring sub-millisecond signature verification for every operation (real-time trading, high-frequency authentication tokens) need the speed of ML-DSA.

**Mobile applications:** While modern smartphones can easily handle SLH-DSA computationally, the signature sizes impact cellular data usage and response times for mobile API calls.

### Combining SLH-DSA with ML-DSA

A layered approach leverages each scheme's strengths:

**Tiered PKI deployment:**
- Root CA: SLH-DSA-SHA2-256s (maximum security, signs rarely)
- Intermediate CA: SLH-DSA-SHA2-192s or ML-DSA-87 (high security, moderate signing frequency)
- End-entity certificates: ML-DSA-65 (balanced performance for frequent issuance and verification)

**Dual-signature critical documents:**
For the highest-assurance applications, sign the same document with both ML-DSA and SLH-DSA. The document is considered authentic if either signature verifies. This provides:
- Performance of ML-DSA for routine verification
- Insurance of SLH-DSA if lattice problems are broken
- Continued protection as long as either underlying assumption holds

**Algorithm negotiation:**
Protocols like TLS can negotiate the signature algorithm at connection time:
- Offer ML-DSA as the primary (faster, smaller)
- Fall back to SLH-DSA if the peer doesn't support ML-DSA
- Use SLH-DSA for the handshake signature if maximum security is configured

## 13.12 Implementation Considerations

### Memory Requirements and Constraints

SLH-DSA signing requires significant working memory compared to ML-DSA, primarily for tree computation:

**Stack/heap usage during signing (approximate):**
- FORS computation: k × 2^a × n bytes for leaf generation (e.g., 14 × 4096 × 16 ≈ 900 KB if all leaves generated at once, or ~2 KB per tree if computed incrementally)
- Merkle tree state: h' × n bytes per tree level for authentication path computation
- WOTS+ signature: ℓ × n bytes per instance
- Total with streaming computation: Approximately 10-50 KB depending on implementation strategy

**Memory-optimized approaches:**
Rather than computing entire trees in memory, implementations can use BDS (Buchmann-Dahmen-Schneider) tree traversal or similar algorithms that compute Merkle authentication paths with O(h × n) memory by cleverly scheduling node computations:

1. **Treehash algorithm:** Computes authentication paths using a stack-based approach, requiring only O(h' × n) memory per tree (instead of O(2^{h'} × n) for full materialization)
2. **On-the-fly computation:** FORS leaves are generated only as needed (using PRF), never stored all at once
3. **Streaming WOTS+ chains:** Each chain is computed sequentially, with only the current value kept in memory

**Constrained device feasibility:**
- ARM Cortex-M4 (256 KB flash, 64 KB RAM): Feasible with memory-optimized implementation
- 8-bit microcontrollers (≤8 KB RAM): Not feasible for signing; verification-only is possible with careful implementation
- Smart cards (limited RAM, hardware SHA): Feasible with hardware hash acceleration

### Deterministic vs. Randomized Signing

SLH-DSA supports both modes through the `opt` parameter:

**Deterministic (opt = 0^n):**
- Same message + same key always produces identical signature
- Reproducible for testing and debugging
- No RNG dependency during signing
- Vulnerable to differential fault analysis (attacker can repeat the same computation)

**Randomized (opt ← Random(n)):**
- Different signature each time, even for the same message
- Requires n bytes of randomness per signature
- Protects against fault attacks (different internal state each time)
- Recommended by FIPS 205 for general deployment

**Security implications of the choice:**
- Core EUF-CMA security is identical for both modes (rejection sampling is not needed as in ML-DSA)
- The choice affects only side-channel and fault attack resistance
- For software-only implementations on general-purpose CPUs, deterministic mode is often sufficient
- For hardware implementations (smart cards, HSMs) in physically adversarial environments, randomized mode is strongly recommended

### Key Storage and Management

SLH-DSA keys are remarkably compact:

**Secret key structure:** SK = (SK.seed, SK.prf, PK.seed, PK.root)
- SK.seed (n bytes): Seed for deriving all WOTS+ and FORS secret values
- SK.prf (n bytes): Key for the message-dependent PRF (index generation)
- PK.seed (n bytes): Public seed for tweakable hash instantiation
- PK.root (n bytes): Root of the top-level tree (redundant with public key, stored for convenience)
- Total: 4n bytes (64, 96, or 128 bytes for Level 1, 3, 5)

**Public key structure:** PK = (PK.seed, PK.root)
- PK.seed (n bytes): Same as in secret key (needed for verification)
- PK.root (n bytes): Root hash of the hypertree
- Total: 2n bytes (32, 48, or 64 bytes for Level 1, 3, 5)

**Key generation process:**
1. Sample SK.seed, SK.prf, PK.seed randomly (3n bytes of entropy required)
2. Compute the entire hypertree from SK.seed and PK.seed to derive PK.root
3. This computation is expensive (equivalent to one signing operation × 2^{h'} for the top layer)
4. PK.root can be cached after first computation

**Key backup and recovery:** Because the secret key is just seeds, key backup is simple — back up the 4n seed bytes. The entire tree structure (all WOTS+ and FORS keys, all internal tree nodes) can be regenerated deterministically from these seeds.

### Signature Serialization

The encoding of SLH-DSA signatures follows a straightforward concatenation format specified in FIPS 205:

```
Encoded signature = R ‖ σ_FORS ‖ σ_HT
                  = R ‖ (val₀ ‖ auth₀ ‖ ... ‖ val_{k-1} ‖ auth_{k-1})
                      ‖ (σ_WOTS₀ ‖ AUTH₀ ‖ ... ‖ σ_WOTS_{d-1} ‖ AUTH_{d-1})
```

All components are fixed-size for a given parameter set, so no length prefixes or delimiters are needed. Parsing is simply reading sequential fixed-size blocks.

### Side-Channel Considerations

SLH-DSA's hash-only construction simplifies side-channel resistance compared to lattice schemes:

**Inherently constant-time operations:** Hash functions (SHA-256, SHAKE-256) have no data-dependent branches or memory accesses in standard implementations. The entire SLH-DSA computation consists of hash function calls, array indexing with publicly-known indices, and simple concatenation.

**Secret-dependent values:** The only values that must remain secret are:
- SK.seed and SK.prf (stored in secure memory)
- WOTS+ and FORS secret leaf values (derived from SK.seed via PRF, never stored)
- Intermediate hash chain values during signing

**Timing channels:** The tree traversal path depends on the message (through the deterministic index), which is not secret. The signing time is constant for a given parameter set (no rejection sampling or variable-length loops). This makes SLH-DSA naturally easier to implement in constant time compared to ML-DSA.

**Power/EM emanation:** The primary leakage vector is through hash function computations that process secret key-derived values. Standard countermeasures (shuffling, blinding) for hash function implementations apply.

## 13.13 Advanced Topics

### Relationship to Stateful Schemes (XMSS, LMS)

SLH-DSA evolved from stateful hash-based signature schemes standardized earlier:

**XMSS (RFC 8391) and LMS (RFC 8554):** These schemes use a simple Merkle tree of WOTS+ instances, with a counter tracking which leaf to use next. They are more efficient than SLH-DSA (signatures are 2-3 KB, signing is fast) but require careful state management:
- The counter must be persisted before the signature is released
- Rollback must be prevented (using the same counter value twice breaks security)
- Distributed signing requires synchronized counter access
- Backup and restore operations must coordinate counter state

SLH-DSA trades size and speed for operational simplicity: no counter, no state synchronization, no rollback risk. For organizations that can manage state rigorously (e.g., dedicated HSMs with non-volatile counters), stateful schemes remain an option with better performance characteristics. NIST has published SP 800-208 covering XMSS and LMS for this purpose.

### Multi-Tree and Hybrid Constructions

Research continues on optimizations and variants:

**Gravity-SPHINCS:** A variant using a different tree structure optimized for smaller signatures at the cost of increased verification time.

**SPHINCS-α:** Research proposals for tighter security proofs that could enable smaller parameters.

**Hash-then-sign optimizations:** For very large messages, computing the message digest outside the signature scheme allows streaming processing without buffering the entire message.

### Post-Quantum Security Margins

The security margins in SLH-DSA parameters deserve explicit discussion:

For Level 1 (n=16 bytes = 128 bits):
- Classical second-preimage: 2^128 work
- Quantum second-preimage (Grover): 2^64 quantum queries
- NIST Level 1 target: "as hard as AES-128 against quantum"
- Grover on AES-128: ~2^64 quantum gates

The margins are thus tight at Level 1 — the security is exactly at the target level, not significantly above it. This motivates choosing Level 3 or Level 5 for applications with long-term security requirements or where a conservative margin is desired.

For Level 5 (n=32 bytes = 256 bits):
- Classical second-preimage: 2^256 work
- Quantum second-preimage (Grover): 2^128 quantum queries
- This provides a substantial quantum security margin even accounting for potential improvements in quantum algorithms

### Future Directions

The SLH-DSA design space continues to evolve:

**Signature size reduction:** Research into more efficient few-time signatures (beyond FORS) could reduce the bottom-layer contribution to signature size.

**Faster hash functions:** Purpose-built hash functions optimized for tree hashing (like KangarooTwelve or Skein's tree mode) could accelerate SLH-DSA without changing the overall structure.

**Hardware co-design:** ASIC/FPGA designs specifically optimized for SLH-DSA's tree structure could close the performance gap with lattice-based schemes for dedicated signing appliances.

**Improved security proofs:** Tighter reductions in the QROM could allow more aggressive parameter choices while maintaining provable security guarantees.

## 13.14 Key Takeaways

- SLH-DSA (FIPS 205) provides the most conservative post-quantum signature scheme, relying solely on hash function properties rather than algebraic hardness assumptions
- Security requires only second-preimage resistance and pseudorandomness of the hash function — properties that have withstood over 30 years of intensive cryptanalysis
- The hypertree architecture composes FORS (few-time), WOTS+ (one-time), and Merkle trees into a unified stateless signature scheme
- Stateless operation is achieved through deterministic index derivation: the message itself determines which signing keys are used, eliminating state management entirely
- Twelve parameter sets cover three security levels × two hash families × two optimization targets (small signatures vs. fast signing)
- Signatures are large (7.8-49.9 KB) compared to ML-DSA (2.4-4.6 KB), representing the primary practical trade-off for stronger security assumptions
- Keys are extremely compact (32-128 bytes) — the smallest of any post-quantum signature scheme
- The "s" variants minimize signature size (7.8-29.8 KB) at the cost of slower signing (60-350 ms); "f" variants optimize for speed (5-25 ms) with larger signatures (17-50 KB)
- SHA-256 and SHAKE-256 instantiations provide equivalent security; the choice depends on available hardware acceleration and existing infrastructure
- SLH-DSA serves as the cryptographic backstop: if lattice-based schemes are ever broken, SLH-DSA provides an independent line of defense
- Ideal deployment: root CA keys, long-term document signing, firmware signing, and any application where maximum security confidence justifies the performance cost
- Can be combined with ML-DSA in layered architectures: ML-DSA for routine operations, SLH-DSA for trust anchors and long-term protection
- Implementation is simpler than ML-DSA in some respects: no rejection sampling, naturally constant-time (hash-only computation), and no complex polynomial arithmetic

---

*Next: [Chapter 14 — Additional Candidates and Round 4 Algorithms](./14-additional-candidates.md)*
