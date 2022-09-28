#!/usr/bin/env python3

import tweepy
from dotenv import load_dotenv
import os
import sys

load_dotenv()

# Authenticate to Twitter
auth = tweepy.OAuthHandler(os.getenv("APIKEY"), os.getenv("APISECRET"))
auth.set_access_token(os.getenv("TOKEN"), os.getenv("TOKENSECRET"))

# Create API object
api = tweepy.API(auth)

# Create a tweet
media = api.media_upload(sys.argv[1])

tweet = ""
api.update_status(status=tweet, media_ids=[media.media_id])

