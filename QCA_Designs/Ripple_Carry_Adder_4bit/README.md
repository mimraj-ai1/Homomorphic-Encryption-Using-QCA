# QCA 4-bit Ripple Carry Adder (RCA) Implementation

## 1. Overview & Architecture

The 4-bit Ripple Carry Adder (RCA) computes the multi-bit arithmetic addition of two 4-bit binary unsigned integers $A = (A_3, A_2, A_1, A_0)_2$ and $B = (B_3, B_2, B_1, B_0)_2$ with an initial carry-in $C_{in}$, producing a 4-bit sum vector $S = (S_3, S_2, S_1, S_0)_2$ and a final carry-out bit $C_{out}$:

$$A + B + C_{in} = 2^4 \cdot C_{out} + \sum_{k=0}^{3} 2^k \cdot S_k$$

The architecture cascades 4 verified 1-bit Full Adders in series:
$$\text{FA}_0(A_0, B_0, C_{in}) \longrightarrow S_0, C_1$$
$$\text{FA}_1(A_1, B_1, C_1) \longrightarrow S_1, C_2$$
$$\text{FA}_2(A_2, B_2, C_2) \longrightarrow S_2, C_3$$
$$\text{FA}_3(A_3, B_3, C_3) \longrightarrow S_3, C_{out}$$

### Carry-Propagation Pipeline
In QCA, data flow is driven by electrostatic field interactions under a 4-phase clock. The carry-out bit of each Full Adder stage ripples into the subsequent stage along dedicated transmission channels synchronized across clock zones.

---

## 2. Circuit Layout & Physical Metrics

- **Layout File:** `RCA_4bit.qca`
- **Total Cell Count:** 315 cells
- **Cell Size:** 18 nm × 18 nm
- **Dot Diameter:** 5.0 nm
- **Grid Spacing:** 20.0 nm center-to-center
- **Clock Zones Utilized:** 4 zones (Clock 0, Clock 1, Clock 2, Clock 3)
- **Clock Latency:** 4.0 clock cycles (total pipelined ripple latency from $C_{in}$ to $C_{out}$)
- **Bounding Box:** $1338.0\text{ nm} \times 218.0\text{ nm}$ ($x \in [51.0, 1389.0]$, $y \in [91.0, 309.0]$)
- **Calculated Layout Area:** $291,684\text{ nm}^2 = 0.291684\ \mu\text{m}^2 \approx 0.292\ \mu\text{m}^2$

### Primary I/O Pin List

| Pin Type | Label | Bit Index | Position $(x, y)$ in nm | Clock Zone | Function |
| :--- | :--- | :---: | :--- | :---: | :--- |
| **INPUT** | `A0` | Bit 0 | $(60.0, 100.0)$ | Clock 0 | Least significant addend bit of $A$ |
| **INPUT** | `B0` | Bit 0 | $(60.0, 140.0)$ | Clock 0 | Least significant addend bit of $B$ |
| **INPUT** | `Cin` | Carry-In | $(60.0, 220.0)$ | Clock 0 | Global Carry-In |
| **INPUT** | `A1` | Bit 1 | $(400.0, 100.0)$ | Clock 0 | Addend bit 1 of $A$ |
| **INPUT** | `B1` | Bit 1 | $(400.0, 140.0)$ | Clock 0 | Addend bit 1 of $B$ |
| **INPUT** | `A2` | Bit 2 | $(740.0, 100.0)$ | Clock 0 | Addend bit 2 of $A$ |
| **INPUT** | `B2` | Bit 2 | $(740.0, 140.0)$ | Clock 0 | Addend bit 2 of $B$ |
| **INPUT** | `A3` | Bit 3 | $(1080.0, 100.0)$ | Clock 0 | Most significant addend bit of $A$ |
| **INPUT** | `B3` | Bit 3 | $(1080.0, 140.0)$ | Clock 0 | Most significant addend bit of $B$ |
| **OUTPUT** | `S0` | Bit 0 | $(360.0, 240.0)$ | Clock 3 | Sum bit 0 |
| **OUTPUT** | `S1` | Bit 1 | $(700.0, 240.0)$ | Clock 3 | Sum bit 1 |
| **OUTPUT** | `S2` | Bit 2 | $(1040.0, 240.0)$ | Clock 3 | Sum bit 2 |
| **OUTPUT** | `S3` | Bit 3 | $(1380.0, 240.0)$ | Clock 3 | Sum bit 3 |
| **OUTPUT** | `Cout` | Carry-Out | $(1380.0, 120.0)$ | Clock 3 | Most significant Carry-Out ($C_4$) |

---

## 3. Pipelining & Clock Zone Alignment

1. **Stage 0 ($\text{FA}_0$):** Operates on Clock phases $0 \to 1 \to 2 \to 3$. Produces $S_0$ and propagates $C_1$.
2. **Stage 1 ($\text{FA}_1$):** Receives $C_1$ via inter-stage bridge; computes $S_1$ and $C_2$.
3. **Stage 2 ($\text{FA}_2$):** Receives $C_2$; computes $S_2$ and $C_3$.
4. **Stage 3 ($\text{FA}_3$):** Receives $C_3$; delivers $S_3$ and final $C_{out}$.

---

## 4. Verification Status

- **File Syntax & Layout Loading:** Fully verified in QCADesigner 2.0.3 (zero parsing errors).
- **Physical Simulation Verification:** `PENDING MANUAL QCADESIGNER VERIFICATION`
  *(Refer to `simulation_notes.md` for exact manual execution and waveform inspection instructions).*
