# MAKAUT B.Tech (IT) 7th Semester — MidTerm 1 Viva Voce & Presentation Guide

**Project Title:** Homomorphic Encryption Using Quantum-dot Cellular Automata (QCA)  
**Institution:** Maulana Abul Kalam Azad University of Technology (MAKAUT), West Bengal  
**Department:** Department of Information Technology  
**Student Presenters:** Subhadip Dutta, SK Mimraj  
**Project Supervisor:** Dr. Jadav Chandra Das  
**Examination Date:** 24th September 2026 (11:00 AM onwards)  
**Venues:** Panel 1 (Group 1 to 8): Room 324 | Panel 2 (Group 9 to rest): Room 326  

---

## 1. The 90-Second Opening Pitch (Say this on Slide 1 & 2)

> "Respected panel members and faculty, good morning. Our B.Tech final-year project is titled **'Homomorphic Encryption Using Quantum-dot Cellular Automata (QCA)'**, carried out under the guidance of **Dr. Jadav Chandra Das**.
>
> In today's cloud datacenters, **Homomorphic Encryption (HE)** is the gold standard for privacy-preserving computation because it allows computing directly over encrypted data without decrypting it. However, ciphertext expansion makes encrypted arithmetic 100 to 1000 times larger, hitting the **CMOS thermodynamic wall** below 3 nm due to massive static leakage current and thermal throttling.
>
> To solve this, we investigate **Quantum-dot Cellular Automata (QCA)**—an emerging post-CMOS nanotechnology. In QCA, digital logic is processed by **electrostatic charge steering** of electron pairs inside 18 nm quantum cells, **eliminating electrical currents and static power dissipation**.
>
> For this MidTerm 1 review, we have **100% completed all Phase-1 baseline objectives**: we designed, clocked, and verified **11 QCA circuit layouts** in QCADesigner 2.0.3, built a functioning **Python Homomorphic Encryption demo**, established a **Six-Layer System Architecture**, and derived the **Full-Wave Quantum Master Equation**. We are pleased to present our progress and our project diaries today."

---

## 2. Top 10 Anticipated Viva Questions & Direct Answers

### Q1: Is QCA an encryption algorithm, or is it a hardware technology?
**Model Answer:**  
> "QCA is **NOT an encryption algorithm**; it is a **physical hardware technology** (a post-CMOS nanotechnology). The encryption scheme we use is Paillier or Ring-LWE (which are mathematical cryptographic algorithms). Our contribution is designing dedicated **nanoscale QCA arithmetic accelerators** (such as multipliers, ripple carry adders, and modular adders) that physically execute the intensive modular ciphertext arithmetic of Homomorphic Encryption with sub-femtojoule energy dissipation."

---

### Q2: Why did you choose QCA instead of conventional FPGAs, GPUs, or standard CMOS ASICs?
**Model Answer:**  
> "Conventional CMOS in sub-3 nm nodes suffers from **Boltzmann's thermodynamic limit** ($S \ge 60\text{ mV/decade}$), leading to high static leakage current ($I_{leak}$) and severe thermal dissipation when computing multi-thousand-bit modular arithmetic.  
> In contrast, QCA has **zero current flow** because information is encoded purely by the electrostatic polarization of electron pairs. Our benchmarks show that a QCA Full Adder achieves an area footprint **6.5 times smaller than 7 nm FinFET** and reduces static power dissipation by **more than 10,000 times**."

---

### Q3: Explain why QCA needs 4 clock phases. What happens if you use only 1 clock phase?
**Model Answer:**  
> "QCA requires a **4-phase adiabatic clock**: **Switch (0°), Hold (90°), Release (180°), and Relax (270°)**.  
> 1. In **Switch**, inter-dot barriers rise and the cell locks into polarization dictated by its inputs.  
> 2. In **Hold**, barriers stay high and the cell acts as a stable input for the next zone.  
> 3. In **Release & Relax**, barriers lower so the cell unpolarizes, clearing past data.  
>  
> If we only used 1 clock phase, information would propagate bidirectionally, causing **back-reflections, race conditions, and signal decay**. The 4 phases enforce **strict unidirectional pipelining** without needing physical diodes or transistors."

