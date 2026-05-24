# Chapter 12: FIPS 204 — ML-DSA (Module-Lattice Digital Signature Algorithm)

## 12.1 Overview

ML-DSA (Module-Lattice-Based Digital Signature Algorithm), standardized as FIPS 204 by NIST in August 2024, is the primary post-quantum digital signature standard selected through NIST's multi-year Post-Quantum Cryptography Standardization Process. Derived from the CRYSTALS-Dilithium submission, ML-DSA represents the culmination of over a decade of research into practical lattice-based signature schemes. It provides existential unforgeability under chosen-message attacks (EUF-CMA), the standard security notion for digital signatures, meaning that an adversary who can adaptively obtain signatures on messages of their choice still cannot produce a valid signature on any new message not previously queried.

The mathematical foundation of ML-DSA rests on two well-studied computational problems over module lattices: the Module Learning With Errors (Module-LWE) problem and the Module Short Integer Solution (Module-SIS) problem. These problems generalize their "plain" lattice counterparts by working over the polynomial ring R_q = Z_q[X]/(X^256 + 1), where operations on polynomials can be performed efficiently using the Number Theoretic Transform (NTT). The module structure provides a careful middle ground between efficiency (achieved through algebraic structure) and security (maintained by working with modules of dimension greater than one, avoiding the potential risks of purely ring-based constructions).

The signature scheme follows the Fiat-Shamir with Aborts paradigm, originally introduced by Vadim Lyubashevsky in 2009 and refined in subsequent works. This paradigm transforms a lattice-based identification protocol into a full signature scheme while using rejection sampling to eliminate any information leakage about the secret key from the produced signatures. The "aborts" mechanism is what distinguishes ML-DSA from naive lattice-based Schnorr-like constructions and is essential for achieving provable security.

ML-DSA is positioned as the general-purpose signature algorithm in NIST's post-quantum portfolio. It offers the best overall balance of signature size, key size, signing speed, and verification speed among the standardized options, making it suitable for the widest range of applications from TLS certificate authentication to code signing and document signatures.

## 12.2 Design Philosophy: Fiat-Shamir with Aborts

### The Classical Fiat-Shamir Transform

The Fiat-Shamir heuristic, introduced by Amos Fiat and Adi Shamir in 1986, is a foundational technique that converts an interactive three-round public-coin identification protocol (a sigma protocol) into a non-interactive signature scheme. The transformation works as follows:

1. **Commit:** The prover generates internal randomness and computes a commitment value w. In the interactive setting, this is sent to the verifier.
2. **Challenge:** In the interactive protocol, the verifier would send a random challenge c. In the Fiat-Shamir transformation, the challenge is instead derived deterministically as c = H(message || w), where H is a cryptographic hash function modeled as a random oracle. This binds the challenge to both the message being signed and the commitment.
3. **Response:** The prover computes a response z using the secret key, the commitment randomness, and the challenge. The pair (w, z) or equivalently (c, z) constitutes the signature.

Verification reconstructs the commitment from the response and public key, then checks that the hash of the message and reconstructed commitment matches the challenge. This paradigm has been extraordinarily successful, underpinning schemes like Schnorr signatures, which form the basis of Ed25519 and similar elliptic curve signature schemes.

### Why Naive Lattice Signatures Fail

A natural first attempt at constructing a lattice-based signature applies the Fiat-Shamir transform directly to a lattice-based identification scheme, analogous to how Schnorr signatures work over discrete-logarithm groups. Consider the following naive construction:

- **Key Generation:** Sample a random matrix **A** ∈ R_q^{k×ℓ}, sample a short secret vector **s** ∈ R_q^ℓ with small coefficients, and compute the public key **t** = **A**·**s**.
- **Commitment:** Sample a random masking vector **y** with moderately-sized coefficients, compute the commitment **w** = **A**·**y**.
- **Challenge:** Compute c = H(message, **w**) and interpret c as a polynomial with small coefficients.
- **Response:** Compute **z** = **y** + c·**s** and output (c, **z**) as the signature.

Verification checks that **A**·**z** - c·**t** = **A**·(**y** + c·**s**) - c·**A**·**s** = **A**·**y** = **w**, then verifies the hash.

The fatal flaw in this construction lies in the response computation **z** = **y** + c·**s**. While **y** is sampled freshly for each signature, the term c·**s** introduces a bias in the distribution of **z** that depends on the secret key **s**. Specifically, the covariance of **z** correlates with **s**. After observing sufficiently many signatures (on the order of n signatures for a dimension-n scheme), an attacker can perform statistical analysis to recover **s** with high probability. This is fundamentally different from the discrete-logarithm setting where the group structure automatically provides the necessary statistical hiding.

The leakage is subtle but devastating. Each signature reveals the vector **z** = **y** + c·**s**, where c is known (it is part of the signature) and **y** is drawn from some distribution. The conditional distribution of **z** given c shifts by c·**s**, and averaging over many signatures with known challenges allows recovery of **s** through lattice reduction or simple linear algebra on the covariance matrix.

### The Abort Solution: Lyubashevsky's Framework

ML-DSA employs rejection sampling (the "abort" mechanism) to completely decouple the distribution of output signatures from the secret key. The key insight, due to Lyubashevsky, is elegant: rather than outputting every computed response, the signer checks whether the response "looks like" it could have been generated without knowledge of the secret key. If it does not, the signer discards the attempt and tries again with fresh randomness.

More precisely, the signing procedure operates as follows:

1. Sample the masking vector **y** uniformly from a large range [-γ₁+1, γ₁].
2. Compute the response **z** = **y** + c·**s₁**.
3. Apply rejection sampling: output **z** only if its infinity norm is strictly less than γ₁ - β. If any coefficient of **z** exceeds this bound, reject and restart with a new **y**.
4. Additionally, check that the low-order bits of the commitment do not become too large (which would indicate that the response is close to a "boundary" that could leak information).

The rejection bound γ₁ - β is chosen so that the acceptance probability is reasonably high (roughly 1/e ≈ 0.37 per attempt for well-chosen parameters, leading to an average of about 4-7 iterations), while simultaneously ensuring that the conditional distribution of accepted **z** values is statistically close to the uniform distribution over the appropriate range, regardless of what secret key was used.

