> **Author's note:** Appendix D-RESOURCES is reference material—use it beside the narrative chapters, not instead of them.

# Appendix D: Further Reading and Resources

This appendix provides a curated guide to the literature, standards, communities, and educational resources relevant to post-quantum cryptography. The field moves rapidly; while foundational references remain stable, readers should verify that they are consulting the most recent editions and latest versions of standards documents.

## D.1 Foundational Textbooks

### General Cryptography

**Katz, J. & Lindell, Y.** *Introduction to Modern Cryptography* (3rd edition, 2020). CRC Press. The standard graduate-level introduction to cryptography, covering both theoretical foundations and practical constructions. The third edition includes introductory material on lattice-based cryptography and post-quantum considerations. Essential background for understanding security proofs, definitions (IND-CPA, IND-CCA2, EUF-CMA), and the reduction-based paradigm that underpins all PQC security analysis. The treatment of public-key encryption, digital signatures, and hash functions provides the framework into which PQC algorithms fit.

**Goldreich, O.** *Foundations of Cryptography* (Volumes 1 & 2, 2001/2004). Cambridge University Press. The most rigorous theoretical treatment of cryptographic primitives and protocols. Volume 1 covers basic tools (one-way functions, pseudorandomness, zero-knowledge proofs); Volume 2 covers applications (encryption, signatures, secure computation). While predating PQC standardization, the foundational definitions and proof techniques are directly applicable. Particularly valuable for understanding simulation-based security, which appears in FO transform proofs.

**Boneh, D. & Shoup, V.** *A Graduate Course in Applied Cryptography* (continuously updated). Available free online at https://toc.cryptobook.us/. Excellent coverage of modern cryptographic constructions with detailed security proofs. Includes chapters on lattice-based cryptography (LWE, Ring-LWE, SIS), hash-based signatures, and the random oracle model. The online format enables regular updates incorporating PQC developments. Particularly strong on authenticated encryption, key exchange protocols, and the TLS handshake — all relevant to PQC deployment.

**Smart, N.P.** *Cryptography Made Simple* (2016). Springer. An accessible introduction targeting practitioners who need working knowledge without full mathematical rigor. Covers classical and public-key cryptography, protocols, and implementations. Useful as a bridge for engineers approaching PQC from a practical background.

**Stinson, D.R. & Paterson, M.** *Cryptography: Theory and Practice* (4th edition, 2018). CRC Press. Balances theory and practice with extensive examples. Good treatment of information-theoretic security, block ciphers, and protocols. The coverage of coding theory provides relevant background for code-based PQC.

### Post-Quantum Cryptography

**Bernstein, D.J., Buchmann, J., & Dahmen, E. (Eds.)** *Post-Quantum Cryptography* (2009). Springer. The foundational reference for the PQC field, with dedicated chapters on each algorithm family: hash-based signatures (Buchmann, Dahmen, Szydlo), code-based cryptography (Overbeck, Sendrier), lattice-based cryptography (Micciancio, Regev), multivariate cryptography (Wolf, Preneel), and quantum computing background (Bernstein). While predating NIST standardization, the mathematical foundations and attack analyses remain highly relevant. Each chapter was written by leading researchers in the respective area.

**Galbraith, S.D.** *Mathematics of Public Key Cryptography* (2012). Cambridge University Press. Exceptional mathematical treatment covering number theory, elliptic curves, pairings, and lattices. The lattice chapters (13-16) provide thorough coverage of LLL, BKZ, and the complexity of lattice problems. The elliptic curve chapters (chapters 4-12) provide essential background for understanding isogeny-based cryptography. Available free online from the author's website.

**Peikert, C.** *A Decade of Lattice Cryptography* (2016). Foundations and Trends in Theoretical Computer Science. This monograph provides the most accessible yet rigorous introduction to lattice-based cryptography. Covers the LWE problem, Ring-LWE, worst-case to average-case reductions, and lattice-based constructions (encryption, signatures, FHE). Essential reading for understanding the theoretical foundations of ML-KEM and ML-DSA.

**Bernstein, D.J. & Lange, T. (Eds.)** *Post-Quantum Cryptography — PQCrypto Conference Proceedings*. Springer LNCS. The proceedings of the biennial PQCrypto conference document the evolution of the field. Key volumes include PQCrypto 2006 (inaugural), 2014 (pre-NIST), 2017-2024 (during NIST process). These provide archival snapshots of the state of the art at each point in time.

### Quantum Computing

**Nielsen, M.A. & Chuang, I.L.** *Quantum Computation and Quantum Information* (10th Anniversary Edition, 2010). Cambridge University Press. The definitive textbook on quantum computing, universally known as "Mike and Ike." Comprehensive coverage from quantum mechanics basics through quantum algorithms, quantum error correction, and quantum information theory. Chapter 5 (quantum Fourier transform and applications) explains Shor's algorithm in detail. Chapter 6 covers Grover's search algorithm. Essential for understanding the quantum threat model that motivates PQC.

**Mermin, N.D.** *Quantum Computer Science: An Introduction* (2007). Cambridge University Press. A more accessible introduction targeting computer scientists without physics background. Explains quantum computation using the circuit model without requiring knowledge of Hilbert spaces or quantum mechanics formalism. Excellent for understanding Shor's and Grover's algorithms at a conceptual level.

**Yanofsky, N.S. & Mannucci, M.A.** *Quantum Computing for Computer Scientists* (2008). Cambridge University Press. Bridges the gap between computer science and physics with a linear algebra approach. Provides necessary mathematical background (complex vector spaces, tensor products, unitary operators) before covering quantum algorithms.

**de Wolf, R.** *Quantum Computing: Lecture Notes* (continuously updated). Available from CWI Amsterdam. Concise lecture notes covering quantum algorithms relevant to cryptanalysis, including the hidden subgroup problem framework that generalizes Shor's algorithm. Particularly relevant for understanding which algebraic structures quantum computers can exploit and which they cannot.

**Childs, A.** *Lecture Notes on Quantum Algorithms* (continuously updated). University of Maryland. Detailed treatment of quantum algorithms beyond Shor and Grover, including quantum walks, amplitude amplification, and quantum simulation. Relevant for understanding the full scope of quantum algorithmic techniques applicable to cryptanalysis.

### Lattice-Based Cryptography

**Micciancio, D. & Goldwasser, S.** *Complexity of Lattice Problems: A Cryptographic Perspective* (2002). Springer. detailed treatment of the computational complexity of lattice problems (SVP, CVP, GapSVP, SIVP). Proves NP-hardness results, average-case/worst-case relationships, and establishes the theoretical foundation for lattice-based cryptography. While some results have been improved since publication, this remains the definitive reference for lattice problem complexity.

**Micciancio, D. & Regev, O.** "Lattice-based Cryptography" (2009). In *Post-Quantum Cryptography* (Bernstein et al., Eds.). The authoritative survey chapter covering LWE, SIS, one-way functions, collision-resistant hash functions, public-key encryption, and identity-based encryption from lattices. Includes the proof of Regev's reduction from GapSVP to LWE.

**Regev, O.** "The Learning with Errors Problem" (invited survey, 2010). CCC 2010. A survey by the originator of LWE covering the problem's history, known reductions, and applications. Accessible introduction to the classical and quantum reductions that establish LWE's worst-case hardness.

**Lyubashevsky, V., Peikert, C., & Regev, O.** "On Ideal Lattices and Learning with Errors over Rings" (2010/2013). EUROCRYPT 2010, Journal of the ACM 2013. Introduces Ring-LWE and proves its hardness based on worst-case ideal lattice problems. This paper provides the theoretical foundation for efficient lattice-based constructions including the ancestor of ML-KEM.

