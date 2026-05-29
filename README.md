# 🔍 Port Scanner using Python-Nmap

A Python-based port scanning tool that leverages Nmap to perform TCP SYN scans, UDP scans, and comprehensive network reconnaissance on target hosts.

## 📖 Overview

This project provides a simple command-line interface for performing network scans using the Nmap engine through the Python-Nmap library.

The scanner supports multiple scanning techniques and helps identify open ports, active services, and host information for network analysis and security assessments.

## 🚀 Features

* TCP SYN Scan
* UDP Port Scan
* Comprehensive Network Scan
* Service Detection
* Host Discovery
* OS Detection
* Default Script Scanning
* Displays Open Ports
* Displays Host Status
* Displays Supported Protocols

---

## 🛠️ Technologies Used

* Python 3
* Nmap
* Python-Nmap Library

---

## 📂 Project Structure

```text
Port-Scanner/
│
├── port_scanner.py
├── README.md
└── requirements.txt
```

---

## ⚙️ Prerequisites

### Install Nmap

#### Kali Linux / Ubuntu

```bash
sudo apt update
sudo apt install nmap
```

#### Windows

Download and install Nmap from:

https://nmap.org/download.html

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/vigneshVG20/port-scanner.git
cd port-scanner
```

Install Python dependency:

```bash
pip install python-nmap
```

---

## ▶️ Usage

Run the script:

```bash
python3 port_scanner.py
```

Example:

```text
Enter the IP address: scanme.nmap.org

Enter the scanning method
1. SYN Scan
2. UDP Scan
3. Comprehensive Scan

Enter: 1
```

---

## 🔍 Scan Types

### 1. TCP SYN Scan

Uses:

```text
-sS
```

Features:

* Fast scan
* Stealthier than full TCP connect scans
* Identifies open TCP ports

---

### 2. UDP Scan

Uses:

```text
-sU
```

Features:

* Detects open UDP services
* Useful for DNS, SNMP, DHCP, and other UDP-based services

---

### 3. Comprehensive Scan

Uses:

```text
-sS -sV -sC -A -O
```

Features:

* TCP SYN Scan
* Service Version Detection
* Default NSE Scripts
* OS Detection
* Traceroute Information
* Advanced Host Enumeration

---

## 📊 Sample Output

```text
Nmap Version: (7, 95)

Status: up

Protocols:
['tcp']

Open Ports:
[22, 80, 443]
```

---

## 🎯 Skills Demonstrated

* Network Reconnaissance
* Port Scanning
* Service Enumeration
* OS Fingerprinting
* Python Automation
* Nmap Integration
* Cybersecurity Fundamentals
* Network Security Assessment

---

## 🔮 Future Improvements

* Multi-threaded scanning
* Custom port ranges
* Banner grabbing
* Export results to CSV/JSON
* GUI interface
* Vulnerability detection integration
* Scan report generation
* CIDR range scanning

---

## ⚠️ Disclaimer

This tool is intended for educational and authorized security testing purposes only. Always obtain proper permission before scanning any network or system.

---

## 👨‍💻 Author

**Vignesh S**

Aspiring SOC Analyst | Cybersecurity Enthusiast

### Connect With Me

* LinkedIn: https://linkedin.com/in/vignesh-s20
* GitHub: https://github.com/vigneshVG20

---

⭐ If you found this project useful, consider giving it a star!
