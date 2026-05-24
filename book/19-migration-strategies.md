# Chapter 19: Cryptographic Agility and Migration Strategies

## 19.1 The Scale of the Challenge

Migrating to post-quantum cryptography is one of the largest coordinated technology transitions in history. Consider the scope:

- **Billions** of TLS endpoints
- **Millions** of applications using cryptographic libraries
- **Thousands** of protocol implementations
- **Hundreds** of hardware platforms with embedded cryptography
- **Decades** of legacy systems still in production

This chapter provides a systematic framework for planning and executing this migration.

## 19.2 Cryptographic Agility

### Definition

**Cryptographic agility** is the ability to swap cryptographic algorithms without redesigning protocols, applications, or infrastructure. It is both the solution to the current migration challenge and the long-term strategy for handling future cryptographic transitions.

### Principles of Cryptographic Agility

1. **Algorithm abstraction:** Applications reference algorithms by identifier, not by implementation
2. **Negotiation support:** Protocols negotiate algorithms between parties
3. **Configuration-driven:** Algorithm selection via configuration, not code changes
4. **Key format flexibility:** Key storage accommodates different algorithm types
5. **Size tolerance:** Systems handle varying key, signature, and ciphertext sizes
6. **Performance flexibility:** Systems adapt to different computational requirements

### Current State of Agility

Many systems LACK cryptographic agility:
- Hard-coded algorithm choices in application code
- Fixed-size fields in protocols and databases
- Assumptions about key/signature sizes in UI and storage
- Embedded devices with no update mechanism
- Hardware tokens with fixed algorithm support

### Building Agility Into Systems

**Architecture patterns:**
```
Application Layer
    ↓ (algorithm identifier)
Crypto Abstraction Layer
    ↓ (dispatch to implementation)
Algorithm Provider (OpenSSL, BoringSSL, etc.)
    ↓ (configurable)
Specific Implementation (ML-KEM, ML-DSA, etc.)
```

**Key practices:**
- Use algorithm identifiers (OIDs, named algorithms) not raw implementations
- Design protocols with algorithm negotiation from the start
- Size key/signature storage generously or make it dynamic
- Plan for algorithm deprecation as a normal operation

## 19.3 Migration Framework

### The Three-Phase Approach

Based on guidelines from NIST, BSI, and industry best practices:

**Phase 1: Discovery and Assessment**
- Inventory all cryptographic usage
- Assess quantum vulnerability of each use case
- Prioritize by risk (data lifetime × migration complexity)
- Identify dependencies and constraints

**Phase 2: Planning and Preparation**
- Select target algorithms for each use case
- Design migration architecture (hybrid/direct replacement)
- Develop and test implementations
- Plan rollout sequence considering dependencies

**Phase 3: Execution and Validation**
- Deploy PQC capabilities (hybrid first)
- Validate interoperability
- Monitor for issues
- Progressively increase PQC requirements
- Eventually deprecate vulnerable algorithms

### Prioritization Framework

| Priority | Criteria | Examples |
|----------|---------|---------|
| Critical | Long-lived data, high value, exposed to HNDL | Government classified, medical records |
| High | Moderate data lifetime, significant impact | Financial transactions, corporate IP |
| Medium | Shorter data lifetime, moderate impact | Session keys, authentication tokens |
| Lower | Ephemeral data, limited exposure | Internal logging, test environments |

## 19.4 Cryptographic Inventory

### What to Inventory

A complete cryptographic inventory captures:

1. **Algorithms in use:** RSA-2048, ECDSA P-256, AES-128, SHA-256, etc.
2. **Usage context:** Key exchange, authentication, encryption, signing
3. **Key locations:** HSMs, key stores, certificates, embedded in code
4. **Protocol dependencies:** TLS versions, cipher suites, SSH algorithms
5. **Library versions:** OpenSSL 1.1, BoringSSL, libsodium, etc.
6. **Hardware dependencies:** HSMs, smart cards, TPMs with fixed algorithms
7. **Data protection duration:** How long must encrypted data remain confidential?
8. **External dependencies:** Third-party APIs, partner connections, vendor systems

### Automated Discovery Tools

- **Network scanners:** Identify TLS/SSH configurations across infrastructure
- **Code analysis:** Static analysis tools that find cryptographic API calls
- **Certificate inventories:** CT log monitoring, certificate management platforms
- **Library dependency:** Software composition analysis (SCA) tools
- **CBOM tools:** Automated Cryptographic Bill of Materials generation