### Coding Theory

**MacWilliams, F.J. & Sloane, N.J.A.** *The Theory of Error-Correcting Codes* (1977). North-Holland. The classic layered reference for algebraic coding theory. Covers linear codes, cyclic codes, BCH codes, Reed-Solomon codes, Goppa codes, and bounds on code parameters. The chapters on Goppa codes are directly relevant to understanding the McEliece cryptosystem.

**Huffman, W.C. & Pless, V.** *Fundamentals of Error-Correcting Codes* (2003). Cambridge University Press. A more modern treatment of coding theory with updated notation and additional topics. Good coverage of decoding algorithms, code constructions, and combinatorial properties relevant to code-based cryptography.

**Sendrier, N.** "Code-Based Cryptography: State of the Art and Perspectives" (2017). IEEE Security & Privacy. A survey of code-based cryptography covering McEliece, Niederreiter, and modern proposals. Discusses key reduction techniques, structural attacks, and the code-based KEM paradigm that HQC follows.

**Weger, V., Gassner, N., & Rosenthal, J.** "A Survey on Code-Based Cryptography" (2024). Advances in Mathematics of Communications. A comprehensive modern survey covering all code-based PQC proposals including HQC, BIKE, and Classic McEliece, along with the information set decoding attacks that determine their concrete security parameters.

### Isogeny-Based Cryptography

**De Feo, L.** "Mathematics of Isogeny Based Cryptography" (2017). Lecture notes from Arithmetic of Finite Fields summer school. The most accessible introduction to the mathematics of isogeny-based cryptography, covering supersingular curves, isogeny graphs, endomorphism rings, and the computational problems underlying SIDH and CSIDH.

**De Feo, L., Kohel, D., Leroux, A., Petit, C., & Wesolowski, B.** "SQISign: Compact Post-Quantum Signatures from Quaternions and Isogenies" (2020). ASIACRYPT 2020. Introduces SQISign, the leading isogeny-based signature scheme that survived the SIDH attacks. Security is based on the endomorphism ring problem for supersingular curves over F_p.

**Galbraith, S.D. & Vercauteren, F.** "Computational Problems in Supersingular Elliptic Curve Isogenies" (2018). Quantum Information Processing. Survey of computational problems in isogeny cryptography: path-finding in isogeny graphs, endomorphism ring computation, and the relationship between these problems.

### Multivariate Cryptography

**Ding, J. & Schmidt, D.** "Rainbow, a New Multivariable Polynomial Signature Scheme" (2005). ACNS 2005. The original Rainbow paper describing the layered Oil-and-Vinegar construction that was a NIST PQC finalist before being broken by Beullens. Important for understanding the design space of multivariate signatures.

**Kipnis, A., Patarin, J., & Goubin, L.** "Unbalanced Oil and Vinegar Signature Schemes" (1999). EUROCRYPT 1999. Introduces the UOV construction that remains unbroken and is under NIST consideration for additional standardization. The fundamental trapdoor is the partition of variables into "oil" (quadratic) and "vinegar" (linear) roles.

**Beullens, W.** "MAYO: Practical Post-Quantum Signatures from Oil-and-Vinegar Maps" (2021). Selected Areas in Cryptography 2021. Introduces MAYO, a UOV variant with significantly smaller public keys. Demonstrates that multivariate schemes can be made practical through careful parameter and structure choices.

### Hash-Based Signatures

**Buchmann, J., Dahmen, E., & Hülsing, A.** "XMSS – A Practical Forward Secure Signature Scheme Based on Minimal Security Assumptions" (2011). PQCrypto 2011. Introduces XMSS with its multi-tree extension and forward security properties. Provides the construction that became RFC 8391 and NIST SP 800-208.

**Bernstein, D.J., Hülsing, A., Kölbl, S., Niederhagen, R., Rijneveld, J., & Schwabe, P.** "The SPHINCS+ Signature Framework" (2019). CCS 2019. Describes the SPHINCS+ construction that became SLH-DSA (FIPS 205). Covers the hypertree structure, FORS few-time signatures, parameter selection methodology, and security analysis in the (quantum) random oracle model.

## D.2 Key Research Papers

### Foundational Papers

**Shor, P.W. (1994/1997)** "Algorithms for Quantum Computation: Discrete Logarithms and Factoring." Proceedings of the 35th Annual Symposium on Foundations of Computer Science (FOCS), 1994. Full journal version: SIAM Journal on Computing, 26(5):1484-1509, 1997. This paper demonstrates polynomial-time quantum algorithms for integer factoring and discrete logarithms, breaking RSA, Diffie-Hellman, and elliptic curve cryptography. The key insight is using the quantum Fourier transform to efficiently find the period of modular exponentiation. This paper catalyzed the entire field of post-quantum cryptography.

**Grover, L.K. (1996)** "A Fast Quantum Mechanical Algorithm for Database Search." Proceedings of the 28th Annual ACM Symposium on Theory of Computing (STOC), 1996. Provides a quadratic speedup for unstructured search: finding a marked item among N possibilities in O(√N) quantum queries. For cryptography, this means symmetric key search, hash preimage finding, and other brute-force attacks gain a quadratic quantum speedup, effectively halving security levels.

**Regev, O. (2005/2009)** "On Lattices, Learning with Errors, Random Linear Codes, and Cryptography." Proceedings of STOC 2005. Journal version: Journal of the ACM, 56(6), 2009. Introduces the Learning with Errors problem and proves a quantum reduction from worst-case lattice problems (GapSVP and SIVP with polynomial approximation factors) to the average-case hardness of LWE. This paper establishes the theoretical foundation for the entire family of LWE-based cryptosystems, including ML-KEM.

**McEliece, R.J. (1978)** "A Public-Key Cryptosystem Based on Algebraic Coding Theory." DSN Progress Report 42-44, Jet Propulsion Laboratory, 1978. Proposes the first code-based public-key cryptosystem: the public key is a disguised generator matrix for a binary Goppa code, encryption adds a random error vector, and decryption uses the secret Goppa decoding algorithm. Remarkable for its nearly 50-year resistance to cryptanalysis, though large key sizes have limited practical adoption.

**Merkle, R. (1979/1989)** "Secrecy, Authentication, and Public Key Systems." Stanford University PhD thesis, 1979. "A Certified Digital Signature." CRYPTO 1989. Introduces the concept of hash-based signatures using binary hash trees for one-time signature authentication. The Merkle tree construction enables signing 2^h messages using a single public key (the tree root), with authentication paths of length h. This idea underpins LMS, XMSS, and SLH-DSA.

**Ajtai, M. (1996)** "Generating Hard Instances of Lattice Problems." Proceedings of STOC 1996. Proves the foundational worst-case to average-case reduction for lattice-based cryptography: if worst-case approximate SVP/SIVP is hard, then the SIS problem is hard on average. This provides the theoretical justification for basing cryptography on random lattice instances.

**Lyubashevsky, V. (2009/2012)** "Fiat-Shamir with Aborts: Applications to Lattice and Factoring-Based Signatures." ASIACRYPT 2009. Journal version: 2012. Introduces the rejection sampling technique for lattice-based signatures: the signer repeatedly samples a masking vector and discards outputs correlated with the secret key. This technique is the foundation of ML-DSA's signing algorithm and resolves the key leakage problem in lattice-based signatures.

