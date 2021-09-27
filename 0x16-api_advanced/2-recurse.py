#!/usr/bin/python3
""" This module requests Reddit API """
import json
import requests

def recurse(subreddit):
    """ Return the hot posts of list using recursion. """
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

    url = "https://oauth.reddit.com/r/{}/hot".format(subreddit)
    try:
        request = json.loads(
            requests.get(
                url,
                headers=headers).content.decode("utf-8"))
        data = request['data']['children']
        return hot(data, 0, len(data))
    except:
        print(None)

def hot(complete_list, counter, length, hot_list=[]):
    """ Recurse list """
    if (counter < length):
        hot_list.append(complete_list[counter]['data']['title'])
        counter += 1
        return hot(complete_list, counter, length, hot_list)
    else:
        return hot_list
