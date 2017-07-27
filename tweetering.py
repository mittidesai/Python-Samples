""" Streaming twitter API example """

from __future__ import print_function
import sys
import tweepy
from tweepy import OAuthHandler
from ConfigParser import ConfigParser
import json

#Assigning max_tweets to 100 if argument not given
max_tweets = 250

if(len(sys.argv)==3):
    max_tweets = int(sys.argv[2])

class TwitterListener(tweepy.StreamListener):
    """ Twitter stream listener. """
    
    def on_status(self, tweet):
        
        #capture only max_tweets number of tweets and save them to a text file
        
        self.num_tweets += 1
        if(self.num_tweets <= max_tweets):
            s = (tweet.text + '\n').encode('UTF-8')
            f = open('trump.txt', 'a')
            f.write(s)
            #print (s)
            f.close()
            return True
        else:
            return False

    def on_error(self, msg):
        print('Error: %s', msg)

    def on_timeout(self):
        print('timeout : wait for next poll')
        sleep(60)
        
    def __init__(self, api=None):
        self.api = api
        self.num_tweets = 0


def get_config():
    """ Get the configuration """
    conf = ConfigParser()
    conf.read('sample.cfg.txt')
    return conf

def get_stream():

     # keys and tokens from the Twitter Dev Console
        access_token = '334700312-RbFnOySH2X103PiHyS7nbhDcqHIoj6luBSfiw5dx'
        access_token_secret = 'lcevOHD2IAZ3goXkr3DnIZHmLnMfKFAsuGjLDh969fSq5'
        consumer_key = '9fe8nBe9TiLFMYkchZrsPR1Ek'
        consumer_secret = 'mhh1v5Z7jKGlVFy4RM93FovnFe0CCdFp8M3CseWJ1BDtoo8x0H'
 
        # attempt authentication
        
            # create OAuthHandler object
            
       
        config = get_config()
        auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
        auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
        api = tweepy.API(auth)
        listener = TwitterListener()
        stream = tweepy.Stream(auth=auth, listener=listener)
        return stream

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: %s <word>" % (sys.argv[0]))
    else:
        word = sys.argv[1]
        stream = get_stream()
        print("Listening to '%s' and '%s' ..." %('#' + word, word))
        stream.filter(track=['#' + word, word])
