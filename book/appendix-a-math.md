# Appendix A: Mathematical Prerequisites

This appendix provides the mathematical foundations needed to understand the constructions, security proofs, and parameter selections in post-quantum cryptography. Readers familiar with undergraduate mathematics may use this as a reference; those encountering these topics for the first time should work through examples alongside the definitions.

## A.1 Number Theory Basics

### Modular Arithmetic

For integers a, b, and a positive integer n, we say a is congruent to b modulo n, written a ≡ b (mod n), if n divides (a - b). The set of residues modulo n is denoted Z_n = {0, 1, 2, ..., n-1}. This set forms a ring under addition and multiplication modulo n.

The multiplicative group of Z_n, denoted Z_n* = {a ∈ Z_n : gcd(a, n) = 1}, consists of elements that have multiplicative inverses. The order of this group is given by Euler's totient function φ(n). For prime p, φ(p) = p - 1, meaning every nonzero element is invertible. For a product of two distinct primes p and q, φ(pq) = (p-1)(q-1).

Modular exponentiation can be performed efficiently via repeated squaring: to compute a^k mod n, we decompose k in binary and perform O(log k) multiplications. This is critical for both classical and post-quantum cryptographic operations.

The extended Euclidean algorithm computes gcd(a, b) along with integers x, y satisfying ax + by = gcd(a, b). When gcd(a, n) = 1, this yields the modular inverse a^(-1) mod n in O(log n) arithmetic operations.

### Euler's Theorem and Fermat's Little Theorem

Euler's theorem states that for any a with gcd(a, n) = 1:

```
a^φ(n) ≡ 1 (mod n)
```

As a special case, Fermat's little theorem gives a^(p-1) ≡ 1 (mod p) for prime p and a not divisible by p. This result is fundamental for understanding the structure of finite fields and for efficient computation of modular inverses: a^(-1) ≡ a^(p-2) (mod p).

### Chinese Remainder Theorem (CRT)

If n₁, n₂, ..., nₖ are pairwise coprime, then the system of congruences x ≡ aᵢ (mod nᵢ) for i = 1, ..., k has a unique solution modulo N = n₁n₂···nₖ. The CRT provides an isomorphism:

```
Z_N ≅ Z_{n₁} × Z_{n₂} × ... × Z_{nₖ}
```

This isomorphism preserves ring structure and enables computations modulo a large N to be decomposed into independent computations modulo smaller moduli. In the context of PQC, the CRT appears in NTT decompositions and in some parameter choices for lattice-based schemes.

The constructive form of the CRT computes the solution as x = Σᵢ aᵢ · Nᵢ · (Nᵢ^(-1) mod nᵢ) mod N, where Nᵢ = N/nᵢ. This can be computed in O(k · log²N) bit operations.

### Finite Fields

A finite field (or Galois field) F_q has exactly q elements, where q must be a prime power q = p^k. The prime p is called the characteristic of the field.

**Prime fields:** When k = 1, we have F_p = Z_p, the integers modulo a prime p. Arithmetic is simply addition and multiplication of integers reduced modulo p.

**Extension fields:** When k > 1, the field F_{p^k} is constructed as a quotient F_p[x]/(f(x)) where f(x) is an irreducible polynomial of degree k over F_p. Elements are polynomials of degree less than k with coefficients in F_p, and multiplication is polynomial multiplication reduced modulo f(x).

Every finite field of a given order is unique up to isomorphism. The multiplicative group F_q* = F_q \ {0} is cyclic of order q - 1, meaning there exists a generator g (primitive element) such that every nonzero element can be written as a power of g.

**Frobenius endomorphism:** The map φ: F_{p^k} → F_{p^k} defined by φ(x) = x^p is a field automorphism. It generates the Galois group Gal(F_{p^k}/F_p), which is cyclic of order k. The fixed field of φ is precisely F_p. The Frobenius plays a central role in the theory of elliptic curves over finite fields and in the analysis of extension field arithmetic relevant to isogeny-based cryptography.

**Subfield structure:** F_{p^m} is a subfield of F_{p^k} if and only if m divides k. The trace map Tr: F_{p^k} → F_p defined by Tr(x) = x + x^p + x^(p²) + ... + x^(p^(k-1)) is a surjective F_p-linear map used in various cryptographic constructions.

## A.2 Abstract Algebra

### Groups

A group (G, ·) is a set G equipped with a binary operation satisfying four axioms:

1. **Closure:** For all a, b ∈ G, the product a · b ∈ G.
2. **Associativity:** For all a, b, c ∈ G, (a · b) · c = a · (b · c).
3. **Identity:** There exists an element e ∈ G such that e · a = a · e = a for all a ∈ G.
4. **Inverse:** For every a ∈ G, there exists a⁻¹ ∈ G with a · a⁻¹ = a⁻¹ · a = e.

If additionally a · b = b · a for all elements, the group is called abelian (or commutative). We often write abelian groups additively, with the operation denoted + and the identity denoted 0.

**Cyclic groups:** A group G is cyclic if G = ⟨g⟩ = {g^k : k ∈ Z} for some generator g. Every cyclic group of order n is isomorphic to Z_n. Cyclic groups are always abelian. The number of generators of a cyclic group of order n equals φ(n).

**Group order:** The order |G| is the number of elements. The order of an element g, written ord(g), is the smallest positive integer k such that g^k = e. By Lagrange's theorem, the order of any element divides the order of the group.

**Group homomorphisms:** A map φ: G → H between groups is a homomorphism if φ(ab) = φ(a)φ(b) for all a, b ∈ G. An isomorphism is a bijective homomorphism. The kernel ker(φ) = {a ∈ G : φ(a) = e_H} is always a normal subgroup.

**Quotient groups:** For a normal subgroup N of G, the quotient group G/N consists of cosets gN with multiplication (gN)(hN) = (gh)N. This construction is essential for understanding polynomial quotient rings.

### Rings and Ideals

A ring (R, +, ·) is a set with two operations where (R, +) is an abelian group, multiplication is associative, and the distributive laws hold: a(b + c) = ab + ac and (a + b)c = ac + bc. A commutative ring has ab = ba. A ring with identity has a multiplicative identity element 1.

An ideal I of a ring R is a subset that is an additive subgroup and absorbs multiplication: for all r ∈ R and a ∈ I, both ra ∈ I and ar ∈ I. The principal ideal generated by element a is (a) = {ra : r ∈ R}.

