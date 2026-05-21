# Book Proposal: *Cracking Smart Contracts*
### Build, Break, and Defend Decentralized Applications

> Status: Pre-acquisition proposal · Target publisher: **No Starch Press** · Priority **P0**
> Compiled: May 2026 · All technical claims and demand signals sourced; see Appendix A.

---

## 1. Working title

**Cracking Smart Contracts: Build, Break, and Defend Decentralized Applications**

Series-positioning subtitle (alternative for the cover): *A Hands-On Introduction to Solidity Security, Auditing, and Adversarial Web3*

## 2. One-line hook

> "$3.35 billion was stolen from Web3 protocols in 2025 alone. This is the book that teaches you to write the contracts that survive — and to find the bugs in the ones that don't."

## 3. Detailed description (~250 words)

*Cracking Smart Contracts* teaches Solidity, Foundry, and the modern smart-contract security toolchain by walking the reader through **seven complete projects** — a token, a vault, a DEX, a lending market, a governance DAO, a bridge, and an account-abstraction wallet — and **breaking each of them on purpose** before showing how to harden them.

The pedagogy is taken straight from No Starch's hits: build it, break it, fix it. The same arc that powered Sweigart's *Cracking Codes with Python* and Erickson's *Hacking: The Art of Exploitation*. By page 400 the reader has not just learned Solidity, they have written, exploited, and audited working DeFi systems. They have run Foundry invariant tests, Slither static analysis, Echidna fuzz campaigns, and Halmos symbolic execution against their own code. They know what a re-entrancy bug looks like in real source, and they know how to find one in someone else's.

The book ships with a versioned mono-repo. Each project lives in its own folder with a vulnerable version, a working exploit suite, a hardened version, and a test harness. The final chapter is a CTF: a fresh contract, no spoilers, the reader's first audit.

The audience is large and underserved. Existing material is either an aged 2019 O'Reilly book, a free open-source CTF (*Damn Vulnerable DeFi*), or a video course (Cyfrin Updraft). **There is no contemporary major-publisher book** that bundles modern Solidity (post-Pectra, 0.8.x) with the modern audit toolchain in a hands-on, security-first, beginner-accessible package.

## 4. Target reader persona

**Primary readers** (in order of size):

1. **Backend / full-stack engineers entering Web3.** Often coming from JavaScript, Python, or Go. They have read a Solidity tutorial. They have not yet written or broken a real contract. The book takes them from "I can write a `Hello World` contract" to "I can audit a vault."
2. **Junior security researchers / aspiring auditors.** Want a structured path to bug-bounty platforms (Code4rena, Sherlock, Cantina, Immunefi). The book is their training ground. Cyfrin's online course is the closest analogue and works well — but a book sells into corporate L&D budgets, libraries, university courses, and people who learn better from print.
3. **Senior engineers / staff engineers asked by their company to "review the contracts."** They have never used Foundry or Slither. They need a one-month ramp.
4. **Computer-science students taking a blockchain or applied-cryptography course.** The book is course-adoptable.

**Secondary readers:** PMs / CTOs scoping audit budgets; traditional Big-4 IT auditors crossing into Web3; smart-contract authors at audited protocols who want to think like an attacker.

**Not the audience:** non-technical investors, "blockchain for [X industry]" survey readers, Vyper/Rust-only developers (mentioned in the book but not the focus).

## 5. Prerequisites & reading level

- Comfortable in **one** general-purpose language (Python, JS, or Go preferred).
- Basic command-line literacy.
- No prior Solidity, Foundry, or cryptography knowledge required. The book teaches what's needed.
- The bar matches *Cracking Codes with Python* (Sweigart, NSP 2018) and is one notch below *Hacking: The Art of Exploitation* (Erickson, NSP).

