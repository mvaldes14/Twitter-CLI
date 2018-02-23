import pytest
from twython.exceptions import TwythonError
from twittercli.helpers import twitter_search, twitter_stream, twitter_tweet


def test_twitter_search(mocker):
    twitter_search = mocker.patch('twittercli.helpers.twitter_search')
    twitter_search('Example')
    twitter_search.called_with_arguments('Example')
    twitter_search(123)
    twitter_search.called_with_arguments(123)
    

def test_twitter_search_empty_parameter():
    with pytest.raises(TwythonError):
        twitter_search(' ')

def test_twitter_stream(mocker):
   twitter_stream = mocker.patch('twittercli.helpers.twitter_stream')
   twitter_stream('Example')
   twitter_stream.called_with_arguments('Example')


def test_twitter_stream_empty_parameter(mocker):
   twitter_stream = mocker.patch('twittercli.helpers.twitter_stream')
   twitter_stream.return_value = 406
   assert twitter_stream(' ') == 406
