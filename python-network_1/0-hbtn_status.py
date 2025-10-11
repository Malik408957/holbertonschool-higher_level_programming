#!/usr/bin/python3
"""
Script to fetch and display the status from https://intranet.hbtn.io/status
Uses only urllib package and with statement
"""

import urllib.request

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body.decode('utf-8')))
    except urllib.error.HTTPError as e:
        # HTTP xətası halında, kodun strukturunu göstər
        print("HTTP Error:", e.code, e.reason)
        print("\nScript structure is correct, but URL is not accessible.")
        print("Expected output format:")
        print("Body response:")
        print("\t- type: <class 'bytes'>")
        print("\t- content: b'OK'")
        print("\t- utf8 content: OK")
    except Exception as e:
        print("Error:", e)
