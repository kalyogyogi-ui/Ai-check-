# Chapter 21: Industry and Government PQC Initiatives

## 21.1 Government Programs and Mandates

### United States

**National Security Memorandum 10 (NSM-10, 2022):**
- Directed federal agencies to inventory cryptographic systems
- Required migration plans within specific timelines
- Established the Quantum Computing Cybersecurity Preparedness Act
- Created urgency across the federal government

**OMB Memorandum M-23-02:**
- Requires agencies to submit cryptographic inventories
- Deadlines for identifying vulnerable systems
- Migration roadmap requirements
- Annual progress reporting

**CNSA 2.0 (NSA Commercial National Security Algorithm Suite 2.0):**

| Timeline | Requirement |
|----------|-------------|
| 2025 | PQC preferred for firmware and software signing |
| 2026 | PQC for web browsers, cloud services |
| 2027 | PQC for TLS, network protocols |
| 2030 | PQC for all new equipment acquisitions |
| 2033 | Complete migration for national security systems |

**NIST Post-Quantum Cryptography Program:**
- Standardization (FIPS 203, 204, 205) — completed 2024
- Migration guidance (SP 1800-38) — ongoing
- Validation testing (ACVP) — available
- Implementation guidance — published

**DHS/CISA:**
- Post-Quantum Cryptography Initiative
- Guidance for critical infrastructure
- Awareness campaigns for private sector
- Technical assistance programs

### European Union

**ENISA (European Union Agency for Cybersecurity):**
- PQC algorithm recommendations
- Migration guidelines for EU institutions
- Research coordination across member states
- Standards harmonization with NIST selections

**BSI (German Federal Office for Information Security):**
- Technical Guideline TR-02102 updated for PQC
- Recommends FrodoKEM alongside NIST standards (conservative)
- Mandates hybrid mode (classical + PQC together)
- Earlier timeline pressure than NIST

**ANSSI (French National Cybersecurity Agency):**
- Strongest hybrid mandate: classical algorithm MUST be present
- Recommends only hybrid deployments, not PQC-only
- Conservative approach — wants extended validation of PQC
- Publishes algorithm whitelists

**European Cybersecurity Certification Scheme:**
- Future requirements for quantum-safe certification
- Impact on Common Criteria evaluations
- Cloud certification (EUCS) considering PQC requirements

### United Kingdom

**NCSC (National Cyber Security Centre):**
- Advice on preparing for quantum computers
- Phased approach: awareness → preparation → migration
- Emphasis on cryptographic agility
- Industry engagement through CyberFirst and similar programs

### Asia-Pacific

**Japan (CRYPTREC):**
- Evaluating NIST selections for Japanese standards
- Parallel research programs on quantum-safe cryptography
- Government procurement guidelines updating

**South Korea (KISA):**
- National PQC migration program
- KpqC competition for additional algorithm evaluation
- Industry engagement for critical infrastructure

**China:**
- Separate PQC standardization effort (partially aligned with NIST)
- Significant quantum computing investment
- National standards for PQC algorithms
- Strategic priority for quantum readiness

**Australia (ASD):**
- Aligned with Five Eyes partners on PQC timelines
- ISM (Information Security Manual) updates for PQC
- Critical infrastructure protection guidance

## 21.2 Industry Initiatives

### Technology Companies

**Google/Alphabet:**
- Chrome browser: Hybrid PQC key exchange deployed since 2024
- Internal infrastructure: Progressive PQC migration
- Research: NTRU-HRSS variant, PQC performance optimization
- Cloud: PQC in Google Cloud VPN and other services

**Microsoft:**
- Windows: PQC in TLS stack (Schannel)
- Azure: PQC key exchange support
- Research: SymCrypt PQC implementation, PQC for Signal
- Quantum: Microsoft Quantum development and PQC integration

**Apple:**
- iMessage: PQ3 protocol with ML-KEM ratcheting
- iOS/macOS: PQC library integration
- Research: Efficient PQC for mobile platforms

