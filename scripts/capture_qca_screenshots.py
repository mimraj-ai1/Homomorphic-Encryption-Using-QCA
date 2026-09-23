"""
Automated QCADesigner Canvas Screenshot Capture Utility.
Opens each of the 11 QCA circuit layouts in QCADesigner 2.0.3,
captures the high-resolution canvas rendering using Win32 PrintWindow API,
crops cleanly to the circuit layout (matching the exact canvas perspective
with complete layout visibility and authentic black dotted grid background),
and saves layout images into both the respective design folders
and Documentation/screenshots/.
"""

import os
import re
import subprocess
import time
import ctypes
import win32gui
import win32process
import win32ui
from PIL import Image


def get_qcadesigner_window(pid: int):
    """Finds the main QCADesigner window for the given process ID."""
    found_hwnd = None

    def enum_windows_callback(hwnd, _):
        nonlocal found_hwnd
        _, window_pid = win32process.GetWindowThreadProcessId(hwnd)
        if window_pid == pid and win32gui.IsWindowVisible(hwnd):
            text = win32gui.GetWindowText(hwnd)
            if "QCADesigner" in text and not text.startswith("GDI+"):
                found_hwnd = hwnd

    win32gui.EnumWindows(enum_windows_callback, None)
    return found_hwnd


def capture_window_to_image(hwnd, width: int = 2200, height: int = 1100) -> Image.Image:
    """Resizes window and captures using PrintWindow into a PIL Image."""
    win32gui.MoveWindow(hwnd, 0, 0, width, height, True)
    time.sleep(0.4)

    hwnd_dc = win32gui.GetWindowDC(hwnd)
    mfc_dc = win32ui.CreateDCFromHandle(hwnd_dc)
    save_dc = mfc_dc.CreateCompatibleDC()
    save_bitmap = win32ui.CreateBitmap()
    save_bitmap.CreateCompatibleBitmap(mfc_dc, width, height)
    save_dc.SelectObject(save_bitmap)

    # PW_RENDERFULLCONTENT = 2
    ctypes.windll.user32.PrintWindow(hwnd, save_dc.GetSafeHdc(), 2)

    bmp_info = save_bitmap.GetInfo()
    bmp_str = save_bitmap.GetBitmapBits(True)
    image = Image.frombuffer(
        "RGB",
        (bmp_info["bmWidth"], bmp_info["bmHeight"]),
        bmp_str,
        "raw",
        "BGRX",
        0,
        1,
    )

    win32gui.DeleteObject(save_bitmap.GetHandle())
    save_dc.DeleteDC()
    mfc_dc.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwnd_dc)

    return image


def calculate_crop_box(circuit_name: str, qca_filepath: str):
    """Calculates the optimal crop box for the circuit canvas."""
    with open(qca_filepath, "r") as f:
        text = f.read()

    cell_blocks = text.split("[TYPE:QCADCell]")
    coords = []
    for b in cell_blocks[1:]:
        mx = re.search(r"x=([0-9\.\-]+)", b)
        my = re.search(r"y=([0-9\.\-]+)", b)
        if mx and my:
            coords.append((float(mx.group(1)), float(my.group(1))))

    if not coords:
        return (126, 118, 724, 519)

    xs = [c[0] for c in coords]
    ys = [c[1] for c in coords]
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)

    # Physical (nm) to screen canvas coordinates mapping
    cx1 = 121 + xmin
    cx2 = 121 + xmax
    cy1 = 101 + ymin
    cy2 = 101 + ymax

    # Per-circuit bounding boxes tailored for clean framing
    if circuit_name == "XOR":
        return (126, 118, 724, 519)
    elif circuit_name == "Half_Adder":
        return (126, 118, 724, 519)
    elif circuit_name in ("AND", "OR"):
        return (max(124, int(cx1 - 55)), max(115, int(cy1 - 55)), int(cx2 + 55), int(cy2 + 55))
    elif circuit_name == "NOT":
        return (max(124, int(cx1 - 55)), max(115, int(cy1 - 55)), int(cx2 + 55), int(cy2 + 55))
    elif circuit_name in ("NAND", "NOR"):
        return (max(124, int(cx1 - 55)), max(115, int(cy1 - 55)), int(cx2 + 55), int(cy2 + 55))
    elif circuit_name == "Full_Adder":
        return (126, 118, 560, 460)
    elif circuit_name == "Multiplier_2x2":
        return (126, 118, 560, 450)
    elif circuit_name == "Modular_Adder":
        return (126, 118, 910, 520)
    elif circuit_name == "Ripple_Carry_Adder_4bit":
        return (126, 118, 1560, 460)
    else:
        return (max(124, int(cx1 - 55)), max(115, int(cy1 - 55)), int(cx2 + 65), int(cy2 + 55))


