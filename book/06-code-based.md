# Chapter 6: Code-Based Cryptography

## 6.1 Error-Correcting Codes: Background

Error-correcting codes were developed to enable reliable communication over noisy channels. The central idea is adding structured redundancy to messages so that errors introduced during transmission can be detected and corrected.

### Linear Codes

A **linear code** C(n, k, d) over a finite field F_q is a k-dimensional subspace of F_q^n:
- **n:** Block length (total symbols)
- **k:** Dimension (information symbols)
- **d:** Minimum distance (minimum Hamming weight of non-zero codewords)
- **Rate:** R = k/n (information density)

A linear code can correct up to t = ⌊(d-1)/2⌋ errors.

### Generator and Parity-Check Matrices

- **Generator matrix G ∈ F_q^(k×n):** Encodes messages as codewords: c = mG
- **Parity-check matrix H ∈ F_q^((n-k)×n):** Defines the code via HcT = 0 for all codewords c
- **Syndrome:** For a received word r = c + e, the syndrome is s = HrT = HeT

### Important Code Families

| Code Family | Parameters | Decoding | Notes |
|-------------|-----------|----------|-------|
| Goppa codes | (n, n-mt, ≥2t+1) | Patterson's algorithm | Used in McEliece |
| BCH codes | (2^m-1, k, d) | Berlekamp-Massey | Subfield subcodes used in McEliece |
| Reed-Solomon | (q, k, q-k+1) | Various algebraic | Not directly quantum-safe |
| LDPC codes | Various | Iterative (belief propagation) | Used in BIKE |
| Reed-Muller | (2^m, k, 2^(m-r)) | Majority logic | Historical importance |

## 6.2 The McEliece Cryptosystem

Robert McEliece proposed the first code-based public-key cryptosystem in 1978, predating RSA by only a year. Despite its age, it has resisted all attacks including quantum ones.

### Construction

