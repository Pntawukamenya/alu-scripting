#!/usr/bin/python3

import snoowrap

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given, the function returns 0.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the given subreddit, or 0 if the subreddit is invalid.
    """
    # Set up the Reddit API wrapper with the provided credentials
    r = snoowrap({
        'userAgent': 'My custom user agent',
        'clientId': '<client_id>',
        'clientSecret': '<client_secret>'
    })

    # Get the user's subscriptions
    subscriptions = r.getSubscriptions()

    # Check if the provided subreddit is in the user's subscriptions
    for subscription in subscriptions:
        if subscription.display_name == subreddit:
            return subscription.subscribers

    # If the subreddit is not found, return 0
    return 0
