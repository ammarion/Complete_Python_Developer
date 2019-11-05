import time
import tweepy

auth = tweepy.OAuthHandler(
    "OkWvZewDdWyLjoc9rhBAiV0mO", "91O2E0VhoHQJ4lgJWRlMLCF7beXFhUaAnZnGJdnc8Kqtwyq4As"
)
auth.set_access_token(
    "896876624490237954-WyV8GIZnfO1jDSVUMIqQJxx7IeSDEM2",
    "xVVUrp82oxP4Xe0PWlfZRrxT9g2bWyhVuSI518tXQTzPN",
)

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


# print(user.screen_name)
# print(api.followers)


for follower in tweepy.Cursor(api.followers).items():
    try:
        follower.follow()
        print(follower.name)
    except StopIteration as e:
        print(e.reason)
        break
search_string = "Architecting Security & Governance Across your AWS Accounts"
number_of_tweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(number_of_tweets):
    try:
        tweet.retweet()
        print(" I liked that tweet")
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