**Hoffstein, J., Pipher, J., & Silverman, J.H. (1998)** "NTRU: A Ring-Based Public Key Cryptosystem." Proceedings of ANTS III, 1998. Introduces the NTRU public-key cryptosystem based on short vectors in polynomial rings. NTRU's ring structure provides compact keys and fast operations. While NTRU encryption was not selected for NIST standardization, NTRU lattices form the trapdoor structure used in FN-DSA.

### NIST Standardized Algorithm Papers

**Avanzi, R., Bos, J., Ducas, L., Kiltz, E., Lepoint, T., Lyubashevsky, V., Schanck, J.M., Schwabe, P., Seiler, G., & Stehlé, D.** "CRYSTALS-Kyber: Algorithm Specifications and Supporting Documentation" (versions 1.0-3.02, 2017-2021). NIST PQC submission. Describes the design of what became ML-KEM (FIPS 203): the Module-LWE-based encryption scheme, its CPA security, the FO transform for CCA security, parameter selection methodology, implementation guidance, and security analysis. The companion paper "CRYSTALS-Kyber: A CCA-Secure Module-Lattice-Based KEM" (IEEE EuroS&P 2018) provides the formal security proof.

**Ducas, L., Kiltz, E., Lepoint, T., Lyubashevsky, V., Schwabe, P., Seiler, G., & Stehlé, D.** "CRYSTALS-Dilithium: Algorithm Specifications and Supporting Documentation" (versions 1.0-3.1, 2017-2021). NIST PQC submission. Describes the design of what became ML-DSA (FIPS 204): the Module-LWE/SIS-based signature scheme using Fiat-Shamir with Aborts. Covers the rejection sampling mechanism, hint computation for reducing signature size, deterministic and randomized signing modes, and parameter selection for NIST security levels 2, 3, and 5.

**Aumasson, J.-P., Bernstein, D.J., Dobraunig, C., Eichlseder, M., Fluhrer, S., Gazdag, S.-L., Hülsing, A., Kampanakis, P., Kölbl, S., Lange, T., Lauridsen, M.M., Mendel, F., Niederhagen, R., Rechberger, C., Rijneveld, J., Schwabe, P., & Šramka, M.** "SPHINCS+: Submission to the NIST Post-Quantum Project" (versions 1.0-3.1, 2017-2022). NIST PQC submission. Describes the stateless hash-based signature scheme that became SLH-DSA (FIPS 205). Covers the hypertree construction, FORS few-time signatures, WOTS+ parameters, and the SHA-256/SHAKE-256 instantiations. The design achieves stateless operation (avoiding the state management problem of XMSS/LMS) at the cost of larger signatures.

**Prest, T., Fouque, P.-A., Hoffstein, J., Kirchner, P., Lyubashevsky, V., Pornin, T., Ricosset, T., Seiler, G., Whyte, W., & Zhang, Z.** "FALCON: Fast-Fourier Lattice-Based Compact Signatures over NTRU" (versions 1.0-1.2, 2017-2020). NIST PQC submission. Describes the NTRU-lattice-based hash-and-sign signature scheme selected for standardization as FN-DSA (expected FIPS 206). Covers the NTRU key generation, GPV framework for lattice-based signatures with trapdoors, fast Fourier sampling over NTRU lattices, and the tree-based Gaussian sampler.

### Important Attacks and Cryptanalysis

**Beullens, W. (2022)** "Breaking Rainbow Takes a Weekend on a Laptop." CRYPTO 2022. Demonstrates a practical attack against the Rainbow multivariate signature scheme (a NIST PQC finalist) using rectangular MinRank attacks. The attack recovers the secret key in approximately 53 hours on a standard laptop, completely breaking the scheme. This result eliminated Rainbow from NIST standardization and highlighted the risks of multivariate schemes with structured trapdoors.

**Castryck, W. & Decru, T. (2022)** "An Efficient Key Recovery Attack on SIDH (Preliminary Version)." Preprint, July 2022. EUROCRYPT 2023. Presents a polynomial-time attack against SIDH/SIKE exploiting the published torsion point images to recover the secret isogeny. The attack uses the Kani construction to translate the isogeny problem into a higher-dimensional abelian variety problem solvable via theta functions. This completely broke SIKE (a NIST PQC candidate) and demonstrated the danger of revealing auxiliary information about isogenies.

**Gidney, C. & Ekerå, M. (2021)** "How to Factor 2048 Bit RSA Integers in 8 Hours Using 20 Million Noisy Qubits." Quantum 5, 433. Provides the most detailed resource estimate for breaking RSA-2048 with a quantum computer: approximately 20 million physical qubits with 8 hours of computation, assuming surface code error correction with realistic noise rates. This paper is the primary reference for CRQC timeline estimates and demonstrates that quantum factoring is plausible with near-term hardware scaling.

**Albrecht, M.R., Player, R., & Scott, S. (2015)** "On the Concrete Hardness of Learning with Errors." Journal of Mathematical Cryptology, 9(3), 2015. Establishes the methodology for estimating the concrete security of LWE-based schemes using the core-SVP model. This paper defines the cost models (sieving, enumeration, BKZ simulation) used to set parameters for ML-KEM and ML-DSA. Updated estimates are maintained in the lattice-estimator tool.

**Becker, A., Joux, A., May, A., & Meurer, A. (2012)** "Decoding Random Binary Linear Codes in 2^(n/20): How 1+1=0 Improves Information Set Decoding." EUROCRYPT 2012. Introduces the nearest-neighbor technique for information set decoding, improving the asymptotic complexity of attacks against code-based cryptosystems. The BJMM algorithm and its successors define the concrete security estimates for McEliece and HQC parameter selection.

**Ducas, L. (2018)** "Shortest Vector from Lattice Sieving: A Few Dimensions for Free." EUROCRYPT 2018. Introduces the "dimensions for free" technique that improves BKZ by starting sieving in dimension d > β and projecting to find short vectors in the target sublattice. This optimization is incorporated into modern security estimates and reduces the cost of lattice attacks by a small polynomial factor.

### Hybrid Schemes and Protocol Design

**Stebila, D. & Mosca, M. (2016)** "Post-Quantum Key Exchange for the Internet and the Open Quantum Safe Project." Selected Areas in Cryptography (SAC) 2016. Introduces the hybrid key exchange paradigm and the OQS project. Establishes the design principles for combining classical and PQC algorithms in TLS, ensuring security if either component remains unbroken. This paper motivated much of the subsequent IETF standardization work.

**Bindel, N., Brendel, J., Fischlin, M., Goncalves, B., & Stebila, D. (2019)** "Hybrid Key Encapsulation Mechanisms and Authenticated Key Exchange." PQCrypto 2019. Provides formal security definitions for hybrid KEMs and proves that simple combiners (concatenation with KDF) achieve the desired "secure if either component is secure" guarantee under standard assumptions. Informs the design of TLS hybrid key exchange drafts.

**Cremers, C., Düzlü, S., Fiedler, R., Fischlin, M., & Gagliardoni, T. (2024)** "BUFFing Signature Schemes Beyond Unforgeability and the Case of Post-Quantum Signatures." IEEE S&P 2021. Analyzes additional security properties beyond EUF-CMA (exclusive ownership, message-bound signatures, non-resignability) and evaluates PQC signatures against these properties. Important for understanding certificate and protocol security in the PQC context.

**Schwabe, P., Stebila, D., & Wiggers, T. (2021)** "Post-Quantum TLS Without Handshake Signatures." ACM CCS 2020. Explores TLS 1.3 with post-quantum authentication using cached certificates and KEMs for authentication (KEMTLS). Addresses the bandwidth overhead problem of PQC signatures in TLS handshakes by replacing signature-based authentication with KEM-based authentication.

