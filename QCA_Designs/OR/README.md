# QCA OR Gate Implementation

## 1. Overview & Boolean Expression

In Quantum-dot Cellular Automata (QCA), the logical OR operation is implemented using the 3-input Majority Voter ($M$) by fixing one of the three input cells to a constant polarization of $P = +1$ (representing binary `1`).

$$\text{OR}(A, B) = M(A, B, 1) = A \cdot B + B \cdot 1 + A \cdot 1 = A + B$$

---

## 2. Circuit Layout Specification

- **File Name:** `OR.qca`
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
| **FIXED** | `1.00` | $(100.0, 120.0)$ | Clock 0 | Fixed $P = +1.0$ (Logic 1) |
| **NORMAL** | *(Center)* | $(100.0, 100.0)$ | Clock 0 | Neutral evaluation cell |
| **OUTPUT** | `Y` | $(120.0, 100.0)$ | Clock 0 | Driven Output ($Y = A + B$) |

---

## 3. Physical Switching Principle

In the majority arrangement, the fixed polarization cell at $(100.0, 120.0)$ provides a permanent positive electrostatic bias ($P = +1$). Therefore:
- If neither $A$ nor $B$ is positive ($A = 0, B = 0$), the inputs present two negative polarizations vs. one positive polarization, driving the center cell to $P = -1$ (logic `0`).
- If either $A$ or $B$ (or both) is positive ($P = +1$), there are at least two positive polarizations among the three neighbors, driving the center cell to $P = +1$ (logic `1`).

---

## 4. Verification Status

- **Layout File Verification:** Validated via automated QCADesigner 2.0.3 loader.
- **Physical Simulation Verification:** `PENDING MANUAL QCADESIGNER VERIFICATION`
  *(Refer to `simulation_notes.md` for execution protocol).*
