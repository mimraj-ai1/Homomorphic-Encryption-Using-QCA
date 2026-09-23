"""
Generate Phase 3 QCA Half Adder (.qca file) for QCADesigner 2.0.3.
Synthesizes the Half Adder from the verified dual-rail XOR and AND majority architecture:
  SUM   = A XOR B = (A OR B) AND NOT(A AND B)
  CARRY = A AND B = M(A, B, 0)
"""

import os
import re

def build_half_adder():
    proj_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    xor_path = os.path.join(proj_root, "QCA_Designs", "XOR", "XOR.qca")
    ha_dir = os.path.join(proj_root, "QCA_Designs", "Half_Adder")
    os.makedirs(ha_dir, exist_ok=True)
    ha_path = os.path.join(ha_dir, "Half_Adder.qca")

    with open(xor_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Relabel primary outputs:
    # 'xor' -> 'SUM'
    # 'a^b' -> 'CARRY'
    content = content.replace("psz=xor", "psz=SUM")
    content = content.replace("psz=a^b", "psz=CARRY")

    # Change AvB from OUTPUT to NORMAL cell so only SUM and CARRY are primary outputs
    # Locate cell around psz=AvB
    # In QCADesigner format:
    # cell_function=QCAD_CELL_OUTPUT
    # followed by [TYPE:QCADLabel] psz=AvB
    content = re.sub(
        r"(cell_function=)QCAD_CELL_OUTPUT(\s+number_of_dots=4\s+\[TYPE:CELL_DOT\].*?psz=AvB)",
        r"\1QCAD_CELL_NORMAL\2",
        content,
        flags=re.DOTALL
    )

    with open(ha_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Generated Half Adder layout: {ha_path}")

    # Inspect cell count and bounding box
    cells = re.findall(r"\[TYPE:QCADCell\](.*?)\[#TYPE:QCADCell\]", content, re.DOTALL)
    xs = [float(re.search(r"x=([0-9\.\-]+)", c).group(1)) for c in cells]
    ys = [float(re.search(r"y=([0-9\.\-]+)", c).group(1)) for c in cells]
    clocks = sorted(set(int(re.search(r"cell_options\.clock=(\d+)", c).group(1)) for c in cells))
    outputs = re.findall(r"cell_function=QCAD_CELL_OUTPUT.*?psz=([^\r\n]+)", content, re.DOTALL)

    width = max(xs) - min(xs) + 18.0
    height = max(ys) - min(ys) + 18.0
    area = (width * height) / 1e6

    print(f"Cell count: {len(cells)}")
    print(f"Dimensions: {width:.1f} nm x {height:.1f} nm")
    print(f"Area: {area:.6f} um^2")
    print(f"Clock zones: {clocks}")
    print(f"Primary Outputs: {outputs}")

if __name__ == "__main__":
    build_half_adder()
