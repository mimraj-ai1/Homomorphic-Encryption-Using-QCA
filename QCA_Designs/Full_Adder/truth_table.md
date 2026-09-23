# QCA Full Adder: Truth Table & Arithmetic Verification

## 1. 3-Input Binary Addition Truth Table

| Vector # | $A$ | $B$ | $C_{in}$ | Integer Sum ($A + B + C_{in}$) | Output `Cout` | Output `SUM` | Binary State $(C_{out}, \text{SUM})$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `0` | `0` | `0` | 0 | **`0`** | **`0`** | `00` |
| 2 | `0` | `0` | `1` | 1 | **`0`** | **`1`** | `01` |
| 3 | `0` | `1` | `0` | 1 | **`0`** | **`1`** | `01` |
| 4 | `0` | `1` | `1` | 2 | **`1`** | **`0`** | `10` |
| 5 | `1` | `0` | `0` | 1 | **`0`** | **`1`** | `01` |
| 6 | `1` | `0` | `1` | 2 | **`1`** | **`0`** | `10` |
| 7 | `1` | `1` | `0` | 2 | **`1`** | **`0`** | `10` |
| 8 | `1` | `1` | `1` | 3 | **`1`** | **`1`** | `11` |

---

## 2. Stage-by-Stage Majority Evaluation

| Vector | $M_1 = C_{out}$ | $\overline{C_{in}}$ | $M_2 = M(A, B, \overline{C_{in}})$ | $\overline{M_1} = \overline{C_{out}}$ | $M_3 = M(\overline{M_1}, M_2, C_{in}) = \text{SUM}$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `000` | `0` | `1` | `0` | `1` | $M(1, 0, 0) = \mathbf{0}$ |
| `001` | `0` | `0` | `0` | `1` | $M(1, 0, 1) = \mathbf{1}$ |
| `010` | `0` | `1` | `1` | `1` | $M(1, 1, 0) = \mathbf{1}$ |
| `011` | `1` | `0` | `0` | `0` | $M(0, 0, 1) = \mathbf{0}$ |
| `100` | `0` | `1` | `1` | `1` | $M(1, 1, 0) = \mathbf{1}$ |
| `101` | `1` | `0` | `0` | `0` | $M(0, 0, 1) = \mathbf{0}$ |
| `110` | `1` | `1` | `1` | `0` | $M(0, 1, 0) = \mathbf{0}$ |
| `111` | `1` | `0` | `1` | `0` | $M(0, 1, 1) = \mathbf{1}$ |

---

## 3. Waveform Verification Criteria

In QCADesigner simulation across 12,800 samples:
- `Cout` transitions high exclusively for input combinations with two or more 1s (vectors 4, 6, 7, 8).
- `SUM` transitions high exclusively for input combinations with an odd number of 1s (vectors 2, 3, 5, 8).
- Both outputs emerge with a synchronized 1.0 clock cycle latency (Clock Zone 3).
