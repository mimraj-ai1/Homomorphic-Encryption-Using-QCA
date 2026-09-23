# Homomorphic Encryption Using Quantum-dot Cellular Automata (QCA)

**Academic Project — Department of Information Technology**  
**Maulana Abul Kalam Azad University of Technology (MAKAUT), West Bengal**  
**Supervision:** Dr. Jadav Chandra Das  
**Investigators:** Subhadip Dutta (Roll: 10000224076), SK Mimraj (Roll: 10000224077)  

---

## 1. Project Overview

Homomorphic Encryption (HE) represents a transformative cryptographic paradigm that allows mathematical computations to be performed directly on encrypted ciphertexts without requiring preliminary decryption. However, evaluating homomorphic circuits introduces substantial computational and memory overhead.

Quantum-dot Cellular Automata (QCA) is an emerging post-CMOS nanotechnology that encodes binary information through electrostatic charge configurations of quantum-dot cells rather than conventional electric currents. QCA offers ultra-low power dissipation (limited to tunneling events), extremely high device density (~20 nm feature sizes), and theoretical terahertz switching speeds with zero static leakage current.

This project investigates QCA as an efficient hardware architecture for implementing the fundamental digital logic and arithmetic primitives required for homomorphic evaluations.

```
+-------------------------------------------------------------+
|                   Cryptographic Algorithm                   |
|          (PHE / SHE / Leveled FHE Mathematical Schema)       |
+-------------------------------------------------------------+
                              |
                              v
+-------------------------------------------------------------+
|                   Homomorphic Computation                   |
|                 (Ciphertext Domain Operations)              |
+-------------------------------------------------------------+
                              |
                              v
+-------------------------------------------------------------+
|                 Integer / Modular Arithmetic                |
|             (Modular Addition, Modular Multipliers)         |
+-------------------------------------------------------------+
                              |
                              v
+-------------------------------------------------------------+
|                      Binary Arithmetic                      |
|           (Ripple Carry Adders, Multiplier Arrays)          |
+-------------------------------------------------------------+
                              |
                              v
+-------------------------------------------------------------+
|                     Binary Logic Gates                      |
|               (AND, OR, NOT, NAND, NOR, XOR)                |
+-------------------------------------------------------------+
                              |
                              v
+-------------------------------------------------------------+
|                  QCA Hardware Implementation                |
|              (Majority Voters, 4-Phase Clocking)            |
+-------------------------------------------------------------+
```

---

## 2. Directory Structure

```
HE-QCA-Project/
├── QCA_Designs/                     # QCA circuit implementations (.qca, test vectors, notes)
│   ├── AND/                         # QCA Majority-based AND gate
│   ├── OR/                          # QCA Majority-based OR gate
│   ├── NOT/                         # QCA Inverter gate (rotated / displaced)
│   ├── NAND/                        # QCA NAND gate
│   ├── NOR/                         # QCA NOR gate
│   ├── XOR/                         # QCA XOR gate
│   ├── Half_Adder/                  # QCA Half Adder
│   ├── Full_Adder/                  # QCA Full Adder
│   ├── Ripple_Carry_Adder_4bit/     # QCA 4-bit Ripple Carry Adder
│   ├── Multiplier_2x2/              # QCA 2x2 Binary Multiplier
│   └── Modular_Arithmetic/          # Modular arithmetic design and test vectors
├── HE_Demo/                         # Software demonstration of Homomorphic Encryption
├── Analysis/                        # Quantitative circuit performance metrics and plots
│   └── plots/                       # Generated comparison plots
├── tests/                           # Automated Python test suite
├── Documentation/                   # Thesis chapters, presentation, and project diary
├── .gitignore                       # Git exclusions
├── PROJECT_STATUS.md                # Real-time progress and verification log
├── README.md                        # Master project documentation
└── requirements.txt                 # Python dependencies
```

---

## 3. Engineering Tools

- **CAD & Physical Simulation:** QCADesigner 2.0.3 (Bistable Approximation Engine)
- **Software Prototyping & Testing:** Python 3.10.11, NumPy 2.2.6, Matplotlib 3.10.8, pytest 8.3.3
- **Version Control:** Git
- **Operating Environment:** Windows 11 64-bit

---

## 4. Current Phase

The project has completed **Phase 0 (Project Initialization)**. No circuits have been implemented yet, pending authorization to commence Phase 1.
See [PROJECT_STATUS.md](file:///c:/Users/sekhm/Desktop/HE-QCA-Project/PROJECT_STATUS.md) for detailed phase tracking.