**Amazon/AWS:**
- AWS KMS: Post-quantum key agreement support
- s2n-tls: Hybrid PQC key exchange
- AWS CloudHSM: PQC algorithm roadmap
- Research: PQC for AWS services

**Meta:**
- Internal infrastructure PQC evaluation
- Messaging services PQC consideration
- Research contributions to PQC community

**Cloudflare:**
- Full hybrid PQC deployment across network
- Published performance measurements
- Open-source CIRCL library (Go PQC)
- Research on PQC certificate optimization

### Messaging and Communication

**Signal:**
- PQXDH protocol deployed (ML-KEM-1024 + X25519)
- First major messaging app with PQC protection
- Open specification for community adoption

**WhatsApp / Meta Messenger:**
- Following Signal's approach
- PQC integration in progress
- Billions of users to protect

### Financial Services

**SWIFT:**
- Quantum-safe readiness program
- Testing PQC for financial messaging
- Timeline aligned with regulatory requirements
- Member engagement and awareness

**Major Banks:**
- JPMorgan, Goldman Sachs, Deutsche Bank: PQC pilots
- Quantum-safe VPN connections between trading centers
- HSM upgrades for PQC key management
- Certificate infrastructure preparation

**Payment Networks:**
- Visa, Mastercard: PQC research and pilots
- PCI SSC: Monitoring PQC standards for future requirements
- HSM certification for PQC algorithms

### Telecommunications

**GSMA:**
- Post-Quantum Telco Network Taskforce
- Guidelines for mobile network PQC migration
- SIM card PQC capability roadmap
- Network equipment vendor coordination

**Major Carriers:**
- Vodafone, AT&T, Deutsche Telekom: PQC pilot programs
- VPN/IPsec migration for backbone networks
- 5G security architecture PQC considerations

### Hardware and Semiconductor

**Intel:**
- PQC acceleration in future CPUs (instruction set extensions)
- Firmware signing with PQC
- Platform security (TPM, SGX) PQC updates

**Thales/Gemalto:**
- HSM firmware updates for PQC algorithms
- Luna HSM PQC support
- Smart card PQC roadmap

**Entrust:**
- nShield HSM PQC support
- PKI platform PQC certificate issuance
- Code signing PQC integration

**NXP/Infineon:**
- Smart card chips with PQC capability
- Automotive security PQC support
- IoT hardware PQC readiness

## 21.3 Standards Organizations

### IETF (Internet Engineering Task Force)

Active PQC-related RFCs and drafts:
- **RFC 9370:** PQC key exchange in IKEv2
- **Hybrid TLS:** Key share combination for TLS 1.3
- **PQC certificates:** X.509 with PQC algorithms
- **Composite signatures:** Multiple signatures in one structure
- **PQC in S/MIME:** Email security updates
- **PQC in DNSSEC:** DNS security adaptations

### ISO/IEC

- ISO/IEC 14888 (digital signatures): Adding PQC algorithms
- ISO/IEC 18033 (encryption): PQC encryption standards
- ISO/IEC 11770 (key management): PQC key agreement
- Joint Technical Committee 1 / SC 27: Coordinating with NIST

### ETSI (European Telecommunications Standards Institute)

- QSC (Quantum-Safe Cryptography) working group
- TR 103 619: PQC implementation guidance
- Migration guidelines for telecom industry
- Interoperability testing framework

### TCG (Trusted Computing Group)

- TPM 2.0 specification updates for PQC
- Algorithm registry for PQC in trusted hardware
- Platform integrity with PQC measurements
- Remote attestation with PQC

## 21.4 Research and Academic Initiatives

### Major Research Programs

**EU Quantum Flagship:**
- €1 billion investment in quantum technologies
- PQC research as part of communication pillar
- Industry-academic collaboration

**US National Quantum Initiative:**
- Multi-agency quantum research coordination
- PQC research through NSF, DARPA, DOE
- Quantum internet testbeds with PQC

