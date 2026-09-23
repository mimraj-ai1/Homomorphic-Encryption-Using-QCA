"""
QCA Circuit Builder & Layout Engine for QCADesigner 2.0.3.

Provides programmatically defined cell placements, clock assignments,
dot charge configurations, and file exporting matching the native QCADesigner 2.0.3 file format.
"""

import math
from typing import List, Optional, Tuple


class QCACell:
    """Represents an individual 4-dot Quantum-dot Cellular Automata cell."""

    def __init__(
        self,
        x: float,
        y: float,
        cell_function: str = "NORMAL",  # INPUT, OUTPUT, FIXED, NORMAL
        clock: int = 0,
        polarization: float = 0.0,      # +1.0 for Logic 1, -1.0 for Logic 0 (used when FIXED)
        label: Optional[str] = None,
        cx: float = 18.0,
        cy: float = 18.0,
        dot_diameter: float = 5.0,
    ):
        self.x = float(x)
        self.y = float(y)
        self.cell_function = cell_function.upper()
        self.clock = int(clock)
        self.polarization = float(polarization)
        self.label = label
        self.cx = float(cx)
        self.cy = float(cy)
        self.dot_diameter = float(dot_diameter)

    @property
    def bounding_box(self) -> Tuple[float, float, float, float]:
        """Returns (xWorld, yWorld, cxWorld, cyWorld)."""
        return (self.x - self.cx / 2.0, self.y - self.cy / 2.0, self.cx, self.cy)

    @property
    def color(self) -> Tuple[int, int, int]:
        """Returns (red, green, blue) as 16-bit integers (0 - 65535)."""
        if self.cell_function == "INPUT":
            return (0, 0, 65535)  # Blue
        elif self.cell_function == "OUTPUT":
            return (65535, 65535, 0)  # Yellow
        elif self.cell_function == "FIXED":
            return (65535, 32768, 0)  # Orange
        else:
            # Normal cells colored according to clock zone
            clock_colors = {
                0: (0, 65535, 0),       # Green
                1: (65535, 0, 65535),   # Magenta
                2: (0, 65535, 65535),   # Cyan
                3: (65535, 65535, 65535) # White
            }
            return clock_colors.get(self.clock % 4, (0, 65535, 0))

    def get_dot_charges(self) -> List[float]:
        """
        Computes 4 dot charges:
        Dot 0: top-right (+x, -y)
        Dot 1: bottom-right (+x, +y)
        Dot 2: bottom-left (-x, +y)
        Dot 3: top-left (-x, -y)
        """
        e_charge = 1.602176e-19
        neutral = 8.010882e-20

        if self.cell_function == "FIXED":
            if self.polarization > 0.0:  # Logic 1: dots 0 and 2 active
                return [e_charge, 0.0, e_charge, 0.0]
            else:  # Logic 0: dots 1 and 3 active
                return [0.0, e_charge, 0.0, e_charge]
        else:
            return [neutral, neutral, neutral, neutral]

    def to_qca_block(self) -> str:
        """Serializes cell to QCADesigner format."""
        r, g, b = self.color
        bx, by, bcx, bcy = self.bounding_box
        func_name = f"QCAD_CELL_{self.cell_function}"

        lines = [
            "[TYPE:QCADCell]",
            "[TYPE:QCADDesignObject]",
            f"x={self.x:.6f}",
            f"y={self.y:.6f}",
            "bSelected=FALSE",
            f"clr.red={r}",
            f"clr.green={g}",
            f"clr.blue={b}",
            f"bounding_box.xWorld={bx:.6f}",
            f"bounding_box.yWorld={by:.6f}",
            f"bounding_box.cxWorld={bcx:.6f}",
            f"bounding_box.cyWorld={bcy:.6f}",
            "[#TYPE:QCADDesignObject]",
            f"cell_options.cxCell={self.cx:.6f}",
            f"cell_options.cyCell={self.cy:.6f}",
            f"cell_options.dot_diameter={self.dot_diameter:.6f}",
            f"cell_options.clock={self.clock}",
            "cell_options.mode=QCAD_CELL_MODE_NORMAL",
            f"cell_function={func_name}",
            "number_of_dots=4",
        ]

        charges = self.get_dot_charges()
        # Dot offsets from cell center:
        # dot 0: (+4.5, -4.5)
        # dot 1: (+4.5, +4.5)
        # dot 2: (-4.5, +4.5)
        # dot 3: (-4.5, -4.5)
        dot_offsets = [
            (4.5, -4.5),
            (4.5, 4.5),
            (-4.5, 4.5),
            (-4.5, -4.5)
        ]

        for i, (dx, dy) in enumerate(dot_offsets):
            dx_world = self.x + dx
            dy_world = self.y + dy
            lines.extend([
                "[TYPE:CELL_DOT]",
                f"x={dx_world:.6f}",
                f"y={dy_world:.6f}",
                f"diameter={self.dot_diameter:.6f}",
                f"charge={charges[i]:.6e}",
                "spin=0.000000",
                "potential=0.000000",
                "[#TYPE:CELL_DOT]",
            ])

        # Attach label if specified
        if self.label:
            # Place label slightly above cell
            lbl_x = self.x - 2.0
            lbl_y = self.y - 21.0
            lbl_w = max(14.0, len(self.label) * 9.0)
            lines.extend([
                "[TYPE:QCADLabel]",
                "[TYPE:QCADStretchyObject]",
                "[TYPE:QCADDesignObject]",
                f"x={lbl_x:.6f}",
                f"y={lbl_y:.6f}",
                "bSelected=FALSE",
                f"clr.red={r}",
                f"clr.green={g}",
                f"clr.blue={b}",
                f"bounding_box.xWorld={lbl_x - lbl_w/2.0:.6f}",
                f"bounding_box.yWorld={lbl_y - 11.0:.6f}",
                f"bounding_box.cxWorld={lbl_w:.6f}",
                f"bounding_box.cyWorld=22.000000",
                "[#TYPE:QCADDesignObject]",
                "[#TYPE:QCADStretchyObject]",
                f"psz={self.label}",
                "[#TYPE:QCADLabel]",
            ])

        lines.append("[#TYPE:QCADCell]")
        return "\n".join(lines)