**Difficulty curve:** Chapters 1-6 are gentle. Chapters 7-22 escalate steadily. Chapters 23-28 (the auditor's toolbox + capstone) are advanced.

## 6. Proposed table of contents

> ~440 pages, 32 chapters + appendices, full-colour. Format and length deliberately match *Cracking Codes with Python* (NSP 2018, 416pp) and *Practical Deep Learning, 2nd Edition* (NSP 2025, 584pp).

### Part I — Foundations (~60 pp)

**Chapter 1 — The Threat Model**
What you're getting into; $3.35B stolen in 2025; the difference between "exploit" and "feature" on an immutable chain; the canonical seven failure modes (re-entrancy, integer math, access control, oracle manipulation, flash loans, signature replay, governance attack); a tour of three famous incidents (TheDAO, Parity multisig, Wormhole).

**Chapter 2 — Setting Up the Lab**
Install Foundry, Anvil, Cast, Forge. Install Slither, Echidna, Halmos, Aderyn. Configure VS Code. The book's companion repository — clone, build, run tests. A 10-minute first exploit so the reader smells blood early.

**Chapter 3 — Solidity in 40 Pages**
The minimum Solidity needed for everything that follows: types, mappings, modifiers, events, errors, interfaces, inheritance, storage layout, gas, ABI, calldata. Deliberately compressed. Pointers to the Solidity docs for what we skip.

**Chapter 4 — How the EVM Actually Runs Your Code**
Stack, memory, storage. The opcode cheat sheet. Calldata vs memory vs storage. Why this matters for security (delegatecall, storage collision, proxy patterns).

### Part II — Project 1: A Vulnerable Token (~30 pp)

**Chapter 5 — Build It: Your First ERC-20**
Write a deliberately-broken ERC-20 from scratch. No imports, no OpenZeppelin. Deploy it to Anvil. Mint, transfer.

**Chapter 6 — Break It: Three Bugs, Three Exploits**
1. Missing access control on `mint()` -> unlimited supply attack.
2. Pre-0.8 integer math behaviour -> underflow exploit (instructive even with 0.8.x check; we re-introduce it explicitly).
3. Unchecked external call return -> silent failure.
Each bug is exploited in a Foundry test that assertively drains the contract.

**Chapter 7 — Fix It: The OpenZeppelin Mindset**
Refactor to use OpenZeppelin's `ERC20`, `Ownable`, `AccessControl`, and `SafeERC20`. Run the same exploits — watch them fail. Run Slither. Read the report.

### Part III — Project 2: A Vulnerable Vault (~35 pp)

**Chapter 8 — Build It: A Yield Vault**
Deposit, withdraw, share accounting. ERC-4626 introduced.

**Chapter 9 — Break It: Re-entrancy and Inflation**
1. Classic external-call re-entrancy via a malicious receiver.
2. Cross-function re-entrancy.
3. Read-only re-entrancy.
4. The first-depositor share-inflation attack.
Each exploit is a runnable Foundry test.

**Chapter 10 — Fix It: CEI, Guards, and Virtual Offsets**
Checks-Effects-Interactions. `ReentrancyGuard`. ERC-4626 virtual-offset defence. Re-run exploits, watch them break.

### Part IV — Project 3: A Vulnerable AMM/DEX (~40 pp)

**Chapter 11 — Build It: A Constant-Product Market Maker**
Uniswap-V2-style. Liquidity, swap, fee, LP tokens.

**Chapter 12 — Break It: The Oracle Problem**
1. Spot-price manipulation via flash loan.
2. Sandwich attack with two transactions.
3. Donation attack on the price calculation.
4. Slippage abuse via missing `minAmountOut`.

**Chapter 13 — Fix It: TWAP, Slippage Guards, Invariants**
Time-weighted averages. `minAmountOut`. Foundry **invariant testing** — write a property like "k never decreases" and let the fuzzer hunt for counter-examples.

### Part V — Project 4: A Vulnerable Lending Market (~40 pp)

**Chapter 14 — Build It: A Compound-V2-Style Market**
cToken, supply, borrow, liquidation, interest-rate model.

**Chapter 15 — Break It: Bad Oracles, Bad Math**
1. Manipulate the price oracle, drain the market.
2. Liquidation grief — block your own liquidation by gas-griefing.
3. Bad-debt accumulation when `liquidate()` is mis-priced.
4. Read-only re-entrancy strikes the lending market too.

**Chapter 16 — Fix It: Chainlink Oracles, Health Factors, Liquidation Incentives**
Production oracle patterns. Health-factor maths. Why bots care about the liquidation incentive.

### Part VI — Project 5: A Vulnerable Governance DAO (~35 pp)

**Chapter 17 — Build It: Governor + Timelock**
OpenZeppelin's Governor. Voting token, proposal, quorum, execute, timelock.

**Chapter 18 — Break It: Govern by Flash Loan**
1. The Beanstalk-style flash-loan governance attack.
2. Proposal-spam grief.
3. Vote-buying via bribes.
4. Re-org attack on the proposal queue.

**Chapter 19 — Fix It: Snapshots, Quorums, Timelocks**
Snapshot-style off-chain voting. Quorum tuning. Timelock-as-defence-in-depth.

### Part VII — Project 6: A Vulnerable Bridge (~30 pp)

**Chapter 20 — Build It: A Lock-and-Mint Bridge**
Validator set on chain B. Lock on A, mint on B. Burn on B, unlock on A.

**Chapter 21 — Break It: The Most-Hacked Pattern in Web3**
1. Signature replay across chains.
2. Fake validator-set attack (the Ronin pattern).
3. Message-replay on the same chain.
4. The Wormhole-style signature-verifier flaw, reproduced in miniature.

**Chapter 22 — Fix It: Chain-ID Binding, EIP-712, Validator Rotation**
EIP-712 typed data. Domain separators. Why "just hash the message" was wrong every time. Validator-set rotation patterns.

### Part VIII — Project 7: A Vulnerable AA Wallet (~30 pp)

**Chapter 23 — Build It: A Smart Account on ERC-4337 + EIP-7702**
EntryPoint, UserOperation, paymaster, account factory. The post-Pectra EOA-to-smart-account upgrade path (EIP-7702 has been live on mainnet since 7 May 2025).

**Chapter 24 — Break It: Paymaster Grief, Session-Key Abuse, Aggregator Collisions**
1. Paymaster-griefing by reverting after gas is paid.
2. Session-key over-permissioning.
3. Validator/executor confusion.
4. Replay attacks across smart-account nonces.

**Chapter 25 — Fix It: ERC-7579, Validator/Executor Separation, Nonces, Gas Limits**
Modular accounts. Gas-grief defenses. Why "the wallet is a smart contract" rewrites all your assumptions.

### Part IX — The Auditor's Toolbox (~70 pp)

**Chapter 26 — Static Analysis: Slither, Aderyn, Mythril**
What each tool catches. How to read a Slither report. How to write a custom Slither detector for your own codebase.

**Chapter 27 — Fuzzing: Echidna, Foundry Invariants, Medusa**
Property-based testing for smart contracts. Writing invariants. Tuning fuzzers. Real bugs that fuzzers caught.

**Chapter 28 — Symbolic Execution and Bounded Verification: Halmos**
What symbolic execution buys you over fuzzing. Practical Halmos. Where it scales and where it doesn't.

**Chapter 29 — Formal Verification: A Tour of Certora**
What FV is, what it is not. The cost-benefit of writing specs. A worked example on the vault from Project 2.

**Chapter 30 — Manual Review: Reading Like a Detective**
A 50-question audit checklist. Note-taking practice. The two-pass technique. How a senior auditor reads a 4,000-line codebase.

### Part X — Going Pro (~30 pp)

**Chapter 31 — Bug Bounty Platforms and Audit Contests**
Code4rena, Sherlock, Cantina, Immunefi, CodeHawks. How payouts work. How to pick a contest. How to write a finding.

**Chapter 32 — Capstone: Your First Audit**
A fresh, never-before-seen 600-line protocol. The reader has 4 hours. Write the report. The book provides the model answer at the end of the chapter — but only after the reader's own attempt.

### Appendices (~30 pp)

- **A — The EVM in 25 Pages.** Opcodes, gas, storage layout, memory model, calldata, return data, the call stack.
- **B — Foundry Cheat Sheet.** `forge`, `cast`, `anvil`, `chisel`. Most-used commands.
- **C — Slither / Echidna / Halmos Cheat Sheets.** One page each.
- **D — The 30 Most Common Smart-Contract Vulnerabilities, Annotated.** With CWE numbers and example exploit patterns.
- **E — Glossary.**
- **F — Companion Repo Layout.** What's in `cracking-smart-contracts/`.

## 7. Differentiator vs existing material

| Existing resource | What it is | Why this book is different |
|---|---|---|
| *Hands-On Smart Contract Development with Solidity and Ethereum* (Solorio, Kanna, Hoover, O'Reilly, 2019) | Practitioner Solidity tutorial | Pre-Foundry, pre-AA, pre-Solidity 0.8.x, no security tilt. Six years out of date in a fast-moving field. |
| *Mastering Ethereum, 2e* (Antonopoulos, Wood et al., O'Reilly, 2025) | Reference manual | Reference-style; wide; not project-based; not security-driven. |
| *Building Ethereum DApps* (Infante, Manning, 2019) | Practitioner DApp book | Pre-Foundry, pre-AA. Aged. |
| *Solidity Programming Essentials, 2e* (Modi, Packt, 2022) | Language reference | Language-focused, not security-focused. Pre-Pectra. |
| *Real-World Cryptography* (Wong, Manning, 2021) | Cryptography practitioner book | One chapter touches blockchain crypto; not a Solidity book. |
| *Damn Vulnerable DeFi* (OpenZeppelin, OSS) | Free CTF series | A challenge set, not a book. Hardhat-based; no narrative; no toolchain training; no audit pedagogy. **Complementary, not competitive.** |
| *Ethernaut* (OpenZeppelin, OSS) | Free CTF | Same as above. |
| *Cyfrin Updraft Security & Auditing* (Patrick Collins, free) | Video course | Excellent course; ~80 hours of video. Different medium, different price/distribution channel. The book is for readers who learn from print, sells into corporate L&D, libraries, and universities. |
| *Secureum / RareSkills bootcamps* | Online cohort programs | Paid cohorts ($2k-$5k). The book is a $40 product that opens this funnel for the next million developers. |

**The single sentence:** *Cracking Smart Contracts* is the **No Starch-voiced, Foundry-first, security-driven, project-based book that does not currently exist** anywhere on the major-publisher shelf.

## 8. Estimated market size & demand signals

| Signal | Evidence | Source |
|---|---|---|
| Smart-contract exploit losses | **$3.35B stolen from Web3 in 2025**, +37% YoY across 630+ incidents; average hack $5.3M (+66% YoY) | [Sherlock — Top 10 Best Smart Contract Auditing Companies in 2026](https://sherlock.xyz/post/top-10-best-smart-contract-auditing-companies-in-2026) |
| Cumulative exploit losses 2020-2025 | $3.8B; $3.1B in H1 2025 alone | [metana.io — What you Need to Know in 2026](https://metana.io/blog/smart-contract-security-guide/) |
| Top-5 vulnerability classes | Re-entrancy, integer overflow, access control, oracle manipulation, flash loans | metana.io (above) — exactly the seven projects in this book's TOC. |
| Smart-contract audit market | Audits priced $5K-$300K; typical $15K-$40K | [Sherlock — Smart Contract Audit Pricing 2026](https://sherlock.xyz/post/smart-contract-audit-pricing-a-market-reference-for-2026) |
| Bug-bounty platforms | Code4rena, Sherlock, Cantina, Immunefi, CodeHawks all active and paying | [Sherlock — Best Web3 Bug Bounties 2026](https://sherlock.xyz/post/best-web3-bug-bounties-in-2026-the-highest-paying-programs-on-every-platform) |
| Engineering supply | Cyfrin Updraft, Secureum, RareSkills, Web3 Security all running paid cohorts | publicly listed on each platform |
| Tooling adoption | Foundry, Slither, Echidna, Halmos all mainstream in 2024-2026 | tool docs (cited) |
| Active community | r/ethdev, Code4rena Discord, Cyfrin Discord, Secureum Discord | publicly visible |

**Buyer segments where the book sells in volume:**

- Audit firms (Trail of Bits, OpenZeppelin, Spearbit, Cyfrin, Cantina, Halborn, ConsenSys Diligence, Hexens, Pashov Audit Group, Guardian Audits) — corporate training budget.
- Bug-bounty platforms — onboarding material for new wardens.
- Universities running blockchain or applied-crypto courses — course-adoption potential.
- Web3 protocol teams — developer training spend ahead of audit.
- Bootcamps and L&D providers — included reading.
- Individual buyers via Amazon, NoStarch.com, O'Reilly Learning subscription, Humble Bundle.

**Volume estimate:** **[ESTIMATE]** A 5,000-10,000 unit first-year run is plausible based on No Starch's known performance with comparable security-tilted hands-on books (*Black Hat Python*, *Practical Malware Analysis*) and the size of the smart-contract security developer base. Companion training-cohort licensing and bug-bounty-platform onboarding can drive a comparable second-year revenue stream.

## 9. Suggested format

- **Print:** No Starch standard 7"x9" full-colour, ~440 pages.
- **Digital:** EPUB, KF8, PDF; free e-book bundled with print purchase per No Starch policy.
- **Companion repository:** versioned mono-repo, Apache-2.0 licensed.
- **Optional companion:** a printable / physical "CTF deck" — one card per attack class with the failure pattern, the canonical fix, and a one-line example. Sells separately or as a pre-order bonus.

## 10. Companion assets

The repo `cracking-smart-contracts/` ships with one folder per project:

```
cracking-smart-contracts/
  01-vulnerable-token/
    src/Vulnerable.sol
    src/Hardened.sol
    test/Exploit.t.sol
    test/Invariant.t.sol
    test/echidna/Property.sol
    slither.config.json
    foundry.toml
    README.md
  02-vulnerable-vault/
  03-vulnerable-amm/
  04-vulnerable-lending/
  05-vulnerable-governance/
  06-vulnerable-bridge/
  07-vulnerable-aa-wallet/
  auditor-toolbox/
    slither-detectors/
    echidna-templates/
    halmos-specs/
  capstone/
    target/        (the unseen audit target)
    solution/      (the model audit report — sealed in a separate branch until ready)
  ctf-deck/
    attack-cards/  (printable PDFs)
```

Every chapter's code compiles and runs against the tagged release. CI runs the entire repo against every push; broken chapters cannot be merged.

## 11. Suggested author archetype

A **single experienced practising auditor with content-creation experience** is the strongest profile. Examples of the right archetype (these are public-figure shapes, not specific individuals being pitched):

- A working senior auditor at Trail of Bits, OpenZeppelin, Spearbit, Cantina, Cyfrin, Hexens, Halborn, ConsenSys Diligence, or Guardian Audits, who also runs a YouTube channel, Substack, or Twitter presence with consistent technical content.
- A top Code4rena warden / Sherlock judge with public audit reports.
- An ex-Big-Four IT auditor who pivoted into Web3 (broader appeal for the secondary persona).

If a single author cannot carry the whole arc, the runner-up structure is **a working auditor as primary author + a senior educator co-author** (someone who has taught Solidity at scale via bootcamp, university, or YouTube).

The author must be willing to publish working exploit code for **toy contracts**, not for live mainnet contracts. The book's ethics chapter (in Chapter 1) and the publisher's liability stance must align here.

## 12. Priority tier

**P0 — ship within 6 months of contract.**

Reasoning:

- The toolchain has stabilised. Foundry is no longer churning weekly. Slither, Echidna, and Halmos are mature.
- The post-Pectra Ethereum stack (May 2025) is a stable target. Account abstraction is in production.
- Solidity 0.8.x is the long-term default; the next major version is not on the near-term horizon.
- A 12-month book risks being scooped by the next O'Reilly / Manning Solidity refresh.
- A 6-month book lands in the heart of the bug-bounty boom and the audit-firm hiring cycle.

## 13. Risk factors and mitigation

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Foundry / Slither / Halmos toolchain change between writing and ship | Medium | Medium | Pin every tool version in `foundry.toml` and `slither.config.json`. Companion repo branches: `book-print-1` (frozen at print date) and `main` (kept current). |
| Solidity language change (e.g., 0.9.x or 1.0) | Low-Medium | Medium | Book teaches the *concepts*; companion repo handles version-specific syntax. Digital edition gets free updates. |
| Ethereum AA / EIP-7702 spec change | Low | Medium | Chapter 23-25 is structured around principles + a code-first reference branch. |
| Author misuse of working-exploit material | Low | High | Strict editorial line: working exploits only against toy contracts in the repo. Ethics chapter. Coordinated-disclosure framing for the techniques themselves. |
| Competing major-publisher book commissioned mid-cycle | Low-Medium | Medium | The 6-month P0 window is the moat. Speed of execution is the defense. |
| Author scarcity / dropout | Medium | High | Maintain a backup co-author from the audit-firm pool. The companion repo is a contractual deliverable from chapter 1; if an author drops, the repo reduces re-onboarding risk. |
| Toxic community blowback from "teaching attacks" | Low | Low | The Web3 audit community already publishes far more aggressive material (Damn Vulnerable DeFi, public Code4rena finds, public post-mortems). The book sits within community norms. |
| Ethereum market downturn reducing demand | Medium | Low | Audit-firm hiring is counter-cyclical to bull markets; exploits accelerate in bear markets. The book sells either way. |
| Quantum / PQ migration (BIP-361 / Q-STARK) makes ECDSA-based exploits obsolete | Low (within shelf life) | Low | Out of scope; covered in the *Post-Quantum Blockchain Engineering* companion proposal. |

## 14. Marketing levers

- **Launch tied to Code4rena, Sherlock, Immunefi, and Cyfrin community channels.** Author does AMAs in each Discord at launch.
- **Companion CTF challenges.** A monthly "Cracking Smart Contracts" challenge, sponsored by a bug-bounty platform; winners get the print book + a Code4rena/Sherlock voucher.
- **Conference circuit:** EthCC, Devcon, ETHGlobal events, ETHDenver, the OWASP Web3 track, DEF CON Smart Contract Village.
- **Course adoption:** offer instructor copies + slide decks to universities running blockchain courses (Cornell, Stanford, Berkeley, IIT Bombay, NUS, ETH Zurich).
- **Bundle SKUs:** book + Cyfrin Updraft cohort discount; book + Secureum bootcamp discount; book + Code4rena First Flight ticket.
- **Localisations within 12 months:** Hindi, Mandarin, Japanese, Spanish, Portuguese — each maps to a high-volume Web3 developer market.
- **The CTF deck.** A printable / physical card deck of attack patterns. Pre-order bonus and conference giveaway. Becomes a desk artefact, which is its own distribution.

## 15. Why this is *the* No Starch pitch

Every No Starch heuristic from the editorial assessment is satisfied:

- **Hacker culture** — explicit "build, break, fix" pedagogy.
- **Project-based** — seven complete projects + a capstone.
- **Open-source toolchain** — Foundry, Slither, Echidna, Halmos, OpenZeppelin.
- **Voice on the page** — Sweigart-meets-Antonopoulos; conversational, irreverent, technically uncompromising.
- **Named passionate community** — smart-contract auditors and the bug-bounty cohort.
- **Visual treatment** — full-colour, code-heavy, with attack-flow diagrams per chapter.
- **Gap on their list** — No Starch's current blockchain shelf is *Bitcoin for the Befuddled* (2014). This book defines an empty shelf.
- **6-month P0 window** — toolchain stable, demand massive, gap unfilled.

The book ships into a $3.35-billion-a-year exploit-loss market, an active audit-firm hiring cycle, and a developer base measured in the hundreds of thousands. It does not compete with a single book in No Starch's catalog. It complements *Serious Cryptography 2e*, *Cracking Codes with Python*, *Black Hat Python*, *Practical Packet Analysis*, and *Practical Malware Analysis*. It opens a new house list.

---

## Appendix A — Sources for every non-trivial claim

### Demand signals
- [Sherlock — Top 10 Best Smart Contract Auditing Companies in 2026](https://sherlock.xyz/post/top-10-best-smart-contract-auditing-companies-in-2026): "$3.35 billion was stolen from Web3 protocols in 2025 — a 37% increase over 2024, across 630+ incidents. The average hack yielded $5.3M, up 66% year-over-year."
- [metana.io — What you Need to Know in 2026](https://metana.io/blog/smart-contract-security-guide/): "$3.8B stolen 2020-2025; $3.1B lost in H1 2025 alone." Top-5 vulnerabilities listed.
- [Sherlock — Smart Contract Audit Pricing 2026](https://sherlock.xyz/post/smart-contract-audit-pricing-a-market-reference-for-2026): audit price ranges.
- [Sherlock — Best Web3 Bug Bounties 2026](https://sherlock.xyz/post/best-web3-bug-bounties-in-2026-the-highest-paying-programs-on-every-platform): bounty platform landscape.

### Existing competing material
- [O'Reilly — Hands-On Smart Contract Development with Solidity and Ethereum](https://www.amazon.com/Hands-Contract-Development-Solidity-Ethereum/dp/1492045268) (Solorio, Kanna, Hoover, 2019).
- [O'Reilly — Mastering Ethereum 2e](https://github.com/ethereumbook/ethereumbook) (Antonopoulos, Wood, Parisi, Mazza, Pozzolini, 2025).
- [Damn Vulnerable DeFi](https://www.damnvulnerabledefi.xyz/) (OpenZeppelin, OSS).
- [OpenZeppelin damn-vulnerable-defi GitHub](https://github.com/OpenZeppelin/damn-vulnerable-defi).
- [Cyfrin Updraft Security & Auditing](https://updraft.cyfrin.io/courses/security) (Patrick Collins, free video course).
- [Cyfrin security-and-auditing-full-course-s23](https://github.com/Cyfrin/security-and-auditing-full-course-s23).
- [Awesome Web3 Security curated list](https://github.com/Anugrahsr/Awesome-web3-Security).
- [Cyfrin — How To Become A Smart Contract Auditor](https://www.cyfrin.io/blog/how-to-become-a-smart-contract-auditor).

### Toolchain
- [crytic/slither](https://github.com/crytic/slither) — static analyzer.
- [foundry-rs/foundry](https://github.com/foundry-rs/foundry/) — Foundry toolkit.
- [Halmos](https://github.com/a16z/halmos) — symbolic execution.
- [Echidna](https://github.com/crytic/echidna) — fuzzer.

### No Starch fit
- [`nostarch.com/about`](https://nostarch.com/about), [`nostarch.com/writeforus`](https://nostarch.com/writeforus).
- [Cracking Codes with Python (No Starch, 2018)](https://nostarch.com/crackingcodes) — the template this book follows.
- [Bitcoin for the Befuddled (No Starch, 2014)](https://nostarch.com/bitcoinforthebefuddled) — the only existing blockchain title at NSP.
- [Serious Cryptography 2e (No Starch, 2024)](https://nostarch.com/serious-cryptography-2nd-edition) — credibility bridge.

### Modern Ethereum context
- ERC-4337 active on mainnet since March 2023; EIP-7702 live since Pectra, 7 May 2025 ([Ethereum Foundation Pectra Mainnet](https://blog.ethereum.org/2025/04/23/pectra-mainnet)).

## Appendix B — One-page elevator pitch (for the editor's first read)

In 2025 alone, **$3.35 billion** was stolen from Web3 protocols across 630+ incidents. The average hack yielded $5.3 million. The five most exploited vulnerability classes — re-entrancy, integer overflow, access control, oracle manipulation, and flash loans — are the same five that have been draining DeFi for half a decade. The pattern doesn't change because the supply of engineers who understand it is too small.

*Cracking Smart Contracts* increases that supply.

Built explicitly for No Starch Press, the book follows the *Cracking Codes with Python* / *Hacking: The Art of Exploitation* template. The reader writes seven complete protocols — a token, a vault, a DEX, a lending market, a governance DAO, a bridge, and an account-abstraction wallet — and breaks each one with working Foundry exploits before hardening it. The auditor's toolbox (Slither, Echidna, Halmos, Certora) is taught against the reader's own code. The capstone is a fresh, never-before-seen audit.

The book ships with a versioned mono-repo, full Foundry test suites, a printable CTF attack-card deck, and a sealed model-audit branch. The audience is large (hundreds of thousands of Web3 engineers, the entire audit-firm hiring market), the gap is real (No Starch has *one* blockchain title from 2014), and the alternatives are aged 2019 textbooks, free CTFs, and video courses — none of which compete on the print-book shelf.

It is **P0**: 6 months from contract to print. Author archetype: senior auditor + content creator, single or paired. Companion executive-briefing format optional. Localisations into Hindi, Mandarin, Japanese, Spanish, and Portuguese inside 12 months of release.

The book defines the No Starch blockchain list and ships into a $3.35-billion-a-year market.

---

*End of proposal.*