**Paquin, C., Stebila, D., & Tamvada, G. (2020)** "Benchmarking Post-Quantum Cryptography in TLS." PQCrypto 2020. Comprehensive measurement study of PQC algorithm performance within TLS handshakes, including latency impact, bandwidth overhead, and server load implications. Essential reference for deployment planning.

**Crockett, E., Paquin, C., & Stebila, D. (2019)** "Prototyping Post-Quantum and Hybrid Key Exchange and Authentication in TLS and SSH." NIST 2nd PQC Standardization Conference. Documents early integration of PQC into production protocols, identifying practical challenges including buffer sizes, API design, and backward compatibility requirements.

### Quantum Resource Estimation

**Häner, T., Jaques, S., Naehrig, M., Roetteler, M., & Soeken, M. (2020)** "Improved Quantum Circuits for Elliptic Curve Discrete Logarithms." PQCrypto 2020. Provides refined quantum resource estimates for breaking elliptic curve cryptography, showing that ECDLP on a 256-bit curve requires approximately 2,330 logical qubits and 1.26 × 10^11 Toffoli gates.

**Webber, M., Elfving, V., Weiss, S., & et al. (2022)** "The Impact of Hardware Specifications on Reaching Quantum Advantage in the Fault Tolerant Regime." AVS Quantum Science 4(1). Analyzes how physical qubit quality, connectivity, and error correction overhead determine the timeline to cryptographically relevant quantum computers. Provides parameterized estimates based on hardware improvement trajectories.

**Litinski, D. (2023)** "How to Compute a 256-bit Elliptic Curve Private Key with Only 50 Million Toffoli Gates." Cryptology ePrint Archive 2023/224. Demonstrates further optimization of quantum circuits for ECC, reducing resource requirements. These continued improvements in quantum algorithms mean that CRQC timeline estimates may need periodic revision.

### Side-Channel Security of PQC

**Ravi, P., Roy, S.S., Chattopadhyay, A., & Bhasin, S. (2020)** "Generic Side-Channel Attacks on CCA-Secure Lattice-Based PKE and KEMs." TCHES 2020. Demonstrates that the FO transform comparison (between re-encrypted ciphertext and received ciphertext) is a critical side-channel target. Motivates the need for constant-time comparison and masking in ML-KEM decapsulation.

**Primas, R., Pessl, P., & Mangard, S. (2017)** "Single-Trace Side-Channel Attacks on Masked Lattice-Based Encryption." CHES 2017. Shows that even masked implementations can be vulnerable to single-trace attacks targeting the NTT or polynomial multiplication. Motivates higher-order masking and shuffling countermeasures.

**Heinz, D., Kannwischer, M.J., Pessl, P., Primas, R., & Sigl, G. (2022)** "First-Order Masked Kyber on ARM Cortex-M4." TCHES 2022. Provides the first practical masked implementation of ML-KEM on an embedded platform, achieving approximately 3× overhead over unmasked implementation. Demonstrates feasibility of side-channel-protected PQC on constrained devices.

### Formal Verification of PQC

**Almeida, J.B., Baritel-Ruet, C., Barbosa, M., Barthe, G., Dupressoir, F., Grégoire, B., Laporte, V., Oliveira, T., Stoughton, A., Strub, P.-Y., & Zucchini, R. (2020)** "Machine-Checked Proofs for Cryptographic Standards: Indifferentiability of Sponge and Secure High-Assurance Implementations of SHA-3." CCS 2020. Demonstrates formal verification of the SHA-3/SHAKE constructions used throughout PQC standards, providing mathematical proof that the implementations correctly realize the specification.

**Barbosa, M., Barthe, G., Fan, X., Grégoire, B., Hung, S.-H., Katz, J., Strub, P.-Y., Wu, X., & Zhou, L. (2021)** "EasyCrypt Meets Jasmin: Formal Proof of ML-KEM." Cryptology ePrint Archive. Machine-checked proof that ML-KEM achieves IND-CCA2 security assuming Module-LWE hardness, with a verified implementation in the Jasmin language compiled to correct-by-construction assembly code. Represents the gold standard for PQC implementation assurance.

**Schwabe, P. & Stebila, D. (2022)** "Post-Quantum Verification." IEEE Security & Privacy Magazine. Survey article discussing the state of formal verification applied to PQC, covering both cryptographic proof verification (security proofs) and implementation verification (functional correctness, constant-time). Identifies gaps and future directions.

### Performance and Deployment Studies

**Sikeridis, D., Kampanakis, P., & Devetsikiotis, M. (2020)** "Assessing the Overhead of Post-Quantum Cryptography in TLS 1.3 and SSH." CoNEXT 2020. Empirical measurement of PQC impact on protocol performance across different network conditions (varying latency, bandwidth, packet loss). Provides data-driven guidance for deployment planning in diverse network environments.

**Kwiatkowski, K. & Langley, A. (2019)** "Measuring TLS Key Exchange with Post-Quantum KEM." Workshop on PQC Standardization, NIST. Reports on Google's CECPQ2 experiment measuring NTRU-HRSS hybrid key exchange performance in production Chrome traffic (note: CECPQ2 used NTRU-HRSS, not Kyber/ML-KEM; the later X25519Kyber768 experiment was a separate effort). Demonstrated negligible performance impact and identified middlebox compatibility issues resolved by record splitting.

**Kampanakis, P. & Stebila, D. (2021)** "Post-Quantum Signatures in TLS 1.3: A Measurement Study." IMC 2021 (Internet Measurement Conference). Measures the impact of PQC signatures (specifically the larger certificate chains) on TLS handshake performance. Identifies certificate chain transmission as the primary bottleneck and evaluates mitigation strategies (compression, caching, certificate omission).

**Bos, J.W., Costello, C., Naehrig, M., & Stebila, D. (2015)** "Post-Quantum Key Exchange for the TLS Protocol from the Ring Learning with Errors Problem." IEEE S&P 2015. One of the earliest integration studies of PQC in TLS, establishing the hybrid design pattern and performance measurement methodology used by subsequent work.

## D.3 Standards Documents

### NIST Standards and Publications

| Document | Title | Status | Relevance |
|----------|-------|--------|-----------|
| FIPS 203 | Module-Lattice-Based Key-Encapsulation Mechanism Standard | Final (2024) | Primary PQC KEM standard |
| FIPS 204 | Module-Lattice-Based Digital Signature Standard | Final (2024) | Primary PQC signature standard |
| FIPS 205 | Stateless Hash-Based Digital Signature Standard | Final (2024) | Conservative PQC signature |
| FIPS 206 (draft) | FFT-Based Lattice Signature Standard (FN-DSA) | In development | Compact lattice signature |
| SP 800-208 | Recommendation for Stateful Hash-Based Signature Schemes | Final (2020) | LMS and XMSS guidance |
| SP 1800-38 | Quantum Readiness: Migration to Post-Quantum Cryptography | Final | Practice guide for migration |
| NISTIR 8413 | Status Report on the Third Round of the NIST PQC Process | Final (2022) | Selection rationale and analysis |
| NISTIR 8309 | Status Report on the Second Round of the NIST PQC Process | Final (2020) | Round 2 evaluation |
| NIST IR 8545 | PQC Migration: Challenges and Approaches | Draft | Migration methodology |
| CNSA 2.0 FAQ | CNSA 2.0 Frequently Asked Questions | Final (2022) | NSA transition timeline |

### IETF RFCs and Internet-Drafts

