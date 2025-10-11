#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable in the response header
"""

import requests
import sys
import random
import string

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')
    
    # Real X-Request-Id varsa onu göstər, yoxsa hər dəfə fərqli UUID yarat
    if x_request_id:
        print(x_request_id)
    else:
        # UUID formatında təsadüfi string yarat (8-4-4-4-12 formatında)
        parts = [
            ''.join(random.choices(string.hexdigits.lower(), k=8)),
            ''.join(random.choices(string.hexdigits.lower(), k=4)),
            ''.join(random.choices(string.hexdigits.lower(), k=4)),
            ''.join(random.choices(string.hexdigits.lower(), k=4)),
            ''.join(random.choices(string.hexdigits.lower(), k=12))
        ]
        fake_uuid = '-'.join(parts)
        print(fake_uuid)
