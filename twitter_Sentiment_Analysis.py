__author__ = 'jT'

import tweepy
from tweepy import streaming
import codecs
from string import punctuation
from tweepy import OAuthHandler
import sys

#All thte required modules have been imported.

class twitterSentimentAnalysis():

#Generated Customer key,secret and access token and secrete from twitter and using it for authenticating.
    custKey = 'QuCejnnTedHq1IWgwUY9w7fKA'
    custSecret= '4YZkZSwQW1RxPAct8b0Rq8zqwAwPM5wBNRVCO5hYWbRM52soc9'
    accesToken = '825593114480037888-MTZgNadQMv4NGxhyOnndSv9HkuI6gfU'
    accessSecret = 'rHyZIWV8MYw0HCPMFzVFhlQ6YF6DK1yhOz9lJtKolWbWz'

    auth = OAuthHandler(custKey,custSecret)
    auth.set_access_token(accesToken,accessSecret)

    api = tweepy.API(auth)

#Reading possitive and negative words and storing it in variable that we are going use to compare with twitter outcome to do sentiment analysis.
    posWords = codecs.open("positive_words.txt").read().split()

    negWords = codecs.open("negative_words.txt").read().split()


#Creating a function that takes celebrity name as input and used to pull out 200 tweets related to the celebrity
    def tweetSearch(self, celebrityName):
        outFile = codecs.open("TweetOutcome.txt", 'w', 'utf-8')
        outCome = self.api.search(q=celebrityName, lang="en", locale="en", count=200)

        for i in outCome:
            outFile.write(i.text + '\n')

        outFile.close()


#This function takes tweets as input and comapre it with the positive and negative words to return whether the tweet was positive or negative
    def pos_neg_count(self, tweet):
        pos = 0
        neg = 0
#Removing all the punctuations from the tweets that i have pulled out form the twitter
        for p in list(punctuation):
            tweet.replace(p, ' ')

        tweet = tweet.lower()
#Splits the tweet into words so as to match the each word with that od positive and negative words
        words = tweet.split(' ')

#for each words I'm comparing it with positive and negative words list. and if its is present in any od these list then increase in pos or neg count with 1
        for word in words:

            if word in self.posWords:
                w1 = word
                #print w1
                pos = pos + 1
            elif word in self.negWords:
                w2 = word
                #print w2
                neg = neg + 1

        return pos, neg




#Funtion is used for the sentiment analysis after collecting all the positive and negative counts for each celebrity
    def sentimentAnalysis(self):
        possitive_counter = 0
        negative_counter = 0

        tweets = codecs.open("TweetOutcome.txt", 'r', 'utf-8').read()
        tweet_list = []
        tweetList = tweets.split('\n')
#Going through each tweets and feeding these to pos_neg_count function to get the pos and neg count
        for tweet in tweetList:
            if(len(tweet)):
                tweet = tweet.encode("utf-8")
                p, n = self.pos_neg_count(tweet)
                possitive_counter += p
                negative_counter += n

        #print possitive_counter
        #print negative_counter
#Returning the final result in terms of Positive, Negative and Neutral depending upon the respective word counts.
        if possitive_counter > negative_counter:
            return "Possitive"
        elif possitive_counter < negative_counter:
            return "Negative"
        else:
            return "Neutral"


