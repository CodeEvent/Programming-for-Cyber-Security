#!/usr/bin/env python3

import socket
import subprocess
import sys

def test_port53(address, port_target=53, wait_secs=2):
    """
    Checks if the specified 'address' is accepting connections on port 53.
    Performs a basic TCP connect test.
    """
    try:
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.settimeout(wait_secs)
        connection.connect((address, port_target))
        connection.close()
        print(f"Port 53 is open on {address}.")
        return True
    except:
        print(f"Port 53 is closed or unreachable on {address}.")
        return False

def find_domain(address):
    """
    Attempts to perform a reverse DNS lookup on 'address'.
    Returns the domain name if successful, otherwise None.
    """
    try:
        host_data = socket.gethostbyaddr(address)
        print(f"Reverse DNS successful for {address}: {host_data[0]}")
        return host_data[0]
    except:
        print(f"Reverse DNS failed for {address}.")
        return None

def verify_dns(address):
    """
    Sends a DNS query to the specified 'address' on port 53 using 'dig'.
    Returns True if the server responds with valid data, otherwise False.
    """
    try:
        # Construct the dig command
        cmd = ["dig", "@" + address, "google.com", "+short"]
        # Execute the command
        result_proc = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
        # Debugging output
        if result_proc.returncode == 0:
            print(f"'dig' command executed successfully for {address}.")
        else:
            print(f"'dig' command failed for {address} with return code {result_proc.returncode}.")
        print(f"dig output for {address}:\n{result_proc.stdout}")
        # Check if the command was successful and returned output
        if result_proc.returncode == 0 and result_proc.stdout.strip():
            print(f"DNS query successful for {address}.")
            return True
        return False
    except Exception as e:
        print(f"Exception during DNS verification for {address}: {e}")
        return False

def orchestrate_dns_checks():
    """
    Orchestrates the DNS confirmation process:
    - Reads IPs from ips.txt
    - Checks port 53
    - Performs reverse DNS
    - Verifies DNS server functionality
    - Writes confirmed DNS servers to confirmed_dns.txt
    """
    # Step 1: Read IP addresses from ips.txt
    try:
        with open("ips.txt", "r", encoding="utf-8") as ip_file:
            ip_addresses = [line.strip() for line in ip_file if line.strip()]
    except FileNotFoundError:
        print("Error: 'ips.txt' not found in the current directory.")
        sys.exit(1)

    # Step 2: Initialize list to hold confirmed DNS servers
    confirmed_dns_servers = []

    # Step 3: Iterate over each IP address
    for ip in ip_addresses:
        print(f"\nProcessing IP: {ip}")
        # Check if port 53 is open
        if test_port53(ip, 53):
            # Perform reverse DNS lookup
            domain = find_domain(ip)
            if domain:
                # Verify DNS server functionality
                if verify_dns(ip):
                    # Format the result string
                    result_entry = f"DNS Server at {ip} : {domain}"
                    confirmed_dns_servers.append(result_entry)
        else:
            print(f"Skipping {ip} as port 53 is not open.")

    # Step 4: Write confirmed DNS servers to confirmed_dns.txt
    if confirmed_dns_servers:
        with open("confirmed_dns.txt", "w", encoding="utf-8") as output_file:
            for entry in confirmed_dns_servers:
                output_file.write(entry + "\n")
        print(f"\nDNS verification complete. {len(confirmed_dns_servers)} server(s) confirmed and saved to 'confirmed_dns.txt'.")
    else:
        print("\nNo DNS servers confirmed. 'confirmed_dns.txt' remains empty.")

# Execute the DNS confirmation process
orchestrate_dns_checks()
