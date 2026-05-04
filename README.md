# Programming for Cyber Security — COMP08101

> **University of the West of Scotland** | BEng (Hons) Cyber Security | 2024/25 Term 1  
> **Module:** COMP08101 — Programming for Cyber Security  
> **Assessment:** Component 1 (40%) · Component 2 (60%)

---

## Overview

This repository contains all assessed coursework from COMP08101. The module covers practical Python development for cyber security — from cryptographic primitives and API integration to automated network reconnaissance and DNS enumeration.

---

## Components

### [Component 1 — Python Security Portfolio](./Component-1-Portfolio/)
A portfolio of seven Python exercises demonstrating core security programming concepts: classical encryption, password hashing with SHA-256, live API integration with HaveIBeenPwned, and algorithm implementation.

### [Component 2 — DNS Confirmation Pipeline](./Component-2-DNS-Confirmation/)
Four chained Python scripts forming an end-to-end DNS reconnaissance pipeline: HTTP brute force to breach a protected site, web scraping to extract server logs, regex-based IP extraction, and automated DNS server confirmation via port scanning, reverse DNS, and live `dig` queries.

---

## Skills Demonstrated

| Category | Technologies |
|----------|-------------|
| **Cryptography** | SHA-256 (hashlib), SHA-1, Caesar Cipher, password hashing and verification |
| **API Integration** | HaveIBeenPwned API (k-anonymity model), requests library |
| **Web Scraping** | BeautifulSoup4, HTML parsing, CSS selector targeting |
| **Network Programming** | Raw TCP sockets, HTTP request construction, port scanning |
| **Reconnaissance** | HTTP brute force, IP extraction, reverse DNS, DNS server verification |
| **Data Processing** | Regex (`re`), `ipaddress` module, file I/O, argparse |
| **Automation** | Chained script pipeline, subprocess (`dig`), systematic enumeration |

---

> All scripts were developed and tested in an authorised academic environment. The brute force and reconnaissance techniques were applied exclusively to intentionally vulnerable academic targets (cyforsec.co.uk).
