# Component 2 — DNS Confirmation Pipeline

> **Module:** COMP08101 — Programming for Cyber Security | UWS  
> **Weighting:** 60% | **Due:** 24th December 2024

---

## Overview

Four chained Python scripts forming a complete DNS reconnaissance pipeline. Starting from a password-protected website, the pipeline brute forces access, scrapes server logs, extracts and validates IP addresses, and confirms which hosts are running DNS servers on port 53.

---

## Pipeline

```
cyforsec.co.uk (protected)
        │
        ▼
[Task 1] brute_force.py     → cracks 4-digit PIN via HTTP enumeration
        │
        ▼
[Task 2] capture_logs.py    → scrapes <p class="logs"> → log.txt
        │
        ▼
[Task 3] extract_ips.py     → extracts valid IPv4 addresses → ips.txt
        │
        ▼
[Task 4] confirm_dns.py     → port 53 scan + reverse DNS + dig → confirmed_dns.txt
```

---

## Scripts

### Task 1 — HTTP Brute Force [`brute_force.py`]

Enumerates all 4-digit PIN codes (0000–9999) against `cyforsec.co.uk` using raw TCP sockets — **no HTTP libraries used** as required by the brief.

For each candidate PIN, constructs a minimal HTTP GET request manually, sends it over a raw socket, reads the full response, and checks for `"Login Succesful"` in the body.

**Key implementation details:**
- Uses `__import__('socket')` for dynamic module loading (no direct import)
- Zero-pads all codes to 4 digits (`%04d`)
- Gracefully handles connection failures and continues enumeration
- Stops immediately on success and outputs the cracked PIN

```python
# Raw HTTP request construction (no libraries)
request = "GET /index.php?uname=admin&password=" + code + " HTTP/1.1\r\n" \
          "Host: cyforsec.co.uk\r\nConnection: close\r\n\r\n"
```

---

### Task 2 — Log Scraper [`capture_logs.py`]

Authenticates to `cyforsec.co.uk` using the cracked credentials and scrapes all content from the `<p class="logs">` element using BeautifulSoup. Writes the raw log data to `log.txt`.

**Libraries:** `requests`, `BeautifulSoup4`

```python
paragraph_logs = parsed_html.find("p", class_="logs")
raw_data = paragraph_logs.get_text()
```

---

### Task 3 — IP Extractor [`extract_ips.py`]

Parses `log.txt` using BeautifulSoup and regex to identify candidate IPv4 addresses, then validates each one using Python's `ipaddress` module. Writes unique, validated IPs to `ips.txt` — one per line.

**Libraries:** `re`, `BeautifulSoup4`, `ipaddress`

```python
ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
ip_obj = ipaddress.IPv4Address(ip)  # Validates against RFC spec
```

**Output:** 20 unique valid IP addresses extracted.

---

### Task 4 — DNS Confirmation [`confirm_dns.py`]

For each IP in `ips.txt`, performs three sequential checks:

1. **Port 53 TCP scan** — confirms DNS port is open via `socket.connect()`
2. **Reverse DNS lookup** — resolves IP to domain name via `socket.gethostbyaddr()`
3. **DNS server verification** — sends a live `dig @IP google.com +short` query via `subprocess`

Only IPs that pass all three checks are written to `confirmed_dns.txt`.

```
DNS Server at 54.36.148.92  : hydrogen092-ext2.a.ahrefs.com
DNS Server at 54.36.148.108 : hydrogen108-ext2.a.ahrefs.com
DNS Server at 54.36.148.1   : hydrogen001-ext2.a.ahrefs.com
DNS Server at 54.36.149.55  : hydrogen311-ext2.a.ahrefs.com
```

**Libraries:** `socket`, `subprocess`, `sys`

---

## Output Files

| File | Description |
|------|-------------|
| `log.txt` | Raw server access log scraped from cyforsec.co.uk |
| `ips.txt` | 20 validated IPv4 addresses extracted from the log |
| `confirmed_dns.txt` | Confirmed DNS servers (IP + domain name) |
| `Coursework2_Task1_html.html` | Raw HTML source of the protected page |

---

## Requirements

```bash
pip install requests beautifulsoup4
```

Scripts must be run in sequence — each script depends on the output of the previous.

---

## Security Notes

- The brute force script targets an intentionally vulnerable academic platform (`cyforsec.co.uk`) designed for this exercise.
- No rate limiting or lockout mechanisms were present on the target — this is by design for the lab.
- DNS confirmation uses standard `dig` queries against public IPs found in server logs.

---

## Disclaimer

> All scripts were developed and executed exclusively against authorised academic targets as part of assessed coursework at UWS. No real production systems were targeted.
