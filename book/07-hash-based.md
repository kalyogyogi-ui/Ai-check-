# Chapter 7: Hash-Based Signatures

## 7.1 The Appeal of Hash-Based Cryptography

Among the families of post-quantum cryptographic schemes, hash-based signatures occupy a philosophically distinctive position. Their security relies on what cryptographers consider the **minimal possible assumption**: the existence of a secure hash function. There are no hidden algebraic structures to exploit, no lattice problems whose hardness might one day be undermined by clever algorithms, and no error-correcting codes whose parameters might prove insufficiently conservative. The entire security argument reduces to the one-wayness, second preimage resistance, and collision resistance of a well-studied hash function.

This minimalism carries profound implications for long-term confidence. Consider the history of cryptographic assumptions: RSA's security depends on the hardness of integer factorization, a problem studied for centuries yet broken in polynomial time by Shor's algorithm on a quantum computer. Elliptic curve discrete logarithm, once considered an independent assumption, fell to the same quantum algorithm. Lattice problems, while promising, have been studied intensively for only a few decades in the cryptographic context, and new algorithmic ideas continue to emerge. Hash functions, by contrast, have been the workhorses of computer science for over fifty years, and the best known quantum attack against them — Grover's algorithm — provides only a quadratic speedup, meaning that doubling the output length fully compensates for quantum adversaries.

The concrete benefits of hash-based security assumptions include:

- **Maximum confidence in quantum resistance.** A quantum computer running Grover's algorithm against a 256-bit hash function achieves only 128-bit quantum security. This is well understood, and no better quantum algorithm is known or expected for generic hash functions. The mathematical arguments for this lower bound are substantially stronger than those for lattice or code-based problems.

- **Conceptual simplicity and transparency.** The constructions — Lamport signatures, Winternitz chains, Merkle trees — can be explained to undergraduate computer science students. Each component has a clear purpose, and the overall security argument composes cleanly from the security of individual building blocks.

- **Cryptographic agility and future-proofing.** If a specific hash function (say SHA-256) were found to be weak, the scheme could be re-instantiated with a different hash function without changing the structural design. The signature scheme is parameterized by an abstract hash function family, and its security proof holds for any instantiation meeting the required properties.

- **Proven security with tight reductions.** Hash-based signature schemes typically enjoy security proofs where the security loss between the scheme and the underlying hash function is minimal — often logarithmic in the number of signatures issued. This contrasts with many lattice-based or code-based schemes where the security reductions involve polynomial or even super-polynomial loss factors.

The trade-offs, however, are significant. Hash-based signatures typically produce larger signatures than lattice-based alternatives: SLH-DSA signatures range from approximately 8 KB to 50 KB, compared to 2.4 KB for ML-DSA at comparable security levels. Signing and verification operations require hundreds or thousands of hash function evaluations, making them slower in absolute terms, though still practical for most applications. Key generation for stateful schemes can also be expensive when large trees must be constructed upfront. These trade-offs make hash-based signatures a complement to lattice-based approaches rather than a replacement: they serve as the conservative fallback when maximum security confidence outweighs performance concerns.

## 7.2 One-Time Signatures: The Building Block

The entire edifice of hash-based cryptography rests on a deceptively simple foundation: the one-time signature (OTS). A one-time signature scheme allows a signer to produce exactly one signature under a given key pair. If the key pair is reused, the scheme's security guarantees evaporate. While this seems like an absurd limitation, it turns out that one-time signatures can be constructed from hash functions alone with extraordinary efficiency, and the limitation can be managed through tree-based key management structures described in later sections.

### Lamport Signatures (1979)

Leslie Lamport proposed the simplest possible hash-based signature in 1979, and it remains the most intuitive introduction to the field. The construction requires nothing beyond a one-way function.

**Key Generation.** Suppose we want to sign messages whose hash is n bits long. For each bit position i from 1 to n, the signer generates two independent random values: x_i^0 and x_i^1, each of length n bits. The signer then computes y_i^0 = H(x_i^0) and y_i^1 = H(x_i^1) for each i. The secret key consists of all 2n random values (x_i^0, x_i^1), and the public key consists of all 2n hash values (y_i^0, y_i^1).

**Signing.** To sign a message m, the signer first computes h = H(m), obtaining n bits h_1, h_2, ..., h_n. The signature is the sequence of n secret values, one per bit position, selected according to the corresponding message hash bit: sigma = (x_1^{h_1}, x_2^{h_2}, ..., x_n^{h_n}).

**Verification.** The verifier receives the signature sigma = (sigma_1, sigma_2, ..., sigma_n). For each position i, the verifier computes H(sigma_i) and checks that it equals y_i^{h_i} from the public key, where h_i is the i-th bit of H(m).

**Security argument.** If an adversary observes a signature on message m, they learn exactly one preimage per bit position — the one corresponding to the actual bit value of H(m). To forge a signature on a different message m', the adversary would need to find a preimage for at least one position where H(m') differs from H(m). Since the adversary has never seen the corresponding secret value for that position, they would need to invert the hash function, which contradicts the one-wayness assumption.

**Practical limitations.** Lamport signatures have enormous key and signature sizes. For n = 256 (using a 256-bit hash), the public key contains 512 hash values (16,384 bytes), and each signature contains 256 hash values (8,192 bytes). Furthermore, the scheme is strictly one-time: signing two different messages reveals preimages for both bit patterns, potentially allowing an adversary to construct a valid signature for a third message whose hash bits are covered by the union of revealed preimages.

Despite its impracticality, the Lamport scheme establishes the conceptual foundation: hash functions alone suffice for digital signatures, and the one-time limitation can be addressed through structural means.

### Winternitz One-Time Signature (WOTS)

Robert Winternitz observed in 1979 that Lamport signatures could be compressed dramatically by signing multiple bits simultaneously using iterated hash chains rather than individual hash function evaluations. This insight reduces signature size by a factor roughly proportional to the Winternitz parameter w, at the cost of increased computation.

**Core Idea: Hash Chains.** Instead of signing one bit at a time, WOTS processes the message hash in base-w digits. A hash chain of length w-1 is a sequence of values computed by iterating the hash function: given a starting value x, the chain is x, H(x), H(H(x)), ..., H^{w-1}(x). The signer reveals an intermediate value in the chain, and the verifier can check it by hashing forward to the chain's endpoint (which is part of the public key).

