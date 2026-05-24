# Appendix B: Glossary of Terms

## A

**AES (Advanced Encryption Standard):** NIST-standardized symmetric block cipher. AES-256 provides 128-bit quantum security.

**Algorithm agility:** See *Cryptographic agility*.

**Authentication:** The process of verifying identity or data origin. PQC provides quantum-resistant authentication via digital signatures.

## B

**BKZ (Block Korkine-Zolotarev):** A lattice reduction algorithm parameterized by block size β. The primary tool for estimating lattice problem hardness.

**BQP (Bounded-Error Quantum Polynomial Time):** The class of problems efficiently solvable by quantum computers.

## C

**CBOM (Cryptographic Bill of Materials):** A structured inventory of cryptographic assets within a system or organization.

**CBD (Centered Binomial Distribution):** The noise distribution used in ML-KEM and ML-DSA, parameterized by η.

**CCA (Chosen Ciphertext Attack):** An attack model where the adversary can query a decryption oracle. IND-CCA2 is the standard security notion for KEMs.

**CNSA (Commercial National Security Algorithm Suite):** NSA's recommended algorithms. CNSA 2.0 specifies the PQC transition timeline.

**CPA (Chosen Plaintext Attack):** An attack model where the adversary can query an encryption oracle.

**CRQC (Cryptographically Relevant Quantum Computer):** A quantum computer capable of breaking production cryptographic keys (estimated 10-20 years away).

**Cryptographic agility:** The ability to replace cryptographic algorithms without redesigning systems.

**CSIDH:** Commutative Supersingular Isogeny Diffie-Hellman. A key exchange protocol based on class group actions on elliptic curves.

## D

**Decapsulation:** The KEM operation that recovers a shared secret from a ciphertext using the secret key.

**Digital signature:** A cryptographic mechanism proving that a message was created by a specific entity.

**DRBG (Deterministic Random Bit Generator):** A cryptographic pseudo-random number generator seeded by true entropy.

## E

**ECC (Elliptic Curve Cryptography):** Public-key cryptography based on elliptic curve discrete logarithm. Broken by Shor's algorithm.

**Encapsulation:** The KEM operation that generates a shared secret and corresponding ciphertext.

**Endomorphism ring:** The ring of group homomorphisms from an elliptic curve to itself. Central to isogeny-based cryptography.

**EUF-CMA (Existential Unforgeability under Chosen Message Attack):** The standard security notion for digital signature schemes.

## F

**FIPS (Federal Information Processing Standard):** US government standards for computing. PQC standards: FIPS 203 (ML-KEM), FIPS 204 (ML-DSA), FIPS 205 (SLH-DSA).

**FN-DSA:** Fast-Fourier Lattice-based Compact Signatures over NTRU. Formerly known as FALCON.

**FO Transform (Fujisaki-Okamoto):** A generic transform converting CPA-secure encryption into CCA-secure KEM.

**FORS (Forest of Random Subsets):** A few-time signature scheme used as a component in SLH-DSA.

**FHE (Fully Homomorphic Encryption):** Encryption allowing computation on ciphertexts. All practical schemes are lattice-based.

## G

**Goppa code:** A class of error-correcting codes used in the McEliece cryptosystem.

**Grover's algorithm:** A quantum algorithm providing quadratic speedup for unstructured search. Halves the effective security of symmetric algorithms.

## H

**Harvest Now, Decrypt Later (HNDL):** Attack model where encrypted data is collected today for future decryption by quantum computers.

**Hash-based signatures:** Digital signatures whose security relies only on hash function properties. SLH-DSA is the NIST standard.

**HQC (Hamming Quasi-Cyclic):** A code-based KEM selected by NIST for additional standardization.

**HSM (Hardware Security Module):** Tamper-resistant hardware for cryptographic key management and operations.

**Hybrid scheme:** Combining classical and PQC algorithms so security holds if either remains unbroken.

**Hypertree:** The multi-layer tree structure used in SLH-DSA, combining FORS, WOTS+, and Merkle trees.

## I

**IND-CCA2 (Indistinguishability under Adaptive Chosen Ciphertext Attack):** The gold standard security notion for encryption and KEM schemes.

**Information Set Decoding (ISD):** The best known attack family for code-based cryptographic schemes.

**Isogeny:** A surjective group homomorphism between elliptic curves that is also a morphism of varieties.

## K

