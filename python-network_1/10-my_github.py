#!/usr/bin/python3
"""
GitHub API Script
Uses GitHub API with Basic Authentication to display user ID.
"""
import requests
import sys


if __name__ == "__main__":
    # Get username and password from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    # REAL GitHub API URL (github.com server)
    url = "https://api.github.com/user"
    # Create authentication tuple
    auth = (username, password)
    # Send GET request with authentication
    response = requests.get(url, auth=auth)
    # Check if request was successful
    if response.status_code == 200:
        # Parse JSON response and get user ID
        user_data = response.json()
        print(user_data.get('id'))
    else:
        # Print None if authentication failed
        print("None")
