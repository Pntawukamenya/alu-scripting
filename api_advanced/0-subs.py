import requests

def number_of_subscribers(subreddit):
    """
    Query the Reddit API and return the number of subscribers for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)\
          AppleWebKit/537.36(KHTML, like Gecko) \
         Chrome/90.0.4430.93 Safari/537.36'
    }
    params = {
        'limit': 1,
    }
    url = f'https://www.reddit.com/r/{subreddit}/about/subscribers'
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
