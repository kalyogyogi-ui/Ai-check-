# Chapter 10: The NIST Post-Quantum Standardization Process

## 10.1 Why NIST?

The National Institute of Standards and Technology (NIST) has a long history of cryptographic standardization:
- **DES (1977):** Data Encryption Standard
- **AES (2001):** Advanced Encryption Standard (open competition)
- **SHA-3 (2012):** Third-generation hash standard (open competition)

NIST's approach of open, transparent competitions with public analysis has proven effective at selecting robust standards. For post-quantum cryptography, NIST initiated its most ambitious standardization effort to date.

## 10.2 Timeline of the PQC Standardization

### Pre-Competition (2014-2016)

- **2014:** NIST workshops on quantum-resistant cryptography begin
- **2015:** NSA announces it will transition to quantum-resistant algorithms
- **December 2016:** NIST publishes the Call for Proposals (NISTIR 8105)
- **Deadline:** November 2017 for submissions

### Round 1 (2017-2019)

- **69 complete submissions** received (of 82 total)
- Categories: Key Establishment (KEM/PKE) and Digital Signatures
- Public analysis and comment period
- **January 2019:** 26 candidates advance to Round 2

**Round 1 Eliminations:** Candidates removed due to:
- Complete breaks (security failures)
- Insufficient security margins
- Poor performance relative to alternatives
- Incomplete specifications

### Round 2 (2019-2020)

- **26 candidates** undergo intense scrutiny
- NIST-sponsored workshops and conferences
- Extensive third-party cryptanalysis
- **July 2020:** 7 finalists and 8 alternates announced for Round 3

### Round 3 (2020-2022)

**Finalists (7):**

*KEMs:*
- CRYSTALS-Kyber (lattice)
- NTRU (lattice)
- Classic McEliece (code)
- SABER (lattice)

*Signatures:*
- CRYSTALS-Dilithium (lattice)
- FALCON (lattice)
- Rainbow (multivariate)

**Alternates (8):**
- BIKE, FrodoKEM, HQC, NTRU Prime, SIKE (KEMs)
- GeMSS, Picnic, SPHINCS+ (signatures)

### Key Events During Round 3

