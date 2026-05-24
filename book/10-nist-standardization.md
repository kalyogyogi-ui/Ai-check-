# Chapter 10: The NIST Post-Quantum Standardization Process

## 10.1 Why NIST?

### A Legacy of Cryptographic Standards

The National Institute of Standards and Technology (NIST) occupies a unique position in the global cryptographic ecosystem. As a non-regulatory agency of the United States Department of Commerce, NIST has the dual mandate of promoting innovation and establishing measurement standards that serve industry, government, and the public. In cryptography, this has translated into a decades-long track record of defining the algorithms that protect the world's digital infrastructure.

NIST's involvement in cryptographic standardization dates back to the 1970s, when the agency (then called the National Bureau of Standards) worked with IBM and the NSA to develop the Data Encryption Standard (DES) in 1977. Despite controversies about potential NSA backdoors and the 56-bit key length, DES became the foundational block cipher for commercial cryptography and demonstrated that a federal standard could drive widespread adoption across industries and borders.

The agency's approach matured significantly with the Advanced Encryption Standard (AES) competition in 1997-2001. Rather than developing an algorithm internally or accepting one from a single submitter, NIST organized an open international competition. Fifteen candidate algorithms were submitted, publicly analyzed, and progressively narrowed to a single winner—Rijndael, designed by Belgian cryptographers Joan Daemen and Vincent Rijmen. The AES competition established the template that NIST would refine in subsequent efforts: public call for proposals, transparent evaluation criteria, multiple rounds of public analysis, and a final selection informed by community input.

The SHA-3 competition (2007-2012) further refined this model. After theoretical weaknesses were discovered in the SHA-1 family, NIST solicited hash function candidates and received 64 submissions. Through five years of analysis across multiple rounds, Keccak was selected as SHA-3. Notably, the competition served its purpose even though the feared practical breaks of SHA-2 never materialized—SHA-3 provided algorithmic diversity as insurance.

### Why Not Another Organization?

Several factors make NIST the natural choice for post-quantum standardization rather than alternative bodies:

**Institutional credibility.** NIST standards carry weight in both government procurement (through FIPS mandates) and private industry (through voluntary adoption). When NIST publishes a standard, hardware manufacturers embed it in silicon, software libraries implement it, and compliance frameworks reference it. No other organization achieves this degree of practical impact.

**Technical capacity.** NIST employs dedicated cryptographers and mathematicians who can evaluate submissions at a deep technical level. The agency's Computer Security Division has decades of experience managing the interplay between theoretical security and practical deployment.

**Open process expertise.** NIST has refined the mechanics of open competitions over multiple iterations—managing submissions, organizing workshops, soliciting public comments, and navigating the political dynamics of international participation. These procedural capabilities are as important as technical ones.

**Neutrality and accessibility.** Unlike national security agencies (NSA, GCHQ) that might favor classified algorithms or intelligence equities, NIST operates transparently. Unlike standards bodies (ISO, IETF) that can be slow or politically constrained, NIST can drive a focused multi-year effort with clear decision authority.

**Regulatory impact.** FIPS standards are mandatory for US federal agencies and widely adopted by regulated industries (finance, healthcare, critical infrastructure). This creates a guaranteed adoption pathway that incentivizes participation from the best cryptographers worldwide.

### The Scale of the Post-Quantum Challenge

The post-quantum standardization effort was unprecedented in scope even by NIST's standards. Unlike AES (one block cipher) or SHA-3 (one hash function), this effort needed to standardize replacements for multiple cryptographic primitives—key encapsulation mechanisms, digital signatures, and potentially more—across different mathematical foundations. The threat model was also unusual: standardizing defenses against an adversary (a large-scale quantum computer) that did not yet exist but whose capabilities could be precisely characterized through quantum computational complexity theory.

## 10.2 Timeline of the PQC Standardization

### Pre-Competition Phase (2014-2016)

The formal standardization process was preceded by years of growing concern within the cryptographic community about quantum threats and increasing governmental attention to the problem.

**2013-2014: Early workshops.** NIST began hosting workshops on quantum-resistant cryptography, bringing together academic researchers, industry practitioners, and government stakeholders. These workshops served to gauge the maturity of post-quantum proposals and assess whether the field was ready for standardization.

**April 2015: The NSA announcement.** The National Security Agency issued a surprising public advisory through its Information Assurance Directorate, stating that it planned to transition to quantum-resistant algorithms and advising partners to begin preparing. The advisory specifically noted that Suite B algorithms (which NSA had been promoting since 2005) would need to be replaced. This was widely interpreted as a signal that the intelligence community assessed quantum computing progress as more advanced than publicly known, though the simpler explanation—prudent long-term planning given the decades-long deployment cycles of cryptographic infrastructure—was also compelling.

**2015-2016: NIST internal deliberations.** NIST's cryptographic team, led by Dustin Moody and others, developed the framework for the competition. Key decisions included: evaluating KEMs and signatures together rather than separately; defining security levels relative to existing standards (AES-128, AES-192, AES-256); requiring complete specifications and reference implementations with submissions; and establishing evaluation criteria that weighted security, performance, and implementation characteristics.

**December 2016: The formal call.** NIST published the "Call for Proposals" in NISTIR 8105, setting a November 2017 deadline for submissions. The document specified five security levels (corresponding to the difficulty of breaking AES-128, SHA-256, AES-192, SHA-384, and AES-256), required both KEM and signature functionality, and established submission requirements including security proofs, parameter justifications, reference implementations, and known-answer test vectors.

### Round 1 (December 2017 – January 2019)

**The initial submissions.** NIST received 82 submissions, of which 69 were deemed complete and accepted for evaluation. These spanned five major mathematical approaches:

- **Lattice-based (26):** Including Kyber, Dilithium, FALCON, NTRU, SABER, FrodoKEM, NewHope, and many others
- **Code-based (17):** Including Classic McEliece, BIKE, HQC, and variations on the McEliece/Niederreiter frameworks
- **Multivariate (9):** Including Rainbow, GeMSS, LUOV, and related schemes
- **Hash-based (3):** Including SPHINCS+ and variations
- **Isogeny-based (2):** SIKE and CSIDH-related proposals
- **Other/hybrid (12):** Including zero-knowledge-based schemes and novel constructions

**Early eliminations.** Several submissions were broken almost immediately after publication—a testament to the value of open analysis. Some fell to trivial attacks exploiting implementation errors in the specification, while others had fundamental design flaws revealed by the community. Notable early breaks included schemes with algebraic vulnerabilities that allowed polynomial-time key recovery.

