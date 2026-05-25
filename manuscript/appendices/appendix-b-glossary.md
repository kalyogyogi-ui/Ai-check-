> **Author's note:** Appendix B-GLOSSARY is reference material—use it beside the narrative chapters, not instead of them.

# Appendix B: Glossary of Terms

This glossary provides comprehensive definitions of key terms used throughout this text. Terms are organized alphabetically, with cross-references indicated in italics. Where relevant, the relationship to specific PQC standards or algorithms is noted.

## A

**ACVP (Automated Cryptographic Validation Protocol):** A protocol developed by NIST for automated testing and validation of cryptographic implementations. ACVP enables continuous validation of cryptographic modules against algorithm specifications, replacing manual testing processes. It supports ML-KEM, ML-DSA, and SLH-DSA validation.

**AES (Advanced Encryption Standard):** The NIST-standardized symmetric block cipher (FIPS 197), operating on 128-bit blocks with key sizes of 128, 192, or 256 bits. AES-256 provides approximately 128-bit security against quantum adversaries due to *Grover's algorithm* providing at most a quadratic speedup. AES is used within PQC standards as a building block for key derivation and as an alternative to SHAKE for certain internal functions.

**Algorithm agility:** See *Cryptographic agility*.

**Approximate SVP (γ-SVP):** The problem of finding a lattice vector within a factor γ of the shortest vector length λ₁. For polynomial γ, this problem is known to be NP-hard. For exponential γ, efficient algorithms exist (LLL achieves γ ≈ 2^{n/2}). The security of lattice-based PQC depends on the hardness of γ-SVP for sub-exponential approximation factors.

**Authentication:** The process of verifying the identity of a communicating party or the integrity and origin of data. PQC provides quantum-resistant authentication through digital signature schemes (*ML-DSA*, *SLH-DSA*, *FN-DSA*) and through authenticated key exchange protocols.

**Avalanche effect:** A desirable property of cryptographic functions where a small change in input produces a large, unpredictable change in output. Hash functions and block ciphers exhibit this property, which is essential for the security of hash-based signature schemes like *SLH-DSA*.

## B

**BDD (Bounded Distance Decoding):** A lattice problem where given a target point within a promised distance of a lattice point, the goal is to find the nearest lattice point. The *LWE* problem can be viewed as a BDD instance on a q-ary lattice. BDD is easier than general *CVP* but still believed to be hard for lattice parameters used in cryptography.

**BKZ (Block Korkine-Zolotarev):** A lattice reduction algorithm parameterized by block size β that iteratively applies SVP solvers to projected sublattices of dimension β. BKZ-β achieves approximation factor approximately 2^{n/β} in time dominated by the SVP oracle calls in dimension β. The BKZ cost model is the primary tool for estimating the concrete security of lattice-based cryptographic parameters. As β increases, the reduction quality improves but runtime increases exponentially.

**Block cipher:** A symmetric encryption primitive that encrypts fixed-length blocks of plaintext under a key. *AES* is the standard block cipher. Block ciphers are not directly affected by quantum computers beyond the Grover speedup, but their modes of operation must be analyzed for quantum security.

**BPP (Bounded-Error Probabilistic Polynomial Time):** The class of decision problems solvable by a probabilistic polynomial-time Turing machine with error probability at most 1/3 on all inputs. BPP represents efficient classical randomized computation. It is widely conjectured that P = BPP.

