#!/usr/bin/env python3
# TWITTER CLI 2.0

from pprint import pprint
from twython import Twython
from twython import TwythonStreamer
import argparse
import yaml
import sys

# Meta
__version__ = "2.0"
__author__ = "Miguel Valdes"


# Configuration from YAML
with open('twitterConfig.yaml') as f:
    config = yaml.load(f)

# Keys
CONSUMER_KEY = config['Twitter_API']['CONSUMER_KEY']
CONSUMER_SECRET = config['Twitter_API']['CONSUMER_SECRET']
AUTH_TOKEN = config['Twitter_API']['AUTH_TOKEN']
AUTH_SECRET = config['Twitter_API']['AUTH_SECRET']

# API
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, AUTH_TOKEN, AUTH_SECRET)


# Search
def twitter_search(query):
    """ Searches in the Twitter API  based on a query
    :query - String character of what you want to search for
    Can include hashtags(#) if needed"""
    search_query = twitter.search(q=query)
    result_query = [str("Tweet:" + str(i) + "->" + search_query['statuses'][i]['text']).splitlines()
                    for i in range(len(search_query['statuses']))]
    pprint(result_query)

# TODO: Save the results to a file if the user wants it.


# Update
def twitter_tweet(update):
    """Tweet via command line
    :update - String characters of what you want to Tweet
    Does not support media like pictures/videos"""
    twitter.update_status(status=update)
    return "Tweet Sent"

# TODO: Add options to tweet with media

# Streaming Class Definition
# https://twython.readthedocs.io/en/latest/api.html#streaming-interface


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print(data['text'].encode('utf-8'))

    def on_error(self, status_code, data):
        print(status_code)
        self.disconnect()

    def on_timeout(self, data):
        print("Request timed out, try again later")
        self.disconnect()

# TODO: Put this on a separate file


# Start Streaming process
def twitter_stream(query):
    """ Starts a streaming process to live track items related to your query
    :query - String character of what you want to search or track"""
    stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, AUTH_TOKEN, AUTH_SECRET)
    stream.statuses.filter(track=query)

# TODO: Create this as a subprocess so it doesn't stop the application.


# CLI Interface
parser = argparse.ArgumentParser(
    description="Twitter CLI Client: " + __version__, add_help=True)

parser.add_argument('-u', dest="update", help="Tweet something")
parser.add_argument('-s', dest="search", help="Search for tweets")
parser.add_argument('-t', dest="stream", help="Start the streaming process")

# TODO Add options to save to file

# Main


def main():
    args = parser.parse_args()
    if len(sys.argv) == 1:
        print("No arguments provided")

    if args.update:
        print("Tweeting...")
        twitter_tweet(args.update)
        print("Done")

    if args.search:
        print("Searching for: " + args.search)
        twitter_search(args.search)

    if args.stream:
        print("Starting Streaming process for: " + args.stream)
        twitter_stream(args.stream)


# Run
if __name__ == "__main__":
    main()
