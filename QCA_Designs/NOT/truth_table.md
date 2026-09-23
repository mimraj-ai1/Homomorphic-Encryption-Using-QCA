# QCA NOT Gate: Truth Table & Polarization Inversion

## 1. Boolean & Physical State Truth Table

| State # | Input $A$ (Logic) | Input Polarization $P_A$ | Output $A'$ (Logic) | Output Polarization $P_{A'}$ | Coupling Mechanism |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `0` | $-1.00$ | **`1`** | $\approx +1.00$ | Diagonal anti-phase inversion |
| 2 | `1` | $+1.00$ | **`0`** | $\approx -1.00$ | Diagonal anti-phase inversion |

---

## 2. Inversion Operation

The QCA inverter satisfies the ideal negation property:
$$P_{\text{out}} = - P_{\text{in}}$$

- When $A = 0$ ($P = -1$), electrons in $A$ occupy diagonal dots (bottom-right and top-left). Diagonal repulsion shifts electrons in the displaced cell to top-right and bottom-left ($P = +1$, Logic 1).
- When $A = 1$ ($P = +1$), electrons in $A$ occupy top-right and bottom-left dots. Diagonal repulsion flips the displaced cell into bottom-right and top-left ($P = -1$, Logic 0).

---

## 3. Waveform Verification Criteria

In QCADesigner simulation:
- Input $A$ alternates between low ($-1.00$) and high ($+1.00$).
- Output $A'$ produces a strictly inverted waveform: high ($+0.954$) when $A$ is low, and low ($-0.954$) when $A$ is high.
