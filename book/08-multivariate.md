# Chapter 8: Multivariate Polynomial Cryptography

## 8.1 The Multivariate Quadratic Problem

Multivariate cryptography is based on the hardness of solving systems of multivariate polynomial equations over finite fields.

**The MQ Problem:** Given a system of m quadratic polynomials in n variables over a finite field F_q:

```
p₁(x₁, ..., xₙ) = 0
p₂(x₁, ..., xₙ) = 0
...
pₘ(x₁, ..., xₙ) = 0
```

where each pᵢ has the form:

```
pᵢ(x) = Σⱼ≤ₖ aᵢⱼₖ · xⱼ · xₖ + Σⱼ bᵢⱼ · xⱼ + cᵢ
```

Find a solution (x₁, ..., xₙ) ∈ F_q^n.

**Complexity:**
- The MQ problem is NP-hard (even over F_2)
- No known polynomial-time quantum algorithm
- Best quantum attacks provide only modest improvements over classical

## 8.2 The Trapdoor Construction Paradigm

Random multivariate systems are hard to solve but also hard to invert — useless for cryptography. The challenge is constructing systems with a **trapdoor**: a secret structure enabling efficient inversion.

### The Central Map Approach

Most multivariate schemes use the following structure:

1. **Central map F:** An easily invertible multivariate map (the trapdoor)
2. **Affine transformations S, T:** Secret linear maps that disguise the structure
3. **Public key P = T ∘ F ∘ S:** Composition appears random but is invertible with knowledge of S, F, T

The public key is the set of m polynomials in n variables that constitute P. The secret key is (S, F, T).

### Types of Central Maps

| Central Map | Name | Properties |
|-------------|------|-----------|
| Oil and Vinegar | UOV | Quadratic, specialized variable structure |
| Matsumoto-Imai | C* | Monomial over extension field |
| HFE | Hidden Field Equations | Low-degree polynomial over extension field |
| Rainbow | Layered Oil-and-Vinegar | Multi-layer structure (broken 2022) |

## 8.3 Unbalanced Oil and Vinegar (UOV)

UOV is the most successful surviving multivariate signature scheme and is a candidate for NIST additional standardization.

### The Oil and Vinegar Principle

Variables are divided into two types:
- **Vinegar variables** (v₁, ..., vᵥ): Mixed freely in quadratic terms
- **Oil variables** (o₁, ..., oₒ): Never multiplied with each other in the central map

The central map has the form:
```
fₖ(o, v) = Σᵢ Σⱼ αᵢⱼ^(k) · oᵢ · vⱼ + Σᵢ≤ⱼ βᵢⱼ^(k) · vᵢ · vⱼ + linear terms
```

The key observation: once vinegar variables are fixed to random values, the system becomes **linear** in oil variables and can be solved by Gaussian elimination.

### UOV Signature Scheme

**Key Generation:**
- Choose central map F with oil/vinegar structure
- Choose random invertible linear map T (S is identity in UOV)
- Public key: P = F ∘ T (m quadratic polynomials in n = v + o variables)
- Secret key: (F structure, T)

**Signing message m:**
1. Compute target: h = Hash(m) ∈ F_q^o
2. Choose random vinegar values (random v₁, ..., vᵥ)
3. Solve the resulting linear system for oil variables
4. Apply T^(-1) to get the signature

**Verification:**
- Compute P(signature) and check if it equals Hash(m)

### Parameters

For NIST Level 1 security:
- n = 112 variables (68 vinegar + 44 oil)
- m = 44 equations
- Field: F_256
- Public key: ~66 KB
- Signature: 112 bytes

### Security Considerations

UOV has been extensively studied since 1999:
- **Direct attacks:** Solve the system directly (Gröbner basis, XL)
- **Structural attacks:** Recover the oil/vinegar partition
- **Kipnis-Shamir attack:** Key recovery by finding an equivalent secret key
- **Reconciliation attack:** Exploits the MinRank problem

All known attacks are exponential with properly chosen parameters.

## 8.4 Rainbow (Historical — Broken in 2022)

Rainbow was a leading multivariate signature candidate until a devastating attack was published:

### Construction
Rainbow used a multi-layer oil-and-vinegar structure:
- Layer 1: v₁ vinegar variables, o₁ oil variables
- Layer 2: v₁ + o₁ vinegar variables, o₂ new oil variables
- Each layer's oil variables become the next layer's vinegar variables

This layered structure was intended to allow smaller keys than UOV.

### The Attack (Beullens, 2022)

Ward Beullens discovered an attack combining:
1. A new intersection attack exploiting the layered structure
2. MinRank problem formulation
3. Efficient algebraic solving

The attack broke Rainbow at all security levels:
- Rainbow Level 1 (SL-I): Broken in approximately 53 hours
- Rainbow Level 5 (SL-V): Feasible with moderate resources

### Lessons Learned

The Rainbow break illustrates important principles:
- Structured trapdoors enable efficiency but create attack surfaces
- Multi-layer constructions can be vulnerable to attacks that exploit inter-layer relationships
- Decades of study do not guarantee security — new techniques can emerge suddenly
- Algorithmic diversity in PQC standardization is essential

## 8.5 Other Multivariate Schemes

