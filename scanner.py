import nmap
import sys

def scan(target, ports="1-1024", scan_type="-sV"):
    nm = nmap.PortScanner()
    print(f"\n[*] Scanning {target} on ports {ports}...\n")
    nm.scan(hosts=target, ports=ports, arguments=scan_type)

    for host in nm.all_hosts():
        print(f"Host: {host} ({nm[host].hostname()})")
        print(f"State: {nm[host].state()}")
        for proto in nm[host].all_protocols():
            for port, info in sorted(nm[host][proto].items()):
                print(f"  {port}/{proto}\t{info['state']}\t{info['name']}\t{info.get('version','')}")
    print()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scanner.py <target> [ports] [scan_type]")
        print("Example: python scanner.py 192.168.1.1 1-1024 -sV")
        sys.exit(1)

    target = sys.argv[1]
    ports  = sys.argv[2] if len(sys.argv) > 2 else "1-1024"
    stype  = sys.argv[3] if len(sys.argv) > 3 else "-sV"
    scan(target, ports, stype)
```

**`requirements.txt`**
```
python-nmap
