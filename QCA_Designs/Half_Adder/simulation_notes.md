# QCA Half Adder: Simulation Notes & Verification Protocol

## 1. Simulation Engine Parameters (Standardized)

- **Software:** QCADesigner 2.0.3
- **Simulation Engine:** Bistable Approximation (BA)
- **Number of Samples:** 12,800
- **Convergence Tolerance:** 0.001000
- **Radius of Effect:** 65.000000 nm
- **Relative Permittivity ($\epsilon_r$):** 12.900000
- **Clock High:** $9.800000 \times 10^{-22}$ J
- **Clock Low:** $1.000000 \times 10^{-23}$ J
- **Clock Shift:** 0.000000
- **Clock Amplitude Factor:** 2.000000
- **Max Iterations per Sample:** 100

---

## 2. Step-by-Step Manual Simulation Procedure

1. Launch QCADesigner 2.0.3.
2. Select **File $\to$ Open** and load:
   `c:\Users\sekhm\Desktop\HE-QCA-Project\QCA_Designs\Half_Adder\Half_Adder.qca`
3. Verify the layout geometry:
   - 91 total cells arranged in 4 distinct clock zones (Green, Magenta, Cyan, White).
   - Inputs: `A` (left, blue) at $(60, 140)$ and `B` (left, blue) at $(120, 180)$.
   - Outputs: `SUM` (right, yellow) at $(480, 300)$ and `CARRY` (middle-top, yellow) at $(300, 180)$.
4. Open **Simulation $\to$ Simulation Engine Setup**, verify Bistable Approximation parameters.
5. Click **Start Simulation**.
6. Inspect the resulting waveform traces:
   - Trace `B`: Square wave.
   - Trace `A`: Square wave at higher frequency.
   - Trace `SUM`: Evaluated Half Adder Sum ($A \oplus B$).
   - Trace `CARRY`: Evaluated Half Adder Carry ($A \cdot B$).

---

## 3. Waveform Verification Checklist

| Quadrant | Input $A$ | Input $B$ | Expected `SUM` | Expected `CARRY` | Observed `(C, S)` | Verification |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | Low ($0$) | Low ($0$) | Low ($-1.00$) | Low ($-1.00$) | `[Pending Manual Run]` | PENDING |
| 2 | High ($1$) | Low ($0$) | High ($+1.00$) | Low ($-1.00$) | `[Pending Manual Run]` | PENDING |
| 3 | Low ($0$) | High ($1$) | High ($+1.00$) | Low ($-1.00$) | `[Pending Manual Run]` | PENDING |
| 4 | High ($1$) | High ($1$) | Low ($-1.00$) | High ($+1.00$) | `[Pending Manual Run]` | PENDING |

---

## 4. Current Verification Status

- **Status:** `PENDING MANUAL QCADESIGNER VERIFICATION`
- **Integrity Note:** Layout syntax and file integrity verified by automated parser and QCADesigner loader. Waveforms pending manual GUI execution.
