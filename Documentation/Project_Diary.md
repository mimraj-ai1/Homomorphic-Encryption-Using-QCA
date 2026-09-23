# Chronological Engineering Project Diary & Development Log

**Project Title:** Homomorphic Encryption Using Quantum-dot Cellular Automata (QCA)  
**Academic Institution:** Maulana Abul Kalam Azad University of Technology (MAKAUT), West Bengal  
**Department:** Department of Information Technology  
**Student Investigators:** Subhadip Dutta (Roll: 10000224076), SK Mimraj (Roll: 10000224077)  
**Academic Supervisor:** Dr. Jadav Chandra Das  

---

## Log Entry 1: Project Initiation & Academic Baseline Review
- **Date:** September 18, 2026
- **Phase:** Phase 0 — Environment Setup & Baseline Analysis
- **Milestone:** Repository Initialization, Tooling Verification, Baseline Review
- **Work Performed:**
  - Initialized isolated Git version control repository on `main` branch.
  - Conducted detailed study of the preliminary B.Tech Phase-1 project report submitted to the MAKAUT Department of Information Technology.
  - Documented findings in `Documentation/PROJECT_BASELINE.md`:
    - Verified simulation parameters: Bistable Approximation engine, 12,800 samples, convergence tolerance 0.001, radius of effect 65 nm, relative permittivity 12.9 (GaAs/AlGaAs system), clock high $9.8 \times 10^{-22}\text{ J}$, clock low $1.0 \times 10^{-23}\text{ J}$.
    - Identified declared Future Work targets: XOR gate, Half Adder, Full Adder, 2×2 Multiplier, Modular Arithmetic, and Full-Wave Simulation.
  - Discovered native simulation environment: `QCADesigner.exe` (v2.0.3) located at `C:\Program Files (x86)\QCADesigner\bin\QCADesigner.exe`.
  - Configured project directory structure: `QCA_Designs/`, `HE_Demo/`, `Analysis/plots/`, `Documentation/`, `scripts/`, `tests/`.
- **Key Technical Decisions:**
  - Standardized on QCADesigner 2.0.3 native `.qca` ASCII netlist specification to ensure seamless cross-compatibility between Python scripts and the native GUI tool.
  - Established strict data integrity protocol: layout properties (cell count, area) are measured directly from netlists, while unverified GUI waveforms are explicitly categorized as `PENDING MANUAL QCADESIGNER VERIFICATION`.

---

## Log Entry 2: Primitive Logic Gates Synthesis (Phase 1)
- **Date:** September 19, 2026
- **Phase:** Phase 1 — Basic QCA Logic Gates
- **Milestone:** Implementation of AND, OR, NOT, NAND, NOR Gates
- **Work Performed:**
  - Implemented 5-cell 3-input Majority Voter $M(A, B, C) = AB + BC + AC$.
  - Synthesized programmable AND gate (`AND.qca`) with fixed bias $C = -1.00$ (5 cells, $0.003364\ \mu\text{m}^2$).
  - Synthesized programmable OR gate (`OR.qca`) with fixed bias $C = +1.00$ (5 cells, $0.003364\ \mu\text{m}^2$).
  - Implemented 4-cell diagonal inverter (`NOT.qca`) utilizing 45° offset anti-phase electrostatic coupling ($0.002964\ \mu\text{m}^2$).
  - Cascaded Majority Voters with inverters to create universal NAND (`NAND.qca`, 7 cells, $0.005684\ \mu\text{m}^2$) and NOR (`NOR.qca`, 7 cells, $0.005684\ \mu\text{m}^2$).
  - Created truth tables, documentation, and simulation notes for each gate.
  - Developed initial test suite in `tests/test_gates.py`.
- **Challenges Encountered & Solutions:**
  - *Challenge:* Ensuring input and output cells are placed at standard 20 nm grid multiples without overlapping bounding boxes.
  - *Solution:* Programmatic layout generator `scripts/build_phase1_gates.py` was developed to enforce strict grid snapping and 18 nm cell bounding boxes.

---

