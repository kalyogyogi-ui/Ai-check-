# Chapter 17: Performance Analysis and Benchmarking

## 17.1 Performance Metrics for PQC

Evaluating PQC algorithm performance requires considering multiple dimensions:

- **Computation time:** Key generation, encapsulation/signing, decapsulation/verification
- **Communication size:** Public keys, secret keys, ciphertexts, signatures
- **Memory usage:** RAM during operations, persistent storage
- **Energy consumption:** Critical for battery-powered and embedded devices
- **Throughput:** Operations per second under sustained load
- **Latency:** End-to-end time including network effects

## 17.2 KEM Performance Comparison

### Computational Performance (x86-64, AVX2)

| Algorithm | KeyGen (μs) | Encaps (μs) | Decaps (μs) | Total KE (μs) |
|-----------|------------|------------|------------|---------------|
| X25519 (ECDH) | - | 48 | 48 | 96 |
| RSA-2048 | 200,000 | 25 | 800 | 825 |
| ML-KEM-512 | 30 | 40 | 45 | 85 |
| ML-KEM-768 | 50 | 65 | 70 | 135 |
| ML-KEM-1024 | 75 | 95 | 100 | 195 |
| HQC-128 | 120 | 250 | 350 | 600 |
| Classic McEliece 348864 | 200,000 | 50 | 120 | 170 |
| X25519 + ML-KEM-768 | 50 | 113 | 118 | 231 |

ML-KEM is computationally competitive with — or faster than — most classical algorithms for key exchange.

### Size Comparison

| Algorithm | Public Key | Ciphertext | Total Bandwidth |
|-----------|-----------|------------|-----------------|
| X25519 | 32 B | 32 B | 64 B |
| RSA-2048 | 256 B | 256 B | 512 B |
| ML-KEM-512 | 800 B | 768 B | 1,568 B |
| ML-KEM-768 | 1,184 B | 1,088 B | 2,272 B |
| ML-KEM-1024 | 1,568 B | 1,568 B | 3,136 B |
| HQC-128 | 2,249 B | 4,497 B | 6,746 B |
| Classic McEliece | 261,120 B | 128 B | 261,248 B |

### ARM Cortex-M4 Performance (STM32F4 @ 168 MHz)

| Algorithm | KeyGen (ms) | Encaps (ms) | Decaps (ms) |
|-----------|------------|------------|------------|
| ML-KEM-512 | 0.7 | 0.9 | 1.0 |
| ML-KEM-768 | 1.1 | 1.4 | 1.5 |
| ML-KEM-1024 | 1.6 | 2.0 | 2.2 |

Even on constrained platforms, ML-KEM operates in millisecond timescales.

## 17.3 Signature Performance Comparison

### Computational Performance (x86-64, AVX2)

| Algorithm | KeyGen (μs) | Sign (μs) | Verify (μs) |
|-----------|------------|-----------|------------|
| Ed25519 | 25 | 50 | 120 |
| ECDSA P-256 | 30 | 60 | 120 |
| RSA-2048 | 200,000 | 1,000 | 30 |
| ML-DSA-44 | 150 | 700 | 200 |
| ML-DSA-65 | 250 | 1,100 | 300 |
| ML-DSA-87 | 400 | 1,500 | 450 |
| SLH-DSA-128f | 1,000 | 5,000 | 800 |
| SLH-DSA-128s | 1,000 | 60,000 | 3,000 |
| FN-DSA-512 | 10,000 | 5,000 | 500 |

### Size Comparison

| Algorithm | Public Key | Signature | Combined (PK+Sig) |
|-----------|-----------|-----------|-------------------|
| Ed25519 | 32 B | 64 B | 96 B |
| ECDSA P-256 | 64 B | 64 B | 128 B |
| RSA-2048 | 256 B | 256 B | 512 B |
| ML-DSA-44 | 1,312 B | 2,420 B | 3,732 B |
| ML-DSA-65 | 1,952 B | 3,309 B | 5,261 B |
| ML-DSA-87 | 2,592 B | 4,627 B | 7,219 B |
| SLH-DSA-128f | 32 B | 17,088 B | 17,120 B |
| SLH-DSA-128s | 32 B | 7,856 B | 7,888 B |
| FN-DSA-512 | 897 B | 666 B | 1,563 B |

## 17.4 Protocol-Level Performance

### TLS 1.3 Handshake

The real-world impact depends on the full protocol context:

**Classical TLS 1.3 (ECDHE + ECDSA):**
- Key share: 32 B (client) + 32 B (server) = 64 B
- Certificate chain (3 certs): ~3 KB
- Certificate verify: 64 B
- Total additional data: ~3.1 KB
- Handshake time (1 RTT): Dominated by network latency

