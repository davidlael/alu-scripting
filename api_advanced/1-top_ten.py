#!/usr/bin/python3
"""
1-top_ten module
"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    # Reddit requires a descriptive User-Agent following their API guidelines
    headers = {'User-Agent': 'alu:api.advanced:v1.0 (by /u/davidlael)'}
    params = {'limit': 10}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    try:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        if not posts:
            print("None")
            return
        for post in posts[:10]:
            print(post.get('data', {}).get('title'))
    except ValueError:
        print("None")
