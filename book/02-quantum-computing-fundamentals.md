# Chapter 2: Quantum Computing Fundamentals

## 2.1 Classical vs. Quantum Computation

To understand why quantum computers threaten cryptography, we must first understand how they differ from classical computers at a fundamental level.

### Classical Bits

A classical computer processes information using **bits** — binary digits that are definitively either 0 or 1. An n-bit register can be in exactly one of 2^n possible states at any given time. Classical algorithms process these states sequentially or with limited parallelism.

### Quantum Bits (Qubits)

A **qubit** is the quantum analog of a classical bit. Unlike a classical bit, a qubit can exist in a **superposition** of the |0⟩ and |1⟩ states simultaneously:

```
|ψ⟩ = α|0⟩ + β|1⟩
```

where α and β are complex numbers called **probability amplitudes**, satisfying |α|² + |β|² = 1. When measured, the qubit collapses to |0⟩ with probability |α|² or |1⟩ with probability |β|².

### The Power of Superposition

An n-qubit register can exist in a superposition of all 2^n possible states simultaneously:

```
|ψ⟩ = Σ αᵢ|i⟩  for i = 0 to 2^n - 1
```

This does NOT mean a quantum computer tries all possibilities at once (a common misconception). Rather, through careful manipulation of amplitudes via quantum gates, a quantum algorithm can arrange for correct answers to have high probability amplitudes while incorrect answers cancel out through **destructive interference**.

## 2.2 Key Quantum Phenomena

### Superposition

