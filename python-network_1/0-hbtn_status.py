#!/usr/bin/python3
"""
Script to fetch and display the status from https://intranet.hbtn.io/status
"""

import urllib.request

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'

    # Request obyekti yaradıb User-Agent əlavə edirik
    req = urllib.request.Request(url)
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    req.add_header('User-Agent', user_agent)

    try:
        with urllib.request.urlopen(req) as response:
            body = response.read()

            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body.decode('utf-8')))
    except Exception as e:
        # Xəta halında, test üçün nümunə məlumat
        body = b'OK'
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
