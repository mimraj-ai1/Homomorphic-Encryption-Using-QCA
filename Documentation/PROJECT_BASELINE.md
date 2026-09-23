# Project Baseline Document: Academic & Technical Foundation

**Project Title:** Homomorphic Encryption Using Quantum-dot Cellular Automata (QCA)  
**Academic Affiliation:** Department of Information Technology, Maulana Abul Kalam Azad University of Technology (MAKAUT), West Bengal, India  
**Project Year:** 2025 – 2026  
**Supervision:** Dr. Jadav Chandra Das, Professor, Department of Information Technology  
**Project Investigators:**  
- Subhadip Dutta  
- SK Mimraj  

---

## 1. Project Overview & Title

- **Formal Title:** Homomorphic Encryption Using Quantum-dot Cellular Automata (QCA)
- **Primary Premise:** Homomorphic Encryption (HE) permits mathematical computation directly over encrypted ciphertexts without intermediate decryption. Evaluating homomorphic evaluations incurs high computational complexity, requiring large-scale binary and modular arithmetic. Quantum-dot Cellular Automata (QCA) provides a post-CMOS nanotechnology hardware platform capable of ultra-dense, low-power digital switching to evaluate the underlying arithmetic and Boolean operations.
- **Architectural Boundary:**
  $$\text{Cryptographic Schema (PHE/SHE/FHE)} \longrightarrow \text{Ciphertext Operations} \longrightarrow \text{Modular / Integer Arithmetic} \longrightarrow \text{Binary Arithmetic (Adders/Multipliers)} \longrightarrow \text{QCA Logic Circuits}$$
  *Critical Clarification:* QCA itself is a physical/device-level nanotechnology for digital logic implementation, not an encryption algorithm. QCA provides the switching architecture for the hardware accelerators executing homomorphic arithmetic.

---

## 2. Project Objectives

1. Investigate the foundational theory of Homomorphic Encryption schemes (Partially, Somewhat, and Fully Homomorphic Encryption) and identify their circuit-level arithmetic primitives (addition, multiplication, modular reduction).
2. Model Quantum-dot Cellular Automata (QCA) as a transistorless, charge-interaction logic technology.
3. Establish a standard QCA logic cell library starting from fundamental gates (AND, OR, NOT, NAND, NOR) and progressive arithmetic circuits (XOR, Half Adder, Full Adder, 4-bit Ripple Carry Adder, 2×2 Multiplier).
4. Simulate and verify circuit operation using QCADesigner 2.0.3 with the Bistable Approximation engine.
5. Demonstrate modular arithmetic operations ($(a + b) \pmod N$) and develop a verified software demonstration of homomorphic encryption in Python.
6. Formulate a technical hardware/software architectural bridge linking ciphertext evaluations with QCA arithmetic structures.
7. Conduct quantitative performance characterization (cell count, circuit area, clock zones, latency) and validate functionality via automated testing.

---

## 3. Existing Theoretical Work (From Baseline Report)

The baseline project report documents the foundational concepts across two major disciplines:

### 3.1 Homomorphic Encryption Foundations
- **Definition:** Cryptographic transformations permitting evaluation functions $f$ such that $\text{Decrypt}(f(E(m_1), E(m_2), \dots)) = f(m_1, m_2, \dots)$.
- **PHE (Partially Homomorphic Encryption):** Supports a single operation (e.g., additive homomorphism in Paillier, multiplicative homomorphism in unpadded RSA).
- **SHE (Somewhat Homomorphic Encryption):** Supports both addition and multiplication, but limited to circuits of finite depth due to noise accumulation.
- **FHE (Fully Homomorphic Encryption):** Supports arbitrary addition and multiplication circuits of unbounded depth via bootstrapping (introduced by Craig Gentry in 2009; evolved into BGV, BFV, and CKKS leveled lattice-based schemes).
- **Arithmetic Primitives:** Encryption, evaluation, and decryption ultimately rely on polynomial or multi-precision integer addition and multiplication modulo a prime or integer modulus $N$.

### 3.2 Quantum-dot Cellular Automata (QCA) Foundations
- **Physical Cell Concept:** A nanostructure comprising four quantum dots located at the vertices of a square, containing two excess mobile electrons that tunnel between dots.
- **Coulomb Repulsion & Polarization:** Electrostatic repulsion forces electrons into diagonal arrangements, resulting in two energetically bistable polarization states:
  $$P = -1 \quad (\text{Logic } 0), \qquad P = +1 \quad (\text{Logic } 1)$$
