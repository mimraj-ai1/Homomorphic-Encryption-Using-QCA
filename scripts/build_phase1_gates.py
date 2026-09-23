"""
Generate Phase 1 QCA Gates (.qca files) for QCADesigner 2.0.3.
Constructs: AND, OR, NOT, NAND, NOR gates adhering strictly to
MAKAUT baseline layouts and QCADesigner file specifications.
"""

import os
from qca_circuit_builder import QCACell, QCACircuit


def build_and_gate() -> QCACircuit:
    circuit = QCACircuit("AND_Gate")
    # Universal Majority Voter with Fixed C = -1.0 (Logic 0)
    circuit.add_cell(QCACell(80, 100, cell_function="INPUT", clock=0, label="A"))
    circuit.add_cell(QCACell(100, 80, cell_function="INPUT", clock=0, label="B"))
    circuit.add_cell(QCACell(100, 120, cell_function="FIXED", clock=0, polarization=-1.0, label="-1.00"))
    circuit.add_cell(QCACell(100, 100, cell_function="NORMAL", clock=0))
    circuit.add_cell(QCACell(120, 100, cell_function="OUTPUT", clock=0, label="Y"))
    return circuit


def build_or_gate() -> QCACircuit:
    circuit = QCACircuit("OR_Gate")
    # Universal Majority Voter with Fixed C = +1.0 (Logic 1)
    circuit.add_cell(QCACell(80, 100, cell_function="INPUT", clock=0, label="A"))
    circuit.add_cell(QCACell(100, 80, cell_function="INPUT", clock=0, label="B"))
    circuit.add_cell(QCACell(100, 120, cell_function="FIXED", clock=0, polarization=1.0, label="1.00"))
    circuit.add_cell(QCACell(100, 100, cell_function="NORMAL", clock=0))
    circuit.add_cell(QCACell(120, 100, cell_function="OUTPUT", clock=0, label="Y"))
    return circuit


def build_not_gate() -> QCACircuit:
    circuit = QCACircuit("NOT_Gate")
    # Diagonally displaced anti-phase coupling inverter
    circuit.add_cell(QCACell(60, 80, cell_function="INPUT", clock=0, label="A"))
    circuit.add_cell(QCACell(80, 80, cell_function="NORMAL", clock=0))
    circuit.add_cell(QCACell(100, 100, cell_function="NORMAL", clock=0))
    circuit.add_cell(QCACell(120, 100, cell_function="OUTPUT", clock=0, label="A_inv"))
    return circuit


def build_nand_gate() -> QCACircuit:
    circuit = QCACircuit("NAND_Gate")
    # Cascaded AND Majority Voter + Inverter
    circuit.add_cell(QCACell(80, 100, cell_function="INPUT", clock=0, label="A"))
    circuit.add_cell(QCACell(100, 80, cell_function="INPUT", clock=0, label="B"))
    circuit.add_cell(QCACell(100, 120, cell_function="FIXED", clock=0, polarization=-1.0, label="-1.00"))
    circuit.add_cell(QCACell(100, 100, cell_function="NORMAL", clock=0))
    circuit.add_cell(QCACell(120, 100, cell_function="NORMAL", clock=0))
    circuit.add_cell(QCACell(140, 120, cell_function="NORMAL", clock=0))
    circuit.add_cell(QCACell(160, 120, cell_function="OUTPUT", clock=0, label="Y"))
    return circuit


def build_nor_gate() -> QCACircuit:
    circuit = QCACircuit("NOR_Gate")
    # Cascaded OR Majority Voter + Inverter
    circuit.add_cell(QCACell(80, 100, cell_function="INPUT", clock=0, label="A"))
    circuit.add_cell(QCACell(100, 80, cell_function="INPUT", clock=0, label="B"))
    circuit.add_cell(QCACell(100, 120, cell_function="FIXED", clock=0, polarization=1.0, label="1.00"))
    circuit.add_cell(QCACell(100, 100, cell_function="NORMAL", clock=0))
    circuit.add_cell(QCACell(120, 100, cell_function="NORMAL", clock=0))
    circuit.add_cell(QCACell(140, 120, cell_function="NORMAL", clock=0))
    circuit.add_cell(QCACell(160, 120, cell_function="OUTPUT", clock=0, label="Y"))
    return circuit


def main():
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    gates = [
        ("AND", "AND.qca", build_and_gate()),
        ("OR", "OR.qca", build_or_gate()),
        ("NOT", "NOT.qca", build_not_gate()),
        ("NAND", "NAND.qca", build_nand_gate()),
        ("NOR", "NOR.qca", build_nor_gate()),
    ]

    print("Generating Phase 1 QCA circuits...")
    for dir_name, file_name, circuit in gates:
        target_dir = os.path.join(root, "QCA_Designs", dir_name)
        os.makedirs(target_dir, exist_ok=True)
        target_path = os.path.join(target_dir, file_name)
        circuit.save(target_path)
        m = circuit.metrics()
        print(f"[{dir_name}] Saved to {target_path}")
        print(f"       Cells: {m['cell_count']}, Area: {m['area_um2']:.6f} um^2 ({m['width_nm']:.1f}nm x {m['height_nm']:.1f}nm), Latency: {m['latency_cycles']} cycles")


if __name__ == "__main__":
    main()
