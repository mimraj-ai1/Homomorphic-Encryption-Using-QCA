# QCA 2×2 Binary Multiplier: Simulation Notes & Verification Protocol

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
   `c:\Users\sekhm\Desktop\HE-QCA-Project\QCA_Designs\Multiplier_2x2\Multiplier_2x2.qca`
3. Inspect the layout visually:
   - 91 cells arranged in pipelined stages (Colors: Green, Magenta, Cyan, White).
   - Inputs on the left: `A0`, `B0`, `A1`, `B1` (Blue pins).
   - Outputs on the right: `P0`, `P1`, `P2`, `P3` (Yellow pins).
4. Open **Simulation $\to$ Simulation Engine Setup**, verify Bistable Approximation parameters.
5. Click **Start Simulation**.
6. Inspect the resulting waveform traces:
   - Traces `A0, B0, A1, B1`: Excitation waveforms covering the 16 binary products.
   - Traces `P0, P1, P2, P3`: Evaluated product bits.

---

## 3. Waveform Verification Checklist

| Quadrant | Inputs ($A_1 A_0 \times B_1 B_0$) | Expected Product ($P_3 P_2 P_1 P_0$) | Observed Product | Verification Status |
| :---: | :---: | :---: | :---: | :---: |
| 1 | `00` $\times$ `00` | `0000` (0) | `[Pending Manual Run]` | PENDING |
| 2 | `01` $\times$ `01` | `0001` (1) | `[Pending Manual Run]` | PENDING |
| 3 | `01` $\times$ `10` | `0010` (2) | `[Pending Manual Run]` | PENDING |
| 4 | `10` $\times$ `10` | `0100` (4) | `[Pending Manual Run]` | PENDING |
| 5 | `10` $\times$ `11` | `0110` (6) | `[Pending Manual Run]` | PENDING |
| 6 | `11` $\times$ `11` | `1001` (9) | `[Pending Manual Run]` | PENDING |

---

## 4. Current Verification Status

- **Status:** `PENDING MANUAL QCADESIGNER VERIFICATION`
- **Integrity Note:** Automated loading test confirms valid `.qca` file geometry and schema. Visual waveform confirmation in the GUI will mark this test verified upon execution.
