"""
Generate Phase 6: 2x2 Binary Multiplier QCA layout for QCADesigner 2.0.3.
Computes:
  A = (A1 A0)_2, B = (B1 B0)_2
  PP0 = A0 AND B0  (Bit 0)
  PP1 = A1 AND B0
  PP2 = A0 AND B1
  PP3 = A1 AND B1
  HA1(PP1, PP2) -> P1 (Bit 1), C1
  HA2(PP3, C1)  -> P2 (Bit 2), P3 (Bit 3)
  Output: P3 P2 P1 P0
"""

import os
from qca_circuit_builder import QCACell, QCACircuit


def build_multiplier_2x2() -> QCACircuit:
    mult = QCACircuit("Multiplier_2x2")

    # =========================================================================
    # CLOCK ZONE 0: Primary Inputs & Input Busses
    # =========================================================================
    # Inputs: A0, A1, B0, B1
    mult.add_cell(QCACell(60, 60, cell_function="INPUT", clock=0, label="A0"))
    mult.add_cell(QCACell(80, 60, cell_function="NORMAL", clock=0))
    mult.add_cell(QCACell(100, 60, cell_function="NORMAL", clock=0))

    mult.add_cell(QCACell(60, 120, cell_function="INPUT", clock=0, label="B0"))
    mult.add_cell(QCACell(80, 120, cell_function="NORMAL", clock=0))
    mult.add_cell(QCACell(100, 120, cell_function="NORMAL", clock=0))

    mult.add_cell(QCACell(60, 180, cell_function="INPUT", clock=0, label="A1"))
    mult.add_cell(QCACell(80, 180, cell_function="NORMAL", clock=0))
    mult.add_cell(QCACell(100, 180, cell_function="NORMAL", clock=0))

    mult.add_cell(QCACell(60, 240, cell_function="INPUT", clock=0, label="B1"))
    mult.add_cell(QCACell(80, 240, cell_function="NORMAL", clock=0))
    mult.add_cell(QCACell(100, 240, cell_function="NORMAL", clock=0))

    # =========================================================================
    # CLOCK ZONE 1: Partial Product Generation (4 AND Majority Voters)
    # =========================================================================
    # AND0: A0 AND B0 -> PP0 (at y = 80)
    mult.add_cell(QCACell(120, 60, cell_function="NORMAL", clock=1))
    mult.add_cell(QCACell(140, 60, cell_function="NORMAL", clock=1))  # A0 into AND0
    mult.add_cell(QCACell(120, 100, cell_function="NORMAL", clock=1))
    mult.add_cell(QCACell(140, 100, cell_function="NORMAL", clock=1)) # B0 into AND0
    mult.add_cell(QCACell(160, 60, cell_function="FIXED", clock=1, polarization=-1.0, label="-1.00")) # Bias
    mult.add_cell(QCACell(160, 80, cell_function="NORMAL", clock=1))  # AND0 Center (PP0)
    mult.add_cell(QCACell(180, 80, cell_function="NORMAL", clock=1))  # PP0 Output wire

    # AND1: A1 AND B0 -> PP1 (at y = 140)
    mult.add_cell(QCACell(140, 120, cell_function="NORMAL", clock=1)) # B0 into AND1
    mult.add_cell(QCACell(120, 160, cell_function="NORMAL", clock=1))
    mult.add_cell(QCACell(140, 160, cell_function="NORMAL", clock=1)) # A1 into AND1
    mult.add_cell(QCACell(160, 120, cell_function="FIXED", clock=1, polarization=-1.0, label="-1.00")) # Bias
    mult.add_cell(QCACell(160, 140, cell_function="NORMAL", clock=1)) # AND1 Center (PP1)
    mult.add_cell(QCACell(180, 140, cell_function="NORMAL", clock=1)) # PP1 Output wire

    # AND2: A0 AND B1 -> PP2 (at y = 200)
    mult.add_cell(QCACell(100, 80, cell_function="NORMAL", clock=0))
    mult.add_cell(QCACell(100, 100, cell_function="NORMAL", clock=0))
    mult.add_cell(QCACell(100, 160, cell_function="NORMAL", clock=0))
    mult.add_cell(QCACell(120, 180, cell_function="NORMAL", clock=1))
    mult.add_cell(QCACell(140, 180, cell_function="NORMAL", clock=1)) # A0 into AND2
    mult.add_cell(QCACell(120, 220, cell_function="NORMAL", clock=1))
    mult.add_cell(QCACell(140, 220, cell_function="NORMAL", clock=1)) # B1 into AND2
    mult.add_cell(QCACell(160, 180, cell_function="FIXED", clock=1, polarization=-1.0, label="-1.00")) # Bias
    mult.add_cell(QCACell(160, 200, cell_function="NORMAL", clock=1)) # AND2 Center (PP2)
    mult.add_cell(QCACell(180, 200, cell_function="NORMAL", clock=1)) # PP2 Output wire

    # AND3: A1 AND B1 -> PP3 (at y = 260)
    mult.add_cell(QCACell(140, 240, cell_function="NORMAL", clock=1)) # A1 into AND3
    mult.add_cell(QCACell(120, 280, cell_function="NORMAL", clock=1))
    mult.add_cell(QCACell(140, 280, cell_function="NORMAL", clock=1)) # B1 into AND3
    mult.add_cell(QCACell(160, 240, cell_function="FIXED", clock=1, polarization=-1.0, label="-1.00")) # Bias
    mult.add_cell(QCACell(160, 260, cell_function="NORMAL", clock=1)) # AND3 Center (PP3)
    mult.add_cell(QCACell(180, 260, cell_function="NORMAL", clock=1)) # PP3 Output wire

    # =========================================================================
    # CLOCK ZONE 2: Half Adder 1 (adds PP1 and PP2) -> P1, C1
    # =========================================================================
    # PP1 wire: (180, 140) -> (200, 140) -> (220, 140)
    mult.add_cell(QCACell(200, 140, cell_function="NORMAL", clock=2))
    mult.add_cell(QCACell(220, 140, cell_function="NORMAL", clock=2))

    # PP2 wire: (180, 200) -> (200, 200) -> (220, 200)
    mult.add_cell(QCACell(200, 200, cell_function="NORMAL", clock=2))
    mult.add_cell(QCACell(220, 200, cell_function="NORMAL", clock=2))

    # HA1 CARRY Majority Voter: M(PP1, PP2, 0) -> C1
    mult.add_cell(QCACell(240, 140, cell_function="NORMAL", clock=2)) # PP1 in
    mult.add_cell(QCACell(240, 180, cell_function="NORMAL", clock=2)) # PP2 in
    mult.add_cell(QCACell(220, 160, cell_function="FIXED", clock=2, polarization=-1.0, label="-1.00")) # 0 bias
    mult.add_cell(QCACell(240, 160, cell_function="NORMAL", clock=2)) # HA1 CARRY Center (C1)
    mult.add_cell(QCACell(260, 160, cell_function="NORMAL", clock=2)) # C1 wire

    # HA1 SUM Majority Voter: M(PP1 + PP2, ~C1, 0) -> P1
    # OR branch: M(PP1, PP2, 1)
    mult.add_cell(QCACell(220, 120, cell_function="FIXED", clock=2, polarization=1.0, label="1.00")) # 1 bias
    mult.add_cell(QCACell(240, 120, cell_function="NORMAL", clock=2)) # HA1 OR Center
    mult.add_cell(QCACell(260, 120, cell_function="NORMAL", clock=2))

    # Invert C1: diagonal coupling from (260, 160) to (280, 180)
    mult.add_cell(QCACell(280, 180, cell_function="NORMAL", clock=2)) # ~C1

    # Output Majority of HA1: at (300, 140)
    mult.add_cell(QCACell(280, 120, cell_function="NORMAL", clock=2))
    mult.add_cell(QCACell(300, 120, cell_function="NORMAL", clock=2)) # OR in
    mult.add_cell(QCACell(300, 160, cell_function="NORMAL", clock=2)) # ~C1 in
    mult.add_cell(QCACell(280, 140, cell_function="FIXED", clock=2, polarization=-1.0, label="-1.00")) # 0 bias
    mult.add_cell(QCACell(300, 140, cell_function="NORMAL", clock=2)) # HA1 SUM Center (P1)
    mult.add_cell(QCACell(320, 140, cell_function="NORMAL", clock=2)) # P1 output wire

    # =========================================================================
    # CLOCK ZONE 3: Half Adder 2 (adds PP3 and C1) -> P2, P3
    # =========================================================================
    # Route C1 down: from (260, 160) -> (260, 220) -> (280, 220)
    mult.add_cell(QCACell(260, 200, cell_function="NORMAL", clock=3))
    mult.add_cell(QCACell(260, 220, cell_function="NORMAL", clock=3))
    mult.add_cell(QCACell(280, 220, cell_function="NORMAL", clock=3))

    # Route PP3 across: (180, 260) -> (240, 260) -> (280, 260)
    mult.add_cell(QCACell(200, 260, cell_function="NORMAL", clock=3))
    mult.add_cell(QCACell(220, 260, cell_function="NORMAL", clock=3))
    mult.add_cell(QCACell(240, 260, cell_function="NORMAL", clock=3))
    mult.add_cell(QCACell(260, 260, cell_function="NORMAL", clock=3))
    mult.add_cell(QCACell(280, 260, cell_function="NORMAL", clock=3))

    # HA2 CARRY Majority Voter: M(PP3, C1, 0) -> P3 (Bit 3)
    mult.add_cell(QCACell(300, 220, cell_function="NORMAL", clock=3)) # C1 in
    mult.add_cell(QCACell(300, 260, cell_function="NORMAL", clock=3)) # PP3 in
    mult.add_cell(QCACell(280, 240, cell_function="FIXED", clock=3, polarization=-1.0, label="-1.00")) # 0 bias
    mult.add_cell(QCACell(300, 240, cell_function="NORMAL", clock=3)) # HA2 CARRY Center (P3)
    mult.add_cell(QCACell(320, 240, cell_function="NORMAL", clock=3))

    # HA2 SUM Majority Voter: M(PP3 + C1, ~P3, 0) -> P2 (Bit 2)
    mult.add_cell(QCACell(320, 200, cell_function="NORMAL", clock=3))
    mult.add_cell(QCACell(340, 200, cell_function="NORMAL", clock=3))
    mult.add_cell(QCACell(320, 220, cell_function="NORMAL", clock=3))
    mult.add_cell(QCACell(340, 220, cell_function="NORMAL", clock=3))

    # Output Pins (Synchronized in Clock 3):
    # P0: from PP0 wire (180, 80) -> (360, 80)
    mult.add_cell(QCACell(200, 80, cell_function="NORMAL", clock=2))
    mult.add_cell(QCACell(220, 80, cell_function="NORMAL", clock=2))
    mult.add_cell(QCACell(240, 80, cell_function="NORMAL", clock=3))
    mult.add_cell(QCACell(260, 80, cell_function="NORMAL", clock=3))
    mult.add_cell(QCACell(280, 80, cell_function="NORMAL", clock=3))
    mult.add_cell(QCACell(300, 80, cell_function="NORMAL", clock=3))
    mult.add_cell(QCACell(320, 80, cell_function="NORMAL", clock=3))
    mult.add_cell(QCACell(340, 80, cell_function="NORMAL", clock=3))
    mult.add_cell(QCACell(360, 80, cell_function="OUTPUT", clock=3, label="P0"))

    # P1: from HA1 SUM (320, 140) -> (360, 140)
    mult.add_cell(QCACell(340, 140, cell_function="NORMAL", clock=3))
    mult.add_cell(QCACell(360, 140, cell_function="OUTPUT", clock=3, label="P1"))

    # P2: from HA2 SUM (340, 200) -> (360, 200)
    mult.add_cell(QCACell(360, 200, cell_function="OUTPUT", clock=3, label="P2"))

    # P3: from HA2 CARRY (320, 240) -> (360, 240)
    mult.add_cell(QCACell(340, 240, cell_function="NORMAL", clock=3))
    mult.add_cell(QCACell(360, 240, cell_function="OUTPUT", clock=3, label="P3"))

    return mult


def main():
    proj_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    mult_dir = os.path.join(proj_root, "QCA_Designs", "Multiplier_2x2")
    os.makedirs(mult_dir, exist_ok=True)
    mult_path = os.path.join(mult_dir, "Multiplier_2x2.qca")

    mult = build_multiplier_2x2()
    mult.save(mult_path)

    m = mult.metrics()
    print("=" * 60)
    print("2x2 Binary Multiplier Layout Generated Successfully:")
    print(f"  Target File : {mult_path}")
    print(f"  Cell Count  : {m['cell_count']}")
    print(f"  Dimensions  : {m['width_nm']:.1f} nm x {m['height_nm']:.1f} nm")
    print(f"  Area        : {m['area_um2']:.6f} um^2")
    print(f"  Clock Zones : {m['clock_zones']}")
    print(f"  Latency     : {m['latency_cycles']} clock cycles")
    print("=" * 60)


if __name__ == "__main__":
    main()