- **February 2022:** Rainbow completely broken (Beullens' attack)
- **July 2022:** SIKE completely broken (Castryck-Decru attack)
- **July 2022:** NIST announces selections

### Selections and Standards (2022-2024)

**July 2022 — NIST announces primary selections:**
- **CRYSTALS-Kyber** → Standardized as ML-KEM (FIPS 203)
- **CRYSTALS-Dilithium** → Standardized as ML-DSA (FIPS 204)
- **SPHINCS+** → Standardized as SLH-DSA (FIPS 205)
- **FALCON** → Selected for standardization (pending)

**August 2024 — Final standards published:**
- FIPS 203 (ML-KEM): Final standard
- FIPS 204 (ML-DSA): Final standard
- FIPS 205 (SLH-DSA): Final standard

### Round 4 and Beyond (2022-present)

NIST continues evaluating additional algorithms:
- **KEM:** Classic McEliece, BIKE, HQC (HQC selected 2024)
- **Signatures:** Additional call issued for diverse signature schemes
- **Additional signatures:** UOV, MAYO, SQISign, and others under evaluation

## 10.3 Selection Criteria

NIST evaluated candidates across multiple dimensions:

### Security

1. **Theoretical security:** Quality of security proofs and reductions
2. **Cryptanalytic resistance:** Withstanding community analysis
3. **Security margin:** Buffer between parameters and known attacks
4. **Algorithm diversity:** Different mathematical foundations provide insurance

### Performance

1. **Computational cost:** Key generation, encapsulation/signing, decapsulation/verification
2. **Communication cost:** Key sizes, ciphertext/signature sizes
3. **Platform diversity:** Performance on servers, desktops, embedded, and HSMs
4. **Scalability:** Behavior under high load

### Implementation Characteristics

1. **Constant-time feasibility:** Can be implemented without timing leaks
2. **Misuse resistance:** Robustness against implementation errors
3. **Simplicity:** Ease of correct implementation
4. **Side-channel resistance:** Natural resistance or feasibility of protection

## 10.4 Why Kyber/ML-KEM Won

CRYSTALS-Kyber was selected over NTRU, SABER, and Classic McEliece for several reasons:

### Advantages of Kyber/ML-KEM

1. **Balanced performance:** Good key sizes, fast operations, reasonable ciphertext
2. **Strong security proofs:** Tight reduction to Module-LWE
3. **Implementation friendly:** Simple NTT-based arithmetic, no floating-point needed
4. **Flexibility:** Three parameter sets cover all security levels
5. **CCA security:** Clean Fujisaki-Okamoto transform application
6. **No decryption failures:** Negligible failure probability with chosen parameters

### Why Not NTRU?
- Slightly less favorable size/performance trade-off
- More complex key generation (finding invertible elements)
- Decryption failures require careful handling
- Less clean theoretical framework

### Why Not Classic McEliece?
- Public keys too large (hundreds of KB to MB)
- Not practical for most deployment scenarios
- Selected for Round 4 (standardized separately)

### Why Not SABER?
- Very similar to Kyber in structure and performance
- Kyber's use of NTT-friendly modulus (q = 3329) provided efficiency edge
- NIST selected one lattice KEM to avoid redundancy

## 10.5 Why Dilithium/ML-DSA Won

### Advantages of Dilithium/ML-DSA

1. **Best overall balance:** Reasonable signature and key sizes with good speed
2. **Clean design:** Fiat-Shamir with aborts is well-understood
3. **Implementation simplicity:** Straightforward rejection sampling
4. **No floating-point:** Unlike FALCON, no Gaussian sampling over reals needed
5. **Constant-time:** Naturally constant-time (rejection loop has bounded, public count)

### Why Not FALCON?
- Requires floating-point Gaussian sampling (complex, side-channel sensitive)
- Selected for standardization but with caveats about implementation difficulty
- Smaller signatures than ML-DSA, important for some applications
- Standardization as FN-DSA is proceeding separately

### Why Not Rainbow?
- Broken during Round 3 (February 2022)
- Demonstrated risk of multivariate layered constructions

## 10.6 The Role of SPHINCS+/SLH-DSA

SPHINCS+ was selected despite being slower and producing larger signatures than ML-DSA because:

1. **Algorithmic diversity:** Only hash-based scheme among finalists
2. **Conservative security:** Minimal assumptions (only hash function security)
3. **Insurance policy:** If lattice-based cryptanalysis advances, SLH-DSA remains secure
4. **Proven foundations:** Hash-based signatures have the longest theoretical track record

NIST explicitly stated that SLH-DSA provides a "hedge" against unexpected developments in lattice cryptanalysis.

## 10.7 Naming Conventions

NIST renamed algorithms for their standards:

| Original Name | Standard Name | FIPS Number |
|--------------|--------------|-------------|
| CRYSTALS-Kyber | ML-KEM | FIPS 203 |
| CRYSTALS-Dilithium | ML-DSA | FIPS 204 |
| SPHINCS+ | SLH-DSA | FIPS 205 |
| FALCON | FN-DSA | (Pending) |

The "ML" prefix stands for "Module-Lattice," indicating the underlying mathematical structure. "SLH" stands for "Stateless Hash-based."

## 10.8 Ongoing Standardization Activities

### HQC Standardization

In 2024, NIST announced HQC (Hamming Quasi-Cyclic) would be standardized as an additional KEM:
- Provides code-based diversity alongside ML-KEM
- Different mathematical foundation from lattice-based ML-KEM
- Slightly larger parameters but well-understood security

### Additional Signature Competition

NIST issued a separate call for additional digital signature schemes, seeking:
- Short signatures and/or short public keys
- Diversity from lattice-based ML-DSA
- Schemes with unique properties (e.g., aggregation capability)

Candidates under evaluation include:
- **UOV:** Multivariate, small signatures
- **MAYO:** Compressed multivariate
- **SQISign:** Isogeny-based, smallest overall sizes
- **CROSS:** Code-based
- **Various others:** ~40 submissions received

### Stateful Hash-Based Signatures

Already standardized separately:
- **XMSS:** RFC 8391, NIST SP 800-208
- **LMS:** RFC 8554, NIST SP 800-208
- Recommended for specific use cases (firmware signing, CAs)

## 10.9 International Standardization

NIST's process has influenced but does not stand alone internationally:

### ISO/IEC

- ISO/IEC 14888-4: Will include PQC signature standards
- Working to align with NIST selections

### ETSI

- ETSI QSC (Quantum-Safe Cryptography) working group
- Publishes guidance on migration and deployment
- TR 103 619: Quantum-safe cryptography implementation

### IETF

- Integrating PQC into internet protocols
- RFC 9370: PQC key exchange in TLS
- Drafts for post-quantum certificates, VPNs, email

### BSI (German Federal Office)

- Published separate PQC recommendations
- Generally aligned with NIST but with some parameter differences
- Emphasizes FrodoKEM (conservative, unstructured lattice) alongside NIST standards

### ANSSI (French National Cybersecurity Agency)

- Recommends hybrid-only approach during transition
- Requires classical + PQC in combination
- More conservative timeline than NIST

## 10.10 Lessons Learned

The NIST PQC standardization provides several lessons:

1. **Open competitions work:** Public analysis found critical flaws (Rainbow, SIKE) before standardization
2. **Diversity matters:** Having multiple mathematical foundations prevents single points of failure
3. **Implementation matters:** Theoretical elegance doesn't guarantee practical deployability
4. **Patience pays:** The 8-year process (2016-2024) allowed thorough analysis
5. **Expect surprises:** Major breaks (Rainbow, SIKE) came late in the process
6. **Balance needed:** Security confidence, performance, and implementation complexity must all be weighed
7. **Migration begins before completion:** Organizations should start planning during standardization, not after

## 10.11 Key Takeaways

- NIST's 8-year open competition process selected algorithms from 69 initial submissions
- Three primary standards: ML-KEM (FIPS 203), ML-DSA (FIPS 204), SLH-DSA (FIPS 205)
- Algorithm diversity was explicitly prioritized (lattice + hash-based)
- Two schemes (Rainbow, SIKE) were broken during the competition
- Additional standardization continues for code-based KEM (HQC) and diverse signatures
- International bodies are aligning with NIST selections
- The standards are final and deployment should begin immediately

---

*Next: [Chapter 11 — FIPS 203: ML-KEM](./11-fips-203-ml-kem.md)*
