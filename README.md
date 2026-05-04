# Python Cyber Security Tooling

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Topics](https://img.shields.io/badge/Topics-Brute%20Force%20%7C%20DNS%20Recon%20%7C%20Cryptography%20%7C%20Web%20Scraping-green)
![UWS](https://img.shields.io/badge/UWS-BEng%20Cyber%20Security-darkblue)

Two Python courseworks demonstrating practical security tooling — built from scratch, fully functional, and chained into an automated reconnaissance pipeline.

---

## What This Repository Shows

**You can write working security tools in Python.**

Not theoretical exercises — actual scripts that hit real servers, crack credentials, scrape protected content, extract network artefacts, and confirm live DNS infrastructure. Every tool here was written to solve a concrete problem and produces real output.

---

## Component 2 — DNS Reconnaissance Pipeline

> The most technically interesting part of this repo.

A four-stage automated pipeline that starts from a password-protected website and ends with a list of confirmed DNS servers — with zero manual steps between stages.

```
Protected website → crack PIN → scrape logs → extract IPs → confirm DNS servers
```

### Stage 1 — HTTP Brute Force [`brute_force.py`]

Cracks a 4-digit PIN on a live protected site by enumerating all 10,000 possibilities using **raw TCP sockets** — no HTTP libraries, HTTP requests constructed manually byte by byte.

```python
# No requests, no urllib — raw socket only
s = sock_mod.socket(sock_mod.AF_INET, sock_mod.SOCK_STREAM)
s.connect((host, port))
s.sendall(b"GET /index.php?uname=admin&password=0342 HTTP/1.1\r\nHost: cyforsec.co.uk\r\nConnection: close\r\n\r\n")
```

**Output:**
```
Correct passcode: 0342
----- Revealed Page -----
<html><h1>Login Succesful</h1><p class="logs">...
```

---

### Stage 2 — Log Scraper [`capture_logs.py`]

Authenticates with cracked credentials and extracts server access logs from the protected page using BeautifulSoup CSS selector targeting. Writes raw log data to `log.txt`.

```python
paragraph_logs = parsed_html.find("p", class_="logs")
raw_data = paragraph_logs.get_text()
# → writes 200+ lines of Apache access log to log.txt
```

---

### Stage 3 — IP Extractor [`extract_ips.py`]

Parses `log.txt` with regex to identify candidate IPv4 addresses, then validates each one against the RFC spec using Python's `ipaddress` module. Deduplicates and writes clean results.

```python
ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
ip_obj = ipaddress.IPv4Address(ip)  # rejects malformed candidates
```

**Output — 20 unique validated IPs extracted:**
```
13.66.139.0
157.48.153.185
54.36.148.92
162.158.203.24
66.249.64.41
... (20 total)
```

---

### Stage 4 — DNS Confirmation [`confirm_dns.py`]

For each IP, runs three sequential checks — port 53 TCP scan, reverse DNS lookup, and a live `dig` query to confirm the server is actually resolving DNS. Only IPs passing all three are written to output.

```python
socket.connect((ip, 53))           # Check 1: port open?
socket.gethostbyaddr(ip)           # Check 2: reverse DNS?
subprocess.run(["dig", "@"+ip, "google.com", "+short"])  # Check 3: live DNS?
```

**Final output — confirmed DNS servers:**
```
DNS Server at 54.36.148.92  : hydrogen092-ext2.a.ahrefs.com
DNS Server at 54.36.148.108 : hydrogen108-ext2.a.ahrefs.com
DNS Server at 54.36.148.1   : hydrogen001-ext2.a.ahrefs.com
DNS Server at 54.36.149.55  : hydrogen311-ext2.a.ahrefs.com
```

---

## Component 1 — Security Programming Portfolio

Seven Python implementations covering core security programming concepts.

| Exercise | What it demonstrates |
|----------|----------------------|
| **Caesar Cipher** | Classical encryption, modular arithmetic, character-level manipulation |
| **SHA-256 Password Hashing** | hashlib, UTF-8 encoding, never storing plaintext |
| **Password Verification** | Hash comparison, credential validation without plaintext exposure |
| **HaveIBeenPwned API** | Live API integration, k-anonymity model |
| **Command Line Tool** | argparse, CLI design, operator handling, error protection |
| **Binary Search** | O(log n) divide-and-conquer algorithm |
| **Fibonacci Sequence** | Iterative algorithm, list-based computation |

The HIBP integration uses the k-anonymity model correctly — only the first 5 characters of the hash are sent to the API, meaning the full password never leaves your system:

```python
response = requests.get(f"https://api.pwnedpasswords.com/range/{hash[:5]}")
```

---

## Technical Skills Demonstrated

| Skill | Implementation |
|-------|---------------|
| **Raw socket programming** | HTTP requests built manually, no libraries |
| **Web scraping** | BeautifulSoup4, CSS selectors, HTML parsing |
| **Regex & data extraction** | re module, IP pattern matching, validation pipeline |
| **Network reconnaissance** | Port scanning, reverse DNS, live DNS verification |
| **Cryptography** | SHA-256, SHA-1, Caesar cipher, k-anonymity |
| **API integration** | HaveIBeenPwned, requests, response parsing |
| **CLI tooling** | argparse, interactive fallback, operator handling |
| **Process automation** | subprocess, chained scripts, file I/O pipeline |

---

## Running the Pipeline

```bash
pip install requests beautifulsoup4

python brute_force.py     # → finds PIN, prints cracked page
python capture_logs.py    # → writes log.txt
python extract_ips.py     # → writes ips.txt
python confirm_dns.py     # → writes confirmed_dns.txt
```

---

## Academic Context

> **Module:** COMP08101 — Programming for Cyber Security
> **University:** University of the West of Scotland | BEng (Hons) Cyber Security
> All scripts were developed and tested against authorised academic targets only. The brute force and reconnaissance techniques were applied exclusively to cyforsec.co.uk, an intentionally vulnerable platform provided for this assessment.
