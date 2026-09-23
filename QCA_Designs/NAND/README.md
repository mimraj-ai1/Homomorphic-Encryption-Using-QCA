# QCA NAND Gate Implementation

## 1. Overview & Boolean Expression

In Quantum-dot Cellular Automata, the universal NAND gate is implemented by cascading a 3-input Majority AND configuration with an anti-phase inverting stage:

$$\text{NAND}(A, B) = \overline{A \cdot B} = \overline{M(A, B, 0)}$$

The Majority Voter evaluates $A \cdot B$, which is subsequently inverted by a diagonally displaced QCA cell stage to produce $\overline{A \cdot B}$.

---

## 2. Circuit Layout Specification

- **File Name:** `NAND.qca`
- **Cell Count:** 7 cells
- **Cell Size:** 18 nm × 18 nm
- **Dot Diameter:** 5.0 nm
- **Grid Spacing:** 20.0 nm center-to-center
- **Clock Zones Utilized:** Clock 0 (1 zone)
- **Clock Latency:** 0.25 clock cycles
- **Bounding Box:** $98.0\text{ nm} \times 58.0\text{ nm}$ ($x \in [71.0, 169.0]$, $y \in [71.0, 129.0]$)
- **Calculated Layout Area:** $5,684\text{ nm}^2 = 0.005684\ \mu\text{m}^2 \approx 0.0057\ \mu\text{m}^2$

### Cell Placement Netlist

| Cell Function | Label | Position $(x, y)$ in nm | Clock Zone | Function / Description |
| :--- | :--- | :--- | :--- | :--- |
| **INPUT** | `A` | $(80.0, 100.0)$ | Clock 0 | Dynamic Input $A$ |
| **INPUT** | `B` | $(100.0, 80.0)$ | Clock 0 | Dynamic Input $B$ |
| **FIXED** | `-1.00` | $(100.0, 120.0)$ | Clock 0 | Fixed $P = -1.0$ (AND bias) |
| **NORMAL** | *(Center)* | $(100.0, 100.0)$ | Clock 0 | Majority Voter central cell ($A \cdot B$) |
| **NORMAL** | *(Wire)* | $(120.0, 100.0)$ | Clock 0 | Transmission cell |
| **NORMAL** | *(Inverter)* | $(140.0, 120.0)$ | Clock 0 | Diagonally displaced anti-phase cell ($\overline{A \cdot B}$) |
| **OUTPUT** | `Y` | $(160.0, 120.0)$ | Clock 0 | Driven Output pin |

---

## 3. Physical Switching Principle

1. **Majority Stage:** The center cell at $(100.0, 100.0)$ computes $M(A, B, 0) = A \cdot B$.
2. **Coupling Stage:** Cell $(120.0, 100.0)$ carries the un-inverted product $A \cdot B$.
3. **Inversion Stage:** Cell $(140.0, 120.0)$ is placed diagonally adjacent to $(120.0, 100.0)$ ($\Delta x = +20\text{ nm}, \Delta y = +20\text{ nm}$). Due to diagonal Coulomb repulsion, its electrons take the anti-phase configuration, inverting the AND result into NAND.
4. **Output Driver:** Cell $(160.0, 120.0)$ outputs the final NAND result to output $Y$.

---

## 4. Verification Status

- **Layout File Verification:** Validated via automated QCADesigner 2.0.3 loader.
- **Physical Simulation Verification:** `PENDING MANUAL QCADESIGNER VERIFICATION`
  *(Refer to `simulation_notes.md` for execution protocol).*
