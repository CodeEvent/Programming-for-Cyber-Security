#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import re
import os

def captured_logs():
    # The URL includes the known username & passcode
    site_url = "http://cyforsec.co.uk/index.php?uname=admin&password=0000"

    # Make a GET request to the site
    request_result = requests.get(site_url)

    # If there's an error, stop
    if request_result.status_code != 200:
        print("Error: HTTP status", request_result.status_code)
        return

    # Parse the HTML
    parsed_html = BeautifulSoup(request_result.text, "html.parser")

    # Locate the <p class="logs"> element
    paragraph_logs = parsed_html.find("p", class_="logs")

    # If not found, stop
    if not paragraph_logs:
        print("No <p class='logs'> section found. (Maybe wrong passcode or not logged in?)")
        return

    # Extract the text content
    raw_data = paragraph_logs.get_text()

    # (Optional) regex usage here if needed
    # raw_data = re.sub(r"\s+", " ", raw_data).strip()

    # Write the logs to log.txt (in current working directory)
    with open("log.txt", "w", encoding="utf-8") as file_out:
        file_out.write(raw_data)

    # Show where the file was saved
    print("Logs successfully written to:", os.path.abspath("log.txt"))

# The function is called immediately when this script runs
captured_logs()
