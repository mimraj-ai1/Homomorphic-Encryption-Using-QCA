# QCA NOT Gate: Simulation Notes & Verification Protocol

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
   `c:\Users\sekhm\Desktop\HE-QCA-Project\QCA_Designs\NOT\NOT.qca`
3. Verify the layout geometry:
   - Input cell `A` at $(60.0, 80.0)$ (Blue)
   - Collinear wire cell at $(80.0, 80.0)$ (Green)
   - Displaced inverter cell at $(100.0, 100.0)$ (Green)
   - Output cell `A_inv` at $(120.0, 100.0)$ (Yellow)
4. Confirm Bistable Approximation parameters in **Simulation $\to$ Simulation Engine Setup**.
5. Click **Start Simulation**.
6. Inspect the resulting waveform traces for `A` and `A_inv`:
   - Trace 1 (`A`): Square wave alternating between $-1.00$ and $+1.00$.
   - Trace 2 (`A_inv`): Inverted square wave alternating between $+0.954$ and $-0.954$.

---

## 3. Waveform Verification Checklist

| Time Interval | Input $A$ | Expected $A_{\text{inv}}$ Polarization | Observed $A_{\text{inv}}$ Polarization | Verification |
| :---: | :---: | :---: | :---: | :---: |
| Interval 1 | Low ($-1.00$) | Positive ($\approx +0.954$) | `[Pending Manual Run]` | PENDING |
| Interval 2 | High ($+1.00$) | Negative ($\approx -0.954$) | `[Pending Manual Run]` | PENDING |

---

## 4. Current Verification Status

- **Status:** `PENDING MANUAL QCADESIGNER VERIFICATION`
- **Integrity Note:** Layout validated by QCADesigner parser. Waveform verification pending manual GUI run.
