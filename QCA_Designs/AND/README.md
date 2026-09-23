# QCA AND Gate Implementation

## 1. Overview & Boolean Expression

In Quantum-dot Cellular Automata (QCA), the logical AND operation is realized using the fundamental 3-input Majority Voter ($M$) by fixing one of the three input lines to a constant polarization of $P = -1$ (representing binary `0`).

$$\text{AND}(A, B) = M(A, B, 0) = A \cdot B + B \cdot 0 + A \cdot 0 = A \cdot B$$

---

## 2. Circuit Layout Specification

- **File Name:** `AND.qca`
- **Cell Count:** 5 cells
- **Cell Size:** 18 nm × 18 nm
- **Dot Diameter:** 5.0 nm
- **Grid Spacing:** 20.0 nm center-to-center
- **Clock Zones Utilized:** Clock 0 (1 zone)
- **Clock Latency:** 0.25 clock cycles
- **Bounding Box:** $58.0\text{ nm} \times 58.0\text{ nm}$ ($x \in [71.0, 129.0]$, $y \in [71.0, 129.0]$)
- **Calculated Layout Area:** $3,364\text{ nm}^2 = 0.003364\ \mu\text{m}^2 \approx 0.0034\ \mu\text{m}^2$

### Cell Placement Netlist

| Cell Function | Label | Position $(x, y)$ in nm | Clock Zone | Polarization / Initial State |
| :--- | :--- | :--- | :--- | :--- |
| **INPUT** | `A` | $(80.0, 100.0)$ | Clock 0 | Dynamic Input ($P \in \{-1, +1\}$) |
| **INPUT** | `B` | $(100.0, 80.0)$ | Clock 0 | Dynamic Input ($P \in \{-1, +1\}$) |
| **FIXED** | `-1.00` | $(100.0, 120.0)$ | Clock 0 | Fixed $P = -1.0$ (Logic 0) |
| **NORMAL** | *(Center)* | $(100.0, 100.0)$ | Clock 0 | Neutral evaluation cell |
| **OUTPUT** | `Y` | $(120.0, 100.0)$ | Clock 0 | Driven Output ($Y = A \cdot B$) |

---

## 3. Physical Switching Principle

Electrostatic Coulomb repulsion between diagonal quantum dots within neighboring cells dictates the polarization of the central majority cell:
$$E_k = \frac{q_i q_j}{4 \pi \epsilon_0 \epsilon_r r_{ij}}$$
Because the fixed cell exerts a constant electrostatic bias equivalent to logic `0`, the center cell assumes polarization $P = +1$ (logic `1`) if and only if **both** input cells $A$ and $B$ possess polarization $P = +1$. If either $A$ or $B$ (or both) is logic `0`, the majority of the three influencing cells is logic `0`, driving the center cell and output cell $Y$ to polarization $P = -1$.

---

## 4. Verification Status

- **Layout File Verification:** Fully verified against QCADesigner 2.0.3 file parser.
- **Physical Simulation Verification:** `PENDING MANUAL QCADESIGNER VERIFICATION`
  *(Refer to `simulation_notes.md` for exact manual execution and waveform inspection instructions).*
