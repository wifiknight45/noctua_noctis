#!/usr/bin/env python3
"""
noctua_noctis.py
----------------
"Noctua Noctis" = "Night Owl" (Latin)
A mythic network sweep and service fingerprinting tool.

Features:
- Host discovery & service enumeration via Nmap
- Optional Scapy packet probes for verification
- Structured output with Pandas
- CSV/JSON export
- Optional Matplotlib visualization
- Modular design for CLI & Jupyter/Colab

Usage:
    python noctua_noctis.py 192.168.1.0/24 --visualize --scapy-probe
"""

import argparse
from scanner import nmap_scan, data_parser, visualizer, scapy_probe

def main():
    parser = argparse.ArgumentParser(description="Noctua Noctis - Network sweep & fingerprinting")
    parser.add_argument("target", help="Target IP/CIDR range (e.g., 192.168.1.0/24)")
    parser.add_argument("--output", default="scan_results", help="Base filename for output")
    parser.add_argument("--visualize", action="store_true", help="Generate open port distribution graph")
    parser.add_argument("--scapy-probe", action="store_true", help="Run Scapy custom packet probes after Nmap scan")
    args = parser.parse_args()

    # Step 1: Run Nmap scan
    hosts, nm = nmap_scan.run_scan(args.target)

    # Step 2: Parse into DataFrame
    df = data_parser.parse_scan((hosts, nm))

    # Step 3: Optional Scapy probe
    if args.scapy_probe:
        print("[+] Running Scapy probes on discovered hosts/ports...")
        # Extract unique ports per host
        host_ports = {}
        for _, row in df.iterrows():
            host_ports.setdefault(row["host"], set()).add(row["port"])
        # Run probes
        scapy_results = scapy_probe.probe_hosts(host_ports.keys(), {p for ports in host_ports.values() for p in ports})
        # Add verification column
        df["scapy_verified"] = df.apply(lambda r: r["port"] in scapy_results.get(r["host"], []), axis=1)

    # Step 4: Export results
    data_parser.export_results(df, args.output)

    # Step 5: Optional visualization
    if args.visualize:
        visualizer.plot_open_ports(df, f"{args.output}_ports.png")

if __name__ == "__main__":
    main()
