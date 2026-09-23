# QCA NAND Gate: Simulation Notes & Verification Protocol

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

1. Open QCADesigner 2.0.3.
2. Select **File $\to$ Open** and load:
   `c:\Users\sekhm\Desktop\HE-QCA-Project\QCA_Designs\NAND\NAND.qca`
3. Inspect the 7-cell structure:
   - Majority AND core at $(100, 100)$ with inputs $A, B$ and fixed $-1.00$.
   - Wire cell at $(120, 100)$ extending right.
   - Diagonal anti-phase cell at $(140, 120)$.
   - Output cell `Y` at $(160, 120)$.
4. Open **Simulation $\to$ Simulation Engine Setup**, verify Bistable Approximation parameters.
5. Click **Start Simulation**.
6. Examine the generated waveform traces:
   - Trace 1 (`B`): Square wave.
   - Trace 2 (`A`): Square wave.
   - Trace 3 (`Y`): Evaluated NAND output polarization waveform.

---

## 3. Waveform Verification Checklist

| Time Interval | Input $A$ | Input $B$ | Expected $Y$ Polarization | Observed $Y$ Polarization | Verification |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Interval 1 | Low ($-1$) | Low ($-1$) | Positive ($\approx +0.954$) | `[Pending Manual Run]` | PENDING |
| Interval 2 | High ($+1$) | Low ($-1$) | Positive ($\approx +0.954$) | `[Pending Manual Run]` | PENDING |
| Interval 3 | Low ($-1$) | High ($+1$) | Positive ($\approx +0.954$) | `[Pending Manual Run]` | PENDING |
| Interval 4 | High ($+1$) | High ($+1$) | Negative ($\approx -0.954$) | `[Pending Manual Run]` | PENDING |

---

## 4. Current Verification Status

- **Status:** `PENDING MANUAL QCADESIGNER VERIFICATION`
- **Integrity Note:** Validated by automated QCADesigner load test. Manual waveform evaluation pending.