This achieves a strong zero-knowledge property: given only the public key and a collection of valid signatures, no adversary can distinguish which of the many possible secret keys (all consistent with the public key) was actually used to generate those signatures. The signatures carry essentially zero information about the specific secret key beyond what is already revealed by the public key itself.

The technique can be understood through an analogy: imagine a biased coin that tends to land on heads. If you want to simulate a fair coin using this biased coin, you can flip the biased coin and sometimes "reject" the result (reflip) according to a carefully chosen rule. The outputs you do accept will follow the uniform distribution, even though the underlying mechanism is biased. Rejection sampling in ML-DSA applies this same principle to multivariate polynomial distributions.

## 12.3 Parameter Sets

ML-DSA defines three parameter sets targeting different NIST security levels:

| Parameter | ML-DSA-44 | ML-DSA-65 | ML-DSA-87 |
|-----------|----------|----------|----------|
| NIST Security Level | 2 | 3 | 5 |
| Classical security target | AES-128 equivalent | AES-192 equivalent | AES-256 equivalent |
| (k, ℓ) — matrix dimensions | (4, 4) | (6, 5) | (8, 7) |
| n — polynomial degree | 256 | 256 | 256 |
| q — modulus | 8,380,417 | 8,380,417 | 8,380,417 |
| d — dropped bits in t | 13 | 13 | 13 |
| τ — challenge weight (non-zero coefficients) | 39 | 49 | 60 |
| γ₁ — masking vector range | 2^17 = 131,072 | 2^19 = 524,288 | 2^19 = 524,288 |
| γ₂ — decomposition parameter | (q-1)/88 = 95,232 | (q-1)/32 = 261,888 | (q-1)/32 = 261,888 |
| η — secret coefficient range | 2 | 4 | 2 |
| β — rejection norm bound (= τ·η) | 78 | 196 | 120 |
| ω — maximum hint weight | 80 | 55 | 75 |
| Public key size | 1,312 bytes | 1,952 bytes | 2,592 bytes |
| Secret key size | 2,560 bytes | 4,032 bytes | 4,896 bytes |
| Signature size | 2,420 bytes | 3,309 bytes | 4,627 bytes |

The naming convention encodes the matrix dimensions: "ML-DSA-44" uses a 4×4 module (k=4, ℓ=4), "ML-DSA-65" uses a 6×5 module (k=6, ℓ=5), and "ML-DSA-87" uses an 8×7 module (k=8, ℓ=7).

**Understanding the parameter relationships:** The modulus q = 8,380,417 = 2^23 - 2^13 + 1 is chosen specifically because it is a prime congruent to 1 modulo 2·256 = 512, which enables efficient NTT computations of degree-256 polynomials. The decomposition parameter γ₂ divides (q-1) exactly, facilitating the high-bits/low-bits decomposition that enables the hint mechanism. The rejection bound β = τ·η represents the maximum infinity norm that the product c·**s₁** can achieve (since c has exactly τ non-zero ±1 coefficients, and each coefficient of **s₁** is bounded by η in absolute value).

**Security level rationale:** ML-DSA-44 targets NIST Level 2, meaning it is at least as hard to break as AES-128 against a quantum adversary. This is the minimum recommended level for new deployments. ML-DSA-65 at Level 3 provides a comfortable margin and is recommended as the default choice for most applications. ML-DSA-87 at Level 5 provides the highest security margin and is intended for applications requiring the utmost long-term assurance or regulatory compliance with the highest tiers.

## 12.4 Algorithm Description

### Key Generation (ML-DSA.KeyGen)

Key generation produces a public-private key pair from 32 bytes of random seed material:

```
ML-DSA.KeyGen():
1.  ξ ← Random(32)                          // Sample 32 bytes of entropy
2.  (ρ, ρ', K) ← H(ξ)                      // Expand seed into three components:
                                             //   ρ (32B): seed for public matrix A
                                             //   ρ' (64B): seed for secret vectors
                                             //   K (32B): signing key component
3.  Â ← ExpandA(ρ)                          // Generate matrix A ∈ R_q^{k×ℓ} in NTT domain
4.  (s₁, s₂) ← ExpandS(ρ')                 // Sample secret vectors:
                                             //   s₁ ∈ R_q^ℓ, coefficients in [-η, η]
                                             //   s₂ ∈ R_q^k, coefficients in [-η, η]
5.  t ← NTT⁻¹(Â · NTT(s₁)) + s₂           // Compute t = A·s₁ + s₂
6.  (t₁, t₀) ← Power2Round(t, d)           // Decompose: t = t₁·2^d + t₀
7.  pk ← (ρ, t₁)                           // Public key: matrix seed + high bits of t
8.  tr ← H(pk)                             // Public key hash (for binding)
9.  sk ← (ρ, K, tr, s₁, s₂, t₀)           // Secret key: includes low bits of t
10. return (pk, sk)
```

The Power2Round decomposition in step 6 splits each coefficient of **t** into high-order bits (t₁) and low-order bits (t₀), keeping only d=13 bits in the low part. The public key contains only t₁, reducing its size while retaining enough information for verification. The full precision t₀ is stored in the secret key and used during signing to compute the hint vector.

The matrix **A** is generated pseudorandomly from the seed ρ using an extendable output function (XOF). Since ρ is part of the public key, any party can regenerate **A** from the public key alone, which is essential for verification. This "seed-based" representation is standard in lattice cryptography and dramatically reduces key sizes compared to storing the full matrix.

### Signing (ML-DSA.Sign)

The signing algorithm implements the Fiat-Shamir with Aborts paradigm. It may require multiple iterations before producing a valid signature:

```
ML-DSA.Sign(sk, M, ctx):
1.  Parse sk as (ρ, K, tr, s₁, s₂, t₀)
2.  Â ← ExpandA(ρ)                          // Regenerate A in NTT domain
3.  μ ← H(tr ‖ M)                          // Message representative (binds pk to msg)
4.  ρ' ← H(K ‖ rnd ‖ μ)                    // Commitment seed:
                                             //   rnd = random (hedged) or zeros (deterministic)
5.  κ ← 0                                   // Nonce/attempt counter
6.  (z, h) ← ⊥                             // Will hold the signature components
7.  while (z, h) = ⊥:                       // Rejection sampling loop
    a.  y ← ExpandMask(ρ', κ)              // Masking vector ∈ [-γ₁+1, γ₁]^{256·ℓ}
    b.  w ← NTT⁻¹(Â · NTT(y))             // Compute commitment w = A·y
    c.  w₁ ← HighBits(w, 2γ₂)             // Extract high-order bits
    d.  c̃ ← H(μ ‖ w₁)                     // Hash to get challenge seed
    e.  c ← SampleInBall(c̃)                // Sparse challenge polynomial:
                                             //   exactly τ coefficients are ±1, rest are 0
    f.  ĉ ← NTT(c)
    g.  z ← y + NTT⁻¹(ĉ · NTT(s₁))       // Candidate response: z = y + c·s₁
    h.  if ‖z‖∞ ≥ γ₁ - β:                  // REJECTION CHECK 1:
            (z, h) ← ⊥; κ++; continue       //   Response too large → abort
    i.  r₀ ← LowBits(NTT⁻¹(Â·NTT(z)) - c·t, 2γ₂)
    j.  if ‖r₀‖∞ ≥ γ₂ - β:                // REJECTION CHECK 2:
            (z, h) ← ⊥; κ++; continue       //   Low bits too large → abort
    k.  h ← MakeHint(-c·t₀, w - c·s₂ + c·t₀)  // Compute hint vector
    l.  if ‖c·t₀‖∞ ≥ γ₂ or ones(h) > ω:   // REJECTION CHECK 3:
            (z, h) ← ⊥; κ++; continue       //   Hint too heavy → abort
    m.  κ ← κ + 1
8.  σ ← (c̃, z, h)                          // Signature
9.  return σ
```

The three rejection checks serve distinct purposes:
- **Check 1** (line h) ensures the response **z** is small enough that it could plausibly have come from a uniform distribution over [-γ₁+1, γ₁], regardless of the secret key.
- **Check 2** (line j) ensures the low-order bits of the reconstructed commitment remain bounded, preventing information leakage through the decomposition.
- **Check 3** (line l) ensures the hint vector h is sparse enough (at most ω ones) to fit within the allocated signature space and prevents leakage through the hint.

### Verification (ML-DSA.Verify)

Verification is deterministic and substantially faster than signing:

```
ML-DSA.Verify(pk, M, σ, ctx):
1.  Parse pk as (ρ, t₁)
2.  Parse σ as (c̃, z, h)
3.  Â ← ExpandA(ρ)                          // Regenerate A (same as in KeyGen/Sign)
4.  tr ← H(pk)                             // Compute public key hash
5.  μ ← H(tr ‖ M)                          // Recompute message representative
6.  c ← SampleInBall(c̃)                    // Reconstruct challenge polynomial
7.  w₁' ← UseHint(h, NTT⁻¹(Â·NTT(z) - NTT(c)·NTT(t₁·2^d)))
                                             // Recover high bits using hint
8.  Verify: ‖z‖∞ < γ₁ - β                  // Response within bounds
9.  Verify: ones(h) ≤ ω                     // Hint weight valid
10. Verify: c̃ = H(μ ‖ w₁')                 // Challenge consistency check
11. return (all checks pass)
```

The critical operation in verification is step 7, which computes **A**·**z** - c·**t₁**·2^d and uses the hint h to recover the same high-order bits w₁ that were computed during signing. The hint corrects for the discrepancy introduced by using only the high bits t₁ of the public key (rather than the full vector t = t₁·2^d + t₀).

## 12.5 Key Mechanisms Explained

### Rejection Sampling: Purpose and Theory

The rejection sampling mechanism is the central innovation that makes lattice-based signatures secure. To understand it deeply, consider what happens without rejection:

If the signer always outputs **z** = **y** + c·**s₁** without any checks, the expected value of **z** conditioned on a known challenge c is E[**z** | c] = E[**y**] + c·**s₁** = c·**s₁** (since **y** has zero mean). An attacker who collects multiple signatures with their associated challenges can compute:

E[**z** · c^T] = E[(**y** + c·**s₁**) · c^T] = **s₁** · E[c · c^T]

Since the challenges c are known (they are part of the signature), this system of equations can be solved for **s₁** after collecting sufficiently many samples. In practice, only O(n) signatures are needed for full key recovery.

With rejection sampling, the accepted values of **z** follow a distribution that is statistically independent of **s₁**. The formal guarantee is that for any two secret keys **s₁** and **s₁'** (both consistent with the same public key), the distributions of accepted signatures are statistically close — within distance 2^{-256} or less. This makes the attack described above completely ineffective.

The rejection probability depends on the parameters but is typically around 70-85% per iteration. This means the geometric distribution of the number of attempts has an expected value of roughly 4-7 iterations depending on the parameter set. While this introduces variability in signing time, the expected time is well-bounded and the probability of requiring more than 20 iterations is negligible (less than 2^{-10}).

### The Hint Vector: Bridging Precision Gaps

The hint vector h is a subtle but crucial efficiency optimization. To understand its role, consider the verification equation. The verifier needs to check that the commitment matches the challenge, but faces a precision problem:

- During signing, the commitment **w** = **A**·**y** is computed from the exact masking vector **y**.
- During verification, the verifier does not know **y** but can compute **A**·**z** - c·**t** = **A**·**y** - c·**s₂** (using the relationship **t** = **A**·**s₁** + **s₂**).
- Furthermore, the public key only contains t₁ (the high bits of **t**), so the verifier actually computes **A**·**z** - c·t₁·2^d, which differs from **A**·**y** by c·**s₂** + c·t₀.

The high-order bits HighBits(**A**·**z** - c·t₁·2^d) may differ from HighBits(**A**·**y**) = w₁ at some positions due to carries from the discarded low-order bits. The hint h encodes exactly which positions differ, allowing the verifier to "correct" its computation and recover w₁ exactly.

The hint is encoded as a binary vector indicating which positions need correction. Its weight (number of ones) is bounded by ω, which is chosen so that the probability of exceeding this bound is negligible for honest signers but would require finding short vectors for a forger. The hint occupies k·256 bits in the worst case but is compressed using the weight bound.

### Deterministic vs. Hedged Signing

ML-DSA supports two signing modes that differ in how the nonce seed ρ' is generated:

