from twython import Twython
from twython import TwythonStreamer
from pprint import pprint
from .config import CONSUMER_KEY, CONSUMER_SECRET, AUTH_TOKEN, AUTH_SECRET


# API
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, AUTH_TOKEN, AUTH_SECRET)


# TODO: Save the results to a file if the user wants it.
# Search
def twitter_search(query):
    """ Searches in the Twitter API  based on a query
    :query - String character of what you want to search for
    Can include hashtags(#) if needed"""
    search_query = twitter.search(q=query)
    result_query = [str("Tweet:" + str(i) + "->" + search_query['statuses'][i]['text']).splitlines()
                    for i in range(len(search_query['statuses']))]
    pprint(result_query)


# TODO: Add options to tweet with media
# Update
def twitter_tweet(update):
    """Tweet via command line
    :update - String characters of what you want to Tweet
    Does not support media like pictures/videos"""
    twitter.update_status(status=update)


# Streaming Class Definition
# https://twython.readthedocs.io/en/latest/api.html#streaming-interface
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print(data['text']+"\n")

    def on_error(self, status_code, data):
        print(status_code)
        self.disconnect()
        return False

    def on_timeout(self, data):
        print("Request timed out, try again later")
        self.disconnect()


# TODO: Create this as a subprocess so it doesn't stop the application.
# Start Streaming process
def twitter_stream(query):
    """ Starts a streaming process to live track items related to your query
    :query - String character of what you want to search or track"""
    stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, AUTH_TOKEN, AUTH_SECRET)
    stream.statuses.filter(track=query)