class QCACircuit:
    """Represents a complete QCA circuit layout."""

    def __init__(self, name: str):
        self.name = name
        self.cells: List[QCACell] = []

    def add_cell(self, cell: QCACell) -> QCACell:
        self.cells.append(cell)
        return cell

    def metrics(self) -> dict:
        """Computes layout metrics (cell count, bounding dimensions, area, clock zones)."""
        if not self.cells:
            return {
                "cell_count": 0,
                "width_nm": 0.0,
                "height_nm": 0.0,
                "area_um2": 0.0,
                "clock_zones": [],
                "latency_cycles": 0.0,
            }

        min_x = min(c.x - c.cx / 2.0 for c in self.cells)
        max_x = max(c.x + c.cx / 2.0 for c in self.cells)
        min_y = min(c.y - c.cy / 2.0 for c in self.cells)
        max_y = max(c.y + c.cy / 2.0 for c in self.cells)

        width_nm = max_x - min_x
        height_nm = max_y - min_y
        area_um2 = (width_nm * height_nm) / 1e6

        clocks = sorted(list(set(c.clock for c in self.cells)))
        latency = len(clocks) / 4.0

        return {
            "cell_count": len(self.cells),
            "width_nm": width_nm,
            "height_nm": height_nm,
            "area_um2": area_um2,
            "clock_zones": clocks,
            "latency_cycles": latency,
        }

    def generate_qca_file(self) -> str:
        """Produces full .qca file content conforming to QCADesigner 2.0.3 specification."""
        header = [
            "[VERSION]",
            "qcadesigner_version=2.000000",
            "[#VERSION]",
            "[TYPE:DESIGN]",
            "[TYPE:QCADLayer]",
            "type=3",
            "status=1",
            "pszDescription=Drawing Layer",
            "[#TYPE:QCADLayer]",
            "[TYPE:QCADLayer]",
            "type=0",
            "status=1",
            "pszDescription=Substrate",
            "[TYPE:QCADSubstrate]",
            "[TYPE:QCADStretchyObject]",
            "[TYPE:QCADDesignObject]",
            "x=3000.000000",
            "y=1500.000000",
            "bSelected=FALSE",
            "clr.red=65535",
            "clr.green=65535",
            "clr.blue=65535",
            "bounding_box.xWorld=0.000000",
            "bounding_box.yWorld=0.000000",
            "bounding_box.cxWorld=6000.000000",
            "bounding_box.cyWorld=3000.000000",
            "[#TYPE:QCADDesignObject]",
            "[#TYPE:QCADStretchyObject]",
            "grid_spacing=20.000000",
            "[#TYPE:QCADSubstrate]",
            "[#TYPE:QCADLayer]",
            "[TYPE:QCADLayer]",
            "type=1",
            "status=0",
            "pszDescription=Main Cell Layer",
        ]

        cell_blocks = [c.to_qca_block() for c in self.cells]

        footer = [
            "[#TYPE:QCADLayer]",
            "[#TYPE:DESIGN]",
            "",
        ]

        return "\n".join(header + cell_blocks + footer)

    def save(self, filepath: str):
        content = self.generate_qca_file()
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
