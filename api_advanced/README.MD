# api_advanced

Reddit API project: querying subreddits with the `requests` module.

| File | Description |
|------|-------------|
| `0-subs.py` | `number_of_subscribers(subreddit)` returns subscriber count (0 if invalid) |
| `1-top_ten.py` | `top_ten(subreddit)` prints the titles of the first 10 hot posts (`None` if invalid) |
| `2-recurse.py` | `recurse(subreddit, hot_list=[])` recursively returns all hot post titles (`None` if invalid) |
| `3-count.py` | `count_words(subreddit, word_list)` recursively prints sorted keyword counts |

All requests set a custom User-Agent and do not follow redirects, so invalid
subreddits are detected correctly.
