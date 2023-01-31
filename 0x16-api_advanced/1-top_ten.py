#!/usr/bin/python3
"""Queries the reddit api and prints the titles of
first 10 hot posts listed for given subreddit
"""
import requests


def top_ten(subreddit):
    headers = {
        'User-Agent': 'MyBot/1.0'
    }
    response = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10 \
            ".format(subreddit), headers=headers)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            print(title)
    else:
        print(None)
