# Truth Table: QCA 2-bit Modular Adder (Modulo 4)

## 1. Mathematical Formulation

The 2-bit Modular Adder evaluates addition in the ring of integers modulo 4 ($\mathbb{Z}_4$):

$$R = (A + B) \pmod 4$$

alongside the quotient (modular overflow / wrap flag):

$$Q = \left\lfloor \frac{A + B}{4} \right\rfloor$$

where $A, B \in \{0, 1, 2, 3\}$, represented as 2-bit binary words:
- $A = 2 A_1 + A_0$
- $B = 2 B_1 + B_0$
- Residue: $R = 2 R_1 + R_0$

The total integer sum reconstructs as:
$$A + B = 4 \cdot Q + R = 4 \cdot Q + 2 R_1 + R_0$$

---

## 2. Complete Modulo-4 Truth Table (16 Input Vectors)

| Row # | $A$ (dec) | $A_1$ | $A_0$ | $B$ (dec) | $B_1$ | $B_0$ | Integer Sum ($A+B$) | Quotient / Overflow ($Q$) | Residue ($R$) | $R_1$ (MSB) | $R_0$ (LSB) | Reconstruction $4Q + 2R_1 + R_0$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | $0 = 0$ |
| 2 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 1 | $1 = 1$ |
| 3 | 0 | 0 | 0 | 2 | 1 | 0 | 2 | 0 | 2 | 1 | 0 | $2 = 2$ |
| 4 | 0 | 0 | 0 | 3 | 1 | 1 | 3 | 0 | 3 | 1 | 1 | $3 = 3$ |
| 5 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | $1 = 1$ |
| 6 | 1 | 0 | 1 | 1 | 0 | 1 | 2 | 0 | 2 | 1 | 0 | $2 = 2$ |
| 7 | 1 | 0 | 1 | 2 | 1 | 0 | 3 | 0 | 3 | 1 | 1 | $3 = 3$ |
| 8 | 1 | 0 | 1 | 3 | 1 | 1 | 4 | 1 | 0 | 0 | 0 | $4 = 4$ |
| 9 | 2 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 2 | 1 | 0 | $2 = 2$ |
| 10 | 2 | 1 | 0 | 1 | 0 | 1 | 3 | 0 | 3 | 1 | 1 | $3 = 3$ |
| 11 | 2 | 1 | 0 | 2 | 1 | 0 | 4 | 1 | 0 | 0 | 0 | $4 = 4$ |
| 12 | 2 | 1 | 0 | 3 | 1 | 1 | 5 | 1 | 1 | 0 | 1 | $5 = 5$ |
| 13 | 3 | 1 | 1 | 0 | 0 | 0 | 3 | 0 | 3 | 1 | 1 | $3 = 3$ |
| 14 | 3 | 1 | 1 | 1 | 0 | 1 | 4 | 1 | 0 | 0 | 0 | $4 = 4$ |
| 15 | 3 | 1 | 1 | 2 | 1 | 0 | 5 | 1 | 1 | 0 | 1 | $5 = 5$ |
| 16 | 3 | 1 | 1 | 3 | 1 | 1 | 6 | 1 | 2 | 1 | 0 | $6 = 6$ |

---

## 3. Bit-Slice Logic Formulation

### Stage 0: LSB Addition ($A_0, B_0, C_{in0} = 0$)
- $C_1 = M(A_0, B_0, 0) = A_0 \cdot B_0$
- $R_0 = S_0 = M(\overline{C_1}, M(A_0, B_0, 1), 0) = A_0 \oplus B_0$
- $R_0$ is routed along an equalized 4-phase delay line to synchronize with Stage 1 outputs.

### Stage 1: MSB Addition with Carry ($A_1, B_1, C_1$)
- $Q = C_2 = M(A_1, B_1, C_1) = A_1 B_1 + C_1 (A_1 \oplus B_1)$ (Modulo-4 Overflow / Quotient)
- $R_1 = S_1 = M(\overline{C_2}, M(A_1, B_1, \overline{C_1}), C_1) = A_1 \oplus B_1 \oplus C_1$ (Residue MSB)

---

## 4. QCADesigner Polarization Values

| Logic Value | Nominal Cell Polarization ($P$) | Stable Potential Minimum |
| :---: | :---: | :---: |
| **Logic 0** | $-1.00$ | Lower diagonal electron localization |
| **Logic 1** | $+1.00$ | Upper diagonal electron localization |
| **Unpolarized / Null** | $0.00$ | Clock low (reset/relaxed phase) |
