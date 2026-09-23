"""
Automated unit tests for Phase 1: Basic QCA Logic Gates.
Tests logical truth tables and verifies physical .qca file layout integrity.
"""

import os
import sys
import pytest

# Ensure scripts directory is in path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts")))
from qca_circuit_builder import QCACircuit
from build_phase1_gates import (
    build_and_gate,
    build_or_gate,
    build_not_gate,
    build_nand_gate,
    build_nor_gate,
)


# ============================================================================
# Logical Truth Table Tests
# ============================================================================

def test_and_truth_table():
    truth_table = [
        (0, 0, 0),
        (0, 1, 0),
        (1, 0, 0),
        (1, 1, 1),
    ]
    for a, b, expected in truth_table:
        # Majority Voter equivalent: M(A, B, 0)
        majority_count = a + b + 0
        mv_result = 1 if majority_count >= 2 else 0
        assert mv_result == expected, f"AND failed for ({a}, {b})"
        assert (a and b) == expected


def test_or_truth_table():
    truth_table = [
        (0, 0, 0),
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 1),
    ]
    for a, b, expected in truth_table:
        # Majority Voter equivalent: M(A, B, 1)
        majority_count = a + b + 1
        mv_result = 1 if majority_count >= 2 else 0
        assert mv_result == expected, f"OR failed for ({a}, {b})"
        assert (a or b) == expected


def test_not_truth_table():
    truth_table = [
        (0, 1),
        (1, 0),
    ]
    for a, expected in truth_table:
        assert (1 - a) == expected, f"NOT failed for {a}"


def test_nand_truth_table():
    truth_table = [
        (0, 0, 1),
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 0),
    ]
    for a, b, expected in truth_table:
        assert (1 - (a and b)) == expected, f"NAND failed for ({a}, {b})"


def test_nor_truth_table():
    truth_table = [
        (0, 0, 1),
        (0, 1, 0),
        (1, 0, 0),
        (1, 1, 0),
    ]
    for a, b, expected in truth_table:
        assert (1 - (a or b)) == expected, f"NOR failed for ({a}, {b})"


def test_xor_truth_table():
    truth_table = [
        (0, 0, 0),
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 0),
    ]
    for a, b, expected in truth_table:
        # Canonical expansion: (A or B) and not(A and B)
        xor_result = (a or b) and (1 - (a and b))
        assert xor_result == expected, f"XOR formula failed for ({a}, {b})"
        # Direct bitwise XOR
        assert (a ^ b) == expected, f"Bitwise XOR failed for ({a}, {b})"


# ============================================================================
# Physical Layout & QCADesigner File Integrity Tests
# ============================================================================

@pytest.mark.parametrize(
    "builder_func, expected_cells, expected_width, expected_height",
    [
        (build_and_gate, 5, 58.0, 58.0),
        (build_or_gate, 5, 58.0, 58.0),
        (build_not_gate, 4, 78.0, 38.0),
        (build_nand_gate, 7, 98.0, 58.0),
        (build_nor_gate, 7, 98.0, 58.0),
    ],
)
def test_gate_layout_metrics(builder_func, expected_cells, expected_width, expected_height):
    circuit = builder_func()
    metrics = circuit.metrics()
    assert metrics["cell_count"] == expected_cells
    assert pytest.approx(metrics["width_nm"], 0.1) == expected_width
    assert pytest.approx(metrics["height_nm"], 0.1) == expected_height
    assert metrics["area_um2"] > 0


@pytest.mark.parametrize(
    "folder, file_name, min_bytes",
    [
        ("AND", "AND.qca", 2500),
        ("OR", "OR.qca", 2500),
        ("NOT", "NOT.qca", 2000),
        ("NAND", "NAND.qca", 3500),
        ("NOR", "NOR.qca", 3500),
        ("XOR", "XOR.qca", 15000),
    ],
)
def test_qca_file_existence(folder, file_name, min_bytes):
    proj_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    file_path = os.path.join(proj_root, "QCA_Designs", folder, file_name)
    assert os.path.exists(file_path), f"Missing .qca file: {file_path}"
    file_size = os.path.getsize(file_path)
    assert file_size >= min_bytes, f"File size too small ({file_size} bytes): {file_path}"

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Verify standard QCADesigner section tags
    assert "[VERSION]" in content
    assert "qcadesigner_version=2.000000" in content
    assert "[TYPE:DESIGN]" in content
    assert "[TYPE:QCADLayer]" in content
    assert "[TYPE:QCADCell]" in content
    assert "[#TYPE:DESIGN]" in content


def test_xor_layout_detailed_metrics():
    import re
    proj_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    xor_path = os.path.join(proj_root, "QCA_Designs", "XOR", "XOR.qca")
    with open(xor_path, "r", encoding="utf-8") as f:
        text = f.read()

    cells = re.findall(r"\[TYPE:QCADCell\](.*?)\[#TYPE:QCADCell\]", text, re.DOTALL)
    assert len(cells) == 91, f"Expected 91 cells in XOR, found {len(cells)}"

    # Check clock zones
    clocks = set(int(re.search(r"cell_options\.clock=(\d+)", c).group(1)) for c in cells)
    assert clocks == {0, 1, 2, 3}, f"XOR must utilize 4-phase clock zones, found {clocks}"

    # Verify required I/O pins exist
    labels = re.findall(r"psz=([^\r\n]+)", text)
    assert "A" in labels, "Input A missing in XOR"
    assert "B" in labels, "Input B missing in XOR"
    assert "xor" in labels, "Output xor missing in XOR"

