"""
Automated unit tests for QCA Adders (Half Adder, Full Adder, Ripple Carry Adder).
Verifies binary addition arithmetic, truth tables, and physical .qca file integrity.
"""

import os
import re
import pytest

PROJ_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


# ============================================================================
# Half Adder Logical Arithmetic Tests
# ============================================================================

def half_adder_logic(a: int, b: int) -> tuple[int, int]:
    """Computes (sum, carry) for a Half Adder."""
    sum_bit = (a ^ b)
    carry_bit = (a & b)
    return (sum_bit, carry_bit)


def test_half_adder_all_combinations():
    """Verify all 4 input combinations for Half Adder: 00, 01, 10, 11."""
    test_vectors = [
        (0, 0, 0, 0),  # 0 + 0 = 0 (carry 0)
        (0, 1, 1, 0),  # 0 + 1 = 1 (carry 0)
        (1, 0, 1, 0),  # 1 + 0 = 1 (carry 0)
        (1, 1, 0, 1),  # 1 + 1 = 2 (sum 0, carry 1)
    ]
    for a, b, expected_sum, expected_carry in test_vectors:
        s, c = half_adder_logic(a, b)
        assert s == expected_sum, f"Sum mismatch for ({a}, {b})"
        assert c == expected_carry, f"Carry mismatch for ({a}, {b})"
        assert (c * 2 + s) == (a + b), f"Arithmetic value mismatch for {a} + {b}"


def test_half_adder_majority_synthesis():
    """Verify Half Adder logic when expressed via QCA Majority equations."""
    for a in (0, 1):
        for b in (0, 1):
            # Majority CARRY = M(A, B, 0)
            carry_mv = 1 if (a + b + 0) >= 2 else 0
            # Majority OR = M(A, B, 1)
            or_mv = 1 if (a + b + 1) >= 2 else 0
            # Inverted CARRY
            carry_inv = 1 - carry_mv
            # SUM = M(OR, carry_inv, 0)
            sum_mv = 1 if (or_mv + carry_inv + 0) >= 2 else 0

            exp_s, exp_c = half_adder_logic(a, b)
            assert carry_mv == exp_c
            assert sum_mv == exp_s


# ============================================================================
# Half Adder Physical Layout & QCADesigner File Integrity Tests
# ============================================================================

def test_half_adder_file_integrity():
    ha_path = os.path.join(PROJ_ROOT, "QCA_Designs", "Half_Adder", "Half_Adder.qca")
    assert os.path.exists(ha_path), f"Half Adder file not found: {ha_path}"
    assert os.path.getsize(ha_path) > 10000, "Half Adder file suspiciously small"

    with open(ha_path, "r", encoding="utf-8") as f:
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
    assert len(cells) == 91, f"Expected 91 cells in Half Adder, found {len(cells)}"

    # Clock zones
    clocks = set(int(re.search(r"cell_options\.clock=(\d+)", c).group(1)) for c in cells)
    assert clocks == {0, 1, 2, 3}, f"Must span 4 clock zones, found {clocks}"

    # Verify primary input and output pin labels
    labels = re.findall(r"psz=([^\r\n]+)", content)
    assert "A" in labels, "Input pin A missing"
    assert "B" in labels, "Input pin B missing"
    assert "SUM" in labels, "Output pin SUM missing"
    assert "CARRY" in labels, "Output pin CARRY missing"

    # Verify output cells have cell_function=QCAD_CELL_OUTPUT
    output_cells = re.findall(r"cell_function=QCAD_CELL_OUTPUT.*?psz=([^\r\n]+)", content, re.DOTALL)
    assert "SUM" in output_cells
    assert "CARRY" in output_cells


# ============================================================================
# Full Adder Logical Arithmetic Tests
# ============================================================================

def full_adder_logic(a: int, b: int, cin: int) -> tuple[int, int]:
    """Computes (sum, cout) for a 1-bit Full Adder."""
    sum_bit = a ^ b ^ cin
    cout_bit = (a & b) | (cin & (a ^ b))
    return (sum_bit, cout_bit)


