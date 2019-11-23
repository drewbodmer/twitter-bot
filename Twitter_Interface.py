import tweepy
import secrets

auth = tweepy.OAuthHandler(secrets.CONSUMER_KEY, secrets.CONSUMER_SECRET)
auth.set_access_token(secrets.ACCESS_KEY, secrets.ACCESS_SECRET)

api = tweepy.API(auth)


# return an array of tweets of specified length
def get_tweets(number, inquiry):
    tweets = []
    for tweet_info in tweepy.Cursor(api.search, q=inquiry, lang='en', tweet_mode='extended').items(number):
        if 'retweeted_status' in dir(tweet_info):
            tweet = tweet_info.retweeted_status.full_text
        else:
            tweet = tweet_info.full_text
        print(tweet)

        tweets.append(tweet)
    return tweets