# QCA Half Adder: Truth Table & Arithmetic Verification

## 1. Binary Addition & State Truth Table

| State # | Input $A$ | Input $B$ | Integer Sum ($A + B$) | Output `SUM` ($A \oplus B$) | Output `CARRY` ($A \cdot B$) | Output State $(C, S)$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `0` | `0` | 0 | **`0`** | **`0`** | `00` |
| 2 | `0` | `1` | 1 | **`1`** | **`0`** | `01` |
| 3 | `1` | `0` | 1 | **`1`** | **`0`** | `01` |
| 4 | `1` | `1` | 2 | **`0`** | **`1`** | `10` |

---

## 2. Arithmetic Mapping & Polarization States

- **Case 1 ($0 + 0 = 0$):**
  - Inputs: $P_A = -1.00$, $P_B = -1.00$
  - `CARRY` evaluates to logic `0` ($P \approx -1.00$)
  - `SUM` evaluates to logic `0` ($P \approx -1.00$)
- **Case 2 ($0 + 1 = 1$):**
  - Inputs: $P_A = -1.00$, $P_B = +1.00$
  - `CARRY` evaluates to logic `0` ($P \approx -1.00$)
  - `SUM` evaluates to logic `1` ($P \approx +1.00$)
- **Case 3 ($1 + 0 = 1$):**
  - Inputs: $P_A = +1.00$, $P_B = -1.00$
  - `CARRY` evaluates to logic `0` ($P \approx -1.00$)
  - `SUM` evaluates to logic `1` ($P \approx +1.00$)
- **Case 4 ($1 + 1 = 2_{10} = 10_2$):**
  - Inputs: $P_A = +1.00$, $P_B = +1.00$
  - `CARRY` evaluates to logic `1` ($P \approx +1.00$)
  - `SUM` evaluates to logic `0` ($P \approx -1.00$)

---

## 3. Waveform Verification Criteria

In QCADesigner simulation across 12,800 samples:
- `SUM` waveform must be high only during intermediate quadrants ($01$ and $10$).
- `CARRY` waveform must be low for the first 3 quadrants and transition to high exclusively during the 4th quadrant ($11$).
- Both outputs exhibit 1 full clock cycle latency matching the 4 pipelined clock zones.
