# QCA AND Gate: Simulation Notes & Verification Protocol

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
2. Select **File $\to$ Open** and navigate to:
   `c:\Users\sekhm\Desktop\HE-QCA-Project\QCA_Designs\AND\AND.qca`
3. Verify that the 5 cells are visible:
   - Input cell `A` (Blue, left)
   - Input cell `B` (Blue, top)
   - Fixed cell `-1.00` (Orange, bottom)
   - Center cell (Green, middle)
   - Output cell `Y` (Yellow, right)
4. Navigate to **Simulation $\to$ Simulation Engine Setup**.
5. Select **Bistable Approximation** and confirm the parameters match Section 1 above.
6. Click **Start Simulation** (or press the simulation icon / shortcut).
7. Inspect the generated waveform viewer:
   - Trace 1 (`B`): Square wave.
   - Trace 2 (`A`): Square wave at twice the frequency of `B`.
   - Trace 3 (`Y`): Evaluated output polarization.

---

## 3. Waveform Verification Checklist

| Time Interval | Input $A$ | Input $B$ | Expected $Y$ Polarization | Observed $Y$ Polarization | Verification |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Interval 1 | Low ($-1$) | Low ($-1$) | Negative ($\approx -0.954$) | `[Pending Manual Run]` | PENDING |
| Interval 2 | High ($+1$) | Low ($-1$) | Negative ($\approx -0.954$) | `[Pending Manual Run]` | PENDING |
| Interval 3 | Low ($-1$) | High ($+1$) | Negative ($\approx -0.954$) | `[Pending Manual Run]` | PENDING |
| Interval 4 | High ($+1$) | High ($+1$) | Positive ($\approx +0.954$) | `[Pending Manual Run]` | PENDING |

---

## 4. Current Verification Status

- **Status:** `PENDING MANUAL QCADESIGNER VERIFICATION`
- **Integrity Note:** Automated loading test confirms valid `.qca` file geometry and schema. Visual waveform confirmation in the GUI will mark this test verified upon execution.