---

### Q4: What is the fundamental building block of QCA logic? How do you get AND and OR gates?
**Model Answer:**  
> "Unlike CMOS where NAND is the primitive, the fundamental building block of QCA is the **3-input Majority Voter (MV)**:  
> $$M(A, B, C) = AB + BC + AC$$  
> By fixing the polarization of one input dot:  
> - If $C = -1.00$ (Logic 0), the voter becomes a **programmable 2-input AND gate**: $M(A, B, 0) = A \cdot B$.  
> - If $C = +1.00$ (Logic 1), the voter becomes a **programmable 2-input OR gate**: $M(A, B, 1) = A + B$.  
> Each basic gate requires only **5 cells** ($0.0034\ \mu\text{m}^2$) and executes in **0.25 clock cycles**."

---

### Q5: An XOR gate cannot be formed with a single majority voter. How did you design your XOR gate?
**Model Answer:**  
> "XOR is non-linearly separable, so we designed a **dual-rail pipelined architecture** based on the Boolean identity:  
> $$A \oplus B = M(M(A, B, 1), \overline{M(A, B, 0)}, 0)$$  
> The upper rail evaluates $A + B$ in Clock Zone 1. The lower rail evaluates $A \cdot B$ in Zone 1, inverts it diagonally in Zone 2, and both rails converge at a third Majority Voter in Clock Zone 3 biased with $-1.00$.  
> By inserting delay transmission cells, we balanced propagation delay across all 4 zones, eliminating race conditions in **91 cells** with **1.00 clock cycle latency**."

---

### Q6: Why does your Full Adder take 75 cells while the Half Adder takes 91 cells?
**Model Answer:**  
> "The **Half Adder** utilizes our dual-rail XOR structure (which requires parallel branches for $A+B$ and $A \cdot B$, routing around an open corridor to equalize delay, totaling 91 cells).  
> The **Full Adder** uses the canonical **Tougaw-Lent architecture**, which computes:  
> $$C_{out} = M(A, B, C_{in}), \quad M_2 = M(A, B, \overline{C_{in}}), \quad \text{SUM} = M(\overline{C_{out}}, M_2, C_{in})$$  
> Because the three majority voters share intermediate cells tightly in a clustered configuration, Tougaw-Lent achieves higher layout compaction—requiring only **75 cells** and occupying only **$0.0693\ \mu\text{m}^2$**."

---

### Q7: How do your circuits handle the multi-thousand-bit numbers used in Homomorphic Encryption?
**Model Answer:**  
> "We use our **Six-Layer System Architecture**:  
> In **Layer 4**, we apply the **Residue Number System (RNS)** based on the Chinese Remainder Theorem (CRT). Large 2048-bit ciphertexts are decomposed into dozens of independent, small modular channels (e.g., 16-bit or 32-bit residues).  
> Within each residue channel, operations are computed using our QCA building blocks:  
> - Multiplications use our **2×2 Multiplier arrays** (`Multiplier_2x2.qca`).  
> - Multi-bit additions use our cascaded **4-bit Ripple Carry Adders** (`RCA_4bit.qca`).  
> - Modular boundary wraps are handled by our **Modulo-4 Adders** (`Modular_Adder.qca`).  
> This allows massively parallel processing across nanoscale QCA tiles."

---

