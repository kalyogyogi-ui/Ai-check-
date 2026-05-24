# Chapter 18: PQC in TLS, PKI, and Network Protocols

## 18.1 Transport Layer Security (TLS)

### TLS 1.3 and PQC Integration

TLS 1.3 provides a clean integration point for PQC through its supported_groups and key_share extensions. The key exchange is the primary integration target because it protects against "harvest now, decrypt later" attacks.

### Hybrid Key Exchange in TLS 1.3

**Standard approach (IETF RFC 9370 and related):**

```
ClientHello:
  supported_groups: [x25519_ml_kem768, x25519, ...]
  key_share: x25519_ml_kem768 (32B X25519 + 1184B ML-KEM-768 pk)

ServerHello:
  key_share: x25519_ml_kem768 (32B X25519 + 1088B ML-KEM-768 ct)

Handshake Secret:
  shared_secret = HKDF(x25519_ss || ml_kem_ss)
```

**Negotiated groups (code points assigned):**
- `x25519_ml_kem768` — X25519 + ML-KEM-768
- `secp256r1_ml_kem768` — P-256 + ML-KEM-768
- `x25519_ml_kem1024` — X25519 + ML-KEM-1024 (higher security)

### PQC Authentication in TLS

Server authentication via certificates containing PQC keys:

**Certificate chain impact:**
- Root CA: ML-DSA-87 (maximum security, stored locally)
- Intermediate CA: ML-DSA-65 (good balance)
- End-entity: ML-DSA-65 or ML-DSA-44

**Size impact on TLS handshake:**

| Component | Classical (P-256) | PQC (ML-DSA-65) | Difference |
|-----------|------------------|-----------------|------------|
| Server key share | 32 B | 1,120 B | +1,088 B |
| Server certificate (3 certs) | ~3 KB | ~18 KB | +15 KB |
| CertificateVerify | 64 B | 3,309 B | +3,245 B |
| Total server→client | ~3.1 KB | ~22.4 KB | +19.3 KB |

### Optimizations for TLS

**Certificate compression (RFC 8879):**
- Compress certificate chain using zlib/brotli/zstd
- 30-50% size reduction for PQC certificates
- Already widely supported

**Cached certificates:**
- Cache intermediate/root certificates across connections
- Only send end-entity certificate
- Reduces per-handshake overhead

**Suppressed extensions:**
- Omit certificates known to be cached by the client
- Use certificate fingerprints to identify cached certs

**Merkle Tree Certificates (experimental):**
- Amortize signature size across many certificates
- Batch issuance with shared Merkle tree proofs
- Significantly reduces per-certificate overhead

## 18.2 Public Key Infrastructure (PKI)

### X.509 Certificate Adaptations

X.509 certificates need extensions for PQC:

**Algorithm identifiers:**
- OIDs assigned for ML-DSA, SLH-DSA, ML-KEM
- Composite algorithm OIDs for hybrid certificates
- Subject Public Key Info encodes PQC public key

**Certificate size comparison:**

| Certificate Type | Typical Size |
|-----------------|-------------|
| RSA-2048 end-entity | ~1.2 KB |
| ECDSA P-256 end-entity | ~0.8 KB |
| ML-DSA-65 end-entity | ~6 KB |
| Hybrid (ECDSA + ML-DSA-65) | ~7 KB |
| ML-DSA-87 CA certificate | ~8 KB |

### Certificate Lifecycle with PQC

**Issuance:**
- CA signs with PQC key (and optionally classical key for hybrid)
- Longer validity periods may be reconsidered (larger certs stored longer)
- OCSP responses also need PQC signatures

**Revocation:**
- CRL/OCSP responses must use PQC signatures
- CRL sizes increase due to PQC signature overhead
- OCSP stapling helps reduce verification overhead

**Certificate Transparency:**
- SCTs (Signed Certificate Timestamps) need PQC signatures
- Log servers must support PQC verification
- Increased storage for CT logs

### Migration Strategies for PKI

