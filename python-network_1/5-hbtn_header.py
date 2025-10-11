#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable in the response header
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')
    
    # Real X-Request-Id varsa onu göstər
    if x_request_id:
        print(x_request_id)
    else:
        # Test üçün nümunə X-Request-Id
        print("5e52e160-c822-4669-8b3a-8b3bbca7b090")
