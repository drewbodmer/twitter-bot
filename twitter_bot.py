import  Twitter_Interface as ti

print('Hello Twitter')

q = input("What do you want to search for? \n")

tweets = ti.get_tweets(10, q)

for tweet in tweets:
    print(tweet)
    print("------------------------")