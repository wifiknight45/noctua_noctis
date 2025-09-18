import matplotlib.pyplot as plt

def plot_open_ports(df, output_file):
    """
    Plots distribution of open ports.
    """
    port_counts = df["port"].value_counts()
    plt.figure(figsize=(10, 6))
    port_counts.plot(kind="bar")
    plt.title("Open Port Distribution - Noctua Noctis")
    plt.xlabel("Port")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(output_file)
    print(f"[+] Port distribution graph saved to {output_file}")