The quotient ring R/I consists of cosets r + I with operations (r + I) + (s + I) = (r + s) + I and (r + I)(s + I) = (rs) + I. A maximal ideal M yields a field R/M; a prime ideal P yields an integral domain R/P.

### Polynomial Rings

The polynomial ring R[x] consists of formal expressions a₀ + a₁x + a₂x² + ... + aₙxⁿ with coefficients aᵢ ∈ R. Addition is coefficient-wise; multiplication uses the convolution formula. If R is a commutative ring with identity, so is R[x].

**Division with remainder:** When R is a field F, we can perform polynomial division: for any f(x), g(x) ∈ F[x] with g ≠ 0, there exist unique q(x), r(x) with f = qg + r and deg(r) < deg(g). This makes F[x] a Euclidean domain and principal ideal domain.

**Irreducible polynomials:** A polynomial f(x) ∈ F[x] of degree ≥ 1 is irreducible if it cannot be factored as a product of two polynomials of smaller positive degree. Irreducible polynomials play the role of primes. The quotient F[x]/(f(x)) is a field if and only if f(x) is irreducible.

### Quotient Rings of Polynomials

The quotient ring R[x]/(f(x)) consists of equivalence classes of polynomials modulo f(x). Each class has a unique representative of degree less than deg(f). Elements can be identified with polynomials of degree < deg(f), with multiplication followed by reduction modulo f(x).

**The key ring for PQC: Z_q[x]/(x^n + 1)** where n is a power of 2 and q is a prime.

This ring is central to ML-KEM and ML-DSA. Its elements are polynomials a₀ + a₁x + ... + a_{n-1}x^{n-1} with coefficients in Z_q = {0, 1, ..., q-1}. Arithmetic proceeds as follows:

- **Addition:** Coefficient-wise modulo q: (a + b)ᵢ = aᵢ + bᵢ mod q.
- **Multiplication:** Polynomial multiplication followed by reduction modulo x^n + 1 and coefficient reduction modulo q. The key identity is x^n ≡ -1 (mod x^n + 1), so any term x^{n+j} becomes -x^j.

The polynomial x^n + 1 is the 2n-th cyclotomic polynomial Φ_{2n}(x) when n is a power of 2. It factors into n irreducible polynomials of degree 1 over Z_q when q ≡ 1 (mod 2n), which is precisely the condition enabling the Number Theoretic Transform. This ring has nice algebraic properties: it is a principal ideal domain, and the negacyclic structure provides resistance against certain algebraic attacks that affect simpler quotient rings.

The module structure used in ML-KEM and ML-DSA considers vectors and matrices over this ring: an element of R_q^k is a vector of k ring elements, and multiplication of a matrix A ∈ R_q^{k×k} by a vector s ∈ R_q^k involves ring multiplications rather than scalar multiplications.

## A.3 Linear Algebra over Finite Fields

### Vectors and Matrices

A vector space over F_q consists of n-tuples F_q^n = {(v₁, v₂, ..., vₙ) : vᵢ ∈ F_q} with component-wise addition and scalar multiplication. A matrix M ∈ F_q^{m×n} has m rows and n columns with entries in F_q.

Standard matrix operations — addition, scalar multiplication, transposition, and matrix multiplication — work identically to real linear algebra, except all arithmetic occurs in F_q. The key difference is that F_q has finite characteristic p, so p · v = 0 for any vector v.

**Linear maps and matrices:** Every F_q-linear map T: F_q^n → F_q^m can be represented by a matrix M ∈ F_q^{m×n} via T(v) = Mv. Composition of linear maps corresponds to matrix multiplication.

### Rank, Kernel, and Image

The rank of a matrix A ∈ F_q^{m×n} is the dimension of its column space (equivalently, its row space). Key facts:

- rank(A) ≤ min(m, n)
- A has full row rank if rank(A) = m
- A has full column rank if rank(A) = n
- The rank-nullity theorem: rank(A) + dim(ker(A)) = n

The kernel (null space) of A is ker(A) = {x ∈ F_q^n : Ax = 0}. Its dimension is n - rank(A). In code-based cryptography, the kernel of a parity-check matrix contains exactly the codewords.

The image (column space) of A is im(A) = {Ax : x ∈ F_q^n}. Its dimension equals rank(A).

### Syndrome and Decoding

For a linear code C with parity-check matrix H ∈ F_q^{(n-k)×n}, the syndrome of a received vector r is s = Hr^T. The syndrome captures the "error pattern":

- If r = c + e where c is a codeword and e is an error, then s = Hr^T = He^T (since Hc^T = 0 for all codewords).
- Syndrome decoding: find the minimum weight vector e with He^T = s.
- This decoding problem underlies the security of code-based cryptography (McEliece, HQC).

The syndrome space F_q^{n-k} has q^{n-k} elements, while there are q^n possible received vectors. Each coset of C maps to a unique syndrome, providing a many-to-one mapping that is computationally hard to invert for random codes.

### Gaussian Elimination

Gaussian elimination over F_q proceeds identically to the real case: pivot selection, row scaling, and row addition, with all arithmetic in F_q. It achieves:

- Row echelon form in O(mn · min(m,n)) field operations
- Determinant computation for square matrices
- System solving: Ax = b has solutions if and only if rank(A) = rank(A|b)
- Kernel computation: the null space basis can be read from the reduced row echelon form

Over finite fields, Gaussian elimination never encounters numerical stability issues (no rounding errors), making it perfectly reliable. However, its cubic complexity means it is not suitable for very large instances, motivating the use of structured matrices in lattice-based cryptography.

### Inner Products and Norms

While norms are typically defined over the reals, several norm-like functions on Z_q^n are essential for PQC:

**Inner product:** For vectors a, b ∈ Z_q^n, the inner product is ⟨a, b⟩ = Σᵢ aᵢbᵢ mod q. The LWE problem involves distinguishing (A, As + e) from (A, u) where s is secret and e is a short error vector.

**Euclidean norm (ℓ₂ norm):** For a vector x ∈ Z^n (lifted to integers in [-q/2, q/2)), ‖x‖₂ = √(Σᵢ xᵢ²). This measures the "size" of a lattice vector or error term. Short vectors with small ℓ₂ norm are central to lattice-based cryptography.

**Infinity norm (ℓ∞ norm):** ‖x‖∞ = max|xᵢ| where coefficients are centered in [-q/2, q/2). ML-KEM parameter selection ensures that error terms have bounded ℓ∞ norm with overwhelming probability.

