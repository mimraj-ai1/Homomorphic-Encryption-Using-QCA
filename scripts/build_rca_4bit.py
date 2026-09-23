"""
Generate Phase 5: 4-bit Ripple Carry Adder (RCA) QCA layout for QCADesigner 2.0.3.
Cascades 4 Full Adder stages:
  FA0(A0, B0, Cin) -> S0, C1
  FA1(A1, B1, C1)  -> S1, C2
  FA2(A2, B2, C2)  -> S2, C3
  FA3(A3, B3, C3)  -> S3, Cout
Connects carry ripples between adjacent bit stages.
"""

import os
from qca_circuit_builder import QCACell, QCACircuit
from build_full_adder import build_full_adder


def build_rca_4bit() -> QCACircuit:
    rca = QCACircuit("RCA_4bit")

    stage_dx = 340.0
    stage_dy = 0.0

    # We will instantiate 4 Full Adder stages with appropriate coordinate and clock offsets
    for k in range(4):
        x_base = k * stage_dx
        y_base = k * stage_dy
        clk_base = (k * 4) % 4  # Clock zones cycle modulo 4

        # Inputs for stage k
        rca.add_cell(QCACell(x_base + 60, y_base + 100, cell_function="INPUT", clock=clk_base, label=f"A{k}"))
        rca.add_cell(QCACell(x_base + 80, y_base + 100, cell_function="NORMAL", clock=clk_base))
        rca.add_cell(QCACell(x_base + 100, y_base + 100, cell_function="NORMAL", clock=clk_base))

        rca.add_cell(QCACell(x_base + 60, y_base + 140, cell_function="INPUT", clock=clk_base, label=f"B{k}"))
        rca.add_cell(QCACell(x_base + 80, y_base + 140, cell_function="NORMAL", clock=clk_base))
        rca.add_cell(QCACell(x_base + 100, y_base + 140, cell_function="NORMAL", clock=clk_base))

        if k == 0:
            # Primary Cin input
            rca.add_cell(QCACell(x_base + 60, y_base + 220, cell_function="INPUT", clock=clk_base, label="Cin"))
        else:
            # Carry input received from previous stage wire
            rca.add_cell(QCACell(x_base + 60, y_base + 220, cell_function="NORMAL", clock=clk_base))

        rca.add_cell(QCACell(x_base + 80, y_base + 220, cell_function="NORMAL", clock=clk_base))
        rca.add_cell(QCACell(x_base + 100, y_base + 220, cell_function="NORMAL", clock=clk_base))

        # Clock Zone 1 (Routing)
        clk1 = (clk_base + 1) % 4
        # A branch
        rca.add_cell(QCACell(x_base + 120, y_base + 100, cell_function="NORMAL", clock=clk1))
        rca.add_cell(QCACell(x_base + 140, y_base + 100, cell_function="NORMAL", clock=clk1))
        rca.add_cell(QCACell(x_base + 160, y_base + 100, cell_function="NORMAL", clock=clk1))
        rca.add_cell(QCACell(x_base + 180, y_base + 100, cell_function="NORMAL", clock=clk1))
        rca.add_cell(QCACell(x_base + 180, y_base + 120, cell_function="NORMAL", clock=clk1))

        rca.add_cell(QCACell(x_base + 120, y_base + 120, cell_function="NORMAL", clock=clk1))
        rca.add_cell(QCACell(x_base + 120, y_base + 160, cell_function="NORMAL", clock=clk1))
        rca.add_cell(QCACell(x_base + 120, y_base + 180, cell_function="NORMAL", clock=clk1))
        rca.add_cell(QCACell(x_base + 120, y_base + 200, cell_function="NORMAL", clock=clk1))
        rca.add_cell(QCACell(x_base + 140, y_base + 200, cell_function="NORMAL", clock=clk1))
        rca.add_cell(QCACell(x_base + 160, y_base + 200, cell_function="NORMAL", clock=clk1))
        rca.add_cell(QCACell(x_base + 180, y_base + 200, cell_function="NORMAL", clock=clk1))

        # B branch
        rca.add_cell(QCACell(x_base + 140, y_base + 140, cell_function="NORMAL", clock=clk1))
        rca.add_cell(QCACell(x_base + 160, y_base + 140, cell_function="NORMAL", clock=clk1))
        rca.add_cell(QCACell(x_base + 140, y_base + 160, cell_function="NORMAL", clock=clk1))
        rca.add_cell(QCACell(x_base + 140, y_base + 180, cell_function="NORMAL", clock=clk1))
        rca.add_cell(QCACell(x_base + 160, y_base + 220, cell_function="NORMAL", clock=clk1))

        # Cin branch
        rca.add_cell(QCACell(x_base + 120, y_base + 220, cell_function="NORMAL", clock=clk1))
        rca.add_cell(QCACell(x_base + 160, y_base + 160, cell_function="NORMAL", clock=clk1))
        rca.add_cell(QCACell(x_base + 180, y_base + 160, cell_function="NORMAL", clock=clk1))

        # Cin inverter for M2
        rca.add_cell(QCACell(x_base + 120, y_base + 240, cell_function="NORMAL", clock=clk1))
        rca.add_cell(QCACell(x_base + 140, y_base + 260, cell_function="NORMAL", clock=clk1))
        rca.add_cell(QCACell(x_base + 160, y_base + 260, cell_function="NORMAL", clock=clk1))
        rca.add_cell(QCACell(x_base + 180, y_base + 240, cell_function="NORMAL", clock=clk1))

        # Cin bus to M3
        rca.add_cell(QCACell(x_base + 80, y_base + 260, cell_function="NORMAL", clock=clk_base))
        rca.add_cell(QCACell(x_base + 80, y_base + 280, cell_function="NORMAL", clock=clk_base))
        rca.add_cell(QCACell(x_base + 80, y_base + 300, cell_function="NORMAL", clock=clk_base))
        rca.add_cell(QCACell(x_base + 100, y_base + 300, cell_function="NORMAL", clock=clk1))
        rca.add_cell(QCACell(x_base + 120, y_base + 300, cell_function="NORMAL", clock=clk1))
        rca.add_cell(QCACell(x_base + 140, y_base + 300, cell_function="NORMAL", clock=clk1))
        rca.add_cell(QCACell(x_base + 160, y_base + 300, cell_function="NORMAL", clock=clk1))
        rca.add_cell(QCACell(x_base + 180, y_base + 300, cell_function="NORMAL", clock=clk1))

        # Clock Zone 2 (Evaluation M1, M2)
        clk2 = (clk_base + 2) % 4
        rca.add_cell(QCACell(x_base + 200, y_base + 300, cell_function="NORMAL", clock=clk2))
        rca.add_cell(QCACell(x_base + 220, y_base + 300, cell_function="NORMAL", clock=clk2))
        rca.add_cell(QCACell(x_base + 240, y_base + 300, cell_function="NORMAL", clock=clk2))
        rca.add_cell(QCACell(x_base + 260, y_base + 300, cell_function="NORMAL", clock=clk2))
        rca.add_cell(QCACell(x_base + 280, y_base + 300, cell_function="NORMAL", clock=clk2))
        rca.add_cell(QCACell(x_base + 300, y_base + 300, cell_function="NORMAL", clock=clk2))
        rca.add_cell(QCACell(x_base + 300, y_base + 280, cell_function="NORMAL", clock=clk2))
        rca.add_cell(QCACell(x_base + 300, y_base + 260, cell_function="NORMAL", clock=clk2))

        rca.add_cell(QCACell(x_base + 180, y_base + 140, cell_function="NORMAL", clock=clk2))  # M1 center
        rca.add_cell(QCACell(x_base + 200, y_base + 140, cell_function="NORMAL", clock=clk2))

        rca.add_cell(QCACell(x_base + 180, y_base + 220, cell_function="NORMAL", clock=clk2))  # M2 center
        rca.add_cell(QCACell(x_base + 200, y_base + 220, cell_function="NORMAL", clock=clk2))

        # Cout inverter for M3
        rca.add_cell(QCACell(x_base + 220, y_base + 140, cell_function="NORMAL", clock=clk2))
        rca.add_cell(QCACell(x_base + 240, y_base + 160, cell_function="NORMAL", clock=clk2))
        rca.add_cell(QCACell(x_base + 260, y_base + 160, cell_function="NORMAL", clock=clk2))
        rca.add_cell(QCACell(x_base + 280, y_base + 160, cell_function="NORMAL", clock=clk2))
        rca.add_cell(QCACell(x_base + 300, y_base + 180, cell_function="NORMAL", clock=clk2))
        rca.add_cell(QCACell(x_base + 300, y_base + 200, cell_function="NORMAL", clock=clk2))
        rca.add_cell(QCACell(x_base + 300, y_base + 220, cell_function="NORMAL", clock=clk2))

        # M2 to M3 left input
        rca.add_cell(QCACell(x_base + 220, y_base + 220, cell_function="NORMAL", clock=clk2))
        rca.add_cell(QCACell(x_base + 240, y_base + 240, cell_function="NORMAL", clock=clk2))
        rca.add_cell(QCACell(x_base + 260, y_base + 240, cell_function="NORMAL", clock=clk2))
        rca.add_cell(QCACell(x_base + 280, y_base + 240, cell_function="NORMAL", clock=clk2))

        # Carry transmission
        rca.add_cell(QCACell(x_base + 240, y_base + 120, cell_function="NORMAL", clock=clk2))
        rca.add_cell(QCACell(x_base + 260, y_base + 120, cell_function="NORMAL", clock=clk2))

        clk3 = (clk_base + 3) % 4
        rca.add_cell(QCACell(x_base + 280, y_base + 120, cell_function="NORMAL", clock=clk3))
        rca.add_cell(QCACell(x_base + 300, y_base + 120, cell_function="NORMAL", clock=clk3))
        rca.add_cell(QCACell(x_base + 320, y_base + 120, cell_function="NORMAL", clock=clk3))
        rca.add_cell(QCACell(x_base + 340, y_base + 120, cell_function="NORMAL", clock=clk3))

        if k == 3:
            # Final Cout Output pin
            rca.add_cell(QCACell(x_base + 360, y_base + 120, cell_function="OUTPUT", clock=clk3, label="Cout"))
        else:
            # Inter-stage carry wire connecting FA_k to FA_{k+1}
            # Connects from (x_base + 340, 120) down to (x_base + 380, 220),
            # which directly neighbors the next stage carry input at (x_base + 400, 220)
            rca.add_cell(QCACell(x_base + 360, y_base + 120, cell_function="NORMAL", clock=clk3))
            rca.add_cell(QCACell(x_base + 360, y_base + 140, cell_function="NORMAL", clock=clk3))
            rca.add_cell(QCACell(x_base + 360, y_base + 160, cell_function="NORMAL", clock=clk3))
            rca.add_cell(QCACell(x_base + 380, y_base + 180, cell_function="NORMAL", clock=clk3))
            rca.add_cell(QCACell(x_base + 380, y_base + 200, cell_function="NORMAL", clock=clk3))
            rca.add_cell(QCACell(x_base + 380, y_base + 220, cell_function="NORMAL", clock=clk3))


        # Clock Zone 3: M3 (SUM_k)
        rca.add_cell(QCACell(x_base + 300, y_base + 240, cell_function="NORMAL", clock=clk3))
        rca.add_cell(QCACell(x_base + 320, y_base + 240, cell_function="NORMAL", clock=clk3))
        rca.add_cell(QCACell(x_base + 340, y_base + 240, cell_function="NORMAL", clock=clk3))
        rca.add_cell(QCACell(x_base + 360, y_base + 240, cell_function="OUTPUT", clock=clk3, label=f"S{k}"))

    return rca


def main():
    proj_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    rca_dir = os.path.join(proj_root, "QCA_Designs", "Ripple_Carry_Adder_4bit")
    os.makedirs(rca_dir, exist_ok=True)
    rca_path = os.path.join(rca_dir, "RCA_4bit.qca")

    rca = build_rca_4bit()
    rca.save(rca_path)

    m = rca.metrics()
    print("=" * 60)
    print("4-bit Ripple Carry Adder Layout Generated Successfully:")
    print(f"  Target File : {rca_path}")
    print(f"  Cell Count  : {m['cell_count']}")
    print(f"  Dimensions  : {m['width_nm']:.1f} nm x {m['height_nm']:.1f} nm")
    print(f"  Area        : {m['area_um2']:.6f} um^2")
    print(f"  Clock Zones : {m['clock_zones']}")
    print(f"  Latency     : {m['latency_cycles']} clock cycles")
    print("=" * 60)


if __name__ == "__main__":
    main()
