# QCA Full Adder Implementation

## 1. Overview & Boolean Equations

A 1-bit Full Adder computes the arithmetic sum of three binary inputs: addend $A$, addend $B$, and carry-in $C_{in}$, producing sum bit $\text{SUM}$ and carry-out bit $C_{out}$. In Quantum-dot Cellular Automata (QCA), the Full Adder is constructed using the elegant 3-Majority-Voter architecture originally conceptualized by Tougaw and Lent:

$$\text{SUM} = A \oplus B \oplus C_{in}$$
$$C_{out} = (A \cdot B) + (C_{in} \cdot (A \oplus B)) = A \cdot B + B \cdot C_{in} + A \cdot C_{in}$$

In QCA Majority logic representation:
$$C_{out} = M(A, B, C_{in})$$
$$M_2 = M(A, B, \overline{C_{in}})$$
$$\text{SUM} = M\Big(\overline{C_{out}},\ M_2,\ C_{in}\Big)$$

### Mathematical Derivation of QCA Majority Representation

1. **Carry-Out:** The definition of the 3-input Majority Voter directly matches the Boolean expression for carry-out:
   $$M(A, B, C_{in}) = AB + BC_{in} + AC_{in} \equiv C_{out}$$
2. **Sum:** When $A = B$:
   - $C_{out} = A = B \implies \overline{C_{out}} = \overline{A}$
   - $M_2 = M(A, A, \overline{C_{in}}) = A$
   - $\text{SUM} = M(\overline{A}, A, C_{in}) = C_{in}$
   - Since $A \oplus B = 0$, $A \oplus B \oplus C_{in} = 0 \oplus C_{in} = C_{in}$. Match.
3. When $A \ne B$:
   - $C_{out} = M(A, \overline{A}, C_{in}) = C_{in} \implies \overline{C_{out}} = \overline{C_{in}}$
   - $M_2 = M(A, \overline{A}, \overline{C_{in}}) = \overline{C_{in}}$
   - $\text{SUM} = M(\overline{C_{in}}, \overline{C_{in}}, C_{in}) = \overline{C_{in}}$
   - Since $A \oplus B = 1$, $A \oplus B \oplus C_{in} = 1 \oplus C_{in} = \overline{C_{in}}$. Match.

The architecture uses exactly 3 Majority Voters and 2 inverters.

---

## 2. Circuit Layout & Physical Metrics

- **Layout File:** `Full_Adder.qca`
- **Total Cell Count:** 75 cells
- **Cell Size:** 18 nm × 18 nm
- **Dot Diameter:** 5.0 nm
- **Grid Spacing:** 20.0 nm center-to-center
- **Clock Zones Utilized:** 4 zones (Clock 0, Clock 1, Clock 2, Clock 3)
- **Clock Latency:** 1.0 clock cycle (4 phases)
- **Bounding Box:** $318.0\text{ nm} \times 218.0\text{ nm}$ ($x \in [51.0, 369.0]$, $y \in [91.0, 309.0]$)
- **Calculated Layout Area:** $69,324\text{ nm}^2 = 0.069324\ \mu\text{m}^2 \approx 0.069\ \mu\text{m}^2$

### Key Pin & Landmark Cell Locations

| Cell Function | Pin Label | Position $(x, y)$ in nm | Clock Zone | Function / Description |
| :--- | :--- | :--- | :---: | :--- |
| **INPUT** | `A` | $(60.0, 100.0)$ | Clock 0 | Primary Addend Input $A$ |
| **INPUT** | `B` | $(60.0, 140.0)$ | Clock 0 | Primary Addend Input $B$ |
| **INPUT** | `Cin` | $(60.0, 220.0)$ | Clock 0 | Primary Carry-In Input $C_{in}$ |
| **NORMAL** | *(M1 Center)* | $(180.0, 140.0)$ | Clock 2 | $M_1$ Majority Center cell ($C_{out}$) |
| **NORMAL** | *(M2 Center)* | $(180.0, 220.0)$ | Clock 2 | $M_2$ Majority Center cell ($M(A, B, \overline{C_{in}})$) |
| **NORMAL** | *(M3 Center)* | $(300.0, 240.0)$ | Clock 3 | $M_3$ Majority Center cell ($\text{SUM}$) |
| **OUTPUT** | `Cout` | $(360.0, 120.0)$ | Clock 3 | Primary Carry-Out Pin ($C_{out}$) |
| **OUTPUT** | `SUM` | $(360.0, 240.0)$ | Clock 3 | Primary Sum Pin ($\text{SUM}$) |

---

## 3. Clocking Scheme & Synchronization

- **Clock 0 (Phase 1):** Captures inputs $A$, $B$, and $C_{in}$ and distributes them into routing channels.
- **Clock 1 (Phase 2):** Routes $A$ and $B$ to both $M_1$ and $M_2$, and routes $C_{in}$ to $M_1$ and via an inverter to $M_2$.
- **Clock 2 (Phase 3):** Evaluates $M_1$ ($C_{out}$) and $M_2$, and performs inversion of $C_{out}$ towards $M_3$.
- **Clock 3 (Phase 4):** Evaluates $M_3$ ($\text{SUM}$) and outputs both $C_{out}$ and $\text{SUM}$ in phase alignment.

---

## 4. Verification Status

- **File Syntax & Layout Loading:** Fully verified in QCADesigner 2.0.3 (zero parsing errors).
- **Physical Simulation Verification:** `PENDING MANUAL QCADESIGNER VERIFICATION`
  *(Refer to `simulation_notes.md` for exact manual execution and waveform inspection instructions).*
