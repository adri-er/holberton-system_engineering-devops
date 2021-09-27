#!/usr/bin/python3
""" This module requests Reddit API """
import json
import requests


def number_of_subscribers(subreddit):
    """ Return the number of subscribers. """
    client_id = "q0TBAXHRud-XgBAnJGZMHA"
    sec_code = "wrP3myYvIZ-lh_ezcpeZVW4NO0p17w"
    username = "Spirited_Equal8759"
    password = "temppass"

    auth = requests.auth.HTTPBasicAuth(client_id, sec_code)
    data = {'grant_type': 'password',
            'username': username,
            'password': password}

    headers = {'User-Agent': 'MyBot/0.0.1'}

    # send our request for an OAuth token
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)

    # convert response to JSON and pull access_token value
    TOKEN = res.json()['access_token']

    # add authorization to our headers dictionary
    headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

    url = "https://oauth.reddit.com/r/{}/about.json".format(subreddit)
    try:
        request = json.loads(
            requests.get(url, headers=headers).content.decode("utf-8"))
        return request["data"]["subscribers"]
    except(KeyError):
        return 0