**Deterministic signing:** The nonce seed is computed as ρ' = H(K ‖ 0^32 ‖ μ), where the 32 zero bytes replace what would be random bytes. This means the same key signing the same message always produces the same signature. Benefits include:
- Reproducibility for testing and auditing
- No dependency on a random number generator during signing
- Immunity to RNG failures (a common failure mode in embedded systems)
- Simplified implementation with fewer failure modes

**Hedged (randomized) signing:** The nonce seed incorporates 32 bytes of fresh randomness: ρ' = H(K ‖ rnd ‖ μ) where rnd ← Random(32). This provides:
- Protection against differential fault analysis (DFA), where an attacker induces faults during computation and compares faulty signatures with correct ones
- Side-channel resistance through randomization — each signing operation uses different intermediate values
- Defense against hypothetical hash function weaknesses that might allow prediction of deterministic nonces
- Protection against "rowhammer" style attacks that might flip bits in deterministic computations

FIPS 204 mandates the hedged variant for general use because the additional protections against physical attacks are considered essential for hardware implementations. Deterministic signing remains available for constrained environments or applications where reproducibility is required.

### The Challenge Polynomial

The challenge c is constructed with specific structure that enables the security proof and bounds the rejection probability:

- c is a polynomial of degree 255 (in R_q = Z_q[X]/(X^256 + 1))
- Exactly τ coefficients are non-zero, each being +1 or -1
- The remaining 256 - τ coefficients are zero
- The non-zero positions and signs are derived from the challenge hash c̃ using a rejection sampling procedure (SampleInBall)

This sparsity is critical: since c·**s₁** has infinity norm at most τ·η = β (because c has at most τ non-zero ±1 entries and **s₁** has coefficients bounded by η), the rejection bound γ₁ - β determines the acceptance probability. If c were a general polynomial with larger coefficients, the product c·**s₁** would be much larger, requiring either a much larger γ₁ (increasing signature size) or suffering much lower acceptance probability.

The SampleInBall algorithm uses the hash output c̃ as a seed to generate the positions and signs through a Fisher-Yates-like shuffle, ensuring uniform distribution over the set of all polynomials with exactly τ non-zero ±1 coefficients.

## 12.6 Security Analysis

### Module-LWE and Module-SIS Hardness

ML-DSA's security is formally reduced to two computational problems over module lattices:

**Module-LWE (MLWE_{k,ℓ,η}):** Given a random matrix **A** ∈ R_q^{k×ℓ} and a vector **t** ∈ R_q^k, distinguish whether **t** = **A**·**s** + **e** (for short secrets **s**, **e** with coefficients in [-η, η]) or **t** is uniformly random. This problem protects the secret key: recovering **s₁** from (A, t = A·s₁ + s₂) is at least as hard as solving MLWE.

