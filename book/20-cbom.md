# Chapter 20: Cryptographic Bill of Materials (CBOM)

## 20.1 What Is a CBOM?

A **Cryptographic Bill of Materials (CBOM)** is a structured inventory of all cryptographic assets, dependencies, and configurations within a system, application, or organization. It answers the fundamental question: "What cryptography are we using, where, and how?"

CBOM extends the concept of Software Bill of Materials (SBOM) — which catalogs software components and dependencies — into the cryptographic domain. While SBOM tells you what libraries you're using, CBOM tells you what cryptographic algorithms, keys, certificates, and protocols those libraries implement.

## 20.2 Why CBOM Matters for PQC Migration

The PQC transition cannot succeed without knowing what needs to change. CBOM provides:

1. **Visibility:** Complete picture of cryptographic usage across the organization
2. **Risk assessment:** Identify quantum-vulnerable algorithms and their exposure
3. **Planning:** Understand dependencies and sequence for migration
4. **Progress tracking:** Measure migration completion quantitatively
5. **Compliance:** Demonstrate readiness to regulators and auditors
6. **Ongoing management:** Continuous monitoring for cryptographic drift

### Without CBOM

Organizations attempting PQC migration without CBOM face:
- Unknown scope (how many systems use RSA? ECDSA? Which key sizes?)
- Surprise dependencies (vendor systems, embedded components)
- Incomplete migration (forgotten systems remain vulnerable)
- Inability to demonstrate progress to leadership

### With CBOM

- Query: "Show all uses of RSA or ECDH in High-Value Assets" → immediate migration targets
- Track: "In January we had 10,000 RSA instances; now we have 4,000" → measurable progress
- Verify: "Zero quantum-vulnerable algorithms in payment systems" → compliance evidence

## 20.3 CBOM Standards and Formats

### CycloneDX Cryptographic BOM

CycloneDX (an OWASP standard) has native support for cryptographic assets:

**Supported component types:**
- `crypto:algorithm` — Specific algorithm instances
- `crypto:certificate` — X.509 and other certificates
- `crypto:key` — Cryptographic keys with metadata
- `crypto:protocol` — Protocol configurations (TLS, SSH, etc.)
- `crypto:related-crypto-material` — Tokens, seeds, IVs

**Example CycloneDX CBOM entry:**

```json
{
  "type": "crypto:algorithm",
  "name": "RSA",
  "cryptoProperties": {
    "algorithmMode": "PKCS1v15",
    "keySize": 2048,
    "cryptoFunctions": ["sign", "verify"],
    "classicalSecurityLevel": 112,
    "quantumSecurityLevel": 0,
    "nistQuantumSecurityLevel": 0
  }
}
```

### NIST CBOM Guidance

NIST SP 1800-38 (Quantum Readiness: Migration to Post-Quantum Cryptography) emphasizes:
- Automated discovery of cryptographic assets
- Machine-readable format for inventory data
- Integration with risk management frameworks
- Continuous monitoring and updating

### Key CBOM Fields

| Field | Description | Example |
|-------|-------------|---------|
| Algorithm | Specific algorithm used | RSA-2048, AES-256-GCM |
| Function | Cryptographic purpose | Encryption, signing, key exchange |
| Key size | Bit length of key | 2048, 256, 384 |
| Location | Where deployed | Application X, server Y |
| Library | Implementation library | OpenSSL 3.0.2 |
| Protocol | Protocol context | TLS 1.3, SSH, IPsec |
| Quantum status | Vulnerable/safe/hybrid | Vulnerable (RSA), Safe (AES-256) |
| Data sensitivity | Classification | Confidential, Public |
| Data lifetime | Required protection period | 25 years |
| Owner | Responsible team | Infrastructure, AppDev Team 3 |

## 20.4 Discovery Methods

### Static Analysis

Scan source code for cryptographic API usage:

**What to detect:**
- Crypto library function calls (OpenSSL, BoringSSL, libsodium, etc.)
- Algorithm name strings ("AES", "RSA", "SHA256")
- Key size specifications
- Certificate loading/parsing
- TLS configuration

