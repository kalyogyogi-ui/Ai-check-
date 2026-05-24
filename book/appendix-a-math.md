# Appendix A: Mathematical Prerequisites

## A.1 Number Theory Basics

### Modular Arithmetic

For integers a, b, and positive integer n:
- a ≡ b (mod n) means n divides (a - b)
- Z_n = {0, 1, ..., n-1} with addition and multiplication modulo n
- Z_n* = {a ∈ Z_n : gcd(a, n) = 1} — the multiplicative group

### Finite Fields

A finite field F_q (also denoted GF(q)) has exactly q elements, where q = p^k for prime p:
- F_p = Z_p for prime p (integers mod p)
- F_{p^k} constructed via irreducible polynomials over F_p
- Every finite field is unique up to isomorphism

Key properties:
- F_q* is cyclic (has a generator/primitive element)
- |F_q*| = q - 1
- Frobenius endomorphism: x → x^p generates Gal(F_{p^k}/F_p)

## A.2 Abstract Algebra

### Groups

A group (G, ·) satisfies:
- Closure: a · b ∈ G for all a, b ∈ G
- Associativity: (a · b) · c = a · (b · c)
- Identity: ∃e ∈ G such that e · a = a · e = a
- Inverse: ∀a ∈ G, ∃a⁻¹ such that a · a⁻¹ = e

**Cyclic groups:** G = ⟨g⟩ = {g^k : k ∈ Z} for generator g

**Group order:** |G| = number of elements; ord(g) = smallest positive k with g^k = e

### Rings and Polynomial Rings

A ring (R, +, ·) has addition forming an abelian group and multiplication being associative with distributive laws.

**Polynomial ring R[x]:** Polynomials with coefficients in R
- R[x]/(f(x)): Quotient ring — polynomials modulo f(x)
- If f(x) is irreducible over R, then R[x]/(f(x)) is a field

**Key ring for PQC:** Z_q[x]/(x^n + 1) where n is a power of 2
- Elements: Polynomials of degree < n with coefficients in Z_q
- Addition: Coefficient-wise modulo q
- Multiplication: Polynomial multiplication modulo (x^n + 1) and coefficient-wise modulo q

## A.3 Linear Algebra over Finite Fields

### Vectors and Matrices

Over F_q:
- Vector space F_q^n: n-tuples of field elements
- Matrix M ∈ F_q^(m×n): m rows, n columns of field elements
- Standard operations: addition, scalar multiplication, matrix multiplication

### Important Concepts

- **Rank:** Maximum number of linearly independent rows/columns
- **Kernel/Null space:** ker(A) = {x : Ax = 0}
- **Syndrome:** For parity-check matrix H and vector r: s = Hr^T
- **Gaussian elimination:** Efficient over any field (O(n³) operations)

### Inner Products and Norms

Over Z_q (not a field if q is not prime, but operations still defined):
- Inner product: ⟨a, b⟩ = Σ aᵢbᵢ mod q
- Euclidean norm: ‖x‖₂ = √(Σ xᵢ²)
- Infinity norm: ‖x‖∞ = max|xᵢ|
- Hamming weight: wt(x) = |{i : xᵢ ≠ 0}|

## A.4 Lattice Theory

### Definitions

A lattice L ⊆ R^n is the set of all integer linear combinations of basis vectors:
```
L = L(b₁, ..., bₙ) = {Σ zᵢbᵢ : zᵢ ∈ Z}
```

### Key Parameters

- **Dimension:** n (number of basis vectors)
- **Determinant:** det(L) = |det(B)| where B is a basis matrix
- **Successive minima:** λ₁ ≤ λ₂ ≤ ... ≤ λₙ where λᵢ is the minimum radius of a ball containing i linearly independent lattice vectors
- **Covering radius:** Maximum distance from any point to the nearest lattice point

### Gaussian Heuristic

For a random lattice in dimension n:
```
λ₁(L) ≈ √(n/(2πe)) · det(L)^(1/n)
```

This gives the expected shortest vector length in a "typical" lattice.

### Dual Lattice

The dual lattice L* = {x ∈ R^n : ⟨x, v⟩ ∈ Z for all v ∈ L}
- det(L*) = 1/det(L)
- (L*)* = L

## A.5 Probability and Statistics

### Discrete Distributions

**Uniform distribution U(S):** Equal probability 1/|S| for each element of finite set S.

**Centered Binomial Distribution CBD_η:**
- Sample 2η bits (b₁, ..., b₂η)
- Output: Σᵢ₌₁^η bᵢ - Σᵢ₌η₊₁^²η bᵢ
- Range: [-η, η]
- Variance: η/2

