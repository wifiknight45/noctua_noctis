#!/usr/bin/env python3
"""
aka net_sweep_and_fingerprint.py
----------------------------
Performs a network sweep and service fingerprinting using Nmap's Python bindings.
Exports results to CSV/JSON and optionally visualizes open port distribution.

Concepts Covered:
- Host discovery & service enumeration
- Parsing structured results with pandas
- Exporting to multiple formats
- Modular code design for CLI and Jupyter/Colab use
"""

import argparse
from scanner import nmap_scan, data_parser, visualizer

def main():
    parser = argparse.ArgumentParser(description="Network sweep & fingerprinting tool")
    parser.add_argument("target", help="Target IP/CIDR range (e.g., 192.168.1.0/24)")
    parser.add_argument("--output", default="scan_results", help="Base filename for output")
    parser.add_argument("--visualize", action="store_true", help="Generate open port distribution graph")
    args = parser.parse_args()

    # Step 1: Run Nmap scan
    scan_data = nmap_scan.run_scan(args.target)

    # Step 2: Parse into DataFrame
    df = data_parser.parse_scan(scan_data)

    # Step 3: Export results
    data_parser.export_results(df, args.output)

    # Step 4: Optional visualization
    if args.visualize:
        visualizer.plot_open_ports(df, f"{args.output}_ports.png")

if __name__ == "__main__":
    main()