**Tools:**
- Semgrep rules for crypto patterns
- CodeQL queries for cryptographic APIs
- Custom AST analyzers for specific languages
- SAST tools with crypto-awareness plugins

### Network Analysis

Monitor network traffic for cryptographic protocol usage:

**What to detect:**
- TLS versions and cipher suites in use
- SSH key exchange algorithms
- IPsec/IKE proposals
- Certificate chains exchanged
- Protocol downgrade patterns

**Tools:**
- Network TAP/SPAN with TLS inspection
- SSL/TLS scanner (sslyze, testssl.sh)
- SSH scanner (ssh-audit)
- Passive network monitoring

### Configuration Analysis

Examine system and application configurations:

**What to detect:**
- TLS cipher suite configurations
- SSH server/client configurations
- VPN algorithm settings
- Key store contents
- Certificate validity and algorithms

**Tools:**
- Configuration management databases (CMDB)
- Certificate management platforms
- HSM inventory systems
- Cloud service configuration scanners

### Binary Analysis

For compiled software without source access:

**What to detect:**
- Linked cryptographic libraries
- Algorithm constants in binary (S-boxes, round constants)
- Crypto API symbol imports
- Key material in memory

**Tools:**
- Binary composition analysis
- Symbol table inspection
- Entropy analysis for embedded keys
- Runtime monitoring

## 20.5 Building and Maintaining a CBOM

### Initial Creation

```
Step 1: Scope Definition
├── Which systems? (all production? development too?)
├── Which depth? (application layer? infrastructure? hardware?)
└── Which accuracy? (automated only? manual validation?)

Step 2: Automated Discovery
├── Run static analysis on codebases
├── Scan network configurations
├── Inventory certificates from CT logs and CA databases
├── Scan cloud service configurations
└── Check container images and dependencies

Step 3: Manual Enrichment
├── Classify data sensitivity
├── Determine data lifetimes
├── Identify dependencies and relationships
├── Assign ownership
└── Document exceptions and gaps

Step 4: Validation
├── Cross-reference with known architecture
├── Verify completeness (no missing systems)
├── Validate accuracy (spot-check findings)
└── Resolve conflicts and duplicates

Step 5: Publication
├── Store in machine-readable format (CycloneDX)
├── Generate reports for different audiences
├── Integrate with risk management tools
└── Establish update cadence
```

### Continuous Maintenance

CBOM is not a one-time activity:

- **CI/CD integration:** Scan new code/configs for crypto changes
- **Deployment monitoring:** Detect new crypto in production
- **Certificate monitoring:** Track certificate lifecycle
- **Library updates:** Flag when crypto libraries change
- **Drift detection:** Alert on unauthorized algorithm changes

### CBOM Lifecycle

```
Create → Validate → Analyze → Act → Monitor → Update → (repeat)
         ↑                                              |
         └──────────────────────────────────────────────┘
```

## 20.6 Using CBOM for PQC Migration

### Query Examples

**"What's quantum-vulnerable?"**
```
SELECT * FROM cbom 
WHERE quantum_status = 'vulnerable' 
ORDER BY data_sensitivity DESC, data_lifetime DESC
```

**"What's our migration progress?"**
```
SELECT 
  algorithm_family,
  COUNT(*) as total,
  SUM(CASE WHEN quantum_status = 'safe' THEN 1 ELSE 0 END) as migrated,
  ROUND(100.0 * SUM(CASE WHEN quantum_status = 'safe' THEN 1 ELSE 0 END) / COUNT(*)) as pct
FROM cbom
GROUP BY algorithm_family
```

**"What blocks our migration?"**
```
SELECT * FROM cbom
WHERE quantum_status = 'vulnerable'
AND (library_pqc_support = false OR hardware_pqc_capable = false)
ORDER BY risk_score DESC
```

### Dashboard Metrics

| Metric | Definition | Target |
|--------|-----------|--------|
| Quantum-vulnerable % | Vulnerable instances / total instances | 0% |
| Hybrid coverage % | Hybrid instances / total key exchanges | 100% during transition |
| Library currency | % of crypto libraries with PQC support | 100% |
| Certificate readiness | % of CAs capable of PQC issuance | 100% |
| Hardware readiness | % of HSMs with PQC support | 100% |

