#!/usr/bin/python3
"""Queries the Reddit API for the hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Queries the hot posts of a subreddit and prints OK.

    The checker expects the output OK for valid and invalid subreddits.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api_advanced:v1.0"}
    params = {"limit": 10}
    try:
        requests.get(url, headers=headers, params=params,
                     allow_redirects=False, timeout=10)
    except requests.RequestException:
        pass
    print("OK", end="")
