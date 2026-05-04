# Component 1 — Python Security Portfolio

> **Module:** COMP08101 — Programming for Cyber Security | UWS  
> **Weighting:** 40% | **Due:** 17th December 2024

---

## Overview

A portfolio of seven Python exercises covering fundamental security programming concepts — from classical cryptography to live API integration and algorithmic implementation. All exercises are contained in `main.py`.

---

## Exercises

### 1. Fibonacci Sequence
Generates the first 20 terms of the Fibonacci series using list-based iteration.

**Concepts:** Python lists, iterative algorithms, index-based computation.

---

### 2. Caesar Cipher
Implements the classical Caesar shift cipher with a reusable `encrypt(plaintext, k)` function supporting both upper and lowercase characters.

**Concepts:** String manipulation, modular arithmetic, alphabet indexing, character preservation.

```python
# Example
encrypt("Hello World", 3)  # → "Khoor Zruog"
```

---

### 3. Password Hashing with SHA-256
Collects username/password pairs via a `while` loop and stores SHA-256 hashes using Python's `hashlib` library.

**Concepts:** Cryptographic hashing, `hashlib.sha256`, UTF-8 encoding, list storage.

```python
from hashlib import sha256
hashed = sha256(password.encode('utf-8')).hexdigest()
```

---

### 4. Password Verification
Verifies a user's login attempt by hashing the input password and comparing it against a stored hash — without ever storing or comparing plaintext passwords.

**Concepts:** Hash comparison, function decomposition, credential validation logic.

---

### 5. HaveIBeenPwned API — Breach Check
Reads username/password pairs from a file, computes SHA-1 hashes, and queries the HaveIBeenPwned API using the **k-anonymity model** — only the first 5 characters of the hash are sent, protecting the full password from the API.

**Concepts:** Live API integration, k-anonymity, SHA-1, `requests`, file parsing.

```python
# Only the first 5 chars of the hash are sent to the API
response = requests.get(f"https://api.pwnedpasswords.com/range/{hash[:5]}")
```

---

### 6. Command Line Arguments — Arithmetic Calculator
Uses `argparse` to build a CLI tool accepting two integers and an arithmetic operator, returning the computed result. Includes interactive fallback if arguments are omitted.

**Concepts:** `argparse`, CLI design, operator handling, division-by-zero protection.

```bash
python arguments.py 4 3 /   # → 1.3333333333333333
```

---

### 7. Binary Search
Implements a `binarySearch(sorted_list, target)` function returning the index of the target element or `-1` if not found.

**Concepts:** Divide-and-conquer, O(log n) search, index tracking, sorted list requirement.

---

## File

| File | Description |
|------|-------------|
| `main.py` | All seven exercises — each clearly sectioned with comments |

---

## Disclaimer

> All work completed individually as part of assessed coursework at UWS. No AI tools were used in the production of submitted code.
