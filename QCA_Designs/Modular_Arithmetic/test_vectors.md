# Test Vectors and Truth Table: QCA Modular Adder (Modulo 4)

## 1. Complete Input-Output Test Vectors

The 2-bit Modular Adder accepts two 2-bit unsigned operands $A = (A_1, A_0)_2$ and $B = (B_1, B_0)_2$ and produces the 2-bit residue $R = (R_1, R_0)_2 = (A + B) \pmod 4$ alongside the quotient / modular overflow bit $Q = \lfloor (A + B) / 4 \rfloor$.

| Vector # | $A$ (dec) | $A_1$ | $A_0$ | $B$ (dec) | $B_1$ | $B_0$ | Sum ($A+B$) | $Q$ (Quotient / Overflow) | $R$ (dec) | $R_1$ (MSB) | $R_0$ (LSB) | Verification Check |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **TV-01** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | $0 = 4(0) + 0$ OK |
| **TV-02** | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 1 | $1 = 4(0) + 1$ OK |
| **TV-03** | 0 | 0 | 0 | 2 | 1 | 0 | 2 | 0 | 2 | 1 | 0 | $2 = 4(0) + 2$ OK |
| **TV-04** | 0 | 0 | 0 | 3 | 1 | 1 | 3 | 0 | 3 | 1 | 1 | $3 = 4(0) + 3$ OK |
| **TV-05** | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | $1 = 4(0) + 1$ OK |
| **TV-06** | 1 | 0 | 1 | 1 | 0 | 1 | 2 | 0 | 2 | 1 | 0 | $2 = 4(0) + 2$ OK |
| **TV-07** | 1 | 0 | 1 | 2 | 1 | 0 | 3 | 0 | 3 | 1 | 1 | $3 = 4(0) + 3$ OK |
| **TV-08** | 1 | 0 | 1 | 3 | 1 | 1 | 4 | 1 | 0 | 0 | 0 | $4 = 4(1) + 0$ OK |
| **TV-09** | 2 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 2 | 1 | 0 | $2 = 4(0) + 2$ OK |
| **TV-10** | 2 | 1 | 0 | 1 | 0 | 1 | 3 | 0 | 3 | 1 | 1 | $3 = 4(0) + 3$ OK |
| **TV-11** | 2 | 1 | 0 | 2 | 1 | 0 | 4 | 1 | 0 | 0 | 0 | $4 = 4(1) + 0$ OK |
| **TV-12** | 2 | 1 | 0 | 3 | 1 | 1 | 5 | 1 | 1 | 0 | 1 | $5 = 4(1) + 1$ OK |
| **TV-13** | 3 | 1 | 1 | 0 | 0 | 0 | 3 | 0 | 3 | 1 | 1 | $3 = 4(0) + 3$ OK |
| **TV-14** | 3 | 1 | 1 | 1 | 0 | 1 | 4 | 1 | 0 | 0 | 0 | $4 = 4(1) + 0$ OK |
| **TV-15** | 3 | 1 | 1 | 2 | 1 | 0 | 5 | 1 | 1 | 0 | 1 | $5 = 4(1) + 1$ OK |
| **TV-16** | 3 | 1 | 1 | 3 | 1 | 1 | 6 | 1 | 2 | 1 | 0 | $6 = 4(1) + 2$ OK |

---

## 2. Polarization Signal Mapping

In QCADesigner 2.0.3:
- Logic 0 corresponds to cell polarization $P = -1.00$.
- Logic 1 corresponds to cell polarization $P = +1.00$.

| Input Polarization ($A_1, A_0, B_1, B_0$) | Expected Output Polarization ($Q, R_1, R_0$) | Resulting State |
| :---: | :---: | :---: |
| $(-1.0, -1.0, -1.0, -1.0)$ | $(-1.0, -1.0, -1.0)$ | $Q=0, R_1=0, R_0=0$ (Residue 0) |
| $(-1.0, +1.0, -1.0, +1.0)$ | $(-1.0, +1.0, -1.0)$ | $Q=0, R_1=1, R_0=0$ (Residue 2) |
| $(-1.0, +1.0, +1.0, +1.0)$ | $(+1.0, -1.0, -1.0)$ | $Q=1, R_1=0, R_0=0$ (Residue 0, Overflow 1) |
| $(+1.0, +1.0, +1.0, +1.0)$ | $(+1.0, +1.0, -1.0)$ | $Q=1, R_1=1, R_0=0$ (Residue 2, Overflow 1) |