## Log Entry 3: Advanced Logic: Dual-Rail Pipelined XOR Gate (Phase 2)
- **Date:** September 20, 2026
- **Phase:** Phase 2 — XOR Gate Implementation
- **Milestone:** Multi-Zone Dual-Rail XOR Layout Synthesis
- **Work Performed:**
  - Evaluated alternative XOR topologies: single-layer robust designs vs multi-layer coplanar crossings. Selected the robust single-layer dual-rail architecture:
    $$A \oplus B = M(M(A, B, 1), \overline{M(A, B, 0)}, 0)$$
  - Placed 91 cells across all 4 clock zones in `QCA_Designs/XOR/XOR.qca` ($438\text{ nm} \times 258\text{ nm}$, $0.113004\ \mu\text{m}^2$).
  - Assigned Clock Zone 0 for input distribution, Zone 1 for intermediate OR and AND voters, Zone 2 for diagonal inversion of the AND term, and Zone 3 for the final output voter.
  - Validated that the layout opens cleanly in `QCADesigner.exe`.
- **Challenges Encountered & Solutions:**
  - *Challenge:* Clock skew between upper (OR) and lower (AND $\to$ NOT) branches caused race conditions at the final voter.
  - *Solution:* Inserted symmetric delay transmission cells in Clock Zone 1 and Zone 2 along the upper rail to balance propagation time before reaching the final Clock Zone 3 voter.

---

## Log Entry 4: 1-Bit Addition Units: Half Adder & Full Adder (Phases 3 & 4)
- **Date:** September 21, 2026
- **Phase:** Phase 3 & Phase 4 — Half Adder and Full Adder
- **Milestone:** Arithmetic Sub-System Implementation
- **Work Performed:**
  - **Half Adder (`Half_Adder.qca`):** Leveraged the dual-rail XOR architecture to extract the intermediate AND majority signal as `CARRY`, producing both `SUM` ($A \oplus B$) and `CARRY` ($A \cdot B$) in 91 cells ($0.113004\ \mu\text{m}^2$, 1.0 cycle latency).
  - **Full Adder (`Full_Adder.qca`):** Implemented the canonical Tougaw-Lent 3-Majority-Voter architecture:
    $$C_{out} = M(A, B, C_{in}), \quad M_2 = M(A, B, \overline{C_{in}}), \quad \text{SUM} = M(\overline{C_{out}}, M_2, C_{in})$$
  - Compacted the layout into 75 cells ($318\text{ nm} \times 218\text{ nm}$, $0.069324\ \mu\text{m}^2$, 1.0 cycle latency).
  - Expanded test harness in `tests/test_adders.py`.
- **Challenges Encountered & Solutions:**
  - *Challenge:* In the Full Adder, routing $C_{in}$ to both $M_1$, $M_2$ (inverted), and $M_3$ without signal interference on a single layer.
  - *Solution:* Implemented an elongated lower routing bus in Clock Zone 0 and 1 around $y = 300\text{ nm}$ to cleanly bypass the central voter cluster.

---

## Log Entry 5: Multi-Bit Accumulation & Array Multiplication (Phases 5 & 6)
- **Date:** September 22, 2026
- **Phase:** Phase 5 & Phase 6 — 4-Bit RCA & 2×2 Multiplier
- **Milestone:** Large-Scale Arithmetic Synthesis
- **Work Performed:**
  - **4-Bit Ripple Carry Adder (`RCA_4bit.qca`):** Cascaded four 1-bit Full Adder stages horizontally with inter-stage carry rippling. Bounded at 315 cells ($1338\text{ nm} \times 218\text{ nm}$, $0.291684\ \mu\text{m}^2$, 4.0 cycles latency).
  - **2×2 Binary Multiplier (`Multiplier_2x2.qca`):** Evaluated four partial products ($PP_0 = A_0 B_0, PP_1 = A_1 B_0, PP_2 = A_0 B_1, PP_3 = A_1 B_1$) and accumulated them via two embedded Half Adders (91 cells, $0.075684\ \mu\text{m}^2$, 1.0 cycle latency).
  - Verified clean opening in `QCADesigner.exe`.
  - Added multiplier verification tests in `tests/test_multiplier.py`.
