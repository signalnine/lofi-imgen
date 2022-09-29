#!/usr/bin/env python3

import tweepy
from dotenv import load_dotenv
import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--filename", type=str)
parser.add_argument("--prompt", type=str)
args = parser.parse_args()
load_dotenv()

# Authenticate to Twitter
auth = tweepy.OAuthHandler(os.getenv("APIKEY"), os.getenv("APISECRET"))
auth.set_access_token(os.getenv("TOKEN"), os.getenv("TOKENSECRET"))

# Create API object
api = tweepy.API(auth)

# Create a tweet
media = api.media_upload(args.filename)
alt_text = api.create_media_metadata(media.media_id, args.prompt)
tweet = ""
api.update_status(status=tweet, media_ids=[media.media_id])

