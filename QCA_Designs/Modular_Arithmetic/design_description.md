# Architectural and Mathematical Design Description: QCA Modular Adder

## 1. Mathematical Foundation of Modular Arithmetic in Homomorphic Encryption

Homomorphic Encryption (HE) schemes depend fundamentally on arithmetic over finite algebraic structures:
- **Integer Rings $\mathbb{Z}_N$**: Paillier cryptosystem performs homomorphic addition via modular multiplication in $\mathbb{Z}_{n^2}^*$, mapping to plaintext addition in $\mathbb{Z}_n$:
  $$\mathcal{D}(c_1 \cdot c_2 \pmod{n^2}) = (m_1 + m_2) \pmod n$$
- **Polynomial Quotient Rings $\mathcal{R}_q = \mathbb{Z}_q[X]/(X^N + 1)$**: Modern fully homomorphic schemes (BFV, BGV, CKKS) represent ciphertexts as high-degree polynomials where all coefficient additions and multiplications are evaluated modulo an integer modulus $q$.
- **Learning With Errors (LWE / Ring-LWE)**: Noise growth during homomorphic evaluations requires periodic modulus switching, bootstrapping, and modular rounding operations.

In modern hardware accelerators for HE, large moduli (e.g., 60-bit or 128-bit words) are mapped into parallel channels via Residue Number Systems (RNS) using the Chinese Remainder Theorem (CRT). At the lowest hardware level, each channel requires efficient modular adders and multipliers.

---

## 2. Modular Addition Logic Formulation

For two inputs $A, B \in \{0, 1, \dots, N-1\}$:
$$R = (A + B) \pmod N$$

### 2.1 Power-of-Two Modulus ($N = 2^k$)
When the modulus is an exact power of two ($N = 2^k$, here $k = 2, N = 4$):
1. The full integer sum evaluates as:
   $$S = A + B \in [0, 2(N-1)] = [0, 6]$$
2. In binary representation, $S$ requires $k + 1 = 3$ bits: $(S_2, S_1, S_0)_2$.
3. The residue modulo $2^k$ is simply the truncation to the lower $k$ bits:
   $$R = S \pmod{2^k} = (S_1, S_0)_2$$
4. The high bit represents the integer quotient / modular wrap-around indicator:
   $$Q = S_2 = \left\lfloor \frac{A + B}{2^k} \right\rfloor \in \{0, 1\}$$
5. Thus:
   $$A + B = 2^k \cdot Q + R = 4 \cdot Q + (2 R_1 + R_0)$$

### 2.2 Arbitrary Modulus ($N < 2^k$) Architecture Comparison
For general non-power-of-two moduli (such as $N = 3$):
A modular adder incorporates:
1. Primary addition: $S = A + B$.
2. Constant subtraction: $D = S - N = S + \overline{N} + 1$.
3. Modular reduction multiplexer:
   $$R = \begin{cases} S & \text{if } S < N \ (C_{borrow} = 0) \\ D & \text{if } S \ge N \ (C_{borrow} = 1) \end{cases}$$
The power-of-two implementation represents the most area-efficient and high-speed primitive in QCA because the modular reduction occurs natively through bit-slice boundaries without requiring comparison and subtraction sub-blocks.

---

## 3. QCA Circuit Partitioning and Cell Layout

The 2-bit Modular Adder layout in `Modular_Adder.qca` is organized into two pipelined stages:

```
[Inputs A0, B0] ---> [Stage 0: Half Adder / FA0] --- Carry C1 ---> [Stage 1: FA1] ---> [Outputs R1, Q]
                              |                                                           ^
                              +-------- Delay Line (y = 340 nm) -------------------------+
                                                                                          |
                                                                                    [Output R0]
```

### Stage 0: LSB Slice ($x \in [0, 360]\text{ nm}$)
- **Cell Count**: 73 cells
- **Inputs**: $A_0$ at $(60, 100)$, $B_0$ at $(60, 140)$, and $C_{in0}$ at $(60, 220)$ configured as a `FIXED` cell with polarization $P = -1.0$ (Logic 0).
- **Majority Voters**:
  - $M_{0,1}$ centered at $(180, 140)$ computes $C_1 = M(A_0, B_0, 0) = A_0 \cdot B_0$.
  - $M_{0,2}$ centered at $(180, 220)$ computes $M(A_0, B_0, 1)$.
  - $M_{0,3}$ centered at $(300, 240)$ evaluates the sum:
    $$R_0 = M(\overline{C_1}, M_{0,2}, 0) = A_0 \oplus B_0$$
- **Carry Out**: Propagated via horizontal wire $(240, 120) \to (340, 120)$ into inter-stage ripple interface $(360, 120) \to (380, 220)$.

### Synchronization Corridor ($y = 340\text{ nm}$)
- To ensure all primary outputs ($R_0, R_1, Q$) are valid simultaneously at Clock Zone 3 of the final cycle, $R_0$ is routed downward from $(360, 240)$ to $(360, 340)$ and horizontally across 20 intermediate cells.
- The delay line traverses Clock Zones 3 $\to$ 0 $\to$ 1 $\to$ 2 $\to$ 3, matching the exact clock phase progression of Stage 1.

### Stage 1: MSB Slice ($x \in [340, 700]\text{ nm}$)
- **Cell Count**: 84 cells
- **Inputs**: $A_1$ at $(400, 100)$, $B_1$ at $(400, 140)$, and incoming ripple carry $C_1$ at $(400, 220)$.
- **Majority Voters**:
  - $M_{1,1}$ centered at $(520, 140)$ evaluates the modular overflow / quotient carry:
    $$Q = C_2 = M(A_1, B_1, C_1)$$
  - $M_{1,2}$ centered at $(520, 220)$ evaluates $M(A_1, B_1, \overline{C_1})$.
  - $M_{1,3}$ centered at $(640, 240)$ evaluates the residue MSB:
    $$R_1 = M(\overline{C_2}, M_{1,2}, C_1) = A_1 \oplus B_1 \oplus C_1$$
- **Primary Outputs**:
  - $Q$ at $(700, 120)$ (Yellow output cell, Clock 3)
  - $R_1$ at $(700, 240)$ (Yellow output cell, Clock 3)
  - $R_0$ at $(700, 340)$ (Yellow output cell, Clock 3)

---

## 4. Clocking and Latency Analysis

QCA circuits require a 4-phase clocking mechanism (Switch, Hold, Release, Relax) to control the tunneling barrier and direct data propagation:
- **Stage 0 Latency**: 4 clock zones (1.0 clock cycle: Zones 0, 1, 2, 3).
- **Stage 1 Latency**: 4 clock zones (1.0 clock cycle: Zones 0, 1, 2, 3).
- **Total Latency**: 2.0 clock cycles (8 clock phases).
- Because the pipeline registers information in polarized cells during the Hold phase, a new pair of 2-bit operands can be injected every clock cycle, achieving maximum pipelined throughput.
