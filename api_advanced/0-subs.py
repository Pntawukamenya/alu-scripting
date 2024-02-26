#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    """
    Query the Reddit API and return the number of subscribers for a given subreddit.
    If the subreddit is invalid, return 0.

    Parameters:
    subreddit (str): The name of the subreddit to query.

    Returns:
    int: The number of subscribers for the given subreddit, or 0 if the subreddit is invalid.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
        'User-Agent': 'My User Agent 1.0',
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
