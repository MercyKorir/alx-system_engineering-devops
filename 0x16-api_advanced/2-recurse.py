#!/usr/bin/python3
"""queries redditapi and returns list containing title
of all hot articles for given subreddit
"""
import requests


def recurse(subreddit, after=None, hot_list=[]):
    headers = {
        'User-Agent': 'MyBot/1.0'
    }
    params = {
        'limit': 100
    }
    if after:
        params['after'] = after
    response = requests.get("https://www.reddit.com/r/{}/hot.json".format(
        subreddit), headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            hot_list.append(title)
        after = data['data']['after']
        if after:
            return recurse(subreddit, after, hot_list)
        else:
            return hot_list
    else:
        return None
