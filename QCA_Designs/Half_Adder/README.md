# QCA Half Adder Implementation

## 1. Overview & Boolean Equations

The Half Adder is the fundamental 1-bit arithmetic addition unit that computes the sum and carry-out of two binary inputs without taking a carry-in from a preceding stage. In Quantum-dot Cellular Automata (QCA), the Half Adder is constructed by synergistically integrating the verified dual-rail XOR gate with the Majority AND voter.

$$\text{SUM} = A \oplus B = (A + B) \cdot \overline{A \cdot B}$$
$$\text{CARRY} = A \cdot B = M(A, B, 0)$$

In QCA Majority logic representation:
$$\text{CARRY} = M(A, B, 0)$$
$$\text{OR}_{\text{int}} = M(A, B, 1)$$
$$\text{SUM} = M\Big(\text{OR}_{\text{int}},\ \overline{\text{CARRY}},\ 0\Big)$$

Because the evaluation of $\text{CARRY} = A \cdot B$ is an intrinsic intermediate step in evaluating $\text{SUM} = (A + B) \cdot \overline{A \cdot B}$, the carry output is tapped directly from the AND branch, eliminating redundant majority voters and saving circuit area and power dissipation.

---

## 2. Circuit Layout & Physical Metrics

- **Layout File:** `Half_Adder.qca`
- **Total Cell Count:** 91 cells
- **Cell Size:** 18 nm × 18 nm
- **Dot Diameter:** 5.0 nm
- **Grid Spacing:** 20.0 nm center-to-center
- **Clock Zones Utilized:** 4 zones (Clock 0, Clock 1, Clock 2, Clock 3)
- **Clock Latency:** 1.0 clock cycle (4 phases)
- **Bounding Box:** $438.0\text{ nm} \times 258.0\text{ nm}$ ($x \in [51.0, 489.0]$, $y \in [91.0, 349.0]$)
- **Calculated Layout Area:** $113,004\text{ nm}^2 = 0.113004\ \mu\text{m}^2 \approx 0.113\ \mu\text{m}^2$

### Key Pin & Landmark Cell Locations

| Cell Function | Pin Label | Position $(x, y)$ in nm | Clock Zone | Function / Description |
| :--- | :--- | :--- | :---: | :--- |
| **INPUT** | `A` | $(60.0, 140.0)$ | Clock 0 | Primary Addend Input $A$ |
| **INPUT** | `B` | $(120.0, 180.0)$ | Clock 0 | Primary Addend Input $B$ |
| **FIXED** | `-1.00` | $(260.0, 220.0)$ | Clock 2 | Fixed bias ($P = -1$) for Carry Majority Voter |
| **FIXED** | `1.00` | $(260.0, 260.0)$ | Clock 3 | Fixed bias ($P = +1$) for OR intermediate branch |
| **FIXED** | `-1.00` | $(440.0, 340.0)$ | Clock 3 | Fixed bias ($P = -1$) for Sum output stage |
| **OUTPUT** | `CARRY` | $(300.0, 180.0)$ | Clock 3 | Primary Carry Output ($A \cdot B$) |
| **OUTPUT** | `SUM` | $(480.0, 300.0)$ | Clock 3 | Primary Sum Output ($A \oplus B$) |

---

## 3. Clocking Scheme & Synchronization

Both primary outputs (`SUM` and `CARRY`) are synchronized to transition and hold valid data within **Clock Zone 3**, ensuring that downstream arithmetic circuits (such as Full Adders and Ripple Carry Adders) receive glitch-free, phase-aligned inputs.

- **Clock 0 (Phase 1):** Inputs $A$ and $B$ are sampled and distributed.
- **Clock 1 (Phase 2):** Propagates inputs into both the AND and OR branches.
- **Clock 2 (Phase 3):** Evaluates $A \cdot B$ and initiates anti-phase inversion for $\overline{A \cdot B}$.
- **Clock 3 (Phase 4):** Evaluates the final recombination majority voter for `SUM` and delivers both `SUM` and `CARRY` to the output pins.

---

## 4. Verification Status

- **File Syntax & Layout Loading:** Fully verified in QCADesigner 2.0.3 (zero parsing errors).
- **Physical Simulation Verification:** `PENDING MANUAL QCADESIGNER VERIFICATION`
  *(Refer to `simulation_notes.md` for exact manual execution and waveform inspection instructions).*
