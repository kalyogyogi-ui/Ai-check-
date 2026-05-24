# Chapter 5: Lattice-Based Cryptography

## 5.1 Introduction to Lattices

A **lattice** is a discrete additive subgroup of R^n, or equivalently, the set of all integer linear combinations of a set of linearly independent vectors (a **basis**):

```
L(B) = {Bx : x ∈ Z^n} = {Σ xᵢbᵢ : xᵢ ∈ Z}
```

where B = [b₁, b₂, ..., bₙ] is the basis matrix with columns bᵢ ∈ R^n.

Key properties of lattices:
- The same lattice can have many different bases
- Some bases are "better" (more orthogonal) than others
- Hard lattice problems involve finding short or close vectors

### Geometric Intuition

Think of a lattice as a regular grid of points in space. In 2D, imagine a set of dots arranged in a repeating pattern (like atoms in a crystal). The difficulty comes in high dimensions: finding the shortest non-zero vector or the closest lattice point to a given target becomes exponentially hard as the dimension grows.

## 5.2 Hard Lattice Problems

### Shortest Vector Problem (SVP)

**Definition:** Given a lattice L, find the shortest non-zero vector v ∈ L (in Euclidean norm).

**Approximate SVP (γ-SVP):** Find a non-zero vector v ∈ L with ||v|| ≤ γ · λ₁(L), where λ₁ is the length of the shortest vector and γ is the approximation factor.

**Hardness:**
- Exact SVP is NP-hard (under randomized reductions)
- Approximate SVP with γ = poly(n) is believed hard for quantum computers
- Best known algorithms (lattice sieving): Time 2^(0.292n + o(n))

### Closest Vector Problem (CVP)

**Definition:** Given a lattice L and a target point t, find the closest lattice point to t.

**Relationship to SVP:** CVP is at least as hard as SVP, and approximate CVP reduces to approximate SVP.

### Learning With Errors (LWE)

The **Learning With Errors** problem, introduced by Oded Regev in 2005, is the foundation of modern lattice-based cryptography.

**Definition:** Given pairs (aᵢ, bᵢ = ⟨aᵢ, s⟩ + eᵢ mod q), where:
- aᵢ ∈ Z_q^n are uniformly random vectors
- s ∈ Z_q^n is a secret vector
- eᵢ are "errors" sampled from a discrete Gaussian distribution

The **search LWE** problem is to find s.  
The **decision LWE** problem is to distinguish (aᵢ, bᵢ) from truly uniform random pairs.

**Security:** Regev proved a quantum reduction from worst-case lattice problems (GapSVP, SIVP) to average-case LWE. This means breaking LWE is at least as hard as solving certain lattice problems in the worst case.

### Short Integer Solution (SIS)

**Definition:** Given a random matrix A ∈ Z_q^(n×m), find a short non-zero vector x ∈ Z^m such that Ax = 0 mod q and ||x|| ≤ β.

SIS is the foundation for lattice-based hash functions and signature schemes.

## 5.3 Structured Lattice Problems

Plain LWE and SIS require large matrices, leading to large keys. Structured variants improve efficiency:

### Ring-LWE

Operates over polynomial rings R_q = Z_q[x]/(x^n + 1) where n is a power of 2:
- Secret, error, and samples are polynomials in R_q
- Multiplication in R_q can be performed using NTT in O(n log n)
- Key sizes: O(n log q) instead of O(n² log q)

### Module-LWE

A middle ground between LWE and Ring-LWE:
- Operates over R_q^k — vectors of k ring elements
- Adjusting k allows trading structure for security confidence
- Module-LWE with k=1 reduces to Ring-LWE
- Module-LWE with large n and k=n gives plain LWE

ML-KEM and ML-DSA use Module-LWE with different parameters for different security levels.

### Security of Structured Variants

The security landscape of structured lattice problems:

| Problem | Security Confidence | Efficiency |
|---------|-------------------|------------|
| Plain LWE | Highest | Lowest |
| Module-LWE (k≥2) | High | Good |
| Ring-LWE | Good (less studied) | Highest |

NIST's selected algorithms use Module-LWE/Module-SIS, balancing security confidence with practical efficiency.

## 5.4 Lattice-Based Encryption: The Regev/LPR Framework

### Regev's Encryption Scheme (Conceptual)

