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
    
    # X-Request-Id varsa onu göstər, yoxsa heç nə göstərmə (None)
    print(x_request_id)