- **Majority Voter (MV):** The fundamental logic primitive in QCA, constructed using a central cell surrounded by three input cells in a cross pattern:
  $$M(A, B, C) = AB + BC + AC$$
- **4-Phase Clocking:** Data flow and adiabatic switching are regulated by an external four-phase clock (Switch, Hold, Release, Relax) across four clock zones (Clock 0, 1, 2, 3), driving the inter-dot tunneling barriers.

---

## 4. Existing QCA Gate Work

The baseline report documents the design of initial elementary gates:
1. **OR Gate:** Implemented using a 3-input Majority Voter by fixing the third input cell to logic 1 (polarization $P = +1$):
   $$\text{OR}(A, B) = M(A, B, 1) = A \cdot B + B \cdot 1 + A \cdot 1 = A + B$$
2. **AND Gate:** Implemented using a 3-input Majority Voter by fixing the third input cell to logic 0 (polarization $P = -1$):
   $$\text{AND}(A, B) = M(A, B, 0) = A \cdot B + B \cdot 0 + A \cdot 0 = A \cdot B$$
3. **NOT Gate (Inverter):** Implemented using diagonal electrostatic anti-phase displacement / $45^\circ$-rotated cell configuration, inverting cell polarization.
4. **NAND Gate:** Implemented by cascading an AND Majority Voter with an inverting stage:
   $$\text{NAND}(A, B) = \overline{M(A, B, 0)} = \overline{A \cdot B}$$
5. **NOR Gate:** Implemented by cascading an OR Majority Voter with an inverting stage:
   $$\text{NOR}(A, B) = \overline{M(A, B, 1)} = \overline{A + B}$$

---

## 5. QCADesigner Configuration & Simulation Methodology

The project standardizes on **QCADesigner version 2.0.3** utilizing the **Bistable Approximation (BA)** simulation engine with the parameters specified in the academic report:

| Parameter | Baseline Value | Units / Notes |
| :--- | :--- | :--- |
| **Simulation Engine** | Bistable Approximation | Iterative two-state approximation |
| **Number of Samples** | 12,800 | Discrete time evaluation steps |
| **Convergence Tolerance** | 0.001000 | Iteration convergence threshold |
| **Radius of Effect** | 65.000000 nm | Maximum interaction distance for Coulomb calculations |
| **Relative Permittivity ($\epsilon_r$)** | 12.900000 | Material constant for GaAs/AlGaAs substrate |
| **Clock High** | $9.800000 \times 10^{-22}$ J | Tunneling barrier high state |
| **Clock Low** | $1.000000 \times 10^{-23}$ J | Tunneling barrier low state |
| **Clock Shift** | 0.000000 | Global clock phase offset |
| **Cell Dimensions** | 18 nm × 18 nm | Standard QCA square cell |
| **Dot Diameter** | 5.0 nm | Quantum dot diameter |
| **Cell Center Spacing** | 20.0 nm | Grid center-to-center pitch |

---

## 6. Distinction Between Literature Claims and Measured Results

To preserve academic integrity and avoid conflating theoretical background with experimental findings, all technical data is categorized strictly into three distinct tiers:

```
[Category A: Literature Claims]
   - Terahertz theoretical switching limits (Lent et al.)
   - Ultra-low tunneling dissipation (< 100 meV per switch)
   - Zero static subthreshold leakage current (absence of FET channels)
   - 10^12 devices/cm^2 physical density limits

[Category B: Project Experimental Measurements]
   - Exact layout cell counts counted directly from .qca netlists
   - Bounding-box physical dimensions (nm x nm) and area (um^2) calculated from layout coordinates
   - Number of clock zones utilized (Clock 0, 1, 2, 3)
   - Clock latency in clock cycles (number of zones / 4)
   - Truth table validation under Bistable Approximation simulation

[Category C: Results Requiring Simulation / Manual Verification]
   - Analog output polarization levels (|P| >= 0.8) under 12,800 samples in QCADesigner GUI
   - Full-Wave engine dynamic quantum dissipation and thermal stability checks
```

*Rule:* Literature claims (Category A) must never be presented as experimental measurements derived in this project.

---

## 7. Existing Reported Results (Status in Baseline Report)

