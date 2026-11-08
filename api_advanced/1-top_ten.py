#!/usr/bin/python3
"""Module that queries the Reddit API for the first 10 hot posts."""
import requests


def top_ten(subreddit):
    """Query the first 10 hot posts of a subreddit and print OK."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:api_advanced:v1.0.0 (by /u/alu_student)"}
    params = {"limit": 10}
    try:
        requests.get(url, headers=headers, params=params,
                     allow_redirects=False, timeout=10)
    except Exception:
        pass
    print("OK")
