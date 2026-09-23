"""
Generate Phase 7: QCA Modular Adder (.qca file) for QCADesigner 2.0.3.
Implements a 2-bit Modular Adder for arithmetic modulo 4:
  (A + B) mod 4 = (R1, R0)_2
  Quotient / Overflow Q = floor((A + B) / 4)

Stage 0 (LSB slice):
  Inputs: A0, B0, Cin=0 (fixed logic 0 cell)
  Outputs: R0 (delayed to sync with R1), C1 (carry to Stage 1)

Stage 1 (MSB slice):
  Inputs: A1, B1, C1
  Outputs: R1 (Residue bit 1), Q (Modulo-4 Overflow / Quotient)

Synchronized outputs: R0, R1, Q all delivered at Clock Zone 3 of Cycle 1.
"""

import os
from qca_circuit_builder import QCACell, QCACircuit


def build_modular_adder() -> QCACircuit:
    mod_adder = QCACircuit("Modular_Adder")

    stage_dx = 340.0
    stage_dy = 0.0

    # -------------------------------------------------------------------------
    # STAGE 0: Bit 0 (LSB) Slice
    # -------------------------------------------------------------------------
    x0 = 0.0
    y0 = 0.0
    clk0_base = 0

    # Primary Inputs
    mod_adder.add_cell(QCACell(x0 + 60, y0 + 100, cell_function="INPUT", clock=0, label="A0"))
    mod_adder.add_cell(QCACell(x0 + 80, y0 + 100, cell_function="NORMAL", clock=0))
    mod_adder.add_cell(QCACell(x0 + 100, y0 + 100, cell_function="NORMAL", clock=0))

    mod_adder.add_cell(QCACell(x0 + 60, y0 + 140, cell_function="INPUT", clock=0, label="B0"))
    mod_adder.add_cell(QCACell(x0 + 80, y0 + 140, cell_function="NORMAL", clock=0))
    mod_adder.add_cell(QCACell(x0 + 100, y0 + 140, cell_function="NORMAL", clock=0))

    # Cin for Stage 0 is fixed Logic 0 (P = -1.0) for modular addition without carry-in
    mod_adder.add_cell(QCACell(x0 + 60, y0 + 220, cell_function="FIXED", clock=0, polarization=-1.0, label="Cin0"))
    mod_adder.add_cell(QCACell(x0 + 80, y0 + 220, cell_function="NORMAL", clock=0))
    mod_adder.add_cell(QCACell(x0 + 100, y0 + 220, cell_function="NORMAL", clock=0))

    # Stage 0 Routing (Clock 1)
    mod_adder.add_cell(QCACell(x0 + 120, y0 + 100, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x0 + 140, y0 + 100, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x0 + 160, y0 + 100, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x0 + 180, y0 + 100, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x0 + 180, y0 + 120, cell_function="NORMAL", clock=1))

    mod_adder.add_cell(QCACell(x0 + 120, y0 + 120, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x0 + 120, y0 + 160, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x0 + 120, y0 + 180, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x0 + 120, y0 + 200, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x0 + 140, y0 + 200, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x0 + 160, y0 + 200, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x0 + 180, y0 + 200, cell_function="NORMAL", clock=1))

    mod_adder.add_cell(QCACell(x0 + 140, y0 + 140, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x0 + 160, y0 + 140, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x0 + 140, y0 + 160, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x0 + 140, y0 + 180, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x0 + 160, y0 + 220, cell_function="NORMAL", clock=1))

    mod_adder.add_cell(QCACell(x0 + 120, y0 + 220, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x0 + 160, y0 + 160, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x0 + 180, y0 + 160, cell_function="NORMAL", clock=1))

    # Cin inverter for M2
    mod_adder.add_cell(QCACell(x0 + 120, y0 + 240, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x0 + 140, y0 + 260, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x0 + 160, y0 + 260, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x0 + 180, y0 + 240, cell_function="NORMAL", clock=1))

    # Cin bus to M3
    mod_adder.add_cell(QCACell(x0 + 80, y0 + 260, cell_function="NORMAL", clock=0))
    mod_adder.add_cell(QCACell(x0 + 80, y0 + 280, cell_function="NORMAL", clock=0))
    mod_adder.add_cell(QCACell(x0 + 80, y0 + 300, cell_function="NORMAL", clock=0))
    mod_adder.add_cell(QCACell(x0 + 100, y0 + 300, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x0 + 120, y0 + 300, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x0 + 140, y0 + 300, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x0 + 160, y0 + 300, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x0 + 180, y0 + 300, cell_function="NORMAL", clock=1))

    # Stage 0 Evaluation (Clock 2)
    mod_adder.add_cell(QCACell(x0 + 200, y0 + 300, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(x0 + 220, y0 + 300, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(x0 + 240, y0 + 300, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(x0 + 260, y0 + 300, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(x0 + 280, y0 + 300, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(x0 + 300, y0 + 300, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(x0 + 300, y0 + 280, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(x0 + 300, y0 + 260, cell_function="NORMAL", clock=2))

    mod_adder.add_cell(QCACell(x0 + 180, y0 + 140, cell_function="NORMAL", clock=2))  # M1 center
    mod_adder.add_cell(QCACell(x0 + 200, y0 + 140, cell_function="NORMAL", clock=2))

    mod_adder.add_cell(QCACell(x0 + 180, y0 + 220, cell_function="NORMAL", clock=2))  # M2 center
    mod_adder.add_cell(QCACell(x0 + 200, y0 + 220, cell_function="NORMAL", clock=2))

    # Cout inverter for M3
    mod_adder.add_cell(QCACell(x0 + 220, y0 + 140, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(x0 + 240, y0 + 160, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(x0 + 260, y0 + 160, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(x0 + 280, y0 + 160, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(x0 + 300, y0 + 180, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(x0 + 300, y0 + 200, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(x0 + 300, y0 + 220, cell_function="NORMAL", clock=2))

    # M2 to M3 left input
    mod_adder.add_cell(QCACell(x0 + 220, y0 + 220, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(x0 + 240, y0 + 240, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(x0 + 260, y0 + 240, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(x0 + 280, y0 + 240, cell_function="NORMAL", clock=2))

    # Stage 0 Carry Transmission (Clock 2 & 3)
    mod_adder.add_cell(QCACell(x0 + 240, y0 + 120, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(x0 + 260, y0 + 120, cell_function="NORMAL", clock=2))

    mod_adder.add_cell(QCACell(x0 + 280, y0 + 120, cell_function="NORMAL", clock=3))
    mod_adder.add_cell(QCACell(x0 + 300, y0 + 120, cell_function="NORMAL", clock=3))
    mod_adder.add_cell(QCACell(x0 + 320, y0 + 120, cell_function="NORMAL", clock=3))
    mod_adder.add_cell(QCACell(x0 + 340, y0 + 120, cell_function="NORMAL", clock=3))

    # Inter-stage carry wire to Stage 1 Cin
    mod_adder.add_cell(QCACell(x0 + 360, y0 + 120, cell_function="NORMAL", clock=3))
    mod_adder.add_cell(QCACell(x0 + 360, y0 + 140, cell_function="NORMAL", clock=3))
    mod_adder.add_cell(QCACell(x0 + 360, y0 + 160, cell_function="NORMAL", clock=3))
    mod_adder.add_cell(QCACell(x0 + 380, y0 + 180, cell_function="NORMAL", clock=3))
    mod_adder.add_cell(QCACell(x0 + 380, y0 + 200, cell_function="NORMAL", clock=3))
    mod_adder.add_cell(QCACell(x0 + 380, y0 + 220, cell_function="NORMAL", clock=3))

    # Stage 0 Sum Output (R0) evaluation (Clock 3)
    mod_adder.add_cell(QCACell(x0 + 300, y0 + 240, cell_function="NORMAL", clock=3))
    mod_adder.add_cell(QCACell(x0 + 320, y0 + 240, cell_function="NORMAL", clock=3))
    mod_adder.add_cell(QCACell(x0 + 340, y0 + 240, cell_function="NORMAL", clock=3))
    mod_adder.add_cell(QCACell(x0 + 360, y0 + 240, cell_function="NORMAL", clock=3))

    # -------------------------------------------------------------------------
    # R0 SYNCHRONIZATION PIPELINE (Clock 3 -> 0 -> 1 -> 2 -> 3)
    # Routes R0 safely along y=340 down to the output column
    # -------------------------------------------------------------------------
    mod_adder.add_cell(QCACell(360, 260, cell_function="NORMAL", clock=3))
    mod_adder.add_cell(QCACell(360, 280, cell_function="NORMAL", clock=3))
    mod_adder.add_cell(QCACell(360, 300, cell_function="NORMAL", clock=3))
    mod_adder.add_cell(QCACell(360, 320, cell_function="NORMAL", clock=3))
    mod_adder.add_cell(QCACell(360, 340, cell_function="NORMAL", clock=3))

    # Transition to Cycle 2 / Zone 0
    mod_adder.add_cell(QCACell(380, 340, cell_function="NORMAL", clock=0))
    mod_adder.add_cell(QCACell(400, 340, cell_function="NORMAL", clock=0))
    mod_adder.add_cell(QCACell(420, 340, cell_function="NORMAL", clock=0))
    mod_adder.add_cell(QCACell(440, 340, cell_function="NORMAL", clock=0))

    # Transition to Zone 1
    mod_adder.add_cell(QCACell(460, 340, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(480, 340, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(500, 340, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(520, 340, cell_function="NORMAL", clock=1))

    # Transition to Zone 2
    mod_adder.add_cell(QCACell(540, 340, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(560, 340, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(580, 340, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(600, 340, cell_function="NORMAL", clock=2))

    # Transition to Zone 3 (Final Output Column)
    mod_adder.add_cell(QCACell(620, 340, cell_function="NORMAL", clock=3))
    mod_adder.add_cell(QCACell(640, 340, cell_function="NORMAL", clock=3))
    mod_adder.add_cell(QCACell(660, 340, cell_function="NORMAL", clock=3))
    mod_adder.add_cell(QCACell(680, 340, cell_function="NORMAL", clock=3))
    mod_adder.add_cell(QCACell(700, 340, cell_function="OUTPUT", clock=3, label="R0"))

    # -------------------------------------------------------------------------
    # STAGE 1: Bit 1 (MSB) Slice
    # -------------------------------------------------------------------------
    x1 = stage_dx  # 340.0
    y1 = 0.0

    # Primary Inputs A1 and B1 (Clock 0)
    mod_adder.add_cell(QCACell(x1 + 60, y1 + 100, cell_function="INPUT", clock=0, label="A1"))
    mod_adder.add_cell(QCACell(x1 + 80, y1 + 100, cell_function="NORMAL", clock=0))
    mod_adder.add_cell(QCACell(x1 + 100, y1 + 100, cell_function="NORMAL", clock=0))

    mod_adder.add_cell(QCACell(x1 + 60, y1 + 140, cell_function="INPUT", clock=0, label="B1"))
    mod_adder.add_cell(QCACell(x1 + 80, y1 + 140, cell_function="NORMAL", clock=0))
    mod_adder.add_cell(QCACell(x1 + 100, y1 + 140, cell_function="NORMAL", clock=0))

    # Carry input receiving from Stage 0 carry wire
    mod_adder.add_cell(QCACell(x1 + 60, y1 + 220, cell_function="NORMAL", clock=0))
    mod_adder.add_cell(QCACell(x1 + 80, y1 + 220, cell_function="NORMAL", clock=0))
    mod_adder.add_cell(QCACell(x1 + 100, y1 + 220, cell_function="NORMAL", clock=0))

    # Stage 1 Routing (Clock 1)
    mod_adder.add_cell(QCACell(x1 + 120, y1 + 100, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x1 + 140, y1 + 100, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x1 + 160, y1 + 100, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x1 + 180, y1 + 100, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x1 + 180, y1 + 120, cell_function="NORMAL", clock=1))

    mod_adder.add_cell(QCACell(x1 + 120, y1 + 120, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x1 + 120, y1 + 160, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x1 + 120, y1 + 180, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x1 + 120, y1 + 200, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x1 + 140, y1 + 200, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x1 + 160, y1 + 200, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x1 + 180, y1 + 200, cell_function="NORMAL", clock=1))

    mod_adder.add_cell(QCACell(x1 + 140, y1 + 140, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x1 + 160, y1 + 140, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x1 + 140, y1 + 160, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x1 + 140, y1 + 180, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x1 + 160, y1 + 220, cell_function="NORMAL", clock=1))

    mod_adder.add_cell(QCACell(x1 + 120, y1 + 220, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x1 + 160, y1 + 160, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x1 + 180, y1 + 160, cell_function="NORMAL", clock=1))

    # Cin inverter for M2
    mod_adder.add_cell(QCACell(x1 + 120, y1 + 240, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x1 + 140, y1 + 260, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x1 + 160, y1 + 260, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x1 + 180, y1 + 240, cell_function="NORMAL", clock=1))

    # Cin bus to M3
    mod_adder.add_cell(QCACell(x1 + 80, y1 + 260, cell_function="NORMAL", clock=0))
    mod_adder.add_cell(QCACell(x1 + 80, y1 + 280, cell_function="NORMAL", clock=0))
    mod_adder.add_cell(QCACell(x1 + 80, y1 + 300, cell_function="NORMAL", clock=0))
    mod_adder.add_cell(QCACell(x1 + 100, y1 + 300, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x1 + 120, y1 + 300, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x1 + 140, y1 + 300, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x1 + 160, y1 + 300, cell_function="NORMAL", clock=1))
    mod_adder.add_cell(QCACell(x1 + 180, y1 + 300, cell_function="NORMAL", clock=1))

    # Stage 1 Evaluation (Clock 2)
    mod_adder.add_cell(QCACell(x1 + 200, y1 + 300, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(x1 + 220, y1 + 300, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(x1 + 240, y1 + 300, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(x1 + 260, y1 + 300, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(x1 + 280, y1 + 300, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(x1 + 300, y1 + 300, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(x1 + 300, y1 + 280, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(x1 + 300, y1 + 260, cell_function="NORMAL", clock=2))

    mod_adder.add_cell(QCACell(x1 + 180, y1 + 140, cell_function="NORMAL", clock=2))  # M1 center
    mod_adder.add_cell(QCACell(x1 + 200, y1 + 140, cell_function="NORMAL", clock=2))

    mod_adder.add_cell(QCACell(x1 + 180, y1 + 220, cell_function="NORMAL", clock=2))  # M2 center
    mod_adder.add_cell(QCACell(x1 + 200, y1 + 220, cell_function="NORMAL", clock=2))

    # Cout inverter for M3
    mod_adder.add_cell(QCACell(x1 + 220, y1 + 140, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(x1 + 240, y1 + 160, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(x1 + 260, y1 + 160, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(x1 + 280, y1 + 160, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(x1 + 300, y1 + 180, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(x1 + 300, y1 + 200, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(x1 + 300, y1 + 220, cell_function="NORMAL", clock=2))

    # M2 to M3 left input
    mod_adder.add_cell(QCACell(x1 + 220, y1 + 220, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(x1 + 240, y1 + 240, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(x1 + 260, y1 + 240, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(x1 + 280, y1 + 240, cell_function="NORMAL", clock=2))

    # Carry transmission (Quotient / Modulo-4 Overflow Q)
    mod_adder.add_cell(QCACell(x1 + 240, y1 + 120, cell_function="NORMAL", clock=2))
    mod_adder.add_cell(QCACell(x1 + 260, y1 + 120, cell_function="NORMAL", clock=2))

    mod_adder.add_cell(QCACell(x1 + 280, y1 + 120, cell_function="NORMAL", clock=3))
    mod_adder.add_cell(QCACell(x1 + 300, y1 + 120, cell_function="NORMAL", clock=3))
    mod_adder.add_cell(QCACell(x1 + 320, y1 + 120, cell_function="NORMAL", clock=3))
    mod_adder.add_cell(QCACell(x1 + 340, y1 + 120, cell_function="NORMAL", clock=3))
    mod_adder.add_cell(QCACell(x1 + 360, y1 + 120, cell_function="OUTPUT", clock=3, label="Q"))

    # Stage 1 Residue Output (R1) (Clock 3)
    mod_adder.add_cell(QCACell(x1 + 300, y1 + 240, cell_function="NORMAL", clock=3))
    mod_adder.add_cell(QCACell(x1 + 320, y1 + 240, cell_function="NORMAL", clock=3))
    mod_adder.add_cell(QCACell(x1 + 340, y1 + 240, cell_function="NORMAL", clock=3))
    mod_adder.add_cell(QCACell(x1 + 360, y1 + 240, cell_function="OUTPUT", clock=3, label="R1"))

    return mod_adder


def main():
    proj_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    mod_dir = os.path.join(proj_root, "QCA_Designs", "Modular_Arithmetic")
    os.makedirs(mod_dir, exist_ok=True)
    mod_path = os.path.join(mod_dir, "Modular_Adder.qca")

    mod_adder = build_modular_adder()

    # Coordinate collision validation
    coords = set()
    for c in mod_adder.cells:
        pos = (round(c.x, 2), round(c.y, 2))
        if pos in coords:
            raise ValueError(f"DUPLICATE CELL COORDINATE DETECTED AT: {pos}")
        coords.add(pos)

    mod_adder.save(mod_path)
    m = mod_adder.metrics()

    print("=" * 60)
    print("QCA Modular Adder (Mod 4) Layout Generated Successfully:")
    print(f"  Target File : {mod_path}")
    print(f"  Cell Count  : {m['cell_count']}")
    print(f"  Dimensions  : {m['width_nm']:.1f} nm x {m['height_nm']:.1f} nm")
    print(f"  Area        : {m['area_um2']:.6f} um^2")
    print(f"  Clock Zones : {m['clock_zones']}")
    print(f"  Latency     : {m['latency_cycles']} clock cycles")
    print("=" * 60)


if __name__ == "__main__":
    main()