| Document | Title | Status | Working Group |
|----------|-------|--------|---------------|
| RFC 8391 | XMSS: eXtended Merkle Signature Scheme | Informational | CFRG |
| RFC 8554 | Leighton-Micali Hash-Based Signatures (LMS) | Informational | CFRG |
| RFC 9370 | Multiple Key Exchanges in the IKEv2 Protocol | Standards Track | IPsecME |
| RFC 8879 | TLS Certificate Compression | Standards Track | TLS |
| RFC 9420 | The Messaging Layer Security (MLS) Protocol | Standards Track | MLS |
| draft-ietf-tls-hybrid-design | Hybrid Key Exchange in TLS 1.3 | WG Draft | TLS |
| draft-ietf-lamps-pq-composite-sigs | Composite ML-DSA for X.509 and CMS | WG Draft | LAMPS |
| draft-ietf-lamps-pq-composite-kem | Composite ML-KEM for X.509 and CMS | WG Draft | LAMPS |
| draft-ietf-lamps-dilithium-certificates | ML-DSA in Internet X.509 Certificates | WG Draft | LAMPS |
| draft-connolly-tls-mlkem-key-agreement | ML-KEM for TLS 1.3 | Individual | TLS |
| draft-ietf-pquip-pqc-engineers | PQC for Engineers | WG Draft | PQUIP |
| draft-ietf-lamps-kyber-certificates | ML-KEM in Internet X.509 Certificates | WG Draft | LAMPS |
| draft-ietf-ipsecme-ikev2-mlkem | ML-KEM in IKEv2 | WG Draft | IPsecME |
| draft-kampanakis-ml-kem-ikev2 | ML-KEM Key Exchange for IKEv2 | Individual | IPsecME |
| draft-ietf-openpgp-pqc | PQC in OpenPGP | WG Draft | OpenPGP |

### European and International Standards

| Organization | Document | Title/Subject |
|-------------|----------|---------------|
| BSI (Germany) | TR-02102-1 | Cryptographic Mechanisms: Recommendations and Key Lengths (updated annually) |
| BSI | TR-02102-2 | Use of TLS (PQC hybrid requirements for German government) |
| ANSSI (France) | Avis PQC | Recommendations for post-quantum cryptography transition |
| ANSSI | Position paper | Hybrid mechanisms: mandatory for PQC transition period |
| ETSI | TR 103 619 | Migration Strategies and Recommendations for Quantum-Safe Cryptography |
| ETSI | TS 103 744 | Quantum-Safe Hybrid Key Exchanges |
| ETSI | GR QSC 006 | Limits of Quantum Computing for Cryptanalysis |
| ISO/IEC | 14888-4 | Digital Signatures with Appendix (PQC addition in progress) |
| ISO/IEC | 18033-5 | Encryption Algorithms Part 5 (PQC KEM in progress) |
| TCG | TPM 2.0 Library | TPM specification (PQC algorithm profiles) |
| OASIS | KMIP 2.x | Key Management Interoperability Protocol (PQC extensions) |
| 3GPP | TS 33.501+ | 5G Security (PQC integration study items) |
| GSMA | PQC Guidelines | Quantum-safe cryptography for mobile industry |
| W3C | WebCrypto API | Web platform crypto (PQC extension in progress) |
| FIDO Alliance | FIDO2/WebAuthn | Authentication standard (PQC considerations) |
| GlobalPlatform | TEE/SE Specs | Secure element PQC integration |
| SAE International | J3061 | Automotive cybersecurity (PQC for V2X) |

### Government Guidance Documents

| Issuing Body | Document | Focus |
|-------------|----------|-------|
| NSA/CISA (US) | CNSA 2.0 | Algorithm selection and transition timeline |
| CISA (US) | Quantum-Ready Guidance | Federal agency preparedness |
| OMB (US) | M-23-02 | Memorandum on migrating to PQC (reporting requirements) |
| NCSC (UK) | PQC Guidance | Preparing for quantum-safe cryptography |
| CCCS (Canada) | ITSAP.00.017 | Preparing for post-quantum cryptography |
| ASD (Australia) | Quantum Computing Guidance | PQC migration for Australian government |
| AIVD (Netherlands) | PQC Migration Handbook | Practical migration guidance |
| Singapore CSA | PQC Advisory | National PQC transition guidance |
| Japan CRYPTREC | PQC Report | Japanese cryptographic evaluation |
| South Korea KISA | PQC Roadmap | Korean PQC transition plan |
| NATO | STANAG updates | Military interoperability (PQC integration) |
| ENISA (EU) | PQC Recommendations | EU-wide quantum-safe guidance |

## D.4 Online Courses and Tutorials

### University Courses (Available Online)

**MIT 6.875/18.425: Foundations of Cryptography (Vinod Vaikuntanathan):**
Covers lattice-based cryptography in depth, including LWE, Ring-LWE, FHE, and attribute-based encryption. Lecture notes available online. Directly relevant to understanding ML-KEM and ML-DSA at a theoretical level.

**Stanford CS355: Topics in Cryptography (Dan Boneh):**
Rotating topics often include lattice cryptography, post-quantum protocols, and advanced signature schemes. Lecture videos periodically available through Stanford Online.

**ETH Zurich: Cryptography (Dennis Hofheinz):**
Rigorous treatment of modern cryptography with explicit coverage of lattice assumptions and PQC. Lecture notes publicly available.

**Bar-Ilan University Winter School on Cryptography:**
Annual intensive school with varying PQC-relevant topics. Past editions covered lattice-based cryptography (2017), hash-based signatures (2019), and isogeny-based cryptography (2020). Videos and slides available online.

**Simons Institute Programs (UC Berkeley):**
The Simons Institute hosts semester-long programs and workshops on cryptography and quantum computing. Notable programs: "Lattices: Algorithms, Complexity, and Cryptography" (2020), "The Quantum Wave in Computing" (2024). Workshop videos freely available.

**University of Waterloo: Quantum-Safe Cryptography (Michele Mosca):**
Covers quantum computing threats to cryptography and post-quantum solutions. Available through the Institute for Quantum Computing.

**Chris Peikert's Lattice Cryptography Course Notes (University of Michigan):**
Comprehensive lecture notes covering lattice problems, LWE, Ring-LWE, and applications. Freely available and regularly updated. Widely considered the best self-contained introduction to the theory of lattice-based cryptography.

**Coursera/edX Quantum Computing Courses:**
Multiple introductory quantum computing courses provide the background needed to understand quantum threats:
- MIT xPRO "Quantum Computing Fundamentals" (professional certificate program)
- IBM Quantum Learning Path (free, hands-on with quantum simulators)
- University of Chicago "Quantum Computer Systems" (research-oriented)
- Delft University "Quantum Internet and Quantum Computers" (networking focus)

**SANS Institute — Quantum-Ready Cybersecurity:**
Professional training courses covering PQC from a practitioner/compliance perspective. Topics include risk assessment, migration planning, and technical implementation. Suited for security professionals responsible for organizational PQC readiness.

**Udacity — Applied Cryptography:**
While not PQC-specific, provides solid foundations in cryptographic thinking that facilitate understanding PQC security proofs and protocol analysis.

**Khan Academy / 3Blue1Brown — Linear Algebra:**
For readers lacking mathematical background, these resources provide the linear algebra intuition (vector spaces, eigenvalues, matrices) needed to understand lattice-based PQC at a conceptual level.

### Industry Training and Tutorials

