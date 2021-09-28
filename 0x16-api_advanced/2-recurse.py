#!/usr/bin/python3
""" This module requests Reddit API """
import json
import requests


def recurse(subreddit, hot_list=[], counter=0, after=None):
    """ Return the hot posts list. """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    header = {"Content-Type": "application/json",
              "User-Agent": "Mozilla/5.0"}
    request = requests.get(
        url,
        headers=header,
        allow_redirects=False,
        params={"count": counter, "after": after})
    if request.status_code >= 400:
        return None

    data = json.loads(request.content.decode("utf-8"))["data"]["children"]
    data_gen = json.loads(request.content.decode("utf-8"))
    new_list = hot_list + [post['data']['title'] for post in data]

    if not data_gen.get('data').get('after'):
        return new_list

    return recurse(
        subreddit,
        new_list,
        data_gen.get('data').get('count'),
        data_gen.get('data').get('after'))