**Open Quantum Safe (OQS):**
- Open-source PQC library (liboqs)
- Integration with OpenSSL, BoringSSL
- Reference implementations for all NIST candidates
- Community-maintained, university-led

### Academic Conferences

Key venues for PQC research:
- **CRYPTO / EUROCRYPT / ASIACRYPT:** Top-tier cryptography
- **PQCrypto:** Dedicated PQC conference (biennial)
- **CHES:** Cryptographic Hardware and Embedded Systems
- **CCS / IEEE S&P:** Applied security

### Cryptanalysis Community

Ongoing analysis of deployed standards:
- **Lattice Estimation tools:** Estimating concrete security
- **Reduction improvements:** Tighter security proofs
- **Implementation attacks:** Side-channel and fault analysis
- **Quantum algorithm research:** Better quantum attacks (if any)

## 21.5 Industry Consortia and Alliances

### PQC Coalition

Industry group coordinating PQC migration:
- Member companies share best practices
- Interoperability testing events
- Vendor coordination for ecosystem readiness
- Public guidance documents

### NCCoE (National Cybersecurity Center of Excellence)

NIST's collaborative research center:
- PQC migration demonstration projects
- Reference architectures
- Practice guides (SP 1800 series)
- Industry partner engagement

### Cloud Security Alliance (CSA)

- Quantum-safe security guidance for cloud
- Working group on PQC in cloud services
- Guidance for cloud service providers and consumers

### Linux Foundation / PQCA

Post-Quantum Cryptography Alliance:
- Open-source PQC ecosystem coordination
- Reference implementations
- Testing and validation infrastructure
- Industry collaboration on common challenges

## 21.6 Supply Chain Considerations

### Vendor Readiness Assessment

Questions for vendors:
1. Do you have a PQC migration roadmap?
2. When will your products support FIPS 203/204/205?
3. Can your current products be upgraded to PQC?
4. What's your PQC testing and validation status?
5. Do you support hybrid mode during transition?
6. What's the cost/effort for PQC upgrades?

### Critical Supply Chain Dependencies

| Component | Current Status | Challenge |
|-----------|---------------|-----------|
| TLS libraries (OpenSSL, etc.) | PQC support available | Application recompilation/update |
| HSMs | Firmware updates rolling out | May require hardware replacement |
| Smart cards/tokens | Limited PQC support | Hardware refresh cycle |
| Network equipment | Vendor-dependent | Firmware/hardware updates |
| Certificate authorities | PQC issuance beginning | Trust store updates |
| Cloud services | Major clouds supporting | Customer application updates |

## 21.7 Economic Considerations

### Cost of Inaction

- **Data breach from quantum attack:** Potentially existential for some organizations
- **Regulatory non-compliance:** Fines, sanctions, loss of contracts
- **Competitive disadvantage:** Clients requiring quantum-safe services
- **Retroactive liability:** If preventable breach occurs with known timeline

### Cost of Action

- **Technology investment:** Library updates, HSM replacements, testing
- **Personnel:** Training, hiring cryptography expertise
- **Performance overhead:** Bandwidth costs during transition
- **Opportunity cost:** Engineering effort diverted from other priorities

### ROI Framework

Migration ROI improves with:
- Higher value of protected data
- Longer required data confidentiality period
- Regulatory pressure and compliance requirements
- Competitive advantage of early quantum readiness
- Reduced cost of gradual vs. emergency migration

## 21.8 Key Takeaways

- Governments worldwide are mandating PQC migration with specific timelines
- US CNSA 2.0 requires progressive PQC adoption through 2033
- Major technology companies have already deployed PQC in production
- Financial services and telecommunications are actively preparing
- Standards organizations are integrating PQC across protocol specifications
- Hardware vendors are adding PQC support to HSMs, TPMs, and chips
- Industry consortia provide coordination and best practice sharing
- Supply chain readiness varies — assess vendors' PQC roadmaps
- Early movers gain competitive advantage and reduced migration risk

---

*Next: [Chapter 22 — Future Directions and Open Problems](./22-future-directions.md)*
