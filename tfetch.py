# tfetch.py
import argparse
from scanner import ports, services, hosts, vulns

def main():
    parser = argparse.ArgumentParser(
        description="TFetch 1.0 - CLI Port, Host & Vulnerability Scanner",
        epilog="""
Examples:
  python tfetch.py --host 192.168.1.1
  python tfetch.py --network 192.168.1.0/24
  python tfetch.py --host 192.168.1.1 --network 192.168.1.0/24
""",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('--host', help='Target IP or hostname')
    parser.add_argument('--network', help='Target network (e.g., 192.168.1.0/24)')
    parser.add_argument('--verbose', action='store_true', help='Show detailed output')

    args = parser.parse_args()

    # Auto-select scan modes based on inputs
    if args.host and args.network:
        print("[*] Running all scans on host and network...")
        ports.scan_ports(args.host, verbose=args.verbose)
        services.detect_services(args.host, verbose=args.verbose)
        vulns.find_vulnerabilities(args.host, verbose=args.verbose)
        hosts.discover_hosts(args.network, verbose=args.verbose)
    elif args.host:
        print("[*] Running port, service, and vulnerability scans on host...")
        ports.scan_ports(args.host, verbose=args.verbose)
        services.detect_services(args.host, verbose=args.verbose)
        vulns.find_vulnerabilities(args.host, verbose=args.verbose)
    elif args.network:
        print("[*] Running host discovery on network...")
        hosts.discover_hosts(args.network, verbose=args.verbose)
    else:
        print("[!] Please provide at least --host or --network to start scanning.")

if __name__ == '__main__':
    main()