**BQP (Bounded-Error Quantum Polynomial Time):** The class of decision problems efficiently solvable by a quantum computer with error probability at most 1/3. BQP contains factoring and discrete logarithm problems (via *Shor's algorithm*) but is believed not to contain NP-complete problems. PQC problems are chosen to lie outside BQP.

## C

**CBOM (Cryptographic Bill of Materials):** A structured, machine-readable inventory of all cryptographic algorithms, protocols, keys, and certificates used within a system, application, or organization. CBOMs enable systematic discovery of quantum-vulnerable cryptography and planning for PQC migration. The CycloneDX standard provides a format for CBOM generation.

**CBD (Centered Binomial Distribution):** A discrete probability distribution parameterized by η, producing values in {-η, ..., η} by computing the difference of two sums of η uniform random bits. CBD_η has variance η/2 and is used in *ML-KEM* and *ML-DSA* for sampling error vectors. The CBD is preferred over discrete Gaussians because it can be sampled in constant time without rejection, preventing timing side channels.

**CCA (Chosen Ciphertext Attack):** An attack model where the adversary can submit ciphertexts to a decryption oracle and observe the results. IND-CCA2 (adaptive chosen ciphertext) security is the standard security notion for *KEMs* and public-key encryption schemes. The *Fujisaki-Okamoto transform* elevates CPA-secure schemes to CCA-secure KEMs.

**CFRG (Crypto Forum Research Group):** An IRTF research group that evaluates and recommends cryptographic algorithms for IETF protocols. CFRG plays a key role in specifying how PQC algorithms are integrated into Internet protocols like *TLS* and *SSH*.

**CNSA (Commercial National Security Algorithm Suite):** The NSA's set of recommended cryptographic algorithms for protecting classified and sensitive information. CNSA 2.0, published in 2022, specifies a transition timeline to PQC: ML-KEM by 2025, ML-DSA by 2025, and exclusive use of PQC by 2033-2035.

**Code-based cryptography:** A family of PQC schemes whose security is based on the difficulty of decoding random linear error-correcting codes. Includes the *McEliece* cryptosystem (1978), *HQC*, *BIKE*, and related schemes. The general decoding problem is NP-hard, and the best algorithms (*ISD* variants) require exponential time.

**Commitment scheme:** A two-phase cryptographic protocol where a sender first commits to a value (hiding it) and later reveals it (binding the sender to the committed value). Commitments appear in sigma protocols underlying *ML-DSA* and in the Fiat-Shamir transform.

**Composite algorithm:** A cryptographic construction that combines two or more algorithms (typically one classical and one PQC) into a single combined algorithm with unified key and signature/ciphertext formats. Defined in IETF drafts for composite ML-DSA and composite ML-KEM, enabling hybrid security with a single OID and certificate.

**CPA (Chosen Plaintext Attack):** An attack model where the adversary can query an encryption oracle to obtain ciphertexts of chosen plaintexts. IND-CPA security means ciphertexts reveal no information about plaintexts beyond their length. CPA security is the base notion that the *FO transform* elevates to *CCA* security.

**CRQC (Cryptographically Relevant Quantum Computer):** A quantum computer with sufficient logical qubits and gate fidelity to execute *Shor's algorithm* against production cryptographic keys (e.g., breaking RSA-2048 or ECDSA-256). Current estimates suggest a CRQC may emerge within 10-20 years, motivating urgent PQC migration.

**Cryptanalysis:** The study of methods for breaking cryptographic schemes, recovering keys, or forging signatures/ciphertexts without knowing the secret key. For PQC, relevant cryptanalysis includes lattice reduction attacks, algebraic attacks on multivariate schemes, and information set decoding for code-based systems.

**Cryptographic agility:** The architectural property of a system that enables replacement of cryptographic algorithms and parameters without requiring fundamental redesign of protocols, data formats, or infrastructure. Cryptographic agility is essential for PQC migration because it allows incremental deployment and rapid response to algorithm compromises.

**CSIDH (Commutative Supersingular Isogeny Diffie-Hellman):** A key exchange protocol based on the action of an ideal class group on a set of supersingular elliptic curves defined over F_p. Unlike SIDH/SIKE, CSIDH does not reveal torsion point images, making it resistant to the *Castryck-Decru attack*. However, its security relies on assumptions about quantum resistance of class group computation.

**CVP (Closest Vector Problem):** Given a lattice L and a target point t, find the lattice vector closest to t in Euclidean distance. CVP is at least as hard as *SVP* (via Kannan's reduction). The *LWE* problem can be reformulated as a CVP instance.

**Cyclotomic polynomial:** The minimal polynomial Φ_n(x) of primitive n-th roots of unity over the rationals. For n = 2^k, Φ_n(x) = x^{n/2} + 1, which defines the polynomial ring used in *ML-KEM* and *ML-DSA*.

## D

**Decapsulation:** The *KEM* operation performed by the recipient, taking a ciphertext and secret key as input and producing a shared secret. In ML-KEM, decapsulation involves polynomial operations, decompression, comparison with re-encapsulation (implicit rejection), and key derivation.

**Decryption failure:** An event where a correctly formed ciphertext decrypts to an incorrect plaintext due to noise accumulation exceeding the scheme's error-correction capacity. ML-KEM parameters are chosen so that decryption failure probability is less than 2^{-139}, making it negligible in practice. Non-negligible failure rates can enable chosen-ciphertext attacks.

**Digital signature:** A cryptographic mechanism that provides authentication, integrity, and non-repudiation. A signature scheme consists of key generation, signing, and verification algorithms. PQC signature standards include *ML-DSA*, *SLH-DSA*, and *FN-DSA*.

**DRBG (Deterministic Random Bit Generator):** A cryptographic algorithm that produces a sequence of pseudorandom bits from a seed value. Also called a cryptographic PRNG. DRBGs based on AES-CTR or HMAC are used within PQC implementations for deterministic key generation from a seed.

**DSA (Digital Signature Algorithm):** A classical digital signature standard based on the discrete logarithm problem. Broken by *Shor's algorithm*. Being replaced by *ML-DSA* and *SLH-DSA* in the post-quantum era.

## E

**ECC (Elliptic Curve Cryptography):** A family of public-key cryptographic algorithms based on the algebraic structure of elliptic curves over finite fields. Provides equivalent security to RSA with shorter keys. All standard ECC schemes (ECDSA, ECDH, EdDSA) are broken by *Shor's algorithm* applied to the elliptic curve discrete logarithm problem.

**Encapsulation:** The *KEM* operation performed by the sender, taking a public key as input and producing both a ciphertext and a shared secret. In ML-KEM, encapsulation involves sampling a random message, polynomial operations, compression, and key derivation.

**Endomorphism ring:** The ring End(E) of algebraic group homomorphisms from an elliptic curve E to itself, under addition and composition. For ordinary curves, End(E) is an order in an imaginary quadratic field. For supersingular curves, End(E) is a maximal order in a quaternion algebra. Computing the endomorphism ring is believed to be hard and forms the security basis for some isogeny-based schemes.

**EUF-CMA (Existential Unforgeability under Chosen Message Attack):** The standard security definition for digital signature schemes. An adversary who can obtain signatures on adaptively chosen messages should be unable to produce a valid signature on any new message. *ML-DSA*, *SLH-DSA*, and *FN-DSA* all target EUF-CMA security.

## F

**Fault attack:** A physical attack that induces computational errors (via voltage glitching, clock manipulation, laser injection, or electromagnetic pulses) to extract secret information or bypass security checks. PQC implementations must incorporate countermeasures such as redundant computation, error detection codes, and verification after signing.

**FIPS (Federal Information Processing Standard):** US government standards for computing and information processing, issued by NIST. PQC standards: FIPS 203 (*ML-KEM*), FIPS 204 (*ML-DSA*), FIPS 205 (*SLH-DSA*). Compliance with FIPS is mandatory for US federal systems and widely adopted in industry.

**FN-DSA (Fast-Fourier Lattice-based Compact Signatures over NTRU):** A lattice-based digital signature scheme formerly known as FALCON, expected to be standardized as FIPS 206. FN-DSA uses NTRU lattices and Gaussian sampling via a "hash-and-sign" paradigm with a trapdoor basis. It offers the smallest combined public key and signature sizes among PQC signature schemes but requires careful constant-time implementation of floating-point Gaussian sampling.

**FO Transform (Fujisaki-Okamoto Transform):** A generic cryptographic construction that converts a weakly secure (IND-CPA) public-key encryption scheme into a strongly secure (IND-CCA2) *KEM*. The transform uses a hash function to derive encryption randomness from the message, enabling implicit rejection of invalid ciphertexts. ML-KEM uses a variant of the FO transform with security proven in the *QROM*.

**FORS (Forest of Random Subsets):** A few-time signature scheme used as the bottom layer in *SLH-DSA*. FORS signs a message by revealing secret values at positions determined by the message hash. Security allows a bounded number of signatures (determined by the hypertree height) before the scheme is compromised.

**FHE (Fully Homomorphic Encryption):** An encryption scheme that allows arbitrary computations on ciphertexts, producing encrypted results that decrypt to the computation applied to the plaintexts. All practical FHE schemes (BGV, BFV, CKKS, TFHE) are lattice-based and benefit from the same hardness assumptions as *LWE*-based PQC.

## G

**Galois field:** See *Finite field*.

**GapSVP (Gap Shortest Vector Problem):** A promise problem version of SVP: given a lattice and a threshold d, determine whether λ₁ ≤ d or λ₁ > γ·d (promised that one case holds). GapSVP is the problem that appears in worst-case to average-case reductions for *LWE*.

**Gaussian elimination:** A systematic algorithm for solving systems of linear equations, computing matrix rank, determinants, and null spaces. Over finite fields, it runs in O(n³) operations without numerical stability concerns. Used in *ISD* attacks against code-based cryptography.

**Goppa code:** A class of algebraic error-correcting codes defined using rational functions over finite fields. Binary Goppa codes are used in the Classic McEliece cryptosystem. Their algebraic structure enables efficient decoding (given the secret structure) while random instances resist all known decoding attacks.

**Grover's algorithm:** A quantum algorithm that searches an unstructured database of N items in O(√N) quantum queries, providing a quadratic speedup over classical exhaustive search. Implications for cryptography: effectively halves the security level of symmetric ciphers and hash functions. AES-256 provides 128-bit quantum security; SHA-256 provides approximately 128 bits of quantum preimage resistance.

## H

**Harvest Now, Decrypt Later (HNDL):** A threat model in which adversaries collect and store encrypted communications today with the intention of decrypting them in the future when a *CRQC* becomes available. HNDL motivates immediate deployment of PQC for *key exchange* and encryption, even before quantum computers exist, to protect data with long-term confidentiality requirements.

**Hash-based signatures:** A family of digital signature schemes whose security relies solely on the properties of cryptographic hash functions (preimage resistance, collision resistance, or second preimage resistance). Includes stateful schemes (*LMS*, *XMSS*) and the stateless scheme *SLH-DSA*. Hash-based signatures are considered the most conservative PQC signatures because their security assumption is minimal.

**HNDL:** See *Harvest Now, Decrypt Later*.

**HQC (Hamming Quasi-Cyclic):** A code-based *KEM* selected by NIST for additional standardization (expected as FIPS 207). HQC is based on the difficulty of decoding random quasi-cyclic codes and uses the Hamming metric. It provides an alternative to lattice-based KEMs with different security assumptions, offering diversification in case lattice problems are found vulnerable.

**HSM (Hardware Security Module):** A dedicated, tamper-resistant hardware device for secure cryptographic key management, key generation, and cryptographic operations. HSM vendors are adding PQC algorithm support; the transition requires firmware updates and potentially new hardware to accommodate larger PQC key sizes and different computational requirements.

**Hybrid key exchange:** A key exchange protocol that combines a classical algorithm (e.g., X25519 or ECDH) with a PQC algorithm (e.g., ML-KEM) so that the resulting shared secret is secure if either component remains unbroken. Typically implemented by concatenating or KDF-combining both shared secrets. Standardized for TLS 1.3 in IETF drafts.

**Hybrid signature:** A combined digital signature using both a classical and a PQC algorithm, requiring both signatures to verify. Can be implemented as composite signatures (single OID, combined format) or as dual signatures (two separate signatures). Provides backward compatibility and defense-in-depth.

**Hypertree:** The multi-layer Merkle tree structure used in *SLH-DSA*. The hypertree consists of d layers of Merkle trees, where each leaf of a tree at one layer certifies the root of a tree at the layer below. The bottom layer signs the *FORS* public key. This structure reduces signature size by amortizing the authentication path cost across multiple tree layers.

## I

**IND-CCA2 (Indistinguishability under Adaptive Chosen Ciphertext Attack):** The strongest standard security notion for encryption and KEMs. An adversary with access to a decryption oracle (except on the challenge ciphertext) cannot distinguish encryptions of two chosen plaintexts with non-negligible advantage. All PQC KEMs (*ML-KEM*, *HQC*) target IND-CCA2 security.

**IND-CPA (Indistinguishability under Chosen Plaintext Attack):** A security notion where an adversary with access only to an encryption oracle cannot distinguish encryptions of chosen plaintexts. Weaker than *IND-CCA2*. The base encryption scheme in ML-KEM achieves IND-CPA security, which the *FO transform* elevates to IND-CCA2.

**Implicit rejection:** A design choice in *ML-KEM* where decapsulation of an invalid ciphertext produces a pseudorandom key (derived from a secret hash of the ciphertext) rather than an error message. This prevents chosen-ciphertext attacks that exploit knowledge of decryption failure and ensures constant-time behavior.

**Information Set Decoding (ISD):** A family of algorithms for decoding random linear codes, representing the best known attacks against code-based cryptographic schemes. ISD works by guessing information sets (positions without errors), with optimizations including partial Gaussian elimination, birthday decoding (Stern/Dumer), nearest-neighbor techniques (MMT, BJMM), and representation techniques. The exponential complexity of ISD provides the security foundation for *McEliece*, *HQC*, and *BIKE*.

**Isogeny:** A non-constant rational map between elliptic curves that is also a group homomorphism. Isogenies are determined (up to isomorphism of the target curve) by their kernel subgroup. They preserve the group structure while mapping between curves with potentially different equations. Isogenies form the basis of *CSIDH* and *SQISign*.

## K

**KAT (Known Answer Test):** A test vector consisting of specified inputs and the corresponding correct outputs for a cryptographic algorithm. NIST provides official KAT files for FIPS 203, 204, and 205 to validate implementation correctness. KAT testing is a requirement for FIPS validation (CMVP).

**KDF (Key Derivation Function):** A cryptographic function that derives one or more cryptographic keys from a shared secret, password, or other key material. KDFs incorporate domain separation, context binding, and output expansion. HKDF and KMAC are commonly used in PQC protocol integration.

**KEM (Key Encapsulation Mechanism):** A public-key cryptographic primitive consisting of three algorithms: KeyGen (generate key pair), Encapsulate (produce ciphertext and shared secret from public key), and Decapsulate (recover shared secret from ciphertext and secret key). KEMs replaced public-key encryption as the standard primitive for key establishment because they provide cleaner security definitions and more natural composition with symmetric encryption.

**Key pair:** A matched public key and private (secret) key generated by a key generation algorithm. In PQC, key pairs are typically much larger than classical counterparts: ML-KEM-768 has 1,184-byte public keys (vs. 32 bytes for X25519), and ML-DSA-65 has 1,952-byte public keys (vs. 32 bytes for Ed25519).

## L

**Lattice:** A discrete additive subgroup of R^n, equivalently the set of all integer linear combinations of a set of linearly independent basis vectors. Lattices are the mathematical structure underlying the majority of PQC constructions (*ML-KEM*, *ML-DSA*, *FN-DSA*). Their security relies on the computational difficulty of finding short vectors or close vectors.

**Lattice reduction:** A family of algorithms that, given a "bad" lattice basis (with long, nearly parallel vectors), produce a "better" basis with shorter, more orthogonal vectors. Key algorithms include LLL (polynomial time, exponential approximation), *BKZ* (exponential time, better approximation), and lattice sieving (exponential time, near-optimal approximation).

**LLL (Lenstra-Lenstra-Lovász):** A polynomial-time lattice reduction algorithm that produces a basis whose shortest vector is within a factor of 2^{(n-1)/2} of λ₁. While insufficient to break cryptographic parameters directly, LLL serves as a subroutine in more powerful algorithms like *BKZ* and as a preprocessing step in lattice attacks.

**LMS (Leighton-Micali Signature):** A stateful hash-based signature scheme standardized in RFC 8554 and NIST SP 800-208. LMS uses a Merkle tree over one-time signatures and requires careful state management to prevent key reuse. Suitable for firmware signing and other applications where state management is feasible.

**LWE (Learning With Errors):** A computational problem: given a matrix A ∈ Z_q^{m×n} and a vector b = As + e (mod q) where s is a secret vector and e is a "short" error vector, recover s (search-LWE) or distinguish (A, b) from uniform (decision-LWE). LWE is the foundational hardness assumption for *ML-KEM* and *ML-DSA*. It enjoys a worst-case to average-case reduction from lattice problems (GapSVP, SIVP).

## M

**McEliece cryptosystem:** The first code-based public-key encryption scheme, proposed by Robert McEliece in 1978. The public key is a disguised generator matrix for a Goppa code; encryption adds random errors. Classic McEliece is a NIST PQC candidate with very large public keys (~261 KB for 128-bit security) but fast operations and strong security confidence from 45+ years of cryptanalysis.

**Merkle tree:** A binary tree data structure where each leaf contains a hash of a data block and each internal node contains the hash of its two children. The root hash authenticates the entire tree. Merkle trees enable efficient membership proofs (authentication paths of O(log n) hashes). They are fundamental to hash-based signature schemes (*SLH-DSA*, *XMSS*, *LMS*).

**ML-DSA (Module-Lattice Digital Signature Algorithm):** The primary PQC digital signature standard (FIPS 204), based on the Module-LWE and Module-SIS problems. Formerly known as CRYSTALS-Dilithium. Uses the Fiat-Shamir with Aborts paradigm: signing involves rejection sampling to prevent secret key leakage. Available in three security levels: ML-DSA-44, ML-DSA-65, and ML-DSA-87.

**ML-KEM (Module-Lattice Key Encapsulation Mechanism):** The primary PQC key encapsulation standard (FIPS 203), based on the Module-LWE problem. Formerly known as CRYSTALS-Kyber. Uses the *FO transform* to achieve IND-CCA2 security from an IND-CPA-secure base scheme. Available in three security levels: ML-KEM-512, ML-KEM-768, and ML-KEM-1024.

**Module-LWE:** A variant of *LWE* where the matrix A has entries in a polynomial ring R_q = Z_q[x]/(x^n + 1) rather than Z_q. Module-LWE with rank k and ring dimension n interpolates between Ring-LWE (k=1) and standard LWE (k=n). This construction provides compact key sizes through ring structure while maintaining security confidence through the module dimension.

**Module-SIS (Module Short Integer Solution):** The module variant of *SIS*: given A ∈ R_q^{k×ℓ}, find a short vector x ∈ R_q^ℓ with Ax = 0 mod q. Module-SIS underlies the security of *ML-DSA* signatures.

**Mosca's theorem (inequality):** A risk assessment framework: if the time to migrate systems (x) plus the required secrecy duration of data (y) exceeds the time until a *CRQC* arrives (z), then migration is already overdue: if x + y > z, act now. This motivates the urgency of PQC deployment for long-lived secrets.

**MQ (Multivariate Quadratic) problem:** The problem of solving a system of m quadratic polynomial equations in n variables over a finite field F_q. The MQ problem is NP-hard in general and forms the security basis for multivariate PQC schemes like *UOV* and the broken Rainbow scheme.

**Multivariate cryptography:** A family of PQC schemes based on the difficulty of solving systems of multivariate polynomial equations over finite fields. The public key is a set of quadratic (or higher degree) polynomials; the trapdoor provides a way to invert the system efficiently. *UOV* is the leading multivariate signature scheme.

## N

**Negligible function:** A function ν(n) that decreases faster than any inverse polynomial: for every constant c > 0, there exists N such that ν(n) < n^{-c} for all n > N. Cryptographic security requires that attack success probability is negligible in the security parameter. Concretely, 2^{-128} is negligible for any practical security parameter.

**NIST (National Institute of Standards and Technology):** The US federal agency responsible for developing cryptographic standards. NIST conducted the PQC standardization process from 2016 to 2024, resulting in FIPS 203, 204, and 205, with additional algorithms (FN-DSA, HQC) under continued standardization.

**NTT (Number Theoretic Transform):** The finite-field analog of the Fast Fourier Transform, enabling polynomial multiplication in O(n log n) operations. The NTT maps polynomials to their evaluation representation, where multiplication becomes pointwise. Critical for the performance of *ML-KEM* and *ML-DSA*, where the ring Z_q[x]/(x^n+1) with q ≡ 1 (mod 2n) admits an efficient NTT decomposition.

**NTRU:** A lattice-based cryptosystem family introduced in 1996. NTRU operates in the ring Z_q[x]/(x^n - 1) or related quotient rings. While NTRU encryption was not selected by NIST (ML-KEM was preferred), *FN-DSA* uses NTRU lattices for its trapdoor construction. The NTRU assumption posits that a ratio f/g of two short ring elements is indistinguishable from random.

## O

**OID (Object Identifier):** A globally unique hierarchical identifier used in ASN.1 and X.509 to identify cryptographic algorithms, curves, and protocols. PQC algorithms have assigned OIDs for use in certificates, CMS, and other standards. Composite algorithms receive their own OIDs distinct from their component algorithms.

**One-time signature (OTS):** A signature scheme that is secure for signing exactly one message per key pair. Signing multiple messages with the same key compromises security. Lamport signatures and *WOTS+* are one-time schemes. They serve as building blocks for many-time schemes via Merkle trees.

**One-way function:** A function f that is easy to compute but hard to invert: given y = f(x), finding any x' with f(x') = y is computationally infeasible. The existence of one-way functions is the minimal assumption for much of cryptography. Hash functions are assumed to be one-way.

## P

**Parity-check matrix:** A matrix H ∈ F_q^{(n-k)×n} defining a linear code C = {c : Hc^T = 0}. The syndrome s = Hr^T of a received word r reveals the error pattern. Syndrome decoding (finding minimum-weight error given syndrome) is the hard problem underlying code-based PQC.

**PKI (Public Key Infrastructure):** The systems, policies, and procedures for managing digital certificates and public keys. PKI must be upgraded for PQC: certificates grow larger (PQC public keys and signatures are larger), chain validation becomes more expensive, and transition mechanisms (hybrid certificates, composite algorithms) must be deployed.

**PQC (Post-Quantum Cryptography):** Cryptographic algorithms designed to be secure against attacks by both classical and quantum computers, while running on conventional classical hardware. PQC is distinct from quantum cryptography (which requires quantum hardware). The main PQC families are lattice-based, code-based, hash-based, multivariate, and isogeny-based.

**PQXDH (Post-Quantum Extended Diffie-Hellman):** Signal's hybrid key agreement protocol combining the classical X3DH protocol (using X25519) with *ML-KEM*-1024 for post-quantum security. PQXDH provides forward secrecy and post-quantum protection for the initial key exchange in the Signal Protocol.

**PRF (Pseudorandom Function):** A keyed function family F_k: {0,1}^n → {0,1}^m that is computationally indistinguishable from a truly random function to any efficient adversary not knowing k. PRFs are used extensively in PQC constructions for key derivation, deterministic randomness generation, and mask computation.

## Q

**QKD (Quantum Key Distribution):** A method of generating shared secret keys using quantum mechanical properties (typically photon polarization or entanglement) that guarantees detection of eavesdropping. QKD requires dedicated quantum optical hardware and cannot traverse the classical Internet infrastructure. It complements but does not replace PQC.

**QROM (Quantum Random Oracle Model):** A security model where the adversary can evaluate the random oracle on quantum superpositions of inputs. The QROM is the appropriate model for analyzing PQC security because quantum adversaries can compute hash functions on superpositions. Security proofs in the QROM are more complex than in the classical ROM but provide stronger guarantees against quantum attacks.

**Quantum advantage (supremacy):** A demonstration that a quantum computer can perform a specific computational task faster than any classical computer. Google's Sycamore (2019) and subsequent demonstrations have shown quantum advantage for specialized sampling problems, though not yet for cryptographically relevant computations.

**Quantum Fourier Transform (QFT):** A quantum analog of the discrete Fourier transform, implemented efficiently on quantum computers in O(n²) gates for n qubits. The QFT is the key subroutine in *Shor's algorithm*, enabling efficient period-finding which breaks RSA, DH, and ECC.

**Qubit:** The fundamental unit of quantum information, analogous to a classical bit. A qubit can exist in a superposition of |0⟩ and |1⟩ states: α|0⟩ + β|1⟩ where |α|² + |β|² = 1. Current quantum computers have thousands of noisy physical qubits; a *CRQC* requires millions of physical qubits to support thousands of error-corrected logical qubits.

## R

**Random oracle:** An idealized hash function that behaves as a truly random function: each distinct input maps to a uniformly random independent output. Used as a proof technique in the *Random Oracle Model*. Real hash functions (SHA-3, SHAKE) instantiate the random oracle in practice.

**Reduction (security):** A proof technique showing that breaking a cryptographic scheme implies solving a computationally hard problem. If no efficient algorithm solves the hard problem, no efficient adversary can break the scheme. Reductions are characterized by their tightness (how much security is lost in the translation).

**Rejection sampling:** A technique where computation outputs are probabilistically discarded and recomputed if they would leak information about the secret key. *ML-DSA* uses rejection sampling during signing: candidate signatures correlated with the secret key are rejected, with the process repeating until an independent-looking signature is produced. This makes ML-DSA signing non-deterministic and variable-time (in terms of number of iterations, not per-iteration time).

**Ring-LWE:** A variant of *LWE* where the secret and error are elements of a polynomial ring R_q = Z_q[x]/(f(x)), and the "matrix" is defined by multiplication by a single ring element. Ring-LWE provides very compact parameters but concentrates security in the ring structure. *Module-LWE* generalizes Ring-LWE to vectors of ring elements, providing better security/efficiency tradeoffs.

**RSA:** A public-key cryptosystem based on the difficulty of factoring large integers, invented by Rivest, Shamir, and Adleman in 1977. RSA key exchange, encryption, and signatures are all broken by *Shor's algorithm*. RSA is being replaced by *ML-KEM* (for key exchange) and *ML-DSA* (for signatures).

## S

**SHA-3 (Secure Hash Algorithm 3):** A family of cryptographic hash functions (SHA3-224/256/384/512) and extendable output functions (SHAKE128/256) based on the Keccak sponge construction. SHA-3 functions are used throughout PQC standards for hashing, key derivation, pseudorandom generation, and domain separation.

**Shor's algorithm:** A quantum polynomial-time algorithm for integer factoring and computing discrete logarithms in any finite abelian group. Shor's algorithm breaks RSA, Diffie-Hellman, DSA, ECDSA, ECDH, and all cryptosystems based on factoring or discrete logarithms. It is the primary motivation for PQC.

**Side-channel attack:** An attack that exploits physical leakage from a cryptographic implementation rather than mathematical weaknesses. Leakage channels include timing, power consumption, electromagnetic emanation, cache behavior, and acoustic/thermal emissions. PQC implementations must be hardened against side channels, particularly timing attacks (constant-time code) and power analysis (masking, shuffling).

**SIKE/SIDH (Supersingular Isogeny Key Encapsulation / Diffie-Hellman):** An isogeny-based key exchange scheme that was a NIST PQC candidate. SIDH was completely broken in 2022 by the *Castryck-Decru attack*, which exploited the published torsion point information to recover the secret isogeny in polynomial time. This demonstrated the risk of schemes relying on novel mathematical assumptions.

**SIS (Short Integer Solution):** A lattice problem: given a random matrix A ∈ Z_q^{n×m}, find a non-zero vector x ∈ Z^m with Ax ≡ 0 (mod q) and ‖x‖ ≤ β. SIS is the basis for lattice-based hash functions (Ajtai's construction) and signature schemes. The hardness of SIS is related to worst-case lattice problems via average-case reductions.

**SLH-DSA (Stateless Hash-Based Digital Signature Algorithm):** A PQC signature standard (FIPS 205), formerly known as SPHINCS+. SLH-DSA relies only on the security of hash functions, making it the most conservative PQC signature scheme. It uses a *hypertree* structure combining *FORS* few-time signatures with *WOTS+* one-time signatures and Merkle trees. Signatures are relatively large (7-50 KB) but security assumptions are minimal.

**Smoothing parameter:** For a lattice L and ε > 0, the smoothing parameter η_ε(L) is the smallest Gaussian parameter s such that the discrete Gaussian distribution D_{L*,1/s} over the dual lattice is within statistical distance ε of uniform. The smoothing parameter determines when Gaussian sampling over the lattice produces "smooth" outputs useful for cryptographic proofs.

**SQISign:** A compact isogeny-based digital signature scheme whose security is based on the endomorphism ring problem for supersingular elliptic curves. SQISign produces very small signatures (~177 bytes) but has relatively slow signing operations. It represents the state of the art in isogeny-based signatures after the SIDH break.

**Supersingular curve:** An elliptic curve over a finite field F_q whose trace of Frobenius is divisible by the characteristic p of the field. Equivalently, a curve whose endomorphism ring is a maximal order in a quaternion algebra. Supersingular curves have richer algebraic structure than ordinary curves, and their isogeny graphs have good expansion properties exploited in isogeny-based cryptography.

**SVP (Shortest Vector Problem):** Given a lattice L (specified by a basis), find a non-zero lattice vector of minimum Euclidean length. SVP is NP-hard under randomized reductions (for exact SVP). Approximate SVP with polynomial approximation factor is the computational problem underlying the security of lattice-based PQC.

## T

**Tight reduction:** A security reduction where the security loss (ratio between the adversary's advantage against the scheme and the implied advantage against the hard problem) is close to 1. Tight reductions enable smaller parameters because no "security gap" needs to be compensated. ML-KEM has relatively tight reductions; ML-DSA's reductions involve a loss proportional to the number of signing queries.

**TLS (Transport Layer Security):** The dominant protocol for secure communication on the Internet (HTTPS, email, VPN). TLS 1.3 is being extended with PQC through hybrid key exchange (combining X25519 with ML-KEM) and PQC authentication (ML-DSA certificates). The transition requires handling larger handshake messages and potentially multiple round trips.

**TPM (Trusted Platform Module):** A hardware chip providing platform integrity measurement, secure key storage, and cryptographic operations. The TCG is updating TPM specifications to support PQC algorithms, requiring both firmware updates and hardware changes to accommodate larger key sizes and PQC-specific operations.

**Trapdoor:** Secret information that makes an otherwise hard problem easy. In PQC: the private key in *FN-DSA* is a short basis for an NTRU lattice (making lattice decoding easy); the private key in McEliece is the structure of the Goppa code (making syndrome decoding easy). The public key hides the trapdoor while preserving functionality.

## U

**UOV (Unbalanced Oil and Vinegar):** A multivariate digital signature scheme under NIST consideration for additional standardization. UOV uses a system of quadratic equations with a trapdoor based on the partition of variables into "oil" (secret) and "vinegar" (public) sets. It offers small signatures but large public keys.

## V

**Vélu's formulas:** Explicit algebraic formulas for computing an *isogeny* given its kernel subgroup. For a kernel of size ℓ, Vélu's formulas compute the isogeny and target curve in O(ℓ) field operations. The √élu algorithm (Bernstein, De Feo, Leroux, Smith) improves this to O(√ℓ) for large prime-degree isogenies.

## W

**WOTS+ (Winternitz One-Time Signature Plus):** An optimized one-time hash-based signature scheme used as a building block in *XMSS*, *LMS*, and *SLH-DSA*. WOTS+ signs a message by iteratively hashing secret values; the Winternitz parameter w trades signature size for computation (larger w gives smaller signatures but more hashing). The "+" variant includes randomized hashing for multi-target security.

## X

**X.509:** The ITU-T/ISO standard defining the format for public key certificates used in TLS, S/MIME, code signing, and other PKI applications. X.509 is being extended for PQC through new algorithm OIDs, composite certificate formats (containing both classical and PQC keys/signatures), and mechanisms for handling larger PQC certificates.

**XMSS (eXtended Merkle Signature Scheme):** A stateful hash-based signature scheme standardized in RFC 8391 and NIST SP 800-208. XMSS uses a Merkle tree over *WOTS+* one-time signatures with L-tree construction. State management is critical: signing the same one-time key twice catastrophically compromises security. XMSS^MT extends XMSS with a multi-tree structure for larger signing capacity.

**XOF (Extendable Output Function):** A hash function variant that can produce arbitrary-length output. SHAKE-128 and SHAKE-256 are the primary XOFs used in PQC standards. XOFs enable efficient generation of pseudorandom matrices, mask values, and other variable-length cryptographic material from fixed-length seeds.

## Y

**Y-00 protocol:** A physical-layer encryption scheme sometimes confused with quantum cryptography. Y-00 uses coherent optical states for communication security but does not provide information-theoretic security guarantees. It is unrelated to PQC and should not be confused with quantum-resistant algorithms.

## Z

**Zero-knowledge proof:** A cryptographic protocol where a prover convinces a verifier of a statement's truth without revealing any information beyond the statement's validity. The sigma protocols underlying *ML-DSA* (Fiat-Shamir with Aborts) have a zero-knowledge property: the transcript reveals nothing about the secret key. Zero-knowledge proofs are also being developed with post-quantum security for blockchain and privacy applications.

---

## Extended Terms

### Additional Lattice and Algebra Terms

**Basis (lattice):** A set of linearly independent vectors b₁, ..., bₙ ∈ R^n that generate a lattice L = {Σ zᵢbᵢ : zᵢ ∈ Z}. A lattice has infinitely many bases related by unimodular transformations. The quality of a basis (how short and orthogonal its vectors are) determines how easy it is to solve lattice problems. Cryptographic public keys correspond to "bad" bases while secret keys correspond to "good" bases.

**Canonical embedding:** The ring homomorphism σ: Q[x]/(f(x)) → C^n that maps a polynomial to its evaluations at all complex roots of f(x). For cyclotomic polynomials, the canonical embedding maps ring elements to vectors in R^n (after appropriate identification), providing the geometric interpretation needed for lattice analysis of ring-based schemes.

**Circulant matrix:** A matrix where each row is a cyclic shift of the previous row. Anti-circulant matrices (negacyclic shifts) arise naturally from multiplication in Z_q[x]/(x^n + 1). The special structure of circulant matrices enables NTT-based fast multiplication but also introduces algebraic structure that must be carefully analyzed for security.

**Coppersmith's method:** A technique for finding small roots of polynomial equations modulo a composite number or over the integers, using the *LLL* lattice reduction algorithm. Coppersmith's method has applications in RSA cryptanalysis and in analyzing certain lattice-based constructions.

**Deterministic signature:** A signature scheme where the signing algorithm is deterministic (no fresh randomness needed). ML-DSA supports a deterministic mode where the per-signature randomness is derived from the message and secret key via a PRF. Deterministic signing prevents failures due to poor randomness but may enable fault attacks that exploit repeated computations.

**Dimension (lattice):** The rank of a lattice, equal to the number of basis vectors. Lattice problems become exponentially harder as dimension increases. ML-KEM-768 operates in effective lattice dimension 768, and ML-KEM-1024 in dimension 1024. The security level roughly doubles with each additional 256 dimensions.

### Additional Protocol and Implementation Terms

**Constant-time implementation:** A software implementation whose execution time (and memory access patterns) are independent of secret data. Constant-time code prevents timing side-channel attacks. PQC implementations must avoid secret-dependent branches, secret-dependent array indexing, and variable-time instructions (like division) on secret data. The NTT butterfly structure naturally supports constant-time implementation.

**Decryption failure rate (DFR):** The probability that a correctly-generated ciphertext fails to decrypt correctly. For ML-KEM, the DFR must be extremely small (< 2^{-139}) to prevent exploitation. The DFR is determined by the noise distribution parameters and the modulus/rounding parameters. Schemes with non-negligible DFR are vulnerable to "failure boosting" attacks.

**Domain separation:** A technique ensuring that hash function calls in different contexts produce independent outputs, typically by prepending a unique label or byte to each hash input. PQC standards use domain separation extensively to prevent cross-protocol attacks where a hash collision in one context could be exploited in another.

**Encapsulation key:** The public key in a *KEM*, used by the encapsulator to generate a ciphertext and shared secret. In ML-KEM, the encapsulation key consists of a compressed representation of the public matrix and public vector.

**Expansion factor:** The ratio between ciphertext size and plaintext size in an encryption scheme or between public key size and secret key size. PQC schemes typically have larger expansion factors than classical schemes, impacting bandwidth and storage requirements.

**Forward secrecy (perfect forward secrecy):** A property of key exchange protocols ensuring that compromise of long-term keys does not compromise past session keys. Achieved by using ephemeral key pairs for each session. PQC hybrid key exchange in TLS 1.3 maintains forward secrecy through ephemeral ML-KEM key pairs.

**Gaussian sampler:** An algorithm that produces samples from the discrete Gaussian distribution D_{Z,σ}. Implementations must be constant-time and avoid floating-point arithmetic on secret data. *FN-DSA* requires high-precision Gaussian sampling (a significant implementation challenge), while ML-KEM/ML-DSA avoid it by using the *CBD* instead.

**Hedged signature:** A signature scheme that incorporates both deterministic (derived from message and key) and random components in its nonce generation. Hedging provides security against both poor randomness (deterministic component) and fault attacks (random component). ML-DSA supports a hedged mode recommended for most implementations.

**IKE/IKEv2 (Internet Key Exchange):** The protocol used to establish security associations for IPsec VPNs. RFC 9370 specifies how to combine multiple key exchanges (including PQC) in IKEv2. strongSwan and Libreswan implement PQC-hybrid IKEv2.

**Key compression:** A technique for reducing public key or ciphertext size by representing elements with fewer bits. ML-KEM uses coefficient compression (rounding to fewer bits) for both the public key and ciphertext. Compression introduces a small rounding error that must remain within the scheme's error-correction capacity.

**Lattice sieving:** A family of algorithms for finding short lattice vectors by generating many lattice vectors and finding pairs that can be combined into shorter vectors. Sieving algorithms (e.g., GaussSieve, HashSieve, BDGL) achieve time complexity 2^{0.292n+o(n)} for SVP in dimension n, making them the most efficient known SVP solvers for cryptographic dimensions. They serve as the SVP oracle in *BKZ*.

**Masking (countermeasure):** A side-channel countermeasure that splits sensitive values into multiple random shares, performing computations on shares independently. First-order masking splits a value x into (r, x⊕r) for random r. Higher-order masking uses more shares for stronger protection. Masking PQC implementations (especially the NTT and polynomial arithmetic) is an active research area.

**NIST security levels:** Five discrete security strength categories defined by NIST for PQC standardization: Level 1 (at least as hard as AES-128 key recovery), Level 2 (at least SHA-256 collision), Level 3 (at least AES-192 key recovery), Level 4 (at least SHA-384 collision), Level 5 (at least AES-256 key recovery). ML-KEM-512/768/1024 target Levels 1/3/5; ML-DSA-44/65/87 target Levels 2/3/5.

**Polynomial multiplication:** The core algebraic operation in lattice-based PQC. Naive multiplication of two degree-(n-1) polynomials costs O(n²) coefficient operations. The *NTT* reduces this to O(n log n). In the NTT domain, multiplication is pointwise (n independent modular multiplications), making it highly parallelizable.

**Post-quantum TLS:** TLS 1.3 extended with PQC algorithms for key exchange and/or authentication. Key exchange uses hybrid groups (e.g., X25519+ML-KEM-768); authentication uses PQC certificates (ML-DSA or SLH-DSA). Challenges include larger handshake messages potentially exceeding UDP MTU, requiring multiple round trips or certificate compression.

**Rounding:** The operation of reducing the precision of a value by mapping to a smaller set of representatives. In ML-KEM, rounding (compression) maps Z_q coefficients to Z_{2^d} for small d, reducing ciphertext size. The rounding error behaves like additional noise that must be absorbed by the scheme's error tolerance.

**Seed (cryptographic):** A short random value from which longer pseudorandom values are derived. In ML-KEM, the public matrix A is generated by expanding a 32-byte seed using SHAKE-128. This "seed representation" dramatically reduces public key size compared to storing A explicitly. Key generation starts from a 64-byte random seed that determines the entire key pair.

**Sigma protocol:** A three-move interactive proof (commitment, challenge, response) between a prover and verifier. Sigma protocols form the basis for many digital signatures via the *Fiat-Shamir transform*. ML-DSA's signing procedure follows this structure: compute a commitment w₁, derive challenge c = H(message, w₁), compute response z, and verify bounds on z.

**Syndrome decoding:** The problem of finding a minimum-weight error vector e given a syndrome s = He^T for a parity-check matrix H. For random codes, syndrome decoding is NP-hard (in the worst case). The average-case hardness of syndrome decoding for random codes provides the security foundation for code-based cryptography.

**Torsion point:** A point P on an elliptic curve with finite order: [n]P = O for some positive integer n. The n-torsion subgroup E[n] = {P ∈ E : [n]P = O} has structure Z/nZ × Z/nZ for n coprime to the characteristic. The Castryck-Decru attack on SIDH exploited auxiliary torsion point information that was published as part of the public key.

**Unforgeability:** See *EUF-CMA*. The primary security goal for digital signatures: no efficient adversary should be able to produce a valid signature on a message not previously signed by the legitimate signer, even after observing polynomially many legitimate signatures on adaptively chosen messages.

### Additional Security and Deployment Terms

**Agile cryptography:** See *Cryptographic agility*. The design principle of building systems that can transition between cryptographic algorithms with minimal disruption. Critical for PQC migration and for future-proofing against potential algorithm compromises.

**BIKE (Bit Flipping Key Encapsulation):** A code-based KEM candidate in NIST's additional algorithms track, based on quasi-cyclic moderate-density parity-check (MDPC) codes. BIKE uses a bit-flipping decoder and offers compact key sizes relative to Classic McEliece but has a non-negligible (though very small) decryption failure rate requiring careful analysis.

**Certificate chain:** A sequence of X.509 certificates from an end-entity certificate to a trusted root CA, where each certificate is signed by the next certificate's key. PQC migration affects certificate chains significantly: larger PQC signatures increase chain size, potentially causing fragmentation in protocols like TLS (especially over DTLS/UDP). Certificate compression (RFC 8879) helps mitigate this.

**Certificate transparency (CT):** A framework for publicly logging TLS certificates to detect misissued certificates. PQC certificates will be logged in CT logs, requiring log infrastructure to handle larger certificate entries and PQC signature verification during audit.

**CMVP (Cryptographic Module Validation Program):** The joint NIST/CSE program that validates cryptographic modules against FIPS 140 requirements. PQC algorithms in FIPS 203/204/205 will require CMVP validation before use in federal systems. The validation process includes algorithm testing (ACVP), physical security testing, and documentation review.

**Combiners (KEM combiners):** Constructions that combine multiple KEMs into a single KEM whose security holds if any constituent KEM remains secure. Common combiners include concatenation (K = KDF(K₁ ‖ K₂)), XOR (for equal-length keys), and split-key PRF constructions. The choice of combiner affects the security proof model and whether CCA security is preserved.

**Compression (ML-KEM):** The process of representing polynomial coefficients with fewer bits by rounding. In ML-KEM, the public key vector t is compressed to d_u bits per coefficient, and the ciphertext components are compressed to d_v bits. This lossy compression is a form of rounding that introduces noise within the scheme's error tolerance.

**Core-SVP model:** A security estimation methodology that measures lattice hardness by the cost of one SVP oracle call in the BKZ block dimension β needed to break the scheme. The cost is estimated as 2^{0.292β} (classical sieving) or 2^{0.265β} (quantum sieving). This model is used to set concrete security levels for lattice-based PQC parameters.

**Crypto discovery:** The process of identifying and cataloging all cryptographic algorithms, keys, certificates, and protocols in use across an organization's systems. Crypto discovery is the first step in PQC migration planning, enabling organizations to identify quantum-vulnerable assets and prioritize remediation.

**Decapsulation key:** The private (secret) key in a *KEM*, used by the decapsulator to recover the shared secret from a ciphertext. In ML-KEM, the decapsulation key contains the secret vector s, the public key (for re-encapsulation check), a hash of the public key, and a random value z for implicit rejection.

**Dual-use algorithm:** A cryptographic algorithm suitable for both classified and unclassified applications. ML-KEM and ML-DSA are positioned as dual-use under CNSA 2.0 guidelines, intended to protect both national security and commercial systems.

**Entropy source:** A physical or computational process providing unpredictable random bits for cryptographic key generation and nonce creation. PQC key generation requires high-quality entropy; the security of the entire scheme depends on the unpredictability of the initial seed. Hardware random number generators (ring oscillators, shot noise circuits) and operating system entropy pools (/dev/urandom) are standard sources.

**Ephemeral key:** A key pair generated for a single session or transaction and discarded afterward. Ephemeral ML-KEM key pairs in TLS provide *forward secrecy*: compromise of the server's long-term key does not reveal past session keys. The cost of generating ephemeral ML-KEM key pairs is low enough for per-connection use.

**ETSI QSC (Quantum-Safe Cryptography):** The ETSI Industry Specification Group focused on quantum-safe cryptographic standards and migration guidance. ETSI publishes technical reports (TR 103 619) on migration strategies and maintains a quantum-safe cryptography reference framework.

**Fiat-Shamir with Aborts:** The paradigm used in *ML-DSA* where the Fiat-Shamir transform is combined with rejection sampling. After computing a candidate signature, the signer checks whether it would leak information about the secret key; if so, the signature is "aborted" and the process restarts. This prevents key recovery from multiple signature observations.

**Forking lemma:** A proof technique for the Fiat-Shamir transform showing that a forger who can produce a valid signature with non-negligible probability can be "rewound" (run again with a different hash value) to extract a witness for the underlying hard problem. The forking lemma introduces a quadratic security loss. Quantum generalizations exist but are more complex.

**Grover oracle:** A quantum oracle implementation needed to apply *Grover's algorithm* to a specific search problem. The concrete cost of constructing a Grover oracle for AES key search (requiring quantum implementations of AES circuits) significantly exceeds the O(√N) query complexity, reducing Grover's practical impact on symmetric cryptography.

**Hash-then-sign:** A signature paradigm where the message is first hashed to a fixed-length digest, which is then signed. All PQC signature schemes effectively use this paradigm (the message is absorbed into a hash context before signing), enabling signing of messages of arbitrary length.

**Hybrid certificate:** An X.509 certificate containing both classical and PQC public keys and/or signed with both classical and PQC signature algorithms. Hybrid certificates enable gradual migration: verifiers that support PQC validate the PQC signature, while legacy verifiers validate the classical signature. Multiple encoding approaches exist (composite, dual-signed, and alternative extensions).

**Key encapsulation:** See *Encapsulation*. The process of generating a fresh shared secret and a ciphertext (encapsulation of the secret) using only the recipient's public key. The recipient uses their private key to recover (decapsulate) the shared secret.

**Lattice Gaussian sampling:** The process of sampling vectors from the discrete Gaussian distribution over a lattice, required by *FN-DSA* for producing signatures. This operation requires high precision (53+ bits of floating-point arithmetic) and must be performed in constant time to prevent side-channel attacks, making it the primary implementation challenge for FN-DSA.

**LUOV:** Lifted Unbalanced Oil and Vinegar, a variant of *UOV* that operates over extension fields to reduce public key size. LUOV and related schemes demonstrate the ongoing research in improving multivariate signature efficiency.

**NIST PQC competition:** The multi-year standardization process (2016-2024) conducted by NIST to select post-quantum algorithms for standardization. The process consisted of three rounds of public evaluation, with community cryptanalysis, performance benchmarking, and security analysis informing selection decisions. 82 initial submissions were narrowed to four standards plus additional algorithms.

**Pre-hash mode:** A signature scheme mode where the message is hashed externally before being passed to the signature algorithm. FIPS 204 and 205 define pre-hash variants (HashML-DSA, HashSLH-DSA) alongside direct signing modes. Pre-hashing enables streaming and reduces memory requirements for large messages.

**Quantum annihilation:** A colloquial term for the threat that quantum computers pose to currently deployed public-key cryptography. Used in awareness campaigns to emphasize the urgency of PQC migration.

**Ring structure:** The algebraic structure present in polynomial rings Z_q[x]/(f(x)) used in ring-LWE and module-LWE. Ring structure enables compact representation (one ring element replaces an entire matrix row) but introduces algebraic relations that could potentially be exploited. No practical attack exploiting ring structure against standard parameters is known.

**Security parameter (λ):** A positive integer parameterizing the security strength of a cryptographic scheme. All algorithms run in time polynomial in λ, while attacks require time super-polynomial (typically exponential) in λ. For NIST Level 1/3/5, the concrete security parameter corresponds to 128/192/256 bits respectively.

**Structural lattice:** A lattice with additional algebraic structure (such as ideal lattices, module lattices, or NTRU lattices) that enables more compact cryptographic constructions. The security of structural lattices depends on whether their additional structure can be exploited by attackers — an area of active cryptanalytic research.

**Worst-case hardness:** A hardness guarantee that holds for all instances of a problem, not just random or average instances. Lattice-based PQC uniquely benefits from worst-case to average-case reductions: solving random LWE instances (the cryptographic assumption) is provably at least as hard as solving the worst case of approximate lattice problems (GapSVP, SIVP).
