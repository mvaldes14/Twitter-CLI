import pytest
from twython.exceptions import TwythonError
from twittercli.helpers import twitter_search, twitter_stream, twitter_tweet


def test_twitter_search():
    assert twitter_search('Example')
    assert twitter_search(123)


def test_twitter_search_empty_parameter():
    with pytest.raises(TwythonError):
        twitter_search(' ')

# def test_twitter_stream():
#     assert twitter_stream('Example')


def test_twitter_stream_empty_parameter():
    assert twitter_stream(' ') is False
