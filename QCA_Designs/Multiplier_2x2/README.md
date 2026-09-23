# QCA 2×2 Binary Multiplier Implementation

## 1. Overview & Arithmetic Formulation

The 2×2 binary multiplier computes the arithmetic product of two 2-bit unsigned binary integers $A = (A_1 A_0)_2$ and $B = (B_1 B_0)_2$, generating a 4-bit product $P = (P_3 P_2 P_1 P_0)_2$:

$$P = A \times B = (2A_1 + A_0) \times (2B_1 + B_0) = 4(A_1 B_1) + 2(A_1 B_0 + A_0 B_1) + (A_0 B_0)$$

### Step 1: Partial Product Generation
Four 1-bit partial products ($PP_k$) are computed concurrently using QCA Majority AND gates ($M(X, Y, 0)$):
- $PP_0 = A_0 \cdot B_0$ (Weight $2^0$)
- $PP_1 = A_1 \cdot B_0$ (Weight $2^1$)
- $PP_2 = A_0 \cdot B_1$ (Weight $2^1$)
- $PP_3 = A_1 \cdot B_1$ (Weight $2^2$)

### Step 2: Partial Product Accumulation
- **Bit 0 ($2^0$):**
  $$P_0 = PP_0 = A_0 \cdot B_0$$
- **Bit 1 ($2^1$):** Sum of $PP_1$ and $PP_2$ using Half Adder $\text{HA}_1$:
  $$\text{HA}_1(PP_1, PP_2) \longrightarrow P_1, C_1$$
  $$P_1 = PP_1 \oplus PP_2 = (A_1 \cdot B_0) \oplus (A_0 \cdot B_1)$$
  $$C_1 = PP_1 \cdot PP_2 = (A_1 \cdot B_0) \cdot (A_0 \cdot B_1)$$
- **Bit 2 ($2^2$) and Bit 3 ($2^3$):** Sum of $PP_3$ and $C_1$ using Half Adder $\text{HA}_2$:
  $$\text{HA}_2(PP_3, C_1) \longrightarrow P_2, P_3$$
  $$P_2 = PP_3 \oplus C_1 = (A_1 \cdot B_1) \oplus C_1$$
  $$P_3 = PP_3 \cdot C_1 = (A_1 \cdot B_1) \cdot C_1$$

---

## 2. Circuit Layout & Physical Metrics

- **Layout File:** `Multiplier_2x2.qca`
- **Total Cell Count:** 91 cells
- **Cell Size:** 18 nm × 18 nm
- **Dot Diameter:** 5.0 nm
- **Grid Spacing:** 20.0 nm center-to-center
- **Clock Zones Utilized:** 4 zones (Clock 0, Clock 1, Clock 2, Clock 3)
- **Clock Latency:** 1.0 clock cycle (4 phases)
- **Bounding Box:** $318.0\text{ nm} \times 238.0\text{ nm}$ ($x \in [51.0, 369.0]$, $y \in [51.0, 289.0]$)
- **Calculated Layout Area:** $75,684\text{ nm}^2 = 0.075684\ \mu\text{m}^2 \approx 0.076\ \mu\text{m}^2$

### Primary I/O Pin List

| Pin Type | Label | Position $(x, y)$ in nm | Clock Zone | Function |
| :--- | :--- | :--- | :---: | :--- |
| **INPUT** | `A0` | $(60.0, 60.0)$ | Clock 0 | Least significant bit of multiplicand $A$ |
| **INPUT** | `B0` | $(60.0, 120.0)$ | Clock 0 | Least significant bit of multiplier $B$ |
| **INPUT** | `A1` | $(60.0, 180.0)$ | Clock 0 | Most significant bit of multiplicand $A$ |
| **INPUT** | `B1` | $(60.0, 240.0)$ | Clock 0 | Most significant bit of multiplier $B$ |
| **OUTPUT** | `P0` | $(360.0, 80.0)$ | Clock 3 | Product bit 0 ($2^0$) |
| **OUTPUT** | `P1` | $(360.0, 140.0)$ | Clock 3 | Product bit 1 ($2^1$) |
| **OUTPUT** | `P2` | $(360.0, 200.0)$ | Clock 3 | Product bit 2 ($2^2$) |
| **OUTPUT** | `P3` | $(360.0, 240.0)$ | Clock 3 | Product bit 3 ($2^3$) |

---

## 3. Pipelining & Clock Synchronization

All 4 outputs ($P_0, P_1, P_2, P_3$) are synchronized to emerge simultaneously in **Clock Zone 3**:
1. **Clock 0:** Samples and routes operands $A_0, A_1, B_0, B_1$.
2. **Clock 1:** Evaluates 4 partial products ($PP_0, PP_1, PP_2, PP_3$).
3. **Clock 2:** Evaluates $\text{HA}_1$ generating intermediate sum $P_1$ and carry $C_1$.
4. **Clock 3:** Evaluates $\text{HA}_2$ generating $P_2, P_3$, and outputs all 4 product bits in phase alignment.

---

## 4. Verification Status

- **File Syntax & Layout Loading:** Fully verified in QCADesigner 2.0.3 (zero parsing errors).
- **Physical Simulation Verification:** `PENDING MANUAL QCADESIGNER VERIFICATION`
  *(Refer to `simulation_notes.md` for exact manual execution and waveform inspection instructions).*
