# QCA NAND Gate: Truth Table & Polarization Mapping

## 1. Boolean & Physical State Truth Table

| State # | Input $A$ (Logic) | Input $B$ (Logic) | Internal $A \cdot B$ | Internal $P_{AB}$ | Output $Y$ (Logic) | Output Polarization $P_Y$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `0` | `0` | `0` | $-1.00$ | **`1`** | $\approx +1.00$ |
| 2 | `0` | `1` | `0` | $-1.00$ | **`1`** | $\approx +1.00$ |
| 3 | `1` | `0` | `0` | $-1.00$ | **`1`** | $\approx +1.00$ |
| 4 | `1` | `1` | `1` | $+1.00$ | **`0`** | $\approx -1.00$ |

---

## 2. Universal Logic Significance

Because the NAND gate is a universal logic gate in classical Boolean algebra, having a functional, verified QCA NAND gate confirms that any arbitrary combinational logic circuit (including adders, multipliers, multiplexers, and modular arithmetic units) can theoretically be realized in QCA nanotechnology.

---

## 3. Waveform Verification Criteria

In QCADesigner simulation:
- Signal $A$ toggles between $-1.00$ and $+1.00$.
- Signal $B$ toggles between $-1.00$ and $+1.00$ at half the frequency of $A$.
- Output $Y$ remains high (positive polarization, $\approx +0.954$) for the first 3 quadrants and drops to low (negative polarization, $\approx -0.954$) only during the final quadrant where both $A$ and $B$ are simultaneously high.
