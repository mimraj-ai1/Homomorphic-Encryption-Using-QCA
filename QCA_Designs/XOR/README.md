# QCA XOR Gate Implementation

## 1. Overview & Boolean Expression

The Exclusive-OR (XOR) gate is a vital arithmetic primitive in digital computing and cryptography. In Quantum-dot Cellular Automata (QCA), because there is no single elementary Majority Voter that directly computes XOR, the gate is synthesized using verified majority and inversion primitives based on the canonical Boolean expansion:

$$A \oplus B = (A + B) \cdot \overline{A \cdot B} = (A \text{ OR } B) \text{ AND } \text{NOT}(A \text{ AND } B)$$

In QCA Majority logic representation:
$$\text{OR}(A, B) = M(A, B, 1)$$
$$\text{AND}(A, B) = M(A, B, 0)$$
$$\text{NAND}(A, B) = \overline{M(A, B, 0)}$$
$$A \oplus B = M\Big(M(A, B, 1),\ \overline{M(A, B, 0)},\ 0\Big)$$

This architecture splits the inputs $A$ and $B$ across dual rails:
1. **Upper Rail:** Computes $A \cdot B = M(A, B, 0)$ and inverts it to $\overline{A \cdot B}$.
2. **Lower Rail:** Computes $A + B = M(A, B, 1)$.
3. **Recombination Stage:** Combines both rails in an output Majority AND gate ($M(\dots, 0)$) to synthesize $A \oplus B$.

---

## 2. Circuit Layout & Physical Metrics

- **Layout File:** `XOR.qca`
- **Total Cell Count:** 91 cells
- **Cell Size:** 18 nm × 18 nm
- **Dot Diameter:** 5.0 nm
- **Grid Spacing:** 20.0 nm center-to-center
- **Clock Zones Utilized:** 4 zones (Clock 0, Clock 1, Clock 2, Clock 3)
- **Clock Latency:** 1.0 clock cycle (4 clock phases from input to primary `xor` output)
- **Bounding Box:** $438.0\text{ nm} \times 258.0\text{ nm}$ ($x \in [51.0, 489.0]$, $y \in [91.0, 349.0]$)
- **Calculated Layout Area:** $113,004\text{ nm}^2 = 0.113004\ \mu\text{m}^2 \approx 0.113\ \mu\text{m}^2$

### Key Pin & Landmark Cell Locations

| Cell Function | Pin Label | Position $(x, y)$ in nm | Clock Zone | Function / Description |
| :--- | :--- | :--- | :---: | :--- |
| **INPUT** | `A` | $(60.0, 140.0)$ | Clock 0 | Primary Input $A$ |
| **INPUT** | `B` | $(120.0, 180.0)$ | Clock 0 | Primary Input $B$ |
| **FIXED** | `-1.00` | $(260.0, 220.0)$ | Clock 2 | Fixed bias ($P = -1$) for AND stage |
| **FIXED** | `1.00` | $(260.0, 260.0)$ | Clock 3 | Fixed bias ($P = +1$) for OR stage |
| **FIXED** | `-1.00` | $(440.0, 340.0)$ | Clock 3 | Fixed bias ($P = -1$) for output recombination |
| **OUTPUT** | `a^b` | $(300.0, 180.0)$ | Clock 3 | Tap for $A \cdot B$ (Half Adder Carry) |
| **OUTPUT** | `AvB` | $(300.0, 300.0)$ | Clock 0 | Tap for $A + B$ (Intermediate OR) |
| **OUTPUT** | `xor` | $(480.0, 300.0)$ | Clock 3 | Primary Evaluated Output ($A \oplus B$) |

---

## 3. Clocking & Pipelining Scheme

To maintain unidirectional signal propagation and prevent backward signal reflections, the layout incorporates the standard QCA 4-phase clocking mechanism:
- **Clock 0 (Switch/Input):** Captures inputs $A$ and $B$ and begins distribution.
- **Clock 1 (Hold/Propagation):** Propagates inputs toward the majority voter branches.
- **Clock 2 (Switch/Evaluation):** Evaluates intermediate products and performs inversion.
- **Clock 3 (Hold/Output):** Final recombination majority voter locks and delivers the stable $A \oplus B$ polarization.

---

## 4. Verification Status

- **File Syntax & Layout Loading:** Fully verified in QCADesigner 2.0.3 (zero parsing errors).
- **Physical Simulation Verification:** `PENDING MANUAL QCADESIGNER VERIFICATION`
  *(Refer to `simulation_notes.md` for exact manual execution and waveform inspection instructions).*