**ℓ₁ norm:** ‖x‖₁ = Σᵢ |xᵢ|, used occasionally in analysis of noise growth.

**Hamming weight:** wt(x) = |{i : xᵢ ≠ 0}|, counting nonzero positions. Central to code-based cryptography where errors have bounded Hamming weight.

The relationship between these norms for vectors in Z^n satisfies: ‖x‖∞ ≤ ‖x‖₂ ≤ ‖x‖₁ ≤ n·‖x‖∞ and ‖x‖₂ ≤ √n · ‖x‖∞. These inequalities are used in security proofs to convert between different notions of "shortness."

## A.4 Lattice Theory

### Definitions

A lattice L in R^n is the set of all integer linear combinations of a set of linearly independent vectors b₁, b₂, ..., bₘ ∈ R^n:

```
L = L(b₁, ..., bₘ) = {Σᵢ₌₁^m zᵢbᵢ : zᵢ ∈ Z}
```

The vectors b₁, ..., bₘ form a basis of the lattice. The integer m is the rank of the lattice, and n is the ambient dimension. When m = n, the lattice is called full-rank. Most cryptographic lattices are full-rank.

A lattice has infinitely many bases: if B is a basis matrix (columns are basis vectors) and U is any unimodular matrix (integer matrix with determinant ±1), then BU is also a basis for the same lattice. Different bases can look dramatically different — some with short, nearly orthogonal vectors and others with long, highly correlated vectors. This disparity between "good" and "bad" bases is what makes lattice cryptography possible.

**q-ary lattices:** For a matrix A ∈ Z_q^{n×m}, define:
- Λ_q(A) = {x ∈ Z^m : x ≡ A^T s (mod q) for some s ∈ Z_q^n}
- Λ_q⊥(A) = {x ∈ Z^m : Ax ≡ 0 (mod q)}

These q-ary lattices are the natural lattice families arising in LWE-based and SIS-based cryptography. Both have determinant q^n (for suitable dimensions).

### Key Parameters

**Dimension:** The rank m of the lattice. Lattice problems become harder as dimension increases (super-exponentially in the best known algorithms). Cryptographic parameters typically use dimensions between 256 and 1024.

**Determinant:** For a full-rank lattice with basis matrix B ∈ R^{n×n}, det(L) = |det(B)|. This is independent of the choice of basis. The determinant measures the "density" of the lattice: larger determinant means lattice points are more spread out, and the fundamental domain has larger volume.

**Successive minima:** The i-th successive minimum λᵢ(L) is the smallest radius r such that the closed ball of radius r centered at the origin contains at least i linearly independent lattice vectors:

```
λᵢ(L) = inf{r : dim(span(L ∩ B̄(0, r))) ≥ i}
```

The first successive minimum λ₁(L) is the length of the shortest nonzero vector. Minkowski's first theorem gives λ₁(L) ≤ √n · det(L)^{1/n}, ensuring short vectors exist.

**Covering radius:** μ(L) = max_{x ∈ R^n} min_{v ∈ L} ‖x - v‖₂. This is the maximum distance from any point in space to the nearest lattice point. The Bounded Distance Decoding (BDD) problem asks to find the nearest lattice point to a target within some fraction of the covering radius.

**Smoothing parameter:** η_ε(L) is the smallest s such that the discrete Gaussian over the dual lattice with parameter 1/s has statistical distance at most ε from uniform. This parameter governs when a discrete Gaussian over the lattice "looks" continuous, and appears in security reductions for lattice-based schemes.

### Gaussian Heuristic

For a "random" lattice of rank n with determinant det(L), the Gaussian heuristic predicts:

```
λ₁(L) ≈ √(n/(2πe)) · det(L)^{1/n)
```

This approximation estimates the shortest vector length by modeling lattice points as if they were uniformly distributed with the correct density. The heuristic becomes increasingly accurate as dimension grows and is the basis for concrete security estimates in lattice-based cryptography.

For q-ary lattices with det(L) = q^{n/m} (in the appropriate formulation), the Gaussian heuristic gives λ₁ ≈ √(m/(2πe)) · q^{n/m}. Parameters are chosen so that the LWE error vector is shorter than this heuristic bound, enabling correct decryption while ensuring that finding such short vectors is computationally hard.

### Dual Lattice

The dual lattice of L is defined as:

```
L* = {x ∈ R^n : ⟨x, v⟩ ∈ Z for all v ∈ L}
```

Key properties of the dual:
- If B is a basis for L, then (B^{-T}) is a basis for L* (for full-rank lattices)
- det(L*) = 1/det(L)
- (L*)* = L (biduality)
- λ₁(L) · λₙ(L*) ≥ 1 (transference theorem)
- For q-ary lattices: (Λ_q⊥(A))* = (1/q) · Λ_q(A)

The dual lattice appears in the security analysis of LWE: the decision-LWE problem can be rephrased in terms of distinguishing a point close to the dual lattice from a random point. Transference theorems relate the hardness of problems on L to problems on L*.

### Minkowski's Bounds and Blichfeldt's Theorem

Minkowski's convex body theorem states: if S ⊂ R^n is a convex set symmetric about the origin with vol(S) > 2^n · det(L), then S contains a nonzero lattice point. Applied to an n-dimensional ball:

```
λ₁(L) ≤ √n · det(L)^{1/n}
```

A tighter bound due to Minkowski-Hlawka shows existence of lattices achieving λ₁(L) ≥ c · √n · det(L)^{1/n} for a constant c, demonstrating the Gaussian heuristic is roughly tight.

### Computational Lattice Problems

The following problems form the security foundation of lattice-based PQC:

**Shortest Vector Problem (SVP):** Given a basis B of lattice L, find a nonzero vector v ∈ L with ‖v‖₂ = λ₁(L). The approximate version γ-SVP asks for v with ‖v‖ ≤ γ · λ₁(L).

**Closest Vector Problem (CVP):** Given a basis B and target t ∈ R^n, find the lattice vector v ∈ L closest to t. The approximate version γ-CVP allows ‖v - t‖ ≤ γ · dist(t, L).

**Bounded Distance Decoding (BDD):** A special case of CVP where the target is promised to be within distance α · λ₁(L) of a lattice point (for α < 1/2). The LWE problem reduces to BDD on q-ary lattices.