**Discrete Gaussian D_{σ}:**
- Over Z: probability of x proportional to exp(-x²/(2σ²))
- Over lattice L: probability of v proportional to exp(-‖v‖²/(2σ²))
- Parameterized by standard deviation σ

### Statistical Distance

For distributions X and Y over domain D:
```
Δ(X, Y) = (1/2) · Σ_{d∈D} |Pr[X=d] - Pr[Y=d]|
```

Distributions are **statistically close** if Δ(X, Y) is negligible in the security parameter.

### Computational Indistinguishability

Distributions X and Y are computationally indistinguishable if no polynomial-time algorithm can distinguish samples from X vs. Y with non-negligible advantage.

## A.6 Elliptic Curves

### Weierstrass Form

Over a field K with char(K) ≠ 2, 3:
```
E: y² = x³ + ax + b  (4a³ + 27b² ≠ 0)
```

### Group Law

Points on E(K) form an abelian group:
- Identity: Point at infinity O
- Addition: Geometric (chord-and-tangent rule)
- Negation: -(x, y) = (x, -y)

### Key Properties for PQC

- **j-invariant:** j(E) classifies curves up to isomorphism over algebraically closed fields
- **Endomorphism ring:** End(E) — ring of group homomorphisms E → E
  - Ordinary curves: End(E) is an order in an imaginary quadratic field
  - Supersingular curves: End(E) is a maximal order in a quaternion algebra
- **Isogeny:** Surjective group homomorphism φ: E₁ → E₂ (morphism of varieties)
  - Determined by kernel subgroup
  - Vélu's formulas compute isogeny from kernel

## A.7 Number Theoretic Transform (NTT)

### Definition

For polynomial ring Z_q[x]/(x^n + 1) where q ≡ 1 (mod 2n):

Let ω be a primitive 2n-th root of unity in Z_q. The NTT maps:
```
â = NTT(a): âᵢ = Σⱼ aⱼ · ωⁱ⁽²ʲ⁺¹⁾  for i = 0, ..., n-1
```

### Properties

- **Pointwise multiplication:** NTT(a · b) = NTT(a) ⊙ NTT(b) (component-wise)
- **Inverse:** INTT recovers original polynomial
- **Complexity:** O(n log n) using butterfly decomposition
- **In ML-KEM:** q = 3329, n = 256, primitive root ω = 17

### Butterfly Operation

The basic NTT building block:
```
(a', b') = (a + ω^k · b,  a - ω^k · b)
```

All operations modulo q, computed in constant time.

## A.8 Hash Functions and Random Oracles

### Cryptographic Hash Function Properties

A hash function H: {0,1}* → {0,1}^n should satisfy:
- **Preimage resistance:** Given y, hard to find x with H(x) = y
- **Second preimage resistance:** Given x, hard to find x' ≠ x with H(x) = H(x')
- **Collision resistance:** Hard to find any x ≠ x' with H(x) = H(x')

### Random Oracle Model

The Random Oracle (RO) is an idealized hash function:
- Behaves as a truly random function (each output is uniformly random and independent)
- Security proofs in the RO model: Show that breaking the scheme requires "unusual" hash queries
- Standard model: Proofs that don't assume RO (stronger but harder to achieve)

### Quantum Random Oracle Model (QROM)

In the QROM:
- Adversary can query the random oracle in quantum superposition
- Provides stronger security guarantees than classical ROM
- Some classical ROM proofs fail in QROM; new techniques needed

## A.9 Complexity Theory Basics

### Key Complexity Classes

- **P:** Problems solvable in polynomial time
- **NP:** Problems verifiable in polynomial time
- **BPP:** Problems solvable in probabilistic polynomial time with bounded error
- **BQP:** Problems solvable on a quantum computer in polynomial time with bounded error

### Reductions

A **reduction** from problem A to problem B shows that solving B solves A:
- If A is hard, then B is at least as hard
- Security reductions show: breaking the crypto scheme implies solving the hard problem
- **Tight reduction:** Security loss is minimal (close to 1:1)

### Negligible Functions

A function ν(n) is negligible if for every polynomial p(n), there exists N such that for all n > N:
```
ν(n) < 1/p(n)
```

Cryptographic security requires that attack success probability is negligible in the security parameter.

## A.10 Further Mathematical Reading

For deeper study:
- **Lattice theory:** Micciancio & Goldwasser, "Complexity of Lattice Problems"
- **Algebraic number theory:** Neukirch, "Algebraic Number Theory"
- **Elliptic curves:** Silverman, "The Arithmetic of Elliptic Curves"
- **Coding theory:** MacWilliams & Sloane, "The Theory of Error-Correcting Codes"
- **Computational complexity:** Arora & Barak, "Computational Complexity: A Modern Approach"
- **Quantum computing:** Nielsen & Chuang, "Quantum Computation and Quantum Information"
