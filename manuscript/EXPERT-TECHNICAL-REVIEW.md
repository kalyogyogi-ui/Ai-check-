# Expert Technical & Editorial Review

**Reviewer role:** Technical reviewer + developmental editor (cryptography / PQC / enterprise migration)  
**Manuscript location:** `manuscript/chapters/`, `manuscript/appendices/`  
**Review date:** 2026-05-25  

---

## Executive verdict

| Question | Verdict |
|----------|---------|
| Is the **original** draft technically usable? | **Yes** — broad coverage, mostly correct cryptography, timely FIPS focus |
| Did the **automated “author voice” pass** fix the book? | **No — it made several things worse** |
| Is author voice now authentic end-to-end? | **No** — ~90% of body text is still encyclopedic / LLM-style |
| Are figures “proper” technical architecture? | **Partially** — many are generic; some are **misplaced** or **off-topic** |
| Ready for publisher? | **No** — needs human rewrite, sourced benchmarks, figure redesign, remove botched section numbers |

**Bottom line:** You were right to push back. The previous delivery was **cosmetic** (headers + Mermaid blocks), not the **chapter-by-chapter author rewrite and technical hardening** you asked for.

---

## What the automated pass did wrong (specific defects)

### 1. Fake section numbering (unpublishable)

Every chapter ends with `## N.99 Author's Closing Perspective`. **Section 99 does not exist** in your outline; publishers and reviewers will treat this as an error or AI artifact.

### 2. Copy-paste “Author's note” (technically embarrassing)

The **same** note was injected into **16 unrelated chapters**:

> *When in doubt, pilot hybrid TLS on internal services first…*

That advice is **wrong context** for: lattice math (Ch. 5), ML-KEM spec (Ch. 11), SLH-DSA (Ch. 13), multivariate (Ch. 8), quantum fundamentals (Ch. 2), CBOM (Ch. 20), etc. A technical reviewer would flag this as **template spam**, not expertise.

### 3. Figures placed incorrectly

Example: **Figure 1.2 (HNDL)** was inserted **inside §1.1** after the RSA paragraph, splitting the narrative. Figures must follow the **first paragraph of the section they illustrate**, not mid-argument.

### 4. Author voice only in ~5% of words

Openers/closings use “we”; the body still reads like anonymous reference prose (“Cryptography is the invisible foundation…”, “The United States has taken the most comprehensive…”).

### 5. Diagrams too shallow for a technical book

Many Mermaid charts are 4–6 nodes with labels like `App → TLS → liboqs`. They are **slide-deck level**, not **architecture diagrams** (no trust boundaries, data flows, byte sizes, failure modes, HSM boundaries).

### 6. Technical review gaps (unchanged from original)

| Issue | Example | Severity |
|-------|---------|----------|
| Unsourced statistics | “4.5 billion users”, “$35B investment”, Ponemon “40%” | High |
| Benchmark tables without provenance | Ch. 17 μs timings — no CPU, library, date | High |
| Forward-dated deployment claims | Chrome/Signal “2024 full deployment” — needs RFC/blog cite | Medium |
| HQC / FN-DSA as finalized FIPS | Often stated as done; still **in progress** | Medium |
| SIKE break date | July vs August 2022 inconsistent | Low |

### 7. India content still thin

Ch. 21 India block remains a **short bullet list**; not integrated into migration (Ch. 19) or TLS (Ch. 18). Not adequate for an India-based author positioning.

### 8. Front matter still placeholder

`[Your Name]` — cannot submit.

---

## Chapter-by-chapter scorecard (after voice pass)

**Voice** = authorial, consistent practitioner tone in **body**, not only intro.  
**Tech** = cryptographic correctness + citations + deployability.  
**Figs** = relevant, well-placed, publication-grade.

| Ch | Title | Voice | Tech | Figs | Critical fix |
|----|-------|-------|------|------|----------------|
| 1 | Introduction | D | B+ | C | Rewrite §1.1–1.4; move Fig 1.2; cite Mosca/GRI |
| 2 | Quantum fundamentals | D | A- | C | Remove TLS note; add error-correction depth cite |
| 3 | Quantum attacks | D | A | C | Keep Shor steps; add resource estimates (CRQC gates) |
| 4 | PQC overview | D | A- | B | Family comparison table needs sources |
| 5 | Lattices | D | A | C | Remove TLS note; add toy LWE example |
| 6 | Code-based | D | A- | C | McEliece size vs TLS MTU figure |
| 7 | Hash-based | D | A | C | Stateful vs stateless **operations** diagram |
| 8 | Multivariate | D | A- | C | Rainbow break OK; date-stamp NIST extra sig round |
| 9 | Isogeny | D | A- | B | SQISign “experimental” banner |
| 10 | NIST process | D | A | B | Good history; cite NISTIR 8105 |
| 11 | ML-KEM | D | A | C | **Remove TLS note**; add byte-size + KAT figure |
| 12 | ML-DSA | D | A | C | Signing latency percentiles |
| 13 | SLH-DSA | D | A- | C | Parameter selection flowchart |
| 14 | Additional candidates | D | A- | C | FN-DSA float-FFT warning diagram |
| 15 | Hybrid | C | A | B | Best topic-fit; still needs combiner security cite |
| 16 | Implementation | C | A | B | Strongest; expand STQC/FIPS 140-3 India path |
| 17 | Performance | D | B | C | **Reject table until sourced** |
| 18 | TLS/PKI | D | A- | B | Cert chain byte budget figure |
| 19 | Migration | C | A- | B | Good structure; India playbook missing |
| 20 | CBOM | D | B+ | C | Remove TLS note; cite CycloneDX spec version |
| 21 | Industry/gov | D | B+ | C | Expand India; verify NQM ₹ figure source |
| 22 | Future | D | A- | C | Mark research claims speculative |
| A | Math appendix | N/A | A | B | OK as reference |
| B | Glossary | N/A | A- | — | Update FIPS 206/207 status |
| C | Tools | N/A | B+ | C | Version-date all tools |
| D | Bibliography | N/A | A | — | Strongest asset |

**Grades:** A excellent · B good with fixes · C weak · D not author voice / botched pass

---

## What “proper” author voice + figures should look like

**Voice (body paragraph example — target style):**

> *When we inventory Indian banks, the first surprise is not missing PQC code—it is **three TLS libraries** in one payment stack. Migration starts by naming those dependencies, not by debating whether IBM's Condor qubit count matters in 2033.*

**Figure (target quality):**

- Caption states **what decision** the figure supports  
- Shows **trust boundaries**, **algorithm names**, **sizes** where relevant  
- Placed immediately after the section intro it supports  

---

## Corrective actions (in progress in repo)

1. Remove all `§N.99` blocks → replace with `## Chapter Summary`  
2. Delete generic hybrid-TLS notes from non-TLS chapters  
3. Relocate misplaced figures (Ch. 1 Fig 1.2 → §1.4)  
4. Add chapter-specific `Author's note` only where relevant  
5. Substantive rewrite pilot: **Ch. 1 §1.1** (see updated `01-introduction.md`)  
6. This review document for your submission package  

---

## Recommendation to author

Do **not** send the voice-pass branch to publishers as-is. Plan:

1. **4–8 weeks** human rewrite (or hire crypto editor) on body text  
2. Commission **professional diagrams** (or Mermaid with byte counts + RFC numbers)  
3. Legal review India regulatory sentences  
4. Cryptographer **read-through** of Ch. 11–13 against FIPS PDFs  

---

*This review supersedes any prior implication that the automated pass completed author voice transformation.*