### HFE (Hidden Field Equations)

**Concept:** Define a low-degree univariate polynomial over an extension field F_{q^n}, then project to multivariate over F_q.

**Central Map:** P(X) = Σ aᵢⱼ X^(qⁱ+qʲ) over F_{q^n} (degree bound D)

**Properties:**
- Inversion uses Berlekamp's algorithm over the extension field
- Security depends on degree bound D
- Original HFE is insecure; variants (HFEv-, HFE+) add vinegar variables or remove equations

### GeMSS

A HFEv- variant that was a NIST candidate:
- Very small signatures (~33 bytes at Level 1)
- Very large public keys (~352 KB at Level 1)
- Slow verification
- Not selected for standardization

### MAYO

A recent multivariate signature scheme using "whipping" technique:
- Based on UOV with a compressed public key representation
- Significantly smaller keys than plain UOV
- Under consideration for NIST additional standardization
- Uses a public seed to derive part of the key, reducing storage

## 8.6 Gröbner Basis Attacks

The most powerful general attack on multivariate systems:

### What Are Gröbner Bases?

A Gröbner basis is a special generating set for a polynomial ideal that enables:
- Systematic solving of polynomial systems
- Extension of Gaussian elimination to nonlinear systems
- Decision procedure for ideal membership

### Algorithms

**Buchberger's Algorithm:** The original Gröbner basis algorithm (1965).

**F4 (Faugère, 1999):** Matrix-based approach:
- Reduces polynomial operations to linear algebra
- Much faster than Buchberger for cryptographic systems

**F5 (Faugère, 2002):** Avoids redundant reductions:
- More efficient criterion for detecting useless pairs
- Practically the most effective algorithm for structured systems

### Complexity

The complexity of Gröbner basis computation depends on the **degree of regularity** d_reg:
- For random systems with m = n: d_reg grows linearly with n
- Complexity: O(n^(ω·d_reg)) where ω ≈ 2.4 is the matrix multiplication exponent
- For properly parameterized multivariate schemes: super-exponential

### The XL Algorithm

A simplified version of F5 for overdetermined systems:
1. Multiply all equations by all monomials up to degree D
2. Linearize: treat each monomial as a separate variable
3. Solve the resulting large linear system

Effective when m > n (more equations than variables).

## 8.7 Quantum Attacks on Multivariate Systems

### Grover-Based Speedups

- Quantum search can be applied to exhaustive search for solutions
- Provides quadratic speedup: 2^n → 2^(n/2)
- Parameters must be doubled to maintain security

### Quantum Gröbner Basis Computation

- Some components of F4/F5 (linear algebra) get modest quantum speedups
- Overall impact is limited — the core complexity is algebraic, not search
- No exponential quantum speedup is known for MQ

### Quantum Linear Algebra

- Quantum algorithms for matrix operations provide polynomial speedups
- Applied to the linearization step in XL-like attacks
- Impact: Modest reduction in concrete security, compensated by parameter increase

## 8.8 Implementation Aspects

### Key Compression

The main practical challenge is key size:
- Full public key: m quadratic polynomials in n variables ≈ m·n(n+1)/2 field elements
- **MAYO approach:** Use a public seed to derive most of the key structure
- **Cyclic structures:** Use quasi-cyclic matrices to compress keys
- **Trade-off:** Compressed keys require more computation during signing/verification

### Signature Generation

Signing in multivariate schemes is typically very efficient:
- Fix random values (vinegar variables)
- Solve a small linear system (Gaussian elimination)
- Apply inverse affine transformation

Total: A few microseconds on modern hardware.

### Verification

Verification involves evaluating m quadratic polynomials:
- Highly parallelizable (each polynomial independent)
- Suitable for hardware acceleration
- Can use lookup tables for small fields

### Side-Channel Considerations

- **Timing:** Linear system solving must be constant-time
- **Power analysis:** Polynomial evaluation must be uniform
- **Fault attacks:** Faulted signatures can leak the secret structure

## 8.9 Comparison with Other PQC Families

| Property | UOV | ML-DSA | SLH-DSA |
|----------|-----|--------|---------|
| Signature size | ~100 B | ~2,400 B | ~8,000-50,000 B |
| Public key | ~66 KB | ~1,300 B | 32-64 B |
| Signing speed | Very fast | Fast | Moderate-Slow |
| Verification | Fast | Fast | Moderate |
| Security confidence | Medium-High | High | Very High |
| Mathematical basis | MQ problem | Module-LWE | Hash functions |
| Years of study | 25+ | 20+ | 40+ |

Multivariate signatures excel in signature size but suffer from large public keys.

## 8.10 Key Takeaways

- Multivariate cryptography is based on the NP-hard MQ problem
- The trapdoor approach disguises an invertible central map with affine transformations
- UOV is the primary surviving multivariate signature scheme
- Rainbow's break in 2022 demonstrated risks of layered multivariate constructions
- Multivariate signatures are very small and fast to sign/verify
- The main weakness is large public keys
- Gröbner basis algorithms are the primary attack tool
- No efficient quantum algorithm for MQ is known
- MAYO and other new designs address key size through compression techniques

---

*Next: [Chapter 9 — Isogeny-Based Cryptography](./09-isogeny-based.md)*
