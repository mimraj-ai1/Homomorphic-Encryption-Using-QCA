# Truth Table & Carry Ripple Progression: 4-bit Ripple Carry Adder (RCA)

## 1. Functional Specification

A 4-bit Ripple Carry Adder accepts two 4-bit unsigned binary operands:
$$A = (A_3, A_2, A_1, A_0)_2, \quad B = (B_3, B_2, B_1, B_0)_2$$
and a single carry-in bit $C_{in} \in \{0, 1\}$. It computes the 4-bit sum:
$$S = (S_3, S_2, S_1, S_0)_2$$
and a carry-out bit $C_{out} \in \{0, 1\}$, satisfying the arithmetic identity:

$$A + B + C_{in} = 16 \cdot C_{out} + S = 16 \cdot C_{out} + \sum_{i=0}^3 S_i \cdot 2^i$$

Total possible input combinations: $2^4 \times 2^4 \times 2^1 = 16 \times 16 \times 2 = 512$ combinations.

---

## 2. Stage-by-Stage Bit Slice Truth Tables

The 4-bit RCA cascades four 1-bit Full Adders ($\text{FA}_0 \to \text{FA}_3$):

$$\text{FA}_0: (A_0, B_0, C_{in}) \longrightarrow S_0, C_1$$
$$\text{FA}_1: (A_1, B_1, C_1) \longrightarrow S_1, C_2$$
$$\text{FA}_2: (A_2, B_2, C_2) \longrightarrow S_2, C_3$$
$$\text{FA}_3: (A_3, B_3, C_3) \longrightarrow S_3, C_{out}$$

Each Full Adder stage $k \in \{0, 1, 2, 3\}$ evaluates:
$$C_{k+1} = M(A_k, B_k, C_k) = (A_k \cdot B_k) + (B_k \cdot C_k) + (A_k \cdot C_k)$$
$$S_k = A_k \oplus B_k \oplus C_k = M(\overline{C_{k+1}}, M(A_k, B_k, \overline{C_k}), C_k)$$

| $A_k$ | $B_k$ | $C_k$ | $C_{k+1}$ (Carry Out) | $S_k$ (Sum Bit) | Arithmetic Value ($2 C_{k+1} + S_k$) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 | 0 | $0 + 0 + 0 = 0$ |
| 0 | 0 | 1 | 0 | 1 | $0 + 0 + 1 = 1$ |
| 0 | 1 | 0 | 0 | 1 | $0 + 1 + 0 = 1$ |
| 0 | 1 | 1 | 1 | 0 | $0 + 1 + 1 = 2$ |
| 1 | 0 | 0 | 0 | 1 | $1 + 0 + 0 = 1$ |
| 1 | 0 | 1 | 1 | 0 | $1 + 0 + 1 = 2$ |
| 1 | 1 | 0 | 1 | 0 | $1 + 1 + 0 = 2$ |
| 1 | 1 | 1 | 1 | 1 | $1 + 1 + 1 = 3$ |

---

## 3. Representative 4-bit Arithmetic Truth Table

Below are representative, critical, and boundary input vectors covering all key operational regimes with both $C_{in} = 0$ and $C_{in} = 1$:

| # | $A$ (dec) | $A_3 A_2 A_1 A_0$ | $B$ (dec) | $B_3 B_2 B_1 B_0$ | $C_{in}$ | $C_1$ | $C_2$ | $C_3$ | $C_{out}$ | $S_3 S_2 S_1 S_0$ | $S$ (dec) | Total ($16 C_{out} + S$) | Verification |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| 1 | 0 | `0000` | 0 | `0000` | 0 | 0 | 0 | 0 | 0 | `0000` | 0 | 0 | $0+0+0 = 0$ OK |
| 2 | 0 | `0000` | 0 | `0000` | 1 | 0 | 0 | 0 | 0 | `0001` | 1 | 1 | $0+0+1 = 1$ OK |
| 3 | 1 | `0001` | 1 | `0001` | 0 | 1 | 0 | 0 | 0 | `0010` | 2 | 2 | $1+1+0 = 2$ OK |
| 4 | 1 | `0001` | 1 | `0001` | 1 | 1 | 0 | 0 | 0 | `0011` | 3 | 3 | $1+1+1 = 3$ OK |
| 5 | 3 | `0011` | 2 | `0010` | 0 | 0 | 1 | 0 | 0 | `0101` | 5 | 5 | $3+2+0 = 5$ OK |
| 6 | 3 | `0011` | 2 | `0010` | 1 | 1 | 1 | 0 | 0 | `0110` | 6 | 6 | $3+2+1 = 6$ OK |
| 7 | 5 | `0101` | 3 | `0011` | 0 | 1 | 0 | 1 | 0 | `1000` | 8 | 8 | $5+3+0 = 8$ OK |
| 8 | 7 | `0111` | 1 | `0001` | 0 | 1 | 1 | 1 | 0 | `1000` | 8 | 8 | $7+1+0 = 8$ OK |
| 9 | 10 | `1010` | 3 | `0011` | 0 | 0 | 1 | 0 | 0 | `1101` | 13 | 13 | $10+3+0 = 13$ OK |
| 10 | 10 | `1010` | 5 | `0101` | 1 | 0 | 1 | 0 | 1 | `0000` | 0 | 16 | $10+5+1 = 16$ OK |
| 11 | 15 | `1111` | 0 | `0000` | 1 | 1 | 1 | 1 | 1 | `0000` | 0 | 16 | $15+0+1 = 16$ OK |
| 12 | 15 | `1111` | 1 | `0001` | 0 | 1 | 1 | 1 | 1 | `0000` | 0 | 16 | $15+1+0 = 16$ OK |
| 13 | 15 | `1111` | 1 | `0001` | 1 | 1 | 1 | 1 | 1 | `0001` | 1 | 17 | $15+1+1 = 17$ OK |
| 14 | 15 | `1111` | 15 | `1111` | 0 | 1 | 1 | 1 | 1 | `1110` | 14 | 30 | $15+15+0 = 30$ OK |
| 15 | 15 | `1111` | 15 | `1111` | 1 | 1 | 1 | 1 | 1 | `1111` | 15 | 31 | $15+15+1 = 31$ OK |

---

## 4. Complete Carry Ripple Analysis (Vector 12: $1111_2 + 0001_2 + 0$)

1. **Stage 0 ($\text{FA}_0$):**
   - Inputs: $A_0 = 1, B_0 = 1, C_{in} = 0$.
   - Intermediate Carry: $C_1 = M(1, 1, 0) = 1$.
   - Sum bit: $S_0 = 1 \oplus 1 \oplus 0 = 0$.
2. **Stage 1 ($\text{FA}_1$):**
   - Inputs: $A_1 = 1, B_1 = 0, C_1 = 1$.
   - Intermediate Carry: $C_2 = M(1, 0, 1) = 1$.
   - Sum bit: $S_1 = 1 \oplus 0 \oplus 1 = 0$.
3. **Stage 2 ($\text{FA}_2$):**
   - Inputs: $A_2 = 1, B_2 = 0, C_2 = 1$.
   - Intermediate Carry: $C_3 = M(1, 0, 1) = 1$.
   - Sum bit: $S_2 = 1 \oplus 0 \oplus 1 = 0$.
4. **Stage 3 ($\text{FA}_3$):**
   - Inputs: $A_3 = 1, B_3 = 0, C_3 = 1$.
   - Output Carry: $C_{out} = M(1, 0, 1) = 1$.
   - Sum bit: $S_3 = 1 \oplus 0 \oplus 1 = 0$.

Total result: $C_{out} = 1, S = 0000_2 \implies 10000_2 = 16_{10}$. The ripple carry completes through all 4 stages, propagating across 16 clock zones (4 clock cycles).
