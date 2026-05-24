# Appendix D: Further Reading and Resources

## D.1 Foundational Textbooks

### Cryptography

- **Katz, J. & Lindell, Y.** *Introduction to Modern Cryptography* (3rd edition). CRC Press. Comprehensive introduction covering both classical and post-quantum foundations.

- **Goldreich, O.** *Foundations of Cryptography* (Volumes 1 & 2). Cambridge University Press. Rigorous theoretical treatment of cryptographic primitives and protocols.

- **Boneh, D. & Shoup, V.** *A Graduate Course in Applied Cryptography*. Available online. Excellent coverage of modern cryptographic constructions with security proofs.

### Post-Quantum Cryptography

- **Bernstein, D.J., Buchmann, J., & Dahmen, E. (Eds.)** *Post-Quantum Cryptography*. Springer. The foundational reference covering all PQC families.

- **Galbraith, S.** *Mathematics of Public Key Cryptography*. Cambridge University Press. Excellent mathematical treatment of public-key systems including PQC-relevant mathematics.

### Quantum Computing

- **Nielsen, M.A. & Chuang, I.L.** *Quantum Computation and Quantum Information*. Cambridge University Press. The definitive textbook on quantum computing.

- **Mermin, N.D.** *Quantum Computer Science: An Introduction*. Cambridge University Press. Accessible introduction for computer scientists.

### Lattice-Based Cryptography

- **Micciancio, D. & Goldwasser, S.** *Complexity of Lattice Problems: A Cryptographic Perspective*. Springer. Comprehensive treatment of computational lattice problems.

- **Peikert, C.** "A Decade of Lattice Cryptography." Foundations and Trends in Theoretical Computer Science. Excellent survey of lattice-based constructions.

### Coding Theory

- **MacWilliams, F.J. & Sloane, N.J.A.** *The Theory of Error-Correcting Codes*. North-Holland. Classic reference for coding theory fundamentals.

## D.2 Key Research Papers

### Foundational Papers

- **Shor, P.W. (1994)** "Algorithms for quantum computation: Discrete logarithms and factoring." FOCS 1994. The paper that started the PQC field.

- **Grover, L.K. (1996)** "A fast quantum mechanical algorithm for database search." STOC 1996. Quadratic speedup for unstructured search.

- **Regev, O. (2005)** "On lattices, learning with errors, random linear codes, and cryptography." STOC 2005. Introduced LWE and proved quantum reduction from lattice problems.

- **McEliece, R.J. (1978)** "A public-key cryptosystem based on algebraic coding theory." DSN Progress Report. The first code-based cryptosystem.

- **Merkle, R. (1979)** "Secrecy, Authentication, and Public Key Systems." Stanford PhD thesis. Introduced hash-based signatures.

### NIST Standardized Algorithm Papers

- **Avanzi, R. et al.** "CRYSTALS-Kyber: Algorithm Specifications and Supporting Documentation." NIST submission (ML-KEM).

- **Ducas, L. et al.** "CRYSTALS-Dilithium: Algorithm Specifications and Supporting Documentation." NIST submission (ML-DSA).

- **Aumasson, J.-P. et al.** "SPHINCS+: Submission to the NIST Post-Quantum Project." NIST submission (SLH-DSA).

### Important Attacks

- **Beullens, W. (2022)** "Breaking Rainbow Takes a Weekend on a Laptop." CRYPTO 2022. Complete break of Rainbow signature scheme.

- **Castryck, W. & Decru, T. (2022)** "An efficient key recovery attack on SIDH." EUROCRYPT 2023. Polynomial-time attack breaking SIKE.

- **Gidney, C. & Ekerå, M. (2021)** "How to factor 2048 bit RSA integers in 8 hours using 20 million noisy qubits." Quantum 5, 433. Optimized quantum factoring resources.

### Hybrid Schemes and Protocols

- **Stebila, D. & Mosca, M. (2016)** "Post-quantum Key Exchange for the Internet and the Open Quantum Safe Project." Selected Areas in Cryptography.

- **Bindel, N. et al. (2017)** "Transitioning to a Quantum-Resistant Public Key Infrastructure." PQCrypto 2017.

## D.3 Standards Documents

### NIST Standards

| Document | Title |
|----------|-------|
| FIPS 203 | Module-Lattice-Based Key-Encapsulation Mechanism Standard |
| FIPS 204 | Module-Lattice-Based Digital Signature Standard |
| FIPS 205 | Stateless Hash-Based Digital Signature Standard |
| SP 800-208 | Recommendation for Stateful Hash-Based Signature Schemes |
| SP 1800-38 | Quantum Readiness: Migration to Post-Quantum Cryptography |
| NISTIR 8413 | Status Report on the Third Round of the NIST PQC Process |

### IETF RFCs and Drafts

| Document | Title |
|----------|-------|
| RFC 8391 | XMSS: eXtended Merkle Signature Scheme |
| RFC 8554 | Leighton-Micali Hash-Based Signatures |
| RFC 9370 | Multiple Key Exchanges in the IKEv2 Protocol |
| RFC 8879 | TLS Certificate Compression |
| draft-ietf-tls-hybrid-design | Hybrid Key Exchange in TLS 1.3 |
| draft-ietf-lamps-pq-composite-sigs | Composite ML-DSA Signatures |
| draft-ietf-lamps-pq-composite-kem | Composite ML-KEM |