**The evaluation process.** During Round 1, NIST organized the First PQC Standardization Conference (April 2018) where submitters presented their schemes and attendees shared cryptanalysis results. The NIST team also conducted internal evaluations of performance, studying implementations on multiple platforms including ARM Cortex-M4 microcontrollers (representative of IoT/embedded devices).

**Round 1 results (January 2019).** NIST advanced 26 candidates to Round 2: 17 KEMs/encryption schemes and 9 signature schemes. The eliminated candidates fell into categories: complete breaks, insufficient security margins relative to parameter sizes, dramatically inferior performance compared to better alternatives in the same mathematical family, and incomplete or unclear specifications.

### Round 2 (January 2019 – July 2020)

Round 2 saw dramatically intensified scrutiny. With the field narrowed from 69 to 26 candidates, researchers could focus their analysis more deeply.

**Enhanced cryptanalysis.** The reduced candidate pool allowed for more thorough cryptanalytic attention. Several important results emerged: improved lattice reduction estimates affected security claims of lattice-based schemes; new side-channel attacks demonstrated practical vulnerabilities in some implementations; and theoretical advances in understanding the relationships between different lattice problems refined security proofs.

**Implementation studies.** NIST and the community produced extensive benchmarking data across platforms. The PQM4 project (post-quantum crypto on Cortex-M4) became a crucial reference for embedded performance. Researchers also identified implementation challenges including constant-time requirements, stack usage constraints on embedded devices, and hardware acceleration opportunities.

**The Second PQC Conference (August 2019).** This workshop provided critical input for Round 2 decisions, featuring updated security analyses, performance comparisons, and discussions about evaluation criteria.

**Round 2 results (July 2020).** NIST announced 7 finalists (candidates expected to be standardized) and 8 alternates (candidates that might advance or be standardized later):

*Finalists:*
- KEMs: CRYSTALS-Kyber, NTRU, Classic McEliece, SABER
- Signatures: CRYSTALS-Dilithium, FALCON, Rainbow

*Alternates:*
- KEMs: BIKE, FrodoKEM, HQC, NTRU Prime, SIKE
- Signatures: GeMSS, Picnic, SPHINCS+

The finalist/alternate distinction was significant: finalists were considered the most promising for standardization, while alternates might be standardized if finalists failed or if additional diversity was needed.

### Round 3 (July 2020 – July 2022)

Round 3 was the decisive phase, producing both the final selections and two spectacular breaks that validated the extended evaluation process.

**Deepening analysis.** The 15 remaining candidates received extraordinary attention from the global cryptographic community. Hundreds of papers analyzed security, efficiency, and implementation aspects. NIST conducted the Third PQC Conference (June 2021) and the Fourth Conference (scheduled to coincide with announcements).

**The SABER-Kyber-NTRU convergence.** For KEMs, the three lattice-based finalists (Kyber, NTRU, SABER) presented NIST with a complex choice. All three offered strong security from lattice assumptions, competitive performance, and reasonable parameter sizes. The choice between them came down to subtle differences in efficiency, implementation characteristics, and theoretical elegance.

**Signature competition dynamics.** For signatures, Dilithium and FALCON represented different approaches within lattice cryptography (Fiat-Shamir with aborts versus NTRU-based sampling), while Rainbow represented the multivariate alternative. SPHINCS+ as an alternate provided hash-based diversity.

### Key Events During Round 3

#### The Rainbow Break (February 2022)

Ward Beullens published a devastating attack against Rainbow that reduced its security far below claimed levels. The attack exploited the layered structure of Rainbow's multi-layered Oil-and-Vinegar construction, using algebraic techniques to peel apart the layers and recover the private key.

Specifically, Beullens' attack combined two techniques: a "rectangular min-rank" attack that exploited the structure visible in the public key, and intersection attacks that leveraged relationships between the layers. For Rainbow's Level I parameters, the attack required only approximately 2^53 operations—far below the claimed 2^128 security level and well within practical reach.

The implications were profound. Rainbow had been a finalist—one of seven schemes NIST considered most likely to be standardized. Its complete break validated several principles: the value of extended evaluation periods, the risks of schemes whose security relies on the difficulty of problems not yet extensively studied, and the importance of algorithmic diversity across different mathematical foundations.

#### The SIKE Break (July 2022)

Even more dramatic was the break of SIKE (Supersingular Isogeny Key Encapsulation), announced by Wouter Castryck and Thomas Decru just days before NIST's planned selection announcement. The attack recovered SIKE private keys in minutes on a single laptop—a complete and total break of what had been considered a serious contender.

The attack exploited the mathematical structure of the auxiliary torsion point information that SIKE published alongside isogeny computations. By applying the work of Ernst Kani on "gluing" of abelian varieties, Castryck and Decru showed that this auxiliary information created a computational shortcut, reducing the hard isogeny problem to a much easier computation on a higher-dimensional abelian variety.

The SIKE break was remarkable for several reasons. First, it came from relatively classical number theory applied in a novel way—the mathematical tools were decades old, but no one had recognized their applicability to isogeny-based cryptography. Second, SIKE had been studied for years by a large community without anyone discovering this vulnerability. Third, the break was so complete (minutes on a laptop) that it eliminated not just SIKE but cast doubt on the entire design pattern of publishing auxiliary torsion information.

Both breaks powerfully demonstrated why NIST's multi-year, open evaluation process was essential. Had standards been rushed, either Rainbow or SIKE could have been deployed worldwide before their fatal flaws were discovered.

### Selections and Standards (2022-2024)

**July 2022: NIST announces primary selections.** After six years of evaluation, NIST announced four algorithms for standardization:

- **CRYSTALS-Kyber** → to become ML-KEM (FIPS 203)
- **CRYSTALS-Dilithium** → to become ML-DSA (FIPS 204)
- **SPHINCS+** → to become SLH-DSA (FIPS 205)
- **FALCON** → selected for future standardization (implementation complexity warranted additional time)

**2022-2024: Standards development.** NIST worked with the algorithm designers to produce final standards documents. This involved minor parameter tweaks, specification clarifications, and the development of conformance testing requirements. Draft standards were published for public comment in August 2023.

**August 13, 2024: Final standards published.** NIST officially released FIPS 203, FIPS 204, and FIPS 205 as final standards, marking the culmination of eight years of work. These documents replaced the earlier competition specifications with normative standards suitable for implementation and compliance purposes.

