"""
Generate Phase 4 QCA Full Adder (.qca file) for QCADesigner 2.0.3.
Implements the canonical 1-bit Full Adder based on the Tougaw-Lent Majority architecture:
  Cout = M(A, B, Cin)
  M2   = M(A, B, ~Cin)
  SUM  = M(~Cout, M2, Cin)
All 3 Majority Voters and 2 inverters are placed with strict 4-phase clock zone synchronization.
"""

import os
from qca_circuit_builder import QCACell, QCACircuit


def build_full_adder() -> QCACircuit:
    circuit = QCACircuit("Full_Adder")

    # =========================================================================
    # CLOCK ZONE 0: Primary Inputs & Distribution
    # =========================================================================
    # Input A
    circuit.add_cell(QCACell(60, 100, cell_function="INPUT", clock=0, label="A"))
    circuit.add_cell(QCACell(80, 100, cell_function="NORMAL", clock=0))
    circuit.add_cell(QCACell(100, 100, cell_function="NORMAL", clock=0))

    # Input B
    circuit.add_cell(QCACell(60, 140, cell_function="INPUT", clock=0, label="B"))
    circuit.add_cell(QCACell(80, 140, cell_function="NORMAL", clock=0))
    circuit.add_cell(QCACell(100, 140, cell_function="NORMAL", clock=0))

    # Input Cin
    circuit.add_cell(QCACell(60, 220, cell_function="INPUT", clock=0, label="Cin"))
    circuit.add_cell(QCACell(80, 220, cell_function="NORMAL", clock=0))
    circuit.add_cell(QCACell(100, 220, cell_function="NORMAL", clock=0))

    # =========================================================================
    # CLOCK ZONE 1: Routing to M1 (Cout) and M2
    # =========================================================================
    # Branching A:
    # A to M1 top input: (160, 100) -> (180, 100) -> (180, 120)
    circuit.add_cell(QCACell(120, 100, cell_function="NORMAL", clock=1))
    circuit.add_cell(QCACell(140, 100, cell_function="NORMAL", clock=1))
    circuit.add_cell(QCACell(160, 100, cell_function="NORMAL", clock=1))
    circuit.add_cell(QCACell(180, 100, cell_function="NORMAL", clock=1))
    circuit.add_cell(QCACell(180, 120, cell_function="NORMAL", clock=1))  # M1 top input

    # A to M2 top input: route down along x=120
    circuit.add_cell(QCACell(120, 120, cell_function="NORMAL", clock=1))
    circuit.add_cell(QCACell(120, 160, cell_function="NORMAL", clock=1))
    circuit.add_cell(QCACell(120, 180, cell_function="NORMAL", clock=1))
    circuit.add_cell(QCACell(120, 200, cell_function="NORMAL", clock=1))
    circuit.add_cell(QCACell(140, 200, cell_function="NORMAL", clock=1))
    circuit.add_cell(QCACell(160, 200, cell_function="NORMAL", clock=1))
    circuit.add_cell(QCACell(180, 200, cell_function="NORMAL", clock=1))  # M2 top input

    # Branching B:
    # B to M1 left input: (120, 140) -> (140, 140) -> (160, 140)
    circuit.add_cell(QCACell(140, 140, cell_function="NORMAL", clock=1))
    circuit.add_cell(QCACell(160, 140, cell_function="NORMAL", clock=1))  # M1 left input

    # B to M2 left input: (140, 160) -> (140, 180) -> (140, 220) -> (160, 220)
    circuit.add_cell(QCACell(140, 160, cell_function="NORMAL", clock=1))
    circuit.add_cell(QCACell(140, 180, cell_function="NORMAL", clock=1))
    circuit.add_cell(QCACell(160, 220, cell_function="NORMAL", clock=1))  # M2 left input

    # Branching Cin:
    # Cin to M1 bottom input: (120, 220) -> (180, 160)
    circuit.add_cell(QCACell(120, 220, cell_function="NORMAL", clock=1))
    circuit.add_cell(QCACell(160, 160, cell_function="NORMAL", clock=1))
    circuit.add_cell(QCACell(180, 160, cell_function="NORMAL", clock=1))  # M1 bottom input

    # Inverting Cin for M2:
    # diagonal displacement from (120, 240) to (140, 260)
    circuit.add_cell(QCACell(120, 240, cell_function="NORMAL", clock=1))
    circuit.add_cell(QCACell(140, 260, cell_function="NORMAL", clock=1))  # ~Cin
    circuit.add_cell(QCACell(160, 260, cell_function="NORMAL", clock=1))
    circuit.add_cell(QCACell(180, 240, cell_function="NORMAL", clock=1))  # M2 bottom input

    # Cin passthrough line for M3 bottom input (runs along y=300)
    circuit.add_cell(QCACell(80, 260, cell_function="NORMAL", clock=0))
    circuit.add_cell(QCACell(80, 280, cell_function="NORMAL", clock=0))
    circuit.add_cell(QCACell(80, 300, cell_function="NORMAL", clock=0))
    circuit.add_cell(QCACell(100, 300, cell_function="NORMAL", clock=1))
    circuit.add_cell(QCACell(120, 300, cell_function="NORMAL", clock=1))
    circuit.add_cell(QCACell(140, 300, cell_function="NORMAL", clock=1))
    circuit.add_cell(QCACell(160, 300, cell_function="NORMAL", clock=1))
    circuit.add_cell(QCACell(180, 300, cell_function="NORMAL", clock=1))
    circuit.add_cell(QCACell(200, 300, cell_function="NORMAL", clock=2))
    circuit.add_cell(QCACell(220, 300, cell_function="NORMAL", clock=2))
    circuit.add_cell(QCACell(240, 300, cell_function="NORMAL", clock=2))
    circuit.add_cell(QCACell(260, 300, cell_function="NORMAL", clock=2))
    circuit.add_cell(QCACell(280, 300, cell_function="NORMAL", clock=2))
    circuit.add_cell(QCACell(300, 300, cell_function="NORMAL", clock=2))
    circuit.add_cell(QCACell(300, 280, cell_function="NORMAL", clock=2))
    circuit.add_cell(QCACell(300, 260, cell_function="NORMAL", clock=2))  # M3 bottom input

    # =========================================================================
    # CLOCK ZONE 2: Majority Evaluations (M1 = Cout, M2)
    # =========================================================================
    # M1 Center: at (180, 140)
    circuit.add_cell(QCACell(180, 140, cell_function="NORMAL", clock=2))
    # M1 Output: at (200, 140)
    circuit.add_cell(QCACell(200, 140, cell_function="NORMAL", clock=2))

    # M2 Center: at (180, 220)
    circuit.add_cell(QCACell(180, 220, cell_function="NORMAL", clock=2))
    # M2 Output: at (200, 220)
    circuit.add_cell(QCACell(200, 220, cell_function="NORMAL", clock=2))

    # Cout Inverter stage (~Cout for M3):
    # From (200, 140), route and invert diagonally to (220, 160)
    circuit.add_cell(QCACell(220, 140, cell_function="NORMAL", clock=2))
    circuit.add_cell(QCACell(240, 160, cell_function="NORMAL", clock=2))  # ~Cout
    circuit.add_cell(QCACell(260, 160, cell_function="NORMAL", clock=2))
    circuit.add_cell(QCACell(280, 160, cell_function="NORMAL", clock=2))
    circuit.add_cell(QCACell(300, 180, cell_function="NORMAL", clock=2))
    circuit.add_cell(QCACell(300, 200, cell_function="NORMAL", clock=2))
    circuit.add_cell(QCACell(300, 220, cell_function="NORMAL", clock=2))  # M3 top input

    # M2 to M3 left input: (220, 220) -> (240, 240) -> (260, 240) -> (280, 240)
    circuit.add_cell(QCACell(220, 220, cell_function="NORMAL", clock=2))
    circuit.add_cell(QCACell(240, 240, cell_function="NORMAL", clock=2))
    circuit.add_cell(QCACell(260, 240, cell_function="NORMAL", clock=2))
    circuit.add_cell(QCACell(280, 240, cell_function="NORMAL", clock=2))  # M3 left input

    # Cout transmission to primary output pin:
    circuit.add_cell(QCACell(240, 120, cell_function="NORMAL", clock=2))
    circuit.add_cell(QCACell(260, 120, cell_function="NORMAL", clock=2))
    circuit.add_cell(QCACell(280, 120, cell_function="NORMAL", clock=3))
    circuit.add_cell(QCACell(300, 120, cell_function="NORMAL", clock=3))
    circuit.add_cell(QCACell(320, 120, cell_function="NORMAL", clock=3))
    circuit.add_cell(QCACell(340, 120, cell_function="NORMAL", clock=3))
    circuit.add_cell(QCACell(360, 120, cell_function="OUTPUT", clock=3, label="Cout"))

    # =========================================================================
    # CLOCK ZONE 3: M3 (SUM) Evaluation & Primary Outputs
    # =========================================================================
    # M3 Center: at (300, 240)
    circuit.add_cell(QCACell(300, 240, cell_function="NORMAL", clock=3))
    # M3 Output: at (320, 240) -> (340, 240) -> (360, 240)
    circuit.add_cell(QCACell(320, 240, cell_function="NORMAL", clock=3))
    circuit.add_cell(QCACell(340, 240, cell_function="NORMAL", clock=3))
    circuit.add_cell(QCACell(360, 240, cell_function="OUTPUT", clock=3, label="SUM"))

    return circuit


def main():
    proj_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    fa_dir = os.path.join(proj_root, "QCA_Designs", "Full_Adder")
    os.makedirs(fa_dir, exist_ok=True)
    fa_path = os.path.join(fa_dir, "Full_Adder.qca")

    circuit = build_full_adder()
    circuit.save(fa_path)

    m = circuit.metrics()
    print("=" * 60)
    print("Full Adder Layout Generated Successfully:")
    print(f"  Target File : {fa_path}")
    print(f"  Cell Count  : {m['cell_count']}")
    print(f"  Dimensions  : {m['width_nm']:.1f} nm x {m['height_nm']:.1f} nm")
    print(f"  Area        : {m['area_um2']:.6f} um^2")
    print(f"  Clock Zones : {m['clock_zones']}")
    print(f"  Latency     : {m['latency_cycles']} clock cycles")
    print("=" * 60)


if __name__ == "__main__":
    main()