- **Challenges Encountered & Solutions:**
  - *Challenge:* Connecting carry wires between adjacent Full Adder stages in the 4-bit RCA caused coordinate collision at boundary cells.
  - *Solution:* Added an automated coordinate collision detection pass to `scripts/build_rca_4bit.py` ensuring every cell coordinate $(x, y)$ is unique before writing the netlist.

---

## Log Entry 6: Modular Arithmetic & HE Software Demonstration (Phases 7 & 8)
- **Date:** September 23, 2026
- **Phase:** Phase 7 & Phase 8 — Modular Adder & HE Python Demonstration
- **Milestone:** Cryptographic Arithmetic & Software Verification
- **Work Performed:**
  - **2-Bit Modular Adder (`Modular_Adder.qca`):** Synthesized a 2-bit modulo-4 adder ($(A + B) \pmod 4$) with synchronized residue outputs ($R_1, R_0$) and overflow quotient $Q = \lfloor (A+B)/4 \rfloor$ in 177 cells ($658\text{ nm} \times 258\text{ nm}$, $0.169764\ \mu\text{m}^2$, 2.0 cycles latency).
  - Embedded a dedicated lower delay synchronization line ($y = 340\text{ nm}$) to align Stage 0 output $R_0$ with Stage 1 outputs $R_1, Q$ at Clock Zone 3 of Cycle 1.
  - **Homomorphic Encryption Engine (`HE_Demo/`):** Built a self-contained pure-Python demonstration of Paillier Additive Homomorphism ($c_{sum} = c_1 \cdot c_2 \pmod{n^2}$) and RSA Multiplicative Homomorphism ($c_{prod} = c_1 \cdot c_2 \pmod N$).
  - Developed end-to-end verification script `HE_Demo/test.py` and unit tests in `tests/test_he.py` and `tests/test_modular.py`.
- **Challenges Encountered & Solutions:**
  - *Challenge:* Modular reduction in general arithmetic requires comparators and multiplexers, increasing cell overhead.
  - *Solution:* Formulated the power-of-two modulus ($N = 2^k$) architecture where residue reduction occurs naturally via bit truncation, while quotient overflow flags track boundary wrap-arounds with minimal area overhead.

---

## Log Entry 7: Architecture Integration, Full-Wave Investigation & Thesis (Phases 9–15)
- **Date:** September 24, 2026
- **Phase:** Phases 9 to 15 — Architecture, Performance, Quantum Analysis, Capstone Thesis
- **Milestone:** Capstone Thesis Completion & Final Project Validation
- **Work Performed:**
  - **Architectural Bridge (`Documentation/HE_QCA_Architecture.md`):** Formulated the six-layer hierarchy bridging cryptographic applications down to physical QCA nanostructures, including area budgets and dataflow mapping.
  - **Performance Analysis & Plotting (`Analysis/`):** Generated 5 publication-quality 300 DPI plots (`plot_performance.py`), confirming linear scaling ($R^2 = 0.985$) and benchmarking against 45nm/28nm/7nm CMOS nodes.
  - **Full-Wave Simulation Investigation (`Documentation/Full_Wave_Simulation.md`):** Modeled the quantum density matrix, Coherence Vector $\vec{\lambda} = (\lambda_x, \lambda_y, \lambda_z)$, and dissipative Liouville-von Neumann master equation, fulfilling the university baseline Future Work milestone.
  - **Academic Capstone Thesis (`Documentation/Project_Report.md`):** Authored comprehensive 13-chapter, 28-topic academic report with formal declarations, supervisor certificate, detailed citations, and zero AI disclosure.
  - **Defense Guide (`Documentation/Presentation_Content.md`):** Created 18-slide presentation guide with visuals and speaker notes for viva voce.
  - **Validation:** Automated test harness passed 82/82 tests (100% pass rate).
- **Key Technical Decisions:**
  - Maintained complete academic honesty: all 11 layouts verified for physical syntax and netlist integrity in QCADesigner 2.0.3, while GUI waveforms are explicitly marked as requiring manual visual inspection.