**Short Integer Solution (SIS):** Given A ∈ Z_q^{n×m}, find a short nonzero x ∈ Z^m with Ax ≡ 0 (mod q) and ‖x‖ ≤ β. This problem underlies lattice-based hash functions and signature schemes.

The best known algorithms for these problems in high dimensions are lattice sieving algorithms achieving time 2^{0.292n+o(n)} for SVP and the BKZ algorithm with block size β achieving approximation factor roughly 2^{n/β} in time 2^{0.292β+o(β)}.

## A.5 Probability and Statistics

### Discrete Distributions

**Uniform distribution U(S):** Assigns equal probability 1/|S| to each element of a finite set S. In cryptography, uniformly random values serve as idealized keys, nonces, and challenges. Sampling uniformly from Z_q or {0,1}^n is a fundamental primitive.

**Bernoulli distribution:** A binary random variable X with Pr[X = 1] = p and Pr[X = 0] = 1 - p. The building block for more complex distributions.

**Binomial distribution B(n, p):** The sum of n independent Bernoulli(p) trials. Takes values in {0, 1, ..., n} with Pr[X = k] = C(n,k) · p^k · (1-p)^{n-k}.

**Centered Binomial Distribution CBD_η:** The noise distribution used in ML-KEM and ML-DSA. To sample from CBD_η:
1. Sample 2η independent uniform bits b₁, ..., b_{2η}.
2. Output: (b₁ + b₂ + ... + b_η) - (b_{η+1} + b_{η+2} + ... + b_{2η}).

Properties of CBD_η:
- Range: {-η, -η+1, ..., η-1, η}
- Mean: 0 (centered/symmetric)
- Variance: η/2
- Maximum absolute value: η (with probability 2^{-2η+1})
- Efficiently samplable from uniform random bits
- Approximates a discrete Gaussian with σ² = η/2

The CBD is preferred over the discrete Gaussian in ML-KEM/ML-DSA because it can be sampled in constant time without rejection sampling, eliminating a potential timing side-channel. The parameter η controls the tradeoff between noise magnitude and security.

**Discrete Gaussian Distribution D_{Z,σ,c}:** Over the integers Z, centered at c (often c = 0), with parameter σ > 0:

```
Pr[X = x] = ρ_σ(x - c) / Σ_{z ∈ Z} ρ_σ(z - c)
```

where ρ_σ(x) = exp(-πx²/σ²) is the Gaussian function. Properties:
- Symmetric about c
- Tails decrease super-exponentially: Pr[|X - c| > t·σ] ≤ 2·exp(-πt²)
- With overwhelming probability, samples satisfy |x - c| < σ√(2ln(2/ε)·n) for dimension n

Over a lattice L, the discrete Gaussian D_{L,σ,c} assigns probability proportional to ρ_σ(v - c) to each lattice point v ∈ L. This distribution is used in FN-DSA (FALCON) signature generation via lattice-based trapdoor sampling.

**Uniform over bounded sets:** Many PQC schemes sample coefficients uniformly from small ranges, e.g., from {-η, ..., η} or {0, 1, ..., q-1}. ML-KEM samples public matrix entries uniformly from Z_q.

### Statistical Distance

The statistical distance (total variation distance) between two distributions X and Y over a common domain D is:

```
Δ(X, Y) = (1/2) · Σ_{d∈D} |Pr[X = d] - Pr[Y = d]|
```

Equivalent characterizations:
- Δ(X, Y) = max_{S ⊆ D} |Pr[X ∈ S] - Pr[Y ∈ S]|
- Δ(X, Y) represents the maximum advantage any (even unbounded) distinguisher can achieve

Properties of statistical distance:
- 0 ≤ Δ(X, Y) ≤ 1
- Δ(X, Y) = 0 if and only if X and Y are identical distributions
- Triangle inequality: Δ(X, Z) ≤ Δ(X, Y) + Δ(Y, Z)
- Data processing inequality: for any (randomized) function f, Δ(f(X), f(Y)) ≤ Δ(X, Y)

Distributions are statistically close (written X ≈_s Y) if Δ(X, Y) ≤ negl(λ) for security parameter λ. Statistical closeness implies that no distinguisher — even an computationally unbounded one — can tell them apart with non-negligible probability.

### Rényi Divergence

The Rényi divergence of order α > 1 between distributions P and Q is:

```
R_α(P ‖ Q) = (1/(α-1)) · ln(Σ_x P(x)^α / Q(x)^{α-1})
```

The Rényi divergence provides tighter security bounds than statistical distance in some lattice-based proofs, particularly for FN-DSA. It satisfies a multiplicative version of the data processing inequality and enables security proofs with better parameters.

### Computational Indistinguishability

Two distribution ensembles {X_λ}_{λ∈N} and {Y_λ}_{λ∈N} are computationally indistinguishable (written X ≈_c Y) if for every probabilistic polynomial-time (PPT) algorithm D:

```
|Pr[D(X_λ) = 1] - Pr[D(Y_λ) = 1]| ≤ negl(λ)
```

This is weaker than statistical closeness: distributions may be far apart statistically but still computationally indistinguishable because efficient algorithms cannot detect the difference. The LWE assumption, for instance, asserts that (A, As + e) is computationally indistinguishable from (A, u) even though they are statistically far apart.

### Negligible Functions

A function ν: N → R is negligible if for every positive polynomial p(n), there exists N₀ such that for all n > N₀:

```
ν(n) < 1/p(n)
```

Equivalently, ν(n) decreases faster than the inverse of any polynomial. Typical examples: 2^{-n}, 2^{-√n}, n^{-log n}. Non-examples: 1/n², 1/n^{100} (these are polynomial-bounded).

Cryptographic security guarantees take the form: "the advantage of any PPT adversary is negligible in the security parameter λ." Concretely, for 128-bit security, we want attack success probability at most 2^{-128}, which is negligible for practical security parameter choices.

The sum and product of negligible functions remain negligible. This closure property enables hybrid arguments in security proofs where the overall advantage bounds a polynomial sum of negligible terms.

### Leftover Hash Lemma

The leftover hash lemma (LHL) states that if H is a universal hash family from {0,1}^n to {0,1}^m and X is a random variable with min-entropy k, then for a random h ← H:

```
Δ((h, h(X)), (h, U_m)) ≤ (1/2) · 2^{(m-k)/2}
```

This is negligible when k > m + 2λ for security parameter λ. The LHL is used in lattice-based constructions to argue that products As (mod q) are close to uniform when s has sufficient entropy.

## A.6 Elliptic Curves