**Key Generation:**
- Choose random matrix A ∈ Z_q^(n×m)
- Choose secret s ∈ Z_q^n
- Compute b = As + e (where e is short error vector)
- Public key: (A, b), Secret key: s

**Encryption of bit μ ∈ {0,1}:**
- Choose random subset S of rows
- Ciphertext: (c₁, c₂) = (Σ aᵢ for i∈S, Σ bᵢ + μ·⌊q/2⌋ for i∈S)

**Decryption:**
- Compute c₂ - ⟨c₁, s⟩ ≈ μ·⌊q/2⌋
- Round to nearest multiple of ⌊q/2⌋ to recover μ

### The LPR Framework (Lyubashevsky-Peikert-Regev)

For Ring-LWE based encryption:

**Key Generation:**
- Choose random a ∈ R_q
- Choose secret s, error e from discrete Gaussian
- Public key: (a, b = a·s + e), Secret key: s

**Encryption:**
- Choose random r, errors e₁, e₂
- c₁ = a·r + e₁
- c₂ = b·r + e₂ + ⌊q/2⌋·m

**Decryption:**
- Compute c₂ - s·c₁ = e₂ + s·e₁ - e·r + ⌊q/2⌋·m
- Errors are small enough that message m can be recovered

## 5.5 From Encryption to Key Encapsulation (KEM)

Modern lattice cryptography uses the **KEM/DEM paradigm** rather than direct public-key encryption:

### Fujisaki-Okamoto Transform

The FO transform converts a CPA-secure public-key encryption scheme into a CCA-secure KEM:

1. To encapsulate: Choose random message m, derive randomness r = H(m), encrypt m using r
2. Shared secret: K = H(m, ciphertext)
3. To decapsulate: Decrypt to recover m, re-encrypt to verify, output K

This provides **IND-CCA2 security** (security against adaptive chosen-ciphertext attacks), which is necessary for real-world protocols.

### Why KEM Instead of Encryption?

- **Cleaner security definitions** for key exchange
- **No padding oracles** — common source of vulnerabilities in PKE
- **Composability** — KEMs combine naturally with symmetric encryption
- **Protocol fit** — TLS and other protocols use key exchange, not direct encryption

## 5.6 The NTRU Family

NTRU (N-th degree Truncated polynomial Ring Units) predates the LWE-based approach:

### NTRU Problem

In the polynomial ring Z_q[x]/(x^n - 1):
- Given h = g · f^(-1) mod q where f, g have small coefficients
- Find f (or any short vector in the NTRU lattice)

### NTRU Encryption

**Key Generation:**
- Choose small polynomials f, g ∈ Z[x]/(x^n - 1)
- Public key: h = p·g · f^(-1) mod q

**Encryption:**
- Ciphertext: c = r·h + m mod q (r random small, m is message)

**Decryption:**
- Compute a = f·c mod q = p·r·g + f·m mod q
- Reduce mod p to recover m

### NTRU vs. LWE-Based Approaches

| Property | NTRU | Module-LWE |
|----------|------|------------|
| Hard problem | NTRU problem | Module-LWE |
| Security history | Since 1996 | Since 2005 |
| Decryption failures | Possible (mitigated) | Possible (mitigated) |
| Performance | Competitive | Slightly better for KEM |
| Standardization | Not selected by NIST primary | Selected (ML-KEM) |

## 5.7 Lattice-Based Signatures

### Hash-and-Sign Approach (GPV Framework)

Based on Gaussian sampling in lattices:
1. Public key: a matrix A (defines a lattice)
2. Secret key: a short basis B of the lattice
3. Signing: Use B to sample a short vector in the coset defined by the hash of the message
4. Verification: Check that the signature is short and maps to the correct coset

### Fiat-Shamir with Aborts (Lyubashevsky)

The approach used in ML-DSA:
1. Commit: Generate a masking vector y, compute commitment w = Ay
2. Challenge: Hash the commitment to get a challenge c
3. Response: Compute z = y + c·s (where s is the secret)
4. **Rejection sampling:** If z reveals information about s, reject and restart

The "abort" step is crucial — without it, the signature would leak the secret key. By aborting when the response z is too correlated with s, the scheme achieves **zero-knowledge** properties.

### Comparison of Signature Approaches

