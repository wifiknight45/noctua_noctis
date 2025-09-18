import pandas as pd

def parse_scan(scan_tuple):
    """
    Converts Nmap scan results into a pandas DataFrame.
    """
    hosts, nm = scan_tuple
    rows = []
    for host in hosts:
        for proto in nm[host].all_protocols():
            ports = nm[host][proto].keys()
            for port in ports:
                service = nm[host][proto][port]
                rows.append({
                    "host": host,
                    "protocol": proto,
                    "port": port,
                    "state": service["state"],
                    "name": service["name"],
                    "product": service.get("product", ""),
                    "version": service.get("version", "")
                })
    return pd.DataFrame(rows)

def export_results(df, base_filename):
    """
    Exports DataFrame to CSV and JSON.
    """
    csv_file = f"{base_filename}.csv"
    json_file = f"{base_filename}.json"
    df.to_csv(csv_file, index=False)
    df.to_json(json_file, orient="records", indent=2)
    print(f"[+] Results saved to {csv_file} and {json_file}")