### Round 4 and Beyond (2022-Present)

NIST recognized that three standards were insufficient for all deployment scenarios and continued evaluation of additional candidates:

**Classic McEliece.** Despite enormous public keys (ranging from 261 KB to over 1 MB depending on parameter set), Classic McEliece's decades-long security track record and conservative design made it attractive for applications where key size is not a constraint (certificate authorities, firmware signing). Standardization is proceeding separately.

**HQC selection (2024).** NIST announced that HQC (Hamming Quasi-Cyclic) would be standardized as an additional KEM, providing code-based diversity alongside the lattice-based ML-KEM. This gives implementers a choice between mathematical foundations—if lattice problems prove easier than expected, HQC provides an independent fallback.

**Additional signature call.** Recognizing that ML-DSA's relatively large signatures might be problematic for some applications, and seeking greater diversity, NIST issued a separate call for additional signature algorithms in 2022. Approximately 40 submissions were received, currently under evaluation.

## 10.3 Selection Criteria

NIST's evaluation balanced multiple dimensions, explicitly acknowledging that no single metric could determine the best algorithm. The criteria evolved through the competition as NIST gained understanding of the practical trade-offs.

### Security Evaluation

**Theoretical foundations.** NIST assessed the quality of security proofs—how tightly the scheme's security reduces to well-studied hard problems, how well-understood those underlying problems are, and whether the proofs require idealized models (random oracle model) or hold in the standard model. Schemes with tighter reductions to better-studied problems scored higher.

**Cryptanalytic resistance.** The most important security criterion was empirical: how well did the scheme withstand six years of public analysis by the world's best cryptanalysts? Schemes that required parameter adjustments during the competition (due to improved attacks) were viewed less favorably than those whose original parameters remained secure. The complete breaks of Rainbow and SIKE demonstrated why this empirical testing was essential.

**Security margins.** NIST preferred parameters with comfortable margins between estimated attack costs and target security levels. A scheme claiming NIST Level 3 security should ideally have attack costs significantly above the 2^143 quantum operation threshold, not barely meeting it. Larger margins protect against future improvements in cryptanalysis.

**Confidence level.** Distinct from raw security, NIST assessed how confident the community could be in security estimates. Problems studied for decades (LWE, coding theory) inspired more confidence than newer constructions (isogenies, layered multivariate). This "confidence level" was separate from the nominal security level—a scheme might claim 2^200 security but with lower confidence than another claiming 2^180 based on a better-understood problem.

### Performance Evaluation

**Computational efficiency.** NIST measured key generation, encapsulation/signing, and decapsulation/verification speeds across multiple platforms: modern x86-64 servers with vector instructions (AVX2/AVX-512), ARM-based mobile/embedded processors, and constrained microcontrollers (Cortex-M4 with 192 KB RAM). Performance needed to be acceptable across all target platforms, not just the fastest.

**Communication overhead.** Public key sizes, ciphertext sizes, and signature sizes directly impact protocol performance. In TLS, additional bytes increase handshake latency. In constrained networks (IoT, satellite), bandwidth is expensive. NIST weighted communication costs heavily, recognizing that bandwidth overhead is the primary practical impact of post-quantum migration for most deployed protocols.

**Memory requirements.** Embedded devices and hardware security modules have limited RAM and code storage. Stack usage during computations, total memory footprint, and code size all factored into evaluation. Schemes requiring megabytes of RAM or code were penalized for constrained environments.

**Scalability.** How do schemes perform under load? For high-throughput servers handling thousands of TLS connections per second, the computational cost of key exchange and signing multiplies. NIST considered how schemes would perform at scale in real deployment scenarios.

### Implementation Characteristics

**Constant-time feasibility.** Modern cryptographic implementations must execute in time independent of secret data to prevent timing side-channel attacks. NIST evaluated whether each scheme could be practically implemented in constant time. Schemes requiring operations like Gaussian sampling (which naturally varies in execution time) or complex rejection loops were scrutinized for side-channel resistance.

**Misuse resistance.** How badly does a scheme fail if implementers make mistakes? Some schemes are fragile—leaking a nonce destroys security entirely—while others gracefully degrade. NIST valued robustness against common implementation errors, recognizing that real-world code is written by developers with varying cryptographic expertise.

**Implementation simplicity.** Simpler algorithms are less likely to contain implementation bugs. NIST considered specification complexity, the number of distinct operations required, and the potential for subtle errors. This criterion favored schemes like Kyber (straightforward polynomial arithmetic) over schemes requiring floating-point Gaussian sampling or complex algebraic geometry.

**Side-channel resistance.** Beyond constant-time execution, NIST evaluated resistance to power analysis, electromagnetic emanation, and fault injection attacks. Hardware implementations face threats that pure software never encounters. Schemes with simpler data flows and fewer secret-dependent operations rated higher for hardware deployment.

**Hardware acceleration potential.** Would the algorithm benefit from dedicated hardware? Could existing hardware (AES-NI, SHA extensions) be leveraged? The NTT operations central to lattice schemes map well to existing DSP hardware, while some other operations require entirely new hardware designs.

## 10.4 Why Kyber/ML-KEM Won

The selection of CRYSTALS-Kyber as the primary KEM standard over three other lattice finalists (NTRU, SABER) and one code-based finalist (Classic McEliece) was among NIST's most closely debated decisions. The three lattice KEMs were remarkably close in overall quality, and NIST's decision ultimately rested on a combination of technical advantages and practical considerations.

### Kyber's Comprehensive Advantages

**Efficient arithmetic with NTT-friendly parameters.** Kyber's choice of q = 3329 (where 3329 ≡ 1 mod 256) enables a particularly efficient Number Theoretic Transform. The polynomial ring R_q = Z_q[X]/(X^256 + 1) factors into 256 linear factors modulo q, enabling complete NTT decomposition. This means polynomial multiplication can be performed entirely as pointwise multiplication in the NTT domain, avoiding the need for incomplete NTT with Karatsuba multiplication that other parameter choices require.

**Strong, clean security reduction.** Kyber's security reduces tightly to the Module-LWE problem, which itself reduces (with some tightness loss) to worst-case lattice problems. The module structure (working with vectors of ring elements rather than single ring elements or unstructured matrices) provides a sweet spot between efficiency and security confidence—more structure than plain LWE (enabling efficient implementation) but less structure than Ring-LWE (providing larger security margins against potential algebraic attacks).

