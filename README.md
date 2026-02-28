# 🔍 Nmap Port Scanner

A clean, minimal Python wrapper around Nmap for fast and readable port scanning from the command line.

## Requirements

- Python 3.x
- [Nmap](https://nmap.org/download.html) installed on your system
- Python dependencies:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python scanner.py <target> [ports] [scan_type]
```

| Argument | Description | Default |
|---|---|---|
| `target` | IP address or hostname | required |
| `ports` | Port range | `1-1024` |
| `scan_type` | Nmap flag | `-sV` |

## Examples

```bash
# Basic scan
python scanner.py 192.168.1.1

# Custom port range
python scanner.py 192.168.1.1 1-65535

# SYN scan (requires root)
sudo python scanner.py 192.168.1.1 1-1024 -sS

# Aggressive scan
sudo python scanner.py scanme.nmap.org 1-1024 -A
```

## Sample Output

```
[*] Scanning 192.168.1.1 on ports 1-1024...

Host: 192.168.1.1 (router.local)
State: up
  22/tcp    open    ssh       OpenSSH 8.4
  80/tcp    open    http      Apache 2.4.51
  443/tcp   open    https     Apache 2.4.51
```

## Common Scan Types

| Flag | Description |
|---|---|
| `-sV` | Version detection (default) |
| `-sS` | SYN stealth scan (root) |
| `-sU` | UDP scan (root) |
| `-A` | Aggressive (OS, version, scripts) |
| `-sn` | Ping scan only (no ports) |