**Detailed Construction.** Let the message hash be n bits long, and let w be the Winternitz parameter (typically a power of 2). The construction proceeds as follows:

1. Divide the message hash into l_1 = ceil(n / log_2(w)) base-w digits, each ranging from 0 to w-1.
2. Compute a checksum over these digits: C = sum_{i=1}^{l_1} (w - 1 - m_i), where m_i is the i-th digit. This checksum is then encoded as l_2 additional base-w digits.
3. The total number of hash chains is l = l_1 + l_2.
4. The secret key consists of l random starting values (x_1, ..., x_l).
5. The public key consists of l chain endpoints: (H^{w-1}(x_1), ..., H^{w-1}(x_l)).
6. To sign, reveal the chain value at position m_i for message digit i: sigma_i = H^{m_i}(x_i).
7. To verify, hash each signature component forward by (w - 1 - m_i) steps and check against the public key: H^{w-1-m_i}(sigma_i) should equal the corresponding public key element.

**The checksum's role.** Without the checksum, an adversary who observes a signature could trivially forge signatures for messages with larger digit values — they would simply hash forward on the revealed chain values. The checksum ensures that any increase in a message digit must be compensated by a decrease in a checksum digit, which would require inverting the hash function (hashing backward on a chain). This elegant mechanism preserves one-time security without additional assumptions.

**WOTS+ (Used in SPHINCS+/SLH-DSA).** The WOTS+ variant, developed by Hülsing in 2013, introduces two refinements that yield tighter security proofs:

First, WOTS+ uses a **tweakable hash function** rather than a plain hash function for chain computation. Each hash evaluation incorporates a unique "address" that specifies the chain index, the position within the chain, and a public seed. This prevents an adversary from exploiting relationships between different chains or between different signers' keys.

Second, WOTS+ adds **randomized bitmasks** to the hash chain computation. Before each hash evaluation, the input is XORed with a position-dependent bitmask derived from the public seed. This eliminates multi-target attack advantages where an adversary might benefit from seeing many hash chain values across different positions or key pairs.

These modifications enable a security proof that reduces tightly to the properties of the underlying hash function, with security loss that is essentially independent of the number of chains or the chain length.

**The Trade-off Parameter w.** The Winternitz parameter w controls a fundamental space-time trade-off:

| w | Chains (l) for n=256 | Signature Size | Hash Calls (Sign) | Hash Calls (Verify) |
|---|----------------------|----------------|-------------------|---------------------|
| 4 | 133 | ~4,256 bytes | ~199 | ~199 |
| 16 | 67 | ~2,144 bytes | ~503 | ~503 |
| 256 | 34 | ~1,088 bytes | ~4,335 | ~4,335 |

With w = 4, each chain has only 3 intermediate values, so signing and verification require few hash evaluations per chain, but there are many chains. With w = 256, each chain has 255 intermediate values, so there are far fewer chains (smaller signature), but each signing or verification operation requires traversing potentially long chains.

In practice, w = 16 provides the best balance for most applications, and this is the default in both XMSS and SLH-DSA. The choice of w = 256 is occasionally used when signature size must be minimized regardless of computational cost.

## 7.3 Few-Time Signatures: HORST and FORS

One-time signatures must be used exactly once, and violating this constraint catastrophically compromises security. For stateless hash-based schemes, we need a slightly more forgiving primitive: a **few-time signature** (FTS) that remains secure even if a small number of messages are signed with the same key. The degradation in security should be gradual and quantifiable, allowing scheme parameters to compensate for the expected number of reuses.

### HORST (Hash to Obtain Random Subset Tree)

HORST, introduced in the original SPHINCS proposal (2015), was the first few-time signature designed specifically for use within a hypertree construction. Its core idea is simple: the signer possesses a large set of secret values organized into a Merkle tree, and signing a message involves revealing a pseudorandomly selected subset of these values along with their authentication paths.

The construction works as follows: the signer generates t secret values s_1, ..., s_t and builds a Merkle tree over their hashes. To sign a message, the message hash is split into k portions, each selecting one of the t secret values to reveal. The signature consists of the k revealed values plus their Merkle authentication paths.

HORST's security degrades with each additional signature: every signature reveals k secret values, and after q signatures, an adversary knows up to qk values. For the adversary to forge a signature, they need the message hash to select only from the already-revealed values, which has probability approximately (qk/t)^k. By choosing t and k appropriately, this probability can be made negligible for any expected number of signatures.

However, HORST has a significant weakness: its security degrades relatively quickly, and achieving high security levels requires very large parameter sets.

### FORS (Forest of Random Subsets)

FORS, introduced in SPHINCS+ (2019) and used in the standardized SLH-DSA, improves upon HORST with a cleaner construction and better concrete security.

**Structure.** FORS uses k independent binary trees, each of height a (having 2^a leaves). The signer generates k × 2^a random secret values, organized as leaves of k separate Merkle trees. Each tree has its own root, and the k roots are hashed together to form the FORS public key.

**Key generation.** For tree j (j = 0, ..., k-1) and leaf index i (i = 0, ..., 2^a - 1):
- Secret value: sk_{j,i} is derived pseudorandomly from the master secret key and an address
- Leaf node: H(sk_{j,i})
- The tree is built up using standard Merkle tree construction
- The FORS public key is H(root_0 || root_1 || ... || root_{k-1})

**Signing.** To sign a message (or rather, a message digest) of ka bits:
1. Split the digest into k blocks of a bits each: b_0, b_1, ..., b_{k-1}
2. Each block b_j selects a leaf index in tree j
3. The signature consists of k secret values (one per tree, at the selected leaf) plus k authentication paths (one per tree, from the selected leaf to the root)

**Verification.** The verifier:
1. Splits the message digest identically
2. For each tree j, hashes the revealed secret value to obtain the leaf, then uses the authentication path to compute the root
3. Hashes all k roots together and compares with the FORS public key

**Security analysis.** The security of FORS against forgery after observing q signatures depends on the probability that a new message digest selects, in every tree, a leaf that was previously revealed. For tree j, each signature reveals one of 2^a leaves, so after q signatures, the fraction of known leaves is at most q/2^a. The probability that a random message selects only known leaves across all k trees is at most (q/2^a)^k.

