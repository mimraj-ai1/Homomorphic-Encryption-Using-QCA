"""
Publication-Quality Performance Visualization Engine for QCA Circuits.
Reads: Analysis/performance.csv
Generates:
1. Analysis/plots/cell_count_by_circuit.png
2. Analysis/plots/area_by_circuit.png
3. Analysis/plots/latency_by_circuit.png
4. Analysis/plots/qca_vs_cmos_comparison.png
5. Analysis/plots/area_vs_cells_scaling.png
"""

import os
import csv
import matplotlib.pyplot as plt
import numpy as np


def parse_performance_csv(csv_path: str):
    circuits = []
    cell_counts = []
    areas = []
    latencies = []
    categories = []

    basic_gates = {"AND", "OR", "NOT", "NAND", "NOR"}

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["Circuit"].strip()
            count = int(row["Cell_Count"].strip())
            # Parse area (e.g. "0.003364 um^2" -> 0.003364)
            area_str = row["Area"].replace("um^2", "").strip()
            area = float(area_str)
            # Parse latency (e.g. "0.25 cycles" -> 0.25)
            lat_str = row["Latency"].replace("cycles", "").strip()
            lat = float(lat_str)

            circuits.append(name)
            cell_counts.append(count)
            areas.append(area)
            latencies.append(lat)
            categories.append("Basic Gate" if name in basic_gates else "Arithmetic Circuit")

    return circuits, cell_counts, areas, latencies, categories


def plot_cell_counts(circuits, cell_counts, categories, out_dir):
    plt.figure(figsize=(12, 6), dpi=300)
    colors = ["#2b5c8f" if c == "Basic Gate" else "#d95f02" for c in categories]

    bars = plt.bar(circuits, cell_counts, color=colors, edgecolor="black", linewidth=0.8, width=0.65)
    plt.title("QCA Circuit Complexity: Physical Cell Count by Circuit", fontsize=14, fontweight="bold", pad=15)
    plt.xlabel("Circuit Architecture", fontsize=12, labelpad=10)
    plt.ylabel("Total Cell Count (cells)", fontsize=12, labelpad=10)
    plt.xticks(rotation=30, ha="right", fontsize=10)
    plt.grid(axis="y", linestyle="--", alpha=0.6)

    # Value labels
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, height + 5, f"{int(height)}", ha="center", va="bottom", fontsize=9, fontweight="bold")

    # Legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor="#2b5c8f", edgecolor="black", label="Basic Logic Gates (1-4 zones)"),
        Patch(facecolor="#d95f02", edgecolor="black", label="Arithmetic & Modular Circuits"),
    ]
    plt.legend(handles=legend_elements, loc="upper left", frameon=True)
    plt.tight_layout()

    out_path = os.path.join(out_dir, "cell_count_by_circuit.png")
    plt.savefig(out_path)
    plt.close()
    print(f"Generated: {out_path}")


def plot_areas(circuits, areas, categories, out_dir):
    plt.figure(figsize=(12, 6), dpi=300)
    colors = ["#1b9e77" if c == "Basic Gate" else "#7570b3" for c in categories]

    bars = plt.bar(circuits, areas, color=colors, edgecolor="black", linewidth=0.8, width=0.65)
    plt.title("QCA Layout Footprint: Physical Area by Circuit", fontsize=14, fontweight="bold", pad=15)
    plt.xlabel("Circuit Architecture", fontsize=12, labelpad=10)
    plt.ylabel("Physical Area (μm²)", fontsize=12, labelpad=10)
    plt.xticks(rotation=30, ha="right", fontsize=10)
    plt.grid(axis="y", linestyle="--", alpha=0.6)

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, height + 0.005, f"{height:.4f}", ha="center", va="bottom", fontsize=8, fontweight="bold", rotation=0)

    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor="#1b9e77", edgecolor="black", label="Basic Logic Gates"),
        Patch(facecolor="#7570b3", edgecolor="black", label="Arithmetic & Modular Circuits"),
    ]
    plt.legend(handles=legend_elements, loc="upper left", frameon=True)
    plt.tight_layout()

    out_path = os.path.join(out_dir, "area_by_circuit.png")
    plt.savefig(out_path)
    plt.close()
    print(f"Generated: {out_path}")


def plot_latencies(circuits, latencies, categories, out_dir):
    plt.figure(figsize=(12, 6), dpi=300)
    colors = ["#386cb0" if c == "Basic Gate" else "#e7298a" for c in categories]

    bars = plt.bar(circuits, latencies, color=colors, edgecolor="black", linewidth=0.8, width=0.65)
    plt.title("QCA Propagation Latency: Clock Cycles by Circuit", fontsize=14, fontweight="bold", pad=15)
    plt.xlabel("Circuit Architecture", fontsize=12, labelpad=10)
    plt.ylabel("Pipeline Latency (Clock Cycles)", fontsize=12, labelpad=10)
    plt.xticks(rotation=30, ha="right", fontsize=10)
    plt.yticks(np.arange(0, 4.6, 0.5))
    plt.grid(axis="y", linestyle="--", alpha=0.6)

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, height + 0.08, f"{height:.2f}", ha="center", va="bottom", fontsize=9, fontweight="bold")

    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor="#386cb0", edgecolor="black", label="Basic Logic Gates (Single Zone / Quarter Cycle)"),
        Patch(facecolor="#e7298a", edgecolor="black", label="Pipelined Multi-Zone Arithmetic Circuits"),
    ]
    plt.legend(handles=legend_elements, loc="upper left", frameon=True)
    plt.tight_layout()

    out_path = os.path.join(out_dir, "latency_by_circuit.png")
    plt.savefig(out_path)
    plt.close()
    print(f"Generated: {out_path}")