def test_full_adder_all_combinations():
    """Verify all 8 input combinations for Full Adder: 000 through 111."""
    test_vectors = [
        (0, 0, 0, 0, 0),  # 0 + 0 + 0 = 0 (sum 0, cout 0)
        (0, 0, 1, 1, 0),  # 0 + 0 + 1 = 1 (sum 1, cout 0)
        (0, 1, 0, 1, 0),  # 0 + 1 + 0 = 1 (sum 1, cout 0)
        (0, 1, 1, 0, 1),  # 0 + 1 + 1 = 2 (sum 0, cout 1)
        (1, 0, 0, 1, 0),  # 1 + 0 + 0 = 1 (sum 1, cout 0)
        (1, 0, 1, 0, 1),  # 1 + 0 + 1 = 2 (sum 0, cout 1)
        (1, 1, 0, 0, 1),  # 1 + 1 + 0 = 2 (sum 0, cout 1)
        (1, 1, 1, 1, 1),  # 1 + 1 + 1 = 3 (sum 1, cout 1)
    ]
    for a, b, cin, expected_sum, expected_cout in test_vectors:
        s, cout = full_adder_logic(a, b, cin)
        assert s == expected_sum, f"Sum mismatch for ({a}, {b}, {cin})"
        assert cout == expected_cout, f"Cout mismatch for ({a}, {b}, {cin})"
        assert (cout * 2 + s) == (a + b + cin), f"Arithmetic value mismatch for {a} + {b} + {cin}"


def test_full_adder_tougaw_lent_majority_synthesis():
    """Verify Tougaw-Lent 3-Majority-Voter Full Adder formulation across all 8 vectors."""
    for a in (0, 1):
        for b in (0, 1):
            for cin in (0, 1):
                # M1: Cout = M(A, B, Cin)
                m1_cout = 1 if (a + b + cin) >= 2 else 0
                # Invert Cin
                cin_inv = 1 - cin
                # M2 = M(A, B, ~Cin)
                m2 = 1 if (a + b + cin_inv) >= 2 else 0
                # Invert Cout
                m1_inv = 1 - m1_cout
                # M3: SUM = M(~Cout, M2, Cin)
                m3_sum = 1 if (m1_inv + m2 + cin) >= 2 else 0

                exp_s, exp_c = full_adder_logic(a, b, cin)
                assert m1_cout == exp_c, f"Majority Cout mismatch for ({a}, {b}, {cin})"
                assert m3_sum == exp_s, f"Majority SUM mismatch for ({a}, {b}, {cin})"


# ============================================================================
# Full Adder Physical Layout & QCADesigner File Integrity Tests
# ============================================================================

def test_full_adder_file_integrity():
    fa_path = os.path.join(PROJ_ROOT, "QCA_Designs", "Full_Adder", "Full_Adder.qca")
    assert os.path.exists(fa_path), f"Full Adder file not found: {fa_path}"
    assert os.path.getsize(fa_path) > 10000, "Full Adder file suspiciously small"

    with open(fa_path, "r", encoding="utf-8") as f:
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
    assert len(cells) == 75, f"Expected 75 cells in Full Adder, found {len(cells)}"

    # Clock zones
    clocks = set(int(re.search(r"cell_options\.clock=(\d+)", c).group(1)) for c in cells)
    assert clocks == {0, 1, 2, 3}, f"Must span 4 clock zones, found {clocks}"

    # Verify primary input and output pin labels
    labels = re.findall(r"psz=([^\r\n]+)", content)
    assert "A" in labels, "Input pin A missing"
    assert "B" in labels, "Input pin B missing"
    assert "Cin" in labels, "Input pin Cin missing"
    assert "SUM" in labels, "Output pin SUM missing"
    assert "Cout" in labels, "Output pin Cout missing"

    # Verify output cells have cell_function=QCAD_CELL_OUTPUT
    output_cells = re.findall(r"cell_function=QCAD_CELL_OUTPUT.*?psz=([^\r\n]+)", content, re.DOTALL)
    assert "SUM" in output_cells
    assert "Cout" in output_cells

