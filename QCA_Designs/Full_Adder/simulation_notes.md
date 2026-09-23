# QCA Full Adder: Simulation Notes & Verification Protocol

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
   `c:\Users\sekhm\Desktop\HE-QCA-Project\QCA_Designs\Full_Adder\Full_Adder.qca`
3. Verify the layout geometry:
   - 75 total cells arranged across 4 clock zones (Clock 0: Green, Clock 1: Magenta, Clock 2: Cyan, Clock 3: White).
   - Inputs: `A` at $(60, 100)$, `B` at $(60, 140)$, and `Cin` at $(60, 220)$ (Left, Blue).
   - Outputs: `Cout` at $(360, 120)$ and `SUM` at $(360, 240)$ (Right, Yellow).
4. Open **Simulation $\to$ Simulation Engine Setup**, verify Bistable Approximation parameters.
5. Click **Start Simulation**.
6. Inspect the resulting waveform traces:
   - Traces `Cin`, `B`, `A`: Binary excitation square waves generating all 8 combinations.
   - Trace `Cout`: Evaluated carry-out waveform.
   - Trace `SUM`: Evaluated sum waveform.

---

## 3. Waveform Verification Checklist (All 8 Vectors)

| Vector | $A$ | $B$ | $C_{in}$ | Expected `SUM` | Expected `Cout` | Observed `(Cout, SUM)` | Verification |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `0` | `0` | `0` | Low ($-1.00$) | Low ($-1.00$) | `[Pending Manual Run]` | PENDING |
| 2 | `0` | `0` | `1` | High ($+1.00$) | Low ($-1.00$) | `[Pending Manual Run]` | PENDING |
| 3 | `0` | `1` | `0` | High ($+1.00$) | Low ($-1.00$) | `[Pending Manual Run]` | PENDING |
| 4 | `0` | `1` | `1` | Low ($-1.00$) | High ($+1.00$) | `[Pending Manual Run]` | PENDING |
| 5 | `1` | `0` | `0` | High ($+1.00$) | Low ($-1.00$) | `[Pending Manual Run]` | PENDING |
| 6 | `1` | `0` | `1` | Low ($-1.00$) | High ($+1.00$) | `[Pending Manual Run]` | PENDING |
| 7 | `1` | `1` | `0` | Low ($-1.00$) | High ($+1.00$) | `[Pending Manual Run]` | PENDING |
| 8 | `1` | `1` | `1` | High ($+1.00$) | High ($+1.00$) | `[Pending Manual Run]` | PENDING |

---

## 4. Current Verification Status

- **Status:** `PENDING MANUAL QCADESIGNER VERIFICATION`
- **Integrity Note:** Layout syntax and file integrity verified by automated parser and QCADesigner loader. Waveforms pending manual GUI execution.