| Approach | Example | Signature Size | Signing Speed |
|----------|---------|----------------|---------------|
| Hash-and-sign | FALCON | ~666 bytes (Level 1) | Moderate |
| Fiat-Shamir w/ aborts | ML-DSA | ~2,420 bytes (Level 2) | Fast |
| One-time + Merkle | SLH-DSA | ~7,856 bytes (Level 1) | Slow |

## 5.8 Lattice Reduction Algorithms

Understanding lattice attacks is essential for parameter selection:

### LLL Algorithm (Lenstra-Lenstra-Lovász, 1982)

- Runs in polynomial time
- Finds vectors within 2^(n/2) factor of shortest
- Sufficient for low-dimensional lattices (n < 50)
- Foundation for more advanced algorithms

### BKZ (Block Korkine-Zolotarev)

- Parameterized by block size β
- Uses an SVP oracle for β-dimensional sublattices
- Achieves approximation factor: γ ≈ β^(n/β)
- Running time grows exponentially with β
- BKZ-2.0 with progressive strategies is the practical standard

### Lattice Sieving

- Best asymptotic complexity for SVP: 2^(0.292n + o(n)) time and space
- Practically viable for dimensions up to ~150
- Can be parallelized and has known (limited) quantum speedups
- Sets the concrete security boundary for PQC parameters

### Quantum Lattice Attacks

Known quantum speedups for lattice problems:
- **Grover speedup for sieving:** Reduces time exponent from 0.292n to potentially 0.265n
- **Quantum BKZ:** Moderate improvements to BKZ efficiency
- **No Shor-like breakthrough:** No polynomial-time quantum algorithm for lattice problems is known

This limited quantum advantage is why lattice problems are considered quantum-resistant.

## 5.9 Parameter Selection

Choosing secure lattice parameters requires balancing:

1. **Dimension n:** Higher = more secure, but larger keys/slower operations
2. **Modulus q:** Affects the error tolerance and security
3. **Error distribution width σ:** Smaller = more efficient, but less security margin
4. **Module rank k:** In Module-LWE, adjusts the security/efficiency trade-off

### Security Estimation

The concrete security of lattice parameters is estimated by:
1. Determining the cost of the best attack (typically BKZ + lattice sieving)
2. Computing the required block size β to solve the specific LWE instance
3. Estimating the cost of BKZ-β (using the Core-SVP model or more refined estimates)
4. Adding margins for unknown improvements

### NIST Security Levels for ML-KEM

| Parameter Set | n | k | q | Security Level |
|--------------|---|---|---|---------------|
| ML-KEM-512 | 256 | 2 | 3329 | Level 1 (128-bit) |
| ML-KEM-768 | 256 | 3 | 3329 | Level 3 (192-bit) |
| ML-KEM-1024 | 256 | 4 | 3329 | Level 5 (256-bit) |

## 5.10 Advanced Lattice Constructions

Beyond basic encryption and signatures, lattices enable:

### Fully Homomorphic Encryption (FHE)
- Compute on encrypted data without decryption
- All practical FHE schemes are lattice-based
- Applications: Private cloud computing, secure machine learning

### Attribute-Based Encryption (ABE)
- Access policies embedded in ciphertexts or keys
- Lattice-based constructions achieve full security proofs

### Zero-Knowledge Proofs
- Lattice-based ZK proofs for NP statements
- Applications: Privacy-preserving credentials, blockchain privacy

### Multi-Party Computation
- Lattice-based protocols for secure multi-party computation
- Threshold key generation and decryption from lattices

## 5.11 Key Takeaways

- Lattices are geometric objects in high-dimensional space; finding short vectors is hard
- LWE is the central hard problem — provably as hard as worst-case lattice problems
- Module-LWE provides a practical middle ground between efficiency and security confidence
- The FO transform converts CPA encryption into CCA-secure KEMs
- Lattice-based signatures use either hash-and-sign or Fiat-Shamir with aborts
- Lattice reduction algorithms (BKZ, sieving) determine concrete security parameters
- Quantum computers provide only modest speedups for lattice problems (no exponential advantage)
- Lattices are the most versatile PQC family, supporting KEMs, signatures, and advanced primitives

---

*Next: [Chapter 6 — Code-Based Cryptography](./06-code-based.md)*
