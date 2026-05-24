# Chapter 3: Why Current Cryptography Fails: Shor's and Grover's Algorithms

## 3.1 The Foundation of Classical Cryptographic Security

The security of modern public-key cryptography rests entirely on computational hardness assumptions. No one has proven that these problems are inherently hard — we rely on the empirical evidence that decades of effort by brilliant mathematicians have failed to find efficient classical algorithms.

The central hard problems are:

- **Integer Factorization:** Given N = p × q (where p, q are large primes), find p and q
- **Discrete Logarithm:** Given g, h in a group G, find x such that g^x = h
- **Elliptic Curve Discrete Logarithm:** Given points P and Q on an elliptic curve, find k such that Q = kP

The best classical algorithms for these problems have sub-exponential running time:
- General Number Field Sieve (factoring): O(exp(c · n^(1/3) · (log n)^(2/3)))
- Index Calculus (discrete log in finite fields): Similar sub-exponential complexity
- Pollard's rho (ECDLP): O(√n) — exponential in key size

## 3.2 Shor's Algorithm: The Quantum Threat

In 1994, Peter Shor published what is arguably the most consequential algorithm in computer science history. Shor's algorithm solves both integer factorization and discrete logarithm problems in **polynomial time** on a quantum computer.

### The Factoring Algorithm

Shor's factoring algorithm consists of two parts:

**Classical Reduction:** Factoring is reduced to the problem of finding the **period** (or order) of a function. Specifically, given N to factor:

1. Choose random a with 1 < a < N and gcd(a, N) = 1
2. Find the smallest r such that a^r ≡ 1 (mod N) — this is the order of a modulo N
3. If r is even and a^(r/2) ≢ -1 (mod N), then gcd(a^(r/2) ± 1, N) gives non-trivial factors

**Quantum Period Finding:** The quantum part finds the period r using:

1. Prepare a superposition of all possible exponents: |0⟩|0⟩ → Σ|x⟩|a^x mod N⟩
2. Apply the **Quantum Fourier Transform (QFT)** to the first register
3. Measure to obtain a value that reveals the period r

The QFT converts periodic signals in the computational basis into peaks at multiples of the frequency, exploiting quantum interference to amplify the correct period.

### Complexity Analysis

| Operation | Classical (GNFS) | Quantum (Shor) |
|-----------|------------------|----------------|
| Time complexity | O(exp(c·n^(1/3)·(log n)^(2/3))) | O(n² · log n · log log n) |
| For RSA-2048 (n=2048 bits) | ~2^112 operations | ~2^26 operations |
| Practical implication | Infeasible | Hours to days on CRQC |

### Resource Requirements for Breaking RSA

To factor a 2048-bit RSA modulus using Shor's algorithm:

- **Logical qubits needed:** ~4,000-6,000
- **T-gate depth:** ~10^10
- **Physical qubits (with surface codes):** ~4-20 million
- **Estimated time:** Hours to days (depending on clock speed)

Recent optimizations have continued to reduce these requirements:
- Gidney & Ekerå (2021): 2,048 + 2 logical qubits using windowed arithmetic
- Further optimizations reduce space-time volume through various trade-offs

### Shor's Algorithm for Discrete Logarithm

Shor's algorithm also solves the discrete logarithm problem in any finite abelian group:

1. Given generator g and target h = g^s in a group of order N
2. Prepare superposition over (a, b) pairs: Σ|a⟩|b⟩|g^a · h^b⟩
3. Apply QFT to first two registers
4. Measurement reveals linear constraints on s
5. Repeat O(1) times to determine s completely

This breaks:
- **Diffie-Hellman key exchange** — Compute private key from public key
- **DSA/ECDSA signatures** — Recover signing key from public key
- **ElGamal encryption** — Decrypt without private key

### Impact on Elliptic Curve Cryptography

ECC relies on the hardness of the Elliptic Curve Discrete Logarithm Problem (ECDLP). Shor's algorithm adapted to elliptic curve groups breaks ECDLP with:

- **Logical qubits:** ~2n + O(log n) for an n-bit curve
- **For P-256:** ~521 logical qubits, ~10^8 Toffoli gates
- **Physical qubits:** ~2,500-5,000 (with good error correction)

Ironically, ECC — often recommended as a more efficient alternative to RSA — is actually *easier* to break with a quantum computer due to the smaller key sizes involved.

## 3.3 Grover's Algorithm: Quadratic Speedup for Search

In 1996, Lov Grover discovered an algorithm providing a quadratic speedup for unstructured search problems.

### The Algorithm

Given a function f: {0,1}^n → {0,1} with a unique x₀ such that f(x₀) = 1:

1. Initialize uniform superposition: H^⊗n|0⟩^n
2. Repeat √(2^n) times:
   a. **Oracle:** Apply phase flip to |x₀⟩ (negate amplitude of marked item)
   b. **Diffusion:** Reflect about the mean amplitude (amplify marked item)
3. Measure to obtain x₀ with high probability

### Complexity

- **Classical search:** O(2^n) evaluations
- **Grover's search:** O(2^(n/2)) evaluations — quadratic speedup
- **This is provably optimal** for unstructured search on quantum computers

### Impact on Symmetric Cryptography

Grover's algorithm effectively halves the security level of symmetric algorithms:

