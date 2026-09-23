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

- **Current Phase:** Phase 0 — Project Initialization & Baseline Analysis
- **Phase Status:** Complete
- **Next Step:** Phase 1 — Basic QCA Logic Gates (AND, OR, NOT, NAND, NOR)

---

## Phase Roadmap & Progress Tracker

| Phase | Description | Status | Verification Status |
| :--- | :--- | :--- | :--- |
| **Phase 0** | Project Initialization, Tool Discovery & Baseline Analysis | **COMPLETED** | Verified (File tree, tools detected, `PROJECT_BASELINE.md` generated) |
| **Phase 1** | Basic QCA Logic Gates (AND, OR, NOT, NAND, NOR) | PLANNED | Pending Phase 1 execution |
| **Phase 2** | XOR Gate Implementation | PLANNED | Pending Phase 2 execution |
| **Phase 3** | Half Adder Implementation | PLANNED | Pending Phase 3 execution |
| **Phase 4** | Full Adder Implementation | PLANNED | Pending Phase 4 execution |
| **Phase 5** | 4-bit Ripple Carry Adder (RCA) | PLANNED | Pending Phase 5 execution |
| **Phase 6** | 2×2 Binary Multiplier | PLANNED | Pending Phase 6 execution |
| **Phase 7** | Modular Arithmetic ($(a + b) \pmod N$) | PLANNED | Pending Phase 7 execution |
| **Phase 8** | Homomorphic Encryption (HE) Python Demonstration | PLANNED | Pending Phase 8 execution |
| **Phase 9** | QCA / HE Technical Architecture Integration | PLANNED | Pending Phase 9 execution |
| **Phase 10** | Quantitative Performance Characterization (`performance.csv`) | PLANNED | Pending Phase 10 execution |
| **Phase 11** | Automated Testing Suite (`pytest`) | PLANNED | Pending Phase 11 execution |
| **Phase 12** | Full-Wave Simulation Investigation | PLANNED | Pending Phase 12 execution |
| **Phase 13** | Comprehensive Academic Thesis Documentation | PLANNED | Pending Phase 13 execution |
| **Phase 14** | Presentation Content & Chronological Project Diary | PLANNED | Pending Phase 14 execution |

---

## Tooling & Environment Verification

| Tool / Dependency | Detected Path / Version | Operational Status | Notes |
| :--- | :--- | :--- | :--- |
| **QCADesigner** | `C:\Program Files (x86)\QCADesigner\bin\QCADesigner.exe` (v2.0.3) | Available | Native Win32 GUI tool. Cell format verified against standard library. |
| **Python** | Python 3.10.11 (64-bit) | Available | System Python verified for simulation analysis and cryptosystem demo. |
| **Git** | git version 2.49.0.windows.1 | Available | Clean Git repository initialized at `HE-QCA-Project/` on branch `main`. |
| **NumPy** | Version 2.2.6 | Available | Operational for vector math and arithmetic testing. |
| **Matplotlib** | Version 3.10.8 | Available | Operational for performance graphing. |
| **pytest** | Version 8.3.3 | Available | Operational for test harness execution. |

---

## Standardized QCADesigner Simulation Parameters

All QCA circuits will be simulated under the standardized Bistable Approximation engine parameters specified in the MAKAUT academic baseline:
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

To prevent conflation of theoretical literature claims with experimental project findings:
1. **Literature Claims (Theoretical Foundations):** High-level claims such as terahertz switching, ultra-low tunneling power (< 100 meV), zero subthreshold leakage, and nanoscale density are strictly cited as literature background (Lent et al., Tougaw et al., Walus et al.).
2. **Experimental Measurements:** Only exact physical cell counts, computed layout areas ($\mu\text{m}^2$), clock zones, and clock latency derived directly from circuit netlists are reported in `performance.csv`.
3. **Simulation Status:** If a simulation has not been physically executed via QCADesigner GUI, it is strictly classified as `PENDING MANUAL QCADESIGNER VERIFICATION` with explicit step-by-step verification instructions. No fabricated waveforms or simulation values are permitted.
