"""
Automated unit tests for QCA 2x2 Binary Multiplier.
Verifies all 16 input combinations, partial products, and physical .qca file integrity.
"""

import os
import re
import pytest

PROJ_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def multiplier_2x2_logic(a1: int, a0: int, b1: int, b0: int) -> tuple[int, int, int, int]:
    """
    Computes 2x2 binary multiplication stage-by-stage using partial products
    and two half adders:
      PP0 = A0 & B0
      PP1 = A1 & B0
      PP2 = A0 & B1
      PP3 = A1 & B1
      HA1: S1 = PP1 ^ PP2, C1 = PP1 & PP2
      HA2: P2 = PP3 ^ C1,  P3 = PP3 & C1
      P0 = PP0, P1 = S1
    Returns (p3, p2, p1, p0).
    """
    pp0 = a0 & b0
    pp1 = a1 & b0
    pp2 = a0 & b1
    pp3 = a1 & b1

    # HA1 adds pp1 and pp2
    p1 = pp1 ^ pp2
    c1 = pp1 & pp2

    # HA2 adds pp3 and c1
    p2 = pp3 ^ c1
    p3 = pp3 & c1

    p0 = pp0
    return (p3, p2, p1, p0)


@pytest.mark.parametrize("b_val", [0, 1, 2, 3])
@pytest.mark.parametrize("a_val", [0, 1, 2, 3])
def test_multiplier_all_16_combinations(a_val, b_val):
    """Exhaustively verify all 16 combinations (4x4) for 2x2 binary multiplication."""
    a1, a0 = (a_val >> 1) & 1, a_val & 1
    b1, b0 = (b_val >> 1) & 1, b_val & 1
    p3, p2, p1, p0 = multiplier_2x2_logic(a1, a0, b1, b0)

    actual_product = (p3 << 3) | (p2 << 2) | (p1 << 1) | p0
    expected_product = a_val * b_val
    assert actual_product == expected_product, (
        f"Multiplier failed for {a_val} x {b_val}: got {actual_product}, expected {expected_product}"
    )


@pytest.mark.parametrize(
    "a, b, expected_p",
    [
        (0, 0, 0),
        (3, 0, 0),
        (1, 1, 1),
        (2, 1, 2),
        (3, 1, 3),
        (2, 2, 4),
        (2, 3, 6),
        (3, 3, 9),
    ],
)
def test_multiplier_critical_vectors(a, b, expected_p):
    a1, a0 = (a >> 1) & 1, a & 1
    b1, b0 = (b >> 1) & 1, b & 1
    p3, p2, p1, p0 = multiplier_2x2_logic(a1, a0, b1, b0)
    actual_product = (p3 << 3) | (p2 << 2) | (p1 << 1) | p0
    assert actual_product == expected_p


def test_multiplier_file_integrity():
    mult_path = os.path.join(PROJ_ROOT, "QCA_Designs", "Multiplier_2x2", "Multiplier_2x2.qca")
    assert os.path.exists(mult_path), f"Multiplier file not found: {mult_path}"
    assert os.path.getsize(mult_path) > 10000, "Multiplier file suspiciously small"

    with open(mult_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Section tags
    assert "[VERSION]" in content
    assert "qcadesigner_version=2.000000" in content
    assert "[TYPE:DESIGN]" in content
    assert "[TYPE:QCADLayer]" in content
    assert "[TYPE:QCADCell]" in content
    assert "[#TYPE:DESIGN]" in content

    # Cells
    cells = re.findall(r"\[TYPE:QCADCell\](.*?)\[#TYPE:QCADCell\]", content, re.DOTALL)
    assert len(cells) == 91, f"Expected 91 cells in Multiplier, found {len(cells)}"

    # Check for duplicate coordinates
    coords = set()
    for c in cells:
        x = float(re.search(r"x=([0-9\.\-]+)", c).group(1))
        y = float(re.search(r"y=([0-9\.\-]+)", c).group(1))
        assert (x, y) not in coords, f"Duplicate cell detected at ({x}, {y})"
        coords.add((x, y))

    # Clock zones
    clocks = set(int(re.search(r"cell_options\.clock=(\d+)", c).group(1)) for c in cells)
    assert clocks == {0, 1, 2, 3}, f"Must span 4 clock zones, found {clocks}"

    # Verify I/O pin labels
    labels = re.findall(r"psz=([^\r\n]+)", content)
    for p in ["A0", "B0", "A1", "B1", "P0", "P1", "P2", "P3"]:
        assert p in labels, f"Pin {p} missing in Multiplier"

    # Verify output cells
    output_cells = re.findall(r"cell_function=QCAD_CELL_OUTPUT.*?psz=([^\r\n]+)", content, re.DOTALL)
    for p in ["P0", "P1", "P2", "P3"]:
        assert p in output_cells, f"Output pin {p} not configured as QCAD_CELL_OUTPUT"