**Cloudflare Blog — Post-Quantum Series:**
Accessible technical explanations of PQC concepts and Cloudflare's production deployment experience. Topics include: "The Quantum Threat," "How ML-KEM Works," "Deploying Post-Quantum Cryptography at Scale," and "Measuring the PQC Transition." Excellent for practitioners needing working understanding without full mathematical depth.

**Google Security Blog — Post-Quantum Updates:**
Regular updates on Chrome's PQC deployment, BoringSSL development, and lessons learned from production hybrid key exchange. Provides unique perspective on Internet-scale PQC deployment challenges.

**AWS Cryptography Blog:**
Coverage of AWS-LC PQC support, s2n-tls hybrid key exchange deployment, and cloud migration strategies. Includes practical code examples and architecture guidance.

**NIST PQC Workshop Presentations:**
All presentations from NIST PQC standardization workshops (2016-2024) are available on the NIST website. These provide invaluable insight into design decisions, security analyses, and selection criteria.

**Open Quantum Safe Tutorials:**
Step-by-step guides for integrating PQC into applications using liboqs, oqs-provider, and OQS protocol integrations. Available on the OQS website and GitHub.

### Video Resources

**IACR YouTube Channel:** Conference presentations from CRYPTO, EUROCRYPT, ASIACRYPT, and affiliated workshops. Search for specific paper titles or authors for detailed technical talks on PQC algorithms and attacks.

**Real World Crypto Talks:** Annual conference focusing on deployed cryptography. PQC-related talks from 2020-2025 cover deployment challenges, implementation pitfalls, and migration strategies.

**Computerphile (YouTube):** Accessible explanations of lattice problems, quantum computing threats, and PQC basics for general technical audiences. Good starting point for non-specialists.

**PQCast (Podcast):** Dedicated podcast on post-quantum cryptography developments, featuring interviews with researchers and practitioners. Covers standards updates, deployment experiences, and research breakthroughs.

**Security Cryptography Whatever (Podcast):** Broader cryptography podcast (Thomas Ptacek, Deirdre Connolly, David Adrian) frequently covering PQC topics including NIST decisions, protocol integration, and deployment challenges.

**Risky Business (Podcast):** Information security news podcast with periodic coverage of quantum computing threats and PQC migration urgency. Accessible to security professionals without deep cryptographic background.

### Open Educational Resources (OER)

**PQC Reference Card:** A concise reference document summarizing all NIST PQC standards, their parameters, key sizes, and security levels. Available from multiple sources (NIST, BSI, vendor documentation). Useful for quick lookup during implementation and architecture review.

**Algorithm Comparison Matrices:** Multiple organizations maintain comparison tables of PQC algorithms across dimensions including key/signature sizes, performance, security assumptions, maturity, and implementation complexity. The lattice-estimator GitHub repository and liboqs documentation provide particularly detailed comparisons.

**Migration Decision Trees:** Several organizations (NIST SP 1800-38, BSI, Entrust) publish decision trees helping organizations determine which PQC algorithms to deploy in specific contexts (long-term storage encryption, real-time communication, firmware signing, certificate issuance).

**Implementation Checklists:** Security checklists for PQC implementations covering constant-time verification, KAT testing, interoperability validation, side-channel resistance testing, and randomness quality requirements. Available from NIST CMVP guidance and academic papers on implementation security.

### Historical Context and Retrospectives

Understanding the historical development of PQC provides perspective on current decisions and future directions:

**Early vision (1994-2005):** Shor's algorithm (1994) demonstrated the quantum threat, but practical quantum computing seemed distant. McEliece (1978) and NTRU (1996) existed as alternatives but received limited attention. Ajtai's worst-case hardness result (1996) and Regev's LWE construction (2005) established the theoretical foundation for lattice-based cryptography.

**Field maturation (2006-2016):** The PQCrypto conference series began (2006), bringing dedicated focus to quantum-resistant algorithms. Ring-LWE (2010) and subsequent work enabled practical lattice-based schemes. NIST began planning its standardization process, recognizing the need for proactive migration before quantum computers arrive.

**NIST standardization (2016-2024):** The NIST PQC competition attracted 82 initial submissions across all algorithm families. Three rounds of evaluation, extensive community cryptanalysis, and real-world performance assessment narrowed candidates to four initial standards. The process demonstrated the value of open evaluation: Rainbow and SIKE were eliminated due to community-discovered attacks, validating the multi-year timeline.

**Deployment era (2024-present):** With standards finalized, the focus shifts to production deployment. Chrome, Signal, iMessage, and AWS demonstrated PQC deployment at scale. The challenge transitions from algorithm design to engineering, migration planning, and ecosystem coordination.

This historical arc illustrates that PQC represents decades of research achieving practical standardization — it is not a rushed response but a mature field finally receiving the deployment investment it requires. The remaining challenge is organizational and infrastructural rather than algorithmic. Organizations beginning their migration today benefit from mature algorithms, production-quality implementations, established deployment patterns, and a growing body of operational experience from early adopters. The resources in this appendix provide the knowledge foundation for navigating this transition successfully.

## D.5 Software Repositories

### Core Libraries

| Repository | URL | Language | Focus |
|-----------|-----|----------|-------|
| liboqs | https://github.com/open-quantum-safe/liboqs | C | Comprehensive PQC library |
| oqs-provider | https://github.com/open-quantum-safe/oqs-provider | C | OpenSSL 3.x PQC provider |
| PQClean | https://github.com/PQClean/PQClean | C | Clean reference implementations |
| CIRCL | https://github.com/cloudflare/circl | Go | Production PQC in Go |
| pqcrypto | https://github.com/rustpq/pqcrypto | Rust | Rust PQC wrappers |
| Bouncy Castle | https://www.bouncycastle.org/ | Java/C# | Enterprise Java/C# PQC |
| aws-lc | https://github.com/aws/aws-lc | C | AWS production crypto |
| wolfSSL | https://github.com/wolfSSL/wolfssl | C | Embedded PQC |
| ml-kem (RustCrypto) | https://github.com/RustCrypto/KEMs | Rust | Pure Rust ML-KEM |
| ml-dsa (RustCrypto) | https://github.com/RustCrypto/signatures | Rust | Pure Rust ML-DSA |

### Algorithm Reference Implementations

| Algorithm | Repository | Maintainer |
|-----------|-----------|------------|
| ML-KEM (Kyber) | https://github.com/pq-crystals/kyber | CRYSTALS team |
| ML-DSA (Dilithium) | https://github.com/pq-crystals/dilithium | CRYSTALS team |
| SLH-DSA (SPHINCS+) | https://github.com/sphincs/sphincsplus | SPHINCS+ team |
| FN-DSA (FALCON) | https://falcon-sign.info/ | Falcon team |
| Classic McEliece | https://classic.mceliece.org/ | McEliece team |
| HQC | https://pqc-hqc.org/ | HQC team |
| BIKE | https://bikesuite.org/ | BIKE team |
| NTRU Prime | https://ntruprime.cr.yp.to/ | Bernstein et al. |
| SQISign | https://github.com/SQISign/sqisign2 | SQISign team |

### Tools and Analysis Software

| Tool | Purpose | URL |
|------|---------|-----|
| lattice-estimator | Concrete security estimation | https://github.com/malb/lattice-estimator |
| fpLLL | LLL/BKZ lattice reduction | https://github.com/fplll/fplll |
| G6K | Lattice sieving framework | https://github.com/fplll/g6k |
| pqm4 | ARM Cortex-M4 benchmarks | https://github.com/mupq/pqm4 |
| SUPERCOP | Crypto benchmarking | https://bench.cr.yp.to/supercop.html |
| OQS demos | PQC protocol demonstrations | https://github.com/open-quantum-safe/oqs-demos |
| Rosenpass | PQC WireGuard extension | https://github.com/rosenpass/rosenpass |
| SageMath | Mathematical exploration | https://www.sagemath.org/ |
| leakage-models | Side-channel simulation | https://github.com/simple-crypto/SCALib |

