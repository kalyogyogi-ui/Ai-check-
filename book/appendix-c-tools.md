# Appendix C: Reference Implementations and Tools

## C.1 Cryptographic Libraries with PQC Support

### liboqs (Open Quantum Safe)

- **Language:** C (with bindings for Python, Go, Java, .NET, Rust)
- **Repository:** https://github.com/open-quantum-safe/liboqs
- **Algorithms:** All NIST standardized and candidate algorithms
- **Status:** Research/reference quality; integrates with OpenSSL via oqs-provider
- **License:** MIT

### OpenSSL 3.5+

- **Language:** C
- **Algorithms:** ML-KEM, ML-DSA, SLH-DSA (via native support or oqs-provider)
- **Status:** Production quality for supported algorithms
- **Notes:** Provider architecture allows modular algorithm addition

### BoringSSL (Google)

- **Language:** C/C++
- **Algorithms:** ML-KEM (Kyber) for TLS hybrid key exchange
- **Status:** Production (deployed in Chrome)
- **Notes:** Focused on TLS use cases

### wolfSSL

- **Language:** C
- **Algorithms:** ML-KEM, ML-DSA, SLH-DSA, XMSS, LMS
- **Status:** Production quality, FIPS validation in progress
- **Notes:** Optimized for embedded systems

### PQClean

- **Language:** C
- **Repository:** https://github.com/PQClean/PQClean
- **Algorithms:** All NIST candidates (clean, portable implementations)
- **Status:** Reference quality; designed for correctness over performance
- **License:** Various (per-algorithm)

### CIRCL (Cloudflare)

- **Language:** Go
- **Repository:** https://github.com/cloudflare/circl
- **Algorithms:** ML-KEM, ML-DSA, SLH-DSA, X25519+ML-KEM hybrid
- **Status:** Production quality (used by Cloudflare)
- **License:** BSD-3-Clause

### pqcrypto (Rust)

- **Language:** Rust
- **Algorithms:** ML-KEM, ML-DSA, SLH-DSA
- **Status:** Production quality with Rust memory safety benefits
- **Notes:** Wrapper around C implementations and native Rust versions

### Bouncy Castle

- **Language:** Java / C#
- **Algorithms:** ML-KEM, ML-DSA, SLH-DSA, FN-DSA, XMSS, LMS
- **Status:** Production quality
- **Notes:** Wide enterprise Java ecosystem support

### libsignal

- **Language:** Rust (with bindings for Java, Swift, TypeScript)
- **Algorithms:** ML-KEM-1024 (PQXDH protocol)
- **Status:** Production (deployed in Signal)
- **Notes:** Specific to Signal Protocol integration

## C.2 Protocol Implementations

### TLS Libraries with PQC

| Library | PQC Key Exchange | PQC Authentication | Language |
|---------|-----------------|-------------------|----------|
| OpenSSL 3.5+ | ML-KEM hybrid | ML-DSA, SLH-DSA | C |
| BoringSSL | ML-KEM hybrid | In development | C/C++ |
| s2n-tls (AWS) | ML-KEM hybrid | ML-DSA | C |
| rustls | ML-KEM hybrid | In development | Rust |
| wolfSSL | ML-KEM hybrid | ML-DSA | C |
| GnuTLS | ML-KEM hybrid | In development | C |
| NSS (Mozilla) | ML-KEM hybrid | In development | C |

### SSH Implementations

| Implementation | PQC Key Exchange | PQC Authentication |
|---------------|-----------------|-------------------|
| OpenSSH 9.x+ | ML-KEM hybrid (experimental) | In development |
| libssh | Via liboqs integration | Via liboqs |
| PuTTY | Experimental | Experimental |

### VPN/IPsec

| Implementation | PQC Support |
|---------------|------------|
| strongSwan | ML-KEM hybrid in IKEv2 |
| Libreswan | PQC key exchange (experimental) |
| WireGuard + Rosenpass | ML-KEM overlay |

## C.3 Testing and Validation Tools

### Known Answer Test (KAT) Generators

- **NIST KAT files:** Official test vectors for FIPS 203, 204, 205
- **ACVP (Automated Cryptographic Validation Protocol):** NIST's automated testing
- **kat-generator (PQClean):** Generates KAT files for all algorithms

### Side-Channel Analysis Tools

| Tool | Purpose | Platform |
|------|---------|----------|
| ChipWhisperer | Power analysis, fault injection | Hardware + Python |
| Langer | EM probes, power analysis | Hardware |
| Riscure Inspector | Side-channel evaluation | Hardware + Software |
| ctgrind | Constant-time checking via Valgrind | Software |
| timecop | Timing leak detection | Software |
| dudect | Statistical timing analysis | Software |

### Benchmarking Frameworks