**Hybrid TLS 1.3 (X25519+ML-KEM-768, ML-DSA-65 certs):**
- Key share: 1,216 B (client) + 1,120 B (server) = 2,336 B
- Certificate chain (3 certs with ML-DSA-65): ~18 KB
- Certificate verify (ML-DSA-65): 3,309 B
- Total additional data: ~23.6 KB
- Handshake time: ~1.5 ms additional computation, dominated by bandwidth

**Measured impact (real-world):**
- Additional handshake latency: 0.3-1.5 ms (depending on bandwidth)
- No measurable impact on subsequent data transfer
- Acceptable for virtually all web applications

### SSH Connection

**Classical (Ed25519):**
- Host key: 32 B public key + 64 B signature
- User key: 32 B public key + 64 B signature

**Post-Quantum (ML-DSA-65 + ML-KEM-768):**
- Key exchange: +2,272 B
- Host authentication: +5,261 B
- User authentication: +5,261 B
- Total overhead: ~12.8 KB

Impact: Negligible on modern networks; noticeable on very slow connections.

### IPsec/IKEv2

**Classical IKE_SA_INIT:**
- Key exchange: ~64 B DH share
- Authentication: ~128 B per signature

**Hybrid IKE_SA_INIT:**
- Key exchange: ~2,400 B (ML-KEM + DH)
- Authentication: ~5,300 B per ML-DSA signature
- May require UDP fragmentation or IKE fragmentation (RFC 7383)

## 17.5 Throughput Benchmarks

### Server-Side Signature Operations

For high-traffic servers (web servers, API gateways):

| Algorithm | Signatures/sec (1 core) | Verifications/sec (1 core) |
|-----------|------------------------|---------------------------|
| ECDSA P-256 | ~15,000 | ~8,000 |
| Ed25519 | ~20,000 | ~8,000 |
| ML-DSA-65 | ~900 | ~3,300 |
| SLH-DSA-128f | ~200 | ~1,250 |

For server signing (e.g., TLS Certificate Verify):
- ML-DSA-65: Adequate for most servers (900 new connections/sec/core)
- High-traffic sites: Scale with cores (linear scaling)
- SLH-DSA: May be a bottleneck for very high-traffic services

### Key Exchange Throughput

| Algorithm | Encaps/sec (1 core) | Decaps/sec (1 core) |
|-----------|--------------------|--------------------|
| X25519 | ~20,000 | ~20,000 |
| ML-KEM-768 | ~15,000 | ~14,000 |
| Hybrid (X25519+ML-KEM-768) | ~9,000 | ~8,500 |

ML-KEM throughput is excellent — comparable to classical ECDH.

## 17.6 Memory Usage

### Stack/Heap Requirements

| Algorithm | Operation | Peak Memory |
|-----------|-----------|-------------|
| ML-KEM-768 | KeyGen | ~6 KB |
| ML-KEM-768 | Encaps | ~6 KB |
| ML-KEM-768 | Decaps | ~7 KB |
| ML-DSA-65 | KeyGen | ~12 KB |
| ML-DSA-65 | Sign | ~32 KB |
| ML-DSA-65 | Verify | ~15 KB |
| SLH-DSA-128f | Sign | ~8 KB |
| SLH-DSA-128f | Verify | ~4 KB |

### Key Storage

For systems managing many keys:

| Scenario | Classical (ECDSA) | PQC (ML-DSA-65) | Ratio |
|----------|------------------|-----------------|-------|
| 1,000 key pairs | 96 KB | 5,984 KB | 62x |
| 10,000 key pairs | 960 KB | 59,840 KB | 62x |
| Certificate store (1000 CAs) | ~64 KB | ~1,952 KB | 30x |

Storage is rarely a bottleneck on modern systems but matters for constrained devices and large-scale certificate stores.

## 17.7 Energy Consumption

### Embedded Device Energy Comparison

For battery-powered IoT devices (measurements on ARM Cortex-M4):

| Algorithm | Operation | Energy (μJ) | Relative to ECC |
|-----------|-----------|-------------|-----------------|
| ECDH P-256 | Full exchange | 850 | 1.0x |
| ML-KEM-768 | Full exchange | 420 | 0.5x |
| ECDSA P-256 | Sign | 420 | 1.0x |
| ML-DSA-44 | Sign | 2,800 | 6.7x |
| SLH-DSA-128s | Sign | 250,000 | 595x |

ML-KEM is actually MORE energy-efficient than classical ECDH on many platforms, while ML-DSA costs more energy per signature.

## 17.8 Bandwidth-Constrained Scenarios

### Satellite Communications