For the parameters used in SLH-DSA-128f (k = 33, a = 6), even after 2^10 signatures to the same FORS instance, the forgery probability is approximately (2^10 / 2^6)^33 = (2^4)^33 = 2^132, which is negligible. In practice, the hypertree structure ensures that each FORS instance is used far fewer times than this bound.

**Advantages over HORST.** FORS provides better concrete security with smaller parameters because the tree structure allows efficient authentication without revealing the global structure. The separation into independent trees also simplifies the security analysis and allows tighter reductions.

## 7.4 Merkle Trees: Managing Many Keys

The fundamental limitation of one-time and few-time signatures — that they can sign only a limited number of messages — must be overcome for practical use. Ralph Merkle's brilliant insight in 1979 was that a binary hash tree could aggregate an exponential number of one-time key pairs under a single compact public key, with verification requiring only a logarithmic-length proof.

### Construction

A Merkle signature tree of height h manages N = 2^h one-time signature key pairs:

1. **Leaf generation.** Generate N independent OTS key pairs (sk_0, pk_0), (sk_1, pk_1), ..., (sk_{N-1}, pk_{N-1}).
2. **Leaf hashing.** Compute the leaf nodes of the tree as L_i = H(pk_i) for each i.
3. **Internal nodes.** Build the binary tree bottom-up: each internal node is the hash of the concatenation of its two children: Node_{level, index} = H(Node_{level-1, 2·index} || Node_{level-1, 2·index+1}).
4. **Root.** The single root node at level h serves as the aggregate public key for all N key pairs.

The tree structure creates a binding commitment: modifying any leaf would change the root, so the root effectively commits to all N public keys simultaneously.

### Authentication Path

To sign a message with the i-th OTS key pair, the signer provides:
1. The OTS signature on the message
2. The OTS public key pk_i (which the verifier needs to verify the OTS signature)
3. An **authentication path**: the sequence of h sibling nodes along the path from leaf i to the root

The authentication path allows the verifier to recompute the root independently:
1. Verify the OTS signature against pk_i
2. Compute L_i = H(pk_i)
3. For each level from 0 to h-1, combine the current node with the provided sibling (respecting left/right ordering) and hash to obtain the parent
4. Compare the computed root against the known public key (the published root)

The authentication path contains exactly h hash values, so its size is h × |hash output|. For a tree of height 20 with 256-bit hashes, the authentication path is only 640 bytes — remarkably compact for authenticating one key among over a million.

### Tree Traversal and Efficiency

A naive implementation would store the entire tree (2^{h+1} - 1 nodes), which is impractical for large h. Several algorithms optimize the computation of successive authentication paths:

**Classical Merkle traversal.** The original Merkle traversal algorithm computes authentication paths on-the-fly using O(h^2) storage and O(h) hash computations per signature. It keeps a "stack" of partially computed subtrees and schedules their computation across multiple signing operations.

**BDS (Buchmann-Dahmen-Szydlo) traversal.** The BDS algorithm (2009) reduces the per-signature computation to O(h/2) hash evaluations using O(2h + h·2^(h/d)) storage, where d is a tuning parameter. It achieves this by pre-computing and caching treehash instances — partial tree computations that are advanced incrementally with each signature.

**Fractal Merkle trees.** Fractal tree traversal distributes the computation of future authentication path nodes across current signing operations, maintaining near-constant per-signature cost at the expense of increased storage for intermediate computations.

**Multi-tree approaches.** Rather than using a single large tree, one can layer multiple smaller trees. A tree at level i+1 certifies (signs) the roots of trees at level i. This reduces the memory required for tree traversal at any single level and allows on-demand generation of subtrees.

The choice of traversal algorithm affects only performance, not security. All algorithms produce identical signatures and authentication paths; they differ only in how efficiently these are computed.

## 7.5 Stateful Hash-Based Signatures: XMSS and LMS

The combination of one-time signatures and Merkle trees yields practical signature schemes with excellent security properties. Two such schemes have been standardized: XMSS (eXtended Merkle Signature Scheme) and LMS (Leighton-Micali Signature). Both are **stateful**: the signer must maintain and update a counter indicating which leaf to use next.

### XMSS (eXtended Merkle Signature Scheme)

XMSS, standardized in RFC 8391 (2018) and approved by NIST in SP 800-208, extends the basic Merkle construction with modern security features.

**Structure.** An XMSS instance consists of:
- A single Merkle tree of height h, giving capacity for 2^h signatures
- WOTS+ instances at each leaf, providing one-time signatures
- A bitmask and key generation scheme using a public seed, ensuring that all hash computations are domain-separated

**Detailed signing process:**
1. Retrieve the current leaf index idx from the state and increment it
2. Compute the WOTS+ signature on the message using the secret key at leaf idx
3. Compute the authentication path from leaf idx to the root
4. Output the signature: (idx, WOTS+ signature, authentication path)
5. Persist the updated state (new idx value)

**Parameters and sizes:**

| Parameter Set | h | n | w | Signatures | Sig Size | PK Size | SK Size |
|--------------|---|---|---|-----------|----------|---------|---------|
| XMSS-SHA2_10_256 | 10 | 32 | 16 | 1,024 | 2,500 B | 64 B | 1,395 B |
| XMSS-SHA2_16_256 | 16 | 32 | 16 | 65,536 | 2,692 B | 64 B | 2,083 B |
| XMSS-SHA2_20_256 | 20 | 32 | 16 | 1,048,576 | 2,820 B | 64 B | 2,467 B |

The signature sizes are remarkably compact for hash-based schemes: approximately 2.5–2.8 KB depending on tree height. Public keys are just 64 bytes (a root hash plus a public seed). The signature grows by 32 bytes for each additional level of tree height, reflecting the authentication path.

**Key generation.** XMSS key generation involves computing the entire tree (or at minimum, the root and initial authentication path). For h = 20, this requires computing over one million WOTS+ public keys and building a tree with over two million nodes — a one-time cost that may take several seconds.

### XMSS^MT (Multi-Tree XMSS)

For applications requiring more than 2^20 signatures (approximately one million), a single XMSS tree becomes impractical because key generation would require computing an astronomically large tree. XMSS^MT addresses this through a layered approach.

