# QCA XOR Gate: Truth Table & Intermediate Polarization Mapping

## 1. Full Functional Truth Table

| State # | Input $A$ | Input $B$ | Intermediate $A + B$ (`AvB`) | Intermediate $A \cdot B$ (`a^b`) | Inverted $\overline{A \cdot B}$ | Output $A \oplus B$ (`xor`) | Output Polarization $P_{\text{xor}}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `0` | `0` | `0` | `0` | `1` | **`0`** | $\approx -1.00$ |
| 2 | `0` | `1` | `1` | `0` | `1` | **`1`** | $\approx +1.00$ |
| 3 | `1` | `0` | `1` | `0` | `1` | **`1`** | $\approx +1.00$ |
| 4 | `1` | `1` | `1` | `1` | `0` | **`0`** | $\approx -1.00$ |

---

## 2. Recombination Majority Evaluation

For each input combination, the output stage evaluates:
$$Y = M( (A + B),\ \overline{A \cdot B},\ 0 )$$

1. **State 1 $(A=0, B=0)$:**
   $$(A+B) = 0, \quad \overline{A \cdot B} = 1, \quad C = 0 \implies M(0, 1, 0) = 0$$
2. **State 2 $(A=0, B=1)$:**
   $$(A+B) = 1, \quad \overline{A \cdot B} = 1, \quad C = 0 \implies M(1, 1, 0) = 1$$
3. **State 3 $(A=1, B=0)$:**
   $$(A+B) = 1, \quad \overline{A \cdot B} = 1, \quad C = 0 \implies M(1, 1, 0) = 1$$
4. **State 4 $(A=1, B=1)$:**
   $$(A+B) = 1, \quad \overline{A \cdot B} = 0, \quad C = 0 \implies M(1, 0, 0) = 0$$

All four Boolean combinations match the canonical XOR specification.

---

## 3. Waveform Verification Criteria

When simulated under QCADesigner:
- Output trace `xor` must transition high ($\ge +0.80$ polarization) exclusively during the two intermediate states $(0, 1)$ and $(1, 0)$.
- Output trace `xor` must remain low ($\le -0.80$ polarization) during the identical input states $(0, 0)$ and $(1, 1)$.
- Because the signal propagates across 4 clock zones (Clock 0 $\to$ Clock 3), the valid output waveform exhibits a latency offset of 1 full clock cycle relative to the input application.
