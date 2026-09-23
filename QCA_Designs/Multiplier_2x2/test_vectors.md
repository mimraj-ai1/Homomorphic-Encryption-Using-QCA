# QCA 2×2 Binary Multiplier: Test Vectors & Verification Protocol

## 1. Selected Critical Test Vectors

| Test Case | Operands ($A \times B$) | Binary Inputs ($A_1 A_0 \times B_1 B_0$) | Expected Product ($P_3 P_2 P_1 P_0$) | Significance |
| :---: | :---: | :---: | :---: | :--- |
| **Zero Product** | $0 \times 0 = 0$ | `00` $\times$ `00` | `0000` | Quiescent state check |
| **Zero Factor** | $3 \times 0 = 0$ | `11` $\times$ `00` | `0000` | Multiplicand suppression |
| **Identity Factor** | $1 \times 1 = 1$ | `01` $\times$ `01` | `0001` | Single bit 0 propagation |
| **Linear Scale** | $2 \times 1 = 2$ | `10` $\times$ `01` | `0010` | Single bit 1 propagation |
| **Cross Product** | $3 \times 1 = 3$ | `11` $\times$ `01` | `0011` | Lower rail accumulation |
| **Square 2** | $2 \times 2 = 4$ | `10` $\times$ `10` | `0100` | Single bit 2 propagation |
| **Mixed Product** | $2 \times 3 = 6$ | `10` $\times$ `11` | `0110` | Partial product carry propagation |
| **Max Capacity** | $3 \times 3 = 9$ | `11` $\times$ `11` | `1001` | Full carry rippling to MSB ($P_3 = 1$) |

---

## 2. Multiplicative Homomorphism Hardware Significance

In Homomorphic Encryption schemes (such as unpadded RSA, BGV, BFV, and CKKS), ciphertext evaluation requires integer polynomial and modular multiplication:
$$\text{Eval}_{\text{mult}}(c_1, c_2) \propto c_1 \times c_2 \pmod q$$
The 2×2 binary multiplier represents the fundamental hardware building block for generating multi-bit array multipliers and Montgomery multiplication engines used in cryptographic coprocessors.
