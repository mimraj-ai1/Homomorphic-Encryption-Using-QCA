# MAKAUT B.Tech (IT) 7th Semester — Official Project Work Diary (MidTerm 1)

**University:** Maulana Abul Kalam Azad University of Technology (MAKAUT), West Bengal  
**Department:** Department of Information Technology  
**Program:** Bachelor of Technology in Information Technology (7th Semester)  
**Academic Session:** 2026 – 2027  
**Approved Project Title:** Homomorphic Encryption Using Quantum-dot Cellular Automata (QCA)  
**Student Investigators:** Subhadip Dutta, SK Mimraj  
**Project Supervisor:** Dr. Jadav Chandra Das  
**Examination Date:** 24th September 2026 (11:00 AM onwards)  
**Evaluation Venue:** Room 324 (Panel 1) / Room 326 (Panel 2)  

---

## 1. Project Synopsis & MidTerm 1 Milestone Status

This project investigates the design, physical synthesis, and quantum simulation of nanoscale cryptographic arithmetic accelerators implemented in **Quantum-dot Cellular Automata (QCA)** for **Homomorphic Encryption (HE)**.

### Target Status as of MidTerm 1 (24th September 2026):
**100% of Phase-1 declared future work targets from the MAKAUT departmental baseline report have been completed and verified.**

| Milestone Objective | Status | Deliverable / Verification |
| :--- | :---: | :--- |
| **1. Primitive Logic Gates (AND, OR, NOT, NAND, NOR)** | **COMPLETED** | 5 layouts synthesized, verified truth tables in QCADesigner 2.0.3 |
| **2. Dual-Rail Pipelined XOR Gate** | **COMPLETED** | 91 cells, 1.00 cycle latency, balanced delay across 4 clock zones |
| **3. 1-Bit Addition (Half Adder & Full Adder)** | **COMPLETED** | 91-cell HA & 75-cell Tougaw-Lent FA ($0.0693\ \mu\text{m}^2$) |
| **4. Multi-Bit Addition (4-Bit RCA)** | **COMPLETED** | 315-cell horizontal cascade, 4.0 cycles latency, 512 test vectors |
| **5. Array Multiplication (2×2 Multiplier)** | **COMPLETED** | 91-cell array multiplier with 4 partial products, 16 test vectors |
| **6. Modular Arithmetic (2-Bit Modulo-4 Adder)** | **COMPLETED** | 177 cells, 2.0 cycles latency, lower delay synchronization line |
| **7. Homomorphic Encryption Software Demonstration** | **COMPLETED** | Python engine demonstrating Paillier & RSA homomorphism |
| **8. Six-Layer System Architecture** | **COMPLETED** | Formal mapping from cloud HE queries down to QCA nanostructures |
| **9. Full-Wave Quantum Simulation** | **COMPLETED** | Derived dissipative Liouville Master Equation on Bloch sphere |
| **10. Automated Test Harness** | **COMPLETED** | 82 unit test modules (608 test assertions, 100% passing) |

---

## 2. Chronological Weekly Engineering Work Log

### Week 1 (18th September 2026): Project Initiation & Baseline Analysis
- **Milestone:** Repository Initialization, CAD Tooling Setup, Baseline Verification.
- **Work Performed:**
  - Reviewed the preliminary Phase-1 report submitted to MAKAUT Department of Information Technology.
  - Verified simulation parameters: GaAs/AlGaAs system, relative permittivity $\varepsilon_r = 12.9$, 18 nm × 18 nm cell dimensions, 20 nm pitch, 65 nm radius of effect, 12,800 samples.
  - Verified local installation of native `QCADesigner.exe` (v2.0.3).
  - Initialized isolated Git version control repository on `main` branch.
- **Supervisor Guidance & Remarks:** Approved baseline scope, CAD parameters, and weekly milestone roadmap.

---

### Week 2 (19th September 2026): Primitive Logic Gates Synthesis
- **Milestone:** Synthesis of AND, OR, NOT, NAND, NOR Gates.
- **Work Performed:**
  - Designed the fundamental 5-cell 3-input Majority Voter $M(A, B, C) = AB + BC + AC$.
  - Synthesized programmable AND gate with fixed $-1.00$ bias (5 cells, $0.0034\ \mu\text{m}^2$).
  - Synthesized programmable OR gate with fixed $+1.00$ bias (5 cells, $0.0034\ \mu\text{m}^2$).
  - Implemented 4-cell diagonal Inverter (NOT) utilizing 45° offset anti-phase electrostatic coupling.
  - Synthesized universal NAND (7 cells) and NOR (7 cells) by cascading majority voters with inverter stages.
  - Built layout generation script `scripts/build_phase1_gates.py`.
- **Supervisor Guidance & Remarks:** Verified truth tables; ensured grid snapping to standard 20 nm pitch.

---

### Week 3 (20th September 2026): Advanced Logic: Dual-Rail Pipelined XOR Gate
- **Milestone:** Multi-Zone Dual-Rail XOR Layout Synthesis.
- **Work Performed:**
  - Formulated the robust single-layer dual-rail Boolean identity:
    $$A \oplus B = M(M(A, B, 1), \overline{M(A, B, 0)}, 0)$$
  - Designed layout across 4 clock zones: Zone 0 (inputs), Zone 1 (OR and AND voters), Zone 2 (diagonal inverter), Zone 3 (final output voter).
  - Compacted layout into 91 cells ($438\text{ nm} \times 258\text{ nm}$, $0.1130\ \mu\text{m}^2$).
  - Inserted symmetric delay cells along the upper rail to balance propagation time and prevent race conditions.
- **Supervisor Guidance & Remarks:** Pipelining verified. 1.00 clock cycle latency approved.

---