**Key Generation:**
1. Choose a random binary Goppa code with parameters (n, k, t) — this code has an efficient decoding algorithm
2. Let G' be the generator matrix for this code
3. Choose a random invertible k×k matrix S and a random n×n permutation matrix P
4. Public key: G = SG'P (disguised generator matrix)
5. Secret key: (S, G', P) along with the Goppa polynomial

**Encryption:**
- Encode message m as c = mG + e where e is a random error vector of weight t
- Ciphertext: c

**Decryption:**
1. Compute c' = cP^(-1) = mSG' + eP^(-1)
2. Since eP^(-1) still has weight t, decode using the Goppa decoder to recover mS
3. Compute m = (mS)S^(-1)

### Security Basis

The security rests on two hard problems:

1. **Indistinguishability of Goppa codes from random codes:** The public key G should look like a random matrix
2. **Syndrome Decoding Problem:** Decoding a random linear code (finding low-weight error from syndrome) is NP-hard

### Parameters and Key Sizes

The main drawback of Classic McEliece is key size:

| Security Level | n | k | t | Public Key Size |
|---------------|-----|------|---|----------------|
| Level 1 | 3488 | 2720 | 64 | ~255 KB |
| Level 3 | 4608 | 3360 | 96 | ~524 KB |
| Level 5 | 6688 | 5024 | 128 | ~1,044 KB |
| Level 5 (alt) | 8192 | 6528 | 128 | ~1,357 KB |

These large keys make Classic McEliece impractical for many constrained applications, though the ciphertext is compact (equal to n-k bits plus overhead).

## 6.3 The Syndrome Decoding Problem

The fundamental hard problem in code-based cryptography:

**Definition:** Given a random parity-check matrix H ∈ F_2^((n-k)×n) and syndrome s ∈ F_2^(n-k), find a vector e of Hamming weight ≤ t such that He^T = s.

**Complexity:**
- NP-complete (Berlekamp, McEliece, van Tilborg, 1978)
- No known polynomial-time quantum algorithm
- Best quantum speedup: Grover's algorithm provides quadratic improvement to information-set decoding

### Best Known Attacks: Information Set Decoding (ISD)

Information Set Decoding (ISD) is the most effective approach for attacking generic linear codes:

**Basic Idea (Prange, 1962):**
1. Choose k coordinates, hoping the error is zero in all of them
2. If so, solving the linear system in those coordinates gives the message
3. Probability of success: C(n-t, k) / C(n, k)
4. Repeat until successful

**Modern Variants:**
- **Stern's algorithm:** Allows some errors in the information set
- **BJMM:** Further optimizations using nearest-neighbor techniques
- **May-Meurer-Thomae:** Representation technique improvements

**Quantum ISD:**
- Grover's applied to the search step provides quadratic speedup
- Best quantum ISD: ~2^(0.06n) for typical McEliece parameters
- This is still exponential — no polynomial-time quantum attack exists

## 6.4 Niederreiter Variant

Niederreiter (1986) proposed a dual construction using the parity-check matrix:

**Key Generation:**
- Public key: H' = SHP (scrambled parity-check matrix)
- Secret key: (S, H, P)

**Encryption:**
- The message IS the error vector e of weight t
- Ciphertext: c = H'e^T (the syndrome)

**Decryption:**
- Unscramble and decode

**Advantages over McEliece:**
- Smaller ciphertexts (n-k bits instead of n bits)
- Equivalent security
- Natural KEM construction (message = random error = shared secret source)

Classic McEliece (the NIST submission) actually uses the Niederreiter form.

## 6.5 Quasi-Cyclic Codes: BIKE and HQC

To address McEliece's large key problem, structured codes with compact representations have been developed.

### BIKE (Bit Flipping Key Encapsulation)

BIKE uses **Quasi-Cyclic MDPC (Moderate Density Parity-Check)** codes:

**Structure:**
- Parity-check matrix: H = [h₀ | h₁] where h₀, h₁ are circulant matrices
- Each circulant is defined by its first row (an n-bit vector)
- Key size: ~n bits per circulant ≈ few kilobytes

**Security:**
- Based on quasi-cyclic syndrome decoding
- MDPC structure means the parity-check matrix has moderate weight (not sparse like LDPC)
- Decoding uses iterative bit-flipping algorithms

**Parameters (BIKE Level 1):**
- Block length: n = 12,323 per block
- Error weight: t = 134
- Public key: ~1,541 bytes
- Ciphertext: ~1,573 bytes

**Concerns:**
- Decryption failure rate must be extremely low (< 2^-128) for IND-CCA security
- Iterative decoders don't have guaranteed success
- Timing side-channels from decoder iteration count

### HQC (Hamming Quasi-Cyclic)

HQC uses a different approach: adding noise to a random code rather than hiding a structured code.

**Key Idea:**
- Public key encodes a secret vector using a random quasi-cyclic code PLUS noise
- Encryption adds more noise
- Decryption uses a special decoder for the "inner" code (a public Reed-Muller or BCH code)

**Parameters (HQC-128):**
- Public key: ~2,249 bytes
- Ciphertext: ~4,497 bytes
- Shared secret: 64 bytes

**Advantages:**
- Cleaner security reduction
- No decryption failures (guaranteed decoding of inner code)
- Relatively small keys compared to Classic McEliece

**NIST Status:** HQC has been selected for standardization as an additional KEM, providing diversity from lattice-based ML-KEM.

## 6.6 Learning Parity with Noise (LPN)

LPN is a binary variant of LWE and forms the basis of some code-based constructions:

**Definition:** Given (a_i, b_i = ⟨a_i, s⟩ ⊕ e_i) where e_i is Bernoulli noise with parameter τ, find s.

**Relationship to Syndrome Decoding:**
- LPN with uniform noise is equivalent to decoding random linear codes
- LPN can be viewed as "binary LWE"

**Applications:**
- Lightweight authentication protocols
- IoT-friendly constructions
- Hybrid schemes with very small computational overhead

## 6.7 Code-Based Signatures: An Open Challenge

Unlike encryption, code-based digital signatures have been extremely challenging to construct:

### Historical Attempts
- **CFS (Courtois-Finiasz-Sendrier, 2001):** First code-based signature scheme; impractical due to very large keys
- **Wave (2019):** Uses ternary codes; promising but keys are still large
- **LESS:** Based on the Linear Equivalence of codes

### Why Signatures Are Hard

The Fiat-Shamir approach requires a hard problem with:
1. Efficient prover (knows secret structure)
2. Hard for verifier without secret (generic code is hard to decode)
3. Zero-knowledge (signature doesn't leak secret)

For codes, efficient signing requires a structured code (to decode), but the signature must not reveal this structure. The "all-or-nothing" nature of decoding makes this difficult.

### Current Research Directions
- **WAVE:** Ternary generalized (U, U+V) codes
- **LESS/MEDS:** Linear/matrix equivalence problems
- **Durandal:** Rank-metric code-based signatures

## 6.8 Rank-Metric Codes

An alternative metric for code-based cryptography:

### Definition
Instead of Hamming weight (number of non-zero coordinates), rank metric uses the rank of a matrix formed by the error vector's coordinates over an extension field.

### Advantages
- Harder generic decoding problems in rank metric
- Smaller parameters for equivalent security
- Enables more compact schemes

### Schemes
- **ROLLO:** Rank-metric KEM (broken in some variants)
- **RQC:** Rank quasi-cyclic codes
- **Durandal:** Rank-metric signatures

### Caution
Rank-metric cryptography is less mature, and several proposals have been broken. More analysis is needed before deployment.

## 6.9 Security Analysis and Attacks

### Structural Attacks
- **Distinguishing attacks:** Determine if a matrix has hidden structure (Goppa, QC, etc.)
- **Key recovery:** Recover the secret code structure from the public key
- **Filtration attacks:** Exploit algebraic structure of Goppa codes

### Generic Decoding Attacks
- **ISD variants:** The primary attack class for all code-based schemes
- **Statistical decoding:** Use statistical properties of the code
- **Algebraic attacks:** Model decoding as a system of equations

### Quantum Attacks
- **Quantum ISD:** Quadratic speedup via Grover's on the search component
- **No exponential quantum speedup known:** Security reduction to NP-hard problem
- **Estimated quantum security:** Parameters chosen with quantum ISD cost ≥ 2^128

## 6.10 Implementation Considerations

### Constant-Time Decoding
- Goppa code decoding (Patterson's algorithm) must be constant-time
- MDPC/LDPC decoders must avoid timing leaks from iteration counts
- Comparison and branching on secret-dependent values must be avoided

### Key Generation
- Generating random Goppa codes requires finding irreducible polynomials
- QC-code key generation is simpler (random circulant blocks)
- Random number generation quality is critical

### Memory and Performance
- Classic McEliece: Large keys but fast encryption/decryption
- BIKE/HQC: Moderate keys, moderate speed
- All schemes benefit from hardware polynomial/matrix multiplication

## 6.11 Key Takeaways

- Code-based cryptography has the longest security track record (since 1978)
- The McEliece cryptosystem has never been broken despite nearly 50 years of analysis
- The main drawback is large public keys (addressed by structured variants)
- Syndrome decoding is NP-hard and has no known efficient quantum algorithm
- HQC has been selected by NIST for standardization alongside ML-KEM
- Code-based signatures remain an open research challenge
- Structured variants (QC codes) reduce keys but introduce new assumptions
- The quantum speedup for code attacks is limited to quadratic (Grover's on ISD)

---

*Next: [Chapter 7 — Hash-Based Signatures](./07-hash-based.md)*