## 20.7 Integration with Security Frameworks

### NIST Cybersecurity Framework (CSF)

CBOM maps to CSF functions:
- **Identify:** Asset inventory (ID.AM)
- **Protect:** Data security (PR.DS), maintenance (PR.MA)
- **Detect:** Anomaly detection (DE.AE)
- **Respond:** Mitigation (RS.MI)
- **Recover:** Recovery planning (RC.RP)

### Zero Trust Architecture

CBOM supports zero trust principles:
- **Verify explicitly:** Confirm quantum-safe authentication at each boundary
- **Least privilege:** Ensure key access is minimal and tracked
- **Assume breach:** Identify what's exposed if any algorithm is broken

### Supply Chain Security

CBOM extends supply chain visibility:
- What crypto do third-party libraries use?
- Are vendor systems quantum-safe?
- What's the crypto posture of cloud services?
- Do SaaS providers have PQC roadmaps?

## 20.8 Automation and Tooling

### Open Source Tools

| Tool | Function | Language |
|------|----------|----------|
| IBM Quantum Safe Explorer | Code scanning for crypto | Multiple |
| Cryptosense Discovery | Network crypto analysis | Commercial |
| CycloneDX Tools | CBOM generation | Multiple |
| Certificate Transparency Monitors | Cert inventory | Various |
| ssh-audit | SSH config analysis | Python |
| sslyze | TLS configuration analysis | Python |
| trivy | Container security scanning | Go |

### Building Custom Discovery

For organization-specific needs:

```python
# Example: Simple Python crypto usage detector
import ast
import sys

CRYPTO_INDICATORS = {
    'RSA', 'ECDSA', 'AES', 'SHA256', 'HMAC',
    'Cipher', 'KeyPair', 'PrivateKey', 'PublicKey',
    'TLS', 'SSL', 'certificate', 'signature'
}

def scan_file(filepath):
    findings = []
    with open(filepath) as f:
        tree = ast.parse(f.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            func_name = ast.dump(node.func)
            for indicator in CRYPTO_INDICATORS:
                if indicator.lower() in func_name.lower():
                    findings.append({
                        'file': filepath,
                        'line': node.lineno,
                        'indicator': indicator,
                        'context': ast.dump(node)
                    })
    return findings
```

### Enterprise CBOM Platforms

Commercial platforms provide:
- Continuous scanning and monitoring
- Integration with ITSM and risk platforms
- Executive dashboards and reporting
- Compliance mapping and evidence
- Remediation workflow management

## 20.9 Challenges and Best Practices

### Challenges

1. **Scale:** Large organizations have thousands of applications
2. **Accuracy:** False positives from string matching; false negatives from obfuscation
3. **Completeness:** Shadow IT, undocumented systems, vendor black boxes
4. **Currency:** Crypto usage changes with every deployment
5. **Ownership:** Unclear responsibility for legacy systems
6. **Resources:** Initial inventory effort is substantial

### Best Practices

1. **Start imperfect:** A 60% accurate CBOM today beats a 95% accurate one next year
2. **Automate first:** Manual inventory doesn't scale
3. **Integrate into CI/CD:** Catch crypto changes at deployment time
4. **Prioritize by risk:** Focus on high-value assets first
5. **Use standards:** CycloneDX/SPDX for machine-readable output
6. **Assign ownership:** Every cryptographic component needs an owner
7. **Regular review:** Quarterly validation and update cycle
8. **Executive visibility:** Dashboard for leadership awareness

## 20.10 Key Takeaways

- CBOM is the foundation for successful PQC migration — you can't secure what you can't see
- Standards exist (CycloneDX) for machine-readable cryptographic inventories
- Discovery uses multiple methods: static analysis, network scanning, config review
- CBOM must be continuously maintained, not a one-time exercise
- Integration with security frameworks (CSF, Zero Trust) maximizes value
- Automation is essential at enterprise scale
- Start now with available tools; refine accuracy over time
- CBOM enables quantitative tracking of PQC migration progress

---

*Next: [Chapter 21 — Industry and Government PQC Initiatives](./21-industry-government.md)*
