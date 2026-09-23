# QCA NOR Gate: Truth Table & Polarization Mapping

## 1. Boolean & Physical State Truth Table

| State # | Input $A$ (Logic) | Input $B$ (Logic) | Internal $A + B$ | Internal $P_{A+B}$ | Output $Y$ (Logic) | Output Polarization $P_Y$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `0` | `0` | `0` | $-1.00$ | **`1`** | $\approx +1.00$ |
| 2 | `0` | `1` | `1` | $+1.00$ | **`0`** | $\approx -1.00$ |
| 3 | `1` | `0` | `1` | $+1.00$ | **`0`** | $\approx -1.00$ |
| 4 | `1` | `1` | `1` | $+1.00$ | **`0`** | $\approx -1.00$ |

---

## 2. Universal Logic Significance

Alongside the NAND gate, the NOR gate represents a complete set of Boolean operators in digital logic. Constructing and simulating a viable NOR gate in QCA guarantees universal functional completeness using Majority-based nano-devices.

---

## 3. Waveform Verification Criteria

In QCADesigner simulation:
- Signal $A$ toggles between $-1.00$ and $+1.00$.
- Signal $B$ toggles between $-1.00$ and $+1.00$ at half the frequency of $A$.
- Output $Y$ is high (positive polarization, $\approx +0.954$) exclusively during the single quadrant where both $A$ and $B$ are low, and drops to low (negative polarization, $\approx -0.954$) for the other three quadrants.
