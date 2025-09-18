![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey?logo=linux&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Security](https://img.shields.io/badge/Security-Nmap%20%7C%20Scapy%20%7C%20Pandas-critical?logo=hackaday)
![Status](https://img.shields.io/badge/Status-Active-success)
![Colab](https://img.shields.io/badge/Run%20in-Google%20Colab-orange?logo=googlecolab&logoColor=white)
![Jupyter](https://img.shields.io/badge/Notebook-Jupyter-orange?logo=jupyter&logoColor=white)
![GitHub last commit](https://img.shields.io/github/last-commit/wifiknight45/noctua_noctis)
![GitHub issues](https://img.shields.io/github/issues/wifiknight45/noctua_noctis)
![GitHub stars](https://img.shields.io/github/stars/wifiknight45/noctua_noctis?style=social)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Network Security](https://img.shields.io/badge/category-network%20security-red.svg)]()

# 🦉 Noctua Noctis
*"Night Owl" - A Mythic Network Reconnaissance Tool*


## 🌙 What is Noctua Noctis?

Like its namesake nocturnal hunter, **Noctua Noctis** prowls through network darkness with silent precision. This sophisticated reconnaissance tool combines the raw power of Nmap with the surgical precision of Scapy packet crafting, delivering comprehensive network discovery and service fingerprinting in a beautifully structured format.

Born from the need for both depth and clarity in network analysis, Noctua Noctis transforms complex scan data into actionable intelligence through pandas-powered analytics and optional matplotlib visualizations.

## ✨ Key Features

### 🎯 **Dual-Layer Reconnaissance**
- **Primary Sweep**: Lightning-fast Nmap-based host discovery and port enumeration
- **Verification Layer**: Optional Scapy packet probes for enhanced accuracy and stealth

### 📊 **Intelligent Data Processing**
- Structured output via pandas DataFrames for advanced analysis
- Cross-verification between Nmap and Scapy results
- Export capabilities: CSV and JSON formats

### 📈 **Visual Intelligence**
- Optional matplotlib-powered port distribution graphs
- Clear visual representation of network topology
- Publication-ready charts for reporting

### 🔧 **Modular Architecture**
- CLI-ready for automated workflows
- Jupyter/Google Colab compatible for interactive analysis
- Extensible design for custom probe development

## 🚀 Quick Start

### Installation
```bash
git clone https://github.com/wifiknight45/noctua_noctis.git
cd noctua_noctis
pip install -r requirements.txt
```

### Basic Usage
```bash
# Simple network sweep
python noctua_noctis.py 192.168.1.0/24

# Full reconnaissance with visualization
python noctua_noctis.py 192.168.1.0/24 --visualize --scapy-probe

# Custom output naming
python noctua_noctis.py 10.0.0.0/8 --output corporate_sweep --visualize
```

## 📋 Command Line Options

| Option | Description | Example |
|--------|-------------|---------|
| `target` | IP address or CIDR range to scan | `192.168.1.0/24` |
| `--output` | Base filename for results (default: scan_results) | `--output my_scan` |
| `--visualize` | Generate port distribution graphs | `--visualize` |
| `--scapy-probe` | Enable Scapy verification probes | `--scapy-probe` |

## 🏗️ Architecture Overview

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Nmap Scanner  │───▶│  Data Parser     │───▶│  Visualizer     │
│   (Primary)     │    │  (pandas)        │    │  (matplotlib)   │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│  Scapy Prober   │    │   Export Engine  │    │   Results       │
│  (Verification) │    │   (CSV/JSON)     │    │   (Files/Viz)   │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## 📁 Module Breakdown

### `nmap_scan.py`
The primary reconnaissance engine leveraging python-nmap for comprehensive host discovery and service enumeration.

### `scapy_probe.py`
Advanced packet crafting module for stealth verification and custom protocol analysis.

### `data_parser.py`
Pandas-powered data transformation layer that structures raw scan results into analyzable formats with export capabilities.

### `visualizer.py`
Matplotlib-based visualization engine for creating insightful network topology charts and port distribution graphs.

## 📊 Output Examples

### CSV Export Sample
```csv
host,port,protocol,state,service,version,scapy_verified
192.168.1.1,22,tcp,open,ssh,OpenSSH 8.2,True
192.168.1.1,80,tcp,open,http,Apache 2.4.41,True
192.168.1.5,443,tcp,open,https,nginx 1.18.0,False
```

### Visualization Output
- Port distribution histograms
- Service type breakdowns
- Host availability heatmaps
- Verification status overlays

## 🛡️ Ethical Usage

**Noctua Noctis** is designed for legitimate security testing, network administration, and educational purposes. Users are responsible for:

a) Obtaining proper authorization before scanning networks
b) Complying with local laws and regulations
c) Respecting network policies and terms of service
d) Using results responsibly and ethically

## 🔧 Dependencies

```python
python-nmap>=0.6.1
scapy>=2.4.5
pandas>=1.3.0
matplotlib>=3.3.0
numpy>=1.19.0
```

##  License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Nmap Project** - For the foundational scanning capabilities
- **Scapy Community** - For the powerful packet manipulation library
- **Security Researchers** - Who inspire better defensive tools

---

*"Revolution is the struggle between the past and the future. And the future has just begun."
         -julian assange

---

**⚠️ Disclaimer**: This tool is for authorized security testing and educational purposes only. Unauthorized network scanning may be illegal in your jurisdiction and is generally frowned upon by society so be discerning in it's usage contexts etc.