**KDF (Key Derivation Function):** Derives cryptographic keys from shared secrets or passwords.

**KEM (Key Encapsulation Mechanism):** A public-key primitive that establishes a shared secret between two parties.

## L

**Lattice:** A discrete additive subgroup of R^n; equivalently, the set of all integer linear combinations of basis vectors.

**LMS (Leighton-Micali Signature):** A stateful hash-based signature scheme standardized in RFC 8554.

**LWE (Learning With Errors):** The hard problem underlying most lattice-based cryptography. Given noisy linear equations, recover the secret.

## M

**Merkle tree:** A binary hash tree enabling efficient authentication of large datasets using a single root hash.

**ML-DSA (Module-Lattice Digital Signature Algorithm):** FIPS 204. The primary PQC signature standard, based on Module-LWE/SIS.

**ML-KEM (Module-Lattice Key Encapsulation Mechanism):** FIPS 203. The primary PQC KEM standard, based on Module-LWE.

**Module-LWE:** A variant of LWE over a module of polynomial rings, balancing security and efficiency.

**Mosca's theorem:** If data lifetime + migration time > CRQC arrival time, then action is already overdue.

**MQ problem:** Solving systems of multivariate quadratic polynomial equations. NP-hard; basis of multivariate PQC.

## N

**NIST:** National Institute of Standards and Technology. Conducted the PQC standardization process.

**NTT (Number Theoretic Transform):** The finite-field FFT enabling O(n log n) polynomial multiplication. Critical for ML-KEM/ML-DSA performance.

**NTRU:** A lattice-based hard problem and cryptosystem family. FN-DSA uses NTRU lattices.

## O

**OID (Object Identifier):** A globally unique identifier for algorithms in standards like X.509.

**One-time signature:** A signature scheme secure for signing exactly one message (e.g., WOTS+, Lamport).

## P

**PQC (Post-Quantum Cryptography):** Cryptographic algorithms secure against both classical and quantum computers, running on classical hardware.

**PQXDH:** Post-Quantum Extended Diffie-Hellman. Signal's hybrid key agreement protocol combining X25519 with ML-KEM.

## Q

**QKD (Quantum Key Distribution):** Key distribution using quantum mechanical properties. Requires specialized hardware.

**QROM (Quantum Random Oracle Model):** Security model where adversaries can query hash functions in quantum superposition.

**Quantum supremacy/advantage:** Demonstration that a quantum computer outperforms classical computers at a specific task.

## R

**Rejection sampling:** Technique where outputs correlated with the secret are discarded. Used in ML-DSA signing.

**Ring-LWE:** LWE variant over polynomial rings, providing compact key sizes. Module-LWE generalizes this.

## S

**Shor's algorithm:** Quantum algorithm for factoring integers and computing discrete logarithms in polynomial time. Breaks RSA, DH, ECC.

**SIKE/SIDH:** Broken isogeny-based key exchange. Defeated by Castryck-Decru attack in 2022.

**SIS (Short Integer Solution):** Given matrix A, find short x with Ax = 0. Basis for lattice-based signatures.

**SLH-DSA (Stateless Hash-Based Digital Signature Algorithm):** FIPS 205. Conservative PQC signature relying only on hash function security.

**Supersingular curve:** An elliptic curve with endomorphism ring isomorphic to a maximal order in a quaternion algebra. Used in isogeny-based crypto.

**SVP (Shortest Vector Problem):** Given a lattice, find the shortest non-zero vector. Fundamental hard problem for lattice-based crypto.

## T

**TLS (Transport Layer Security):** Protocol for secure communication over networks. PQC integrated via hybrid key exchange and PQC certificates.

**TPM (Trusted Platform Module):** Hardware chip for platform security. PQC support being added to TPM specifications.

## U

**UOV (Unbalanced Oil and Vinegar):** A multivariate signature scheme under NIST consideration for additional standardization.

## V

**Vélu's formulas:** Explicit formulas for computing isogenies given their kernel subgroups.

## W

**WOTS+ (Winternitz One-Time Signature Plus):** An optimized one-time signature used within XMSS and SLH-DSA.

## X

**X.509:** Standard format for public key certificates. Being extended for PQC algorithms and composite/hybrid certificates.

**XMSS (eXtended Merkle Signature Scheme):** Stateful hash-based signature standardized in RFC 8391 and NIST SP 800-208.
