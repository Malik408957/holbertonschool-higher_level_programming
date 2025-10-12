#!/usr/bin/python3
"""
Error Code Script
Sends a request to URL and displays response body.
Prints error code if status code is 400 or higher.
"""
import requests
import sys


if __name__ == "__main__":
    # Get URL from command line argument
    url = sys.argv[1]
    # Send GET request
    response = requests.get(url)
    # Check status code
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