**Negligible decryption failure probability.** Kyber's parameters are chosen so that the probability of decryption failure is less than 2^(-139) for ML-KEM-512 and even lower for larger parameter sets. This effectively eliminates decryption failures from practical consideration, simplifying protocol design and preventing failure-boosting attacks where an adversary selects ciphertexts that maximize failure probability.

**Simple noise sampling.** The Centered Binomial Distribution (CBD) used for noise sampling is trivial to implement in constant time: sample random bits, count them, subtract. No rejection sampling, no floating-point arithmetic, no lookup tables that might leak through cache timing. This simplicity dramatically reduces the surface area for implementation errors and side-channel vulnerabilities.

**Compact specification.** The core Kyber algorithm can be described concisely, making it accessible to implementers without deep algebraic expertise. The operations are straightforward: matrix-vector multiplication, polynomial addition, sampling from simple distributions, and compression via rounding. This accessibility is crucial for the diverse set of implementations needed across the ecosystem.

**Balanced size/performance trade-off.** At the NIST Level 3 target (ML-KEM-768), Kyber achieves a combined key-plus-ciphertext size of 2,272 bytes with operations completing in approximately 100 microseconds on commodity hardware. This balance made it suitable for the widest range of applications, from bandwidth-constrained IoT to latency-sensitive web traffic.

### Why Not NTRU?

NTRU, invented in 1996 by Hoffstein, Pipher, and Silverman, is the oldest lattice-based encryption scheme and has undergone decades of analysis. Despite this impressive pedigree, several factors worked against its selection as the primary standard:

**Complex key generation.** NTRU key generation requires finding a polynomial f in the ring such that f is invertible modulo both q and a smaller modulus p (typically 3). This invertibility requirement makes key generation more complex than Kyber's straightforward matrix-vector computation. While not a fundamental obstacle, it adds implementation complexity and requires additional validation.

**Decryption failure handling.** NTRU has non-negligible decryption failure probability for some parameter choices, requiring either larger parameters (increasing size) or careful failure management. The interaction between decryption failures and CCA security through the Fujisaki-Okamoto transform creates subtle implementation requirements.

**Weaker security reduction.** While NTRU has a long track record of empirical security, its formal security reductions are less tight than Kyber's Module-LWE foundation. The NTRU problem is a specific structured lattice problem rather than a general module problem, and the exact hardness relationship to standard lattice problems remains less clean.

**Similar performance.** NTRU offered no clear performance advantage over Kyber that might compensate for its added complexity. Given that the two schemes were roughly comparable in size and speed, Kyber's simpler implementation profile tipped the balance.

### Why Not Classic McEliece?

Classic McEliece, based on the original McEliece cryptosystem from 1978, has the most conservative security story of any candidate—nearly 50 years without a fundamental break. However, its selection as the primary standard was effectively impossible due to one factor:

**Enormous public keys.** Classic McEliece public keys range from approximately 261 KB (lowest security level) to over 1 MB (highest security level). These sizes are incompatible with most deployed protocols. A TLS handshake carrying a 261 KB public key would require fragmentation across multiple TCP packets, dramatically increasing latency. Certificate chains containing such keys would be impractical. Storage of millions of such keys (as in key transparency systems) would require orders of magnitude more infrastructure.

NIST acknowledged Classic McEliece's outstanding security properties and continued its evaluation for separate standardization, recognizing its value for applications where key size is acceptable (long-lived CA certificates, firmware signing systems, air-gapped environments).

### Why Not SABER?

SABER was Kyber's closest competitor—so close that NIST's decision was arguably the most marginal of the entire process. The schemes shared almost identical design philosophy (module lattice, CPA-secure core plus FO transform, similar parameter sizes). The key differences:

**Power-of-two modulus.** SABER used a modulus that was a power of two, enabling modular reduction via simple masking rather than explicit reduction modulo a prime. While this simplifies some operations, it prevented the use of NTT for polynomial multiplication (since NTT requires a prime modulus with appropriate roots of unity). SABER instead used Toom-Cook or schoolbook multiplication.

**Kyber's NTT advantage.** Kyber's NTT-based arithmetic provided a consistent performance edge, particularly on platforms with wide SIMD registers (AVX2, NEON). The NTT naturally maps to parallel butterfly operations that modern processors execute efficiently. SABER's polynomial multiplication, while not slow, could not leverage this parallelism as effectively.

**Avoiding redundancy.** NIST explicitly stated that standardizing both Kyber and SABER would provide minimal additional value—they share the same fundamental security assumption (module lattice problems) and similar parameter sizes. Choosing one was sufficient; choosing both would not meaningfully increase diversity.

## 10.5 Why Dilithium/ML-DSA Won

The signature competition saw three finalists from two mathematical families: CRYSTALS-Dilithium and FALCON (both lattice-based) and Rainbow (multivariate). Rainbow's break left the decision between two lattice approaches.

### Dilithium's Design and Advantages

CRYSTALS-Dilithium uses the "Fiat-Shamir with Aborts" paradigm: generate a commitment, hash it with the message to get a challenge, compute the response, and check whether the response would leak information about the secret key. If it would leak, abort and retry (rejection sampling). This design provides several advantages:

**No floating-point arithmetic.** Dilithium's operations are entirely integer-based: polynomial arithmetic over Z_q, sampling from uniform or bounded distributions, and comparison operations. This eliminates an entire class of potential implementation errors and side-channel vulnerabilities related to floating-point unit behavior.

**Predictable rejection count.** While Dilithium uses rejection sampling (aborting and retrying if the signature would leak), the expected number of repetitions is small (approximately 4-7 for standard parameters) and publicly visible (an observer can count how many attempts were needed). Since the iteration count is not secret, it does not constitute a timing side-channel.

**Straightforward constant-time implementation.** Every individual iteration of Dilithium's signing loop can be implemented in constant time with standard techniques. The only variable is the number of iterations, which leaks no information about the secret key. This makes secure implementation accessible to developers without deep side-channel expertise.

**Module-LWE foundation.** Like Kyber, Dilithium builds on Module-LWE (specifically, Module-SIS for the signature scheme), providing a shared mathematical foundation between NIST's KEM and signature standards. This conceptual consistency simplifies security analysis and may allow shared implementations of core arithmetic routines.

**Reasonable sizes.** At NIST Level 3, ML-DSA produces 3,293-byte signatures with 1,952-byte public keys. While significantly larger than classical ECDSA (64-byte signatures, 32-byte keys), these sizes are manageable for most applications. Certificate chains, signed software updates, and protocol messages can accommodate this overhead without fundamental redesign.

