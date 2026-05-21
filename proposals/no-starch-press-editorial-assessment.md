# No Starch Press — Editorial Assessment & Acquisitions Brief
### Catalog audit (Blockchain, AI, Quantum) · Submission requirements · Book ideas matched to house voice

> Compiled: May 2026 · Author: Senior acquisitions-style editorial assessment
> All catalog items verified by live searches against `nostarch.com` and full reads of their public Programming, Hacking & Computer Security, and category taxonomy pages. Where I could not verify, I say so.

---

## 0. Executive summary

| Domain | What's on the shelf | Editorial verdict |
|---|---|---|
| **Blockchain / Web3** | One non-technical Bitcoin title from 2014; one Python ciphers book (2018) that touches Bitcoin; *Crypto Dictionary* (2021) which is **explicitly cryptography, not cryptocurrency**; *Serious Cryptography 2e* (2024). **No Solidity, Ethereum, smart contract, DeFi, ZK, Hyperledger, Solana, or Move book in catalog or 2026 pipeline.** | **Blue-ocean shelf.** A single well-pitched, hacker-voiced practitioner book could define this list. |
| **AI / Machine Learning** | ~20 titles. Strong recent investment: *Practical Deep Learning 2e* (2025, 584pp), *Deep Learning Crash Course* (2025, 680pp), *Machine Learning Q and AI* (2024), *How AI Works* (2023). | **Crowded but actively expanding.** 2026 pipeline is heavily security-tilted (*Practical AI Security*, *Red Teaming AI*) and engineering-tilted (*Post-Training*, *The Developer's Guide to AI*). Don't pitch another LLM intro. |
| **Quantum** | One dedicated title: *Quantum Computing* by Andrew Glassner. *Computer Architecture* covers quantum tangentially. *The Shape of Data* (Farrelly, 2023) touches QML in one chapter. | **Single-title shelf.** The intro slot is filled. Adjacent angles (PQC, hacker-tilted, Manga Guide) remain wide open. |
| **Cryptography (bridge)** | Strong: *Serious Cryptography 2e* (Aumasson, Aug 2024), *Crypto Dictionary* (Aumasson, 2021), *The Manga Guide to Cryptography* (2018), *Cracking Codes with Python* (Sweigart, 2018). | **The credibility bridge.** Every viable PQC, ZK, or crypto-engineering pitch sells against this list and benefits from it. |

**The single most acquirable pitch** — based on No Starch's editorial DNA, current gaps, and 2026 commissioning patterns — is a hacker-voiced, project-based, smart-contract-security book in the *Hacking: The Art of Exploitation* / *Black Hat Python* / *Cracking Codes with Python* tradition. Working title: ***Cracking Smart Contracts***. Section 5 below details ten more.

---

## Part 1 — Editorial DNA: how to read No Starch as an acquisitions editor

Verified from [`nostarch.com/about`](https://nostarch.com/about), [`nostarch.com/writeforus`](https://nostarch.com/writeforus), founder Bill Pollock interviews, and the books they actually publish:

### 1.1 The taxonomy they admit to

> "We focus on computer programming, security, hacking, alternative operating systems, STEM, and LEGO. Our titles have personality, our authors are passionate, and we read and edit everything we publish."

Wikipedia and their own copy expand that to: **networking, computer security, hacking, Linux, programming, technology for kids, Lego, math, science, alternative operating systems, open source.**

### 1.2 The house voice (extracted from their hits)

Their flagships are the answer key to their voice:
- *Hacking: The Art of Exploitation* (Erickson)
- *Black Hat Python*, *Black Hat Go*, *Black Hat GraphQL*
- *Practical Packet Analysis* (Sanders)
- *Practical Malware Analysis* (Sikorski & Honig)
- *The Linux Programming Interface* (Kerrisk) — heavyweight reference
- *How Linux Works* (Ward)
- *The Manga Guide* series (math, statistics, cryptography, calculus, physics, etc.)
- *Python Crash Course* (Matthes)
- *Automate the Boring Stuff with Python* (Sweigart)
- *Cracking Codes with Python* (Sweigart)
- *Serious Cryptography* (Aumasson)
- *Bitcoin for the Befuddled* (Barski & Wilmer)

Pattern recognition from this list:

1. **Hacker-curious, not corporate.** They publish for someone who wants to *take something apart*, not someone who wants a vendor certification.
2. **Project-based or build-it-yourself.** "Build your own X" titles (compiler, debugger, interpreter, malware analysis lab, smart-contract attack lab) have a strong fit.
3. **Visual + accessible at one end (Manga Guide, Crash Course, Befuddled), uncompromising at the other (Hacking AOE, Linux Programming Interface).** Few middle-of-the-road books.
4. **Personality on the page.** Pollock rejects manuals-as-books. Authors must have a voice.
5. **Heavy editing.** Differentiator vs Packt and self-published.
6. **Open source preferred.** Tools, datasets, and code should be free and runnable.
7. **They publish topics they care about.** Pollock: "I publish books on topics that I care about. I like to support passionate communities and passionate people."

### 1.3 The taboos (what they won't acquire)

- Pure-finance or pure-investor books. *Bitcoin for the Befuddled* is borderline; the rest of the list is engineering.
- Vendor-flavoured manuals dressed as books.
- "Blockchain for [non-tech industry]" survey books.
- Pure-academic monographs (Springer / Cambridge UP territory).
- Reheated LLM-101 books — they have these slots filled.

---

## Part 2 — Catalog inventory (verified)

### 2.1 Blockchain / cryptocurrency / Web3

> Verified by site searches for: blockchain, bitcoin, cryptocurrency, ethereum, solidity, smart contract, defi, web3, nft, hyperledger, solana, move, zero knowledge, zk-snark. Plus a full read of the Programming and Hacking categories.

| # | Title | Author | Date | ISBN | What it really is |
|---|---|---|---|---|---|
| B1 | *Bitcoin for the Befuddled* | Conrad Barski & Chris Wilmer | November 2014 | 9781593275730 | Non-technical 256-page Bitcoin primer. Pre-Ethereum. The only dedicated blockchain title. |
| B2 | *Cracking Codes with Python* | Al Sweigart | January 2018 | 9781593278229 | Python + classical ciphers + intro public-key. Bitcoin appears only as an example of where public-key crypto is used. **Not a blockchain book.** |
| B3 | *Crypto Dictionary* | Jean-Philippe Aumasson | March 2021 | 9781718501409 | 500-term cryptography reference. The book's own marketing copy includes *"A polemic against referring to cryptocurrency as 'crypto'"* — explicitly distancing from blockchain framing. |
| B4 | *Serious Cryptography, 2nd Edition* | Jean-Philippe Aumasson | August 2024 | 9781718503847 | Modern cryptography, including a PQC chapter. **Not a blockchain book.** |

**Editorial reading:** the blockchain shelf is effectively empty. Even being generous and counting cryptography titles that *mention* blockchain primitives, there is no engineering book on Solidity, Ethereum, smart contracts, DeFi, ZK proofs, Hyperledger, Solana, or Move. Their nearest analogues exist at Manning (Wong's *Real-World Cryptography*), O'Reilly (the *Mastering Bitcoin/Ethereum* franchise), Springer LNCS, and BPB. None at No Starch.

### 2.2 AI / Machine Learning

> Site search returns "24 results" for AI. The substantive titles:

| # | Title | Author | Date | Pages | Note |
|---|---|---|---|---|---|
| A1 | [*How AI Works*](https://nostarch.com/how-ai-works) | Ronald T. Kneusel | Sept 2023 | 192 | Pop-explainer. Demystifier slot. |
| A2 | [*Machine Learning Q and AI*](https://nostarch.com/machine-learning-and-ai-beyond-basics) | Sebastian Raschka | March 2024 | 264 | 30 advanced Q&As. Above-101 slot. |
| A3 | [*Practical Deep Learning, 2nd Edition*](https://nostarch.com/practical-deep-learning-python-2E) | Ronald T. Kneusel | July 2025 | 584 | CV, transfer learning, generative AI, RAG, in-context learning. |
| A4 | [*Deep Learning Crash Course*](https://nostarch.com/node/796) | Volpe, Midtvedt, Pineda, Klein Moberg, Bachimanchi, Pereira, Manzo | Nov 2025 | 680 | PyTorch; CNNs through transformers, diffusion, GNNs. |
| A5 | [*Deep Learning: A Visual Approach*](https://nostarch.com/deep-learning-visual-approach) | Andrew Glassner | — | — | No-math visual explainer. |
| A6 | [*Math for Deep Learning*](https://nostarch.com/math-deep-learning) | Ronald T. Kneusel | — | — | Probability, stats, linear algebra, calculus. |
| A7 | [*The Art of Machine Learning*](https://nostarch.com/node/641) | Norman Matloff | — | — | R-based, dataset-driven. |
| A8 | [*The Shape of Data*](https://nostarch.com/shapeofdata) | Farrelly & Gaba | July 2023 | 264 | Geometry-based ML in R; one chapter touches QML. |
| A9 | [*Machine Learning for Kids*](https://nostarch.com/machine-learning-kids) | Dale Lane | Feb 2021 | 288 | 13 ML projects for kids. |
| A10 | [*Malware Data Science*](https://nostarch.com/malwaredatascience) | Joshua Saxe with Hillary Sanders | Sept 2018 | 272 | ML applied to malware detection. |
| A11 | [*Math for Programming*](https://nostarch.com/math-programming/) | Ronald T. Kneusel | recent | — | Math foundations. |
| A12 | [*Elements of Data Science*](https://nostarch.com/elementsofdatascience) | — | — | — | Beginner data science. |
| A13 | [*Dive Into Data Science*](https://nostarch.com/dive-data-science/) | — | — | — | A/B tests, regression, ML. |
| A14 | [*Automate Excel with Python*](https://nostarch.com/) | John Wengler | March 2026 | — | "AI can write the code. You still need to know what it does." |

**Forthcoming / Early Access — the editorial signal:**

| # | Title | Author | Ship | Pages | Note |
|---|---|---|---|---|---|
| A15 | [*The Developer's Guide to AI*](https://nostarch.com/developers-guide-to-AI) | Orshalick, Reghunadh, Thompson | April 2026 | 320 | LLM integration for app developers. |
| A16 | [*Practical AI Security*](https://nostarch.com/practical-ai-security) | Harriet Farlow | April 2026 | 392 | Data poisoning, model theft, prompt injection. |
| A17 | [*Red Teaming AI*](https://nostarch.com/red-teaming-AI) | Philip A. Dursey | June 2026 | 500 | "Field manual for attacking intelligent systems." |
| A18 | [*Post-Training*](https://nostarch.com/post-training) | Chris von Csefalvay | Fall 2026 | 416 | Fine-tuning, alignment, deployment for AI engineers. |

**Editorial reading:** the 2026 list is **explicitly security-tilted and engineering-tilted**. They are no longer commissioning "another LLM intro" — they are commissioning *adversarial*, *production*, and *fine-tuning* angles. Pitch new AI books *into the gaps these titles leave*, not against them.

### 2.3 Quantum technology

| # | Title | Author | Date | Note |
|---|---|---|---|---|
| Q1 | [*Quantum Computing*](https://nostarch.com/quantum-computing) | Andrew Glassner | 2024+ | "A friendly introduction to quantum programming for complete beginners." Beginner slot occupied. |
| Q2 | [*Computer Architecture*](https://nostarch.com/computerarchitecture) | — | — | Broad history-of-computing book; quantum is one final chapter. |
| Q3 | [*The Shape of Data*](https://nostarch.com/shapeofdata) | Farrelly & Gaba | July 2023 | One chapter on distributed/quantum algorithms. |

**Editorial reading:** Glassner's introductory book holds the entry-level slot. There is no PQC book, no QML book, no quantum-hardware book, no quantum-networking book, no QEC book, no Manga Guide to Quantum, and nothing hacker-tilted. Multiple adjacent angles are open.

### 2.4 Cryptography (the bridge)

| # | Title | Author | Date | Pages | Note |
|---|---|---|---|---|---|
| C1 | [*Serious Cryptography, 2nd Edition*](https://nostarch.com/serious-cryptography-2nd-edition) | Aumasson | Aug 2024 | 376 | Modern crypto + PQC chapter. |
| C2 | [*Crypto Dictionary*](https://nostarch.com/crypto-dictionary) | Aumasson | Mar 2021 | 160 | 500-term reference. |
| C3 | [*The Manga Guide to Cryptography*](https://nostarch.com/mangacrypto) | Mitsuhashi & Tsutsumi | July 2018 | 248 | Visual narrative. |
| C4 | [*Cracking Codes with Python*](https://nostarch.com/crackingcodes) | Sweigart | Jan 2018 | 416 | Beginner cipher programming. |

This is the **credibility bridge** for any PQC, ZK, or crypto-engineering pitch. Aumasson is their flagship cryptography author. The Manga Guide format is a proven house franchise.

---

## Part 3 — Submission requirements (verified)

From [`nostarch.com/writeforus`](https://nostarch.com/writeforus):

### 3.1 What you must include

1. **A clear description of the book** — what it's about, who it's for, what makes it different.
   *They explicitly call this one of the two most important factors.*
2. **A detailed outline** — minimum: chapter titles plus first-level headings within each chapter.
   *The other most important factor.*
3. **Audience definition** — who is the target reader and how does the book meet their needs?
4. **Writing samples** — sample chapter, blog post, prior book, or other published technical writing in your voice.
5. **Author bio** — credentials, professional experience, online presence, how you'll help promote the book.

### 3.2 What an editor will weight beyond the form

Drawn from how their books actually look and what Bill Pollock has said in interviews:

- **Voice on the page.** A sterile manuscript will be edited heavily or rejected.
- **A named, passionate community.** Pitch to a specific tribe (smart-contract auditors, AI red-teamers, quantum hardware engineers), not a generic "developers" audience.
- **Hands-on/project-based pedagogy.** Their template is *build N things*, *break N things*, or *trace N concepts through code*.
- **Open-source toolchain.** Closed/proprietary stacks make a book obsolete fast and don't fit their values.
- **Visual treatment.** Diagrams, code listings, full-colour print, the Manga format. A pitch with strong visual planning lands better.
- **Authors willing to be edited heavily.** They edit everything.

### 3.3 Where to send

Per their site, proposals go to the editorial team via the Write for Us form / email. Bill Pollock founded the press and remains involved in acquisitions; recent jobs listings refer pitches to `editorial-team@nostarch.com`.

---

## Part 4 — What an editor at No Starch is actually looking for in 2026

Reading their forthcoming list as signal:

- **Cybersecurity remains the centre of gravity.** *The Ghidra Book 2e* (Feb 2026), *Red Team Engineering* (Feb 2026), *Practical AI Security* (Apr 2026), *Red Teaming AI* (Jun 2026), *Dissecting the Dark Web* (May 2026), *Foundations of Cybersecurity 2e* (Apr 2026), *The Spacecraft Hacker's Handbook* (Spring 2027).
- **AI security is a major bet.** Two adjacent titles in two months (Apr/Jun 2026), both 392–500 pp. They're positioning to own this micro-shelf.
- **Reference Linux/BSD systems internals.** *The Linux Memory Manager* (Fall 2026), *The Linux Command Line 3e*, *The Book of PF 4e* (Jan 2026).
- **Project-based / "build-your-own" continues.** *Building a Debugger*, *Computer Science From Scratch*, *Heavy Wizardry 101*, *The Art of 64-Bit Assembly Vol 2*.
- **Manga Guide franchise still active.** Multiple manga titles in their backlist; new ones occasionally.

**Implication for a new pitch:** a book that combines *security tilt* + *project-based pedagogy* + *named community* + *open toolchain* + *No Starch voice* will get the closest editorial reading.

---

## Part 5 — Book ideas, tailored to No Starch's house voice

> Not a wishlist. Each idea is matched to a specific NSP template (Hacking AOE, Black Hat X, Cracking X, Manga Guide, Practical X, Build Your Own X) and has a stated competitor / gap.

### 5.1 Blockchain / Web3 (10 ideas — the largest gap on their shelf)

| # | Working title | NSP template it fits | Hook | Why an editor will say yes |
|---|---|---|---|---|
| 1 | **Cracking Smart Contracts** | Sweigart's *Cracking Codes with Python* | "Build, break, and defend decentralized applications." | Same author archetype as Sweigart. Beginner-friendly, project-based, hands-on. Reader builds a DeFi protocol then breaks it five ways (re-entrancy, oracle manipulation, governance attack, MEV sandwich, signature replay) and audits it. **The single best fit on their entire missing shelf.** |
| 2 | **The Manga Guide to Blockchain** | Manga Guide series | A visual narrative explaining UTXO, consensus, smart contracts, ZK, account abstraction through illustrated chapters. | Manga Guide is a proven NSP franchise (13-book set). Blockchain is famously hard to teach without diagrams. |
| 3 | **Hacking Ethereum** | *Hacking: The Art of Exploitation* | A serious, hacker-voiced book on EVM internals, opcode-level analysis, gas-cost attacks, formal verification, and adversarial smart-contract testing. | The Erickson treatment but for the EVM. NSP has no Ethereum book; this is the heavyweight slot. |
| 4 | **Black Hat Solidity** | *Black Hat Python / Go / GraphQL* series | Offensive-tooling cookbook: write your own honeypot, your own MEV searcher, your own audit fuzzer, your own malicious upgrade. | Direct extension of their *Black Hat* franchise into Web3. |
| 5 | **Postmortems: 50 Smart Contract Disasters** | *Practical Malware Analysis* / *Practical Packet Analysis* | Annotated case studies: TheDAO, Parity multisig, Ronin, Wormhole, Nomad, Multichain, Euler, Curve, Mango, Poly Network. | Narrative + technical. Sells into corporate training. Matches their *Practical X Analysis* tradition. |
| 6 | **Build Your Own Blockchain** | *Build Your Own Debugger / Lisp / Compiler* tradition | From `genesis.json` to consensus to a working light client, in Rust. | NSP loves "build your own X" projects. Currently no blockchain version exists. |
| 7 | **The Smart Contract Auditor's Field Manual** | *Practical Packet Analysis* / *Bug Hunter's Diary* | Tooling-first: Foundry invariants, Slither, Echidna, Halmos, Certora, manual review checklists. | Named tribe (auditors), hacker tilt, current toolchain, security-driven — all NSP signals. |
| 8 | **Wallet Internals** | *The Linux Programming Interface* / *Operating Systems: Three Easy Pieces* | Heavyweight reference: BIP-32/39/44 derivation, hardware-wallet protocols, secure-element design, MPC custody, AA wallets, the post-EIP-7702 flow. | Heavyweight reference is a recognised NSP slot. Wallet engineering is unique territory. |
| 9 | **Cracking the Web3 Coding Interview** | extends *Cracking Codes* + interview-prep niche | EVM, Solidity, ZK, system design problems, mock interviews. Appendix with 100 problems. | New format for NSP but consistent with their hacker-pedagogy DNA. Sells into bootcamps. |
| 10 | **Bitcoin for the Befuddled, 2nd Edition (or Successor)** | direct sequel | Update the 2014 book for Taproot, the BIP-361 PQ migration debate, Lightning, modern wallets, and inscriptions/ordinals. | Their existing blockchain title is 12 years old. A 2e or branded successor is the lowest-risk acquisition. |

### 5.2 AI / Machine Learning (8 ideas — pitched into gaps in their pipeline)

| # | Working title | NSP template it fits | Hook | Why an editor will say yes |
|---|---|---|---|---|
| 11 | **The Manga Guide to Large Language Models** | Manga Guide series | Tokenisation, attention, transformers, RLHF, alignment — visualised. | NSP has no manga AI title. Demand is huge. |
| 12 | **Build Your Own Transformer** | *Build Your Own X* | From scratch in PyTorch: tokenizer, attention, training loop, RLHF, inference; runnable on a laptop. | The "from scratch" angle differentiates from *Practical Deep Learning 2e* and *Deep Learning Crash Course*. |
| 13 | **Hacking Neural Networks** | *Hacking: The Art of Exploitation* | Adversarial examples, gradient masking, model extraction, side-channel inference, jailbreaks, training-data extraction. | Adjacent to *Practical AI Security* and *Red Teaming AI* but **lower-level / more technical** — they leave room. |
| 14 | **Cracking AI Models** | *Cracking Codes with Python* | Beginner-friendly companion to #13: build your own attacks in Python, learn defences. | Sweigart-template entry point into AI security. |
| 15 | **Practical Prompt Engineering for Hackers** | *Practical X* | Prompt injection at scale, jailbreak chaining, agent abuse, defensive prompting, OWASP LLM Top 10. | Explicitly hacker-tilted; differentiated from *The Developer's Guide to AI*. |
| 16 | **AI for Reverse Engineers** | tooling cookbook | Use LLMs and ML to assist with binary analysis, decompilation, pattern matching, malware triage; integrates with Ghidra and IDA. | Bridges their AI list and their reverse-engineering list (*The Ghidra Book*, *Practical Malware Analysis*). |
| 17 | **AI Hardware: Build Your Own Inference Accelerator** | *Hardware / DIY* category | FPGA-based inference acceleration walkthrough; quantisation, custom kernels, INT8/INT4 deployment. | NSP has a Hardware/DIY shelf; AI hardware is missing. |
| 18 | **Machine Learning for Kids, Vol. 2: AI Agents** | direct sequel | Project-based; build a simple agent that can use tools and call APIs. | Kids' list is core NSP; agentic AI for kids has no major-publisher book. |

### 5.3 Quantum (6 ideas — the second-largest gap)

| # | Working title | NSP template it fits | Hook | Why an editor will say yes |
|---|---|---|---|---|
| 19 | **The Manga Guide to Quantum Computing** | Manga Guide series | Superposition, gates, entanglement, measurement, Grover, Shor — all illustrated. | Glassner's *Quantum Computing* (the existing NSP intro) is text-heavy; the manga audience is a different reader. |
| 20 | **Quantum Computing for Hackers** | *Hacking: The Art of Exploitation* | Grover and Shor as offensive primitives. Side-channel and fault-injection on quantum hardware. Defensive PQC. | Direct line to NSP's hacker DNA. No competing book. |
| 21 | **Practical Post-Quantum Cryptography** | *Serious Cryptography* successor | Engineering migration to ML-KEM, ML-DSA, SLH-DSA, FN-DSA, HQC. CBOM, hybrid TLS, code-signing supply chain. | Natural Aumasson-or-successor follow-up. NIST FIPS 203/204/205 effective Aug 2024; HQC selected Mar 2025. |
| 22 | **Build Your Own Quantum Simulator** | *Build Your Own X* | Implement a state-vector simulator from scratch in Rust or Python. Run real circuits on it. | "Build your own X" is a proven NSP format; no quantum version exists. |
| 23 | **Cracking Quantum Codes** | *Cracking Codes with Python* | Beginner's hands-on tour of Grover, Shor, BB84, E91 — written for the Sweigart audience. | Beginner-friendly entry to a topic where Glassner's existing book is intermediate. |
| 24 | **The Quantum Hardware Hacker's Handbook** | *Spacecraft Hacker's Handbook* template (Spring 2027) | How quantum hardware physically works (superconducting, trapped ion, neutral atom, photonic, silicon spin); attack surfaces; lab tooling. | NSP has explicitly committed to the *Hacker's Handbook* format with the spacecraft title. |

### 5.4 Cross-domain (5 ideas)

| # | Working title | NSP template it fits | Hook |
|---|---|---|---|
| 25 | **Black Hat Web3** | *Black Hat Python / Go / GraphQL* | Offensive Web3 toolkit: build your own MEV sandwich bot, exploit rapper, governance-attack tool. |
| 26 | **The Manga Guide to Cryptography, Vol. 2: Post-Quantum** | Manga Guide successor | Lattices, hash-based signatures, the FIPS 203/204/205 algorithms — illustrated. |
| 27 | **Cracking Zero-Knowledge Proofs** | *Cracking Codes* | Beginner Python introduction to Circom, Noir, and small Halo2 circuits. |
| 28 | **Hacking AI Agents On-Chain** | hybrid Hacking AOE + Black Hat | When the agent holds the keys: signing-policy attacks, intent-routing exploits, custody compromise, kill-switch design. |
| 29 | **The Crypto Engineer's Field Manual** | *Practical Packet Analysis* template | A unified field manual covering classical crypto, blockchain primitives, ZK, FHE, and PQC migration — for working backend engineers. |

---

## Part 6 — If I were the acquisitions editor: top 5 picks for FY 2026–27

Ranked by combined fit + gap-filling + commercial signal:

| Rank | Title | Tier | Why this one |
|---|---|---|---|
| 1 | **Cracking Smart Contracts** | P0 | Defines an empty shelf. Sweigart-template author archetype is a known NSP shape. Hacker tilt, project-based, beginner-accessible, security-driven. Lowest acquisition risk. |
| 2 | **Practical Post-Quantum Cryptography** | P0 | Aumasson follow-up energy. NIST FIPS standards effective; demand from regulated enterprises. Sells alongside *Serious Cryptography 2e*. |
| 3 | **Hacking Ethereum** | P1 | The heavyweight Erickson-tradition Ethereum book that doesn't exist anywhere. Fits NSP's flagship voice. |
| 4 | **The Manga Guide to Zero-Knowledge Proofs** | P1 | Manga Guide franchise + the single hardest topic in modern Web3 to teach. Differentiated and commercial. |
| 5 | **Build Your Own Blockchain** | P1 | "Build your own" is a proven template. Currently no blockchain version exists. Project-based pedagogy with a Rust toolchain fits NSP perfectly. |

---

## Appendix A — Sources

### Editorial DNA & taxonomy
- [`nostarch.com/about`](https://nostarch.com/about)
- [`nostarch.com/writeforus`](https://nostarch.com/writeforus)
- [`nostarch.com/jobs`](https://nostarch.com/jobs)
- [`en.wikipedia.org/wiki/No_Starch_Press`](https://en.wikipedia.org/wiki/No_Starch_Press)
- [opensource.com — "Meet Bill Pollock, founder of No Starch Press"](https://opensource.com/article/17/10/no-starch)
- [helpnetsecurity.com — "For the love of a good IT book"](https://www.helpnetsecurity.com/2018/06/25/no-starch-press-story/)

### Catalog pages used to verify titles and 2026 pipeline
- Programming category: `nostarch.com/taxonomy/term/2/...`
- Hacking & Computer Security category: `nostarch.com/taxonomy/term/5/all`
- Linux & BSD category: `nostarch.com/taxonomy/term/22/...`
- Specific title pages cited inline in §§ 2.1–2.4.

### Verified standards / industry context referenced in book ideas
- NIST FIPS 203/204/205 effective 14 August 2024; HQC selected 11 March 2025; FIPS 206 in development. ([NIST CSRC](https://csrc.nist.gov/projects/post-quantum-cryptography/))
- ERC-4337 + EIP-7702 active on Ethereum mainnet since Pectra (May 2025). (`blog.ethereum.org`)

## Appendix B — What this brief does not claim

- Not an exhaustive census of every NSP title ever published. Their backlist contains hundreds of titles; this brief covers the three named domains and the bridge cryptography list.
- No first-party sales numbers (private company, won't invent).
- The 2026 pipeline is a May 2026 snapshot. Acquisitions priorities can shift quarterly.
- "If I were the acquisitions editor" is editorial judgement, not a contract. Real acquisitions also depend on author availability, advance economics, list-fit at a given moment, and personal editor preferences I cannot model.

---

*End of editorial assessment.*
