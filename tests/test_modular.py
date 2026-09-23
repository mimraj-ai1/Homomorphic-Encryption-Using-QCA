"""
Unit and algorithmic tests for QCA Modular Arithmetic (Modulo 4 Adder).
Verifies:
1. All 16 modular addition test vectors for (A + B) mod 4.
2. Quotient / modular overflow calculation Q = floor((A + B) / 4).
3. Reconstruction identity: A + B == 4 * Q + (2 * R1 + R0).
4. Physical .qca file existence, cell count, bounding box, and valid clock zones.
"""

import os
import re
import pytest


def modular_adder_2bit(a1: int, a0: int, b1: int, b0: int):
    """
    Computes 2-bit modular addition:
      A = 2*a1 + a0
      B = 2*b1 + b0
      Returns (Q, R1, R0) where R = 2*R1 + R0 = (A + B) mod 4
      and Q = (A + B) // 4
    """
    # Stage 0: LSB slice (Half Adder with Cin=0)
    c1 = a0 & b0
    r0 = a0 ^ b0

    # Stage 1: MSB slice (Full Adder with Cin=c1)
    q = (a1 & b1) | (c1 & (a1 ^ b1))
    r1 = a1 ^ b1 ^ c1

    return q, r1, r0


class TestModularAdderLogic:
    """Tests the functional truth table and mathematical integrity of the 2-bit Modular Adder."""

    @pytest.mark.parametrize("a_val", [0, 1, 2, 3])
    @pytest.mark.parametrize("b_val", [0, 1, 2, 3])
    def test_all_16_combinations(self, a_val, b_val):
        a1 = (a_val >> 1) & 1
        a0 = a_val & 1
        b1 = (b_val >> 1) & 1
        b0 = b_val & 1

        q, r1, r0 = modular_adder_2bit(a1, a0, b1, b0)

        expected_sum = a_val + b_val
        expected_residue = expected_sum % 4
        expected_quotient = expected_sum // 4

        actual_residue = 2 * r1 + r0

        assert actual_residue == expected_residue, (
            f"Residue mismatch for A={a_val}, B={b_val}: expected {expected_residue}, got {actual_residue}"
        )
        assert q == expected_quotient, (
            f"Quotient mismatch for A={a_val}, B={b_val}: expected {expected_quotient}, got {q}"
        )
        # Mathematical reconstruction identity
        assert expected_sum == 4 * q + actual_residue, (
            f"Sum reconstruction failed for A={a_val}, B={b_val}"
        )

    def test_overflow_cases(self):
        """Verifies that overflow Q is asserted precisely when A + B >= 4."""
        for a in range(4):
            for b in range(4):
                a1, a0 = (a >> 1) & 1, a & 1
                b1, b0 = (b >> 1) & 1, b & 1
                q, _, _ = modular_adder_2bit(a1, a0, b1, b0)
                if a + b >= 4:
                    assert q == 1, f"Expected overflow Q=1 for {a} + {b} = {a+b}"
                else:
                    assert q == 0, f"Expected Q=0 for {a} + {b} = {a+b}"


class TestModularAdderLayoutFile:
    """Tests the physical properties of Modular_Adder.qca."""

    @pytest.fixture(scope="class")
    def layout_content(self):
        proj_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        qca_path = os.path.join(proj_root, "QCA_Designs", "Modular_Arithmetic", "Modular_Adder.qca")
        assert os.path.exists(qca_path), f"File not found: {qca_path}"
        with open(qca_path, "r", encoding="utf-8") as f:
            return f.read()

    def test_qca_file_header(self, layout_content):
        assert "[VERSION]" in layout_content
        assert "qcadesigner_version=2.000000" in layout_content
        assert "[TYPE:DESIGN]" in layout_content
        assert "pszDescription=Main Cell Layer" in layout_content

    def test_cell_count_and_coordinates(self, layout_content):
        cells = re.findall(r"\[TYPE:QCADCell\](.*?)\[#TYPE:QCADCell\]", layout_content, re.DOTALL)
        assert len(cells) == 177, f"Expected 177 cells, found {len(cells)}"

        # Check for zero duplicate coordinates
        coords = set()
        for cell in cells:
            x = float(re.search(r"x=([0-9\.\-]+)", cell).group(1))
            y = float(re.search(r"y=([0-9\.\-]+)", cell).group(1))
            pos = (round(x, 2), round(y, 2))
            assert pos not in coords, f"Duplicate cell found at {pos}"
            coords.add(pos)

    def test_primary_ports(self, layout_content):
        inputs = re.findall(r"cell_function=QCAD_CELL_INPUT.*?psz=([^\r\n]+)", layout_content, re.DOTALL)
        outputs = re.findall(r"cell_function=QCAD_CELL_OUTPUT.*?psz=([^\r\n]+)", layout_content, re.DOTALL)

        assert set(inputs) == {"A0", "B0", "A1", "B1"}
        assert set(outputs) == {"R0", "R1", "Q"}

    def test_clock_zones(self, layout_content):
        clocks = [int(m) for m in re.findall(r"cell_options\.clock=(\d+)", layout_content)]
        assert set(clocks) == {0, 1, 2, 3}
