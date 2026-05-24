# Appendix C: Reference Implementations and Tools

This appendix catalogs the software libraries, protocol implementations, testing tools, and development resources available for working with post-quantum cryptography. The landscape evolves rapidly; URLs and version numbers are current as of the time of writing but should be verified against upstream sources.

## C.1 Cryptographic Libraries with PQC Support

### liboqs (Open Quantum Safe)

The Open Quantum Safe (OQS) project provides the most comprehensive open-source PQC library, serving as a reference integration point for multiple algorithms.

- **Language:** C99 (with language bindings for Python, Go, Java, .NET, Rust, C++)
- **Repository:** https://github.com/open-quantum-safe/liboqs
- **Algorithms:** All NIST standardized algorithms (ML-KEM, ML-DSA, SLH-DSA) plus candidates under evaluation (FN-DSA, HQC, BIKE, Classic McEliece)
- **Status:** Research and reference quality; suitable for prototyping and interoperability testing
- **License:** MIT
- **Key features:**
  - Uniform API across all algorithms
  - Pluggable architecture supporting multiple implementations per algorithm (reference, optimized, AVX2, ARM NEON)
  - Integration with OpenSSL via oqs-provider
  - Comprehensive test infrastructure including KAT verification
  - Performance benchmarking utilities
  - Regular updates tracking specification changes

The OQS project maintains several integration layers:
- **oqs-provider:** OpenSSL 3.x provider enabling PQC in any application using OpenSSL
- **oqs-demos:** Docker-based demonstrations of PQC in Apache, nginx, curl, and other applications
- **liboqs-python/go/java/dotnet:** Language-specific wrappers providing idiomatic APIs

### OpenSSL 3.5+

OpenSSL is the dominant TLS and cryptographic library in production deployments, making its PQC support critical for ecosystem-wide adoption.

- **Language:** C
- **Repository:** https://github.com/openssl/openssl
- **Algorithms:** ML-KEM-512/768/1024, ML-DSA-44/65/87, SLH-DSA (all parameter sets)
- **Status:** Production quality for standardized algorithms; FIPS module validation in progress
- **License:** Apache 2.0
- **Key features:**
  - Provider architecture enables modular algorithm addition without core library changes
  - Native ML-KEM and ML-DSA support integrated in OpenSSL 3.5
  - Hybrid key exchange support for TLS 1.3
  - Certificate generation and verification with PQC algorithms
  - FIPS 140-3 validated module (validation in progress for PQC algorithms)
  - EVP API provides algorithm-agnostic interface for applications

Configuration for PQC in OpenSSL:
- TLS hybrid key exchange groups: `x25519_mlkem768`, `secp384r1_mlkem1024`
- Signature algorithms: `mldsa65`, `mldsa87`, `slhdsa_sha2_128s`
- Certificate generation supports PQC key types via standard `-algorithm` parameter

### BoringSSL (Google)

Google's OpenSSL fork prioritizes simplicity, correctness, and deployment in Google services.

- **Language:** C/C++
- **Repository:** https://boringssl.googlesource.com/boringssl
- **Algorithms:** ML-KEM-768 (hybrid with X25519 for TLS key exchange)
- **Status:** Production (deployed in Chrome, Android, and Google Cloud services since 2023)
- **License:** ISC/OpenSSL dual license
- **Key features:**
  - Battle-tested in the largest TLS deployment in the world
  - Hybrid key exchange (X25519Kyber768) enabled by default in Chrome
  - Optimized implementations with AVX2/AVX-512 support
  - Constant-time implementation verified through tooling
  - Focused scope: TLS use cases only, not a general-purpose PQC library

BoringSSL's production deployment provides valuable real-world data on PQC performance, compatibility issues, and protocol behavior at Internet scale. Key lessons from their deployment include: middlebox interference with larger TLS ClientHello messages (addressed by splitting into multiple records), negligible performance impact of ML-KEM hybrid key exchange on typical web connections, and the importance of split-handshake architectures for managing PQC computation costs at load balancers.

Google's experience demonstrates that PQC hybrid key exchange can be deployed transparently at global scale with minimal user-visible impact. The slightly larger handshake messages (approximately 1.1 KB additional for ML-KEM-768) are well within normal network path MTU for TCP-based connections, though QUIC/UDP deployments required additional consideration for packet fragmentation boundaries.

### wolfSSL

An embedded-focused TLS library offering PQC support for resource-constrained devices.

- **Language:** C (ANSI C89 compatible)
- **Repository:** https://github.com/wolfSSL/wolfssl
- **Algorithms:** ML-KEM-512/768/1024, ML-DSA-44/65/87, SLH-DSA, XMSS, LMS
- **Status:** Production quality with FIPS 140-3 validation in progress
- **License:** GPLv2 (commercial licenses available)
- **Key features:**
  - Small footprint suitable for embedded systems (ARM Cortex-M, RISC-V)
  - Hardware acceleration support (ARM Cryptographic Extensions, Intel AES-NI/AVX2)
  - Stateful hash-based signature support (XMSS, LMS) with state management
  - Progressive algorithm implementation tracking NIST standardization
  - DO-178C, ISO 26262, and IEC 62443 certification paths
  - Integration with FreeRTOS, Zephyr, and bare-metal environments

wolfSSL is particularly relevant for IoT and automotive PQC deployment where memory and computation are severely constrained.

### PQClean

A community project providing clean, portable, and auditable reference implementations.

- **Language:** C (no dependencies beyond standard library)
- **Repository:** https://github.com/PQClean/PQClean
- **Algorithms:** All NIST Round 3+ candidates and standards, with multiple parameter sets
- **Status:** Reference quality; prioritizes correctness and readability over performance
- **License:** Various (per-algorithm, matching upstream submissions)
- **Key features:**
  - Strict coding standards: no dynamic memory allocation, no global state
  - Comprehensive test suites including functional tests, KAT verification, and memory safety checks
  - Each implementation is standalone (can be extracted independently)
  - API compatibility with NIST submission format
  - Continuous integration with sanitizers (ASan, MSan, UBSan)
  - Used as upstream source by many other projects (pqcrypto-rs, liboqs)

PQClean serves as the baseline for correctness comparison and as source material for higher-level libraries.

### CIRCL (Cloudflare Interoperable Reusable Cryptographic Library)

Cloudflare's Go cryptographic library with first-class PQC support.

