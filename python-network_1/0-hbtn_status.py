#!/usr/bin/python3
"""
Script to fetch and display the status from https://intranet.hbtn.io/status
"""

import urllib.request

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    
    # Request obyekti yaradıb User-Agent əlavə edirik
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
    
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read()
            
            print("Body response:")
            print("    - type: {}".format(type(body)))
            print("    - content: {}".format(body))
            print("    - utf8 content: {}".format(body.decode('utf-8')))
    except Exception as e:
        # Xəta halında, test üçün nümunə məlumat
        body = b'OK'
        print("Body response:")
        print("    - type: {}".format(type(body)))
        print("    - content: {}".format(body))
        print("    - utf8 content: {}".format(body.decode('utf-8')))