### Other Standards

| Organization | Document |
|-------------|----------|
| BSI | TR-02102-1: Cryptographic Mechanisms (2024 update) |
| ANSSI | Avis relatif à la migration vers la cryptographie post-quantique |
| ETSI | TR 103 619: Migration Strategies and Recommendations for QSC |
| ISO/IEC | 14888-4: Digital Signatures (PQC addition in progress) |
| TCG | TPM 2.0 Library Specification (PQC algorithms) |

## D.4 Online Courses and Tutorials

### University Courses

- **MIT 6.875:** Foundations of Cryptography (includes PQC topics)
- **Stanford CS355:** Topics in Cryptography (lattice cryptography modules)
- **Bar-Ilan Winter Schools:** Annual cryptography school with PQC sessions
- **Simons Institute Programs:** Berkeley hosts quantum and PQC workshops

### Online Resources

- **Cloudflare Blog - Post-Quantum Series:** Accessible explanations of PQC deployment
- **IACR YouTube Channel:** Conference presentations from CRYPTO, EUROCRYPT
- **Daniel J. Bernstein's PQC resources:** https://pqcrypto.org/
- **Chris Peikert's lattice course notes:** Comprehensive lattice cryptography lectures

### Tutorials and Workshops

- **NIST PQC Workshops:** Presentations from all standardization rounds
- **Real World Crypto:** Annual conference with PQC deployment talks
- **CHES Workshop:** Cryptographic hardware and implementation topics
- **PQCrypto Conference:** Biennial conference dedicated to PQC research

## D.5 Software Repositories

### Core Libraries

| Repository | URL |
|-----------|-----|
| liboqs | https://github.com/open-quantum-safe/liboqs |
| PQClean | https://github.com/PQClean/PQClean |
| CIRCL | https://github.com/cloudflare/circl |
| pqcrypto (Rust) | https://github.com/rustpq/pqcrypto |
| Bouncy Castle | https://www.bouncycastle.org/ |
| oqs-provider | https://github.com/open-quantum-safe/oqs-provider |

### Reference Implementations

| Algorithm | Repository |
|-----------|-----------|
| ML-KEM (Kyber) | https://github.com/pq-crystals/kyber |
| ML-DSA (Dilithium) | https://github.com/pq-crystals/dilithium |
| SLH-DSA (SPHINCS+) | https://github.com/sphincs/sphincsplus |
| FN-DSA (FALCON) | https://falcon-sign.info/ |
| Classic McEliece | https://classic.mceliece.org/ |

### Tools and Utilities

| Tool | Purpose | URL |
|------|---------|-----|
| lattice-estimator | Lattice security estimation | https://github.com/malb/lattice-estimator |
| pqm4 | ARM Cortex-M4 benchmarks | https://github.com/mupq/pqm4 |
| SUPERCOP | Crypto benchmarking | https://bench.cr.yp.to/supercop.html |
| OQS demos | PQC protocol demos | https://github.com/open-quantum-safe/oqs-demos |

## D.6 Communities and Mailing Lists

- **NIST PQC Forum:** Official NIST discussion forum for PQC standardization
- **IETF Mailing Lists:** CFRG, TLS, LAMPS working groups
- **IACR Communications:** Research community announcements
- **Open Quantum Safe:** GitHub discussions and community
- **PQC Coalition:** Industry consortium for PQC migration
- **Linux Foundation PQCA:** Post-Quantum Cryptography Alliance

## D.7 Conferences and Events

### Academic Conferences

| Conference | Focus | Frequency |
|-----------|-------|-----------|
| CRYPTO | General cryptography | Annual (August) |
| EUROCRYPT | General cryptography | Annual (May) |
| ASIACRYPT | General cryptography | Annual (December) |
| PQCrypto | Post-quantum cryptography | Biennial |
| CHES | Implementation security | Annual |
| TCC | Theory of cryptography | Annual |
| CCS | Computer security | Annual |
| IEEE S&P | Security and privacy | Annual |

### Industry Events

| Event | Focus | Audience |
|-------|-------|---------|
| Real World Crypto | Deployed cryptography | Practitioners |
| RSA Conference | Enterprise security | Industry |
| Black Hat | Security research | Researchers/practitioners |
| NIST PQC Workshops | Standardization | All stakeholders |
| ETSI QSC Events | Quantum-safe deployment | Telecom/industry |

## D.8 Keeping Current

The PQC field moves rapidly. To stay current:

1. **Follow NIST announcements:** Subscribe to PQC forum updates
2. **Monitor IACR ePrint:** New cryptanalysis appears here first
3. **Track library releases:** OpenSSL, liboqs, BoringSSL changelogs
4. **Attend conferences:** RWC, PQCrypto, CHES for latest developments
5. **Join working groups:** IETF, ETSI, TCG for standards evolution
6. **Read vendor blogs:** Cloudflare, Google, AWS publish deployment insights
7. **Engage with community:** Open Quantum Safe, PQCA for collaborative work

---

*This concludes the appendices. The field of post-quantum cryptography continues to evolve rapidly. Stay engaged, keep learning, and begin your migration today.*
