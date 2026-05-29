import nmap

def main():
    scanner = nmap.PortScanner()

    ip_addr = input("Enter the target IP address or hostname: ").strip()

    print("\nSelect Scan Type")
    print("1. TCP SYN Scan")
    print("2. UDP Scan")
    print("3. Comprehensive Scan")

    scanning = input("\nEnter your choice (1/2/3): ").strip()

    try:
        print("\nNmap Version:", scanner.nmap_version())

        if scanning == '1':
            print("\n[*] Running TCP SYN Scan...")
            scanner.scan(ip_addr, '1-1024', arguments='-sS')

        elif scanning == '2':
            print("\n[*] Running UDP Scan...")
            scanner.scan(ip_addr, '1-1024', arguments='-sU')

        elif scanning == '3':
            print("\n[*] Running Comprehensive Scan...")
            scanner.scan(ip_addr, '1-1024', arguments='-sS -sV -sC -A -O')

        else:
            print("[-] Invalid Choice")
            return

        print("\nScan Information:")
        print(scanner.scaninfo())

        if ip_addr not in scanner.all_hosts():
            print("[-] Host not found or is down.")
            return

        print("\nHost Status:", scanner[ip_addr].state())

        protocols = scanner[ip_addr].all_protocols()
        print("Protocols:", protocols)

        for protocol in protocols:
            print(f"\n--- {protocol.upper()} Ports ---")

            ports = sorted(scanner[ip_addr][protocol].keys())

            if not ports:
                print("No open ports found.")
                continue

            for port in ports:
                state = scanner[ip_addr][protocol][port]['state']
                print(f"Port {port}: {state}")

    except nmap.PortScannerError:
        print("[-] Nmap is not installed or not in PATH.")

    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    main()