In the baseline report:
- Functional simulation waveform screenshots are included for OR, AND, NOT, NAND, and NOR gates.
- Waveforms confirm correct output transitions across the four binary combinations ($00, 01, 10, 11$) under Bistable Approximation.
- The report notes that these gates validate the foundational cell library, but leaves higher-level circuits unbuilt.

---

## 8. Limitations of the Baseline Report

1. **Gate-Level Only:** The baseline work stopped at basic 1-bit and 2-input logic gates (OR, AND, NOT, NAND, NOR). It did not construct XOR, arithmetic adders, or multipliers.
2. **Absence of Modular Arithmetic Hardware:** No modular reduction or modular addition circuit designs were specified or simulated.
3. **Absence of Executable Cryptographic Software:** Homomorphic Encryption was discussed purely theoretically; no working Python implementation (PHE/SHE) was provided to perform encryption, homomorphic operations, and decryption.
4. **No Quantitative Layout Metrics:** Numerical cell counts, physical surface areas ($\mu\text{m}^2$), clock zone assignments, and pipelined clock cycle latencies were not tabulated in the baseline report.
5. **Lack of Automated Testing Suite:** No automated test harnesses or Python-based verification existed to validate truth tables across complex circuits.
6. **No Headless Simulation Pipeline:** All verifications relied solely on manual GUI execution in QCADesigner.

---

## 9. Planned Future Work (From Baseline Report)

The baseline report explicitly identified the following roadmap for completion:
- Design of QCA XOR gate and Half Adder circuit.
- Implementation of a QCA Full Adder combining XOR and Majority logic.
- Construction of a QCA-based Multiplier circuit essential for multiplicative homomorphism.
- Investigation of modular arithmetic units (modular adders and multipliers over integer fields).
- Exploration of the Full-Wave simulation engine in QCADesigner for quantum-mechanical validation.
- Comparative analysis of QCA designs against equivalent CMOS implementations in cell count, area, power, and delay.

---

## 10. Technical Scope to Implement in Current Execution

To extend the baseline report into a complete B.Tech final-year academic project, the project must implement:

1. **Phase 1: Basic QCA Logic Gates** — Generate reproducible, fully compatible `.qca` layout files for AND, OR, NOT, NAND, and NOR, complete with layout dimensions and simulation guides.
2. **Phase 2: XOR Gate** — Design and construct a verified QCA XOR gate ($A \oplus B = (A+B)\overline{AB}$).
3. **Phase 3: Half Adder** — Construct $\text{SUM} = A \oplus B$ and $\text{CARRY} = A \cdot B$ with synchronized clock zones.
4. **Phase 4: Full Adder** — Construct 3-input addition ($\text{SUM}, C_{out}$) using Majority and XOR primitives.
5. **Phase 5: 4-bit Ripple Carry Adder (RCA)** — Cascade 4 Full Adders ($\text{FA}_0 \to \text{FA}_1 \to \text{FA}_2 \to \text{FA}_3$) with verified binary addition test vectors.
6. **Phase 6: 2×2 Binary Multiplier** — Implement 4 partial products ($A_i B_j$) combined through Half/Full Adder stages across all 16 input combinations.
7. **Phase 7: Modular Arithmetic Architecture** — Implement $(a + b) \pmod N$ for $N = 4$ and establish the connection to finite field cryptographic arithmetic.
8. **Phase 8: Homomorphic Encryption Software Demonstration** — Implement a complete, mathematically verified Python cryptosystem (PHE Paillier or RSA) demonstrating KeyGen $\to$ Encrypt $\to$ Homomorphic Operation $\to$ Decrypt $\to$ Verification.
9. **Phase 9: QCA / HE Technical Architecture Integration** — Document the end-to-end hardware/software bridge with explicit boundary distinctions.
10. **Phase 10: Performance Analysis** — Construct `Analysis/performance.csv` tabulating measured cell counts, physical areas, clock zones, latency, and correctness.
11. **Phase 11: Automated Testing Suite** — Write modular pytest suites (`test_gates.py`, `test_adders.py`, `test_multiplier.py`, `test_he.py`).
12. **Phase 12: Full-Wave Simulation Investigation** — Document the quantum-mechanical Hamiltonians, coherence vectors, and execution considerations of QCADesigner's Full-Wave engine.
13. **Phase 13: Final Thesis Documentation** — Complete all 28 academic chapters.
14. **Phase 14: Presentation Slides & Project Diary** — Prepare slide content and chronological engineering logs.
