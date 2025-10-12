#!/usr/bin/python3
"""
Search API Script
Sends POST request with letter parameter and processes JSON response.
"""
import requests
import sys


if __name__ == "__main__":
    # Get letter from command line argument or set to empty string
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""
    # Prepare URL and data
    url = "http://0.0.0.0:5000/search_user"
    data = {'q': letter}
    # Send POST request
    response = requests.post(url, data=data)
    # Process JSON response
    try:
        json_response = response.json()
        if json_response:
            # Display id and name if JSON is not empty
            print("[{}] {}".format(json_response.get('id'), json_response.get('name')))
        else:
            # Display if JSON is empty
            print("No result")
    except ValueError:
        # Display if JSON is invalid
        print("Not a valid JSON")