def capture_circuit(circuit_name: str, relative_path: str, qcadesigner_bin: str, doc_dir: str):
    """Opens a circuit in QCADesigner, captures the window, crops to canvas, and saves screenshots."""
    abs_path = os.path.abspath(relative_path)
    file_basename = os.path.basename(relative_path)

    process = subprocess.Popen([qcadesigner_bin, abs_path])
    time.sleep(1.8)

    hwnd = get_qcadesigner_window(process.pid)
    if not hwnd:
        print(f"[ERROR] Window not detected for {circuit_name} ({relative_path})")
        process.terminate()
        process.wait()
        return None

    win32gui.SetWindowText(hwnd, f"{file_basename} - QCADesigner")
    time.sleep(0.2)

    raw_image = capture_window_to_image(hwnd, width=2200, height=1100)
    process.terminate()
    process.wait()
    time.sleep(0.2)

    crop_box = calculate_crop_box(circuit_name, abs_path)
    canvas_image = raw_image.crop(crop_box)

    # Save to circuit folder
    circuit_dir = os.path.dirname(abs_path)
    circuit_png = os.path.join(circuit_dir, f"{circuit_name}_layout.png")
    canvas_image.save(circuit_png)

    # Save to documentation folder
    doc_png = os.path.join(doc_dir, f"{circuit_name}_layout.png")
    canvas_image.save(doc_png)

    print(f"[OK] Captured: {circuit_name:25s} -> size={canvas_image.size} -> {doc_png}")
    return doc_png


def main():
    proj_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    qcadesigner_bin = r"C:\Program Files (x86)\QCADesigner\bin\QCADesigner.exe"
    doc_screenshots_dir = os.path.join(proj_root, "Documentation", "screenshots")
    os.makedirs(doc_screenshots_dir, exist_ok=True)

    circuits = [
        ("AND", os.path.join("QCA_Designs", "AND", "AND.qca")),
        ("OR", os.path.join("QCA_Designs", "OR", "OR.qca")),
        ("NOT", os.path.join("QCA_Designs", "NOT", "NOT.qca")),
        ("NAND", os.path.join("QCA_Designs", "NAND", "NAND.qca")),
        ("NOR", os.path.join("QCA_Designs", "NOR", "NOR.qca")),
        ("XOR", os.path.join("QCA_Designs", "XOR", "XOR.qca")),
        ("Half_Adder", os.path.join("QCA_Designs", "Half_Adder", "Half_Adder.qca")),
        ("Full_Adder", os.path.join("QCA_Designs", "Full_Adder", "Full_Adder.qca")),
        ("Ripple_Carry_Adder_4bit", os.path.join("QCA_Designs", "Ripple_Carry_Adder_4bit", "RCA_4bit.qca")),
        ("Multiplier_2x2", os.path.join("QCA_Designs", "Multiplier_2x2", "Multiplier_2x2.qca")),
        ("Modular_Adder", os.path.join("QCA_Designs", "Modular_Arithmetic", "Modular_Adder.qca")),
    ]

    print("=" * 70)
    print("CAPTURING QCADESIGNER 2.0.3 CANVAS SCREENSHOTS FOR ALL 11 CIRCUITS")
    print("=" * 70)

    captured_files = []
    for name, rel_path in circuits:
        out = capture_circuit(name, rel_path, qcadesigner_bin, doc_screenshots_dir)
        if out:
            captured_files.append(out)

    print("=" * 70)
    print(f"SUCCESS: Captured {len(captured_files)}/{len(circuits)} layout screenshots!")
    print(f"Screenshots saved to: {doc_screenshots_dir}")
    print("=" * 70)


if __name__ == "__main__":
    main()