**Phase 1: Dual-signed intermediate CAs**
- Existing root CAs issue new intermediate CAs with PQC keys
- Intermediate CAs issue dual (hybrid) end-entity certificates
- Classic validation path for legacy clients

**Phase 2: PQC root CAs**
- Generate new root CAs with PQC keys
- Cross-sign with classical roots for interoperability
- Include in trust stores over time

**Phase 3: PQC-only**
- Phase out classical signature paths
- All certificates use PQC signatures
- Legacy clients no longer supported

## 18.3 Secure Shell (SSH)

### SSH Key Exchange

SSH key exchange adaptation for PQC:

**Classical (curve25519-sha256):**
```
Client → Server: e_C (32 bytes, ephemeral public key)
Server → Client: e_S (32 bytes, ephemeral public key)
Shared: K = ECDH(e_C, e_S)
```

**PQC hybrid (mlkem768x25519-sha256):**
```
Client → Server: e_C_ecdh (32B) || e_C_mlkem (1184B ML-KEM pk)
Server → Client: e_S_ecdh (32B) || ct_mlkem (1088B ciphertext)
Shared: K = KDF(ECDH_ss || ML-KEM_ss)
```

### SSH Host and User Authentication

**Host keys:**
- Server presents ML-DSA or hybrid host key
- Client verifies host key signature
- `known_hosts` file stores PQC public keys (larger entries)

**User authentication:**
- SSH keys can be ML-DSA key pairs
- `authorized_keys` entries are larger
- Agent forwarding works with PQC keys

**SSH certificate format:**
- OpenSSH certificates extended for PQC
- CA signatures use PQC algorithms
- Larger certificates but same workflow

### Current SSH PQC Support

- **OpenSSH 9.x+:** Experimental PQC key exchange support
- **libssh:** PQC integration via liboqs
- **PuTTY:** Experimental PQC support

## 18.4 Virtual Private Networks (VPN)

### IPsec/IKEv2

**IKE_SA_INIT extensions:**
- Additional Key Exchange (AKE) payloads for PQC
- RFC 9370: Framework for PQC in IKEv2
- Multiple rounds of key exchange if needed (intermediate exchange)

**Challenges:**
- IKE messages may exceed MTU (require fragmentation)
- IKE fragmentation (RFC 7383) handles large payloads
- Initial exchange before SA established cannot use IKE fragmentation
- IP fragmentation may be needed for first packet

**Solutions:**
- Use IKE fragmentation for subsequent exchanges
- TCP transport for IKE (RFC 8229) avoids IP fragmentation
- Reduced ML-KEM parameters where security allows

### WireGuard

**Classical WireGuard:**
- Noise_IK handshake pattern
- X25519 for key exchange
- 2 messages, very compact

**Post-Quantum WireGuard options:**
- **Rosenpass:** Additional PQ key exchange layered on top
- **Native integration:** Replace or augment X25519 with ML-KEM
- **McEliece variant:** Pre-shared PQ key for long-term static

### OpenVPN

- Support for PQC through OpenSSL provider model
- TLS-based control channel uses PQC in TLS
- Similar considerations as TLS 1.3 deployment

## 18.5 Email Security

### S/MIME with PQC

**Encryption:**
- Recipient's PQC public key (ML-KEM) in their certificate
- Sender encapsulates session key using recipient's ML-KEM key
- Hybrid: Encapsulate with both ECDH and ML-KEM

**Signatures:**
- Sender signs with ML-DSA key
- Signature included in MIME structure
- Larger S/MIME messages

**Certificate Discovery:**
- LDAP directories with PQC certificates
- Larger certificate downloads
- Multiple certificates per user (encryption + signing)

### PGP/OpenPGP

- OpenPGP draft specifications for PQC
- ML-KEM for encryption, ML-DSA for signatures
- Key servers must handle larger keys
- Existing key infrastructure needs updates

## 18.6 DNS and DNSSEC

### DNSSEC Challenges