### Why FALCON Was Not Primary (But Still Selected)

FALCON (Fast Fourier Lattice-based Compact Signatures over NTRU) produces significantly smaller signatures than Dilithium—approximately 666 bytes at Level I versus Dilithium's 2,420 bytes. This size advantage is important for bandwidth-constrained applications. However, FALCON's implementation characteristics made it unsuitable as the primary standard:

**Gaussian sampling requirement.** FALCON requires sampling from a discrete Gaussian distribution over a lattice using a "fast Fourier sampling" procedure originally proposed by Gentry, Peikert, and Vaikuntanathan. This sampling procedure operates over floating-point numbers and is intricate to implement securely. Even small errors in floating-point precision can completely break security, and achieving constant-time behavior in floating-point code is notoriously difficult.

**Side-channel vulnerability surface.** The tree-based recursive Gaussian sampler in FALCON's signing algorithm operates on secret data in complex patterns, creating numerous potential side-channel leakage points. While constant-time implementations exist, they require exceptional care and sacrifice some of FALCON's performance advantages.

**Implementation complexity.** FALCON's specification is substantially more complex than Dilithium's. Correct implementation requires understanding NTRU lattice geometry, recursive sampling trees, and floating-point arithmetic for lattice reduction. NIST judged that the risk of widespread incorrect implementations outweighed FALCON's size benefits for a primary standard.

**Separate standardization track.** NIST selected FALCON for standardization as FN-DSA (FFT-based NTRU Digital Signature Algorithm) on a separate timeline, acknowledging that its compact signatures are valuable for applications that can invest in careful implementation (hardware security modules, specialized cryptographic libraries).

### Why Not Rainbow?

Rainbow's February 2022 break by Ward Beullens eliminated it from consideration entirely. The break demonstrated that Rainbow's "layered" oil-and-vinegar construction introduced algebraic structure that could be exploited to recover secret keys in practical time. Beyond the specific attack, the break highlighted risks inherent in multivariate schemes whose security depends on the difficulty of solving systems of multivariate quadratic equations—while the general MQ problem is NP-hard, the specific structured instances created by cryptographic constructions may be much easier.

The broader lesson was that decades of study do not guarantee security if the right attack technique has not yet been discovered. Oil-and-vinegar schemes were proposed in 1997, and Rainbow specifically in 2005, yet the fatal flaw was not identified until 2022.

## 10.6 The Role of SPHINCS+/SLH-DSA

### Selection Rationale

SPHINCS+ was the only non-lattice signature scheme selected for standardization in the initial set. Its selection was motivated by strategic diversity considerations rather than raw performance—in every performance metric, ML-DSA is superior. NIST's reasoning was explicit and deliberate:

**Minimal security assumptions.** SLH-DSA's security depends only on the properties of the underlying hash function (second-preimage resistance, pseudorandom function security, target collision resistance). These properties are extremely well-understood, having been studied for decades. If the hash function (SHA-256 or SHAKE-256) remains secure, SLH-DSA remains secure regardless of any developments in lattice cryptanalysis, quantum algorithms, or algebraic geometry.

**Insurance against lattice breakthroughs.** If an unexpected advance dramatically reduces the cost of solving Module-LWE or Module-SIS problems, both ML-KEM and ML-DSA could be compromised. SLH-DSA provides a "safety net"—organizations can deploy it alongside or instead of ML-DSA for high-value applications where long-term security is paramount.

**Proven theoretical lineage.** Hash-based signatures have the strongest theoretical foundation of any signature primitive. Lamport signatures (1979) demonstrated that one-time signatures could be built from any one-way function. Merkle trees (1979) extended this to many-time signatures. The line of development through XMSS and SPHINCS to SPHINCS+ represents a mature, deeply analyzed construction pattern with no fundamental surprises remaining.

### Performance Trade-offs

SLH-DSA's conservative design comes at a significant performance cost:

**Large signatures.** SLH-DSA signatures range from approximately 7,856 bytes (fastest parameter sets) to 49,856 bytes (smallest parameter sets), compared to ML-DSA's 2,420-3,293 bytes. This is a direct consequence of the Merkle tree structure—the signature must include an authentication path through the tree.

**Slow signing.** Signing operations require traversing and computing multiple hash trees, taking milliseconds rather than microseconds. The SLH-DSA-SHAKE-128f ("fast") parameter set takes approximately 5 ms to sign, while SLH-DSA-SHAKE-128s ("small") takes approximately 100 ms but produces smaller signatures.

**Fast verification.** Verification is relatively fast (approximately 1 ms for the fast parameter sets) because it only recomputes hashes along the authentication path rather than the full tree.

### Appropriate Use Cases

Given these trade-offs, SLH-DSA is best suited for applications where signing is infrequent and security requirements are extreme: root certificate authority certificates (signed once, verified millions of times), code signing for critical infrastructure firmware, long-lived document signatures, and applications where a future lattice break would be catastrophic.

## 10.7 Naming Conventions

### The Renaming Decision

When NIST published final standards, all algorithms were renamed from their competition names to standardized designations following a consistent naming scheme:

| Competition Name | Standard Name | Standard Number | Naming Logic |
|-----------------|--------------|----------------|--------------|
| CRYSTALS-Kyber | ML-KEM | FIPS 203 | Module-Lattice Key Encapsulation Mechanism |
| CRYSTALS-Dilithium | ML-DSA | FIPS 204 | Module-Lattice Digital Signature Algorithm |
| SPHINCS+ | SLH-DSA | FIPS 205 | Stateless Hash-based Digital Signature Algorithm |
| FALCON | FN-DSA | (Pending) | FFT over NTRU-lattice Digital Signature Algorithm |

### Rationale for Renaming

NIST's decision to rename algorithms was controversial among some in the community but followed sound institutional logic:

**Standardization convention.** Previous NIST standards similarly renamed algorithms: Rijndael became AES, Keccak became SHA-3. Standards documents have their own naming conventions reflecting the standardized function rather than the competition entry.

**Descriptive naming.** The new names encode the mathematical foundation ("ML" for Module-Lattice, "SLH" for Stateless Hash-based) and the cryptographic function ("KEM" for Key Encapsulation, "DSA" for Digital Signature Algorithm). This helps implementers and procurement officers understand what they are deploying without deep mathematical background.