### The Inventory Process

```
1. Scope Definition
   └─ Which systems, networks, applications?
   
2. Automated Discovery
   └─ Network scans, code analysis, config collection
   
3. Manual Assessment
   └─ Embedded systems, custom protocols, vendor systems
   
4. Classification
   └─ Quantum-vulnerable vs. quantum-safe
   └─ Data lifetime and sensitivity
   
5. Gap Analysis
   └─ What needs to change?
   └─ What are the dependencies?
   
6. Prioritized Migration Plan
   └─ Sequenced roadmap based on risk and feasibility
```

## 19.5 Risk Assessment

### Mosca's Inequality Revisited

For each system/data type, evaluate:
- **x:** Security shelf life (how long must data remain protected?)
- **y:** Migration time (how long will it take to deploy PQC?)
- **z:** Time until CRQC (when will quantum computers break current crypto?)

If x + y > z → **immediate action required**

### Risk Scoring Matrix

| Data Lifetime | Migration Difficulty | Risk Score | Action |
|--------------|---------------------|-----------|--------|
| >25 years | High (hardware, embedded) | Critical | Start immediately |
| >25 years | Low (software update) | High | Plan now, execute soon |
| 10-25 years | High | High | Plan immediately |
| 10-25 years | Low | Medium | Begin planning |
| <10 years | Any | Lower | Monitor, plan for future |

### Quantum Risk Categories

1. **Store-and-break (HNDL):** Encrypted data captured now, broken later
   - Risk exists TODAY for long-lived confidential data
   - Mitigation: PQC key exchange (highest priority)

2. **Real-time break:** Authentication/signatures broken when CRQC arrives
   - Risk begins when CRQC exists
   - Mitigation: PQC signatures and authentication

3. **Retroactive forgery:** Historical signatures become untrustworthy
   - Risk: Digital records from before PQC migration lose integrity
   - Mitigation: Timestamp + re-sign with PQC

## 19.6 Migration Patterns

### Pattern 1: Hybrid Overlay

Add PQC alongside existing cryptography without removing classical:

```
Before: Client ←(ECDH)→ Server
After:  Client ←(ECDH + ML-KEM)→ Server
```

**Advantages:** No loss of classical security, gradual rollout
**Challenges:** Increased bandwidth, complexity

### Pattern 2: Algorithm Replacement

Direct replacement of classical with PQC:

```
Before: Sign(ECDSA, document)
After:  Sign(ML-DSA, document)
```

**Advantages:** Simpler, no ongoing classical dependency
**Challenges:** Requires confidence in PQC, no fallback

### Pattern 3: Parallel Infrastructure

Run separate classical and PQC systems in parallel during transition:

```
Classical PKI: Existing roots → intermediates → end-entity
PQC PKI:      New PQC roots → PQC intermediates → PQC end-entity
Bridge:       Cross-certification between classical and PQC
```

**Advantages:** Clean separation, easy rollback
**Challenges:** Double the infrastructure, synchronization

### Pattern 4: Phased Protocol Migration

Upgrade protocol layers from bottom to top:

```
1. Key exchange → PQC (protects against HNDL immediately)
2. Session authentication → PQC (when implementations ready)
3. Long-term keys/certificates → PQC (when ecosystem supports)
4. Stored data re-encryption → PQC (when feasible)
```

## 19.7 Dependency Management

### Critical Dependencies

PQC migration often reveals complex dependencies:

```
Application A uses Library L1 version X
Library L1 depends on OpenSSL version Y
OpenSSL version Y doesn't support ML-KEM
Upgrading OpenSSL requires kernel version Z
Kernel version Z isn't supported by hardware vendor
```

### Dependency Resolution Strategies

1. **Bottom-up:** Update foundational libraries first (OpenSSL, BoringSSL)
2. **Top-down:** Identify application needs first, pull through requirements
3. **Middleware abstraction:** Insert a crypto abstraction layer
4. **Parallel deployment:** Run new stack alongside old, migrate applications gradually

### Vendor Dependencies

External dependencies require coordination:
- Cloud provider PQC support timeline
- Certificate authority PQC certificate issuance
- HSM vendor firmware updates for PQC
- Smart card/token PQC capability
- Partner/customer readiness for PQC protocols

## 19.8 Testing Strategy

### Compatibility Testing

