import tweepy
import json
import time
import requests
import os
from os import environ


client = tweepy.Client(environ['bearer_token'],
                       environ['consumer_key'],
                       environ['consumer_secret'],
                       environ['access_token'],
                       environ['access_token_secret'])


r = requests.get('https: // cdn.jsdelivr.net/gh/fawazahmed0/hadith-api@1/editions/fra-malik.min.json)

jsons = r.json()


for r in jsons['hadiths']:
    if (len(r['text']) < 281 and (len(r['text']) > 10)):

        client.create_tweet(text=r['text'])

        time.sleep(43200)
    else:
        continue