**Intellectual property neutrality.** Competition names often reflected team identities or references (CRYSTALS, Dilithium from Star Trek, Kyber crystals from Star Wars). Standard names should be neutral and generic, reflecting function rather than origin.

**Version distinction.** The standardized algorithms differ slightly from their competition versions (minor parameter tweaks, specification clarifications). Distinct names prevent confusion about which version is being referenced in implementations, compliance documents, and protocol specifications.

### Practical Implications

The dual naming creates some confusion during the transition period. Literature from before 2024 references "Kyber" and "Dilithium," while standards-compliant implementations reference "ML-KEM" and "ML-DSA." Practitioners should understand both names and recognize that the standardized versions are the authoritative specifications for new implementations.

## 10.8 Ongoing Standardization Activities

### HQC Standardization

In 2024, NIST announced the selection of HQC (Hamming Quasi-Cyclic) as an additional KEM standard. This decision reflects NIST's commitment to algorithmic diversity:

**Code-based security.** HQC's security relies on the difficulty of decoding random quasi-cyclic codes, a problem from coding theory with different mathematical foundations than lattice problems. If Module-LWE proves unexpectedly easier than believed (due to new algebraic techniques or quantum algorithms), HQC provides a fallback from an entirely different hardness assumption.

**Quasi-cyclic structure.** HQC uses quasi-cyclic codes for efficiency—the underlying matrix has a structure that enables compact representation and efficient computation. This structured approach is analogous to how ML-KEM uses module lattices rather than unstructured lattices for efficiency, accepting somewhat less security confidence in exchange for practical deployability.