**Construction.** XMSS^MT uses d layers of XMSS trees, each of height h/d:
- The top layer contains a single tree whose root is the overall public key
- Each leaf of a tree at layer i contains the root of a tree at layer i-1
- The bottom layer's leaves contain the actual WOTS+ key pairs used to sign messages
- Total signing capacity: 2^h signatures, distributed across 2^{h-h/d} bottom-layer trees

**Signing.** To sign with leaf index idx:
1. Decompose idx into d components, one per layer
2. At the bottom layer, sign the message with the appropriate WOTS+ instance
3. At each higher layer, sign the root of the layer below with the appropriate WOTS+ instance
4. The final signature contains d WOTS+ signatures and d authentication paths

**Trade-offs.** XMSS^MT signatures are d times larger than single-tree XMSS signatures (each layer contributes one WOTS+ signature and one authentication path). However, key generation only requires building the top-layer tree immediately, and lower-layer trees can be generated on demand. With d = 4, for example, total height h = 40 gives 2^40 (approximately one trillion) signatures, with each layer having height 10.

### LMS (Leighton-Micali Signature)

LMS, standardized in RFC 8554 (2019) and also approved in NIST SP 800-208, follows the same conceptual design as XMSS but with different technical choices.

**Key differences from XMSS:**
- Uses LM-OTS (Leighton-Micali One-Time Signature) instead of WOTS+. LM-OTS is similar to WOTS but uses a slightly different chain construction with a checksum mechanism.
- Does not use bitmasks or tweakable hash functions in the tree construction, instead relying on a simpler hash construction with explicit type bytes.
- The multi-tree variant is called HSS (Hierarchical Signature System) and allows up to 8 layers.
- Parameters are identified by numeric identifiers rather than algorithm names.

**LMS parameter sets include:**
- LMS_SHA256_M32_H5 through LMS_SHA256_M32_H25 (tree heights 5 through 25)
- LM-OTS parameters with Winternitz values w = 1, 2, 4, 8

**Comparative note.** XMSS has somewhat tighter security proofs due to its use of tweakable hash functions, while LMS has a simpler specification and slightly faster implementation in constrained environments. Both schemes provide equivalent practical security when instantiated with appropriate parameters.

### The State Management Problem

The stateful nature of XMSS and LMS introduces their most significant operational challenge: **the signer must never, under any circumstances, reuse a one-time key pair.**

**Why reuse is catastrophic.** If a WOTS+ key pair is used to sign two different messages, an adversary observing both signatures sees two different intermediate chain values for each position. In positions where the two message digits differ, the adversary can compute hash chain values they should never have seen. With sufficient information from just two signatures on distinct messages, a complete key recovery is often possible, enabling arbitrary forgeries.

**Sources of accidental reuse:**
- **System crashes:** If the state is not persisted to non-volatile storage before the signature is released, a crash and restart could cause the same index to be used again.
- **Virtual machine snapshots and rollbacks:** Restoring a VM to a previous state resets the index counter, causing certain reuse of one-time keys.
- **Backup and restore:** Restoring a system from backup similarly resets the state.
- **Cloning:** Copying a signing system (for load balancing or redundancy) creates two instances with identical state that will inevitably produce colliding signatures.
- **Concurrent access:** Multiple threads or processes accessing the same key without proper synchronization may read the same index.

**Mitigation strategies:**
- Write the incremented index to persistent storage before computing the signature (not after)
- Use hardware security modules (HSMs) with non-volatile monotonic counters
- Reserve index ranges: advance the persisted counter by a batch size (e.g., 1000) and use the reserved range in memory, so a crash wastes at most one batch but never causes reuse
- Never clone, snapshot, or backup the signing key state without permanent decommissioning of the original

These requirements restrict stateful hash-based signatures to controlled, high-security environments where operational discipline can be maintained. They are poorly suited to general-purpose applications where signing keys might be deployed on commodity hardware without specialized state management.

## 7.6 Stateless Hash-Based Signatures: SPHINCS+ / SLH-DSA

### Motivation

The state management burden of XMSS and LMS fundamentally limits their applicability. Most real-world signing scenarios — web servers handling TLS connections, software update systems signing packages, email clients signing messages — cannot guarantee the operational requirements that stateful schemes demand. A single VM rollback or database restore could silently compromise the signature scheme's security, with no detection mechanism.

SPHINCS+ (Stateless Practical Hash-based Incredibly Nice Cryptographic Signatures, Plus) was designed to eliminate state entirely while retaining the hash-only security assumption. Standardized as SLH-DSA (Stateless Hash-Based Digital Signature Algorithm) in FIPS 205 (2024), it achieves statelessness through a combination of large virtual trees and deterministic leaf selection.

### Architecture

SLH-DSA's architecture combines three cryptographic components in a layered structure:

1. **FORS (Forest of Random Subsets):** A few-time signature at the bottom layer that directly signs messages. Each FORS instance can safely sign a small number of messages.

2. **WOTS+ (Winternitz One-Time Signature Plus):** One-time signatures used at every internal tree level to authenticate the roots of trees at the level below.

3. **Hypertree:** A d-layer hierarchy of Merkle trees. The top tree's root is the public key. Each successive layer provides authentication for the layer below, down to the FORS instances at the bottom.

The hypertree contains an enormous number of virtual FORS instances — far more than will ever be used. The key insight is that these instances need not be generated in advance; they can be computed on demand from the secret key using pseudorandom derivation.

### Detailed Operation

**Key generation:**
1. Generate a secret seed SK.seed, a secret PRF key SK.prf, and a public seed PK.seed
2. Compute the root of the top-layer Merkle tree (this requires computing all nodes in the top tree, including all WOTS+ public keys at its leaves)
3. The public key is (PK.seed, PK.root) — just two n-byte values
4. The secret key is (SK.seed, SK.prf, PK.seed, PK.root) — four n-byte values

**Signing a message M:**
1. **Randomized message hashing.** Compute an optional randomizer R = PRF(SK.prf, OptRand, M), then compute the message digest = H_msg(R, PK.seed, PK.root, M). This digest determines both the FORS leaf index and provides the message to be signed.

