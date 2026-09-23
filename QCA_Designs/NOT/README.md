# QCA NOT Gate (Inverter) Implementation

## 1. Overview & Boolean Expression

The NOT gate (inverter) in Quantum-dot Cellular Automata operates by exploiting the electrostatic anti-phase coupling that occurs when two QCA cells are positioned diagonally adjacent to each other.

$$\text{NOT}(A) = \overline{A}$$

Unlike conventional CMOS inverters that require complementary PMOS/NMOS transistor pairs, a QCA inverter achieves logical negation entirely through geometry and diagonal Coulombic repulsion without any active biasing voltage or fixed cells.

---

## 2. Circuit Layout Specification

- **File Name:** `NOT.qca`
- **Cell Count:** 4 cells
- **Cell Size:** 18 nm × 18 nm
- **Dot Diameter:** 5.0 nm
- **Grid Spacing:** 20.0 nm center-to-center
- **Clock Zones Utilized:** Clock 0 (1 zone)
- **Clock Latency:** 0.25 clock cycles
- **Bounding Box:** $78.0\text{ nm} \times 38.0\text{ nm}$ ($x \in [51.0, 129.0]$, $y \in [71.0, 109.0]$)
- **Calculated Layout Area:** $2,964\text{ nm}^2 = 0.002964\ \mu\text{m}^2 \approx 0.0030\ \mu\text{m}^2$

### Cell Placement Netlist

| Cell Function | Label | Position $(x, y)$ in nm | Clock Zone | Polarization / Initial State |
| :--- | :--- | :--- | :--- | :--- |
| **INPUT** | `A` | $(60.0, 80.0)$ | Clock 0 | Dynamic Input ($P \in \{-1, +1\}$) |
| **NORMAL** | *(Wire)* | $(80.0, 80.0)$ | Clock 0 | Collinear transmission cell |
| **NORMAL** | *(Inverter)* | $(100.0, 100.0)$ | Clock 0 | Diagonally displaced anti-phase cell |
| **OUTPUT** | `A_inv` | $(120.0, 100.0)$ | Clock 0 | Driven Inverted Output ($\overline{A}$) |

---

## 3. Physical Switching Principle (Anti-Phase Coupling)

- In collinear cell placement (cells positioned horizontally side by side along the $x$-axis), adjacent quantum dots on the right edge of cell $i$ face quantum dots on the left edge of cell $i+1$. Minimum Coulomb energy occurs when electron alignments match, causing **ferroelectric-like (in-phase)** coupling: polarization is directly preserved.
- When cell $i+1$ is displaced diagonally ($\Delta x = +20\text{ nm}, \Delta y = +20\text{ nm}$), the bottom-right quantum dot of cell $i$ lies in closest physical proximity to the top-left quantum dot of cell $i+1$. Strong electrostatic repulsion between these two dots forces their electrons apart. Consequently, the minimum electrostatic energy configuration in cell $i+1$ is the **exact inverse** of the polarization in cell $i$, producing **anti-phase (inverting)** coupling:
  $$P_{i+1} \approx -P_i$$
- Cell $(120.0, 100.0)$ then transmits this inverted state collinear to the output pin.

---

## 4. Verification Status

- **Layout File Verification:** Validated via automated QCADesigner 2.0.3 loader.
- **Physical Simulation Verification:** `PENDING MANUAL QCADESIGNER VERIFICATION`
  *(Refer to `simulation_notes.md` for execution protocol).*