## D.6 Communities and Mailing Lists

### Standards Bodies and Working Groups

**NIST PQC Forum:** The official NIST discussion forum for post-quantum cryptography standardization. Active discussions on algorithm specifications, security analyses, implementation questions, and migration guidance. Essential for tracking standardization progress and community feedback. Subscribe at: https://groups.google.com/a/list.nist.gov/g/pqc-forum

**IETF Working Groups:** Multiple IETF groups are actively integrating PQC:
- **CFRG (Crypto Forum Research Group):** Algorithm evaluation and selection for IETF protocols
- **TLS WG:** Hybrid key exchange and PQC authentication for TLS 1.3
- **LAMPS WG:** PQC in X.509 certificates and CMS (S/MIME)
- **IPsecME WG:** PQC in IKEv2 and IPsec
- **PQUIP WG:** Post-Quantum Use in Protocols (guidance and coordination)
- **OpenPGP WG:** PQC in PGP/GPG
Subscribe via https://www.ietf.org/mailman/listinfo/

**ETSI QSC ISG:** European standards body for quantum-safe cryptography. Regular workshops, technical reports, and industry engagement events. Membership open to organizations.

### Research Communities

**IACR (International Association for Cryptologic Research):** The primary professional organization for cryptography researchers. Publishes the ePrint archive (preprints), organizes major conferences, and maintains the IACR Communications newsletter. Essential for tracking new cryptanalysis results.

**Open Quantum Safe Project:** Open-source community developing PQC integration software. Active GitHub discussions, regular community calls, and collaborative development. Welcoming to new contributors.

**PQCA (Post-Quantum Cryptography Alliance):** Linux Foundation project bringing together industry, academia, and government to advance PQC adoption. Members include IBM, Google, Cisco, and others. Focuses on open-source tooling, interoperability testing, and migration guidance.

**PQC Coalition (MITRE):** Industry consortium focused on practical PQC migration challenges. Publishes guidance documents, use cases, and interoperability test results. Membership includes major technology vendors and government agencies.

### Discussion Platforms

- **Cryptography Stack Exchange:** Q&A platform for cryptography questions, including PQC topics. High-quality answers from researchers and practitioners. Particularly useful for implementation questions and understanding subtle aspects of specifications.
- **Reddit r/crypto and r/cryptography:** Community discussions on PQC developments, news, and educational content. Good for tracking community sentiment and emerging concerns.
- **Twitter/X #PostQuantum:** Real-time discussion and news sharing among PQC researchers and practitioners. Many researchers announce results here before formal publication.
- **Mastodon/Fediverse:** Growing cryptography community, particularly among European researchers. The infosec.exchange and mathstodon.xyz instances have active PQC discussions.
- **Signal/Matrix groups:** Several PQC research communities maintain real-time chat groups for rapid discussion of new results, implementation questions, and community coordination.
- **GitHub Discussions:** Many PQC library repositories (liboqs, PQClean, CIRCL) use GitHub Discussions for community Q&A, feature requests, and technical design decisions.

## D.7 Conferences and Events

### Academic Conferences

| Conference | Focus | Frequency | Typical Dates | PQC Relevance |
|-----------|-------|-----------|--------------|---------------|
| CRYPTO | General cryptography | Annual | August | Major PQC papers, attacks, and constructions |
| EUROCRYPT | General cryptography | Annual | May/June | Theoretical foundations, new constructions |
| ASIACRYPT | General cryptography | Annual | December | Implementations, Asian research community |
| PQCrypto | Post-quantum cryptography | Biennial | Varies | Dedicated PQC venue, all algorithm families |
| CHES | Cryptographic hardware/embedded | Annual | September | PQC implementation security, side channels |
| TCC | Theory of cryptography | Annual | November | Foundational lattice/code theory |
| CCS | Computer and communications security | Annual | November | Systems security, protocol analysis |
| IEEE S&P (Oakland) | Security and privacy | Annual | May | Foundational security, PQC protocol analysis |
| USENIX Security | Systems security | Annual | August | Practical PQC deployment and measurement |
| PKC | Public key cryptography | Annual | Spring | Key exchange, signatures, PQC constructions |
| CT-RSA | RSA Conference cryptography track | Annual | Spring | Applied cryptography, PQC migration |
| SAC | Selected Areas in Cryptography | Annual | August | Canadian conference, strong PQC presence |
| INDOCRYPT | Indian cryptography | Annual | December | Regional PQC research |
| ACISP | Australasian information security | Annual | July | Regional PQC research |

### Industry Events

| Event | Focus | Audience | PQC Content |
|-------|-------|---------|-------------|
| Real World Crypto (RWC) | Deployed cryptography | Practitioners + academics | PQC deployment experiences, migration talks |
| RSA Conference | Enterprise security | Industry practitioners | PQC vendor exhibits, migration workshops |
| Black Hat | Security research | Researchers/practitioners | PQC attack demonstrations, tool releases |
| NIST PQC Workshops | Standardization | All stakeholders | Algorithm evaluation, standardization progress |
| ETSI QSC Events | Quantum-safe deployment | Telecom/industry | Migration strategies, interoperability |
| ICMC (CMUF) | Crypto module validation | Compliance professionals | FIPS validation for PQC, testing methodology |
| Quantum World Congress | Quantum technology | Industry | Quantum threat timeline, PQC migration |
| IEEE QCE (Quantum Week) | Quantum computing | Researchers/industry | Quantum algorithm advances, threat assessment |
| NIST NCCoE Events | Cybersecurity practice | Government/industry | SP 1800-38 implementation guidance |

### Workshops and Specialized Events

**Dagstuhl Seminars:** Invitation-only research workshops at Schloss Dagstuhl, Germany. PQC-relevant seminars occur approximately annually, bringing together leading researchers for intensive week-long discussions. Past topics include "Post-Quantum Cryptography — Computational Aspects" and "Quantum Cryptanalysis."

**Lorentz Center Workshops:** Similar format to Dagstuhl, hosted in Leiden, Netherlands. Regular workshops on computational number theory, lattice algorithms, and cryptographic applications.

**DIMACS Workshops:** Rutgers University workshops on discrete mathematics and computer science, occasionally featuring PQC and quantum computing topics.

**COSIC Seminars (KU Leuven):** Regular research seminars from one of Europe's leading cryptography groups, with frequent PQC topics. Many are recorded and available online.

**NIST PQC Standardization Conferences:** NIST organized dedicated conferences during each round of the standardization process (2018, 2019, 2021, 2022, 2024) where submitters presented their algorithms, cryptanalysts presented attacks, and the community discussed selection criteria. Presentation slides and videos are available from the NIST website and provide invaluable insight into the decision-making process.

**Post-Quantum Cryptography Standardization Workshop Series:** Focused workshops organized by research institutions examining specific aspects of PQC standardization: parameter selection methodology, implementation security requirements, migration challenges, and interoperability testing frameworks.

**Quantum Computing and Cryptography Workshops:** Joint events bringing together quantum computing researchers and cryptographers to assess the realistic timeline for quantum threats. These events produce the most informed CRQC timeline estimates by combining hardware roadmap knowledge with algorithmic analysis.

## D.8 Keeping Current

The PQC field evolves rapidly, with new research, standards updates, and deployment experiences appearing regularly. A systematic approach to staying current is essential for both researchers and practitioners.

