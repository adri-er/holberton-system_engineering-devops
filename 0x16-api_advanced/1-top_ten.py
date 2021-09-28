#!/usr/bin/python3
""" This module requests Reddit API """
import json
import requests


def top_ten(subreddit):
    """ Return the hot posts of list. """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    header = {"Content-Type": "application/json",
              "User-Agent": "Mozilla/5.0"}
    request = requests.get(
        url,
        headers=header,
        allow_redirects=False)
    if request.status_code >= 300:
        print('None')
    data = json.loads(request.content.decode("utf-8"))["data"]["children"]
    for title in data:
        print(title['data']['title'])