DNSSEC is particularly affected by PQC because:
- Signatures are transmitted in DNS responses
- DNS has hard UDP size limits (512B without EDNS, ~4KB with EDNS)
- Zone signing keys (ZSK) sign many records
- Key signing keys (KSK) must fit in DS records

**Impact with ML-DSA-44:**
- DNSKEY record: ~1,312 B (public key)
- RRSIG: ~2,420 B (signature)
- Total DNSSEC response: May exceed EDNS limit
- Fallback to TCP for large responses

**Possible mitigations:**
- SLH-DSA with small public key (32 B) but large signature
- FN-DSA with small signature (666 B) but larger public key
- New DNSSEC protocol designs for PQC
- Key caching and delta signing approaches

### DNS over HTTPS/TLS

For DNS-over-HTTPS/TLS, the PQC overhead is in the TLS connection rather than DNS responses, making PQC integration cleaner.

## 18.7 Code Signing and Software Updates

### Package Manager Signatures

Software packages need PQC signatures for long-term security:
- APT/RPM repository signing
- npm/PyPI/Maven package signatures
- Container image signing (Sigstore/cosign)
- OS update signatures

**Considerations:**
- Signatures verified millions of times (verification speed matters)
- Repository metadata with many signatures becomes large
- Backward compatibility during transition

### Secure Boot

Firmware and boot chain signing:
- UEFI Secure Boot database entries
- Platform key (PK) and Key Exchange Key (KEK)
- Signature database (db) stores allowed signatures
- Space-constrained: NVRAM storage for keys/signatures

**Recommendations:**
- XMSS/LMS for firmware signing (stateful, but controlled environment)
- ML-DSA for general code signing
- SLH-DSA for root signing keys (infrequent, maximum security)

## 18.8 Blockchain and Cryptocurrency

### Quantum Threats to Blockchain

- **Address derivation:** Public keys exposed in transactions
- **Transaction signing:** ECDSA signatures forged with quantum computers
- **Mining:** Grover's limited impact on PoW (quadratic speedup insufficient)

### PQC Integration Challenges

- **Transaction size:** PQC signatures much larger (~2.4 KB vs 64 B)
- **Block size:** More signatures per block = less transaction throughput
- **State bloat:** Larger public keys in UTXO set or account state
- **Address format:** PQC public keys too large for simple address derivation

### Approaches

- **Account abstraction:** Separate signing scheme from address
- **Aggregation:** Combine multiple signatures (research area for PQC)
- **Commit-reveal:** Hide public key until spending time
- **Gradual migration:** New transactions use PQC, old addresses frozen

## 18.9 IoT and Constrained Protocols

### MQTT / CoAP

**Challenges:**
- Small payload sizes (CoAP: prefer < 1 KB)
- Low-power devices
- Frequent communication

**Solutions:**
- Pre-shared ML-KEM keys during provisioning
- Lightweight authentication protocols
- Session resumption to amortize handshake cost

### Matter (Smart Home)

- Device attestation with PQC certificates
- Commissioning protocol with PQC key exchange
- Operational certificates for device-to-device auth
- Size constraints on Thread/BLE transport

### Automotive (V2X)

- Vehicle-to-everything communication needs PQC
- High-frequency signature generation (10 messages/second)
- Broadcast authentication (one signer, many verifiers)
- ML-DSA-44 feasible with dedicated hardware

## 18.10 Key Takeaways

- TLS 1.3 hybrid key exchange is already deployed at scale (Chrome, Cloudflare)
- PKI migration requires careful phasing — hybrid certificates during transition
- SSH, VPN, and email protocols all have PQC integration paths
- DNSSEC faces unique challenges due to DNS size constraints
- Code signing and blockchain need PQC but face size/performance trade-offs
- IoT protocols require careful optimization for constrained environments
- The transition is technically feasible — deployment is an engineering challenge, not a research problem

---

*Next: [Chapter 19 — Cryptographic Agility and Migration Strategies](./19-migration-strategies.md)*
