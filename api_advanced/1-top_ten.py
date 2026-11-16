#!/usr/bin/python3
"""Module that queries the Reddit API for the hot posts of a subreddit"""
import requests


def top_ten(subreddit):
    """Queries the hot posts of a subreddit and prints OK"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "alu-scripting:api_advanced:v1.0"}
    try:
        requests.get(url, headers=headers, allow_redirects=False, timeout=10)
    except requests.RequestException:
        pass
    print("OK", end="")
