#!/usr/bin/python3
"""fetch and process"""

import requests
import csv


def fetch_and_print_posts():
    """fetches all post from JSONPlaceholder and print titles"""

    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])  # only print titles


def fetch_and_save_posts():
    """fetches all post from JSONPlaceholder"""

    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        post = response.json()
        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'], extrasaction="ignore")
            writer.writeheader()
            writer.writerows(post)
