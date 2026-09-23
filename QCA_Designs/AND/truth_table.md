# QCA AND Gate: Truth Table & Polarization Mapping

## 1. Boolean & Physical State Truth Table

| State # | Input $A$ (Logic) | Input $B$ (Logic) | Polarization $P_A$ | Polarization $P_B$ | Fixed Input $C$ | Output $Y$ (Logic) | Output Polarization $P_Y$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `0` | `0` | $-1.00$ | $-1.00$ | $-1.00$ | **`0`** | $\approx -1.00$ |
| 2 | `0` | `1` | $-1.00$ | $+1.00$ | $-1.00$ | **`0`** | $\approx -1.00$ |
| 3 | `1` | `0` | $+1.00$ | $-1.00$ | $-1.00$ | **`0`** | $\approx -1.00$ |
| 4 | `1` | `1` | $+1.00$ | $+1.00$ | $-1.00$ | **`1`** | $\approx +1.00$ |

---

## 2. Majority Voter Mapping

The evaluation follows:
$$Y = M(A, B, C) \quad \text{where } C = -1.00$$

1. For $(A, B) = (0, 0)$: Majority $(-1, -1, -1) \to -1$ (Logic 0)
2. For $(A, B) = (0, 1)$: Majority $(-1, +1, -1) \to -1$ (Logic 0)
3. For $(A, B) = (1, 0)$: Majority $(+1, -1, -1) \to -1$ (Logic 0)
4. For $(A, B) = (1, 1)$: Majority $(+1, +1, -1) \to +1$ (Logic 1)

---

## 3. Waveform Verification Criteria

In QCADesigner simulation:
- Signal $A$ toggles at period $T_A$.
- Signal $B$ toggles at period $T_B = 2 T_A$.
- Output $Y$ remains in the low state (polarization negative, approximately $-0.95$ to $-1.00$) for the first 3 quadrants and transitions to the high state (polarization positive, approximately $+0.95$ to $+1.00$) only during the final quadrant where both $A$ and $B$ are high.
