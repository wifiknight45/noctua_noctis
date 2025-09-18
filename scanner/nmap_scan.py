import nmap

def run_scan(target):
    """
    Runs an Nmap scan on the given target.
    Returns a tuple: (list_of_hosts, nmap.PortScanner object)
    """
    nm = nmap.PortScanner()
    print(f"[+] Scanning target: {target}")
    nm.scan(hosts=target, arguments="-sS -sV -T4")  # SYN scan, service version, faster timing
    return nm.all_hosts(), nm
