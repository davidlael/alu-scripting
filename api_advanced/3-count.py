#!/usr/bin/python3
"""Module that recursively counts keywords in the titles of hot posts."""
import requests


def count_words(subreddit, word_list, instances=None, after=None):
    """Print a sorted count of keywords found in hot post titles.

    Matching is case-insensitive and on whole space-delimited words.
    Sorted by count (descending), then alphabetically (ascending).
    Prints nothing if the subreddit is invalid or nothing matches.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return
    if instances is None:
        instances = {}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:api_advanced:v1.0.0 (by /u/alu_student)"}
    params = {"limit": 100}
    if after is not None:
        params["after"] = after
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False, timeout=10)
        if response.status_code != 200:
            return
        data = response.json().get("data", {})
    except Exception:
        return

    for post in data.get("children", []):
        title = post.get("data", {}).get("title") or ""
        tokens = title.lower().split()
        for word in word_list:
            word = word.lower()
            found = tokens.count(word)
            if found:
                instances[word] = instances.get(word, 0) + found

    next_after = data.get("after")
    if next_after is not None:
        return count_words(subreddit, word_list, instances, next_after)

    for word, total in sorted(instances.items(),
                              key=lambda kv: (-kv[1], kv[0])):
        print("{}: {}".format(word, total))
