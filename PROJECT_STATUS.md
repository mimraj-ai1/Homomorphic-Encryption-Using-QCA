# Project Status: Homomorphic Encryption Using Quantum-dot Cellular Automata (QCA)

## Project Overview

- **Project Title:** Homomorphic Encryption Using Quantum-dot Cellular Automata (QCA)
- **Academic Context:** B.Tech Final-Year Academic Project, Department of Information Technology, Maulana Abul Kalam Azad University of Technology (MAKAUT), West Bengal, India.
- **Supervision:** Dr. Jadav Chandra Das
- **Investigators:** Subhadip Dutta (Roll No: 10000224076, Reg No: 241000121037), SK Mimraj (Roll No: 10000224077, Reg No: 241000121038)
- **Academic Baseline:** Phase-1 preliminary report analyzed and documented in [Documentation/PROJECT_BASELINE.md](file:///c:/Users/sekhm/Desktop/HE-QCA-Project/Documentation/PROJECT_BASELINE.md).
- **Core Premise:** Homomorphic encryption permits computation directly on ciphertexts. QCA provides a post-CMOS, nanoscale, ultra-low-power physical hardware architecture for implementing the arithmetic (addition, multiplication, modular reduction) and binary logic required to evaluate encrypted data.
- **Fundamental Architectural Flow:**
  $$\text{Cryptographic Scheme (PHE/SHE/FHE)} \longrightarrow \text{Ciphertext Evaluation} \longrightarrow \text{Modular / Integer Arithmetic} \longrightarrow \text{Binary Arithmetic} \longrightarrow \text{Binary Logic} \longrightarrow \text{QCA Physical Implementation}$$
  *Notice:* QCA itself is NOT an encryption algorithm. QCA provides the hardware substrate for executing digital logic.

---

## Current Status

- **Current Phase:** Phase 1 — Basic QCA Logic Gates (AND, OR, NOT, NAND, NOR)
- **Phase Status:** Complete
- **Next Step:** Phase 2 — XOR Gate Implementation

---

## Phase Roadmap & Progress Tracker

| Phase | Description | Status | Verification Status |
| :--- | :--- | :--- | :--- |
| **Phase 0** | Project Initialization, Tool Discovery & Baseline Analysis | **COMPLETED** | Verified (File tree, tools detected, `PROJECT_BASELINE.md` generated) |
| **Phase 1** | Basic QCA Logic Gates (AND, OR, NOT, NAND, NOR) | **COMPLETED** | Layout files verified in QCADesigner 2.0.3; 15/15 unit tests passing; GUI waveforms PENDING MANUAL VERIFICATION |
| **Phase 2** | XOR Gate Implementation | PLANNED | Pending Phase 2 execution |
| **Phase 3** | Half Adder Implementation | PLANNED | Pending Phase 3 execution |
| **Phase 4** | Full Adder Implementation | PLANNED | Pending Phase 4 execution |
| **Phase 5** | 4-bit Ripple Carry Adder (RCA) | PLANNED | Pending Phase 5 execution |
| **Phase 6** | 2×2 Binary Multiplier | PLANNED | Pending Phase 6 execution |
| **Phase 7** | Modular Arithmetic ($(a + b) \pmod N$) | PLANNED | Pending Phase 7 execution |
| **Phase 8** | Homomorphic Encryption (HE) Python Demonstration | PLANNED | Pending Phase 8 execution |
| **Phase 9** | QCA / HE Technical Architecture Integration | PLANNED | Pending Phase 9 execution |
| **Phase 10** | Quantitative Performance Characterization (`performance.csv`) | IN PROGRESS | Phase 1 gates measured and logged to `Analysis/performance.csv` |
| **Phase 11** | Automated Testing Suite (`pytest`) | IN PROGRESS | `tests/test_gates.py` passing (15 tests) |
| **Phase 12** | Full-Wave Simulation Investigation | PLANNED | Pending Phase 12 execution |
| **Phase 13** | Comprehensive Academic Thesis Documentation | PLANNED | Pending Phase 13 execution |
| **Phase 14** | Presentation Content & Chronological Project Diary | PLANNED | Pending Phase 14 execution |

---

## Tooling & Environment Verification

| Tool / Dependency | Detected Path / Version | Operational Status | Notes |
| :--- | :--- | :--- | :--- |
| **QCADesigner** | `C:\Program Files (x86)\QCADesigner\bin\QCADesigner.exe` (v2.0.3) | Available | Native Win32 GUI tool. All 5 gate layouts verified to open cleanly. |
| **Python** | Python 3.10.11 (64-bit) | Available | System Python verified; executes circuit builders and test suites. |
| **Git** | git version 2.49.0.windows.1 | Available | Clean Git repository initialized at `HE-QCA-Project/` on branch `main`. |
| **NumPy** | Version 2.2.6 | Available | Operational for vector math and arithmetic testing. |
| **Matplotlib** | Version 3.10.8 | Available | Operational for performance graphing. |
| **pytest** | Version 8.3.3 | Available | Operational for test harness execution (15/15 passing). |

---

## Phase 1 Circuit Characterization Summary

| Circuit | Cell Count | Bounding Box Dimensions | Layout Area | Clock Zones | Clock Latency | Physical Verification Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **AND** | 5 | $58.0\text{ nm} \times 58.0\text{ nm}$ | $0.003364\ \mu\text{m}^2$ | 1 (Clock 0) | 0.25 cycles | PENDING MANUAL QCADESIGNER VERIFICATION |
| **OR** | 5 | $58.0\text{ nm} \times 58.0\text{ nm}$ | $0.003364\ \mu\text{m}^2$ | 1 (Clock 0) | 0.25 cycles | PENDING MANUAL QCADESIGNER VERIFICATION |
| **NOT** | 4 | $78.0\text{ nm} \times 38.0\text{ nm}$ | $0.002964\ \mu\text{m}^2$ | 1 (Clock 0) | 0.25 cycles | PENDING MANUAL QCADESIGNER VERIFICATION |
| **NAND** | 7 | $98.0\text{ nm} \times 58.0\text{ nm}$ | $0.005684\ \mu\text{m}^2$ | 1 (Clock 0) | 0.25 cycles | PENDING MANUAL QCADESIGNER VERIFICATION |
| **NOR** | 7 | $98.0\text{ nm} \times 58.0\text{ nm}$ | $0.005684\ \mu\text{m}^2$ | 1 (Clock 0) | 0.25 cycles | PENDING MANUAL QCADESIGNER VERIFICATION |

---

## Standardized QCADesigner Simulation Parameters

All QCA circuits are simulated under the standardized Bistable Approximation engine parameters specified in the MAKAUT academic baseline:
- **Simulation Engine:** Bistable Approximation (BA)
- **Number of Samples:** 12,800
- **Convergence Tolerance:** 0.001000
- **Radius of Effect:** 65.000000 nm
- **Relative Permittivity ($\epsilon_r$):** 12.900000 (GaAs/AlGaAs system)
- **Clock High:** $9.800000 \times 10^{-22}$ J
- **Clock Low:** $1.000000 \times 10^{-23}$ J
- **Clock Shift:** 0.000000
- **Clock Amplitude Factor:** 2.000000
- **Maximum Iterations per Sample:** 100
- **Physical Cell Dimensions:** 18 nm × 18 nm cell, 5 nm dot diameter, 20 nm center-to-center pitch

---

## Data Classification & Academic Integrity Protocol

1. **Literature Claims (Theoretical Foundations):** High-level claims (terahertz speed, sub-100 meV power dissipation, zero subthreshold leakage, $10^{12}\text{ devices/cm}^2$ density) are documented strictly as theoretical background from literature citations (Lent et al., Tougaw et al., Walus et al.) and will not be claimed as measurements obtained in this project.
2. **Experimental Measurements:** Only exact physical cell counts, computed layout areas ($\mu\text{m}^2$), clock zones, and clock latency derived directly from circuit netlists are reported in `performance.csv`.
3. **Simulation Status:** If a simulation has not been physically executed via QCADesigner GUI, it is strictly classified as `PENDING MANUAL QCADESIGNER VERIFICATION` with explicit step-by-step verification instructions. No fabricated waveforms or simulation values are permitted.
