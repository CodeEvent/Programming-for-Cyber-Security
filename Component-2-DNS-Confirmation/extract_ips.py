#!/usr/bin/env python3

import re
from bs4 import BeautifulSoup
import ipaddress

def extract_ips():
    """
    Extracts valid IPv4 addresses from log.txt and writes them to ips.txt.
    Utilizes BeautifulSoup to parse the log file and regex for initial matching,
    followed by ipaddress module for validation.
    """
    try:
        # Read the content of log.txt
        with open("log.txt", "r", encoding="utf-8") as f:
            raw_logs = f.read()
    except FileNotFoundError:
        print("Error: 'log.txt' not found in the current directory.")
        return

    # Parse the log content with BeautifulSoup
    soup = BeautifulSoup(raw_logs, "html.parser")
    text_data = soup.get_text()

    # Regex pattern to identify potential IPv4 addresses
    ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"

    # Find all matches in the text
    potential_ips = re.findall(ip_pattern, text_data)

    # Validate each IP address
    valid_ips = []
    for ip in potential_ips:
        try:
            # Validate using ipaddress module
            ip_obj = ipaddress.IPv4Address(ip)
            valid_ips.append(ip)
        except ipaddress.AddressValueError:
            # Skip invalid IP addresses
            continue

    if not valid_ips:
        print("No valid IP addresses found in 'log.txt'.")
        return

    # Remove duplicates while preserving order
    unique_valid_ips = sorted(set(valid_ips), key=valid_ips.index)

    # Write the valid IPs to ips.txt
    with open("ips.txt", "w", encoding="utf-8") as out_file:
        for ip in unique_valid_ips:
            out_file.write(ip + "\n")

    print(f"Successfully extracted {len(unique_valid_ips)} valid IP address(es) to 'ips.txt'.")

# Execute the extraction function
extract_ips()
