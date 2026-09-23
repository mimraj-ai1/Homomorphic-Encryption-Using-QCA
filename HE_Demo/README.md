# Homomorphic Encryption (HE) Demonstration

## 1. Overview and Theoretical Foundation

**Homomorphic Encryption (HE)** is a cryptographic paradigm that permits computation directly over encrypted data without requiring access to secret decryption keys. The result of a homomorphic operation is an encrypted ciphertext whose underlying plaintext matches the output of the corresponding operation performed on the unencrypted data:

$$\mathcal{D}(\mathcal{E}(m_1) \odot \mathcal{E}(m_2)) = m_1 \oplus m_2$$

Cryptographic schemes are classified based on the algebraic operations they support:
1. **Partially Homomorphic Encryption (PHE)**: Supports a single operation (either addition or multiplication) for an unlimited number of operations (e.g., Paillier for addition, Unpadded RSA / ElGamal for multiplication).
2. **Somewhat Homomorphic Encryption (SHE)**: Supports both addition and a limited depth of multiplications before noise drowns the signal (e.g., DGHV, initial Brakerski-Vaikuntanathan schemes).
3. **Fully Homomorphic Encryption (FHE)**: Supports arbitrary circuits of unlimited depth through bootstrapping noise reduction algorithms (e.g., Gentry, BGV, BFV, CKKS, TFHE).

This software module provides a mathematically rigorous, self-contained educational implementation of **Paillier Additive Homomorphism** and **RSA Multiplicative Homomorphism**, accompanied by an architectural mapping to the QCA nanotechnological hardware circuits designed in this project.

---

## 2. Mathematical Formulations & Proofs of Correctness

### 2.1 Paillier Additive Homomorphism

#### Key Generation:
1. Select two large independent prime numbers $p$ and $q$.
2. Compute public modulus $n = p \cdot q$ and $n^2$.
3. Compute private parameter $\lambda = \text{lcm}(p-1, q-1)$.
4. Select base generator $g = n + 1 \in \mathbb{Z}_{n^2}^*$.
5. Compute modular inverse $\mu = \left(\frac{g^\lambda \bmod n^2 - 1}{n}\right)^{-1} \pmod n = \lambda^{-1} \pmod n$.
6. **Public Key**: $(n, g)$, **Private Key**: $(\lambda, \mu, n)$.

#### Encryption:
For plaintext message $m \in \mathbb{Z}_n$ and random blinding factor $r \in \mathbb{Z}_n^*$:
$$c = g^m \cdot r^n \pmod{n^2}$$

#### Decryption:
$$m = L(c^\lambda \bmod n^2) \cdot \mu \pmod n, \quad \text{where } L(u) = \frac{u - 1}{n}$$

#### Proof of Additive Homomorphism:
Given two ciphertexts $c_1 = g^{m_1} r_1^n \pmod{n^2}$ and $c_2 = g^{m_2} r_2^n \pmod{n^2}$:
$$c_{sum} = c_1 \cdot c_2 \pmod{n^2} = (g^{m_1} r_1^n)(g^{m_2} r_2^n) = g^{m_1 + m_2} (r_1 r_2)^n \pmod{n^2}$$
Since $(r_1 r_2) \in \mathbb{Z}_n^*$, $c_{sum}$ is a strictly valid Paillier encryption of $(m_1 + m_2) \pmod n$:
$$\mathcal{D}(c_1 \cdot c_2 \pmod{n^2}) = (m_1 + m_2) \pmod n$$

#### Proof of Scalar Multiplication:
Given ciphertext $c_1$ and integer scalar $k$:
$$c_{scale} = c_1^k \pmod{n^2} = (g^{m_1} r_1^n)^k = g^{k \cdot m_1} (r_1^k)^n \pmod{n^2}$$
$$\mathcal{D}(c_1^k \pmod{n^2}) = (k \cdot m_1) \pmod n$$

---

### 2.2 Multiplicative Homomorphism (Unpadded RSA)

#### Key Generation:
1. $N = p \cdot q$, Euler totient $\phi(N) = (p - 1)(q - 1)$.
2. Public exponent $e = 65537$, private exponent $d = e^{-1} \pmod{\phi(N)}$.
3. **Public Key**: $(e, N)$, **Private Key**: $(d, N)$.