2. **Index extraction.** From the digest, extract a (h - h/d)-bit index idx that selects a specific FORS instance in the virtual hypertree, plus a ka-bit message digest md to be signed by FORS.

3. **FORS signing.** Use SK.seed and the FORS address (determined by idx) to derive the FORS secret key, then sign md using FORS. Output the FORS signature and compute the FORS public key.

4. **Hypertree authentication.** Starting from the bottom layer:
   - The FORS public key hash is a leaf in the bottom-layer Merkle tree
   - Sign this leaf's tree root with the WOTS+ instance at the appropriate position in the next layer up
   - Compute and include the authentication path for that layer
   - Repeat for each layer up to the top

5. **Signature output.** The complete signature consists of: R (the randomizer), the FORS signature (k secret values + k authentication paths), and d WOTS+ signatures each with their Merkle authentication paths.

**Verification:**
1. Recompute the message digest from (R, PK.seed, PK.root, M)
2. Extract the same index and message digest
3. Verify the FORS signature and reconstruct the FORS public key
4. For each hypertree layer (bottom to top), verify the WOTS+ signature and use the authentication path to compute the next layer's expected root
5. Compare the final computed root against PK.root

### Why Stateless Works

The elimination of state relies on several interacting properties:

**Deterministic leaf selection.** Given the same secret key and the same message (and the same optional randomness), the signing algorithm always selects the same FORS instance and produces the same signature. There is no counter to maintain; the "address" in the hypertree is derived solely from the message and key material.

**Few-time signature tolerance.** If two different messages happen to map to the same FORS instance (a "collision" in the index derivation), FORS can tolerate this because it is a few-time signature. Security degrades gracefully with the number of messages signed per FORS instance, and the parameters are chosen so that the expected number of collisions remains safely within FORS's security margin.

**Astronomical virtual key space.** The hypertree contains 2^{h-h/d} FORS instances. For SLH-DSA-128f with total height h = 66 and d = 22, there are 2^63 FORS instances. Even signing 2^64 messages (far more than any practical system would ever produce), the expected number of messages per FORS instance is only about 2, well within FORS's few-time security tolerance.

**On-demand computation.** The signer never materializes the full hypertree. Each signing operation computes only the specific path from the selected FORS instance up to the root. This requires generating WOTS+ key pairs, building Merkle tree portions, and computing authentication paths for the specific indices needed — all derived deterministically from SK.seed and the addresses.

### Parameters (SLH-DSA, FIPS 205)

SLH-DSA offers six parameter sets spanning three security levels and two performance profiles:

| Parameter Set | Security Level | n | h | d | a | k | w | Sig Size | PK | SK |
|--------------|---------------|---|---|---|---|---|---|----------|----|----|
| SLH-DSA-128s | 1 (128-bit) | 16 | 63 | 7 | 12 | 14 | 16 | 7,856 B | 32 B | 64 B |
| SLH-DSA-128f | 1 (128-bit) | 16 | 66 | 22 | 6 | 33 | 16 | 17,088 B | 32 B | 64 B |
| SLH-DSA-192s | 3 (192-bit) | 24 | 63 | 7 | 14 | 17 | 16 | 16,224 B | 48 B | 96 B |
| SLH-DSA-192f | 3 (192-bit) | 24 | 66 | 22 | 8 | 33 | 16 | 35,664 B | 48 B | 96 B |
| SLH-DSA-256s | 5 (256-bit) | 32 | 64 | 8 | 14 | 22 | 16 | 29,792 B | 64 B | 128 B |
| SLH-DSA-256f | 5 (256-bit) | 32 | 68 | 17 | 9 | 35 | 16 | 49,856 B | 64 B | 128 B |

**The "s" vs "f" trade-off:** The "small" variants use fewer hypertree layers (smaller d) with taller trees per layer. This produces smaller signatures (fewer WOTS+ signatures in the authentication chain) but requires more hash computations during signing because each tree is taller. The "fast" variants use more layers of shorter trees, resulting in larger signatures (more WOTS+ components) but faster signing due to shorter trees.

### Performance Characteristics

| Operation | SLH-DSA-128s | SLH-DSA-128f | ML-DSA-44 | ECDSA P-256 |
|-----------|-------------|-------------|-----------|-------------|
| Key generation | ~5 ms | ~0.5 ms | ~0.1 ms | ~0.1 ms |
| Signing | ~50 ms | ~5 ms | ~0.3 ms | ~0.1 ms |
| Verification | ~5 ms | ~1 ms | ~0.3 ms | ~0.2 ms |
| Signature size | 7,856 B | 17,088 B | 2,420 B | 64 B |
| Public key size | 32 B | 32 B | 1,312 B | 64 B |

Several observations about these numbers:

- SLH-DSA signing is 15–500x slower than ML-DSA depending on the parameter set, making it poorly suited for high-throughput signing applications.
- Verification is faster than signing (typically 5–10x) because verifiers only hash forward on chains and recompute authentication paths, while signers must additionally generate key material.
- Public keys are extraordinarily compact (32–64 bytes), smaller than any other post-quantum scheme. This is advantageous in certificate chains where the same public key is transmitted repeatedly.
- The wide gap between "s" and "f" variants allows applications to choose their preferred point on the speed-vs-size curve.

## 7.7 Hash Function Requirements

The security of hash-based signatures reduces to properties of the underlying hash function, but not all hash function properties are equally important for all components. Understanding which properties are needed where is essential for correct instantiation and security analysis.

### Standard Cryptographic Properties

**Preimage resistance (one-wayness).** Given a hash output y, it must be computationally infeasible to find any input x such that H(x) = y. This is the foundational property used in Lamport and WOTS+ signatures: the public key consists of hash outputs, and forging requires finding their preimages.

Formally, for n-bit security, finding a preimage should require approximately 2^n hash evaluations. Against a quantum adversary using Grover's algorithm, this reduces to 2^{n/2} evaluations, so 256-bit hash outputs provide 128-bit quantum security.

**Second preimage resistance.** Given a specific input x, it must be infeasible to find a different input x' such that H(x) = H(x'). This property is crucial for Merkle tree security: given a valid authentication path, an adversary should not be able to find an alternative leaf that produces the same root.