| Algorithm | Classical Security | Post-Quantum Security |
|-----------|-------------------|----------------------|
| AES-128 | 128-bit | 64-bit |
| AES-192 | 192-bit | 96-bit |
| AES-256 | 256-bit | 128-bit |
| SHA-256 (preimage) | 256-bit | 128-bit |
| SHA-256 (collision) | 128-bit | 85-bit (BHT algorithm) |

**Mitigation:** Simply double key sizes. AES-256 provides 128-bit security against quantum attacks, which is considered adequate.

### Practical Considerations for Grover's Algorithm

While Grover's algorithm provides a theoretical quadratic speedup, practical considerations limit its impact:

1. **Massive parallelism defeats Grover:** A classical computer with 2^64 cores searching in parallel outperforms a single quantum computer running Grover's on a 128-bit space, because Grover cannot be parallelized as efficiently.

2. **Circuit depth:** Grover's requires sequential iterations — the √N queries must be performed sequentially, limiting the advantage when the oracle is complex.

3. **No memory advantage for AES:** Actually implementing an AES oracle in a quantum circuit requires thousands of ancilla qubits and is extremely deep.

## 3.4 Other Quantum Algorithms Relevant to Cryptography

### Simon's Algorithm

Solves Simon's problem (finding the period of a 2-to-1 function) exponentially faster than classical algorithms. Relevant to attacks on certain block cipher modes and MACs (e.g., breaking Even-Mansour in quantum superposition oracle model).

### Quantum Hidden Subgroup Problem

Many quantum speedups (including Shor's) can be viewed as instances of the **Hidden Subgroup Problem (HSP)** over abelian groups. The HSP over non-abelian groups (e.g., the symmetric group, dihedral group) remains hard even for quantum computers — this is relevant because some PQC proposals rely on non-abelian HSP hardness.

### Quantum Walk Algorithms

Quantum walks provide polynomial speedups for certain graph problems and have been used to improve attacks on:
- Subset-sum problems
- Code-based cryptographic schemes (moderate speedups)
- Lattice problems (limited impact)

### BHT Algorithm (Brassard-Høyer-Tapp)

Finds collisions in a function using O(2^(n/3)) queries and time, relevant to hash function security:
- SHA-256 collision resistance: Reduced from 128-bit to ~85-bit quantum security
- Birthday attacks with quantum computing: Improved from O(2^(n/2)) to O(2^(n/3))

## 3.5 What Quantum Computers Cannot Break

Not all cryptography falls to quantum computers:

### Provably Quantum-Resistant Primitives
- **One-time pads** — Information-theoretically secure
- **Symmetric ciphers** (with doubled key sizes) — AES-256 remains secure
- **Hash functions** (with appropriate output sizes) — SHA-384/512 remain secure for most uses

### Problems Without Known Quantum Speedups
- **Learning With Errors (LWE)** — Foundation of lattice-based PQC
- **Syndrome Decoding** — Foundation of code-based PQC
- **Hash function inversion** (beyond Grover) — Foundation of hash-based signatures
- **Multivariate Quadratic (MQ)** — Foundation of multivariate PQC

These problems form the basis of post-quantum cryptographic constructions, explored in detail in subsequent chapters.

## 3.6 Summary of Quantum Impact on Cryptographic Primitives

| Cryptosystem | Type | Quantum Impact | Mitigation |
|-------------|------|---------------|------------|
| RSA | Asymmetric | Completely broken (Shor) | Replace with PQC |
| Diffie-Hellman | Key exchange | Completely broken (Shor) | Replace with ML-KEM |
| ECDH/ECDSA | Asymmetric | Completely broken (Shor) | Replace with PQC |
| DSA | Signatures | Completely broken (Shor) | Replace with ML-DSA |
| AES-128 | Symmetric | Reduced to 64-bit (Grover) | Use AES-256 |
| AES-256 | Symmetric | Reduced to 128-bit (Grover) | Acceptable |
| SHA-256 | Hash | Preimage: 128-bit; Collision: ~85-bit | Use SHA-384+ for critical apps |
| SHA-3 | Hash | Similar to SHA-256 | Adequate with appropriate sizes |
| HMAC | MAC | Halved security (Grover) | Double key size |

## 3.7 The Cryptographic Apocalypse Scenario

If a CRQC appeared tomorrow without post-quantum migration:

1. **All TLS/HTTPS breaks** — Every "secure" website connection is insecure
2. **All VPNs break** — Corporate and government communications exposed
3. **All digital signatures break** — Software updates can be forged, certificates are meaningless
4. **All encrypted email breaks** — Historical and current communications exposed
5. **Financial systems collapse** — Transaction authentication fails
6. **Identity systems fail** — PKI-based authentication becomes worthless
7. **Blockchain/cryptocurrency at risk** — ECDSA signatures can be forged

This scenario motivates the urgency of PQC migration, even though CRQCs may be years away.

## 3.8 Key Takeaways

- Shor's algorithm breaks RSA, DH, and ECC in polynomial time — an exponential speedup
- Grover's algorithm halves the effective security of symmetric algorithms — manageable by doubling key sizes
- The quantum threat to public-key cryptography is existential; for symmetric cryptography, it is manageable
- Several mathematical problems remain hard for quantum computers, forming the basis of PQC
- The "Harvest Now, Decrypt Later" threat means the urgency exists today, not in the future
- Complete replacement of public-key cryptographic infrastructure is necessary

---

*Next: [Chapter 4 — Overview of Post-Quantum Cryptography](./04-pqc-overview.md)*