Superposition allows a qubit to be in multiple states simultaneously. This is not the same as classical probability (where the bit IS in one state but we don't know which). The qubit genuinely exists in both states, which enables interference effects.

### Entanglement

**Quantum entanglement** creates correlations between qubits that have no classical analog. When qubits are entangled, the state of one qubit is instantaneously correlated with the state of another, regardless of distance. For example, the Bell state:

```
|Φ+⟩ = (1/√2)(|00⟩ + |11⟩)
```

means that measuring either qubit as 0 guarantees the other will also be measured as 0, and similarly for 1. Entanglement is a resource that quantum algorithms exploit to create complex correlations across many qubits.

### Interference

**Quantum interference** is the mechanism by which quantum algorithms produce correct answers with high probability. Probability amplitudes are complex numbers and can add constructively (increasing probability) or destructively (decreasing probability). Well-designed quantum algorithms structure computations so that paths leading to correct answers interfere constructively while paths to incorrect answers interfere destructively.

## 2.3 Quantum Gates and Circuits

Quantum computation is performed by applying **quantum gates** — unitary transformations — to qubits. Common gates include:

### Single-Qubit Gates

**Hadamard Gate (H):** Creates superposition from a basis state.
```
H|0⟩ = (1/√2)(|0⟩ + |1⟩)
H|1⟩ = (1/√2)(|0⟩ - |1⟩)
```

**Pauli-X Gate:** Quantum NOT gate, flips |0⟩ ↔ |1⟩.

**Phase Gate (S, T):** Adds relative phase to the |1⟩ component.

### Multi-Qubit Gates

**CNOT (Controlled-NOT):** Flips the target qubit if the control qubit is |1⟩. Creates entanglement.

**Toffoli Gate:** A controlled-controlled-NOT gate. Universal for classical computation.

### Circuit Model

A quantum algorithm is expressed as a **quantum circuit** — a sequence of quantum gates applied to a register of qubits. The circuit model is the most common framework for quantum algorithms relevant to cryptography.

## 2.4 Quantum Computational Complexity

### BQP: Bounded-Error Quantum Polynomial Time

**BQP** is the class of decision problems solvable by a quantum computer in polynomial time with bounded error probability (at most 1/3 on any input). This is the quantum analog of BPP for classical randomized algorithms.

The relationships between complexity classes are:

```
P ⊆ BPP ⊆ BQP ⊆ PSPACE
```

It is widely believed (but not proven) that BQP is strictly larger than BPP — that is, quantum computers can efficiently solve problems that classical computers cannot. The problems most relevant to cryptography (factoring, discrete log) are believed to be in BQP but not in BPP.

### What Quantum Computers Cannot Do

Quantum computers are NOT omnipotent. Important limitations:

- They cannot solve NP-complete problems in polynomial time (unless NP ⊆ BQP, which is not believed)
- They provide at most quadratic speedup for unstructured search (Grover's algorithm)
- Not all exponential speedups are possible — the problem must have exploitable structure
- Quantum error correction imposes massive overhead

## 2.5 Quantum Error Correction

Real quantum hardware suffers from **decoherence** and **noise**. Qubits lose their quantum properties through interaction with the environment, and quantum gates have error rates far higher than classical transistors.

### The Threshold Theorem

The **threshold theorem** states that if the physical error rate per gate is below a certain threshold (approximately 10^-3 to 10^-4 for surface codes), then arbitrarily long quantum computations can be performed reliably using quantum error correction.

### Logical vs. Physical Qubits

A single **logical qubit** (a noise-free computational qubit) requires many **physical qubits** for error correction. Current estimates suggest:

- Surface codes: ~1,000-10,000 physical qubits per logical qubit
- Breaking RSA-2048: Requires approximately 4,000 logical qubits
- Therefore: Approximately 4-40 million physical qubits needed

### Current State of Hardware (2025-2026)

| Platform | Leading Qubits | Error Rates |
|----------|---------------|-------------|
| Superconducting (IBM, Google) | 1,000+ physical | ~10^-3 two-qubit gate |
| Trapped Ion (IonQ, Quantinuum) | 50-100 | ~10^-4 two-qubit gate |
| Neutral Atom (QuEra) | 256+ | ~10^-2 to 10^-3 |
| Photonic (Xanadu, PsiQuantum) | Varies | Architecture-dependent |

The gap between current hardware and cryptographically relevant quantum computers (CRQCs) remains significant but is narrowing. Most estimates place CRQCs at 10-20 years away, though breakthrough developments could accelerate this timeline.

## 2.6 The Quantum Advantage for Cryptanalysis

The relevance to cryptography comes from two specific quantum algorithms:

1. **Shor's Algorithm** — Provides exponential speedup for factoring and discrete logarithm problems, completely breaking RSA, Diffie-Hellman, and elliptic curve cryptography.

2. **Grover's Algorithm** — Provides quadratic speedup for unstructured search, effectively halving the security level of symmetric cryptography and hash functions.

These algorithms exploit specific mathematical structures. Not all cryptographic problems have known quantum speedups, which is precisely why post-quantum cryptography is possible — we can build new cryptosystems based on problems that remain hard even for quantum computers.

## 2.7 Quantum Computing Architectures

Several physical platforms are being developed for quantum computing:

### Superconducting Qubits
- **Companies:** IBM, Google, Rigetti
- **Pros:** Fast gate operations (~ns), scalable fabrication
- **Cons:** Require extreme cooling (~15 mK), limited connectivity

### Trapped Ions
- **Companies:** IonQ, Quantinuum, AQT
- **Pros:** High fidelity, all-to-all connectivity, long coherence times
- **Cons:** Slower gates (~μs), scaling challenges

### Neutral Atoms
- **Companies:** QuEra, Pasqal, Atom Computing
- **Pros:** Large qubit counts, native multi-qubit gates
- **Cons:** Relatively new, gate fidelities improving

### Photonic
- **Companies:** Xanadu, PsiQuantum
- **Pros:** Room temperature operation, networking natural
- **Cons:** Probabilistic gates, loss management

### Topological (Theoretical)
- **Companies:** Microsoft
- **Pros:** Inherent error protection if realized
- **Cons:** Still largely theoretical, Majorana fermions elusive

## 2.8 Timeline to Cryptographically Relevant Quantum Computers

Estimating when a CRQC will exist involves considering:

1. **Physical qubit count scaling** — Must reach millions of qubits
2. **Error rate reduction** — Must achieve below threshold for error correction
3. **Logical qubit overhead** — Determines physical-to-logical ratio
4. **Algorithm optimization** — Reduces resource requirements
5. **Engineering challenges** — Control systems, cooling, interconnects

### Expert Estimates

Various surveys and reports provide different timelines:

- **Conservative:** 20-30 years (significant engineering breakthroughs needed)
- **Moderate:** 10-20 years (steady progress on current trajectories)
- **Aggressive:** 5-15 years (assumes major breakthroughs)

The global quantum computing investment exceeds $30 billion annually across public and private sectors, with multiple nations treating quantum computing as a strategic priority.

## 2.9 Key Takeaways

- Quantum computers use qubits that can exist in superpositions of states
- Entanglement and interference enable quantum speedups for specific problems
- Shor's algorithm provides exponential speedup for problems underlying current cryptography
- Quantum error correction is required for useful computation but imposes large overhead
- Current estimates suggest CRQCs are 10-20 years away
- The uncertainty in timelines combined with long migration periods demands immediate action
- Post-quantum cryptography is designed to resist quantum attacks using classical hardware

---

*Next: [Chapter 3 — Why Current Cryptography Fails](./03-quantum-attacks.md)*