**Collision resistance.** It must be infeasible to find any pair of distinct inputs (x, x') such that H(x) = H(x'). This property is needed for the binding property of Merkle trees and for the security of the message hashing step.

### Extended Properties for SLH-DSA

SLH-DSA's security proof requires additional properties beyond the standard three:

**Pseudorandom function (PRF) security.** The secret key includes a PRF key SK.prf used to derive the randomizer R for message hashing. This PRF must be indistinguishable from a random function to an adversary who does not know SK.prf. In the SLH-DSA instantiations, PRF is constructed from the same hash primitive (e.g., HMAC-SHA-256 or SHAKE-256 with appropriate domain separation).

**Tweakable hash function (Th) security.** A tweakable hash function takes an additional "tweak" input (called an address in SLH-DSA) that parameterizes the function. The security requirement is that the function behaves as an independent random function for each distinct tweak value. This is formalized through properties including:

- **Single-function multi-target second preimage resistance (SM-SPR):** Even when targeting many different instances (tweaks) simultaneously, finding a second preimage for any one should be no easier than finding a second preimage for a single instance.
- **Single-function multi-target decisional second preimage resistance (SM-DSPR):** A technical variant needed for the undetectability property.

**Interleaved target subset resilience (ITSR).** This property, specific to FORS, captures the difficulty of finding a message whose FORS signing indices fall entirely within a set of previously revealed indices. It is a strengthening of standard subset resilience that accounts for the adaptive nature of the attack (the adversary can choose which messages to request signatures on before attempting the forgery).

### Hash Function Instantiations

SLH-DSA specifies two primary instantiation families:

**SHA-256 based (SLH-DSA-SHA2).** Uses SHA-256 (for 128-bit security) or SHA-512 (for higher security levels) as the core primitive:
- The tweakable hash function Th is constructed using SHA-256 with the address prepended to the input
- The PRF uses HMAC-SHA-256
- The message hash H_msg uses MGF1 (Mask Generation Function 1) based on SHA-256
- This instantiation benefits from hardware acceleration (SHA-NI instructions) on modern x86 processors

**SHAKE-256 based (SLH-DSA-SHAKE).** Uses SHAKE-256 (the extendable-output variant of SHA-3) throughout:
- All hash functions (Th, PRF, H_msg, F) are instantiated as SHAKE-256 with appropriate prefixes for domain separation
- This provides conceptual simplicity (one primitive does everything) and benefits from platforms with Keccak hardware acceleration
- The sponge construction of Keccak provides natural domain separation through its capacity

**Haraka (optional/non-standard).** Haraka is a short-input hash function based on AES round functions, designed specifically for hash-based signatures. It achieves very high throughput on platforms with AES-NI acceleration but is not part of the FIPS 205 standard. Some SPHINCS+ implementations offer it as an optional instantiation for performance-critical applications.

**Choosing between instantiations.** On platforms with SHA-NI (Intel Ice Lake and later, AMD Zen 3 and later), the SHA-256 instantiation typically provides better performance. On platforms without SHA-NI but with general-purpose AES-NI support, SHAKE can be competitive. On platforms with dedicated SHA-3 hardware (certain embedded security controllers), SHAKE is preferred. The security level is identical for both instantiations given the same parameter set.

## 7.8 Security Analysis

Hash-based signatures enjoy the strongest security arguments of any post-quantum signature scheme. This section examines the nature of these proofs, their tightness, and the known attack vectors.

### Tight Security Reductions

A security reduction shows that breaking the signature scheme implies breaking the underlying hash function. The **tightness** of this reduction — how much security is "lost" in the implication — directly affects the concrete security level.

For XMSS, the security reduction is remarkably tight. The reduction from XMSS to the underlying hash function properties loses only a factor of approximately q·l, where q is the number of signature queries and l is the number of WOTS+ chains. For typical parameters (q = 2^20, l = 67), this represents a loss of only about 26 bits — well within the security margin.

For SLH-DSA, the security proof is somewhat more complex due to the multi-layer structure and the few-time nature of FORS. The overall security loss depends on:
- The number of hypertree layers d (multiplicative loss per layer)
- The FORS security degradation as a function of the number of signatures per instance
- The multi-target security properties of the tweakable hash function

NIST's security analysis for SLH-DSA accounts for all these factors and confirms that the standardized parameter sets provide their claimed security levels with comfortable margins.

**Comparison with lattice-based reductions.** ML-DSA's security reduces to the Module-LWE problem, but the reduction involves a significant tightness gap. The concrete hardness of Module-LWE is estimated through extrapolation from the best known algorithms (BKZ, lattice sieving), which introduces uncertainty. Hash-based signatures avoid this uncertainty entirely: the concrete security of SHA-256 against preimage attacks is directly characterized by the hash output length, with no extrapolation needed.

### Multi-Target Attacks

In many deployment scenarios, an adversary can observe signatures from millions of different signers or on millions of different messages. This creates a **multi-target** attack surface: rather than needing to break one specific hash chain, the adversary succeeds if they break any one of millions of instances.

**The threat.** Consider an adversary targeting N different WOTS+ public keys. For a standard hash function, finding a preimage for any one of N random targets costs approximately 2^n / N hash evaluations (a factor-N speedup over single-target attacks). For N = 2^40 (a billion signers), this reduces 256-bit security to 216-bit security.

**Mitigation through tweakable hash functions.** SLH-DSA's use of tweakable hash functions eliminates multi-target advantages. Because each hash evaluation incorporates a unique address (specifying the tree layer, tree index, chain index, and chain position), hash values computed for different signers or different positions within the same signature are effectively independent. An adversary cannot combine effort across different positions.

Formally, the SM-SPR (single-function multi-target second preimage resistance) property guarantees that even with access to many targets, the adversary's advantage is no better than for a single target. This is achieved because the address effectively makes each position's hash function independent, so parallelism across targets provides no benefit.

**Public seed's role.** Each SLH-DSA key pair includes a public seed PK.seed that is incorporated into all hash computations. Different signers have different public seeds with overwhelming probability, ensuring cryptographic independence between their hash function instances.

### Fault Attacks

Physical attacks on hash-based signature implementations present a distinct threat model from purely computational attacks. Fault injection — using voltage glitches, electromagnetic pulses, or laser beams to cause computational errors — can compromise hash-based signatures in several ways:

**WOTS+ chain faults.** If an attacker can induce a fault during WOTS+ signing that causes the hash chain computation to skip a step, the resulting signature contains a chain value at an incorrect position. By comparing the faulted signature with a correct signature on a different message, the attacker may be able to derive chain values at positions that should never have been revealed, potentially enabling forgery.

**Merkle tree computation faults.** Faulting the authentication path computation could cause the signer to output incorrect sibling values. While this doesn't directly enable forgery, it can reveal information about the tree structure that aids other attacks.

**FORS index manipulation.** If the message hash computation is faulted such that the FORS indices are modified, the resulting signature reveals secret values at unintended positions. Combined with a correct signature on the same message, this can reveal additional FORS secret values, accelerating forgery.

**Countermeasures:**
- **Signature verification before release:** The signer verifies each signature against the public key before outputting it. Any fault that corrupts the signature will cause verification to fail, preventing the faulted signature from being released.
- **Redundant computation:** Critical computations (especially hash chain evaluations) are performed twice and compared, detecting single faults.
- **Protected implementations:** Using hardware countermeasures such as dual-rail logic, error-detecting codes on intermediate values, or computation in protected memory regions.

For software implementations on general-purpose hardware, signature verification before release is the most practical countermeasure, adding only modest performance overhead (verification is typically faster than signing).

### Side-Channel Attacks

Hash-based signatures have relatively favorable side-channel properties compared to algebraic schemes:

- Hash functions have regular, data-independent control flow (no branching on secret data)
- Memory access patterns during hash computation are typically independent of the input
- The main side-channel risk is the secret key derivation step, where SK.seed is used

However, the address computation and tree traversal may leak information about which leaf index is being used. For stateless schemes like SLH-DSA, this information is derivable from the signature itself (the index is part of the signature), so it does not represent an additional vulnerability. For stateful schemes, leaking the current index is less concerning than leaking key material, but may still be undesirable in some threat models.

## 7.9 Use Cases for Hash-Based Signatures

The performance and size characteristics of hash-based signatures make them ideal for some applications and poorly suited for others. This section provides concrete guidance for practitioners.

### Ideal Applications

**Firmware and software signing.** Hash-based signatures are exceptionally well-suited for signing firmware and software updates:
- Signatures are computed infrequently (at release time) in a controlled environment
- Verification happens on the device, where signature size is less critical (firmware images are already large)
- Long-term security is paramount: firmware may need to remain securely verified for 15–20 years
- Both stateful (XMSS/LMS) and stateless (SLH-DSA) schemes work well here
- NIST explicitly recommends LMS/XMSS for firmware signing as an immediate deployment option

**Certificate authority root and intermediate certificates.** CA signing keys are used in highly controlled HSM environments where state management is feasible:
- Root CAs sign infrequently (perhaps a few certificates per year)
- The security requirement is extreme: root key compromise affects all subordinate certificates
- Small signature sizes are less critical for certificates that are cached and reused
- Stateful schemes (LMS/XMSS) are ideal here due to their compact signatures and strong security

**Document notarization and timestamping.** For legal and archival purposes:
- Documents must remain verifiable for decades
- The conservative security assumptions of hash-based signatures provide maximum confidence against future cryptanalytic advances
- Signing volume is manageable (documents, not network packets)
- SLH-DSA provides the simplest deployment model (no state management)

**Code signing for package managers and repositories.** Similar to firmware signing:
- Controlled signing environment
- Moderate frequency (thousands of packages, not millions per second)
- Long-term verification requirement
- Both stateful and stateless schemes appropriate

**Trust anchor and root of trust initialization.** When establishing hardware or software roots of trust:
- The root public key is embedded once (small public key is beneficial)
- Verification is infrequent
- Maximum security confidence required
- SLH-DSA's 32-byte public key is actually smaller than ML-DSA's 1,312 bytes

### Less Ideal Applications

**TLS/HTTPS authentication.** Hash-based signatures present challenges for TLS:
- Each handshake requires signature transmission, and 17–50 KB signatures increase latency
- High-traffic servers may perform thousands of signatures per second, making SLH-DSA's 5–50 ms signing time problematic
- Certificate chains compound the size issue (multiple signatures per chain)
- ML-DSA's 2.4 KB signatures and sub-millisecond operations are strongly preferred here

**IoT and embedded devices.** Constrained environments face multiple challenges:
- Limited bandwidth for transmitting large signatures
- Limited RAM for verification (authentication path reconstruction requires buffering)
- Limited computational resources for the many hash evaluations required
- Battery-constrained devices penalized by hash computation energy cost

**Real-time and high-frequency signing.** Applications requiring microsecond-level signing latency:
- Financial trading systems
- Real-time authentication protocols
- High-throughput message authentication
- SLH-DSA's millisecond-scale signing is too slow; even ML-DSA may be marginal for some of these applications

**Bandwidth-constrained communications.** Applications where every byte counts:
- Satellite communications with limited downlink capacity
- Low-power wide-area networks (LoRaWAN, NB-IoT)
- Blockchain transactions where signature size directly affects costs
- DNS responses where UDP packet size is limited

### Hybrid Deployment Strategies

Given the complementary strengths of hash-based and lattice-based signatures, several hybrid strategies are emerging:

**Dual-signature approach.** Some high-security applications sign with both ML-DSA and SLH-DSA, providing redundancy against cryptanalytic breakthroughs in either assumption. The combined signature is larger but provides the intersection of both threat models' security.

**Algorithm selection by tier.** Organizations may use SLH-DSA for root certificates and long-lived trust anchors (maximum confidence) while using ML-DSA for entity certificates and session authentication (performance-sensitive). This leverages each scheme's strengths at the appropriate tier.

**Migration readiness.** Even organizations currently deploying ML-DSA may maintain SLH-DSA implementation readiness as a contingency against lattice cryptanalysis breakthroughs. The hash-only security assumption of SLH-DSA makes it the natural fallback position.

## 7.10 SLH-DSA vs. ML-DSA Selection Guidance

Choosing between SLH-DSA and ML-DSA is one of the most consequential decisions in post-quantum deployment. The following framework organizes the decision criteria:

### Choose SLH-DSA When:

**Security confidence is the primary requirement.** If the application demands the absolute highest confidence in long-term security — perhaps protecting national secrets, critical infrastructure, or information with multi-decade sensitivity — SLH-DSA's minimal assumption (hash function security) provides substantially higher confidence than ML-DSA's lattice-based assumptions.

**You need a cryptographic "insurance policy."** If your organization is primarily deploying ML-DSA but wants a fallback in case of lattice cryptanalysis breakthroughs, maintaining SLH-DSA capability provides this insurance at low operational cost.

**Public key size matters more than signature size.** SLH-DSA's 32-byte public key is dramatically smaller than ML-DSA's 1,312-byte public key. In applications where the public key is stored or transmitted repeatedly (embedded in hardware, cached in verifiers, included in certificate chains), SLH-DSA may actually require less total bandwidth despite larger signatures.

**Signing is infrequent but verification persistence matters.** For applications like certificate authorities, software signing, or document notarization, the signing performance penalty is irrelevant (signatures are created rarely in controlled environments), and the security benefit is paramount.

**Regulatory or compliance requirements specify hash-based schemes.** Some government and critical infrastructure standards specifically require or recommend hash-based signatures for certain use cases (e.g., CNSA 2.0 recommends LMS/XMSS for firmware signing).

### Choose ML-DSA When:

**Performance is a primary constraint.** If the application requires sub-millisecond signing, high throughput, or low latency, ML-DSA's order-of-magnitude performance advantage is decisive.

**Bandwidth is limited.** ML-DSA signatures (2.4 KB) are 3–20x smaller than SLH-DSA signatures (7.8–49.9 KB). For applications transmitting many signatures (TLS handshakes, blockchain transactions, API authentication), this difference is substantial.

**The application requires frequent signing.** High-volume signing (web servers, authentication systems, real-time protocols) strongly favors ML-DSA's fast signing.

**You are comfortable with lattice assumptions.** Module-LWE has been studied for decades, survives intensive cryptanalysis, and is supported by worst-case to average-case reductions. While not as conservative as hash-based assumptions, it provides strong evidence of security.

**Interoperability with the broader ecosystem.** ML-DSA is likely to become the default post-quantum signature in most protocols and libraries, making it the path of least resistance for interoperability.

### Decision Matrix

| Criterion | Favors SLH-DSA | Favors ML-DSA |
|-----------|----------------|---------------|
| Security assumption strength | Strong | Moderate |
| Signing speed | Slow (ms) | Fast (μs) |
| Verification speed | Moderate | Fast |
| Signature size | Large (8–50 KB) | Small (2.4 KB) |
| Public key size | Very small (32 B) | Moderate (1.3 KB) |
| Secret key size | Small (64 B) | Moderate (4 KB) |
| Implementation complexity | Moderate | Moderate |
| Maturity of assumption | Decades (hash functions) | Decades (lattices) |
| Standardization status | FIPS 205 | FIPS 204 |
| Quantum security confidence | Highest | High |

## 7.11 Implementation Considerations

### Constant-Time Implementation

Hash-based signatures have a natural advantage for constant-time implementation because hash functions themselves typically have data-independent control flow. However, implementers must still ensure:

- The leaf index derivation does not leak timing information about the message
- Memory access patterns during tree traversal do not reveal the authentication path indices
- The conditional operations in WOTS+ chain computation (determining when to stop) do not create timing variations

Modern implementations typically achieve constant-time behavior by always computing the full chain and selecting the appropriate intermediate value through constant-time conditional moves.

### Memory Requirements

SLH-DSA signing is memory-intensive due to the need to compute Merkle tree portions on the fly:

- Each tree layer requires storing one full tree level during computation (2^{h_layer} nodes)
- The authentication path construction requires temporary storage for sibling nodes
- FORS computation requires storing k tree computations simultaneously

For the "fast" parameter sets with short trees per layer, memory requirements are modest (tens of kilobytes). For "small" parameter sets with taller trees, memory usage can reach hundreds of kilobytes during signing. Verification is less memory-intensive, as it processes authentication paths sequentially.

### Parallelization Opportunities

Hash-based signature operations offer substantial parallelism:

- WOTS+ chain computations are independent across chains (l chains can be computed in parallel)
- FORS tree computations are independent across the k trees
- Merkle tree node computations at the same level are independent
- Different hypertree layers, once lower layers complete, can overlap in computation

Hardware implementations and multi-core software implementations can exploit this parallelism to significantly reduce wall-clock signing and verification times. On a 16-core processor, SLH-DSA signing can be 8–12x faster than single-threaded execution.

## 7.12 Key Takeaways

- Hash-based signatures rest on the minimal assumption that secure hash functions exist, providing the strongest security confidence of any post-quantum signature scheme.

- The construction builds upward from simple primitives: Lamport one-time signatures demonstrate feasibility, Winternitz chains compress signatures through the time-space trade-off parameter w, and Merkle trees aggregate many key pairs under a single public key.

- FORS provides the few-time signature capability that enables stateless operation, tolerating a bounded number of key reuses with quantifiable security degradation.

- Stateful schemes (XMSS, LMS) offer compact signatures (~2.5 KB) and fast operations but impose strict state management requirements that limit their applicability to controlled environments like HSMs, firmware signing, and certificate authorities.

- Stateless SLH-DSA eliminates the state management burden through a hypertree architecture with deterministic leaf selection, at the cost of larger signatures (8–50 KB) and slower signing (milliseconds rather than microseconds).

- SLH-DSA is standardized as FIPS 205 with six parameter sets spanning three security levels and two performance profiles, offering flexibility for different deployment scenarios.

- The security proofs for hash-based signatures are tight, meaning that the concrete security closely matches the theoretical guarantees with minimal loss factors.

- Hash function instantiations (SHA-256 or SHAKE-256) determine implementation characteristics and hardware acceleration availability without affecting the security argument.

- Hash-based signatures are ideal for high-security, low-frequency signing (firmware, certificates, documents) and serve as the conservative fallback against potential breakthroughs in lattice cryptanalysis.

- The choice between SLH-DSA and ML-DSA should be driven by the specific application's requirements for security confidence, performance, bandwidth, and operational environment.

---

*Next: [Chapter 8 — Multivariate Polynomial Cryptography](./08-multivariate.md)*
