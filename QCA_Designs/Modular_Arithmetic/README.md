# QCA Modular Arithmetic Design: 2-bit Modular Adder (Modulo 4)

## 1. Overview
Modular arithmetic forms the computational bedrock of modern cryptography, including public-key cryptosystems (RSA, ECC) and **Homomorphic Encryption (HE)** schemes such as Paillier, BFV, BGV, CKKS, and Learning With Errors (LWE / Ring-LWE). In these cryptosystems, ciphertexts and plaintexts reside within modular rings $\mathbb{Z}_q$ or polynomial quotient rings $\mathcal{R}_q = \mathbb{Z}_q[X] / (f(X))$.

This design presents a physically valid, pipelined **2-bit Modular Adder** implemented in Quantum-dot Cellular Automata (QCA). It evaluates modular addition:

$$R = (A + B) \pmod 4$$

along with the modular overflow / quotient carry flag:

$$Q = \left\lfloor \frac{A + B}{4} \right\rfloor$$

where $A, B \in \{0, 1, 2, 3\}$ represented as 2-bit unsigned binary integers $(A_1 A_0)_2$ and $(B_1 B_0)_2$.

---

## 2. Circuit Architecture and Logic Formulation

The circuit processes two 2-bit binary words $A = (A_1, A_0)_2$ and $B = (B_1, B_0)_2$:

### Stage 0 (Least Significant Bit Slice, $k=0$):
- **Inputs**: $A_0, B_0$, with initial carry $C_{in0} = 0$ permanently configured via a fixed polarization cell ($P = -1.0$).
- **Intermediate Signals**:
  $$M_{0,1} = M(A_0, B_0, C_{in0}) = A_0 \cdot B_0 = C_1 \quad (\text{Stage Carry})$$
  $$M_{0,2} = M(A_0, B_0, \overline{C_{in0}})$$
  $$R_0 = S_0 = M(\overline{C_1}, M_{0,2}, C_{in0}) = A_0 \oplus B_0$$
- **Synchronization**: The $R_0$ output is routed through a 4-phase delay line along a dedicated lower routing corridor ($y = 340\text{ nm}$) to synchronize its arrival with Stage 1 outputs at Clock Zone 3 of Cycle 1.

### Stage 1 (Most Significant Bit Slice, $k=1$):
- **Inputs**: $A_1, B_1$, and inter-stage ripple carry $C_1$ propagated from Stage 0.
- **Evaluation**:
  $$Q = C_2 = M(A_1, B_1, C_1) \quad (\text{Quotient / Modulo-4 Overflow})$$
  $$M_{1,2} = M(A_1, B_1, \overline{C_1})$$
  $$R_1 = S_1 = M(\overline{C_2}, M_{1,2}, C_1) = A_1 \oplus B_1 \oplus C_1$$
- **Primary Outputs**:
  - Residue MSB: $R_1$ (Clock Zone 3)
  - Residue LSB: $R_0$ (Clock Zone 3, pipelined)
  - Modulo-4 Quotient / Wrap flag: $Q$ (Clock Zone 3)

The total sum reconstructs as:
$$A + B = 4 \cdot Q + 2 \cdot R_1 + R_0$$
The residue in $\mathbb{Z}_4$ is given directly by $(R_1, R_0)_2$.

---

## 3. Physical Layout Metrics

Measured directly from `Modular_Adder.qca` using standard 18 nm × 18 nm cell dimensions with 20 nm center-to-center grid pitch:

| Metric | Measured Layout Value |
| :--- | :--- |
| **Total Cell Count** | 177 cells |
| **Active Clock Zones** | 4 zones (Zone 0, Zone 1, Zone 2, Zone 3) |
| **Circuit Latency** | 2.0 clock cycles (8 clock phases) |
| **Bounding Box Width** | 658.00 nm |
| **Bounding Box Height** | 258.00 nm |
| **Layout Footprint Area** | $0.169764\ \mu\text{m}^2$ ($169,764\text{ nm}^2$) |
| **Primary Inputs** | 4 ($A_0, B_0, A_1, B_1$) + 1 Fixed Bias Cell ($C_{in0} = -1.0$) |
| **Primary Outputs** | 3 ($R_0, R_1, Q$) |
| **QCADesigner Target** | Version 2.0.3 (Bistable Approximation Engine) |

---

## 4. Connection to Homomorphic Encryption (HE)

Homomorphic Encryption enables computation over ciphertexts without decryption:
1. **Lattice-Based Schemes (BFV, BGV, CKKS, TFHE)**: Operate over polynomial rings $\mathcal{R}_q = \mathbb{Z}_q[X]/(X^N + 1)$, where each coefficient addition and multiplication requires modulo-$q$ reduction.
2. **Residue Number Systems (RNS)**: Practical HE implementations decompose large moduli into small prime channels via the Chinese Remainder Theorem (CRT). Hardware slices of modular adders (such as this modulo-$2^k$ unit) execute the low-level coefficient accumulations in parallel.
3. **Paillier Cryptosystem**: Homomorphic addition corresponds to ciphertext multiplication modulo $n^2$:
   $$c_{sum} = c_1 \cdot c_2 \pmod{n^2}$$
   where the underlying plaintext addition $m_1 + m_2 \pmod n$ is reflected.

The QCA Modular Adder demonstrates how fundamental modular arithmetic operations are physically mapped onto nanometer-scale quantum-dot cellular automata substrates with zero Joule Joule-heating static power dissipation.
