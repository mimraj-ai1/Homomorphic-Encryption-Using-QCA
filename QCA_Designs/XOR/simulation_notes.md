# QCA XOR Gate: Simulation Notes & Verification Protocol

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
   `c:\Users\sekhm\Desktop\HE-QCA-Project\QCA_Designs\XOR\XOR.qca`
3. Verify the layout visually:
   - 91 total cells arranged in pipelined clock zones (colors: Green = Clock 0, Magenta = Clock 1, Cyan = Clock 2, White = Clock 3).
   - Inputs: `A` (left, blue) at $(60, 140)$ and `B` (left, blue) at $(120, 180)$.
   - Outputs: `xor` (right, yellow) at $(480, 300)$, along with debug taps `a^b` and `AvB`.
4. Open **Simulation $\to$ Simulation Engine Setup**, verify Bistable Approximation parameters.
5. Click **Start Simulation**.
6. Examine the generated waveform traces:
   - Trace `B`: Square wave.
   - Trace `A`: Square wave at higher frequency.
   - Trace `xor`: Primary evaluated XOR polarization waveform.
   - Trace `a^b`: Intermediate AND/Carry waveform.

---

## 3. Waveform Verification Checklist

| Time Interval | Input $A$ | Input $B$ | Expected `xor` State | Observed Polarization | Verification |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Quadrant 1 | Low ($0$) | Low ($0$) | Low ($-1.00$) | `[Pending Manual Run]` | PENDING |
| Quadrant 2 | High ($1$) | Low ($0$) | High ($+1.00$) | `[Pending Manual Run]` | PENDING |
| Quadrant 3 | Low ($0$) | High ($1$) | High ($+1.00$) | `[Pending Manual Run]` | PENDING |
| Quadrant 4 | High ($1$) | High ($1$) | Low ($-1.00$) | `[Pending Manual Run]` | PENDING |

---

## 4. Current Verification Status

- **Status:** `PENDING MANUAL QCADESIGNER VERIFICATION`
- **Integrity Note:** Automated loading test confirms valid `.qca` file geometry and schema. Visual waveform confirmation in the GUI will mark this test verified upon execution.