- **SUPERCOP:** Standardized crypto benchmarking (https://bench.cr.yp.to/)
- **PQM4:** Benchmarking PQC on ARM Cortex-M4 (https://github.com/mupq/pqm4)
- **liboqs speed tests:** Built-in benchmarking for all algorithms
- **NIST submission benchmarks:** Official reference performance data

### Interoperability Testing

- **OQS interop tests:** Cross-library interoperability validation
- **Wycheproof-style tests:** Edge case and malformed input testing
- **IETF hackathons:** Multi-vendor interoperability events

## C.4 Discovery and Inventory Tools

### Cryptographic Discovery

| Tool | Function | Type |
|------|----------|------|
| Cryptosense Analyzer | Application crypto discovery | Commercial |
| IBM Quantum Safe Explorer | Code scanning for crypto | Commercial |
| sslyze | TLS configuration scanning | Open source |
| testssl.sh | TLS/SSL testing | Open source |
| ssh-audit | SSH configuration analysis | Open source |
| CycloneDX CLI | CBOM generation | Open source |

### Certificate Management

| Tool | Function |
|------|----------|
| cert-manager (Kubernetes) | Automated certificate lifecycle |
| Venafi | Enterprise certificate management |
| DigiCert CertCentral | CA with PQC certificate support |
| Let's Encrypt | Automated certificates (PQC roadmap) |
| Step CA | Open source CA with PQC support |

## C.5 Development and Debugging Tools

### Algorithm Exploration

- **SageMath:** Mathematical software for experimenting with lattices, curves, codes
- **Magma:** Computational algebra (commercial, widely used in cryptography research)
- **FLINT/NTL:** Number theory libraries for algorithm prototyping
- **lattice-estimator:** Estimate concrete security of lattice parameters (https://github.com/malb/lattice-estimator)

### Implementation Development

```bash
# Building liboqs from source
git clone https://github.com/open-quantum-safe/liboqs
cd liboqs
mkdir build && cd build
cmake -DBUILD_SHARED_LIBS=ON ..
make -j$(nproc)
make install

# Running tests
make run_tests

# Benchmarking
./tests/speed_kem
./tests/speed_sig
```

```bash
# Using OpenSSL with PQC (oqs-provider)
git clone https://github.com/open-quantum-safe/oqs-provider
cd oqs-provider
mkdir build && cd build
cmake -DOPENSSL_ROOT_DIR=/path/to/openssl ..
make

# Generate ML-DSA key pair
openssl genpkey -algorithm mldsa65 -out mldsa_key.pem
openssl pkey -in mldsa_key.pem -pubout -out mldsa_pub.pem

# Sign a file
openssl dgst -sign mldsa_key.pem -out signature.bin document.pdf

# Verify signature
openssl dgst -verify mldsa_pub.pem -signature signature.bin document.pdf
```

### Container Images

```dockerfile
# Example: Dockerfile with PQC-enabled OpenSSL
FROM ubuntu:24.04

RUN apt-get update && apt-get install -y \
    build-essential cmake git \
    libssl-dev

# Build liboqs
RUN git clone --depth 1 https://github.com/open-quantum-safe/liboqs /opt/liboqs \
    && cd /opt/liboqs && mkdir build && cd build \
    && cmake -DBUILD_SHARED_LIBS=ON .. \
    && make -j$(nproc) && make install

# Build oqs-provider for OpenSSL
RUN git clone --depth 1 https://github.com/open-quantum-safe/oqs-provider /opt/oqs-provider \
    && cd /opt/oqs-provider && mkdir build && cd build \
    && cmake .. && make && make install
```

## C.6 Formal Verification Tools

| Tool | Purpose | Language |
|------|---------|----------|
| Jasmin | Verified assembly for crypto | Custom DSL → x86/ARM |
| EasyCrypt | Computer-aided cryptographic proofs | Custom |
| F*/HACL* | Verified C crypto implementations | F* → C |
| Coq | Theorem proving for correctness | Coq |
| ct-verif | Constant-time verification | LLVM IR |

## C.7 Online Resources

### Standards and Specifications

- NIST PQC: https://csrc.nist.gov/projects/post-quantum-cryptography
- FIPS 203 (ML-KEM): https://csrc.nist.gov/pubs/fips/203/final
- FIPS 204 (ML-DSA): https://csrc.nist.gov/pubs/fips/204/final
- FIPS 205 (SLH-DSA): https://csrc.nist.gov/pubs/fips/205/final

### Community and Research

- IACR ePrint Archive: https://eprint.iacr.org/ (latest cryptography research)
- PQC Forum: https://groups.google.com/a/list.nist.gov/g/pqc-forum
- Real World Crypto: https://rwc.iacr.org/ (annual conference)
- PQCrypto Conference: Biennial dedicated PQC conference

### Migration Guidance

- NIST SP 1800-38: Quantum Readiness: Migration to PQC
- BSI TR-02102: Cryptographic Mechanisms (updated for PQC)
- ETSI TR 103 619: Migration Strategies for PQC
- CISA PQC Resources: https://www.cisa.gov/quantum