**Module-SIS (MSIS_{k,ℓ+1,β'}):** Given **A** ∈ R_q^{k×ℓ}, find a short non-zero vector **v** ∈ R_q^{ℓ+1} such that [**A** | **I**]·**v** = 0 and ‖**v**‖ ≤ β'. This problem protects against forgery: producing a valid signature without the secret key requires solving an MSIS instance.

The module structure (working over R_q^{k×ℓ} rather than Z_q^{n×m}) provides a factor of 256 efficiency improvement (since each ring element encodes 256 coefficients) while maintaining security. The best known attacks against module lattice problems scale with the total dimension n·k (or n·ℓ), and no attack exploiting the special ring structure X^256 + 1 is known to provide more than a small constant factor improvement.

### Provable Security: EUF-CMA in the (Q)ROM

ML-DSA achieves EUF-CMA security in the Quantum Random Oracle Model (QROM), meaning security holds even if the adversary can evaluate the hash function in quantum superposition. The security proof proceeds through a sequence of game hops:

1. Replace the hash function with a random oracle (standard model to ROM)
2. Show that any forger must either solve MLWE (to recover the key) or MSIS (to forge directly)
3. The "lossy mode" technique handles the adaptive nature of chosen-message attacks
4. The QROM reduction accounts for quantum access to the random oracle using techniques such as the "compressed oracle" framework

The concrete security loss in the QROM reduction is larger than in the classical ROM (roughly a factor of q_H, the number of hash queries), which motivates the relatively conservative parameter choices.

### Concrete Security Estimates

The security of ML-DSA parameter sets is evaluated against the best known classical and quantum attacks:

| Parameter Set | Classical BKZ Cost | Quantum BKZ Cost | NIST Level | Equivalent Symmetric |
|--------------|-------------------|-----------------|-----------|---------------------|
| ML-DSA-44 | ~2^128 gates | ~2^115 gates | 2 | AES-128 |
| ML-DSA-65 | ~2^192 gates | ~2^170 gates | 3 | AES-192 |
| ML-DSA-87 | ~2^256 gates | ~2^225 gates | 5 | AES-256 |

These estimates are based on the "Core-SVP" methodology, which estimates the cost of the BKZ lattice reduction algorithm using the best known quantum speedups for the underlying SVP oracle (such as Grover-accelerated sieving). The quantum estimates assume access to a large-scale fault-tolerant quantum computer running optimized lattice sieving algorithms.

The security margin between classical and quantum estimates (roughly 10-15%) reflects the current understanding of quantum speedups for lattice problems, which are more modest than the quadratic speedup Shor's algorithm provides for factoring.

### Known Attack Vectors and Cryptanalysis

**1. Primal attack (key recovery via lattice reduction):**
The attacker constructs a lattice from the public matrix **A** and target vector **t**, then applies BKZ (Block Korzlov-Zolotarev) reduction to find the short secret vectors **s₁**, **s₂**. The cost scales exponentially with the lattice dimension and inversely with the ratio of the secret norm to the lattice determinant. This is the most relevant attack and determines parameter selection.

**2. Dual attack:**
Rather than finding the secret directly, the attacker finds a short vector in the dual lattice that can serve as a distinguisher between MLWE samples and random. Recent work has refined dual attack estimates, with some analyses suggesting slightly better performance than the primal attack in certain regimes, though this remains debated in the community.

**3. Forgery via Module-SIS:**
An attacker attempts to directly construct a valid signature (c̃, **z**, h) without knowing the secret key. This requires finding a short vector **z** and challenge c such that the verification equation holds. The MSIS hardness ensures this is infeasible.

**4. Hybrid attacks:**
Combining lattice reduction with combinatorial search (e.g., guessing some coordinates of the secret, then reducing a lower-dimensional lattice). These attacks are considered in parameter selection and do not provide significant advantages for ML-DSA parameters.

**5. Algebraic attacks exploiting ring structure:**
The ring R_q = Z_q[X]/(X^256+1) has algebraic structure (it is the 512th cyclotomic ring). No practical attack exploiting this structure is known for the module dimensions used in ML-DSA. The module structure (k,ℓ > 1) provides additional protection compared to pure ring-based schemes.

**6. Side-channel and fault attacks:**
These are implementation-dependent rather than algorithmic. The most significant risks include timing attacks on the rejection sampling loop (mitigated by constant-time implementation), power analysis of NTT operations (mitigated by masking), and fault attacks on deterministic signing (mitigated by the hedged mode).

## 12.7 Implementation Guidance

### Constant-Time Programming Requirements

Side-channel resistance demands that the execution time and memory access patterns of the signing algorithm be independent of secret data. The following operations are critical:

**NTT and polynomial arithmetic:** All butterfly operations in the NTT must execute in constant time. Barrett or Montgomery reduction must avoid conditional branches. Coefficient-wise operations (addition, subtraction, multiplication modulo q) must use constant-time modular arithmetic. On platforms without hardware multipliers of sufficient width, careful implementation is needed to avoid timing variations.

**Norm computation and comparison:** The infinity norm check ‖**z**‖∞ ≥ γ₁ - β must be computed without early termination. A naive implementation might return true as soon as any coefficient exceeds the bound, leaking information about which coefficient was "bad" (and thus about the secret). Instead, all coefficients must be checked and the results combined through bitwise operations.

**Rejection decision:** The boolean decision of whether to accept or reject must be computed in constant time, with both code paths (accept/continue) taking the same time. The counter κ and the fact of rejection are not secret (the number of attempts is observable through timing regardless), but intermediate values from rejected attempts must be securely erased.

**Hint computation:** The MakeHint function compares values derived from the secret (specifically c·**s₂** and c·**t₀**) and must not leak these through memory access patterns or timing.

**Hash function calls:** The underlying hash (SHAKE-256 for the XOF operations) must be implemented in constant time. Most standard library implementations already satisfy this requirement, but verification is important.

### Managing the Rejection Loop

The signing loop presents unique implementation challenges:

**Timing variability:** The number of loop iterations varies between signatures (average 4-7, but occasionally much more). This timing variation is considered acceptable because the iteration count does not depend on the secret key — it depends only on the (random) masking vector **y** and the (publicly derivable) challenge c. An attacker observing timing cannot learn anything about the secret beyond what is already public.

**Memory management:** Each rejected iteration produces intermediate values (the candidate **z**, partial computations of **w**, etc.) that must be securely zeroed before the next iteration. Failure to clear these values could allow a memory-scanning attacker to recover rejected candidates, which do carry information about the secret key.

**Maximum iterations:** While the expected number of iterations is small, there is no hard upper bound. Implementations must handle the (astronomically unlikely) case of very many iterations gracefully, without buffer overflows or integer overflow in the counter κ. In practice, limiting to 1000 iterations and returning an error is acceptable — the probability of exceeding this is less than 2^{-100}.

**Streaming vs. batch processing:** Implementations can either regenerate the matrix **A** for each signature (lower memory) or cache it (lower computation). Since **A** depends only on the public seed ρ, it can be precomputed once per key pair and reused across all signing operations.

### Random Number Generation Requirements

**Key generation:** Requires 32 bytes (256 bits) of entropy from a cryptographically secure random number generator. This is the most critical randomness in the system — compromise of this entropy compromises all future operations with the resulting key.

**Hedged signing:** Requires 32 bytes of fresh randomness per signature. The quality requirements are less stringent than for key generation: even partially predictable randomness provides some fault-attack protection (the attacker cannot precisely predict the internal state). However, best practice demands full-quality randomness.

**Deterministic signing:** No randomness is needed during signing operations. The nonce is derived entirely from the secret key component K and the message. This mode is particularly valuable for environments where RNG quality is uncertain (embedded devices, early boot stages, virtual machines with limited entropy).

**RNG failure modes:** Unlike ECDSA (where RNG failure in signing leads to immediate key compromise), ML-DSA's hedged mode degrades gracefully under RNG failure. If the RNG produces constant output, the scheme reduces to deterministic signing. If the RNG is partially biased, the rejection sampling still provides security — the bias can only affect the fault-attack protection, not the core EUF-CMA security.

### Batch Verification

When multiple signatures need verification (common in blockchain, certificate chains, and bulk document processing), batch verification provides significant speedups:

**Technique:** Given n signatures (pk_i, M_i, σ_i), verify them simultaneously using random linear combinations:
1. Choose random weights α₁, ..., αₙ
2. Compute the combined verification equation using a single large matrix-vector product
3. Check the combined result

**Correctness:** If all signatures are valid, the combined check passes. If any signature is invalid, the combined check fails with overwhelming probability (at least 1 - 1/q per invalid signature).

**Speedup:** The dominant cost in verification is the matrix-vector product **A**·**z**. By batching, the n individual products can be replaced with fewer operations, yielding 2-4x speedup for batches of 10-20 signatures, with diminishing returns beyond that.

**Failure handling:** If batch verification fails, the verifier must identify which signature(s) are invalid. This can be done through binary search (log₂(n) batch verifications) or sequential fallback.

## 12.8 Performance Characteristics

### Operation Timing

Performance measurements on modern hardware (Intel x86-64 with AVX2 vector instructions, 3.5 GHz):

| Operation | ML-DSA-44 | ML-DSA-65 | ML-DSA-87 |
|-----------|----------|----------|----------|
| KeyGen | ~150 μs | ~250 μs | ~400 μs |
| Sign (average) | ~700 μs | ~1,100 μs | ~1,500 μs |
| Sign (worst 1%) | ~2,500 μs | ~4,000 μs | ~5,500 μs |
| Verify | ~175 μs | ~280 μs | ~420 μs |
| Batch Verify (per sig, n=32) | ~90 μs | ~140 μs | ~210 μs |

On ARM platforms (Cortex-A72, 1.5 GHz, without NEON optimization):

| Operation | ML-DSA-44 | ML-DSA-65 | ML-DSA-87 |
|-----------|----------|----------|----------|
| KeyGen | ~400 μs | ~650 μs | ~1,000 μs |
| Sign (average) | ~1,800 μs | ~2,800 μs | ~3,900 μs |
| Verify | ~450 μs | ~700 μs | ~1,100 μs |

On constrained platforms (ARM Cortex-M4, 168 MHz):

| Operation | ML-DSA-44 | ML-DSA-65 | ML-DSA-87 |
|-----------|----------|----------|----------|
| KeyGen | ~10 ms | ~18 ms | ~30 ms |
| Sign (average) | ~40 ms | ~70 ms | ~100 ms |
| Verify | ~12 ms | ~20 ms | ~32 ms |

### Comparison with Classical Signature Schemes

| Metric | ML-DSA-65 | Ed25519 | RSA-2048 | RSA-4096 | ECDSA P-256 |
|--------|----------|---------|----------|----------|-------------|
| Public key | 1,952 B | 32 B | 256 B | 512 B | 64 B |
| Signature | 3,309 B | 64 B | 256 B | 512 B | 64 B |
| Combined (pk+sig) | 5,261 B | 96 B | 512 B | 1,024 B | 128 B |
| KeyGen time | ~250 μs | ~50 μs | ~100 ms | ~2 s | ~60 μs |
| Sign time | ~1.1 ms | ~50 μs | ~1 ms | ~5 ms | ~60 μs |
| Verify time | ~280 μs | ~120 μs | ~30 μs | ~60 μs | ~120 μs |

The size overhead of ML-DSA compared to elliptic curve schemes is approximately 30-50x for public keys and signatures. While significant, this is acceptable for most modern network protocols (a TLS handshake adding 5-10 KB is manageable on typical internet connections). The computational overhead is more modest: signing is about 20x slower than Ed25519 but comparable to RSA-2048, and verification is only about 2x slower than Ed25519.

### Bandwidth and Storage Implications

For protocol designers considering ML-DSA deployment, the size implications deserve careful analysis:

**TLS 1.3 handshake:** A typical handshake with ML-DSA-65 adds approximately 5-10 KB compared to the ECDSA equivalent (accounting for certificate chain, signature, and potentially the server's ephemeral key). On broadband connections this is negligible; on satellite links or congested mobile networks, the added latency from larger handshakes may be noticeable.

**X.509 certificates:** Each certificate grows by approximately 5 KB (public key + signature). A three-certificate chain (end-entity, intermediate, root) adds roughly 15 KB total overhead compared to ECDSA-based chains.

**Code signing:** Software packages are typically megabytes to gigabytes; a 3.3 KB signature is insignificant. ML-DSA is well-suited for this application.

**Blockchain:** Each transaction carrying an ML-DSA signature is roughly 50x larger than with ECDSA. For high-throughput chains processing thousands of transactions per second, this is a meaningful consideration that may require larger blocks or more aggressive aggregation techniques.

## 12.9 Comparison with Other PQC Signatures

### ML-DSA vs. SLH-DSA (FIPS 205)

| Metric | ML-DSA-65 | SLH-DSA-SHA2-192s | SLH-DSA-SHA2-192f |
|--------|----------|-------------------|-------------------|
| Public key | 1,952 B | 48 B | 48 B |
| Signature | 3,309 B | 16,224 B | 35,664 B |
| Sign time | ~1.1 ms | ~120 ms | ~10 ms |
| Verify time | ~280 μs | ~6 ms | ~2 ms |
| Security basis | Module-LWE/SIS | Hash functions only | Hash functions only |
| Implementation complexity | Moderate | Low | Low |
| Key generation | Fast (~250 μs) | Fast (~1 ms) | Fast (~1 ms) |

ML-DSA offers dramatically smaller signatures and faster operations, while SLH-DSA provides the conservative advantage of relying only on hash function security. Organizations with the highest security requirements may prefer SLH-DSA for root-of-trust applications where the performance penalty is acceptable.

### ML-DSA vs. FN-DSA (FIPS 206, forthcoming)

| Metric | ML-DSA-65 | FN-DSA-512 | FN-DSA-1024 |
|--------|----------|-----------|------------|
| Public key | 1,952 B | 897 B | 1,793 B |
| Signature | 3,309 B | 666 B | 1,280 B |
| Sign time | ~1.1 ms | ~5 ms | ~12 ms |
| Verify time | ~280 μs | ~0.5 ms | ~1 ms |
| Security basis | Module-LWE/SIS | NTRU lattice | NTRU lattice |
| Implementation complexity | Low | High | High |
| Constant-time feasibility | Straightforward | Very difficult | Very difficult |

FN-DSA (based on FALCON) achieves the smallest combined public key plus signature size of any lattice-based scheme, making it attractive for bandwidth-constrained applications. However, its reliance on discrete Gaussian sampling over lattices makes constant-time implementation extremely challenging. The signing procedure requires high-precision floating-point arithmetic that is difficult to implement securely on embedded platforms. ML-DSA's simpler rejection sampling is significantly easier to implement correctly and securely.

### Positioning in the PQC Ecosystem

ML-DSA occupies the "default choice" position in the NIST PQC portfolio. It should be the first algorithm considered for any new signature application unless there are specific constraints that favor alternatives:
- If signature size is the overriding concern and implementation expertise is available → consider FN-DSA
- If maximum conservatism is required and large signatures are acceptable → choose SLH-DSA
- For all other cases → ML-DSA provides the best balance

## 12.10 Use Cases and Deployment

### Ideal Applications for ML-DSA

**TLS certificate authentication:** ML-DSA-65 is well-suited for TLS server authentication. The additional handshake overhead of approximately 5-10 KB is acceptable for nearly all deployment scenarios. Modern TLS 1.3 implementations can accommodate the larger certificate chains with minimal impact on connection establishment time. The fast verification speed (sub-millisecond) ensures that clients can validate certificates without noticeable delay.

**Code signing and software distribution:** Software packages are signed infrequently (at release time) but verified frequently (at every installation). ML-DSA's fast verification and moderate signature size make it ideal for this asymmetric use case. The signing time of approximately 1 ms is negligible compared to the build process.

**Document signatures (PDF, XML, office formats):** Digital signature standards for documents are transitioning to support post-quantum algorithms. ML-DSA signatures can be embedded within existing signature container formats (CAdES, XAdES, PAdES) with straightforward modifications to accommodate the larger signature data.

**Authentication tokens and credentials:** JWT-like tokens signed with ML-DSA are larger than their ECDSA counterparts but remain practical for API authentication and identity assertion. The impact on HTTP header sizes is manageable for server-to-server communication.

**Email security (S/MIME):** Post-quantum S/MIME using ML-DSA adds several kilobytes to each signed email. For typical email sizes (tens to hundreds of KB), this overhead is minor. The greater challenge lies in the certificate chain sizes embedded in each message.

### Deployment Considerations for Specific Scenarios

**Certificate chains and PKI:** A complete PKI migration to ML-DSA involves:
- Root CA keys: ML-DSA-87 for maximum long-term security
- Intermediate CA keys: ML-DSA-65 for the balance of security and size
- End-entity certificates: ML-DSA-44 or ML-DSA-65 depending on the application
- Certificate chain overhead: 3-4 certificates × ~5 KB each = 15-20 KB total

Organizations may initially deploy hybrid certificates (containing both classical and PQ signatures) during the transition period, further increasing sizes temporarily.

**Blockchain and distributed ledger technology:** The larger transaction sizes present a genuine challenge. A Bitcoin-style UTXO transaction with ML-DSA signatures would grow from approximately 250 bytes to approximately 4,000 bytes. This 16x increase affects block propagation time, storage requirements, and network bandwidth. Solutions include:
- Signature aggregation where applicable
- Batch verification to maintain validation throughput
- Gradual transition with hybrid approaches
- Layer-2 protocols to reduce on-chain signature volume

**Embedded and IoT devices:** ML-DSA-44 is feasible on ARM Cortex-M4 class devices with approximately 30 KB of RAM for signing operations. Key considerations include:
- Stack usage during signing: approximately 30 KB (significant for devices with 64-256 KB total RAM)
- Flash storage for the implementation: approximately 20-40 KB compiled code size
- Precomputation of NTT(A) if the key is fixed: trades 7 KB storage for 30% signing speedup
- Verification-only deployments (e.g., firmware update validation) have lower resource requirements

**High-performance computing and HSMs:** Hardware Security Modules must accommodate the larger key and signature sizes. The computational requirements of ML-DSA are well within the capabilities of modern HSMs, with signing rates of thousands of operations per second achievable with dedicated hardware. The NTT structure maps well to DSP-like hardware accelerators.

## 12.11 Deterministic Signatures, Nonce Safety, and Fault Resistance

### The Critical Importance of Nonce Quality in Classical Schemes

To appreciate ML-DSA's nonce handling, recall the devastating consequences of nonce failure in ECDSA: if two signatures ever reuse the same nonce k with different messages, the secret key d is immediately and trivially recoverable through simple algebra:

s₁ = k⁻¹(H(m₁) + r·d) and s₂ = k⁻¹(H(m₂) + r·d)
⟹ s₁ - s₂ = k⁻¹(H(m₁) - H(m₂))
⟹ k = (H(m₁) - H(m₂))/(s₁ - s₂)
⟹ d = (s₁·k - H(m₁))/r

This catastrophic failure mode has been responsible for numerous real-world key compromises, including the Sony PlayStation 3 root key extraction in 2010 and various cryptocurrency wallet thefts. Even partial nonce bias (a few bits of predictability) can enable lattice-based attacks that recover the key after observing hundreds of signatures.

### ML-DSA's Improved Nonce Safety

ML-DSA provides substantially better resilience to nonce-related failures:

**No catastrophic nonce reuse:** In ML-DSA, the masking vector **y** plays the role of the nonce. If the same **y** is used twice with different messages, the resulting challenges c and c' will differ. The two signatures reveal **z** = **y** + c·**s₁** and **z'** = **y** + c'·**s₁**, giving **z** - **z'** = (c - c')·**s₁**. While this leaks information about **s₁**, it does not immediately reveal the secret (solving for **s₁** still requires finding a short vector in a lattice). Moreover, the rejection sampling may prevent both signatures from being output.

**Deterministic derivation:** In deterministic mode, the masking vector is derived as **y** = ExpandMask(H(K ‖ 0^32 ‖ μ), κ), where K is a secret key component and μ depends on the message. Since different messages produce different μ values, different messages always produce different masking vectors, completely preventing nonce reuse across messages.

**Key component K:** The secret value K, stored in the private key, acts as a per-key secret that prevents an attacker from predicting the deterministic nonce even if the message is known. This is analogous to the role of the additional secret in EdDSA (RFC 8032) deterministic signing.

### Hedged Mode as Defense in Depth

The hedged signing mode (FIPS 204's default) provides multiple layers of protection against physical attacks:

**Fault injection resistance:** If an attacker can inject a fault during signing (e.g., flipping a bit in memory or disrupting a computation), the resulting faulty signature might leak information about the secret key. With deterministic signing, the attacker can cause the same computation to execute again (with the same message and key) and compare correct versus faulty outputs. Hedged signing includes fresh randomness, so repeating the operation produces entirely different intermediate values, making differential fault analysis ineffective.

**Side-channel decorrelation:** Power analysis attacks (DPA/CPA) and electromagnetic emanation attacks work by correlating many traces from the same operation. If each signing operation uses different randomness, the internal state differs each time, requiring the attacker to correlate across different random values — dramatically increasing the number of traces needed for a successful attack.

**Implementation simplicity for security-critical code:** By including randomness, the implementation is less sensitive to subtle constant-time failures. A minor timing leak that reveals a few bits of information is less dangerous when combined with unpredictable randomness, as the leaked bits are different each time.

### Signature Non-Malleability

ML-DSA signatures are not unique: for a given message and key, there are many valid signatures (different choices of **y** in the rejection loop lead to different valid (c̃, **z**, h) triples). This non-uniqueness has implications:

- **Deterministic signing** produces the same signature each time, providing de facto uniqueness per (key, message) pair
- **Hedged signing** produces a different valid signature each time the same message is signed
- Applications requiring signature uniqueness (e.g., some blockchain protocols) should use deterministic mode or hash the signature for deduplication
- The non-uniqueness does not affect security — all valid signatures are equally secure

## 12.12 Advanced Topics

### NTT-Based Arithmetic

The Number Theoretic Transform is the computational workhorse of ML-DSA. The choice of q = 8,380,417 = 2^23 - 2^13 + 1 ensures that:
- q is prime (enabling NTT over Z_q)
- q ≡ 1 (mod 512), so 512th roots of unity exist in Z_q (enabling radix-2 NTT of length 256)
- q fits in 23 bits (enabling efficient single-word arithmetic on 32-bit and 64-bit platforms)
- The special form allows fast reduction: x mod q can be computed efficiently using shifts and additions

All polynomial multiplications in ML-DSA (A·y, A·z, c·s₁, c·s₂) are performed in the NTT domain for O(n log n) efficiency rather than O(n²) schoolbook multiplication. The matrix **A** is stored permanently in NTT form (as Â) to avoid repeated forward transforms.

### Compressed Representations and Encoding

ML-DSA uses several encoding optimizations to minimize sizes:
- **Public key t₁:** Each coefficient is at most ⌈log₂(q)⌉ - d = 10 bits, packed without waste
- **Signature z:** Coefficients are in [-γ₁+1, γ₁], encoded using γ₁-dependent bit width
- **Hint h:** Encoded as indices of the non-zero positions (using the ω bound for allocation)
- **Challenge seed c̃:** Raw 32-byte hash output (the polynomial c is reconstructed from this)

### Formal Verification Efforts

Given ML-DSA's importance as a foundational standard, several formal verification efforts are underway:
- Machine-checked proofs of the cryptographic security reduction (using EasyCrypt and similar tools)
- Formal verification of reference implementations (ensuring correctness and constant-time properties)
- Side-channel verification using tools like ct-verif that check for secret-dependent branching
- Verification of the NTT implementation against the mathematical specification

These efforts provide high assurance that implementations faithfully realize the security guarantees of the mathematical design.

## 12.13 Migration and Interoperability

### Hybrid Signatures During Transition

During the migration period from classical to post-quantum cryptography, organizations may deploy hybrid signature schemes that combine ML-DSA with a classical algorithm (typically ECDSA or Ed25519):

- **Concatenated signatures:** Both signatures are generated and both must verify
- **Composite keys:** A single certificate contains both a classical and a PQ public key
- **Backward compatibility:** Older systems that do not support ML-DSA can still verify the classical component

Standards bodies including IETF (RFC drafts for composite signatures) and X.509 working groups are developing interoperability specifications for hybrid deployment.

### Algorithm Agility and OID Assignment

ML-DSA has been assigned specific Object Identifiers (OIDs) for use in X.509 certificates, CMS (Cryptographic Message Syntax), and related standards:
- Each parameter set (ML-DSA-44, ML-DSA-65, ML-DSA-87) has its own OID
- Pure and pre-hash variants have separate OIDs
- The pre-hash variant (HashML-DSA) hashes the message before signing, enabling streaming of large messages

### Timeline Considerations

Organizations should plan their ML-DSA migration with awareness that:
- NIST has indicated that RSA and ECDSA will eventually be deprecated (target: 2035 for disallowing in federal systems)
- Certificate lifetimes mean that certificates issued today may still be in use when quantum computers arrive
- "Harvest now, decrypt later" attacks on signatures are less concerning than for encryption (signatures protect authenticity at a point in time, not long-term secrecy), but long-lived signatures on critical documents do benefit from post-quantum protection

## 12.14 Testing and Validation

### Known Answer Tests (KATs)

NIST provides official Known Answer Test vectors for ML-DSA that implementations must pass before deployment. These test vectors cover:

- **Key generation:** Given a specific seed ξ, verify that the produced public key and secret key match expected values exactly. This tests the ExpandA, ExpandS, and Power2Round functions.
- **Signing:** Given a specific key pair, message, and (for deterministic mode) all inputs, verify the output signature matches. Due to the rejection loop, deterministic signing with a fixed seed must produce the exact same signature on every compliant implementation.
- **Verification:** Both positive tests (valid signatures that must be accepted) and negative tests (corrupted signatures that must be rejected).

### Intermediate Value Testing

Beyond end-to-end KATs, thorough testing should verify intermediate computations:
- NTT and inverse NTT against known polynomial multiplication results
- HighBits/LowBits/Power2Round decomposition consistency
- MakeHint/UseHint round-trip correctness
- SampleInBall output distribution (correct weight and coefficient range)
- Rejection bounds: verify that all three rejection checks fire appropriately on crafted inputs

### Interoperability Testing

As ML-DSA implementations proliferate across different languages and platforms, interoperability testing ensures that:
- A signature produced by implementation A verifies correctly under implementation B
- Key encoding formats are interpreted identically across implementations
- Context strings and domain separators are handled consistently
- Pre-hash mode (HashML-DSA) produces compatible results across implementations

The NIST Algorithm Validation Program (CAVP) provides automated testing infrastructure for certifying implementations against the standard.

## 12.15 Key Takeaways

- ML-DSA (FIPS 204) is the primary post-quantum signature standard, derived from CRYSTALS-Dilithium and finalized in 2024
- Security reduces to Module-LWE and Module-SIS problems, with no known quantum polynomial-time algorithms
- Three parameter sets target NIST Security Levels 2, 3, and 5, with ML-DSA-65 recommended as the default
- The Fiat-Shamir with Aborts paradigm uses rejection sampling to achieve zero-knowledge, preventing secret key leakage through signatures
- Signatures range from 2.4 to 4.6 KB; public keys from 1.3 to 2.6 KB — larger than classical schemes but practical for most applications
- Signing involves a probabilistic rejection loop averaging 4-7 iterations, with overall signing time around 1 ms on modern hardware
- The hint vector h enables efficient verification without transmitting the full commitment
- Hedged signing (incorporating fresh randomness) is mandated for general use, providing fault-attack resistance
- Deterministic signing is available for applications requiring reproducibility or lacking quality randomness
- Constant-time implementation is essential; the rejection loop structure and NTT arithmetic require careful attention to avoid side-channel leakage
- Batch verification provides 2-4x speedup for bulk signature validation
- ML-DSA is the recommended default for nearly all signature applications, with SLH-DSA and FN-DSA serving specialized needs
- Migration should begin now: standards, libraries, and protocols are ready for deployment

---

*Next: [Chapter 13 — FIPS 205: SLH-DSA](./13-fips-205-slh-dsa.md)*
