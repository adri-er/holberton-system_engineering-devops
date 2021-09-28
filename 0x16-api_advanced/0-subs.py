#!/usr/bin/python3
""" This module requests Reddit API for suscribers """
import json
import requests


def number_of_subscribers(subreddit):
    """ Return the number of subscribers. """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {"Content-Type": "application/json",
              "User-Agent": "Mozilla/5.0"}
    request = requests.get(
        url,
        headers=header,
        allow_redirects=False)
    if request.status_code >= 300:
        return 0
    return json.loads(request.content.decode("utf-8"))["data"]["subscribers"]
