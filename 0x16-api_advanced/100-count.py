#!/usr/bin/python3
"""recursive function that queries the redditapi,
parse the title of all hot articles and prints a sorted count
of given keywords
"""
import requests


def count_words(subreddit, word_list, after=None, count={}):
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}
    response = requests.get("https://www.reddit.com/r/{}/hot.json".format(
        subreddit), headers=headers, params=params)

    if response.status_code != 200:
        return None

    data = response.json()
    children = data['data']['children']

    if not children:
        return None

    for child in children:
        title = child['data']['title'].lower()
        words = title.split()
        for word in words:
            word = word.strip('.!_')
            if word in word_list:
                if word not in count:
                    count[word] = 0
                count[word] += 1
    after = data['data']['after']
    if after:
        count_words(subreddit, word_list, after, count)

    return count


def top_ten_words(subreddit, word_list):
    count = count_words(subreddit, word_list)
    if not count:
        return

    sorted_count = sorted(count.items(), key=lambda x: (-x[1], x[0]))
    for word, frequency in sorted_count[:10]:
        print(word, frequency)