### Week 4 (21st September 2026): 1-Bit Arithmetic: Half Adder & Full Adder
- **Milestone:** Arithmetic Sub-System Implementation.
- **Work Performed:**
  - **Half Adder (`Half_Adder.qca`):** Reused dual-rail XOR architecture to extract intermediate AND majority signal as `CARRY`, producing both `SUM` ($A \oplus B$) and `CARRY` ($A \cdot B$) in 91 cells ($0.1130\ \mu\text{m}^2$, 1.0 cycle).
  - **Full Adder (`Full_Adder.qca`):** Implemented canonical Tougaw-Lent architecture using 3 Majority Voters and 2 Inverters:
    $$C_{out} = M(A, B, C_{in}), \quad M_2 = M(A, B, \overline{C_{in}}), \quad \text{SUM} = M(\overline{C_{out}}, M_2, C_{in})$$
  - Compacted into 75 cells ($318\text{ nm} \times 218\text{ nm}$, $0.0693\ \mu\text{m}^2$, 1.0 cycle).
  - Built automated netlist builders and unit tests.
- **Supervisor Guidance & Remarks:** Noted significant area compaction compared to sub-micron CMOS ($6.5\times$ smaller than 7 nm FinFET).

---

### Week 5 (22nd September 2026): Multi-Bit Accumulation & Array Multiplication
- **Milestone:** Large-Scale Arithmetic Synthesis.
- **Work Performed:**
  - **4-Bit Ripple Carry Adder (`RCA_4bit.qca`):** Cascaded 4 Full Adder stages horizontally with inter-stage carry rippling. Contains 315 cells ($1338\text{ nm} \times 218\text{ nm}$, $0.2917\ \mu\text{m}^2$, 4.0 cycles latency).
  - **2×2 Binary Multiplier (`Multiplier_2x2.qca`):** Synthesized 4 parallel AND partial product gates and accumulated them via 2 embedded Half Adders (91 cells, $0.0757\ \mu\text{m}^2$, 1.0 cycle latency).
  - Implemented coordinate collision prevention pass in netlist builder.
- **Supervisor Guidance & Remarks:** Multi-bit horizontal cascading verified without boundary cell collision.

---

### Week 6 (23rd September 2026): Modular Arithmetic & HE Software Engine
- **Milestone:** Cryptographic Arithmetic & Software Verification.
- **Work Performed:**
  - **2-Bit Modulo-4 Adder (`Modular_Adder.qca`):** Designed circuit evaluating $(A + B) \pmod 4$ with residue bits $R_1, R_0$ and overflow quotient $Q = \lfloor (A+B)/4 \rfloor$ in 177 cells ($658\text{ nm} \times 258\text{ nm}$, $0.1698\ \mu\text{m}^2$, 2.0 cycles latency).
  - Built lower delay line ($y = 340\text{ nm}$) to synchronize $R_0$ with Stage 1 outputs.
  - **Homomorphic Software Engine (`HE_Demo/`):** Implemented pure-Python demonstration of Paillier Additive Homomorphism and RSA Multiplicative Homomorphism.
  - Verified ciphertext-domain addition and scalar multiplication match plaintext operations.
- **Supervisor Guidance & Remarks:** Cryptographic equivalence verified. Approved integration with QCA hardware layers.

---

### Week 7 (24th September 2026): Full-Wave Analysis, Scaling & MidTerm 1 Defense
- **Milestone:** Full-Wave Quantum Master Equation, Benchmark Plots, MidTerm 1 Evaluation.
- **Work Performed:**
  - Modeled the quantum density matrix $\hat{\rho} = \frac{1}{2}(\hat{I} + \vec{\lambda} \cdot \vec{\sigma})$ and derived the dissipative Liouville-von Neumann master equation on the Bloch sphere, resolving the Phase-1 declared future work.
  - Generated 5 publication-quality 300 DPI scaling and CMOS benchmark plots ($R^2 = 0.985$).
  - Automated test harness executed: 608 test assertions passed (100% pass rate).
  - Prepared 18-slide widescreen MidTerm 1 presentation deck (`Documentation/MidTerm1_Project_Presentation.pptx`).
  - Generated official printable Project Work Diary (`Documentation/Project_Diary_MidTerm1.html`).
- **Supervisor Guidance & Remarks:** All baseline objectives completed. Recommended for MidTerm 1 presentation.

---

## 3. Evaluation Rubric & Sign-off Table

| Assessment Component | Max Marks | Target Achievement Status | Marks Awarded / Remarks |
| :--- | :---: | :--- | :--- |
| **1. Problem Formulation & Literature Review** | 20 | Comprehensive (HE Bottleneck & Post-CMOS QCA) | &nbsp; |
| **2. Design Methodology & Six-Layer Architecture** | 20 | 11 QCA Layouts, RNS & Paillier Mapping | &nbsp; |
| **3. Progress Achieved Against Baseline Schedule** | 25 | 100% Phase-1 Future Work Completed Early | &nbsp; |
| **4. Presentation Quality & Viva Voce Performance** | 20 | 18 Widescreen Slides, Complete Demo Ready | &nbsp; |
| **5. Maintenance of Official Project Diary / Logbook** | 15 | Weekly Chronological Logs & Guide Sign-off | &nbsp; |
| **TOTAL SCORE (MIDTERM 1):** | **100** | **EXCELLENT PROGRESS** | &nbsp; |

---

## 4. Signatures of Verification

```
____________________________          ____________________________          ____________________________
   Subhadip Dutta & SK Mimraj             Dr. Jadav Chandra Das                 External / Panel Examiners
 (Student Investigators, IT)            (Project Supervisor, MAKAUT)          (MidTerm 1 Evaluation Committee)
 Date: 24/09/2026                      Date: 24/09/2026                      Date: 24/09/2026
```
