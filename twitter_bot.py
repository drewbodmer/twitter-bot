import tweepy
import csv

print('Hello Twitter')

import secrets

auth = tweepy.OAuthHandler(secrets.CONSUMER_KEY, secrets.CONSUMER_SECRET)
auth.set_access_token(secrets.ACCESS_KEY, secrets.ACCESS_SECRET)

api = tweepy.API(auth)


def train(doc, tweet, lor):
    with open(lor, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        words = {}
        print("reading rows:")
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            words[row["word"]] = row["frequency"]
            line_count += 1

        print(f'Processed {line_count} lines.')

    with open(lor, mode='w') as tweets:
        fieldnames = ['word', 'frequency']
        writer = csv.DictWriter(tweets, fieldnames=fieldnames)

        writer.writeheader()
        for word in doc:
            word.strip('.').strip(',').strip().lower()
            freq = tweet.lower().count(word)

            if word in words:
                oldfreq = words[word]
                words[word] = int(oldfreq) + freq
            else:
                words[word] = freq

        for word in words.keys():
            writer.writerow({'word': word, 'frequency': words[word]})

def test(tweet):
    with open('left_tweets.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        leftwords = {}
        print("reading rows for test:")
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            leftwords[row["word"]] = row["frequency"]
            line_count += 1

    with open('right_tweets.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        rightwords = {}
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            rightwords[row["word"]] = row["frequency"]
            line_count += 1

    left_freq = 0
    right_freq = 0

    for word in tweet:
        if word in leftwords:
            left_freq += int(leftwords[word])
        if word in rightwords:
            right_freq += int(rightwords[word])
    if left_freq>right_freq:
        print("left")
    else:
        print("right")


for tweet_info in tweepy.Cursor(api.search, q='trump', lang='en', tweet_mode='extended').items(1):
    if 'retweeted_status' in dir(tweet_info):
        tweet=tweet_info.retweeted_status.full_text
    else:
        tweet=tweet_info.full_text
    doc = tweet.split(' ')
    print(tweet)
    # if input("left or right: ") == 'l':
    #     lor = "left_tweets.csv"
    # else:
    #     lor = 'right_tweets.csv'

    # train(doc, tweet, lor)
    test(tweet)

