#!/usr/bin/python3
"""Module that recursively collects the titles of all hot posts."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of titles of all hot posts of a subreddit.

    Uses recursion to follow Reddit pagination.
    Returns None if the subreddit is invalid.
    """
    if after is None:
        hot_list = []
    if subreddit is None or not isinstance(subreddit, str):
        return None
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:api_advanced:v1.0.0 (by /u/alu_student)"}
    params = {"limit": 100}
    if after is not None:
        params["after"] = after
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False, timeout=10)
        if response.status_code != 200:
            return None if after is None else hot_list
        data = response.json().get("data", {})
    except Exception:
        return None if after is None else hot_list

    for post in data.get("children", []):
        hot_list.append(post.get("data", {}).get("title"))

    next_after = data.get("after")
    if next_after is not None:
        return recurse(subreddit, hot_list, next_after)
    return hot_list