#### Encryption:
$$c = m^e \pmod N$$

#### Proof of Multiplicative Homomorphism:
$$c_{prod} = c_1 \cdot c_2 \pmod N = (m_1^e)(m_2^e) = (m_1 \cdot m_2)^e \pmod N$$
$$\mathcal{D}(c_{prod}) = (c_{prod})^d = ((m_1 \cdot m_2)^e)^d \equiv (m_1 \cdot m_2) \pmod N$$

---

## 3. Conceptual Bridge: Mapping HE Computation to QCA Hardware

A critical academic distinction must be maintained:
> **Academic Integrity Principle**: Quantum-dot Cellular Automata (QCA) is NOT an encryption algorithm, nor does QCADesigner execute Python scripts. QCA is a post-CMOS nanotechnology hardware paradigm designed to execute fundamental digital logic operations at nanometer scale with near-zero static power dissipation.

The connection between Homomorphic Encryption and QCA operates across a six-level architectural hierarchy:

```
[Layer 6: Cryptographic Application]    Cloud Private Query / Encrypted AI / Secure Voting
               │
               ▼
[Layer 5: Homomorphic Scheme]           Paillier / BFV / BGV / CKKS / TFHE
               │                        Evaluates: c_sum = (c1 * c2) mod n^2
               ▼
[Layer 4: Residue / Modular Reduction]  Chinese Remainder Theorem (CRT) / RNS Decomposition
               │                        Decomposes large integers into small modular channels
               ▼
[Layer 3: Binary Word Arithmetic]       4-bit / 8-bit / 64-bit Binary Multipliers & Adders
               │                        Evaluates partial products & carry propagation
               ▼
[Layer 2: QCA Arithmetic Modules]       QCA 2x2 Multiplier (Multiplier_2x2.qca)
               │                        QCA 4-bit Ripple Carry Adder (RCA_4bit.qca)
               │                        QCA 2-bit Modular Adder (Modular_Adder.qca)
               ▼
[Layer 1: QCA Physical Nanostructures]  4-dot Quantum Cells (18x18 nm), Coulombic Interactions,
                                        3-input Majority Voters, 4-phase Tunneling Clock
```

### Hardware Mapping Breakdown:
1. **Partial Product Evaluation**: In HE ciphertext multiplication, 2-bit binary slices of high-dimensional words are multiplied via arrays of **QCA 2x2 Multipliers** (`Multiplier_2x2.qca`), evaluating 4 partial products $PP_0 = A_0 B_0, PP_1 = A_1 B_0, PP_2 = A_0 B_1, PP_3 = A_1 B_1$.
2. **Carry Ripple Accumulation**: Partial products and ciphertext words are accumulated across multi-stage **QCA Ripple Carry Adders** (`RCA_4bit.qca`) and **Full Adders** (`Full_Adder.qca`).
3. **Modular Residue Reduction**: Intermediate accumulations are reduced modulo channels via **QCA Modular Adders** (`Modular_Adder.qca`), evaluating $(A + B) \pmod 4$ with overflow tracking.
4. **Physical Realization**: All logic executes through majority-voter logic $M(A, B, C)$ and diagonal inverter coupling without conventional transistor switches or dynamic charge transfer.

---

## 4. How to Run the Demonstration

Execute the standalone verification script from the project root:
```bash
python HE_Demo/test.py
```

Expected terminal output verifies all three homomorphic arithmetic operations:
- `c_add = (c1 * c2) mod n^2` $\implies$ Decrypt yields $(m_1 + m_2) \pmod n$ [PASSED]
- `c_scale = (c1 ^ k) mod n^2` $\implies$ Decrypt yields $(k \cdot m_1) \pmod n$ [PASSED]
- `c_sub = (c2 * c1^-1) mod n^2` $\implies$ Decrypt yields $(m_2 - m_1) \pmod n$ [PASSED]
- `c_prod = (c_a * c_b) mod N` $\implies$ Decrypt yields $(m_a \cdot m_b) \pmod N$ [PASSED]
- Full hardware decomposition trace into QCA building blocks [PASSED]