- Typical LEO satellite link: 1-10 Mbps
- GEO satellite link: 50-500 kbps
- PQC overhead (TLS handshake): ~20 KB additional
- Impact: 0.02-2 seconds additional at link layer
- **Verdict:** Acceptable for most satellite applications

### LoRaWAN / LPWAN

- Data rates: 0.3-50 kbps
- Max payload: 51-222 bytes per frame
- ML-KEM-768 public key (1,184 B): Requires multiple frames
- **Challenge:** Fragmentation and reassembly needed
- **Possible solutions:** Use pre-shared keys, or specialized lightweight PQC

### Bluetooth Low Energy

- Typical data rate: 1 Mbps (BLE 4.2+), 2 Mbps (BLE 5.0)
- Max ATT MTU: 517 bytes (negotiated)
- ML-DSA signature (3,309 B): Multiple ATT packets
- **Impact:** Additional ~30 ms at BLE data rates
- **Verdict:** Manageable but requires careful protocol design

## 17.9 Benchmarking Methodology

### Correct Benchmarking Practices

1. **Warm-up:** Run algorithm multiple times before measuring
2. **Statistical rigor:** Report median and percentiles, not just mean
3. **Cycle-accurate:** Use CPU cycle counters (RDTSC on x86)
4. **Disable turbo boost:** Ensure stable clock frequency
5. **Account for variance:** ML-DSA signing has inherent variance (rejection loop)
6. **Platform documentation:** Report CPU model, frequency, compiler, flags

### Common Pitfalls

- Measuring debug builds instead of optimized
- Including I/O or memory allocation in timing
- Not accounting for DVFS (frequency scaling)
- Ignoring cache warm-up effects
- Comparing different security levels unfairly

### SUPERCOP Benchmarking Framework

The standard framework for cryptographic benchmarking:
- Standardized measurement methodology
- Cross-platform comparison
- Historical data for tracking improvements
- Community-maintained, open source

## 17.10 Performance Optimization Techniques

### NTT Optimization

The NTT dominates ML-KEM and ML-DSA computation:
- **Merged layers:** Combine NTT stages to reduce memory accesses
- **Montgomery multiplication:** Efficient modular multiplication
- **Barrett reduction:** Alternative modular reduction without division
- **Vectorized butterflies:** Process 4-16 butterflies in parallel with SIMD
- **Precomputed twiddle factors:** Store and reuse NTT constants

### Hash Function Optimization

Hash functions dominate SLH-DSA and contribute to ML-KEM/ML-DSA:
- **SIMD hashing:** Process multiple hash invocations in parallel
- **Incremental hashing:** Reuse state across related computations
- **Hardware acceleration:** SHA-NI, ARMv8 Crypto Extensions
- **Batched tree computation:** Parallel leaf computation in Merkle trees

### Memory Optimization for Constrained Devices

- **Streaming computation:** Process data in chunks, avoid full buffer allocation
- **In-place NTT:** Transform polynomial without extra buffer
- **On-the-fly matrix generation:** Regenerate A from seed instead of storing
- **Stack allocation only:** Avoid heap for predictable memory usage

## 17.11 Future Performance Improvements

### Hardware Acceleration (Expected 2025-2028)

- **Dedicated PQC instructions:** Similar to AES-NI for NTT operations
- **PQC coprocessors:** FPGA/ASIC acceleration in network equipment
- **TPM integration:** PQC operations in trusted hardware
- **Smart card support:** ML-DSA on next-generation cards

### Algorithmic Improvements

- **Tighter parameters:** Better security analysis may allow smaller parameters
- **Improved NTT algorithms:** Asymptotically faster transforms for larger dimensions
- **Amortized operations:** Batch key generation and signing optimizations
- **Pre-computation:** Trade memory for computation time

## 17.12 Key Takeaways

- ML-KEM is computationally competitive with classical ECDH (similar or better speed)
- ML-DSA is 10-20x slower than ECDSA for signing but acceptable for most applications
- SLH-DSA is 100-1000x slower than ECDSA — suitable for infrequent signing only
- Primary PQC overhead is bandwidth (10-50x larger keys/signatures), not computation
- Hybrid schemes roughly double bandwidth but have minimal computational overhead
- TLS handshake with hybrid PQC adds <2 ms latency in practice
- Constrained devices (Cortex-M4) can run ML-KEM in ~1.5 ms and ML-DSA in ~10 ms
- Memory requirements are manageable (6-32 KB) for most platforms
- NTT optimization is key to ML-KEM/ML-DSA performance
- Hardware acceleration will further improve PQC performance in coming years

---

*Next: [Chapter 18 — PQC in TLS, PKI, and Network Protocols](./18-pqc-protocols.md)*