### Weierstrass Form

An elliptic curve over a field K is a smooth projective algebraic curve of genus 1 with a specified rational point. Over a field with char(K) ≠ 2, 3, every elliptic curve can be written in short Weierstrass form:

```
E: y² = x³ + ax + b
```

where a, b ∈ K satisfy the non-singularity condition 4a³ + 27b² ≠ 0 (equivalently, the discriminant Δ = -16(4a³ + 27b²) ≠ 0).

Over fields of characteristic 2 or 3, more general Weierstrass equations are needed:

```
y² + a₁xy + a₃y = x³ + a₂x² + a₄x + a₆
```

The set of K-rational points E(K) = {(x, y) ∈ K² : y² = x³ + ax + b} ∪ {O} includes the point at infinity O, which serves as the identity element.

### Group Law

The K-rational points E(K) form an abelian group under a geometrically-defined addition operation:

**Point addition (P ≠ Q):** To add P = (x₁, y₁) and Q = (x₂, y₂) with x₁ ≠ x₂:
- Slope: λ = (y₂ - y₁)/(x₂ - x₁)
- x₃ = λ² - x₁ - x₂
- y₃ = λ(x₁ - x₃) - y₁
- P + Q = (x₃, y₃)

**Point doubling (P = Q):** To compute 2P = P + P for P = (x₁, y₁) with y₁ ≠ 0:
- Slope: λ = (3x₁² + a)/(2y₁)
- x₃ = λ² - 2x₁
- y₃ = λ(x₁ - x₃) - y₁
- 2P = (x₃, y₃)

**Identity and inverses:** The point at infinity O is the identity: P + O = P for all P. The inverse of P = (x, y) is -P = (x, -y).

For E over F_q, the group E(F_q) is finite. By Hasse's theorem: |#E(F_q) - (q + 1)| ≤ 2√q. The structure theorem gives E(F_q) ≅ Z/n₁Z × Z/n₂Z where n₂ | n₁ and n₂ | (q - 1).

### j-Invariant

The j-invariant of an elliptic curve E: y² = x³ + ax + b is:

```
j(E) = 1728 · (4a³)/(4a³ + 27b²)
```

Two elliptic curves over an algebraically closed field are isomorphic if and only if they have the same j-invariant. Over non-closed fields, the j-invariant classifies isomorphism classes up to twists.

For every j₀ ∈ K, there exists an elliptic curve with j(E) = j₀ (except j = 0 and j = 1728 require special treatment in small characteristic). The j-invariant takes all values in F_q as E ranges over isomorphism classes of curves over F_q, and the number of isomorphism classes of curves with a given j-invariant is either 1, 2, or 6.

In isogeny-based cryptography, the j-invariant serves as the "public key" component: walking along isogeny graphs changes the j-invariant, and security relies on the difficulty of finding the path between two j-invariants.

### Endomorphism Ring

The endomorphism ring End(E) of an elliptic curve E over K consists of all group homomorphisms φ: E → E that are also morphisms of algebraic varieties, together with the zero map. Under addition and composition, End(E) forms a ring.

Every endomorphism ring contains Z (generated by the multiplication-by-n maps [n]: P → nP). The structure depends on the curve type:

**Ordinary curves:** End(E) is isomorphic to an order in an imaginary quadratic field Q(√(-d)) for some positive squarefree d. The discriminant of End(E) determines the isogeny class and connects to class field theory.

**Supersingular curves:** End(E) is isomorphic to a maximal order in a quaternion algebra B_{p,∞} ramified at p and ∞. Supersingular curves have richer endomorphism structure (rank 4 over Z versus rank 2 for ordinary curves). The quaternion algebra structure makes the endomorphism ring problem computationally hard, which is exploited in SQISign and related schemes.

The endomorphism ring problem (computing End(E) given E) is believed to be hard for supersingular curves and forms the foundation of some isogeny-based signature schemes.

### Isogenies

An isogeny φ: E₁ → E₂ is a non-constant morphism of elliptic curves that is also a group homomorphism. Key properties:

- Every isogeny is surjective (over the algebraic closure)
- The kernel ker(φ) is a finite subgroup of E₁
- The degree of φ equals |ker(φ)| (for separable isogenies)
- For every finite subgroup G ⊂ E, there exists a unique (up to isomorphism) isogeny φ: E → E/G with kernel G

**Vélu's formulas:** Given a finite subgroup G ⊂ E(K), Vélu's formulas explicitly compute the isogenous curve E' = E/G and the isogeny φ: E → E' in O(|G|) field operations. For large kernels, the √élu algorithm achieves O(√|G|) complexity.

**Dual isogeny:** For every isogeny φ: E₁ → E₂ of degree d, there exists a unique dual isogeny φ̂: E₂ → E₁ with φ̂ ∘ φ = [d] and φ ∘ φ̂ = [d].

**Isogeny graphs:** Fix a prime ℓ. The ℓ-isogeny graph has vertices representing j-invariants of elliptic curves (or isomorphism classes) and edges representing degree-ℓ isogenies. For supersingular curves over F_{p²}, this graph is (ℓ+1)-regular (a Ramanujan graph) with excellent expansion properties. Walking in this graph forms the basis of isogeny-based key exchange and signatures.

The security of isogeny-based cryptography relies on the difficulty of the path-finding problem: given two vertices in the supersingular isogeny graph, find a path (sequence of isogenies) connecting them. After the Castryck-Decru attack broke SIDH/SIKE (which revealed torsion point information), current schemes like SQISign avoid revealing such auxiliary data.

## A.7 Number Theoretic Transform (NTT)

### Definition and Context

The Number Theoretic Transform is the finite-field analog of the discrete Fourier transform. It enables polynomial multiplication in Z_q[x]/(x^n + 1) in O(n log n) operations rather than the naive O(n²), making it indispensable for efficient lattice-based cryptography.

For the NTT to work on Z_q[x]/(x^n + 1) where n is a power of 2, we need q ≡ 1 (mod 2n). This ensures the existence of a primitive 2n-th root of unity ω ∈ Z_q (meaning ω^{2n} ≡ 1 and ω^k ≢ 1 for 0 < k < 2n).

The forward NTT maps a polynomial a(x) = a₀ + a₁x + ... + a_{n-1}x^{n-1} to its evaluation representation:

```
â_i = NTT(a)_i = Σ_{j=0}^{n-1} a_j · ω^{(2i+1)j}  for i = 0, 1, ..., n-1
```

