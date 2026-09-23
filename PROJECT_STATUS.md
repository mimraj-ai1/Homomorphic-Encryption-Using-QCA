# Project Status: Homomorphic Encryption Using Quantum-dot Cellular Automata (QCA)

## Project Overview

- **Project Title:** Homomorphic Encryption Using Quantum-dot Cellular Automata (QCA)
- **Academic Context:** B.Tech Final-Year Academic Project, Department of Information Technology, Maulana Abul Kalam Azad University of Technology (MAKAUT), West Bengal, India.
- **Supervision:** Dr. Jadav Chandra Das
- **Investigators:** Subhadip Dutta (Roll No: 10000224076), SK Mimraj (Roll No: 10000224077)
- **Project Objective:** Investigate Quantum-dot Cellular Automata (QCA) as an ultra-low-power, nanoscale hardware substrate for fundamental digital logic and arithmetic operations (addition, multiplication, modular reduction) underlying homomorphic computation, complemented by an educational software demonstration of homomorphic encryption principles and comprehensive performance analysis.
- **Architectural Separation:**
  $$\text{Cryptographic Algorithm} \longrightarrow \text{Homomorphic Computation} \longrightarrow \text{Modular / Integer Arithmetic} \longrightarrow \text{Binary Arithmetic} \longrightarrow \text{Binary Logic} \longrightarrow \text{QCA Hardware Implementation}$$
  *Note:* QCA is a nanoscale digital logic technology, not an encryption algorithm. QCA provides the hardware switching mechanism for computing on binary and modular values required during homomorphic evaluations.

---

## Current Status

- **Current Phase:** Phase 0 — Project Initialization
- **Phase Status:** Complete
- **Next Phase:** Phase 1 — Basic QCA Logic Gates (AND, OR, NOT, NAND, NOR)

---

## Planned Phases & Progress Tracker

| Phase | Description | Status | Verification Status |
| :--- | :--- | :--- | :--- |
| **Phase 0** | Project Initialization & Environment Setup | **COMPLETED** | Verified (File tree, tool detection, git repo initialized) |
| **Phase 1** | Basic QCA Logic Gates (AND, OR, NOT, NAND, NOR) | PLANNED | Pending Phase 1 execution |
| **Phase 2** | XOR Gate Implementation | PLANNED | Pending Phase 2 execution |
| **Phase 3** | Half Adder Implementation | PLANNED | Pending Phase 3 execution |
| **Phase 4** | Full Adder Implementation | PLANNED | Pending Phase 4 execution |
| **Phase 5** | 4-bit Ripple Carry Adder (RCA) | PLANNED | Pending Phase 5 execution |
| **Phase 6** | 2×2 Binary Multiplier | PLANNED | Pending Phase 6 execution |
| **Phase 7** | Modular Arithmetic Integration ($(a + b) \pmod N$) | PLANNED | Pending Phase 7 execution |
| **Phase 8** | Homomorphic Encryption (HE) Demonstration | PLANNED | Pending Phase 8 execution |
| **Phase 9** | QCA / HE Technical Architecture Documentation | PLANNED | Pending Phase 9 execution |
| **Phase 10** | Circuit Performance Data Collection | PLANNED | Pending Phase 10 execution |
| **Phase 11** | Data Analysis & Metric Visualization (Matplotlib) | PLANNED | Pending Phase 11 execution |
| **Phase 12** | Automated Software Test Suite (pytest) | PLANNED | Pending Phase 12 execution |
| **Phase 13** | Academic Documentation & Final Thesis Report | PLANNED | Pending Phase 13 execution |
| **Phase 14** | Project Presentation Slides Preparation | PLANNED | Pending Phase 14 execution |
| **Phase 15** | Project Engineering Diary | PLANNED | Pending Phase 15 execution |
| **Phase 16** | Comprehensive Master README.md | PLANNED | Pending Phase 16 execution |

---

## Tooling & Environment Verification

| Tool / Dependency | Detected Path / Version | Operational Status | Notes |
| :--- | :--- | :--- | :--- |
| **QCADesigner** | `C:\Program Files (x86)\QCADesigner\bin\QCADesigner.exe` (v2.0.3) | Available | Standard Win32 GUI tool. Bistable Approximation engine default parameters verified via internal cell library. |
| **Python** | Python 3.10.11 | Available | System Python installed and verified. |
| **Git** | git version 2.49.0.windows.1 | Available | Clean Git repository initialized in `HE-QCA-Project/`. |
| **NumPy** | Version 2.2.6 | Available | Operational for vector and arithmetic computations. |
| **Matplotlib** | Version 3.10.8 | Available | Operational for performance graphing. |
| **pytest** | Version 8.3.3 | Available | Operational for automated test harness execution. |

---

## Standard Simulation Parameters (QCADesigner 2.0.3)

All QCA circuits in subsequent phases will adhere strictly to the standardized Bistable Approximation simulation parameters:
- **Simulation Engine:** Bistable Approximation
- **Number of Samples:** 12,800
- **Convergence Tolerance:** 0.001000
- **Radius of Effect:** 65.000000 nm
- **Relative Permittivity:** 12.900000 (GaAs/AlGaAs material system)
- **Clock High:** 9.800000e-22 J
- **Clock Low:** 1.000000e-23 J
- **Clock Shift:** 0.000000
- **Clock Amplitude Factor:** 2.000000
- **Maximum Iterations per Sample:** 100
- **Layer Substrate Dimensions:** Cell size = 18 nm × 18 nm, Dot diameter = 5 nm, Cell spacing = 20 nm center-to-center

---

## Known Limitations & Verification Protocol

1. **QCADesigner Automation Constraint:** QCADesigner 2.0.3 is a native Win32/GTK+ graphical tool without a headless batch simulation CLI. All `.qca` circuit layout files will be constructed with mathematically exact coordinates and cell layer specifications matching the QCADesigner format specification. Step-by-step manual GUI verification instructions and expected waveform behavior will be documented for every circuit.
2. **Measurement Integrity:** No physical cell counts, clock phases, or latencies will be fabricated. Where circuits require visual or manual verification via QCADesigner GUI, they will be explicitly designated as `PENDING MANUAL QCADESIGNER VERIFICATION` until confirmed.
3. **Cryptographic Scope Distinction:** QCA provides the physical device-level implementation of Boolean logic and arithmetic units; the mathematical ciphertext transformations occur at the algorithmic layer demonstrated in Python.
