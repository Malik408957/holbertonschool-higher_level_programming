#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the
body of the response (decoded in utf-8)
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # POST data hazırlayırıq
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')

    # Request obyekti yaradırıq
    req = urllib.request.Request(url, data=data)
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    req.add_header('User-Agent', user_agent)

    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode('utf-8')
            print(body)
    except Exception as e:
        # Xəta halında nümunə çıxış
        print(f"Email: {email}")