Before deployment, test:
- **Interoperability:** Different implementations communicate correctly
- **Backward compatibility:** PQC systems talk to non-PQC systems (via negotiation)
- **Performance:** Acceptable latency and throughput under production loads
- **Failure modes:** Graceful handling of unsupported algorithms
- **Rollback:** Ability to revert to classical if issues arise

### Performance Testing

| Test | Purpose | Key Metrics |
|------|---------|-------------|
| Latency test | Handshake time increase | P50, P95, P99 latency |
| Throughput test | Operations/sec under load | Max TPS, saturation point |
| Bandwidth test | Network utilization | Bytes/connection, peak bandwidth |
| Memory test | RAM usage under load | Peak memory, per-connection cost |
| Endurance test | Long-term stability | Memory leaks, performance degradation |

### Security Testing

- **Constant-time verification:** Ensure implementations don't leak via timing
- **Fuzzing:** Random inputs to PQC implementations (malformed keys, ciphertexts)
- **KAT verification:** Known Answer Tests against reference vectors
- **Formal verification:** For critical implementations, mathematical proof of correctness

## 19.9 Organizational Readiness

### Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| CISO | Strategy, risk acceptance, resource allocation |
| Security Architect | Algorithm selection, protocol design |
| Application Teams | Implementation, integration testing |
| Infrastructure | Library updates, certificate deployment |
| Compliance | Regulatory alignment, audit preparation |
| Vendor Management | Third-party PQC readiness tracking |

### Timeline Planning

A realistic PQC migration for a large organization:

```
Months 0-3:    Awareness and strategy
Months 3-6:    Cryptographic inventory
Months 6-12:   Risk assessment and prioritization
Months 12-18:  Architecture and standards development
Months 18-24:  Pilot implementations (hybrid)
Months 24-36:  Broad hybrid deployment
Months 36-48:  Full PQC coverage (hybrid)
Months 48-60+: Transition to PQC-primary
```

### Budget Considerations

- Library and tool upgrades
- HSM replacements or firmware updates
- Personnel training and hiring
- Testing infrastructure
- Increased bandwidth costs (temporary)
- Consultant/vendor support
- Extended validation and certification

## 19.10 Government and Regulatory Drivers

### United States

- **NSM-10 (2022):** National Security Memorandum on quantum readiness
- **OMB M-23-02:** Migrating to PQC — requires inventory by certain deadlines
- **CNSA 2.0:** NSA's Commercial National Security Algorithm Suite timeline

**CNSA 2.0 Timeline:**
- 2025: PQC algorithms preferred for firmware/software signing
- 2027: PQC required for web browsers and TLS
- 2030: PQC required for network equipment
- 2033: Complete PQC migration for national security systems

### European Union

- **ENISA:** Post-quantum cryptography guidelines
- **BSI (Germany):** Technical guidelines for PQC migration
- **ANSSI (France):** Hybrid-mandatory approach

### Financial Sector

- **PCI DSS:** Monitoring PQC requirements for payment industry
- **SWIFT:** Post-quantum readiness program for financial messaging
- **Central banks:** Evaluating PQC for payment systems

## 19.11 Common Pitfalls and Lessons Learned

1. **Underestimating scope:** Cryptography is everywhere — inventory takes longer than expected
2. **Ignoring embedded systems:** IoT and OT devices are hardest to migrate
3. **Vendor lock-in:** Proprietary systems without upgrade paths
4. **Testing insufficient:** PQC changes subtle behaviors (timing, sizes, error handling)
5. **Big-bang approach:** Trying to migrate everything at once — phased approach works better
6. **Ignoring data at rest:** Focus on protocols but forget stored encrypted data
7. **Compliance tunnel vision:** Meeting minimum requirements without genuine security improvement
8. **Underestimating bandwidth:** PQC's size impact on constrained networks

## 19.12 Key Takeaways

- Cryptographic agility is both the solution and the long-term strategy
- Migration follows: Inventory → Assess → Plan → Execute → Validate
- Prioritize by risk: HNDL-vulnerable data with long lifetimes first
- Hybrid deployment is the recommended transition pattern
- Dependencies (libraries, HSMs, vendors) often determine the critical path
- Testing (interoperability, performance, security) is essential before production
- Government mandates provide both motivation and timelines
- Start now — even if the CRQC is years away, migration takes years too

---

*Next: [Chapter 20 — Cryptographic Bill of Materials (CBOM)](./20-cbom.md)*
