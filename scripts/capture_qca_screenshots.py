"""
Automated QCADesigner Window Screenshot Capture Utility.
Opens each of the 11 QCA circuit layouts in QCADesigner 2.0.3,
captures the full GUI window rendering using Win32 PrintWindow API,
and saves high-resolution layout images into both the respective design folders
and Documentation/screenshots/.
"""

import os
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


def capture_window_to_image(hwnd) -> Image.Image:
    """Captures a window HWND using PrintWindow into a PIL Image."""
    rect = win32gui.GetWindowRect(hwnd)
    width = rect[2] - rect[0]
    height = rect[3] - rect[1]

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


def capture_circuit(circuit_name: str, relative_path: str, qcadesigner_bin: str, doc_dir: str):
    """Opens a circuit in QCADesigner, captures the window, and saves screenshots."""
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

    # Set window title explicitly to standard formatting
    win32gui.SetWindowText(hwnd, f"{file_basename} - QCADesigner")
    time.sleep(0.2)

    image = capture_window_to_image(hwnd)

    # Save to circuit folder
    circuit_dir = os.path.dirname(abs_path)
    circuit_png = os.path.join(circuit_dir, f"{circuit_name}_layout.png")
    image.save(circuit_png)

    # Save to documentation folder
    doc_png = os.path.join(doc_dir, f"{circuit_name}_layout.png")
    image.save(doc_png)

    print(f"[OK] Captured: {circuit_name:25s} -> {doc_png} ({image.size[0]}x{image.size[1]})")

    process.terminate()
    process.wait()
    time.sleep(0.3)
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
    print("CAPTURING QCADESIGNER 2.0.3 GUI SCREENSHOTS FOR ALL 11 CIRCUITS")
    print("=" * 70)

    captured_files = []
    for name, rel_path in circuits:
        out = capture_circuit(name, rel_path, qcadesigner_bin, doc_screenshots_dir)
        if out:
            captured_files.append(out)

    print("=" * 70)
    print(f"SUCCESS: Captured {len(captured_files)}/{len(circuits)} QCADesigner layout screenshots!")
    print(f"Screenshots saved to: {doc_screenshots_dir}")
    print("=" * 70)


if __name__ == "__main__":
    main()
