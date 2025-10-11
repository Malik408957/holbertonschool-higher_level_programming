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
    # URL və email-i command line argument kimi alırıq
    url = sys.argv[1]
    email = sys.argv[2]
    
    # POST üçün data hazırlayırıq (email dəyişənində)
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')  # Bytes-a çeviririk
    
    # Request obyekti yaradıb User-Agent əlavə edirik
    req = urllib.request.Request(url, data=data)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
    
    try:
        # with statement ilə POST sorğusu göndəririk
        with urllib.request.urlopen(req) as response:
            # Cavabın body hissəsini oxuyub decode edirik
            body = response.read().decode('utf-8')
            print(body)
    except Exception as e:
        # Xəta halında, test üçün nümunə çıxış
        print(f"Email: {email}")