The evaluations are at the points ω, ω³, ω⁵, ..., ω^{2n-1} (the primitive 2n-th roots of unity), which are the roots of x^n + 1 in Z_q. This means the NTT decomposes the ring Z_q[x]/(x^n + 1) into a product of n copies of Z_q:

```
Z_q[x]/(x^n + 1) ≅ Z_q × Z_q × ... × Z_q  (n copies, via CRT)
```

### Properties

**Pointwise multiplication:** The key property enabling fast polynomial multiplication:
```
NTT(a · b mod (x^n + 1)) = NTT(a) ⊙ NTT(b)
```
where ⊙ denotes component-wise multiplication. This reduces polynomial multiplication (O(n²) naively) to n independent modular multiplications plus two NTT computations.

**Linearity:** NTT(a + b) = NTT(a) + NTT(b) and NTT(c·a) = c·NTT(a) for scalar c.

**Inverse NTT:** The INTT recovers the polynomial from its evaluation representation:
```
a_j = n^{-1} · Σ_{i=0}^{n-1} â_i · ω^{-(2i+1)j}  for j = 0, 1, ..., n-1
```

**Parseval-like property:** ‖NTT(a)‖² = n · ‖a‖² (up to the n^{-1} normalization factor in INTT).

### Butterfly Operation

The NTT is computed using the Cooley-Tukey butterfly decomposition. The basic butterfly operation combines two values using a "twiddle factor" ω^k:

```
(a', b') = (a + ω^k · b,  a - ω^k · b)  mod q
```

This in-place operation takes two inputs and produces two outputs using one multiplication and two additions modulo q. The full n-point NTT uses (n/2)·log₂(n) butterfly operations arranged in log₂(n) layers.

The inverse butterfly (Gentleman-Sande) reverses the process:
```
(a', b') = ((a + b)/2,  (a - b)/(2ω^k))  mod q
```

Implementation considerations:
- All operations are modular arithmetic in Z_q — no floating point
- The butterfly structure enables parallelization and vectorization
- Constant-time implementation is straightforward (no data-dependent branches)
- Memory access patterns are fixed (no data-dependent indexing)

### Connection to ML-KEM

In ML-KEM (FIPS 203), the NTT uses:
- Ring: Z_q[x]/(x^n + 1) with q = 3329 and n = 256
- Primitive 2n-th root: ω = 17 (since 17^{512} ≡ 1 mod 3329 and 17^{256} ≡ -1 mod 3329)
- The condition q ≡ 1 (mod 2n): 3329 ≡ 1 (mod 512) ✓

ML-KEM stores polynomials in NTT domain for efficiency. Key generation, encapsulation, and decapsulation perform most operations in NTT domain, converting back only when needed (e.g., for compression). The NTT representation also facilitates modular multiplication: multiplying two polynomials requires just n = 256 modular multiplications of their NTT coefficients.

For ML-DSA, the same NTT structure applies with q = 8380417 and n = 256, where q ≡ 1 (mod 512) ensures the required roots of unity exist.

### Montgomery and Barrett Reduction

Efficient NTT implementation requires fast modular reduction. Two key techniques:

**Barrett reduction:** Precomputes an approximation of 1/q to avoid explicit division. Computes a mod q using only multiplications and shifts, suitable when q is fixed.

**Montgomery reduction:** Represents elements in Montgomery form aR mod q (for a power of 2 R > q). Modular multiplication in Montgomery form avoids division by q, replacing it with division by R (a simple bit shift). This is the preferred approach in ML-KEM and ML-DSA implementations.

## A.8 Hash Functions and Random Oracles

### Cryptographic Hash Function Properties

A cryptographic hash function H: {0,1}* → {0,1}^n maps arbitrary-length inputs to fixed-length outputs (the hash or digest). Three fundamental security properties are required:

**Preimage resistance (one-wayness):** Given a hash value y, it should be computationally infeasible to find any x such that H(x) = y. Formally: for y ← H(U), any PPT adversary A has Pr[H(A(y)) = y] ≤ negl(λ).

**Second preimage resistance:** Given x, it should be computationally infeasible to find x' ≠ x with H(x) = H(x'). This is generally weaker than collision resistance.

**Collision resistance:** It should be computationally infeasible to find any pair x ≠ x' with H(x) = H(x'). By the birthday paradox, this requires output length n ≥ 2λ for λ-bit security (e.g., 256-bit output for 128-bit collision resistance).

Additional properties used in PQC constructions:

**Pseudorandomness (PRF-like behavior):** For a keyed hash H_k, the output should be indistinguishable from random to anyone not knowing k. HMAC and KMAC provide this property.

**Extractable/programmable:** In security proofs, we sometimes need the hash to be "extractable" (the prover must "know" the preimage) or "programmable" (the simulator can set hash outputs).

### Hash Functions in PQC Standards

ML-KEM and ML-DSA use SHAKE (SHA-3 based extendable output functions) extensively:
- **SHAKE-128/256:** XOF (extendable output function) for generating pseudorandom bytes
- **SHA3-256/512:** For deriving keys and commitments
- **H, G, PRF, XOF:** Abstract functions in the specification instantiated with SHA-3 family

SLH-DSA relies entirely on hash functions for security: its only assumption is the security of the underlying hash (SHA-256 or SHAKE-256, depending on the parameter set).

### Random Oracle Model (ROM)

The Random Oracle (RO) is an idealized hash function modeled as a truly random function: for each new input x, the output H(x) is chosen uniformly at random from the output space, and repeated queries to the same input return the same output. The random oracle is accessible to all parties (including the adversary) only through oracle queries.

Security proofs in the ROM proceed by:
1. Replacing the hash function with a random oracle in the security game
2. Showing that any successful adversary must make "useful" queries to the oracle
3. Extracting a solution to the underlying hard problem from the adversary's queries

The Fujisaki-Okamoto (FO) transform, used to construct ML-KEM from a CPA-secure encryption scheme, has its security proof in the ROM. The transform uses the random oracle to bind the encryption randomness to the message, enabling implicit rejection of invalid ciphertexts.

Limitations of the ROM: there exist (contrived) schemes that are provably secure in the ROM but insecure for any concrete hash function instantiation. Despite this theoretical concern, ROM proofs are widely accepted in practice and provide meaningful security assurance.

### Quantum Random Oracle Model (QROM)

In the QROM, the adversary can query the random oracle on quantum superpositions of inputs:

```
|x⟩|y⟩ → |x⟩|y ⊕ H(x)⟩
```

This models a quantum adversary's ability to evaluate any efficiently computable function (including hash functions) on superpositions. The QROM is the appropriate model for post-quantum security.

Key differences from classical ROM:
- **No recording of queries:** The simulator cannot observe individual queries without disturbing the quantum state (measurement collapses superposition).
- **No lazy sampling:** The oracle must be defined on all inputs simultaneously (cannot be programmed on-the-fly without detection).
- **Stronger techniques needed:** Proofs require quantum-specific tools like the "compressed oracle" technique (Zhandry), "measure-and-reprogram" (Don et al.), or "one-way-to-hiding" (Unruh).

The FO transform has been proven secure in the QROM, but the proof is more complex and sometimes yields slightly looser security bounds than the classical ROM proof. NIST standards require QROM security.

### Fiat-Shamir Transform in the (Q)ROM

The Fiat-Shamir transform converts a public-coin interactive proof (sigma protocol) into a non-interactive signature scheme by replacing the verifier's challenge with a hash of the commitment:

```
Challenge c = H(message ‖ commitment)
```

ML-DSA uses this paradigm: the signer generates a commitment w, computes the challenge c = H(μ ‖ w) where μ encodes the message and public key, then computes the response. Classical ROM security of Fiat-Shamir follows from the forking lemma. QROM security requires more sophisticated techniques but has been established.

## A.9 Complexity Theory Basics

### Deterministic Complexity Classes

**P (Polynomial Time):** The class of decision problems solvable by a deterministic Turing machine in time polynomial in the input length. Problems in P are considered "efficiently solvable." Examples: sorting, shortest paths, linear programming, GCD computation.

**NP (Nondeterministic Polynomial Time):** The class of decision problems for which "yes" instances have polynomial-length certificates verifiable in polynomial time. Equivalently, problems solvable in polynomial time on a nondeterministic Turing machine.

- Every problem in P is also in NP (the certificate can be ignored)
- P ≠ NP is the most important open problem in theoretical computer science
- NP-hard: at least as hard as any NP problem (via polynomial reductions)
- NP-complete: in NP and NP-hard (e.g., SAT, 3-coloring, subset sum)

**coNP:** The class of problems whose complements are in NP. A problem is in coNP if "no" instances have efficiently verifiable certificates.

### Probabilistic Complexity Classes

**BPP (Bounded-Error Probabilistic Polynomial Time):** Decision problems solvable by a probabilistic polynomial-time machine with error probability at most 1/3 (on both yes and no instances). The error can be reduced to 2^{-k} by repeating k times and taking majority vote. BPP is the classical analog of efficient computation with randomness.

**RP (Randomized Polynomial Time):** Yes instances accepted with probability ≥ 1/2; no instances always rejected. One-sided error.

**ZPP (Zero-Error Probabilistic Polynomial Time):** Always gives correct answer but runtime is polynomial only in expectation. ZPP = RP ∩ coRP.

It is widely believed (but unproven) that P = BPP, meaning randomness does not help for decision problems. Under standard derandomization assumptions, this holds.

### Quantum Complexity Classes

**BQP (Bounded-Error Quantum Polynomial Time):** Decision problems solvable by a polynomial-time quantum algorithm with error probability at most 1/3. This is the quantum analog of BPP and represents what quantum computers can efficiently solve.

Known relationships: P ⊆ BPP ⊆ BQP. It is believed (but unproven) that BPP ⊊ BQP, meaning quantum computers provide genuine advantage. Evidence comes from Shor's algorithm (factoring is in BQP but not known to be in BPP) and quantum simulation.

**QMA (Quantum Merlin-Arthur):** The quantum analog of NP — problems verifiable by a polynomial-time quantum machine given a quantum proof (witness state). QMA contains NP.

### The Polynomial Hierarchy and PQC

The computational problems underlying PQC are chosen to be hard for BQP:

- **Lattice problems (LWE, SIS):** Not known to be in BQP. Best quantum algorithms provide at most polynomial speedup over classical algorithms.
- **Syndrome decoding:** NP-hard in general; random instances are assumed hard even quantumly.
- **Multivariate quadratic systems:** NP-hard; best quantum algorithms offer limited advantage.
- **Hash function inversion:** Grover's algorithm provides only quadratic speedup (√N vs N for search in space of size N).

The only structured problems broken by quantum computers are those with hidden algebraic structure exploitable by the quantum Fourier transform: integer factoring, discrete logarithms in abelian groups, and period-finding problems.

### Reductions and Security Proofs

A reduction from problem A to problem B is an efficient algorithm that solves A using an oracle for B. If such a reduction exists and A is hard, then B must also be hard (contrapositive: if B were easy, we could solve A efficiently).

**Karp (many-one) reductions:** Map instances of A to instances of B such that x ∈ A ⟺ f(x) ∈ B. Used for NP-completeness.

**Cook (Turing) reductions:** Algorithm for A makes adaptive queries to a B-oracle. More general than Karp reductions.

**Security reductions in cryptography:** Show that breaking a cryptographic scheme implies solving a hard problem. The reduction is an algorithm (often called a simulator) that:
1. Receives a hard problem instance
2. Constructs a cryptographic scheme instance (simulating the honest environment)
3. Runs the adversary as a subroutine
4. Extracts a solution to the hard problem from the adversary's output