**Parameter sizes.** HQC has somewhat larger parameters than ML-KEM: approximately 2,249 bytes for the public key and 4,481 bytes for the ciphertext at 128-bit security (compared to ML-KEM-768's 1,184 and 1,088 bytes). This size premium is the cost of code-based diversity.

**Standardization timeline.** HQC standardization is proceeding on a separate timeline from the initial three FIPS standards, with draft standards expected to follow the same public comment process.

### Additional Signature Competition

NIST's call for additional digital signature schemes, issued in 2022, seeks to address gaps in the initial standardization:

**Short signatures.** ML-DSA's signatures (2,420-4,627 bytes) are large compared to classical ECDSA (64 bytes). Applications transmitting many signatures (certificate chains, blockchain) need shorter alternatives. Candidates like MAYO and UOV (Unbalanced Oil-and-Vinegar, in a new less-layered configuration) offer shorter signatures from multivariate assumptions.

**Short public keys.** Some applications (constrained storage, key transparency) need compact public keys more than compact signatures. Different trade-off points between key size and signature size serve different deployment needs.

**Novel properties.** Some candidates offer properties beyond basic signing—signature aggregation (combining multiple signatures into one), threshold signing (distributed key generation and signing), or unique algebraic structures that enable advanced protocols.

**Current candidates under evaluation include:**

- **UOV (Unbalanced Oil-and-Vinegar):** Multivariate scheme with very short signatures (~100 bytes) but large public keys (~67 KB). Unlike Rainbow, UOV has a simpler single-layer structure that has resisted cryptanalysis for over 25 years.
- **MAYO:** A compressed variant of UOV that achieves shorter public keys while maintaining short signatures. Uses "whipping" technique to reduce key sizes.
- **SQISign:** Based on isogenies between supersingular elliptic curves, offering the smallest combined key+signature size of any candidate. However, signing is computationally expensive and the security analysis of the underlying problem (computing isogenies without auxiliary points) is less mature.
- **CROSS:** Code-based signature scheme using the syndrome decoding problem. Offers medium-sized signatures with conservative security assumptions.
- **LESS, MEDS, HAWK, SquirrelS, and others:** Representing diverse mathematical approaches including group actions, matrix equivalence, and structured lattice variants.

### Stateful Hash-Based Signatures

Before the main PQC competition concluded, NIST standardized two stateful hash-based signature schemes in SP 800-208:

**XMSS (eXtended Merkle Signature Scheme, RFC 8391).** A stateful scheme based on Merkle trees where each key pair can produce a fixed number of signatures. The signer must maintain state (a counter of which one-time keys have been used). Reusing a one-time key catastrophically breaks security.

**LMS (Leighton-Micali Signature, RFC 8554).** Similar to XMSS with different design choices. Also stateful with the same one-time key reuse caveat.

These schemes are recommended for specific use cases where state management is feasible: firmware signing (small number of signatures from a controlled signing server), certificate authority root certificates (signed very infrequently), and systems with hardware-enforced monotonic counters to prevent state reuse.

The statelessness of SLH-DSA (which uses randomized "few-time" keys within a hyper-tree structure) makes it applicable to general-purpose signing where state management is impractical.

## 10.9 International Standardization

### ISO/IEC

The International Organization for Standardization's Joint Technical Committee 1 (JTC 1), Subcommittee 27 (Information Security) has been working to incorporate post-quantum algorithms into international standards:

**ISO/IEC 14888-4.** This forthcoming part of the digital signature standard will include post-quantum signature schemes, expected to align closely with NIST's selections (ML-DSA and SLH-DSA).

**ISO/IEC 18033-2.** The public-key encryption standard is being updated to include post-quantum KEMs, expected to incorporate ML-KEM.

**Timeline alignment.** ISO's standards process is generally slower than NIST's, involving broader international consensus-building. ISO standards are expected to reference or align with the FIPS specifications, potentially with minor notational differences but identical algorithms.

**Independent evaluation.** While ISO generally defers to NIST's security evaluation for PQC algorithms, the ISO process provides an additional layer of review, particularly for implementation guidance and interoperability requirements.

### ETSI (European Telecommunications Standards Institute)

ETSI's Quantum-Safe Cryptography (QSC) working group has been particularly active in bridging the gap between cryptographic standards and deployment reality:

**Migration guidance (TR 103 619).** ETSI published comprehensive technical reports on migrating existing systems to quantum-safe cryptography, covering TLS, IPsec, IKEv2, and other protocols. These reports provide practical deployment advice beyond what algorithm standards themselves contain.

**Hybrid mechanisms (TS 103 744).** ETSI standards for combining classical and post-quantum algorithms address the transition period where confidence in new algorithms is still building. These specify how to combine ECDH with ML-KEM, how to handle dual signatures, and how hybrid schemes interact with existing protocol infrastructure.

**Quantum Key Distribution integration.** Uniquely among standards bodies, ETSI also addresses the integration of quantum key distribution (QKD) with post-quantum cryptographic schemes, relevant for organizations pursuing defense-in-depth with both quantum-information-theoretic and computational security.

### IETF (Internet Engineering Task Force)

The IETF is responsible for integrating post-quantum algorithms into internet protocols:

**TLS integration.** RFC 9370 and subsequent drafts specify how ML-KEM integrates into TLS 1.3 key exchange, including hybrid mechanisms combining ML-KEM-768 with X25519. These drafts address practical concerns: how to handle the larger key exchange messages, how to negotiate PQC support, and how to maintain backward compatibility.

**Certificate formats.** Internet-Drafts specify how post-quantum public keys and signatures fit into X.509 certificates and the Web PKI. Challenges include certificate size impacts on TLS handshakes, the need for intermediate caching strategies, and certificate transparency log implications.

**IPsec/IKEv2.** Drafts extend the Internet Key Exchange protocol with post-quantum key exchange, addressing both initial key establishment and rekey operations.

**SSH.** Post-quantum key exchange methods for Secure Shell, enabling quantum-resistant server authentication and session key establishment.

**S/MIME and OpenPGP.** Drafts for post-quantum email security address the unique challenges of asynchronous communication: messages encrypted today might be stored and decrypted decades hence, making post-quantum protection particularly urgent for email.

### BSI (German Federal Office for Information Security)

Germany's BSI has taken a notably independent approach to post-quantum recommendations:

**FrodoKEM endorsement.** BSI has explicitly recommended FrodoKEM (based on unstructured LWE, without ring or module structure) as a conservative option alongside NIST's structured selections. BSI's reasoning is that unstructured LWE eliminates any risk from attacks exploiting algebraic structure, providing a higher confidence floor at the cost of larger parameters and slower performance.

**Technical guidelines (TR-02102).** BSI's cryptographic recommendation documents include post-quantum algorithms with specific guidance for German government and critical infrastructure. These sometimes differ from NIST in parameter recommendations or transition timelines.

**Hybrid requirement.** BSI mandates hybrid modes (combining classical and post-quantum) for government communications during the transition period, reflecting a conservative approach that maintains security even if PQC algorithms have undiscovered weaknesses.

### ANSSI (French National Cybersecurity Agency)

France's ANSSI has adopted the most conservative stance among major national agencies:

**Hybrid-only requirement.** ANSSI requires that post-quantum algorithms be deployed exclusively in hybrid mode—combining them with classical algorithms (ECDH, ECDSA) that have decades of security track record. This policy reflects the position that confidence in new algorithms builds gradually and that premature standalone deployment risks catastrophic failure if PQC algorithms prove weaker than expected.

**Extended timeline.** ANSSI's migration guidance specifies a longer transition period than NIST's, with hybrid modes remaining mandatory for an extended period. Standalone post-quantum deployment is envisioned only after additional years of cryptanalytic study post-standardization.

**Algorithm-agnostic approach.** Rather than endorsing specific algorithms, ANSSI's guidance focuses on security levels and hybrid construction principles. This approach provides flexibility to adopt whatever algorithms prove most robust over time.

### Other National and Regional Efforts

Beyond the major bodies listed above, numerous other organizations have published PQC guidance or initiated their own evaluations:

**CCCS (Canadian Centre for Cyber Security).** Aligned closely with NIST selections, recommending immediate adoption of FIPS 203/204/205 for Canadian government systems. Published guidance on hybrid deployment and migration planning timelines.

**AISA/ASD (Australia).** The Australian Signals Directorate has endorsed NIST algorithms for Australian government use, with particular emphasis on the urgency of protecting classified information against "harvest now, decrypt later" attacks.

**KISA (Korea).** South Korea's Internet & Security Agency has been evaluating post-quantum algorithms for national infrastructure, with particular focus on performance on domestic hardware platforms and integration with Korean cryptographic standards (ARIA, LEA).

**CRYPTREC (Japan).** Japan's cryptographic evaluation committee is assessing NIST selections for inclusion in Japanese government recommendations, conducting independent performance evaluations on Japanese computing platforms.

### Alignment and Divergence

While international bodies are broadly aligned—all recognize NIST's selections as the primary reference point—meaningful differences exist in:

- **Transition aggressiveness:** NIST encourages immediate deployment; ANSSI counsels patience
- **Hybrid requirements:** Some mandate hybrid, others merely recommend it
- **Algorithm diversity:** BSI endorses unstructured options (FrodoKEM) that NIST did not standardize
- **Timeline:** Varying urgency about "harvest now, decrypt later" threats
- **Compliance mechanisms:** Some jurisdictions mandate adoption by specific dates; others rely on voluntary adoption

These differences reflect legitimate policy trade-offs rather than technical disagreements. Organizations operating internationally must navigate this landscape, typically defaulting to the most conservative position that satisfies all relevant jurisdictions. In practice, this often means: deploying NIST-standardized algorithms (for broadest interoperability), in hybrid mode (satisfying ANSSI and BSI requirements), with a migration timeline that meets the most aggressive applicable deadline.

## 10.10 Lessons Learned

The eight-year NIST PQC standardization process offers profound lessons for cryptographic engineering, standards development, and technology governance. These lessons are relevant not only for future cryptographic standards but for any large-scale technology selection process where long-term security implications are at stake.

### Open Competitions Discover Fatal Flaws

The complete breaks of Rainbow and SIKE—both during the final round, after years of public analysis—powerfully validate the open competition model. Had these schemes been standardized through a closed process with limited analysis time, they could have been deployed worldwide before their vulnerabilities were discovered. The open process created incentives for the world's best cryptanalysts to scrutinize candidates, and they delivered crucial results.

The timing of these breaks is instructive. Rainbow was studied since 2005 and SIKE since 2011, yet their fatal flaws were not discovered until 2022. This demonstrates that even sustained public attention does not guarantee timely discovery of vulnerabilities—the eight-year competition was barely long enough.

The incentive structure of open competitions deserves particular attention. By publicly listing candidate algorithms and inviting analysis, NIST created a situation where breaking a prominent candidate would bring academic recognition and career advancement. This aligned individual researcher incentives with collective security goals. In contrast, proprietary or classified algorithms benefit from no such alignment—their security depends on the competence and diligence of a limited internal review team.

### Diversity Is Not Optional

NIST's explicit decision to standardize SLH-DSA alongside ML-DSA—despite SLH-DSA's inferior performance in every metric—reflects hard-won wisdom about cryptographic monocultures. If every deployed system depends on the same mathematical assumption (Module-LWE), then a single unexpected advance could compromise global infrastructure simultaneously. Diversity of mathematical foundations provides systemic resilience even if individual alternatives are less efficient.

This lesson extends beyond algorithm selection to deployment strategy: organizations should consider which of their systems can tolerate the performance overhead of hash-based signatures, and deploy SLH-DSA there as insurance.

### Implementation Complexity Is a First-Order Concern

NIST's preference for Dilithium over FALCON as the primary signature standard—despite FALCON's smaller signatures—reflects the reality that most cryptographic code is written by developers who are not cryptographers. A scheme that is simple to implement correctly provides better real-world security than one that is theoretically superior but frequently implemented with subtle bugs.

The catastrophic consequences of implementation errors in cryptography (total security failure rather than mere performance degradation) make simplicity a security property, not merely an engineering convenience.

### Patience Enables Better Outcomes

The eight-year timeline (2016-2024) was longer than the AES competition (4 years) or SHA-3 competition (5 years), and it was barely sufficient. The Rainbow break in year 6 and the SIKE break in year 6 demonstrate that even extended timelines cannot guarantee all flaws are found—but shorter timelines would certainly have missed them.

The lesson is that cryptographic standardization should not be rushed, even under the pressure of quantum computing advances. The "harvest now, decrypt later" threat creates urgency, but deploying a broken standard is worse than deploying a good standard a year or two later.

### Migration Must Begin Before Standards Are Final

Organizations that waited until August 2024 (final standards publication) to begin migration planning are years behind those that started with the July 2022 selections or even earlier. The practical work of migrating cryptographic infrastructure—inventorying systems, testing compatibility, updating protocols, training staff, purchasing new hardware—takes years and should begin as soon as algorithm selections are reasonably stable, not when standards documents receive their final stamp.

### The Quantum Threat Model Creates Unique Pressure

Unlike previous cryptographic transitions (DES to AES, SHA-1 to SHA-2), the post-quantum transition is driven by a threat that does not yet fully exist. Large-scale quantum computers capable of running Shor's algorithm on production key sizes have not been demonstrated. This creates an unusual dynamic: the urgency comes from the combination of uncertain threat timelines and the decades-long deployment cycles of cryptographic infrastructure.

The "harvest now, decrypt later" attack—where adversaries capture encrypted communications today for future quantum decryption—means that data requiring long-term confidentiality (decades) is already at risk even though quantum computers cannot yet break the encryption. This is not speculative: intelligence agencies are widely believed to be stockpiling encrypted data.

### Standards Are Beginnings, Not Endings

The publication of FIPS 203, 204, and 205 marks the beginning of post-quantum deployment, not the end of post-quantum work. Continued cryptanalysis of the standardized algorithms, development of efficient implementations across platforms, integration into protocols and applications, migration of existing systems, and standardization of additional algorithms all continue indefinitely.

The cryptographic community must maintain vigilant analysis of ML-KEM and ML-DSA parameters even after standardization. If new attack techniques significantly reduce security margins, parameter updates or even algorithm replacements might be needed. The modularity of modern protocols (algorithm agility) supports this ongoing evolution.

### The Importance of Ecosystem Readiness

A standard is only as useful as the ecosystem that implements it. The NIST PQC effort benefited enormously from parallel efforts to prepare the implementation ecosystem: the PQClean project provided clean reference implementations, the PQM4 project benchmarked on embedded platforms, major cryptographic libraries (OpenSSL, BoringSSL, wolfSSL) developed implementations alongside the competition, and protocol working groups (IETF) drafted integration specifications before final standards were published. This ecosystem co-development meant that practical deployment could begin almost immediately upon standard publication, rather than requiring years of additional implementation work.

### Balancing Conservatism and Practicality

The tension between security conservatism (preferring the safest possible algorithms regardless of performance) and deployment practicality (needing algorithms efficient enough for real-world use) was a constant theme. NIST's resolution—standardizing both the efficient-but-newer lattice schemes and the conservative-but-slower hash-based scheme—represents a thoughtful compromise that gives different communities appropriate options.

BSI's additional endorsement of FrodoKEM (unstructured LWE, even more conservative but significantly larger) and ANSSI's hybrid-only mandate represent alternative positions on this spectrum. No single point is "correct"—the appropriate choice depends on threat model, performance constraints, and institutional risk tolerance. The existence of multiple options at different conservatism levels is a feature, not a deficiency, of the standardization landscape.

### Communication and Transparency Build Trust

Throughout the eight-year process, NIST maintained remarkable transparency: publishing detailed evaluation reports explaining selection rationale, holding public workshops where community members could question decisions, and explicitly acknowledging uncertainties and trade-offs. This transparency built trust in the process and the resulting standards, even among those who might have preferred different selections.

The contrast with earlier, less transparent standardization efforts (the DES controversy around S-box design, concerns about Dual_EC_DRBG) underscores how important procedural legitimacy is for cryptographic standards that the world depends on. Organizations are more willing to adopt standards they trust were selected on merit through a fair process.

## 10.11 Key Takeaways

- NIST's open competition model, refined over AES and SHA-3, proved effective at its most ambitious scale: evaluating 69 submissions across multiple mathematical families over eight years
- Three primary standards emerged: ML-KEM (FIPS 203) for key encapsulation, ML-DSA (FIPS 204) for digital signatures, and SLH-DSA (FIPS 205) for hash-based signature diversity
- The breaks of Rainbow and SIKE during Round 3 validated both the extended timeline and the multi-foundation diversity strategy
- Selection criteria balanced security confidence, performance, and implementation simplicity—no single dimension dominated
- Kyber won over NTRU and SABER primarily due to NTT efficiency, implementation simplicity, and avoidance of redundancy among lattice KEMs
- Dilithium won over FALCON primarily due to implementation simplicity and avoidance of floating-point Gaussian sampling
- SPHINCS+/SLH-DSA was selected explicitly as insurance against potential lattice cryptanalysis breakthroughs
- Additional standardization continues: HQC for code-based KEM diversity, additional signatures for compact alternatives, and FN-DSA for applications needing small signatures
- International bodies (ISO, ETSI, IETF, BSI, ANSSI) are aligned on NIST algorithms but differ on transition policies, hybrid requirements, and timelines
- Organizations should be deploying post-quantum cryptography now, not waiting for additional standards or quantum computing milestones

---

*Next: [Chapter 11 — FIPS 203: ML-KEM](./11-fips-203-ml-kem.md)*