def plot_scaling_correlation(cell_counts, areas, circuits, out_dir):
    plt.figure(figsize=(10, 6), dpi=300)
    x = np.array(cell_counts)
    y = np.array(areas)

    # Linear fit
    slope, intercept = np.polyfit(x, y, 1)
    fit_line = slope * x + intercept
    corr = np.corrcoef(x, y)[0, 1]

    plt.scatter(x, y, color="#b2182b", s=70, edgecolor="black", zorder=5, label="Measured QCA Circuits")
    plt.plot(x, fit_line, color="#2166ac", linestyle="--", linewidth=1.8, label=f"Linear Fit (R² = {corr**2:.4f}, slope = {slope*1000:.3f} nm²/cell)")

    for i, circ in enumerate(circuits):
        offset_y = 0.008 if i % 2 == 0 else -0.015
        plt.annotate(circ, (x[i], y[i]), textcoords="offset points", xytext=(0, offset_y * 1000), ha="center", fontsize=8)

    plt.title("Physical Scaling Analysis: Layout Area vs. Cell Count in QCA Designs", fontsize=13, fontweight="bold", pad=15)
    plt.xlabel("Total Cell Count (N)", fontsize=11, labelpad=8)
    plt.ylabel("Physical Area (μm²)", fontsize=11, labelpad=8)
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend(loc="upper left", frameon=True)
    plt.tight_layout()

    out_path = os.path.join(out_dir, "area_vs_cells_scaling.png")
    plt.savefig(out_path)
    plt.close()
    print(f"Generated: {out_path}")


def plot_qca_vs_cmos(out_dir):
    """
    Theoretical literature benchmark comparison: QCA vs Conventional CMOS nodes.
    Category A: Literature Claims (clearly labeled).
    """
    technologies = ["45 nm CMOS", "28 nm CMOS", "7 nm FinFET", "QCA (18 nm Cells)"]
    # Gate footprint in um^2 (approximate standard full adder cell footprint from ITRS / literature)
    fa_footprints = [8.50, 3.20, 0.45, 0.0693]  # QCA Full Adder measured: 0.069324 um^2
    # Static power per FA (Watts)
    static_power_nW = [45.0, 18.0, 6.2, 0.0001]  # QCA near-zero static dissipation

    fig, ax1 = plt.subplots(figsize=(11, 6), dpi=300)

    color1 = "#1f78b4"
    color2 = "#e31a1c"

    x = np.arange(len(technologies))
    width = 0.35

    rects1 = ax1.bar(x - width/2, fa_footprints, width, label="Full Adder Area (μm²)", color=color1, edgecolor="black")
    ax1.set_ylabel("Full Adder Area (μm²)", color=color1, fontsize=12, fontweight="bold")
    ax1.tick_params(axis="y", labelcolor=color1)
    ax1.set_xticks(x)
    ax1.set_xticklabels(technologies, fontsize=11, fontweight="bold")
    ax1.set_title("Post-CMOS Architecture Comparison: Full Adder Footprint & Static Power\n[Literature & Theoretical Benchmarks — Category A Context]", fontsize=13, fontweight="bold", pad=15)

    ax2 = ax1.twinx()
    rects2 = ax2.bar(x + width/2, static_power_nW, width, label="Static Leakage Power (nW)", color=color2, edgecolor="black", alpha=0.85)
    ax2.set_ylabel("Static Leakage Power (nW) [Log Scale]", color=color2, fontsize=12, fontweight="bold")
    ax2.set_yscale("log")
    ax2.tick_params(axis="y", labelcolor=color2)

    # Value annotations
    for rect in rects1:
        h = rect.get_height()
        ax1.text(rect.get_x() + rect.get_width()/2., h + 0.1, f"{h:.2f} μm²", ha="center", va="bottom", fontsize=8, color=color1, fontweight="bold")

    for rect in rects2:
        h = rect.get_height()
        ax2.text(rect.get_x() + rect.get_width()/2., h * 1.3, f"{h} nW", ha="center", va="bottom", fontsize=8, color=color2, fontweight="bold")

    plt.grid(axis="y", linestyle=":", alpha=0.5)
    fig.tight_layout()

    out_path = os.path.join(out_dir, "qca_vs_cmos_comparison.png")
    plt.savefig(out_path)
    plt.close()
    print(f"Generated: {out_path}")


def main():
    proj_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    csv_path = os.path.join(proj_root, "Analysis", "performance.csv")
    out_dir = os.path.join(proj_root, "Analysis", "plots")
    os.makedirs(out_dir, exist_ok=True)

    circuits, cell_counts, areas, latencies, categories = parse_performance_csv(csv_path)

    plot_cell_counts(circuits, cell_counts, categories, out_dir)
    plot_areas(circuits, areas, categories, out_dir)
    plot_latencies(circuits, latencies, categories, out_dir)
    plot_scaling_correlation(cell_counts, areas, circuits, out_dir)
    plot_qca_vs_cmos(out_dir)

    print("\nAll 5 publication-quality performance plots successfully generated in Analysis/plots/!")


if __name__ == "__main__":
    main()