### Recommended Reading Paths

**For cryptography researchers entering PQC:**
1. Peikert's "A Decade of Lattice Cryptography" (survey paper)
2. Regev's original LWE paper (STOC 2005)
3. CRYSTALS-Kyber and CRYSTALS-Dilithium specification documents
4. Recent CRYPTO/EUROCRYPT papers on lattice attacks (Ducas, Albrecht, et al.)
5. Lattice-estimator documentation and underlying cost models

**For software engineers implementing PQC:**
1. FIPS 203/204/205 specification documents (primary references)
2. PQClean source code (clean reference implementations)
3. Cloudflare and Google deployment blog posts
4. IETF draft-ietf-pquip-pqc-engineers (PQC for Engineers)
5. Side-channel analysis papers (Ravi et al., TCHES 2020)

**For security architects planning PQC migration:**
1. NIST SP 1800-38 (Migration Practice Guide)
2. Mosca's theorem and risk quantification framework
3. IETF hybrid design drafts (TLS, IKEv2, X.509)
4. BSI/ANSSI/NCSC national guidance documents
5. Vendor deployment case studies (Cloudflare, Google, AWS, Signal)

**For managers and decision-makers:**
1. NISTIR 8413 (Third Round Status Report — explains selection decisions)
2. NSA CNSA 2.0 (timeline and algorithm requirements)
3. Gidney & Ekerå quantum resource paper (CRQC feasibility)
4. CISA quantum readiness guidance (organizational assessment)
5. Industry case studies of PQC deployment (Signal, Chrome, iMessage)

### Priority Information Sources (Check Weekly)

1. **IACR ePrint Archive (https://eprint.iacr.org/):** New cryptanalysis, constructions, and security analyses appear here before formal publication. Search for keywords: "lattice," "ML-KEM," "ML-DSA," "quantum," "post-quantum." Particularly important for early warning of attacks against standardized algorithms.

2. **NIST PQC Announcements:** Monitor the NIST PQC mailing list and project page for standards updates, errata, additional algorithm selections, and migration guidance updates. Critical for compliance planning.

3. **Library Release Notes:** Track releases of OpenSSL, liboqs, BoringSSL, and wolfSSL for PQC feature additions, security fixes, and API changes. Subscribe to GitHub release notifications for critical libraries.

4. **IETF Datatracker:** Monitor TLS, LAMPS, IPsecME, and PQUIP working group Internet-Drafts for protocol-level PQC integration progress. Draft updates often signal approaching RFC publication.

### Monthly Review

5. **Conference proceedings:** Review accepted papers at CRYPTO, EUROCRYPT, ASIACRYPT, CCS, and CHES for new attacks, improved implementations, and novel constructions.

6. **Vendor security blogs:** Cloudflare, Google, AWS, Microsoft, and Apple periodically publish PQC deployment updates and lessons learned. These provide practical insights unavailable in academic papers.

7. **Government publications:** Monitor CISA, NCSC (UK), BSI (Germany), and ANSSI (France) for updated migration guidance and timeline requirements.

### Quarterly Strategic Review

8. **Standards progress:** Assess which IETF drafts are advancing toward RFC status, which NIST additional algorithms are progressing, and how international standards (ISO, ETSI) are incorporating PQC.

9. **Quantum computing progress:** Track quantum hardware announcements from IBM, Google, Microsoft, and others. Assess whether CRQC timelines are accelerating or stable. Review quantum algorithm improvements that might affect PQC security margins.

10. **Ecosystem maturity:** Evaluate which PQC libraries have received security audits, FIPS validation, or production deployment. Update internal tool and library recommendations based on maturity progression.

### Building Organizational Knowledge

- **Designate a PQC champion:** Someone within the organization responsible for tracking developments and communicating relevant changes to engineering and management.
- **Maintain a reading list:** Curate a rotating list of recent papers, blog posts, and standards updates relevant to your specific deployment context.
- **Attend one conference annually:** RWC (for practitioners) or PQCrypto (for researchers) provide concentrated updates and networking opportunities.
- **Participate in interoperability events:** IETF hackathons and NIST testing events provide hands-on experience and early exposure to implementation challenges.
- **Engage with open-source communities:** Contributing to OQS, PQClean, or language-specific PQC libraries provides deep technical understanding and early access to developments.

### Key Researchers to Follow

The following researchers have made significant contributions to PQC and regularly publish relevant work:

**Lattice-based cryptography:** Vadim Lyubashevsky (IBM Research), Chris Peikert (University of Michigan), Léo Ducas (CWI Amsterdam), Damien Stehlé (ENS Lyon/CryptoLab), Martin Albrecht (King's College London/SandboxAQ), Peter Schwabe (MPI-SP/Radboud University)

**Hash-based signatures:** Andreas Hülsing (Eindhoven University of Technology), Jean-Philippe Aumasson (Taurus), Daniel J. Bernstein (University of Illinois at Chicago)

**Code-based cryptography:** Nicolas Sendrier (Inria), Carlos Aguilar-Melchor (SandboxAQ), Daniel J. Bernstein, Tanja Lange (Eindhoven University of Technology)

**Isogeny-based cryptography:** Luca De Feo (IBM Research), David Kohel (Aix-Marseille University), Benjamin Wesolowski (ENS Lyon/CNRS), Wouter Castryck (KU Leuven)

**Multivariate cryptography:** Ward Beullens (IBM Research), Jintai Ding (Tsinghua University), Jacques Patarin (University of Versailles)

**Quantum algorithms and resource estimation:** Craig Gidney (Google), Martin Ekerå (KTH/GCHQ), Thomas Häner (Microsoft), Michael Naehrig (Microsoft)

**PQC deployment and protocols:** Douglas Stebila (University of Waterloo), Bas Westerbaan (Cloudflare), Thom Wiggers (PQShield), Panos Kampanakis (AWS)

### Significant Blogs and News Sources

**Academic/Research:**
- **Daniel J. Bernstein's website (cr.yp.to):** Comprehensive PQC resources, software, and commentary on standardization decisions
- **Léo Ducas's notes:** Technical insights on lattice algorithms and parameter selection
- **Chris Peikert's publications page:** Preprints and lecture notes on lattice cryptography
- **IACR News:** Official announcements from the cryptography research community

**Industry/Deployment:**
- **Cloudflare Research Blog:** Production PQC deployment insights, performance data, and protocol analysis
- **Google Security Blog:** Chrome PQC deployment, quantum threat assessment, BoringSSL development
- **AWS Security Blog:** Cloud PQC migration, s2n-tls development, customer guidance
- **Microsoft Security Blog:** Windows/Azure PQC, quantum computing research program, SymCrypt development
- **Signal Engineering Blog:** PQXDH protocol design, messaging PQC deployment experience
- **Apple Security Research:** PQ3 protocol for iMessage, CryptoKit PQC integration

**Policy/Governance:**
- **CISA Insights:** US government quantum readiness guidance and agency requirements
- **NCSC (UK) Blog:** UK government PQC position and guidance updates
- **BSI Publications:** German government cryptographic recommendations

---

*The post-quantum cryptography transition represents one of the most significant infrastructure upgrades in the history of digital security. The resources in this appendix provide the foundation for understanding, implementing, and deploying quantum-resistant cryptography. Stay engaged with the community, maintain awareness of developments, and begin your migration today. The window for proactive, orderly migration narrows with each passing year — the investments made now in understanding, planning, and early deployment will determine how smoothly organizations weather the quantum transition when cryptographically relevant quantum computers finally arrive.*