- **Language:** Go
- **Repository:** https://github.com/cloudflare/circl
- **Algorithms:** ML-KEM-512/768/1024, ML-DSA-44/65/87, SLH-DSA (all parameter sets), X25519+ML-KEM-768 hybrid
- **Status:** Production quality (deployed across Cloudflare's network)
- **License:** BSD-3-Clause
- **Key features:**
  - Native Go implementation with assembly-optimized critical paths
  - Hybrid key exchange support matching IETF drafts
  - HPKE integration with PQC KEMs
  - Used in Cloudflare's production TLS termination (serving millions of connections per second)
  - Group-based API design enabling algorithm-agnostic code
  - CSIDH and SQISign experimental implementations for research

CIRCL demonstrates that PQC can be deployed at massive scale in production Go services.

### pqcrypto (Rust)

The Rust ecosystem's primary PQC library, leveraging Rust's memory safety guarantees.

- **Language:** Rust
- **Crates:** `pqcrypto`, `pqcrypto-kyber`, `pqcrypto-dilithium`, `pqcrypto-sphincsplus`
- **Repository:** https://github.com/rustpq/pqcrypto
- **Algorithms:** ML-KEM, ML-DSA, SLH-DSA, Classic McEliece, FN-DSA
- **Status:** Production quality for standardized algorithms
- **License:** MIT/Apache 2.0 dual license
- **Key features:**
  - Rust's type system prevents many classes of implementation bugs
  - No unsafe code in high-level API (unsafe confined to low-level optimization)
  - Zero-copy API design for performance
  - Serde integration for serialization
  - Wasm compilation target for browser-based PQC
  - Integration with RustCrypto ecosystem (traits, algorithms)

The `ml-kem` and `ml-dsa` crates from the RustCrypto project provide pure Rust implementations without C dependencies, offering an alternative to the PQClean-wrapping approach.

### Bouncy Castle

The dominant Java/C# cryptographic library for enterprise applications.

- **Language:** Java (bcprov/bcpqc), C# (bc-csharp)
- **Repository:** https://www.bouncycastle.org/
- **Algorithms:** ML-KEM, ML-DSA, SLH-DSA, FN-DSA, XMSS, LMS, Classic McEliece, BIKE, HQC, Picnic, Rainbow (deprecated)
- **Status:** Production quality
- **License:** MIT
- **Key features:**
  - Comprehensive Java Cryptography Architecture (JCA) provider
  - X.509 certificate generation and parsing with PQC algorithms
  - CMS (S/MIME) support for PQC signatures and encryption
  - PKCS#12 keystore support with PQC keys
  - TLS implementation with PQC key exchange and authentication
  - Long track record of enterprise deployment and security audits
  - Composite signature and KEM support per IETF drafts

Bouncy Castle is critical for Java enterprise migration to PQC, including application servers, PKI systems, and document signing.

### libsignal

Signal's cryptographic library implementing the Signal Protocol with post-quantum extensions.

- **Language:** Rust (with bindings for Java/Kotlin, Swift, TypeScript)
- **Repository:** https://github.com/signalapp/libsignal
- **Algorithms:** ML-KEM-1024 (within PQXDH protocol)
- **Status:** Production (deployed to billions of Signal users)
- **License:** AGPL 3.0
- **Key features:**
  - First major deployment of PQC in end-to-end encrypted messaging
  - PQXDH protocol combines X25519 with ML-KEM-1024 for initial key agreement
  - Post-quantum ratcheting for ongoing message encryption
  - Careful protocol design maintaining forward secrecy and deniability
  - Production-hardened against side channels and implementation attacks

### AWS LibCrypto (AWS-LC)

Amazon's cryptographic library for AWS services, forked from BoringSSL.

- **Language:** C/C++
- **Repository:** https://github.com/aws/aws-lc
- **Algorithms:** ML-KEM-768/1024, ML-DSA-65/87
- **Status:** Production (used in AWS services)
- **License:** Apache 2.0 and ISC
- **Key features:**
  - FIPS 140-3 validated
  - Optimized for cloud workloads (x86-64, ARM64)
  - Integrated with AWS SDK, s2n-tls, and AWS Nitro Enclaves
  - Formal verification of critical code paths using SAW
  - Supports PQC hybrid key exchange in TLS via s2n-tls

## C.2 Protocol Implementations

### TLS Libraries with PQC

| Library | PQC Key Exchange | PQC Authentication | Language | Status |
|---------|-----------------|-------------------|----------|--------|
| OpenSSL 3.5+ | ML-KEM hybrid (x25519_mlkem768) | ML-DSA, SLH-DSA | C | Production |
| BoringSSL | ML-KEM hybrid (X25519Kyber768Draft00) | In development | C/C++ | Production |
| s2n-tls (AWS) | ML-KEM hybrid | ML-DSA | C | Production |
| rustls | ML-KEM hybrid (via aws-lc-rs) | In development | Rust | Production |
| wolfSSL | ML-KEM hybrid | ML-DSA, SLH-DSA | C | Production |
| GnuTLS | ML-KEM hybrid | In development | C | Experimental |
| NSS (Mozilla) | ML-KEM hybrid | In development | C | Experimental |
| Mbed TLS | ML-KEM hybrid | ML-DSA | C | Experimental |
| Java JSSE | ML-KEM hybrid | ML-DSA (via Bouncy Castle) | Java | Experimental |

TLS PQC key exchange negotiation uses code points defined in IETF drafts. The most widely deployed combination is X25519+ML-KEM-768 (providing hybrid NIST Level 3 security). Authentication migration (PQC certificates) is proceeding more slowly due to certificate chain size concerns and PKI infrastructure dependencies.

### SSH Implementations

| Implementation | PQC Key Exchange | PQC Authentication | Notes |
|---------------|-----------------|-------------------|-------|
| OpenSSH 9.x+ | sntrup761x25519 (hybrid) | In development | sntrup761 is Streamlined NTRU Prime |
| OpenSSH (OQS) | ML-KEM hybrids | ML-DSA host/user keys | Research fork via liboqs integration |
| libssh | Via liboqs integration | Via liboqs integration | Library-level support |
| PuTTY | sntrup761x25519 | Experimental | Windows SSH client |
| Dropbear | Experimental | Experimental | Embedded SSH server |

OpenSSH's adoption of sntrup761 (a NTRU-based KEM) predates NIST standardization. Migration to ML-KEM-based key exchange is expected as IETF SSH PQC drafts mature. SSH host key authentication with ML-DSA requires updates to known_hosts formats and SSH certificate infrastructure.

### VPN and IPsec

| Implementation | PQC Support | Protocol | Notes |
|---------------|------------|----------|-------|
| strongSwan | ML-KEM hybrid in IKEv2 | RFC 9370 | Most mature PQC VPN |
| Libreswan | ML-KEM key exchange | IKEv2 | Experimental support |
| WireGuard + Rosenpass | ML-KEM overlay protocol | Custom | Separate PQC key agreement layer |
| OpenVPN | PQC via TLS library | TLS-based VPN | Inherits OpenSSL/wolfSSL PQC |
| Cisco IOS-XE | ML-KEM in IKEv2 | IKEv2 | Enterprise networking |
| Juniper Junos | PQC IKEv2 (planned) | IKEv2 | Enterprise networking |

RFC 9370 standardizes the framework for multiple key exchanges in IKEv2, enabling hybrid PQC deployment in IPsec VPNs. strongSwan provides the most mature open-source implementation with ML-KEM hybrid key exchange.

### Messaging Protocols

| Protocol/App | PQC Integration | Algorithm | Status |
|-------------|----------------|-----------|--------|
| Signal (PQXDH) | Initial key exchange | ML-KEM-1024 | Production |
| Signal (PQ ratchet) | Ongoing ratchet | ML-KEM-768 | Production |
| iMessage (PQ3) | Key exchange | ML-KEM-768 | Production |
| Matrix/Element | Vodozemac PQC | ML-KEM (planned) | Development |
| MLS (RFC 9420) | Key package | ML-KEM hybrid | Specification |

## C.3 Testing and Validation Tools

### Known Answer Test (KAT) Infrastructure

**NIST KAT Files:** Official test vectors for FIPS 203, 204, and 205, available from the NIST PQC project page. These include intermediate values enabling step-by-step validation of implementations.

**ACVP (Automated Cryptographic Validation Protocol):** NIST's framework for automated algorithm testing:
- Server: https://acvts.nist.gov/
- Specification: ACVP documents for ML-KEM, ML-DSA, SLH-DSA
- Client implementations: libacvp (Cisco), acvp-server (NIST reference)
- Tests: Key generation, encapsulation/decapsulation, signing/verification with various parameters
- Integration: Required for FIPS 140-3 module validation

**KAT generation tools:**
- PQClean includes KAT generators for all algorithms matching NIST format
- liboqs provides KAT verification as part of its test suite
- Algorithm-specific reference implementations include their own KAT generation

**Test vector format:** NIST KAT files use a request/response format:
```
count = 0
seed = [64 hex bytes]
pk = [public key hex]
sk = [secret key hex]
ct = [ciphertext hex]
ss = [shared secret hex]
```

### Side-Channel Analysis Tools

| Tool | Purpose | Type | Platform |
|------|---------|------|----------|
| ChipWhisperer | Power analysis, fault injection, glitching | Hardware + Python | CW-Lite, CW-Pro, CW-Husky boards |
| Langer EMV | EM near-field probes for side-channel measurement | Hardware | Oscilloscope integration |
| Riscure Inspector | Professional side-channel evaluation suite | Hardware + Software | Commercial platform |
| NewAE Scared | Side-channel analysis framework | Software (Python) | Open source |
| ctgrind | Constant-time checking via Valgrind instrumentation | Software | x86/x64 Linux |
| timecop | Timing leak detection through instruction tracing | Software | LLVM-based |
| dudect | Statistical timing analysis (Welch's t-test) | Software | C, platform-independent |
| DATA (Differential Address Trace Analysis) | Cache timing leak detection | Software | Pin-based instrumentation |
| ct-fuzz | Fuzzing for constant-time violations | Software | LLVM-based |
| ELMO | Power model for ARM Cortex-M | Software | Simulation-based |
| Microwalk | Microarchitectural timing leakage detection | Software | Intel Pin framework |

Side-channel analysis methodology for PQC implementations:
1. **Profiling phase:** Collect power/EM traces during algorithm execution with known keys
2. **Attack phase:** Apply statistical techniques (DPA, CPA, template attacks) to recover keys
3. **Validation:** Confirm key recovery success rate and required trace count
4. **Specific PQC targets:** NTT butterfly twiddle factors, rejection sampling loops, Gaussian sampling, decapsulation comparison

### Benchmarking Frameworks

**SUPERCOP (System for Unified Performance Evaluation Related to Cryptographic Operations and Primitives):**
- URL: https://bench.cr.yp.to/supercop.html
- Provides standardized benchmarking across all cryptographic primitives
- Supports multiple platforms and compilers
- Results published at https://bench.cr.yp.to/results-kem.html
- Includes cycle counts, key sizes, and signature/ciphertext sizes

**PQM4 (Post-Quantum Crypto for ARM Cortex-M4):**
- Repository: https://github.com/mupq/pqm4
- Benchmarks PQC algorithms on the STM32F4 Discovery board
- Measures cycle counts, stack usage, and code size
- Critical for evaluating PQC feasibility on embedded platforms
- Includes implementations optimized for ARM Cortex-M4 (e.g., using UMAAL instruction)

**pqax (PQC on ARM Cortex-A):**
- Repository: https://github.com/mupq/pqax
- Benchmarks on application-class ARM processors (Cortex-A72, Apple M1/M2)
- Tests NEON vectorization effectiveness

**liboqs speed tests:**
- Built into liboqs: `./tests/speed_kem` and `./tests/speed_sig`
- Measures key generation, encapsulation/decapsulation, sign/verify times
- Reports cycles and wall-clock time
- Supports algorithm comparison across all implemented schemes

**Criterion.rs / Google Benchmark:**
- Statistical benchmarking frameworks used within Rust and C++ PQC implementations
- Provide statistical confidence intervals and regression detection
- Integrated into CI/CD pipelines for performance monitoring

### Interoperability Testing

**OQS Interop Tests:** Cross-library interoperability validation ensuring implementations produce compatible outputs:
- Key exchange interoperability between liboqs, BoringSSL, wolfSSL
- Certificate generation and verification across libraries
- TLS handshake testing with mixed client/server implementations

**NIST PQC Interoperability Events:** Periodic testing events organized by NIST:
- Validate algorithm implementations against specification
- Test interoperability between vendors
- Identify specification ambiguities

**Wycheproof-style Testing:** Edge case and malformed input testing:
- Invalid public keys (points not on curve, incorrect length)
- Malformed ciphertexts (wrong size, invalid encoding)
- Boundary value testing (maximum/minimum parameter values)
- Test vectors for error handling and implicit rejection

**IETF Hackathons:** Multi-vendor interoperability events at IETF meetings:
- TLS 1.3 with PQC hybrid key exchange
- Certificate chain validation with PQC signatures
- SSH key exchange interoperability
- Protocol-level testing beyond algorithm correctness

## C.4 Discovery and Inventory Tools

### Cryptographic Discovery

| Tool | Function | Type | Key Features |
|------|----------|------|-------------|
| Cryptosense Analyzer | Application crypto discovery via API monitoring | Commercial | Runtime analysis, identifies weak crypto usage patterns |
| IBM Quantum Safe Explorer | Static code scanning for crypto | Commercial | Identifies crypto libraries, algorithms, key sizes in source code |
| InfoSec Global AgileSec | Network crypto discovery | Commercial | Passive network monitoring, protocol analysis |
| Symantec/Broadcom Crypto Discovery | Enterprise crypto inventory | Commercial | Certificate and key management integration |
| sslyze | TLS configuration scanning | Open source | Tests server TLS configuration including PQC group support |
| testssl.sh | Comprehensive TLS/SSL testing | Open source | Shell script, tests all TLS parameters |
| ssh-audit | SSH configuration analysis | Open source | Python-based, checks SSH algorithms and key sizes |
| CycloneDX CLI | CBOM generation | Open source | Produces machine-readable crypto inventories |
| OWASP Dependency-Check | Dependency vulnerability scanning | Open source | Identifies libraries with crypto vulnerabilities |
| Anchore/Syft | Container SBOM/CBOM | Open source | Scans container images for crypto libraries |

Discovery methodology for PQC migration:
1. **Network scanning:** Identify all TLS, SSH, VPN, and other crypto protocol endpoints
2. **Code analysis:** Scan source code and binaries for cryptographic API calls and library usage
3. **Certificate inventory:** Catalog all X.509 certificates, their algorithms, and expiration dates
4. **Key management audit:** Map HSMs, key stores, and key lifecycle processes
5. **Data classification:** Identify data with long-term confidentiality requirements (HNDL-vulnerable)
6. **Prioritization:** Rank assets by quantum vulnerability and migration complexity

### Certificate Management

| Tool | Function | PQC Support | Type |
|------|----------|-------------|------|
| cert-manager (Kubernetes) | Automated certificate lifecycle | PQC CAs via external issuers | Open source |
| Venafi Trust Protection Platform | Enterprise certificate management | PQC certificate inventory/planning | Commercial |
| DigiCert CertCentral | Public CA with certificate management | PQC hybrid certificates (pilot) | Commercial |
| Sectigo Certificate Manager | CA and certificate lifecycle | PQC readiness assessment | Commercial |
| Let's Encrypt (ISRG) | Automated free certificates | PQC roadmap published | Open source |
| Step CA (Smallstep) | Private CA with ACME support | ML-DSA, SLH-DSA support | Open source |
| EJBCA | Enterprise CA software | PQC algorithm support | Open source |
| HashiCorp Vault PKI | Secrets management and PKI | PQC plugin development | Open source |
| Keyfactor EJBCA/Command | Certificate lifecycle platform | PQC migration planning | Commercial |

Certificate management considerations for PQC:
- PQC certificates are significantly larger (ML-DSA-65: ~4 KB vs. ECDSA: ~300 bytes for a signature)
- Certificate chains may need compression (RFC 8879) or pruning
- Hybrid certificates require dual validation paths
- Certificate transparency logs must accommodate larger entries
- OCSP and CRL distribution handles larger signed responses

## C.5 Development and Debugging Tools

### Algorithm Exploration and Research

**SageMath:**
- The premier open-source mathematical software for cryptography research
- Built-in support for finite fields, polynomial rings, lattices, elliptic curves
- Lattice reduction (LLL, BKZ via fpLLL), ideal arithmetic, isogeny computation
- Python-based interface enabling rapid prototyping
- Example: Exploring ML-KEM parameters

```python
# SageMath: Exploring ML-KEM ring structure
q = 3329; n = 256
R.<x> = PolynomialRing(GF(q))
Rq = R.quotient(x^n + 1)

# Verify NTT root of unity
omega = GF(q)(17)
assert omega^(2*n) == 1
assert omega^n == q-1  # omega^256 = -1 mod 3329

# Sample a small polynomial (like CBD_2)
from random import randint
def sample_cbd(eta):
    coeffs = []
    for i in range(n):
        a = sum(randint(0,1) for _ in range(eta))
        b = sum(randint(0,1) for _ in range(eta))
        coeffs.append(a - b)
    return Rq(coeffs)

s = sample_cbd(2)
print(f"Secret polynomial norm: {sqrt(sum(int(c)^2 for c in s.list())):.2f}")
```

**Magma Computational Algebra System:**
- Commercial system widely used in number theory and algebraic geometry research
- High-performance implementations of lattice algorithms
- Elliptic curve and isogeny computation
- Used extensively in PQC cryptanalysis research
- Strongest for algebraic number theory computations

**FLINT (Fast Library for Number Theory):**
- Repository: https://github.com/flintlib/flint
- High-performance C library for number theory
- Polynomial arithmetic, finite fields, linear algebra over Z and Z_q
- Basis for many research implementations

**NTL (Number Theory Library):**
- Victor Shoup's C++ library for number theory
- Lattice reduction (LLL/BKZ), polynomial arithmetic
- Used in many lattice cryptography research papers
- Well-documented and battle-tested

**lattice-estimator:**
- Repository: https://github.com/malb/lattice-estimator
- Python/SageMath tool for estimating concrete security of lattice parameters
- Models: primal attack, dual attack, enumeration, sieving
- Used by NIST and PQC community for parameter selection
- Input: LWE parameters (n, q, error distribution); Output: estimated bit security

```python
# Using lattice-estimator to analyze ML-KEM-768 parameters
from estimator import *

params = LWE.Parameters(
    n=768,
    q=3329,
    Xs=ND.CenteredBinomial(2),  # Secret distribution CBD_2
    Xe=ND.CenteredBinomial(2),  # Error distribution CBD_2
)

# Estimate security against various attacks
result = LWE.estimate(params)
print(result)
```

### Implementation Development

```bash
# Building liboqs from source with all optimizations
git clone --depth 1 https://github.com/open-quantum-safe/liboqs
cd liboqs
mkdir build && cd build
cmake -GNinja \
    -DBUILD_SHARED_LIBS=ON \
    -DCMAKE_BUILD_TYPE=Release \
    -DOQS_USE_OPENSSL=ON \
    -DOQS_DIST_BUILD=ON \
    -DOQS_ENABLE_KEM_ML_KEM=ON \
    -DOQS_ENABLE_SIG_ML_DSA=ON \
    -DOQS_ENABLE_SIG_SLH_DSA=ON \
    ..
ninja
ninja install

# Running the full test suite
ninja run_tests

# Performance benchmarking
./tests/speed_kem --duration 5 --filter ML-KEM
./tests/speed_sig --duration 5 --filter ML-DSA

# KAT verification
./tests/kat_kem
./tests/kat_sig
```

```bash
# Using OpenSSL with PQC (via oqs-provider or native 3.5+)
# Generate ML-DSA-65 key pair
openssl genpkey -algorithm mldsa65 -out mldsa_key.pem
openssl pkey -in mldsa_key.pem -pubout -out mldsa_pub.pem

# Examine key details
openssl pkey -in mldsa_key.pem -text -noout

# Sign a document
openssl dgst -sign mldsa_key.pem -out signature.bin document.pdf

# Verify a signature
openssl dgst -verify mldsa_pub.pem -signature signature.bin document.pdf

# Generate ML-KEM-768 key pair
openssl genpkey -algorithm mlkem768 -out mlkem_key.pem
openssl pkey -in mlkem_key.pem -pubout -out mlkem_pub.pem

# Generate a self-signed certificate with ML-DSA
openssl req -new -x509 -key mldsa_key.pem \
    -out cert.pem -days 365 \
    -subj "/CN=PQC Test/O=Example"

# Examine certificate
openssl x509 -in cert.pem -text -noout

# Test TLS server with PQC
openssl s_server -cert cert.pem -key mldsa_key.pem \
    -groups x25519_mlkem768 -port 4433

# Test TLS client with PQC
openssl s_client -connect localhost:4433 \
    -groups x25519_mlkem768
```

```bash
# Using CIRCL (Go) for PQC operations
cat > pqc_example.go << 'EOF'
package main

import (
    "fmt"
    "github.com/cloudflare/circl/kem/mlkem/mlkem768"
    "github.com/cloudflare/circl/sign/mldsa/mldsa65"
)

func main() {
    // ML-KEM-768 key exchange
    pk, sk, _ := mlkem768.GenerateKeyPair(nil)
    ct, ss1, _ := mlkem768.Encapsulate(nil, pk)
    ss2, _ := mlkem768.Decapsulate(sk, ct)
    fmt.Printf("KEM shared secrets match: %v\n", ss1 == ss2)
    fmt.Printf("Public key size: %d bytes\n", len(pk.Bytes()))
    fmt.Printf("Ciphertext size: %d bytes\n", len(ct))

    // ML-DSA-65 signing
    pubKey, privKey, _ := mldsa65.GenerateKey(nil)
    msg := []byte("Hello, post-quantum world!")
    sig, _ := mldsa65.Sign(privKey, msg, nil)
    valid := mldsa65.Verify(pubKey, msg, sig)
    fmt.Printf("Signature valid: %v\n", valid)
    fmt.Printf("Signature size: %d bytes\n", len(sig))
}
EOF
```

### Container Images for PQC Development

```dockerfile
# Dockerfile: Complete PQC development environment
FROM ubuntu:24.04 AS builder

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    build-essential cmake ninja-build git \
    libssl-dev python3-dev python3-pip \
    astyle valgrind \
    && rm -rf /var/lib/apt/lists/*

# Build liboqs
RUN git clone --depth 1 --branch main \
    https://github.com/open-quantum-safe/liboqs /opt/liboqs \
    && cd /opt/liboqs && mkdir build && cd build \
    && cmake -GNinja -DBUILD_SHARED_LIBS=ON \
       -DCMAKE_INSTALL_PREFIX=/usr/local .. \
    && ninja && ninja install

# Build OpenSSL with oqs-provider
RUN git clone --depth 1 \
    https://github.com/open-quantum-safe/oqs-provider /opt/oqs-provider \
    && cd /opt/oqs-provider && mkdir build && cd build \
    && cmake -GNinja .. && ninja && ninja install

# Configure OpenSSL to load oqs-provider
RUN echo '[openssl_init]\nproviders = provider_sect\n\
[provider_sect]\noqsprovider = oqsprovider_sect\ndefault = default_sect\n\
[default_sect]\nactivate = 1\n[oqsprovider_sect]\n\
activate = 1\nmodule = /usr/local/lib/ossl-modules/oqsprovider.so' \
    > /usr/local/ssl/openssl.cnf

FROM ubuntu:24.04
COPY --from=builder /usr/local /usr/local
ENV LD_LIBRARY_PATH=/usr/local/lib
RUN ldconfig

# Verify installation
RUN openssl list -kem-algorithms | grep -i ml && \
    openssl list -signature-algorithms | grep -i ml
```

```bash
# Docker Compose for PQC interoperability testing
# docker-compose.yml
cat > docker-compose.yml << 'EOF'
version: '3.8'
services:
  pqc-server:
    image: openquantumsafe/oqs-openssl
    command: openssl s_server -cert /certs/server.pem -key /certs/server.key
             -groups x25519_mlkem768 -port 443 -www
    ports: ["4433:443"]
    volumes: ["./certs:/certs"]

  pqc-client:
    image: openquantumsafe/curl
    command: curl --curves x25519_mlkem768 https://pqc-server:443/
    depends_on: [pqc-server]
EOF
```

## C.6 Formal Verification Tools

Formal verification provides mathematical guarantees about implementation correctness and security properties, going beyond testing to prove absence of bugs.

| Tool | Purpose | Input Language | Output | Notable Results |
|------|---------|---------------|--------|-----------------|
| Jasmin | Verified high-performance crypto assembly | Jasmin DSL | x86-64, ARM64 assembly | Verified ML-KEM, Kyber implementations |
| EasyCrypt | Computer-aided cryptographic proofs | Custom procedural language | Proof certificates | ML-KEM IND-CCA2 proof |
| F*/HACL* | Verified C crypto implementations | F* (ML dialect) | Portable C via KaRaMeL | Verified Curve25519, SHA-3, ChaCha20 |
| Coq/Mathcomp | General theorem proving | Gallina (Coq) | Proof objects | Foundational crypto proofs |
| Isabelle/HOL | Interactive theorem prover | Isabelle theory files | Proof documents | Protocol verification |
| ct-verif | Constant-time verification of binaries | LLVM IR | Pass/fail + counterexample | Verified constant-time NTT |
| SAW (Software Analysis Workbench) | Equivalence checking against specification | Cryptol + LLVM/JVM | Proof of equivalence | AWS-LC verification |
| CryptoLine | Algebraic verification of assembly | Annotated assembly | Correctness proofs | Verified modular arithmetic |
| Vale | Verified assembly framework | Vale DSL | x86-64, ARM64 | Microsoft's verified crypto |

Formal verification achievements in PQC:
- **Jasmin ML-KEM:** Fully verified implementation of ML-KEM-768 producing assembly code with proven functional correctness (output matches specification) and constant-time execution
- **EasyCrypt ML-KEM:** Machine-checked proof that ML-KEM satisfies IND-CCA2 security assuming Module-LWE hardness in the QROM
- **HACL*:** Verified C implementations of hash functions used within PQC (SHA-3, SHAKE)
- **ct-verif:** Verified absence of timing leaks in NTT implementations used by ML-KEM/ML-DSA

## C.7 Hardware and Accelerator Support

### FPGA Implementations

| Platform | Algorithm | Performance | Resource Usage |
|----------|-----------|-------------|----------------|
| Xilinx Artix-7 | ML-KEM-768 | ~50 μs keygen, ~65 μs encaps | ~15K LUTs, ~20 BRAMs |
| Xilinx Zynq UltraScale+ | ML-KEM-1024 | ~25 μs keygen | ~25K LUTs |
| Intel Cyclone V | ML-DSA-65 | ~200 μs sign | ~30K ALMs |
| Lattice iCE40 | ML-KEM-512 | ~5 ms encaps | ~5K LUTs |

FPGA implementations are critical for high-throughput applications (TLS termination, HSMs) and for embedded systems requiring hardware acceleration.

### ASIC and SoC Integration

Several vendors are developing PQC hardware accelerators:
- **PQShield:** PQC IP cores for ASIC integration (ML-KEM, ML-DSA, SLH-DSA)
- **Xiphera:** FPGA/ASIC crypto IP including PQC
- **Rambus:** DPA-resistant PQC hardware implementations
- **ARM CryptoCell:** PQC acceleration in future generations

### Platform Crypto Support

| Platform | PQC Status | Algorithms | Notes |
|----------|-----------|------------|-------|
| Windows CNG | Preview | ML-KEM, ML-DSA | SymCrypt backend |
| macOS/iOS CryptoKit | Preview | ML-KEM | Apple Security framework |
| Android Keystore | Planned | ML-KEM, ML-DSA | Via Conscrypt/BoringSSL |
| Linux Kernel Crypto API | Patches submitted | ML-KEM | In-kernel PQC for IKE/TLS |
| Java JCA/JCE | Available | ML-KEM, ML-DSA | Via Bouncy Castle provider |
| .NET Cryptography | Preview | ML-KEM, ML-DSA | System.Security.Cryptography |

## C.8 Online Resources and Documentation

### Standards and Specifications

- **NIST PQC Project:** https://csrc.nist.gov/projects/post-quantum-cryptography
- **FIPS 203 (ML-KEM):** https://csrc.nist.gov/pubs/fips/203/final
- **FIPS 204 (ML-DSA):** https://csrc.nist.gov/pubs/fips/204/final
- **FIPS 205 (SLH-DSA):** https://csrc.nist.gov/pubs/fips/205/final
- **NIST SP 800-208:** https://csrc.nist.gov/pubs/sp/800-208/final (Stateful HBS)
- **NIST SP 1800-38:** Migration to Post-Quantum Cryptography (practice guide)

### IETF Specifications

- **draft-ietf-tls-hybrid-design:** Hybrid key exchange in TLS 1.3
- **draft-ietf-lamps-pq-composite-sigs:** Composite ML-DSA for X.509/CMS
- **draft-ietf-lamps-pq-composite-kem:** Composite ML-KEM for X.509/CMS
- **draft-ietf-lamps-dilithium-certificates:** ML-DSA in X.509 certificates
- **draft-connolly-tls-mlkem-key-agreement:** ML-KEM key agreement for TLS
- **RFC 9370:** Multiple Key Exchanges in IKEv2

### Community and Research

- **IACR ePrint Archive:** https://eprint.iacr.org/ (latest cryptography research preprints)
- **PQC Forum (NIST):** https://groups.google.com/a/list.nist.gov/g/pqc-forum
- **Open Quantum Safe:** https://openquantumsafe.org/
- **PQCA (Post-Quantum Cryptography Alliance):** https://pqca.org/ (Linux Foundation)
- **PQCrypto Conference:** Biennial academic conference dedicated to PQC research
- **Real World Crypto:** https://rwc.iacr.org/ (annual applied cryptography conference)

### Migration Guidance Documents

- **NIST SP 1800-38:** Quantum Readiness: Migration to Post-Quantum Cryptography
- **BSI TR-02102:** Cryptographic Mechanisms (updated annually with PQC recommendations)
- **ANSSI:** Avis relatif à la migration vers la cryptographie post-quantique
- **ETSI TR 103 619:** Migration Strategies and Recommendations for Quantum-Safe Cryptography
- **CISA:** Post-Quantum Cryptography Resources (https://www.cisa.gov/quantum)
- **NSA CNSA 2.0:** Cybersecurity Advisory on PQC transition timeline
- **Canadian Centre for Cyber Security:** Guidance on PQC migration for Canadian organizations

## C.9 Detailed Usage Examples

### ML-KEM Key Exchange in Python (via liboqs)

```python
# pip install liboqs-python
import oqs

# ML-KEM-768 Key Encapsulation
kem_name = "ML-KEM-768"

# Key Generation (performed by recipient)
with oqs.KeyEncapsulation(kem_name) as kem:
    public_key = kem.generate_keypair()
    secret_key = kem.export_secret_key()
    print(f"Public key size: {len(public_key)} bytes")
    print(f"Secret key size: {len(secret_key)} bytes")

# Encapsulation (performed by sender using recipient's public key)
with oqs.KeyEncapsulation(kem_name) as kem_sender:
    ciphertext, shared_secret_sender = kem_sender.encap_secret(public_key)
    print(f"Ciphertext size: {len(ciphertext)} bytes")
    print(f"Shared secret size: {len(shared_secret_sender)} bytes")

# Decapsulation (performed by recipient using their secret key)
with oqs.KeyEncapsulation(kem_name, secret_key) as kem_recipient:
    shared_secret_recipient = kem_recipient.decap_secret(ciphertext)

assert shared_secret_sender == shared_secret_recipient
print("Key exchange successful!")

# Available parameter sets
print("\nAvailable ML-KEM variants:")
for alg in oqs.get_enabled_kem_mechanisms():
    if "ML-KEM" in alg:
        with oqs.KeyEncapsulation(alg) as k:
            details = k.details
            print(f"  {alg}: pk={details['length_public_key']}B, "
                  f"ct={details['length_ciphertext']}B, "
                  f"ss={details['length_shared_secret']}B")
```

### ML-DSA Signing in Python (via liboqs)

```python
import oqs

# ML-DSA-65 Digital Signature
sig_name = "ML-DSA-65"

# Key Generation
with oqs.Signature(sig_name) as signer:
    public_key = signer.generate_keypair()
    secret_key = signer.export_secret_key()
    print(f"Public key: {len(public_key)} bytes")
    print(f"Secret key: {len(secret_key)} bytes")

    # Signing
    message = b"This message is authenticated with ML-DSA-65"
    signature = signer.sign(message)
    print(f"Signature: {len(signature)} bytes")

# Verification (by any party with the public key)
with oqs.Signature(sig_name) as verifier:
    is_valid = verifier.verify(message, signature, public_key)
    print(f"Signature valid: {is_valid}")

    # Tampered message should fail verification
    tampered = message + b"!"
    try:
        verifier.verify(tampered, signature, public_key)
        print("ERROR: Tampered message verified!")
    except Exception:
        print("Tampered message correctly rejected")
```

### Hybrid TLS Configuration (nginx with OpenSSL)

```nginx
# nginx.conf - PQC hybrid TLS configuration
server {
    listen 443 ssl;
    server_name example.com;

    # PQC certificate (ML-DSA-65 signed)
    ssl_certificate /etc/nginx/certs/server-mldsa65.pem;
    ssl_certificate_key /etc/nginx/certs/server-mldsa65-key.pem;

    # Fallback classical certificate for non-PQC clients
    ssl_certificate /etc/nginx/certs/server-ecdsa.pem;
    ssl_certificate_key /etc/nginx/certs/server-ecdsa-key.pem;

    # Hybrid key exchange groups (PQC + classical)
    ssl_ecdh_curve x25519_mlkem768:X25519:P-256;

    # TLS 1.3 only for PQC
    ssl_protocols TLSv1.3;
    ssl_prefer_server_ciphers off;

    # Signature algorithms preference
    ssl_conf_command SignatureAlgorithms mldsa65:ecdsa_secp384r1_sha384:rsa_pss_rsae_sha256;
}
```

### Rust Implementation Example

```rust
// Cargo.toml dependency: ml-kem = "0.1"
use ml_kem::{MlKem768, KemCore};
use ml_kem::kem::{Encapsulate, Decapsulate};
use rand::rngs::OsRng;

fn main() {
    // Key Generation
    let (dk, ek) = MlKem768::generate(&mut OsRng);

    // Encapsulation
    let (ct, ss_sender) = ek.encapsulate(&mut OsRng).unwrap();

    // Decapsulation
    let ss_recipient = dk.decapsulate(&ct).unwrap();

    assert_eq!(ss_sender.as_bytes(), ss_recipient.as_bytes());
    println!("ML-KEM-768 key exchange successful");
    println!("Shared secret: {} bytes", ss_sender.as_bytes().len());
}
```

### Java Implementation with Bouncy Castle

```java
import org.bouncycastle.pqc.crypto.mlkem.*;
import org.bouncycastle.pqc.crypto.mldsa.*;
import org.bouncycastle.crypto.AsymmetricCipherKeyPair;
import java.security.SecureRandom;

public class PQCExample {
    public static void main(String[] args) {
        // ML-KEM-768 Key Encapsulation
        MLKEMKeyPairGenerator kemGen = new MLKEMKeyPairGenerator();
        kemGen.init(new MLKEMKeyGenerationParameters(
            new SecureRandom(), MLKEMParameters.ml_kem_768));
        AsymmetricCipherKeyPair kemKeyPair = kemGen.generateKeyPair();

        // Encapsulation
        MLKEMEncapsulator encapsulator = new MLKEMEncapsulator();
        encapsulator.init(kemKeyPair.getPublic());
        SecretWithEncapsulation encapsulated = encapsulator.encapsulate();
        byte[] ciphertext = encapsulated.getEncapsulation();
        byte[] sharedSecret1 = encapsulated.getSecret();

        // Decapsulation
        MLKEMDecapsulator decapsulator = new MLKEMDecapsulator();
        decapsulator.init(kemKeyPair.getPrivate());
        byte[] sharedSecret2 = decapsulator.decapsulate(ciphertext);

        assert java.util.Arrays.equals(sharedSecret1, sharedSecret2);
        System.out.println("ML-KEM-768 successful, shared secret: " +
            sharedSecret1.length + " bytes");

        // ML-DSA-65 Signing
        MLDSAKeyPairGenerator sigGen = new MLDSAKeyPairGenerator();
        sigGen.init(new MLDSAKeyGenerationParameters(
            new SecureRandom(), MLDSAParameters.ml_dsa_65));
        AsymmetricCipherKeyPair sigKeyPair = sigGen.generateKeyPair();

        MLDSASigner signer = new MLDSASigner();
        signer.init(true, sigKeyPair.getPrivate());
        byte[] message = "Hello PQC".getBytes();
        byte[] signature = signer.generateSignature(message);

        signer.init(false, sigKeyPair.getPublic());
        boolean valid = signer.verifySignature(message, signature);
        System.out.println("ML-DSA-65 signature valid: " + valid);
    }
}
```

## C.10 Performance Comparison Tables

### KEM Performance (x86-64, Intel Core i7-12700, single core)

| Algorithm | KeyGen (μs) | Encaps (μs) | Decaps (μs) | PK (bytes) | CT (bytes) | SS (bytes) |
|-----------|-------------|-------------|-------------|------------|------------|------------|
| ML-KEM-512 | 12 | 15 | 17 | 800 | 768 | 32 |
| ML-KEM-768 | 20 | 24 | 26 | 1,184 | 1,088 | 32 |
| ML-KEM-1024 | 30 | 35 | 38 | 1,568 | 1,568 | 32 |
| X25519 (classical) | 48 | 48 | 48 | 32 | 32 | 32 |
| RSA-2048 (classical) | 82,000 | 18 | 640 | 256 | 256 | 32 |
| HQC-128 | 65 | 125 | 170 | 2,249 | 4,497 | 64 |
| Classic McEliece 348864 | 250,000 | 42 | 120 | 261,120 | 128 | 32 |

### Signature Performance (x86-64, Intel Core i7-12700, single core)

| Algorithm | KeyGen (μs) | Sign (μs) | Verify (μs) | PK (bytes) | Sig (bytes) |
|-----------|-------------|-----------|-------------|------------|-------------|
| ML-DSA-44 | 25 | 80 | 28 | 1,312 | 2,420 |
| ML-DSA-65 | 42 | 140 | 45 | 1,952 | 3,309 |
| ML-DSA-87 | 65 | 210 | 70 | 2,592 | 4,627 |
| SLH-DSA-SHA2-128s | 3,200 | 52,000 | 2,800 | 32 | 7,856 |
| SLH-DSA-SHA2-128f | 450 | 8,500 | 520 | 32 | 17,088 |
| SLH-DSA-SHAKE-256f | 1,800 | 35,000 | 2,100 | 64 | 49,856 |
| FN-DSA-512 | 8,500 | 320 | 55 | 897 | 666 |
| FN-DSA-1024 | 18,000 | 680 | 110 | 1,793 | 1,280 |
| Ed25519 (classical) | 20 | 48 | 70 | 32 | 64 |
| RSA-2048 (classical) | 82,000 | 1,200 | 18 | 256 | 256 |

### Embedded Performance (ARM Cortex-M4 @ 168 MHz)

| Algorithm | KeyGen (kcycles) | Encaps/Sign (kcycles) | Decaps/Verify (kcycles) | Stack (bytes) |
|-----------|-----------------|----------------------|------------------------|---------------|
| ML-KEM-512 | 580 | 740 | 790 | 2,400 |
| ML-KEM-768 | 960 | 1,200 | 1,260 | 3,200 |
| ML-KEM-1024 | 1,450 | 1,800 | 1,870 | 4,100 |
| ML-DSA-44 | 1,500 | 5,800 | 1,600 | 28,000 |
| ML-DSA-65 | 2,500 | 8,200 | 2,600 | 40,000 |
| SLH-DSA-SHA2-128s | 1.2M | 18M | 1.0M | 3,500 |

## C.11 Build System Integration

### CMake Integration with liboqs

```cmake
# CMakeLists.txt for a project using liboqs
cmake_minimum_required(VERSION 3.16)
project(pqc_application)

find_package(liboqs REQUIRED)

add_executable(pqc_app main.c)
target_link_libraries(pqc_app PRIVATE OQS::oqs)

# Enable ASAN for development
if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    target_compile_options(pqc_app PRIVATE -fsanitize=address,undefined)
    target_link_options(pqc_app PRIVATE -fsanitize=address,undefined)
endif()
```

### Go Module Integration

```go
// go.mod
module github.com/example/pqc-service

go 1.22

require (
    github.com/cloudflare/circl v1.3.7
    golang.org/x/crypto v0.21.0
)
```

### Rust Cargo Integration

```toml
# Cargo.toml for a PQC application
[package]
name = "pqc-service"
version = "0.1.0"
edition = "2021"

[dependencies]
ml-kem = { version = "0.1", features = ["std"] }
ml-dsa = { version = "0.1", features = ["std"] }
slh-dsa = "0.1"
rand = "0.8"
sha3 = "0.10"

[dev-dependencies]
criterion = "0.5"
hex = "0.4"

[[bench]]
name = "pqc_benchmarks"
harness = false
```

## C.12 Continuous Integration and Testing

### GitHub Actions Workflow for PQC Testing

```yaml
# .github/workflows/pqc-test.yml
name: PQC Algorithm Tests
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        algorithm: [ML-KEM-768, ML-DSA-65, SLH-DSA-SHA2-128f]
    steps:
      - uses: actions/checkout@v4

      - name: Install liboqs
        run: |
          sudo apt-get update
          sudo apt-get install -y cmake ninja-build
          git clone --depth 1 https://github.com/open-quantum-safe/liboqs
          cd liboqs && mkdir build && cd build
          cmake -GNinja -DCMAKE_INSTALL_PREFIX=/usr/local ..
          ninja && sudo ninja install
          sudo ldconfig

      - name: Run PQC tests
        run: |
          cmake -B build -DCMAKE_BUILD_TYPE=Release
          cmake --build build
          ctest --test-dir build --output-on-failure

      - name: Run constant-time checks
        run: |
          cmake -B build-ct -DCMAKE_BUILD_TYPE=Debug \
            -DENABLE_CT_TESTING=ON
          cmake --build build-ct
          valgrind --tool=memcheck ./build-ct/tests/ct_test_${{ matrix.algorithm }}

  interop:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Cross-library interoperability
        run: |
          # Generate keys with liboqs, verify with OpenSSL
          ./tests/interop/run_interop_tests.sh

  benchmark:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Performance regression check
        run: |
          cmake -B build -DCMAKE_BUILD_TYPE=Release
          cmake --build build
          ./build/bench/pqc_bench --benchmark_out=results.json
          python3 scripts/check_regression.py results.json baseline.json
```

### Constant-Time Verification in CI

```bash
#!/bin/bash
# Script: verify_constant_time.sh
# Verifies that PQC implementations have no timing leaks

# Method 1: Using ctgrind (Valgrind-based)
valgrind --tool=memcheck \
    --track-origins=yes \
    --error-exitcode=1 \
    ./tests/ct_mlkem768

# Method 2: Using dudect (statistical timing analysis)
./tests/dudect_mlkem768_decaps \
    --number-measurements 1000000 \
    --threshold 10.0

# Method 3: Using timecop
./tests/timecop_mlkem768 2>&1 | grep -c "TIMING LEAK" | \
    xargs -I{} test {} -eq 0
```

## C.13 Debugging and Troubleshooting

### Common Issues and Solutions

**Issue: ML-KEM decapsulation produces wrong shared secret**
- Check: Are public key bytes correctly serialized (compressed representation)?
- Check: Is the NTT domain correctly handled (forward vs. inverse)?
- Check: Are coefficients properly centered (symmetric vs. unsigned representation)?
- Tool: Compare intermediate values against NIST KAT files

**Issue: ML-DSA signature verification fails**
- Check: Is the message hash correctly bound to context/pre-hash mode?
- Check: Is the challenge polynomial correctly reconstructed from hash output?
- Check: Are coefficient bounds (γ₁, γ₂) applied correctly in hint computation?
- Tool: Enable verbose logging of intermediate values and compare against reference

**Issue: Performance regression after optimization**
- Check: Verify functional correctness first (run KAT tests)
- Check: Ensure optimized code paths are actually being exercised (check CPU feature detection)
- Tool: Use `perf stat` to identify bottleneck (cache misses, branch mispredictions)

**Issue: Side-channel leakage detected**
- Check: Secret-dependent branches in NTT butterfly selection
- Check: Secret-dependent table lookups (rejection sampling, encode/decode)
- Check: Variable-time division or modular reduction
- Tool: Run dudect with increased measurement count for statistical confidence

### Debugging with Intermediate Values

```c
// Enable intermediate value output for debugging
#define MLKEM_DEBUG 1

#ifdef MLKEM_DEBUG
#include <stdio.h>
static void debug_poly(const char* label, const int16_t* coeffs, int n) {
    printf("%s: [", label);
    for (int i = 0; i < 8 && i < n; i++)
        printf("%d, ", coeffs[i]);
    printf("...]\n");
}
#else
#define debug_poly(label, coeffs, n) ((void)0)
#endif
```

### Memory and Resource Analysis

```bash
# Stack usage analysis for embedded targets
arm-none-eabi-gcc -fstack-usage -c mlkem768.c
cat mlkem768.su | sort -k2 -n -r | head -20

# Heap allocation analysis
valgrind --tool=massif ./pqc_application
ms_print massif.out.* | head -40

# Code size analysis
arm-none-eabi-size -A mlkem768.o | sort -k2 -n -r

# Binary size for each PQC algorithm
for alg in mlkem768 mldsa65 slhdsa_sha2_128s; do
    size=$(arm-none-eabi-size build/lib${alg}.a | tail -1 | awk '{print $1}')
    echo "${alg}: ${size} bytes (text)"
done
```

## C.14 Algorithm-Specific Implementation Notes

### ML-KEM Implementation Considerations

**NTT Implementation:** The NTT is the performance-critical component of ML-KEM. Key implementation choices include:
- Layer ordering: Cooley-Tukey (forward) vs. Gentleman-Sande (inverse) butterfly
- Twiddle factor storage: precomputed table vs. on-the-fly computation
- Modular reduction: Barrett (for general q) vs. Montgomery (for odd q) vs. special reduction for q = 3329
- Vectorization: AVX2 processes 16 coefficients simultaneously; ARM NEON processes 8

For q = 3329, a specialized reduction exists: since 3329 = 13 × 256 + 1, Barrett reduction can be implemented with a simple shift-and-subtract sequence avoiding general-purpose multiplication.

**Compression and decompression:** ML-KEM uses lossy compression to reduce ciphertext and public key sizes. The compress function maps Z_q → Z_{2^d} via Compress_d(x) = ⌈(2^d/q)·x⌋ mod 2^d. The decompress function reverses this approximately: Decompress_d(x) = ⌈(q/2^d)·x⌋. The rounding error must be accounted for in decryption correctness analysis.

**Implicit rejection:** When decapsulation detects an invalid ciphertext (re-encapsulation check fails), ML-KEM does not return an error. Instead, it derives a pseudorandom shared secret from a hash of the ciphertext and a secret random value z stored as part of the secret key. This prevents chosen-ciphertext attackers from distinguishing valid/invalid ciphertexts through the API. The implementation must ensure constant-time behavior regardless of whether the ciphertext is valid.

**Serialization:** ML-KEM uses a specific byte-encoding format for polynomials and polynomial vectors. Each coefficient (0 to q-1, needing 12 bits) is packed into bytes using a bitpacking routine. Implementations must handle the byte-to-coefficient and coefficient-to-byte conversions correctly, particularly for compressed representations using fewer bits per coefficient.

### ML-DSA Implementation Considerations

**Rejection sampling loops:** ML-DSA signing involves multiple rejection checks that cause the signing algorithm to restart:
1. The challenge response z = y + cs must satisfy ‖z‖∞ < γ₁ - β (otherwise, z would leak information about s)
2. The low-order bits of Az - ct must have small norm
3. The hint vector h must have Hamming weight ≤ ω

On average, signing requires approximately 4-7 iterations (depending on the parameter set). The implementation must ensure that the number of iterations does not leak information beyond what the final signature reveals. Each iteration should take constant time, though the total signing time is inherently variable.

**Expandable output functions:** ML-DSA uses SHAKE-128 and SHAKE-256 extensively for deterministic generation of the public matrix A from a seed, for sampling the masking vector y, and for computing the challenge hash. Efficient SHAKE implementation (particularly incremental/streaming absorption) is important for overall ML-DSA performance.

**Hint encoding:** The hint vector h (used to reconstruct high-order bits during verification) is encoded using a sparse representation since it has at most ω nonzero positions out of 256k total. The encoding stores the positions of ones, enabling efficient transmission without revealing the exact distribution.

### SLH-DSA Implementation Considerations

**Tree traversal:** SLH-DSA involves traversing a multi-layer tree structure (hypertree) of total height h. Efficient tree traversal requires computing authentication paths — the sibling nodes along the path from a leaf to the root. For a tree of height h', this requires h' hash computations per layer.

**FORS signing:** The few-time signature at the base uses k trees of height a. For each message chunk, one leaf secret is revealed and its authentication path is included. The FORS public key (root of a Merkle tree over the k individual tree roots) must be computed during signing.

**Parallelization opportunities:** The multi-layer tree structure offers natural parallelism: different layers can be computed independently, and within a layer, different tree computations are independent. SIMD implementations can hash multiple tree nodes simultaneously.

**Parameter set selection:** SLH-DSA offers many parameter sets trading signature size against speed:
- "s" (small) variants: smaller signatures but slower signing (more tree layers, smaller trees per layer)
- "f" (fast) variants: faster signing but larger signatures (fewer layers, larger trees)
- SHA-256 vs. SHAKE-256 instantiations: SHA-256 is faster on platforms with hardware acceleration; SHAKE-256 offers simplicity and security margin

### FN-DSA Implementation Considerations

**Gaussian sampling:** FN-DSA requires sampling from a discrete Gaussian distribution over an NTRU lattice. This involves:
1. Computing a Gram-Schmidt orthogonalization of the secret basis (precomputed at key generation)
2. Sampling coordinates in the Gram-Schmidt basis using independent 1D Gaussian samples
3. Converting back to the original lattice

The 1D Gaussian sampler must achieve sufficient precision (53-bit floating point for FN-DSA-512, 64-bit for FN-DSA-1024) and operate in constant time. This is the primary implementation challenge: floating-point arithmetic on secret data raises side-channel concerns, and the precision requirements demand careful numerical analysis.

**Tree-based fast Fourier sampling:** FN-DSA uses a recursive FFT-like structure (the "falcon tree") to efficiently sample vectors from the target Gaussian distribution. The tree representation of the Gram-Schmidt information enables O(n log n) Gaussian sampling rather than O(n²).

**Key generation complexity:** FN-DSA key generation requires finding an NTRU key pair (f, g, F, G) satisfying fG - gF = q and with all polynomials short. The required basis quality makes key generation significantly slower than signing or verification (approximately 100× slower).

## C.15 Platform-Specific Optimization Guides

### x86-64 Optimizations

Modern x86-64 processors offer several features exploitable by PQC implementations:

**AVX2 (256-bit SIMD):** Process 16 16-bit coefficients simultaneously in ML-KEM/ML-DSA NTT operations. The butterfly operations map naturally to vpaddw/vpsubw (add/subtract) and vpmullw/vpmulhw (multiply low/high halves). AVX2 implementations achieve 3-5× speedup over scalar code.

**AVX-512 (512-bit SIMD):** Process 32 16-bit coefficients simultaneously. Available on Intel Ice Lake+ and AMD Zen 4+. Provides additional speedup over AVX2 but with potential frequency throttling on some processors.

**AES-NI + AVX2 for hashing:** When SLH-DSA uses the SHA-256 instantiation, hardware SHA extensions (SHA-NI) provide significant acceleration for the hash-intensive tree computations. For SHAKE-based instantiations, the Keccak permutation benefits from scatter/gather instructions.

**BMI2 (Bit Manipulation Instructions):** PEXT/PDEP instructions enable efficient bitpacking/unpacking of compressed polynomial coefficients. Useful for ML-KEM serialization routines.

### ARM Optimizations

**NEON (128-bit SIMD):** Process 8 16-bit coefficients simultaneously. ARM NEON is available on all modern ARM application processors (Cortex-A series, Apple M-series) and provides the primary vectorization path for mobile and server ARM platforms.

**SVE/SVE2 (Scalable Vector Extension):** Available on ARMv9 (Cortex-X2+, Neoverse V1+), SVE provides scalable vectors up to 2048 bits. PQC implementations can be written with vector-length-agnostic code that automatically benefits from wider SVE implementations.

**Cryptographic extensions:** ARM Cryptographic Extensions provide hardware acceleration for SHA-256 and SHA-512, benefiting SLH-DSA and internal hashing in ML-KEM/ML-DSA. Some implementations use these for SHAKE by leveraging the Keccak-f permutation structure.

**Cortex-M optimization:** For embedded ARM (Cortex-M4), key optimizations include:
- Using the DSP multiply-accumulate instructions (UMAAL, SMLAD) for NTT butterflies
- Careful register allocation to minimize stack spills in the NTT
- Lazy reduction (deferring modular reduction to reduce instruction count)
- Barrett reduction optimized for the specific modulus (q = 3329 for ML-KEM)

### RISC-V Optimizations

RISC-V is gaining importance for PQC in IoT and embedded applications:

**Vector extension (RVV):** Scalable vector processing similar to ARM SVE. PQC implementations using RVV intrinsics adapt to different vector register widths.

**Bitmanip extension (Zb*):** Provides population count, byte reversal, and bit extraction useful for constant-time implementations and serialization.

**Crypto extensions (Zkn*):** Hardware acceleration for AES and SHA-256, benefiting PQC hash operations.

**Custom extensions:** RISC-V's extensibility allows vendors to add PQC-specific instructions (NTT butterfly, modular multiply-accumulate) for maximum throughput in hardware accelerators.

## C.16 Security Audit Resources

### Audit Frameworks for PQC Implementations

When commissioning or performing security audits of PQC implementations, the following areas require specialized review:

**Correctness verification:**
- KAT test vector validation against NIST reference
- Interoperability testing with at least two independent implementations
- Boundary condition testing (maximum-size inputs, zero vectors, identity elements)
- Error handling validation (malformed inputs, truncated keys/ciphertexts)

**Side-channel resistance:**
- Constant-time analysis (timing, cache, branch prediction)
- Power analysis resistance (if hardware deployment)
- Fault injection resistance (redundant computation, verification after signing)
- Microarchitectural leakage (speculative execution, memory access patterns)

**Memory safety:**
- Buffer overflow/underflow in serialization routines
- Integer overflow in index computation
- Stack buffer overflows in recursive algorithms (tree traversal)
- Zeroization of sensitive values after use

**Randomness quality:**
- Entropy source validation
- DRBG seeding and reseeding
- Nonce generation uniqueness (particularly critical for deterministic signatures)
- Failure mode when entropy is unavailable

### Notable PQC Security Audits

Several significant audits have been conducted on PQC implementations:
- **NCC Group:** Audit of pqcrypto Rust crates (2023)
- **Trail of Bits:** Audit of AWS-LC ML-KEM implementation (2024)
- **X41 D-Sec:** Audit of wolfSSL PQC implementations (2024)
- **Quarkslab:** Audit of liboqs core algorithms (2023)
- **Cure53:** Audit of Signal's PQXDH implementation (2023)

These audits typically identify issues in serialization, error handling, and subtle constant-time violations rather than fundamental cryptographic flaws, highlighting the importance of implementation quality beyond algorithmic correctness.

## C.17 Migration Planning Tools

### Assessment and Planning

| Tool/Framework | Purpose | Provider |
|---------------|---------|----------|
| NIST Quantum Readiness Assessment | Organizational readiness evaluation | NIST |
| IBM Quantum Safe Roadmap | Enterprise migration planning | IBM |
| Microsoft PQC Migration Guide | Azure/Windows ecosystem guidance | Microsoft |
| AWS PQC Migration Hub | Cloud service PQC transition | AWS |
| Entrust PQC Readiness | Certificate and PKI assessment | Entrust |
| PQC Risk Assessment Tool | Crypto risk quantification | Various vendors |

### Migration Execution Tools

**Protocol Analyzer:** Tools for identifying PQC-relevant protocol usage in network traffic:
- Wireshark with PQC dissectors (OQS plugin provides ML-KEM/ML-DSA TLS decode)
- Network traffic analysis for identifying quantum-vulnerable key exchanges
- Certificate chain analysis identifying classical-only signatures

**Configuration Management:**
- Ansible/Terraform modules for PQC algorithm deployment across infrastructure
- Kubernetes operators for automated PQC certificate rotation
- CI/CD pipeline integration for PQC testing and validation

**Monitoring and Alerting:**
- Dashboard templates for tracking PQC migration progress
- Alerting on non-PQC connections after migration deadlines
- Performance monitoring comparing classical vs. PQC operation latency

### Compliance and Reporting

Organizations undergoing PQC migration need to demonstrate compliance with various mandates:

**US Federal:** OMB M-23-02 requires agencies to submit cryptographic inventory and migration plans. CISA's Quantum-Ready guidance mandates prioritized migration based on data sensitivity.

**Financial Services:** PCI DSS and SOC 2 requirements are being updated to address quantum threats. Financial institutions must demonstrate quantum risk awareness and migration planning.

**Healthcare:** HIPAA's security requirements extend to quantum threats for long-lived PHI. Healthcare organizations must assess quantum vulnerability of stored health records.

**Defense/Intelligence:** CNSA 2.0 mandates specific PQC algorithm adoption by defined dates. DoD Instruction 8523.01 addresses quantum computing preparedness.

Compliance reporting tools help organizations track:
- Percentage of systems migrated to PQC
- Remaining quantum-vulnerable cryptographic assets
- Timeline adherence against regulatory deadlines
- Risk quantification for remaining classical cryptography
- Evidence collection for audit and certification purposes

The tooling ecosystem for PQC continues to mature rapidly. Organizations should establish relationships with library maintainers, participate in interoperability testing events, and monitor standards development to stay current with evolving best practices and tool capabilities.
