# QCA 4-bit Ripple Carry Adder: Simulation Notes & Verification Protocol

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
   `c:\Users\sekhm\Desktop\HE-QCA-Project\QCA_Designs\Ripple_Carry_Adder_4bit\RCA_4bit.qca`
3. Inspect the multi-stage layout:
   - 315 total cells cascading across 4 pipelined Full Adder stages.
   - Inputs: $A_0 \dots A_3$, $B_0 \dots B_3$, and $C_{in}$ (Blue input cells).
   - Outputs: $S_0, S_1, S_2, S_3$ and $C_{out}$ (Yellow output pins).
4. Open **Simulation $\to$ Simulation Engine Setup**, verify Bistable Approximation parameters.
5. Click **Start Simulation**.
6. Inspect the resulting waveform traces for:
   - Input vectors $A[3:0], B[3:0], C_{in}$.
   - Sum outputs $S[3:0]$.
   - Final carry-out $C_{out}$.

---

## 3. Waveform Verification Checklist (Required Project Vectors)

| Test Case | Inputs ($A + B + C_{in}$) | Expected Result ($C_{out}, S_3 S_2 S_1 S_0$) | Observed Waveform States | Verification Status |
| :---: | :---: | :---: | :---: | :---: |
| 1 | $0000 + 0000 + 0$ | `0` and `0000` | `[Pending Manual Run]` | PENDING |
| 2 | $0001 + 0001 + 0$ | `0` and `0010` | `[Pending Manual Run]` | PENDING |
| 3 | $0011 + 0010 + 0$ | `0` and `0101` | `[Pending Manual Run]` | PENDING |
| 4 | $0101 + 0011 + 0$ | `0` and `1000` | `[Pending Manual Run]` | PENDING |
| 5 | $0111 + 0001 + 0$ | `0` and `1000` | `[Pending Manual Run]` | PENDING |
| 6 | $1010 + 0011 + 0$ | `0` and `1101` | `[Pending Manual Run]` | PENDING |
| 7 | $1111 + 0001 + 0$ | `1` and `0000` | `[Pending Manual Run]` | PENDING |
| 8 | $1111 + 1111 + 0$ | `1` and `1110` | `[Pending Manual Run]` | PENDING |

---

## 4. Current Verification Status

- **Status:** `PENDING MANUAL QCADESIGNER VERIFICATION`
- **Integrity Note:** Automated loading test confirms valid `.qca` file geometry and schema. Visual waveform confirmation in the GUI will mark this test verified upon execution.