**Tight reductions:** A reduction is tight if the security loss (ratio between the hardness assumption and the scheme's security) is small (ideally 1 or a small constant). Non-tight reductions require larger parameters to compensate for the security loss. ML-KEM has a relatively tight reduction from Module-LWE; ML-DSA has a somewhat less tight reduction involving a loss proportional to the number of signing queries.

**Average-case to worst-case reductions:** A distinctive feature of lattice-based cryptography: Regev's original LWE reduction shows that solving random LWE instances is at least as hard as solving worst-case lattice problems (approximate GapSVP and SIVP). This provides stronger theoretical guarantees than most cryptographic assumptions, which are average-case.

### Negligible Functions and Asymptotic Security

A function ν: N → [0,1] is negligible if it vanishes faster than any inverse polynomial:

```
∀c > 0, ∃N₀: ∀n > N₀, ν(n) < n^{-c}
```

Examples of negligible functions: 2^{-n}, 2^{-√n}, n^{-log n}, e^{-n^{1/3}}.
Not negligible: 1/n^{100}, 1/(n · log n), any function ≥ 1/p(n) for some fixed polynomial p.

In cryptographic definitions, security means that no PPT adversary succeeds with more than negligible probability. Concretely, for security parameter λ = 128:
- Negligible means probability < 2^{-128}
- An adversary running in time T with advantage ε achieves "bit security" log₂(T/ε)
- Parameters are chosen so that the best known attack achieves bit security ≥ λ

The asymptotic framework provides clean definitions and proof techniques, while concrete security analysis ensures practical parameter choices provide the claimed security level.

### Quantum Algorithms Relevant to PQC

**Shor's algorithm:** Factors n-bit integers in O(n³) quantum gates using O(n) qubits (simplified). Relies on quantum Fourier transform to find periods. Breaks RSA, DH, ECDSA/ECDH, and any system based on factoring or discrete logarithms in abelian groups.

**Grover's algorithm:** Searches an unstructured space of N elements in O(√N) queries (versus O(N) classically). For symmetric crypto: effectively halves key lengths (AES-128 → 64-bit quantum security, AES-256 → 128-bit quantum security). For hash functions: reduces collision resistance from 2^{n/2} to 2^{n/3} (via BHT algorithm, though practical impact is debated).

**Quantum walks and amplitude amplification:** Generalize Grover's search; can provide sub-quadratic speedups for certain graph problems. Applied to lattice sieving, they might reduce exponents slightly (e.g., from 2^{0.292n} to 2^{0.265n}) but do not fundamentally change the exponential hardness.

## A.10 Additional Topics in Algebraic Structures

### Ideal Lattices

An ideal lattice is a lattice that corresponds to an ideal in a number ring. Specifically, consider the ring of integers O_K of a number field K = Q[x]/(f(x)). An ideal I ⊂ O_K, when embedded into R^n via the canonical embedding σ: K → R^n (or C^n), yields a lattice σ(I) ⊂ R^n.

For the ring R = Z[x]/(x^n + 1) used in PQC (with n a power of 2), ideals in R correspond to lattices with additional algebraic structure. Specifically, if a = (a₀, a₁, ..., a_{n-1}) represents an element of R, then multiplication by a corresponds to a matrix-vector product with a special anti-circulant matrix:

```
       [ a₀   -a_{n-1}  -a_{n-2}  ...  -a₁  ]
       [ a₁    a₀       -a_{n-1}  ...  -a₂  ]
M_a =  [ a₂    a₁        a₀      ...  -a₃  ]
       [ ...                                  ]
       [ a_{n-1} a_{n-2}  a_{n-3}  ...   a₀  ]
```

This algebraic structure means that ring-LWE and module-LWE problems operate on structured lattices rather than arbitrary ones. The benefit is significantly smaller key sizes (a single ring element specifies an entire lattice basis). The risk is that structure might enable faster attacks — though decades of cryptanalysis have not found practical exploits of this structure for the parameters used in standards.

### Module Structure

ML-KEM and ML-DSA use module lattices, which generalize both unstructured lattices and ring lattices. A module over R_q = Z_q[x]/(x^n + 1) is a free R_q-module of rank k, analogous to a vector space but over a ring instead of a field.

The Module-LWE problem with rank k and ring dimension n provides:
- k = 1: Equivalent to Ring-LWE (most structured, smallest parameters)
- k = n: Equivalent to standard LWE (least structured, largest parameters)
- Intermediate k: Balances structure and security confidence

ML-KEM-768 uses k = 3, n = 256, giving a total dimension of 768 with module structure. This provides a middle ground where keys are compact (leveraging ring structure) but security does not depend on ring-specific vulnerabilities (due to the module dimension).

### Cyclotomic Polynomials

The n-th cyclotomic polynomial Φ_n(x) is the minimal polynomial of primitive n-th roots of unity over Q:

```
Φ_n(x) = Π_{gcd(k,n)=1, 1≤k≤n} (x - e^{2πik/n})
```

Key properties:
- deg(Φ_n) = φ(n) (Euler's totient)
- x^n - 1 = Π_{d|n} Φ_d(x) (factorization into cyclotomic polynomials)
- For n = 2^k: Φ_n(x) = x^{n/2} + 1

The ring Z[x]/(Φ_n(x)) is the ring of integers of the cyclotomic field Q(ζ_n). For PQC, we primarily use Φ_{2n}(x) = x^n + 1 with n a power of 2, which yields the cleanest algebraic properties and NTT-friendliness.

### Tensor Products and Module Operations

For understanding the module structure in ML-KEM/ML-DSA, consider:
- A public matrix A ∈ R_q^{k×k} (each entry is a polynomial in R_q)
- A secret vector s ∈ R_q^k (k polynomials)  
- The product As ∈ R_q^k involves k² ring multiplications

The tensor product R_q^k ⊗ R_q^k provides the correct framework for understanding the public key structure. The matrix A acts as a linear map on the module R_q^k, and the LWE instance (A, b = As + e) lives in R_q^{k×k} × R_q^k.

## A.11 Further Mathematical Reading

For deeper study of the mathematical foundations:

- **Lattice theory:** Micciancio & Goldwasser, "Complexity of Lattice Problems: A Cryptographic Perspective" provides the definitive treatment of computational lattice problems. Peikert's survey "A Decade of Lattice Cryptography" covers modern constructions.
- **Algebraic number theory:** Neukirch, "Algebraic Number Theory" covers the number field theory relevant to ideal lattice constructions and ring-LWE.
- **Elliptic curves:** Silverman, "The Arithmetic of Elliptic Curves" is the standard graduate reference. Washington's "Elliptic Curves: Number Theory and Cryptography" provides a more applied treatment.
- **Coding theory:** MacWilliams & Sloane, "The Theory of Error-Correcting Codes" remains the classic reference. Huffman & Pless provide a modern treatment.
- **Computational complexity:** Arora & Barak, "Computational Complexity: A Modern Approach" covers all the complexity theory needed for cryptographic security analysis.
- **Quantum computing:** Nielsen & Chuang, "Quantum Computation and Quantum Information" is comprehensive. For quantum algorithms specifically, see Childs' lecture notes.
- **Probability theory:** Mitzenmacher & Upfal, "Probability and Computing" covers the probabilistic techniques used in cryptographic proofs.
- **Abstract algebra:** Dummit & Foote, "Abstract Algebra" provides thorough coverage of groups, rings, and fields at the level needed for understanding PQC constructions.