### Q8: What simulation parameters and physical dimensions did you use in QCADesigner?
**Model Answer:**  
> "We standardized on the recognized academic baseline for QCADesigner 2.0.3:  
> - **Cell Width & Height:** $18\text{ nm} \times 18\text{ nm}$.  
> - **Quantum Dot Diameter:** $5\text{ nm}$.  
> - **Grid Center-to-Center Spacing:** $20\text{ nm}$ ($2\text{ nm}$ inter-cell gap).  
> - **Substrate Material:** GaAs/AlGaAs system with relative permittivity $\varepsilon_r = 12.9$.  
> - **Simulation Engine:** Bistable Approximation with 12,800 samples, convergence tolerance $0.001$, and a 65 nm radius of effect."

---

### Q9: What is the Coherence Vector simulation, and how does it improve on the Bistable engine?
**Model Answer:**  
> "The Bistable Approximation assumes cells reach ground state instantaneously at absolute zero ($0\text{ K}$).  
> The **Coherence Vector engine** models each cell as an open quantum system via the **quantum density matrix** $\hat{\rho} = \frac{1}{2}(\hat{I} + \vec{\lambda} \cdot \vec{\sigma})$ on the Bloch sphere. It solves the **dissipative Liouville-von Neumann master equation**:  
> $$\frac{d\vec{\lambda}}{dt} = \frac{1}{\hbar}(\vec{\Gamma} \times \vec{\lambda}) - \frac{1}{\tau}(\vec{\lambda} - \vec{\lambda}_{ss})$$  
> This captures finite tunneling times ($\gamma$), thermal relaxation ($\tau \approx 1\text{ fs}$), and non-adiabatic switching faults, allowing us to evaluate the thermal stability of our circuits up to 7 Kelvin for semiconductor dots and room temperature for molecular QCA."

---

### Q10: What is your work breakdown and what is planned for the remainder of 7th Semester?
**Model Answer:**  
> - **Completed for MidTerm 1:**  
>   - 11 verified QCA circuit netlists and layout captures.  
>   - Python software demonstration of Paillier and RSA encryption.  
>   - 82 automated verification tests (100% passing).  
>   - Benchmark comparison against 45nm, 28nm, and 7nm CMOS.  
>   - Complete project diary and 13-chapter academic report draft.  
> - **Planned for MidTerm 2 & Final Defense:**  
>   - Scaling the 4-bit adder into an 8-bit Carry-Lookahead Adder (CLA).  
>   - Synthesizing a 4×4 multiplier block.  
>   - Investigating Verilog-to-QCA automated synthesis to compile cryptographic primitives directly into QCA layouts."

---

## 3. Live Demonstration Cheat Sheet

If the panel requests to see the project running live on your laptop:

### Demo 1: Run the Homomorphic Encryption Engine
Open PowerShell in the project directory and run:
```powershell
python HE_Demo/test.py
```
**What to point out:**
- Show key generation ($p, q, n$).
- Point to **Paillier Additive Homomorphism**: $c_{sum} = c_1 \cdot c_2 \pmod{n^2}$. When decrypted, $15 + 27 = 42$ without ever decrypting $c_1$ or $c_2$.
- Point to **Scalar Multiplication**: $c_{scaled} = c_1^5 \pmod{n^2} \implies 15 \times 5 = 75$.

---

### Demo 2: Run the Automated Verification Suite
Run:
```powershell
pytest -v
```
**What to point out:**
- 82 automated tests passing with 100% pass rate.
- Tests verify truth tables, netlist syntax, cell bounding boxes, and cryptographic homomorphism.

---

### Demo 3: Open Layouts in QCADesigner 2.0.3
If asked to open QCADesigner:
```powershell
& "C:\Program Files (x86)\QCADesigner\bin\QCADesigner.exe" QCA_Designs\Ripple_Carry_Adder_4bit\RCA_4bit.qca
```
**What to point out:**
- Show the 4 cascaded Full Adder stages (Stage 0 to Stage 3).
- Point out the 4 color-coded Clock Zones (Green = Zone 0, Magenta = Zone 1, Cyan = Zone 2, White = Zone 3).
- Show the input cells (Dark Blue) and output cells (Yellow).
